import collections

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def PUBLIC_APIS(r, f):
    return [
        ('registration', reverse('api-registration', request=r, format=f)),
        ('login', reverse('api-login', request=r, format=f)),
        ('logout', reverse('api-logout', request=r, format=f))

    ]

@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    GET:
    Display all available urls.

    Since some urls have specific permissions, you might not be able to access
    them all.
    """
    apis = PUBLIC_APIS(request, format)
    return Response(collections.OrderedDict(apis))
