import graphviz
import os

# Diccionario con las reacciones emocionales y números asignados
emotional_reactions = {
    'positive': ('✅ Positiva', '44'),
    'negative': ('❌ Negativa', '13'),
    'neutral':  ('😐 Desinterés', '34'),
    'angry':    ('😠 Enfado', '9'),
    'sad':      ('😢 Tristeza', '22'),
    'silent':   ('🤔 Silencio', '35'),
}

dot = graphviz.Digraph(format='png')
dot.attr(rankdir='TB', size='10')

# Nodo raíz
dot.node('27', '27')

# Función recursiva para construir el árbol hasta cierto nivel
def build_tree(parent_id, depth, max_depth, path=''):
    if depth > max_depth:
        return
    for reaction_key, (emoji, number) in emotional_reactions.items():
        node_id = f"{path}{reaction_key}"
        dot.node(node_id, f"{number}\n{emoji}")
        dot.edge(parent_id, node_id)
        # Recurse para siguientes niveles
        build_tree(node_id, depth + 1, max_depth, path=f"{node_id}_")

# Construir árbol hasta 3 niveles o más, aquí 5 por ejemplo
build_tree('27', 1, 2)

# Para no sobreescribir archivos, generamos un nombre con sufijo incremental
base_name = 'arbol_emocional_numeros'
suffix = 0
while os.path.exists(f'{base_name}{suffix}.png'):
    suffix += 1

filename = f'{base_name}{suffix}'

# Guardamos el archivo PNG
dot.render(filename, view=True)

print(f"Archivo generado: {filename}.png")
print("Ábrelo manualmente con tu visor de imágenes preferido.")
