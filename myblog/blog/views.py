from django.shortcuts import render
from post.models import Post


# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'main/frontpage.html', {'posts':posts,})

def about(request):
    return render(request, 'main/about.html')
