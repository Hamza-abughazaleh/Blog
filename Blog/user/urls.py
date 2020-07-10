from django.conf.urls import url
from user import views

from main.helper import anonymous_required

# TEMPLATE TAGGING
app_name = 'user'

urlpatterns = (
    url('^login', anonymous_required(views.UserLogin.as_view()), name='user_login'),
    url('^logout', views.user_logout, name='user_logout'),
    url(r'^register/$', anonymous_required(views.UserRegister.as_view()), name='user_register'),

)
