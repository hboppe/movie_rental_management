from rest_framework import serializers
from .models import Ratings
from .models import Movie, MovieOrder
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(choices=Ratings.choices, default=Ratings.DEFAULT)
    synopsis = serializers.CharField(default=None, required=False)
    added_by = serializers.EmailField(
        read_only=True,
        source="user.email"
    )

    def create(self, validated_data: dict) -> Movie:
        movie = Movie.objects.create(**validated_data)
        
        return movie


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, source="ordered_movie.title", read_only=True)
    buyed_at = serializers.DateField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField(
        source="client.email",
        read_only=True
    )

    def create(self, validated_data: dict) -> MovieOrder:
        movie_order = MovieOrder.objects.create(**validated_data)
        return movie_order