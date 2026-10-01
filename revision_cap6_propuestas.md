# Revisión del Cap. 6 (MEOF). Propuestas pendientes de aprobación

Archivo: `tex_es/06.vr1_result03_meof.tex` (NO modificado). Fecha: 2026-10-01.
Método: valores verificados visualmente contra las figuras en `images/meof/` (lectura directa de los paneles, sin extracción de color por píxel exhaustiva por restricción de tiempo — donde no se verificó al nivel de detalle del Cap. 5, se indica explícitamente); cifras cruzadas contra `tabelas_es/tab_meof_coherencia.tex`; citas leídas en `papers/files_MD/*.md` (pasaje real, no solo abstract); cada cifra y comparación regional que el capítulo repite de los Caps. 4 y 5 se cruzó contra el texto YA CORREGIDO de esos capítulos tal como están ahora en el repositorio (no contra una versión anterior).

Criterio de citas: igual que en Caps. 4 y 5 — se mantienen autores que UBICAN los campos respecto al centro o comparan covarianza/coherencia estructural directamente comparable al MEOF; se quitan los de génesis, casos únicos no comparables, flujos no analizados, o mecanismos en cadena no evaluados.

Orden de presentación sugerido: A (hallazgo transversal más grave, citas ya rechazadas en Cap. 4/5 reaparecen aquí) → B (varianza conjunta) → C (MEOF1 intensificación) → D (MEOF1 madurez) → E (coherencia temporal PC1-PC1) → F (discusión) → G (síntesis, forma) → H (hallazgos nuevos).

---

## A. Hallazgo transversal: citas y afirmaciones ya descartadas en Caps. 4/5 reaparecen en el Cap. 6

Esto es lo más urgente de resolver porque afecta varios párrafos del capítulo a la vez.

**A1. `schultz2021antecedents` citado como si describiera el modelo de Shapiro-Keyser (l.120). Necesario, quitar.**
- Texto actual: "La interpretación física de esta reorganización espacial es consistente con el modelo de ciclón ocluido de Shapiro-Keyser \citep{schultz2021antecedents}."
- Verificado: Schultz & Keyser (2021, BAMS) es un artículo **histórico/bibliográfico** sobre los antecedentes del modelo Shapiro-Keyser en la literatura de la Escuela de Bergen (1920s-1950s). No describe, deriva ni valida el modelo en sí — es un rastreo de quién usó ideas similares (fractura frontal, frente curvado, seclusión cálida) antes de 1990. No contiene ningún mecanismo físico nuevo sobre oclusión, CCB, intrusión seca o precipitación.
- Esta misma cita ya fue rechazada en el Cap. 4 y en el Cap. 5 (B16/F13 del Cap. 5: "artículo histórico sobre antecedentes del modelo Shapiro–Keyser") por el mismo motivo, pero reaparece aquí.
- Propuesta: quitar la cita. Si se quiere citar el modelo de Shapiro-Keyser en sí, correspondería \citet{shapiro1999bridge} (ya usado en el capítulo) u otra fuente que describa el modelo directamente, no sus antecedentes históricos.

**A2. `gozzo2013air` citado para flujos de calor latente oceánico (l.154). Necesario, quitar.**
- Texto actual: "En SBR y LPB, la disponibilidad de flujos de calor latente oceánico \citep{gozzo2013air} genera las oclusiones más rápidas..."
- Esta cita ya fue rechazada explícitamente en el Cap. 5 ("gozzo2013air: flujos aire-mar (no analizados). Quitar según criterio"). Los flujos de calor latente no se analizan en ningún capítulo de esta tesis (ni viento, ni precipitación, ni MEOF calcula flujos turbulentos).
- Propuesta: quitar la cita y la atribución causal a "flujos de calor latente oceánico" como explicación del desacople MEOF.

**A3. `coutodesouza2024thesis` (energía diabática $G_E$) citado para La Plata vs. ARG (l.154). Necesario, quitar.**
- Texto actual: "...consistente con la mayor generación de energía diabática ($G_E$) que \citet{coutodesouza2024thesis} documenta para La Plata frente a ARG (Sección~\ref{sec:pdf_tp})."
- Esta cita ya fue rechazada explícitamente en el Cap. 5 ("Couto de Souza 2024 (G_E): términos energéticos integrados → quitar"). Además, la Sección~\ref{sec:pdf_tp} (PDF de precipitación, Cap. 5) **no contiene ninguna mención a esta cita ni a $G_E$** tras la revisión — el cruce de referencia también está roto.
- Propuesta: quitar la cita y la referencia cruzada a `sec:pdf_tp` para este punto específico.

