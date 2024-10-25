from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def text_response(request):
    return HttpResponse("Hello, this is a text response!")

def html_response(request):
    return render(request, 'myapp/template.html')

def post_list(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query)  # Фильтрация по заголовку

    paginator = Paginator(posts, 10)  # 10 постов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/post_list.html', {'page_obj': page_obj, 'query': query})

