from rest_framework import serializers, status
from .models import Meal, Rating

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        # fields = '__all__'
        
        


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description','num_of_rating','avr_rating',)
      

class RatingSerializer(serializers.ModelSerializer):
    # meal_title = serializers.CharField(source='meal.title')
    # username = serializers.CharField(source='user.username')
    #'meal_title','username'

    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal',)