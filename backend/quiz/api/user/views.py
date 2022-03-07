'''
defines the views for the user app
'''
# Create your views here.
from django.http import JsonResponse
from django.contrib.auth import get_user_model,login,logout
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from api.quizes.models import Quiz, AssignDeassignQuiz
from api.user.models import CustomUser
from api.user.serializers import UserSerializer

UserModel = get_user_model()


@csrf_exempt
@api_view(['POST', ])
def signup(request):
    '''
    user register
    '''
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only'})

    serializer = UserSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        for index in range(1, len(Quiz.objects.all()) + 1):

            AssignDeassignQuiz.objects.create(
                topic=Quiz.objects.get(id=index),
                user=CustomUser.objects.get(id=user.id),

            )
        data['response'] = 'Successfully registered'
        data['username'] = user.username
    else:
        data = serializer.errors
    return JsonResponse(data)


@csrf_exempt
def signin(request):
    '''
    user login
    '''
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only'})

    username = request.POST['username']
    password = request.POST['password']

# validation part
    # if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$]", username):
    #     return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at least of 3 char'})

    try:
        user = UserModel.objects.get(username=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                username=username).values().first()
            usr_dict.pop('password')
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)

            return JsonResponse({'user': usr_dict, 'token': token.key})

        else:
            return JsonResponse({'error': 'Invalid Password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Username'})


def signout(request, user_id):
    '''
    user logout
    '''
    try:
        user = CustomUser.objects.get(id=user_id)
        user.auth_token.delete()
        logout(request)
        return JsonResponse({'success': 'Logout Success'})
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid'})


# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes_by_action = {'create': [AllowAny]}
#     queryset = CustomUser.objects.all().order_by('id')
#     serializer_class = UserSerializer

#     def get_permissions(self):
#         try:
#             return [permission() for permission in self.permission_classes_by_action[self.action]]

#         except KeyError:
#             return [permission() for permission in self.permission_classes]