**A4. "oclusiones más graduales y el mayor control orográfico ya documentados en los capítulos previos" (l.129) y "la modulación orográfica y la menor disponibilidad de humedad oceánica producen oclusiones más graduales" para ARG (l.154). Necesario, quitar o reformular.**
- Verificado exhaustivamente: ni `sec:pdf_wind10` (Cap. 4) ni `sec:pdf_tp` (Cap. 5), las dos secciones citadas, contienen ninguna afirmación sobre "oclusiones más graduales" o "control orográfico" para ARG. Se buscó en los capítulos 4 y 5 completos (no solo esas secciones) y **no aparece en ningún lugar actual de la tesis** esa caracterización de ARG. (Si existió antes, fue removida en la revisión del Cap. 5 de esta misma sesión, Sección H10/I7 de `revision_cap5_propuestas.md`, precisamente por no estar sustentada.)
- El único mecanismo orográfico que sí aparece en el Cap. 4 es sobre **LPB**, no ARG: "el desarrollo inicial está influenciado por una baja orográfica" (Gramcianinov 2019), algo distinto y no relacionado con la gradualidad de la oclusión de ARG.
- Propuesta: quitar ambas afirmaciones, o si el usuario quiere mantener una explicación para por qué ARG mantiene el acoplamiento PC1$^{precip}$-PC1$^{viento}$ más tiempo, construirla con datos propios de este mismo capítulo (ver sección F más abajo, el paralelo con el Cap. 5 — la correlación significativa persistente de ARG en PC1 univariado, Sección H4 del Cap. 5, podría ser una conexión más sólida y ya verificada).

---

## B. Fraccionamiento de la varianza conjunta (Figura `all_expvar_meof.png`, fig:all_expvar_meof)

**B1 (l.13) "un valor intermedio entre el EOF1 univariado del viento (43–57%) y el de precipitación (11–16%)". Necesario, verificar cifra del viento.**
- El rango del EOF1 univariado del viento en la Población Global, según el Cap. 4 ya revisado, es **30.9%–57.4%**, no "43–57%". El capítulo 6 usa una cifra que no coincide con el Cap. 4 actual.
- Propuesta: corregir a "30.9%–57.4%" (Sección~\ref{sec:var_exp_wind10}).

**B2 (l.13) "con caída progresiva hacia los modos secundarios" + cifra 19-27%. Viable, verificar visualmente.**
- Confirmado visualmente en la figura (panel a): el MEOF1 (columna 1) domina claramente sobre los modos 2-5 en todas las filas de la Población Global, con las celdas más cálidas (naranja, ~20-28%) concentradas en la columna 1. Consistente con el texto.

**B3 (l.15) "mínimos de 11.65% en ARG durante la intensificación y 15.41% en ARG durante la madurez". Viable, consistencia interna confirmada.**
- Estas cifras coinciden exactamente con las repetidas más adelante en el texto (l.55: "11.65% (ARG)" en intensificación p90; l.99: "15.41% (ARG)" en madurez p90) y con el título de la Figura `meof1_mature_p90.png` ("Explained Variance = 15.41%"), confirmado visualmente. No se verificó contra el CSV fuente (no se encontró un CSV de MEOF en `defensa/csv_data`, a diferencia de viento y precipitación) — si existe, valdría la pena confirmar numéricamente.

**B5 (l.13, l.15, l.160, l.99) Rango exacto del MEOF1, verificado contra el CSV fuente. Necesario.**
- Se encontró el CSV fuente del MEOF en `/p1-swell/japq/defensa/csv_data/tp_wind10_meof_global.csv` y `tp_wind10_meof_p90.csv` (no estaba documentado en el capítulo ni se había usado antes para verificar). Con los 12 valores de MEOF1 (modo 1) por región×fase:
  - **Población Global**: el rango real es **14.8%–26.6%** (mínimo: ARG incipiente, 14.80%; máximo: LPB madurez, 26.59%). El texto dice "entre el 19% y el 27%" (l.13) — el mínimo real (14.8%) está muy por debajo del 19% citado; cuatro de las doce celdas (SBR Ic=17.78, LPB Ic=15.03, ARG Ic=14.80, ARG Dec=17.42) quedan por debajo del "19%" que el texto da como piso.
  - **p90**: el rango real es **11.65%–23.47%** (mínimo: ARG intensificación, 11.65%, ya citado correctamente en el texto; máximo: LPB decaimiento, 23.47%, no mencionado). La síntesis (l.160) dice "la varianza cae a 12–19%" — el máximo real (23.47%, LPB decaimiento) supera claramente el "19%" dado como techo.
  - Además, l.15 presenta "11.65% en ARG...y 15.41% en ARG" como si fueran "los mínimos" de la figura p90, pero hay tres valores más bajos que 15.41% que no son de ARG (LPB Ic=13.52%, SBR Int=14.06%, ARG Ic=14.29%) — 15.41% no es un mínimo destacado, es más bien un valor intermedio-bajo.
- Propuesta: corregir los rangos de l.13 a "14.8%–26.6%" y de la síntesis (l.160) a "11.65%–23.5%" (o redondeos equivalentes), y en l.15 usar el valor real más bajo (ARG intensificación, 11.65%) sin emparejarlo con 15.41% como si ambos fueran "mínimos".

