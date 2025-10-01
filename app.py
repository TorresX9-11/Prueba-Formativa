# app.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from ui.tareaitem import TareasView
from gestor.db import insertar_tarea
from kivy.lang import Builder
from kivy.clock import Clock
from ui.tareaitem import TareaItem
from kivy.uix.label import Label
Builder.load_file("ui/tareaitem.kv")



class ToDoApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        entrada = BoxLayout(size_hint_y=None, height=50)
        self.input = TextInput(hint_text='Nueva tarea')
        boton = Button(text='Agregar')
        boton.bind(on_press=self.agregar_tarea)
        entrada.add_widget(self.input)
        entrada.add_widget(boton)

        self.lista = TareasView()
        self.mensaje = Label(text="", size_hint_y=None, height=30)

        root.add_widget(entrada)
        root.add_widget(self.mensaje)
        root.add_widget(self.lista)
        return root

    def agregar_tarea(self, instance):
        titulo = self.input.text.strip()
        if titulo:
            insertar_tarea(titulo)
            self.input.text = ''
            self.lista.actualizar_lista()
            self.mostrar_mensaje("✅ Tarea creada correctamente")

    def mostrar_mensaje(self, texto):
        self.mensaje.text = texto
        Clock.schedule_once(lambda dt: self.limpiar_mensaje(), 2.5)

    def limpiar_mensaje(self):
        self.mensaje.text = ""


if __name__ == "__main__":
    ToDoApp().run()