from collections import OrderedDict

from django.conf import settings
from rest_framework import viewsets, generics, permissions, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    Each API Endpoint contains corresponding documentation.
    """
    if getattr(settings, 'API_ROOT', 'DISABLED') == "DISABLED":
        return Response({"project": "{{ project_name }}"})

    return Response(OrderedDict([
        ('Currency', OrderedDict([
            ('currencies', reverse('currency-list', request=request, format=format)),
        ])),
    ]))
