from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movies, Directors, Actors

class MoviesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movies
        fields = ('id', 'title', 'released', 'runtime', 'description', 'genre', 'director', 'main_actor', 'languae', 'country')
        
class DirectorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Directors
        fields = ('id', 'name','movies_directed', 'country')
        
class ActorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actors
        fields = ('id', 'name','age','movies_featured', 'country')



