# Revisión del Cap. 5 (precipitación). Propuestas pendientes de aprobación

Archivo: `tex_es/05.vr2_result02_tp.tex` (NO modificado). Fecha: 2026-09-30.
Método: valores verificados en las figuras (colores de la barra extraídos por píxel para PDFe; curvas de `PDF_tp_sigma025.png`; `all_expvar_tp_mean2times.png` + `defensa/csv_data/expvar_tp_*.csv`); citas leídas en `papers/files_MD/*.md`.
Criterio de citas: se mantienen los autores que UBICAN la precipitación o las corrientes respecto al centro (o comparan directamente precipitación por región o momento del ciclo de vida). Se quitan los de génesis, flujos no analizados, casos únicos de otra naturaleza o energía integrada (igual que en el Cap. 4).

Orden de presentación sugerido: A (estructurales) → B (PDF) → C (PDFe PG) → D (PDFe p90) → E (varianza) → F (EOF1) → G (significancia, requiere lectura del achurado por el usuario) → H (PC) → I (síntesis) → J (hallazgos nuevos a añadir).

---

## A. Estructurales

**A1. Referencia rota (l.125).** `Sección~\ref{subsubsec:tb_eof}` → `Sección~\ref{subsec:tb_eof}` (la etiqueta existe en `02.vr4_fundamentacao.tex:199`). Necesario.

**A2. Títulos y leyendas con "---" o " - " (l.139, 142, 161, 164, 193, 200, 212).** Unificar con el estilo del Cap. 4 (paréntesis):
- `\subsection{EOF1 --- Población Global}` → `\subsection{EOF1 en la Población Global}`
- `\subsection{EOF1 --- Subconjunto p90}` → `\subsection{EOF1 en el subconjunto p90}`
- `[EOF1 de precipitación total - Población Global]` → `[EOF1 de precipitación total (Población Global)]` (ídem p90, PDFe PG/p90 l.55 y l.84, significancia l.193/l.200 → `(Población Global, madurez)`).
- `\section{Componentes principales (PC1)}` → `\section{Componentes principales}` (la sección trata PC1–PC3).
Necesario (pedido previo).

**A3. "series temporales" (l.190 y leyenda l.195).** Igual que en el Cap. 4, las PC no son series temporales sino amplitudes por caso. Proponer "las amplitudes de las componentes principales (PC1--PC3)". Revisar cómo quedó exactamente en el Cap. 4 y copiar la misma frase.

**A4. "verificación representativa de que los patrones EOF documentados en las demás fases no son artefactos del muestreo" (l.190).** Igual que en Cap. 4. Solo se evaluó madurez, no se puede extender. Copiar la formulación que quedó en el Cap. 4.

---

## B. PDF de magnitudes (Figura `PDF_tp_sigma025.png`, fig:pdf_tp)

Valores leídos en la figura (PG = sombra gris; p90 = línea roja):
- Ic/It SBR y LPB: PG pico ≈ 19–20 mm/h, densidad ≈ 0.03–0.04. p90: SBR Ic ≈ 25, LPB It ≈ 30 (desplazado a la derecha); SBR It ≈ igual que PG.
- ARG Ic/It: PG pico ≈ 5–6 mm/h, densidad ≈ 0.10. p90 It pico ≈ 11 mm/h, densidad ≈ 0.055.
- M: SBR PG pico estrecho ≈ 17 mm/h (≈0.11–0.12), p90 ≈ 7 mm/h (≈0.08). LPB PG plano ≈ 10 mm/h (≈0.04), p90 pico ≈ 10 mm/h (≈0.08), mismo valor pero más agudo. ARG PG ≈ 5 (≈0.12), p90 ≈ 7 (≈0.08).
- D: PG ≈ 4–5 mm/h en las tres. p90 SBR ≈ 3 (0.18), LPB ≈ 3 (0.13), ARG ≈ 2 (>0.20).

**B1 (l.22).** "con pico modal entre 10 y 20~mm/h" → "con pico modal cercano a 20~mm/h". Necesario.

**B2 (l.23).** "Los ciclones intensos (p90) exhiben mayores tasas, con colas que llegan a 60~mm/h" → añadir precisión: "En p90, el pico se desplaza hacia valores mayores en SBR durante la fase incipiente (${\sim}$25~mm/h) y en LPB durante la intensificación (${\sim}$30~mm/h), con colas que llegan a 60~mm/h…". Viable.

**B3 (l.24, cita Chen 2024 y Flaounas 2018).** Chen ✓ (total = convectiva + gran escala). Flaounas ✓ pero el texto no usa lo más útil. Flaounas 2018 (Mediterráneo): la convección profunda da las mayores tasas; >40% de la lluvia del WCB cae al norte (hacia el polo) del centro, y la banda de lluvia se extiende de 2.5°W a 10°E del centro; la convección se concentra cerca del centro y hacia el este. Propuesta: mantener la frase y añadir la ubicación. Ver J1.

**B4 (l.25) Sinclair 2023 y Oertel 2021. Necesario.**
- Actual: "En entornos con mayor humedad e inestabilidad estática, SBR y LPB, el desarrollo de los ciclones más intensos está ligado a mayor actividad convectiva \citep{sinclair2023relationship}. Organizada dentro del WCB, esta convección libera calor latente y genera precipitaciones de alta intensidad \citep{oertel2021warm}. Por ello, en los p90, el WCB es responsable de los máximos de precipitación durante las primeras fases de desarrollo."
- Problema: Sinclair 2023 es un acuaplaneta idealizado, no habla de SBR ni LPB. Oertel 2021 es UN ciclón del Atlántico Norte (Sánchez, NAWDEX). "el WCB es responsable" no se prueba aquí.
- Propuesta: "En SBR y LPB, regiones con mayor disponibilidad de humedad, estas colas podrían asociarse a convección embebida en el WCB, que en un ciclón del Atlántico Norte produjo tasas locales superiores a 6~mm en 15~minutos \citep{oertel2021warm}. Por ello, en los p90, el WCB podría explicar parte de los máximos de precipitación durante las primeras fases de desarrollo."
- (Verificar en Oertel la cifra: abstract "peak values exceeding 6 mm in 15 min" ✓.)

**B5 (l.19) Sinclair 2023.** "los ciclones extratropicales son la causa principal de la precipitación en estas latitudes" ✓ se mantiene. Pero "Como fundamentan" → "Según". Viable.

**B6 (l.28) ARG It p90. Necesario.**
- Actual: "El subconjunto p90 durante la intensificación (panel f) muestra el pico desplazado a valores algo mayores ($\sim$10~mm/h), pero con las densidades más bajas de la fila, confirmando una menor eficiencia para concentrar precipitación extrema respecto a SBR y LPB."
- Figura: p90 ARG It ≈ 0.055, mayor que SBR (≈0.038) y LPB (≈0.03). Lo que es menor en ARG es la magnitud (pico en 11 frente a 20–30).
- Propuesta: "El subconjunto p90 durante la intensificación (panel f) muestra el pico desplazado a valores algo mayores (${\sim}$10~mm/h) y una densidad menor que la de la Población Global, aunque sus valores siguen muy por debajo de los de SBR y LPB."

**B7 (l.27).** ARG PG "densidades >0.10" ✓ (≈0.10). "rara vez superan los 50~mm/h" ✓. "modulación orográfica de los Andes" es interpretación sin cita; mantener pero con "podría reflejar". Viable.

