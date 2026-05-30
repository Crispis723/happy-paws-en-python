=== INICIO DOCUMENTO HAPPY PAWS V3.3 FINAL CORREGIDA ===

# HAPPY PAWS - DOCUMENTO TÉCNICO Y COMERCIAL VERSIÓN 3.3 FINAL CORREGIDA

**Fecha de actualización:** 30 de mayo de 2026  
**Cliente:** Veterinaria V+Kotiando  
**Proyecto:** Plataforma SaaS multiempresa para bienestar animal en Colombia  
**Stack:** React, Spring Boot, PostgreSQL, JWT + Spring Security, Docker, Cloudinary, AWS/Railway

## ÍNDICE GENERAL
1. RESUMEN EJECUTIVO
2. MÓDULOS OBLIGATORIOS DEL MVP
3. STACK TECNOLÓGICO Y ARQUITECTURA
4. COSTOS CORREGIDOS DEL PROYECTO
5. MODELO DE SUSCRIPCIÓN
6. CRONOGRAMA CON FECHAS REALES
7. ASPECTOS LEGALES COLOMBIANOS
8. SEGURIDAD ADICIONAL Y CUMPLIMIENTO TÉCNICO
9. STORY POINTS REALISTAS
10. ENDPOINTS REST Y CÓDIGOS DE ERROR
11. ANÁLISIS DE COMPETENCIA
12. ANÁLISIS DE RIESGOS LEGALES Y TÉCNICOS
13. DEFINICIÓN DE DONE MEJORADA
14. QUÉ NO INCLUIR EN EL MVP
15. CONCLUSIÓN Y PRÓXIMOS PASOS
16. ANEXOS


## 1. RESUMEN EJECUTIVO

HAPPY PAWS opera bajo un modelo SaaS por SUSCRIPCIÓN MENSUAL. Las veterinarias NO compran el software; pagan una cuota mensual para acceder y usar la plataforma. El costo de desarrollo del MVP (COP 18.860.000) es una inversión inicial para la construcción de la plataforma y NO se cobra a cada veterinaria; el retorno se recupera con las suscripciones de múltiples clientes.

NOTA ACLARATORIA: El costo total de desarrollo de COP 18.860.000 (o COP 24.518.000 con margen) corresponde a la inversión inicial para construir la plataforma. En el modelo SaaS, este valor NO es pagado por cada veterinaria. Las veterinarias solo pagan la suscripción mensual. El costo de desarrollo se recupera con las suscripciones de múltiples clientes.

Breve descripción: Happy Paws conecta dueños de mascotas, veterinarias, refugios y autoridades en un ecosistema para gestión de citas, historiales, adopciones y reportes ciudadanos, con control administrativo y métricas para operadores.


## 2. MÓDULOS OBLIGATORIOS DEL MVP

| MÓDULO | INCLUYE | RESULTADO ESPERADO |
|---|---|---|
| Registro e inicio de sesión | JWT + roles: Administrador, Veterinaria, Propietario, Refugio | Acceso seguro y segmentado |
| CRUD de mascotas | Nombre, raza, edad, peso, foto, vacunas | Ficha unificada por mascota |
| Agenda de citas | Crear, cancelar, reprogramar, notificar | Control operativo de agenda |
| Historial clínico | Consultas, diagnósticos, medicamentos, vacunas | Trazabilidad de atención médica |
| Módulo de adopciones | Publicar, postular, aprobar, rechazar | Flujo digital de adopción |
| Reportes ciudadanos | Maltrato o abandono con geolocalización y seguimiento | Canal de protección animal |
| Panel administrativo | Métricas, usuarios, moderación | Control del ecosistema |


## 3. STACK TECNOLÓGICO Y ARQUITECTURA

Arquitectura recomendada: frontend en React, backend en Spring Boot, base relacional PostgreSQL (opcional Oracle para clientes empresariales), autenticación con JWT + Spring Security, contenedores Docker, imágenes en Cloudinary y despliegue en AWS o Railway.

| Capa | TECNOLOGÍA | USO |
|---|---|---|
| Frontend | React | Interfaz web responsiva |
| Backend | Spring Boot | API REST versionada (/api/v1) |
| Base de datos | PostgreSQL / Oracle (opcional) | Persistencia relacional |
| Autenticación | JWT + Spring Security | Control de acceso y roles |
| Contenedores | Docker | Despliegue reproducible |
| Imágenes | Cloudinary | Gestión de fotos |
| Despliegue | AWS / Railway | Entorno productivo |