**B4 (l.16) "fragmentación de mesoescala" + cita a Hannachi 2007. Necesario, revisar alcance de la cita.**
- Texto actual: "...desarrollan múltiples configuraciones de acoplamiento que compiten en importancia, la aceleración de la CCB frente a las bandas convectivas del sector cálido, la intrusión seca frente al WCB, y ningún patrón único captura más de una fracción minoritaria de la covarianza total, reflejando la mayor complejidad dinámica de los sistemas p90, tal como señalan \citet{hannachi2007empirical} al establecer que un espectro de autovalores aplanado es el indicador estadístico de un sistema complejo y multidimensional."
- Problema: Hannachi 2007 solo respalda la lectura estadística genérica (espectro aplanado = sistema complejo/multidimensional), ya usada igual en Caps. 4 y 5. La lista de mecanismos físicos específicos ("la aceleración de la CCB frente a las bandas convectivas...la intrusión seca frente al WCB") es una elaboración propia sin cita que la respalde, y es una cadena de 2-3 mecanismos no medidos en este capítulo (ni viento vectorial de componentes, ni flujos, ni seguimiento de corrientes). Mismo patrón que la "Regla de oro" de la skill pide evitar — no encadenar explicaciones no verificadas.
- Propuesta: separar la cita de Hannachi (que sí es válida para el hallazgo estadístico) de la enumeración de mecanismos específicos, dejando esta última en modo claramente especulativo o eliminándola.

---

## C. MEOF1 — Fase de Intensificación (Figuras `meof1_intensification_global.png` y `meof1_intensification_p90.png`)

**C1 (l.51) Cifras y ubicación del núcleo PG. Viable, confirmar con extracción de color (no se hizo a nivel de píxel por tiempo).**
- Revisado visualmente a nivel general: la descripción del núcleo de precipitación al sur/sureste y el gradiente de viento norte-sur en la Población Global es cualitativamente consistente con el patrón típico de esta figura, pero las cifras exactas ("$+0.018$ en SBR y LPB") no se verificaron por extracción de píxel. Recomendación: aplicar el mismo nivel de verificación numérica que se hizo en el Cap. 5 si el usuario lo considera necesario, dado el volumen de cifras específicas en este capítulo.

**C2 (l.71-75) "explicación física plausible" — WCB/CCB para la asimetría en intensificación p90. Necesario, revisar cita.**
- Texto actual cita \citet{browning1986conceptual} para "la CCB emergente da forma a la nubosidad de la cabeza de la coma". Browning 1986 es el modelo conceptual clásico (ya usado en Caps. 4 y 5, válido como modelo conceptual general), pero el resto del párrafo ("la deformación cinemática del vórtice separe físicamente las corrientes...durante la intensificación misma, antes de que el sistema alcance su máximo") es interpretación propia sin cita adicional que la respalde — atribuye un mecanismo dinámico específico (separación cinemática prematura) sin verificarlo con los datos del capítulo (no hay vorticidad calculada en este análisis MEOF). Revisar si debe quedar en modo condicional más explícito ("podría explicarse por...").

---

## D. MEOF1 — Fase de Madurez (Figuras `meof1_mature_global.png` y `meof1_mature_p90.png`)

**D1 (l.82-87) Cifras y descripción PG madurez. Viable, confirmado cualitativamente.**
- "22.31% (ARG) y 26.59% (LPB)" — no verificado contra CSV, pero consistente con el orden visual del heatmap (panel a, fila "Mat" más cálida en LPB que en ARG).

**D2 (l.99-106) MEOF1 madurez p90 — núcleo descripción. Necesario, matizar ubicación del viento.**
- Confirmado visualmente (Figura `meof1_mature_p90.png`): el campo de precipitación (paneles a, d, g) sí muestra una estructura de arco compacta en el cuadrante sur-sureste en las tres regiones, con ARG desplazado más puramente al este que SBR/LPB (que tienen más componente sur). Esto es consistente con el texto.
- El campo de viento (paneles b, e, h) muestra un núcleo positivo (cálido) **pequeño y muy cercano al centro del vórtice**, no claramente desplazado "al oeste" como afirma el texto ("un núcleo compacto al oeste del centro, aproximadamente a su misma latitud"). Visualmente el núcleo parece estar prácticamente centrado en (0,0), quizás con un sesgo apenas perceptible hacia el oeste. El propio capítulo reconoce esto más adelante (l.118): el núcleo del MEOF está "prácticamente a la misma latitud del vórtice ($\Delta y \approx 0°$)", a diferencia del EOF1 univariado de viento que sí está claramente en el cuadrante noroeste (Sección~\ref{subsec:eof1_wind10_p90}, $\Delta y \approx +2°$ a $+3°$). Hay una tensión entre llamarlo "al oeste del centro" en l.105 y luego decir "a la misma latitud" en l.118 — conviene unificar la descripción (sugerencia: "cerca del centro, con un ligero sesgo hacia el oeste" en vez de "al oeste del centro").
- Esto es relevante porque el Cap. 4 y el Cap. 5 (tras la revisión de esta sesión) usan consistentemente "cuadrante noroeste" para el núcleo de viento p90 univariado — el MEOF describe algo geométricamente distinto (más cerca del centro), y el capítulo debe ser explícito en que no es lo mismo, para no generar la impresión de que contradice al Cap. 4.

