# Import the necessary modules

from django.conf import settings
from django.db import models


class RabbitHole(models.Model):
    """
    Represents a rabbit hole where bunnies live.
    """

    # Location of the rabbit hole
    location = models.CharField(max_length=64, unique=True)

    # Owner of the rabbit hole
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    # Maximum number of bunnies allowed in the rabbit hole
    bunnies_limit = models.PositiveIntegerField(default=5)


class Bunny(models.Model):
    """
    Represents a bunny that lives in a rabbit hole.
    """

    # Name of the bunny
    name = models.CharField(max_length=64)

    # Rabbit hole where the bunny lives
    home = models.ForeignKey(
        RabbitHole,
        on_delete=models.CASCADE,
        related_name='bunnies'
    )
