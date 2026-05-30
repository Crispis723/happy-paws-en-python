# HAPPY PAWS
# VERSIÓN 3.2 - DEFINITIVA CORREGIDA

**Fecha de actualización:** 30 de mayo de 2026  
**Cliente:** Veterinaria V+Kotiando  
**Proyecto:** Plataforma SaaS multiempresa para bienestar animal en Colombia  
**Stack:** React, Spring Boot, PostgreSQL, JWT + Spring Security, Docker, Cloudinary, AWS/Railway

## ÍNDICE GENERAL
1. Resumen Ejecutivo
2. Módulos Obligatorios del MVP
3. Stack Tecnológico y Arquitectura
4. Costos Corregidos del Proyecto
5. Cronograma con Fechas Reales
6. Aspectos Legales Colombianos
7. Seguridad Adicional y Cumplimiento Técnico
8. Story Points Realistas
9. Endpoints REST y Códigos de Error
10. Análisis de Competencia
11. Análisis de Riesgos Legales y Técnicos
12. Definición de Done Mejorada
13. Qué No Incluir en el MVP
14. Conclusión y Próximos Pasos
15. Anexos

## 1. RESUMEN EJECUTIVO
Happy Paws es una plataforma SaaS multiempresa para bienestar animal en Colombia. Conecta dueños de mascotas, veterinarias, refugios y entidades de bienestar animal en un solo ecosistema digital orientado a citas, historiales, adopciones, reportes ciudadanos y control administrativo.

| Elemento | Valor / alcance | Observación |
|---|---|---|
| Mercado objetivo inicial | Bogotá, Medellín e Ibagué | Entrada comercial por ciudades con alta densidad de mascotas |
| Enfoque de negocio | SaaS B2B + componente social B2C | Vets y refugios como clientes principales |
| Inversión requerida | COP 18.860.000 | Costo total MVP corregido |
| Precio sugerido al cliente | COP 24.518.000 | Margen comercial de 30% |

## 2. MÓDULOS OBLIGATORIOS DEL MVP

| Módulo | Incluye | Resultado esperado |
|---|---|---|
| Registro e inicio de sesión | JWT + roles: Administrador, Veterinaria, Propietario, Refugio | Acceso seguro y segmentado |
| CRUD de mascotas | Nombre, raza, edad, peso, foto, vacunas | Ficha unificada por mascota |
| Agenda de citas | Crear, cancelar, reprogramar, notificar | Control operativo de agenda |
| Historial clínico | Consultas, diagnósticos, medicamentos, vacunas | Trazabilidad de atención médica |
| Módulo de adopciones | Publicar, postular, aprobar, rechazar | Flujo digital de adopción |
| Reportes ciudadanos | Maltrato o abandono con geolocalización y seguimiento | Canal de protección animal |
| Panel administrativo | Métricas, usuarios, moderación | Control del ecosistema |

## 3. STACK TECNOLÓGICO Y ARQUITECTURA
La arquitectura recomendada es modular, segura y escalable. Se prioriza desacoplar frontend, backend y almacenamiento de imágenes para facilitar mantenimiento y despliegue.

| Capa | Tecnología | Uso |
|---|---|---|
| Frontend | React | Interfaz web responsiva y mantenible |
| Backend | Spring Boot | API REST principal del negocio |
| Base de datos | PostgreSQL (base) / Oracle Database (opcional empresarial) | Persistencia relacional y alternativa corporativa |
| Autenticación | JWT + Spring Security | Seguridad y control de acceso |
| Contenedores | Docker | Portabilidad y despliegue reproducible |
| Imágenes | Cloudinary | Gestión de fotos de mascotas y archivos |
| Despliegue | AWS / Railway | Publicación y escalamiento inicial |

| Componente | Decisión técnica | Motivo |
|---|---|---|
| API | REST versionada /api/v1 | Facilita evolución sin romper integraciones |
| Seguridad | Cifrado de contraseñas con bcrypt | Protección robusta de credenciales |
| Datos | Validación backend obligatoria | No depender solo del frontend |
| Auditoría | Logs de acciones críticas | Trazabilidad legal y operativa |

