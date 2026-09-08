# Auditoría de redacción y veracidad — Capítulo "Viento a 10 metros"

**Archivo auditado:** `tex_es/04.vr1_result01_w10.tex` (versión resumida del capítulo de resultados de viento a 10 m)
**Fuentes de verificación:** `papers/files_MD/*.md`, `tex_es/bibliografia.bib`, `tabelas_es/tab_stat_global_w10.tex`, `tabelas_es/tab_stat_p90_w10.tex`
**Fecha:** 2026-07-21

Este documento separa los hallazgos en dos bloques: (A) problemas de redacción, consistencia terminológica y estructura del `.tex`, verificables leyendo el propio archivo; y (B) verificación de que las afirmaciones atribuidas a cada autor citado son fieles al contenido real de esos papers (usando los resúmenes en `papers/files_MD`). El bloque B se corrió con un agente dedicado a leer cada fuente; yo verifiqué manualmente 2-3 ítems adicionales.

---

## A. Redacción, consistencia y estructura

### A.1 — Siglas de fase inconsistentes (línea 92)
El capítulo define las fases como **Ic, It, M, D** (línea 20 y en todo el resto del texto), pero en la línea 92 aparecen como **"Inc"** e **"Int"**:

> "En fases iniciales (**Inc**; paneles a, b y c)... Al intensificarse (**Int**; paneles d, e y f)..."

Es el único lugar del capítulo donde se usan estas abreviaturas alternativas. Deben normalizarse a "Ic" e "It".

### A.2 — "Población Global" con capitalización inconsistente
El término se usa como una etiqueta cuasi-propia y aparece capitalizado ("Población Global") en la mayoría de las ~30 ocurrencias, pero en minúscula ("población global") en el pie de figura de la línea 30, en la línea 79, dos veces en la línea 92, y sistemáticamente en **toda la sección de Síntesis** (líneas 225, 228, 230, 233, 238). Conviene fijar un criterio único (recomendado: mantener la mayúscula, ya que "Población Global" y "p90" funcionan como nombres de las dos poblaciones de estudio definidas en la Sección de métodos).

### A.3 — Sigla "CCB" usada antes de ser definida
"CCB" aparece por primera vez en la línea 94 ("los máximos superficiales asociados al CCB") y de nuevo en la línea 96 ("producto combinado de la CCB"), pero la expansión completa —"cinta transportadora fría (CCB, *cold conveyor belt*)"— no se presenta hasta la línea 186, muy posterior. Debe introducirse la sigla la primera vez que se usa (línea 94), no 90 líneas después.

### A.4 — "Sudeste" vs. "sureste" sin criterio único
Línea 39: "la costa del sur y **sudeste** de Brasil"
Líneas 131 y 184: "...con atenuamiento progresivo hacia el **sureste**" / "...(sur y **sureste**, respectivamente)"

Ambas formas son válidas en español, pero deben unificarse dentro del mismo capítulo.

### A.5 — Separador decimal inconsistente (línea 182)
Todo el capítulo usa el punto como separador decimal (23 ocurrencias, ej. "23.4", "31.4~m\,s$^{-1}$"), **excepto** el párrafo de la línea 182, que usa coma:

> "SBR concentra mayor variabilidad explicada por EOF2 (**8,7**\%) que LPB (**7,5**\%) y ARG (**11,5**\%)... EOF3 (**5,4--6,3**\%)"

Es casi con certeza un pegado de un borrador con configuración regional distinta. Corregir a "8.7", "7.5", "11.5", "5.4--6.3".

### A.6 — Texto comentado que quedó "flotando" en el archivo (línea 134)
Justo después de un párrafo activo hay una línea completa comentada con `%`:

> `% Como establece \citet{hannachi2007empirical}... la emergencia de una estructura dipolar en EOF1  constituye la firma matemática...`

Contiene además un doble espacio ("EOF1  constituye"). Si el contenido ya no se usa, debería eliminarse; si se descartó por error, debería revisarse y reincorporarse. Dejar prosa comentada en un capítulo final no es buena práctica editorial.

### A.7 — Etiquetas (`\label`) inconsistentes con la jerarquía de secciones
El proyecto sigue la convención `sec:` para `\section` y `subsec:` para `\subsection`, pero se rompe en varios puntos:
- Línea 55 y 81: dos `\subsection` etiquetadas como `sec:kde_espacial_global` / `sec:kde_espacial_p90` (debería ser `subsec:`).
- Línea 108: `\subsection{Fraccionamiento de varianza}\label{sec:var_exp_wind10}` (debería ser `subsec:`).
- Línea 192: `\section{Componentes principales (PC1)}\label{subsec:res_dinamica_pc1}` — aquí es al revés: una `\section` con prefijo `subsec:`.
- Línea 54 (`\section{Distribución espacial de máximos (PDFe)}`) y las `\subsection` de las líneas 198 y 210 **no tienen ningún `\label`**, por lo que no pueden referenciarse con `\ref` desde otros capítulos.

