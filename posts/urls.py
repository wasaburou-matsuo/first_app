from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # トップページのURLパターンと対応するビュー
    path('create/', views.CreateView.as_view(), name='create'), # 投稿作成ページのURLパターンと対応するビュー
]