## 4. COSTOS CORREGIDOS DEL PROYECTO

Los cálculos a continuación reflejan el costo de desarrollo del MVP como inversión inicial (NO cobrable por veterinaria en el modelo SaaS):

### 4.1 Recursos humanos

| Rol | HORAS | TARIFA POR HORA | SUBTOTAL |
|---|---:|---:|---:|
| Scrum Master | 60 | COP 35.000 | COP 2.100.000 |
| Desarrollador Frontend | 100 | COP 40.000 | COP 4.000.000 |
| Desarrollador Backend | 100 | COP 40.000 | COP 4.000.000 |
| QA / Tester | 50 | COP 35.000 | COP 1.750.000 |
| Diseñador UX/UI | 70 | COP 35.000 | COP 2.450.000 |
| DevOps | 40 | COP 45.000 | COP 1.800.000 |
| TOTAL recursos humanos | 420 | - | COP 16.100.000 |

### 4.2 Infraestructura (primer mes)

| INFRAESTRUCTURA | VALOR |
|---|---:|
| Servidor cloud | COP 120.000 |
| Base de datos administrada | COP 80.000 |
| Cloudinary | COP 40.000 |
| Correo transaccional | COP 30.000 |
| Dominio .com (prorrateado) | COP 10.000 |
| Monitoreo | COP 20.000 |
| TOTAL infraestructura | COP 300.000 |

### 4.3 Consolidado y contingencia

| CONCEPTO | VALOR |
|---|---:|
| Total recursos humanos | COP 16.100.000 |
| Infraestructura primer mes | COP 300.000 |
| Base para contingencia (RH + Inf) | COP 16.400.000 |
| Contingencia (15%) | COP 2.460.000 |
| Costo total desarrollo MVP | COP 18.860.000 |
| Precio sugerido al cliente (30% margen) | COP 24.518.000 |

**NOTA IMPORTANTE:** El costo total de desarrollo de COP 18.860.000 (o COP 24.518.000 con margen) corresponde a la inversión inicial para construir la plataforma. En el modelo SaaS, este valor NO es pagado por cada veterinaria. Las veterinarias solo pagan la suscripción mensual. El costo de desarrollo se recupera con las suscripciones de múltiples clientes.

Si el cliente exige Oracle como gestor de base de datos, se estima un ajuste de COP 1.200.000 para el primer mes.


## 5. MODELO DE SUSCRIPCIÓN

El negocio se comercializa exclusivamente por SUSCRIPCIÓN MENSUAL. Los planes y condiciones son los siguientes:

| Plan | PRECIO MENSUAL (COP) | SLA DE RESPUESTA | CARACTERÍSTICAS PRINCIPALES |
|---|---:|---|---|
| Básico | COP 79.000 | 48 horas | Funcionalidades principales, soporte por ticket |
| Estándar | COP 199.000 | 24 horas | Todo lo anterior + backups gestionados + soporte prioritario |
| Empresarial | COP 299.000 | 8 horas | Todo lo anterior + API personalizada + soporte dedicado |

Facturación y condiciones:
- Facturación mensual por domiciliación o factura electrónica. Los precios no incluyen IVA (19%).
- Descuento por pago anual anticipado: 10% sobre la tarifa anual.
- Periodo de prueba opcional: 14 días sin cargo.
- Cancelación: con preaviso de 30 días; datos conservados 30 días para exportación antes de eliminación (salvo retención legal).

Opciones de financiación de implementación:
- Cargo inicial (inversión MVP): COP 18.860.000 (pago único) — esta cifra es inversión de la empresa, no cobrada a cada cliente.
- Alternativa: financiación del cargo inicial en 6 cuotas junto con suscripción (sujeto a acuerdo comercial).


## 6. CRONOGRAMA CON FECHAS REALES

| SPRINT | FECHAS | OBJETIVO | STORY POINTS |
|---|---|---|---:|
| Sprint 1 | 15/06/2026 - 28/06/2026 | Base y autenticación | 25 SP |
| Sprint 2 | 29/06/2026 - 12/07/2026 | Mascotas y citas | 28 SP |
| Sprint 3 | 13/07/2026 - 26/07/2026 | Adopciones y reportes | 30 SP |
| Sprint 4 | 27/07/2026 - 09/08/2026 | Panel admin y despliegue | 25 SP |

