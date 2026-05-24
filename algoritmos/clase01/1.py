# print("Hello, World!")
##########################################################################################
#ESTRUCTURAS DE CONTROL (ALGORITMOS) para el manejo de datos
# estructura condicional simple

# age = input("¿Cuál es tu edad? ")
# age = int(age)
# if age >= 18:
#     print("Eres mayor de edad")

# estructura condicional repetitiva

# current_value= 1
# while current_value <= 5:
#     print(current_value)
#     current_value += 1 

# for value in range(1,6):
#     print(value)
####################################################################################
#  ESTRUCTURA PARA ALMACENAR DATOS
# estructura lineal
#arreglo
#numeros = [10, 20, 30, 40, 50]
#print(numeros[0])
#for numero in numeros:
    #print(numero)

#listas
# frutas = ["manzana", "banana", "naranja"]
# print(frutas[0])

#tuplas
# coordenadas = (10, 20)
# print(coordenadas[0])

#estructura no lineal
#arboles
papa = {
    "juan": 20,
    "pedro": [
        {
            "maria": 10,
            "pepe": ["abigail", "jose"]
        },
        {
            "valor": 15,
            "hijos": []
        }
    ]
}
# print(papa["pedro"][0]["pepe"][0])  # Imprime "jose"

organigrama = {
    "GERENCIA MUNICIPAL METROPOLITANA": [
        {
            "GERENCIA DE COMUNICACIÓN SOCIAL Y RELACIONES PUBLICAS": [
                "SUBGERENCIA DE EVENTOS Y PROTOCOLO",
                "SUBGERENCIA DE PRENSA Y COMUNICACIONES"
            ]
        },
        {
            "GERENCIA DE DEFENSA DEL CIUDADANO": [
                "PROGRAMA DE DEFENSA MUNICIPAL DE VÍCTIMAS DE ACCIDENTES DE TRÁNSITO"
            ]
        },
        {
            "GERENCIA DE ADMINISTRACIÓN": [
                "SUBGERENCIA DE PERSONAL",
                "SUBGERENCIA DE LOGÍSTICA CORPORATIVA",
                "SUBGERENCIA DE SERVICIOS GENERALES",
                "SUBGERENCIA DE GOBIERNO DIGITAL E INNOVACIÓN"
            ]
        },
        {
            "GERENCIA DE FINANZAS": [
                "SUBGERENCIA DE PLANEAMIENTO FINANCIERO CORPORATIVO",
                "SUBGERENCIA DE PRESUPUESTO",
                "SUBGERENCIA DE TESORERÍA",
                "SUBGERENCIA DE CONTABILIDAD"
            ]
        },
        {
            "PROCURADURÍA PÚBLICA MUNICIPAL": []
        },
        {
            "GERENCIA DE ASUNTOS JURÍDICOS": []
        },
        {
            "GERENCIA DE PLANIFICACIÓN": [
                "SUBGERENCIA DE PLANEAMIENTO CORPORATIVO",
                "SUBGERENCIA DE PROGRAMACIÓN MULTIANUAL DE INVERSIONES",
                "SUBGERENCIA DE ORGANIZACIÓN Y MODERNIZACIÓN",
                "SUBGERENCIA DE COOPERACIÓN TÉCNICA INTERNACIONAL"
            ]
        }
    ]
}
print(organigrama["GERENCIA MUNICIPAL METROPOLITANA"][0]["GERENCIA DE COMUNICACIÓN SOCIAL Y RELACIONES PUBLICAS"][0])