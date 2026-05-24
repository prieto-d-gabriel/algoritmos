class Animal():
    idanimal = int
    nombre = str
    persona = object

    # constructor
    def __init__(self,persona,nombre):
        self.persona = persona
        self.nombre = nombre

    def getnombre(self):
        return self.nombre