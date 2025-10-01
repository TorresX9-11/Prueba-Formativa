# ui/tareaitem.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty, NumericProperty
from kivy.app import App
from gestor.db import actualizar_tarea, eliminar_tarea, listar_tareas

class TareaItem(BoxLayout):
    id_tarea = NumericProperty()
    titulo = StringProperty()
    estado = StringProperty()

    def completar(self):
        actualizar_tarea(self.id_tarea, "completada")
        App.get_running_app().lista.actualizar_lista()
        App.get_running_app().mostrar_mensaje(f"✔️ Tarea {self.id_tarea} completada")

    def eliminar(self):
        eliminar_tarea(self.id_tarea)
        App.get_running_app().lista.actualizar_lista()
        App.get_running_app().mostrar_mensaje(f"🗑️ Tarea {self.id_tarea} eliminada")

class TareasView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actualizar_lista()

    def actualizar_lista(self):
        tareas = listar_tareas()
        self.data = [
            {
                'id_tarea': id,
                'titulo': titulo,
                'estado': estado
            } for id, titulo, estado in tareas
        ]