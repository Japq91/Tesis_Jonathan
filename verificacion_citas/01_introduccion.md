# Verificación de citas — Capítulo 1: Introducción

Fuente tesis: `tex_es/01.vr5_introducao.tex`
Formato por entrada: (1) frase/oración de la tesis en español, (2) frase/párrafo equivalente del paper original en su idioma original, (3) fuente, (4) marcas de pausa real de 30s con hora `HHMMSS` (para auditoría).

---

## Cita 1 — `hoskins2005new` (línea 9)

**Tesis (ES):**
> \citet{hoskins2005new} caracterizan los *storm tracks* del HS, los corredores preferenciales por donde estos ciclones canalizan gran parte del transporte latitudinal de energía del hemisferio.

**Paper original (EN):**
> "The storm tracks of the Southern Hemisphere (SH) are important for the weather there and also for climate processes through their latitudinal transports and their structure obtained over many years..." (nota: el `.md` fuente proviene de un PDF a dos columnas y presenta artefactos de OCR/orden de lectura; texto reconstruido de las columnas 1 y 2 de la Introducción, línea 42-58).

**Fuente:** `papers/files_MD/hoskins2005new.md` (Introducción, líneas 42-58)

PAUSA INICIO: 235012
PAUSA FIN: 235042

---

## Cita 2 — `sinclair1994objective` (línea 10) — [ACTUALIZADA vía OCR]

**Tesis (ES):**
> \citet{sinclair1994objective} propuso el uso de la vorticidad relativa para identificar y rastrear ciclones independientemente del flujo de fondo.

**Paper original (EN):**
> "An objective method is developed and used to derive a climatology of centers of cyclonic vorticity for the Southern Hemisphere... These centers were computed as local minima of geostrophic relative vorticity ζ_r, extending previous studies based on pressure minima. This use of ζ_r avoids a bias favoring slower and/or deeper cyclones that occurs when pressure is used and includes a large number of additional mobile vorticity centers in the 45°-55°S band that are missed where a local pressure minimum cannot be found."

**Fuente:** `papers/files_MD/sinclair1994objective.md` (Abstract, líneas 11-20) — texto recuperado mediante OCR (pdftoppm 300dpi + tesseract 5.5.3, idioma `eng`) tras la nota original de "FUENTE NO EXTRAÍBLE" (el `.pdf` es un escaneo de 1994 sin capa de texto).

PAUSA INICIO [extracción original]: 235144
PAUSA FIN [extracción original]: 235214

---

## Cita 3 — `simmonds1999southern` (línea 10)

**Tesis (ES):**
> mientras que \citet{simmonds1999southern} desarrollaron un esquema complementario, basado en la Laplaciana de la presión a nivel del mar, para el seguimiento automático de sistemas en el HS.

**Paper original (EN):**
> "In this work the automatic scheme we implement finds and tracks cyclones from the digital analyses. The algorithm, based on that of Murray and Simmonds (1991a, hereafter MS), is an objective system, which has been applied to a variety of problems associated with synoptic behavior in extratropical regions... In the algorithm, the Laplacian of the MSLP, ∇²p, is taken as a measure of the strength of a low."

**Fuente:** `papers/files_MD/simmonds1999southern.md` (líneas 96-118)

PAUSA INICIO: 235224
PAUSA FIN: 235254

---

## Cita 4 — `padilhareinke2024objective` (línea 10)

**Tesis (ES):**
> más recientemente, \citet{padilhareinke2024objective} refinaron específicamente el enfoque de vorticidad relativa para la región.

**Paper original (EN):**
> "Abstract: In this study, we propose an easy and robust algorithm to identify and track extratropical cyclone events using 850 hPa relative vorticity data, gaussian filter and connected-component labeling technique... We implemented the algorithm in the Southern Hemisphere, using a 41-year high resolution dataset. Sensitivity tests were performed to determine the best parameters for detection and tracking, such as degree of smoothing, thresholds of relative vorticity at 850 hPa and the minimum area within the threshold."

**Fuente:** `papers/files_MD/padilhareinke2024objective.md` (Abstract, líneas 13-26)

PAUSA INICIO: 235304
PAUSA FIN: 235334

---

## Cita 5 — `gan1991surface` (línea 13) — [ACTUALIZADA vía OCR]

**Tesis (ES):**
> Inicialmente, autores como \citet{gan1991surface} cuantificaron que la ciclogénesis en la región sudamericana es más frecuente en invierno y que su variabilidad interanual repercute en la precipitación del sur de Brasil.

**Paper original (EN):**
> "The frequency of surface cyclogenesis over South America (approximately the area enclosed by 15°-50°S and 30°-90°W) has been calculated using 10 years (1979-1988) of data. The frequency of cyclogenesis is more in winter than in any other season... In addition to seasonal variation, the frequency of cyclogenesis shows interannual variation... The years of higher (lower) cyclogenesis are found to be associated with higher (lower) rainfall. This explains the negative correlation between the precipitation over southern Brazil and the Southern Oscillation index."

**Fuente:** `papers/files_MD/gan1991surface.md` (Abstract, líneas 8-18) — texto recuperado mediante OCR (pdftoppm 300dpi + tesseract 5.5.3, idioma `eng`).

PAUSA INICIO [extracción original]: 235344
PAUSA FIN [extracción original]: 235414

---

## Cita 6 — `jones1993climatology` (línea 14)

**Tesis (ES):**
> Poco después, la climatología hemisférica de \citet{jones1993climatology} confirmó a mayor escala esta señal, identificando a la región sudamericana como un núcleo de densidad ciclónica propio de las latitudes extratropicales, distinto de las concentraciones mayores en latitudes cercanas al polo.

