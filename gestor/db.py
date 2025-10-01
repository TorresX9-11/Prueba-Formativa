# gestor/db.py

import sqlite3

conexion = sqlite3.connect("data/tareas.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    estado TEXT NOT NULL
)
""")
conexion.commit()

def insertar_tarea(titulo):
    cursor.execute("INSERT INTO tareas (titulo, estado) VALUES (?, ?)", (titulo, "pendiente"))
    conexion.commit()

def listar_tareas():
    cursor.execute("SELECT id, titulo, estado FROM tareas")
    return cursor.fetchall()

def actualizar_tarea(id, nuevo_estado):
    cursor.execute("UPDATE tareas SET estado = ? WHERE id = ?", (nuevo_estado, id))
    conexion.commit()

def eliminar_tarea(id):
    cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conexion.commit()