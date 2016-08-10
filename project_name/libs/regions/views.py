"""
"""
from rest_framework import viewsets, filters, generics

from {{ project_name }}.libs.regions.models import Country, State, City
from {{ project_name }}.libs.regions.serializers import CountrySerializer, StateSerializer, CitySerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    **Search fields :**

    + `name`

    **Ordering fields :**

    + `code`
    + `name`
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name',)
    ordering_fields = ('code', 'name',)


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    **Query parameters :**

    `country` -- _id_, get states of country

    **Search fields :**

    + `name`

    **Ordering fields :**

    + `code`
    + `name`

    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filter_fields = ('country',)
    search_fields = ('name',)
    ordering_fields = ('code', 'name',)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    **Query parameters :**

    `country` -- _id_, get cities of country

    `state` -- _id_, get cities of state

    **Search fields :**

    + `name`

    **Ordering fields :**

    + `name`
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filter_fields = ('country', 'state',)
    search_fields = ('name',)
    ordering_fields = ('name',)


class CountryStateList(generics.ListAPIView):
    """
    **Search fields :**

    + `name`

    **Ordering fields :**

    + `code`
    + `name`

    """
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name',)
    ordering_fields = ('code', 'name',)

    def get_queryset(self):
        queryset = super(CountryStateList, self).get_queryset()
        return queryset.filter(country_id=self.kwargs.get('country_id'))


class StateCityList(generics.ListAPIView):
    """

    **Search fields :**

    + `name`

    **Ordering fields :**

    + `name`
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('name',)
    ordering_fields = ('name',)

    def get_queryset(self):
        queryset = super(StateCityList, self).get_queryset()
        return queryset.filter(state_id=self.kwargs.get('state_id'))
