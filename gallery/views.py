from django.shortcuts import render
from django.http import HttpResponse,Http404
from gallery.models import Category,Image,Location

# Create your views here.

def home(request):
    # import pdb; pdb.set_trace()
    return  render(request, 'all/dashboard.html')

def about(request):
    return  render(request, 'all/about.html')  

def images(request):
    images= Image.objects.all()
    categories= Category.objects.all()
    location= Location.objects.all()
    return render(request, 'all/images.html',locals())

def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get("image")
        search_images=Image.search_by_category(search_term)
        message=f"{search_term}"
        
        return render(request, 'all/images.html', {"message":message, "images": search_images})
    
    else:
        message="You haven't  searched for any term"
        return render(request, 'all/images.html',{"message": message})