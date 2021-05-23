from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'astro/home.html')

def form(request):
    return render(request, 'astro/form.html')

def response(request):
    return render(request,'astro/response.html')    