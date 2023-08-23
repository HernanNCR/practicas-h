class Clase:
    @classmethod
    def metododeclase(cls):
        return 'Método de clase', cls

        Clase.metododeclase()
# ('Método de clase', __main__.Clase)

        mi_clase.metododeclase()
# ('Método de clase', __main__.Clase)