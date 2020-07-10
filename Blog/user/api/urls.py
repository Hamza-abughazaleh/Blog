from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from user.api import views

urlpatterns = [
    # urls for Django Rest Framework API

    url(r'^register/', csrf_exempt(views.RegisterAPIView.as_view()), name='api-registration'),
    url(r'^login/$', csrf_exempt(views.LoginView.as_view()), name='api-login'),
    url(r'^logout/$', csrf_exempt(views.LogoutView.as_view()), name='api-logout'),

]