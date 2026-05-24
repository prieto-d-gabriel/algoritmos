# ==========================================
# PLAYLIST CIRCULAR
# SOLO AGREGAR Y ELIMINAR CANCIONES
# ==========================================

# Clase Cancion
class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

    def __str__(self):
        return f"{self.nombre} - {self.artista}"


# Clase Nodo
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None


# Clase PlaylistCircular
class PlaylistCircular:

    def __init__(self):
        self.ultimo = None


    # ==========================================
    # AGREGAR CANCIÓN
    # ==========================================
    def agregar_cancion(self, nombre, artista):

        # 1. Crear canción
        nueva_cancion = Cancion(nombre, artista)

        # 2. Crear nodo
        nuevo_nodo = Nodo(nueva_cancion)

        # CASO 1:
        # La lista está vacía
        if self.ultimo is None:

            # El nuevo nodo será el último
            self.ultimo = nuevo_nodo

            # El nodo apunta a sí mismo
            nuevo_nodo.siguiente = nuevo_nodo

        # CASO 2:
        # La lista ya tiene elementos
        else:

            # El nuevo nodo apunta al primero
            nuevo_nodo.siguiente = self.ultimo.siguiente

            # El último apunta al nuevo nodo
            self.ultimo.siguiente = nuevo_nodo

            # Actualizamos el último
            self.ultimo = nuevo_nodo

        print(f"✅ Canción agregada: {nombre}")


    # ==========================================
    # ELIMINAR CANCIÓN
    # ==========================================
    def eliminar_cancion(self, nombre):

        # Si la lista está vacía
        if self.ultimo is None:
            print("⚠️ Playlist vacía")
            return

        # Nodo actual
        actual = self.ultimo.siguiente

        # Nodo anterior
        anterior = self.ultimo

        while True:

            # Si encuentra la canción
            if actual.cancion.nombre.lower() == nombre.lower():

                # CASO 1:
                # Solo existe un nodo
                if actual == self.ultimo and actual == self.ultimo.siguiente:

                    self.ultimo = None

                # CASO 2:
                # Hay varios nodos
                else:

                    # Saltar el nodo eliminado
                    anterior.siguiente = actual.siguiente

                    # Si eliminamos el último
                    if actual == self.ultimo:
                        self.ultimo = anterior

                print(f"🗑️ Canción eliminada: {nombre}")
                return

            anterior = actual
            actual = actual.siguiente

            # Si regresamos al inicio
            if actual == self.ultimo.siguiente:
                break

        print("❌ Canción no encontrada")


    # ==========================================
    # MOSTRAR PLAYLIST
    # ==========================================
    def mostrar_playlist(self):

        if self.ultimo is None:
            print("⚠️ Playlist vacía")
            return

        print("\n🎵 PLAYLIST 🎵")

        temp = self.ultimo.siguiente

        while True:

            print(temp.cancion)

            temp = temp.siguiente

            if temp == self.ultimo.siguiente:
                break


# ==========================================
# PRUEBAS
# ==========================================

playlist = PlaylistCircular()

# Agregar canciones
playlist.agregar_cancion("Believer", "Imagine Dragons")
playlist.agregar_cancion("Viva La Vida", "Coldplay")
playlist.agregar_cancion("Halo", "Beyonce")

# Mostrar playlist
playlist.mostrar_playlist()

# Eliminar canción
playlist.eliminar_cancion("Viva La Vida")

# Mostrar nuevamente
playlist.mostrar_playlist()