#Import the necessary modules

from rest_framework import serializers
from bunnies.models import Bunny, RabbitHole


class RabbitHoleSerializer(serializers.ModelSerializer):
    """Serializer for RabbitHole model"""

    # Specify related field for bunnies and queryset for PrimaryKeyRelatedField
    bunnies = serializers.PrimaryKeyRelatedField(many=True, queryset=Bunny.objects.all())

    # Create custom serializer method to get bunny count for each rabbit hole
    bunny_count = serializers.SerializerMethodField()

    def get_bunny_count(self, obj):
        """Method to get bunny count for each rabbit hole"""
        return obj.bunnies.count()

    class Meta:
        model = RabbitHole
        fields = ('location', 'bunnies', 'bunny_count', 'owner')


class BunnySerializer(serializers.ModelSerializer):
    """Serializer for Bunny model"""

    # Specify related field for home and queryset for SlugRelatedField
    home = serializers.SlugRelatedField(queryset=RabbitHole.objects.all(), slug_field='location')

    # Create custom serializer method to get family members for each bunny
    family_members = serializers.SerializerMethodField()

    def get_family_members(self, obj):
        """Method to get family members for each bunny"""
        return []

    def validate(self, attrs):
        """Method to validate data"""
        return attrs

    class Meta:
        model = Bunny
        fields = ('name', 'home', 'family_members')
