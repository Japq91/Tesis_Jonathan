# Auditoría de redacción y veracidad — Capítulo "Precipitación total"

**Archivo auditado:** `tex_es/05.vr1_result02_tp.tex` (versión resumida del capítulo de resultados de precipitación)
**Fuentes de verificación:** `papers/files_MD/*.md`, `tex_es/bibliografia.bib`, `tabelas_es/tab_stat_global_tp.tex`, `tabelas_es/tab_stat_p90_tp.tex`, cruce de labels con `tex_es/04.vr2_result01_w10.tex`
**Fecha:** 2026-07-21

Mismo procedimiento que la auditoría del Capítulo 04 (`papers/auditoria_04.vr1_result01_w10.md`): (A) redacción, consistencia terminológica y estructura; (B) consistencia del texto con sus propias tablas; (C) fidelidad de las citas a las fuentes reales, verificada con un agente que leyó cada `.md` en `papers/files_MD`.

---

## A. Redacción, consistencia y estructura

### A.1 — Referencia cruzada rota (rompe la compilación de la referencia): `\ref{subsubsec:eof1_wind10_p90}`
Línea 186:
> "Al contrastar estos patrones con los campos de viento equivalentes (Sección~\ref{subsubsec:eof1_wind10_p90})..."

La etiqueta `subsubsec:eof1_wind10_p90` **no existe en ningún archivo del proyecto**. La sección real de EOF1–p90 del capítulo de viento está etiquetada `subsec:eof1_wind10_p90` (sin el "sub" extra) en `tex_es/04.vr2_result01_w10.tex` (línea 137, y también en la versión `vf6`). Al compilar, este `\ref` se resuelve como `??` en el PDF. Es el hallazgo más urgente de esta auditoría — a diferencia de las inconsistencias de estilo, este es un error que se ve literalmente en el documento final.

### A.2 — "Población Global" con capitalización inconsistente (mismo patrón que en el Capítulo 04)
Capitalizado ("Población Global") en la mayoría de las ~25 ocurrencias, pero en minúscula en el pie de figura de la línea 14, en la línea 170, y sistemáticamente en **toda la sección de Síntesis** (líneas 250, 252, 253, 257). Igual que en el capítulo anterior, conviene fijar un criterio único.

### A.3 — Sigla "WCB" usada antes de definirse
"WCB" aparece en las líneas 24, 25 y 40 ("embebidas en el WCB", "organizada dentro del WCB", "transportada por el WCB"), pero su expansión completa —"Cinturón Transportador Cálido (WCB)"— no se presenta hasta la línea 69, treinta líneas después del primer uso. Mismo problema que la sigla "CCB" detectado en el Capítulo 04.

### A.4 — Párrafo comentado que duplica contenido activo (línea 107)
Igual que el párrafo comentado del Capítulo 04, aquí hay un párrafo completo comentado con `%`:

> `% Esta configuración implica que, en ciclones intensos maduros, los forzantes de viento y precipitación operan en cuadrantes opuestos: mientras las ráfagas de viento más intensas se concentran en el sector noroeste (asociadas a la CCB), los máximos remanentes de lluvia se desplazan hacia el sureste y sur...`

Este contenido comentado es, además, **redundante** con lo que ya se afirma en el texto activo (línea 186: "mientras la variabilidad de las ráfagas más intensas se compacta en el cuadrante noroeste... la lluvia remanente se organiza en una herradura sólida en los cuadrantes sureste y sur") y en la Síntesis (línea 262). Es texto descartado que quedó sin limpiar.

### A.5 — Etiqueta con prefijo incorrecto
Línea 218: `\subsection{Población Global}\label{subsubsec:pc1_global_tp}` — es una `\subsection`, no una `\subsubsection`; el prefijo debería ser `subsec:`. Solo se referencia una vez, internamente (línea 243), por lo que renombrarla es seguro.

### A.6 — Encabezado sin `\label`
Línea 47: `\section{Distribución espacial de máximos (PDFe)}` no tiene ninguna etiqueta, igual que el encabezado análogo del Capítulo 04 antes de la corrección aplicada ahí.

### A.7 — Nombre propio sin capitalizar
Línea 24: "ciclones del mediterráneo" — "Mediterráneo" es un nombre propio (mar/región) y debería ir capitalizado.

### A.8 — Terminología del chorro de bajo nivel inconsistente entre capítulos
Línea 36 usa "Chorro de Capas Bajas" (con mayúsculas) para lo que el Capítulo 04 llama "chorro de bajo nivel" / "corrientes en chorro de niveles bajos" (minúsculas, fraseo distinto). Mismo concepto (low-level jet), términos distintos entre capítulos. Prioridad baja — no es incorrecto, solo inconsistente.

