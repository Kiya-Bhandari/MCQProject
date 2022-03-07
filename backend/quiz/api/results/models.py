'''
creates the model for results app
'''
from django.db import models
from django.contrib.auth import get_user_model
from api.quizes.models import Quiz
# Create your models here.


class Result(models.Model):
    """
        A class to represent Result.

        ...

        Attributes
        ----------
        quiz : foreign key(Quiz)
            relate result to quiz(topic)
        user : foreign key(User)
            relate result to user
        score : float
            total marks secured in the test(quiz)
        created : date field
            specifies the date on which the test is given.

    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.FloatField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        '''
        A class that defines name of table in DB and in django admin
        '''
        db_table = 'results'
