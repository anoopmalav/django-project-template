"""
"""
from rest_framework import serializers
from {{ project_name }}.libs.regions.models import Country, State, City


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    _id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = Country


class StateSerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    _id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = State
        exclude = ('country',)


class CitySerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    _id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = City
        exclude = ('country', 'state',)
