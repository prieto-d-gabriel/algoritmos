intentos = 3

usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

while intentos > 0:
    if usuario == "admin" and contraseña == "1234":
        print("¡Inicio de sesión exitoso!")
        break
    else:
        intentos = intentos -1
        print(f"Credenciales incorrectas. Intento {intentos} de 3.")
        if intentos > 0:
            usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
        

