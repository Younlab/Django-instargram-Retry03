from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts':posts,
    }

    return render(request, 'posts/post_list.html', context)

@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        Post.objects.create(
            author=request.user,
            photo=request.FILES['photo'],
            content=request.POST['content'],
        )
        return redirect('index')
    else:
        return render(request, 'posts/post_create.html')
@login_required(login_url='/accounts/login/')
def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect('index')

def post_edit(request):
    pass

def recent_post(request):
    pass

