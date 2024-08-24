from . import views
from django.urls import path

urlpatterns = [
  path('', views.measurements_view, name='measurements_view'),
  path('<int:pk>', views.measurement_view, name='measurement_view'),
]
