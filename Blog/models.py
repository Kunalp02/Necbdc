from django.db import models
from Accounts.models import Account



class Post(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog_images/')
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(default=None)

    def __str__(self):  
        return self.title  


class Post_Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length = 10, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    def __str__(self):
        return self.subject





