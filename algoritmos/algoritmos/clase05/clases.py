 #creando una clase
#las clases son plantillas, moldes, el todo que consta
#de atributos y metodos, es decir, de caracteristicas y acciones
# atributo = dato 
# metodo = accion
class Persona:
    #atributos
    nombre = ""
    edad = 0
    profesion = ""

    #metodos
    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

#creando un objeto de la clase Persona
#un objeto es una instancia de una clase,
#es decir, una realizacion concreta de la clase
persona1 = Persona()
persona1.nombre = "Juan"
print(persona1.nombre)
#persona1.saludar()


