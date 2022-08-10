class Vehiculo:
    def __init__(self, cantidad_puertas, cantidad_ruedas, motor='Diesel'):
        self._cant_puertas = cantidad_puertas
        self._cant_ruedas = cantidad_ruedas
        self.__motor = motor

    def get_motor(self):
        return self.__motor

    motor = property(get_motor)


class Transporte():
    def __init__(self, max_pasajeros, tipo='Público'):
        self.tipo = tipo
        self.cant_max_pasajero = max_pasajeros


class Auto(Vehiculo, Transporte):
    def __init__(self, marca, modelo, patente, tipo, pasajeros, puertas, ruedas, motor):
        super().__init__(puertas, ruedas, motor)
        Transporte.__init__(self, pasajeros, tipo)
        self.marca = marca
        self.modelo = modelo
        self.patente = patente

    def __str__(self):
        return f'Motor {self.motor}, cantidad puertas: {self._cant_puertas}, cantidad ruedas: {self._cant_ruedas}'


auto_nuevo = Auto('FIAT', "Cronos", 'AA588ZM', 'Particular', 5, 5, 4, 'Nafta')
print(auto_nuevo)
