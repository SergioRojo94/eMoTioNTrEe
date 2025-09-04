import os
import json

# Emociones con nombre, emoji y código numérico
emotional_reactions = {
    'Positiva':  {'emoji': '✅ Positiva',   'num': 44},
    'Negativa':  {'emoji': '❌ Negativa',   'num': 13},
    'Desinteres':{'emoji': '😐 Desinterés', 'num': 34},
    'Enfado':    {'emoji': '😠 Enfado',     'num': 9},
    'Tristeza':  {'emoji': '😢 Tristeza',   'num': 22},
    'Silencio':  {'emoji': '🤔 Silencio',   'num': 35},
}

BASE_PATH = r"C:\Users\Sergio\Documentos\rutas_emocionales"

NIVELES = 6

# Interpretación básica por ruta (breve)
def interpretar_ruta(ruta):
    # Ejemplo simple que usa frecuencia de emociones y patrón inicial-final
    frec = {emo: ruta.count(emo) for emo in emotional_reactions}
    inicio = ruta[0]
    fin = ruta[-1]
    partes = []
    if frec['Positiva'] > 2:
        partes.append("predomina un ánimo positivo")
    if frec['Negativa'] > 2:
        partes.append("se siente una fuerte negatividad")
    if frec['Enfado'] >= 1:
        partes.append("hay presencia de enfado o frustración")
    if frec['Silencio'] >= 2:
        partes.append("predomina reflexión o silencio")
    if inicio == fin:
        partes.append(f"la emoción comienza y termina en {inicio.lower()}")
    if not partes:
        partes.append("mezcla emocional equilibrada sin predominancia clara")
    return "Ruta emocional que " + ", ".join(partes) + "."

# Función para crear todas las rutas, guardarlas como JSON y organizar carpetas
def crear_rutas_y_guardar(nivel_actual=1, ruta_actual=[]):
    if nivel_actual > NIVELES:
        carpetas = ruta_actual[:-1]
        carpeta_path = os.path.join(BASE_PATH, *carpetas)
        os.makedirs(carpeta_path, exist_ok=True)  # Primero aseguro que la carpeta exista
        
        # Ahora sí puedo listar la carpeta para saber cuántos archivos hay
        archivo_nombre = f"ruta_{len(os.listdir(carpeta_path)) + 1}.json"
        archivo_path = os.path.join(carpeta_path, archivo_nombre)
        
        ruta_info = {
            "ruta": ruta_actual,
            "codigos": [emotional_reactions[e]['num'] for e in ruta_actual],
            "interpretacion": interpretar_ruta(ruta_actual)
        }
        with open(archivo_path, "w", encoding="utf-8") as f:
            json.dump(ruta_info, f, ensure_ascii=False, indent=2)
        return
    
    for emocion in emotional_reactions.keys():
        crear_rutas_y_guardar(nivel_actual + 1, ruta_actual + [emocion])



# Ejecución principal
if __name__ == "__main__":
    print("Generando rutas emocionales y guardando en JSON...")
    crear_rutas_y_guardar()
    print(f"¡Listo! Archivos generados en '{BASE_PATH}'")