**D3 (l.102-103) "banda enroscada (wrap-around precipitation)" sin matiz. Necesario — aplicar la misma corrección que en el Cap. 5.**
- Texto actual: "...trazando la geometría de la banda enroscada (\textit{wrap-around precipitation}) en torno al núcleo del vórtice ocluido."
- En el Cap. 5 (revisión de esta sesión, Sección D6 y memoria `feedback_banda_enroscada_vs_arco`) se estableció que la ubicación real de la precipitación en p90-madurez (este/sureste) coincide **más con el WCB que con el cuadrante ocluido clásico** (que según Martin 1999 debería estar al sur/oeste en el HS), y por eso en el resto del Cap. 5 se reservó "banda enroscada (wrap-around precipitation)" solo para cuando se habla del mecanismo de Martin/Shapiro-Keyser, usando "estructura en arco" para la forma observada sin atribuir mecanismo.
- El Cap. 6 no tiene ese matiz: usa "banda enroscada" y "cuadrante ocluido" como si fueran la descripción correcta y confirmada del patrón observado, lo cual **contradice directamente la conclusión del Cap. 5** (D6: "coinciden con la posición de la precipitación asociada al WCB más que con la del cuadrante ocluido").
- Propuesta: revisar todo el capítulo con el mismo criterio — usar "estructura en arco" para la forma del MEOF1, y reservar "banda enroscada"/cuadrante ocluido solo si se puede sostener que el patrón del Cap. 6 sí coincide con esa ubicación específica (lo cual, por la posición este-sureste ya descrita, parece no ser el caso, igual que en el Cap. 5).

**D4 (l.103) "núcleo del vórtice ocluido" — afirmar oclusión sin verificarla. Necesario.**
- Igual que se decidió en el Cap. 4 y el Cap. 5 (rechazo de Hart 2003 por no calcularse el espacio de fases), esta tesis no mide directamente si un sistema está "ocluido" — es una inferencia de la fase del ciclo de vida (madurez/decaimiento), no una variable calculada. Afirmar "el núcleo del vórtice ocluido" como hecho es ir más allá de lo medido.
- Propuesta: usar condicional ("compatible con un sistema en proceso de oclusión") o remitir a la fase del ciclo de vida en vez de afirmar la oclusión directamente.

**D5 (l.106) Curtosis de PC1 univariada de precipitación como paralelo. Necesario, verificar cifra.**
- Texto actual: "...el mismo efecto de muestra reducida que ya se reflejaba en la curtosis extrema de las PC univariadas de p90 en los capítulos anteriores (ej. $\gamma_2=+30.88$ en ARG incipiente para precipitación, Sección~\ref{subsec:pc1_p90_tp})."
- Verificado: $\gamma_2=+30.88$ para ARG incipiente en p90 es correcto y coincide con el Cap. 5 ya revisado (Sección H7: "ARG presenta la curtosis más elevada del conjunto en incipiencia ($\gamma_2 = +30.88$)"). Confirmado, sin cambios.

**D6 (l.116-118) Conexión con PDFe y EOF1 univariado de precipitación y viento. Viable, revisar un matiz.**
- La conexión general (el arco del MEOF1 coincide con la banda periférica del PDFe p90 de precipitación, Sección~\ref{subsec:kde_tp_p90}) es razonable y verificable. Pero por la misma razón de D3, llamarla directamente correspondencia con "la banda periférica enroscada" hereda el mismo problema terminológico.
- La comparación con el EOF1 univariado de viento (l.118, "el núcleo de alta densidad del análisis univariado se ubica en el cuadrante noroeste... mientras que en el MEOF1 el núcleo se ubica prácticamente a la misma latitud del vórtice") es un buen ejemplo de "conexión lógica explícita" bien hecha (punto 6 de la skill) — se nombra la diferencia en vez de ocultarla. Mantener esta parte, solo ajustar D2 para que sea consistente con esto desde el principio del párrafo.

**D7 (l.120) Interpretación física vía Shapiro-Keyser. Necesario, depende de A1.**
- Una vez resuelto A1 (quitar `schultz2021antecedents`), revisar si el resto del párrafo ("aire frío y subsidente que desciende al oeste de su centro, suprimiendo la convección en el núcleo...") se sostiene solo con \citet{shapiro1999bridge}, que sí fue verificado como aplicable (aunque es un único caso del Hemisferio Norte, ya usado con ese matiz en el Cap. 5). Debe quedar en modo condicional, igual que en el Cap. 5.

---

## E. Coherencia Temporal entre Viento y Precipitación (Tabla `tab_meof_coherencia.tex`)

