from django.shortcuts import render

# Create your views here.

def home(request):
	title = "Index Home"
	return render(request, 'index.html', locals())