**B8 (l.31) M y D en SBR y LPB. Necesario.**
- Actual: "En SBR y LPB, la Población Global mantiene el pico amplio entre 15 y 20~mm/h, mientras p90 colapsa hacia la izquierda durante la madurez y, en el decaimiento, se vuelve agudo en valores mínimos (1--4~mm/h), con densidades que alcanzan 0.17 en SBR y 0.12 en LPB."
- Figura: SBR M PG es un pico ESTRECHO en ≈17; LPB M PG es plano en ≈10; en D la PG de ambas tiene pico ≈4–5. En LPB M p90 no se desplaza a la izquierda (≈10, igual que PG), solo es más agudo. p90 D ≈0.18 SBR, ≈0.13 LPB.
- Propuesta: "En la madurez, la Población Global de SBR presenta un pico estrecho cerca de 17~mm/h, mientras que p90 se desplaza hacia ${\sim}$7~mm/h. En LPB ambas poblaciones tienen su pico cerca de 10~mm/h, pero la curva de p90 es más aguda. En el decaimiento, la Población Global de ambas regiones se desplaza hacia ${\sim}$5~mm/h y p90 se vuelve aguda en valores mínimos (1--4~mm/h), con densidades de ${\sim}$0.18 en SBR y ${\sim}$0.13 en LPB."

**B9 (l.32) ARG D.** ✓ (>0.20 en 2–5 mm/h). Sin cambio.

**B10 (l.33) Yanase 2014 y Gramcianinov 2019. Necesario.**
- Yanase 2014: parámetros ambientales de ciclogénesis a escala global (distribución bimodal trópicos-extratrópicos). Génesis → quitar.
- Gramcianinov 2019: sí es directo (ver B12). En l.33 dice "la combinación de baroclinicidad costera y disponibilidad de humedad determina la evolución de los sistemas". El paper dice que al norte de 35°S la génesis se asocia a transporte de humedad en verano y a forzante de altura en invierno, y al sur de 35°S a alta baroclinicidad con poca influencia de procesos húmedos. Es de génesis, no de evolución.
- Propuesta: fusionar l.33 con l.38 y dejar solo Gramcianinov 2019 con lo que sí dice sobre precipitación (B12). Quitar la oración de Yanase.

**B11 (l.35) Laurila 2021 y Oertel 2021. Necesario, quitar.**
- Laurila: rachas de viento en tormentas del norte de Europa, no precipitación. Oertel: no habla de predictibilidad. La oración completa es interpretación sin respaldo. Proponer eliminar el párrafo l.35.

**B12 (l.36) Russo 2025 y Gramcianinov 2024. Necesario.**
- Russo 2025: 6 casos, flujos de calor latente sostienen el desarrollo baroclínico. Flujos no analizados en la tesis → quitar.
- Gramcianinov 2024: compuestos de la fase temprana de TODOS los ciclones por región, no de p90. La frase atribuye a p90 algo que el paper no hace. Lo que dice (advección cálida y convergencia de humedad, Alta Subtropical en SBR, SALLJ en LPB) sí es por región.
- Propuesta: eliminar la parte de Russo y la de "ensanchamiento…todo el año". Reescribir: "En la fase temprana, los ciclones de SBR se asocian a advección cálida y convergencia de humedad ligadas a la Alta Subtropical, y los de LPB a su interacción con el SALLJ \citep{gramcianinov2024early}." (Sin mencionar p90.)

**B13 (l.38) Gramcianinov 2019 y Couto de Souza 2024. Necesario.**
- Gramcianinov 2019 ✓ en lo central: "SE-BR and LA PLATA cyclones generate the most intense precipitation with a similar pattern… ARG and SE-SAO… fewer cyclones with precipitation above 20 mm/day" (precipitación media en 6° del centro, máximo en el ciclo de vida, NCEP-CFSR). NO dice "dependen de la liberación de calor latente".
- Couto de Souza 2024 (G_E): términos energéticos integrados → quitar (decisión ya tomada en Cap. 4).
- "reflejo de un forzamiento de latitudes altas con baja humedad absoluta y advecciones frías y secas del Pacífico sur" → sin cita, sobredimensionado. Suavizar.
- Propuesta: "En contraste, ARG presenta precipitaciones menores en todas las fases. Esto concuerda con \citet{gramcianinov2019properties}, quienes encuentran que los ciclones de SBR y LPB producen la precipitación más intensa, con distribuciones similares entre ambas regiones, mientras que en ARG son menos los ciclones que superan los 20~mm/día. Según los mismos autores, al sur de 35°S los ciclones se desarrollan en un ambiente muy baroclínico con poca influencia de los procesos húmedos (Sección~\ref{subsec:tb_arg}), mientras que en LPB y SBR los procesos húmedos tienen mayor peso (Secciones~\ref{subsec:tb_sbr} y~\ref{subsec:tb_lpb})."

**B14 (l.40) Dacre 2023 y Heitmann 2024.**
- Dacre 2023 ✓ y es DIRECTO: Hemisferio Sur, 400 ciclones más intensos alrededor de Australia (mayo–sep, 1979–2021), máximo de precipitación en promedio 24 h antes de la máxima intensidad. Añadir la cifra y el contexto. Ver J2.
- Heitmann 2024 ✓ (≈5000 ciclones invernales del Atlántico Norte). "sugiere que este desfase…podría no ser una particularidad del Atlántico Sur, sino una propiedad más general" → sobredimensionado. Recortar.
- "relación no lineal entre vorticidad y forzantes de precipitación" → sin cita; suprimir.
- Propuesta: "El desfase entre la máxima intensidad dinámica y la máxima precipitación coincide con \citet{dacre2023climatology}, quienes, para los 400 ciclones más intensos del Hemisferio Sur en torno a Australia, encuentran que el máximo de precipitación ocurre en promedio 24~h antes de la máxima intensidad. En ${\sim}$5000 ciclones invernales del Atlántico Norte, \citet{heitmann2024lifecycle} también sitúan el pico del WCB antes del mínimo de presión."

**B15 (l.42) intrusión seca y Shapiro 1999.**
- Shapiro 1999: el ciclón con seclusión cálida (LC2, Pre-ERICA IOP-4) presenta subsidencia al oeste del centro y precipitación inclinada hacia el este por delante del frente frío. Casos del Hemisferio Norte. La ubicación "al oeste del centro" ✓.
- "agotan su acceso…", "El núcleo experimenta entonces una intrusión seca inducida por la fractura frontal" → mecanismo no verificado en la tesis; condicional.
- Propuesta: "Este comportamiento sería compatible con la llegada de una intrusión seca (\textit{dry intrusion}) al núcleo, con aire subsidente y seco que desciende al oeste del centro del sistema, como documenta \citet{shapiro1999bridge} en un ciclón con seclusión cálida del Hemisferio Norte."

**B16 (l.44) Corner 2025 y McErlich 2023.**
- Corner ✓ (r = 0.47 entre precipitación y vorticidad; lo explican por calentamiento diabático → anomalía de VP en niveles bajos, citando a Davis y Emanuel). Añadir "r = 0.47".
- "Esto es evidencia en contra de que…" → frase confusa, quitar.
- "los ciclones con vientos más intensos tienden a secarse en su núcleo" → la tesis selecciona p90 por vorticidad, no por viento; corregir a "ciclones más intensos".
- McErlich ✓ (46% y 80%).
- Propuesta (solo cambios mínimos): "…\citet{corner2025classification} encuentran una correlación moderada ($r = 0.47$) entre precipitación y vorticidad relativa, que atribuyen al calentamiento diabático…"; eliminar "Esto es evidencia en contra de que el forzamiento dinámico se traduzca en mayor lluvia extrema durante todo el ciclo de vida."; "los ciclones con vientos más intensos" → "los ciclones más intensos".

---

## C. PDFe Población Global (Figura `kde_tp_global_fasesxreg.png`, fig:kde_tp_global)

Nivel máximo y posición (lon, lat respecto al centro), por extracción de color:
| Fase | SBR | LPB | ARG |
|---|---|---|---|
| Ic | 15–17 @(+1.7,−0.5) | 9–11 @(+2.1,−0.5) | 5–7 @(+2.4,−0.8) + foco NO |
| It | 23–25 @(+1.9,−1.2) | 19–21 @(+1.7,−1.3) | 11–13 @(+2.9,−1.0) |
| M | 13–15 @(+2.9,−1.6) | 9–11 @(+2.4,−1.8) | 7–9 @(+5.7,−1.4) |
| D | 9–11 @(+4.0,−1.0), mitad E | 7–9 @(+3.9,−1.3) | 5–7 @(+5.5,−0.6) |

