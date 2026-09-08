# Verificación de citas — Capítulo 3: Metodología

Fuente tesis: `tex_es/03.vr3_metodos.tex`
Formato por entrada: (1) frase/oración de la tesis en español, (2) frase/párrafo equivalente del paper original en su idioma original, (3) fuente, (4) marcas de pausa real de 30s con hora `HHMMSS` (para auditoría).

---

## Cita 1 — `hersbach2020era5` (línea 12)

**Tesis (ES):**
> Se utiliza el reanálisis de quinta generación del ECMWF, ERA5 \citep{hersbach2020era5},

**Paper original (EN):**
> "ERA5 is based on the Integrated Forecasting System (IFS) Cy41r2 which was operational in 2016. ERA5 thus benefits from a decade of developments in model physics, core dynamics and data assimilation. In addition to a significantly enhanced horizontal resolution of 31 km..." (mismo pasaje que la Cita 43 del Cap. 1).

**Fuente:** `papers/files_MD/hersbach2020era5.md` (Abstract, líneas 21-33)

PAUSA INICIO: 013039
PAUSA FIN: 013109

---

## Cita 2 — `hersbach_era5_2023b` (línea 12)

**Tesis (ES):**
> mediante el conjunto de datos \textit{``ERA5 hourly data on single levels from 1940 to present''} \citep{hersbach_era5_2023b} para el período 1979--2020.

**Paper original:** FUENTE NO ENCONTRADA — no existe archivo `hersbach_era5_2023b.md` ni `.pdf` en `papers/files_MD/` ni `papers/files_PDF/`. Es probable que corresponda a la entrada de cita del *dataset* de Copernicus Climate Data Store (DOI, no un artículo de revista), por lo que podría no requerir PDF propio — verificar la entrada en `bibliografia.bib` y, si aplica, el DOI del CDS directamente.

**Fuente:** No disponible en el repositorio de papers.

PAUSA INICIO: 013118
PAUSA FIN: 013148

---

## Cita 3 — `gramcianinov2020analysis` (línea 13)

**Tesis (ES):**
> y su mayor densidad de trayectorias y representación de estructuras de mesoescala frente a reanálisis previos \citep{gramcianinov2020analysis},

**Paper original (EN):**
> "This work aims to analyze and compare ERA5 and CFSR/CFSv2 data from 1979 to 2019 with 1-hourly outputs, regarding their ability to reproduce storm tracks and the main characteristics of cyclones at middle and high latitudes... The use of 1-hourly fields improves tracking in areas with complex terrains, such as the lee of Andes (SA) and Greenland (NA)." (mismo pasaje que la Cita 8 del Cap. 1).

**Fuente:** `papers/files_MD/gramcianinov2020analysis.md` (Abstract, líneas 13-22)

PAUSA INICIO: 013154
PAUSA FIN: 013224

---

## Cita 4 — `chen2024evaluation` (línea 14)

**Tesis (ES):**
> No obstante, \citet{chen2024evaluation} demuestran que ERA5 subestima sistemáticamente los extremos del 5\% de ciclones extratropicales más intensos, con sesgos del $-10.2\%$ en viento y $-22.6\%$ en precipitación respecto a observaciones en Estados Unidos de América.

**Paper original (EN):**
> "Compared to the averaged ETCs, ERA5's performance deteriorates for the top 5% extreme ETCs with a stronger tendency to underestimate both wind speed and precipitation (NMB of −10.2% and −22.6%, respectively). Furthermore, ERA5's skill is worse for local extreme values within ETCs than for spatial averages."

**Fuente:** `papers/files_MD/chen2024evaluation.md` (líneas 44-52)

PAUSA INICIO: 013236
PAUSA FIN: 013306

---

## Cita 5 — `gramcianinov2020analysis` (línea 30, segunda mención)

**Tesis (ES):**
> El punto de partida es el catálogo de trayectorias desarrollado por \citet{gramcianinov2020analysis} a partir de ERA5, cuya alta resolución permite capturar sistemas de mesoescala y ciclogénesis en la región de estudio.

**Paper original (EN):**
> "The cyclone tracking was based on relative vorticity at 850 hPa and the intensity is measured using the maximum 10-m wind speed. The climatology produced for both datasets shows the main characteristics of the NA and SA storm tracks, such as seasonal variability and genesis regions. The use of 1-hourly fields improves tracking in areas with complex terrains..."

**Fuente:** `papers/files_MD/gramcianinov2020analysis.md` (Abstract, líneas 16-22)

PAUSA INICIO: 013312
PAUSA FIN: 013342

---

## Cita 6 — `coutodesouza2024new` (línea 35)

**Tesis (ES):**
> Sobre esta base, \citet{coutodesouza2024new} incorporan una clasificación objetiva de las fases evolutivas mediante el algoritmo \textit{CycloPhaser} \citep{deSouza2025CycloPhaser}, que evalúa la tasa de cambio de la vorticidad relativa en 850 hPa ($\zeta_{850}$) para segmentar matemáticamente el desarrollo y decaimiento de cada sistema.

