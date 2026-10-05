# Revisión del Cap. 7 (Prototipos estructurales). Propuestas pendientes de aprobación

Archivo: `tex_es/07.vr1_result04_prototipo.tex` (NO modificado). Fecha: 2026-10-02.
Método: cada cifra, término y comparación regional que el capítulo repite de los Caps. 4, 5 y 6 se cruzó contra el texto YA CORREGIDO de esos capítulos tal como está ahora en el repositorio (no contra una versión anterior ni contra lo que "debería" decir, releído completo con `grep`/`Read` en esta pasada). Citas leídas en `papers/files_MD/*.md` (pasaje real, no solo abstract/key points) para `gozzo2013air`, `shapiro1990life`, `cardoso2022synoptic`, `priestley2022improved`, `reboita2026meteorology`, `gozzo2014subtropical`, `han2025system`, `corner2025classification`. No se verificaron a nivel de píxel las cifras específicas de Δx/Δy de los prototipos (ver sección G); se señala dónde correspondería hacerlo si el usuario lo pide, al mismo nivel que en Caps. 5 y 6.

Dado que este capítulo tiene la función explícita de **consolidar** los Caps. 4-6, el eje más grave no son citas aisladas sino que el capítulo reintroduce, sin matiz, exactamente las afirmaciones y términos que esos tres capítulos ya habían corregido o descartado en esta misma sesión de revisión — deshaciendo ese trabajo en el capítulo que debería reflejarlo con mayor fidelidad.

Orden de presentación sugerido: A (hallazgo transversal, citas/afirmaciones ya descartadas reaparecen) → B (contradicción directa Cap.6↔Cap.7 sobre MEOF vs. EOF univariado) → C (banda enroscada/cuadrante ocluido tratado como mecanismo confirmado) → D (mezcla "temporal"/atribución incorrecta del r de PC1-PC1 al MEOF) → E (atribución orográfica de ARG sin sustento) → F (afirmar "oclusión" como hecho medido) → G (verificación numérica de cifras cruzadas) → H (citas nuevas de este capítulo) → I (shapiro1990life, verificado correcto) → J (las 4 preguntas por figura).

---

## A. Hallazgo transversal: citas y afirmaciones ya descartadas en Caps. 4/5/6 reaparecen en el Cap. 7

**A1. `gozzo2013air` reaparece (l.45, l.58). Necesario, quitar.**
- Texto actual (l.45): "...la fuerte baroclinicidad favorecen una oclusión más rápida, con intrusiones secas que penetran hasta el núcleo del sistema \citep{gozzo2013air}."
- Texto actual (l.58, párrafo completo): "\citet{gozzo2013air} demuestran mediante simulaciones WRF de un ciclón tipo Shapiro-Keyser en el Atlántico subtropical que los flujos de calor latente en superficie son decisivos para la intensidad de la seclusión cálida y para el desarrollo del frente retrocedido... Esto podría explicar por qué la banda de precipitación del prototipo p90 en ARG es más difusa..."
- Verificado en el `.md` fuente: Gozzo & da Rocha (2013) es un estudio de sensibilidad con **un único caso** (ciclón de mayo de 1997) simulado con WRF, que compara una corrida con flujos de calor latente/sensible superficiales y otra sin ellos. Esta cita ya fue rechazada explícitamente en el Cap. 5 y en el Cap. 6 (A2 de `revision_cap6_propuestas.md`: "los flujos de calor latente no se analizan en ningún capítulo de esta tesis") por el mismo motivo: ni el viento, ni la precipitación, ni el MEOF de esta tesis calculan flujos aire-mar. Aquí reaparece, además, como la explicación causal central de todo un párrafo de la Discusión (l.58), ampliando el problema respecto a su aparición puntual en Cap. 6.
- Propuesta: quitar la cita y la atribución causal en ambos lugares. El párrafo de Discusión (l.58) queda sin su premisa central y necesita reconstruirse (ver E más abajo para una alternativa con datos propios).

