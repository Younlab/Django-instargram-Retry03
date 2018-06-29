from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # root page url
    path('', views.post_list, name='post-list'),
    # 포스팅 버튼
    path('posting/', views.post_create, name='post-create'),
    # 해당 포스트의 아이디값을 받아서 삭제 버튼 구현
    path('<int:pk>/delete/', views.post_delete, name='post-delete'),
    path('<post_pk>/comment/', views.comment, name='comment-create')
]
