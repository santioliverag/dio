#--------------
#  FOR
#--------------

texto = "Curso de Python"
VOCALES = "AEIOU"

for letra in texto:
    if letra.upper() in VOCALES:
        print(letra, end="")

else:
    print(letra)


RANGE = 10

for i in range(RANGE): #RANGE es el numero menos 1
    print(i)


#--------------
#  BUILT-IN
#--------------
for numero in range(0, 51, 5): # En este ejemplo es la tabla del 5. el primer numero arranca en 0 y el ultimo en 51 - 1 y se va contando de 5 en 5   
    print(numero, end=" ")


#-------------------------------------------------------------------

#----------------
#  WHILE
#----------------

contador = 0
opcion = -1

while opcion != 0:
    opcion = int(input("Ingrese un numero: "))

    if opcion == 1:
        contador += 1
        print("Aumento en 1")
    elif opcion == 2:
        contador += 2
        print("Aumento en 2")

print(contador)



#----------------
#  BREAK y CONTINUE
#----------------

contador = 0
opcion = -1

while True:
    opcion = int(input("Ingrese un numero: "))

    if opcion == 10:
        break
    else:
        contador += opcion

print(contador)

for i in range(100):
    if i == 10:
        break # Corta el ciclo
    elif i == 4:
        continue # Salta ese numero
    print(i)