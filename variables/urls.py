from django.contrib import admin
from django.urls import path
from . import views


"""
GET, POST
/variables/ 
"""
urlpatterns = [
  path('', views.variables_view, name='variables_view'),
  path('<int:pk>', views.variable_view, name='variable_view')
]
