from django.shortcuts import render
from Blog.models import Post
# Create your views here.


def blog(request):
    all_post = Post.objects.all()
    print(all_post)
    context = {
        'all_post' : all_post,
    }
    return render(request, 'Blogs\Blog.html', context)