| Gestor de base de datos | Costo estimado | Observación |
|---|---|---|
| PostgreSQL | COP 0 | Opción recomendada por costo y escalabilidad para el MVP |
| Oracle Database administrado | COP 1.200.000 | Alternativa empresarial estimada basada en mercado colombiano 2025-2026 |

## 4. COSTOS CORREGIDOS DEL PROYECTO
Los costos originales estaban subestimados porque no reflejaban tarifas reales de mercado para Colombia 2025-2026, ni incluían infraestructura mensual, contingencia suficiente, ni el costo real de perfiles junior-mid con experiencia en React, Spring Boot, QA, diseño UX/UI y DevOps.

### 4.1 Recursos humanos

| Rol | Horas | Tarifa por hora | Subtotal |
|---|---:|---:|---:|
| Scrum Master | 60 | COP 35.000 | COP 2.100.000 |
| Desarrollador Frontend | 100 | COP 40.000 | COP 4.000.000 |
| Desarrollador Backend | 100 | COP 40.000 | COP 4.000.000 |
| QA / Tester | 50 | COP 35.000 | COP 1.750.000 |
| Diseñador UX/UI | 70 | COP 35.000 | COP 2.450.000 |
| DevOps | 40 | COP 45.000 | COP 1.800.000 |
| TOTAL recursos humanos | 420 | - | COP 16.100.000 |

### 4.2 Infraestructura primer mes

| Infraestructura primer mes | Valor |
|---|---:|
| Servidor cloud | COP 120.000 |
| Base de datos administrada | COP 80.000 |
| Cloudinary | COP 40.000 |
| Correo transaccional | COP 30.000 |
| Dominio .com (prorrateado) | COP 10.000 |
| Monitoreo | COP 20.000 |
| TOTAL infraestructura | COP 300.000 |

### 4.3 Consolidado

| Concepto | Valor |
|---|---:|
| Total recursos humanos | COP 16.100.000 |
| Infraestructura primer mes | COP 300.000 |
| Base para contingencia (RH + Inf) | COP 16.400.000 |
| Contingencia (15%) | COP 2.460.000 |
| Costo total desarrollo MVP | COP 18.860.000 |
| Precio sugerido al cliente (30%) | COP 24.518.000 |

Los precios presentados no incluyen IVA (19%) u otros impuestos aplicables según la legislación colombiana vigente. En caso de aplicar, serán liquidados adicionalmente.

Si el cliente exige Oracle como gestor de base de datos, debe añadirse una bolsa adicional estimada de COP 1.200.000 para el primer mes del MVP, considerando el servicio administrado, soporte y operación básica.

## 5. CRONOGRAMA CON FECHAS REALES

| Sprint | Fechas | Objetivo | Story Points |
|---|---|---|---:|
| Sprint 1 | 15/06/2026 - 28/06/2026 | Base y autenticación | 25 SP |
| Sprint 2 | 29/06/2026 - 12/07/2026 | Mascotas y citas | 28 SP |
| Sprint 3 | 13/07/2026 - 26/07/2026 | Adopciones y reportes | 30 SP |
| Sprint 4 | 27/07/2026 - 09/08/2026 | Panel admin y despliegue | 25 SP |

**Fecha de inicio del proyecto:** 15 de junio de 2026  
**Fecha de entrega final (estabilización):** 16 de agosto de 2026

Velocidad estimada del equipo: 6-8 Story Points por semana por persona. Con 4 personas activas, se espera completar entre 24 y 32 SP por Sprint.

## 6. ASPECTOS LEGALES COLOMBIANOS
Esta sección corrige una omisión crítica del documento anterior: la plataforma debe operar con cumplimiento legal colombiano desde el diseño, no como ajuste posterior.

