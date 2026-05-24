from animal import Animal
class Gato(Animal):
    tamaniobigotes = str

    def __init__(self,persona,nombre,tamaniobigotes):
        super().__init__(persona,nombre)
        self.tamaniobigotes = tamaniobigotes


    def gettamaniobigotes(self):
        return self.tamaniobigotes

    def getnombre(self):
        return "polimorfismo " + self.nombre