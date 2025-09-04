import graphviz

# Diccionario de reacciones emocionales posibles (se usan para todas las ramas)
emotional_reactions = {
    'positive':   ('✅ Positiva', '50'),
    'negative':   ('❌ Negativa', '13'),
    'neutral':    ('😐 Desinterés', '30'),
    'angry':      ('😠 Enfado', '5'),
    'sad':        ('😢 Tristeza', '14'),
    'silent':     ('🤔 Silencio', '38'),
}

# Crear el grafo
dot = graphviz.Digraph(format='png')
dot.attr(rankdir='TB', size='10')

# Nodo raíz
dot.node('27', '27')

# Función recursiva para construir el árbol hasta cierto nivel
def build_tree(parent_id, depth, max_depth, path=''):
    if depth > max_depth:
        return

    for key, (emoji, number) in emotional_reactions.items():
        node_id = f"{path}{key}"
        label = f"{number}\n{emoji}"
        dot.node(node_id, label)
        dot.edge(parent_id, node_id)
        # Recurse para construir siguiente nivel
        build_tree(node_id, depth + 1, max_depth, path=f"{node_id}_")

# Construye el árbol hasta 6 niveles
build_tree('27', 1, 6)

# Renderiza el archivo PNG y lo abre automáticamente en Windows
output_path = 'arbol_emocional_6niveles'
dot.render(output_path, view=True)

print(f"Archivo generado: {output_path}.png")
