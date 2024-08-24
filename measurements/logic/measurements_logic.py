from ..models import Measurement

from variables.logic.variables_logic import get_variable_by_name

def get_measurements():
    return Measurement.objects.all()

def get_measurement(measurement_id):
    return Measurement.objects.get(pk=measurement_id)

def create_measurement(new_measurement):
    variable = get_variable_by_name(new_measurement['variable'])

    measurement = Measurement(
        value=new_measurement['value'],
        unit=new_measurement['unit'],
        place=new_measurement['place'],
        variable=variable
    )

    measurement.save()
    return measurement

def update_measurement(pk: int, new_measurement):
    measurement = get_measurement(pk)

    measurement.value = new_measurement['value']
    measurement.unit = new_measurement['unit']
    measurement.place = new_measurement['place']
    measurement.variable = get_variable_by_name(new_measurement['variable'])

    measurement.save()

    return measurement

def delete_measurement(pk: int):
    measurement = Measurement.objects.get(pk=pk)
    measurement.delete()
