import os
import socket
import generadormac
from datetime import datetime
import funciones_aux

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


file = open("./config.txt", "r")
config = []
for line in file:
    line = line.strip()
    words = line.split("=")
    config.append(words[1])
num_pruebas = config[0]
file.close()

clave = "patito"
archivo = "./log/" + str(datetime.now().strftime('%Y_%m'))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    for _ in range(int(num_pruebas)):
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    mensaje = str(data).replace("b'", "")
                    mensaje = mensaje.replace("'", "").split("~")
                    modificado = funciones_aux.gen_prueba_random(mensaje[0])
                    codificado = generadormac.hmacFuncion(modificado, clave)
                    file = open(archivo + ".txt", "a")
                    if codificado == mensaje[1]:
                        print("No ha habido modificacion")
                        file.write("Dia " + str(datetime.now().strftime('%d')) + " a las " + str(datetime.now(
                        ).strftime('%H:%M')) + ": ACIERTO - No se ha alterado ningun mensaje" + os.linesep)
                    else:
                        print("Ha habido modificación")
                        file.write("Dia " + str(datetime.now().strftime('%d')) + " a las " + str(
                            datetime.now().strftime('%H:%M')) + ": FALLO - Se ha alterado un mensaje" + os.linesep)
                    file.close()
                conn.sendall(data)

file = open(archivo + ".txt", "r")
cont = 0
for line in file:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == 'FALLO':
            cont = cont + 1
file.close()
file = open(archivo + ".txt", "a")
file.write("Han ocurrido un total de " + str(cont) + " fallos" + os.linesep + os.linesep)
file.close()
