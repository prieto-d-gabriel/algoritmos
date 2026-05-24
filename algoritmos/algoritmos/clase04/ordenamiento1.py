numeros = [2, 1,3,4]

#mostrar cantidad de elementos en la lista
cantidad= len(numeros)
#print(cantidad)


#ordenar de menor a mayor
for i in range(cantidad):

    for j in range(i +1 , cantidad):
        if numeros[i] > numeros[j]:
            #intercambiar
            numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)