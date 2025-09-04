from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Análisis del Árbol Emocional Numerico (6 niveles)', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, num, label):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f'Rama {num}: {label}', 0, 1)
        self.ln(3)

    def chapter_body(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, text)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

intro_text = (
    "Este documento explica el análisis completo de un árbol emocional numérico con 6 niveles.\n"
    "Cada número representa un estado emocional o reacción, "
    "y la estructura ramificada describe cómo cada emoción lleva a otras emociones posibles.\n"
    "Los niveles reflejan la profundidad de análisis desde la raíz (27) hacia reacciones más específicas.\n"
)
pdf.chapter_title('0', 'Introducción')
pdf.chapter_body(intro_text)

# Función para añadir explicación de cada nivel y rama
def add_branch_explanation(pdf, branch_id, level, description, combinations):
    pdf.chapter_title(branch_id, f'Nivel {level} - {description}')
    pdf.chapter_body("Explicación de las combinaciones y razones de elección:\n")
    for combo, reason in combinations.items():
        pdf.chapter_body(f"- {combo}: {reason}")

# Ejemplo para el nivel 1 (raíz)
level_1_desc = "Raíz 27 con reacciones emocionales primarias"
level_1_combos = {
    '44 Positiva': "Número elegido para representar una reacción muy positiva y abierta.",
    '13 Negativa': "Número que denota rechazo o energía negativa en la interacción.",
    '34 Desinterés': "Número medio que simboliza apatía o falta de respuesta.",
    '9 Enfado': "Número bajo para denotar una reacción brusca o irritada.",
    '22 Tristeza': "Número intermedio para expresar emociones melancólicas.",
    '35 Silencio': "Número cercano a 34 que representa reserva o silencio reflexivo."
}
add_branch_explanation(pdf, '27', 1, level_1_desc, level_1_combos)

# Nivel 2 ejemplo (rama R1)
level_2_desc = "Reacciones derivadas de la rama Positiva (44)"
level_2_combos = {
    '50 Positiva': "Refuerza la emoción positiva con un número alto para amplitud.",
    '13 Negativa': "Contraste para representar posible rechazo incluso tras positividad.",
    '30 Desinterés': "Nivel medio para mostrar respuesta neutra tras emoción positiva.",
    '5 Enfado': "Baja respuesta enfadada para tensiones leves.",
    '14 Tristeza': "Ligeramente superior al 13 para tristeza moderada.",
    '38 Silencio': "Número alto para reflexión o silencio después de positividad."
}
add_branch_explanation(pdf, 'R1', 2, level_2_desc, level_2_combos)

# Nivel 3 ejemplo (rama R1_1)
level_3_desc = "Sub-reacciones tras la reacción 50 Positiva"
level_3_combos = {
    '47 Positiva': "Leve bajada, representa positividad algo menor.",
    '10 Negativa': "Baja negativa para reflejar dudas o molestias leves.",
    '21 Desinterés': "Nivel bajo para neutralidad o apatía.",
    '3 Enfado': "Muy bajo para enfado puntual.",
    '12 Tristeza': "Número bajo para tristeza contenida.",
    '40 Silencio': "Número alto para silencio o reflexión prolongada."
}
add_branch_explanation(pdf, 'R1_1', 3, level_3_desc, level_3_combos)

# Aquí deberías continuar añadiendo explicaciones para los niveles 4, 5 y 6
# por la misma estructura, adaptando descripciones y razones.

# Para ejemplo, añado un resumen final:
pdf.chapter_title('Resumen', 'Interpretación General')
summary_text = (
    "El árbol emocional numérico genera una representación ramificada y profunda "
    "de cómo las emociones se encadenan y evolucionan desde una emoción raíz.\n"
    "Cada número tiene un significado basado en su valor y proximidad a otros estados.\n"
    "La combinación de números y sus asociaciones emocionales permiten entender patrones "
    "y anticipar reacciones en un contexto dinámico.\n"
)
pdf.chapter_body(summary_text)

# Guarda el archivo
pdf.output("arbol_emocional_analisis.pdf")

print("PDF generado: arbol_emocional_analisis.pdf")
