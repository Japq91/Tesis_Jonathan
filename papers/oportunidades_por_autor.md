# Revisión autor por autor — `papers/files_MD/`

Documento de seguimiento del recorrido exhaustivo por los 106 archivos de `papers/files_MD/`, cruzando cada uno contra el uso actual en la tesis (capítulos en versión `vr`, las activas) y contra `tex_es/bibliografia.bib`. Objetivo: detectar contenido relevante (mecanismo físico, cuadrante/ubicación, valores numéricos de magnitud/densidad) que el autor aporta pero que la tesis todavía no aprovecha, y anotar exactamente dónde incorporarlo.

Solo se registran aquí los autores con una **oportunidad concreta** (contenido no aprovechado) o un **hallazgo pendiente** (error/matiz nuevo detectado durante el recorrido que no se había visto antes). Los autores ya usados correctamente y sin oportunidades adicionales no generan entrada — se cuentan en el progreso pero no se listan, para no inflar el documento.

**Progreso:** 106/106 revisados — recorrido completo. 14 oportunidades registradas, 16 errores nuevos pendientes de decisión, 17 matices nuevos, 14 dudas viejas resueltas, 4 puntos marcados "verificar contra fuente directa", 1 problema de redacción (tiempo verbal) detectado fuera del alcance de fidelidad de citas.

**Fase de aplicación completa (2026-09-04).** Los 14 hallazgos pendientes identificados en el conteo exhaustivo del 2026-09-02 fueron revisados y aplicados uno por uno, capítulo por capítulo, con el usuario revisando y ajustando cada redacción antes de aplicar (2 quedaron cerrados sin aplicar por decisión del usuario, ver Cap. 02). Los 7 capítulos activos (`tex_es/0X.vrN_*.tex`) están completos, sin pendientes. Estado por capítulo:

- **Cap. 01 — completo, sin pendientes.** Aplicados: `jones1993climatology` (L14), `reboita2026meteorology` oportunidad (L15 nueva, cifra ~200 ETC/año), `reboita2010south` MATIZ (L16, diferenciación de mecanismos por región), `reboita2022from` MATIZ/posible ERROR (L26, separado en dos mecanismos, añadida `reboita2026meteorology` para el SALLJ), `miranda2026patterns` (L50), `kodama2019perspective`+`simmonds2000variability` (L50, oración nueva conjunta), `neu2013intercomparison` (L42). Cerrados sin aplicar: `IPCC2021_WG1_Chapter11_Extremes`, `masson2022tendencias` (redundantes con Kodama/Simmonds).
- **Cap. 02 — completo, sin pendientes.** Aplicados: `shapiro1990life`→`bjerknes1922life` (L9, + oración puente a Shapiro-Keyser en L10), `inatsu2004zonal`+`vera2002cold` (L11), `reboita2022from` MATIZ (L15, "flujos de calor latente"→"flujos de calor sensible y latente"), `sinclair1997objective`+`padilhareinke2024objective` (L32-33), `gramcianinov2024early` MATIZ (L81), `sinclair1995climatology` (L89), `carlson1980airflow` (L102), `catto2015front` (L104), `gozzo2013air`+`vera2002cold`+`pepler2020dimensional` (L127), `gramcianinov2024early` ERROR+`dejesus2021multimodel` matiz (L135), `chen2025characteristics` (L177), `han2025system` (L188, revisado, sin cambios), `sinclair2023relationship`+`gentile2025response`+`russo2025impacts` (L145), `coutodesouza2024thesis` oportunidad "Decaimiento" (L164, reasignada desde `andrade2024composite` tras comparar ambos autores + añadido anclaje a $\zeta_{850}$ faltante), `coutodesouza2024new` oportunidad dato 60% retención (L53). Diferido por decisión del usuario: `marrafon2022classificacao` Oportunidad 2 (estacionalidad invernal).
- **Cap. 03 — completo, sin pendientes.** 2 aplicados (`gramcianinov2019properties`/`gramcianinov2020analysis` ERROR grave en L30+tabla, `gramcianinov2020analysis` MATIZ en L13) + `marrafon2022classificacao` Oportunidad 1 cerrada sin aplicar (metodología no coincide con la de la tesis, verificado).
- **Cap. 04 — completo, sin pendientes.** Aplicados: `padilhareinke2026characterization` (L45), `eisenstein2023identification` MATIZ (L96, reasignado a "indistinguibles en superficie" en vez de "fractura frontal", + "austral"→"Hemisferio Sur"), `hyeok2024extrem` (L101), `reboita2018extratropical` (L105), `shapiro1990life` (L109), `hoskins2005new`+`dossantos2023response` (L143, reformulado para conectar génesis→madurez con el resultado real de EOF1).
- **Cap. 05 — completo, sin pendientes.** Aplicados: `laurila2021characteristics` ERROR (L35, reasignado a `oertel2021warm` para la cláusula de precipitación), `shapiro1999bridge` MATIZ (L40, "se enrosca hacia el centro"→"desciende al oeste del centro", + disclosure de Hemisferio Norte; L97 revisada sin cambio necesario, hereda la corrección), `mcerlich2023extremes` oportunidad menor (cifras 80%/46% agregadas), `naud2025lifecycle` oportunidad menor (L97, cresta térmica/vértice del sector cálido, reformulada como hallazgo descriptivo en vez de comparativo, con disclosure de Hemisferio Norte), gancho de oclusión (L77, `gramcianinov2019properties` como respaldo de que la oclusión está documentada de forma extendida en la cuenca del Atlántico Sur, + guiones largos corregidos en la misma oración).
- **Cap. 06 — completo, sin pendientes.** Aplicados: `mendes2010climatology`+`simmonds2000mean` MATIZ (L33, se retira la cláusula "más intensos... a medida que profundizan", no respaldada por ninguna de las dos fuentes), `shapiro1999bridge` MATIZ (L118, misma corrección geométrica/terminológica que Cap. 05 L40, + disclosure de Hemisferio Norte + "vórtice"→"sistema" en el párrafo, + se evita mencionar "presión").
- **Cap. 07 — completo, sin pendientes.** Aplicados: `crespo2020potential`→`reboita2026meteorology` ERROR (L45, SALLJ/humedad tropical reasignado a fuente que sí lo documenta como hallazgo propio para SBR/LPB, + "vórtice"→"sistema"), `han2025system` ERROR triple (L68, acrónimo/nombre mal expandido, alcance global no restringido a HN, y contraste "cualitativo vs. cuantitativo" corregido a diferencia de método de cuantificación).

**Nota de coordinación importante:** las entradas de `inatsu2004zonal` (Cap.02 L11) y `vera2002cold` (Cap.02 L11, más abajo) documentan citas dentro de **la misma oración** de la tesis (reconstruida: *"\citet{inatsu2004zonal} demostraron que la asimetría zonal del storm track está forzada por la topografía de los Andes, la cual modula la propagación de ondas baroclínicas sobre el subcontinente sudamericano \citep{vera2002cold} y define regiones preferenciales de desarrollo en latitudes extratropicales."*). Se revisaron por separado (cada fork solo vio la cita que le tocaba) y ambas tienen hallazgos propios — ver ambas entradas antes de aplicar cualquiera de las dos, para no dejar la oración incoherente al editarla.

**Dudas viejas resueltas durante el recorrido:**
- `bjerknes1922life` — auditoría Cap.06-07 lo marcó "no verificable" (`.md` vacío). Ahora hay cartilla basada en el PDF completo (16 pp.); uso actual en Cap. 06 confirmado apropiado (anclaje histórico-conceptual, no evidencia empírica). Sin acción.
- `browning1986conceptual` — auditoría Cap.05 lo marcó "archivo fuente corrupto". Existe `browning1986conceptual_rev.md` (1270 líneas, traducción/adaptación al HS de Silva Dias y Hallak 2012); usos actuales en Cap. 02/05/06 confirmados apropiados. Sin acción.
- `chen2024evaluation` — auditoría Cap.05 marcó como error que se le atribuyera "la convección controla la cola superior de la distribución" (no es hallazgo de este paper). En el texto activo (`05.vr2`, L24) esa afirmación ya está correctamente re-atribuida a `flaounas2018heavy`; `chen2024evaluation` solo respalda la partición estratiforme/convectiva y las cifras de sesgo ERA5. Sin acción.
- `dacre2023climatology` — auditoría antigua de Cap.05 marcó como error que "el máximo de precipitación ocurre antes que el de intensidad" fuera hallazgo propio del paper (creía que venía de Bengtsson 2009/Booth 2018 citados en su introducción). Verificación contra el `.md` fuente completo confirma que **sí es un hallazgo cuantificado propio** (desfase de 24h, calculado sobre su compuesto de 400 ciclones), listado en sus "Hallazgos clave". La auditoría antigua era el error, no el texto de la tesis. Sin acción — no corregir.
- `dalanhese2023new` — auditoría antigua de Cap.04 vr1 marcó como error que se usara para sustentar "previsibilidad geométrica" de máximos de viento (el paper no aborda eso). Esa cita/afirmación ya no existe en el texto activo `04.vr2` — fue removida durante la revisión extensa de Cap. 04 en esta sesión. El único uso activo restante (Cap. 01 L52, comparación de fuentes de datos para detección de ciclogénesis) es fiel al paper. Sin acción.
- `dejesus2021multimodel` — auditoría antigua de Cap.04 vr1 marcó como error el rango "1.5-2 m/s hacia fines de siglo" (ocultaba que LPB/RG2 en realidad proyecta solo 1 m/s). Esa cita/afirmación ya no existe en el texto activo — fue removida durante la revisión de Cap. 04. El uso activo restante (Cap. 02 L133, sector cálido NE en el HS) es fiel y ya estaba verificado contra `citas_verbatim_cuadrantes.md`. Sin acción.
- `gan1994influence` — versión anterior de Cap. 02 atribuía a este paper el mecanismo específico de "compresión-estiramiento-conservación de vorticidad potencial" (en realidad marco teórico de Buzzi/Hayes que Gan & Rao solo usan para interpretar, no derivan). Ya no está en el texto activo `vr4`. Sin acción.
- `gramcianinov2020analysis` — la cartilla advertía sobre una cifra "~2000 km de diámetro de circulación" atribuida a este paper en una versión anterior de Cap. 02 (L29), no verificable en el artículo. Ya no existe en el texto activo — la afirmación de crecimiento del radio en madurez ahora cita correctamente a `simmonds2000size`. Sin acción.
- `gramcianinov2023impact` — auditoría antigua marcó Cap.07 L54 como "MATIZ" (respaldo genérico, no hallazgo específico) para "los análisis climatológicos que promedian el ciclo de vida completo no capturan la reorganización espacial". Verificación directa contra la cartilla desmiente esto: el propio paper reconoce explícitamente esa limitación (analiza tendencias promediando todo el ciclo de vida sin estratificar por fase) — la cita es precisa, no genérica. La auditoría antigua era el error. Sin acción.
- `hyeok2024extrem` — la cartilla describe un uso en una versión anterior de Cap. 02 (L135) con una afirmación de cuadrante explícita ("sectores sur y oeste, especialmente el suroeste") sin marcar espejo. Esa cita ya no existe en el texto activo — solo quedan los 2 usos genéricos (sin cuadrante) en Cap. 04. Sin acción sobre ese punto (ver oportunidad nueva abajo para un uso distinto).
- `machado2020influence` — la cartilla registra que una versión anterior de Cap. 05 atribuía a este paper que las oscilaciones de baroclinicidad "modulan la eficiencia de los sistemas ciclónicos para condensar vapor de agua" (el paper no mide condensación/precipitación, solo posición/intensidad vía storm tracks). El texto activo (`05.vr2`, L226) ya usa una formulación distinta y correcta ("modulan la posición e intensidad... afectando indirectamente"). Sin acción.
- `shapiro1990life` — la cartilla advertía que el PDF local solo tenía 2 páginas y que el modelo de 4 fases se había reconstruido vía fuente secundaria (`schultz2021antecedents`). Verificado: `papers/files_MD/shapiro1990life.md` ahora contiene el capítulo completo vía OCR (2093 líneas), así que esa limitación ya no aplica — puede verificarse directamente contra la fuente primaria. Sin acción (ver hallazgos nuevos abajo).
- `oertel2021warm` — se verificaron las 6 ocurrencias activas restantes (además de las 2 ya conocidas y corregidas en Cap. 05 L101 y Cap. 06 L145) en busca del patrón de error "WCB residual"/"remanente retrocedido". Ninguna ocurrencia nueva repite el error; las 6 usan lenguaje fiel al paper. El patrón queda confirmado como completamente resuelto en todo el texto activo. Sin acción.
- `hannachi2023eof` — la cartilla señalaba dos usos genéricos e imprecisos en versiones anteriores (Cap.04 L262, Cap.05 L147) donde se citaba este paper de comparación multi-modelo para respaldar el principio general "el primer modo EOF concentra la mayor varianza" (no es un hallazgo específico de este paper). Verificado: ambas instancias ya citan ahora `hannachi2007empirical` en su lugar, exactamente como recomendaba la cartilla. Sin acción.

