from django.shortcuts import render
from Blog.models import Post
# Create your views here.


def blog(request):
    All_posts = Post.objects.all()
    print(All_posts)
    return render(request, 'Blogs/Posts.html', context={'All_posts' : All_posts})