**Paper original (EN):**
> "The distribution of cyclones through the hemisphere was found to be dominated by a permanent high latitude core coincident with the circumpolar trough. During the winter and intermediate seasons, two mid latitude branches are evident in the cyclone density originating in the Tasman Sea and South American sectors, both spiraling, poleward and merging with the circumpolar core in the Southern Oceans."

**Fuente:** `papers/files_MD/jones1993climatology.md` (Abstract, líneas 9-22)

PAUSA INICIO: 235427
PAUSA FIN: 235457

---

## Cita 7 — `reboita2010south` (línea 15)

**Tesis (ES):**
> Ya en un trabajo más reciente, \citet{reboita2010south} construyeron una climatología para el Atlántico Sur e identificaron tres centros preferenciales de ciclogénesis, vinculados a la inestabilidad baroclínica de los oestes y a la ciclogénesis de sotavento asociada a los Andes.

**Paper original (EN):**
> "...three cyclogenetic cores have also been found in previous studies (Necco 1982a,b; Sinclair 1996; Hoskins and Hodges 2005; and Reboita et al. 2005)... According to Gan and Rao (1991) and Sinclair (1996) the larger cyclogenesis occurrence in the southeastern Argentina (RG3) is associated with the baroclinic instability in the westerlies... The contribution of lee effect due to the Andes... is pointed [out] by Sinclair (1995) and Hoskins and Hodges (2005) as another important mechanism for the cyclones development."

**Fuente:** `papers/files_MD/reboita2010south.md` (líneas 580-599)

PAUSA INICIO: 235510
PAUSA FIN: 235540

---

## Cita 8 — `gramcianinov2020analysis` (línea 16, primera mención)

**Tesis (ES):**
> Trabajos posteriores, como \citet{gramcianinov2020analysis} y recientemente \citet{padilhareinke2026characterization}, han precisado la distribución espacio-temporal de estos sistemas, aportando conocimiento sobre la frecuencia y localización de la actividad ciclónica en la región.

**Paper original (EN):**
> "This work aims to analyze and compare ERA5 and CFSR/CFSv2 data from 1979 to 2019 with 1-hourly outputs, regarding their ability to reproduce storm tracks and the main characteristics of cyclones at middle and high latitudes in the North Atlantic (NA) and South Atlantic (SA) Oceans... The climatology produced for both datasets shows the main characteristics of the NA and SA storm tracks, such as seasonal variability and genesis regions."

**Fuente:** `papers/files_MD/gramcianinov2020analysis.md` (Abstract, líneas 13-21)

PAUSA INICIO: 235602
PAUSA FIN: 235632

---

## Cita 9 — `padilhareinke2026characterization` (línea 16)

**Tesis (ES):**
> Trabajos posteriores, como \citet{gramcianinov2020analysis} y recientemente \citet{padilhareinke2026characterization}, han precisado la distribución espacio-temporal de estos sistemas, aportando conocimiento sobre la frecuencia y localización de la actividad ciclónica en la región.

**Paper original (EN):**
> "Despite the southwest Atlantic Ocean being recognized for cyclone formation and intensification, several aspects of spatial and temporal variability remain unclear. Hence, in this study, the overall characteristics of cyclones that form within the southwest Atlantic Ocean are investigated. We also analyze the interannual variability in the frequency of cyclone occurrences across each season... The results revealed increased interannual variability... Seasonally, we found a positive trend of 1.7 per decade in cyclone occurrence for the southern part of the area during summer."

**Fuente:** `papers/files_MD/padilhareinke2026characterization.md` (Abstract, líneas 20-27)

PAUSA INICIO: 235637
PAUSA FIN: 235707

---

## Cita 10 — `hart2003cyclone` (línea 17)

**Tesis (ES):**
> Sin embargo, esta actividad ciclónica no es dinámicamente uniforme: \citet{hart2003cyclone} demostró que los sistemas transitan a lo largo de un continuo estructural y no de categorías estáticas,

**Paper original (EN):**
> "An objectively defined three-dimensional cyclone phase space is proposed and explored... A cyclone's life cycle can be analyzed within this phase space, providing substantial insight into the cyclone structural evolution. An objective classification of cyclone phase is possible, unifying the basic structural description of tropical, extratropical, and hybrid cyclones into a continuum."

**Fuente:** `papers/files_MD/hart2003cyclone.md` (Abstract, líneas 8-14)

PAUSA INICIO: 235725
PAUSA FIN: 235755

---

## Cita 11 — `evans2012climatology` (línea 17)

**Tesis (ES):**
> y en el Atlántico Sur esta heterogeneidad se manifiesta en ciclones de estructura térmica híbrida \citep{evans2012climatology}

**Paper original (EN):**
> "A 50-yr climatology (1957–2007) of subtropical cyclones (STs) in the South Atlantic is developed and analyzed. A subtropical cyclone is a hybrid structure (upper-level cold core and lower-level warm core) with associated surface gale-force winds."

**Fuente:** `papers/files_MD/evans2012climatology.md` (Abstract, líneas 7-9)

PAUSA INICIO: 235803
PAUSA FIN: 235833

---

## Cita 12 — `gozzo2013air` (línea 17, primera mención)

**Tesis (ES):**
> y en sistemas que siguen el modelo de Shapiro-Keyser, con fractura del frente frío y seclusión cálida en la madurez \citep{gozzo2013air}.

**Paper original (EN):**
> "This study analyzes the impacts of latent and sensible heat exchanges between the atmosphere and the ocean in a non-explosive Shapiro–Keyser type cyclogenesis event that occurred over the southwestern South Atlantic Ocean. The synoptic evolution shows a relatively strong warm front and a cold frontal fracture during the system's development and a warm seclusion in its mature stage, characterizing a Shapiro–Keyser type cyclone."