**Puntos marcados "verificar contra fuente directa" (no confirmados ni refutados, la cartilla no alcanza a confirmarlos):**
- `coutodesouza2024thesis`, Cap. 02 L74 — "la contribución diabática en SBR se eleva durante el **invierno**, a diferencia de ARG, donde resulta la **menor de las tres regiones en ambas estaciones**" — la cartilla confirma el patrón general (SBR=mixto, ARG=baroclínico clásico) pero no el detalle estacional/ranking específico.
- `coutodesouza2024thesis`, Cap. 02 L80 — "[LPB tiene] la **mayor contribución diabática** entre las tres regiones, de forma consistente en ambas estaciones" — mismo problema, afirmación comparativa específica no confirmada por la cartilla.
- `eisenstein2023identification` — el `.bib` cita el título "Objective identification of sting jets in ERA5..." (Parte 1), pero el `.md` fuente disponible (`papers/files_MD/eisenstein2023identification.md`) corresponde en realidad a la Parte 2 ("...Climatology over Europe"). Ambos artículos comparten la misma clave bib. Ya señalado en la cartilla existente; verificado que las 7 citas activas siguen siendo fieles al contenido real de la Parte 2 disponible, así que no bloquea nada por ahora — pero conviene confirmar antes de la defensa cuál PDF es el efectivamente citado.
- `kaylee2025convection`, Cap. 01 L40 — el `.bib` cita la Parte II de la serie IMPACTS (JAS-D-24-0199.1), pero el `.md` local (`papers/files_MD/kaylee2025convection.md`) es en realidad la Parte I (JAS-D-24-0198.1). La afirmación de la tesis ("convección interna invisible para productos de resolución convencional") es plausible y coherente con la serie, pero no verificable contra el texto real de la Parte II citada (PDF no legible, >20MB). Ya señalado en la cartilla `aporte_autores/02_fajas_transportadoras_WCB_CCB/puntual/kaylee2025convection.txt`; pendiente desde antes de esta sesión. Sugerencia: confirmar cuál PDF hay realmente en `papers/files_PDF/` antes de la defensa.

---

## `andrade2024composite` — Andrade et al. 2024, *Composite Analysis of Explosive Cyclones in the Southern Atlantic Ocean*

**En .bib:** sí.

**Aporta:** compuestos ERA5 (2010–2020, 271 casos) de ciclones explosivos del Atlántico Sur estratificados por intensidad (NDR: débil/moderado/intenso). Hallazgos clave: transición Bjerknes-Solberg → Shapiro-Keyser durante la fase explosiva; **transición de régimen baroclínico a barotrópico al final de la fase explosiva**; dipolo de flujos de calor sensible/latente; núcleo de viento máximo al sureste del centro en sistemas intensos, que migra del lado ecuatorial al polar del jet en altura; trayectorias más restringidas en latitud y menos zonales a mayor intensidad.

**Uso actual (verificado, todas las apariciones activas en versiones `vr`):**
- Cap. 02, L46 — pertinencia de estratificar por intensidad (coherencia de flujos de calor). Bien sustentado.
- Cap. 04, L105 — apoyo genérico a que los flujos de calor sostienen la inestabilidad baroclínica en SBR/LPB. Razonable.
- Cap. 05, L63 — mecanismo de evaporación/condensación que intensifica la circulación. Bien sustentado.
- *(El uso problemático que existía en un borrador anterior de Cap. 06 —desplazamiento de trayectoria hacia el sur, con cifra "56%" no verificable en el artículo— ya fue corregido en la versión activa: `06.vr1` cita ahora `mendes2010climatology, simmonds2000mean` para ese punto específico. Sin acción pendiente ahí.)*

**Oportunidad — reevaluada y resuelta con otro autor:**
- **Ubicación exacta:** Cap. 02 (`02.vr4_fundamentacao.tex`), Sección "Fases del ciclo de vida" (`subsec:tb_fases`), ítem *Decaimiento* (línea 164).
- **Texto original (sin cita):** *"Decaimiento: Fase final marcada por el debilitamiento progresivo del vórtice, debido a la fricción superficial y al cese de la conversión de energía baroclínica una vez que el sistema se ha ocluido completamente o ha entrado en una zona barotrópica."*
- **Por qué se había propuesto este autor:** el paper documenta la transición baroclínico→barotrópico al final de la fase explosiva/decaimiento, y esa oración no tenía respaldo citado.
- **Por qué se descartó al aplicar (a pedido del usuario, comparando ambos autores antes de decidir):** `andrade2024composite` infiere esa transición de forma **cualitativa/estructural** (campos compuestos de MSLP, geopotencial 500 hPa, inclinación de la vaguada en altura, alineamiento vertical superficie-altura), sin calcular términos de energía. En cambio, el ítem anterior de la misma lista (*Intensificación*) ya cita a `coutodesouza2024thesis` por su **análisis energético (Ciclo de Energía de Lorenz)** sobre la misma población regional de ciclones — y ese mismo autor, en su análisis empírico de la fase de decaimiento, encuentra una **reversión de signo del término de conversión baroclínica $C_Z$** (medición directa, no inferencia estructural): *"During the decay phase, ∂A_Z presents significant increases, followed by a reversal in the sign of C_Z compared to previous states."* Se prefirió mantener el mismo tipo de evidencia (energética cuantificada, misma región) que ya usa el resto de la lista, en vez de introducir un tipo de evidencia distinto.
- **Ajuste adicional (a pedido del usuario):** se detectó además que, a diferencia de los otros 3 ítems de la lista (que atan explícitamente cada fase al comportamiento de $\zeta_{850}$: "núcleo de vorticidad", "crecimiento de la vorticidad", "pico de vorticidad"), el ítem de Decaimiento no mencionaba $\zeta_{850}$ en absoluto. Se corrigió para mantener la estructura paralela.
- **Propuesta (versión aplicada):** *"Decaimiento: Fase final marcada por la disminución progresiva de la magnitud de $\zeta_{850}$, reflejo del debilitamiento del vórtice por la fricción superficial y el cese de la conversión de energía baroclínica una vez que el sistema se ha ocluido completamente o ha entrado en una zona barotrópica \citep{coutodesouza2024thesis}."*
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:164`) — con `coutodesouza2024thesis` en lugar de `andrade2024composite`. `andrade2024composite` mantiene sus 3 usos ya verificados en Cap. 02/04/05, sin cambios.

---

## `carlson1980airflow` — Carlson 1980, *Airflow Through Midlatitude Cyclones and the Comma Cloud Pattern*

**En .bib:** sí, pero sin uso en el texto (no citado en ningún capítulo activo).

**Nota técnica:** el `.md`/`.pdf` originales son un escaneo sin capa de texto (OCR ausente). Se transcribió manualmente el contenido completo (12 páginas) leyendo las imágenes renderizadas del PDF y se regeneró `papers/files_MD/carlson1980airflow.md` con el texto íntegro de las 7 secciones y referencias.

**Aporta:** el paper que originó y estableció empíricamente (análisis isentrópico relativo, caso real del 5 dic. 1977) los términos "warm conveyor belt" y "cold conveyor belt" — fuente primaria de la que depende `browning1986conceptual` (que la tesis ya cita extensamente). Define WCB (origen en latitudes bajas, giro anticiclónico sobre el frente cálido, unión al flujo de niveles altos al NE del centro), CCB (flujo anticiclónico de niveles bajos al este del ciclón, asciende rápidamente moviéndose al oeste bajo el WCB, se pliega bajo este cerca de la vaguada) y la "corriente seca" de tres ramas (antecedente directo de la "intrusión seca").

**Oportunidad no aprovechada:**
- **Ubicación exacta:** Cap. 02 (`02.vr4_fundamentacao.tex`), Sección "Estructura interna" → "Modelo conceptual de estructura interna" (~línea 100).
- **Texto actual:** *"...es el modelo de cintas transportadoras \citep{browning1986conceptual} el que explica cómo esa forma se traduce en la distribución de viento y precipitación en superficie..."*
- **Por qué:** Carlson (1980) es la fuente primaria empírica de esta descripción; Browning (1986) es una revisión posterior que la sintetiza.
- **Propuesta (versión aplicada, más sustantiva que el plan original):** en vez de solo agregar la cita, se integró la definición original del WCB que da Carlson (verificada contra el `.md` fuente: *"we will refer to the warm conveyor belt as that air which originated far south of the low in the warm sector, ascended toward the north... and joined the upper-level westerly flow northeast of the low center"*), repartiendo el crédito entre ambos autores según su rol real (Carlson define qué es el WCB; Browning explica cómo esa estructura organiza viento/precipitación en superficie): *"...el WCB, definido originalmente como la corriente ascendente de aire cálido y húmedo que se origina en el sector cálido del ciclón \citep{carlson1980airflow}, y su respectivo chorro de bajo nivel se organizan en torno al vórtice \citep{browning1986conceptual}..."* (sin guiones largos, por preferencia de estilo del usuario para la tesis).
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:102`).

---

## `crespo2020potential` — Crespo et al. 2020/2021, estructuras de vorticidad potencial (PV streamers/cutoffs) forzando ciclogénesis en ARG/Uruguay/SEBrasil

**En .bib:** sí.

**Aporta:** climatología estacional (ERA-Interim, 1979-2017) de estructuras de VP en niveles altos (300-360 hPa) que fuerzan ciclogénesis superficial. **No estudia SALLJ, transporte de humedad ni precipitación** (confirmado explícitamente en su cartilla).

**Uso actual:**
- Cap. 01, L21 — `\citep` genérico en lista de respaldo de "regiones de ciclogénesis documentadas". OK.
- Cap. 04, L40 — "...anomalías de vorticidad potencial en niveles altos durante la ciclogénesis en el este continental \citep{crespo2020potential, gramcianinov2019properties}." OK — coincide exactamente con el tema real del paper.

**ERROR — Cap. 07, L45 (resuelto):**
- **Texto actual:** *"La disponibilidad de humedad tropical canalizada por el SALLJ \citep{crespo2020potential} sostiene la banda enroscada de precipitación con mayor intensidad, incrementando la densidad en el cuadrante sureste..."*
- **Por qué:** esta cita fue puesta aquí como reemplazo de `gramcianinov2024early` en una corrección anterior de esta sesión (que resolvía un problema de fase equivocada), pero el reemplazo introdujo un desajuste de tema — Crespo et al. no trata SALLJ ni humedad de niveles bajos en absoluto.
- **Candidatos descartados:** (1) `gozzo2017climatology` concluye explícitamente que el SALLJ tiene "little contribution" a la humedad de esta región (RG1). (2) `reboita2022from` solo menciona el SALLJ de pasada, citando a otros autores, no como hallazgo propio.
- **Solución encontrada:** `reboita2026meteorology` (ya usado y verificado en Cap. 01 L25 para el mismo mecanismo) declara textualmente: *"the SALLJ increases the transport of moisture and warm air towards southeast SA, influencing rainfall over the La Plata Basin"* — vincula directamente el SALLJ con precipitación en LPB, coincidiendo con la región (SBR/LPB) de la oración de Cap. 07.
- **Propuesta (aplicada, junto con "vórtice"→"sistema" en la oración anterior del mismo párrafo):** *"...con intrusiones secas que penetran hasta el núcleo del sistema y generan la separación más drástica entre cuadrantes \citep{gozzo2013air}. La disponibilidad de humedad tropical canalizada por el SALLJ \citep{reboita2026meteorology} sostiene la banda enroscada de precipitación con mayor intensidad..."*
- **Estado:** ✅ aplicado (`07.vr1_result04_prototipo.tex:45`).

---

## `gozzo2013air` — Gozzo & da Rocha 2013, simulaciones WRF de ciclón Shapiro-Keyser subtropical (may-jun 1997), experimentos FLX vs. NOFLX

**En .bib:** sí. **9 apariciones activas**, 7 OK.

