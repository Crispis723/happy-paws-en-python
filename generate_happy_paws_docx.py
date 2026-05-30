from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION


def add_heading(doc, text, level=1):
    p = doc.add_paragraph()
    p.style = f'Heading {level}'
    run = p.add_run(text)
    run.bold = True
    return p


def add_bullet(doc, text, level=0):
    style = 'List Bullet' if level == 0 else 'List Bullet 2'
    p = doc.add_paragraph(style=style)
    p.add_run(text)
    return p


def add_numbered(doc, text):
    p = doc.add_paragraph(style='List Number')
    p.add_run(text)
    return p


def add_label_value(doc, label, value):
    p = doc.add_paragraph()
    r1 = p.add_run(f'{label}: ')
    r1.bold = True
    p.add_run(value)
    return p


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = value
    return table


doc = Document()

# Global style
styles = doc.styles
styles['Normal'].font.name = 'Aptos'
styles['Normal'].font.size = Pt(11)
for name in ['Heading 1', 'Heading 2', 'Heading 3']:
    styles[name].font.name = 'Aptos'

section = doc.sections[0]
section.top_margin = Inches(0.75)
section.bottom_margin = Inches(0.75)
section.left_margin = Inches(0.9)
section.right_margin = Inches(0.9)

# Cover
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('PROYECTO EJECUTIVO INTEGRAL\nHAPPY PAWS')
run.bold = True
run.font.size = Pt(20)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Plataforma Colombiana de Bienestar Animal y Gestión Veterinaria\nDocumento ejecutivo - Versión mejorada')
run.font.size = Pt(13)

for line in [
    'Fecha de emisión: 30 de mayo de 2026',
    'Empresa: Happy Paws SAS (en formación)',
    'Contacto: contacto@happypaws.com | Tel: +57 320 555 1234'
]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run(line)


doc.add_page_break()

add_heading(doc, '1. CARÁTULA', 1)
add_label_value(doc, 'Proyecto', 'Proyecto Ejecutivo Integral - Happy Paws')
add_label_value(doc, 'Descripción', 'Plataforma colombiana SaaS para bienestar animal, gestión veterinaria y adopción responsable.')
add_label_value(doc, 'Versión', '2.1 - Ejecutiva y optimizada para presentación')
add_label_value(doc, 'Fecha', '30 de mayo de 2026')
add_label_value(doc, 'Empresa', 'Happy Paws SAS (en formación)')
add_label_value(doc, 'Contacto', 'contacto@happypaws.com | +57 320 555 1234')
add_bullet(doc, 'Identidad visual sugerida: huella de mascota integrada con un corazón y un elemento digital, para comunicar tecnología y cuidado.')

add_heading(doc, '2. ÍNDICE GENERAL', 1)
for item in [
    '1. Carátula',
    '2. Índice General',
    '3. Resumen Ejecutivo',
    '4. Análisis de Mercado y Competencia',
    '5. Problema que Resuelve',
    '6. Nuestra Solución',
    '7. MVP Funcional',
    '8. Arquitectura Tecnológica',
    '9. Modelo de Negocio y Planes de Suscripción',
    '10. Plan de Marketing y Ventas',
    '11. Plan Operativo y Soporte',
    '12. Estructura Legal en Colombia',
    '13. Equipo Requerido',
    '14. Costos de Desarrollo Detallados',
    '15. Costos Operativos Mensuales',
    '16. Proyección Financiera a 12 Meses',
    '17. Inversión Requerida y Retorno',
    '18. KPIs de Éxito',
    '19. Riesgos y Plan de Contingencia',
    '20. Roadmap de Implementación',
    '21. Conclusión y Próximos Pasos',
    '22. Anexos'
]:
    add_bullet(doc, item)
add_bullet(doc, 'Nota: el índice puede actualizarse automáticamente en Word cuando se definan estilos y numeración final.')

add_heading(doc, '3. RESUMEN EJECUTIVO', 1)
add_label_value(doc, 'Misión', 'Transformar el bienestar animal en Colombia mediante una plataforma SaaS que conecte veterinarias, refugios y propietarios de mascotas en un ecosistema digital eficiente.')
add_label_value(doc, 'Visión', 'Consolidarse como una de las plataformas líderes en Latinoamérica para la gestión integral de servicios veterinarios, adopción responsable y seguimiento del bienestar animal.')
add_label_value(doc, 'Valores', 'Innovación, bienestar animal, transparencia, responsabilidad social y servicio.')
add_label_value(doc, 'Definición de la plataforma', 'Happy Paws es una solución multiempresa que digitaliza procesos veterinarios, facilita adopciones responsables y centraliza la gestión de mascotas en Colombia.')
add_label_value(doc, 'TAM', '4,2 millones de hogares con mascotas en Colombia (estimación 2025).')
add_label_value(doc, 'SAM', '12.000 veterinarias registradas en Cámara de Comercio.')
add_label_value(doc, 'SOM inicial', '500 veterinarias en Bogotá y Medellín durante el primer año.')
add_heading(doc, 'Objetivos SMART a 12 meses', 2)
for item in [
    'Alcanzar 100 veterinarias activas en la plataforma.',
    'Registrar 50.000 mascotas en el sistema.',
    'Facilitar 2.000 adopciones responsables.',
    'Reducir en 20% el tiempo de gestión administrativa en veterinarias.',
    'Lograr un NPS igual o superior a 70 entre propietarios de mascotas.'
]:
    add_numbered(doc, item)