**A2. "Oclusión más lenta / modulación orográfica" en ARG (l.45, l.78). Necesario, quitar o reformular — ver Sección E.**
- Mismo patrón que A4 de `revision_cap6_propuestas.md`: se buscó esta caracterización en el texto actual de los Caps. 4 y 5 completos y no aparece en ningún lugar. Fue removida del Cap. 6 en esta misma sesión precisamente por no estar sustentada, y aquí reaparece sin cita ni dato propio que la respalde.
- Desarrollo completo en la Sección E.

**A3. "Banda enroscada (wrap-around precipitation)" y "cuadrante ocluido" tratados como mecanismo confirmado, no como hipótesis (l.41, l.43, l.58, l.78, l.80). Necesario — ver Sección C para desarrollo completo, incluida una contradicción directa con `martin1999forcing` tal como se usa en Caps. 5 y 6.**

**A4. "No solo espacial sino también temporal" (l.80). Necesario — ver Sección D.**

**A5. "vórtice ocluido" / "oclusión severa" afirmados como hecho medido (l.41, l.43 "núcleo del sistema ocluido", l.45 "procesos de oclusión severa"). Necesario — ver Sección F.**

---

## B. Contradicción directa entre el cierre del Cap. 6 y la Introducción del Cap. 7: ¿los prototipos usan el MEOF o los EOF univariados?

**B1. Necesario, resolver antes de tocar cualquier otra cosa — afecta la premisa metodológica completa del capítulo.**
- El Cap. 7, Introducción (l.5-7, l.20), es explícito y consistente en que los prototipos se construyen con **los EOF1 univariados independientes** de cada variable (Cap. 4 para viento, Cap. 5 para precipitación), no con el MEOF conjunto del Cap. 6:
  > (l.20) "Se construye a partir de los campos PDFe sobre la grilla lagrangiana fija... combinados con el primer autovector espacial de los análisis EOF independientes (Sección~\ref{sec:eof_tp} y Sección~\ref{sec:eof_wind10})."
- Pero la última oración del Cap. 6 (`tex_es/06.vr1_result03_meof.tex`, última línea, justo antes de la Síntesis), tal como quedó tras la revisión de esta sesión, dice:
  > "Las bases físicas y estadísticas establecidas en este capítulo sustentan los prototipos estructurales presentados en el Capítulo~\ref{cap:prototipos}, donde **la geometría del MEOF1** se integra con las densidades probabilísticas KDE para construir representaciones cuantificadas..."
- Esto es una contradicción directa y verificable entre capítulos: el Cap. 6 afirma que el Cap. 7 usa la geometría del MEOF1 (el modo conjunto de covarianza), mientras que el propio Cap. 7 dice explícitamente que usa los EOF1 univariados e independientes. No es un matiz menor — el Cap. 6 (Sección Discusión/Síntesis, ya revisada) estableció que el MEOF1 está **dominado casi por completo por el viento** en la mayoría de las combinaciones (sesgo de Bretherton, tabla `tab_meof_bias_check.tex`), por lo que presentar los prototipos como "la geometría del MEOF1" sugeriría, incorrectamente, que la precipitación del prototipo ya incorpora la covarianza con el viento, cuando en realidad proviene de un EOF1 de precipitación calculado de forma completamente independiente.
- La Síntesis del propio Cap. 7 (l.80) agrava esto llamando a los prototipos "la síntesis espacial definitiva de los modos de covarianza (MEOF) identificados en el Capítulo~\ref{chap:meof}" — repitiendo la misma imprecisión.
- Propuesta: (i) corregir la última oración del Cap. 6 para que diga algo como "...sustentan los prototipos estructurales presentados en el Capítulo~\ref{cap:prototipos}, donde los patrones EOF1 univariados de cada campo se integran con las densidades probabilísticas KDE..."; (ii) corregir la Síntesis del Cap. 7 (l.80) para que no llame a los prototipos "síntesis... de los modos de covarianza (MEOF)", sino algo como "la síntesis espacial de los patrones dominantes de variabilidad de cada campo (EOF1 univariados) y de su densidad de ocurrencia (PDFe)"; (iii) si se quiere conectar explícitamente con el hallazgo del MEOF (lo cual es legítimo y valioso), hacerlo como una verificación cruzada declarada —no como la base metodológica de los prototipos— por ejemplo: "esta separación geométrica, obtenida de forma independiente a partir de los EOF1 univariados, es consistente con la que documenta el MEOF1 del Capítulo~\ref{chap:meof} mediante un modo de covarianza conjunto."

