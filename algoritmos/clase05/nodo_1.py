#LISTA ENLAZADA DE FORMA LINEAL
#toda clase inicia con la primera letra en mayuscula, es una convencion
# un nodo esta relacionado con las estructuras de datos,
# es un elemento que contiene un valor y una referencia al siguiente nodo
class Nodo:
    valor = None
    siguiente = None
    def __init__(self, valor_parametro):
        self.valor = valor_parametro
        self.siguiente = None
    def saludo(self):
        print("hola")

nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
#nodo1.siguiente es una referencia al nodo2,
#es decir, nodo1 apunta a nodo2
#heredamos las propiedades(atributos,datos) y metodos del nodo2
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
print(nodo1.valor)
print(nodo1.siguiente.valor)
print(nodo2.siguiente.valor)