### 6.1 Ley 1581 de 2012 - Protección de Datos Personales
La Ley 1581 de 2012 regula el tratamiento de datos personales en Colombia. Su principio central es el Habeas Data, entendido como el derecho de toda persona a conocer, actualizar, rectificar y suprimir su información cuando sea procedente.

| Actor | Responsabilidad |
|---|---|
| Responsable del tratamiento | Define finalidades, recopila autorizaciones, responde solicitudes y protege la base de datos |
| Encargado del tratamiento | Procesa datos por cuenta del responsable, implementa medidas de seguridad y atiende instrucciones técnicas |
| Titular | Puede consultar, actualizar, rectificar y solicitar eliminación cuando aplique |

| Derecho del titular | Descripción | Plazo de respuesta |
|---|---|---|
| Consultar | Conocer qué datos se tratan y cómo se usan | 10 días hábiles |
| Actualizar / rectificar | Corregir información incompleta o inexacta | 10 días hábiles |
| Eliminar / suprimir | Solicitar supresión cuando proceda legalmente | 10 días hábiles |

Si la solicitud no puede resolverse en 10 días hábiles, la organización debe responder dentro del plazo legal aplicable y dejar trazabilidad del caso.

### 6.2 Aviso de privacidad obligatorio
**Aviso de privacidad.** Responsable del tratamiento: Happy Paws SAS o la persona jurídica que opere la plataforma para la veterinaria aliada. Finalidades: gestionar usuarios, mascotas, citas, adopciones, reportes, comunicaciones operativas, soporte, seguridad, analítica y cumplimiento legal. Datos recolectados: nombre, cédula o documento, correo, teléfono, dirección, datos de mascotas, historial clínico y registros asociados al uso del sistema. Derechos: consultar, actualizar, rectificar, suprimir, revocar la autorización y presentar quejas ante la autoridad competente. Canal de contacto: soporte@happypaws.co o el correo oficial que defina el responsable. El registro y uso de la plataforma implica aceptación de este tratamiento de datos conforme a la ley vigente. Plazo de conservación: mientras subsista la relación contractual y durante el tiempo exigido por la normatividad aplicable. El titular podrá ejercer sus derechos por los canales oficiales habilitados.

### 6.3 Ley 1774 de 2016 - Bienestar Animal
La plataforma debe alinearse con la Ley 1774 de 2016, que reconoce a los animales como seres sintientes y refuerza el deber de protección contra el maltrato.

| Obligación | Aplicación en Happy Paws |
|---|---|
| Reportar maltrato | Debe existir un flujo de escalamiento a autoridades competentes |
| No promover conductas ilegales | Queda prohibido publicar peleas de animales, zoofilia o contenidos similares |
| Trazabilidad | Todo reporte debe conservar fecha, evidencia, ubicación y seguimiento |
| Bienestar animal | Los módulos deben promover adopción responsable, atención y cuidado |

### 6.4 Contrato de suscripción para veterinarias
**Contrato de Suscripción - cláusulas mínimas:**

| Cláusula | Contenido mínimo |
|---|---|
| 1. Objeto | Uso de la plataforma Happy Paws para la gestión de pacientes, citas, adopciones y reportes |
| 2. Alcance del servicio | Módulos contratados, soporte incluido y límites de uso |
| 3. Obligaciones del cliente | Usar la plataforma conforme a la ley, custodiar credenciales y autorizar tratamiento de datos |
| 4. Obligaciones del proveedor | Disponibilidad razonable, soporte, seguridad y protección de datos |
| 5. Terminación | Causales de suspensión, cancelación, incumplimiento y tratamiento de información al cierre |
| 6. Confidencialidad | Protección de información del negocio y de los titulares |
| 7. Tratamiento de datos | Autorización, finalidades y deberes legales |
| 8. Responsabilidad | Limitaciones razonables y canales de soporte |

### 6.5 Términos y condiciones generales
La estructura mínima del sitio web debe incluir: objeto del servicio, aceptación de condiciones, registro y cuenta de usuario, uso permitido, restricciones, propiedad intelectual, confidencialidad, tratamiento de datos, limitación de responsabilidad, suspensión del servicio, reclamaciones y ley aplicable.

