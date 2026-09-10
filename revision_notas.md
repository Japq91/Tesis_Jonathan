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

### 2. `detrend()` — RESUELTO
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

### Pendiente inmediato (próxima sesión/turno)
Siguiente tramo: `sec:kde_espacial_global` (línea 53, "Distribución espacial de máximos (PDFe),
Población Global") — no revisada todavía.

Recordar también el pendiente abierto de la sección "Pendientes por verificar" arriba (librería de
PCA en swell / convención de signo del EOF) — no resuelto aún.

Capítulos que faltan después de Capítulo 4: Capítulo 5 (Resultados TP), Capítulo 6 (Resultados MEOF),
Capítulo 7 (Prototipo), Capítulo 8 (Conclusiones), Capítulo 9 (Consideraciones) — todos comentados/
deshabilitados en `tese_es.tex` actualmente, y es de esperar que compartan el mismo problema de
labels inconsistentes (`subsec:tb_compound_def`, `subsubsec:tb_compositing`, posiblemente otros)
hasta que se revisen uno por uno.