**ERROR — Cap. 02, L125 (confianza alta, verificado contra `.md` fuente directo):**
- **Texto actual:** *"En el Atlántico Sur, \citet{gozzo2013air}... documentaron este mismo patrón [precipitación dirigida por el WCB] en el sector sureste/este..."*
- **Por qué:** el patrón "sureste/este" corresponde específicamente al experimento **NOFLX** (sin flujos de calor — el escenario degradado/no realista del paper). El experimento **FLX** (el válido, comparable a ERA-Interim) se describe de forma distinta ("distributed around the cyclone center, along the warm front and ahead of the cold front", sin esa etiqueta de cuadrante). La tesis presenta el patrón del experimento degradado como si fuera el hallazgo general.
- **Propuesta (versión aplicada, reenfocada en humedad→ubicación de la lluvia a pedido del usuario, quitando `vera2002cold` y `pepler2020dimensional` de esta oración por estar fuera de foco):** *"En el Atlántico Sur, \citet{gozzo2013air} documentaron que la disponibilidad de humedad superficial condiciona directamente la ubicación de la precipitación: con flujos de calor activos, esta se distribuye ampliamente en torno al centro del ciclón y el frente cálido, mientras que su ausencia la debilita y concentra en el sector sureste/este del sistema."* Verificado antes de aplicar que el enfoque de Gozzo & da Rocha para "frente cálido"/sector es sinóptico-euleriano (fronteras diagnosticadas sobre los campos simulados, más una caja fija 20°×20° centrada en el ciclón para promediar flujos) — no lagrangiano; el elemento lagrangiano del paper (ecuaciones de Neiman & Shapiro) se usa para otra cosa (balance de humedad de parcelas), no para definir el frente/sector. `vera2002cold` no aporta a esta afirmación (no hace compositing centrado en ciclón) y quedó fuera de esta oración, pero sigue bien citado en sus otros 4 usos. `pepler2020dimensional` (relámpagos, ciclones profundos/superficiales) se retiró de aquí por decisión editorial del usuario (fuera de foco para el capítulo), pero sigue citado correctamente en Cap.01 L37.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:127`).

**MATIZ — Cap. 01, L38:** "los estudios de caso de gozzo2013air... han revelado... que los ciclones regionales pueden exhibir evoluciones que se apartan de los modelos tradicionales" — encuadre impreciso: con flujos activos (FLX) el ciclón SIGUE el modelo Shapiro-Keyser consistentemente con ERA-Interim; es la ausencia de flujos (NOFLX) la que lo degrada. No es error grave, prioridad baja.

---

## `gramcianinov2019properties` — climatología de ciclones del Atlántico Sur (NCEP-CFSR, no ERA5), define 4 regiones de génesis (tesis adopta 3)

**En .bib:** sí. *(Nota: lista de autores del .bib no coincide con los 3 autores reales del paper — posible copia de otra entrada bib, revisar aparte.)*

**ERROR grave — Cap. 03 (Métodos), L30, y `tabelas_es/tab_tracking_params.tex`:**
- **Texto actual:** *"El punto de partida es el catálogo de trayectorias desarrollado por \citet{gramcianinov2019properties} **a partir de ERA5**..."* — la tabla de parámetros de tracking repite "Fuente de datos: ERA5 (ECMWF)" bajo la misma cita.
- **Por qué:** el paper real usa **NCEP-CFSR (1979-2010, ~38 km)**, no ERA5. Es una afirmación metodológica fundacional del Cap. 03, incorrecta.
- **Propuesta (versión aplicada, corregida dos veces):** primer intento: se rastreó la cadena de procedencia vía la cartilla de `coutodesouza2024new`, que confirma textualmente ser "la fuente directa de la base de datos de trayectorias" de la tesis, y se cambió la cita de L30/tabla a `coutodesouza2024new`. **Corrección posterior (a pedido del usuario, que recordaba correctamente el detalle):** se verificó el paper `gramcianinov2020analysis` directamente y se confirmó que es *ese* paper el que efectivamente construye la base de datos ("the last important contribution of this work is to produce a cyclone database", con K.I. Hodges —creador del algoritmo TRACK— como coautor) sobre la cual `coutodesouza2024new` aplica después la segmentación en fases (la oración siguiente, L35, ya decía correctamente "Sobre esta base, Couto de Souza et al. incorporan..."). Se corrigió la cita de L30 y de la tabla de `coutodesouza2024new` a `gramcianinov2020analysis`, que es la atribución correcta y más precisa. `gramcianinov2019properties` sigue sin perder su cita real (regionalización SBR/LPB/ARG, L46, sin cambios).
- **Estado:** ✅ aplicado (`03.vr3_metodos.tex:30` → `gramcianinov2020analysis`; `tabelas_es/tab_tracking_params.tex:3` → `gramcianinov2020analysis`).

**MATIZ — Cap. 06, L152 (resuelto durante la revisión de lógica de resultados, Pasada 2):** "...la interacción con el SALLJ \citep{gramcianinov2019properties} generan las oclusiones más rápidas [en SBR/LPB]" — el paper no vincula SALLJ con velocidad de oclusión (describe génesis, no oclusión); la región de mayor actividad de oclusión en el dominio completo es SE-SAO (oceánica) y cerca de la Antártida, no SBR/LPB. El SALLJ solo se menciona como fuente de humedad en el momento de la génesis en LPB. **Propuesta (aplicada):** se retiró la cita de `gramcianinov2019properties` para esta afirmación, manteniendo el argumento de fondo (mayor contribución diabática en SBR/LPB) respaldado por `gozzo2013air` y `coutodesouza2024thesis`, ya establecidos para ese punto en Cap. 02: *"En SBR y LPB, la disponibilidad de flujos de calor latente oceánico \citep{gozzo2013air, coutodesouza2024thesis} genera las oclusiones más rápidas..."*
- **Estado:** ✅ aplicado (`06.vr1_result03_meof.tex:152`).

---

## `gramcianinov2020analysis` — Gramcianinov et al. 2020, creación de la base de trayectorias del Atlántico (ERA5 + TRACK de Hodges) e intercomparación vs. CFSR/CFSv2

**En .bib:** sí. 6 apariciones tras esta fase de aplicación (incluye la nueva atribución del catálogo de trayectorias en L30 del propio Cap.03, ver entrada de `gramcianinov2019properties`), mayoría OK.

**MATIZ — Cap. 03, L13:** *"...su representación superior de la intensidad ciclónica... frente a reanálisis previos \citep{gramcianinov2020analysis}"* — en los percentiles superiores (90/95) es en realidad **CFSR/CFSv2, no ERA5**, quien reporta vientos más intensos; la ventaja real de ERA5 es resolución/densidad de trayectorias/estructuras de mesoescala, no magnitud reportada. Parcialmente mitigado porque la oración siguiente (`chen2024evaluation`) ya reconoce el sesgo bajo de ERA5 en extremos, pero la palabra "superior" puede confundir.
- **Propuesta (versión aplicada, también se quitó la mención "se presenta en la Introducción" por indicación del usuario, y los guiones largos):** *"La justificación de ERA5, resolución espacial ($\sim$31 km) y temporal (horaria), y su mayor densidad de trayectorias y representación de estructuras de mesoescala frente a reanálisis previos \citep{gramcianinov2020analysis}, es la base de la elección de este reanálisis para el catálogo de trayectorias."*
- **Estado:** ✅ aplicado (`03.vr3_metodos.tex:13`).

---

## `han2025system` — marco SyCLoPS (System for Classification of Low-Pressure Systems), clasificación global de sistemas de baja presión

**En .bib:** sí. 4 apariciones.

**MATIZ — Cap. 02, L186 (revisado durante la fase de aplicación):** le atribuía a `han2025system` la técnica de "compositing centrado en el sistema" cuando esa técnica es el aporte específico de `priestley2022improved` (citado en la misma oración); el aporte real de Han es la clasificación taxonómica y contribución fraccional de precipitación por clase de sistema.
- **Propuesta original:** *"Su validez metodológica fue demostrada por \citet{priestley2022improved}, quienes aplicaron compositing para aislar estructuras representativas, en línea con marcos de clasificación objetiva recientes como el de \citet{han2025system}, que vinculan explícitamente la evolución del ciclo de vida de un sistema con su contribución de precipitación y viento."*
- **Resolución:** al revisar el archivo durante la fase de aplicación, el texto real ya no coincidía con lo flagged originalmente — ya reparte el crédito razonablemente (Priestley = compositing, Han = hallazgo de que los campos extremos cambian de ubicación/extensión según la fase del ciclo de vida). El usuario decidió dejarlo como está, sin aplicar la propuesta original.
- **Estado:** ✅ revisado, sin cambios (el texto actual ya es adecuado).

**ERROR doble — Cap. 07, L68 (resuelto):**
- **Texto actual:** *"...marco de clasificación denominado \textit{SyCLoPS} (\textit{System Lifecycle of Precipitating Storms}) para el Hemisferio Norte..."*
- **Error 1:** acrónimo mal expandido — el nombre real es *"System for Classification of Low-Pressure Systems"*, no "System Lifecycle of Precipitating Storms" (ni siquiera coinciden las letras con SyCLoPS).
- **Error 2:** el paper es **global**, no restringido al Hemisferio Norte.
- **Error 3 (detectado al revisar con el usuario, no en la auditoría original):** el párrafo también afirmaba que la diferencia fundamental con los prototipos de la tesis era que Han "describe cualitativamente" mientras la tesis "cuantifica" — verificado contra el paper (`han2025system.md`): SyCLoPS sí cuantifica extensamente (16 parámetros por sistema, composites de corte vertical por clase, accuracy scores, contribución de precipitación/viento por clase). La diferencia real no es cuantificar vs. no cuantificar, sino el método: composites por clase discreta (Han) vs. EOF + densidad de probabilidad espacial en dominio lagrangiano (tesis).
- **Propuesta (versión aplicada, reformulada varias veces a pedido del usuario):** se retiró la explicación del acrónimo/nombre completo (no es necesaria), se reformuló para presentar primero la idea general de Han (los ETC tienen características estructurales particulares según la fase de desarrollo del sistema, relación no lineal entre fases) y luego encuadrar SyCLoPS como uno de varios esfuerzos de caracterización a nivel global de los cuales la tesis "no se distancia en el objetivo sino en la metodología de cuantificación" (sin oponerse a ellos). Se eliminaron los dos puntos (":") por preferencia de estilo del usuario, y "sistemas de alta vorticidad" se cambió a "sistemas intensos ($\zeta_{850}$)". Texto aplicado: *"...\citet{han2025system} señalan que los ciclones extratropicales presentan características estructurales particulares según la fase de desarrollo del sistema, y que esta relación no es lineal entre fases, motivando su marco de clasificación \textit{SyCLoPS}, de alcance global, diseñado para estudiar la frecuencia, estructura y contribución de precipitación y viento de cada tipo de sistema a lo largo de su ciclo de vida. Esta caracterización de los ETC reúne distintos esfuerzos recientes a nivel global, de los cuales el presente trabajo no se distancia en el objetivo sino en la metodología de cuantificación, ya que mientras SyCLoPS caracteriza cada clase mediante composites de corte vertical y parámetros escalares de clasificación, los prototipos aquí presentados cuantifican la arquitectura del sistema en un dominio lagrangiano estandarizado mediante la superposición de densidades de probabilidad espacial y modos dominantes de variabilidad (EOF)..."*
- **Estado:** ✅ aplicado (`07.vr1_result04_prototipo.tex:68`). Cap. 02, L188 sigue sin cambios (ver arriba, ya revisado y confirmado adecuado por el usuario).

---

## `hoskins2005new` — climatología storm tracks HS (ampliación, 4 usos previamente no verificados individualmente)

Los 4 usos nuevos revisados (Cap. 01 L9, Cap. 02 L10/L38/L86) están OK. Ver oportunidad:

**Oportunidad no aprovechada:**
- **Ubicación exacta:** Cap. 04 (`04.vr2_result01_w10.tex`), línea 143 (misma oración ya evaluada como "genérica/defendible" antes en esta sesión).
- **Por qué:** el paper aporta una cifra cuantitativa concreta (75% de eventos de ciclogénesis en superficie en Sudamérica con contraparte ciclónica contemporánea a 500 hPa, 61% de esos al oeste) que fortalecería la afirmación genérica actual sobre "acoplamiento baroclínico".
- **Propuesta (versión aplicada, reformulada tras revisar qué resultado propio explica realmente):** la cifra de Hoskins es sobre el momento de la **génesis**, pero el resultado que la oración explica (consolidación del dipolo de EOF1) ocurre hacia la **madurez** — se reformuló para tender el puente explícito entre ambos momentos, dejando claro que el vínculo génesis→consolidación en madurez es interpretación propia de la tesis, no un hallazgo textual de Hoskins/Dossantos: *"Según \citet{hoskins2005new}, hasta el 75\% de los eventos de ciclogénesis en superficie en Sudamérica ya presentan una contraparte ciclónica contemporánea a 500 hPa. Este acoplamiento baroclínico, consistente con \citet{dossantos2023response}, se refleja aquí en el fortalecimiento progresivo del dipolo de EOF1 hasta la madurez, cuando el sistema expande su campo de viento en superficie en respuesta a la posición del chorro en altura, expansión que \citet{simmonds2000size} documentan como un aumento sistemático del radio ciclónico durante el desarrollo."*
- **Estado:** ✅ aplicado (`04.vr2_result01_w10.tex:143`).

---

## `hyeok2024extrem` — mecanismo de downdrafts, transporte de momento hacia la capa límite (HN, Atlántico Norte)

**En .bib:** sí. 2 usos activos en Cap. 04, ambos OK (genéricos, sin cuadrante).

**Oportunidad no aprovechada:**
- **Ubicación exacta:** Cap. 04 (`04.vr2_result01_w10.tex`), línea 101, mismo párrafo donde ya se cita de forma genérica.
- **Por qué:** el paper reporta que los downdrafts son ~15% más frecuentes al **suroeste** del centro en el HN. Con la regla de espejo N↔S: suroeste (HN) → **noroeste** (HS) — coincide exactamente con la hiperconcentración de viento p90 en el cuadrante noroeste que la tesis ya documenta. Cita cuantitativa lista para reforzar el argumento.
- **Propuesta:** *"...transportan momento horizontal de la alta troposfera hacia la capa límite, con una frecuencia hasta 15\% mayor en el sector suroeste del ciclón en climatologías del Hemisferio Norte, que por inversión hemisférica corresponde al noroeste austral aquí documentado \citep{hyeok2024extrem}."* (sin guiones largos, por preferencia de estilo del usuario).
- **Estado:** ✅ aplicado (`04.vr2_result01_w10.tex:101`).

---

## `inatsu2004zonal` — mismo problema de Cap. 04 (ya corregido), sin corregir en Cap. 02

**ERROR — Cap. 02, L11:**
- **Texto actual:** *"\citet{inatsu2004zonal} demostraron que la asimetría zonal del storm track está **forzada por la topografía de los Andes**..."*
- **Por qué:** invierte la jerarquía real del paper — el forzante primario son las ondas estacionarias excitadas por TSM (tropical y de latitudes medias); la topografía andina es un modulador secundario (removerla solo debilita, no elimina, el storm track). Es el mismo error que ya se corrigió en Cap. 04 L145 ("flujo estacionario de latitudes medias" → "ondas estacionarias troposféricas") pero que nunca se tocó aquí.
- **Propuesta (versión aplicada, coordinada con `vera2002cold` en la misma oración):** *"...mientras que \citet{inatsu2004zonal} demostraron que la asimetría zonal del storm track está organizada por ondas estacionarias troposféricas, moduladas regionalmente por la topografía de los Andes, cuya interacción con el flujo de niveles bajos también favorece la propagación de ondas baroclínicas sobre el subcontinente sudamericano \citep{vera2002cold}."* — se eliminó la cláusula final sobreextendida de `vera2002cold` ("define regiones preferenciales de desarrollo en latitudes extratropicales") y se dejó una contribución genérica que sí es fiel a su hallazgo real.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:11`).

