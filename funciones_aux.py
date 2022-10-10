#Imports:
import secrets
import random

# gen_nonce: 
# Función que genera un nonce
def gen_nonce():
    cod_nonce = secrets.token_urlsafe()
    return cod_nonce

# gen_transacciones: 
# Función que genera las transacciones de manera aleatoria, manteniendo la cuenta destino
def gen_transacciones():
    cuenta_Or   = random.randint(0,99999)
    cuenta_Dest = 65478
    cantidad    = random.randint(0,1000000)
    cadena = str(cuenta_Or) + "_" + str(cuenta_Dest) + "_" + str(cantidad)
    return cadena

# gen_prueba_random: 
# Función que según probabilidad, modifica la transacción
def gen_prueba_random(cadena):
    v = random.random()
    if(v > 0.65):
        x= cadena.split("_")
        x[2] = random.randint(0,1000000)
        cadena = x[0] + "_" + x[1] + "_" + str(x[2])
    return cadena

cad = gen_transacciones()
gen_prueba_random(cad)