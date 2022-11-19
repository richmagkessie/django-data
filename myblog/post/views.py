from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm
# Create your views here.
def details(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'second/details.html', {'post':post, 'form':form,})

def category(request):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'second/category.html', {'category':category,})