El texto usa el límite superior del nivel (p. ej. "~17" para 15–17). Propongo usar rangos como en el Cap. 4.

**C1 (l.63) Ic. Necesario.**
- "densidad máxima (~17) … cuadrante sureste (longitudes 0--5°, latitudes −2 a −4°)" → núcleo en ≈(+2, −0.5), al este y ligeramente al sur del centro. "LPB (~13)" → 9–11. "ARG (~9)" → 5–7.
- Propuesta: "En SBR (panel a), la densidad máxima (${\approx}$\,15--17\,$\times10^{-4}$) se ubica al este del centro, ligeramente al sur (${\sim}$2° de longitud y ${\sim}-$0.5° de latitud), con cola hacia el noroeste. LPB (panel b) presenta un núcleo en posición similar y de menor densidad (${\approx}$\,9--11\,$\times10^{-4}$), con elongación al norte. En ARG (panel c), un núcleo al este-sureste (${\approx}$\,5--7\,$\times10^{-4}$) coexiste con uno secundario en el noroeste…"

**C2 (l.63) It. Necesario.**
- "SBR (~29, máximo de la matriz)" → 23–25 (sigue siendo el máximo de la matriz ✓). "LPB (~21)" → 19–21 ✓. "ARG (~13)" → 11–13 ✓.
- Propuesta: cambiar "$\sim$29" por "${\approx}$\,23--25"; "$\sim$21" por "${\approx}$\,19--21"; "$\sim$13" por "${\approx}$\,11--13". Núcleo de SBR y LPB a ≈2° al este y ≈1.2° al sur del centro.
- "(posible influencia orográfica o advección atlántica)" → especulación sin cita; quitar. Viable.

**C3 (l.65) Gozzo 2013 y Andrade 2024. Necesario.**
- Gozzo 2013: flujos aire-mar (no analizados). Quitar según criterio.
- Andrade 2024 (271 ciclones explosivos de Sudamérica, ERA5 2010–2020): flujos de calor latente grandes en el sector frío SW–S; el vapor evaporado es importado y su condensación calienta y reduce la presión. Es flujo, no ubicación de precipitación → quitar aquí. (Andrade también dice que el viento aumenta en el sector SW con el CCB a medida que el ciclón se profundiza; útil como contraste para el Cap. 4, avisar al usuario.)
- Propuesta: reemplazar el párrafo por: "La mayor densidad de SBR y LPB frente a ARG durante la intensificación es coherente con la mayor intensidad de la precipitación en esas regiones (Sección~\ref{sec:pdf_tp}). ARG muestra las densidades más bajas en todas las fases (paneles c, f, i y l)."

**C4 (l.67) M. Necesario.**
- "SBR (~15)" → 13–15 ✓ rango. "LPB registra el mayor desplazamiento hacia el este de la fila (~11)" → falso: el núcleo más al este es ARG (+5.7). LPB 9–11. "ARG … (~9)" → 7–9.
- Propuesta: "SBR (panel g) desciende a ${\approx}$\,13--15\,$\times10^{-4}$, con el núcleo al sureste (${\sim}$3° al este y ${\sim}$1.5° al sur) y forma ovalada de eje noroeste--sureste. LPB (panel h) presenta un núcleo en posición similar (${\approx}$\,9--11\,$\times10^{-4}$) con contornos que se elongan hasta $+$6°. ARG (panel i) tiene el núcleo más alejado hacia el este de la fila (${\sim}+$5.7°) y la menor densidad (${\approx}$\,7--9\,$\times10^{-4}$), con elongación al noreste."
- "que sugiere influencia del flujo zonal" → quitar (sin respaldo). Viable.

**C5 (l.69) D. Necesario.**
- "SBR (~11) … contornos casi circulares que cubren casi todo el dominio" → nivel 9–11; la densidad se limita a la mitad este (lon −0.4 a +8.8). "LPB (~9)" → 7–9. "ARG (~7, la más baja de la figura)" → 5–7 (empata con ARG Ic).
- Propuesta: "SBR (panel j) registra su densidad más baja (${\approx}$\,9--11\,$\times10^{-4}$), con el núcleo al este del centro y los contornos restringidos a la mitad oriental del dominio. LPB (panel k) … (${\approx}$\,7--9\,$\times10^{-4}$) … ARG (panel l) … (${\approx}$\,5--7\,$\times10^{-4}$, junto con ARG incipiente la densidad más baja de la figura)…"

**C6 (l.71) Browning 1986 y Naud 2020. Necesario (reforzar con ubicación).**
- Browning ✓ (modelo conceptual). Naud 2020 ✓ y MUY DIRECTO: compuestos de ciclones oceánicos (HS invertidos N–S) con máximo de precipitación a ${\sim}$250~km hacia el polo y al este del centro, extendido hacia el ecuador y al este en forma de coma, y mínimo al oeste. En el HS "hacia el polo" = sur. Nuestros núcleos PG Ic/It están a ≈2° al este y 0.5–1.3° al sur (≈200–250 km). Coincide.
- "emerge primariamente de la arquitectura dinámica del WCB" → sobredimensionado.
- Propuesta: "La asimetría hacia el este y sureste de la Población Global (paneles a--f) coincide con la ubicación que la literatura asigna a la precipitación del WCB. En el modelo conceptual de \citet{browning1986conceptual}, el WCB asciende por delante del frente frío y sobre el frente cálido, en el flanco cálido del ciclón. En compuestos de ciclones oceánicos de ambos hemisferios, \citet{naud2020evaluation} sitúan el máximo de precipitación a ${\sim}$250~km del centro, hacia el polo y al este, y un mínimo al oeste, lo que en el Hemisferio Sur corresponde al sureste. Esta distancia es similar a la de los núcleos de SBR y LPB en las fases incipiente e intensificación (${\sim}$2° al este y 0.5--1.3° al sur). La misma posición se observa en la carga positiva del EOF1 (Fig.~\ref{fig:eof1_tp_global}), aunque este análisis no permite atribuirla directamente al WCB."

**C7 (l.72) Catto 2015. Necesario.**
- Paper: frentes con WCB tienen 2 a 10 veces más probabilidad de producir precipitación extrema; hasta 90% de los eventos extremos en frentes coinciden con WCB. "demuestran una vinculación inequívoca" → sobredimensionado.
- Propuesta: "A escala global, \citet{catto2015fronts} encuentran que los frentes acompañados de un WCB tienen entre 2 y 10 veces más probabilidad de producir precipitación extrema que los frentes sin WCB."

**C8 (l.74) Cardoso 2022 y Vera 2002.** Cardoso ✓ (análogo, aceptado antes). Vera 2002 ✓: transporte de humedad desde latitudes tropicales a lo largo de la porción oriental del ciclón en niveles bajos (Sudamérica subtropical, invierno). "resultando en núcleos más densos y extendidos" → condicional.
- Propuesta mínima: "…el transporte de humedad desde latitudes tropicales a lo largo del flanco oriental del ciclón en niveles bajos, documentado por \citet{vera2002cold} para Sudamérica subtropical en invierno, podría acentuar esta asimetría y explicar núcleos más densos (paneles a, b, d, e)."

**C9 (l.75) ARG.** "con estructuras bimodales en las fases inicial y final" → en D el foco secundario de ARG es débil; mantener solo "en la fase incipiente". Viable.

**C10 (l.77).** "caracterizarla es una necesidad metodológica que permite establecer cómo el ciclón promedio concentra la precipitación" → registro. Propuesta: "Caracterizar esta dispersión permite establecer la referencia con la que se compara el subconjunto p90." Viable.

**C11 (l.79) Mendes 2010 y Gramcianinov 2019. Necesario, eliminar el párrafo.**
- Mendes 2010: climatología de ciclogénesis (≈18 eventos por invierno en la costa de Argentina, Uruguay y sur de Brasil). Génesis → no respalda la ubicación de la precipitación. El resto es argumentación circular ("garantiza la representatividad del patrón WCB", "Esto justifica el filtrado p90").
- Gramcianinov 2019 sobre oclusión: solo menciona que la oclusión ocurre en toda la cuenca en el contexto de un problema de seguimiento. No respalda.
- Propuesta: eliminar el párrafo l.79 completo.

