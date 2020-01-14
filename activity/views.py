from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def entry(request):
    if request.method != "POST":
        return HttpResponse("POST expected")
    
    ID = request.POST['id']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    time = request.POST['time']
    speed = request.POST['speed']
    vehicleInfo = request.POST['vehicleinfo']
        
    resp = "{}, {}, {}, {}, {}, {}".format(ID, latitude,
        longitude, time, speed, vehicleInfo)
    return HttpResponse(resp)


def detail(request):
    
    # if request.method != "POST":
    #     return HttpResponseRedirect("/detail/") 
    
    # ID = request.POST['id']
    # latitude = request.POST['latitude']
    # longitude = request.POST['longitude']
    # time = request.POST['time']
    # speed = request.POST['speed']
    # vehicleInfo = request.POST['vehicleinfo']
        
    # resp = "{}, {}, {}, {}, {}, {}".format(ID, latitude,
    #     longitude, time, speed, vehicleinfo)
    return HttpResponse("TODO")


