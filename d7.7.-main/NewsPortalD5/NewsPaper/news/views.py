from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime


# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = 'created_at'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


class NewsSearch(ListView):
    model = Post
    ordering = 'created_at'
    template_name = 'post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context
class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = '/news/'

class NewsEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
