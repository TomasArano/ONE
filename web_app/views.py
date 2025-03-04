from django.shortcuts import render, HttpResponse
from .models import TextItem

# Create your views here.
def home(request):
    return render(request, 'home.html')

def TextItems(request):
    items = TextItem.objects.all()
    return render(request, 'Text-Items.html', {'TextItems': items})