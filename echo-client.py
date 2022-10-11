from http.client import ImproperConnectionState
import socket
import time
import generadormac
import funciones_aux

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def comprobacion(user_input):
    try:
        if (int(user_input)):
            return True
    except ValueError:
        return False


clave = "patito"

file = open("./config.txt", "r")
config = []
for line in file:
    line = line.strip()
    words = line.split("=")
    config.append(words[1])
num_pruebas = config[0]
file.close()
inicio = time.time()
for cont in range(int(num_pruebas)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        transferencia = funciones_aux.gen_transacciones()
        s.connect((HOST, PORT))
        hmac = generadormac.hmacFuncion(transferencia, clave)
        resultado = transferencia + "~" + str(hmac)
        s.sendall(bytes(resultado, encoding='utf8'))
        data = s.recv(1024)

    print(f"Received {data!r}")
fin = time.time()
print(fin-inicio)