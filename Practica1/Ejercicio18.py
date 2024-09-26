# 18. Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la información del vehículo.
# Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.

class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        
    def imprimir(self):
        return self.marca," ",self.modelo


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tamaño):
        super().__init__(marca, modelo)
        self.tamaño=tamaño
    def pedalear(self):
        return
    def cambiarCadena(self):
        return
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo,cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada=cilindrada
        
    def acelerar(self):
        return
    
    def frenar(self):
        return
    
    def cambiarRueda(self):
        return