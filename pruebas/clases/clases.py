class MyClass:
    """aca va un docstring de lo que es o hace el objeto"""
    # Atributos -> variables de clase (son iguales para todas las instancias)
    villanos = []  # publico

    # Atributos -> variables de instancia (solo en una instancia hecha)
    def __init__(self, name='',
                 age=0):  # Asignar un valor por defecto(opcional)
        # la funcion __init__ es llamada automaticamente cuando
        # se crea un objeto nuevo, self hace referencia a esta clase.
        self.__name = name
        self.__age = age
        self.__enemy = []
        # toda variable que empieza con "__" es considerada privada no
        # obligatoriamente pero si por convension.

    # Metodos
    def __my_funcion_metodo(self):
        # para hacer los metodos del objeto
        print("hola, soy " + self.__name)

    # getters y setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def agregar_enemy(self, otro_enemy):
        """
        agregar un enemigo a la lista de enemigos propia de la instancia
        y tambien a la lista de villanos gloval
        """
        self.__enemy.append(otro_enemy)
        MyClass.villanos.append(otro_enemy)
        self.__my_funcion_metodo()

    # toString()
    def __str__(self):
        return "mi nombre es: ", self.get_name(), " y tengo: ", self.__age


"""programa principal"""
# se crea el objeto de la clase
obje = MyClass("john", 20)

# llamar a los atributos del objeto creado
# print(obje.__name) # en este caso no funciona porque es (privada) <--
# llamar mediante un metodo
print(obje.get_name())

# modificar un atributo directamente del objeto
# obje.__name = "Jorge" # en este caso no funciona porque es (privada) <--
# modificar mediante un metodo
obje.set_name("Jorge")

obje.agregar_enemy('uno')
obje.agregar_enemy('dos')
# llamar atributos de clase con el nombre de la clase y el atributo,
# esto si son publicos, si son privados, en la cell siguiente.
print(MyClass.villanos)
