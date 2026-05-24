import time

intentos = 3

while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    while intentos > 0:
        if usuario == "admin" and contraseña == "1234":
            print("¡Inicio de sesión exitoso!")
            exit()
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

            if intentos > 0:
                usuario = input("Ingrese su nombre de usuario: ")
                contraseña = input("Ingrese su contraseña: ")

    # Cuando se quedan sin intentos
    print("Has agotado los intentos. Espera 2 minutos para reintentar...")

    tiempo_inicio = time.time()  # 21:00:00

    # Espera hasta que pasen 10 segundos

    while time.time() - tiempo_inicio < 10:
        pass  # espera activa (simple)

    print("Puedes intentar nuevamente.")
    intentos = 3