---

## D. PDFe p90 (Figura `kde_tp_p90_fasesxreg.png`, fig:kde_tp_p90)

| Fase | SBR | LPB | ARG |
|---|---|---|---|
| Ic | 13–15 @(+1.8,−0.4) | 11–13 @(+3.0,−0.7) | 7–9 @(+3.0,−0.9) |
| It | 17–19 @(+2.0,−1.8) | 17–19 @(+2.3,−1.9) | 9–11 @(+2.6,−1.2) |
| M | 13–15 @(+6.7,−2.1) | 7–9 @(+3.5,−3.1) | 11–13 @(+6.6,−3.0) |
| D | 5–7 @(+5.6,−3.4) | 7–9 @(+6.2,−2.1) | 5–7 @(+6.7,−1.9) |

Visualmente, en madurez los núcleos p90 son ALARGADOS en dirección oeste-suroeste a este-noreste dentro del sector sureste, no arcos que rodeen el centro.

**D1 (l.89–90) introducción. Necesario.**
- "reorganización espacial resulta tan drástica como la observada en el campo de viento, aunque en sentido morfológicamente inverso" y "bandas estrechas y arqueadas" → sobredimensionado; en la PDFe se ven bandas alargadas, no arqueadas.
- Propuesta: "Al contrastar la Población Global con p90 (Figura~\ref{fig:kde_tp_p90}), dos rasgos se repiten. Las distribuciones p90 son más compactas en las fases iniciales, y a partir de la madurez los núcleos se alejan del centro hacia el sureste y el este, en bandas alargadas."

**D2 (l.93) Ic. Necesario.**
- SBR "~15" → 13–15; "flanco sur" → al este, casi a la latitud del centro. LPB "se desplaza al cuadrante noreste, orientación única" → falso: núcleo al este-sureste (+3.0, −0.7); la envolvente se extiende al norte. "~13" → 11–13. ARG "~9" → 7–9.
- Propuesta: "En SBR (panel a), la densidad máxima (${\approx}$\,13--15\,$\times10^{-4}$) se ubica al este del centro, más compacta que en la Población Global y sin la cola noroeste. En LPB (panel b), el núcleo (${\approx}$\,11--13\,$\times10^{-4}$) se ubica al este-sureste, con la envolvente extendida hacia el norte. ARG (panel c) conserva solo el núcleo al este-sureste (${\approx}$\,7--9\,$\times10^{-4}$) y desaparece el foco secundario del noroeste."

**D3 (l.95) It. Necesario.**
- "SBR ~19 … casi centrado" → 17–19, a ≈2° al este y ≈1.8° al sur (no centrado). "inferior al pico de la PG (~29)" → 23–25. "ARG presenta la densidad más baja de la fila (~13)" → 9–11 (sí es la más baja ✓).
- "la mayor simetría sugiere que el filtrado extremo reduce la variabilidad espacial" → quitar (no se sigue).
- Propuesta: cambiar cifras y "casi centrado" por "al sureste, a ${\sim}$2° del centro"; eliminar la inferencia.

**D4 (l.97) M. Necesario.**
- "bandas estrechas y arqueadas" → "bandas alargadas". "dejando el área central y noroccidental sin máximos" ✓. SBR ~15 → 13–15 ✓; núcleo a ≈6.7° al este y 2° al sur (cerca del borde). LPB ~9 → 7–9, núcleo a (+3.5, −3.1): es el más al SUR de la fila, no la "asimetría sureste más marcada"; contornos hasta +7° ✓ (envolvente). ARG ~13 → 11–13 ✓.
- Propuesta: "Al alcanzar la madurez, los núcleos de densidad se alejan del centro y se alargan hacia el sureste y el este, dejando el área central y noroccidental sin máximos. En SBR (panel g), el núcleo (${\approx}$\,13--15\,$\times10^{-4}$) se ubica a ${\sim}$6--7° al este y ${\sim}$2° al sur del centro, cerca del borde del dominio. En LPB (panel h), la densidad es la más baja de la fila (${\approx}$\,7--9\,$\times10^{-4}$) y el núcleo se ubica a ${\sim}$3.5° al este y ${\sim}$3° al sur, con contornos que alcanzan $+$7° de longitud. ARG (panel i) presenta una banda similar a la de SBR (${\approx}$\,11--13\,$\times10^{-4}$, a ${\sim}$6.5° al este y 3° al sur)."

**D5 (l.99) Naud 2025 y Shapiro 1999. Necesario.**
- Naud 2025 ✓ (HN invierno, MERRA-2): en ciclones ocluidos, la precipitación y la nubosidad se maximizan en el TROWAL, la cresta térmica que conecta el mínimo de presión con el vértice del sector cálido, no en el frente ocluido; producen más precipitación que los no ocluidos porque son más intensos. "en la periferia" no lo dice.
- Shapiro 1999: "erradica la nubosidad profunda del núcleo y abre el dry slot" no está en el paper (ver B15).
- Propuesta: "En ciclones ocluidos del Hemisferio Norte, \citet{naud2025lifecycle} encuentran que la precipitación se maximiza a lo largo de la cresta térmica que une el centro del sistema con el vértice del sector cálido (TROWAL), y no sobre el frente ocluido. En el Hemisferio Sur, esa cresta se extendería desde el centro hacia el este y el sureste, que es donde se ubican los núcleos p90 en madurez." + eliminar la oración de Shapiro (ya citado en B15).

**D6 (l.101) Martin 1999, Sawada 2021, Schultz 2021. Necesario.**
- Martin 1999 ✓: la corriente del trowal, que se origina en la capa límite del sector cálido, produce la nubosidad y precipitación "wrap-around" del cuadrante ocluido (situado hacia el polo y al oeste del mínimo de presión en el HN). El texto dice que el bent-back front "arrastra el remanente de humedad del WCB hacia la periferia" → no es de Martin.
- Sawada 2021 ✓ con ubicación: tres ciclones de la costa sur de Japón en invierno, fase madura y ocluyéndose. Precipitación estratiforme amplia al ESTE del centro (WCB sobre CCB); nubes convectivas alrededor del centro con intrusión seca sobre el WCB, que dan tasas extremas y bandas; precipitación estratiforme profunda en la cabeza de nube detrás del centro (CCB). "Pacífico noroccidental" es aceptable pero mejor "costa sur de Japón"; "confirman" → "muestran".
- Schultz 2021: artículo histórico sobre antecedentes del modelo Shapiro–Keyser. Salió del Cap. 4 → quitar.
- Propuesta: "En el marco del modelo de Shapiro--Keyser (Sección~\ref{subsec:tb_modelos}), la banda de precipitación enroscada (\textit{wrap-around precipitation}) del cuadrante ocluido se asocia a la corriente del trowal, que se origina en el sector cálido \citep{martin1999forcing}. En tres ciclones invernales maduros de la costa sur de Japón, \citet{sawada2021heavy} observan precipitación estratiforme extensa al este del centro, asociada al WCB, y bandas convectivas cerca del centro donde la intrusión seca se superpone al WCB. En p90, la PDFe muestra durante la madurez y el decaimiento núcleos alargados al este y sureste del centro, compatibles con esta distribución."

**D7 (l.103) Oertel 2021. Necesario.**
- Oertel: un ciclón; convección embebida en el WCB delante del frente frío y cerca del frente cálido (no "u ocluido"). Esta oración repite B4.
- Propuesta: eliminar l.103 (ya cubierto en B4).

