from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def handlemap(request):
    url = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBqqW5pq28Qera8ScOykfyKpiIP5Cc0XAM&callback=init"
    return render(request,'mappage.html', {'link':url})
