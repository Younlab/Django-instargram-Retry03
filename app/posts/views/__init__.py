from .post_list import *
from .post_create import *
from .post_delete import *
from .comment import *
from .post_like import *
from .post_search import *



# @login_required(redirect_field_name='posts:post-create')
# def post_create_r(request):
#     if request.method == 'POST':
#         # Post.objects.create(
#         #     author=request.user,
#         #     photo=request.FILES['photo'],
#         #     content=request.POST['content'],
#         # )
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(author=request.user)
#             post.save()
#             print(request.GET)
#
#             return redirect('index')
#
#     else:
#         form = PostForm()
#         # return redirect('index')
#     context = {
#         'form':form,
#     }
#     return render(request, 'posts/post_create.html', context)










