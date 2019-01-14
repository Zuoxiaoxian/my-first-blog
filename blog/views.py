from django.shortcuts import render

# Create your views here.
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(title__contains='文章').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    