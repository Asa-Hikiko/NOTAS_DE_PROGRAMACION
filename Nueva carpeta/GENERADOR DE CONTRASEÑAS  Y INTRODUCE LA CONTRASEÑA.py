# cofigo de chat gpt

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contrasena = int(input("Ingrese la longitud deseada para la contraseña: "))
contrasena_generada = generar_contrasena(longitud_contrasena)
print("Contraseña generada:", contrasena_generada)

# mi codigo con ayuda de chat gpt

# contrasena_generada=()

while True:
    x=input("introduce la contraseña: ")
    
    if x== contrasena_generada:
        print("contraseña correcta")
        print("***gracias por participar***")
        break
    else:
        print("contraseña incorrecta")