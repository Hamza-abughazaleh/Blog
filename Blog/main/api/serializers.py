from django.shortcuts import redirect

from rest_framework import serializers

from main.models import Article, Category, Like
from main.service import get_total_like_for_article


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_details = serializers.HyperlinkedIdentityField(view_name='category-detail', lookup_field='pk')

    class Meta:
        model = Category
        fields = ('pk', 'title', 'category_details')


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'title', 'description')


class ArticleSerializer(serializers.ModelSerializer):
    article_details = serializers.HyperlinkedIdentityField(view_name='article-detail', lookup_field='pk')

    class Meta:
        model = Article
        fields = ('pk', 'title', 'author', 'article_details')


class ArticleDetailsSerializer(serializers.ModelSerializer):
    category_details = serializers.HyperlinkedRelatedField(view_name='category-detail', source='category',
                                                           read_only=True)
    created_date = serializers.DateTimeField(format='%b %d,%Y,%I:%M %p.')
    publish_date = serializers.DateTimeField(format='%b %d,%Y,%I:%M %p.')
    total_like = serializers.SerializerMethodField()
    like_article = serializers.HyperlinkedRelatedField(view_name='api_like_article', source='id',
                                                       read_only=True)

    class Meta:
        model = Article
        fields = (
            'pk', 'title', 'author', 'description', 'total_like', 'like_article', 'created_date', 'publish_date',
            'category_details')

    def get_total_like(self, article_id):
        return get_total_like_for_article(article_id)


class LikeSerializer(serializers.Serializer):
    pk = serializers.Serializer()

    class Meta:
        fields = ('pk')
