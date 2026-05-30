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


def add_key_value_table(doc, title, rows):
    add_heading(doc, title, 2)
    add_table(doc, ['Concepto', 'Detalle'], rows)


def money(value):
    return f'COP {value:,.0f}'.replace(',', '.')


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
add_table(doc, ['Elemento', 'Valor clave', 'Lectura ejecutiva'], [
    ['Misión', 'Conectar el ecosistema de bienestar animal', 'Digitalizar la operación veterinaria y de adopciones en un solo entorno.'],
    ['Visión', 'Liderar Latinoamérica', 'Ser referente regional en software para veterinarias, refugios y propietarios.'],
    ['Propuesta de valor', 'Una sola plataforma para cuidar, adoptar y proteger mascotas', 'Reduce fricción operativa y mejora la trazabilidad del servicio.'],
    ['Inversión inicial', money(1200000000), 'Capital requerido para desarrollo, salida comercial y operación del primer año.']
])
add_key_value_table(doc, 'Indicadores de mercado', [
    ['TAM', '4,2 millones de hogares con mascotas en Colombia (estimación 2025).'],
    ['SAM', '12.000 veterinarias registradas en Cámara de Comercio.'],
    ['SOM inicial', '500 veterinarias en Bogotá y Medellín durante el primer año.']
])
add_heading(doc, 'Objetivos SMART a 12 meses', 2)
add_table(doc, ['Objetivo', 'Meta', 'Indicador'], [
    ['Crecimiento comercial', '100 veterinarias activas', 'Número de cuentas activas'],
    ['Base de datos', '50.000 mascotas registradas', 'Total de registros únicos'],
    ['Impacto social', '2.000 adopciones responsables', 'Adopciones completadas'],
    ['Eficiencia', 'Reducir 20% el tiempo administrativo', 'Tiempo promedio por trámite'],
    ['Satisfacción', 'NPS igual o superior a 70', 'NPS de usuarios finales']
])
add_heading(doc, 'Resultados esperados en el primer año', 2)
add_table(doc, ['Resultado', 'Meta anual', 'Impacto esperado'], [
    ['Veterinarias activas', '100', 'Validación comercial y adopción del software.'],
    ['Mascotas registradas', '50.000', 'Base de datos útil para seguimiento y servicios.'],
    ['Adopciones completadas', '2.000', 'Mayor eficiencia para refugios y fundaciones.']
])

add_heading(doc, '4. ANÁLISIS DE MERCADO Y COMPETENCIA', 1)
add_table(doc, ['Variable', 'Dato', 'Interpretación'], [
    ['Tamaño del mercado', '67% de los hogares colombianos con al menos una mascota', 'Existe una masa crítica suficiente para una solución digital especializada.'],
    ['Gasto promedio anual por mascota', money(1800000), 'Los usuarios ya destinan presupuesto a salud, cuidado y servicios.'],
    ['Mercado total estimado', money(7500000000000), 'Oportunidad amplia para monetización por suscripción y servicios complementarios.']
])
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
add_table(doc, ['Fortalezas', 'Oportunidades', 'Debilidades', 'Amenazas'], [[
    'Enfoque local, solución integral y arquitectura escalable tipo SaaS.',
    'Mercado en crecimiento y potencial de alianzas con alcaldías, fundaciones y veterinarias.',
    'Empresa en formación y dependencia de inversión inicial.',
    'Resistencia al cambio digital y competencia internacional con mayor madurez.'
]])
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
add_table(doc, ['Actor', 'Dolor principal', 'Consecuencia'], [
    ['Veterinarias', 'Pérdida de tiempo administrativo y duplicidad de registros', 'Menor capacidad de atención y mayores costos operativos.'],
    ['Propietarios', 'Falta de información confiable y acceso fragmentado', 'Menor confianza y más fricción en el seguimiento.'],
    ['Refugios', 'Baja tasa de adopción y procesos manuales', 'Menor visibilidad y adopciones más lentas.'],
    ['Entidades de control', 'Poca trazabilidad de casos de maltrato o abandono', 'Menor capacidad de intervención oportuna.']
])
add_heading(doc, 'Costo de no tener solución', 2)
add_table(doc, ['Impacto', 'Valor estimado', 'Efecto'], [
    ['Pérdidas por ineficiencia', money(20000000), 'Afecta la rentabilidad de veterinarias pequeñas.'],
    ['Tasa de adopción baja', '30% de animales encuentra hogar', 'Disminuye el impacto social de refugios y fundaciones.']
])
add_heading(doc, 'Validación del problema', 2)
add_bullet(doc, 'Encuestas realizadas en Bogotá durante 2025 muestran que la mayoría de las veterinarias desea digitalizar procesos, pero no encuentra soluciones accesibles y adaptadas al mercado local.')

