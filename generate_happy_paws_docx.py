from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH


OUTPUT_FILE = 'HappyPaws_V2_1_.docx'


def add_heading(doc, text, level=1):
    paragraph = doc.add_paragraph()
    paragraph.style = f'Heading {level}'
    run = paragraph.add_run(text)
    run.bold = True
    return paragraph


def add_paragraph(doc, text=''):
    return doc.add_paragraph(text)


def add_bullet(doc, text, level=0):
    style = 'List Bullet' if level == 0 else 'List Bullet 2'
    paragraph = doc.add_paragraph(style=style)
    paragraph.add_run(text)
    return paragraph


def add_numbered(doc, text):
    paragraph = doc.add_paragraph(style='List Number')
    paragraph.add_run(text)
    return paragraph


def add_label_value(doc, label, value):
    paragraph = doc.add_paragraph()
    label_run = paragraph.add_run(f'{label}: ')
    label_run.bold = True
    paragraph.add_run(value)
    return paragraph


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    header_cells = table.rows[0].cells
    for index, header in enumerate(headers):
        header_cells[index].text = header
    for row in rows:
        cells = table.add_row().cells
        for index, value in enumerate(row):
            cells[index].text = str(value)
    return table


def money(value):
    return f'${value:,.0f}'.replace(',', '.') + ' COP'


doc = Document()
styles = doc.styles
styles['Normal'].font.name = 'Aptos'
styles['Normal'].font.size = Pt(10.5)
for name in ['Heading 1', 'Heading 2', 'Heading 3']:
    styles[name].font.name = 'Aptos'

section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

cover = doc.add_paragraph()
cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = cover.add_run('HAPPY PAWS\nVERSIÓN 2.1 ACTUALIZADA')
run.bold = True
run.font.size = Pt(20)

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('Presupuesto de elaboración, cronograma de Sprints y arquitectura técnica del MVP')
run.font.size = Pt(12)

for line in [
    'Servicio Nacional de Aprendizaje - SENA',
    'Centro de Comercio y Turismo',
    'Tecnólogo en Análisis y Desarrollo de Software - ADSO | Trimestre VI',
    'Cliente: Veterinaria V+Kotiando · Ibagué, Tolima, Colombia',
    'Fecha de emisión: 30 de mayo de 2026'
]:
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run(line)

cover_note = doc.add_paragraph()
cover_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
cover_note.add_run('Documento mejorado con tablas, valores estimados y secciones faltantes integradas a partir del PDF técnico.')

doc.add_page_break()

add_heading(doc, '1. CONTEXTO DEL PROYECTO Y ALCANCE', 1)
add_paragraph(doc, 'El presente documento consolida el presupuesto de elaboración, el cronograma de Sprints y la arquitectura técnica base del proyecto Happy Paws, desarrollado bajo metodología Scrum para la veterinaria V+Kotiando en Ibagué, Tolima. La propuesta combina el enfoque de gestión académica ADSO con una visión funcional y técnica del MVP para el ecosistema de bienestar animal.')
add_table(doc, ['Elemento', 'Descripción'], [
    ['Tipo de proyecto', 'Sistema de gestión veterinaria web y móvil con enfoque MVP'],
    ['Metodología', 'Scrum con entregables por Sprint y revisión continua'],
    ['Objetivo principal', 'Digitalizar citas, historiales, adopciones y control operativo de la veterinaria'],
    ['Alcance inicial', 'Registro de usuarios, mascotas, citas, historial clínico, adopciones y panel admin'],
    ['Duración estimada', '8 semanas de desarrollo activo distribuidas en 4 Sprints de 2 semanas']
])
add_bullet(doc, 'Las cifras de costos son estimadas con base en el mercado colombiano TI 2025 y sirven como marco de negociación tecnológica.')
add_bullet(doc, 'El stack técnico sugerido en el PDF es moderno, desacoplado y listo para escalar desde el día uno.')

