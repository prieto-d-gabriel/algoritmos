#busqueda_lineal
numeros = [1, 2, 3, 4, 5]

# % signo de residuo, devuelve el residuo de la division entre dos numeros
# modulo  - mod 
for n in numeros:
    residuo = n % 2
    if residuo == 0:
        print("el numero " + str(n) + " es par")
    else:
        print("el numero " + str(n) + " es impar")