from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('avail-movielist/<city>/', views.AvailMovieList, name="AvailMovieList"),
    path('update-movie-timing/<str:pk>/', views.UpdateMovieTiming, name="UpdateMovieTiming"),
    path('add-movie/', views.AddMovie, name="AddMovie"),
]