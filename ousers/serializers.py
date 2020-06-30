from rest_framework import serializers
from ousers.models import User,QuestionFeedback,Questions

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = self.validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data.get('email')
        user.set_password(password)
        user.save()
        return user

class QuestionFeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionFeedback
        fields = ['questions','feedback']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
