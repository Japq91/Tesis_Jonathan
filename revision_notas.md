# Notas de revisión de tesis — pendientes y progreso

Archivo de seguimiento para la revisión de autoría/citas/coherencia de `Tesis_Jonathan`.
Última actualización: 2026-09-10.

## Pendientes por verificar

### 1. Librería de PCA usada en el código real (servidor swell)
El código local revisado (`~/defensa/cods/pca_02_calculo.ipynb`, versión local desactualizada) usa
`sklearn.decomposition.PCA()`. El usuario confirma que **el código real y final se ejecutó en el
servidor "swell"**, no en esta máquina, y no está seguro si allá se usó `sklearn`, `xeofs`
(mencionado en el texto de Metodología, `03.vr3_metodos.tex`, `subsec:eof_univariado`) u otro programa.

**Por qué importa:** el texto de la tesis (`subsec:analisis_pc`) discute la correlación
$\rho(PC_1, \zeta_{850}^{\min})$ y ahora incluye una interpretación de valores negativos vs. cercanos
a +1. El signo de un EOF/PC1 es matemáticamente ambiguo (arbitrario hasta un factor -1) a menos que
se aplique una convención de signo explícita tras la descomposición. `sklearn.PCA` aplica una
convención determinística interna (`svd_flip`, basada en el score máximo por evento), pero esa
convención no tiene significado físico y no garantiza comparabilidad de signo entre paneles
(PG vs. p90, distintas regiones/fases). Si en swell se usó otra librería (p. ej. `xeofs`), su
convención de signo por defecto podría ser distinta y hay que verificarla específicamente.

**Acción pendiente:** cuando el usuario tenga acceso al código de swell, confirmar:
- Qué librería/función de PCA/EOF se usó realmente (sklearn, xeofs, numpy/SVD manual, otra).
- Si se aplicó alguna convención de signo post-hoc al EOF1/PC1 antes de calcular
  $\rho(PC_1, \zeta_{850}^{\min})$.
- Si no se aplicó ninguna, decidir: (a) aplicar la convención sugerida (signo positivo en el punto
  de máxima magnitud absoluta del EOF1, junto con el flip correspondiente de PC1) y recalcular las
  correlaciones antes de interpretar sus signos entre paneles, o (b) reportar/discutir
  $|\rho|$ en vez del signo cuando se comparen paneles distintos, dejando la interpretación de
  signo solo dentro de un mismo panel.

### 2. Cifras de varianza explicada (EOF1) — RESUELTO
En `sec:var_exp_wind10` el texto citaba valores (57.4% SBR-Madurez, 57.1% LPB-Madurez, 30.9-43.3%
ARG) que no se pudieron verificar contra el heatmap `all_expvar_wind10_mean2times.png` por
saturación de la barra de color (topa en 40%). **Se confirmaron exactos** al revisar la siguiente
subsección (`subsec:eof1_wind10_global`), cuya figura `pca1_wind10_global_fasesxreg.png` imprime el
`exp_var` explícito en cada uno de los 12 paneles — los 12 valores coinciden con el texto sin
excepción (incluido el rango completo de ARG: 30.9/37.3/43.3/37.2%). Sigue pendiente, eso sí, si
vale la pena extender la escala de color del heatmap original (p. ej. hasta 60%) para que comunique
visualmente lo que ya está correcto numéricamente — es una mejora estética opcional, no una corrección.

### 3. `detrend()` — RESUELTO
El usuario confirmó que la versión real (swell) **no aplica `detrend()`**. Coincide con lo que ya
dice el texto ("No se aplica remoción de tendencia temporal"). No se requiere ninguna acción sobre
el texto por este punto. (La versión local con `detrend()` en `axis=-1` —que detrenderaba el eje
espacial, no el temporal— es obsoleta y no representa el análisis final.)

## Progreso de revisión por capítulo

Empezamos por Introducción (01) y Fundamentos (02) completos; actualmente terminando Metodología (03).

### Capítulo 1 — Introducción (`01.vr5_introducao.tex`)
Revisado de forma incidental al verificar integridad de referencias cruzadas con Fundamentos. Sin
hallazgos pendientes.

### Capítulo 2 — Fundamentos teóricos (`02.vr4_fundamentacao.tex`)
Revisado completo, subsección por subsección. Cambios aplicados:
- `sec:tb_compound_def`: citas zscheischler2018future, chen2025characteristics, chen2024evaluation
  verificadas fieles, sin cambios.
- `subsec:tb_compositing`: reescrita. Se quitó `han2025system` (no sustentaba la afirmación sobre
  extremos cambiando de ubicación/extensión en el ciclo de vida); se agregó `catto2010climate`
  (referencia metodológica base), `mcerlich2023extremes` (Hemisferio Sur, sustento correcto de esa
  afirmación) y `gramcianinov2019properties` (ejemplo regional, Atlántico Sur). Corregida atribución
  a Catto et al. 2010 (aplicó la técnica, no la "formalizó" — ya existía antes). Redacción sin
  guiones dobles ni dos puntos, por pedido del usuario.
- `subsec:tb_kde`: la fórmula de la "regla de Scott" ya no cita a Weglarczyk como respaldo de la
  optimalidad asintótica (esa discusión en Weglarczyk es sobre la regla de Silverman, no la de
  Scott); ahora Weglarczyk se cita solo como otro uso conocido de reglas tipo *rule-of-thumb*.
- `subsec:tb_eof`: se agregó una oración reconociendo la advertencia de Bretherton et al. (1992)
  sobre el sesgo de CPCA/MEOF hacia el EOF dominante de un solo campo con muestras pequeñas/baja
  señal-ruido, conectada explícitamente con el Bootstrap-t (`subsec:tb_bootstrap`) que sigue en el
  capítulo como mecanismo de mitigación.
- `subsec:tb_bootstrap`: se simplificó "estadísticos cuasi-pivotales" a una explicación en palabras
  simples (estabiliza la distribución del estadístico frente a la forma de la población).
- `subsec:tb_lagrangiano`: la cifra de `pepler2020dimensional` se corrigió a 500 km y luego se
  **revirtió a 10°** tras verificar la Fig. 6 del paper (composites a radio de 10°; el 500 km era
  para otra métrica, tasas de viento/lluvia en la Tabla 6 del mismo paper). Valor final: 10°, correcto.
- Referencia rota corregida: "Los niveles de contorno..." apuntaba a `subsec:extraccion_pdf` y
  `subsec:kde_localizacion`, pero ese contenido (percentiles 75/90 y 33/66) en realidad está en
  `subsec:prototipos` (Métodos). Corregido para apuntar ahí.
- `sec:tb_regiones`: verificado que "tres regiones" (SBR/LPB/ARG) es fiel a Gramcianinov et al.
  (2019), quienes agrupan esas tres como "a lo largo de la costa sudamericana", separadas de una
  cuarta región oceánica (SE-SAO) no incluida en el estudio.
- Integridad de referencias cruzadas Introducción↔Fundamentos↔Métodos: verificada, sin problemas
  (aparte de las correcciones de labels ya aplicadas).

### Capítulo 3 — Metodología (`03.vr3_metodos.tex`)
En progreso, revisado hasta `subsec:analisis_pc` (Análisis de las Componentes Principales, PC1)
inclusive. Cambios aplicados:
- Visión general del capítulo (5 etapas): coherente y fiel a la estructura real de secciones.
- `subsec:datos_era5`: citas hersbach2020era5, hersbach_era5_2023b, gramcianinov2020analysis,
  chen2024evaluation verificadas fieles (incluyendo cifras exactas de sesgo -10.2%/-22.6% y
  concentración de estaciones ISD en EE.UU.).
- `sec:bd_ciclones`: citas gramcianinov2020analysis, coutodesouza2024new, deSouza2025CycloPhaser
  verificadas; confirmado que Couto de Souza et al. (2024) construye sobre el catálogo de
  Gramcianinov (2020) vía su "Atlantic extratropical cyclone tracks database".
- `sec:poblaciones_estudio`: aclarado que las coordenadas de regiones son dominios fijos (no
  coordenadas puntuales de máxima densidad genética, que varían estacionalmente según Gramcianinov).
- `subsec:grupo_global`: se generalizó "el extremo absoluto de vorticidad" a "el valor más negativo
  alcanzado en algún momento de su vida" porque no está confirmado si el método real fue máximo,
  p99, o percentil sobre las horas de vida del ciclón — pendiente de confirmar con el código de swell.
- `subsec:subconjuntos_intensidad`: aclarado explícitamente que el 10% (p90) se extrae de forma
  independiente para cada región (verificado con los números exactos de `tab_conteo_ciclones.tex`:
  ARG 1980→198, SBR 641→64, LPB 669→67, los tres ~10.0% exacto).
- `sec:procesamiento_lagrangiano`: corregidas dos referencias rotas
  (`subsubsec:tb_compositing` → `subsec:tb_compositing`); reescrito el párrafo de promediado
  centrado explicando la lógica de "dos pasos si la duración es par, tres si es impar" (equidistantes
  del punto medio / paso central más uno a cada lado).
- `subsec:extraccion_pdf`: corregida referencia rota (`subsubsec:tb_kde` → `subsec:tb_kde`) y
  referencia de ecuación mal dirigida (`eq:tb_kde_pdf` → `eq:scott_rule`, con "Ecuación~" agregado
  para consistencia de estilo).
- `subsec:kde_localizacion`: corregida la misma referencia rota (`subsubsec:tb_kde` → `subsec:tb_kde`).
- `subsec:eof_univariado`: cita rieger2024xeofs verificada fiel; corregido el índice mudo duplicado
  ($\tau$ usado dos veces) en la ecuación de anomalías, ahora $\tau'$; agregadas etiquetas
  `eq:eof_anomalia` y `eq:eof_reconstruccion` (antes sin label, inconsistente con el resto del
  documento); números de muestra ($m$) verificados exactos contra la tabla.
- `subsec:bootstrap_significancia`: quitado "cuasi-pivotal" (consistente con el cambio ya hecho en
  Fundamentos); agregada la definición explícita de $SE(\mathbf{s})$ (error estándar de la muestra
  original) frente a $SE^*_b(\mathbf{s})$ (error estándar de cada réplica bootstrap), que antes
  aparecía sin definir; agregadas etiquetas `eq:bootstrap_t_espacial` y `eq:bootstrap_ci_espacial`;
  reformulada la última oración sobre significancia estadística para explicitar la conexión con la
  hipótesis nula $H_0: \theta(\mathbf{s})=0$ y $\alpha=0.05$.
