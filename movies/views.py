from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import Movies, Directors, Actors
from .serializers import MoviesSerializer, DirectorsSerializer, ActorsSerializer

#create your views here

class MoviesView(APIView):
    
    def get(self, request):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteMovie(APIView):
    
    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MoviesSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActorsView:
    
    def get(self, request):
        actors = Actors.objects.all()
        serializer = ActorsSerializer(actors, many=True)
        return Response(serializer.data)
    
