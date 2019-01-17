from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from django.utils import timezone

from .forms import PostForm

from django.shortcuts import redirect # 创建文章之后，点击保存之后，能在post_detail页面创建新的博客内容

def post_list(request):
    posts = Post.objects.filter(title__contains='文章').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) # 我们要用表单里的数据构建PostForm
        # 检查表单是否正确（所有必填字段都要被设置并且不会保存任何不正确的值）
        if form.is_valid():
            # form.save保存表单，commit=False意味着我们还不想保存Post模型—我们想首先添加作者。
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # 创建完新帖子我们就转去post_detail页面。
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})