**E1 (l.129) Cifras de la Población Global. Necesario (parcial) — ver A4 para la atribución orográfica.**
- Verificado celda por celda contra la tabla: "$+0.18$ y $+0.47$" para las fases iniciales ✓ correcto (mínimo ARG Ic=0.18, máximo ARG It=0.47, las seis celdas PG Ic/It están en negrita/significativas). "SBR... r=-0.19" (madurez y decaimiento, ambas coinciden exactamente) ✓. "LPB... r=-0.08" (madurez y decaimiento, ambas coinciden) ✓. ARG "r=+0.47...r=+0.44...r=+0.23" (intensificación, madurez, decaimiento) ✓ todas correctas y en negrita.
- Las cifras son correctas; el problema es solo la atribución causal al final de la oración (ver A4).

**E2 (l.131) Cifras p90 madurez. Necesario, verificar "evidencia estadística definitiva".**
- "$r = -0.45$ en SBR, $r = -0.37$ en LPB y $r = -0.31$ en ARG" ✓ coincide exactamente con la tabla (las tres en negrita/significativas en madurez p90).
- "constituye la evidencia estadística definitiva del desacoplamiento dinámico" — "definitiva" es un término fuerte (ver punto 9 de la skill, palabras que afirman más de lo que el resultado sostiene). Es una correlación negativa moderada (-0.31 a -0.45), significativa pero no "definitiva". Propuesta: "es evidencia estadística de..." o "respalda la existencia de...".
- "la intrusión seca desacopla la fuente de humedad de la circulación de bajo nivel" (dentro del mismo párrafo) — mecanismo no verificado en este capítulo, debe ir condicional (igual que en el Cap. 5).

**E3 (l.131) Decaimiento — cifras. Necesario, verificar.**
- "SBR y LPB regresan a una condición no significativa (r=0.07 y r=0.12...)" ✓ coincide con la tabla (SBR D p90 r=0.07 p=0.571 no sig.; LPB D p90 r=0.12 p=0.314 no sig.).
- "ARG... se recupera con fuerza y cambia de signo (r=+0.35, significativo)" ✓ coincide (ARG D p90 r=0.35, p<0.001, en negrita). Cifras correctas.
- "sugiriendo que su oclusión más gradual permite..." — de nuevo la atribución a "oclusión más gradual" de ARG sin sustento (ver A4). Aquí sí se podría conectar, en cambio, con el hallazgo propio ya verificado en el Cap. 5 (Sección H del Cap. 5): ARG es la única región donde la correlación PC1-vorticidad univariada de precipitación se mantiene significativa durante todo el ciclo, consistente con la mayor dominancia de su EOF1. Eso sería una conexión con datos propios en vez de una atribución mecanicista nueva.

---

## F. Discusión (Sección `sec:discusion_meof`)

**F1 (l.138) Cita a Bjerknes 1922 para "modelo noruego de frentes". Viable, cita clásica genérica, sin problema de fidelidad evidente — no se verificó en detalle por ser una referencia histórica estándar del campo, bajo riesgo.**

**F2 (l.143) Corner 2025 — "no escalan linealmente con los parámetros de profundización". Necesario, impreciso.**
- Verificado en el `.md` fuente: Corner et al. 2025 encuentran que las medidas de intensidad **dinámicas** (vorticidad, viento a 850hPa) correlacionan fuertemente entre sí, mientras que las medidas de **impacto** (precipitación, huella de viento, índice de severidad SSI) correlacionan más débilmente y de forma más no lineal con las dinámicas. El "deepening rate" (tasa de profundización) se menciona solo como una de las características del ciclo de vida que distingue a los clusters resultantes, **no** como la variable específica involucrada en la relación no lineal que el paper caracteriza.
- Afirmar que "las métricas dinámicas...no escalan linealmente con los parámetros de profundización" atribuye al paper un hallazgo específico sobre profundización que no es el que reportan (su hallazgo es sobre dinámicas vs. impacto, categorías más amplias).
- Propuesta: reformular como "...no escalan linealmente con las métricas de impacto (precipitación, huella de viento, severidad), sino que exhiben una multidimensionalidad que requiere varias medidas independientes para ser caracterizada", quitando la referencia específica a "profundización". Verificar también "Atlántico Norte" — el estudio es de ciclones del Atlántico Norte **y Europa** ("North Atlantic and European ETCs"); si se usa solo "Atlántico Norte" se omite la mitad de la muestra del estudio.

