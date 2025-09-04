import streamlit as st
import json
import os
import random
import time

numeros_por_nivel = [
    {'positiva': 44, 'negativa': 13, 'desinteres': 34, 'enfado': 9, 'tristeza': 22, 'silencio': 35},
    {'positiva': 50, 'negativa': 13, 'desinteres': 30, 'enfado': 5, 'tristeza': 14, 'silencio': 38},
    {'positiva': 47, 'negativa': 10, 'desinteres': 21, 'enfado': 3, 'tristeza': 12, 'silencio': 40},
    {'positiva': 52, 'negativa': 8, 'desinteres': 27, 'enfado': 6, 'tristeza': 13, 'silencio': 41},
    {'positiva': 49, 'negativa': 12, 'desinteres': 29, 'enfado': 4, 'tristeza': 15, 'silencio': 39},
    {'positiva': 51, 'negativa': 11, 'desinteres': 28, 'enfado': 7, 'tristeza': 16, 'silencio': 42},
]

emociones_disponibles = ['positiva', 'negativa', 'desinteres', 'enfado', 'tristeza', 'silencio']

mensajes_magicos = [
    "✨ Las energías del universo convergen...",
    "🌬️ El viento susurra un secreto...",
    "🌟 Las estrellas brillan con fuerza...",
    "🔢 Los números se alinean para ti...",
    "🔮 Un misterioso destino te espera...",
    "⏳ El tiempo se detiene por un instante...",
]

RUTAS_DIR = "rutas_emocionales"

def guardar_ruta_json(ruta_emocional, numero_predicho):
    if not os.path.exists(RUTAS_DIR):
        os.makedirs(RUTAS_DIR)
    
    archivos = os.listdir(RUTAS_DIR)
    nombre_archivo = f"ruta_{len(archivos) + 1}.json"
    ruta_completa = os.path.join(RUTAS_DIR, nombre_archivo)

    datos = {
        "ruta_emocional": ruta_emocional,
        "numero_predicho": numero_predicho
    }
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

st.title("Magia Emocional ✨")

st.write("""
Selecciona tus emociones en cada nivel y descubre el número mágico que hemos predicho para ti.
""")

ruta = []
suma_numeros = 0

for nivel in range(6):
    emocion = st.selectbox(
        f"Nivel {nivel + 1}: ¿Cómo te sientes?",
        options=emociones_disponibles,
        key=f"nivel_{nivel}"
    )
    ruta.append(emocion)
    suma_numeros += numeros_por_nivel[nivel][emocion]



if st.button("Predecir número mágico"):
    for mensaje in mensajes_magicos:
        st.write(mensaje)
        time.sleep(0.8)
    st.success(f"✨ Tu número predicho es: {suma_numeros} ✨")
    st.write(f"Ruta emocional completa: {ruta}")
    guardar_ruta_json(ruta, suma_numeros)
    st.write(f"Ruta guardada en carpeta `{RUTAS_DIR}`. ¡Gracias por jugar! 🎉")