**Fecha de inicio del proyecto:** 15 de junio de 2026  
**Fecha de entrega final (estabilización):** 16 de agosto de 2026


## 7. ASPECTOS LEGALES COLOMBIANOS

### 7.1 Ley 1581 de 2012 - Protección de Datos Personales
La Ley 1581 de 2012 regula el tratamiento de datos personales en Colombia. Se asegurará el cumplimiento de derechos de los titulares (consulta, rectificación, supresión) y plazos de respuesta de 10 días hábiles.

| Actor | RESPONSABILIDAD |
|---|---|
| Responsable del tratamiento | Define finalidades, recopila autorizaciones y responde solicitudes |
| Encargado del tratamiento | Procesa datos por cuenta del responsable y aplica medidas de seguridad |
| Titular | Ejercicio de derechos ARCO |

### 7.2 Aviso de privacidad obligatorio
**Aviso de privacidad:** se incluirá en el registro y en los términos de servicio, con canal de contacto: soporte@happypaws.co. Plazo de conservación: mientras subsista la relación contractual y según normatividad.

### 7.3 Ley 1774 de 2016 - Bienestar Animal
La plataforma incorpora flujos de reporte y escalamiento para cumplimiento de la Ley 1774 de 2016.

### 7.4 Registro ante la SIC
El registro en el RNBD de la SIC será gestionado cuando la base supere 5.000 titulares o sea requerido por operación.


## 8. SEGURIDAD ADICIONAL Y CUMPLIMIENTO TÉCNICO

| MEDIDA | IMPLEMENTACIÓN |
|---|---|
| Rate limiting | Máximo 100 peticiones/minuto por IP |
| CORS | Dominios autorizados |
| Validación de entradas | Backend + frontend |
| Logs de auditoría | Registrar quién hizo qué; retención mínima: 6 meses |
| Backups automáticos | Copias diarias; retención: 30 días |
| Contraseñas | Hash con bcrypt |


## 9. STORY POINTS REALISTAS

| SPRINT | SP ASIGNADOS | JUSTIFICACIÓN |
|---|---:|---|
| Sprint 1 | 25 SP | Base, autenticación y estructura técnica |
| Sprint 2 | 28 SP | Mascotas, agenda y trazabilidad |
| Sprint 3 | 30 SP | Adopciones, reportes y flujo social |
| Sprint 4 | 25 SP | Panel admin, seguridad y despliegue |
| Total | 108 SP | Velocidad realista |

Velocidad estimada del equipo: 6-8 Story Points por semana por persona. Con 4 personas activas, se espera completar entre 24 y 32 SP por Sprint.


## 10. ENDPOINTS REST Y CÓDIGOS DE ERROR

| MÉTODO | ENDPOINT | DESCRIPCIÓN |
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

| CÓDIGO | SIGNIFICADO | EJEMPLO |
|---|---|---|
| 200 OK | Petición exitosa | GET /api/v1/pets |
| 201 Created | Recurso creado | POST /api/v1/pets |
| 400 Bad Request | Datos inválidos | Email mal formado |
| 401 Unauthorized | No autenticado | Token faltante |
| 403 Forbidden | Sin permisos | Usuario común accede a /admin |
| 404 Not Found | Recurso no existe | Pet ID inválido |
| 500 Internal Error | Error del servidor | Excepción no manejada |


## 11. ANÁLISIS DE COMPETENCIA

| Competidor | Precio (COP/mes) | Ventajas | Desventajas |
|---|---|---|---|
| Vetmanager | COP 180.000 - 350.000 | Establecido, muchas funciones | Caro, sin adopciones ni reportes |
| G247 | COP 150.000 - 280.000 | Buen soporte | Curva de aprendizaje alta |
| MVZ Cloud | COP 70.000 - 150.000 | Colombiano, económico | Poca escalabilidad |
| VetSys | COP 100.000 - 200.000 | Opción conocida | Menor foco en bienestar animal |
| Happy Paws | COP 79.000 - 299.000 | Adopciones + reportes + bienestar animal | Nuevo en el mercado |


## 12. ANÁLISIS DE RIESGOS LEGALES Y TÉCNICOS

