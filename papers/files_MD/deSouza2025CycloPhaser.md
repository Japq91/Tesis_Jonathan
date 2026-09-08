CycloPhaser: A Python Package for Detecting
Extratropical Cyclone Life Cycles

Danilo Couto de Souza
Gramcianinov

2, and Ricardo de Camargo 1

1, Pedro Leite da Silva Dias

1, Carolina Barnez

DOI: 10.21105/joss.07363

Software

• Review
• Repository
• Archive

Editor: Hauke Schulz

Reviewers:

• @freemansw1
• @stella-bourdin

Submitted: 18 September 2024
Published: 09 April 2025

License
Authors of papers retain copyright
and release the work under a
Creative Commons Attribution 4.0
International License (CC BY 4.0).

1 Institute of Astronomy, Geophysics and Atmospheric Sciences of the São Paulo University, Rua do
Matão, 226, Cidade Universitária, 05508-090, São Paulo, Brazil 2 Institute for Coastal Systems –
Analysis and Modeling, Helmholtz-Zentrum Hereon, Geesthacht, Germany

Summary

CycloPhaser is a Python package designed to detect and analyze extratropical cyclone life cycles
from central relative vorticity data. It enables researchers in meteorology and atmospheric
sciences to automatically identify key stages of cyclone development, such as intensification,
decay, and mature phases, using the vorticity series and its derivatives. By leveraging vorticity
data, CycloPhaser helps scientists study cyclones across various regions and timeframes,
contributing to improved understanding of cyclone energetics and behavior.

Statement of Need

Extratropical cyclones are key features of the climate system.
In South America, they are
especially important due to the presence of cyclogenesis hotspots in southeast Brazil (SE-BR),
the La Plata River basin (LA-PLATA), and southeastern Argentina (ARG) (C. Gramcianinov
et al., 2019). These cyclones can cause extreme precipitation, intense winds, high sea waves,
and landslides, significantly impacting communities (Cardoso et al., 2022; C. B. Gramcianinov
et al., 2023; D. C. de Souza et al., 2024; D. de Souza & Silva, 2021). Understanding their
temporal and spatial development and evolution is crucial for improving forecasts, ultimately
aiding in the adoption of mitigation and adaptation strategies.

Accurately identifying the regions where cyclones are positioned throughout their distinct life
cycle stages remains a significant challenge in atmospheric sciences. Seminal works by Bjerknes
& Solberg (1922), Shapiro & Keyser (1990), Neiman & Shapiro (1993) described extratropical
cyclone life cycles in terms of structural changes and large-scale dynamics. However, these
classifications were based on manual analysis of satellite imagery and synoptic charts, limiting
their applicability to large datasets with multiple cyclone cases. Recent research has sought
to objectively define cyclone life cycle stages using techniques such as normalizing the life
cycle duration (Rudeva & Gulev, 2007; Schemm et al., 2018) or bisecting the cycle into
“intensification” and “decay” phases by focusing on periods before and after peak vorticity or
the lowest central pressure (Azad & Sorteberg, 2014; Booth et al., 2018; Dacre & Gray, 2009;
Michaelis et al., 2017; Trigo, 2006). While these approaches support the study of cyclone
intensification and decay, they tend to overlook critical phases such as the incipient stage —
where environmental dynamics are still adapting to the developing low-level disturbance and
surface isobars are not yet fully closed. Additionally, they treat the mature phase as a single
time step, failing to account for the possibility that it may encompass multiple time steps
during which the cyclone exhibits homogeneous features.

The pioneering work by Couto de Souza et al. (2024) was the first to offer a comprehensive
analysis of extratropical cyclone life cycles, dissecting systems into distinct life cycle phases

de Souza et al. (2025). CycloPhaser: A Python Package for Detecting Extratropical Cyclone Life Cycles. Journal of Open Source Software, 10(108),
7363. https://doi.org/10.21105/joss.07363.

1

and enabling the detection of multiple configurations across different systems. This study
presents the Python package that facilitated such work. The method allows for an automated
classification of cyclone life cycle stages, enabling the efficient processing of large datasets
with minimal computational cost. This tool opens new avenues for research, such as analyzing
cyclone life cycle behavior in climate change projections, enabling comparisons with present-day
climates, and providing insights into how cyclone life cycles may evolve in response to climate
variability. Additionally, it offers potential for assisting model validation by comparing the
spatial positioning of life cycle phases across different models and reanalysis datasets. The
package is both flexible and fully customizable, making it adaptable to a wide range of datasets
and research needs.

