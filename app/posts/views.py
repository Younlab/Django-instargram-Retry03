from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Post
from .forms import PostForm, PostModelForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts':posts,
    }

    return render(request, 'posts/post_list.html', context)

@login_required(redirect_field_name='posts:post-create')
def post_create_r(request):
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
            print(request.GET)

            return redirect('index')

    else:
        form = PostForm()
        # return redirect('index')
    context = {
        'form':form,
    }
    return render(request, 'posts/post_create.html', context)

def post_create(request):
    # PostModelForm 을 사용
    # form = PostModelForm(request.POST, request.FILE)
    # form.save(author=request.user)
    form = PostModelForm()
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')

    context={
        'form':form,
    }
    return render(request, 'posts/post_create.html', context)
# @require_POST
# @login_required
# def post_delete(request, pk):
# #     if request.method == 'POST':
# #         post = Post.objects.get(pk=pk)
# #         post.delete()
# #     return redirect('index')
# #
# # def post_edit(request):
# #     pass
# #
# # def recent_post(request):
# #     pass
#     post = get_object_or_404(Post, pk=pk)
#     if post.author != request.user:
#         raise PermissionDenied('지울 권한이 없습니다.')
#     post.delete()
#     return redirect('posts:post-list')

def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if request.user.username:
            if post.author.username == request.user.username:
                post.delete()
                return redirect('index')
            elif post.author.username != request.user.username:
                raise PermissionDenied('지울 권한이 없습니다.')
        else:
            return redirect('users:sign-in')

    # if request.method != 'POST':
    #     return HttpResponseNotAlloewd()
    # if not request.user.is_authenticated:
    #     return redirect('users:sign-in')

