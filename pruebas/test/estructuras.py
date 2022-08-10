class CadenaInvertida:
    def __init__(self, cadena):
        self._cadena = cadena
        self._posicion = len(cadena) - 1

    def __iter__(self):
        return (self)

    def __next__(self):
        if self._posicion == -1:
            raise (StopIteration)
        elem = self._cadena[self._posicion]
        self._posicion = self._posicion - 1
        return (elem)

    def es_vacia(self):
        return len(self._cadena) == 0

    def elemento(self):
        return self._cadena[self._posicion]


clase = CadenaInvertida("Python")
cad = ""
for car in clase:
    cad += car

print(cad)
