saldo = 1000
saque = 200
limite = 100
cuenta_especial = True
contactos_emergencia = []

print(saldo >= saque and saque <= limite) #las 2 tienen que ser true para ser true
print(saldo >= saque or saque <= limite) #una de las 2 tiene que ser true, para que sea falso las 2 tienen que ser falsas

#-------------
# NOT
#-------------
print(not 1000 > 1500)
print(not contactos_emergencia) #si la lista esta vacia es true ya que esta negando
print(not "saque 1500;") 
print(not "") #true ya que esta negand

#-------------
# PARENTESIS
#-------------
print((saldo >= saque and saque <= limite) or (cuenta_especial and saldo >= saque))

#-------------
# IN
#-------------
contactos_emergencia = ["Maria", "Pedro"]
print("Maria" in contactos_emergencia)
print("Maria" not in contactos_emergencia)


#-------------
# TABLAS DE VERDAD
#-------------

#AND = Para ser True todo tiene que ser true, si uno es false todo es false
#OR = Para ser False todo tiene que ser false, si uno es true todo es true

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

print(not True) #False
print(not False) #True