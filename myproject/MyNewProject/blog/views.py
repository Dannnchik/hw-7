from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse

def list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
    return HttpResponse("Hello, this is the blog index.")

from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):

@login_required
def post_create(request):

@login_required
def post_detail(request, pk):

