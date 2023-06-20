#conjucion

print("conjuncion (and)")

num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El numero", num_uno, "cumple con la condicion.\n")
else:
    print("El numero", num_uno, "no cumple con la condicion.\n")


#disyuncion

print("disyuncion (or)")

palabra = input("Para cumplir con la condicion escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion no se ha cunplido.\n")


#negacion

print("negacion (not)")

numero_uno = int(input("Introduce un numero igual a 5: "))

if not numero_uno == 5:
    print("El numero es diferente a cinco, si cumple la condicion.")
else:
    print("El numero es igual a cinco y no cumple la condicion.")