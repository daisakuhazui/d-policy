from django.db import models


class Post(models.Model):
    # ブログ記事のタイトル
    title = models.CharField(max_length=200)
    # ブログ記事の本文
    content = models.TextField()
    # ブログ記事が公開された日付
    pub_date = models.DateTimeField(auto_now_add=True)
    # ブログ記事が更新された日付
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
