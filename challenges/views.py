from django.shortcuts import render
from Django import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("crayz ahh message")
