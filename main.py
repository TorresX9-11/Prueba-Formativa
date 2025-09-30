tareas = []

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título de la tarea: ")
        tareas.append({"titulo": titulo, "estado": "pendiente"})
        print("✅ Tarea agregada.")
    elif opcion == "2":
        print("\n📋 Lista de tareas:")
        for i, tarea in enumerate(tareas):
            print(f"{i+1}. {tarea['titulo']} - {tarea['estado']}")
    elif opcion == "3":
        print("👋 Saliendo...")
        break
    else:
        print("❌ Opción inválida.")