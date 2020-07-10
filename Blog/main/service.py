from django.core.exceptions import ValidationError

from main.models import Like, Article


def get_total_like_for_article(article_id):
    query = Like.objects.filter(article_id=article_id).count()
    return query


def validate_like_article(article_id, user):
    article = Article.objects.get(id=article_id)
    try:
        like = Like(
            user_id=user,
            article_id=article
        )
        like.save()
        new_like_count = get_total_like_for_article(article.id)
        return True, new_like_count
    except ValidationError as e:
        error = str(e)
        return False, error
