import json

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Article
from main.service import get_total_like_for_article, validate_like_article


# Create your views here.

class Home(ListView):
    template_name = 'main/index.html'

    def get_queryset(self):
        return Article.objects.all()[:20]


class ArticleDetailView(DetailView):
    template_name = 'main/article_detail.html'
    model = Article
    context_object_name = 'article_detail'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['total_like'] = get_total_like_for_article(self.kwargs['pk'])
        return context


class likeArticleView(View):
    def post(self, request, *args, **kwargs):
        article_id = self.kwargs['pk']
        if article_id:
            is_valid, date = validate_like_article(article_id, request.user)
            if is_valid:
                return HttpResponse(date, status=200)
            else:
                error_dict = ({'error': date})
                return HttpResponse(json.dumps(error_dict), status=406, content_type="application/json")
        return redirect('home')


class PermissionDenied(TemplateView):
    template_name = 'main/403.html'
