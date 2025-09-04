import os

import graphviz

# Creamos un árbol simplificado hasta 3 niveles para que sea legible visualmente.
# En una implementación completa se generaría dinámicamente con más nodos y niveles.

dot = graphviz.Digraph(format='png')
dot.attr(rankdir='TB', size='10')

# Nivel 0 (Raíz)
dot.node('27', '27')

# Nivel 1
reactions_lvl1 = {
    'R1': ('44', '✅ Positiva'),
    'R2': ('13', '❌ Negativa'),
    'R3': ('34', '😐 Desinterés'),
    'R4': ('9',  '😠 Enfado'),
    'R5': ('22', '😢 Tristeza'),
    'R6': ('35', '🤔 Silencio'),
}

for key, (num, label) in reactions_lvl1.items():
    dot.node(key, f'{num}\n{label}')
    dot.edge('27', key)

# Nivel 2 para una sola rama (ej: R1 → R1_1 to R1_6)
reactions_lvl2 = {
    'R1_1': ('50', '✅ Positiva'),
    'R1_2': ('13', '❌ Negativa'),
    'R1_3': ('30', '😐 Desinterés'),
    'R1_4': ('5',  '😠 Enfado'),
    'R1_5': ('14', '😢 Tristeza'),
    'R1_6': ('38', '🤔 Silencio'),
}

for key, (num, label) in reactions_lvl2.items():
    dot.node(key, f'{num}\n{label}')
    dot.edge('R1', key)

# Nivel 3 para una rama de la anterior (ej: R1_1)
reactions_lvl3 = {
    'R1_1_1': ('47', '✅'),
    'R1_1_2': ('10', '❌'),
    'R1_1_3': ('21', '😐'),
    'R1_1_4': ('3',  '😠'),
    'R1_1_5': ('12', '😢'),
    'R1_1_6': ('40', '🤔'),
}

for key, (num, label) in reactions_lvl3.items():
    dot.node(key, f'{num}\n{label}')
    dot.edge('R1_1', key)

base_name = 'arbol_emocional_numeros_first_of_all'
suffix = 0
while os.path.exists(f'{base_name}{suffix}.png'):
    suffix += 1

filename = f'{base_name}{suffix}'

# Guardamos el archivo PNG
dot.render(filename, view=True)

print(f"Archivo generado: {filename}.png")
