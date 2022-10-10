import os
import socket
import generadormac
import datetime

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

clave = "patito"
archivo = "./log/" + str(datetime.now().strftime('%Y_%m'))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                mensaje = str(data).replace("b'","")
                mensaje = mensaje.replace("'","").split("~")
                codificado = generadormac.hmacFuncion(mensaje[0],clave)
                user_input1 = input("Escribe algo si deseas una intercepción simulada, si no dale a intro ")
                mensaje[1] = mensaje[1]+str(user_input1)
                file = open(archivo + ".txt", "a")
                if codificado == mensaje[1]:
                    print("No ha habido modificacion")
                    file.write("Día " + str(datetime.now().strftime('%d')) + " a las " + str(datetime.now().strftime('%H:%M')) + ": ACIERTO - No se ha alterado ningún mensaje" + os.linesep)
                else:
                    print("Ha habido modificación")
                    file.write("Día " + str(datetime.now().strftime('%d')) + " a las " + str(datetime.now().strftime('%H:%M')) + ": FALLO - Se ha alterado un mensaje" + os.linesep)
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
file.write(os.linesep + "Han ocurrido un total de " + str(cont) + " fallos")
file.close()