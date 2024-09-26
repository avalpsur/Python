# Crea una clase llamada Coche con atributos marca y modelo. Crea un método que imprima la información del coche en un formato legible.

class Coche():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        
    def imprimir(self):
        return "La marca del coche es ",self.marca," y el modelo ",self.modelo
    
coche=Coche("Seat","León")

print(coche.imprimir())