No afecta la compilación, pero sí la mantenibilidad y la posibilidad de referencias cruzadas futuras.

### A.8 — Uso repetitivo de fórmulas de atribución
"Según X" se usa 4 veces y "Como sostiene/precisa/establece/enfatiza X" 7 veces como arrancadores de oración para introducir citas, además de "En conjunto" como transición de cierre de párrafo en 3 ocasiones (líneas 104, 158, 190). No es incorrecto, pero en un capítulo de ~230 líneas activas, esta reiteración de fórmulas es perceptible y podría variarse (p. ej. integrando más citas de forma parentética con `\citep` en vez de siempre abrir la oración con el autor).

### A.9 — Único cambio de tiempo verbal (línea 36)
Todo el capítulo narra hallazgos ajenos en presente ("documentan", "muestran", "sostienen"), excepto la línea 36: "quienes **demostraron** que los flujos turbulentos...". Es defendible porque describe un experimento puntual (WRF con/sin flujos), pero conviene decidir conscientemente si se mantiene o se normaliza a presente por consistencia con el resto del capítulo.

### A.10 — Oraciones largas con múltiples atribuciones (línea 5)
La oración que abre con "Modelaciones de alta resolución proyectan..." encadena tres cláusulas con tres citas distintas (`gentile2025response`, `dejesus2021multimodel`, `IPCC2021_WG1_Chapter11_Extremes`) separadas por coma y punto y coma. Es correcta gramaticalmente pero densa; se beneficiaría de dividirse en 2 oraciones para mayor claridad, sobre todo porque —como se detalla en el bloque B— el rango numérico "1.5–2 m/s" corresponde solo a la segunda cita, no a la primera, y el encadenamiento actual dificulta ver esa frontera.

---

## B. Errores de consistencia interna: el texto vs. sus propias tablas

Se comparó el texto narrativo contra `tab_stat_global_w10.tex` y `tab_stat_p90_w10.tex`, que el propio capítulo referencia.

### B.1 — Rango de curtosis mal delimitado (línea 202)
El texto afirma:
> "los valores de curtosis oscilan entre **−0.30** y **−1.03** **durante intensificación y madurez**"

Los valores reales de la tabla para intensificación+madurez (las 6 celdas: SBR, LPB, ARG × 2 fases) son: SBR (−0.910, −0.861), LPB (−1.034, −1.006), ARG (−0.367, −0.430). El mínimo en magnitud de ese subconjunto es **−0.367** (ARG, intensificación), no −0.30. El valor **−0.300** que aparece en el texto corresponde en realidad a **ARG en Decaimiento**, una fase que la oración excluye explícitamente. Es un error de trascripción del rango: o se corrige el límite inferior a −0.37, o se amplía el alcance de la oración para incluir decaimiento.

### B.2 — Interpretación estadística cuestionable: curtosis positiva ≠ bimodalidad
Dos pasajes de la sección p90 (línea 214) interpretan curtosis positiva (leptocúrtica) como evidencia de una distribución **bimodal** o de "bifurcación":

> "LPB exhibe leptocurtosis (γ₂ = +0.96)... indicando una **población bimodal**."
> "SBR... exhibe una **bifurcación extrema** en decaimiento: leptocurtosis (γ₂ = +3.95) con asimetría positiva (+1.15)."

Los valores numéricos coinciden exactamente con la tabla (LPB Intensificación: γ₁=−0.881, γ₂=0.960; SBR Decaimiento: γ₁=1.155, γ₂=3.955), así que no hay error de dato. El problema es conceptual: una curtosis positiva (leptocúrtica) describe típicamente una distribución **unimodal** con pico agudo y colas pesadas (más propensa a valores extremos aislados), no dos modas separadas. La bimodalidad clásica suele asociarse más bien con curtosis **negativa** (platicúrtica), porque la masa se aleja del centro hacia dos protuberancias, aplanando el pico. Sin un test de multimodalidad (p. ej. dip test de Hartigan) o un histograma que lo muestre, la curtosis por sí sola no sustenta la afirmación de "población bimodal" ni "bifurcación". Recomendación: describir estos casos como "distribución con cola extrema/pico agudo" (lo que sí respaldan los datos) o aportar evidencia adicional (histograma, test de bimodalidad) antes de usar el lenguaje de bimodalidad.

