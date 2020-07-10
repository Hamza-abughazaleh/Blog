from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^article/detail/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/like/(?P<pk>\d+)$', views.likeArticleView.as_view(), name='like_article')
]
