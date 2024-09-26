# Crea una clase llamada Estudiante con atributos nombre, edad y curso. Crea varios objetos de tipo Estudiante y almacénalos en una lista. 
# Luego, itera sobre la lista e imprime la información de cada estudiante

class Estudiante():
    def __init__(self,nombre,edad,curso):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso
        
        
estudiante1=Estudiante("Mohcen",23,"1º Primaria")
estudiante2=Estudiante("Álvaro",24,"2º DAW")
estudiante3=Estudiante("Lara",25,"2º ASIR")

lista=[estudiante1,estudiante2,estudiante3]

for i in lista:
    print(i.nombre,", ",i.edad,", ",i.curso)
        