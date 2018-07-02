__all__ = (
    'post_create',
)
from django.shortcuts import redirect, render

from ..forms import PostModelForm

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
            return redirect('posts:post-list')

    context={
        'form':form,
    }
    return render(request, 'posts/post_create.html', context)