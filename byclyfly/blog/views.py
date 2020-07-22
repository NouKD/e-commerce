from django.shortcuts import render

# Create your views here.

def blog(request):

    data = {
        
    }

    return render(request, 'pages/blog/news.html', data)

def single(request):

    data = {
        
    }

    return render(request, 'pages/blog/single-news.html', data)