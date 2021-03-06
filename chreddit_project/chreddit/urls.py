from django.urls import path
from . import views

urlpatterns = [
    # if we go to '/', go to the views, run the post_list function.
    # third argument is naming this path.
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profiles/new', views.profile_create, name='profile_create'),
    path('profiles/<int:pk>/edit', views.profile_edit, name='profile_edit'),
    path('profiles/<int:pk>/delete', views.profile_delete, name='profile_delete'),
]
