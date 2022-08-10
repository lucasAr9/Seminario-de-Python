## Adivina adivinador....

import random

numero_aleatorio = random.randrange(101)
gane = False
intento = 1

print("Tenés 5 intentos para adivinar un entre 0 y 100")

while intento <= 5 and not gane:
    pedir_numero = int(input('Ingresa tu número: '))
    if pedir_numero == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmmm ... No.. ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