**Fuente:** `papers/files_MD/gozzo2013air.md` (Abstract, líneas 8-16)

PAUSA INICIO: 235843
PAUSA FIN: 235913

---

## Cita 13 — `gozzo2014subtropical` (línea 18)

**Tesis (ES):**
> El Atlántico Sur se aparta con frecuencia de la conceptualización clásica de ciclón, tal como lo evidencian las variaciones morfológicas respaldadas por una climatología regional de largo plazo \citep{gozzo2014subtropical}.

**Paper original (EN):**
> "Besides strong and organized storms, a large number of weaker, shallower cyclones with both extratropical and tropical characteristics form in the region, impacting the South American coast. The main focus of this study is to simulate a climatology of subtropical cyclones and their synoptic pattern over the South Atlantic, proposing a broader definition of these systems... The Interim ECMWF Re-Analysis (ERA-Interim) and NCEP–NCAR reanalysis are used to construct the 33-yr (1979–2011) climatology..."

**Fuente:** `papers/files_MD/gozzo2014subtropical.md` (Abstract, líneas 13-19)

PAUSA INICIO: 235921
PAUSA FIN: 235951

---

## Cita 14 — `gan1994influence` (línea 19)

**Tesis (ES):**
> la Cordillera de los Andes, cuyo forzante orográfico incrementa la baroclinicidad a sotavento \citep{gan1994influence}

**Paper original (EN):**
> "The increase of baroclinicity on the lee side results in baroclinic development as predicted from a linearly obtained normal-mode solution in the presence of mountains... the interaction of these anomalies with the Andes Cordillera is responsible for lee cyclogenesis."

**Fuente:** `papers/files_MD/gan1994influence.md` (Abstract, línea 14)

PAUSA INICIO: 000000
PAUSA FIN: 000030

---

## Cita 15 — `reboita2026meteorology` (línea 19, primera mención)

**Tesis (ES):**
> combinada con los gradientes de temperatura superficial del mar \citep{reboita2026meteorology}, consolida focos de actividad ciclogenética diferenciados en la costa este de Sudamérica

**Paper original (EN):**
> "Among the factors that favour the cyclogenetic potential along eastern SA are the mid-upper-level baroclinic waves that propagate from the South Pacific to the South Atlantic Ocean, incursion or formation of subtropical CVs, lee effect of the Andes topography, advection of warm and moist air by the SALLJ and by the SASA northward flow, sea-air turbulent heat fluxes, and baroclinic instability originating from the SST gradient at the confluence of the Malvinas and Brazil currents (Reboita et al., 2010b; Gozzo et al., 2014, 2017; Gramcianinov et al., 2019; Leyba et al., 2023)."

**Fuente:** `papers/files_MD/reboita2026meteorology.md` (Cap. 8, líneas 640-650)

PAUSA INICIO: 000044
PAUSA FIN: 000114

---

## Cita 16 — `crespo2020potential` (línea 21)

**Tesis (ES):**
> Dada esta heterogeneidad estructural y regional, este estudio se centra en tres regiones de ciclogénesis documentadas por diversos autores \citep{crespo2020potential, gramcianinov2019properties, reboita2026meteorology}

**Paper original (EN):**
> "This study investigates the influence of upper-level potential vorticity (PV) structures on surface cyclogenesis in central-eastern South America using 1979–2017 ERA-Interim reanalysis data. Surface cyclones are identified in three regions (Argentina, Uruguay and SE Brazil) and it is quantified how often PV streamers and PV cutoffs co-occur with cyclogenesis events."

**Fuente:** `papers/files_MD/crespo2020potential.md` (Abstract, líneas 11-17)

PAUSA INICIO: 000125
PAUSA FIN: 000155

---

## Cita 17 — `gramcianinov2019properties` (línea 21, mención en grupo)

**Tesis (ES):**
> este estudio se centra en tres regiones de ciclogénesis documentadas por diversos autores \citep{crespo2020potential, gramcianinov2019properties, reboita2026meteorology}

**Paper original (EN):**
> "There are four main cyclogenesis regions in the South Atlantic Ocean: the Southern Brazilian coast (SE-BR), over the continent near the La Plata river discharge region (LA PLATA), the southeastern coast of Argentina (ARG) and the Southeastern..."

**Fuente:** `papers/files_MD/gramcianinov2019properties.md` (Abstract, líneas 7-16)

PAUSA INICIO: 000205
PAUSA FIN: 000235

---

## Cita 18 — `reboita2026meteorology` (línea 21, mención en grupo)

**Tesis (ES):**
> este estudio se centra en tres regiones de ciclogénesis documentadas por diversos autores \citep{crespo2020potential, gramcianinov2019properties, reboita2026meteorology}

**Paper original (EN):**
> "Among the factors that favour the cyclogenetic potential along eastern SA are the mid-upper-level baroclinic waves..., lee effect of the Andes topography, advection of warm and moist air by the SALLJ and by the SASA northward flow, sea-air turbulent heat fluxes, and baroclinic instability originating from the SST gradient..." (misma sección que la Cita 15, referida aquí como respaldo adicional de las regiones de ciclogénesis).

**Fuente:** `papers/files_MD/reboita2026meteorology.md` (Cap. 8, líneas 640-650)

PAUSA INICIO: 000240
PAUSA FIN: 000310

---

## Cita 19 — `gramcianinov2019properties` (línea 21, `\citet` — propuesta de delimitación)

**Tesis (ES):**
> delimitadas siguiendo la propuesta de \citet{gramcianinov2019properties}: la Sur-Sudeste de Brasil (*Southeast Brazil*, SBR), la cuenca de descarga del Río de la Plata (*La Plata Basin*, LPB) y la costa sureste de Argentina (*Argentina*, ARG).

