from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
import requests

# Create your views here.
BASE_URL = 'https://fakestoreapi.com'

def index(request):
    response = requests.get(f"{BASE_URL}/products")
    data = {
        'data':response.json()
    }
    return render(request, 'index.html', data)



def LogOut(request):
    logout(request)
    return redirect('/')