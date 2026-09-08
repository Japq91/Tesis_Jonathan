# Autores en `files_MD` no utilizados — potencial de aporte a los Capítulos 04 (viento) y 05 (precipitación)

**Fecha:** 2026-07-22
**Estado:** revisión 3 — incorpora la corrección de la clave bibliográfica de Laureanti, la exclusión explícita de dos autores de la lista para la Introducción, y la verificación directa del PDF de `gan1991surface` (su `.md` estaba corrupto).

**Alcance:** de los 100 papers en `papers/files_MD`, se identificaron 13 que no están citados en ningún capítulo activo de la tesis (`tese_es.tex`). Se leyó cada uno para evaluar su aporte potencial, y el autor corrigió el encaje de varias recomendaciones en dos rondas de revisión.

**Los 13 no utilizados:** `IPCC2021_WG1_Chapter11_Extremes`, `laureanti2024relation`, `bitencourt2010relating`, `catto2016extratropical`, `dalanhese2023new`, `dejesus2021multimodel`, `gan1991surface`, `hannachi2023eof`, `kaylee2025convection`, `marrafon2022classificacao`, `masson2022tendencias`, `simmonds1999southern`, `sun2022evaluation`.

---

## A. Recomendaciones confirmadas (con ubicación exacta)

### A.1 — `bitencourt2010relating` → **Introducción**, Bloque A2 (línea 11)

Respaldo de que en Brasil ocurren eventos que generan pérdidas económicas y sociales, dando sustento a la necesidad de estudiar el viento en los ciclones extratropicales. "Relating winds along the Southern Brazilian coast to extratropical cyclones" (Bitencourt et al., 2010) demuestra estadísticamente que el viento observado en 9 estaciones meteorológicas de la costa sur de Brasil está asociado a la profundidad y distancia de ciclones extratropicales, motivado explícitamente por pérdidas socioeconómicas ("affecting the populous cities... productive agricultural areas... accidents with fishing boats").

**Dónde insertarlo**, junto a `bartolomei2024extremos` y `miranda2026patterns`:

> "...\citet{bartolomei2024extremos} reportan la letalidad causada por ciclones extratropicales invernales en esa región, mientras que \citet{miranda2026patterns} confirman que estos sistemas son los principales motores de tormentas costeras en el Atlántico Sur. La asociación directa entre el viento observado en la costa y la profundidad de estos sistemas confirma además pérdidas socioeconómicas recurrentes —agrícolas, pesqueras y urbanas— a lo largo del litoral \citep{bitencourt2010relating}. Su influencia se extiende al estado del mar: \citet{sasaki2021intraseasonal}..."

Ya está en el `.bib`.

### A.2 — `catto2016extratropical` → Capítulo 05, línea 42 (confirmado)

La síntesis de Catto (2016) sobre que la precipitación previa al pico de intensidad se relaciona más fuertemente con la profundización del ciclón que la posterior, refuerza el argumento del desacople precipitación–vorticidad en madurez (líneas 40–42, junto a `dacre2023climatology`/`mcerlich2023extremes`). Ya está en el `.bib`.

### A.3 — `laureanti2024relation` → Capítulo 05, línea 36 — sin mencionar la SACZ

**Nota de clave bibliográfica:** la entrada en `tex_es/bibliografia.bib` usa minúsculas: `laureanti2024relation` (no `Laureanti2024relation`, que es solo el nombre del archivo en `files_MD`). Ya está en el `.bib`.

La SACZ no se menciona (ese flujo no está necesariamente acoplado al ciclón bajo el enfoque lagrangiano centrado en el vórtice). Más allá de la SACZ, Laureanti et al. (2024) identifican que **el desplazamiento meridional del SALLJ y su confluencia con el flujo del noreste de la SASH son la causa del calentamiento/enfriamiento oceánico subyacente, y que la intensidad del evento extremo escala con la fuerza de la circulación de viento de niveles bajos** — el mismo mecanismo (confluencia SASH–SALLJ) que el Capítulo 05 ya invoca en la línea 36 vía `gramcianinov2024early`.

**Dónde insertarlo:**

> "...impulsada por la Alta Subtropical en SBR y por su interacción con el Chorro de Capas Bajas en LPB \citep{gramcianinov2024early}, consistente con evidencia de que la intensidad de estos eventos extremos escala con la fuerza de la confluencia entre el SALLJ y el flujo del noreste de la Alta Subtropical \citep{laureanti2024relation}."

