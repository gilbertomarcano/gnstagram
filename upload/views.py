from django.shortcuts import render
from django.shortcuts import redirect

from upload.forms import AvatarUploadForm
from upload.models import UserProfile
from posts.forms import PostForm
from posts.models import Post

# Create your views here.
def avatar_upload(request):
    user = request.user
    instance = UserProfile.objects.get(pk=1)
    print('Epa update')
    if request.method == "POST":
        # form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('upload/')
    else:
        print('GET REQUESTTTTTT')
    form = PostForm()
    return render(request, 'avatar_upload.html', {'form': form})
