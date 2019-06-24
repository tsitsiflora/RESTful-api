from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movies, Directors, Actors

class MoviesSerialiser(serializers.ModelSerializer):
    
    class Meta:
        model = Movies
        fields = ('id', 'title', 'year')
        
class DirectorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Directors
        fields = ('id', 'name', 'country')
        
class ActorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actors
        fields = ('id', 'name', 'country')



