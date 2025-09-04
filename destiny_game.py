import json
import os

# Diccionario con números para cada emoción en cada nivel (6 niveles, 6 emociones por nivel)
# Esta es una estructura de ejemplo con números ficticios pero siguiendo la idea del árbol
numeros_por_nivel = [
    {  # Nivel 1
        'positiva': 44,
        'negativa': 13,
        'desinteres': 34,
        'enfado': 9,
        'tristeza': 22,
        'silencio': 35,
    },
    {  # Nivel 2
        'positiva': 50,
        'negativa': 13,
        'desinteres': 30,
        'enfado': 5,
        'tristeza': 14,
        'silencio': 38,
    },
    {  # Nivel 3
        'positiva': 47,
        'negativa': 10,
        'desinteres': 21,
        'enfado': 3,
        'tristeza': 12,
        'silencio': 40,
    },
    {  # Nivel 4
        'positiva': 52,
        'negativa': 8,
        'desinteres': 27,
        'enfado': 6,
        'tristeza': 13,
        'silencio': 41,
    },
    {  # Nivel 5
        'positiva': 49,
        'negativa': 12,
        'desinteres': 29,
        'enfado': 4,
        'tristeza': 15,
        'silencio': 39,
    },
    {  # Nivel 6
        'positiva': 51,
        'negativa': 11,
        'desinteres': 28,
        'enfado': 7,
        'tristeza': 16,
        'silencio': 42,
    },
]

emociones_disponibles = ['positiva', 'negativa', 'desinteres', 'enfado', 'tristeza', 'silencio']

# Ruta donde guardaremos los JSON (puedes cambiar)
RUTAS_DIR = "rutas_emocionales"

def guardar_ruta_json(ruta_emocional, numero_predicho):
    if not os.path.exists(RUTAS_DIR):
        os.makedirs(RUTAS_DIR)
    
    # Nombre único con índice
    archivos = os.listdir(RUTAS_DIR)
    nombre_archivo = f"ruta_{len(archivos) + 1}.json"
    ruta_completa = os.path.join(RUTAS_DIR, nombre_archivo)

    datos = {
        "ruta_emocional": ruta_emocional,
        "numero_predicho": numero_predicho
    }
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def main():
    print("Bienvenido al 'Magia Emocional' ✨")
    ruta = []
    suma_numeros = 0
    
    for nivel in range(6):
        print(f"\nNivel {nivel + 1}: ¿Cómo te sientes? Elige una emoción:")
        for i, emo in enumerate(emociones_disponibles, 1):
            print(f"{i}. {emo.capitalize()}")
        
        while True:
            try:
                eleccion = int(input("Introduce el número: "))
                if 1 <= eleccion <= len(emociones_disponibles):
                    emocion = emociones_disponibles[eleccion - 1]
                    ruta.append(emocion)
                    numero_nivel = numeros_por_nivel[nivel][emocion]
                    suma_numeros += numero_nivel
                    print(f"Has elegido {emocion.capitalize()} que corresponde al número {numero_nivel}.")
                    break
                else:
                    print("Por favor, elige un número válido.")
            except ValueError:
                print("Introduce un número válido.")
    
    print("\n✨ Calculando número mágico... ✨")
    print(f"Ruta emocional completa: {ruta}")
    print(f"Tu número predicho es: {suma_numeros}")
    
    guardar_ruta_json(ruta, suma_numeros)
    print(f"Ruta guardada en carpeta '{RUTAS_DIR}'")

if __name__ == "__main__":
    main()
