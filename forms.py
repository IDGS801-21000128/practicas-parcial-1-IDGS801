from wtforms import Form
from wtforms import IntegerField

class filedsForm(Form):
    x1 = IntegerField('x1')
    y1 = IntegerField('y1')
    x2 = IntegerField('x2')
    y2 = IntegerField('y2')