### A.9 — Abreviatura "PG" introducida solo en este capítulo
Este capítulo define "Población Global (PG)" en su primer uso (línea 22) y usa "PG" como atajo ~30 veces en el cuerpo del texto, pero vuelve a escribir "población global" completo en toda la Síntesis. El Capítulo 04, en cambio, nunca abrevia y siempre escribe "Población Global" completo. No es un error, pero es una inconsistencia de estilo entre capítulos que vale la pena decidir conscientemente (¿mantener "PG" solo en este capítulo, o extenderlo/quitarlo para uniformidad de la tesis?).

---

## B. Consistencia interna: el texto vs. su propia tabla

Se comparó el texto con `tab_stat_global_tp.tex`, referenciada por el propio capítulo.

### B.1 — "Debilitamiento progresivo" en ARG no es monotónico (línea 226)
El texto dice:
> "ARG mantiene correlaciones negativas significativas durante todo el ciclo, con debilitamiento progresivo (de $-0.51$ en incipiencia a $-0.25$ en decaimiento)."

Los valores extremos citados son correctos, pero la tabla muestra la secuencia completa: Incipiente $-0.51$ → Intensificación $-0.66$ → Madurez $-0.53$ → Decaimiento $-0.25$. Es decir, la correlación en realidad **se fortalece primero** (de $-0.51$ a $-0.66$) antes de debilitarse hacia $-0.25$. Describir esto como "debilitamiento progresivo" tomando solo los extremos omite el pico intermedio en intensificación. Es el mismo tipo de simplificación de trayectoria que se corrigió en el Capítulo 04 (aunque ahí el error era numérico; aquí es de caracterización de la tendencia). El resto de los números de ambas tablas (`tab_stat_global_tp` y `tab_stat_p90_tp`) fueron verificados exhaustivamente contra el texto — incluyendo los saltos de varianza EOF1 y sus diferencias en puntos porcentuales (Sección de Fraccionamiento de varianza) — y **todos coinciden exactamente**; este capítulo es más prolijo numéricamente que el anterior.

---

## C. Verificación de fidelidad a las fuentes citadas

Se revisaron 37 afirmaciones contra `papers/files_MD/<clave>.md` (dos claves —`catto2015fronts` y `rocha2016estudio`— corresponden a archivos con nombre ligeramente distinto, `catto2015front.md` y `rocha2016estudo.md`, mismo patrón de discrepancia de nombre ya visto en el Capítulo 04; el contenido de ambos sí respalda las citas). Resultado agregado: **22 coinciden bien (varias con cita casi literal), 10 coinciden parcialmente, 1 no coincide, y 1 no es verificable por archivo fuente corrupto.**

### C.1 — Hallazgo más grave: `hannachi2023eof` (línea 131) — cita ajena al tema, mismo patrón que en el Capítulo 04
> "...generando una reducción dimensional efectiva \citep{hannachi2023eof} donde el primer modo retiene la mayor fracción posible de la varianza total del campo."

El paper real (Hannachi, Finke & Trendafilov 2023, *"Common EOFs: a tool for multi-model comparison and evaluation"*) trata sobre un método de EOFs comunes para **comparar múltiples modelos climáticos** (CMIP6, reanálisis) — no tiene relación alguna con bandas de precipitación, reducción dimensional de un campo físico, ni estructuras de ciclones. Es la **segunda vez** que esta misma cita se usa de forma genérica/descontextualizada para respaldar una afirmación física específica que el paper no aborda (en el Capítulo 04 se usó para "los modos secundarios han dejado de ser ruido estadístico"). Recomendación: quitar esta cita en ambos capítulos, o sustituirla por una referencia real sobre reducción dimensional en EOF de campos geofísicos.

### C.2 — Archivo fuente corrupto: `browning1986conceptual` (línea 69)
El `.md` correspondiente solo contiene texto de encabezado/pie de página repetido ("Unauthenticated | Downloaded..."), sin el contenido real del artículo. No se pudo verificar la afirmación sobre el modelo conceptual del WCB directamente desde este archivo (aunque el modelo de Browning 1986 es ampliamente corroborado indirectamente por referencias cruzadas en otros papers revisados, p. ej. Catto et al. 2015). Si se quiere una verificación estricta, habría que revisar el PDF original.

### C.3 — Afirmaciones que generalizan más de lo que dice la fuente

**`chen2024evaluation` (línea 24)** — La tesis atribuye a este paper tanto la partición precipitación total = estratiforme + convectiva parametrizada (correcto, es la definición del dato de ERA5) como que "la convectiva es la que controla la cola superior de la distribución" — esto segundo no es un hallazgo del paper, que trata de evaluación de sesgos de ERA5 frente a observaciones, no de qué componente domina la cola.

**`dacre2023climatology` (línea 40)** — La idea de que el máximo de precipitación ocurre antes que el de intensidad se menciona en la introducción del paper citando a su vez a Bengtsson et al. (2009) y Booth et al. (2018) — no es un hallazgo propio de Dacre et al. (2023), cuyo objetivo central es la eficiencia de precipitación y el presupuesto de humedad.

