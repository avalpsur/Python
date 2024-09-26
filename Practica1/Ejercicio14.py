# Crea una clase llamada CuentaBancaria con atributos titular y saldo. Agrega métodos para depositar y retirar dinero de la cuenta.  

class CuentaBancaria():
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
    
    def depositarDinero(self,importe):
        self.saldo+=importe
        
    def retirarDinero(self,importe):
        
        if self.saldo-importe < 0:
            print("No puedes sacar ", importe ," euros, estás tieso")
        else:
            self.saldo-=importe
            

cuenta=CuentaBancaria("Pepita",212)

cuenta.depositarDinero(100)
print(cuenta.saldo)

cuenta.retirarDinero(150)
print(cuenta.saldo)

cuenta.retirarDinero(195)
