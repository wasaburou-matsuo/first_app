from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model): #POSTモデル定義
    class Meta:
        db_table = 'posts'  # このモデルと紐づくテーブル名を指定

    content = models.CharField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
