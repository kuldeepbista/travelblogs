from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def homepage(request):
	return render(request = request,
		template_name = 'main/blog.html',
		context = {'blogs':Blog.objects.all})
def portfoliopage(request):
	return render(request = request,
		template_name = 'main/blog.html',
		context = {'blogs':Blog.objects.all})
def contactpage(request):
	return render(request = request,
		template_name = 'main/blog.html',
		context = {'blogs':Blog.objects.all})

def blogpage(request):
	return render(request = request,
		template_name = 'main/blog.html',
		context = {'blogs':Blog.objects.all})
