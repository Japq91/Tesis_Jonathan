> **Actualización 2026-07-27:** los 2 hallazgos de prioridad alta (B.3.1 `gramcianinov2024early` y B.3.2 `andrade2024composite`) fueron corregidos en el `.tex`. `gramcianinov2024early` → `crespo2020potential` (Cap. 07, banda enroscada/SALLJ); `andrade2024composite` → `mendes2010climatology, simmonds2000mean` (Cap. 06, desplazamiento de trayectoria hacia el sureste). También se unificó terminología: SALLJ (antes "chorro de capas bajas"/"Chorro de Bajos Niveles" con 4 variantes) y "sudeste"→"sureste" en toda la tesis. Ver `auditoria_coherencia_global.md` para el detalle completo de la unificación terminológica.

# Auditoría — Análisis MEOF (Cap. 06) y Prototipos estructurales (Cap. 07)

**Archivos auditados:** `tex_es/06.vr1_result03_meof.tex`, `tex_es/07.vr1_result04_prototipo.tex`
**Fuentes de verificación:** `papers/files_MD/*.md`, `tex_es/bibliografia.bib`, cruce de labels con el resto de `tex_es/`
**Fecha:** 2026-07-27
**Nota:** primera auditoría de estos dos capítulos (nunca revisados antes). Mismo formato que `auditoria_04.vr1_result01_w10.md` y `auditoria_05.vr1_result02_tp.md`: (A) redacción/estructura, verificado directamente; (C) fidelidad de citas, verificado con un agente dedicado que leyó cada `.md` en `papers/files_MD`.

---

## A. Redacción, consistencia y estructura

### A.1 — Sin errores estructurales graves
A diferencia de los Capítulos 04 y 05 en su versión vr1, estos dos capítulos (aunque también vr1) **no presentan**: referencias cruzadas rotas, etiquetas con prefijo incorrecto (`sec:`/`subsec:`/`subsubsec:` bien aplicados en los 20 labels revisados), texto comentado "flotando" (todos los `%` son encabezados organizativos, ej. `% --- PÁRRAFO 1...`), ni inconsistencias de capitalización en "Población Global" (0 ocurrencias en minúscula en ambos capítulos) ni separador decimal (coma vs. punto — ambos usan coma de forma consistente en `9{,}5^{\circ}`, a diferencia del error puntual detectado en el Cap. 04 vr1). Se verificaron los 20 `\ref` de ambos capítulos contra los `\label` del resto del proyecto: **todos resuelven correctamente**, ninguno queda en "??".

### A.2 — Redundancia del mecanismo "intrusión seca → CCB noroeste / banda enroscada sureste" (repetido 3 veces casi textualmente)
El mismo mecanismo físico se explica de forma casi completa en tres capítulos sucesivos:

**Cap. 05, línea 40:**
> "Los ciclones p90... el núcleo experimenta entonces una intrusión seca (*dry intrusion*) inducida por la fractura frontal, mediante la cual aire frío, subsidente y de baja humedad de la alta troposfera o estratosfera se enrosca hacia el centro del sistema \citep{shapiro1999bridge}."

**Cap. 06, línea 118:**
> "...la caída de presión acelerada induce una profunda intrusión seca (*dry intrusion*) que suprime la convección en el núcleo del vórtice y empuja la humedad residual del WCB hacia la banda enroscada exterior \citep{shapiro1999bridge}. ...la cinta transportadora fría (CCB) se consolida en el sector noroeste mientras el WCB residual se reconfigura en la banda periférica sureste."

**Cap. 07, línea 41:**
> "...la cinta transportadora fría (*cold conveyor belt*, CCB) se enrolla alrededor del núcleo del sistema ocluido, generando el máximo de circulación de bajo nivel en el sector posterior... Simultáneamente, la intrusión seca (*dry intrusion*) penetra desde la alta troposfera hacia el núcleo central del ciclón, erradicando la convección profunda y generando el característico pasillo libre de precipitación (*dry slot*)... formando la banda de precipitación enroscada (*wrap-around precipitation*) en el cuadrante sureste y sur."

Es el mismo patrón ya señalado en la auditoría 01-03 (mecanismo explicado con el mismo nivel de detalle en vez de remitir). Aquí es defendible en parte porque cada capítulo aporta una capa nueva (05: precipitación; 06: covarianza MEOF; 07: síntesis visual del prototipo), pero la Sección 07 en particular podría reducirse a "esta reorganización responde al mecanismo de intrusión seca / CCB ya establecido (Secciones~\ref{sec:pdf_tp} y~\ref{sec:discusion_meof})" en vez de repetir los tres términos técnicos (*dry intrusion*, *dry slot*, *bent-back front*, *wrap-around precipitation*) por tercera vez consecutiva.