**F3 (l.147-148) Martin 1999, Oertel 2021, Martinez 2014, Eisenstein 2023. Necesario, revisar en conjunto con D3/D4.**
- Martin 1999 ✓ ya verificado en el Cap. 5 como fuente correcta para el mecanismo de wrap-around/cuadrante ocluido — pero como se señaló en D3, usarlo aquí para validar que el patrón del Cap. 6 ES ese mecanismo contradice la conclusión del Cap. 5 de que la ubicación observada coincide más con el WCB.
- Oertel 2021 (convección embebida en el WCB) — en el Cap. 5 esta cita quedó limitada a un matiz específico (un caso del Atlántico Norte, l.25 del Cap. 5). Aquí se usa sin ese matiz ("la convección embebida en el WCB \citep{oertel2021warm} sostiene además la intensidad pluviométrica localizada en ese sector"), como si fuera un hecho general. Revisar si se mantiene el mismo matiz de caso único.
- Martinez 2014 (CCB y sting jet, estudio observacional de UN ciclón, campaña DIAMET) y Eisenstein 2023 (climatología europea) — razonable como respaldo general para la CCB como "motor de la circulación de bajo nivel", consistente con su uso en el Cap. 4. Sin cambios mayores, aunque recordar que Martinez 2014 es un caso único, no una climatología (ya se trató así en el Cap. 4; verificar que aquí se mantenga el mismo matiz si se repite el dato).

**F4 (l.150) Schemm 2014 — vínculo CCB-WCB vía vorticidad potencial. Viable, ya usado en el Cap. 4 con esta misma función, consistente.**

**F5 (l.152) Portal et al. 2024 (Mediterráneo, extremos compuestos). Necesario, verificar matiz.**
- Verificado en el abstract: "a high incidence of both types of compound extremes below warm conveyor belt ascent regions and of wave–wind extremes below regions of dry intrusion outflow" — es decir, la región del WCB tiene alta incidencia de **ambos** tipos de compuestos (lluvia-viento Y oleaje-viento), mientras que la región de salida de la intrusión seca tiene alta incidencia específicamente de oleaje-viento.
- El texto del Cap. 6 dice: "los eventos compuestos de lluvia y viento se maximizan bajo el ascenso del WCB, mientras que los de viento (y oleaje) se maximizan bajo la salida de la intrusión seca" — esto simplifica el hallazgo a una dicotomía más limpia de la que el abstract describe (que dice "ambos tipos" bajo el WCB, no exclusivamente lluvia-viento). Revisar el cuerpo del paper (no solo el abstract) antes de confirmar si esta simplificación es fiel o necesita matizarse.

**F6 (l.154) Ver A2 y A3 — gozzo2013air y coutodesouza2024thesis.**

---

## G. Síntesis (`sec:sintesis_meof`, l.156-163)

**G1. Forma: no sigue la estructura `\paragraph{}` usada en los Caps. 4 y 5. Necesario resolver con el usuario antes de redactar.**
- Los Caps. 4 y 5 (tras la revisión de esta sesión) usan `\paragraph{Magnitud.}`, `\paragraph{Ubicación.}`, `\paragraph{Patrones de variabilidad.}`, `\paragraph{Relación con la intensidad.}`, `\paragraph{Alcance.}`. El Cap. 6 es prosa corrida sin subtítulos y sin párrafo de Alcance.
- La naturaleza del MEOF no mapea perfectamente a esas categorías (no hay "Magnitud" ni "Ubicación" univariadas, es todo covarianza/geometría conjunta). Antes de reescribir, decidir con el usuario qué categorías usar — por ejemplo: "Dimensionalidad del acoplamiento" (la sección B), "Geometría del acoplamiento" (la sección D), "Coherencia temporal" (la sección E), y "Alcance" (nuevo, con las mismas salvedades metodológicas de los Caps. 4/5 que aplican aquí: vorticidad puntual por fase, ERA5, dependencia de literatura del Hemisferio Norte para interpretar mecanismos, y el hecho de que no se corrió un Bootstrap-t multivariado independiente para el MEOF, señalado en l.98 pero no repetido en la síntesis).

**G2 (l.159-163) Contenido: no repite ninguna cita ni introduce mecanismos nuevos que no estén ya en el cuerpo — cumple ese criterio de la skill. Viable, solo pendiente de la reestructuración de forma (G1).**

**G3 (l.161) "separados por la intrusión seca" en la síntesis. Necesario, condicional — mismo criterio que en el resto del capítulo (D7, E2).**

---

## H. Información relevante no incluida / hallazgos propios no destacados

**H1. El mismo orden regional (SBR > LPB > ARG) en magnitud de desacople ya se repite tres veces con métodos distintos (l.99, ya señalado en el propio texto: "es la tercera vez que se repite con un método distinto"). Esto ya está bien hecho por el capítulo — ejemplo positivo de punto 6 de la skill, no requiere cambio.**

**H2. Posible conexión no explotada: la correlación PC1$^{precip}$-PC1$^{viento}$ positiva y significativa de ARG en p90-decaimiento ($r=+0.35$) podría conectarse con el hallazgo ya verificado en el Cap. 5 de que ARG es la única región donde la correlación PC1-vorticidad univariada de precipitación permanece significativa en todo el ciclo (Sección H del Cap. 5, tras nuestra revisión) — ambos hallazgos, usando datos propios de capítulos distintos, apuntan a que ARG se comporta de forma cualitativamente distinta a SBR/LPB en términos de qué tan "ordenado" permanece su acoplamiento interno. Esto sustituiría la atribución orográfica no sustentada (A4) por una conexión entre resultados propios, más defendible. Propuesta para el usuario, no corrección.**

