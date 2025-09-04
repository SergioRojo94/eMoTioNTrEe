import graphviz

dot = graphviz.Digraph(format='png')
dot.attr(rankdir='TB', size='10')

# Nodo raíz
dot.node('27', '27')

# Reacciones nivel 1 y números asociados
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

# Reacciones nivel 2 para cada rama de nivel 1
reactions_lvl2 = {
    'R1': [('50', '✅ Positiva'), ('13', '❌ Negativa'), ('30', '😐 Desinterés'), ('5',  '😠 Enfado'), ('14', '😢 Tristeza'), ('38', '🤔 Silencio')],
    'R2': [('17', '✅ Positiva'), ('7',  '❌ Negativa'), ('25', '😐 Desinterés'), ('1',  '😠 Enfado'), ('42', '😢 Tristeza'), ('39', '🤔 Silencio')],
    'R3': [('20', '✅ Positiva'), ('4',  '❌ Negativa'), ('37', '😐 Desinterés'), ('15', '😠 Enfado'), ('28', '😢 Tristeza'), ('41', '🤔 Silencio')],
    'R4': [('6',  '✅ Positiva'), ('18', '❌ Negativa'), ('29', '😐 Desinterés'), ('8',  '😠 Enfado'), ('11', '😢 Tristeza'), ('31', '🤔 Silencio')],
    'R5': [('43', '✅ Positiva'), ('19', '❌ Negativa'), ('26', '😐 Desinterés'), ('3',  '😠 Enfado'), ('24', '😢 Tristeza'), ('32', '🤔 Silencio')],
    'R6': [('12', '✅ Positiva'), ('16', '❌ Negativa'), ('21', '😐 Desinterés'), ('23', '😠 Enfado'), ('33', '😢 Tristeza'), ('36', '🤔 Silencio')],
}

for lvl1_key, nodes in reactions_lvl2.items():
    for i, (num, label) in enumerate(nodes, start=1):
        node_key = f'{lvl1_key}_{i}'
        dot.node(node_key, f'{num}\n{label}')
        dot.edge(lvl1_key, node_key)

# Reacciones nivel 3 para cada nodo nivel 2 (solo un ejemplo para R1_1, R2_1,... para no extender mucho el código)
reactions_lvl3_example = {
    'R1_1': [('47', '✅'), ('10', '❌'), ('21', '😐'), ('3', '😠'), ('12', '😢'), ('40', '🤔')],
    'R2_1': [('4', '✅'), ('13', '❌'), ('29', '😐'), ('2', '😠'), ('17', '😢'), ('22', '🤔')],
    'R3_1': [('9', '✅'), ('5', '❌'), ('31', '😐'), ('12', '😠'), ('20', '😢'), ('25', '🤔')],
    'R4_1': [('14', '✅'), ('7', '❌'), ('23', '😐'), ('11', '😠'), ('28', '😢'), ('33', '🤔')],
    'R5_1': [('19', '✅'), ('8', '❌'), ('26', '😐'), ('10', '😠'), ('15', '😢'), ('27', '🤔')],
    'R6_1': [('24', '✅'), ('3', '❌'), ('30', '😐'), ('6', '😠'), ('21', '😢'), ('18', '🤔')],
}

for lvl2_key, nodes in reactions_lvl3_example.items():
    for i, (num, label) in enumerate(nodes, start=1):
        node_key = f'{lvl2_key}_{i}'
        dot.node(node_key, f'{num}\n{label}')
        dot.edge(lvl2_key, node_key)

# Para nivel 4 y 5 podemos repetir el patrón para unos pocos nodos si quieres, para no saturar.
# Por ejemplo, para R1_1_1 (nivel 3), seguimos con nivel 4 (solo 3 nodos por ejemplo)

reactions_lvl4_example = {
    'R1_1_1': [('2', '✅'), ('14', '❌'), ('41', '😐')],
    'R2_1_1': [('13', '✅'), ('11', '❌'), ('26', '😐')],
}

for lvl3_key, nodes in reactions_lvl4_example.items():
    for i, (num, label) in enumerate(nodes, start=1):
        node_key = f'{lvl3_key}_{i}'
        dot.node(node_key, f'{num}\n{label}')
        dot.edge(lvl3_key, node_key)

# Nivel 5 ejemplo (solo 2 nodos para no saturar)
reactions_lvl5_example = {
    'R1_1_1_1': [('9', '✅'), ('27', '❌')],
    'R2_1_1_1': [('18', '✅'), ('35', '❌')],
}

for lvl4_key, nodes in reactions_lvl5_example.items():
    for i, (num, label) in enumerate(nodes, start=1):
        node_key = f'{lvl4_key}_{i}'
        dot.node(node_key, f'{num}\n{label}')
        dot.edge(lvl4_key, node_key)

# Renderizar
# output_path = '/mnt/data/arbol_emocional_nivel5'
# dot.render(output_path, view=False)
# print(f'Árbol generado en {output_path}.png')

# Ruta Windows: aquí cambia el path para tu usuario o proyecto
# Renderiza en la carpeta actual como PNG y lo abre
dot.render('arbol_emocional_todas_las_ramas', view=True)
print("Árbol generado")
