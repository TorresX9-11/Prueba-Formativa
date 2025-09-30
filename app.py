from gestor import agregar_tarea, listar_tareas
# reemplaza tareas.append(...) por agregar_tarea(tareas, titulo)
# reemplaza '\n'.join(...) por '\n'.join(listar_tareas(tareas))
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

tareas = []

class ToDoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input = TextInput(hint_text='Escribe una tarea')
        self.boton = Button(text='Agregar tarea')
        self.boton.bind(on_press=self.agregar_tarea)
        self.resultado = Label(text='')

        self.layout.add_widget(self.input)
        self.layout.add_widget(self.boton)
        self.layout.add_widget(self.resultado)
        return self.layout

    def agregar_tarea(self, instance):
        titulo = self.input.text
        if titulo:
            agregar_tarea(tareas, titulo)
            self.resultado.text = '\n'.join(listar_tareas(tareas))
            self.input.text = ''

ToDoApp().run()