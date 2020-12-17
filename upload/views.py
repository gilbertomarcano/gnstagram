from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from upload.forms import AvatarUploadForm
from upload.models import UserProfile
from posts.forms import PostForm
from posts.models import Post

# Create your views here.
@login_required
def avatar_upload(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.profile = request.user.profile
            form.save()
            return redirect('posts:feed')
        
    form = PostForm()
    return render(
        request,
        'avatar_upload.html',
        {'form': form, 'user': request.user, 'profile': request.user.profile}
    )
