"""
"""
from django.conf.urls import patterns, url
from rest_framework.routers import SimpleRouter

from project_name.libs.currencies import views


router = SimpleRouter()

router.register(r'currencies', views.CurrencyViewSet, base_name='currency')

urlpatterns = router.urls
