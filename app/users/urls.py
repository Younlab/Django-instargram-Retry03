from django.urls import path
from . import views

app_name='users'
urlpatterns=[
    path('', views.sign_in, name='sign-in'),
    path('signout/', views.sign_out, name='sign-out'),
    path('signup/', views.sign_up, name='sign-up'),
]