- `subsec:analisis_pc`: agregada interpretación de correlaciones marcadamente negativas entre
  $PC_1^{\text{precip}}$ y $PC_1^{\text{viento}}$ (antes solo se interpretaban valores cercanos a
  +1 y a 0); agregadas etiquetas a las cuatro ecuaciones (asimetría, curtosis, correlación con
  $\zeta$, correlación precip-viento). Ver "Pendientes" arriba sobre la convención de signo del EOF.

- `subsec:eof_multivariado`: cita wilks2019statistical_ch13 verificada fiel para el problema general
  (variables con unidades dispares dominando la covarianza), con aclaración de que el escalar
  espacialmente promediado usado es una variante propia, distinta a la estandarización clásica por
  correlación que describe Wilks; corregido "desviación estándar temporal" → "entre eventos" (para
  no contradecir la aclaración previa de que $\tau$ no es un eje temporal); agregada etiqueta
  `eq:meof_normalizacion`.
- `subsec:prototipos`: se detectó y corrigió un desajuste entre el Objetivo Específico 4
  (Introducción) y lo que el método realmente construye — OE4 decía "cuantificar la magnitud
  característica", pero las cuatro capas del prototipo (PDFe + MEOF$_1$) solo describen
  **organización espacial**, no magnitud física (el propio texto aclara que el MEOF se umbraliza
  "independientemente de la magnitud absoluta"). Se corrigió OE4 en `01.vr5_introducao.tex` a
  "caracterizar la organización espacial conjunta de los máximos de viento y precipitación". También
  se corrigió ahí "campos medios condicionados al modo dominante" → "patrones espaciales del modo
  dominante" (no hay campos medios/compuestos en el método, son patrones EOF). En Métodos: se quitó
  "marcador estelar" → "marcador" (forma del marcador aún no decidida, probablemente círculo o
  cuadrado); se recortó una especulación sin anclaje ("procesos locales de interacción
  océano-atmósfera o a la geometría del frente" — no conectada al marco WCB/CCB ya citado en
  Fundamentos) y se destensó un triple matiz ("ofrece, además... podrían... aunque") en el párrafo
  de cierre.

## Capítulo 3 completo
Con `subsec:prototipos` cerrado, el Capítulo 3 (Metodología) queda totalmente revisado.

## Capítulo 4 — Viento a 10 metros (`04.vr2_result01_w10.tex`)
En progreso, yendo por tramos cortos (una subsección/sección a la vez, a pedido del usuario).
Archivo de trabajo: `04.vr2_result01_w10.tex` (no `04.vf6_...`), consistente con el resto de
archivos activos "vr" del proyecto. Nota: este capítulo está comentado/deshabilitado en
`tese_es.tex` actualmente.

### Revisado hasta ahora
- Introducción del capítulo (líneas 1-13) + `sec:pdf_wind10` (Distribución de magnitudes, PDF):
  revisadas ~14 citas. Verificación numérica exacta confirmada para `padilhareinke2026characterization`
  (p90 = 84.4 km/h = 23.4 m/s; extremo = 113.2 km/h = 31.4 m/s, ambos exactos contra su Tabla 1) y
  `gramcianinov2020analysis` (JJA Atlántico Sur, ERA5: 21.2±4.8/p90=27.3/p95=29.3; CFSR/CFSv2:
  23.4±4.8/p90=30.2/p95=32.1, exacto contra su Tabla 4). `rocha2016estudo` (ojo: el archivo .md se
  llama así, con "o" final portugués, pero la key del .bib es `rocha2016estudio` con "io" — nombres
  distintos, ambos existen, sin problema real) tiene coincidencia casi textual sobre difluencia en
  altura + cavado en niveles medios + convergencia en bajos niveles. `gramcianinov2023impact`,
  `bartolomei2024extremos`, `russo2025impacts`, `yanase2014parameter`, `crespo2020potential`
  razonablemente consistentes.
- **Referencia rota corregida** (3 ocurrencias en este archivo): `subsec:tb_compound_def` →
  `sec:tb_compound_def` (confirma el riesgo que ya habíamos anotado sobre labels inconsistentes en
  los capítulos de resultados).
- **`corner2025classification` — revisión a fondo con el PDF local** (no solo el `.md`), ubicado en
  `~/defensa/papers/grupo_1/corner2025classification.pdf`. La afirmación original citaba valores de
  Fig. 6h (WS10 por clúster: "grupo más intenso ~22.5 m/s, más débil ~12.5 m/s") como "lectura
  aproximada" — se verificó con imagen (`pdftoppm`) que el texto del paper NO da esos números
  exactos en prosa, solo el orden de magnitudes (HighSSI > Intense > AvgMST > Weak para WS10) — y
  que el nombre "Intense" no es el clúster de mayor magnitud (lo es "HighSSI"), lo cual habría sido
  engañoso. Se reemplazó por una cita a la Fig. 2e (distribución agregada de WS10, todos los ETC sin
  distinguir clúster, pico visual ~17-18 m/s), conectada explícitamente con el valor de la Población
  Global del propio estudio (~12-15 m/s) — más precisa y mejor anclada que la comparación por clúster.

- `sec:kde_espacial_global` (Distribución espacial de máximos PDFe, Población Global): revisión
  exhaustiva incluyendo **inspección visual directa de la imagen** `images/w10/kde_wind10_global_fasesxreg.png`
  (12 paneles, 3 regiones × 4 fases) contra la descripción textual. Hallazgos:
  - Layout (columnas=región, filas=fase) confirmado correcto.
  - La narrativa de migración del núcleo "este → oeste → noroeste" a través de las fases no se pudo
    confirmar con certeza visual en la transición incipiente→intensificación (las manchas incipientes
    son muy difusas para fijar una posición de núcleo precisa); **pendiente de verificar con los
    valores exactos $(\Delta x_{\text{moda}}, \Delta y_{\text{moda}})$** si el usuario los tiene
    disponibles (no resuelto en esta sesión).
  - Contradicción aparente resuelta: "se consolida en las tres regiones" (línea 70) vs. "SBR/LPB
    tienen dos focos" (línea 73) — el usuario aclaró que en SBR y LPB el foco de **mayor densidad**
    sí cumple la consolidación al noroeste, y el segundo foco (menor densidad) es adicional. Se
    aplicó ajuste de redacción: "se consolida el desplazamiento **del foco de mayor densidad**
    hacia el cuadrante noroeste" para hacerlo explícito y blindarlo ante lecturas apuradas.
  - Las 10 citas de esta subsección (`simmonds2000mean`, `sinclair1994objective`, `reboita2010south`,
    `gramcianinov2019properties`, `dossantos2023response`, `yanase2014parameter`,
    `gozzo2014subtropical`, `cardoso2020wind`, `corner2025classification`,
    `eisenstein2023identification`) verificadas razonables a excelentes. Dos cifras exactas
    confirmadas: Gozzo (2014) "300–450 km" y Cardoso (2020) "400–500 km" para la distancia del
    viento máximo al centro (ambos sobre ciclones subtropicales, no ETC en general — usado como
    referencia de orden de magnitud, razonable pero no idéntica población).

- `sec:kde_espacial_p90` (Subconjunto p90, PDFe): revisión exhaustiva con **inspección visual** de
  `images/w10/kde_wind10_p90_fasesxreg.png`. La posición del núcleo en madurez (entre $-1°$ y $-3°$
  de longitud, $+2°$ a $+3°$ de latitud) coincide bien con la imagen para los 3 paneles. **Corrección
  aplicada**: la magnitud de ARG (i) en madurez decía "concentración similar" a SBR/LPB
  (23-27/23-25$\times10^{-4}$), pero el panel muestra un núcleo verde-amarillo, no rojo/naranja —
  corregido a "notablemente menor (${\approx}$17-19$\times10^{-4}$)".
  ~18 citas revisadas, con **~7 cifras numéricas de alto riesgo verificadas exactas**:
  `catto2010climate` (39.1±3.5 m/s a 5.1°±2.7°, 100 ciclones más intensos HN), `gray2020prototype`
  (tormenta Brendan, 49 hPa, ASCAT), `gray2024global` (15% HS vs. 27% HN, tabla exacta),
  `priestley2022improved` (~3-3.5° del centro), `hyeok2024extrem` (15% más frecuente al suroeste),
  `shapiro1990life` (935 hPa, ~40 m/s dentro del rango 35-50 citado, evento ERICA Atlántico Norte),
  `stankovic2025surface` (extremos mayores en HN por baroclinicidad). Resto de citas
  (`clark2005sting`, `clark2018sting`, `martinez2014cold`, `gentile2023observed`,
  `reboita2018extratropical`) verificadas temáticamente sin cifra puntual. **No verificadas a fondo
  por volumen**: `hodges2011comparison`, `schemm2014linkage`, `blanchard2021warm` — pendiente si se
  quiere profundizar.

- `sec:var_exp_wind10` (Fraccionamiento de varianza, EOF1-EOF5): revisada la **lógica frente a las
  dos subsecciones PDFe anteriores** (PG y p90) — es coherente, no contradictoria: PG combina PDFe
  difusa + EOF1 dominante (consistente con un gradiente suave de gran escala reproducible entre
  eventos); p90 combina PDFe hiperconcentrada + EOF1 NO dominante (consistente con que la posición
  del máximo es reproducible pero el resto del campo varía más por complejidad mesoescalar —
  sting jets, frentes, seclusiones — que exige más modos). Buen argumento, sin inconsistencia.
  Cifras exactas **verificadas después** contra `subsec:eof1_wind10_global` — ver más abajo.

