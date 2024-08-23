from ..models import Variable

# https://docs.djangoproject.com/en/2.2/topics/db/queries/

# Django tiene varias funciones que permiten consultar en la base de datos con los modelos definidos
def get_variables():
    variables = Variable.objects.all()
    return variables

def get_variable(var_pk):
    variable = Variable.objects.get(pk=var_pk)
    return variable

def update_variable(var_pk, new_var):
    variable = get_variable(var_pk)
    variable.name = new_var['name']
    variable.save()
    return variable

def create_variable(new_var):
    variable = Variable(name=new_var['name'])
    variable.save()
    return variable
