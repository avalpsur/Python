# Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. Luego, crea clases derivadas como Piano y Guitarra 
# que hereden de InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.

class InstrumentoMusical():
    def __init__(self) -> None:
        pass
    
    def tocar(self):
        return()
    
class Piano(InstrumentoMusical):
    def __init__(self) -> None:
        pass
        
    def tocar(self):
        return "(sonido piano)"
    
class Guitarra(InstrumentoMusical):
    def __init__(self) -> None:
        pass
        
    def tocar(self):
        return "(sonido guitarra)"
    
    
gui=Guitarra()
pi=Piano()
print(pi.tocar())
print(gui.tocar())