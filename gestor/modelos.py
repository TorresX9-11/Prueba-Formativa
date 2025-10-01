# gestor/modelos.py

class Tarea:
    def __init__(self, id, titulo, estado="pendiente"):
        self.id = id
        self.titulo = titulo
        self.estado = estado

    def completar(self):
        self.estado = "completada"

    def __str__(self):
        return f"{self.id}. {self.titulo} - {self.estado}"


class Usuario:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)

    def listar_tareas(self):
        return [str(t) for t in self.tareas]

    def completar_tarea(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.completar()
                return True
        return False

    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]