**Paper original (EN):**
> "There are four main cyclogenesis regions in the South Atlantic Ocean: the Southern Brazilian coast (SE-BR, 30°S), over the continent near the La Plata river discharge region (LA PLATA, 35°S–40°S–55°S), the southeastern coast of Argentina (ARG, 45°S–10°W–35°S) and the Southeastern..."

**Fuente:** `papers/files_MD/gramcianinov2019properties.md` (Abstract, líneas 13-17; coordenadas de las cajas de región repetidas en la Sección 2, líneas 80-158)

PAUSA INICIO: 000320
PAUSA FIN: 000350

---

## Cita 20 — `vera2002cold` (línea 24)

**Tesis (ES):**
> Al este de los Andes, la convergencia de viento en niveles bajos favorece las condiciones que producen precipitaciones intensas en el sureste de Sudamérica, cuya liberación de calor latente retroalimenta y refuerza la intensificación del sistema \citep{vera2002cold}.

**Paper original (EN):**
> "...enhanced moisture transports from tropical latitudes along the eastern portion of the low-level cyclone favor precipitation occurrence over southeastern South America. Those precipitation processes seem to provide a diabatic source of energy that further contributes to the strengthening of the low-level cyclone."

**Fuente:** `papers/files_MD/vera2002cold.md` (Abstract, líneas 28-31)

PAUSA INICIO: 000402
PAUSA FIN: 000432

---

## Cita 21 — `reboita2022from` (línea 25, primera mención)

**Tesis (ES):**
> como demuestran \citet{reboita2022from}, los flujos turbulentos de calor superficiales en el flanco oriental del ciclón no solo inestabilizan la atmósfera, sino que actúan como fuente diabática que refuerza la intensidad del sistema.

**Paper original (EN):**
> "Strong surface heat fluxes, a deep moist troposphere, and the vertical alignment of the warm seclusion with an upper-level cut-off pattern provided the adequate environment for organising convection and, consequently, for subtropical transition at 0600 UTC 28 June. The fundamental role of the surface turbulent heat fluxes for the transition is confirmed through numerical experiments."

**Fuente:** `papers/files_MD/reboita2022from.md` (Abstract, líneas 36-40)

PAUSA INICIO: 000443
PAUSA FIN: 000513

---

## Cita 22 — `gentile2025response` (línea 27)

**Tesis (ES):**
> En esta misma línea, \citet{gentile2025response} anticipan, mediante modelaciones de alta resolución, que el sector cálido de los ETC más intensos se intensificará en un clima futuro, incrementando significativamente los vientos y la precipitación durante sus etapas de desarrollo.

**Paper original (EN):**
> "Instead, compositing the 100 most intense midlatitude cyclones in the North Atlantic, we find that the warm sector exhibits statistically significant increases in wind speed and precipitation of up to 15% locally per degree of warming, while changes in the cold sector are less pronounced."

**Fuente:** `papers/files_MD/gentile2025response.md` (Abstract, líneas 100-102)

PAUSA INICIO: 000523
PAUSA FIN: 000553

---

## Cita 23 — `corner2025classification` (línea 35)

**Tesis (ES):**
> \citet{corner2025classification} muestran que la intensidad de un ciclón no puede capturarse con una única métrica, dado que las relaciones entre distintas medidas de intensidad —incluida la de los vientos en superficie— no son lineales entre sí,

**Paper original (EN):**
> "The question of how to quantify the intensity of extratropical cyclones (ETCs) does not have a simple answer... We show that dynamical intensity measures correlate strongly with each other, while correlations are weaker for impact-relevant measures."

**Fuente:** `papers/files_MD/corner2025classification.md` (Abstract, líneas 16-32)

PAUSA INICIO: 000604
PAUSA FIN: 000634

---

## Cita 24 — `sinclair2023relationship` (línea 35)

**Tesis (ES):**
> y \citet{sinclair2023relationship} confirman este límite al advertir que un ETC puede ser dinámicamente intenso pero generar poca lluvia si carece del suministro de humedad adecuado.

**Paper original (EN):**
> "Not all ETC types exhibit a strong dependency between precipitation and maximum vorticity. ETCs located at high latitudes with weak precipitation show little dependency due to the lack of moisture..."

**Fuente:** `papers/files_MD/sinclair2023relationship.md` (Abstract, líneas 30-33)

PAUSA INICIO: 000643
PAUSA FIN: 000713

---

## Cita 25 — `cardoso2022synoptic` (línea 36)

**Tesis (ES):**
> A esta insuficiencia escalar se suma una insuficiencia posicional: los máximos de viento no se distribuyen uniformemente alrededor del centro del ciclón, sino que se concentran en cuadrantes específicos cuya ubicación varía con estructuras de mesoescala y con la fase del ciclo de vida \citep{cardoso2022synoptic, eisenstein2023identification}

**Paper original (EN):**
> "Eulerian and Lagrangian approaches indicate extreme wind speed in the east and northeast of subtropical cyclogenesis region (RG1)... The positive anomalies of the wind speed to the east of RG1... are in line with Gozzo et al. (2014), who found the maximum winds between 350 and 450 km away from the cyclone center... the six SCs analyzed by Reboita, da Rocha, et al. (2019) also presented more intense winds occupying their east and southeast quadrant."

**Fuente:** `papers/files_MD/cardoso2022synoptic.md` (Key Points, líneas 12-15; cuerpo, líneas 468-474)

PAUSA INICIO: 000727
PAUSA FIN: 000757

---

## Cita 26 — `eisenstein2023identification` (línea 36)

**Tesis (ES):**
> A esta insuficiencia escalar se suma una insuficiencia posicional: los máximos de viento no se distribuyen uniformemente alrededor del centro del ciclón, sino que se concentran en cuadrantes específicos cuya ubicación varía con estructuras de mesoescala y con la fase del ciclo de vida \citep{cardoso2022synoptic, eisenstein2023identification}