| RIESGO | PROBABILIDAD | IMPACTO | MITIGACIÓN |
|---|---|---|---|
| Incumplimiento de protección de datos (Ley 1581) | Media | Alto | Aviso de privacidad, consentimiento, contrato de encargo |
| Denuncias por maltrato animal no gestionadas | Media | Alto | Flujo de escalamiento a autoridades |
| Fuga de información de mascotas y dueños | Baja | Crítico | Encriptación, backups cifrados, controles de acceso |
| Competencia con software establecido | Alta | Medio | Diferenciación por adopciones y reportes |
| Retraso en aprobaciones del cliente | Alta | Medio | Validaciones por sprint y responsables claros |
| Rotación del equipo técnico | Media | Alto | Documentación y pares de respaldo |
| Dependencia de APIs de terceros | Media | Medio | Fallbacks y contratos de servicio |
| Escalabilidad inesperada | Baja | Alto | Pruebas de carga y arquitectura preparada |


## 13. DEFINICIÓN DE DONE MEJORADA

| CRITERIO | DESCRIPCIÓN |
|---|---|
| Código revisado | Aprobado por al menos 2 desarrolladores |
| Pruebas funcionales | Flujos principales probados sin fallas críticas |
| Pruebas de seguridad | Validación básica contra SQL Injection y XSS |
| Documentación | API actualizada y changelog mínimo |
| Calidad | Sin errores críticos de severidad 1 o 2 |
| Aprobación del PO | Aceptación formal del entregable |


## 14. QUÉ NO INCLUIR EN EL MVP

| FUNCIONALIDAD EXCLUIDA | RAZÓN |
|---|---|
| Telemedicina | Requiere validación clínica y regulación adicional |
| E-commerce | Complejidad logística adicional |
| Microservicios | No necesario en primera fase; iniciar monolito modular |
| Gamificación | No prioritaria para validación del mercado |


## 15. CONCLUSIÓN Y PRÓXIMOS PASOS

Happy Paws es una propuesta viable y escalable para digitalizar la operación veterinaria y la protección animal en Colombia. Siguientes pasos:

| Siguiente paso | Responsable | Resultado esperado |
|---|---|---|
| Validar alcance final | Cliente + equipo | Backlog cerrado |
| Aprobar modelo comercial | Cliente | Plan y contrato listos |
| Iniciar desarrollo | Equipo TI | MVP en construcción |
| Abrir piloto | Cliente + usuarios | Validación con usuarios reales |


## 16. ANEXOS

| Anexo | Contenido |
|---|---|
| A1 | Supuestos financieros |
| A2 | Aviso de privacidad completo |
| A3 | Contrato de suscripción completo (ejecutable) |
| A4 | Backlog resumido |
| A5 | Mapa de arquitectura técnica |


### A1. SUPUESTOS FINANCIEROS
Costo base de recursos humanos = COP 16.100.000; contingencia = COP 2.460.000; costo total = COP 18.860.000; precio sugerido = COP 24.518.000.
Suscripción estimada (referencia comercial): Básico COP 79.000/mes; Estándar COP 199.000/mes; Empresarial COP 299.000/mes.


### A2. AVISO DE PRIVACIDAD (COMPLETO)
AVISO DE PRIVACIDAD. Responsable del tratamiento: Happy Paws SAS o la persona jurídica que opere la plataforma para la veterinaria aliada. Finalidades: gestionar usuarios, mascotas, citas, adopciones, reportes, comunicaciones operativas, soporte, seguridad, analítica y cumplimiento legal. Datos recolectados: nombre, número de documento, correo, teléfono, dirección, datos de mascotas, historial clínico y registros asociados al uso del sistema. Derechos: consultar, actualizar, rectificar, suprimir, revocar la autorización y presentar quejas ante la autoridad competente. Canal de contacto: soporte@happypaws.co. Plazo de conservación: mientras subsista la relación contractual y durante los términos exigidos por la normativa aplicable. El titular podrá ejercer sus derechos por los canales oficiales.


### A3. CONTRATO DE SUSCRIPCIÓN (DOCUMENTO EJECUTABLE)

CONTRATO DE SUSCRIPCIÓN ENTRE:

- HAPPY PAWS SAS, identificado con NIT: ______________________, representado por ______________________, mayor de edad, identificado(a) con C.C. No. ______________________, quien en adelante se denominará EL PROVEEDOR.

