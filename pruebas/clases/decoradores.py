import math


class ClaseDecora:
    """Probando los metodos decoradores"""
    __villanos = 0

    def __init__(self, radio=1):
        self.__radio = radio

    # los metodos decoradores de clase
    @classmethod
    def un_metodo_de_clase(cls, nombre):
        """
        Este metodo es de clase, por ende, todas las clases acceden de igual
        manera como con las variables de clase.
        Esta funcion se puede llamar desde afuera, sin estanciar ningun
        objeto, con la sentencia ClaseDecora.un_metodo().
        """
        print(f'Hola {nombre}')

    @classmethod
    def metodo_de_clase_dos(cls):
        cls.__villanos += 1

    # los metodos decoradores static
    @staticmethod
    def saludo_static(nombre):
        """
        El metodo static me permite usarlo sin parametros de self o cls.
        Ademas de que:
        puede ser llamado como ClaseDecora.saludo_static()
        o instanciando un objeto de esta clase obje.saludo_static()
        """
        print(f'Bienvenido {nombre}')

    @staticmethod
    def get_villanos():
        print(f'{ClaseDecora.__villanos}')

    # los metodos decoradores property
    @property
    def area_circulo(self):
        return math.pi * (self.__radio ** 2)

    # @property
    # def radio(self):
    #     """
    #     lo comente para el otro ejemplo de property, pero asi tambien
    #     funca como el get_radio() hecho property
    #     """
    #     return self.__radio

    def get_radio(self):
        return self.__radio

    def set_radio(self, num):
        self.__radio = num

    radio = property(get_radio, set_radio)
    # x = property(get_name, set_name, __str__, 'docstring')
    # En este orden si o si.
    # Definiendo x como property, puedo hacer obj.x = 10 y es como hacer
    # un set() siempre y cuando este definido la funcion set()


# programa principal
# llamar a los metodos de (clase) llamando desde la clase y no desde un objeto
ClaseDecora.un_metodo_de_clase("Juan")
ClaseDecora.metodo_de_clase_dos()
# llamando desde un objeto
obje1 = ClaseDecora()
obje1.un_metodo_de_clase("jose")

# llamar a un metodo (static) desde su clase, y luego instanciando un objeto
ClaseDecora.get_villanos()
obje2 = ClaseDecora()
obje2.saludo_static("Miguel")

# llamar a un metodo (property) desde un objeto si o si, y sin (parentesis)
obje3 = ClaseDecora(5)
area = obje3.area_circulo   # desde el @property
print(area)
print(obje3.radio)
obje3.radio = 3             # desde el radio = property(get_radio, set_radio)
print(obje3.radio)          # desde el radio = property(get_radio, set_radio)
