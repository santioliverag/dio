# Diccionarios es una coleccion de pares clave-valor

persona = {"nombre": "Santiago", "edad": 28}
persona = dict(nombre="Luciana", edad=30)

persona["telefono"]= "123456"

print(persona)

# Acceder a los valores

print(persona["nombre"])
print(persona.get("telefono"))
print(persona.get("telefono", "No tiene telefono"))

# Cambiar valores

persona["nombre"] = "Santi"
print(persona)

# Diccionarios anidados

persona_a = {
    "1": {"nombre": "Santiago", "edad": 28},
    "2": {"nombre": "Luciana", "edad": 30}
}

print(persona_a["1"]["edad"])

# Recorrer diccionarios
for clave, valor in persona_a.items():
    print(clave, valor)


#--------------
#  Claves
#--------------
print(persona_a.keys())
print(persona_a.values())
print(persona_a.items())



#--------------
#  Metodos clase dict
#--------------

frutas = {"nombre": "Naranja", "color": "Naranja"}

print(frutas)

frutas_copia = frutas.copy()
print(frutas)

frutas_copia.pop("color")
print(frutas_copia)

frutas_copia.popitem()
print(frutas_copia)

frutas_copia.clear()
print(frutas_copia)

frutas.fromkeys(["nombre", "color"], "pera")
print(frutas)

frutas.get("color")
print(frutas)

