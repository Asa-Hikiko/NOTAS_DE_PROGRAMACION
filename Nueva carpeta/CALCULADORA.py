print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. divicion entera")
print("6. exponente")
print("7. modulo o resto \n")

numero=int(input("elige cual quier opcion disponible: "))
if numero==1:
    print("elegiste la suma \n")
    numero=int(input("elige el primer numero: "))
    numero += int(input(" elige el segundo numero: "))
    print("El resultado de la suma es:",numero)
elif numero==2:
    print("elegiste la resta \n")
    numero=int(input("elige el primer numero: "))
    numero-= int(input(" elige el segundo numero: "))
    print("El resultado de la resta es:",numero)
elif numero==3:
    print("elegiste la multiplicacion \n")
    numero=int(input("elige el primer numero: "))
    numero*= int(input(" elige el segundo numero: "))
    print("El resultado de la multiplicacion es:",numero)

elif numero==4:
    print("elegiste la division \n")
    numero=float(input("elige el primer numero: "))
    numero/= float(input(" elige el segundo numero: "))
    print("El resultado de la divicion es:",round(numero,2))

elif numero==5:
    print("elegiste la divicion entera \n")
    numero=int(input("elige el primer numero: "))
    numero//= int(input(" elige el segundo numero: "))
    print("El resultado de la divicion estera es:",numero)

elif numero ==6:
    print("elegiste el exponente \n")
    numero=int(input("elige el primer numero: "))
    numero**= int(input(" elige el segundo numero: "))
    print("El resultado de el exponente es:",numero)

elif numero==7:
    print("elegiste el modulo o resto \n")
    numero=int(input("elige el primer numero: "))
    numero%= int(input(" elige el segundo numero: "))
    print("El resultado de el modulo o resto es:",numero)
else:
    print("la opcion escogida no existe ,intentalo  con otra opcion")