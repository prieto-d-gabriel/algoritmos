class Person:
    nombres = ""
    apellido_paterno = ""
    apellido_materno = ""
    #constructor 
    # (metodo obligatorio que se tiene que ejecutar para poder crear un objeto)
    def __init__(self, nombres, apellido_paterno, apellido_materno):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

persona1 = Person("Juan", "Perez", "Gomez")
print(persona1.apellido_paterno)