---

## C. Verificación de fidelidad a las fuentes citadas

Se revisaron 34 afirmaciones atribuidas a autores contra el contenido de `papers/files_MD/<clave>.md`. Resultado agregado: **~24 coinciden bien, 5 coinciden parcialmente (matiz, recorte o generalización excesiva), y 5 presentan una discrepancia real que amerita revisión** (un supuesto "archivo no encontrado" quedó resuelto abajo, ver C.4).

### C.1 — Coincidencias fuertes, sin observaciones (verificación numérica o textual casi literal)
`bartolomei2024extremos`, `padilhareinke2026characterization` (23.4 m/s / 84.4 km/h y 31.4 m/s / 113.2 km/h confirmados exactamente), `gramcianinov2020analysis` (21.2±4.8, p90 27.3, p95 29.3 en ERA5; 23.4±4.8, p90 30.2, p95 32.1 en CFSR — confirmado exacto, incluida la nota al pie), `gozzo2014subtropical` (300–450 km), `cardoso2020wind` (400–500 km), `clark2005sting`/`clark2018sting`, `hodges2011comparison`, `laurila2021characteristics`, `priestley2022improved` (radio ~3–3.5°), `gentile2023observed`, `stankovic2025surface`, `simmonds2000size`, `hart2003cyclone`, `sinclair1997objective`, `sinclair2023relationship`, `IPCC2021_WG1_Chapter11_Extremes`, `gozzo2013air`, `martinez2014cold`, entre otros.

Nota menor sobre `gozzo2014subtropical` y `cardoso2020wind`: ambos hallazgos de distancia al centro provienen de estudios sobre ciclones **subtropicales**, no extratropicales en general; el uso como referencia de rango es razonable pero podría matizarse.

### C.2 — Afirmaciones que generalizan más de lo que dice la fuente (requieren ajuste de matiz)

**`dejesus2021multimodel` (línea 5)** — La tesis dice "un aumento de hasta 1.5–2 m/s... hacia fines de siglo". El paper reporta proyecciones **por región**, no un rango único: RG1(~SBR) hasta 1.5 m/s, RG2(~LPB) hasta **1 m/s**, RG3(~ARG) hasta 2 m/s. El valor más bajo (1 m/s, LPB) queda oculto por el rango "1.5–2". Sugerencia: especificar por región o ajustar el rango a "1–2 m/s".

**`gramcianinov2024early` (línea 35)** — El mecanismo citado (SBR/LPB dependen de advección cálida y convergencia de humedad de bajo nivel) en realidad remite a un hallazgo previo (Gramcianinov, Hodges & Camargo 2019), no es un resultado nuevo del paper de 2024. Además, el propio artículo de 2024 reporta un compuesto de ARG con presión central más profunda (993 hPa) que el de LPB (~1011–1013 hPa), lo cual no respalda con claridad que "SBR y LPB alcanzan intensidades más extremas" que ARG en profundidad. Vale la pena revisar si esta cita es la más adecuada para la afirmación, o si conviene precisar que se habla de intensidad del *viento superficial* y no de profundidad del sistema.

**`russo2025impacts` (línea 37)** — La tesis presenta como regla general que "la ciclogénesis inicial depende de procesos dinámicos de niveles altos" y que la humedad/calor latente es clave solo después. El paper mismo reporta esto para 4 de 6 casos analizados, pero señala explícitamente **excepciones**: en dos casos (I1, I3) hubo flujos de calor fuertes ya *antes* de la ciclogénesis, y en otro (B3) los flujos continentales influyeron desde la etapa temprana. La tesis omite estas excepciones que el propio paper destaca.

**`hoskins2005new` (línea 135)** — Se cita para "la evolución estructural de los ciclones depende del acoplamiento baroclínico". El paper es una climatología de trayectorias del Hemisferio Sur (rol de los Andes en la génesis, trayectorias medias), no un estudio centrado en acoplamiento baroclínico estructural en el sentido específico usado aquí. Es una atribución genérica/tangencial que convendría revisar o acompañar de una cita más directa.

**`inatsu2004zonal` (línea 137)** — El mecanismo real que describe el paper es el forzamiento de la asimetría zonal por **ondas estacionarias excitadas por TSM** (tropical y local), no exactamente "el flujo estacionario de latitudes medias" como lo parafrasea la tesis. El fenómeno (asimetría zonal de trayectorias) sí coincide, pero el mecanismo descrito difiere en énfasis.