---

## C. "Banda enroscada (wrap-around precipitation)" y "cuadrante ocluido" como mecanismo confirmado

**C1. l.41 (párrafo "La génesis de esta diferenciación..."). Necesario — contradice directamente el uso ya establecido de `martin1999forcing` en Caps. 5 y 6.**
- Texto actual: "...el remanente de humedad del WCB es arrastrado por la circulación ciclónica hacia la periferia, quedando confinado en el frente retrocedido (\textit{bent-back front}) y formando la banda de precipitación enroscada (\textit{wrap-around precipitation}) en el cuadrante sureste y sur \citep{martin1999forcing}."
- Verificado: tanto el Cap. 5 (l.93, l.252) como el Cap. 6 (l.149), tras la revisión de esta sesión, establecen explícitamente que Martin (1999) describe la banda enroscada en el **cuadrante ocluido** (que en el Hemisferio Sur correspondería a sur-oeste del centro, por inversión del patrón del Hemisferio Norte descrito al norte-oeste del mínimo), y que **la ubicación real observada en esta tesis (este/sureste) coincide más con la posición de la precipitación asociada al WCB que con la del cuadrante ocluido de Martin 1999**:
  - Cap. 5 (l.252): "la distinción entre la banda este-sureste observada en p90 y el cuadrante ocluido del modelo de Shapiro-Keyser se apoya en estudios de ciclones del Hemisferio Norte \citep{martin1999forcing, sawada2021heavy}... Los núcleos de p90 en madurez, al este y sureste del centro, coinciden con la posición de la precipitación asociada al WCB más que con la del cuadrante ocluido" (l.93).
  - Cap. 6 (l.149): "La estructura en arco de precipitación en el cuadrante sureste capturada por el MEOF1 se ubica en una posición más cercana a la del WCB que a la del cuadrante ocluido que \citet{martin1999forcing} describe para la corriente del trowal."
- El Cap. 7 invierte esta conclusión ya establecida: usa `martin1999forcing` precisamente para afirmar que la banda sureste/sur **es** la banda enroscada del cuadrante ocluido, sin la salvedad de que la propia tesis encontró que esa ubicación coincide mejor con el WCB. Esto deshace, en el capítulo de síntesis, el trabajo de calibración terminológica hecho en Caps. 5 y 6 (ver también memoria `feedback_banda_enroscada_vs_arco`).
- Propuesta: reescribir el tramo final de l.41 para que, en vez de afirmar la banda enroscada como mecanismo confirmado vía Martin 1999, describa la geometría observada (arco de precipitación en el sureste) y la conecte con el WCB, citando a Martin 1999 (y/o Sawada 2021) solo para señalar que esta ubicación se distingue de la que ese estudio asocia al cuadrante ocluido propiamente dicho — igual que en Caps. 5 y 6. Reemplazar "banda de precipitación enroscada (wrap-around precipitation)" por "estructura en arco" en este párrafo, consistente con el resto de la tesis ya revisada.

**C2. l.43 (fase de decaimiento, SBR/LPB). Necesario, mismo criterio que C1.**
- Texto actual: "...la banda enroscada sigue orbitando el margen de la intrusión seca incluso cuando la intensidad del sistema se debilita..."
- Propuesta: "estructura en arco" en vez de "banda enroscada"; "intrusión seca" debería ir en condicional (no se mide directamente en ningún capítulo, ver F).

**C3. l.58, l.78, l.80. Necesario, mismo criterio — ver también A1 (gozzo2013air) y D/E para el resto de cada oración.**

---

## D. Mezcla "espacial"/"temporal" y atribución incorrecta del r de PC1-PC1 al MEOF (Síntesis, l.80)