### A.3 — Terminología del chorro de bajo nivel, inconsistente en todo el documento (no solo 06/07)
Se confirma y amplía el hallazgo A.8 de `auditoria_05`: la variante usada en Cap. 06 (línea 151) y Cap. 07 (línea 45) es "chorro de capas bajas" (minúscula), mientras Cap. 02 y Cap. 05 alternan entre "Chorro de Capas Bajas" (mayúscula) y "corriente en chorro de bajo nivel", y Cap. 04 usa "chorro de bajo nivel"/"corrientes en chorro de niveles bajos". Es el mismo concepto (SALLJ / low-level jet) con al menos 4 formulaciones distintas a lo largo de la tesis. Ver también sección B (coherencia global) más abajo.

### A.4 — Uso correcto y sin inconsistencia de "sudeste"/"sureste"
A diferencia del Cap. 04 (que mezclaba "sudeste" y "sureste"), los Capítulos 06 y 07 usan consistentemente **"sureste"** en las 20 ocurrencias combinadas. Esto es positivo pero crea una inconsistencia de tesis completa: Cap. 01 usa "sudeste" 1 vez, Cap. 04 mezcla ambas, Cap. 06/07 solo "sureste" — no hay un criterio único a nivel de documento (ver sección de coherencia global).

---

## B. Verificación de fidelidad a las fuentes citadas

Se verificaron 23 afirmaciones citadas contra `papers/files_MD/<clave>.md`. Resultado agregado: **13 coinciden bien, 6 coinciden parcialmente, 3 son discrepancias que ameritan corrección, 1 no verificable** (archivo vacío).

**Hallazgo positivo destacable:** el patrón `hannachi2023eof` (cita de "Common EOFs" para comparación de modelos CMIP6, usada incorrectamente **dos veces** en los Capítulos 04 y 05 para respaldar afirmaciones sobre significancia de modos EOF en ciclones) **no se repite en estos capítulos**. La única cita de Hannachi presente es `hannachi2007empirical` (Cap. 06, línea 16) — un *review* general de EOF genuinamente pertinente para el argumento de aplanamiento del espectro de autovalores.

### B.1 — Coincidencias fuertes (selección)
- `martin1999forcing` (Cap. 06 L145; Cap. 07 L41): coincidencia **literal** — el abstract real dice *"This airstream is referred to as the 'trowal airstream'... responsible for the production of the 'wraparound' cloud and precipitation"*. La mejor cita de ambos capítulos.
- `schemm2014linkage` (Cap. 06 L148): coincidencia casi literal con el abstract sobre anomalías de PV en WCB/CCB. (Nota: el archivo real es `schemm2014ccb.md`, no `schemm2014linkage.md` — mismo patrón de discrepancia de nombre ya visto antes con `rocha2016estudio`/`rocha2016estudo` y `catto2015fronts`/`catto2015front`).
- `corner2025classification`, `han2025system`, `priestley2022improved`, `gozzo2013air`, `martinez2014cold`, `browning1986conceptual`, `eisenstein2023identification`, `evans2012climatology`+`gozzo2014subtropical`, `deSouza2025CycloPhaser`, `gramcianinov2023impact` (línea 72, velocidad de traslación): todos verificados con coincidencia buena o literal.
- Mención especial: `priestley2022improved` (Cap. 07 L62) es la cita **mejor matizada** de todo el capítulo — la tesis aclara explícitamente que ese estudio es del Hemisferio Norte y no analiza precipitación, evitando sobregeneralizar.

### B.2 — Coincidencias parciales / generalización excesiva
- **`oertel2021warm`** (Cap. 06 L145): el mecanismo general (convección embebida en WCB genera precipitación intensa localizada) es correcto, pero el paper estudia un WCB **activo en ascenso** (caso NAWDEX), no el "remanente retrocedido" de un WCB en oclusión como lo aplica la tesis.
- **`schultz2021antecedents`** (Cap. 06 L118; Cap. 07 L41): es un análisis **histórico-bibliográfico** sobre el origen del modelo Shapiro-Keyser en la Escuela de Bergen, no un estudio dinámico de la CCB. Atribuirle la explicación mecanicista ("la CCB se enrolla... generando el máximo de circulación") excede su contenido real.
- **`gramcianinov2019properties`** (Cap. 06 L151): vincula el SALLJ con humedad en la *génesis*, no con velocidad de oclusión en SBR/LPB; el propio paper describe la oclusión como distribuida hacia latitudes antárticas, no concentrada en SBR/LPB.
- **`gramcianinov2023impact`** (Cap. 07 L54): usado para "los composites climatológicos no capturan la reorganización espacial viento-precipitación" — el paper trata de tendencias de olas extremas asociadas a ciclones, un respaldo genérico, no un hallazgo específico sobre esa limitación.
- **`bartolomei2024extremos`** y **`reboita2010south`** (Cap. 06 L32): usadas para "variabilidad de intensidad inter-sistémica" en fase incipiente; Bartolomei es un estudio de caso de solo 2 ciclones y Reboita trata variabilidad **interanual** de frecuencia, no variabilidad de intensidad entre sistemas dentro del ciclo de vida. Sería más apropiado citar a Hart (2003) o al propio `deSouza2025CycloPhaser`.

