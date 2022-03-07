'''
helps in serialization and deserialization for Quiz and AssignDeassign model
'''
from rest_framework import serializers
from api.quizes.models import Quiz, AssignDeassignQuiz


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    '''
    A class that helps in serializing and deserializing

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None

    '''
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
        model = Quiz
        fields = ('id', 'topic', 'number_of_questions', 'time', 'difficulty')


class AssignDeassignSerializer(serializers.ModelSerializer):
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
    topic = QuizSerializer()

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
        model = AssignDeassignQuiz
        fields = ('id', 'topic', 'created', 'expired')
