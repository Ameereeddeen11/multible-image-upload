from django.shortcuts import render
from .models import MutipleImage

def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            image.user = request.user
            MutipleImage.objects.create(images=image)
    images = MutipleImage.objects.all()
    return render(request, "upload.html", {"images":images})