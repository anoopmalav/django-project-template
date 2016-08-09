"""
"""
from rest_framework import viewsets, filters

from project_name.libs.currencies.models import Currency
from project_name.libs.currencies.serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    **Search fields :**

    + `name`

    **Ordering fields :**

    + `code`
    + `name`
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('code', 'name',)
    ordering_fields = ('code', 'name',)
