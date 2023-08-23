#   Jazmin Sanriago
#   Descripcion
#   22 DE FEBRERO DE 2023
#   HORA 8:21AM 

class Clase:
    def metodo(self):
        return 'Método normal', self

    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls

    @staticmethod
    def metodoestatico():
        return "Método estático"