add_heading(doc, '2. PRESUPUESTO - RECURSOS HUMANOS', 1)
add_paragraph(doc, 'El componente humano concentra la mayor parte del presupuesto, como ocurre en proyectos de software de alcance medio. Las tarifas son referenciales y pueden ajustarse según el perfil del proveedor o del equipo interno.')
add_table(doc, ['Rol', 'Horas estimadas', 'Tarifa por hora', 'Subtotal'], [
    ['Scrum Master', '40', money(50000), money(2000000)],
    ['Desarrollador Frontend', '60', money(45000), money(2700000)],
    ['Desarrollador Backend', '60', money(45000), money(2700000)],
    ['QA / Tester', '50', money(30000), money(1500000)],
    ['Diseño UX/UI', '45', money(40000), money(1800000)],
    ['DevOps / Despliegue', '22', money(50000), money(1100000)]
])
add_label_value(doc, 'Total recursos humanos estimado', money(11800000))
add_bullet(doc, 'Nota: las tarifas se construyen como referencia de mercado para perfiles junior-mid y pueden renegociarse según el alcance final.')

add_heading(doc, '3. PRESUPUESTO - RECURSOS TECNOLÓGICOS', 1)
add_paragraph(doc, 'El PDF técnico recomienda un stack de bajo costo de entrada y alta escalabilidad. Se privilegian herramientas gratuitas, open source o freemium durante el desarrollo.')
add_table(doc, ['Herramienta / Plataforma', 'Uso', 'Costo estimado'], [
    ['GitHub', 'Control de versiones y colaboración', money(0)],
    ['Trello / Jira Free', 'Gestión de tareas y Sprints', money(0)],
    ['Figma', 'Diseño UX/UI y prototipado', money(0)],
    ['Postman', 'Pruebas de API REST', money(0)],
    ['Docker', 'Empaquetado y despliegue local', money(0)],
    ['Spring Boot / React', 'Backend y frontend principales', money(0)],
    ['Jupyter / LibreOffice', 'Documentación y análisis auxiliar', money(0)]
])
add_bullet(doc, 'La mayoría del stack puede operar sin licenciamiento pago en fase de desarrollo.')
add_bullet(doc, 'Las herramientas comerciales solo se justifican cuando el proyecto entre a producción y requiera soporte ampliado.')

add_heading(doc, '4. PRESUPUESTO - HARDWARE E INFRAESTRUCTURA', 1)
add_paragraph(doc, 'Durante la fase de desarrollo, la infraestructura directa se mantiene controlada para evitar sobredimensionar el costo inicial.')
add_table(doc, ['Recurso', 'Cantidad', 'Valor'], [
    ['Dominio .com', '1', money(80000)],
    ['Hosting / entorno temporal', '1', money(48000)],
    ['Certificado SSL', '1', money(0)],
    ['Almacenamiento adicional', '1', money(0)],
    ['Total hardware e infraestructura', '-', money(128000)]
])
add_bullet(doc, 'En producción, se recomienda migrar a un plan pago en Railway, Render, DigitalOcean o AWS según la demanda real.')

add_heading(doc, '5. OTROS COSTOS DEL PROYECTO', 1)
add_paragraph(doc, 'Se incluyen costos de contingencia y la reserva mínima para ajustes de alcance, cambios menores y validación de entregables.')
add_table(doc, ['Concepto', 'Base de cálculo', 'Valor'], [
    ['Contingencia técnica', '12% sobre recursos humanos + infraestructura', money(1431360)],
    ['Documentación y ajustes', 'Bolsa operativa de cierre', money(0)],
    ['Total otros costos', '-', money(1431360)]
])
add_bullet(doc, 'La contingencia actúa como margen para cubrir riesgos de alcance, ajustes de sprint o retrabajo menor.')

add_heading(doc, '6. RESUMEN Y TOTAL DEL PRESUPUESTO', 1)
add_table(doc, ['Categoría', 'Valor'], [
    ['Recursos humanos', money(11800000)],
    ['Recursos tecnológicos', money(0)],
    ['Hardware e infraestructura', money(128000)],
    ['Otros costos', money(1431360)],
    ['Subtotal estimado', money(13369360)],
    ['Precio propuesto al cliente', money(16957392)]
])
add_bullet(doc, 'El precio propuesto al cliente incluye un margen de negociación adicional y puede ajustarse con descuento por pronto pago o modalidad por Sprints.')
add_bullet(doc, 'Si el proyecto se entrega por fases, también es viable mantener un esquema de mantenimiento mensual posterior.')

