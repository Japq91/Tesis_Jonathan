> **Actualización 2026-07-27 — todos corregidos:**
> - **II.1/II.2 (SALLJ y chorro de bajo nivel):** unificado. SALLJ ahora se expande siempre como "Chorro de Capas Bajas de Sudamérica (SALLJ)" (Cap. 01 y 02) y se usa como sigla en Cap. 05, 06 y 07 (antes decía "Chorro de Capas Bajas"/"chorro de capas bajas" sin la sigla). El chorro de bajo nivel de la CCB (feature distinta, mesoescalar) quedó estandarizado como "chorro de bajo nivel" en Cap. 02 y 04, sin mezclarse con SALLJ.
> - **II.3 (abreviatura "PG"):** eliminada. Las 34 ocurrencias de "PG" en el Cap. 05 se reemplazaron por "Población Global", igual que en el resto de la tesis.
> - **II.4 ("sudeste"/"sureste"):** unificado a "sureste" en las 4 ocurrencias sueltas (Cap. 01, 02, 04, 05).
> - Citas `gramcianinov2024early` (Cap. 07) y `andrade2024composite` (Cap. 06) corregidas — ver `auditoria_06-07_meof_prototipos.md`.
>
> Pendientes sin tocar (no solicitados en esta ronda): los 4 `\label` con prefijo invertido en Cap. 04 (cosmético) y el recorte de la Sección de Discusión del Cap. 07 (hallazgo II.6, redundancia de la explicación de intrusión seca).

# Auditoría de coherencia global — Tesis completa (01-07, con notas de 08-09)

**Fecha:** 2026-07-27
**Alcance:** (I) verificación de si las versiones vr2 (01-05) corrigieron los hallazgos de `auditoria_01-03_intro_fundamentos_metodos.md`, `auditoria_04.vr1_result01_w10.md` y `auditoria_05.vr1_result02_tp.md`; (II) coherencia terminológica y estructural de la tesis como un todo (01-07), con menciones puntuales a 08 (Conclusiones) y 09 (Consideraciones) donde resultó relevante para rastrear un término hasta el final del documento.

---

## Parte I — Verificación de correcciones vr1 → vr2

**Veredicto general: prácticamente todos los hallazgos de prioridad alta y media de las tres auditorías previas fueron corregidos.** Es una revisión notablemente prolija entre versiones. Detalle punto por punto:

### Capítulos 01-03 (vs. `auditoria_01-03`)

| Hallazgo vr1 | Estado en vr2 |
|---|---|
| A.1 — Mecanismo de sotavento andino repetido en Intro y Fundamentos | ✅ **Corregido.** Intro ahora solo remite ("...los mecanismos físicos específicos de cada foco se desarrollan en la Sección de los Fundamentos"); el mecanismo completo (compresión/estiramiento de vorticidad) solo aparece en Fundamentos. |
| A.2 — Bloque B3 completo (mecanismos SBR/LPB/ARG) duplicado | ✅ **Corregido.** La Introducción ahora dedica solo un párrafo genérico + el nombramiento de las 3 regiones; ya no desarrolla mecanismo por mecanismo (eso quedó exclusivamente en `sec:tb_regiones` de Fundamentos). |
| A.3 — Orientación NE/SE del WCB repetida | ✅ **Corregido.** Intro solo menciona la inversión hemisférica en una oración y remite a Fundamentos para el detalle. |
| A.4 — Advertencia de sesgos ERA5 duplicada | ✅ **Corregido.** Solo aparece una vez (Fundamentos, con la cita `chen2024evaluation`); no encontré la repetición en Introducción. |
| A.5 — `zscheischler2018future` duplicado | ✅ **Corregido.** Solo una ocurrencia (Fundamentos). |
| A.6 — Interpretación de asimetría/curtosis de PC1 duplicada (Fundamentos vs. Metodología) | ✅ **Corregido.** Metodología ahora remite explícitamente ("la interpretación cualitativa... se estableció en la Sección de los Fundamentos") en vez de reformular. |
| B.1 — Mecanismo CCB–vorticidad potencial repetido dentro de Fundamentos | ✅ **Corregido.** Ahora aparece una sola vez (línea 106). |
| B.2 — Subsección comentada duplicada (`subsec:tb_poblaciones`) | ✅ **Corregido.** No quedan comentarios de prosa muerta; solo encabezados organizativos (`% BLOQUE A`, etc.), que son legítimos. |
| B.3/B.4 — Fragmentos comentados sueltos | ✅ **Corregido**, mismo diagnóstico que B.2. |
| C — Typos "adicionale"/"Ademas" | ✅ **Corregido.** No se encuentran. |
| C — Capitalización "Población Global" | ✅ **Corregido** en estos tres capítulos (0 ocurrencias en minúscula). |
| C — Sigla SALLJ no retomada en resultados | ⚠️ **Seguía abierto en 04-07** — ver Parte II, hallazgo II.1 (matiz nuevo: sí reaparece en 08-09). |

