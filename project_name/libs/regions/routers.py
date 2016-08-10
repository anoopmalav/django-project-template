"""
"""
from django.conf.urls import patterns, url
from rest_framework.routers import SimpleRouter

from {{ project_name }}.libs.regions import views


router = SimpleRouter()

router.register(r'countries', views.CountryViewSet, base_name='country')
router.register(r'states', views.StateViewSet, base_name='state')
router.register(r'cities', views.CityViewSet, base_name='city')


urlpatterns = patterns('',
    url(r'^countries/(?P<country_id>\d+)/states/$', views.CountryStateList.as_view(), name='countrystate-list'),
    url(r'^states/(?P<state_id>\d+)/cities/$', views.StateCityList.as_view(), name='statecity-list'),
)

urlpatterns += router.urls
