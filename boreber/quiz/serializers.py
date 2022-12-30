from rest_framework import serializers
from .models import Answer, Question, Choice, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'all'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = 'all'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = 'all'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = 'all'