**D1. Necesario, corregir junto con B.**
- Texto actual: "...En conclusión, los prototipos presentados en este capítulo constituyen la síntesis espacial definitiva de los modos de covarianza (MEOF) identificados en el Capítulo~\ref{chap:meof}, cuya anticorrelación entre las PC1 de precipitación y viento durante la madurez ($r$ entre $-0.31$ y $-0.45$ en las tres regiones) respalda que esta separación geométrica no es solo espacial sino también temporal: los eventos que más proyectan sobre la banda enroscada tienden a ser los que menos proyectan sobre el núcleo de viento."
- Dos problemas verificados, además de B (la atribución a "los modos de covarianza (MEOF)"):
  1. La correlación $r$ entre $-0.31$ y $-0.45$ citada corresponde, en el Cap. 6, a la Sección `sec:meof_coherencia` ("Coherencia entre los Modos de Viento y Precipitación", antes "Coherencia Temporal", renombrada en esta sesión precisamente porque es una correlación **entre dos PC1 univariadas independientes a través de los ciclones de la misma fase/región** — transversal, no temporal). El Cap. 7 reintroduce exactamente el error terminológico ("temporal") que el propio Cap. 6 corrigió en su revisión. Las cifras en sí (−0.31 ARG, −0.37 LPB, −0.45 SBR en madurez p90) sí coinciden con la tabla vigente del Cap. 6 (`tab_meof_coherencia.tex`), así que el rango numérico es correcto; el problema es la etiqueta "temporal" y la atribución a "los modos de covarianza (MEOF)" (son los PC1 univariados, no el MEOF1 conjunto).
  2. La Síntesis del Cap. 6 (tal como quedó revisada) ya trata esta misma correlación con el matiz correcto: la llama "Coherencia entre los campos", dice que "está respaldada por la correlación negativa y significativa entre las PC1 univariadas... consistente con la separación en cuadrantes opuestos documentada en el MEOF1" — es decir, el Cap. 6 ya la presenta como evidencia **complementaria e independiente**, no como parte del MEOF. El Cap. 7 debería seguir esa misma formulación en vez de fusionar ambos resultados en uno solo.
- Propuesta: reformular como algo del tipo "...esta separación geométrica, obtenida aquí mediante EOF1 univariados, es consistente con la correlación negativa y significativa entre las PC1 univariadas de precipitación y viento durante la madurez en p90 ($r$ entre $-0.31$ y $-0.45$ en las tres regiones, Capítulo~\ref{chap:meof}), que muestra que los eventos de un ciclo de vida que más proyectan sobre la estructura en arco de precipitación tienden a ser los que menos proyectan sobre el núcleo de viento [sin "espacial"/"temporal", sin "banda enroscada"]." La interpretación con signo en sí es válida para madurez en las tres regiones (ya verificada en el Cap. 6, Sección E, contra la ubicación real del núcleo positivo de cada EOF1), así que no es necesario quitarla, solo corregir el marco conceptual y la terminología.

---

## E. "Oclusión más lenta por modulación orográfica" en ARG, sin sustento

**E1 (l.45). Necesario, quitar o sustituir por una conexión con datos propios.**
- Texto actual: "En ARG (paneles i–l), la oclusión es más lenta debido a la modulación orográfica y a la menor disponibilidad de humedad oceánica y la banda de precipitación resultante es más difusa; sin embargo, la separación euclídea entre las modas de viento y precipitación no resulta menor que en SBR y LPB, sino la mayor de las tres regiones..."
- A diferencia de lo que se planteó como posible hipótesis de partida, el párrafo **no oculta** la tensión entre "oclusión más lenta" y "mayor separación" — de hecho la señala explícitamente y concluye con cautela ("lo que indica que la magnitud de la separación modal no depende linealmente de la velocidad de oclusión ni de la disponibilidad de humedad oceánica"). Ese tratamiento honesto de la tensión es, en sí, un buen ejemplo del punto 6 de la skill (conexión lógica explícita) y no requiere reescritura por esa parte.
- El problema real es la premisa misma ("la oclusión es más lenta debido a la modulación orográfica"): no está sustentada por ninguna cita ni por ningún dato propio de los Caps. 4-6 (búsqueda exhaustiva, igual que en A4 de Cap. 6: no aparece esa caracterización de ARG en ningún capítulo actual de la tesis).
- Propuesta: sustituir la premisa por la conexión alternativa que ya se usó en el Cap. 6 (H2/E3 de `revision_cap6_propuestas.md`, ya aplicada): ARG es la única región donde el EOF1 univariado de precipitación domina de forma más reproducible y donde la correlación PC1-vorticidad se mantiene significativa durante todo el ciclo (Cap. 5, Sección H). Esa conexión con resultados propios, ya verificados, es más defendible que la atribución orográfica. Ejemplo: "En ARG, el EOF1 de precipitación es comparativamente el modo más dominante y reproducible de las tres regiones (Capítulo~\ref{cap:resultados_tp}), lo que podría explicar que la banda de precipitación, aunque más difusa en términos de densidad PDFe, mantenga una posición consistente; la separación euclídea entre las modas de viento y precipitación no resulta menor que en SBR y LPB, sino la mayor de las tres regiones, lo que indica que la magnitud de la separación modal no depende linealmente de un supuesto régimen de oclusión más lento."

