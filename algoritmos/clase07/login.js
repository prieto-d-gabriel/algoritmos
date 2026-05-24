function ejecutar() {
    let intentos = 3;
    let usuario = document.getElementById("txtUsuario").value;
    let password = document.getElementById("txtPassword").value;
    if (usuario === "admin" && password === "1234") {
        alert("Bienvenido al sistema");
    } else {
        intentos = intentos - 1;
        alert("Usuario o contraseña incorrecta. Intentos restantes: " + intentos);
    }

}