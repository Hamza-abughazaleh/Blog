from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers

from main.api import views

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet, basename='article')
router.register(r'catigory', views.CategoryViewSet, basename='category')


urlpatterns = [
    # urls for Django Rest Framework API
    url('^', include(router.urls)),
    url(r'^like_article/(?P<pk>\d+)$', csrf_exempt(views.LikeView.as_view()), name='api_like_article'),

]
