# Set elimina los duplicados

numeros = set([1,2,3,1,2,3,4,5])
print(numeros)

letras = set("abacaxi")
print(letras)

autos = set(("palio","gol", "celta", "uno", "palio"))
print(autos)

lenguajes = {"python", "java", "python"}
print(lenguajes)

#-----------------------
# Conjuntos en python no aceptan indexacion, hay que convertir el set a una lista


numeros_1 = set([1,2,3,1,2,3,4,5])

numeros_1 = list(numeros_1)

print(numeros_1[2])


#-----------------------
# Iterar

autos_1 = {"palio","gol", "celta", "uno", "palio"}

for auto in autos_1:
    print(auto)


#-----------------------
# Enumerate

for indice, auto in enumerate(autos_1):
    print(indice, auto)

#--------------
# Metodos set
#--------------

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

conjunto_c = conjunto_a.intersection(conjunto_b)
print(conjunto_c)

conjunto_c = conjunto_a.difference(conjunto_b)
print(conjunto_c)

conjunto_c = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_c)

conjunto_c = conjunto_a.issubset(conjunto_b)
print(conjunto_c)

conjunto_c = conjunto_a.issuperset(conjunto_b)
print(conjunto_c)

conjunto_c = conjunto_a.isdisjoint(conjunto_b)
print(conjunto_c)

sorteo = {1, 23}

sorteo.add(2)
print(sorteo)

sorteo.remove(23)
print(sorteo)

sorteo.copy()

sorteo.discard(1)

sorteo.pop() #Saca de a uno desde la izquierda

sorteo.clear()


numeros_2 = set([1,2,3,4,5])
len(numeros_2)

1 in numeros_2
10 in numeros_2