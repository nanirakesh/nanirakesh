from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def homepage(request):
	return render(request,'ht/homepage.html')

def lgn(re):
	return render(re,'ht/login.html')

def reg(rt):
	return render(rt,'ht/register.html')

def ree(request):
	return render(request,'ht/rg.html')

def home(request):
	return render(request,'ht/hhh.html')