#0-12  = Reprobado
# 13-16 = Aprobado
# 17-20 = Excelente 
#tambien conocido como if anidado o if encadenado
nota = int(input("Ingrese la nota del estudiante: "))
if nota >= 0 and nota <= 12:
    print("Reprobado")
elif nota >= 13 and nota <= 16:
    print("Aprobado")
elif nota >= 17 and nota <= 20:
    print("Excelente")