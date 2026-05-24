from persona import Persona
from animal import Animal
from gato import Gato
#if __name__ == "__main__":

    # creando el objeto
persona1 = Persona("anthony")
print(persona1.getnombre())

animal1 = Animal(persona1,"miau")
print(animal1.getnombre())
print(animal1.persona.getnombre())

gato1 = Gato(persona1,"miau","20")
print(gato1.getnombre())
print(gato1.persona.getnombre())