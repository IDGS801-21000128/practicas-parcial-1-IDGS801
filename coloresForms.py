from wtforms import Form, StringField

class coloresForms(Form):
    b1 = StringField("b1")
    b2 = StringField("b2")
    b3 = StringField("b3")
    tol = StringField("tol")


class ColorConverter:
    def __init__(self):
        self.color_map1 = {
            '0': 'Negro',
            '1': 'Cafe',
            '2': 'Rojo',
            '3': 'Naranja',
            '4': 'Amarillo',
            '5': 'Verde',
            '6': 'Azul',
            '7': 'Violeta',
            '8': 'Gris',
            '9': 'Blanco'
        }

        self.color_map2 = {
            '1': 'Negro',
            '10': 'Cafe',
            '100': 'Rojo',
            '1000': 'Naranja',
            '10000': 'Amarillo',
            '100000': 'Verde',
            '1000000': 'Azul',
            '10000000': 'Violeta',
            '100000000': 'Gris',
            '1000000000': 'Blanco'
        }

        self.color_english = {
            'Negro': 'Black',
            'Cafe': 'Brown',
            'Rojo': 'Red',
            'Naranja': 'Orange',
            'Amarillo': 'Yellow',
            'Verde': 'Green',
            'Azul': 'Blue',
            'Violeta': 'Violet',
            'Gris': 'Gray',
            'Blanco': 'White'
        }

    def get_color(self, code, map_type):
        if map_type == 1:
            color_map = self.color_map1
        elif map_type == 2:
            color_map = self.color_map2
        else:
            raise ValueError("Invalid map type")

        return color_map.get(code, 'Desconocido')

    def get_english_color(self, color):
        return self.color_english.get(color, 'Desconocido')