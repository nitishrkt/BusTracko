from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from geopy.geocoders import GoogleV3
# Create your views here.
def handlemap(request): 
    print("its working")
    if request.method == 'POST':
        from_place = request.POST['from']
        to = request.POST['to']
        geolocator = GoogleV3()
        location = geolocator.geocode(from_place)
        from_lat = location.latitude
        from_lon = location.longitude 
        location_to = geolocator.geocode(to)
        to_lat = location_to.latitude
        to_lon = location_to.longitude
        return render(request,{'from_lat':from_lat, 'from_lon':from_lon, 'to_lat':to_lat, 'to_lon':to_lon},'mappage.html')