**D8 (l.105) D. Necesario.**
- "exclusivamente en el flanco sureste" → al este-sureste (SBR +5.6,−3.4; LPB +6.2,−2.1; ARG +6.7,−1.9). "densidades similares a la PG" → menores en SBR (5–7 vs 9–11), iguales en LPB (7–9) y ARG (5–7). SBR "con mayores concentraciones" → falso. ARG "~7" → 5–7.
- Propuesta: "En el decaimiento, los núcleos p90 se ubican al este-sureste, a más de 5° del centro, con densidades bajas. En SBR (panel j) el núcleo (${\approx}$\,5--7\,$\times10^{-4}$) es menos denso que en la Población Global. LPB (panel k) mantiene la elongación hacia el este-sureste, con contornos que alcanzan $+$7°. ARG (panel l) presenta ${\approx}$\,5--7\,$\times10^{-4}$, con contornos difusos sobre el semicírculo este."

**D9 (l.107).** "lo que justifica las densidades agudas y localizadas" → sin cita; "podría explicar". Viable.

---

## E. Varianza (Figura `all_expvar_tp_mean2times.png`, fig:var_exp_tp)

Todas las cifras de EOF1 ✓. Suma de EOF1–EOF3 (CSV `defensa/csv_data/expvar_tp_*.csv`): PG madurez SBR 26.8, LPB 28.2, ARG 31.6 ✓; p90 madurez 43.8 (texto 43.7), 40.8, 40.4 ✓.

**E1 (l.121).** "(PC1 a PC5)" → "(EOF1 a EOF5)". Necesario.
**E2 (l.123).** "Los tres primeros modos explican en conjunto aproximadamente 26.8\%…" → añadir "en la madurez". "confirmando" → "lo que indica". Necesario.
**E3 (l.129).** 43.7 → 43.8. Necesario (menor).
**E4 (l.125) Oertel, Hannachi, Graf. Necesario.**
- Oertel (un caso) para "naturaleza discontinua" → quitar cita; la frase puede quedar como interpretación.
- "a diferencia del geopotencial" → la tesis no analiza geopotencial; comparar con el viento (Cap. 4: EOF1 30.9–57.4% en PG).
- Hannachi: mantener, con la etiqueta corregida (A1).
- Graf 2017: génesis en el HN, continuo de condiciones de génesis → quitar.
- Propuesta: "Este reparto contrasta con el del viento, cuyo EOF1 explica entre 30.9\% y 57.4\% en la Población Global (Sección~\ref{sec:var_exp_wind10}), y es consistente con la naturaleza discontinua de la precipitación. Según \citet{hannachi2007empirical} (Sección~\ref{subsec:tb_eof}), cuando la varianza se reparte entre varios modos de valores cercanos, el campo requiere varios modos para reconstruir su variabilidad."
**E5 (l.127).** "patrón opuesto al del viento, cuyas mayores varianzas se localizaban en fases tempranas" → en el viento, p90 REDUCE el EOF1 respecto a PG (25.4–37.6 frente a 30.9–57.4); en precipitación, p90 lo AUMENTA. Hallazgo más claro. Ver J4.
**E6 (l.129) ARG.** "coherente con el carácter más gradual de sus oclusiones" → la tesis no mide oclusión; quitar o condicional. Viable.
**E7 (l.131).** "obedece a la consolidación de la banda enroscada … un solo modo concentra la mayor parte posible de la varianza total" → 36.5% no es "la mayor parte". Propuesta: "…podría reflejar que una misma estructura espacial se repite en muchos casos, de modo que un solo modo concentra más de un tercio de la varianza."
**E8 (l.133) Inatsu 2004. Necesario.**
- Inatsu: modelo de circulación general; asimetría zonal de la trayectoria de tormentas del HS invernal por TSM y orografía (Andes, meseta sudafricana). No menciona frontogénesis ni explica varianza de EOF1 de precipitación. Quitar.
- "Esto explica que ARG presente mayor varianza…" → sin respaldo. Dejar solo las cifras.
- Propuesta: "En la Población Global, ARG presenta mayor varianza explicada por el EOF1 que SBR durante la intensificación (15.6\% frente a 11.7\%), pero no en la fase incipiente, donde registra el valor más bajo de la figura (11.1\%). Los mayores incrementos de p90 respecto a la Población Global ocurren en SBR y LPB en madurez y decaimiento."
**E9 (l.135).** "un comportamiento sin equivalente en los campos de viento y una firma distintiva de los sistemas del Atlántico Sur" → quitar "firma distintiva del Atlántico Sur" (no se comparó con otras cuencas). Necesario.

---

## F. EOF1 (Figuras `pca1_tp_global_fasesxreg.png` y `pca1_tp_p90_fasesxreg.png`)

**F1 (l.149).** "confirmando la baja dominancia … y la naturaleza discontinua" → "lo que indica una menor dominancia del primer modo que en el viento a 10~m". Viable.
**F2 (l.152) SBR It/M "dipolo".** Las zonas negativas son débiles y pequeñas. "creando un dipolo positivo-negativo" / "acentúan el carácter dipolar" → "con pequeñas zonas negativas débiles". Necesario.
**F3 (l.154) LPB Ic "contornos casi circulares".** Es una banda diagonal noroeste-sureste. Corregir. Necesario.
**F4 (l.156) ARG M.** El EOF1 PG de ARG en madurez ya muestra forma de arco; mencionarlo (anticipa p90). Viable.
**F5 (l.158) Gozzo 2017 y Rocha 2016. Necesario, quitar.**
- Gozzo 2017: ciclogénesis SUBTROPICAL (RG1); fuente de humedad principal = sector norte de la Alta Subtropical del Atlántico Sur (vientos del NE), no "Atlántico tropical". Génesis.
- Rocha 2016: génesis (oct–abr); el flujo desde la Amazonía aparece en un caso de estudio.
- Propuesta: "La banda de anomalías positivas orientada noroeste-sureste que muestra el EOF1 coincide con la posición de los máximos de la PDFe (Sección~\ref{subsec:kde_tp_global}). Las anomalías son más intensas y concentradas en SBR y LPB que en ARG, lo que concuerda con la mayor intensidad de la precipitación en esas regiones (Sección~\ref{sec:pdf_tp})."
**F6 (l.170). Necesario.** "dos efectos sistemáticos en todas las regiones y fases: un incremento generalizado" → ARG It baja (−1.0). "en casi todas las regiones y fases (salvo ARG en la intensificación)". "convierte los monopolos y dipolos … en estructuras arqueadas" → "en estructuras en arco".
**F7 (l.172).** "--consistente con la simetría…--" usa rayas; reescribir con conector. "PDFe de esa misma fase" ✓ (It es la más parecida). Necesario (formato).
**F8 (l.174) LPB. Necesario.** "LPB (panel h, 16\%) registra el salto más extraordinario de la figura" → contradice l.207 (+4.2, el menor). Propuesta: "LPB (panel h, 16.0\%, $+$4.2 puntos) forma un arco que envuelve el sistema…".
**F9 (l.176, l.178).** "--una desorganización…--" rayas; ARG D p90 densidad PDF ">0.20" ✓. Reescribir sin rayas. "evidencia de que" → "lo que indica que". Necesario (formato).
**F10 (l.180) Necesario.** "una vez que la intrusión seca desplaza la humedad del núcleo hacia la periferia" → condicional. "coinciden con la banda enroscada ya identificada en la PDFe" → la PDFe p90 muestra bandas alargadas al este-sureste, el EOF1 muestra arcos SW→NE. Propuesta: "Las estructuras en arco del EOF1 abarcan la zona donde la PDFe ubica los máximos p90 (Sección~\ref{subsec:kde_tp_p90})…".
**F11 (l.182 párrafo "flujos de calor latente oceánico ya discutidos").** Esos flujos salen (C3) → eliminar párrafo. Necesario.
**F12 (l.182) Reboita 2022. Necesario, quitar.** Caso único (Raoni, transición subtropical). No trata la banda enroscada ni la seclusión en p90. Salió del Cap. 4.
**F13 (l.184) Hart 2003. Necesario, quitar.** La tesis no calcula el espacio de fases; no se puede afirmar seclusión cálida en p90. Salió del Cap. 4.
**F14 (l.186) comparación con viento. Necesario.**
- "EOF1 del viento … ráfagas más intensas se concentra en el cuadrante noroeste" → el viento es a 10~m (no ráfagas) y la concentración en el noroeste es de la PDFe del viento (Cap. 4, sec:kde_espacial_p90), no del EOF1 (el EOF1 p90 del viento en madurez tiene un núcleo negativo cerca del centro).
- Propuesta: "Al contrastar con el viento a 10~m, en madurez los máximos de viento de p90 se concentran en el cuadrante noroeste, a ${\sim}$2--4° del centro (Sección~\ref{sec:kde_espacial_p90}), mientras que los máximos de precipitación se ubican al este y sureste, a ${\sim}$3.5--7° del centro (Sección~\ref{subsec:kde_tp_p90}). Esta separación entre los sectores de máximo viento y máxima precipitación es uno de los resultados centrales de este capítulo para los ciclones más intensos."

