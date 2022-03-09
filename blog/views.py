from django.shortcuts import redirect, render
from .models import Post,Comment
from django.shortcuts import get_list_or_404,get_object_or_404
from .forms import searchForm,PostForm
from django.db.models import Q
from django.views.generic import ListView,DetailView,FormView,CreateView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

def BlogList(request):
    posts = Post.objects.all()
    q = request.GET.get('search','')
    if q:
        posts = Post.objects.filter(Q(title__icontains = q)|Q(content__icontains =q)).distinct()
    return render(request,'blog/blog_list.html',{'posts':posts,'q':q,})#'form':searchForm,

# class BlogList(ListView,FormView):
#     model = Post
#     template_name = 'blog/blog_list.html'
#     context_object_name = 'posts'
#     #form_class = searchForm

#     def form_valid(self, form) :
#         searchResult = form.cleaned_data.get('search')
#         post_list = Post.objects.filter(Q(title__icontains = searchResult)|
#         Q(content__icontains = searchResult)).distinct()
#         context['posts'] = post_list
#         return(self.request,self.template_name,context)
#BlogList = BlogList.as_view()



# def blog_detail(request,post_pk):
#     post = get_object_or_404(Post,pk = post_pk)
#     return render(request,'blog/blog_detail.html',{'post':post,})

class BlogDeatil(DetailView):
    model = Post
    template_name ='blog/blog_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = "post_pk"

blog_detail = BlogDeatil.as_view()



# def blog_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request,'blog/post_form.html',{'form':form,})


class BlogCreate(CreateView):
    model =Post
    form_class = PostForm
    template_name = 'blog/form.html'
    pk_url_kwarg = "post_pk"
blog_create = BlogCreate.as_view()
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.author = self.request.user
#         messages.success(self.request,'포스티저장')
#         return super().form_valid(form)






# def blog_edit(request,post_pk):
#     post = get_object_or_404(Post,pk =post_pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES,instance=post)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#     return render(request,'blog/post_form.html',{'form':form,})


class BlogEdit(UpdateView):
    model = Post
    form_class = PostForm
    pk_url_kwarg = "post_pk"
    template_name ='blog/form.html'
   
    def form_valid(self, form):
        return super().form_valid(form)
blog_edit = BlogEdit.as_view()




class BlogDelete(DeleteView):
    pk_url_kwarg = "post_pk"
    template_name ='blog/blog_delete.html'
    model=Post
    success_url = reverse_lazy('blog:post_list')
blog_delete = BlogDelete.as_view()


# def blog_delete(request,post_pk):
#     post = get_object_or_404(Post,pk =post_pk)
#     if request.method =='POST':
#         post.delete()
#         return redirect('blog:post_list')
#     return render(request,'blog/blog_delete.html',{'post':post})
  


