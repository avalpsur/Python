# Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico. Luego, crea dos clases derivadas, Perro y Gato, 
# que hereden de Animal y sobrescriban el método hablar para imprimir mensajes diferentes. 

class Animal():
    def __init__(self,nombre):
       self.nombre=nombre
    
    def hablar(self):
        return "Tengo hambre"

class Perro(Animal):
    def __init__(self,nombre):
        self.nombre=nombre
    
    def hablar(self):
        return "GUAU"
    
class Gato(Animal):
    def __init__(self, nombre):
        self.nombre=nombre
    
    def hablar(self):
        return "MIAU"
        

perrete=Perro("Toby")
gatete=Gato("Misifú")

print(perrete.hablar())
print(gatete.hablar())