**Paper original (EN):**
> "These high winds are mostly associated with five mesoscale features: the warm (conveyor belt) jet (WJ); the cold (conveyor belt) jet (CJ); cold frontal convection (CFC); strong cold-sector (CS) winds; and, in some cases, the sting jet (SJ). The timing within the cyclone's life cycle, the location relative to the cyclone core and further characteristics differ between these features..."

**Fuente:** `papers/files_MD/eisenstein2023identification.md` (Abstract, líneas 15-23)

PAUSA INICIO: 000807
PAUSA FIN: 000837

---

## Cita 27 — `pepler2020dimensional` (línea 37)

**Tesis (ES):**
> Esta insuficiencia se confirma también en el HS, donde \citet{pepler2020dimensional} muestran, para el sureste de Australia, que los ciclones sustentados en niveles verticales altos presentan vientos e intensidad de lluvia sistemáticamente mayores que los ciclones configurados solo en niveles bajos.

**Paper original (EN):**
> "Using a combination of reanalysis data and satellite-based rainfall and lightning, we show that in southeast Australia deep cyclones have higher intensities, longer durations, and more severe winds and rainfall than either shallow surface cyclones or upper-level cyclones with no surface low..."

**Fuente:** `papers/files_MD/pepler2020dimensional.md` (Abstract, líneas 13-17)

PAUSA INICIO: 000847
PAUSA FIN: 000917

---

## Cita 28 — `gozzo2013air` (línea 38, segunda mención)

**Tesis (ES):**
> En Sudamérica, los estudios de caso de \citet{gozzo2013air} y \citet{reboita2022from} han revelado, en este mismo sentido, que los ciclones regionales pueden exhibir evoluciones que se apartan de los modelos tradicionales

**Paper original (EN):**
> "This study analyzes... a non-explosive Shapiro–Keyser type cyclogenesis event that occurred over the southwestern South Atlantic Ocean. The synoptic evolution shows a relatively strong warm front and a cold frontal fracture during the system's development and a warm seclusion in its mature stage, characterizing a Shapiro–Keyser type cyclone." (mismo pasaje que la Cita 12; reutilizado aquí como ejemplo de evolución que se aparta del modelo clásico de ciclón).

**Fuente:** `papers/files_MD/gozzo2013air.md` (Abstract, líneas 8-16)

PAUSA INICIO: 000924
PAUSA FIN: 000954

---

## Cita 29 — `reboita2022from` (línea 38, segunda mención)

**Tesis (ES):**
> En Sudamérica, los estudios de caso de \citet{gozzo2013air} y \citet{reboita2022from} han revelado, en este mismo sentido, que los ciclones regionales pueden exhibir evoluciones que se apartan de los modelos tradicionales

**Paper original (EN):**
> "However, in June 2021, an unusual cyclone developed near the boundary of Uruguay and southern Brazil, initially having extratropical features and later undergoing a subtropical transition... the cyclone presented a frontal T-bone pattern and warm seclusion, following the Shapiro–Keyser development model." (mismo pasaje que la Cita 21; reutilizado aquí como ejemplo de evolución atípica).

**Fuente:** `papers/files_MD/reboita2022from.md` (Abstract, líneas 16-34)

PAUSA INICIO: 000958
PAUSA FIN: 001028

---

## Cita 30 — `chen2025characteristics` (línea 39)

**Tesis (ES):**
> \citet{chen2025characteristics} muestran que su coocurrencia —si bien relativamente poco frecuente— no es despreciable, por lo que caracterizar la morfología superficial del sistema exige analizar ambas variables de forma conjunta

**Paper original (EN):**
> "When one type of extreme is observed, the probability that it is a compound wind-precipitation extreme reaches up to 40% along the coasts and ocean, and about 20% in the NNA region. About 90% of compound wind and precipitation extremes in NNA (which occur most frequently in fall) are associated with ETCs."

**Fuente:** `papers/files_MD/chen2025characteristics.md` (Abstract, líneas 19-23)

PAUSA INICIO: 001038
PAUSA FIN: 001108

---

## Cita 31 — `han2025system` (línea 40, primera mención)

**Tesis (ES):**
> \citet{han2025system} enfatizan, en consecuencia, que se requieren marcos de clasificación que vinculen explícitamente la evolución del sistema con sus manifestaciones de viento y precipitación,

**Paper original (EN):**
> "We propose the first unified objective framework (SyCLoPS) for detecting and classifying all types of low-pressure systems (LPSs) in a given dataset... The framework is useful to study the frequency, structure, development, wind impact, and precipitation contribution of each type of LPS."

**Fuente:** `papers/files_MD/han2025system.md` (Abstract, líneas 11-17)

PAUSA INICIO: 001118
PAUSA FIN: 001148

---

## Cita 32 — `kaylee2025convection` (línea 40)

**Tesis (ES):**
> necesidad que campañas de observación aerotransportadas han vuelto más evidente al confirmar la presencia de convección interna invisible para los productos de resolución convencional \citep{kaylee2025convection}.

**Paper original (EN):**
> "Elevated potential instability (EPI) often occurs in the comma head of wintertime extratropical cyclones as air within the storm's dry slot moves above a warm or occluded frontal zone. Lifting of EPI layers may result in elevated convection, enhanced snowfall, and thundersnow. High-Resolution Rapid Refresh (HRRR) initialization values... are used to analyze EPI characteristics along tracks of the NASA Earth Resources-2 (ER-2) aircraft within the comma head of 14 cyclones sampled during the... (IMPACTS) campaign."

**Fuente:** `papers/files_MD/kaylee2025convection.md` (Abstract, líneas 10-16)