---

## G. Significancia (Figuras `xeof_global_tp_mature.png` y `xeof_p90_tp_mature.png`)

**No propongo texto hasta que el usuario describa el achurado** (como en el Cap. 4). Preguntas para el usuario:
1. PG: ¿en qué zonas y regiones es significativo EOF1, EOF2 y EOF3?
2. p90: ídem; ¿LPB EOF1 carece realmente de área significativa?
3. Amplitudes: ¿qué PC tiene mayor rango en cada población?
Además, independientemente del achurado:
- l.207 "coherente con el forzante WCB" → condicional; "(~9, la más baja de la fila)" → "${\approx}$\,7--9"; rayas "--coherente…" → reescribir.
- l.207 "Las series de PC2 y PC3 alcanzan o superan en ciertos periodos los límites" → no son series temporales; "en ciertos casos".
- l.209–210 "predictibilidad de los impactos… permite anticipar mejor… aplicación operativa" → sobredimensionado; eliminar o reducir a una oración.

---

## H. Componentes principales (Tablas `tab_stat_global_tp`, `tab_stat_p90_tp`)

**H1 (l.214) Necesario.** Duplica y contradice el Cap. 4:
- "el campo cinemático mantiene un acoplamiento fuerte entre PC1 y la vorticidad en ambas poblaciones y todas las fases" → falso (p90 PC1 del viento débil, ${\sim}-0.26$).
- "modos secundarios activándose solo en p90" → falso (PG PC3 del viento significativo en 12/12).
- "distribuciones leptocúrticas en todos los estratos" → falso (p90 SBR M $\gamma_2=-0.67$).
- Propuesta: "En la precipitación, la correlación entre PC1 y la vorticidad se debilita durante la madurez en SBR y LPB, e incluso cambia de signo en SBR en la Población Global, mientras que en ARG se mantiene negativa durante todo el ciclo." (sin repetir resultados del viento; solo remitir: "a diferencia del viento (Sección~\ref{subsec:res_dinamica_pc1})").
**H2 (l.222).** Cifras ✓. "$\gamma_1 > +0.8$ en la mayoría de los casos" → "en todos los casos". Necesario.
**H3 (l.224).** Cifras ✓. "desacoplamiento progresivo" OK.
**H4 (l.226).** Frase de dilución de p90 en PG: razonamiento largo; resumir. "configuración periférica" → vago. Viable. "control orográfico ya señalados" → no se analiza orografía; condicional.
**H5 (l.228).** Cifras ✓ (PC2 0.65, 0.61).
**H6 (l.234).** "colapso sistemático" → solo SBR y LPB → "colapso de la correlación de PC1 en SBR y LPB durante la madurez". Necesario.
**H7 (l.236).** "heterogeneización dramática", "explosión leptocúrtica" → registro ("marcada diferencia entre fases", "curtosis muy alta"). ARG "valores positivos extremos durante todo el ciclo" → ARG p90 γ2: 30.88, 5.15, 4.53, 3.37 → "valores positivos durante todo el ciclo, muy altos en la fase incipiente". "alineados por azar" → "que coinciden con la geometría del modo". Necesario.
**H8 (l.240).** "el máximo de precipitación ocurre sistemáticamente antes" → la tesis no mide el tiempo del máximo de precipitación; lo infiere por fases. "tiende a ocurrir antes". "el núcleo ya se ha secado por la intrusión de aire seco" → condicional. Necesario.
**H9 (l.244).** "lo que explica la evolución hacia la normalidad…" → "lo que podría explicar". Viable.
**H10 (l.246).** "control orográfico andino y oclusiones más lentas" → no analizados; condicional. "menor eficiencia de ARG para concentrar precipitación extrema ya documentada en el PDF" → si se aplica B6, reformular como "menor magnitud de precipitación". Necesario.
**H11 (l.247).** "parametrizar la precipitación usando únicamente la vorticidad resulta inadecuado" → "no es suficiente para describir la precipitación durante la madurez…". Viable.

---

## I. Síntesis (l.249–269)

**I1 (l.254).** "pico modal entre 10 y 20" → "cerca de 20"; "ARG ∼5–10" ✓ (5–6). "La curva p90 colapsa…, mientras la PG retiene perfiles amplios centrados en 15--20~mm/h" → falso (ver B8). "Este colapso modal, ausente en el campo de viento, evidencia" → "indica". Necesario.
**I2 (l.256).** "firma del WCB" → "compatible con la posición del WCB"; "~29" → "23--25"; "bandas estrechas y arqueadas … producto de la intrusión seca" → "bandas alargadas al este y sureste, compatibles con…"; "SBR ~7 en el borde" → p90 D SBR 5–7 ✓ ; "LPB elongación este hasta +7°" ✓. "se reconfigura drásticamente" → "cambia". Necesario.
**I3 (l.258–260).** Cifras ✓. "sin equivalente en el campo de viento" ✓ si se añade J4. "cuasi-estacionaria" → no medido, quitar. Necesario.
**I4 (l.261).** "débil o negativa en las fases iniciales ($r \approx -0.5$)" → "negativa y moderada". Necesario.
**I5 (l.265).** "Esto respalda que … deja de depender de forma monotónica…" → aceptable; "una vez que la oclusión desacopla" → condicional. Viable.
**I6 (l.266).** "el forzante eólico se concentra en el cuadrante noroeste (cinta transportadora fría)" → "los máximos de viento se concentran en el cuadrante noroeste, en la zona donde la literatura sitúa el CCB"; "configurando una separación espacial sistemática" → quitar "sistemática". "La intrusión seca vacía de humedad al centro" → condicional. Necesario.
**I7 (l.268).** "los flujos de calor latente oceánico y el SALLJ favorecen el desacople" → no analizados. Propuesta: "En SBR y LPB el desacople entre vorticidad y precipitación es más pronunciado, mientras que en ARG la correlación se mantiene significativa durante todo el ciclo." Necesario.

---

## J. Información relevante no incluida (propuestas de adición)

**J1. Flaounas 2018 (ubicación). Verificado.** Mediterráneo (HN), 500 ciclones. Más del 40\% de la lluvia del WCB ocurre al norte (hacia el polo) del centro; 12~h después de la máxima intensidad, el WCB produce una banda de lluvia que se extiende zonalmente desde 2.5° al oeste hasta 10° al este del centro, con forma de coma; la convección profunda ocurre cerca del centro y hacia el este. Muy útil para la PDFe p90 en madurez y decaimiento (núcleos a 3.5--7° al este y al sur). Propuesta para D4 o D6: "En ciclones del Mediterráneo, \citet{flaounas2018heavy} encuentran que, después de la máxima intensidad, la lluvia del WCB se organiza en una banda que se extiende desde 2.5° al oeste hasta 10° al este del centro, con más del 40\% de los casos hacia el polo, lo que en el Hemisferio Sur corresponde al sur del centro. Esta extensión es compatible con la de los núcleos p90 en madurez y decaimiento."

