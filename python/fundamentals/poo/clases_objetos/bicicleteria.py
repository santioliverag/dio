import re


class Bicicleta:
    def __init__(self, color, modelo, anio, precio):
        self.color = color
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f"{key}: {value}" for key, value in self.__dict__.items()])}'
    
    def tocar_bocina(self):
        print('biiiiiiip')

    def parar(self):
        print('parando la bicicleta')

    def correr(self):
        print('corriendo la bicicleta')

    def get_color(self):
        return self.color


    
b1 = Bicicleta("Rojo", "Caloi", 2022, 100000)

b1.tocar_bocina()
b1.parar()
b1.correr()
print(b1.get_color())

print(b1) #Llamando al metodo __str__


