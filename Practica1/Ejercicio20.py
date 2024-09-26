# 20. Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual que calcule el salario anual del empleado.
# Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y métodos específicos de cada tipo de empleado.

class Empleado():
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
        
    def calcularSalarioAnual(self):
        return self.salario*12
    
class Gerente(Empleado):
    def __init__(self, nombre, salario,empresa,oficina):
        super().__init__(nombre, salario)
        self.empresa=empresa
        self.oficina=oficina
        
        
    def cambiarOficina(self):
        self.oficina=input("Introduzca el nombre de la nueva oficina")
        return
    
class Programador(Empleado):
    def __init__(self, nombre, salario,puesto):
        super().__init__(nombre, salario)
        self.puesto=puesto
        
    def desarrollarPrograma(self):
        return
    
    def cambiarPuesto(self):
        self.puesto=input("Introduzca el nombre del nuevo puesto")
        return
    
    
    
pro=Programador("Lola",1800,"Frontend")
ge=Gerente("María",3200,"Burger King","Gran Plaza")

print(pro.calcularSalarioAnual())
print(ge.calcularSalarioAnual())

pro.cambiarPuesto()
print("El nuevo puesto de ",pro.nombre," es ",pro.puesto)

ge.cambiarOficina()
print("La nueva oficina de ",ge.nombre," es ",ge.oficina)