**E2 (l.78, Síntesis). Necesario, mismo criterio.**
- Texto actual: "...constituye la firma diagnóstica de la estructura ocluida en esta región y no tiene equivalente en la Población Global" — el tramo "siendo ARG, pese a su oclusión más gradual, la de mayor magnitud" repite la misma premisa sin sustento. Propuesta: quitar "pese a su oclusión más gradual" o sustituirlo por la conexión de E1.

**E3 (l.58, Discusión párrafo 2). Necesario, depende de A1.**
- Una vez quitada la atribución a `gozzo2013air` (A1), la oración "Esto podría explicar por qué la banda de precipitación del prototipo p90 en ARG es más difusa y menos intensa que en SBR y LPB" pierde su mecanismo propuesto. Reconstruir con la misma conexión de E1 (dominancia del EOF1 de precipitación en ARG) en vez de los flujos de calor latente de un caso único.

---

## F. Afirmar "oclusión"/"vórtice ocluido" como hecho medido

**F1 (l.41, l.43, l.45). Necesario, mismo criterio ya aplicado en Caps. 4, 5 y 6 (rechazo de Hart 2003 por no calcularse el espacio de fases).**
- "la convergencia de los procesos de oclusión severa" (l.41), "núcleo del sistema ocluido" (l.41), "vórtice se disipa" vs. "núcleo del vórtice ocluido"... — ninguno de los capítulos de esta tesis mide directamente si un sistema está ocluido (es una inferencia de la fase del ciclo de vida vía CycloPhaser, no una variable calculada, como ya se estableció en Caps. 4-6).
- Propuesta: usar condicional ("compatible con un sistema en proceso de oclusión") o remitir a la fase del ciclo de vida (madurez/decaimiento) en vez de afirmar la oclusión como hecho, igual que D4/D7 de `revision_cap6_propuestas.md`.

**F2 (l.41, l.43) "intrusión seca" como mecanismo confirmado sin condicional.**
- Mismo criterio que en Caps. 5 y 6 (E2 de `revision_cap6_propuestas.md`: "la intrusión seca no se mide directamente en ningún capítulo"). Debe quedar en modo condicional en todas sus apariciones (l.41, l.43, l.78, l.80).

---

## G. Verificación numérica de cifras cruzadas con Caps. 4 y 5

**G1 (l.41) "densidades de hasta 23–27$\times10^{-4}$" (viento NW, p90, Sección~\ref{sec:kde_espacial_p90}). Viable, impreciso pero no claramente falso.**
- El Cap. 4 (Sección `sec:kde_espacial_p90`, l.86 del archivo, PDFe de viento en p90) da: SBR 25–27$\times10^{-4}$, LPB ${\approx}$23–25$\times10^{-4}$, ARG ${\approx}$19–21$\times10^{-4}$. El rango real por región no es uniforme; "hasta 23–27" combina el límite superior de SBR (27) con el límite inferior de LPB (23) sin indicar que ARG está claramente por debajo (19–21). No es falso (27 es, en efecto, el máximo observado), pero es una simplificación que oculta que ARG tiene una concentración menor.
- Propuesta: "con densidades de hasta 27$\times10^{-4}$ en SBR y 23–25$\times10^{-4}$ en LPB (Sección~\ref{sec:kde_espacial_p90})" o similar, si se quiere mantener el nivel de detalle regional que el resto del capítulo usa en otros lugares.

