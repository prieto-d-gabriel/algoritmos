class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

    def __str__(self):
        return f"{self.nombre} - {self.artista}"


class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None


class PlaylistCircular:
    def __init__(self):
        self.ultimo = None
        self.actual = None

    # Agregar canción al final
    def agregar_cancion(self, nombre, artista):
        nueva_cancion = Cancion(nombre, artista)
        nuevo_nodo = Nodo(nueva_cancion)

        # Si la lista está vacía
        if self.ultimo is None:
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            self.actual = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.ultimo.siguiente
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

        print(f"✅ Canción agregada: {nombre}")

    # Mostrar toda la playlist
    def mostrar_playlist(self):
        if self.ultimo is None:
            print("⚠️ La playlist está vacía")
            return

        print("\n🎵 PLAYLIST 🎵")

        temp = self.ultimo.siguiente
        contador = 1

        while True:
            print(f"{contador}. {temp.cancion}")
            contador += 1
            temp = temp.siguiente

            if temp == self.ultimo.siguiente:
                break

    # Mostrar canción actual
    def mostrar_actual(self):
        if self.actual is None:
            print("⚠️ No hay canciones")
        else:
            print(f"\n▶️ Reproduciendo: {self.actual.cancion}")

    # Pasar a la siguiente canción
    def siguiente_cancion(self):
        if self.actual is None:
            print("⚠️ No hay canciones")
        else:
            self.actual = self.actual.siguiente
            self.mostrar_actual()

    # Buscar canción
    def buscar_cancion(self, nombre):
        if self.ultimo is None:
            print("⚠️ Playlist vacía")
            return

        temp = self.ultimo.siguiente

        while True:
            if temp.cancion.nombre.lower() == nombre.lower():
                print(f"✅ Canción encontrada: {temp.cancion}")
                return

            temp = temp.siguiente

            if temp == self.ultimo.siguiente:
                break

        print("❌ Canción no encontrada")

    # Eliminar canción
    def eliminar_cancion(self, nombre):
        if self.ultimo is None:
            print("⚠️ Playlist vacía")
            return

        actual = self.ultimo.siguiente
        anterior = self.ultimo

        while True:

            # Si encontró la canción
            if actual.cancion.nombre.lower() == nombre.lower():

                # Caso: solo un nodo
                if actual == self.ultimo and actual == self.ultimo.siguiente:
                    self.ultimo = None
                    self.actual = None

                # Caso: eliminar último
                else:
                    anterior.siguiente = actual.siguiente

                    if actual == self.ultimo:
                        self.ultimo = anterior

                    if self.actual == actual:
                        self.actual = actual.siguiente

                print(f"🗑️ Canción eliminada: {nombre}")
                return

            anterior = actual
            actual = actual.siguiente

            if actual == self.ultimo.siguiente:
                break

        print("❌ Canción no encontrada")


# =========================
# PRUEBA DEL PROGRAMA
# =========================

playlist = PlaylistCircular()

playlist.agregar_cancion("Believer", "Imagine Dragons")
playlist.agregar_cancion("Blinding Lights", "The Weeknd")
playlist.agregar_cancion("Viva La Vida", "Coldplay")

playlist.mostrar_playlist()

playlist.mostrar_actual()

playlist.siguiente_cancion()
playlist.siguiente_cancion()
playlist.siguiente_cancion()  # vuelve al inicio automáticamente

playlist.buscar_cancion("Viva La Vida")

playlist.eliminar_cancion("Blinding Lights")

playlist.mostrar_playlist()