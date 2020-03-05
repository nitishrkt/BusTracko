from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def handlemap(request):
    if request.method == 'POST':
        from_place = request.POST['from']
        to = request.POST['to']
        print("from = "+from_place+" to = "+ to)
        return render(request,{'from':from_place, 'to':to},'mappage2.html')