PAUSA INICIO: 001159
PAUSA FIN: 001229

---

## Cita 33 — `priestley2022improved` (línea 41)

**Tesis (ES):**
> \citet{priestley2022improved} demuestran que los modelos de baja resolución subestiman los vientos extremos asociados a los ciclones al no resolver explícitamente sus estructuras de mesoescala,

**Paper original (EN):**
> "General circulation models are broadly able to capture the shape and structure of extratropical cyclones... However, the intensity of cyclones, and the strength of their winds, are commonly underestimated in models... HighResMIP models show considerable improvements, with a majority of cyclone-scale biases present in the CMIP6 models reduced..."

**Fuente:** `papers/files_MD/priestley2022improved.md` (Abstract, líneas 62-69)

PAUSA INICIO: 001239
PAUSA FIN: 001309

---

## Cita 34 — `neu2013intercomparison` (línea 41)

**Tesis (ES):**
> y \citet{neu2013intercomparison} señalan que la variabilidad en forma y tamaño de los ETC genera divergencias sistemáticas entre métodos de detección, particularmente pronunciadas en regiones de topografía compleja.

**Paper original (EN):**
> "An intercomparison experiment involving 15 commonly used detection and tracking algorithms for extratropical cyclones reveals those cyclone characteristics that are robust between different schemes and those that differ markedly... [cyclones] can range greatly in shape and structure (are often asymmetric), differ rather more in size... In contrast, there are noteworthy discrepancies throughout the Mediterranean, which is of particular societal relevance given the high population density here."

**Fuente:** `papers/files_MD/neu2013intercomparison.md` (líneas 11-27, 282-284)

PAUSA INICIO: 001323
PAUSA FIN: 001353

---

## Cita 35 — `gramcianinov2023impact` (línea 48)

**Tesis (ES):**
> En el HS, los ETC modulan el oleaje regional y representan una amenaza costera recurrente \citep{gramcianinov2023impact},

**Paper original (EN):**
> "This work analyses the extratropical cyclone-related extreme waves in the ocean surface and their trends in the North and South Atlantic Oceans... The hot spot regions of cyclone-related waves occurrence found by the method agree with previous studies and relate to the cyclogenesis region, and storm track orientation."

**Fuente:** `papers/files_MD/gramcianinov2023impact.md` (Abstract, líneas 16-22)

PAUSA INICIO: 001402
PAUSA FIN: 001432

---

## Cita 36 — `sasaki2021intraseasonal` (línea 48)

**Tesis (ES):**
> y \citet{sasaki2021intraseasonal} muestran que esta modulación presenta variabilidad significativa a escala intraestacional en el Atlántico Sur occidental —con un período dominante de aproximadamente 40 días asociado a cambios en el viento en superficie—

**Paper original (EN):**
> "Extratropical cyclones are known to generate extreme significant wave height (swh) values at the ocean surface in the western South Atlantic (wSA), which are highly influenced by intraseasonal scales... The analysis shows that in the western subtropical South Atlantic, the intraseasonal variability of u10 and swh presents a significant signal, with the major peak at approximately 40 d."

**Fuente:** `papers/files_MD/sasaki2021intraseasonal.md` (Abstract, líneas 18-19; Resultados, líneas 341-345)

PAUSA INICIO: 001449
PAUSA FIN: 001519

---

## Cita 37 — `simmonds2000variability` (línea 49)

**Tesis (ES):**
> Esta amenaza no es estática: los registros históricos de 40 años ya muestran una tendencia significativa hacia ciclones de mayor tamaño e intensidad en el HS \citep{simmonds2000variability},

**Paper original (EN):**
> "An analysis of the variability and trends exhibited by many aspects of Southern Hemisphere (SH) mean sea level extratropical cyclones during the period 1958–97 is presented... It is shown that the mean radius of SH extratropical cyclones displays almost everywhere a significant positive trend, and there are also increases in annual mean cyclone 'depth' (i.e., the pressure difference between the center and the 'edge' of a cyclone)."

**Fuente:** `papers/files_MD/simmonds2000variability.md` (Abstract, líneas 11-21)

PAUSA INICIO: 001528
PAUSA FIN: 001558

---

## Cita 38 — `kodama2019perspective` (línea 49)

**Tesis (ES):**
> tendencia que las proyecciones de calentamiento futuro sugieren se profundizará específicamente en la componente de precipitación, con una tasa de escalamiento cercana al 7\%/K \citep{kodama2019perspective}.

**Paper original (EN):**
> "Simulated precipitation from intense oceanic cyclones increases at a rate of 7%/K, following Clausius–Clapeyron, with warming. The same scaling is apparent also in the interhemispheric contrast..."

**Fuente:** `papers/files_MD/kodama2019perspective.md` (Abstract, líneas 21-24)

PAUSA INICIO: 001608
PAUSA FIN: 001638

---

## Cita 39 — `bartolomei2024extremos` (línea 50)

**Tesis (ES):**
> En el litoral sur de Brasil, \citet{bartolomei2024extremos} documentan la letalidad y los impactos socioeconómicos causados por ciclones extratropicales invernales,

**Paper original (PT — idioma original del artículo, Terræ Didatica):**
> "Resumo: Introdução. No inverno de 2023, dois ciclones de escala sinótica foram responsáveis por cerca de 17 óbitos e vários prejuízos no sul do Brasil... Conclusão. Ao se deslocar para sudeste, o ciclone causou precipitação e ventos fortes sobre o continente até que estivesse completamente sobre o oceano."

**Fuente:** `papers/files_MD/bartolomei2024extremos.md` (Resumo, líneas 26-40)

PAUSA INICIO: 001653
PAUSA FIN: 001723

---

## Cita 40 — `miranda2026patterns` (línea 50)

