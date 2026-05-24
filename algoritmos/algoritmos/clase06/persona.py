class Persona():
    idpersona = int
    nombre = str
    # constructor
    def __init__(self,nombre):
        self.nombre = nombre
        
    def getnombre(self):
        return self.nombre
  