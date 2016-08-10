from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', '{{ project_name }}.views.api_root', name='api_root'),
    url(r'^', include('{{ project_name }}.libs.regions.routers')),
    url(r'^', include('{{ project_name }}.libs.currencies.routers')),
)
