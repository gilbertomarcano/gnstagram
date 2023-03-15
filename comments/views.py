from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, DetailView, ListView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from comments.forms import CommentForm
from comments.models import Comment


# Create your views here.
class CommentDetailView(LoginRequiredMixin, DetailView):
    """
    Comment detail view.
    """
    template_name = 'comments/comment_card.html'
    context_object_name = 'comment'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        print(context)
        return context


class CommentListView(LoginRequiredMixin, ListView):
    """
    Commnet list view.
    """
    template_name = 'comments/list.html'
    model = Comment
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'comment'


@login_required
def create(request):
    if request.method == "POST":
        post_id = request.headers['Referer'].split('/')[-2]
        data = {
            'text': request.POST['text'],
            'user': request.user.id,
            'post': post_id
        }
        form = CommentForm(data)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse('posts:detail', kwargs={'pk': post_id}))
    
    print('time to go')
    form = CommentForm()
    return render(
        request,
        'posts/detail.html',
        {'form': form, 'user': request.user}
    )