---

## `coutodesouza2024new` — base de datos de trayectorias + CycloPhaser (segmentación objetiva de fases)

**En .bib:** sí.

**Aporta:** paquete CycloPhaser (segmentación objetiva de 4 fases vía picos/valles de ζ₈₅₀ y su derivada), aplicado a la base de trayectorias del Atlántico Sur 1979-2020; climatología de duración/desplazamiento/velocidad de fases y densidad de trayectorias por región.

**Uso actual (6 apariciones):** todas OK — Cap. 01 (L53, L61), Cap. 02 (L31, L53, L147), Cap. 03 (L35).

**Oportunidad aplicada:**
- **Ubicación exacta:** Cap. 02 (`02.vr4_fundamentacao.tex`), Sección "Estratificación..." (`subsec:tb_poblaciones`), párrafo "Homogeneidad evolutiva: ciclo de vida completo" (línea 53).
- **Texto original (sin cita):** *"Para que el análisis por fases sea consistente, los ciclones seleccionados deben presentar un ciclo de vida completo, la secuencia de las cuatro fases evolutivas (Sección~\ref{subsec:tb_fases}), sin fases secundarias ni re-intensificaciones que introduzcan ruido en los promedios."*
- **Por qué:** el paper reporta el dato que sustenta directamente este criterio: de 39 tipos de ciclo de vida detectados, la configuración de 4 fases completas es la más común pero representa solo ~60% de los ~28,458 sistemas analizados.
- **Propuesta (versión aplicada, oración completa):** *"Para que el análisis por fases sea consistente, los ciclones seleccionados deben presentar un ciclo de vida completo, la secuencia de las cuatro fases evolutivas (Sección~\ref{subsec:tb_fases}), sin fases secundarias ni re-intensificaciones que introduzcan ruido en los promedios, criterio que retiene aproximadamente el 60\% de los sistemas detectados en la región \citep{coutodesouza2024new}."*
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:53`).
- **Nota adicional sin desarrollar:** el paper también reporta diferencias estacionales de densidad de génesis por región (ARG similar DJF/JJA; LPB más activa en JJA; SBR más activa en DJF) no citadas en la Sección "Regiones de ciclogénesis" — posible segunda oportunidad, no evaluada en detalle.

---

## `marrafon2022classificacao` — Marrafon et al. 2022, clasificación de ciclones extratropicales/subtropicales/TT en proyecciones RegCM4 (Atlántico Sur, RCP8.5)

**En .bib:** sí.

**Aporta:** clasifica ciclones extratropicales/subtropicales/tropicales y transiciones tropicales sobre el Atlántico Sur en proyecciones RegCM4+MCGs (RCP8.5, 1979-2080), con el algoritmo de tracking de Reboita et al. (2010) (ζ₉₂₅) y Cyclone Phase Space (Hart 2003). Proyecta reducción de frecuencia de ciclones extratropicales hacia 2080, con invierno como estación más ciclogenética (consistente con Gan & Rao 1991; Reboita 2015/2018a). Documenta el caso Catarina (2004) como TT vía CPS.

**Uso actual:** no usado — sin `\citet`/`\citep{marrafon2022classificacao}` en ningún capítulo activo.

**Oportunidad 1 — descartada durante la fase de aplicación:**
- **Ubicación exacta (original):** Cap. 03 (Métodos), donde se describe el algoritmo de tracking (se creía que compartía linaje con Reboita et al. 2010, igual que el método de esta tesis).
- **Por qué se descartó:** al aplicar la corrección de `gramcianinov2019properties`/`gramcianinov2020analysis` en este mismo capítulo, se confirmó que el algoritmo real de la tesis es **TRACK de Hodges sobre ζ₈₅₀** (`gramcianinov2020analysis`), no el de Reboita et al. 2010 (ζ₉₂₅, vecino más próximo) que usa `marrafon2022classificacao` — son linajes metodológicos distintos. Aplicar la oportunidad tal como estaba planteada habría afirmado un parentesco metodológico falso.
- **Verificación adicional (a pedido del usuario):** se revisó el abstract/introducción completo del paper buscando (a) contenido sobre distribución espacial de variables relativa al centro del ciclón, o (b) justificación/motivación sobre la importancia de estudiar esa distribución — no tiene ninguno de los dos; su alcance se limita a clasificación de tipos de ciclones (extratropical/subtropical/tropical, transiciones tropicales) y proyecciones de frecuencia futura por tipo.
- **Estado:** ⛔ cerrado sin aplicar — no se encontró ningún ángulo de uso real para este autor en la tesis (ni tracking, ni estacionalidad —Oportunidad 2, diferida por decisión previa del usuario—, ni distribución espacial/justificación).

**Oportunidad 2 no aprovechada:**
- **Ubicación exacta:** Cap. 02 (Fundamentación), al describir la estacionalidad de ciclones extratropicales en el Atlántico Sur (invierno como pico), junto a Reboita 2015/2018a.
- **Por qué:** Marrafon et al. reproduce ese mismo patrón en proyecciones futuras y reporta tendencia de disminución de frecuencia hacia fin de siglo — dato relevante si en algún punto se discute cambio climático/proyecciones futuras.
- **Candidatos de ubicación evaluados durante la fase de aplicación:** (a) Cap.01 L13, junto a `gan1991surface` (estacionalidad invernal); (b) junto a la oración de motivación climática de Cap.01 L48-49 (`kodama2019perspective`+`simmonds2000variability`, ya aplicada).
- **Estado:** ⏸️ diferida por decisión del usuario — queda sin aplicar por ahora, prioridad baja.

---

## `IPCC2021_WG1_Chapter11_Extremes` — Seneviratne et al. 2021, IPCC AR6 WG1 Cap. 11 (eventos extremos)

**En .bib:** sí (`tex_es/bibliografia.bib:1109`).

**Aporta:** Sección 11.7.2 (Extratropical Storms): proyecciones CMIP5/Chang 2017 (RCP8.5, 26 modelos) de aumento de 20-50% en ciclones extratropicales *extremos* del HS hacia fin de siglo (según métrica de intensidad), con "high confidence" de que el desplazamiento hacia el polo del storm track del HS está ligado a actividad humana (principalmente sustancias que agotan el ozono); aumento proyectado de ~7%/°C en precipitación asociada a ETCs.

**Uso actual:** no usado — está en el `.bib` pero nunca citado en ningún capítulo activo.

**Oportunidad no aprovechada:**
- **Ubicación exacta:** Cap. 01 (Introducción), párrafo de motivación del estudio.
- **Propuesta:** *"Este interés se ve reforzado por las proyecciones climáticas: el IPCC \citep{IPCC2021_WG1_Chapter11_Extremes} reporta que, bajo escenarios de altas emisiones (RCP8.5), el número de ciclones extratropicales extremos en el Hemisferio Sur podría aumentar entre un 20\% y un 50\% hacia fines de siglo, con alta confianza en que el desplazamiento hacia el polo de las trayectorias de tormentas (\textit{storm tracks}) en el Hemisferio Sur está vinculado a la actividad humana."*
- **Estado:** ⛔ cerrado sin aplicar — decisión del usuario. El párrafo de motivación climática de Cap.01 ya quedó cubierto con `kodama2019perspective` + `simmonds2000variability` (arco pasado→futuro); el usuario decidió no sumar esta cita adicional para no sobrecargar el párrafo.

---

## `naud2025lifecycle` — Naud et al. 2025, precipitación en ciclones ocluidos vs. no ocluidos (HN, IMERG)

**En .bib:** sí. 2 usos activos (Cap. 02 L109, Cap. 05 L97).

**Oportunidad menor — reformulada tras discusión con el usuario (más relevante que la propuesta original):**
- **Ubicación exacta:** Cap. 05 (`05.vr2_result02_tp.tex`), línea 97, mismo párrafo ya citado.
- **Primera propuesta (descartada por el usuario):** agregar la cifra del 42% de exceso de precipitación en ciclones ocluidos vs. no ocluidos (comparación entre dos grupos). **Por qué se descartó:** la Población Global de la tesis exige ciclo de vida completo (las 4 fases, incluyendo Decaimiento) como criterio de selección — no existe un grupo de "no ocluidos" con el que comparar, por lo que una cifra basada en esa comparación no encaja con el diseño muestral de la tesis.
- **Alternativa mejor identificada en el mismo paper:** en vez del hallazgo comparativo (ocluidos vs. no ocluidos), se usó un hallazgo **descriptivo** de la estructura interna de los ciclones ocluidos, que no requiere grupo de comparación y encaja con una población que llega completa a la oclusión: *"Cyclones that occlude develop a characteristic thermal ridge that connects the SLP minimum to the peak of the warm sector... the observed mean precipitation in 162 NH occluded cyclones... is maximized in the thermal ridge region."* Este mecanismo (cresta térmica) es esencialmente el mismo *trowal* que ya cita `martin1999forcing` más adelante en el mismo párrafo — de hecho, el propio Naud et al. citan a J. Martin (1999b) como el origen de este mecanismo.
- **Ajustes adicionales a pedido del usuario:** se evitó mencionar "presión"/"mínimo de presión" (inconsistente con el marco de vorticidad de la tesis), usando en su lugar "centro del sistema"; se añadió la aclaración "para el Hemisferio Norte", ausente en el texto original, siguiendo el patrón de espejo hemisférico que se usa consistentemente en el resto de la tesis (p. ej. Cap. 04 con `hyeok2024extrem`).
- **Propuesta (versión aplicada):** *"Según \citet{naud2025lifecycle} para el Hemisferio Norte, los ciclones ocluidos desarrollan una cresta térmica que conecta el centro del sistema con el vértice del sector cálido, donde se maximiza la precipitación mediante un forzante de ascenso propio en la periferia."*
- **Estado:** ✅ aplicado (`05.vr2_result02_tp.tex:97`).

---

## `masson2022tendencias` — Masson-Delmotte & Zhai 2022, Boletín OMM (versión en español del IPCC AR6 WG1)

**En .bib:** sí.

**Aporta:** versión de divulgación en español del mismo contenido del Cap. 11 del IPCC AR6 WG1 (firmado por los copresidentes del GTI). Relevante: Figura 5 documenta cambios de velocidad de viento tras el desplazamiento hacia los polos de las trayectorias de ciclones extratropicales; "intensificación de ciclones tropicales o tormentas extratropicales (confianza media)" entre los cambios regionales proyectados.

**Uso actual:** no usado.

**Oportunidad no aprovechada:**
- **Ubicación exacta:** Cap. 01 (Introducción), párrafo de motivación climática — mismo punto que la oportunidad de `IPCC2021_WG1_Chapter11_Extremes` (ambas citan el mismo informe; son complementarias — español vs. inglés — no independientes; decidir si usar una, otra, o ambas juntas).
- **Propuesta:** *"...con niveles de confianza medios respecto a la intensificación de ciclones extratropicales y cambios en la velocidad del viento asociados al desplazamiento hacia los polos de sus trayectorias \citep{masson2022tendencias}."*
- **Estado:** ⛔ cerrado sin aplicar — misma decisión que `IPCC2021_WG1_Chapter11_Extremes` (ver esa entrada): el párrafo de motivación climática ya quedó cubierto con `kodama2019perspective` + `simmonds2000variability`.

---

## `miranda2026patterns` — Miranda et al. 2026, tormentas costeras de alto impacto en el litoral sur de Brasil

**En .bib:** sí.

**Aporta:** estudio observacional (avisos CHM + ERA5, 2001-2020) de 51 tormentas costeras de alto impacto en Rio Grande do Sul ("Zona Alfa"). Un sistema de baja presión en 40-45°S (EOF1 de MSLP) domina la señal; oleaje >4 m dirección SE; 355 h de inoperatividad portuaria en Rio Grande (2007-2016).

**MATIZ — Cap. 01, L49:**
- **Texto actual:** *"...mientras que \citet{miranda2026patterns} confirman que estos sistemas son los principales motores de tormentas costeras en el Atlántico Sur..."*
- **Por qué:** el estudio está acotado al litoral sur de Brasil ("Zona Alfa"), no al Atlántico Sur en su conjunto; generalizar amplía el alcance geográfico más allá de lo sustentado.
- **Propuesta:** *"...mientras que \citet{miranda2026patterns} confirman que estos sistemas son los principales motores de tormentas costeras en el litoral sur de Brasil..."*
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:49`).

