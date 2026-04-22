from django.shortcuts import render, redirect





from .models import Post
from .forms import PostForm

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request, request.FILES)
        if form.is_valid():
            pass
    else:
        form = PostForm()
    return render(request, '', {'form': form})