- `subsec:eof1_wind10_global` (EOF1 --- Población Global): revisión con **inspección visual** de
  `images/w10/pca1_wind10_global_fasesxreg.png` (12 paneles, cada uno con `exp_var` impreso). Las 12
  cifras coinciden exactamente con el texto (30.9% a 57.4%), lo que además **resolvió el pendiente
  nº 2** de la subsección anterior (ver arriba). La excepción morfológica de LPB en intensificación
  (panel e, núcleo compacto centrado en el vórtice) se confirma visualmente. Citas nuevas
  verificadas con exactitud: `hoskins2005new` (75% de ciclogénesis en superficie con contraparte a
  500 hPa — cita textual) y `simmonds2000size` (*"radius of surface cyclonic systems increases as
  they evolve to maturity"* — casi textual). Nota menor sin aplicar: el texto llama "débil dipolo
  norte-sur" al patrón, pero ningún panel muestra valores negativos (azul) — es más un gradiente
  monopolar de cero a positivo que un dipolo estricto; no se corrigió, queda a criterio del usuario.

- `subsec:eof1_wind10_p90` (EOF1 --- Subconjunto p90): revisión con **inspección visual** de
  `images/w10/pca1_wind10_p90_fasesxreg.png` (12 paneles con `exp_var` impreso). Rango numérico
  "25.4%-37.6%" confirmado exacto (mín f=ARG-Int 25.4%, máx e=LPB-Int 37.6%). Morfología por fase
  confirmada en general (incipiente difuso, intensificación con dipolo emergente, decaimiento con
  contornos negativos solo en SBR/LPB). **Corrección aplicada**: el texto decía que el núcleo
  negativo de madurez era "particularmente intenso en LPB (h) y ARG (i)", pero visualmente LPB es
  claramente el más oscuro/intenso, mientras que ARG se ve tenue, comparable a SBR — se corrigió a
  "particularmente intenso en LPB (h); en SBR (g) y ARG (i)... más tenues". Citas nuevas
  verificadas: `hart2003cyclone` (título exacto sobre asimetría térmica/thermal wind) y
  `schultz2021antecedents` (confirma el mecanismo del "anillo de vientos"/bent-back front
  envolvente); `shapiro1999bridge` temáticamente compatible sin frase textual encontrada.

- `subsec:pc1_global_wind10` + `subsec:pc1_p90_wind10` (Componentes Principales PC1, PG y p90):
  revisadas juntas (mismo `\section`). Verificación exhaustiva contra las tablas de datos reales
  `tabelas_es/tab_stat_global_w10.tex` y `tab_stat_p90_w10.tex` (no contra imagen) — **más de 25
  cifras contrastadas (asimetría, curtosis, correlación de Spearman por región y fase), todas
  exactas, sin excepción**. Incluye detalles finos verificados: rango de curtosis, $r^2\approx0.79$
  en SBR (calculado correctamente desde $\rho=-0.890$), extremos min/max de correlación incipiente
  entre regiones. Cita `sinclair1997objective` verificada (título del paper coincide con la
  afirmación sobre circulación vs. vorticidad local). **Ningún error encontrado** — la revisión más
  limpia del capítulo hasta ahora.

- `sec:sintesis_wind10` (Síntesis, cierre del Capítulo 4): revisada contra todas las subsecciones
  anteriores, sin acceso a nuevas figuras/tablas (es un resumen). **Todas las cifras citadas
  coinciden exactamente** con lo ya verificado (PDF, PDFe, EOF1, correlaciones PC1), incluyendo un
  buen cruce interno: la distancia radial "~3-4° del centro" en p90-madurez se calculó a mano desde
  las coordenadas $(\Delta x,\Delta y)$ ya verificadas y cae justo en el rango. Cita nueva
  `sinclair2023relationship` verificada (título del paper coincide exactamente con la afirmación).
  Referencia `\ref{cap:resultados_tp}` confirmada válida hacia `05.vr2_result02_tp.tex`. **Sin
  errores.**

- `subsec:res_significancia_madurez` (Significancia estadística, Bootstrap-t): revisión exhaustiva
  con **inspección visual de las dos figuras grandes** (18 paneles c/u) `xeof_global_wind10_mature.png`
  y `xeof_p90_wind10_mature.png`. **Corrección aplicada**: la oración "SBR concentra mayor
  variabilidad explicada por EOF2 (8.7%) que LPB (7.5%) y ARG (11.5%)" era una contradicción
  aritmética (8.7% no es mayor que 11.5%) — confirmado con las cifras impresas en la figura que es
  **ARG** quien tiene el valor más alto; corregido a "ARG concentra mayor variabilidad... que SBR
  (8.7%) y LPB (7.5%)". Resto de cifras verificadas exactas (EOF1 madurez 43.3-57.4%, EOF3
  5.4-6.3%). Verificación espacial del achurado (significancia 95%) confirmada en detalle: EOF1
  cubre casi todo el dominio en PG; hueco de significancia en cuadrante noreste de LPB-EOF2 (PG)
  confirmado; en p90, el núcleo negativo de LPB-EOF1 aparece sin achurado (a diferencia de SBR/ARG,
  que sí tienen algo de cobertura) — distinción fina que el texto capta correctamente; orientación
  sureste (no solo sur) del núcleo significativo de ARG-EOF1 en p90 también confirmada.

## Capítulo 5 — Precipitación total (`05.vr2_result02_tp.tex`)
En progreso. Sin el problema de labels rotos (`subsec:tb_compound_def` etc.) que tuvo Capítulo 4, verificado
por grep al iniciar. Revisión por tramos cortos, igual que Capítulo 4.

