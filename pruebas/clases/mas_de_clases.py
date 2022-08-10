# superclase persona
class Persona:
    def __init__(self, fname, lname):
        self.__firstname = fname
        self.__lastname = lname

    # setters
    def set_firstname(self, otro):
        self.__firstname = otro

    def set_lastname(self, otro):
        self.__lastname = otro

    # toString() propio de la superclase
    def __str__(self):
        return f'{self.__firstname} {self.__lastname}'


# subclase de persona
class Student(Persona):
    # y sus propios atributos -> variables de clase
    __graduacion = 2019  # private y static

    def __init__(self, fname, lname, age):
        # La función __init__() de la hija anula la herencia de la función
        # __init__() de la superclase, por eso llamo al init.
        # Persona.__init__(self, fname, lname)

        # para eredar los atributos y metodos de la superclase se usa super
        super().__init__(fname, lname)

        # sus propio atributos -> variables de instancia
        self.__age = age

    def metodo_publica(self):  # public (se puede llamar de a fuera de la clase)
        self.__metodo_private()
        print('soy public', self.__age)

    def __metodo_private(self):  # private (solo se puede llamar desde la clase)
        print('soy private', self.__age)

    @staticmethod
    def get_graduacion():  # static
        return f'{Student.__graduacion}'

    @staticmethod
    def set_graduacion(numero):  # static
        Student.__graduacion = numero

    # toString() propio de la subclase
    def __str__(self):
        return f'{super().__str__()}, {self.__age}'


# programa principal
# le paso dos atributos de la superclase y uno de la clase hija
obje = Student("Mike", "Olsen", 90)
print(obje)                   # el toString de Student
print(obje.get_graduacion())  # el get de la variable de clase

# metodo para cambiar o agregar a la variable de clase
# como es de clase, si lo modifico en un objeto, lo modifico en todos
obje.set_graduacion(2020)     # el set de la variable de clase
print(obje.get_graduacion())  # el get de la variable de clase

# llamar a los metodos propios de la superclase
obje.set_firstname('otro')
obje.set_lastname('nombre')
print(obje)                   # el toString de Student

# llamar a un metodo publico que tiene un metodo privado dentro
obje.metodo_publica()
