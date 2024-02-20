from wtforms import Form
from wtforms import IntegerField, StringField, RadioField
from wtforms import validators

class filedsForm(Form):
    x1 = IntegerField('x1')
    y1 = IntegerField('y1')
    x2 = IntegerField('x2')
    y2 = IntegerField('y2')



class fieldsTraduccion(Form):
    ingles = StringField('Ingles', [
        validators.DataRequired(message='El campo es requerido')
    ])
    espanol = StringField('Espanol', [
        validators.DataRequired(message='El campo es requerido')
    ])
    

class searchTraduction(Form):
    idioma = RadioField('Idioma', choices=[('Ingles', 'Ingles'), ('Español', 'Español')])
    busqueda = StringField('Busqueda',[
        validators.DataRequired(message='El campo busqueda es requerido')
    ])
