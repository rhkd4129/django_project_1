from django.urls import reverse
from django.db import models
from django.conf import settings 


class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL) # 추천!
    title = models.CharField(max_length=20)
    photo = models.ImageField(blank = True, upload_to = 'blog/post/%Y/%m/%d')
    content = models.TextField()
    is_public = models.BooleanField(default = False,verbose_name= '공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title


    def get_absolute_url(self):
         return reverse('blog:post_detail',args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.message


# Create your models here.
