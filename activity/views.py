from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import accident, authority
from django.core import serializers
import json
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

    if 'id' in request.GET.keys():

        ID = request.GET['id']
        try:
            accidentData = accident.objects.filter(uid=ID)

            # TODO
            # return HTTP FILE FROM HERE

            data = serializers.serialize('json', accidentData)
            return HttpResponse(data, content_type='application/json')


        except Exception as e:
            raise e
            # return HttpResponse("Given accident data not found" + str(e))  #TODO remove printing of Error message
        


    else:
        return HttpResponse("Enter ID") 


@csrf_exempt
def getAccidentData(request):
    if 'id' in request.GET.keys()  :

        ID = request.GET['id']
        try:
            accidentData = accident.objects.filter(uid=ID)

            # if request.GET['type'] == "accX":
            #     pass
            # elif request.GET['type'] == "accY":
            #     pass
            # elif request.GET['type'] == "accZ":
            #     pass
            # elif request.GET['type'] == "rotX":
            #     pass
            # elif request.GET['type'] == "rotY":
            #     pass
            # elif request.GET['type'] == "rotZ":
            #     pass

            data = serializers.serialize('json', accidentData)
            return HttpResponse(json.dump('{"id":"aaa"}'), content_type='application/json')

            # TODO return encoded data from here 

        except Exception as e:
            raise e
        


    else:
        return HttpResponse("Enter ID") 