### 6.6 Registro ante la SIC
Para efectos de este proyecto, el registro ante la SIC y el cumplimiento del Registro Nacional de Bases de Datos debe considerarse obligatorio cuando la base supere 5.000 titulares o cuando la operación crezca a un volumen similar que exija formalización adicional.

| Aspecto | Detalle |
|---|---|
| Autoridad | Superintendencia de Industria y Comercio (SIC) |
| Obligación | Inscripción y mantenimiento del registro de bases de datos cuando aplique |
| Sanción por incumplimiento | Hasta 2.000 salarios mínimos legales mensuales vigentes, según la ley aplicable |

## 7. SEGURIDAD ADICIONAL Y CUMPLIMIENTO TÉCNICO

| Medida | Implementación |
|---|---|
| Rate limiting | Máximo 100 peticiones por minuto por IP |
| CORS | Solo dominios autorizados y ambientes controlados |
| Validación de entradas | Validar en backend y frontend, no solo en UI |
| Logs de auditoría | Registrar quién hizo qué, cuándo y desde dónde; retención mínima de 6 meses |
| Backups automáticos | Copias diarias con verificación de restauración; retención de 30 días |
| Contraseñas | Hash con bcrypt o equivalente seguro |

| Riesgo técnico | Controles mínimos |
|---|---|
| Inyección SQL | Consultas parametrizadas, ORM, validación y pruebas básicas |
| XSS | Escape de salida, sanitización y Content Security Policy |
| Pérdida de datos | Backups, monitoreo y plan de restauración |
| Acceso no autorizado | JWT, expiración, roles y protección de rutas |

## 8. STORY POINTS REALISTAS
La estimación anterior de 122 SP en 8 semanas era demasiado ambiciosa para un equipo junior-mid. Se ajusta a una distribución realista de 108 SP y a una velocidad coherente con un equipo pequeño que trabaja en iteraciones cortas.

| Sprint | SP asignados | Justificación |
|---|---|---|
| Sprint 1 | 25 SP | Base, autenticación y estructura técnica |
| Sprint 2 | 28 SP | Mascotas, agenda y trazabilidad |
| Sprint 3 | 30 SP | Adopciones, reportes y flujo social |
| Sprint 4 | 25 SP | Panel administrativo, seguridad y despliegue |
| Total | 108 SP | Velocidad realista para el plazo y el tamaño del equipo |

Velocidad estimada del equipo: 6-8 Story Points por semana por persona. Con 4 personas activas, se espera completar entre 24 y 32 SP por Sprint.

## 9. ENDPOINTS REST Y CÓDIGOS DE ERROR

| Método | Endpoint | Descripción |
|---|---|---|
| POST | /api/v1/auth/register | Registro de usuario |
| POST | /api/v1/auth/login | Inicio de sesión |
| POST | /api/v1/auth/refresh | Refrescar token JWT |
| GET | /api/v1/pets | Listar mascotas |
| POST | /api/v1/pets | Crear mascota |
| GET | /api/v1/pets/{id} | Detalle de mascota |
| PUT | /api/v1/pets/{id} | Actualizar mascota |
| DELETE | /api/v1/pets/{id} | Eliminar mascota |
| GET | /api/v1/pets/{id}/history | Historial clínico |
| GET | /api/v1/vets | Listar veterinarias |
| GET | /api/v1/appointments | Listar citas |
| POST | /api/v1/appointments | Crear cita |
| PATCH | /api/v1/appointments/{id}/reschedule | Reprogramar cita |
| PATCH | /api/v1/appointments/{id}/cancel | Cancelar cita |
| GET | /api/v1/adoptions | Listar adopciones |
| POST | /api/v1/adoptions | Publicar adopción |
| POST | /api/v1/adoptions/{id}/apply | Postular a adopción |
| PATCH | /api/v1/adoptions/{id}/approve | Aprobar postulación |
| PATCH | /api/v1/adoptions/{id}/reject | Rechazar postulación |
| GET | /api/v1/reports | Listar reportes |
| POST | /api/v1/reports | Crear reporte |
| GET | /api/v1/admin/stats | Métricas admin |
| GET | /api/v1/admin/users | Gestión de usuarios |

