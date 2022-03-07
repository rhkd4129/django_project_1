from django.shortcuts import redirect, render
from .models import Post,Comment
from django.shortcuts import get_list_or_404,get_object_or_404
from .forms import searchForm,PostForm
from django.db.models import Q


def BlogList(request):
    posts = Post.objects.all()
    q = request.GET.get('search','')
    if q:
        posts = Post.objects.filter(Q(title__icontains = q)|Q(content__icontains =q)).distinct()
    return render(request,'blog/blog_list.html',{'posts':posts,'q':q,})#'form':searchForm,



def blog_detail(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    return render(request,'blog/blog_detail.html',{'post':post,})




def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request,'blog/post_form.html',{'form':form,})




def blog_edit(request,post_pk):
    post = get_object_or_404(Post,pk =post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post_form.html',{'form':form,})


def blog_delete(request,post_pk):
    post = get_object_or_404(Post,pk =post_pk)
    if request.method =='POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request,'blog/blog_delete.html',{'post':post})
  


