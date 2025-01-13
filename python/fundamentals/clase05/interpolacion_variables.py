nombre = "Santiago"
edad = 28
cargo = "Desarrollador"
lenguaje = "Python"

datos = {"nombre": "Santiago", "edad": 28, "cargo": "Desarrollador", "lenguaje": "Python"}
#--------------
#  Antigua manera (%)
#--------------
print ("Hola, me llamo %s, tengo %d y soy %s usando %s" % (nombre, edad, cargo, lenguaje))

#--------------
#  Format
#--------------
print("Hola, me llamo {}, tengo {} y soy {} usando {}".format(nombre, edad, cargo, lenguaje))
print("Hola, me llamo {3}, tengo {2} y soy {1} usando {0}".format(edad, cargo, lenguaje, nombre))
print("Hola, me llamo {nombre}, tengo {edad} y soy {cargo} usando {lenguaje}".format(nombre=nombre, edad=edad, cargo=cargo, lenguaje=lenguaje))
print("Hola, me llamo {nombre}, tengo {edad} y soy {cargo} usando {lenguaje}".format(**datos))

#--------------
#  F-String
#--------------
print(f"Hola, me llamo {nombre}, tengo {edad} y soy {cargo} usando {lenguaje}")

PI = 3.14159

print(f"El valor de PI es {PI}")
print(f"El valor de PI es {PI:.2f}")
print(f"El valor de PI es {PI:10.2f}")