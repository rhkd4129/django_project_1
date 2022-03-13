from ..models import Post,Comment
from ..forms import CommentForm
from django.shortcuts import render,redirect

def comment_create(request,post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
    else:
        form = CommentForm()
    return render(request,'comment/comment_create.html',{"form":form})