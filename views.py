from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  context={}
  return render(request,'blog/home.html',context)
def FAQ(request):
  context={}
  return render(request,'blog/FAQ.html',context)
def notifications(request):
  context={}
  return render(request,'blog/notifications.html',context)

class PostListView(ListView):
       queryset = Post.published.all()
       context_object_name = 'posts'
       template_name = 'blog/post/list.html'
        
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,slug=post,
                                  status='published',
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day)
    context={'post':post}
    return render(request,'blog/post/detail.html',context)