add_heading(doc, '6. NUESTRA SOLUCIÓN', 1)
add_table(doc, ['Necesidad', 'Funcionalidad Happy Paws', 'Beneficio'], [
    ['Gestión clínica dispersa', 'Historia clínica centralizada', 'Mejor trazabilidad y atención más rápida.'],
    ['Adopciones manuales', 'Módulo de adopciones y postulaciones', 'Mayor transparencia y más adopciones efectivas.'],
    ['Falta de visibilidad comercial', 'Panel de analítica y reportes', 'Decisiones basadas en datos.'],
    ['Comunicación fragmentada', 'Notificaciones automáticas', 'Mejor experiencia para usuarios y equipos.']
])
add_heading(doc, 'Componentes de la solución', 2)
for item in [
    'Portal para veterinarias con administración de pacientes, citas, vacunas e historiales.',
    'Portal para refugios con catálogo de mascotas, postulaciones y control de adopción.',
    'Portal para propietarios con historial, recordatorios y seguimiento de sus mascotas.',
    'Tablero administrativo con indicadores, reportes y configuración multiempresa.'
]:
    add_bullet(doc, item)

add_heading(doc, '7. MVP FUNCIONAL', 1)
add_table(doc, ['Módulo', 'Alcance MVP', 'Prioridad'], [
    ['Autenticación', 'Registro, login y recuperación de contraseña', 'Alta'],
    ['Gestión de mascotas', 'Ficha básica, datos clínicos y estado', 'Alta'],
    ['Citas y recordatorios', 'Agenda simple y notificaciones', 'Alta'],
    ['Adopciones', 'Publicación, postulación y seguimiento', 'Alta'],
    ['Reportes', 'Indicadores esenciales para operación', 'Media'],
    ['Facturación', 'Planes de suscripción y control básico', 'Media']
])
add_heading(doc, 'Criterios de éxito del MVP', 2)
for item in [
    'Tiempo de registro de mascota menor a 2 minutos.',
    'Publicación de una mascota en adopción en menos de 1 minuto.',
    'Disponibilidad operativa superior al 99,5% durante piloto.',
    'Al menos 10 veterinarias piloto usando el sistema de forma activa.'
]:
    add_bullet(doc, item)

add_heading(doc, '8. ARQUITECTURA TECNOLÓGICA', 1)
add_table(doc, ['Capa', 'Tecnología sugerida', 'Motivo'], [
    ['Frontend', 'React o Next.js', 'Experiencia moderna, rápida y escalable.'],
    ['Backend', 'Python con FastAPI o Django', 'Rapidez de desarrollo y mantenibilidad.'],
    ['Base de datos', 'PostgreSQL', 'Robustez, relaciones y soporte multiempresa.'],
    ['Infraestructura', 'AWS, GCP o Azure', 'Escalabilidad y servicios administrados.'],
    ['Autenticación', 'JWT + OAuth', 'Seguridad y control de acceso.'],
    ['Analítica', 'Metabase o dashboards propios', 'Visualización de KPIs para clientes y operación.']
])
add_heading(doc, 'Principios técnicos', 2)
for item in [
    'Arquitectura multiempresa por tenant.',
    'Escalabilidad horizontal para nuevos clientes.',
    'Seguridad por roles y trazabilidad de acciones.',
    'Diseño API-first para integraciones futuras.'
]:
    add_bullet(doc, item)

add_heading(doc, '9. MODELO DE NEGOCIO Y PLANES DE SUSCRIPCIÓN', 1)
add_table(doc, ['Plan', 'Precio mensual', 'Dirigido a', 'Incluye'], [
    ['Starter', money(99000), 'Veterinarias pequeñas', 'Agenda, pacientes y recordatorios básicos.'],
    ['Pro', money(249000), 'Veterinarias en crecimiento', 'Clínica, adopciones, reportes y usuarios múltiples.'],
    ['Enterprise', money(590000), 'Cadenas y aliados grandes', 'Multi sede, analítica avanzada e integraciones.']
])
add_heading(doc, 'Fuentes de ingresos', 2)
for item in [
    'Suscripción mensual por veterinaria o refugio.',
    'Servicios premium de adopción destacada y campañas.',
    'Implementaciones y soporte especializado.',
    'Convenios con aliados estratégicos.'
]:
    add_bullet(doc, item)