add_heading(doc, '7. CRONOGRAMA DE SPRINTS', 1)
add_paragraph(doc, 'El cronograma se organiza en 4 Sprints de 2 semanas cada uno, para un total de 8 semanas de trabajo activo.')
add_table(doc, ['Sprint', 'Fechas', 'Objetivo principal', 'Entregables'], [
    ['Sprint 1', '01/03/2025 - 14/03/2025', 'Base funcional y autenticación', 'Login JWT, roles, perfil de usuario y estructura inicial'],
    ['Sprint 2', '15/03/2025 - 28/03/2025', 'Gestión de mascotas y citas', 'CRUD de mascotas, agenda, historial básico y tablero inicial'],
    ['Sprint 3', '29/03/2025 - 11/04/2025', 'Módulo social y clínico', 'Historial médico, adopciones, reportes y moderación'],
    ['Sprint 4', '12/04/2025 - 26/04/2025', 'Cierre y estabilización', 'QA, correcciones, despliegue, documentación y aprobación']
])
add_bullet(doc, 'Cada Sprint incluye planeación, desarrollo, revisión, retrospectiva y ajuste de backlog.')

add_heading(doc, '8. PRODUCT BACKLOG - DISTRIBUCIÓN POR SPRINT', 1)
add_paragraph(doc, 'El siguiente backlog resume las historias de usuario principales del sistema Happy Paws organizadas por prioridad, estimación y Sprint sugerido.')
add_table(doc, ['ID', 'Historia de usuario', 'Prioridad', 'SP', 'Sprint'], [
    ['HU-01', 'Como usuario quiero registrarme e iniciar sesión de forma segura', 'Must', '8', 'Sprint 1'],
    ['HU-02', 'Como dueño quiero administrar el perfil de mis mascotas', 'Must', '13', 'Sprint 1'],
    ['HU-03', 'Como dueño quiero agendar y cancelar citas veterinarias', 'Must', '13', 'Sprint 2'],
    ['HU-04', 'Como veterinaria quiero registrar historial clínico', 'Must', '13', 'Sprint 2'],
    ['HU-05', 'Como administrador quiero gestionar usuarios y roles', 'Must', '8', 'Sprint 1'],
    ['HU-06', 'Como refugio quiero publicar mascotas en adopción', 'Must', '13', 'Sprint 3'],
    ['HU-07', 'Como usuario quiero reportar abandono o maltrato con geolocalización', 'Should', '8', 'Sprint 3'],
    ['HU-08', 'Como administrador quiero moderar reportes y contenidos', 'Should', '8', 'Sprint 3'],
    ['HU-09', 'Como dueño quiero recibir recordatorios y notificaciones', 'Should', '5', 'Sprint 2'],
    ['HU-10', 'Como veterinaria quiero consultar estadísticas básicas', 'Should', '8', 'Sprint 4'],
    ['HU-11', 'Como usuario quiero adjuntar fotos y documentos', 'Could', '8', 'Sprint 4'],
    ['HU-12', 'Como dueño quiero ver el estado de mis solicitudes', 'Should', '5', 'Sprint 3'],
    ['HU-13', 'Como administrador quiero consultar métricas globales', 'Must', '12', 'Sprint 4']
])
add_bullet(doc, 'Total estimado: 122 Story Points. La velocidad del equipo puede ajustarse según la experiencia real y la disponibilidad.')

add_heading(doc, '9. DEFINICIÓN DE DONE (DoD)', 1)
add_paragraph(doc, 'Un Sprint se considera terminado únicamente cuando se cumplen todos los criterios de calidad, funcionalidad y validación del equipo.')
add_table(doc, ['Criterio', 'Descripción'], [
    ['Código revisado', 'El desarrollo está versionado, revisado y sin conflictos graves'],
    ['Pruebas aprobadas', 'Las pruebas funcionales y básicas de integración pasan correctamente'],
    ['Documentación', 'El cambio cuenta con registro técnico mínimo y manual si aplica'],
    ['Validación del PO', 'El Product Owner revisa y acepta el entregable'],
    ['Sin bloqueos', 'No existen defectos críticos pendientes al cierre del Sprint']
])
add_bullet(doc, 'La aprobación del Sprint depende de la verificación del Scrum Master y del Product Owner.')

