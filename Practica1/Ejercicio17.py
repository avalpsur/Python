# 17. Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura. 
# Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica y sobrescriban el método area para calcular 
# el área específica de cada figura.

class FiguraGeometrica():
    def __init__(self,ancho,altura):
        self.ancho=ancho
        self.altura=altura
        
    def area(self):
        return


class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, altura):
        super().__init__(ancho, altura)
    
    def area(self):
        area=self.ancho*self.altura
        return area
    
class Triangulo(FiguraGeometrica):
    def __init__(self, ancho, altura):
        super().__init__(ancho, altura)
    
    def area(self):
        area=(self.ancho*self.altura)/2
        return area
    
    
rectangulo=Rectangulo(2,4)
triangulo=Triangulo(5,9)

print("El área del rectángulo es ",rectangulo.area())
print("El área del triángulo es ",triangulo.area())