add_heading(doc, '10. PLAN DE MARKETING Y VENTAS', 1)
add_table(doc, ['Canal', 'Objetivo', 'KPI'], [
    ['Ventas directas', 'Cerrar veterinarias piloto', 'Tasa de cierre'],
    ['Alianzas', 'Firmar acuerdos con refugios y fundaciones', 'Número de convenios'],
    ['Contenido digital', 'Generar autoridad de marca', 'Leads calificados'],
    ['Referidos', 'Escalar adquisición con clientes actuales', 'CAC por canal']
])
add_heading(doc, 'Metas comerciales', 2)
for item in [
    '20 clientes piloto en los primeros 90 días.',
    '60 clientes activos al mes 6.',
    '100 clientes activos al mes 12.'
]:
    add_bullet(doc, item)

add_heading(doc, '11. PLAN OPERATIVO Y SOPORTE', 1)
add_table(doc, ['Proceso', 'Responsable', 'SLA objetivo'], [
    ['Onboarding', 'Customer Success', '24 horas'],
    ['Soporte funcional', 'Mesa de ayuda', '4 horas hábiles'],
    ['Incidentes críticos', 'Equipo técnico', '1 hora'],
    ['Capacitación', 'Customer Success + Producto', 'Primera semana']
])
add_heading(doc, 'Estructura de atención', 2)
for item in [
    'Canal de soporte por correo y chat.',
    'Base de conocimiento para usuarios finales.',
    'Seguimiento de tickets con prioridad y estado.'
]:
    add_bullet(doc, item)

add_heading(doc, '12. ESTRUCTURA LEGAL EN COLOMBIA', 1)
add_table(doc, ['Elemento', 'Requisito', 'Estado recomendado'], [
    ['Tipo societario', 'SAS', 'Adecuado para escalabilidad y entrada de inversión.'],
    ['RUT y cámara de comercio', 'Inscripción formal', 'Necesario para operación comercial.'],
    ['Protección de datos', 'Política de tratamiento y consentimiento', 'Crítico por la información clínica.'],
    ['Términos y condiciones', 'Contratos de uso por tipo de cliente', 'Obligatorio para operación digital.']
])
add_heading(doc, 'Consideraciones legales', 2)
for item in [
    'Cumplimiento de la Ley 1581 de 2012 sobre protección de datos personales.',
    'Trazabilidad de consentimiento para manejo de información sensible.',
    'Soporte documental para relaciones comerciales con veterinarias y fundaciones.'
]:
    add_bullet(doc, item)

add_heading(doc, '13. EQUIPO REQUERIDO', 1)
add_table(doc, ['Rol', 'Dedicación', 'Costo mensual estimado'], [
    ['Product Manager', 'Tiempo completo', money(12000000)],
    ['Desarrollador Full Stack', 'Tiempo completo', money(10000000)],
    ['Diseñador UX/UI', 'Medio tiempo', money(5000000)],
    ['Customer Success', 'Tiempo completo', money(6500000)],
    ['Ventas B2B', 'Tiempo completo', money(7000000)]
])
add_heading(doc, 'Roles críticos', 2)
for item in [
    'Líder de producto para priorizar el roadmap.',
    'Equipo técnico para construir y sostener el MVP.',
    'Área comercial para adquisición y retención.',
    'Soporte para entrenamiento y acompañamiento.'
]:
    add_bullet(doc, item)

add_heading(doc, '14. COSTOS DE DESARROLLO DETALLADOS', 1)
add_table(doc, ['Concepto', 'Valor'], [
    ['Descubrimiento y definición', money(40000000)],
    ['Diseño UX/UI', money(60000000)],
    ['Desarrollo backend y frontend', money(320000000)],
    ['QA y pruebas', money(50000000)],
    ['Infraestructura inicial', money(30000000)],
    ['Lanzamiento piloto', money(50000000)]
])
add_label_value(doc, 'Total estimado desarrollo', money(550000000))

add_heading(doc, '15. COSTOS OPERATIVOS MENSUALES', 1)
add_table(doc, ['Concepto', 'Valor mensual'], [
    ['Nómina base', money(40500000)],
    ['Infraestructura y herramientas', money(8500000)],
    ['Marketing y pauta', money(15000000)],
    ['Soporte y operación', money(7000000)],
    ['Administración y legales', money(5000000)]
])
add_label_value(doc, 'Total operativo mensual estimado', money(76000000))

