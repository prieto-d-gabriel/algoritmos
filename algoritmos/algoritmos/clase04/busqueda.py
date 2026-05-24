#BUSQUEDA LINEAL
#la busqueda lineal es un algoritmo de busqueda que
#  recorre una lista de elementos uno por uno 
# hasta encontrar el elemento buscado o llegar al final de la lista.
usarios = ["ana", "pedro", "maria", "juan", "luis"]
encontrado=False

#foreach
for usuario in usarios:
    if usuario == "maria":
        encontrado = True
        print("Usuario encontrado: " + usuario)
        break

if encontrado == False:
    print("Usuario no encontrado.")