add_heading(doc, '10. CONTROL PRESUPUESTAL POR SPRINT', 1)
add_paragraph(doc, 'Registre el costo real al finalizar cada Sprint para controlar la varianza presupuestal y tomar decisiones correctivas oportunas.')
add_table(doc, ['Sprint', 'Presupuesto planificado', 'Costo real', 'Varianza'], [
    ['Sprint 1', money(4239348), 'Por registrar', 'Por calcular'],
    ['Sprint 2', money(4239348), 'Por registrar', 'Por calcular'],
    ['Sprint 3', money(4239348), 'Por registrar', 'Por calcular'],
    ['Sprint 4', money(4239348), 'Por registrar', 'Por calcular']
])
add_bullet(doc, 'Varianza = Costo planificado - Costo real. Si el acumulado supera el -10%, debe activarse la contingencia.')

add_heading(doc, '11. ANÁLISIS DE RIESGOS DEL PROYECTO', 1)
add_paragraph(doc, 'La gestión de riesgos se revisará al inicio de cada Sprint y se actualizará según la evolución del proyecto.')
add_table(doc, ['Riesgo', 'Probabilidad', 'Impacto', 'Mitigación'], [
    ['Cambios frecuentes de alcance', 'Alta', 'Alto', 'Aprobar backlog congelado por Sprint y priorizar MVP'],
    ['Retrasos técnicos', 'Media', 'Alto', 'Definir tareas pequeñas y revisiones frecuentes'],
    ['Baja adopción del cliente', 'Media', 'Alto', 'Validación temprana con usuarios y demos por Sprint'],
    ['Fallas de despliegue', 'Baja', 'Medio', 'Usar Docker y entornos separados por perfil'],
    ['Problemas de datos o seguridad', 'Baja', 'Crítico', 'Autenticación JWT, roles y validación de entradas']
])
add_bullet(doc, 'La responsabilidad del seguimiento de riesgos recae en el Scrum Master, con reporte inmediato al Product Owner e instructor.')

add_heading(doc, '12. APROBACIÓN Y FIRMAS DEL DOCUMENTO', 1)
add_paragraph(doc, 'El presente presupuesto y cronograma ha sido revisado y puede ser validado por los responsables del proyecto.')
add_table(doc, ['Rol', 'Nombre', 'Firma'], [
    ['Product Owner / Cliente', 'V+Kotiando', '________________'],
    ['Scrum Master', '________________', '________________'],
    ['Equipo ADSO', '________________', '________________'],
    ['Instructor / Tutor', '________________', '________________']
])

doc.add_page_break()

add_heading(doc, '13. ¿QUÉ ES HAPPY PAWS?', 1)
add_paragraph(doc, 'Happy Paws es una plataforma tecnológica que conecta dueños de mascotas, veterinarias, refugios y entidades de bienestar animal en Colombia. No es una EPS veterinaria: es el ecosistema digital donde ocurren las citas, los historiales, las adopciones y la protección animal.')
add_table(doc, ['Actor', 'Necesidad que resuelve', 'Valor entregado'], [
    ['Dueños', 'Perfil y agenda de mascotas', 'Acceso centralizado a información y recordatorios'],
    ['Veterinarias', 'Gestión y visibilidad digital', 'Mejor trazabilidad de pacientes y servicios'],
    ['Entidades / refugios', 'Protección y adopciones', 'Más control y trazabilidad en adopción y reportes']
])

add_heading(doc, '14. ARQUITECTURA DEL SISTEMA', 1)
add_paragraph(doc, 'El stack sugerido es moderno, desacoplado y listo para escalar desde el día uno.')
add_table(doc, ['Capa', 'Tecnología sugerida', 'Motivo'], [
    ['Frontend', 'React o Angular', 'SPA responsiva para web y móvil'],
    ['Backend', 'Spring Boot', 'REST API, escalabilidad y seguridad'],
    ['Autenticación', 'JWT + Spring Security', 'Control de acceso por roles'],
    ['Base de datos', 'PostgreSQL', 'Robustez y soporte relacional'],
    ['ORM / migraciones', 'JPA/Hibernate + Flyway o Liquibase', 'Mantenibilidad y control de cambios'],
    ['Despliegue', 'Docker + AWS / GCP', 'Portabilidad y escalabilidad']
])

