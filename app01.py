import socket
import time
print("Iniciando Programa")
s=socket.socket()
s.connect(("192.168.1.144",5038))

print("Manda Login")
s.send("Action:Login\n".encode())
s.send("Username:nova\n".encode())
s.send("Secret:1234\n".encode())
s.send("\n".encode())
time.sleep(8)

print("Mandado de Logoff")
s.send("Action: Logoff\n".encode())
s.send("\n".encode())

print("Fin de programa")