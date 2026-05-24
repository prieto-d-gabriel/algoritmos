
#BUSQUEDA POR INDICES

#REGLAS DE LA BUSQUEDA POR INDICES
#-DEBE SER UNICO
#INALTERABLE
#NO DEBE DE SER NULO (EN BLANCO)

#la busqueda por indices es un algoritmo de busqueda que
# recorre una lista de elementos utilizando sus indices 
#0,1,2,3,4,5...n-1
#la busqueda por indices consiste en poder convertir un indice en una clave 
# unica para poder acceder a un elemento de una lista de manera directa 
# sin necesidad de recorrer toda la lista.

#cada dato sera referenciado a traves de un indice unico 
empleados = [[1, "ana"], [2, "pedro"], [3, "maria"], [4, "juan"], [5, "luis"]]
sueldos =  [[1, 2000], [2, 3000], [3, 2500], [4, 3500], [5, 4000]]


indice_empleado = {}

for empleado in empleados:
    #empleado_i =1
    empleado_id=empleado[0]
    #nombre_empleado = "ana"
    nombre_empleado=empleado[1]

#aqui el primer indice creado viene a ser 1 y su valor viene a ser ana
    indice_empleado[empleado_id] = nombre_empleado

indice_sueldo = {}
for sueldo in sueldos:
    #sueldo_i = 1
    sueldo_id = sueldo[0]
    #monto_sueldo = 2000
    monto_sueldo = sueldo[1]

    indice_sueldo[sueldo_id] = monto_sueldo

def obtener_sueldo_empleado(empleado_id):
    print(indice_empleado[empleado_id])
    print(indice_sueldo[empleado_id])

obtener_sueldo_empleado(3)
    