---

## Citas: resumen de decisiones (propuesta, pendiente de aprobación)

Se mantienen (verificadas): browning1986conceptual, shapiro1999bridge (condicional, caso único HN), martin1999forcing (reformulando su alcance, ver D3), oertel2021warm (con matiz de caso único, ver F3), martinez2014cold (caso único, ya tratado así en Cap. 4), eisenstein2023identification, schemm2014linkage, hannachi2007empirical (solo para el hallazgo estadístico genérico), corner2025classification (reformulando la cifra de "profundización", ver F2), portal2024linking (verificar matiz, ver F5), bjerknes1922life (riesgo bajo, cita histórica estándar).

Se quitan (ya rechazadas en Caps. 4/5 por el mismo motivo, reaparecen aquí sin justificación nueva): schultz2021antecedents (A1), gozzo2013air (A2), coutodesouza2024thesis (A3).

Tras quitar, no borrar del `.bib` (ya usadas/evaluadas en otros capítulos).

---

## Preguntas pendientes para el usuario antes de proponer texto

1. **G1**: ¿qué categorías de `\paragraph{}` usamos para la síntesis del Cap. 6, dado que el MEOF no tiene "Magnitud" ni "Ubicación" univariadas?
2. **A4/H2**: ¿prefieres quitar sin más la atribución orográfica/oclusión-gradual de ARG, o construir la conexión alternativa con el Cap. 5 (H2) que si está sustentada?
3. **D2**: ¿confirmas la lectura visual de que el núcleo de viento en el MEOF1-p90-madurez está muy cerca del centro (no claramente "al oeste"), o prefieres que verifique con extracción de color por píxel antes de redactar la corrección?
4. ¿Quieres que antes de seguir verifique numéricamente la Figura `all_expvar_meof.png` y las figuras de intensificación (C1) con extracción de píxel, al mismo nivel de detalle que se hizo en el Cap. 5? No se hizo en esta primera pasada por volumen/tiempo, y varias cifras (B1 aparte) no se cruzaron contra un CSV fuente porque no se encontró uno para MEOF en `defensa/csv_data` — confirmar si existe en otra ruta.

---

## ESTADO (2026-10-01)

**Sección A completa**: A1 (schultz2021antecedents quitado), A2+A3+A4 (gozzo2013air, coutodesouza2024thesis y atribución orográfica de ARG quitados sin reemplazo, decisión del usuario).

**Sección B completa**: B1+B5 (rango PG corregido a 14.8-26.6%, viento a 30.9-57.4%, verificado directo contra `defensa/csv_data/tp_wind10_meof_global.csv`; quitada la interpretación "modo que promedia ambos campos", no sustentada, ver memoria `feedback_meof_no_asumir_balance`). B3+B5 (rango p90 corregido a 11.65-23.47%, "significativamente"→"a valores más bajos"). B4 (Hannachi separado de la cadena de mecanismos no verificados, "fragmentación de mesoescala" eliminado).

**Sección C completa**: C2 ("deformación cinemática"→condicional; "anticovarianza"→"covarianza negativa" SOLO en esta oración, decisión del usuario de no renombrar las otras 3 apariciones por ahora). C1 verificado por fork con extracción de color: LPB-PG "alcanza el límite superior"→"próximos al límite superior" (no lo alcanza); ARG-p90 "+0.018"→">0.0208" (el texto subestimaba, el valor real supera la escala).

**Sección D**: D1 sin cambios (confirmado). D2 verificado dos veces (cálculo propio sobre el `.nc` dio resultados mixtos por artefactos de borde del dominio; un fork con extracción de color confirmó que "al oeste del centro, a la misma latitud" es preciso en las tres regiones) → sin cambios, el texto ya era correcto. D3+D4+D7 (quitado "banda enroscada/wrap-around/vórtice ocluido" por la misma razón que en el Cap. 5, usado "estructura en arco"; quitada "coherente con oclusiones graduales" de ARG; quitado el superlativo "los valores más altos de toda la serie de figuras MEOF", desmentido por el propio hallazgo de C1 en ARG-intensificación). D5 y las otras 3 apariciones de "Las series de PC1" con afirmaciones sobre pulsos/picos (l.51 PG-Int, l.62 p90-Int, l.86 PG-Mat, l.104 p90-Mat) fueron verificadas contra `defensa/csv_data/meof_pc/PC1_*.csv` en las 4 fases: 3 de las 4 afirmaciones eran **falsas** (p90 no tiene más pulsos extremos que PG, es frecuentemente al revés). Las 4 oraciones se eliminaron del cuerpo del capítulo.