### Capítulo 04 (vs. `auditoria_04.vr1`)

| Hallazgo vr1 | Estado en vr2 |
|---|---|
| A.1 — "Inc"/"Int" en vez de "Ic"/"It" | ✅ Corregido, no se encuentran. |
| A.2 — Capitalización "Población Global" | ✅ Corregido. |
| A.3 — Sigla CCB usada antes de definirse | ✅ Corregido — la expansión completa ahora está en el primer uso (línea 93). |
| A.4 — "sudeste"/"sureste" mezclados | ⚠️ **Sigue abierto** (1 "sudeste" línea 38, 2 "sureste" líneas 130/182). Baja prioridad, sin cambios. |
| A.5 — Separador decimal con coma (línea 182) | ✅ Corregido, todo el capítulo usa punto. |
| A.6 — Párrafo comentado "flotando" | ✅ Corregido. |
| A.7 — Etiquetas `\label` con prefijo incorrecto | ⚠️ **Sigue abierto** — persisten `\label{sec:...}` en 3 `\subsection` (líneas 54, 80, 107) y `\label{subsec:...}` en una `\section` (línea 190). Cosmético, no rompe compilación. |
| B.1 — Rango de curtosis mal delimitado (−0.30) | ✅ **Corregido** — ahora dice correctamente "−0.37 y −1.03". |
| B.2 — Lenguaje de "bimodalidad"/"bifurcación" injustificado | ✅ Corregido — ya no aparece ese lenguaje. |
| C.1 — `dalanhese2023new` mal usada | ✅ Corregido — la cita ya no aparece en el capítulo. |
| C.2 — `hannachi2023eof` fuera de tema | ✅ **Corregido** — reemplazada por `hannachi2007empirical` (cita correcta y pertinente) en ambas ocurrencias. |
| C.3 — Generalización de `russo2025impacts` (omitía excepciones) | ✅ **Corregido** — el texto ahora incluye explícitamente la salvedad ("—salvo en casos donde los flujos de calor ya son intensos antes de la formación del sistema—"). |
| C.3 — `dejesus2021multimodel` rango 1.5–2 m/s no ajustado por región | ✅ Corregido — la cita/afirmación ya no aparece en el capítulo. |
| C.2 — `hoskins2005new` / `inatsu2004zonal` como citas tangenciales | ⚠️ **Sigue abierto**, sin cambios de fondo (líneas 133 y 135). Prioridad media, no crítico. |

### Capítulo 05 (vs. `auditoria_05.vr1`)

| Hallazgo vr1 | Estado en vr2 |
|---|---|
| A.1 — `\ref{subsubsec:eof1_wind10_p90}` roto | ✅ **Corregido** — ahora `\ref{subsec:eof1_wind10_p90}`, que sí existe y resuelve. |
| A.2 — Capitalización "Población Global" | ✅ Corregido. |
| A.3 — Sigla WCB antes de definirse | ✅ Corregido — expansión en el primer uso (línea 24). |
| A.4 — Párrafo comentado duplicado (línea 107) | ✅ Corregido, eliminado. |
| A.5 — Label `\label{subsubsec:pc1_global_tp}` mal prefijado | ✅ Corregido → `subsec:pc1_global_tp`. |
| A.6 — `\section` sin label (línea 47) | ✅ Corregido, ahora tiene `\label{sec:pdfe_tp}`. |
| A.7 — "mediterráneo" sin capitalizar | ✅ Corregido → "Mediterráneo". |
| A.8 — Terminología del chorro de bajo nivel distinta a Cap. 04 | ⚠️ **Sigue abierto** — ver Parte II, hallazgo II.2 (persiste y se extiende a 06/07). |
| A.9 — Abreviatura "PG" solo en este capítulo | ⚠️ **Sigue abierto, sin cambios** — Cap. 05 sigue siendo el único que abrevia "Población Global" → "PG" (34 veces), mientras los demás 7 capítulos activos siempre la escriben completa. Ver hallazgo II.3. |
| B.1 — Caracterización no monotónica de la correlación en ARG | ✅ **Corregido** — el texto ahora describe correctamente "fortalecimiento inicial hacia la intensificación (−0.66) y un debilitamiento posterior hasta el decaimiento (−0.25)". |
| C.1 — `hannachi2023eof` fuera de tema (segunda ocurrencia) | ✅ **Corregido** — reemplazada por `hannachi2007empirical`. |
| C.2 — Archivo corrupto `browning1986conceptual` | ⚠️ Sin cambios (es un problema del repositorio de fuentes, no del `.tex`); confirmado además en la auditoría de Cap. 06/07 que el archivo válido `browning1986conceptual.md` sí existe y tiene contenido — el corrupto es solo `browning1986conceptual_rev.md`, un duplicado. |
| C.3 — Varias citas con generalización excesiva (`chen2024evaluation`, `hart2003cyclone`, `naud2020evaluation`, `schultz2021antecedents`, etc.) | ✅ **Corregidas** — se verificó que `chen2024evaluation` ya no carga la afirmación sobre "cola superior" (ahora atribuida correctamente a `flaounas2018heavy`); `hart2003cyclone` fue reencuadrada correctamente hacia el espacio de fases/seclusión cálida; `schultz2021antecedents` ahora se usa para "origen conceptual del *bent-back front*" (su alcance real) en vez de mecanismo dinámico. |

