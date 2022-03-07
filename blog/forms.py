from django import forms
from .models import Post


class searchForm(forms.Form):
    search = forms.CharField(label='Search')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','photo','is_public']#'__all__'