### A.4 — `hannachi2023eof` → analogía metodológica, no respaldo físico

Este paper trata la técnica EOF aplicada a otros campos meteorológicos (comparación de modelos climáticos, no ciclones ni precipitación) — se usa como sustento para una similitud de lógica en el uso de técnicas estadísticas, no como respaldo de una afirmación física (ese fue el uso indebido detectado y retirado dos veces antes).

Hannachi, Finke & Trendafilov (2023) desarrollan los "Common EOFs" para comparar formalmente patrones EOF extraídos de **conjuntos de datos distintos** (CMIP6 frente a reanálisis). La lógica de fondo —que comparar descomposiciones EOF entre subconjuntos con condiciones físicas distintas requiere una base metodológica común— es análoga a comparar el EOF1 de la Población Global frente al subconjunto p90 en esta tesis.

**Dónde insertarlo**, Capítulo 04, junto a `hannachi2007empirical` (línea 117), o alternativamente en Fundamentos `subsubsec:tb_eof`:

> "...Este aplanamiento del espectro de autovalores es, según \citet{hannachi2007empirical}, indicador de que la energía del sistema se distribuye entre modos competitivos de distinta escala espacial. La lógica de contrastar formalmente las estructuras EOF entre subconjuntos con condiciones físicas diferenciadas —aquí, Población Global frente a p90— tiene precedente metodológico en otros campos, como la comparación de EOFs comunes entre modelos climáticos y reanálisis \citep{hannachi2023eof}."

**Importante:** debe quedar explícitamente como analogía de lógica metodológica, no como si el paper hubiera estudiado bandas de precipitación, EOF de viento o ciclones.

### A.5 — `gan1991surface` → **Introducción**, Bloque B1 (línea 18) — contenido verificado directamente en el PDF

El `.md` de este paper está corrupto (solo metadatos de descarga repetidos, mismo problema que tenía `browning1986conceptual.md` antes de usar su versión `_rev`). Siguiendo la indicación de revisar el PDF original (`papers/files_PDF`, aunque en la práctica se encontró en `papers/papers2/gan1991surface.pdf`), se renderizaron sus páginas como imágenes y se leyó el contenido directamente.

**Qué dice el paper:** Gan, M. A. y Rao, V. B. (1991), *"Surface Cyclogenesis over South America"* (Monthly Weather Review). Usando 10 años (1979–1988) de cartas de superficie sobre el dominio 15°–50°S, 30°–90°W —que cubre exactamente SBR, LPB y ARG—, cuantifican que la ciclogénesis es más frecuente en invierno (máximo en mayo, 134 casos; mínimo en diciembre, 71 casos) y que su variabilidad interanual está modulada por El Niño/Oscilación del Sur: los años El Niño (1983, 1986, 1987) muestran mayor frecuencia de ciclogénesis, coincidiendo con anomalías de precipitación fuertemente positivas en estaciones del sur de Brasil (São Paulo, Curitiba, Paranaguá, Florianópolis, Porto Alegre, entre otras). Concluyen que la conocida correlación negativa entre la precipitación del sur de Brasil y el índice de Oscilación del Sur se explica por esta mayor frecuencia de ciclogénesis en años El Niño.

**Por qué encaja:** es un antecedente directo y verificable (no una analogía de enfoque) sobre la climatología de ciclogénesis en la región de estudio exacta, complementario a `gan1994influence` (ya citado, mecanismo orográfico) de los mismos autores, y temáticamente afín a `reboita2010south`/`gramcianinov2020analysis`/`padilhareinke2026characterization`, ya citados en el mismo párrafo de la Introducción para la climatología de trayectorias.

**Dónde insertarlo**, línea 18 de `01.vr2_introducao.tex`:

> "En el contexto regional, \citet{reboita2010south} proporcionaron una de las primeras climatologías para el Atlántico Sur [...]. Ya desde una perspectiva pionera, \citet{gan1991surface} habían cuantificado que la ciclogénesis sobre esta misma región es más frecuente en invierno y que su variabilidad interanual —modulada por El Niño/Oscilación del Sur— explica la conocida correlación negativa entre la precipitación del sur de Brasil y dicho índice. Trabajos posteriores como \citet{gramcianinov2020analysis}..."

Ya está en el `.bib` (comparte entrada con `gan1994influence` en cuanto a los mismos autores, pero como referencia distinta).