---

## `jones1993climatology` — Jones & Simmonds 1993, climatología objetiva de ciclones del HS

**En .bib:** sí.

**Aporta:** climatología (1975-89, Bureau of Meteorology) que muestra un núcleo circumpolar de alta latitud (55-70°S) dominante, más dos bandas secundarias de latitudes medias: una principal Pacífico (Tasman Sea→Drake Passage) y **una segunda, "less developed"**, del Gran Chaco sudamericano hacia el Atlántico Sur.

**MATIZ — Cap. 01, L14:**
- **Texto actual:** *"Poco después, la climatología hemisférica de \citet{jones1993climatology} confirmó a mayor escala esta señal al situar a la región sudamericana entre las de mayor densidad ciclónica del HS."*
- **Por qué:** el paper describe esa banda explícitamente como "second, less developed" (menos desarrollada que la del Pacífico), no entre los máximos de mayor densidad absoluta del hemisferio (esos son el núcleo circumpolar y los máximos sur de África/Índico Sur/Ross Sea Este). "Entre las de mayor densidad" sobrestatúa el ranking relativo real.
- **Propuesta (versión aplicada, ajustada en conjunto con el usuario para evitar encuadrar la región como "secundaria" y en su lugar contrastar extratropical vs. polar):** *"Poco después, la climatología hemisférica de \citet{jones1993climatology} confirmó a mayor escala esta señal, identificando a la región sudamericana como un núcleo de densidad ciclónica propio de las latitudes extratropicales, distinto de las concentraciones mayores en latitudes cercanas al polo."*
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:14`).

---

## `kodama2019perspective` — Kodama et al. 2019, precipitación de ciclones oceánicos intensos HN vs. HS (NICAM, GSMaP-GPM)

**En .bib:** sí. Único uso activo (Cap. 02, `02.vr4_fundamentacao.tex:117`) es **OK** — cifras exactas (7.7 vs. 10.7 mm/día) y atribución causal (menor disponibilidad de humedad, no dinámica distinta) fieles al paper; confirmado también por la cartilla.

**Oportunidad menor (opcional, prioridad baja):**
- **Ubicación exacta:** Cap. 01 (Introducción), párrafo de motivación climática (Bloque 3).
- **Por qué:** el paper también reporta un escalamiento ~7%/K (tipo Clausius-Clapeyron) de la precipitación ciclónica con el calentamiento futuro, dato no usado que reforzaría el mismo argumento de intensificación futura.
- **Decisión del usuario:** de las 4 oportunidades propuestas para este párrafo (`IPCC2021_WG1_Chapter11_Extremes`, `masson2022tendencias`, `kodama2019perspective`, `simmonds2000variability`), el usuario eligió aplicar solo `kodama2019perspective` + `simmonds2000variability`, combinadas en una sola oración con arco pasado→futuro (tendencia histórica observada + proyección física futura), sin las otras dos (para no sobrecargar el párrafo).
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:49`, oración nueva insertada tras la cita de `sasaki2021intraseasonal`): *"Esta amenaza no es estática: los registros históricos de 40 años ya muestran una tendencia significativa hacia ciclones de mayor tamaño e intensidad en el HS \citep{simmonds2000variability}, tendencia que las proyecciones de calentamiento futuro sugieren se profundizará específicamente en la componente de precipitación, con una tasa de escalamiento cercana al 7\%/K \citep{kodama2019perspective}."*

---

## `laurila2021characteristics` — Laurila et al. 2021, climatología lagrangiana de ciclones/windstorms del norte de Europa (ERA5, ensemble sensitivity)

**En .bib:** sí. 3 usos activos, 2 OK (Cap. 02 L26 metodología, Cap. 04 L97 migración de racha al sector posterior tras el frente frío).

**ERROR — Cap. 05, L35 (resuelto):**
- **Texto original:** *"\citet{laurila2021characteristics} señalan que los sistemas que terminan generando vientos y lluvias de mayor magnitud poseen firmas dinámicas distinguibles desde etapas iniciales, aunque la predictibilidad de la precipitación máxima suele ser menor que la del viento por su naturaleza intermitente."*
- **Por qué:** el paper no estudia precipitación en absoluto (ni como variable de respuesta ni como precursor comparado). La única comparación de predictibilidad real es entre MSLP mínima y racha máxima de viento (MSLP más predecible), y entre estación fría vs. cálida — no entre viento y precipitación.
- **Primera propuesta (descartada):** comparar viento vs. MSLP en vez de viento vs. precipitación — el usuario indicó que no le sirve introducir MSLP en este punto del párrafo.
- **Propuesta (versión aplicada):** en vez de cambiar el eje de la comparación, se limitó `laurila2021characteristics` a lo que sí estudia (viento, no lluvia) y se reasignó la cláusula de predictibilidad/intermitencia de la precipitación a `oertel2021warm`, ya usado y verificado en este mismo capítulo (L123) para exactamente ese concepto ("naturaleza discontinua de la precipitación... gobernada por la actividad frontal, los núcleos de convección embebida"): *"\citet{laurila2021characteristics} señalan que los sistemas que terminan generando las rachas de viento más intensas poseen firmas dinámicas distinguibles desde etapas iniciales, mientras que la predictibilidad de la precipitación máxima resulta menor debido a su naturaleza intermitente, gobernada por la actividad frontal y la convección embebida \citep{oertel2021warm}."*
- **Estado:** ✅ aplicado (`05.vr2_result02_tp.tex:35`).

---

## `mcerlich2023extremes` — McErlich et al. 2023, compuestos ciclón-centrados de precipitación extrema por fase (ERA5, HS completo)

**En .bib:** sí. 2 usos activos, ambos OK (Cap. 02 L119 rotación horaria de la coma de precipitación —verificada explícitamente como ciclónica en el HS por el propio paper—, Cap. 05 L47 contracción espacial de extremos).

**Oportunidad menor (opcional, prioridad baja) — aplicada:**
- **Ubicación exacta:** Cap. 05 (`05.vr2_result02_tp.tex`), mismo párrafo donde ya se citaba a este autor.
- **Por qué:** el paper aporta cifras exactas (caída a 46%/30% en ocurrencia sobre el percentil 90/98 **de magnitud de precipitación** hacia el resto del ciclo de vida; hasta 80% de la precipitación total de los compuestos ciclón-centrados proviene del decil superior de la distribución) que reforzarían cuantitativamente la afirmación cualitativa ya presente.
- **Aclaración importante hecha al usuario antes de aplicar:** el "percentil 90"/"98" de este paper es un **umbral de magnitud de precipitación** dentro de los compuestos ciclón-centrados (cuánto de la precipitación en la grilla supera ese percentil), **no** el mismo concepto que el subconjunto "p90" de la tesis (estratificación de ciclones por vorticidad). Se evitó deliberadamente escribir "p90"/"p98" en la oración para no generar esa confusión terminológica.
- **Propuesta (versión aplicada, sin guiones largos, sin el dato del percentil 98, acortada a pedido del usuario):** *"Esto coincide con \citet{mcerlich2023extremes}, quienes muestran para el Hemisferio Sur que la precipitación más intensa ocurre en la profundización previa al pico de intensidad, concentrando hasta el 80\% de la precipitación total de los compuestos ciclón-centrados, con una ocurrencia que cae al 46\% de ese máximo hacia el resto del ciclo de vida."*
- **Estado:** ✅ aplicado (`05.vr2_result02_tp.tex`, mismo párrafo).

---

## `mendes2010climatology` — Mendes et al. 2010, climatología de 25 años de ciclones del sector sudamericano (NCEP/NCAR II)

**En .bib:** sí. 3 usos activos, 2 OK (Cap. 02 L88 clustering de trayectorias, Cap. 05 L77 frecuencia ~18 eventos/invierno).

**MATIZ — Cap. 06, L33 (resuelto):**
- **Texto actual:** *"los ciclones más intensos del Atlántico Sudoccidental desplazan su trayectoria preferencialmente hacia el sureste y el océano abierto a medida que profundizan \citep{mendes2010climatology, simmonds2000mean}"*
- **Por qué:** el paper no establece una correlación intensidad/profundización↔trayectoria SE — su clustering de trayectorias es independiente de la intensidad, y su propio análisis de tasas de profundización indica explícitamente que **no difieren significativamente** entre el sector sudamericano y el resto del HS. La cita respalda el rumbo SE general, no la relación "más intensos... a medida que profundizan" que el texto le atribuye. **Confirmado además con `simmonds2000mean`** (co-citado en la misma oración): tampoco vincula intensidad/profundización con dirección de desplazamiento — documenta el eje de sistemas más intensos en una banda zonalmente simétrica cerca de 55°S, y transporte general hacia el este/sureste como comportamiento climatológico de fondo, no correlacionado con intensidad individual. Ninguna de las dos citas respalda la cláusula "a medida que profundizan".
- **Propuesta (aplicada):** *"los ciclones del Atlántico Sudoccidental desplazan su trayectoria preferencialmente hacia el sureste y el océano abierto \citep{mendes2010climatology, simmonds2000mean}"* (sin condicionar a intensidad/profundización).
- **Estado:** ✅ aplicado (`06.vr1_result03_meof.tex:33`).

---

## `neu2013intercomparison` — Neu et al. 2013, IMILAST (intercomparación de 15 algoritmos de tracking, ERA-Interim)

**En .bib:** sí. Única ocurrencia activa, Cap. 01 L41.

**ERROR (parte final de la oración) — Cap. 01, L41:**
- **Texto actual:** *"...\citet{neu2013intercomparison} señalan que la variabilidad en forma y tamaño de los ETC genera divergencias sistemáticas entre métodos de detección, particularmente pronunciadas en regiones de topografía compleja como el Atlántico Sur."*
- **Por qué:** la primera parte es fiel, pero el paper nunca menciona Sudamérica, los Andes ni el Atlántico Sur en relación con topografía — sus ejemplos de divergencia por topografía compleja son zonas montañosas continentales y, específicamente, el Mediterráneo (HN). El Atlántico Sur es una cuenca oceánica sin orografía; de hecho, el único pasaje del paper sobre esa región (sector Atlántico 40-50°S) la describe como zona de **buena concordancia** entre métodos, no de divergencia.
- **Propuesta (versión aplicada, simplificada a pedido del usuario — sin agregar el ejemplo del Mediterráneo, solo quitando la atribución incorrecta):** *"...\citet{neu2013intercomparison} señalan que la variabilidad en forma y tamaño de los ETC genera divergencias sistemáticas entre métodos de detección, particularmente pronunciadas en regiones de topografía compleja."*
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:41`).

---

## `padilhareinke2024objective` — Padilha Reinke et al. 2024, algoritmo objetivo de tracking del HS completo (ζ₈₅₀, ERA5 1982-2022)

**En .bib:** sí. 2 usos activos, Cap. 01 L10 OK.

**MATIZ menor (prioridad baja) — Cap. 02, L31:**
- **Texto actual:** *"esta variable se ha usado objetivamente en estudios regionales del Atlántico Sur \citep{gramcianinov2019properties,padilhareinke2024objective}..."*
- **Por qué:** a diferencia de `gramcianinov2019properties` (sí regional), `padilhareinke2024objective` es una climatología del **Hemisferio Sur completo**, no un estudio regional del Atlántico Sur. No invalida el argumento metodológico (uso de ζ₈₅₀), pero la etiqueta geográfica conjunta es imprecisa.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:33`) — resuelto junto con `sinclair1997objective` (ver esa entrada), separando "Hemisferio Sur completo" (Padilha Reinke) de "regional del Atlántico Sur" (Gramcianinov).

