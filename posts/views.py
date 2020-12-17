from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required


from posts.forms import PostForm

from posts.models import Post

# Create your views here.
class PostDetailView(LoginRequiredMixin, DetailView):
    """
    Post detail view.
    """

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class PostsFeedView(LoginRequiredMixin, ListView):
    """
    Return all published posts.
    """

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

# ###########################
#   OLD LIST VIEW           #
#############################
# @login_required
# def list_posts(request):
#     """
#     List existing posts.
#     """
#     posts = Post.objects.all().order_by('-created')
#     profile = request.user.profile
#     return render(request, 'posts/feed.html', {'posts': posts, 'profile': profile})



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from posts.models import Post
from posts.forms import PostForm

@login_required
def create(request):
    # instance = get_object_or_404(Post, user=user)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    form = PostForm()
    return render(
        request,
        'posts/new.html',
        {'form': form, 'user': request.user}
    )


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    Create a new post.
    """
    
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """
        Add user and profile to context.
        """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        context['backend_form'] = PostForm()
        context['lmao'] = 'LMAAAAAO'
        return context

# Create render without using a View class
# ###########################
#   OLD CREATE              #
#############################
# @login_required
# def create(request):
#     """
#     Create new post view.
#     """
#     if request.method == 'POST':
#        form = PostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('posts:feed')

#     else:
#         form = PostForm()
    
#     return render(
#         request,
#         'posts/new.html',
#         {'form': form,'user': request.user, 'profile': request.user.profile}
#     )