**G2 (l.41) "concentración del EOF1 de precipitación hasta 36.5% en LPB durante el decaimiento (Sección~\ref{subsec:var_exp_tp})". Confirmado correcto, sin cambios.**
- Coincide exactamente con el Cap. 5 (l.118, l.164, l.246: "36.5% en decaimiento" LPB).

**G3. Cifras de separación Δx/Δy y distancia euclídea (l.22-47) no verificadas a nivel de píxel en esta pasada — Viable, señalar para decisión del usuario.**
- Igual que C1 de `revision_cap6_propuestas.md`, estas cifras específicas por panel (ej. "$\Delta x = 6{,}8^{\circ}$, $\Delta y = -1{,}9^{\circ}$" para SBR-madurez-p90) no se verificaron contra los datos reales de los prototipos en esta pasada, por volumen y porque no se identificó un CSV fuente de coordenadas modales en `defensa/csv_data/` (a diferencia de PC1 y MEOF, que sí tienen CSV). Si el usuario quiere el mismo nivel de rigor que en Caps. 5 y 6, correspondería buscar o generar ese CSV (o extraer las coordenadas de las estrellas directamente de las figuras `prototipo_12panels_*.png`) antes de confiar en estas cifras como definitivas.

---

## H. Citas nuevas de este capítulo (no evaluadas en Caps. 4-6)

**H1. `cardoso2022synoptic` (párrafo 1 de Discusión, l.54). Viable, correctamente etiquetada pero merece un matiz de categoría.**
- Verificado: Cardoso et al. (2022) estudia específicamente **ciclones subtropicales** (SC, sistemas híbridos de núcleo cálido en niveles altos) del Atlántico Sur, no ciclones extratropicales baroclínicos como los catalogados en esta tesis (`coutodesouza2024new`, vía $\zeta_{850}$). El Cap. 7 ya los llama correctamente "ciclones subtropicales" y no los presenta como la misma categoría, así que no hay error de atribución, pero dado que el resto de la tesis es cuidadosa en distinguir categorías de sistemas, valdría la pena una cláusula breve señalando que son un tipo de sistema relacionado pero distinto (p. ej. "...coherente con \citet{cardoso2022synoptic} para ciclones subtropicales (sistemas híbridos, distintos de los ETC baroclínicos aquí analizados) del Atlántico Sur..."). Dominio Lagrangiano de 20°×20° centrado en el ciclón, confirmado por los \textit{key points} del paper. Propuesta: Viable, agregar la cláusula de distinción de categoría si el usuario lo considera necesario.

**H2. `priestley2022improved` (párrafo 3, l.62). Confirmado correcto.**
- Verificado en el `.md`: el estudio usa un dominio de ~20° centrado en la trayectoria sobre composites del percentil 90 de vorticidad ciclónica en ERA5 (igual criterio/escala que esta tesis), y encuentra que la CCB se concentra en el "westward flank"/"rear flank" del vórtice — coincide con lo que el Cap. 7 describe ("concentran en el flanco posterior-occidental"). El capítulo ya aclara correctamente que ese estudio no analiza precipitación. Sin cambios.

**H3. `gozzo2014subtropical` (párrafo 3, l.64). Viable, verificar si es el mejor respaldo para "estructura híbrida".**
- Verificado: es la climatología de ciclones subtropicales del Atlántico Sur (Gozzo et al. 2014), misma familia de sistemas que `cardoso2022synoptic` (ver H1), y confirma la noción de "ciclón híbrido" en el resumen. Uso razonable y acotado ("muchos de los sistemas p90... estructura híbrida"), aunque de nuevo cabría un matiz: los sistemas p90 de esta tesis son ETC baroclínicos catalogados por $\zeta_{850}$, no necesariamente sistemas subtropicales en el sentido de Gozzo 2014; "estructura híbrida" aplicada a los p90 de esta tesis sin verificación directa (no se calcula el espacio de fases de Hart, ya rechazado en Caps. 4-6) es una extrapolación. Propuesta: matizar con condicional ("cercanos, en algunos casos, a una estructura híbrida") o quitar si se prefiere no abrir esa comparación sin el cálculo correspondiente.