**J2. Dacre 2023 (24 h, HS).** Incluido en B14.
**J3. Naud 2020 (≈250 km al polo y al este).** Incluido en C6. Es la cita más directa para la PDFe de la Población Global.
**J4. Contraste p90 vs PG entre variables (hallazgo propio, punto 8 de la skill).** En el viento, p90 reduce la varianza del EOF1 respecto a la Población Global (25.4--37.6\% frente a 30.9--57.4\%); en la precipitación la aumenta en casi todos los casos, sobre todo en madurez y decaimiento (hasta $+$22.2 puntos en LPB). Proponer una oración en E (l.127) y en la síntesis.
**J5. Sawada 2021 (ubicación).** Incluido en D6.
**J6. Para el Cap. 4 (solo aviso).** Andrade 2024 (271 ciclones explosivos de Sudamérica) indica que la velocidad del viento aumenta en el sector suroeste con el CCB a medida que el ciclón se profundiza. Verificado: en ciclones explosivos de Sudamérica, el viento aumenta en el sector suroeste (CCB) a medida que el ciclón se profundiza (Andrade 2024, sección de flujos de calor sensible). Contrasta con el núcleo noroeste del viento a 10~m en p90 del Cap. 4. Falta confirmar el nivel del viento en su Fig. 8 antes de proponerlo.

---

## Citas: resumen de decisiones

Se mantienen: sinclair2023 (solo l.19), chen2024, flaounas2018 (+ubicación), oertel2021 (solo l.25), dacre2023, heitmann2024, shapiro1999 (ubicación oeste), corner2025, mcerlich2023, browning1986, naud2020, catto2015 (reformulado), cardoso2022, vera2002, naud2025, martin1999, sawada2021, gramcianinov2019 (solo precipitación por región), gramcianinov2024 (sin p90), hannachi2007.
Se quitan: yanase2014, laurila2021 (Cap. 5), russo2025, coutodesouza2024thesis (G_E), gozzo2013air, andrade2024 (Cap. 5), mendes2010, graf2017, inatsu2004, gozzo2017, rocha2016, reboita2022, hart2003, schultz2021, oertel2021 (l.35, l.103, l.125).
Tras quitar, comprobar que ninguna quede sin uso en otros capítulos antes de borrarla del .bib (no borrar del .bib).

---

## Achurado descrito por el usuario (2026-09-30), para el punto G

Figura `xeof_global_tp_mature.png` (PG, madurez):
- SBR EOF1: achurado sobre los valores positivos; sin achurado en blanco; algo de achurado en zonas azules restringidas (cerca del límite blanco-azul).
- SBR EOF2: achurado fuera del blanco y del primer tono suave; marcado donde la señal es fuerte, positiva y negativa.
- SBR EOF3: achurado principalmente sobre la señal positiva; un poco cerca del centro (azul) y en el extremo sureste (azul).
- LPB EOF1: solo señal positiva; achurado preferentemente donde la señal está dos tonos lejos del blanco.
- LPB EOF2: achurado no simétrico respecto a la señal; no en el azul; en el rojo, área pequeña limitada a los tonos más intensos.
- LPB EOF3: áreas achuradas pequeñas que no coinciden con la señal más fuerte, en positivo y negativo.
- ARG EOF1: casi toda la región achurada; sin achurado en algunas zonas blancas; achurado en la mayor parte del rojo, incluso tonos débiles y algo de blanco en el límite.
- ARG EOF2: achurado marcado sobre la señal positiva y negativa; solo el blanco sin achurado.
- ARG EOF3: área achurada mayor que en LPB, sobre las regiones de señal más intensa; no en blanco ni tonos cercanos.

Figura `xeof_p90_tp_mature.png` (p90, madurez):
- SBR EOF1: achurado mayoritariamente donde la señal positiva es más intensa; blanco sin achurado.
- SBR EOF2: casi sin achurado; solo un área pequeña cerca del máximo positivo.
- SBR EOF3: sin achurado.
- LPB EOF1, EOF2, EOF3: sin achurado.
- ARG EOF1: como SBR, achurado solo donde la señal positiva es intensa.
- ARG EOF2: áreas achuradas sin patrón claro respecto a la señal, en rojo y azul, principalmente al noroeste y sureste.
- ARG EOF3: sin achurado.

Pendiente del usuario: amplitudes de PC1–PC3 en cada población.

---

## ESTADO (2026-09-30, pausa del usuario)

Aplicados en el .tex: A1, A2, A3 (A4 resuelto con A3), B1, B2 (reformulado: p90 dentro de PG), B3 (+sesgo ERA5 Chen, +ubicación Flaounas), B4 (eliminado), B5 (Sinclair reformulado), B6+B7, B8, B9, B10 (eliminado), B11 y B12 (eliminados), B13, B14 (Dacre + Heitmann "mientras el ciclón aún se profundiza"), B15 (Shapiro condicional), B16 (McErlich; Corner pasa a sección H), B17 (reorden PDF y cierre eliminado), C1–C8 (Cardoso eliminado del Cap. 5), C9 (eliminado), C10, C11 (eliminado), D1–D4 (D4 con Flaounas), D5 (Naud comentado, no eliminado), D6 (banda enroscada: p90 M coincide con WCB, no con cuadrante ocluido), D7 (eliminado), D8, D9 (comparación directa viento NW vs precipitación E-SE en p90 madurez).

Pendiente de respuesta del usuario: añadir o no al final de D6 la oración "Esta posición también es compatible con la de la convección profunda y la lluvia del WCB descritas por \citet{flaounas2018heavy} (Sección~\ref{sec:pdf_tp})."

Aplicados además: E1–E9 (EOF1–EOF5; "en la madurez"; 43.7→43.8; párrafo Oertel/Hannachi/Graf reemplazado por contraste con el viento 30.9–57.4%; E5 fusionado con J4 -viento reduce EOF1 en p90, precipitación lo aumenta-; quitado "carácter más gradual de sus oclusiones"; "la mayor parte posible" → "más de un tercio"; quitada cita Inatsu 2004 y su explicación; quitada "firma distintiva del Atlántico Sur"). J4 ya resuelto dentro de E5, no hace falta repetirlo en la síntesis salvo que se quiera reforzar en I3.

