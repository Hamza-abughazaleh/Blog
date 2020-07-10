from rest_framework import viewsets, status
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import permissions
from main.api.serializers import CategorySerializer, CategoryDetailSerializer, ArticleSerializer, \
    ArticleDetailsSerializer, LikeSerializer
from main.models import Article, Category, Like
from main.service import validate_like_article


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    details_serializer_class = CategoryDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        kwargs['context'] = self.get_serializer_context()
        serializer = self.details_serializer_class(instance, context={'request': request})
        return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    details_serializer_class = ArticleDetailsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        kwargs['context'] = self.get_serializer_context()
        serializer = self.details_serializer_class(instance, context={'request': request})
        return Response(serializer.data)


class LikeView(APIView):
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, **kwargs):
        # API for retail user login\
        article_id = self.kwargs['pk']
        if article_id:
            is_valid, date = validate_like_article(article_id, request.user)
            if is_valid:
                return Response("ok", status=status.HTTP_200_OK)
            else:
                return Response({'error': date}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(
            {'error': 'add article id'},
            status=status.HTTP_400_BAD_REQUEST)
