from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .logic import measurements_logic

import json

# Create your views here.
@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id:
            measurement = measurements_logic.get_measurement(id)
            measurement_dto = serializers.serialize('json', [measurement])

            return HttpResponse(measurement_dto, 'application/json')
        else:
            measurements = measurements_logic.get_measurements()
            measurements_dto = serializers.serialize('json', measurements)

            return HttpResponse(measurements_dto, 'application/json')

    if request.method == 'POST':
        print(request.body)
        print(json.loads(request.body))
        measurement = measurements_logic.create_measurement(json.loads(request.body))
        measurement_dto = serializers.serialize('json', [measurement])

        return HttpResponse(measurement_dto, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement = measurements_logic.get_measurement(pk)
        measurement_dto = serializers.serialize('json', [measurement])

        return HttpResponse(measurement_dto, 'application/json')

    if request.method == 'PUT':
        measurement = measurements_logic.update_measurement(pk, json.loads(request.body))
        measurement_dto = serializers.serialize('json', [measurement])

        return HttpResponse(measurement_dto, 'application/json')
    
    if request.method == 'DELETE':
        measurements_logic.delete_measurement(pk)
        return HttpResponse(status=204)
