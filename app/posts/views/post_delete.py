from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from ..models import Post

__all__ = (
    'post_delete',
)

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