Figure 1: Yearly cyclone track densities normalized for the three cyclogenesis regions along the South
American coast (SE-BR, LA-PLATA, and ARG). Contours represent normalized track densities above
0.8, plotted individually for each region. Details regarding the genesis regions, tracking procedures, and
analysis techniques are discussed in de Couto de Souza et al. (2024).

Features

CycloPhaser requires a time series of relative vorticity data as its primary input. The input
data should represent the minimum central relative vorticity of extratropical cyclones, ideally
at a specified pressure level (e.g., 850 hPa). This vorticity series, which is typically derived
from atmospheric reanalysis datasets, serves as a proxy for cyclone intensity. The series must
be provided as a one-dimensional list or array of vorticity values, which will be analyzed to
detect key life cycle stages of the cyclone. Additional optional input includes a time or label
series for the corresponding vorticity values. Users should ensure the time series corresponds
to regular time steps (e.g., hourly or 6-hourly data).

The program includes optional pre-processing steps, such as applying a Lanczos filter to remove
noise from the series and a Savitzky-Golay filter for smoothing, ensuring sinusoidal patterns
in the data for phase detection. Key cyclone phases — intensification, decay, and mature —
are identified through peaks and valleys in the vorticity time series. The intensification phase
spans from a vorticity peak to the next valley, while the decay phase covers the opposite. The
mature phase is defined as the period between a vorticity valley and neighboring derivative
peaks. The pre-processing steps, as well as peaks and valleys detection in the vorticity series,
are computed using Scipy’s package (Virtanen et al., 2020).

Thresholds for phase detection were rigorously calibrated in Couto de Souza et al. (2024) using
a representative set of cyclone tracks, ensuring accurate phase identification while filtering
out noise. CycloPhaser also includes a residual phase to account for tracking anomalies, such
as post-decay re-intensification without returning to maturity. A post-processing step further
refines the phase boundaries by correcting gaps and isolating single time-step phases. Finally,
the incipient stage is detected by missing labels in the series or by selecting the initial time
steps. More details are discussed in Couto de Souza et al. (2024).

de Souza et al. (2025). CycloPhaser: A Python Package for Detecting Extratropical Cyclone Life Cycles. Journal of Open Source Software, 10(108),
7363. https://doi.org/10.21105/joss.07363.

2

Figure 2: Representative example of a cyclone life cycle exhibiting an incipient-intensification-mature-
decay configuration.

Although the package was initially devised for detecting life cycle phases using relative vorticity,
it could potentially be applied to other time series used as proxies for cyclone detection, such as
sea level pressure (SLP) or wind data. However, it has not yet been explicitly tested for these
variables. Additionally, the program includes a hemisphere option, which enables automatic
adjustment for Northern Hemisphere data by multiplying the series by -1, making the package
compatible with both hemispheres without requiring manual data adjustments. Since this
option was devised with relative vorticity series in mind, using hemisphere="northern" is
also suitable for detecting phases in wind speed data, while hemisphere="southern" is more
appropriate for SLP.

References

Azad, R., & Sorteberg, A. (2014). The Vorticity Budgets of North Atlantic Winter Extratropical
Cyclone Life Cycles in MERRA Reanalysis. Part I: Development Phase. Journal of the
Atmospheric Sciences, 71(9), 3109–3128. https://doi.org/10.1175/jas-d-13-0267.1

Bjerknes, J., & Solberg, H. (1922). Life Cycle of Cyclones and the Polar Front Theory of
Atmospheric Circulation. Grondahl. https://doi.org/10.1175/1520-0493(1922)50%3C468:
JBAHSO%3E2.0.CO;2

Booth, J. F., Naud, C. M., & Jeyaratnam, J. (2018). Extratropical Cyclone Precipitation
Life Cycles: A Satellite-Based Analysis. Geophysical Research Letters, 45(16), 8647–8654.
https://doi.org/10.1029/2018gl078977

Cardoso, A. A., Rocha, R. P. da, & Crespo, N. M. (2022). Synoptic Climatology of Subtropical
Cyclone Impacts on Near-Surface Winds Over the South Atlantic Basin. Earth and Space
Science, 9(11), e2022EA002482. https://doi.org/10.1029/2022ea002482