---

## `catto2015front` (citekey en .bib: `catto2015fronts`) — Catto et al. 2015, vínculo global WCB-frentes-precipitación extrema

**En .bib:** sí, registrado como `catto2015fronts`. 2 usos activos.

**Uso OK — Cap. 05, L70:** vinculación WCB-frentes-precipitación extrema (2-10× más propensos), fiel.

**MATIZ/ERROR — Cap. 02, L102:**
- **Texto actual:** *"Esta organización frontal del WCB es la que vincula su posición con los máximos de precipitación, y no la intensidad del vórtice central \citep{catto2015fronts}."*
- **Por qué:** la primera parte es fiel, pero el paper no discute en ningún momento la intensidad/profundidad del vórtice central (MSLP) — verificado por grep en todo el `.md` fuente, sin ninguna mención de "intensity"/"core"/"MSLP"/"deepen". La cláusula "y no la intensidad del vórtice central" es una comparación que Catto et al. no hacen, y al estar dentro de la oración citada se le atribuye como hallazgo propio.
- **Propuesta:** *"Esta organización frontal del WCB es la que vincula su posición con los máximos de precipitación \citep{catto2015fronts}."* (eliminar la cláusula no sustentada), o atribuir el contraste con la intensidad del vórtice a otra fuente y separar la cita.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:104`), versión simplificada.

---

## `chen2025characteristics` — Chen & Di Luca 2025, extremos horarios de viento/precipitación en ciclones (HN, ERA5+IMERG)

**En .bib:** sí. 2 usos activos, Cap. 01 L39 OK.

**MATIZ — Cap. 02, L175:**
- **Texto actual:** *"\citet{chen2025characteristics} establecieron que esta configuración conjunta responde a mecanismos físicos acoplados que varían según el desarrollo del sistema, lo que justifica el análisis integrado..."*
- **Por qué:** el paper no dice que el acoplamiento varíe según la etapa de desarrollo/ciclo de vida del sistema; dice que la exceedance local depende de la **posición relativa** de las estructuras de mesoescala (WCB/CCB, sting jet) dentro del ciclón — un argumento espacial/estructural, no temporal/evolutivo. La propia cartilla ya advertía sobre esta imprecisión ("coherente pero no idéntico").
- **Propuesta:** *"\citet{chen2025characteristics} establecieron que esta configuración conjunta responde a mecanismos físicos acoplados que dependen de la posición relativa de las estructuras internas de mesoescala (cintas transportadoras cálida/fría, sting jet) dentro del ciclón, lo que justifica el análisis integrado..."*
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:177`), también se quitó el guion largo y el ":" iniciales de la oración por preferencia de estilo del usuario.

---

## `eisenstein2023identification` — Eisenstein et al. 2023, identificación objetiva de sting jets (HN, ERA5)

**En .bib:** sí. 7 usos activos (Cap.01 L36, Cap.02 L103/L131, Cap.04 L77/L96/L167, Cap.06 L146) — 6 OK, verificados línea por línea contra el `.md` fuente.

**MATIZ de baja confianza — Cap. 04, L96 (resuelto, verificación más profunda que la nota original):**
- **Texto original:** atribuía tanto al sting jet como al "chorro de la CCB" estar en la "zona de fractura frontal", citando en bloque a `clark2005sting, clark2018sting, eisenstein2023identification`.
- **Verificación adicional (grep exhaustivo del `.md` fuente, no solo lectura puntual):** el término "fracture"/"frontal fracture" **no aparece ni una sola vez** en todo `eisenstein2023identification.md` — no es solo una atribución imprecisa para el CJ, el concepto no forma parte del vocabulario del artículo en absoluto. Lo que el paper sí dice explícitamente, y que es aprovechable, es que el SJ y el CJ tienen características de superficie tan similares por su cercanía espacio-temporal que su propio método de clasificación **funde al SJ dentro de la categoría CJ**: *"As the CJ and SJ have similar surface parameter characteristics due to their proximity in both time and space, the SJ is included in the more frequent CJ feature."*
- **Propuesta (versión aplicada):** se mantiene `clark2005sting, clark2018sting` para la "zona de fractura frontal" (sí la documentan explícitamente, ver verificación de citas del Cap. 2/4), y se reasigna `eisenstein2023identification` a un rol distinto dentro de la misma oración: respaldar por qué el SJ y el CCB son prácticamente indistinguibles en superficie, en vez de la ubicación de fractura frontal que el artículo no menciona. De paso, a pedido del usuario, se reemplazó "en el caso austral" por "en el Hemisferio Sur" (vocabulario más simple y consistente con el resto del capítulo): *"...chorros de bajo nivel como los \textit{sting jets} y el chorro de la cinta transportadora fría (CCB, \textit{cold conveyor belt}) \citep{clark2005sting, clark2018sting}, cuya proximidad espacio-temporal los vuelve prácticamente indistinguibles en superficie \citep{eisenstein2023identification}; la inversión de la circulación entre hemisferios traslada dicho sector al cuadrante noroeste en el Hemisferio Sur."*
- **Estado:** ✅ aplicado (`04.vr2_result01_w10.tex:96`).

---

## `gramcianinov2024early` — ciclogénesis temprana/incipiente en el Atlántico Sur (RCM alta resolución)

**En .bib:** sí. 5 usos activos, todos en Cap. 02 y Cap. 05.

**ERROR (alta confianza, verificado línea por línea) — Cap. 02, L133:**
- **Texto actual:** *"Este patrón se repite en la costa SE de Brasil [=SBR]: \citet{cardoso2020wind} lo asociaron al ASAS, \citet{dejesus2021multimodel} confirmaron que el sector cálido (NE en el HS) concentra los vientos de ciclones incipientes, y \citet{gramcianinov2024early} lo atribuyeron al SALLJ."*
- **Por qué:** el paper distingue explícitamente: en **SBR** el flujo se asocia a la **SASH** (ASAS); en **LPB** resulta de la combinación SASH + **SALLJ**. El SALLJ es el mecanismo diferenciador de LPB, no de SBR — atribuirlo a SBR invierte la regionalización propia del paper, y es redundante porque SASH/ASAS ya está cubierto en la misma oración por `cardoso2020wind`. De hecho, Cap. 05 L36 (mismo autor) sí diferencia correctamente SASH→SBR y SALLJ→LPB, por lo que el propio texto de la tesis se contradice entre capítulos.
- **Propuesta (versión aplicada, con aporte nuevo en vez de repetir el punto de humedad ya cubierto en L81):** en vez de solo reasignar el SALLJ de SBR a LPB (que hubiera repetido el mismo punto de L81), se buscó información nueva del paper para esta oración, que trata sobre *ubicación* de vientos máximos (tema de `cardoso2022synoptic`/`eisenstein2023identification`/`cardoso2020wind`), no sobre humedad/intensificación. Se encontró que el paper reporta que la advección cálida (vientos del noroeste intensos) se ubica **al este del centro** en SBR y LPB, reforzada en el **cuadrante noreste de LPB** por la combinación SASH+SALLJ — verificado que este dato viene de compositing **euleriano centrado en el ciclón** (caja fija 40°×40°), no de un enfoque lagrangiano. También se verificó, a pedido del usuario, que `dejesus2021multimodel` sí habla de "sector" (cálido/NE en el HS) y de "incipient cyclone" en su propio texto — pero se detectó que "incipiente" es un término reservado en esta tesis (una de las cuatro fases formales del CycloPhaser, Cap.03), mientras que `dejesus2021multimodel` lo usa de forma informal (sin ese marco de segmentación), así que se reformuló esa cláusula para evitar la confusión terminológica: *"Este mismo patrón se repite en la costa SE de Brasil. \citet{cardoso2020wind} lo asociaron al ASAS, \citet{dejesus2021multimodel} confirmaron que el sector cálido (NE en el HS) concentra los vientos en la etapa temprana de desarrollo del ciclón, y \citet{gramcianinov2024early} localizaron los vientos del noroeste más intensos al este del centro en SBR y LPB, reforzados en el cuadrante noreste de LPB por su combinación con el SALLJ."*
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:135`).

**MATIZ — Cap. 02, L79:**
- **Texto actual:** atribuye la ciclogénesis en LPB directamente al "efecto de sotavento de la Cordillera de los Andes... mediante el chorro de bajo nivel", citando a `gramcianinov2024early` como confirmación de que la convergencia de humedad en capas bajas es el mecanismo dominante.
- **Por qué:** el paper atribuye el efecto orográfico de los Andes principalmente a **ARG** (entrada de aire frío, niveles medios-altos); a LPB y SBR conjuntamente les atribuye "otros mecanismos... relacionados con flujos de humedad y calor", no específicamente el efecto orográfico. La atribución del efecto Andes específicamente a LPB es una simplificación imprecisa.
- **Propuesta (descartada durante la aplicación):** *"...la ciclogénesis en SBR y LPB está favorecida por el efecto del relieve andino que canaliza aire cálido y húmedo desde los trópicos mediante el chorro de bajo nivel (SALLJ), mientras que en ARG predomina la interacción con perturbaciones de niveles medios-altos..."* — el usuario notó, correctamente, que esta propuesta repetía el mismo tipo de error: seguía atribuyéndole el "relieve andino" a SBR/LPB, cuando el paper regionaliza así: SBR→SASH, LPB→SASH+SALLJ, ARG→efecto orográfico andino (consistente con la cita ya correcta de Cap.05 L36).
- **Propuesta (versión aplicada, corregida):** *"En la región de LPB, \citet{gramcianinov2024early} resaltaron que la ciclogénesis se ve favorecida por la interacción entre la Alta Subtropical del Atlántico Sur y el Chorro de Capas Bajas de Sudamérica, que intensifica el transporte de humedad hacia el sistema, y confirmaron mediante modelos regionales que la convergencia de humedad en capas bajas constituye el mecanismo dominante de intensificación."* — sin mencionar los Andes para LPB en absoluto (ese mecanismo es exclusivo de ARG).
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:81`).

---

## `padilhareinke2026characterization` — Padilha Reinke et al. 2026, climatología horaria de 41 años del Atlántico Sudoccidental (ERA5)

**En .bib:** sí. 3 usos activos, Cap.01 L16 y Cap.04 L44 OK.

**ERROR (verificado línea por línea) — Cap. 04, L45:**
- **Texto actual:** *"\citet{padilhareinke2026characterization} documentan **para SBR** un umbral p90 de 23.4~m\,s$^{-1}$ (84.4~km\,h$^{-1}$) y extremos de hasta 31.4~m\,s$^{-1}$ (113.2~km\,h$^{-1}$)."*
- **Por qué:** el propio paper dice explícitamente que la Tabla 1 (de donde salen estas cifras) muestra estadísticas para "the study area" — el dominio completo (20°-50°S, 65°-30°W), no una subregión SBR. El paper solo desagrega por "parte norte/sur" (división en 35°S) para las tendencias (Tabla 2, no para intensidad de viento), y esa partición tampoco corresponde a la regionalización SBR/LPB/ARG de la tesis. La cartilla existente registra la cita correcta sin la calificación "para SBR" — parece haberse introducido en una edición posterior.
- **Propuesta:** *"\citet{padilhareinke2026characterization} documentan para el conjunto del Atlántico Sudoccidental un umbral p90 de 23.4~m\,s$^{-1}$ (84.4~km\,h$^{-1}$) y extremos de hasta 31.4~m\,s$^{-1}$ (113.2~km\,h$^{-1}$)."* (eliminar "para SBR").
- **Estado:** ✅ aplicado (`04.vr2_result01_w10.tex:45`).

**Oportunidad no aprovechada:** el paper reporta que los compuestos de eventos costeros intensos se asocian a "transporte de humedad por el jet de bajo nivel del noroeste desde los trópicos" — dato con cuadrante explícito, potencialmente útil para Cap. 05/07 si se discute el mecanismo de aporte de humedad en eventos costeros intensos. No evaluado en profundidad.

