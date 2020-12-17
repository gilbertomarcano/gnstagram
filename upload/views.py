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
    user = request.user
    instance = UserProfile.objects.get(pk=1)
    if request.method == "POST":
        # form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        form = PostForm(request.POST, request.FILES)
        print('Form is POST')
        print(form)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
        else:
            print('Form invalid')
    else:
        form = PostForm()
    
    return render(
        request,
        'avatar_upload.html',
        {'form': form}
    )
