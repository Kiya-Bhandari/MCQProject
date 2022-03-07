'''
creates the model for quizes app
'''
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)


class Quiz(models.Model):
    """
        A class to represent a Quiz.

        ...

        Attributes
        ----------
        topic : str
            subject for quiz
        number_of_questions : int
            total number of question respective to the topic
        time : int
            time to be taken for the quiz for the topic
        difficulty : str
            difficulty level for the quiz
        Methods
        -------
        get_questions(self):
            returns the question object respective to the topic
    """
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return str(self.topic) + "," + str(self.difficulty)

    def get_questions(self):
        '''
            Returns the question object respective to the topic

        '''
        return self.question_set.all()

    class Meta:
        '''
        A class that defines name of table in DB and in django admin
        '''
        db_table = 'quiz'
        verbose_name_plural = "Quizes"


class AssignDeassignQuiz(models.Model):

    """
        A class to represent a assigned/deassigned test.

        ...

        Attributes
        ----------
        assign_deassign : boolean
            particular test is assigned or not
        topic : foreign key(Quiz)
        user : foreign key(User)
        created : date field
            date the test is assigned
        expired : date field
            date when will the test gets expired
        is_attempted : boolean
            indicates whether the user has completed the test or not

    """
    assign_deassign = models.BooleanField(default=False)
    topic = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateField(null=True, blank=True)
    expired = models.DateField(null=True, blank=True)
    is_attempted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        '''
        A class that defines name of table in DB and in django admin
        '''
        db_table = 'assignDeassignQuiz'
        verbose_name_plural = "Assign Deassign Quizes"
