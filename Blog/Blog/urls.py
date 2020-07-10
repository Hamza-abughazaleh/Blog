"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf.urls import url, include

from main.views import PermissionDenied
from user.api import root

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    url(r'^', include('main.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^user/api-v1/', include('user.api.urls')),
    url(r'^user/api-v1/$', root.api_root, name='api-root'),
    url(r'^main/api-v1/', include('main.api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^permission-denied', PermissionDenied.as_view(), name='permission-denied'),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)