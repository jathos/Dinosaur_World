from django.shortcuts import render
from .models import dinosaurs

def home(request):
    return render(request, 'home.html', { 'dinosaurs': dinosaurs})
