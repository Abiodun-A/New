from pyexpat import model
from tempfile import template
from unicodedata import name
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    template_name = 'blog.html'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    template_name = 'post_form.html'

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    template_name = 'post_confirm_delete.html'
