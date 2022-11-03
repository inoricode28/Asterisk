import socket
import time
from tkinter  import *

def iniciar_ami(usuario,clave):    
    s.send("Action: Login\n".encode())
    comando = "Username: " + usuario + "\n"
    s.send(comando.encode())
    comando = "Secret: " + clave + "\n"
    s.send(comando.encode())
    s.send("\n".encode())


def llamar(numero):
    s.send("Action:Originate\n".encode())
    comando = "Channel:SIP/" + str(numero) + "\n"
    s.send(comando.encode())
    s.send("Contex:prueba\n".encode())
    s.send("Exten:445\n".encode())
    s.send("Priority:1\n".encode())
    s.send("\n".encode())


def finalizar_ami():
    s.send("Action: Logoff\n".encode())
    s.send("\n".encode())

def revisar():
    print("Ya di click")
    llamar(200)

s=socket.socket()
s.connect(("192.168.1.11",5038))
ventana = Tk()
ventana.geometry("380x300")
boton = Button(ventana,text="Llamar",command=revisar)
boton.pack()
ventana.mainloop()
"""
print("Iniciando Login")
iniciar_ami("Inori","1234")
llamar(200)
time.sleep(8)
print("MAndando Logoff")
finalizar_ami()
"""
print("Fin de programa")