**H4. `han2025system` (SyCLoPS, párrafo 4, l.68). Viable, uso general razonable, un matiz menor sobre "no lineal entre fases".**
- Verificado parcialmente (abstract/estructura): SyCLoPS es un framework de clasificación objetiva de sistemas de baja presión (TC, ETC, subtropicales, etc.) a nivel global, que efectivamente caracteriza estructura, viento y precipitación por clase y fase. La afirmación específica "esta relación no es lineal entre fases" no se verificó contra el cuerpo completo del paper (solo el abstract/introducción), por lo que queda pendiente de una lectura más profunda si el usuario quiere el mismo nivel de rigor aplicado a otras citas de los Caps. 4-6. Uso general (comparación metodológica, SyCLoPS vs. prototipos de esta tesis) es razonable y no hay mala atribución evidente.

**H5. `corner2025classification` (párrafo 4, l.68). Viable, uso distinto al de Cap. 6 (donde se encontró una imprecisión sobre "profundización", F2 de `revision_cap6_propuestas.md`) — aquí el uso es genérico ("análisis multivariado de parámetros dinámicos... caracterización objetiva y cuantificada") y no repite ese problema específico. Sin cambios necesarios.**

**H6. `reboita2026meteorology` (SALLJ, l.45). Confirmado correcto, uso específico y acotado.**
- Verificado: el paper sí describe el SALLJ como mecanismo de transporte de humedad tropical hacia el sureste de Sudamérica, consistente con el uso puntual que le da el Cap. 7.

**H7. `schemm2014linkage` (l.41) y `martinez2014cold`/similares no repetidos aquí. Sin cambios — ya evaluados y aceptados en Caps. 4 y 6 con esta misma función (vínculo CCB-circulación de bajo nivel).**

**H8. `han2025system`, `corner2025classification`, `gramcianinov2023impact`, `deSouza2025CycloPhaser` (párrafo 5, limitaciones). Viable, usos acotados y consistentes con su función ya establecida en Cap. 1/Introducción (CycloPhaser) y Cap. 6 (gramcianinov2023impact, velocidad de traslación). Sin cambios necesarios.**

---

## I. `shapiro1990life` — verificado, uso correcto (no es un problema, a diferencia de lo que se sospechaba al iniciar esta revisión)

**I1. Confirmado: `shapiro1990life` (Shapiro & Keyser, 1990, "Fronts, jet streams and the tropopause") es la cita ya establecida en el Cap. 2 (Fundamentos, l.10 y l.90) y en el Cap. 1 (Introducción, l.52) para el modelo conceptual Shapiro-Keyser en sí (fractura frontal, frente curvado, T-bone, seclusión cálida) — verificado en el `.md` fuente, Sección 10.4 "The Life Cycle of the Marine Extratropical Cyclone" contiene exactamente ese modelo. No es la misma cita que `shapiro1999bridge`, reservada en Caps. 5 y 6 para una observación específica de un único ciclón del Hemisferio Norte (subsidencia al oeste, precipitación al este) usada con el matiz de "caso único". El Cap. 7 usa `shapiro1990life` consistentemente con Caps. 1 y 2 para el modelo general. Sin cambios necesarios en esta distinción.**

**I2 (l.58) "la transición al modelo de Shapiro-Keyser \citep{shapiro1990life} documentada para el Atlántico Sur". Viable, ambigüedad de redacción.**
- La frase puede leerse como si `shapiro1990life` documentara el modelo específicamente para el Atlántico Sur (no es así, es un estudio del Hemisferio Norte/marco general). Lo que probablemente se quiere decir es que la transición al modelo SK ya ha sido documentada para el Atlántico Sur por otros trabajos (p. ej. Gozzo, Reboita). Propuesta: reformular como "...la transición al modelo de Shapiro-Keyser \citep{shapiro1990life}, ya documentada para el Atlántico Sur por estudios de caso \citep{gozzo2013air}..." (si se mantiene gozzo2013air con el matiz de caso único) o quitar "documentada para el Atlántico Sur" si se prefiere no reabrir esa cita.

