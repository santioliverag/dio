nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')

print(nombre, apellido)
print(nombre, apellido, end="... \n") #por padron es un salto de linea
print(nombre, apellido, sep="/")

print(nombre, apellido, sep="#", end="...\n")