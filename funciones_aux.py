#Imports:
import secrets
import random

#Función generar nonce:
def gen_nonce():
    cod_nonce = secrets.token_urlsafe()
    return cod_nonce

#Función número pruebas aleatorias:
def gen_prueba_random(cadena):
    v = random.random()
    if(v > 0.65):
        x= cadena.split("_")
        x[2] = random.randint(0,1000000)
        cadena = x[0] + "_" + x[1] + "_" + str(x[2])
    return cadena

