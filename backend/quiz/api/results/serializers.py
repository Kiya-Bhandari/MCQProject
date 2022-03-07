'''
helps in serialization and deserialization for Result model
'''
from rest_framework import serializers
from api.quizes.serializers import QuizSerializer
from api.results.models import Result

class ResultSerializer(serializers.ModelSerializer):
    """
        A class that helps in serializing and deserializing


        ...

        Attributes
        ----------
        topic : tuple
            all fields of quiz
        Methods
        -------
        None
    """
    quiz = QuizSerializer()

    class Meta:
        '''
        A class that defines the fields to be serialized
        ...

        Attributes
        ----------

        model: model
            model to be serialized
        fields: tuple
            a tuple of fields to be serialized
        '''
        model = Result
        fields = ('quiz', 'score', 'created')
