# Crea una clase llamada Rectangulo con atributos ancho y altura. Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro. 

class Rectangulo():
    def __init__(self,ancho,altura):
        self.ancho=ancho
        self.altura=altura
        
    def area(self):
        
        return self.ancho*self.altura
    
    def perimetro(self):
        return 2*(self.ancho+self.altura)

ancho=int(input("Introduzca el ancho del rectángulo"))
altura=int(input("Introduzca la altura del rectángulo"))

rectangulo=Rectangulo(ancho,altura)

print("El área del rectángulo es ",rectangulo.area()," y el perímetro es ",rectangulo.perimetro())
    