**Conclusión de la Parte I:** de ~45 hallazgos individuales entre las tres auditorías vr1, **solo 5 siguen abiertos**, y los 5 son de prioridad baja/media (etiquetas `\label` cosméticas, "sudeste"/"sureste", terminología del chorro de bajo nivel, sigla "PG" exclusiva del Cap. 05, y las citas `hoskins2005new`/`inatsu2004zonal` algo tangenciales). Ninguno de los errores graves (refs rotas, citas gravemente equivocadas, errores numéricos) sigue presente.

---

## Parte II — Coherencia terminológica y estructural de la tesis completa

### II.1 — La sigla SALLJ tiene un "hueco" de 5 capítulos
Se define y usa en Introducción (línea 45) y Fundamentos (línea 83, con la expansión completa "Chorro de Bajos Niveles de Sudamérica"), pero **no vuelve a aparecer en ningún capítulo de resultados (04, 05, 06, 07)** — estos siempre dicen "chorro de bajo nivel" / "chorro de capas bajas" sin la sigla. Reaparece recién en Conclusiones (Cap. 08, línea 26) y Consideraciones (Cap. 09, línea 15), donde se usa "SALLJ" dando por sentado que el lector todavía recuerda la sigla definida ~100 páginas antes. Recomendación: o se retoma "SALLJ" al menos una vez en los capítulos de resultados (p. ej. en la primera mención del chorro de bajo nivel en Cap. 04 o 05), o se reemplaza por el nombre completo en Conclusiones/Consideraciones para no asumir memoria de largo plazo del lector.

### II.2 — Cuatro formas distintas de nombrar el mismo chorro de bajo nivel en toda la tesis
Confirmado documento por documento:
- Cap. 02: "Chorro de Capas Bajas de Sudamérica (SALLJ)" (línea 83) **y**, 19 líneas después, "corriente en chorro de bajo nivel" (línea 102) — inconsistente dentro del propio capítulo.
- Cap. 04: "corrientes en chorro de niveles bajos" / "chorro de bajo nivel".
- Cap. 05: "Chorro de Capas Bajas" (mayúscula).
- Cap. 06/07: "chorro de capas bajas" (minúscula).

Es el mismo concepto físico (SALLJ / low-level jet) con 5 variantes de redacción. No es un error de contenido, pero para una tesis que define cuidadosamente sus siglas (Ic/It/M/D, WCB, CCB, PDFe, SBR/LPB/ARG) esta es la única que no logró estandarizarse. Recomendación: fijar una única forma (sugerido: "Chorro de Bajos Niveles de Sudamérica (SALLJ)" la primera vez en cada capítulo que lo mencione, y "SALLJ" en las siguientes).

### II.3 — La abreviatura "PG" es exclusiva del Capítulo 05
Confirmado cuantitativamente: de los 8 capítulos activos que mencionan "Población Global", **solo el Capítulo 05 la abrevia** ("PG", 34 veces) mientras los otros 7 (incluyendo 06 y 07, que continúan inmediatamente después) siempre escriben la forma completa. Esto es choque de estilo perceptible para un lector que atraviesa el Cap. 04 → 05 → 06 en secuencia: "Población Global" se convierte en "PG" por 56 líneas y luego vuelve a ser "Población Global" sin transición. Recomendación: decidir conscientemente una sola convención para toda la tesis (probablemente lo más simple es eliminar "PG" del Cap. 05 dado que los demás capítulos no la necesitan y el capítulo funciona igual sin abreviar).

