from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts':posts,
    }

    return render(request, 'posts/post_list.html', context)

@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        # Post.objects.create(
        #     author=request.user,
        #     photo=request.FILES['photo'],
        #     content=request.POST['content'],
        # )
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(author=request.user)
            post.save()
            return redirect('index')

    else:
        form = PostForm()
        # return redirect('index')
    context = {
        'form':form,
    }
    return render(request, 'posts/post_create.html', context)
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