---

## B. Papers que refuerzan la Introducción por *enfoque de investigación*, no por resultado literal

Confirmados por el autor para este uso (con dos exclusiones explícitas: **no usar** `IPCC2021_WG1_Chapter11_Extremes` ni `dejesus2021multimodel`, ambos retirados de esta lista). Ninguno trata el Atlántico Sudoccidental, el viento a 10 m o la precipitación de ciclones extratropicales en los términos de esta tesis — el valor está en el paralelismo de cómo abordaron su problema de investigación, no en sus hallazgos literales.

| Paper | Enfoque replicable (no el resultado literal) | Dónde podría aportar en la Introducción |
|---|---|---|
| `marrafon2022classificacao` | Combinación de un algoritmo de clasificación térmica (Cyclone Phase Space) con modelos climáticos regionales para el Atlántico Sur | Precedente de que la clasificación estructural de ciclones (no solo su frecuencia) ya es un enfoque activo en la región, reforzando la pertinencia metodológica de clasificar fases/estructura en esta tesis. |
| `masson2022tendencias` | Marco de evaluación de tendencias regionales de extremos (resumen del IPCC AR6 en español) | Podría mencionarse como referencia del tipo de evaluación regional de extremos que motiva, en sentido amplio, por qué caracterizar la estructura de viento/precipitación en el Atlántico Sur es relevante para la evaluación de riesgos. |
| `dalanhese2023new` | Comparación de la detección de ciclogénesis entre múltiples fuentes de datos (ERA5, JRA55, datos de la Marina) para Sudamérica | Precedente del enfoque de validar/triangular fuentes de datos para la región; podría mencionarse al justificar ERA5 más que como parte del Bloque A/B/C. |
| `kaylee2025convection` | Campaña de observación aérea dedicada a resolver procesos internos de mesoescala (inestabilidad elevada) dentro de la cabeza de coma de ciclones invernales de EE. UU. | Precedente de que resolver procesos *internos* de un ciclón (no solo su intensidad bulk) es un enfoque de investigación activo y valioso en otras cuencas — refuerza el Bloque C (vacío de caracterización estructural). |
| `simmonds1999southern` | Validación de un algoritmo de rastreo objetivo contra una campaña de observación intensiva (FROST) en el Hemisferio Sur | Precedente de validación de algoritmos objetivos de rastreo en el HS, reforzando el Bloque A1 (ya cita `sinclair1994objective`) con otro ejemplo de rigor metodológico en detección objetiva. |
| `sun2022evaluation` | Uso de EOF/PC para sintetizar variabilidad de precipitación con fines prácticos (pronóstico) | Precedente de que la información extraída vía EOF/PC tiene utilidad más allá de la caracterización académica — refuerza por qué el enfoque MEOF de esta tesis (Bloque E) tiene valor aplicado, no solo descriptivo. |

**Nota de cautela (vigente):** se recomienda incorporar como máximo 1–2 de estos seis, los que se sientan más naturales — no los seis, para no forzar una cuota de citas sin que aporten rigor real.

---

## Resumen de acciones

| Cita | Ubicación final | Estado en `.bib` | Acción |
|---|---|---|---|
| `bitencourt2010relating` | Introducción, línea 11 | En el `.bib` | Insertar cita de pérdidas socioeconómicas |
| `catto2016extratropical` | Capítulo 05, línea 42 | En el `.bib` | Insertar como confirmado |
| `laureanti2024relation` | Capítulo 05, línea 36 | En el `.bib` (clave en minúsculas) | Insertar cita sobre confluencia SALLJ–SASH, sin mencionar la SACZ |
| `hannachi2023eof` | Cap. 04 línea 117, o Fundamentos `tb_eof` | En el `.bib` | Insertar como analogía metodológica explícita |
| `gan1991surface` | Introducción, línea 18 | En el `.bib` | Insertar como antecedente de climatología de ciclogénesis (contenido verificado vía PDF) |
| `marrafon2022classificacao`, `masson2022tendencias`, `dalanhese2023new`, `kaylee2025convection`, `simmonds1999southern`, `sun2022evaluation` | Introducción (opcional) | Variable | Elegir como máximo 1–2, ver tabla B |
| `IPCC2021_WG1_Chapter11_Extremes`, `dejesus2021multimodel` | — | — | **Excluidos explícitamente**, no usar |