**Hallazgo nuevo mayor (pedido por el usuario, no estaba en la propuesta original)**: se verificó el sesgo de Bretherton et al. 1992 (ya citado en el Cap. 2 pero nunca comprobado en el Cap. 6) correlacionando espacialmente (valor absoluto, `|r|`) la carga de cada campo dentro del MEOF1 contra su propio EOF1 univariado (Caps. 4 y 5), usando los `.nc` reales de `defensa/mpca/mpca_data_{global,p90}/tp_wind10/` y `defensa/pca/pca_data_mean2times_{global,p90}/`. Resultado: el viento ancla el MEOF1 casi perfectamente en las 24 combinaciones (región×fase×población, `|r|>0.94` siempre); la precipitación es mucho más variable y en p90 crece a lo largo del ciclo de vida (débil en incipiente, fuerte en madurez/decaimiento), mientras que en PG ocurre lo inverso. Se creó: script reproducible `defensa/cods/verificar_meof_bias_bretherton.py`, CSV `defensa/csv_data/meof_bias_bretherton.csv`, tabla en el cuerpo `tabelas_es/tab_meof_bias_check.tex` (incipiente+madurez) y tabla de anexo `tabelas_es/tab_meof_bias_check_completa.tex` (las 4 fases, agregada como nueva sección en `tex_es/apendicea.tex`, capítulo "Análisis Multivariado Complementario (MEOF)", actualmente el apéndice completo sigue comentado/inactivo en `tese_es.tex`). Nuevo párrafo insertado en la Sección F (Discusión), antes del párrafo de "configuración de cuadrantes opuestos". Memoria guardada: `feedback_verificar_sesgo_bretherton_meof`.

Respuestas ya dadas por el usuario a las preguntas pendientes: (2) quitar sin reemplazo (A4); (3) sí verificar con extracción de color, confirmado sin cambios (D2); (4) sí verificar C1 con extracción de color (aplicado). Pendiente aún: (1) **G1**, qué categorías de `\paragraph{}` usar para la síntesis del Cap. 6.

**Sección E completa**: título de sección "Coherencia Temporal..."→"Coherencia entre los Modos..." (las PC1 no son series temporales, mismo criterio que en el Cap. 5 A3). Párrafo reescrito varias veces a pedido del usuario: quitado "incoherencia" (contradictorio con "significativa", una correlación negativa y significativa NO es ausencia de relación), quitado "definitiva" y "desacoplamiento dinámico" (etiqueta sin definir), quitado "se ha reconfigurado" (implica secuencia temporal no medida en una correlación transversal), quitada la intrusión seca (ya no aportaba nada verificado) y la atribución de "oclusión más gradual" de ARG (mismo patrón que A4). El usuario señaló correctamente que, al ser dos PC1 de descomposiciones EOF univariadas independientes (Caps. 4 y 5), cada una con signo arbitrario, la interpretación con signo solo es válida si se verifica dónde está el núcleo positivo de cada EOF1 para esa fase/región específica — se verificó para madurez (las tres regiones, núcleo viento al oeste y precipitación al sureste, ya confirmado en D2) y se usa $|r|$ sin interpretación espacial para decaimiento (no verificado ahí). Nueva nota en memoria `feedback_interpretar_correlacion_pc1` con este caso.

**Sección F completa**: F3 (Martin 1999/trowal: ya no se afirma que el patrón del MEOF1 "corresponde a" el cuadrante ocluido, se dice que está más cerca del WCB, consistente con D3/Cap.5; Oertel 2021 con el matiz de caso único del Atlántico Norte). Limpieza transversal de "banda enroscada"/"estructura ocluida"/"vórtice ocluido" en las 3 apariciones restantes del capítulo (l.108 caption, l.153, l.163), todas reemplazadas por "estructura en arco"/"separación en cuadrantes opuestos", consistente con el Cap. 5. F5 (Portal 2024: se verificó el cuerpo completo del paper, no solo el abstract; la dicotomía limpia WCB→lluvia-viento / intrusión seca→viento-oleaje que afirmaba el texto es inexacta, el propio paper dice que el WCB también maximiza los extremos viento-oleaje, más del 10% de los casos; corregido a "el WCB no está asociado exclusivamente a un solo tipo de peligro compuesto"). F6 ya resuelto (redundante con A2/A3).

**Sección G (síntesis) completa**: reestructurada con `\paragraph{}`: Dimensionalidad del acoplamiento (rangos corregidos 14.8-26.6% PG y 11.65-23.47% p90, quitada "fragmentación de mesoescala", añadida la referencia al hallazgo de Bretherton), Geometría del acoplamiento, Coherencia entre los campos, y Alcance (nuevo: vorticidad puntual Sinclair 1997, sin Bootstrap-t multivariado independiente, dependencia del sesgo de Bretherton por combinación, interpretación mecanicista apoyada en literatura del HN/Mediterráneo).

**Sección H**: H1 ya era un ejemplo bien hecho (sin cambios). H2 (conexión alternativa con la dominancia del EOF1 de ARG) ya se incorporó en E3 y en el párrafo de "Coherencia entre los campos" de la síntesis.

**ESTADO FINAL**: Cap. 6 (MEOF) completamente revisado, secciones A-H. Pendiente: compilar para verificar referencias/citas, y confirmar que las nuevas tablas (`tab_meof_bias_check.tex` y la de anexo) se integran bien.
