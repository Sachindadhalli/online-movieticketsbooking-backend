from rest_framework import serializers
from .models import Theatre,Movie_detail

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields ='__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_detail
        fields = '__all__'
