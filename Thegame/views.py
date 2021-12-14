from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,"index.html")

def start(request):
    return render(request,"hangman.html")

def aboutus(request):
    return render(request,"aboutus.html")