### C.3 — Discrepancias que ameritan corrección

**`dalanhese2023new` (línea 104)** — Se cita para respaldar la "previsibilidad geométrica" de la localización de los máximos de viento. El paper trata en realidad de una climatología comparativa de ciclogénesis en Sudamérica (ERA5 vs. JRA55 vs. datos de la Marina brasileña), centrada en diferenciar ciclogénesis de sotavento andino vs. costera y teleconexiones océanicas de baja frecuencia — no aborda la organización espacial de los máximos de viento dentro del ciclón. **Esta cita no respalda la afirmación específica que se le atribuye**; conviene verificar si la clave bibliográfica correcta es otra, o reemplazar la referencia.

**`hannachi2023eof` (línea 188)** — Se cita para "los modos secundarios de p90 han dejado de ser ruido estadístico". El paper trata sobre "Common EOFs" como herramienta de comparación entre modelos CMIP6 y reanálisis — un tema distinto al de significancia estadística de modos secundarios en un único conjunto de datos. **No se encontró respaldo directo** para la afirmación específica en el contenido revisado.

**`shapiro1990life` (línea 156)** — El archivo `papers/files_MD/shapiro1990life.md` contiene solo una línea de referencia bibliográfica, sin contenido sustantivo para verificar. No es necesariamente un error (es un clásico de 1990, posiblemente sin PDF de texto completo disponible), pero no pudo confirmarse independientemente; las otras tres citas del mismo pasaje (`schultz2021antecedents`, `reboita2022from`, `shapiro1999bridge`) sí confirman el modelo de seclusión cálida rodeada de un anillo de vientos.

### C.4 — Corrección sobre "archivo no encontrado": `rocha2016estudio` (línea 39)
El agente de verificación reportó inicialmente este ítem como "archivo no encontrado", pero se debe a una diferencia de ortografía: el archivo real se llama **`rocha2016estudo.md`** (sin la "i"), mientras que la clave usada en `tex_es/bibliografia.bib` es **`rocha2016estudio`** (con "i"). Verificado directamente: el contenido del paper (líneas 18-20, 35-37) **sí confirma exactamente** la afirmación de la tesis — difluencia en niveles altos, cavado en niveles medios y convergencia en bajos niveles favoreciendo la ciclogénesis cerca de la costa sur/sudeste de Brasil. La cita es correcta en contenido; lo que vale la pena señalar es la inconsistencia menor entre el nombre del archivo fuente y la clave bibliográfica usada (no afecta la compilación porque la clave sí existe en el `.bib`, pero conviene documentarlo para evitar confusión futura, p. ej. si se reorganiza `files_MD`).

---

## Resumen priorizado de acciones

**Prioridad alta (afecta la veracidad del contenido):**
1. Revisar/reemplazar la cita `dalanhese2023new` (línea 104) — no respalda "previsibilidad geométrica".
2. Revisar la cita `hannachi2023eof` (línea 188) — tema del paper no coincide con la afirmación.
3. Corregir el rango de curtosis de la línea 202 (−0.30 no pertenece a intensificación/madurez, sino a decaimiento de ARG).
4. Suavizar o justificar mejor el lenguaje de "bimodalidad"/"bifurcación" a partir de curtosis positiva (línea 214).
5. Ajustar la generalización de `russo2025impacts` (línea 37) para reflejar las excepciones que el propio paper reporta.
6. Revisar el respaldo de `gramcianinov2024early` (línea 35) dado el contraejemplo de profundidad en ARG dentro del mismo paper.

**Prioridad media (matices/precisión):**
7. Precisar por región el rango de `dejesus2021multimodel` (1–2 m/s, no "1.5–2" uniforme).
8. Revisar si `hoskins2005new` e `inatsu2004zonal` son las citas más precisas para los mecanismos descritos en las líneas 135 y 137.

**Prioridad baja (consistencia editorial, no afecta el contenido científico):**
9. Unificar siglas de fase ("Inc"/"Int" → "Ic"/"It", línea 92).
10. Unificar capitalización de "Población Global" (especialmente en la Síntesis).
11. Introducir la sigla "CCB" en su primer uso (línea 94), no en la línea 186.
12. Unificar "sudeste"/"sureste".
13. Corregir el separador decimal con coma en la línea 182.
14. Eliminar o restaurar el párrafo comentado de la línea 134.
15. Corregir las etiquetas `\label` que no siguen la convención `sec:`/`subsec:`, y añadir labels a los tres encabezados que carecen de ellos (líneas 54, 198, 210).
