from webbrowser import get
from django.shortcuts import render, get_object_or_404
import mistune
from django.db.models import Q
from .models import Post
# Create your views here.
class MyCustomRenderer(mistune.HTMLRenderer):
    def image(self, src, title, alt_text):
       return "<img src='%s' alt='%s' class='img-fluid'>" % (src, alt_text)

def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'posts': posts})

def blog_detail(request, id, **kwargs):
    post = get_object_or_404(Post, id=id)
    renderer = MyCustomRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    post.content = markdown(post.content)
    return render(request, 'main/post.html', {'post': post})

def search_post(request):
    if request.method == "GET":
        search = request.GET.get('search').lower()
        posts = Post.objects.all().filter(Q(title__contains=search) | Q(description__contains=search) | Q(content__contains=search)) 
        return render(request, 'main/search.html', {'posts': posts})