"""
"""
from rest_framework import serializers
from {{ project_name }}.libs.currencies.models import Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    """
    """
    _id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = Currency
