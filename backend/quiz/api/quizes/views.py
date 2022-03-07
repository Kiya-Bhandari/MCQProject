'''
defines the views for the quiz app
'''
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from api.quizes.serializers import AssignDeassignSerializer
from .models import Quiz, AssignDeassignQuiz

UserModel = get_user_model()


def test_list(request, user_id):
    """
    returns the list of test to be taken.
    """
    user = UserModel.objects.get(id=user_id)
    testlist = AssignDeassignQuiz.objects.filter(
        Q(user=user) & Q(assign_deassign=True) & Q(is_attempted=False))
    serializer = AssignDeassignSerializer(testlist, many=True)
    return JsonResponse({'testLists': serializer.data})


def quiz_data_view(request, quiz_id):
    """
        return json response which contains questions and time period for the test.
    """
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = []
    for question in quiz.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append(

            {'question': str(question), 'answers': answers, 'marks': question.marks})

    return JsonResponse({
        'topic':quiz.topic,
        'data': questions,
        'time': quiz.time

    })
