import logging
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TheatreSerializer, MovieDetailSerializer

from .models import Theatre, Movie_detail

from datetime import datetime, timedelta

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Movie':'/availmovielist/<city>/',
        'UpdateMovieTiming':'/update-movie-timing/',
        'AddMovie':'/add-movie/',
		}

	return Response(api_urls)

@api_view(['GET'])
def AvailMovieList(request, city):
    city = city.title()
    requested_city = Theatre.objects.filter(city=city).first()
    if(requested_city):
        movies_in_requested_city = Theatre.objects.filter(
            city=requested_city).values('id').distinct()
        movies_list_json = []
        for movie_in_requested_city in movies_in_requested_city:
            movies = Movie.objects.filter(
                pk=movie_in_requested_city['id'])
            for movie in movies:
                movies_list_json.append(TheatreSerializer(no_of_screen).data)
        return JsonResponse(movies_list_json, safe=False)
    else:
        logging.info("Users requested for movies in city %s"%city)
        return JsonResponse({"message": "Currently %s is not registered in our cities" % city})

@api_view(['POST'])
#Update Movie timing by movie id
def UpdateMovieTiming(request, pk):
	try:
		movie = Movie_detail.objects.get(id=pk)
		serializer = MovieDetailSerializer(instance=movie, data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)
	except:
		return Response(None)

@api_view(['POST'])
#Add new movie to the list
def AddMovie(request):
	try:
		serializer = MovieDetailSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

		return Response(serializer.data)
	except:
		return Response(None)