add_label_value(doc, 'Propuesta de valor', 'Una sola plataforma para cuidar, adoptar y proteger mascotas en Colombia.')
add_heading(doc, 'Resultados esperados en el primer año', 2)
for item in [
    '100 veterinarias activas.',
    '50.000 mascotas registradas.',
    '2.000 adopciones completadas.'
]:
    add_bullet(doc, item)
add_label_value(doc, 'Inversión inicial estimada', 'COP 1.200.000.000 para desarrollo, marketing y operación.')

add_heading(doc, '4. ANÁLISIS DE MERCADO Y COMPETENCIA', 1)
add_label_value(doc, 'Tamaño del mercado', '67% de los hogares colombianos tienen al menos una mascota.')
add_label_value(doc, 'Gasto promedio anual por mascota', 'COP 1.800.000 (fuente de referencia: Euromonitor, 2025).')
add_label_value(doc, 'Mercado total estimado', 'COP 7,5 billones.')
add_heading(doc, 'Tendencias relevantes', 2)
for item in [
    'Digitalización de servicios veterinarios y de atención al cliente.',
    'Mayor conciencia sobre bienestar animal y tenencia responsable.',
    'Adopción responsable impulsada por la Ley 1774 de 2016.',
    'Crecimiento de plataformas SaaS orientadas a la salud y servicios especializados.'
]:
    add_bullet(doc, item)
add_heading(doc, 'Competidores directos e indirectos', 2)
for item in ['PetSmile (Colombia)', 'VetPraxis (Perú)', 'PetDesk (Estados Unidos, con presencia en Latinoamérica)', 'Huellitas App (México)']:
    add_numbered(doc, item)
add_heading(doc, 'Matriz comparativa simplificada', 2)
add_table(doc, ['Plataforma', 'Gestión clínica', 'Adopciones', 'Multiempresa', 'Enfoque Colombia'], [
    ['Happy Paws', 'Sí', 'Sí', 'Sí', 'Sí'],
    ['PetSmile', 'Sí', 'No', 'No', 'Sí'],
    ['VetPraxis', 'Sí', 'No', 'Sí', 'No'],
    ['PetDesk', 'Sí', 'No', 'No', 'No'],
    ['Huellitas App', 'No', 'Sí', 'No', 'No']
])
add_heading(doc, 'Análisis FODA', 2)
add_bullet(doc, 'Fortalezas: enfoque local, solución integral y arquitectura escalable tipo SaaS.')
add_bullet(doc, 'Oportunidades: mercado en crecimiento y potencial de alianzas con alcaldías, fundaciones y veterinarias.')
add_bullet(doc, 'Debilidades: empresa en formación y dependencia de inversión inicial.')
add_bullet(doc, 'Amenazas: resistencia al cambio digital y competencia internacional con mayor madurez.')
add_heading(doc, 'Factores diferenciadores clave', 2)
for item in [
    'Plataforma multiempresa.',
    'Integración con refugios y procesos de adopción.',
    'Cumplimiento del marco legal colombiano.',
    'Flujos digitales de adopción y seguimiento.',
    'KPIs orientados al bienestar animal y a la eficiencia operativa.'
]:
    add_numbered(doc, item)

add_heading(doc, '5. PROBLEMA QUE RESUELVE', 1)
add_heading(doc, 'Problema actual', 2)
for item in [
    'Una gran parte de las veterinarias PYME en Colombia todavía gestiona procesos en papel o con herramientas dispersas.',
    'Los refugios y fundaciones carecen de sistemas digitales para administrar adopciones de forma trazable y organizada.',
    'Los propietarios no cuentan con un acceso centralizado al historial clínico y al seguimiento de sus mascotas.'
]:
    add_bullet(doc, item)
add_heading(doc, 'Dolores específicos', 2)
add_bullet(doc, 'Veterinarias: pérdida de tiempo administrativo, duplicidad de registros y menor capacidad de atención.')
add_bullet(doc, 'Propietarios: falta de información confiable, acceso fragmentado y baja trazabilidad de la atención.')
add_bullet(doc, 'Refugios: baja tasa de adopción y dificultad para gestionar postulaciones.')
add_bullet(doc, 'Entidades de control: dificultad para rastrear casos de maltrato, abandono o incumplimiento.')
add_heading(doc, 'Costo de no tener solución', 2)
add_bullet(doc, 'Pérdidas de hasta COP 20.000.000 anuales por ineficiencias operativas en veterinarias pequeñas.')
add_bullet(doc, 'Baja tasa de adopción: una parte importante de los animales en refugios no logra encontrar hogar oportunamente.')
add_heading(doc, 'Validación del problema', 2)
add_bullet(doc, 'Encuestas realizadas en Bogotá durante 2025 muestran que la mayoría de las veterinarias desea digitalizar procesos, pero no encuentra soluciones accesibles y adaptadas al mercado local.')

add_heading(doc, 'Cierre', 1)
p = doc.add_paragraph()
p.add_run('Este documento deja una base más profesional para Word. ').bold = True
p.add_run('Si quieres, en el siguiente paso puedo continuar con las secciones 6 a 22 en el mismo estilo y dejarte el documento completo listo para presentar.')

doc.save('happy_paws_proyecto_ejecutivo.docx')
print('Generado: happy_paws_proyecto_ejecutivo.docx')
