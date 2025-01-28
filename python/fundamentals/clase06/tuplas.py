# tupla es tipo es tipo una constante. no cambia nunca

from enum import auto


frutas = ("Naranja", "Manzana", "Pera",)
letras = tuple("Curso de Python")
numeros = tuple([1,2,3,4,5])
pais = ("Brasil",)

print(letras)


#----------------
# Tuplas anidadas
#----------------

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz)
print(matriz[0][0])
print(matriz[2][2])


autos = ("gol", "celta", "uno", "palio")
for indice, auto in enumerate(autos):
    print(indice, auto)