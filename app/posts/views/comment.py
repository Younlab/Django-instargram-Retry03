from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from ..models import Comment, Post

__all__ = (
    'comment',
)

def comment(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST['content']
        if not content:
            raise PermissionDenied('내용을 입력해주세요')

        if not request.user.username:
            return redirect('users:sign-in')
        Comment.objects.create(
            post=post,
            author=request.user,
            content=content
        )

        return redirect('posts:post-list')