add_heading(doc, '15. MÓDULOS FUNCIONALES DEL MVP', 1)
add_table(doc, ['Módulo', 'Descripción', 'Estado'], [
    ['Usuarios y roles', 'Registro, login JWT y permisos diferenciados', 'Incluido'],
    ['Perfil de mascota', 'Nombre, raza, edad, peso, foto y vacunas', 'Incluido'],
    ['Citas veterinarias', 'Agendar, cancelar y consultar historial', 'Incluido'],
    ['Historial clínico', 'Consultas, diagnósticos, medicamentos y vacunas', 'Incluido'],
    ['Módulo social', 'Adopciones, abandono y maltrato con geolocalización', 'Incluido'],
    ['Panel admin', 'Gestión de usuarios, veterinarias, reportes y estadísticas', 'Incluido']
])

add_heading(doc, '16. DISEÑO DE BASE DE DATOS', 1)
add_table(doc, ['Entidad', 'Campos principales', 'Relación clave'], [
    ['User', 'id, nombre, email, password, rol, createdAt, updatedAt', 'Base del sistema'],
    ['Pet', 'id, nombre, raza, edad, peso, foto, userId, createdAt, updatedAt', 'Pertenece a un usuario'],
    ['Vet', 'id, nombre, dirección, servicios, horarios, createdAt, updatedAt', 'Relacionada con citas'],
    ['Appointment', 'id, fecha, estado, petId, vetId, userId, createdAt, updatedAt', 'Une mascota, veterinaria y dueño'],
    ['MedicalRecord', 'diagnóstico, medicamentos, petId, createdAt, updatedAt', 'Historial por mascota'],
    ['Report', 'tipo, descripción, lat, lng, userId, createdAt, updatedAt', 'Reporte ciudadano o administrativo']
])
add_bullet(doc, 'Todas las entidades incluyen createdAt y updatedAt para auditoría desde el MVP.')

add_heading(doc, '17. SEGURIDAD Y AUTENTICACIÓN JWT', 1)
add_paragraph(doc, 'Spring Security filtra cada request. Los roles definen el acceso a rutas específicas: /admin para administradores, /vet para veterinarias autenticadas y /pets para dueños verificados.')
add_table(doc, ['Elemento', 'Descripción'], [
    ['Token', 'JWT con expiración de 24 horas'],
    ['Refresh token', 'Opcional para mantener sesión sin relogueo frecuente'],
    ['Acceso por rol', 'Restricción de rutas según permisos'],
    ['Validación', 'Cada request debe validar firma y expiración'],
    ['Buenas prácticas', 'Contraseñas cifradas, control de sesión y protección contra abuso']
])

add_heading(doc, '18. ENDPOINTS REST PRINCIPALES', 1)
add_table(doc, ['Método', 'Endpoint', 'Uso'], [
    ['POST', '/api/v1/auth/register', 'Registro de usuario'],
    ['POST', '/api/v1/auth/login', 'Inicio de sesión'],
    ['GET/POST', '/api/v1/pets', 'Consulta y creación de mascotas'],
    ['GET', '/api/v1/pets/{id}/history', 'Historial de una mascota'],
    ['GET', '/api/v1/vets', 'Listado de veterinarias'],
    ['POST', '/api/v1/appointments', 'Creación de citas'],
    ['PUT', '/api/v1/appointments/{id}/cancel', 'Cancelación de cita'],
    ['GET', '/api/v1/adoptions', 'Listado de adopciones'],
    ['POST', '/api/v1/reports', 'Creación de reportes'],
    ['GET', '/api/v1/admin/stats', 'Indicadores del panel administrativo']
])
add_bullet(doc, 'El versionado /api/v1 debe mantenerse desde el inicio para facilitar evolución sin romper integraciones.')

