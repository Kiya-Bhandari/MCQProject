'''
creates the model for Questions app
'''
from django.db import models
from api.quizes.models import Quiz
# Create your models here.


class Question(models.Model):

    """
        A class to represent a Question.

        ...

        Attributes
        ----------
        text : str
            question
        quiz : foreign key(Quiz)
            to relate question to topic
        marks : float
            marks for the question

        Methods
        -------
        get_answers(self):
            returns the answer object respective to the question
    """
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    marks = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        '''
            Returns the answer object respective to the question

        '''
        return self.answer_set.all()

    class Meta:
        '''
        A class that defines name of table in DB and in django admin
        '''
        db_table = 'question'


class Answer(models.Model):

    """
        A class to represent Answer.

        ...

        Attributes
        ----------
        text : str
            option for the particular queation
        correct : boolean
            states whether option belonging to question is correct or not
        question : foreign key(Question)
            relate answer to the question

    """
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question : {self.question.text},answer:{self.text},correct:{self.correct}"

    class Meta:
        '''
        A class that defines name of table in DB and in django admin
        '''
        db_table = 'answer'
