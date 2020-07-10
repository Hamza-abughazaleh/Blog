
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.id, self.title)


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    author = models.CharField(max_length=50, null=True, blank=True)
    publish_date = models.DateTimeField(blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return '{} {}'.format(self.id, self.title)


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user_id.get_full_name(), self.article_id.title)

    def validate_unique(self, exclude=None):
        qs = Like.objects.filter(user_id_id=self.user_id, article_id_id=self.article_id).exists()
        if qs:
            raise ValidationError(_("You are like this Article before"))

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(Like, self).save(*args, **kwargs)