### II.4 — "sudeste" vs. "sureste": tampoco hay criterio único a nivel de tesis
Cap. 01 usa "sudeste" (1 vez); Cap. 04 mezcla ambas formas; Cap. 05 no tiene ocurrencias problemáticas verificadas; Cap. 06 y 07 usan consistentemente "sureste" (20 ocurrencias combinadas, 0 "sudeste"). El documento en su conjunto se inclina mayoritariamente hacia "sureste", por lo que la corrección más económica sería normalizar las pocas ocurrencias de "sudeste" (Cap. 01 línea 39, Cap. 04 línea 38) a "sureste".

### II.5 — Mapeo Objetivos Específicos ↔ Capítulos: se mantiene exacto y completo
Confirmado nuevamente sobre la versión vr2 de la Introducción (Sección `Objetivos del Proyecto de Investigación`):
- **Objetivo 1** (base de datos lagrangiana, filtrado por ciclo de vida completo, estratificación SBR/LPB/ARG + intensidad) → Cap. 03, Secciones `sec:bd_ciclones` y `sec:poblaciones_estudio`. ✅
- **Objetivo 2** (KDE de magnitud y posición de máximos) → Cap. 04 (`sec:pdf_wind10`, `sec:pdfe_wind10`) y Cap. 05 (`sec:pdf_tp`, `sec:pdfe_tp`). ✅
- **Objetivo 3** (EOF univariado + MEOF multivariado) → Cap. 04/05 (EOF univariado) y Cap. 06 completo (MEOF). ✅
- **Objetivo 4** (prototipos estructurales sintéticos por fase/región) → Cap. 07 completo. ✅

No hay objetivos sin capítulo correspondiente ni capítulos que no respondan a un objetivo — la arquitectura general del documento es sólida y esto no ha cambiado entre vr1 y vr2.

### II.6 — Redundancia del mecanismo de intrusión seca/CCB/banda enroscada (cross-capítulo, no adyacente)
Ya documentado en detalle en `auditoria_06-07_meof_prototipos.md` (hallazgo A.2): el mismo mecanismo se explica con nivel de detalle técnico casi completo en Cap. 05 (línea 40), Cap. 06 (línea 118) y Cap. 07 (línea 41) — tres capítulos no todos adyacentes entre sí en términos de la profundidad de repetición. Es el mismo patrón de fondo que motivó la auditoría 01-03 original (explicar en vez de remitir), esta vez manifestado en la mitad final de la tesis en lugar de la introductoria.

---

## Resumen ejecutivo

**Lo que ya está resuelto:** la revisión vr1→vr2 fue sistemática y efectiva — corrigió prácticamente todos los errores de fondo (referencias rotas, citas mal atribuidas, errores numéricos, redundancia estructural entre Introducción/Fundamentos/Metodología). Los Capítulos 06 y 07, aunque nunca auditados, ya llegan con una calidad estructural superior a la que tenían inicialmente los Capítulos 04 y 05 (sin refs rotas, sin comentarios muertos, sin el error `hannachi2023eof`).

**Lo que queda pendiente es exclusivamente terminológico/cosmético, nunca de contenido científico:**
1. Unificar la terminología del chorro de bajo nivel (SALLJ) en toda la tesis — hallazgos II.1 y II.2.
2. Decidir si "PG" se mantiene solo en el Cap. 05 o se elimina — hallazgo II.3.
3. Normalizar "sudeste"→"sureste" en las ~2 ocurrencias sueltas — hallazgo II.4.
4. Corregir los 4 `\label` con prefijo `sec:`/`subsec:` invertido en Cap. 04 (cosmético, no rompe compilación).
5. Considerar recortar la Sección de Discusión del Cap. 07 para remitir al mecanismo de intrusión seca ya extendido en Cap. 05/06 en vez de repetirlo por tercera vez — hallazgo II.6.

Ninguno de estos 5 puntos afecta la validez científica del argumento; son puliditos editoriales de una tesis que, en su núcleo argumentativo (Objetivos 1-4, hipótesis, y la cadena Intro→Fundamentos→Métodos→Resultados→MEOF→Prototipos), está internamente coherente y bien sustentada por las fuentes citadas.
