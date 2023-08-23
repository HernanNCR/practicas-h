class Clase:
    @staticmethod
    def metodoestatico():
        return "Método estático"
mi_clase = Clase()
Clase.metodoestatico()
mi_clase.metodoestatico()

# 'Método estático'
# 'Método estático'