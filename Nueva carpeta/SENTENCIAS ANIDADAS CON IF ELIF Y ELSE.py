print("menu de opciones: \n")
print("presiona 1 para convertir de numero a palabra.")
print("presiona 2 para convertir de palabra a numero. \n")

opcion=int(input("¿cual es tu opcion deseada?:"))

if opcion==1:
    print("\n conversor de numero a palabra. \n")
    
    opcion_uno=int(input("¿cual esel numero que desea convetir a palabra?: "))
    if   opcion_uno == 1:
        print("el numero es 'UNO' ")
    elif opcion_uno == 2:
        print("el numero es 'DOS' ")
    elif opcion_uno == 3:
        print("el numero es'TRES'")
    elif opcion_uno == 4:
        print("el numero es 'CUATRO'")
    else:
        print("el numero selecionado no esta registrado")



elif opcion== 2:
    
    print("\n conversor de palabra a numero . \n")
    
    opcion_dos=str(input("¿cual es la palabra que desea convertir a numero?:"))
    
    if opcion_dos== "uno":
        print("el numero es '1'")
    elif opcion_dos== "dos":
        print("el numero es '2'")
    elif opcion_dos== "tres":
        print("el numero es '3'")
    elif opcion_dos== "cuatro":
        print("el numero es '4'")
    elif opcion_dos== "cinco":
        print("el numero es '5'")
    else:
        print("el numero seleccionado no esta registrado")
        

else:
    print("opcion no disponible")
    
print("adios")