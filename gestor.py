def agregar_tarea(lista, titulo):
    lista.append({"titulo": titulo, "estado": "pendiente"})

def listar_tareas(lista):
    return [f"{i+1}. {t['titulo']} - {t['estado']}" for i, t in enumerate(lista)]

def completar_tarea(lista, indice):
    try:
        lista[indice]["estado"] = "completada"
    except IndexError:
        raise ValueError("Índice inválido")