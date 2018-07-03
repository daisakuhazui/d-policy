from django.db import models


class Author(models.Model):
    # ブログ著者の名前
    name = models.CharField(max_length=20)
    # ブログ著者のメールアドレス
    email = models.EmailField()
    # ブログ著者のパスワード
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    # ブログ著者のid
    author = models.ForeignKey(
        Author, related_name='posts', on_delete=models.PROTECT
    )
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
