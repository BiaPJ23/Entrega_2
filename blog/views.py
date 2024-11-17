from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

def index(request):
    context = {}
    return render(request, 'blog/index.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.order_by('-created_at') 
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content)
        return redirect('blog:list_post')
    return render(request, 'blog/post_form.html')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('blog:detail_post', pk=pk)
    return render(request, 'blog/post_form.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list_post')
    return render(request, 'blog/post_delete.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    posts = category.posts.all()  
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})


@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Comment.objects.create(
                author=request.user, 
                post=post,
                text=text,
                created_at=now()
            )
            return redirect('blog:detail_post', pk=post.id) 

    return render(request, 'blog/add_comment.html', {'post': post})