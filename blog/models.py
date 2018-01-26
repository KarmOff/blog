from django.contrib.auth.models import User
from django.db import models
from django.contrib import auth


SHORT_TEXT_LEN = 300

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    article_user = models.ForeignKey(User)

    def __str__(self):
        return "%s" % self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        return self.text

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_comments = models.ForeignKey(User, on_delete=models.CASCADE)
    comments_text = models.TextField()


    def __str__(self):
        return self.comments_text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