Couto de Souza, D., Silva Dias, P. L. da, Gramcianinov, C. B., Silva, M. B. L. da, & Camargo,

de Souza et al. (2025). CycloPhaser: A Python Package for Detecting Extratropical Cyclone Life Cycles. Journal of Open Source Software, 10(108),
7363. https://doi.org/10.21105/joss.07363.

3

R. de. (2024). New perspectives on South Atlantic storm track through an automatic
method for detecting extratropical cyclones’ lifecycle. International Journal of Climatology,
44(10), 3568–3588. https://doi.org/10.1002/joc.8539

Dacre, H. F., & Gray, S. L. (2009). The Spatial Distribution and Evolution Characteristics of
North Atlantic Cyclones. Monthly Weather Review, 137 (1), 99–115. https://doi.org/10.
1175/2008mwr2491.1

Gramcianinov, C. B., Camargo, R. de, Campos, R. M., Guedes Soares, C., & Silva Dias,
P. L. da. (2023).
Impact of extratropical cyclone intensity and speed on the extreme
wave trends in the Atlantic Ocean. Climate Dynamics, 60(5-6), 1447–1466. https:
//doi.org/10.21203/rs.3.rs-995499/v1

Gramcianinov, C., Hodges, K., & Camargo, R. de. (2019). The properties and genesis
environments of South Atlantic cyclones. Climate Dynamics, 53, 4115–4140. https:
//doi.org/10.1007/s00382-019-04778-1

Michaelis, A. C., Willison, J., Lackmann, G. M., & Robinson, W. A. (2017). Changes in
Winter North Atlantic Extratropical Cyclones in High-Resolution Regional Pseudo–Global
Warming Simulations. Journal of Climate, 30(17), 6905–6925. https://doi.org/10.1175/
jcli-d-16-0697.1

Neiman, P. J., & Shapiro, M. (1993). The Life Cycle of an Extratropical Marine Cyclone.
Part I: Frontal-Cyclone Evolution and Thermodynamic Air-Sea Interaction. Monthly
Weather Review, 121(8), 2153–2176. https://doi.org/10.1175/1520-0493(1993)121%
3C2153:tlcoae%3E2.0.co;2

Rudeva, I., & Gulev, S. K. (2007). Climatology of Cyclone Size Characteristics and Their
Changes during the Cyclone Life Cycle. Monthly Weather Review, 135(7), 2568–2587.
https://doi.org/10.1175/mwr3420.1

Schemm, S., Sprenger, M., & Wernli, H. (2018). When during Their Life Cycle Are Extratropical
Cyclones Attended by Fronts? Bulletin of the American Meteorological Society, 99(1),
149–165. https://doi.org/10.1175/bams-d-16-0261.1

Shapiro, M. A., & Keyser, D. (1990). Fronts, Jet Streams and the Tropopause. Springer.

https://doi.org/10.1007/978-1-944970-33-8_10

Souza, D. C. de, Crespo, N. M., Silva, D. V. da, Harada, L. M., Godoy, R. M. P. de,
Domingues, L. M., Luiz, R., Bortolozo, C. A., Metodiev, D., Andrade, M. R. M. de,
(2024). Extreme rainfall and landslides as a response to human-induced
& others.
climate change: a case study at Baixada Santista, Brazil, 2020. Natural Hazards, 1–26.
https://doi.org/10.1007/s11069-024-06621-1

Souza, D. de, & Silva, R. R. da. (2021). Ocean-Land Atmosphere Model (OLAM) performance
for major extreme meteorological events near the coastal region of southern Brazil. Climate
Research, 84, 1–21. https://doi.org/10.3354/cr01651

Trigo, I. F. (2006). Climatology and interannual variability of storm-tracks in the Euro-Atlantic
sector: a comparison between ERA-40 and NCEP/NCAR reanalyses. Climate Dynamics,
26(2), 127–143. https://doi.org/10.1007/s00382-005-0065-9

Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D.,
Burovski, E., Peterson, P., Weckesser, W., Bright, J., & others. (2020). SciPy 1.0:
fundamental algorithms for scientific computing in Python. Nature Methods, 17 (3),
261–272. https://doi.org/10.1038/s41592-019-0686-2

de Souza et al. (2025). CycloPhaser: A Python Package for Detecting Extratropical Cyclone Life Cycles. Journal of Open Source Software, 10(108),
7363. https://doi.org/10.21105/joss.07363.

4