**`mendes2010climatology` + `simmonds2000mean` (línea 77)** — La cifra "~18 eventos por invierno" coincide de forma casi literal con Mendes et al. (2010), pero Simmonds & Keay (2000) es una climatología del Hemisferio Sur completo cuyo máximo de ciclogénesis está más al sur; no reporta esa cifra específica — su cita aquí es un respaldo genérico de la existencia de la rama subtropical de tormentas, no una confirmación del número.

**`machado2020influence` (línea 228)** — El paper estudia la modulación de ENSO sobre la inestabilidad baroclínica y los *storm tracks* (energía cinética, transporte de calor), pero no trata sobre "eficiencia de los sistemas para condensar vapor de agua" — esa conexión específica con la condensación es una extensión no respaldada por el contenido del paper.

**`russo2025impacts` (línea 36)** — Es un estudio de solo 6 casos (3 intensos + 3 explosivos), no una climatología regional; la generalización a "SBR y el límite con LPB" como comportamiento regional sistemático excede el alcance de un análisis de casos puntuales.

**`gozzo2017climatology` (línea 158)** — El paper describe el transporte remoto de vapor desde la Alta Subtropical del Atlántico Sur como la fuente principal y la evaporación local como de **"papel secundario"** explícitamente; la tesis presenta ambos mecanismos como igualmente relevantes ("depende de... y de"), sin ese matiz de jerarquía.

**`schultz2021antecedents` (línea 99)** — Se cita para "explicar la geometría arqueada" de la banda de precipitación, pero el paper es un análisis histórico/bibliográfico sobre los antecedentes del modelo Shapiro-Keyser en la literatura de la Escuela de Bergen — documenta el origen conceptual del *bent-back front*, no un mecanismo que explique la geometría de la precipitación.

**`hart2003cyclone` (línea 184)** — Se afirma que este paper trata sobre cómo las seclusiones cálidas "dictan la ubicación de los forzantes frontogenéticos"; en realidad Hart (2003) desarrolla el espacio de fases de ciclones (*Cyclone Phase Space*) para clasificar térmicamente los sistemas, sin abordar específicamente la ubicación de forzantes frontogenéticos.

**`naud2020evaluation` (línea 69)** — Se cita como prueba de que el WCB organiza la precipitación "independientemente de la región de génesis"; el paper evalúa el desempeño de reanálisis/GCMs en reproducir la asimetría este-oeste de precipitación en ciclones oceánicos de 30–60° N/S, pero no hace una comparación explícita entre regiones de génesis distintas.

**`coutodesouza2024thesis` (línea 38) y `gramcianinov2019properties` (líneas 33, 38)** — Ambas coinciden bien en general; `gramcianinov2019properties` en particular tiene una coincidencia casi literal para el número de eventos >20 mm/día en ARG.

---

## Resumen priorizado de acciones

**Prioridad alta:**
1. Corregir `\ref{subsubsec:eof1_wind10_p90}` → `\ref{subsec:eof1_wind10_p90}` (línea 186) — referencia rota, se vería como "??" en el PDF compilado.
2. Quitar o reemplazar la cita `hannachi2023eof` (línea 131) — mismo problema ya detectado en el Capítulo 04, esta vez con una afirmación física distinta pero igualmente no sustentada por el contenido real del paper.

**Prioridad media:**
3. Ajustar la caracterización de la correlación de ARG (línea 226): no es un "debilitamiento progresivo" monotónico, sino que se fortalece primero (a $-0.66$ en intensificación) antes de debilitarse.
4. Revisar/matizar las citas `chen2024evaluation`, `dacre2023climatology`, `mendes2010climatology`+`simmonds2000mean`, `machado2020influence`, `russo2025impacts`, `gozzo2017climatology`, `schultz2021antecedents`, `hart2003cyclone` y `naud2020evaluation` (ver detalle en C.3) — en todos estos casos la fuente respalda la idea general pero no exactamente en los términos o con el alcance que se le atribuye.
5. Si se dispone del PDF original, verificar directamente `browning1986conceptual` (el `.md` disponible está corrupto/vacío).

**Prioridad baja (consistencia editorial):**
6. Unificar capitalización de "Población Global" (especialmente en la Síntesis), igual que en el Capítulo 04.
7. Introducir la sigla "WCB" en su primer uso (línea 24), no en la línea 69.
8. Eliminar el párrafo comentado de la línea 107 (redundante con contenido activo).
9. Corregir la etiqueta `\label{subsubsec:pc1_global_tp}` → `subsec:pc1_global_tp` (línea 218) y añadir un `\label` al `\section` de la línea 47.
10. Capitalizar "Mediterráneo" (línea 24).
11. Decidir si unificar "Chorro de Capas Bajas" con el fraseo del Capítulo 04, y si extender o eliminar la abreviatura "PG" para consistencia entre capítulos.
