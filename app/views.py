from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.conf import settings

# Create your views here.

def file_upload(f):    
    #print("Archivo", f)
    #print("Ruta: ",settings.MEDIA_ROOT)
    #save_path = os.path.join(settings.MEDIA_ROOT, 'gep/', f)
    save_path = '{0}/{1}'.format(settings.MEDIA_ROOT, f)
    #print(save_path)
    
    path = default_storage.save(save_path, f)
    if path:
        print("ok")
    else:
        print("error")
    return f


def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html')


def blog(request):
    return render(request, 'app/blog.html')


def contact(request):
    return render(request, 'app/contact.html')


def hairstyle(request):
    return render(request, 'app/hairstyle.html')
