#lista enlazada doblemente circular
#Lista doblemente enlazada
class NodoDoble():
    def __init__(self,nombre):
        self.nombre = nombre
        self.siguiente= None
        self.anterior = None 
#creamos variables del tipo objeto
juan = NodoDoble("Juan")
ana = NodoDoble("ana")
luis = NodoDoble("luis")

juan.siguiente = ana
ana.anterior = juan

ana.siguiente = luis
luis.anterior = ana

luis.siguiente = juan

#print(juan.siguiente.nombre)
#print(ana.anterior.nombre)
#mostramos el valor del nombre de un objetos anterior 
# de un objeto anterior
#print(luis.anterior.anterior.nombre)

print(luis.siguiente.nombre)

