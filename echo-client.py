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

mensajes = ["89439_43242_200","87123_65434_50","43534_54355_100","54352_98654_33","47784_23435_5",
            "80184_46371_900000","13234_76464_225","92487_99999_43","23433_12333_99","88888_65454_12",
            "90234_53635_23","54232_43599_20","98434_41312_666","12399_22645_66","12342_77854_88",
            "13435_55555_7","22143_24324_10","12334_99948_69","43238_98746_23","87543_98738_276",
            "14244_53425_11","92845_24222_56","54222_22222_90","52432_12322_776","24343_12322_90",
            "64352_12486_8","34633_98979_2"]

clave = "patito"
for mensaje in mensajes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        codificado = generadormac.hmacFuncion(mensaje,clave)
        resultado = mensaje + "~" + str(codificado)
        s.sendall(bytes(resultado, encoding='utf8'))
        data = s.recv(1024)

    print(f"Received {data!r}")