add_heading(doc, '16. PROYECCIÓN FINANCIERA A 12 MESES', 1)
projection_rows = [
    ['1', '10', money(1485000), money(76000000), money(-74515000)],
    ['2', '15', money(2227500), money(76000000), money(-73772500)],
    ['3', '20', money(2970000), money(76000000), money(-73030000)],
    ['4', '28', money(4158000), money(76000000), money(-71842000)],
    ['5', '36', money(5346000), money(76000000), money(-70654000)],
    ['6', '45', money(6682500), money(76000000), money(-69317500)],
    ['7', '55', money(8167500), money(76000000), money(-67832500)],
    ['8', '65', money(9652500), money(76000000), money(-66347500)],
    ['9', '76', money(11284200), money(76000000), money(-64715800)],
    ['10', '88', money(13068000), money(76000000), money(-62932000)],
    ['11', '100', money(14850000), money(76000000), money(-61150000)],
    ['12', '115', money(17077500), money(76000000), money(-58922500)]
]
add_table(doc, ['Mes', 'Clientes activos', 'Ingresos', 'Costos', 'Flujo neto'], projection_rows)
add_bullet(doc, 'Supuesto de cálculo: mezcla de planes Starter, Pro y Enterprise con ingreso promedio por cliente de aproximadamente COP 148.500 al mes al final del año.')

add_heading(doc, '17. INVERSIÓN REQUERIDA Y RETORNO', 1)
add_table(doc, ['Escenario', 'Inversión', 'Horizonte'], [
    ['Base', money(1200000000), '12 meses'],
    ['Conservador', money(1000000000), 'Mayor foco en MVP y ventas orgánicas'],
    ['Agresivo', money(1500000000), 'Más marketing y expansión comercial']
])
add_heading(doc, 'Uso de los recursos', 2)
for item in [
    '45% desarrollo y producto.',
    '25% marketing y adquisición de clientes.',
    '20% operación y talento.',
    '10% contingencia y legales.'
]:
    add_bullet(doc, item)

add_heading(doc, '18. KPIs DE ÉXITO', 1)
add_table(doc, ['KPI', 'Meta', 'Frecuencia'], [
    ['Clientes activos', '100', 'Mensual'],
    ['Retención', '85%', 'Mensual'],
    ['NPS', '70+', 'Trimestral'],
    ['Adopciones gestionadas', '2.000', 'Mensual'],
    ['Tiempo de respuesta soporte', '< 4 horas', 'Mensual']
])

add_heading(doc, '19. RIESGOS Y PLAN DE CONTINGENCIA', 1)
add_table(doc, ['Riesgo', 'Probabilidad', 'Mitigación'], [
    ['Resistencia al cambio', 'Media', 'Capacitación, onboarding y acompañamiento cercano.'],
    ['Retrasos de desarrollo', 'Media', 'Roadmap por hitos y priorización del MVP.'],
    ['Baja adopción comercial', 'Media', 'Pilotos, referidos y alianzas estratégicas.'],
    ['Riesgo legal de datos', 'Baja', 'Políticas, consentimientos y control de acceso.']
])

add_heading(doc, '20. ROADMAP DE IMPLEMENTACIÓN', 1)
add_table(doc, ['Fase', 'Duración', 'Entregables'], [
    ['Descubrimiento', '4 semanas', 'Alcance, requerimientos y diseño funcional.'],
    ['Construcción MVP', '10 semanas', 'Módulos esenciales y pruebas.'],
    ['Piloto', '4 semanas', 'Uso con clientes iniciales y ajustes.'],
    ['Lanzamiento', '4 semanas', 'Comercialización y escalado inicial.']
])

add_heading(doc, '21. CONCLUSIÓN Y PRÓXIMOS PASOS', 1)
add_table(doc, ['Paso', 'Responsable', 'Resultado'], [
    ['Validar alcance final', 'Dirección', 'Documento cerrado y priorizado.'],
    ['Ajustar presupuesto', 'Finanzas', 'Plan de inversión aprobado.'],
    ['Iniciar desarrollo', 'Producto y Tecnología', 'MVP en construcción.'],
    ['Abrir pilotos', 'Comercial', 'Primeros clientes activos.']
])
add_bullet(doc, 'Happy Paws queda posicionado como una solución viable para digitalizar el sector veterinario, con enfoque social, escalabilidad comercial y un modelo claro de monetización.')

add_heading(doc, '22. ANEXOS', 1)
add_table(doc, ['Anexo', 'Contenido'], [
    ['A1', 'Supuestos financieros detallados'],
    ['A2', 'Mapa de procesos del MVP'],
    ['A3', 'Propuesta de diseño visual'],
    ['A4', 'Lista de requerimientos funcionales'],
    ['A5', 'Glosario y definiciones']
])

add_heading(doc, 'Cierre', 1)
p = doc.add_paragraph()
p.add_run('Este documento deja una base más profesional para Word. ').bold = True
p.add_run('Ahora incluye tablas, valores y secciones faltantes para una presentación más completa y ejecutiva.')

doc.save('happy_paws_proyecto_ejecutivo.docx')
print('Generado: happy_paws_proyecto_ejecutivo.docx')