| Código | Significado | Ejemplo |
|---|---|---|
| 200 OK | Petición exitosa | GET /api/v1/pets |
| 201 Created | Recurso creado | POST /api/v1/pets |
| 400 Bad Request | Datos inválidos | Email mal formado |
| 401 Unauthorized | No autenticado | Token faltante |
| 403 Forbidden | Sin permisos | Usuario común accede a /admin |
| 404 Not Found | Recurso no existe | Pet ID inválido |
| 500 Internal Error | Error del servidor | Excepción no manejada |

## 10. ANÁLISIS DE COMPETENCIA

| Competidor | Precio (COP/mes) | Ventajas | Desventajas |
|---|---|---|---|
| Vetmanager | COP 180.000 - 350.000 | Establecido, muchas funciones | Caro, sin adopciones ni reportes |
| G247 | COP 150.000 - 280.000 | Buen soporte | Curva de aprendizaje alta |
| MVZ Cloud | COP 70.000 - 150.000 | Colombiano, económico | Poca escalabilidad |
| VetSys | COP 100.000 - 200.000 | Opción conocida | Menor foco en bienestar animal |
| Happy Paws | COP 79.000 - 299.000 | Adopciones + reportes + bienestar animal | Nuevo en el mercado |

## 11. ANÁLISIS DE RIESGOS LEGALES Y TÉCNICOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Incumplimiento de protección de datos (Ley 1581) | Media | Alto | Incluir aviso de privacidad, obtener consentimiento y firmar contrato de encargo |
| Denuncias por maltrato animal no gestionadas | Media | Alto | Establecer flujo de escalamiento a autoridades |
| Fuga de información de mascotas y dueños | Baja | Crítico | Encriptación, JWT y backups cifrados |
| Competencia con software establecido | Alta | Medio | Enfoque en adopciones y reportes diferenciales |
| Retraso en aprobaciones del cliente | Alta | Medio | Definir validaciones por sprint y responsables de aceptación |
| Rotación del equipo técnico | Media | Alto | Documentación viva, pares de respaldo y backlog priorizado |
| Dependencia de APIs de terceros | Media | Medio | Fallbacks, contratos de servicio y monitoreo de integraciones |
| Escalabilidad inesperada | Baja | Alto | Pruebas de carga, colas y capacidad incremental |

## 12. DEFINICIÓN DE DONE MEJORADA

| Criterio | Descripción |
|---|---|
| Código revisado | Aprobado por al menos 2 desarrolladores |
| Pruebas funcionales | Flujos principales probados sin fallas críticas |
| Pruebas de seguridad | Validación básica contra SQL Injection y XSS |
| Documentación | API actualizada y changelog mínimo |
| Calidad | Sin errores críticos de severidad 1 o 2 |
| Aprobación del PO | Aceptación formal del entregable |

No se considera terminado un Sprint si existe un bloqueo de seguridad, documentación incompleta o deuda técnica crítica sin plan de cierre.

## 13. QUÉ NO INCLUIR EN EL MVP
Mantener el alcance del MVP es tan importante como construirlo. Se conserva la lista de exclusiones para evitar sobrecosto y desvío funcional.

| Funcionalidad excluida | Razón |
|---|---|
| Telemedicina | Requiere infraestructura costosa y validación clínica adicional |
| E-commerce | Añade complejidad logística innecesaria |
| Microservicios | El MVP debe iniciar como monolito modular |
| Gamificación | No es prioritaria para validar el mercado inicial |

## 14. CONCLUSIÓN Y PRÓXIMOS PASOS
Happy Paws queda consolidado como una propuesta viable para digitalizar el sector veterinario con enfoque social, técnico, comercial y legal. El documento corregido ya incluye costos realistas, cronograma ajustado, legalidad colombiana, seguridad base, competidores y una definición de alcance ejecutable.

