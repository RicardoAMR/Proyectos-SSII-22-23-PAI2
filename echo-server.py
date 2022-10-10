import socket
import generadormac

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

clave = "patito"
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
                if codificado == mensaje[1]:
                    print("No ha habido modificacion")
                else:
                    print("Ha habido modificación")
            conn.sendall(data)