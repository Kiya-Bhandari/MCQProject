'''
defines the views for the results app
'''
import json
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from api.questions.models import Question,Answer
from api.quizes.models import Quiz,AssignDeassignQuiz
from api.results.models import Result
from api.results.serializers import ResultSerializer
# Create your views here.

UserModel = get_user_model()


def history(request, user_id):
    """
        if the user is authenticated it will render the 'history page' else redirect to 'login'
    """

    user = UserModel.objects.get(id=user_id)
    history_data = Result.objects.filter(user=user)
    serializer = ResultSerializer(history_data, many=True)
    return JsonResponse({'history_data': serializer.data})


@csrf_exempt
@api_view(['POST', ])
def save_quiz_view(request, user_id,quiz_id):
    """
        stores the result for the test and return json response which contains score for the test.
    """
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid parameters only'})

    questions = []
    total_marks = 0
    data =  json.loads(request.body.decode('utf-8'))
    # print("data : ",data)

    for ques in data.keys():
        print('key : ', ques)
        question = Question.objects.get(text=ques)
        total_marks += question.marks
        questions.append(question)
    # print(questions)

    user = UserModel.objects.get(id=user_id)

    quiz = Quiz.objects.get(pk=quiz_id)

    score = 0

    for question in questions:
        a_selected = request.POST.get(question.text)
        if a_selected != '':
            question_answers = Answer.objects.filter(question=question)
            for answer in question_answers:
                if a_selected == answer.text:
                    if answer.correct:
                        score += question.marks
    AssignDeassignQuiz.objects.filter(Q(user=user) & Q(
            topic=quiz)).update(is_attempted=True)
    Result.objects.create(quiz=quiz, user=user, score=score)
    return JsonResponse({'message': 'Thank you for taking test.',
                        'score': "You have secured " + str(score) +
                        " marks out of "+str(total_marks) + " ."})
                        