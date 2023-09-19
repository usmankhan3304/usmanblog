from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
def homePage(request):
    return render(request,"blogApp/index.html")

def posts(request):
    return render(request,"blogApp/all-posts.html")
def post_detials(request,slug):
   return render(request, 'blogApp/post-details-page.html')
   