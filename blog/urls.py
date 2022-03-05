from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns=[

    
    path('',views.BlogList,name='list'),
    #path('<int:post_pk>/', ,name='detail'),
    # path('/', ,name=),
]