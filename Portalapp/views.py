from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog, Tag
from django.shortcuts import render, reverse
from django.shortcuts import render



def post_list(request):
    posts = Blog.objects.all()
    return render(request, 'index.html', context = {'posts': posts})

def post_detail(request, slug):
    post= Blog.objects.get (slug_iexact=slug)
    return render (request, 'single_post.html', context={'post':post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', context={'tags': tags})


class BlogListView(ListView):

 model=Blog
 template_name = 'index.html'

def get_context_data(self, *args, **kwargs):
    context = super(BlogListView,self).get_context_data(*args, **kwargs)
    context ['posts']=self.model.objects.all()
    context ['custom_managers'] = self.model.custom_manager
    return context






'''class CategoryListView(ListView):

    model=Category
    template_name = 'index.html'

def get_context_data(self, *args, **kwargs):
    context = super(CategoryListView,self).get_context_data(*args, **kwargs)
    context ['category']=self.model.objects.all()
    return context



class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'

def get_context_data(self, **kwargs):
    context = super(CategoryDetailView, self).get_context_data(**kwargs)
    context['categories'] = self.model.objects.all()
    context ['categoriy']= self.get_object()
    context ['posts'] = self.get_object().Blog.all()
    return context'''
