from django.shortcuts import render

# Create your views here.

from upload.forms import AvatarUploadForm
from upload.models import UserProfile
from django.shortcuts import redirect

def avatar_upload(request):
    user = request.user
    instance = UserProfile.objects.get(pk=1)

    if request.method == "POST":
        form = AvatarUploadForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = AvatarUploadForm()
    return render(request, 'avatar_upload.html', {'form': form})