---

## J. Las 4 preguntas por figura (qué es / cómo es / por qué es así / para qué)

**J1. `fig:prototipo_global` y `fig:prototipo_p90`. Viable, satisfechas pero distribuidas entre secciones distintas a las de la figura — mismo patrón que Caps. 4-6, no requiere cambio estructural.**
- Qué es / cómo es: cubierto en la Introducción (l.5-7, construcción) y en el cuerpo de cada sección (l.18-20, l.37).
- Por qué es así: se responde principalmente en la Discusión (mecanismos WCB/CCB/Shapiro-Keyser), no inmediatamente después de presentar la figura — consistente con el patrón ya usado en Caps. 4-6 (separar descripción de interpretación mecanicista). Sin cambio necesario, condicionado a que los mecanismos citados en la Discusión queden correctamente matizados (Secciones C-F de este documento).
- Para qué: explícito en ambas secciones ("su propósito es sintetizar...", l.20; "cerrando el argumento analítico...", l.37).

---

## Citas: resumen de decisiones (propuesta, pendiente de aprobación)

**Se mantienen (verificadas):** `shapiro1990life` (modelo SK general, uso correcto y consistente con Caps. 1-2), `schemm2014linkage`, `priestley2022improved`, `corner2025classification`, `reboita2026meteorology`, `han2025system`, `deSouza2025CycloPhaser`, `gramcianinov2023impact`, `cardoso2022synoptic` (con matiz de categoría sugerido, H1), `gozzo2014subtropical` (con matiz condicional sugerido, H3), `martin1999forcing` (reformulando su alcance, igual que en Caps. 5/6 — no respalda que la banda SE/S observada SEA el cuadrante ocluido).

**Se quitan (ya rechazadas en Caps. 5/6 por el mismo motivo, reaparecen aquí sin justificación nueva):** `gozzo2013air` (A1).

Tras quitar, no borrar del `.bib` (ya usada/evaluada en otros capítulos).

---

## Preguntas pendientes para el usuario antes de proponer texto

1. **B1 (la más urgente)**: ¿corrijo primero la última oración del Cap. 6 (que dice que el Cap. 7 usa "la geometría del MEOF1") para que sea consistente con la Introducción del Cap. 7 (que usa EOF1 univariados), o prefieres discutir primero si en algún momento sí quieres rehacer los prototipos con el MEOF en vez de los EOF univariados? Esto determina cómo se reescribe tanto el cierre del Cap. 6 como la Síntesis del Cap. 7 (D1).
2. **C1/A1**: ¿confirmas que se reescriba el párrafo de "génesis de esta diferenciación" (l.41) con el mismo criterio de Caps. 5/6 (estructura en arco + WCB, sin "banda enroscada"/cuadrante ocluido confirmado, sin gozzo2013air)?
3. **E1/E3**: ¿prefieres quitar sin más la atribución orográfica/gozzo2013air de ARG, o construir la conexión alternativa con la dominancia del EOF1 de precipitación de ARG (Cap. 5), igual que se hizo en el Cap. 6 (H2)?
4. **G3**: ¿quieres que verifique las cifras de Δx/Δy y distancia euclídea de los prototipos contra un CSV fuente o extracción de las figuras reales, al mismo nivel de rigor que se aplicó en Caps. 5 y 6? No se encontró un CSV de coordenadas modales en `defensa/csv_data/` en esta pasada; habría que confirmar si existe en otra ruta o generarlo.
5. **H1/H3**: ¿agregamos las cláusulas de matiz de categoría para `cardoso2022synoptic` y `gozzo2014subtropical` (sistemas subtropicales/híbridos, distintos de los ETC baroclínicos de esta tesis), o se consideran innecesarias dado que el capítulo ya los llama correctamente "subtropicales"?
