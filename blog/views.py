from django.shortcuts import render
from .models import Post
# from django.http import Http404

from django.shortcuts import get_object_or_404

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    post=get_object_or_404(Post, id=id)
    return render(request, 'blog/post/details.html', {'post': post})

    
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    # return render(request, 'blog/post/detail.html', {'post': post})