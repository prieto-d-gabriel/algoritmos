numeros = [5, 2, 9, 1, 7]
#print("Números ordenados:", sorted(numeros))
# #mayor a menor
#print("Números ordenados:", sorted(numeros, reverse=True))
# #de menor a mayor
# print("Números ordenados:", sorted(numeros))
########################################################################################

cantidad= len(numeros) #devuelve el numero de elementos de la lista
# print("Cantidad de números:", cantidad)

# for i in range(cantidad):
#     print("Número en la posición", i, "es:", numeros[i])

# for i in range(len(numeros)):
#     for j in range(i +1, len(numeros)):
#         print("elementos a comparar:", numeros[i], numeros[j])

#aca si no se pone +1 comparara el ultimo elemento consigo mismo
# for i in range(len(numeros)):
#     for j in range(i , len(numeros)):
#         print("elementos a comparar:", numeros[i], numeros[j])

#de menor a mayoR
#recorre la lista de elementos 
for i in range(len(numeros)):
    #recorremos la lista de los elementos pero a partir del elemento i 
    # si los elementos son 4321 entonces el primer elemento es 4 y el segundo elemento es 3, 
    # entonces 4 es mayor que 3 por lo tanto se intercambian de posición y así sucesivamente
    #  hasta ordenar la lista completa
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print("Números ordenados:", numeros)

