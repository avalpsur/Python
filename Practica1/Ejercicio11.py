#Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.

class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad


persona1=Persona("Pepe","25")
print(persona1.nombre,persona1.edad)