add_heading(doc, '19. ROADMAP TÉCNICO', 1)
add_table(doc, ['Fase', 'Duración aproximada', 'Objetivo', 'Entregables'], [
    ['Fase 1', 'Mes 1-3', 'MVP funcional', 'Auth JWT, perfiles, citas, historial básico y panel admin'],
    ['Fase 2', 'Mes 4-6', 'Tracción', 'Adopciones, reportes geolocalizados, notificaciones push y app móvil'],
    ['Fase 3', 'Mes 7-10', 'Monetización', 'Pagos con Wompi/Stripe, membresías veterinarias y analytics avanzado'],
    ['Fase 4', 'Mes 11+', 'Escala', 'Microservicios, alianzas con alcaldías e integración pública']
])

add_heading(doc, '20. MODELO DE NEGOCIO Y MÉTRICAS CLAVE', 1)
add_table(doc, ['Línea de negocio', 'Descripción', 'Valor de referencia'], [
    ['Freemium B2C', 'Plan gratuito para dueños y premium con recordatorios y telemedicina', 'A validar desde Fase 2'],
    ['SaaS B2B', 'Suscripción mensual para veterinarias', '$50k - $150k COP/mes'],
    ['Alianzas públicas', 'Contratos con alcaldías para fauna urbana y reportes', 'Ingresos por convenio']
])
add_table(doc, ['Métrica', 'Meta MVP', 'Observación'], [
    ['Usuarios activos', '500', 'Meta al mes 3'],
    ['Veterinarias aliadas', '20', 'Meta al mes 3'],
    ['Retención', '60%', 'Usuarios del mes 2'],
    ['Conversión a piloto', '10%', 'Referida a leads calificados']
])

add_heading(doc, '21. QUÉ NO INCLUIR EN EL MVP', 1)
add_paragraph(doc, 'Mantener el alcance del MVP es tan importante como lo que se construye. Estas funcionalidades deben dejarse para fases posteriores.')
add_table(doc, ['Funcionalidad', 'Razón para excluirla del MVP', 'Fase sugerida'], [
    ['Telemedicina', 'Requiere infraestructura costosa y validación legal adicional', 'Post-tracción'],
    ['E-commerce', 'Añade complejidad logística innecesaria', 'Fase 3'],
    ['Microservicios', 'El MVP debe iniciar como monolito modular', 'Escala'],
    ['Gamificación', 'No es prioritaria para validar el mercado', 'Fase 2']
])
add_bullet(doc, 'El enfoque ganador es construir primero una experiencia simple y confiable antes de ampliar funciones accesorias.')

add_heading(doc, '22. CIERRE Y PRÓXIMOS PASOS', 1)
add_paragraph(doc, 'Happy Paws queda consolidado como una propuesta viable para digitalizar el sector veterinario con enfoque social, técnico y comercial. El siguiente paso natural es validar el alcance final, aprobar presupuesto y arrancar la construcción del MVP por Sprints.')
add_table(doc, ['Paso', 'Responsable', 'Resultado esperado'], [
    ['Validar alcance', 'Product Owner', 'Backlog priorizado y congelado por Sprint'],
    ['Ajustar presupuesto', 'Equipo ADSO / Cliente', 'Cifras finales aprobadas'],
    ['Iniciar desarrollo', 'Equipo técnico', 'MVP en construcción'],
    ['Abrir piloto', 'Cliente y equipo', 'Primera validación con usuarios reales']
])

add_heading(doc, 'ANEXOS', 1)
add_table(doc, ['Anexo', 'Contenido'], [
    ['A1', 'Supuestos financieros y criterios de cálculo'],
    ['A2', 'Lista ampliada de historias de usuario'],
    ['A3', 'Mapa de arquitectura y despliegue'],
    ['A4', 'Glosario técnico'],
    ['A5', 'Plantilla de seguimiento por Sprint']
])

add_paragraph(doc, 'Documento generado y actualizado a partir de HappyPaws_V2_1_.docx y Happy-Paws.pdf.')

doc.save(OUTPUT_FILE)
print(f'Generado: {OUTPUT_FILE}')