---

## `reboita2010south` — Reboita et al. 2010, climatología RegCM3 fundacional de RG1/RG2/RG3 (Atlántico Sur)

**En .bib:** sí. 5 usos en 4 capítulos (Cap.02 L68/L81, Cap.04 L67, Cap.06 L32), todos OK.

**MATIZ de baja prioridad — Cap. 01, L15:**
- **Texto actual (antes de la corrección):** atribuye conjuntamente "inestabilidad baroclínica de los oestes" y "ciclogénesis de sotavento asociada a los Andes" a los "tres centros preferenciales" en bloque.
- **Por qué:** el paper atribuye estos mecanismos de forma diferenciada por región: la inestabilidad baroclínica de los oestes se asocia específicamente a RG3/ARG, el centro más al sur (~45-50°S, vía Gan & Rao 1991, Sinclair 1996, líneas 588-590 del `.md`), mientras que el efecto de sotavento andino (onda topográfica con el trough cerca de Uruguay y sur de Brasil, vía Gan & Rao 1994, líneas 602-608 del `.md`) se asocia a RG1/RG2, los dos centros más al norte. Presentarlos como aplicables a los tres centros en conjunto era una simplificación defendible en una introducción, pero técnicamente imprecisa.
- **Propuesta (versión aplicada, sin usar aún las etiquetas SBR/LPB/ARG —que se definen formalmente más adelante en el capítulo con una delimitación distinta, de `gramcianinov2019properties`— y con vocabulario simplificado a pedido del usuario, evitando "austral"/"septentrional"):** *"...identificaron tres centros preferenciales de ciclogénesis: uno al sur, vinculado a la inestabilidad baroclínica de los oestes, y dos más al norte, próximos a Uruguay y el sur de Brasil, vinculados a la ciclogénesis de sotavento inducida por la onda topográfica de los Andes."*
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:15`).

---

## `reboita2018extratropical` — Reboita et al. 2018, valor agregado del downscaling RegCM4 para ciclones del Atlántico Sudoccidental

**En .bib:** sí. Única ocurrencia activa.

**MATIZ (confianza moderada) — Cap. 04, L105:**
- **Texto actual:** *"...las interacciones diabáticas y flujos de calor latente océano-atmósfera \citep{reboita2018extratropical} sostienen la inestabilidad baroclínica de baja troposfera que capitalizan SBR y LPB..."*
- **Por qué:** el paper discute (1) que el exceso de densidad de ciclones sobre océano abierto en las simulaciones RegCM se vincula a flujos de calor latente *excesivos del modelo* (un sesgo de simulación, no una climatología observada de mecanismo físico), y (2) que los ciclones explican ~80% de la precipitación anual en la confluencia Brasil-Malvinas. No formula explícitamente que "las interacciones diabáticas sostienen la inestabilidad baroclínica de baja troposfera" en SBR/LPB — es una síntesis/inferencia más fuerte que lo que el texto fuente sustenta directamente.
- **Propuesta (versión aplicada, con precisión adicional del usuario):** se dividió la oración larga en dos, se suavizó "sostienen la inestabilidad baroclínica" a "contribuyen a la actividad ciclónica", y —a pedido del usuario— se reformuló la referencia a SBR/LPB/ARG para dejar explícito que son etiquetas de **región de génesis**, no cajas geográficas donde el ciclón permanece durante todo su ciclo de vida (los sistemas se desplazan hacia el Atlántico abierto en intensificación/madurez/decaimiento): *"Las diferencias interregionales de la Figura~\ref{fig:kde_wind_p90}, la mayor concentración en SBR y LPB respecto a ARG, respaldan el marco dinámico ya descrito (Sección~\ref{sec:pdf_wind10}). Los flujos de calor latente océano-atmósfera \citep{reboita2018extratropical} contribuyen a la actividad ciclónica de los sistemas con génesis en SBR y LPB \citep{andrade2024composite, coutodesouza2024thesis}, mientras que en los de génesis en ARG la dinámica baroclínica clásica y la perturbación orográfica andina producen estructuras más elongadas con máximos menos concentrados."*
- **Estado:** ✅ aplicado (`04.vr2_result01_w10.tex:105`).

---

## `reboita2022from` — Reboita et al. 2022, caso ciclón Raoni (transición extratropical→subtropical, flujos turbulentos WISHE)

**En .bib:** sí. 6 usos activos en 4 capítulos.

**MATIZ — Cap. 02, L14 (ahora L15 tras inserciones previas):**
- **Texto original:** *"la supresión de los **flujos de calor latente** alteró la estructura..."*
- **Por qué:** el experimento NOFLUX del paper apaga los flujos turbulentos de calor superficiales **completos** (sensible + latente), no solo el latente — el propio artículo los llama "the sensible and latent surface heat fluxes" (líneas 286-287) y luego, en conjunto, "the turbulent heat fluxes" (líneas 336, 895, 899).
- **Propuesta (dos opciones evaluadas):** (A) "flujos turbulentos de calor" (término técnico que usa el propio paper) o (B) "flujos de calor sensible y latente" (enumeración explícita, sin jerga). El usuario eligió la opción B, más clara para un lector no especializado sin perder fidelidad.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:15`) — *"...la supresión de los flujos de calor sensible y latente alteró la estructura térmica y la intensidad del vórtice..."*

**MATIZ/posible ERROR — Cap. 01, L25:**
- **Texto actual (antes de la corrección):** *"El transporte meridional de humedad desde los trópicos... es mediado por el Chorro de Capas Bajas de Sudamérica: como demuestran \citet{reboita2022from}, los flujos turbulentos de calor superficiales en el flanco oriental del ciclón..."*
- **Por qué:** conflación de dos mecanismos distintos — el SALLJ (advección continental de humedad tropical) no es lo que `reboita2022from` estudia; su hallazgo real es la retroalimentación de flujos turbulentos océano-atmósfera (WISHE), sin localización específica en "flanco oriental" verificable en el texto (la convección se organiza "alrededor del centro del ciclón", no en un cuadrante fijo).
- **Propuesta (versión aplicada):** se separaron los dos mecanismos y se añadió `reboita2026meteorology` (ya usado y verificado en la tesis, y que menciona explícitamente el SALLJ como mecanismo de advección de aire cálido/húmedo en la región) para respaldar la cláusula del SALLJ, dejando `reboita2022from` limitado a su hallazgo real (flujos turbulentos de calor océano-atmósfera), sin la calificación de cuadrante: *"El transporte meridional de humedad desde los trópicos hacia estos sistemas es mediado por el Chorro de Capas Bajas de Sudamérica \citep{reboita2026meteorology}, mientras que los flujos turbulentos de calor superficiales océano-atmósfera, como demuestran \citet{reboita2022from}, no solo inestabilizan la atmósfera, sino que actúan como fuente diabática que refuerza la intensidad del sistema."*
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:25`).

**Nota — evaluado y descartado como candidato de reemplazo para `crespo2020potential` en Cap.07 L45** (ver esa entrada): su mecanismo central no es el SALLJ.

---

## `reboita2026meteorology` — Reboita et al. 2026, capítulo de síntesis del estado del arte de la meteorología sudamericana (Cambridge)

**En .bib:** sí. 3 usos activos, Cap.01 L19/L21 OK. Tercer uso añadido en esta sesión: Cap.01 L25 (respaldo del SALLJ como mediador del transporte meridional de humedad, ver entrada de `reboita2022from`) — verificado contra el `.md` fuente ("advection of warm and moist air by the SALLJ and by the SASA northward flow"), fiel.

**Oportunidad no aprovechada (resuelta):**
- **Ubicación exacta:** Cap. 01 (motivación), entre las oraciones de `jones1993climatology` (L14) y `reboita2010south` (L15).
- **Por qué:** el capítulo aporta cifras cuantitativas no usadas en ningún capítulo activo (~200 ciclones extratropicales/año en el Atlántico Sur occidental, ~8 subtropicales/año, ~16% explosivos en invierno austral) que reforzarían la motivación.
- **Propuesta (aplicada, simplificada a pedido del usuario: sin "explosivos", sin subtropicales, sin distinción verano/invierno, sin ":")**: *"Sobre el Atlántico Sur occidental, esta actividad ciclónica es particularmente intensa, con aproximadamente 200 ciclones extratropicales registrados por año \citep{reboita2026meteorology}."*
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:15`).

---

## `shapiro1990life` — Shapiro & Keyser 1990, capítulo fundacional del modelo Shapiro-Keyser (caso ERICA)

**En .bib:** sí. 5 usos en 3 capítulos; Cap.01 L53, Cap.02 L99, Cap.04 L165 OK.

