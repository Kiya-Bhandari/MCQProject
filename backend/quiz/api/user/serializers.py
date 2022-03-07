'''
helps in serialization and deserialization for CustomUser model
'''
from rest_framework import serializers
# from rest_framework.decorators import authentication_classes, permission_classes
# from django.contrib.auth.hashers import make_password
from api.user.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        A class that helps in serializing and deserializing


        ...

        Attributes
        ----------
        password2 : char
        Methods
        -------
        validate(self, attrs):
            validate password and password2

        create(self, validated_data):
        creates user
    """
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    # def save(self):
    #     user = CustomUser(
    #         username=self.validated_data['username'],
    #         first_name=self.validated_data['first_name'],
    #         last_name=self.validated_data['last_name'],
    #         email=self.validated_data['email']
    #     )
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']

    #     if password != password2:
    #         raise serializers.ValidationError(
    #             {'password': 'Password must match.'})
    #     user.set_password(password)
    #     user.save()
    #     return user
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)

    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     for attr, value in validated_data.items():
    #         if attr == 'password':
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, attr, value)
    #     instance.save()
    #     return instance

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
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2',
                  'is_active', 'is_staff', 'is_superuser')
