from django.shortcuts import render

# Create your views here.
def shop(request):

    data = {
        
    }

    return render(request, 'pages/services/shop.html', data)

def single_s(request):

    data = {
        
    }

    return render(request, 'pages/service/single-shop.html', data)

def search(request):

    data = {
        
    }

    return render(request, 'pages/service/search_result.html', data)