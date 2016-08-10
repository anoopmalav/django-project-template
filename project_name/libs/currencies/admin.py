from django.contrib import admin

from {{ project_name }}.libs.currencies.models import Currency


admin.site.register(Currency)
