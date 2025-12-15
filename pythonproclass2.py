import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Que longitud quieres que tenga la contrasena?"))

clave = ""

for i in range(length):
    simbolo = random.choice(caracteres)   
    clave += simbolo

print("La contrasena generada es", clave)  