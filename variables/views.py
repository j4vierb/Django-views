from django.shortcuts import render
from django.http import HttpResponse

from .logic import variables_logic
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

# hacer peticiones sin el token de seguridad
@csrf_exempt
def variables_view(request):
  if request.method == 'GET':
    # obtener el query parameter
    id = request.GET.get('id', None)
    if id:
      variable_dto = variables_logic.get_variable(id)
      variable = serializers.serialize('json', [variable_dto])
      return HttpResponse(variable, 'application/json')
    else:
      variables_dto = variables_logic.get_variables()
      variables = serializers.serialize('json', variables_dto)
      return HttpResponse(variables, 'application/json')
  
  if request.method == 'POST':
    # donde se hacen las validaciones?
    variable_dto = variables_logic.create_variable(json.loads(request.body))
    variable = serializers.serialize('json', [variable_dto])
    return HttpResponse(variable, 'application/json')

@csrf_exempt
def variable_view(request, pk):
  if request.method == 'GET':
    variable_dto = variables_logic.get_variable(pk)
    variable = serializers.serialize('json', [variable_dto])
    return HttpResponse(variable, 'application/json')
  
  if request.method == 'PUT':
    variable_dto = variables_logic.update_variable(pk, json.loads(request.body))
    variable = serializers.serialize('json', [variable_dto])

    return HttpResponse(variable, 'application/json')
  
  if request.method == 'DELETE':
    variables_logic.delete_variable(pk)
    return HttpResponse(status=204)
