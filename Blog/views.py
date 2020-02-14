from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
'''
all_posts = [

    {
        'author':'James',
        'title':'How Learn Django Quickly',
        'content':'In this post i will teach you How Learn Django Quickly',
        'date_posted':'Dec 24,2019 10:00 AM'

    },
    {
        'author':'Tom',
        'title':'Python JSON',
        'content':'How to deal with Python JSON',
        'date_posted':'Dec 23,2019 1:00 PM'

    },
    {
        'author':'Pintu',
        'title':'How django Static folder works',
        'content':'In this post i am going to explaine you how django static folder works',
        'date_posted':'Dec 23,2019 1:00 PM'

    }
]

'''

all_posts = Posts.objects.all()


def home(request):
    data = {
        'posts':all_posts
    }
    return render(request, 'home.html',data)
    #return HttpResponse("hii how are you.....")


class PostListView(ListView):
    model = Posts
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-dated_post']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Posts
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)
        # template_name = 'post_form.html'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'

    model = Posts
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'login'

    model = Posts
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


def about(request):
    return render(request,'about.html')