**Tesis (ES):**
> mientras que \citet{miranda2026patterns} confirman que estos sistemas son los principales motores de tormentas costeras en el litoral sur de Brasil;

**Paper original (EN):**
> "Extratropical cyclones are the main drivers of high-energy wave events along the southern coast of Brazil, frequently producing hazardous coastal conditions. Between 2001 and 2020, we identified 51 high-impact coastal storms based on Marine Weather Warnings and ERA5 reanalysis."

**Fuente:** `papers/files_MD/miranda2026patterns.md` (Abstract, líneas 29-31)

PAUSA INICIO: 001732
PAUSA FIN: 001802

---

## Cita 41 — `bitencourt2010relating` (línea 50)

**Tesis (ES):**
> la asociación directa entre el viento observado en la costa y estos sistemas confirma, además, la ocurrencia de pérdidas socioeconómicas asociadas \citep{bitencourt2010relating}.

**Paper original (EN):**
> "Intense wind events at the southern Brazilian coast cause severe socio-economic losses. Generally, such events have been associated with extratropical cyclones over the Southwest Atlantic Ocean. The purpose of this study is to identify favoured locations and the processes through which the winds are associated with the extratropical cyclones."

**Fuente:** `papers/files_MD/bitencourt2010relating.md` (Abstract, líneas 14-16)

PAUSA INICIO: 001811
PAUSA FIN: 001841

---

## Cita 42 — `han2025system` (línea 51, segunda mención)

**Tesis (ES):**
> contribuiría con evidencia regional al esfuerzo internacional, señalado por \citet{han2025system}, de construir marcos de clasificación objetiva que vinculen explícitamente la evolución del sistema con sus manifestaciones de superficie.

**Paper original (EN):**
> "We propose the first unified objective framework (SyCLoPS) for detecting and classifying all types of low-pressure systems (LPSs) in a given dataset... The framework is useful to study the frequency, structure, development, wind impact, and precipitation contribution of each type of LPS." (mismo pasaje que la Cita 31).

**Fuente:** `papers/files_MD/han2025system.md` (Abstract, líneas 11-17)

PAUSA INICIO: 001846
PAUSA FIN: 001917

---

## Cita 43 — `hersbach2020era5` (línea 53)

**Tesis (ES):**
> Primero, la disponibilidad del reanálisis ERA5 \citep{hersbach2020era5}, cuya resolución espacial ($\sim$31 km) y temporal (horaria) permite resolver los gradientes de presión y los flujos de humedad que generaciones anteriores de datos suavizaban;

**Paper original (EN):**
> "In addition to a significantly enhanced horizontal resolution of 31 km, compared to 80 km for ERA-Interim, ERA5 has hourly output throughout, and an uncertainty estimate from an ensemble (3-hourly at half the horizontal resolution)."

**Fuente:** `papers/files_MD/hersbach2020era5.md` (Abstract, líneas 17-33)

PAUSA INICIO: 001926
PAUSA FIN: 001956

---

## Cita 44 — `gramcianinov2020analysis` (línea 53, segunda mención)

**Tesis (ES):**
> validaciones específicas para la región \citep{gramcianinov2020analysis} y comparaciones frente a otras fuentes de datos para la detección de ciclogénesis en Sudamérica \citep{dalanhese2023new} respaldan esta elección,

**Paper original (EN):**
> "This work aims to analyze and compare ERA5 and CFSR/CFSv2 data from 1979 to 2019 with 1-hourly outputs, regarding their ability to reproduce storm tracks and the main characteristics of cyclones at middle and high latitudes in the North Atlantic (NA) and South Atlantic (SA) Oceans." (mismo pasaje que la Cita 8; reutilizado como validación de ERA5 para la región).

**Fuente:** `papers/files_MD/gramcianinov2020analysis.md` (Abstract, líneas 13-16)

PAUSA INICIO: 002002
PAUSA FIN: 002032

---

## Cita 45 — `dalanhese2023new` (línea 53)

**Tesis (ES):**
> y comparaciones frente a otras fuentes de datos para la detección de ciclogénesis en Sudamérica \citep{dalanhese2023new} respaldan esta elección, aunque ERA5 presenta sesgos conocidos en la representación de los extremos más intensos

**Paper original (EN):**
> "A new climatology of South American extratropical cyclogenesis with an intercomparison among ERA5, JRA55 and the Brazilian Navy... By supplementing an observational record with current reanalysis data, this study reveals the general characteristics of cyclones that develop in the lee regions of the Andes and those that develop nearer the Atlantic coast."

**Fuente:** `papers/files_MD/dalanhese2023new.md` (título y Abstract, líneas 4-30)

PAUSA INICIO: 002044
PAUSA FIN: 002114

---

## Cita 46 — `coutodesouza2024new` (línea 54, primera mención)

**Tesis (ES):**
> Segundo, la base de datos de trayectorias de \citet{coutodesouza2024new}, fundamentada en el seguimiento por vorticidad relativa a 850 hPa ($\zeta_{850}$) en lugar de la presión al nivel del mar, [...] que además incorpora la segmentación objetiva del algoritmo \textit{CycloPhaser}, la cual define cuatro fases dinámicas discretas —incipiente, intensificación, madurez y decaimiento—

**Paper original (EN):**
> "This study introduces new insights into the climatology of South Atlantic (SAt) cyclones by employing a novel cyclone life cycle detection method, the CycloPhaser. Utilizing the minimum relative vorticity series and its derivative at the cyclone centre, the program effectively identifies distinct phases in the cyclone life cycle. Cyclone tracks are obtained through the analysis of relative vorticity at 850 hPa, using the ERA5 dataset... The predominant cyclone type... exhibited a four-phase configuration: incipient, intensification, mature and decay."