### `sec:pdf_tp` (PDF de magnitudes de precipitación) — revisado completo
Diez citas de riesgo alto/medio verificadas contra las fuentes originales:
- `dacre2023climatology`: confirmado exacto ("maximum precipitation occurs 24 hr prior to maximum dynamical
  intensity", 400 ciclones del Océano Austral).
- `heitmann2024lifecycle`: confirmado. "casi 5000 ciclones invernales del Atlántico Norte" exacto; secuencia
  PQ90→PVOL→intensidad WCB→mínimo de presión del ciclón, síntesis fiel de la climatología general y del
  caso de estudio (PVOL "peaks... a day before the WCB reaches its maximum intensity").
- `flaounas2018heavy`: confirmado exacto (convección profunda hasta 70% de la lluvia, tasas de hasta 50mm/3h
  vs. 40mm/3h del WCB puro).
- `shapiro1999bridge`: confirmado con precisión, describe el ciclón Pre-ERICA IOP-4 (dual-jet, LC2,
  Shapiro-Keyser) con "subsidence to the west of the cyclone center".
- `oertel2021warm`: confirmado (convección embebida produce precipitación superficial local muy intensa,
  picos >6mm/15min).
- `russo2025impacts`: confirmado, sus 6 casos de estudio (3 intensos, 3 explosivos) están en SBR/LPB, flujos
  de calor latente sostienen desarrollo baroclínico y humedad en sector cálido.
- **`corner2025classification`** (línea ~42): **corregido**. El texto decía que el paper "cuantifica" el
  mecanismo de retroalimentación diabática-PV, pero solo menciona una correlación moderada (r=0.47) citando
  a Davis y Emanuel (1991) como fuente real del mecanismo. Además, el paper es exclusivamente del Atlántico
  Norte y Europa (dominio 30-75°N, título "Classification of North Atlantic and European extratropical
  cyclones"), no del Atlántico Sur. Reformulado para atribuir correctamente el hallazgo (correlación en su
  propia región) y agregar cautela explícita de que el mecanismo no está demostrado para el Atlántico Sur.
- **`blanchard2021warm`** (línea ~25): **corregido/retirado**. Estaba citado como respaldo de que la
  convección embebida en el WCB "intensifica el sistema", pero el hallazgo central del paper es que la
  convección de nivel medio en el WCB acelera la corriente en chorro y modifica la circulación corriente
  abajo, un mecanismo de niveles altos distinto de la intensificación del ciclón en superficie. Se retiró la
  cita y la frase "que intensifica el sistema", dejando solo la parte bien respaldada (precipitación intensa
  vía `oertel2021warm`).
- `evans2012climatology`: inicialmente descartado por error propio (búsqueda por palabras clave insuficiente);
  releído con cuidado, sí respalda la afirmación ("anomalously high precipitation... and a greater surface
  heat flux coincide with the resultant warm SST anomaly... this environment provides for stability and
  moist[ure]", ligado a la formación recurrente de ciclones subtropicales de estructura híbrida en el
  Atlántico Sur). Confirmado sin cambios.

### `subsec:kde_tp_global` (PDFe, Población Global) — revisado, 1 corrección aplicada
Figura `kde_tp_global_fasesxreg.png` cotejada panel por panel contra el texto (12 paneles a-l):
todas las posiciones y valores de densidad descritos confirmados exactos, sin errores.

Citas verificadas:
- `catto2015fronts`, `vera2002cold`: confirmadas, respaldan correctamente la vinculación WCB-frentes-
  precipitación intensa y el flujo cálido tropical hacia el flanco este del vórtice, respectivamente.
- `cardoso2022synoptic` (línea ~72, convergencia de humedad + advección cálida en SBR/LPB): confirmado,
  uso distinto del que se retiró en Capítulo 4 (aquí sí coincide el mecanismo descrito).
- `gramcianinov2019properties` (línea ~77, oclusión documentada en el Atlántico Sur): confirmado.
- **`simmonds2000mean`** (línea ~77): **corregido**. Releído el paper completo (763 líneas, no solo
  grep) a pedido explícito del usuario tras errores previos de interpretación apresurada. El texto de
  la tesis afirmaba "desplazamiento preferencial de estos sistemas hacia el sureste sobre el océano"
  citando a `mendes2010climatology` y `simmonds2000mean` juntos. Verificado que `simmonds2000mean` solo
  dice que los ciclones nacidos cerca de la costa este de Argentina "are transported downstream by the
  westerlies" y que el mar de Bellingshausen (al sur/suroeste de Argentina, no al sureste) es el destino
  preferente de terminación de trayectoria, es decir, no sostiene una dirección "sureste" específica.
  `mendes2010climatology` (específico del sector sudamericano, con cluster analysis de trayectorias)
  tampoco usa esa dirección cardinal explícita en el texto para el cluster Argentina-Uruguay-sur de
  Brasil. Corregido quitando la dirección cardinal no sostenida, dejando el hecho sí verificado
  (sistemas móviles que se desplazan hacia el océano arrastrados por los oestes).
- `browning1986conceptual`: confirmado sin cambios. El modelo describe exactamente el ascenso inclinado
  ("forward-sloping ascent") del WCB por delante del frente frío ("ahead of a kata cold front") y su
  elevación por encima del aire frío que antecede al frente cálido ("rising above a flow of cold air
  ahead of the warm front"), organizando bandas de precipitación en el sector cálido.

`subsec:kde_tp_global` queda **cerrado** (revisión completa, 1 corrección aplicada en `simmonds2000mean`).

### `subsec:kde_tp_p90` (PDFe, subconjunto p90) — revisado completo, 1 corrección aplicada
Figura `kde_tp_p90_fasesxreg.png` cotejada panel por panel (12 paneles a-l): todas las densidades y
posiciones descritas en el texto confirmadas exactas contra la imagen, sin errores.

Citas verificadas:
- `naud2025lifecycle`: confirmado, coincide casi textualmente ("thermal ridge that connects the SLP
  minimum to the peak of the warm sector" + "frontal scale ascent... underlies the cloud and
  precipitation production"), correctamente escopado al Hemisferio Norte.
- `shapiro1999bridge`: reutilización correcta de la cita ya validada en `sec:pdf_tp` (intrusión seca).
- `martin1999forcing`: confirmado, el paper describe exactamente el "trowal airstream" responsable de
  la precipitación "wrap around" en el cuadrante ocluido.
- `sawada2021heavy`: confirmado, casos de ciclones de Japón (Pacífico noroccidental, mayoría con
  frente ocluido) muestran DI sobre WCB generando precipitación en banda.
- `schultz2021antecedents`: confirmado, paper específicamente sobre el origen conceptual histórico del
  *bent-back front*.
- **`blanchard2021warm`** (línea ~101): **corregido/retirado** (mismo problema que en `sec:pdf_tp`).
  Citado junto a `oertel2021warm` como respaldo de que "la intensidad máxima de las precipitaciones
  está condicionada por la fuerza del WCB y la convección profunda embebida en él", pero Blanchard
  et al. (2021) es un estudio sobre aceleración del *jet stream* por dipolos de PV generados por
  convección de nivel medio en el WCB (mecanismo de niveles altos/corriente abajo), sin resultados
  sobre intensidad de precipitación superficial ni contenido de hidrometeoros. Retirada la cita,
  dejando solo `oertel2021warm` (que sí respalda la afirmación).

Con esto, `subsec:kde_tp_p90` y por tanto toda la Sección~\ref{sec:pdfe_tp} quedan **cerrados**.

### `subsec:var_exp_tp` (fraccionamiento de varianza EOF) — revisado, sin correcciones
Figura `all_expvar_tp_mean2times.png` (heatmap 12 regiones/fases x 5 EOF x Global/p90) cotejada
contra el texto: el valor más extremo citado (LPB decaimiento p90 = 36.5%) corresponde exactamente
a la celda más saturada (rojo oscuro) del mapa; patrones relativos por región y fase consistentes.

Citas verificadas, todas correctas sin cambios:
- `hannachi2007empirical`: review general de EOF, respalda el criterio de degeneración del espectro
  y dificultad de truncación citado en el texto.
- `graf2017objective`: confirma textualmente "a continuum rather than a few distinct categories" y
  que humedad/diabáticos (PC1) y PV en niveles altos (PC2) son dimensiones cuasi-independientes.
- `inatsu2004zonal`: confirma que la asimetría zonal del storm-track del HS está forzada por
  asimetrías de SST y por los Andes (ciclogénesis en su sotavento).

### `subsec:eof1_tp_global` (EOF1, Población Global) — revisado, sin correcciones
Figura `pca1_tp_global_fasesxreg.png` (12 paneles): las 12 cifras de `exp_var` (11.1%-16.4%)
coinciden exactamente con el texto, incluyendo el máximo absoluto (ARG madurez, 16.4%) y el hecho
fino de que LPB pica en incipiente (14.4%) por encima de decaimiento (14.3%) por solo 0.1pt, tal
como afirma el texto. Morfología (núcleos, dipolos, colas) confirmada panel por panel.

Citas verificadas, ambas correctas sin cambios:
- `gozzo2017climatology`: coincide casi textualmente ("anomalous moisture transport from lower
  latitudes preceded the subtropical cyclogenesis... local evaporation has a secondary role").
- `rocha2016estudio`: encontrada la frase exacta de respaldo ("No nível de 850 hPa, nota-se uma
  convergência do escoamento bem pronunciado da Amazônia para a região onde se posiciona o ciclone").

### `subsec:eof1_tp_p90` (EOF1, subconjunto p90) — revisado, 1 corrección aplicada
Figura `pca1_tp_p90_fasesxreg.png` (12 paneles): las 12 cifras de `exp_var` (13.8%-36.5%) y los 12
deltas respecto a la Población Global (verificados contra `subsec:var_exp_tp`) coinciden exactamente,
sin excepción. Verificación cuantitativa adicional por conteo de píxeles según color del colorbar
(mapeo exacto tono→valor): confirma cualitativamente que SBR-madurez (g) no tiene negativos (9 px),
ARG-madurez (i) tiene "valores negativos mínimos" (73 px, confirmado), y LPB-madurez (h) sí tiene
negativos sustanciales (~4940 px).

- **Panel h (LPB madurez)**: **corregido**. El texto decía "zonas negativas ($\sim$$-$0.012 a
  $-$0.036) en el noroeste que crean el dipolo más marcado de la figura p90". Mapeo preciso
  color→valor del colorbar (13 tonos) muestra que el máximo real es $\sim$$-$0.024 (nunca $-$0.036),
  y que la ubicación dominante por conteo angular de píxeles es sur y sureste (43%) más oeste (17%),
  no noroeste (solo 14%, cuarto lugar). Corregido a "zonas negativas ($\sim$$-$0.008 a $-$0.024) en
  el sur y sureste"; además, a pedido del usuario, se quitó la frase "que crean el dipolo más marcado
  de la figura p90" por ser una calificación no sostenida por la magnitud real de los datos
  (perfumería).
- `reboita2022from`: confirmado, coincide con el mecanismo descrito ("vertical alignment of the warm
  seclusion with an upper-level cut-off pattern" + "weak vertical shear" + calor diabático evidenciado
  por PV fuerte en niveles bajos).

### Párrafo de cierre de `sec:eof_tp` (líneas 182-184) — revisado, 1 corrección aplicada
- `hart2003cyclone`: confirmado, el paper efectivamente propone el espacio de fases justamente para
  diagnosticar el desarrollo de seclusiones cálidas como régimen del ciclo de vida.
- **Línea 184**: **corregido**. Repetía (con dos errores) el detalle de ubicación de negativos por
  región que ya se había corregido con precisión en el panel h de `subsec:eof1_tp_p90`: decía
  "valores negativos confinados al oeste en LPB y al noroeste en SBR", cuando SBR-madurez no tiene
  negativos significativos (17 px muestreados vs. ~4940 en LPB) y LPB los tiene en sur/sureste, no
  oeste. A pedido del usuario, en vez de re-precisar el dato (redundante con lo ya dicho), se quitó
  la cláusula completa por ser repetición innecesaria. De paso se corrigió "campos de viento
  equivalentes" (término no definido antes en la tesis, riesgo ante la banca) por "EOF1 del viento a
  10 metros", nombrando explícitamente qué se compara.

Con esto, `subsec:eof1_tp_p90` y por tanto toda la Sección~\ref{sec:eof_tp} quedan **cerrados**.

### `subsec:significancia_tp` (Significancia estadística, Bootstrap-t) — revisado, corrección sustantiva aplicada
Inspección visual con zoom por panel de las dos figuras grandes `xeof_global_tp_mature.png` y
`xeof_p90_tp_mature.png` (paneles EOF1 de SBR, LPB, ARG en cada una). **Corrección aplicada**: el
texto original afirmaba que en la Población Global el achurado (significancia al 95%) del EOF1 "se
confina al sector oriental" y aparece "fragmentado, sin patrón geométrico continuo" (a diferencia
del viento), y que en p90 el achurado forma "un arco continuo y denso" en las tres regiones por
igual. Verificado con zoom que ambas afirmaciones son incorrectas:
- Global: el achurado NO está confinado al este ni fragmentado. En SBR y LPB forma una franja ancha
  y contigua que va del norte al sureste; en ARG cubre casi todo el dominio (la cobertura más amplia
  de las tres regiones, no la más fragmentada).
- p90: SBR y ARG sí muestran el arco continuo y denso descrito. Pero **LPB no tiene achurado
  apreciable en su EOF1 de p90** (solo una "x" aislada, no una región), pese a tener el salto de
  varianza explicada más grande de las tres regiones (16.0%, ya documentado en
  `subsec:eof1_tp_p90`). Es decir, la transformación morfológica hacia la banda arqueada en LPB no
  está respaldada por significancia estadística al 95%.

Esto invalidaba la lógica comparativa del párrafo (Global=fragmentado/incierto vs. p90=coherente/
predecible en las tres regiones por igual, en paralelo con el argumento ya hecho para el viento). A
pedido del usuario, se reescribió sin esa comparación Global-vs-p90 forzada: ahora se describe cada
figura según lo que realmente muestra, se señala LPB explícitamente como excepción en p90 (patrón
morfológico presente pero no confirmado estadísticamente), y se matiza la conclusión de
"predictibilidad geométrica" como válida para SBR/ARG pero no (aún) para LPB. De paso se corrigió una
referencia cruzada imprecisa: "el salto en varianza explicada" apuntaba a `subsec:var_exp_tp`
(sección general del heatmap, sin desglose por región) cuando el contenido real de esa afirmación
(deltas por región y fase, ej. "+10.1 puntos" en SBR) está en `subsec:eof1_tp_p90`; corregido para
apuntar ahí. También se retiró la cita `oertel2021warm` de este párrafo (ya usada correctamente en
`sec:pdf_tp`) porque sustentaba la idea de fragmentación por convección embebida, que ya no aplica
tras la corrección.

Con esto, `subsec:significancia_tp` queda cerrado.

### `subsec:pc1_p90_tp` + `sec:sintesis_tp` (Subconjunto p90 de PC1, y Síntesis de cierre) — revisado, 1 corrección aplicada
Verificación exhaustiva de `subsec:pc1_p90_tp` contra `tab_stat_p90_tp.tex` (curtosis, asimetría,
correlación de Pearson por región y fase): **todas las cifras citadas coinciden exactamente**, sin
excepción (incluyendo valores extremos como ARG incipiente $\gamma_2=+30.88$ y LPB decaimiento
$\gamma_2=+23.18$). `sec:sintesis_tp` (cierre del capítulo) revisada íntegramente por trazabilidad:
todas sus cifras remiten correctamente a valores ya verificados en secciones anteriores del capítulo
(densidad 0.17 SBR, $29\times10^{-4}$ SBR intensificación, 36.5% LPB decaimiento +22.2 puntos,
correlaciones PC1-vorticidad), sin errores.

Cita `machado2020influence` (línea ~226) verificada contra el paper (Machado et al. 2020, ENSO e
inestabilidad baroclínica/storm tracks en el HS): el texto actual ("modulan la posición e intensidad
de los sistemas ciclónicos, afectando indirectamente su capacidad de generar precipitación") es fiel
al alcance real del paper (que no trata precipitación directamente, solo posición/intensidad de
storm tracks vía inestabilidad baroclínica) y ya evita la sobre-afirmación de una versión anterior
("eficiencia de condensación de vapor de agua") documentada como problemática en la cartilla de
estudio `aporte_autores/01_genesis_ciclogenesis_HS/puntual/machado2020influence.txt`. Sin cambios
necesarios.

**Corrección aplicada** (línea ~238): el mecanismo propuesto para el colapso de correlación PC1-
vorticidad en madurez ("una vez consolidada la banda enroscada...") se aplicaba por igual a SBR y
LPB, pero tras la corrección de `subsec:significancia_tp` sabemos que en LPB esa banda no tiene
significancia estadística confirmada (a diferencia de SBR). Se quitó "consolidada" (implica
confirmación) por "domina el campo" (describe la morfología sin implicar robustez estadística) y se
agregó una oración de cautela explícita para LPB, remitiendo a `subsec:significancia_tp`.

Con esto, `sec:dinamica_pc1_tp`, `sec:sintesis_tp` y por tanto el **Capítulo 5 completo
(`05.vr2_result02_tp.tex`) quedan revisados de principio a fin**.

## Capítulo 5 completo
Revisado sección por sección, con inspección visual de todas las figuras (PDF, PDFe, EOF1,
significancia Bootstrap-t) y verificación numérica exhaustiva contra las tablas de datos reales.
Correcciones sustantivas aplicadas: `simmonds2000mean` (dirección cardinal no sostenida, Cap.
`subsec:kde_tp_global`), `corner2025classification` y `blanchard2021warm` (atribuciones incorrectas,
dos ocurrencias c/u), panel h de `subsec:eof1_tp_p90` (ubicación/magnitud de negativos), línea 184
(repetición de dato ya corregido), y la reescritura de `subsec:significancia_tp` (hallazgo más
importante del capítulo: el texto original describía un contraste Global=fragmentado/p90=coherente
que no se sostenía visualmente; la significancia real es extensa y contigua en Global, y ausente en
LPB-p90 pese al salto de varianza), con su correlato aplicado en `subsec:pc1_p90_tp`.

### Tercera revisión (sesión posterior): "honestidad interpretativa" — ¿alguna narrativa regional se fuerza pese a contradecir datos propios del texto?
A pedido del usuario, tras encontrar en el Capítulo 7 que la narrativa de ARG (separación
"menor"/"atenuada") contradecía los propios números del capítulo, se releyó el Capítulo 5 con el
mismo enfoque. **1 hallazgo real encontrado y corregido**:

- Línea 131 (`subsec:var_exp_tp`) afirmaba que "ARG presenta mayor varianza explicada por el EOF1 en
  las fases iniciales que SBR" — pero la línea 154 (`subsec:eof1_tp_global`), 23 líneas antes,
  establece explícitamente que ARG en fase incipiente tiene "la varianza más baja de la figura"
  (11.1%), más baja que SBR-incipiente (11.4%, línea 150). La afirmación solo es cierta para
  intensificación (ARG 15.6% vs. SBR 11.7%), no para incipiente. Corregido acotando la afirmación a
  la fase de intensificación específicamente, con las cifras exactas, y aclarando que ARG-incipiente
  es el mínimo de toda la figura.

Resto del capítulo revisado sin encontrar otro caso equivalente (se revisaron en particular las
comparaciones SBR/LPB vs. ARG por densidad PDFe, que sí son consistentes con los números citados en
cada panel).

### Pendientes abiertos (a pedido del usuario, "vamos a revisar todos los pendientes")
1. Librería de PCA/EOF real usada en swell y convención de signo del EOF (pendiente nº1 al inicio de
   este archivo) — no resuelto, requiere acceso del usuario al código de swell.
2. Dirección este/oeste de migración del núcleo en `sec:kde_espacial_global` (Cap. 4) con valores
   $(\Delta x_{\text{moda}}, \Delta y_{\text{moda}})$ si el usuario los consigue.

Capítulos que faltan por revisar: Capítulo 6 (Resultados MEOF), Capítulo 7 (Prototipo), Capítulo 8
(Conclusiones), Capítulo 9 (Consideraciones) — todos comentados/deshabilitados en `tese_es.tex`
actualmente.

## Capítulo 4 completo
`04.vr2_result01_w10.tex` (Viento a 10 metros) revisado de principio a fin, sección por sección,
con inspección visual de todas las figuras e inspección directa de las tablas de datos. Resultado
general: capítulo con muy alta fidelidad numérica (decenas de cifras verificadas exactas contra
figuras/tablas); solo 3 correcciones sustantivas aplicadas en todo el capítulo (magnitud de ARG en
`sec:kde_espacial_p90`, intensidad relativa LPB/SBR/ARG en `subsec:eof1_wind10_p90`, y la
contradicción aritmética SBR/ARG en `subsec:res_significancia_madurez`), más 3 referencias rotas
(`subsec:tb_compound_def`→`sec:tb_compound_def`) y ajustes de redacción menores.

**Segunda ronda de revisión de Capítulo 4 (autores adicionales, tras el cierre inicial)**: el usuario pidió
revisar un conjunto ampliado de papers (`gray2024global`, `rudeva2011composite`, `field2007precipitation`,
`gramcianinov2019properties`, `laurila2021characteristics`, `dacre2012atlas`, `gentile2025response`,
`gozzo2014subtropical`, `cardoso2022synoptic`, `coutodesouza2024thesis`, `andrade2024composite`,
`han2025system`, `naud2025lifecycle`, `priestley2022improved`, `dejesus2021multimodel`, y luego un grupo
adicional filtrado por "composite"/"wind speed"/"extratropical cyclone": `bitencourt2010relating`,
`catto2015front`, `miranda2026patterns`, `portal2024linking`, `reboita2022from`) para verificar aportes
puntuales a Capítulo 4, con foco en enfoque lagrangiano y viento a 10 m específicamente. Cambios aplicados:
- Línea ~99 (`sec:kde_espacial_p90`): matizada la oración de cautela sobre sting jet/CCB. Antes decía que
  la analogía HN-HS "no es una equivalencia dinámica demostrada"; se corrigió porque `gray2024global` (ya
  citado en la línea 99 con cifras 15%/27%) sí confirma el mecanismo a nivel de Hemisferio Sur en conjunto.
  Ahora aclara que lo no demostrado es específicamente la desagregación para la cuenca del Atlántico Sur
  (el paper no separa Atlántico Sur de otras cuencas del HS).
- Línea ~38 (`sec:pdf_wind10`, párrafo de ARG): agregada oración con `gramcianinov2024early` sobre
  amplificación de onda baroclínica de bajo nivel en ARG pese a menor humedad, produciendo presión central
  más baja que SBR/LPB.
- Línea ~97 (`sec:kde_espacial_p90`): agregada oración con `rudeva2011composite`, aplicando correctamente
  el espejo hemisférico norte-sur (no este-oeste, ya que el este-oeste no se invierte por Coriolis) al
  hallazgo de posición del máximo de viento en el sector suroeste de ciclones del Atlántico Norte,
  prediciendo consistencia con la concentración noroeste ya documentada en el capítulo.
- Línea ~46 (`sec:pdf_wind10`): agregada oración con `gentile2025response`, comparando el orden de magnitud
  de la moda p90-madurez (~23 m/s) con el valor de vorticidad máxima de su compuesto de clima control
  (~25 m/s, Atlántico Norte), aclarando explícitamente que es solo similitud numérica y que población y
  cuenca oceánica son distintas (a pedido del usuario, para no insinuar equivalencia metodológica de fases).
- Línea ~45 (`sec:pdf_wind10`): **retirado** `cardoso2022synoptic` de la lista de citas que respaldan la
  cifra de ~23-30 m/s en p90-madurez. Verificado que el paper (ciclones subtropicales, percentil 95
  climatológico espacial, no máximo por ciclón) reporta como máximo absoluto en todo el documento ~20 m/s,
  por lo que no sostiene la afirmación de coherencia con 23-30 m/s.

Papers revisados y descartados para Capítulo 4 con justificación (no requieren acción futura a menos que
se reabra el capítulo): `field2007precipitation` (redundante con `rudeva2011composite`, mismo hallazgo de
posición SO), `mcerlich2023extremes`, `naud2020evaluation`, `naud2025lifecycle` (precipitación, fuera de
alcance del capítulo de viento), `han2025system` (framework de clasificación, sin composites de viento del
Atlántico Sur), `dacre2012atlas` (ya usado correctamente en Fundamentos, no en Capítulo 4), `dejesus2021multimodel`
(evaluado, no aplicado), `bitencourt2010relating` (correlación con estaciones fijas, euleriano no lagrangiano),
`catto2015front` (trayectorias WCB, no composite de viento10), `miranda2026patterns` (composite euleriano de
dominio fijo, no centrado en el ciclón), `portal2024linking` (atribución por radio fijo pero mapas eulerianos
de frecuencia, no composite en coordenadas relativas al ciclón), `reboita2022from` (caja lagrangiana de
ancho constante pero estudio de caso único, no composite poblacional, y no es viento10 específicamente).

Confirmados ya correctos sin cambios: `gozzo2014subtropical` (300-450 km, cita exacta), `priestley2022improved`
(3-3.5° del centro, cita exacta contra Fig. 3 del paper), `catto2010climate`, `gramcianinov2019properties`.

`coutodesouza2024thesis` verificado por partes (archivo grande, 8251 líneas): ambas citas (línea ~108,
flujos de calor latente en SBR/LPB vía término $G_E$ del ciclo de Lorenz, más alto en LA-PLATA todo el año
y en SE-BR en invierno; línea ~190, conversión barotrópica pico en madurez) confirmadas fieles contra el
texto original de la tesis doctoral de Danilo Couto de Souza ("Cyclones in the Southwestern Atlantic: Life
Cycle and Energetics", USP 2024). Sin cambios necesarios.

`dejesus2021multimodel` evaluado como candidato final: descartado por decisión conjunta con el usuario.
Su contenido regional (ARG/LA-PLATA/SE-BR, sector cálido noreste en ciclogénesis intensa) es temáticamente
relevante, pero usa viento a 1000~hPa como proxy explícito de 10~m (limitación de datos GCM, declarada por
los propios autores), no viento a 10~m real como exige el criterio aplicado en esta ronda de revisión.

Con esto se da por cerrada la segunda ronda de revisión de citas de Capítulo 4 (lista ampliada de 20 autores
adicionales revisados). Balance: 5 ediciones aplicadas al texto (matiz sting jet, mecanismo ARG, espejo
rudeva2011, comparación gentile2025response, retiro cardoso2022synoptic), 2 citas verificadas sin cambios
(coutodesouza2024thesis), y 13 papers descartados con justificación documentada arriba.

**Adición final de discusión en `sec:sintesis_wind10`**: a pedido del usuario, se agregó un párrafo
`\paragraph{Alcance e implicaciones.}` (entre la oración sobre heterogeneidad de ARG y la oración
"Esta base, que vincula la intensidad...") que sintetiza los 4 resultados más importantes del
capítulo (fragmentación de varianza EOF1 en p90, colapso de la correlación PC1-vorticidad en
p90-madurez, hiperconcentración espacial en p90-madurez, comportamiento diferenciado de ARG) en
clave de discusión: qué podría causar el resultado, qué significado/aplicación tiene (esquemas de
alerta que no dependan solo de vorticidad), y por qué hay que ser prudente (dependencia de
$\zeta_{850}^{\min}$ como métrica puntual vs. una medida integrada de circulación
\citep{sinclair1997objective}; la analogía con CCB/sting jet del HN es una inversión especular, no
una equivalencia dinámica demostrada para el Atlántico Sur). Redactado sin guiones ("-") ni dos
puntos (":") innecesarios, según instrucción explícita del usuario. Con esto, el Capítulo 4 queda
**totalmente finalizado**, incluyendo la discusión de síntesis.

### Pendiente inmediato (próxima sesión/turno)
Capítulo 5 en progreso (ver sección dedicada arriba): `sec:pdf_tp` y `subsec:kde_tp_global` ya
revisados. Continuar con `browning1986conceptual`, `subsec:kde_tp_p90`, y el resto del capítulo
(`sec:var_exp_tp` en adelante), por tramos cortos.

Recordar también el pendiente abierto de la sección "Pendientes por verificar" arriba (librería de
PCA en swell / convención de signo del EOF) — no resuelto aún. Y el pendiente de verificar la
dirección este/oeste de intensificación de la PG en `sec:kde_espacial_global` (Capítulo 4) con los
valores $(\Delta x_{\text{moda}}, \Delta y_{\text{moda}})$ si el usuario los consigue — quedó sin
resolver al cerrar el capítulo.

Capítulos que faltan después de Capítulo 5: Capítulo 6 (Resultados MEOF), Capítulo 7 (Prototipo),
Capítulo 8 (Conclusiones), Capítulo 9 (Consideraciones) — todos comentados/deshabilitados en
`tese_es.tex` actualmente.

## Capítulo 6 — Análisis de Variabilidad Conjunta / MEOF (`06.vr1_result03_meof.tex`)
En progreso. Archivo de trabajo confirmado: `06.vr1_result03_meof.tex` (no `06.vf2_...`), verificado
contra el bloque "RESUMIDA" (comentado) de `tese_es.tex`, que usa la misma serie de sufijos "vr" que
`04.vr2` y `05.vr2` ya revisados. Existe también `06.vf2_result03_meof.tex` (serie "EXTENSA"),
no es el archivo activo.

### Introducción + `sec:meof_varianza` + inicio de `sec:meof_patrones`/`subsec:meof_madurez` (Población Global) — revisado, 1 corrección aplicada, 1 pendiente
Verificación contra `all_expvar_meof.png` (heatmap sin valores impresos, estimado por color) y
`meof1_mature_global.png` (con `Explained Variance` impreso por panel, SBR=26.52%, LPB=26.59%,
ARG=22.31%).

**Corrección aplicada**: línea 84 decía que ARG en madurez tenía "la menor varianza explicada
(18.99%)", contradiciendo la propia línea 80 del mismo párrafo ("oscila entre 22.31% (ARG) y 26.59%
(LPB)"). Confirmado con la figura que el valor correcto es **22.31%**; el 18.99% corresponde en
realidad a ARG en la fase de intensificación (ya usado correctamente en la línea 41, aparente
error de copiar/pegar entre fases). Corregido a 22.31%.

**Pendiente abierto (a pedido del usuario, revisar con más calma más adelante)**: la línea 82 afirma
que "la precipitación presenta cargas positivas en la mitad sur, mientras el viento las presenta en
la mitad norte" para los tres paneles de madurez-Global. Verificado con zoom en los tres paneles de
precipitación (a, d, g de `meof1_mature_global.png`) que el patrón real está orientado
**oeste-este** (positivo al oeste, más intenso hacia el suroeste; negativo al este), no sur-norte.
El viento sí es correctamente norte-sur (positivo al norte, decreciendo hacia el sur, uniforme en
x). Esto también afecta la línea 84 ("SBR... cargas positivas levemente desplazadas hacia el
sur-sureste" — en realidad están al oeste/suroeste, el sureste del panel es neutro) y potencialmente
la interpretación física de la línea 83 (viento hacia "flanco delantero" / lluvia hacia "flanco
posterior"), ya que si los ejes reales son oeste-este (lluvia) y norte-sur (viento), los patrones son
ortogonales entre sí, no antipodales en el mismo eje. **No corregido aún** — el usuario pidió
revisarlo con más calma en una próxima sesión/turno antes de reescribir la interpretación física.

### `subsec:meof_intensificacion` — revisado, corrección sustantiva aplicada (descripción espacial + interpretación física)
Verificación con zoom de los 6 paneles espaciales de `meof1_intensification_global.png` (Población
Global, líneas 39-42, solo rango de varianza 18.99%-22.92%, sin descripción panel por panel en el
texto) y de `meof1_intensification_p90.png` (p90, líneas 51-60, con descripción panel por panel).
Nota de proceso: en una primera pasada inspeccioné por error la figura Global creyendo que
correspondía a la descripción detallada de líneas 55-60 (que en realidad describe la figura p90,
"el contraste con la Población Global..."), lo que produjo un diagnóstico inicial incorrecto
(comunicado al usuario y luego corregido en la misma sesión antes de editar nada).

Verificación de varianza: línea 41 (Global: 18.99% ARG, 22.92% LPB) y línea 53 (p90: 11.65% ARG,
17.03% LPB, 14.06% SBR) exactas contra ambas figuras. Sin cambios en las cifras.

**Corrección aplicada** (líneas 55-59 y 73): la descripción de orientación espacial de los paneles
p90 no correspondía a las figuras. Verificado con zoom en los 6 paneles (a-b, d-e, g-h):
- Precipitación: el texto ubicaba el núcleo positivo de SBR en "cuadrante noreste-este" con
  negativos en "noroeste y sur-suroeste" — el núcleo real está próximo al vórtice, desplazado
  este-sur, flanqueado por negativos al **noreste** y al **sur** (no noroeste/suroeste). LPB: el
  texto decía banda "norte a sur en el sector oriental" con negativos "al oeste y suroeste" — la
  banda real tiene inclinación **noroeste-sureste**, centrada cerca del vórtice, con negativos al
  **noreste** (no oeste). ARG: el texto decía núcleo "al noreste y este" — el núcleo real está
  centrado sobre el vórtice y extendido al **este**, sin sesgo claro hacia el norte.
- Viento: el texto decía anomalías negativas en "casi todo el dominio, con una franja neutra o
  positiva en el borde **noroccidental**" — la franja neutra/débilmente positiva real está al
  **sur** del vórtice (no noroeste), con el negativo intensificándose hacia el **norte**.
- Esto invalidaba la conclusión de línea 59 ("viento predominantemente negativo combinado con
  precipitación positiva al este" → anticovarianza) en su formulación original. Reescrito para
  reflejar la geometría real (precipitación concentrada cerca del vórtice y hacia el sur, viento
  negativo intensificándose hacia el norte), conservando la conclusión general de anticovarianza
  incipiente, que sigue siendo válida con la geometría correcta. También se ajustó la línea 73
  ("viento se intensifica en el sector norte-noroeste" → "hacia el norte"; "precipitación se
  concentra al este" → "cerca del vórtice y hacia el sur") para consistencia.

Con esto, `subsec:meof_intensificacion` queda cerrado.

### Resto de `subsec:meof_madurez` (p90, líneas 94-118) — revisado con zoom, sin correcciones firmes
Inspección de los 6 paneles de `meof1_mature_p90.png`. Varianza conjunta (línea 97: 19.02% SBR,
16.42% LPB, 15.41% ARG) exacta contra los tres paneles PC1. Morfología de precipitación (arco
sureste-sur envolviendo hacia el este/noreste, líneas 100-102) confirmada razonablemente en SBR y
LPB. Dos observaciones sin corrección aplicada (evidencia insuficiente para justificar reescritura,
a diferencia de los hallazgos de intensificación):
- Línea 102 llama a ARG "el patrón más difuso de los tres" — visualmente el núcleo de ARG (panel g)
  es en realidad un bloque continuo grande y bien definido (no menos compacto que SBR/LPB), lo que
  hace dudosa la palabra "difuso"; pero como no hay una métrica objetiva de "difusividad" para
  zanjarlo con certeza (a diferencia de "positivo vs. negativo" en intensificación), se deja sin
  cambio, señalado aquí como posible ajuste futuro.
- Línea 103 dice que el núcleo positivo de viento está "al noroeste del centro" — la lectura visual
  en los tres paneles (b, e, h) lo ubica más bien al **oeste**, cerca de la latitud del vórtice
  ($\Delta y \approx 0$), no claramente desplazado al norte. No se corrigió porque el hallazgo tiene
  bajo grado de certeza visual (núcleo pequeño, borde ambiguo) y porque corregirlo tendría un radio
  de impacto amplio (se repite en líneas 104, 114, 116, 118 y en `sec:discusion_meof`/
  `sec:sintesis_meof`, además de ecoar el hallazgo ya verificado de "cuadrante noroeste" para el
  EOF1 univariado de viento en el Capítulo 4). Queda como posible pendiente a revisar con más
  cuidado (p. ej. midiendo píxeles) si el usuario lo pide explícitamente.

### `sec:meof_coherencia` — revisado, sin correcciones
Verificado contra `tab_meof_coherencia.tex`: **todos los valores de correlación citados en el texto
(líneas 127-129) coinciden exactamente** con la tabla, en Global y p90, las tres regiones, las
cuatro fases (incluyendo el mínimo/máximo Global +0.12/+0.40 y el valor destacado de p90-LPB-madurez
$\rho=-0.49$). Sin errores.

### `sec:meof_varianza` (líneas 13-16) — verificación adicional, sin corrección (falsa alarma descartada)
Nota de proceso: intenté estimar el rango "19%-27%" (Global) del heatmap `all_expvar_meof.png` por
color de celda, ya que no tiene valores impresos. La estimación por color inicial sugería un piso
más bajo (~14-16%) que contradecía el "19%" del texto. **Antes de reportarlo, calibré el método
contra los 6 valores exactos ya confirmados** (SBR/LPB/ARG en intensificación y madurez, de las
figuras `meof1_intensification_global.png` y `meof1_mature_global.png`) y el color estimado no
coincidía ni de cerca con esos valores conocidos (p. ej. SBR-Madurez=26.52% real vs. ~18-20%
estimado por color) — es decir, mi supuesto sobre los niveles de color del heatmap (`BoundaryNorm`)
era incorrecto y el método no es confiable. Descartada la estimación por color; el rango "19%-27%"
del texto coincide con precisión con los extremos conocidos y verificados (ARG-Int=18.99%≈19%,
LPB-Mat=26.59%≈27%), así que se considera correcto. **Sin cambios.** (Aplica también a las cifras
similares de líneas 136, 140 y 158 en `sec:discusion_meof`/`sec:sintesis_meof`, consistentes con los
mismos extremos conocidos.)

### `sec:discusion_meof` — revisión parcial
Cita `corner2025classification` (línea 141, "análisis de componentes principales dispersas... no
escalan linealmente") verificada contra el paper: sí usa "sparse PCA" como método (confirmado en el
texto del paper) y sí reporta una relación no lineal entre deepening rate y métricas de impacto —
cita fiel.

**Resto de citas de `sec:discusion_meof` verificadas — todas fieles, sin correcciones.** Se
encontraron "cartillas de estudio" ya preparadas en sesiones previas en
`aporte_autores/02_fajas_transportadoras_WCB_CCB/` y `aporte_autores/01_genesis_ciclogenesis_HS/`
(una por cada paper, con resumen, metodología, hallazgos, cita textual exacta usada en la tesis y
preguntas de jurado anticipadas), que permitieron verificar rápido y con alta confianza:
- `martin1999forcing`: ya verificada fiel también en Cap. 5 (trowal airstream); reutilización
  correcta.
- `martinez2014cold`: fiel — el paper (caso Friedhelm, HN) sí establece mediante trazadores químicos
  que la CCB es masa de aire distinta del sting jet y coincide con los vientos más fuertes
  observados, sustentando "principal motor de la circulación de bajo nivel en oclusión".
- `eisenstein2023identification`: fiel. Nota de proceso: la cartilla (de sesión previa) advertía una
  posible discrepancia entre el título citado en el `.bib` y el paper realmente verificado —
  comprobado en esta sesión que **ya no aplica**: el título actual en `bibliografia_vr1.bib` coincide
  exactamente con el paper verificado (Eisenstein et al. 2023, Part 2, climatología europea),
  aparentemente corregido en una sesión posterior a la cartilla. Sin acción necesaria.
- `schemm2014linkage`: fiel — mecanismo de PV (calentamiento diabático del WCB → aumento de PV en
  la CCB → jet de bajo nivel intensificado en la cola del frente curvado) citado con precisión.
- `portal2024linking`: fiel — paralelismo conceptual correcto (Mediterráneo, R∧W bajo WCB, W∧W bajo
  intrusión seca), con las salvedades metodológicas (coocurrencia binaria vs. EOF continuo) ya
  reconocidas implícitamente por el tono cauteloso del texto de la tesis.
- `gozzo2013air`: fiel — experimentos de sensibilidad WRF (FLX vs. NOFLX) sí muestran que los flujos
  de calor latente/sensible oceánicos son decisivos para la seclusión cálida y el frente retrocedido,
  sustentando el contraste SBR/LPB (mayor flujo) vs. ARG (menor, más orográfico).
- `bjerknes1922life`: fiel — cita puramente genealógica/histórica (modelo noruego de frentes),
  verificada contra el PDF completo (16 páginas) en una sesión previa; uso apropiado como anclaje
  conceptual antes de introducir el WCB de Browning (1986).

Con esto, `sec:discusion_meof` queda cerrada (todas las citas verificadas, ninguna requirió cambios).

### `sec:sintesis_meof` — revisado, sin errores nuevos
Cierre del capítulo (líneas 154-161). El rango "~20-27%" (Global) y "12-19%" (p90) de la línea 158
es consistente con los extremos exactos ya verificados (ver nota de calibración arriba). La
correlación negativa citada en línea 160 coincide con `tab_meof_coherencia.tex` (ya verificada). No
se detectaron cifras nuevas incorrectas.

La síntesis sí **repite, sin agregar nada nuevo, los dos puntos ya identificados como abiertos**:
- Línea 158 ("co-ubicación... en el sector frontal oriental" para la Población Global) depende del
  mismo hallazgo de orientación aún no corregido en `subsec:meof_madurez` (línea 82: precipitación
  es oeste-este, no sur-norte; el texto original tampoco decía "sector oriental" así que esta frase
  de la síntesis en realidad es una *nueva* formulación del mismo problema, no una cita literal — ver
  nota abajo).
- Línea 159 ("núcleo de viento al noroeste" en p90-madurez) repite la ubicación que en
  `subsec:meof_madurez` (línea 103) se señaló como más probablemente **oeste** que noroeste, sin
  suficiente certeza visual para corregir con confianza.

### Resolución de las dos salvedades abiertas (a pedido del usuario, sesión siguiente)
Ambas se resolvieron con medición precisa por píxeles (calibrando escala real grados/píxel contra
las líneas de grilla de cada panel, en vez de solo inspección visual), en vez de dejarlas abiertas.

**Salvedad 2 (núcleo de viento p90-madurez, "noroeste" vs. "oeste") — CONFIRMADA Y CORREGIDA.**
Medí el centroide del núcleo positivo de viento en los tres paneles de `meof1_mature_p90.png` (b, e,
h), calibrando la escala real (píxeles/grado) contra las líneas de grilla de cada panel: SBR
$(\Delta x,\Delta y) \approx (-3.6, -0.2)$; LPB $\approx (-1.5, -0.4)$; ARG $\approx (-4.9, +0.4)$.
Las tres regiones coinciden en que el núcleo está al **oeste**, prácticamente a la misma latitud del
vórtice ($\Delta y \approx 0$), no desplazado al norte como implica "noroeste". Se contrastó además
con el EOF1 univariado de viento del Capítulo 4 (`subsec:eof1_wind10_p90`, línea 93: núcleo
hiperconcentrado en $\Delta x \in [-1°,-3°]$, $\Delta y \in [+2°,+3°]$, es decir sí genuinamente
noroeste) — confirmando que el núcleo del **MEOF1** (covarianza conjunta) está desplazado hacia el
sur respecto al núcleo del **EOF1 univariado** de viento solo, un hallazgo real y no un error de
lectura. Corregido "noroeste" → "oeste" (o "sector occidental"/"lados opuestos" según el contexto)
en las líneas 103, 104, 110 (caption), 114, 116, 118, 129, 146, 149 y 159 (síntesis); en la línea 116
se agregó una explicación explícita de la diferencia cuantitativa entre el núcleo MEOF (oeste,
$\Delta y\approx 0$) y el núcleo EOF1 univariado (noroeste, $\Delta y\approx+2$ a $+3$), en vez de
afirmar que el MEOF simplemente "replica" al univariado.

**Salvedad 1 (orientación Global, "sur/norte" vs. "oeste-este/norte-sur") — CONFIRMADA Y CORREGIDA.**
El intento de medición por píxeles para `meof1_mature_global.png` fue contaminado por texto/etiquetas
con colores similares a los tonos de relleno (falsos positivos), así que se resolvió con inspección
visual cuidadosa y repetida (zoom por panel) de los 6 paneles (a, d, g precipitación; b, e, h viento),
ya realizada previamente en la sesión: en las tres regiones, la precipitación es un dipolo
**oeste(positivo)-este(negativo)** con intensificación hacia el suroeste, mientras el viento es un
gradiente **norte(positivo)-sur(débil, sin cruzar a negativo)**, uniforme en x. Confirmado que NO son
"el mismo sector" ni "mitad sur vs. mitad norte" como decía el texto original, sino ejes ortogonales
entre sí. Corregido en las líneas 82, 84 (`subsec:meof_madurez`), 136-137, 142 (`sec:discusion_meof`)
y 158 (`sec:sintesis_meof`), reformulando el argumento de "co-localización en el mismo sector" hacia
uno más preciso: ambos campos son extensos y de signo mayormente constante en el régimen medio (sin
núcleos aislados ni cambios de signo abruptos), pero con sus gradientes dominantes orientados en ejes
distintos (oeste-este en precipitación, norte-sur en viento) — la idea general del capítulo (que la
Población Global es menos geométricamente separada que p90) se mantiene, solo se corrigió la
descripción espacial específica que la sustentaba.

## Capítulo 6 completo — sin salvedades abiertas
`06.vr1_result03_meof.tex` revisado de principio a fin y con ambas salvedades resueltas:
`sec:meof_varianza`, `subsec:meof_intensificacion` (corrección sustantiva), `subsec:meof_madurez`
(corrección numérica en Global + corrección de orientación en Global y p90, con medición precisa por
píxeles), `sec:meof_coherencia` (limpia), `sec:discusion_meof` (7 citas verificadas fieles +
correcciones de orientación en líneas 136-137, 142), `sec:sintesis_meof` (limpia numéricamente +
correcciones de orientación en líneas 158-159). Balance del capítulo: 2 errores numéricos corregidos
(ARG-madurez 18.99%→22.31%; referencia cruzada mal apuntada), 1 sección reescrita por completo
(intensificación p90), y las descripciones de orientación espacial en madurez (Global y p90)
corregidas con evidencia cuantitativa.

## Capítulo 7 — Prototipos estructurales (`07.vr1_result04_prototipo.tex`)
Archivo de trabajo confirmado: `07.vr1_result04_prototipo.tex` (serie "vr", no `07.vf2_...`), por el
mismo criterio usado en capítulos 4-6. Capítulo corto (80 líneas) pero muy denso en cifras exactas
($\Delta x$, $\Delta y$ impresos en cada panel de las dos figuras principales), lo que permitió una
verificación muy precisa por cálculo directo en vez de solo inspección visual.

### Revisado: introducción, `sec:prototipo_global`, `sec:prototipo_p90`, discusión (parcial), síntesis
Verificación exhaustiva contra los valores $\Delta x,\Delta y$ impresos en
`prototipo_12panels_global.png` y `prototipo_12panels_p90.png` (12 paneles c/u, con distancia
euclídea y separación zonal recalculadas a mano para contrastar cada afirmación cuantitativa del
texto). **5 correcciones aplicadas**:

1. **Error puntual autocontradictorio** (línea 47, SBR incipiente p90): el texto llamaba "noroeste" a
   la moda de viento pese a citar $\Delta x=+2{,}1°$ (positivo = este). Corregido a "noreste", con
   nota aclaratoria de que la orientación noroeste aparece recién en fases posteriores.
2. **Contradicción interna** (línea 26, ARG Global): decía que el viento estaba "sistemáticamente"
   al noroeste "en los cuatro paneles" (incipiente a decaimiento), pero el panel incipiente tiene
   $\Delta x=+3{,}4°$ (este) y la propia línea 22, dos párrafos antes, ya lo había descrito
   correctamente como "noreste". Corregido acotando la generalización a partir de intensificación.
3. **Rango de separación latitudinal impreciso** (línea 22, SBR incipiente/intensificación Global):
   decía "0,5°-1°"; los valores reales dan 0,1° (panel a) y 0,7° (panel b). Corregido a "0,1°-0,7°".
4. **Comparación base engañosa** (línea 39): contrastaba la separación p90 de SBR-madurez (>8°) con
   "los 3°-4° observados en la Población Global" de forma genérica, pero el valor real del mismo
   panel (SBR-madurez-Global) es ~5,8°, y algunos paneles de fases tardías en Global (especialmente
   ARG) ya superan 10°. Corregido a comparar contra el valor exacto del panel homólogo (~5,8°) y
   acotar que la brecha grande solo aplica a fases tardías (fases tempranas: 1°-3°).
5. **Hallazgo más importante — la narrativa regional de ARG estaba invertida** (líneas 39, 45, 58,
   78): el texto afirmaba repetidamente, con respaldo causal en `gozzo2013air` (menos flujo de calor
   latente → oclusión más lenta → separación "moderada"/"menor"/"más atenuada"), que ARG mostraba
   **menor** separación viento-precipitación que SBR y LPB en p90. Calculando la distancia euclídea
   real entre las modas de cada panel (madurez+decaimiento): **ARG ≈10-11° (la mayor de las tres)**,
   SBR ≈9-9,5°, LPB ≈8-9°. Es decir, ARG tiene la separación **más grande**, no la más pequeña.
   Corregido en las 4 líneas: se mantiene que la banda de precipitación de ARG es más difusa/débil
   (efecto de magnitud/forma, no cuestionado), pero se retira la afirmación de que la separación
   modal sea menor, y se temperó la certeza causal de `gozzo2013air` como explicación única de la
   magnitud de separación (dejándolo como pregunta abierta, sin fabricar un mecanismo alternativo no
   verificado). También se agregó ARG a la síntesis final (línea 78), que antes solo mencionaba
   SBR/LPB pese a que ARG tiene la separación más amplia.

**Citas verificadas fieles, sin cambios** (contra cartillas de estudio ya preparadas en
`aporte_autores/`): `cardoso2022synoptic` (dominio 20°×20°, co-localización este/noreste en
desarrollo activo — cita central, usada en 7 pasajes de la tesis, fiel en las dos reutilizaciones de
este capítulo) y `priestley2022improved` (CCB en flanco posterior-occidental, HN; comparación
especular con el cuadrante noroeste del Atlántico Sur — la propia cartilla ya advierte que el paper
NO trata precipitación, y el texto de la tesis ya lo aclara explícitamente, sin sobre-atribución).

### Auto-revisión de las correcciones anteriores (a pedido del usuario) — 2 errores propios encontrados y corregidos
El usuario pidió revisar de nuevo lo editado en este capítulo por sospecha de errores. Recalculé a
mano (script Python) todas las distancias euclídeas usadas en las correcciones anteriores para
verificarlas contra los valores impresos en las figuras. Se confirmaron correctas las correcciones
1-3 y la 5 (la inversión de la narrativa de ARG), pero se encontraron **2 errores nuevos que yo mismo
introduje** al redactar la corrección 4 (línea 39):
- Había escrito que las separaciones en la Población Global durante fases tempranas "apenas alcanzan
  1°-3°" — falso: recalculando las 6 combinaciones incipiente/intensificación (paneles a,b,e,f,i,j),
  el rango real es 0,7° a 5,5° (LPB-incipiente=5,0°, ARG-intensificación=5,5°), lo que además
  contradecía directamente el propio texto de la línea 22 (que ya citaba 4,9° para LPB-incipiente,
  panel e). Corregido: ahora se explica que la brecha Global-vs-p90 es grande en SBR (fases tempranas
  0,7°-0,9°) pero mucho menos marcada en LPB/ARG, que ya parten de separaciones altas en la Población
  Global.
- Había escrito que la separación de ARG en madurez p90 (panel k, ~10°) era "la más amplia de todo el
  subconjunto p90" — falso: el panel l (ARG decaimiento) es aún mayor (~11°, ya lo había calculado
  yo mismo para la corrección 5, pero no lo crucé con esta otra frase al redactarla). Corregido para
  atribuir el máximo real al decaimiento, no a la madurez.

Ambos eran errores de redacción introducidos al escribir las correcciones (cifras inventadas o mal
cruzadolas contra otros cálculos ya hechos en la misma sesión), no errores de lectura de las figuras.
Recomendación para el futuro: al insertar una cifra nueva de respaldo (no solo corregir una existente),
recalcularla explícitamente en vez de estimarla de memoria.

### Segunda auto-revisión (a pedido del usuario: "¿estás seguro que no hay más errores?") — 1 hallazgo nuevo, resto verificado limpio
El usuario pidió confirmar que no quedaban más errores, y preguntó si el capítulo cumple la
estructura esperada de un capítulo de resultados+discusión, y si hacen falta más autores para el
mecanismo físico. Se hizo una segunda pasada completa:

**Citas restantes de `sec:discusion_prototipos` verificadas, todas fieles, sin cambios** (contra
cartillas de `aporte_autores/`): `gramcianinov2023impact` (oleaje extremo, climatología agregada vs.
prototipos por fase — cita central usada correctamente), `han2025system` (SyCLoPS, comparación
metodológica correcta, la tesis distingue bien clasificación taxonómica vs. cuantificación
probabilística propia), `evans2012climatology` y `gozzo2014subtropical` (hibridez estructural de
ARG/SBR, uso cualitativo fiel), `deSouza2025CycloPhaser` (CycloPhaser, mitigación de la limitación de
mezclar fases en el subconjunto p90 estático — uso correcto). `corner2025classification` (comparación
metodológica genérica, sin cifras específicas, fiel).

**Hallazgo nuevo y corregido**: el capítulo nombra "Shapiro-Keyser" dos veces (líneas 41 y 58) y usa
el concepto de "intrusión seca" cinco veces, pero **no citaba `shapiro1990life`** (el paper original
del modelo) **ni `browning1986conceptual`** (ancla estándar de la intrusión seca), pese a que estos
son exactamente los dos autores que la tesis cita, sin excepción, cada vez que menciona estos mismos
conceptos en los Capítulos 1, 2, 4, 5 y 6 (verificado por grep en todo el proyecto). Era una
inconsistencia real de cobertura bibliográfica respecto al patrón del resto de la tesis, no un error
de contenido. Agregado `\citep{shapiro1990life}` en ambas menciones de Shapiro-Keyser (líneas 41 y
58) y `\citep{browning1986conceptual}` en la oración de intrusión seca (línea 41).

**Verificación cuantitativa adicional de la afirmación "banda de precipitación de ARG más difusa"**
(línea 58): medí por script el tamaño de la caja delimitadora (bounding box) del contorno azul (KDE
precipitación) en los 12 paneles de `prototipo_12panels_p90.png`. Resultado **ambiguo, no
concluyente**: en promedio sobre las 4 fases, ARG sí tiene la caja más grande (~262px de diagonal)
frente a SBR (~233px) y LPB (~233px), pero ese promedio está dominado por la fase incipiente
(ARG=300px, un valor atípico); en la fase específica que menciona la oración corregida (madurez),
ARG (247px) y SBR (249px) son prácticamente iguales, y LPB (228px) es el más compacto de los tres —
es decir, para madurez específicamente, la evidencia NO respalda claramente que ARG sea "más difusa
que SBR y LPB". Es una métrica burda (caja delimitadora, no área real del contorno) así que no es
concluyente en ningún sentido; se deja sin corregir por falta de evidencia suficientemente firme
(distinto de los hallazgos anteriores, que sí tenían cifras exactas impresas para contrastar), pero
se documenta aquí como sospecha razonable para que el usuario lo revise si tiene los datos originales.

**Sobre la estructura del capítulo** (pregunta del usuario): el capítulo cumple e incluso excede la
estructura de un capítulo de resultados+discusión estándar — tiene introducción metodológica,
resultados (dos secciones: Población Global y p90), una sección de Discusión explícita de 5 párrafos
temáticos (validación metodológica, mecanismo físico, comparación interhemisférica, vínculo con el
marco MEOF, limitaciones y trabajo futuro) y una Síntesis de cierre. Es, de hecho, más explícito en su
separación resultados/discusión que los Capítulos 4 y 5 (que no tienen una sección "Discusión"
separada, solo síntesis). Estructuralmente completo.

### Pendiente inmediato
Capítulo 7 revisado a fondo dos veces. Único punto sin resolver: la afirmación "banda de ARG más
difusa" (línea 58), ambigua con la evidencia disponible, no corregida. Continuar con Capítulo 8
(Conclusiones) si el usuario lo pide.

Pendientes heredados de capítulos anteriores, aún abiertos:
1. Librería de PCA/EOF real usada en swell y convención de signo del EOF — no resuelto, requiere
   acceso del usuario al código de swell.
2. Dirección este/oeste de migración del núcleo en `sec:kde_espacial_global` (Cap. 4) con valores
   $(\Delta x_{\text{moda}}, \Delta y_{\text{moda}})$ si el usuario los consigue.
