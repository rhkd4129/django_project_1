from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns=[

    
    path('',views.BlogList,name='post_list'),
    path('<int:post_pk>/',views.blog_detail ,name='post_detail'),
    path('create/',views.blog_create ,name='blog_create'),
    path('edit/<post_pk>/',views.blog_edit ,name='blog_edit'),
    path('delete/<post_pk>/',views.blog_delete ,name='blog_delete'),
    
]