**Fuente:** `papers/files_MD/coutodesouza2024new.md` (Abstract, líneas 12-27)

PAUSA INICIO: 002125
PAUSA FIN: 002155

---

## Cita 47 — `deSouza2025CycloPhaser` (línea 54)

**Tesis (ES):**
> y supera las limitaciones de las clasificaciones clásicas en el contexto del Atlántico Sur \citep{deSouza2025CycloPhaser},

**Paper original (EN):**
> "Seminal works by Bjerknes & Solberg (1922), Shapiro & Keyser (1990), Neiman & Shapiro (1993) described extratropical cyclone life cycles in terms of structural changes and large-scale dynamics. However, these classifications were based on manual analysis of satellite imagery and synoptic charts, limiting their applicability to large datasets with multiple cyclone cases... While these approaches support the study of cyclone intensification and decay, they tend to overlook critical phases such as the incipient stage... Additionally, they treat the mature phase as a single time step, failing to account for the possibility that it may encompass multiple time steps."

**Fuente:** `papers/files_MD/deSouza2025CycloPhaser.md` (Statement of Need, líneas 62-77)

PAUSA INICIO: 002210
PAUSA FIN: 002240

---

## Cita 48 — `shapiro1990life` (línea 54)

**Tesis (ES):**
> en sintonía con el marco de referencia que ofrece el modelo Shapiro-Keyser \citep{shapiro1990life,shapiro1999bridge} para interpretar la distribución espacial de los máximos de viento y precipitación

**Paper original (EN):**
> "Fig. 10.14. Sea-level temperature (°C, solid lines) and sea-level pressure (mb, dashed lines) from a 24-h numerical simulation of the QE II marine cyclogenesis by the Penn State/NCAR regional model: (a) incipient frontal cyclone; (b) frontal fracture; (c) frontal T-Bone and bent-back warm front; (d) warm-core seclusion."

**Fuente:** `papers/files_MD/shapiro1990life.md` (Cap. 10, líneas 1344-1350)

PAUSA INICIO: 002251
PAUSA FIN: 002321

---

## Cita 49 — `shapiro1999bridge` (línea 54)

**Tesis (ES):**
> en sintonía con el marco de referencia que ofrece el modelo Shapiro-Keyser \citep{shapiro1990life,shapiro1999bridge} para interpretar la distribución espacial de los máximos de viento y precipitación

**Paper original (EN):**
> "When confronted by such a variety of conceptual models, one might ask: Is the T-bone bent-back warm-front seclusion (Shapiro and Keyser 1990) similar to a back-bent warm frontal occlusion (Bjerknes and Solberg 1922; Bjerknes 1930; Bergeron 1934, 1937) or an instant occlusion (McGinnigle et al. 1988)?"

**Fuente:** `papers/files_MD/shapiro1999bridge.md` (líneas 54-61)

PAUSA INICIO: 002331
PAUSA FIN: 002401

---

## Cita 50 — `liang2018multivariate` (línea 55)

**Tesis (ES):**
> el análisis de Funciones Ortogonales Empíricas Multivariadas (MEOF) permite extraer modos de variabilidad inherentemente acoplados entre variables físicamente distintas \citep{liang2018multivariate},

**Paper original (EN):**
> "The multivariate EOF (MEOF) method, a variant of the archetypal EOF method, has been widely used for investigating large-scale atmospheric and oceanic coupled variability structures because of its salient ability to incorporate different variables with their combined variances."

**Fuente:** `papers/files_MD/liang2018multivariate.md` (líneas 115-120)

PAUSA INICIO: 002411
PAUSA FIN: 002441

---

## Cita 51 — `sun2022evaluation` (línea 56)

**Tesis (ES):**
> La utilidad de estos patrones y de sus componentes principales trasciende la caracterización descriptiva, con aplicación práctica incluso en el pronóstico de precipitación \citep{sun2022evaluation},

**Paper original (EN):**
> "Precipitation time series exhibit complex fluctuations and statistical changes... empirical orthogonal function (EOF) and CSEOF analyses are used to examine the periodic changes in the precipitation data. Then, the autoregressive integrated moving average (ARIMA) method is applied to the principal component (PC) time series derived from the EOF and CSEOF precipitation analyses... the EOF–ARIMA composite model and CSEOF–ARIMA composite model are used to obtain quantitative precipitation forecasts."

**Fuente:** `papers/files_MD/sun2022evaluation.md` (Abstract, líneas 12-23)

PAUSA INICIO: 002452
PAUSA FIN: 002522

---

## Cita 52 — `coutodesouza2024new` (línea 62, segunda mención)

**Tesis (ES):**
> los datos de ERA5, la detección dinámica por $\zeta_{850}$ y la clasificación objetiva de fases mediante \textit{CycloPhaser}, ya disponibles en la base de \citet{coutodesouza2024new}, junto con el análisis multivariado (MEOF) desarrollado en esta investigación—

**Paper original (EN):**
> "This study introduces new insights into the climatology of South Atlantic (SAt) cyclones by employing a novel cyclone life cycle detection method, the CycloPhaser... Cyclone tracks are obtained through the analysis of relative vorticity at 850 hPa, using the ERA5 dataset." (mismo pasaje que la Cita 46).

**Fuente:** `papers/files_MD/coutodesouza2024new.md` (Abstract, líneas 12-20)

PAUSA INICIO: 002527
PAUSA FIN: 002557

---


## FIN DEL CAPÍTULO 1

Total de citas procesadas: 52 (de 48 comandos `\cite*`, algunos agrupados con múltiples keys).
PAUSA INICIO [actualización OCR]: 122430
PAUSA FIN [actualización OCR]: 122500
PAUSA INICIO [actualización OCR]: 122513
PAUSA FIN [actualización OCR]: 122543
