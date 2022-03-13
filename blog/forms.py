from django import forms
from .models import Post,Comment


class searchForm(forms.Form):
    search = forms.CharField(label='Search')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','photo','is_public','gender']#'__all__'
        #fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

        
        # labels = {
        #     'content': '댓글내용',
        # }

        #    widgets={
        #     "caption": forms.Textarea,
        # }
        