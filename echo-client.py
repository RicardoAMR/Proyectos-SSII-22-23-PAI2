import socket
import generadormac

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def comprobacion(user_input):
    try:
        if(int(user_input)):
            return True
    except ValueError:
        return False


clave = "patito"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    user_input1 = input("¿Qué mensaje deseas enviar? ")
    comprobacion(user_input1)
    mensaje = str(user_input1)
    codificado = generadormac.hmacFuncion(mensaje,clave)
    resultado = str(mensaje) + "~" + str(codificado)
    s.sendall(bytes(resultado, encoding='utf8'))
    data = s.recv(1024)

print(f"Received {data!r}")