
from django.urls import path,include
from .views import post_views
from .views import comment_views
app_name = 'blog'

urlpatterns=[

    
    path('',post_views.BlogList,name='post_list'),
    path('post/<int:post_pk>/',post_views.blog_detail ,name='post_detail'),
    path('post/create/',post_views.blog_create ,name='blog_create'),
    path('post/edit/<int:post_pk>/',post_views.blog_edit ,name='blog_edit'),
    path('post/delete/<int:post_pk>/',post_views.blog_delete ,name='blog_delete'),

    path('comment/create/<int:post_pk>',comment_views.comment_create,name='comment_create'),
    path('comment/edit/<int:comment_pk>',comment_views.comment_edit,name='comment_edit'),
    path('comment/delete/<int:comment_pk>',comment_views.comment_delete,name='comment_delete'),
]