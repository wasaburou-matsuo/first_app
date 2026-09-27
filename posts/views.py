from django.shortcuts import render ,redirect
from django.shortcuts import render
from django.views import View
from posts.models import Post
from .forms  import PostForm

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, 'posts/index.html', {'posts': posts})

class CreateView(View):
    def get(self, request, *args, **kwargs): # 投稿作成ページを表示するためのGETリクエストの処理
        form = PostForm()
        return render(request, 'posts/create.html', {'form': form})

    # 投稿作成ページでフォームが送信されたときのPOSTリクエストの処理
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        form.save() # フォームの内容を保存して新しい投稿を作成
        if form.is_valid():
            form.save() # フォームの内容を保存して新しい投稿を作成
        # 投稿作成後にトップページにリダイレクトする
        return redirect('posts:index')