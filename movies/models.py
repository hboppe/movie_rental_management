from django.db import models

class Ratings(models.TextChoices):
    DEFAULT = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None, null=True)
    rating = models.CharField(
        max_length=20,
        choices=Ratings.choices,
        default=Ratings.DEFAULT
    )
    synopsis = models.TextField(default=None, null=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies"
    )
