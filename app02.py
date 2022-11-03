import socket
import time

def iniciar_ami(usuario,clave):    
    s.send("Action: Login\n".encode())
    comando = "Username: " + usuario + "\n"
    s.send(comando.encode())
    comando = "Secret: " + clave + "\n"
    s.send(comando.encode())
    s.send("\n".encode())

def finalizar_ami():
    s.send("Action: Logoff\n".encode())
    s.send("\n".encode())

print("Iniciando Programa")
s=socket.socket()
s.connect(("192.168.1.11",5038))

print("Iniciando Login")
iniciar_ami("Inori","1234")
time.sleep(8)
print("Mandando Logoff")
finalizar_ami()

print("Fin de programa")