Aplicados además: F1–F14 (registro "confirmando"→"lo que indica"; SBR dipolo→pequeñas zonas negativas débiles, con "núcleo positivo" explícito; LPB Ic contornos circulares→banda diagonal NO-SE; ARG madurez PG: mención de forma de arco sin atribuir mecanismo, remite a p90; quitadas citas Gozzo 2017 y Rocha 2016 de génesis; "en todas las regiones y fases"→"casi todas...salvo ARG en intensificación"; "estructuras arqueadas"→"en arco"; rayas reescritas en dos párrafos (intensificación y decaimiento); "artefacto"→"no se debe a unos pocos casos aislados"; LPB "salto más extraordinario" corregido (contradecía la Sección de significancia, ahora solo cifras); eliminados párrafos completos de flujos de calor latente oceánico, Reboita 2022 y Hart 2003 (mecanismos no respaldados/ya quitados del Cap. 4); comparación final con el viento reescrita como PDFe-vs-PDFe (cuadrante noroeste ${\sim}$2--4° vs. este/sureste ${\sim}$3.5--7°, con las secciones correctas).

G (significancia) completa: párrafo EOF1-PG corregido con el achurado descrito (sin atribuir WCB a la Población Global); párrafo EOF1-p90 corregido (arco SO-NE, cifra LPB 7--9, rayas y "series"→"amplitudes" corregidos); párrafo NUEVO añadido para EOF2/EOF3 en PG y p90 (decisión del usuario: sí incorporar el achurado de modos secundarios en un párrafo aparte); párrafo de "predictibilidad/aplicación operativa" reemplazado por una explicación estadística (LPB: salto de varianza más moderado + densidad PDFe más baja → menor señal-ruido → no supera el test).

Corner 2025 (r=0.47, PDF de magnitudes) fue retirado de B16 pero NO insertado aún; pendiente para H.

Respuesta del usuario sobre amplitudes PC1–PC3: entre PG y p90 las magnitudes no son muy distintas, y tampoco entre PC1/PC2/PC3 (a diferencia del viento, donde PG tiene PC1>>PC2≈PC3 y p90 tiene PC1≈PC2>PC3). Usado para abrir H1.

H completa (H1–H11): H1 reescrito (3 afirmaciones falsas sobre el viento corregidas: PC1 viento débil en p90 ARG madurez -0.26 no "acoplamiento fuerte en ambas poblaciones"; PC3 viento ya significativo en 12/12 en PG no "solo en p90"; curtosis p90 SBR M -0.67 no "leptocúrtica en todos los estratos"; abre con el contraste de amplitudes que dio el usuario; distingue debilitamiento-hacia-cero (LPB) de cambio-de-signo (SBR) en vez de mezclarlos). H2 (γ1>+0.8 en todos los casos). H4 reescrito dos veces: primera versión encadenaba Gramcianinov2019+Dacre2023 para inventar un mecanismo que ninguno de los dos sostiene (el usuario lo marcó como "peligroso", ver memoria feedback_no_encadenar_citas); versión final conecta con resultados PROPIOS del capítulo (ARG tiene el máximo absoluto de varianza EOF1 en PG-madurez, 16.4%, Sección E/F) en vez de citas externas; quitada la frase "no llegan a secar su núcleo" (causal no verificada sobre el 90% restante, reemplazada por el argumento de que p90 es solo el 10% de la muestra, luego cortada del todo); quitado "intrusión seca" como hecho (es condicional en la Sección B, l.38). H6 (colapso sistemático → solo SBR y LPB). H7 reescrito (quitado "heterogeneización dramática" y "cuasi-normal" sin definir, cifras exactas de curtosis ARG por fase, "alineados por azar"→conectado con el salto de varianza EOF1 ARG-Ic-p90 ya documentado en F, +4.0 puntos). H8 (colon quitado, "sistemáticamente"→"tiende a", "intrusión seca"→condicional con referencia a Shapiro ya citado en B, quitado "en el núcleo" en la ubicación de la generación de precipitación, que contradice la asimetría este/sureste ya establecida). H9 reescrito ("colapso correlacional...correlato temporal"→lenguaje más simple; "explosión leptocúrtica"→"curtosis muy alta"; conectado con D4/D8 propios, núcleos p90 cerca del borde del dominio en madurez y LPB decaimiento llegando a +9° de 20°). H10 reescrito (la referencia a "control orográfico/oclusiones más lentas" apuntaba a algo que H4 ya había quitado; "eficiencia"→"magnitud"; el usuario pidió justificar "dominado por la dinámica del vórtice" y no se pudo sustentar con datos propios, esa frase se cortó). H11 (vorticidad "no es suficiente" en vez de "resulta inadecuado"; se insertó aquí la cita de Corner 2025 r=0.47 que había quedado pendiente de B16). Limpieza transversal: "marcada/marcado" aparecía 7 veces en el capítulo, variado con pronunciada/notable/acentuada/denso/alta/mucho.

Lección de este tramo (guardada en memoria feedback_no_encadenar_citas): no encadenar dos citas reales para fabricar una tercera afirmación causal que ninguna sostiene; preferir conectar hallazgos propios de otras secciones del capítulo antes que inventar una cadena de literatura.

Sección I (Síntesis) completa: I1 (PDF, cifras B1/B2/B5/B8 propagadas, "colapso modal"→"reducción de la magnitud", quitada frase de proceso continuo no medido, reemplazada por "deja de implicar mayor magnitud"). I2 (PDFe, "~29"→"23-25", "firma del WCB"→con matiz C6, "wrap-around...Shapiro-Keyser" corregido para no contradecir D6, que concluyó que p90-madurez coincide más con WCB que con el cuadrante ocluido). I3 (varianza, "intermitente" quitado por consistencia con E4/F1, "cuasi-estacionaria" condicional). I4 (reescrito dos veces a pedido del usuario: prioriza trayectoria de |r| y significancia sobre el signo, trata el cambio de signo en SBR como detalle secundario explícito "del lado opuesto del patrón"; nueva memoria feedback_interpretar_correlacion_pc1 sobre cómo interpretar/redactar este tipo de correlación en general). I5 (reescrito tres veces: oración muy simplificada a pedido del usuario; mecanismo de "oclusión desacopla núcleo de fuente de humedad" se sustituyó por cita real ya usada en el capítulo, Shapiro 1999, en vez de dejarlo como hipótesis sin autor). I6 (conectado con el Cap. 4, que ya deja "intrusión seca" como explicación no distinguible del CCB/sting jet para el núcleo NW de viento; quitado "sistemática", ubicación "este y sureste" en vez de "sureste y sur"). I7 (quitados flujos de calor latente oceánico/SALLJ/orografía no analizados, conectado con la dominancia del EOF1 de ARG ya establecida en H4).

Limpieza transversal adicional: "banda enroscada" se usaba en dos sentidos (mecanismo wrap-around de Martin/Shapiro-Keyser en D6, y como etiqueta descriptiva de la forma de arco del EOF1 en E/F/G/H/I). Se renombraron las 5 apariciones puramente descriptivas (F l.162, G l.195, H l.230×2, I3 l.244) a "estructura en arco", dejando "banda enroscada (wrap-around precipitation)" solo en D6 donde se define y se contrasta con el hallazgo propio. Nueva memoria feedback_banda_enroscada_vs_arco.

Pendiente de respuesta del usuario: si añadir igual la oración de Flaounas 2018 al final de D6 (ya está en D4, sería redundante, recomendado NO añadirla).

Siguiente: Sección J (hallazgos nuevos). J1 (Flaounas, resuelto en D4), J2 (Dacre, resuelto en B14), J3 (Naud 2020, resuelto en C6), J4 (resuelto en E5), J5 (Sawada 2021, resuelto en D6). J6 es solo un aviso para el Cap. 4 (Andrade 2024, sector SW del viento con el CCB), no aplica a este capítulo. Pendiente fuera de este capítulo: revisar Cardoso 2022 en Caps. 2, 3, 4, 7.

Con J ya resuelto a través de B-I, el Cap. 5 queda con todas las secciones (A-J) revisadas. Flaounas NO se duplicó en D6 (ya estaba en D4).

Revisión de forma/fondo de la Síntesis (pedido del usuario, comparando contra el Cap. 4): el Cap. 4 usa `\paragraph{}` con las etiquetas Magnitud, Ubicación, Patrones de variabilidad, Relación con la intensidad y Alcance, y el Cap. 5 no tenía ninguna etiqueta ni párrafo de Alcance. Se reorganizó todo el contenido de la síntesis en esas mismas 5 categorías (mismo orden), repartiendo el antiguo párrafo "En conjunto..." (comparación con el viento) en sus tres partes correspondientes: la comparación de ubicación NW-viento/SE-precipitación pasó a Ubicación, el salto de EOF1 pasó a Patrones de variabilidad, y la salvedad sobre no poder distinguir intrusión seca de CCB/sting jet (ya reconocida como tal en el Cap. 4) pasó a Alcance. Se escribió un párrafo de Alcance nuevo con 3 salvedades, todas verificadas contra el propio capítulo antes de aplicar: (1) vorticidad por fase como medida puntual, igual que en el Cap. 4 (misma metodología, Cap. 3); (2) sesgo de ERA5 (-23%, ya citado en B3); (3) la comparación banda este-sureste vs. cuadrante ocluido se apoya en estudios del Hemisferio Norte (Martin 1999, Sawada 2021) y simetría entre hemisferios. Se corrigió una sobregeneralización propia antes de aplicar: inicialmente iba a decir que TODA la atribución al WCB depende del HN, pero varias citas centrales (Dacre 2023, Vera 2002, McErlich 2023, Gramcianinov) son directamente del Hemisferio Sur sin espejo; se acotó la salvedad solo a la comparación con el cuadrante ocluido, que sí depende de Martin 1999/Sawada 2021 (HN).

ESTADO FINAL: Cap. 5 (precipitación) completamente revisado, secciones A-J + síntesis reestructurada. Pendiente opcional: compilar el .tex para verificar referencias/citas, y una lectura final de corrido.
Los números de línea de las secciones E–I cambiaron; buscar por texto.
Citas aún por revisar en otros capítulos: Cardoso 2022 (Caps. 2, 3, 4, 7).