**Paper original (EN):**
> "It identifies the phases by analysing the relative vorticity at the cyclone centre and its first derivative (Figure 1)." (mismo pasaje que la Cita 18 del Cap. 2).

**Fuente:** `papers/files_MD/coutodesouza2024new.md` (líneas 126-128)

PAUSA INICIO: 013347
PAUSA FIN: 013417

---

## Cita 7 — `deSouza2025CycloPhaser` (línea 35)

**Tesis (ES):**
> mediante el algoritmo \textit{CycloPhaser} \citep{deSouza2025CycloPhaser},

**Paper original (EN):**
> "CycloPhaser is a Python package designed to detect and analyze extratropical cyclone life cycles from central relative vorticity data. It enables researchers... to automatically identify key stages of cyclone development, such as intensification, decay, and mature phases, using the vorticity series and its derivatives."

**Fuente:** `papers/files_MD/deSouza2025CycloPhaser.md` (líneas 43-48)

PAUSA INICIO: 013422
PAUSA FIN: 013452

---

## Cita 8 — `gramcianinov2019properties` (línea 46)

**Tesis (ES):**
> delimitadas según la taxonomía de \citet{gramcianinov2019properties} y detalladas en la Tabla~\ref{tab:regiones_coords}.

**Paper original (EN):**
> "There are four main cyclogenesis regions in the South Atlantic Ocean: the Southern Brazilian coast (SE-BR, 30°S), over the continent near the La Plata river discharge region (LA PLATA, 35°S–40°S–55°S), the southeastern coast of Argentina (ARG, 45°S–10°W–35°S) and the Southeastern..." (mismo pasaje que la Cita 19 del Cap. 1).

**Fuente:** `papers/files_MD/gramcianinov2019properties.md` (Abstract, líneas 13-17; coordenadas, líneas 80-158)

PAUSA INICIO: 013458
PAUSA FIN: 013528

---

## Cita 9 — `rieger2024xeofs` (línea 140)

**Tesis (ES):**
> La implementación utiliza la biblioteca \texttt{xeofs} \citep{rieger2024xeofs} sobre estructuras \texttt{xarray} \citep{hoyer2017xarray}.

**Paper original (EN):**
> "xeofs is a Python package tailored for the climate science community, designed to streamline advanced data analysis using dimensionality reduction techniques like Empirical Orthogonal Functions (EOF) analysis – often called Principal Component Analysis (PCA) in other domains. Integrating seamlessly with xarray objects (Hoyer & Hamman, 2017), makes it easier to analyze large, labeled, multi-dimensional datasets."

**Fuente:** `papers/files_MD/rieger2024xeofs.md` (líneas 15-21)

PAUSA INICIO: 013539
PAUSA FIN: 013609

---

## Cita 10 — `hoyer2017xarray` (línea 140) — [CITA ELIMINADA DE LA TESIS]

**Tesis (ES, texto original antes de la corrección):**
> sobre estructuras \texttt{xarray} \citep{hoyer2017xarray}.

**Paper original:** FUENTE NO ENCONTRADA — no existe archivo `hoyer2017xarray.md` ni `.pdf` en `papers/files_MD/` ni `papers/files_PDF/`.

**Acción tomada:** por instrucción del usuario, se eliminó `\citep{hoyer2017xarray}` del archivo `tex_es/03.vr3_metodos.tex` (línea 140). La oración quedó como: "La implementación utiliza la biblioteca \texttt{xeofs} \citep{rieger2024xeofs} sobre estructuras \texttt{xarray}." — se conserva la mención a la librería `xarray` pero sin atribución bibliográfica no verificable. La entrada correspondiente en `bibliografia.bib` no fue eliminada (queda simplemente sin usar, lo cual no genera error de compilación).

**Fuente:** No disponible en el repositorio de papers (Hoyer & Hamman, "xarray: N-D labeled arrays and datasets in Python", *Journal of Open Research Software*, 2017).

PAUSA INICIO: 013619
PAUSA FIN: 013649

---

## Cita 11 — `wilks2019statistical_ch13` (línea 202)

**Tesis (ES):**
> Este factor escalar preserva la estructura espacial de los gradientes mientras equilibra el peso de ambas variables en la matriz de covarianza, evitando que el campo de mayor varianza domine artificialmente la descomposición conjunta \citep{wilks2019statistical_ch13}.

**Paper original (EN):**
> "Because the variances of the temperature variables are so much larger than the variances of the precipitation variables, the PCA calculated from the covariance matrix is dominated by the temperatures. The eigenvector elements corresponding to the two precipitation variables are negligibly small in the first four eigenvectors, so these variables make negligible contributions to the first four principal components... Since the correlation matrix is the covariance matrix for comparably scaled variables, each has equal variance. Unlike the analysis on the covariance matrix, this PCA does not ignore the precipitation..."

**Fuente:** `papers/files_MD/wilks2019statistical_ch13.md` (líneas 489-504, Sección 13.2)

PAUSA INICIO: 013708
PAUSA FIN: 013738

---


## FIN DEL CAPÍTULO 3

Total de citas procesadas: 11.