| Siguiente paso | Responsable | Resultado esperado |
|---|---|---|
| Validar alcance final | Cliente + equipo | Backlog cerrado y priorizado |
| Aprobar presupuesto | Cliente | Contrato y presupuesto listos |
| Iniciar desarrollo | Equipo TI | MVP en construcción |
| Abrir piloto | Cliente + usuarios | Validación con usuarios reales |

## 15. ANEXOS

| Anexo | Contenido |
|---|---|
| A1 | Supuestos financieros y fórmula de costos |
| A2 | Aviso de privacidad completo |
| A3 | Contrato de suscripción completo |
| A4 | Backlog resumido y criterios de aceptación |
| A5 | Mapa de arquitectura técnica |

### A2. AVISO DE PRIVACIDAD
**Aviso de privacidad.** Responsable del tratamiento: Happy Paws SAS o la persona jurídica que opere la plataforma para la veterinaria aliada. Finalidades: gestionar usuarios, mascotas, citas, adopciones, reportes, comunicaciones operativas, soporte, seguridad, analítica y cumplimiento legal. Datos recolectados: nombre, cédula o documento, correo, teléfono, dirección, datos de mascotas, historial clínico y registros asociados al uso del sistema. Derechos: consultar, actualizar, rectificar, suprimir, revocar la autorización y presentar quejas ante la autoridad competente. Canal de contacto: soporte@happypaws.co o el correo oficial que defina el responsable. El registro y uso de la plataforma implica aceptación de este tratamiento de datos conforme a la ley vigente. Plazo de conservación: mientras subsista la relación contractual y durante el tiempo exigido por la normatividad aplicable. El titular podrá ejercer sus derechos por los canales oficiales habilitados.

### A3. CONTRATO DE SUSCRIPCIÓN
**Contrato de Suscripción.** Cláusula 1. Objeto: el presente contrato regula el uso de la plataforma Happy Paws para la gestión de pacientes, citas, adopciones y reportes. Cláusula 2. Alcance del servicio: el proveedor habilita los módulos contratados, soporte funcional básico, actualizaciones menores y acompañamiento de puesta en marcha. Cláusula 3. Obligaciones del cliente: custodiar credenciales, garantizar el uso lícito del sistema y obtener las autorizaciones necesarias para tratar datos personales. Cláusula 4. Obligaciones del proveedor: mantener medidas razonables de disponibilidad, seguridad, respaldo y atención de incidentes. Cláusula 5. Terminación: cualquiera de las partes podrá terminar el contrato por incumplimiento, vencimiento o decisión mutua, preservando la trazabilidad y la información exigida por ley. Cláusula 6. Confidencialidad: las partes se obligan a no divulgar información técnica, comercial o personal a la que accedan por razón del servicio. Cláusula 7. Tratamiento de datos: el cliente autoriza el tratamiento de datos personales conforme a la Ley 1581 de 2012 y normas relacionadas. Cláusula 8. Responsabilidad: el proveedor no responderá por usos indebidos del sistema fuera del alcance contratado. Cláusula 9. Soporte: los canales y tiempos de respuesta se definirán en la orden de servicio o anexo comercial. Cláusula 10. Ley aplicable: este contrato se rige por la legislación colombiana.

### A1. SUPUESTOS FINANCIEROS
Costo base de recursos humanos = COP 16.100.000; contingencia = COP 2.460.000; costo total = COP 18.860.000; precio sugerido = COP 24.518.000.

### A4. BACKLOG RESUMIDO
Autenticación, mascotas, citas, adopciones, reportes, panel administrativo, auditoría, seguridad y despliegue.

### A5. MAPA DE ARQUITECTURA TÉCNICA
Frontend en React, backend en Spring Boot, base relacional en PostgreSQL, autenticación con JWT, despliegue en Docker y almacenamiento de imágenes en Cloudinary.