**ERROR (alta confianza) — Cap. 02, L9:**
- **Texto actual:** *"La teoría clásica define a los ETC como vórtices de núcleo frío cuya génesis está dominada por la inestabilidad baroclínica de latitudes medias \citep{shapiro1990life}."*
- **Por qué:** invierte el sentido del paper. Shapiro & Keyser (1990) no son el origen de "la teoría clásica" (eso es Bjerknes & Solberg 1919-22 para el modelo frontal, y Charney/Eady para la inestabilidad baroclínica) — su capítulo se presenta explícitamente como una **revisión** de ese modelo clásico noruego, introduciendo la seclusión de núcleo cálido como alternativa. Citarlos para respaldar "la teoría clásica" es atribuirles lo opuesto de su contribución.
- **Propuesta (versión aplicada):** confirmado `bjerknes1922life` en el `.bib`; se verificó además contra su cartilla que el paper **no usa el concepto de "inestabilidad baroclínica"** (esa teoría dinámica es de Charney/Eady, 1947-49, posterior en 25 años) — su modelo es puramente frontal/observacional (onda sobre una discontinuidad térmica). Por eso se reformuló también la descripción, no solo la cita, para no introducir un nuevo anacronismo. El usuario aclaró además que el propósito de esta oración es dar contexto histórico de cómo se estudió el fenómeno desde el inicio, no explicar el mecanismo físico de formación — el ajuste final refleja eso: *"La teoría clásica, desarrollada a partir de los primeros estudios sinópticos de ciclones de latitudes medias, los definió como vórtices de núcleo frío que evolucionan a partir de una onda sobre un frente de discontinuidad térmica entre masas de aire frío y cálido \citep{bjerknes1922life}."* `shapiro1990life` se mantiene sin cambios en Cap.02 L99, donde ya presenta correctamente el modelo Shapiro-Keyser.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:9`). Además, a pedido del usuario, se insertó una oración puente inmediatamente después (L10) que conecta explícitamente el modelo de Bjerknes con la revisión de Shapiro-Keyser, para que la genealogía de estudios de ETC no se corte antes de saltar a la climatología del HS (Hoskins). Se probaron dos versiones (una con adelanto de rasgos estructurales, otra aligerada sin nombrarlos) para evitar redundancia con el desarrollo completo del modelo en L100 (misma sección, `\label{subsec:tb_modelos}`); el usuario eligió la versión aligerada: *"Este modelo fue revisado décadas después por \citet{shapiro1990life}, cuyo marco estructural se desarrolla en la Sección~\ref{subsec:tb_modelos}."*

**ERROR numérico (verificado línea por línea) — Cap. 04, L109:**
- **Texto actual:** *"...en el máximo de viento de bajo nivel dentro de la capa límite marina (${\sim}950$~hPa)..."*
- **Por qué:** el paper dice explícitamente "~900 mb" (no 950 mb) para ese máximo de viento de bajo nivel, en dos pasajes del caso ERICA. El resto de la cita es correcto (935 hPa presión central, ~40 m/s, 35-50 m/s en la sección transversal del núcleo — verificados exactos).
- **Propuesta (versión aplicada, resuelta de otra forma):** en vez de solo corregir el número, el usuario pidió revisar si hacía falta mencionar los niveles isobáricos en absoluto (no, no aporta al argumento) y acortar el pasaje. Se verificó además la hilación con `gray2020prototype` (cita siguiente, L111) — cumplen roles complementarios pero distintos: Shapiro justifica con un número (magnitud observada real, plausible frente a la cola p90 de ERA5), Gray justifica con relevancia práctica (motivación operativa) — la transición es coherente, no requirió cambios. Texto final, sin niveles isobáricos puntuales y sin guiones largos: *"Una referencia observacional directa de la magnitud que puede alcanzar el viento en estas estructuras proviene del caso clásico documentado por \citet{shapiro1990life}: durante la fase de seclusión cálida de un ETC profundo (presión central ${\sim}935$~hPa) del Atlántico Norte, mediciones de aeronave registraron velocidades de hasta 35--50~m\,s$^{-1}$ en niveles bajos. Aunque no corresponden a viento en superficie a 10~m, la fricción reduce sistemáticamente el viento hacia niveles más bajos, por lo que estos valores son consistentes con las colas de hasta 30~m\,s$^{-1}$ observadas en el wind10 de ERA5 para el subconjunto p90..., respaldando que la subestimación de ERA5 es plausible incluso en el extremo superior de la distribución."*
- **Estado:** ✅ aplicado (`04.vr2_result01_w10.tex:109`).

---

## `shapiro1999bridge` — Shapiro et al. 1999, puente teórico-observacional LC1/LC2/LC3 (ERICA, FASTEX)

**En .bib:** sí. 6 usos en 5 capítulos; Cap.01 L53, Cap.02 L159, Cap.04 L165 OK.

**MATIZ (mismo patrón en 3 ocurrencias) — Cap. 05, L40 (resuelto); Cap. 05, L97 (revisado, sin cambio necesario); Cap. 06, L118 (resuelto):**
- **Texto original (Cap. 05, L40):** *"...mediante la cual aire frío, subsidente y de baja humedad de la alta troposfera o estratosfera se enrosca hacia el centro del sistema \citep{shapiro1999bridge}."* (intrusión seca / "dry intrusion").
- **Por qué:** el paper no usa la terminología "dry intrusion"/"dry slot" en ningún momento (verificado por grep, 0 coincidencias) ni describe un mecanismo que "se enrosca hacia el centro". Lo más cercano, verificado con cita textual, es: *"the warm-core seclusion of the Pre-ERICA IOP-4 (dual-jet, LC2) cyclone possessed subsidence to the west of the cyclone center"* — subsidencia al oeste del centro en el caso de seclusión cálida (LC2), no una espiral hacia el centro, y de naturaleza troposférica (no estratosférica; lo estratosférico en el paper son los "tropopause folds", un mecanismo relacionado pero distinto no usado aquí). El caso (ERICA/FASTEX) es del Hemisferio Norte.
- **Propuesta (versión aplicada, simplificada a pedido del usuario sin mencionar "seclusión cálida" explícitamente):** *"...mediante la cual aire frío, subsidente y de baja humedad de la alta troposfera desciende al oeste del centro del sistema, consistente con la subsidencia troposférica documentada para el Hemisferio Norte por \citet{shapiro1999bridge}."*
- **Estado:** ✅ aplicado en Cap. 05 L40 (`05.vr2_result02_tp.tex:40`), con disclosure de Hemisferio Norte agregado. Cap. 05 L97 revisada: solo remite de vuelta a "la intrusión seca descrita en la Sección [L40]" sin repetir la afirmación geométrica, por lo que hereda la corrección sin necesitar cambio propio.
- **Cap. 06, L118 (resuelto):** además de la misma corrección geométrica/terminológica y el disclosure de Hemisferio Norte, se eliminó "caída de presión" (terminología de presión, evitada por preferencia del usuario en favor de vocabulario de intensificación/vorticidad) y "vórtice" se reemplazó por "sistema" en todo el párrafo (a pedido del usuario: "sistema" = el ETC completo, "vórtice" sugiere un área central más pequeña). Sobre si la posición geométrica ("oeste") debía invertirse para el Hemisferio Sur: siguiendo la convención de mirroring ya establecida en Cap. 04 con `eisenstein2023identification` (SO en HN → NO en HS, es decir la inversión hemisférica voltea norte↔sur pero no este↔oeste), se mantuvo "oeste" sin invertir, solo con el disclosure agregado — decisión confirmada explícitamente por el usuario. Texto aplicado: *"...la intensificación acelerada del sistema se acompaña de aire frío y subsidente que desciende al oeste de su centro, suprimiendo la convección en el núcleo y confinando la humedad residual del WCB a la periferia exterior, consistente con la subsidencia troposférica documentada para el Hemisferio Norte por \citet{shapiro1999bridge}."* (`06.vr1_result03_meof.tex:118`).

---

## `simmonds2000variability` — Simmonds & Keay 2000, variabilidad y tendencias de ciclones del HS (1958-97)

**En .bib:** sí. No usado en ningún capítulo activo.

**Aporta:** análisis de tendencias temporales (no climatología media espacial, a diferencia de `simmonds2000mean`/`simmonds2000size`, ya citados): reducción significativa de densidad ciclónica al sur de ~40°S y aumento al norte; tendencia positiva significativa en radio medio y "profundidad" media de los ciclones a lo largo de 40 años; compensación interanual negativa entre densidad de latitudes medias y altas.

**Oportunidad no aprovechada (prioridad baja):**
- **Ubicación exacta:** Cap. 01 (motivación), junto a `IPCC2021_WG1_Chapter11_Extremes`, `masson2022tendencias`, `kodama2019perspective` (ya identificados en esta auditoría como oportunidades de la misma sección).
- **Por qué:** aporta evidencia observacional/histórica (1958-97, a diferencia de las proyecciones futuras de las otras fuentes) de tendencia positiva en radio y "profundidad" de los ciclones del HS — complementa esa línea argumental sin duplicarla.
- **Estado:** ✅ aplicado (`01.vr5_introducao.tex:49`) — ver la entrada de `kodama2019perspective` para el texto exacto insertado y la decisión de combinar solo estos dos autores (sin `IPCC2021_WG1_Chapter11_Extremes` ni `masson2022tendencias`).

---

## `sinclair1995climatology` — Sinclair 1995, ciclogénesis del HS ligada a gradientes térmicos oceánicos y orografía

**En .bib:** sí. 2 usos en Cap. 02 (L11, L87), ambos fieles al contenido.

**Problema de redacción detectado (fuera del alcance de fidelidad de citas, pero concreto y verificable) — Cap. 02, L87:**
- **Qué pasó:** comparando `02.vr3_fundamentacao.tex` (versión anterior) contra `02.vr4_fundamentacao.tex` (versión activa), la oración cambió de *"...\citet{sinclair1995climatology} **muestra**..."* (presente) a *"...\citet{sinclair1995climatology} **mostró**..."* (pretérito) — es decir, en algún punto de esta sesión se convirtió en la dirección **opuesta** a la política de "presente predominante" acordada con el usuario para toda la tesis.
- **Por qué importa:** sugiere que la conversión de tiempos verbales de `vr3`→`vr4` no fue 100% consistente en una dirección; podría haber más casos aislados de este tipo en `02.vr4` que no se detectaron en el barrido original de conversión (ese barrido buscaba pretérito→presente, no casos que fueran accidentalmente en sentido contrario).
- **Propuesta:** cambiar "mostró" de vuelta a "muestra" en Cap.02 L87. Se recomienda además un grep rápido en `02.vr4_fundamentacao.tex` de verbos en pretérito para descartar más casos aislados como este antes de dar por cerrada la conversión de tiempos verbales del capítulo.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:89`, la línea se corrió por las inserciones previas).

---

## `sinclair1997objective` — Sinclair 1997, detección de ciclones vía vorticidad del viento del gradiente a 1000 hPa + "circulación" como medida de intensidad

**En .bib:** sí. 2 usos activos; Cap.04 L227 OK.

**ERROR (verificado por grep exhaustivo, 0 menciones de "850" en el paper) — Cap. 02, L31:**
- **Texto actual:** *"Para resolver este problema, \citet{sinclair1997objective} recomendaron utilizar $\zeta_{850}$..."*
- **Por qué:** el paper trabaja íntegramente con vorticidad del viento del gradiente a **1000 hPa**, nunca a 850 hPa. La cartilla de estudio ya señala este nivel correctamente en su encabezado, pero su sección de "relación con la tesis" parafrasea sueltamente "recomiendan utilizar la vorticidad relativa en 850 hPa" — una imprecisión de la cartilla que parece haberse trasladado tal cual al texto de la tesis. Atribuirle a Sinclair (1997) la recomendación específica de 850 hPa es un error factual de nivel.
- **Propuesta (versión aplicada, dividida en dos oraciones a pedido del usuario, y coordinada con `padilhareinke2024objective`):** *"Para resolver este problema, \citet{sinclair1997objective} recomendaron utilizar la vorticidad relativa en niveles bajos en lugar de la presión al nivel del mar; en esta tesis se adopta específicamente $\zeta_{850}$. Esta variable se ha usado objetivamente en climatologías del Hemisferio Sur completo \citep{padilhareinke2024objective} y en estudios regionales del Atlántico Sur \citep{gramcianinov2019properties}, además en el HN por \citet{corner2025classification}, y su utilidad para la segmentación objetiva del ciclo de vida fue demostrada por \citet{coutodesouza2024new}, quienes identificaron la evolución temporal de esta variable como el predictor más confiable para definir sus fases."*
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:32-33`).

---

## `sinclair2023relationship` — Sinclair & Catto 2023, simulaciones aqua-planet idealizadas de intensidad-precipitación en ETC

**En .bib:** sí. 5 usos en 4 capítulos; Cap.01 L35, Cap.04 L254, Cap.05 L19/L25 OK.

**ERROR — Cap. 02, L143:**
- **Texto actual:** *"Esta separación espacial no es exclusiva de la región: \citet{sinclair2023relationship} y \citet{portal2024linking} la documentaron en el HN/Mediterráneo (lluvia bajo el WCB, viento bajo la intrusión seca)..."*
- **Por qué:** `sinclair2023relationship` es una simulación idealizada aqua-planet **sin continentes ni Mediterráneo**, y no estudia la disociación espacial "lluvia bajo el WCB / viento bajo la intrusión seca" — ese es el hallazgo propio de `portal2024linking` (ya verificado como fiel en esta auditoría). Sinclair & Catto solo mencionan el WCB de pasada en su introducción, citando a terceros — no es un hallazgo propio del paper. Atribuirle este mecanismo regional específico es un error de contenido.
- **Propuesta:** eliminar `sinclair2023relationship` de esta oración y dejar solo `\citep{portal2024linking}`, que sí es la fuente real de ese hallazgo específico.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:145`).
- **Hallazgo adicional detectado en la misma oración durante la aplicación:** `gentile2025response` también estaba citado ahí ("...confirman que el sector cálido concentra los mayores incrementos de ambas variables...") — no estaba registrado antes en esta auditoría. Es un estudio de la **respuesta a un clima futuro más cálido** (+4K SST, X-SHiELD), no de la separación espacial actual entre lluvia y viento; su propia cartilla especifica que solo debería citarse 2 veces en la tesis (Cap.01 L43, Cap.04 L5), no en Cap.02. Se retiró de esta oración por mezclar indebidamente una proyección climática futura con una afirmación sobre estructura presente. Sigue citado correctamente en sus otros 2 usos.
- **Además:** se ajustó la cláusula de `russo2025impacts` (ya verificada fiel antes) para no repetir la palabra "profundización" tan seguido en el párrafo, sin alterar el sentido.

---

## `vera2002cold` — Vera et al. 2002, modo subtropical de ondas sinópticas cruzando los Andes (~30°S)

**En .bib:** sí. 5 usos en 4 capítulos; Cap.01 L24, Cap.04 L39, Cap.05 L72 OK.

**MATIZ — Cap. 02, L11:**
- **Texto actual:** *"...la cual modula la propagación de ondas baroclínicas sobre el subcontinente sudamericano \citep{vera2002cold} y define regiones preferenciales de desarrollo en latitudes extratropicales."*
- **Por qué:** el paper es específico del modo **subtropical** (~30°S); reconoce explícitamente que para zonas más australes (ARG extratropical) es más relevante el modo subpolar, no analizado en este estudio. Atribuirle que "define regiones preferenciales de desarrollo en latitudes extratropicales" en general sobreextiende su alcance real (subtropical).
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:11`) — se resolvió junto con `inatsu2004zonal` (ver esa entrada), quitando la cláusula sobreextendida y dejando una contribución genérica y fiel ("favorece la propagación de ondas baroclínicas sobre el subcontinente sudamericano").

**ERROR (comparte el mismo problema que `gozzo2013air` en la misma oración) — Cap. 02, L125:**
- **Texto actual:** *"En el Atlántico Sur, \citet{gozzo2013air} y \citet{vera2002cold} documentaron este mismo patrón en el sector sureste/este"* (refiriéndose al patrón de sector oriental ascendente/húmedo vs. flanco occidental subsidente/seco, un patrón de compositing centrado en el ciclón).
- **Por qué:** Vera et al. no hacen compositing centrado en ciclón ni reportan un "sector sureste/este" relativo a un vórtice individual — su hallazgo es convergencia de humedad con orientación NW-SE sobre un área geográfica fija (máximo sobre Uruguay), en el contexto del cruce de los Andes. Es un mecanismo geográfico distinto al patrón cuadrante-relativo-al-centro que la oración describe.
- **Estado:** ✅ aplicado (`02.vr4_fundamentacao.tex:127`) — se retiró de esta oración por completo (ver entrada de `gozzo2013air`, que quedó reformulada centrada solo en ese autor). `vera2002cold` sigue bien citado en sus otros 4 usos.

---

**Recorrido de los 106 autores de `papers/files_MD/` completado.**

