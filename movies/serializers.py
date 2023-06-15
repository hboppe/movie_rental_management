from rest_framework import serializers
from .models import Ratings
from .models import Movie


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
