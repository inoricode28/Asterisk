from asterisk.ami import AMIClient
from asterisk.ami import SimpleAction

def llamar_200(self):
        self.cliente.send_action(self.action)
        print("Ya di click")
cliente = AMIClient(address='192.168.1.144',port=5038)
cliente.login(username='nova',secret='1234')

action = SimpleAction(
        'Originate',
        Channel='SIP/200',
        Exten='445',
        Priority=1,
        Context='prueba',
        CallerID='Python',
    )

