MAYOR_EDAD = 18
edad = int(input("Ingrese su edad: "))

if edad > MAYOR_EDAD:
    print("Es mayor de edad")
elif edad == MAYOR_EDAD:
    print("Tienes la mayoria de edad")
else:
    print("Es menor de edad")


#----------------
#  IF TERNARIO
#----------------

staus = "Activo" if edad >= MAYOR_EDAD else "Inactivo"
print(staus)