- LA VETERINARIA SUSCRIPTORA: ______________________, identificada con NIT/C.C. ______________________, representada por ______________________, quien en adelante se denominará EL CLIENTE.

FECHA DEL CONTRATO: ____ / ____ / 2026

PLAN SELECCIONADO: ☐ Básico  ☐ Estándar  ☐ Empresarial

VALOR MENSUAL: COP ____________________ (valor en números)  
IVA (19%): NO INCLUIDO (se liquidará según la normativa vigente)

CLÁUSULAS:

1. OBJETO
El presente contrato tiene por objeto regular la prestación, por EL PROVEEDOR, de acceso a la plataforma Happy Paws en modalidad de suscripción mensual, conforme al plan seleccionado.

2. DURACIÓN Y RENOVACIÓN
La suscripción tendrá duración mensual y se renovará automáticamente por periodos iguales, salvo notificación de cancelación por cualquiera de las partes con treinta (30) días de antelación.

3. FORMA DE PAGO
EL CLIENTE pagará la tarifa mensual mediante domiciliación, transferencia o factura electrónica según acuerdo. Los pagos se realizarán por periodos adelantados. En caso de mora, EL PROVEEDOR podrá suspender el servicio tras quince (15) días de impago.

4. CARGO DE IMPLEMENTACIÓN
El desarrollo del MVP tiene un costo estimado de COP 18.860.000 que corresponde a la inversión inicial del proyecto y NO será cobrado individualmente a cada veterinaria en el modelo SaaS, salvo acuerdo comercial en contrario.

5. NIVELES DE SERVICIO Y SOPORTE
Los niveles de servicio (SLA) dependerán del plan contratado: Básico (48h), Estándar (24h), Empresarial (8h). Los tiempos de respuesta y canales se detallarán en el anexo técnico.

6. PROPIEDAD INTELECTUAL
EL PROVEEDOR conserva todos los derechos de propiedad intelectual del software. EL CLIENTE recibe una licencia de uso intransferible mientras esté al día con sus obligaciones de pago.

7. PROTECCIÓN DE DATOS
Las partes se comprometen a cumplir la Ley 1581 de 2012 y normas relacionadas. EL PROVEEDOR actuará como responsable o encargado según corresponda y facilitará mecanismos para atender los derechos de los titulares.

8. BIENESTAR ANIMAL
EL CLIENTE se compromete a utilizar la plataforma conforme a la Ley 1774 de 2016; el proveedor podrá bloquear o suspender contenido que incumpla la normativa.

9. SUSPENSIÓN POR INCUMPLIMIENTO
En caso de impago reiterado o incumplimiento grave, EL PROVEEDOR podrá suspender o terminar el servicio, conservando los datos por 30 días para exportación.

10. CONFIDENCIALIDAD
Ambas partes se obligan a mantener la confidencialidad de la información técnica y comercial a la que accedan.

11. LIMITACIÓN DE RESPONSABILIDAD
La responsabilidad del proveedor se limitará a daños directos comprobados y no incluirá perjuicios indirectos salvo disposición legal en contrario.

12. TERMINACIÓN
Cualquiera de las partes podrá dar por terminado el contrato por incumplimiento grave o por mutuo acuerdo. Tras terminación se aplicarán las políticas de retención y eliminación de datos indicadas.

13. LEY APLICABLE Y JURISDICCIÓN
El presente contrato se rige por la legislación colombiana y las partes se someten a la jurisdicción de los juzgados de Ibagué, Tolima.

FIRMAS:

Por EL PROVEEDOR: ______________________    Fecha: ____ / ____ / 2026
Nombre representante: ______________________
C.C./NIT: ______________________

Por EL CLIENTE: ______________________    Fecha: ____ / ____ / 2026
Nombre representante: ______________________
C.C./NIT: ______________________


### A4. BACKLOG RESUMIDO
Autenticación, mascotas, citas, adopciones, reportes, panel administrativo, auditoría, seguridad y despliegue.


### A5. MAPA DE ARQUITECTURA TÉCNICA
Frontend: React. Backend: Spring Boot. Base de datos: PostgreSQL. Autenticación: JWT. Contenedores: Docker. Imágenes: Cloudinary. Despliegue: AWS/Railway.

=== FIN DOCUMENTO HAPPY PAWS V3.3 FINAL CORREGIDA ===
