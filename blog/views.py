from django.shortcuts import render
from .models import Post,Comment
from django.shortcuts import get_list_or_404,get_object_or_404

def BlogList(request):
    posts = Post.objects.all()
    return render(request,'blog/blog_list.html',{'posts':posts,})



# Create your views here.