### B.3 — Discrepancias que ameritan corrección
1. **`gramcianinov2024early`** (Cap. 07, línea 45) — **tema equivocado**: la tesis lo cita para "la disponibilidad de humedad tropical canalizada por el SALLJ sostiene la banda enroscada de precipitación" (fase de madurez/oclusión), pero el paper real trata específicamente de mecanismos de la **fase temprana/génesis** y de la capacidad de modelos climáticos regionales para representarla — no aborda en absoluto la banda enroscada. Es la fase opuesta del ciclo de vida a la que estudia el paper.
2. **`andrade2024composite`** (Cap. 06, línea 33) — la tesis lo cita para "los ciclones intensos desplazan su trayectoria hacia el sur y el océano abierto... alejándose del litoral" en decaimiento. El abstract real dice lo contrario para el conjunto general: *"as the explosive cyclone's intensity increases... a more significant impact in the coastal areas of Southern Brazil and Uruguay"* — mayor intensidad se asocia a **mayor** impacto costero, no a alejamiento. La cita, tal como está usada, no sustenta con claridad la afirmación y en un punto parece contradecirla.
3. **`hannachi2007empirical`** (Cap. 06, línea 16) — no es un error del mismo tipo que `hannachi2023eof`, pero la frase "señalan... que un espectro de autovalores aplanado es el indicador estadístico de un sistema complejo y multidimensional" es una paráfrasis interpretativa de un punto metodológico general (degeneración de autovalores en EOF), no una cita textual sobre complejidad dinámica de ciclones. Suavizar el verbo de atribución.

### B.4 — No verificable
- **`bjerknes1922life`** (Cap. 06, línea 136): el archivo `.md` correspondiente existe pero está **completamente vacío**. No se pudo verificar, aunque es la referencia fundacional menos controvertida de la meteorología sinóptica.

---

## Resumen priorizado de acciones

**Prioridad alta:**
1. Corregir/reemplazar `gramcianinov2024early` (Cap. 07, línea 45) — trata de la fase de génesis, no de la banda enroscada en madurez/oclusión.
2. Revisar `andrade2024composite` (Cap. 06, línea 33) — el abstract del paper parece contradecir el sentido de "alejamiento de la costa"; verificar si hay una sección específica que sí respalde esto o sustituir la cita.

**Prioridad media:**
3. Ajustar `schultz2021antecedents` (Cap. 06 L118; Cap. 07 L41) — es histórico-bibliográfico, no dinámico; considerar citar además Shapiro & Keyser (1990) original o `schemm2014linkage`/`martinez2014cold` para el mecanismo.
4. Revisar `gramcianinov2019properties` (Cap. 06, línea 151) y matizar `reboita2010south`/`bartolomei2024extremos` (línea 32) — tipo de variabilidad/fase distinto al que describe cada paper.
5. Suavizar la atribución de `hannachi2007empirical` (línea 16): cambiar "señalan... al establecer que" por "es consistente con...".
6. Matizar `oertel2021warm` (L145) y `gramcianinov2023impact` (Cap.07 L54) — mecanismo general correcto, contexto específico del paper distinto.
7. Reducir la Sección de Discusión del Cap. 07 (línea 41) para remitir al mecanismo ya extendido en Cap. 05/06 en vez de repetirlo por tercera vez con los mismos 4 términos técnicos en inglés.

**Prioridad baja:**
8. Documentar que `bjerknes1922life.md` está vacío y que `schemm2014linkage` (clave `.bib`) corresponde al archivo `schemm2014ccb.md` (no `schemm2014linkage.md`).
9. Unificar la terminología del chorro de bajo nivel (SALLJ) en toda la tesis — ver `auditoria_coherencia_global.md`.

**Hallazgo positivo a destacar:** estos son, de los cuatro capítulos de resultados auditados hasta ahora, los que presentan **mejor calidad estructural** (sin refs rotas, sin comentarios muertos, sin errores de capitalización) y **mejor fidelidad de citas** (más de la mitad fuertes, sin repetir el error `hannachi2023eof`). El nivel de matización explícita de límites de las fuentes (ej. `priestley2022improved`) es el más alto observado en la tesis.
