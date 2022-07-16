from django.shortcuts import render
from .models import Images

# Create your views here.

def home(request):
    if request.method == "POST":
        image = Images()
        image.images = request.FILES['upfile']
        if len(request.FILES['upfile'])!=0:
            image.save()
    img = Images.objects.all()
    return render(request, 'home.html',{'img':img})