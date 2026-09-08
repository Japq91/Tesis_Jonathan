RESEARCH LETTER
10.1029/2024GL112570

Key Points:
• Using kilometer‐scale eXperimental

System for High‐resolution prediction
on Earth‐to‐Local Domains
(X‐SHiELD) we capture fine details of
warm and cold sectors of midlatitude
cyclones, underrepresented in CMIP
models

• Under +4K warming, X‐SHiELD

simulations show a poleward shift in
midlatitude cyclone tracks consistent
with CMIP projections

• The warm sector of extreme cyclones
intensifies with wind speeds and
precipitation increasing by up to 15%
per degree of warming

Correspondence to:

E. S. Gentile,
eg3736@princeton.edu

Citation:

Gentile, E. S., Harris, L., Zhao, M.,
Hodges, K., Tan, Z., Cheng, K.‐Y., &
Zhou, L. (2025). Response of extreme
north Atlantic midlatitude cyclones to a
warmer climate in the GFDL X‐SHiELD
kilometer‐scale global storm‐resolving
model. Geophysical Research Letters, 52,
e2024GL112570. https://doi.org/10.1029/
2024GL112570

Received 17 SEP 2024
Accepted 23 DEC 2024

Author Contributions:

Conceptualization: Emanuele
Silvio Gentile
Data curation: Emanuele Silvio Gentile,
Lucas Harris
Formal analysis: Emanuele
Silvio Gentile, Zhihong Tan
Funding acquisition: Lucas Harris,
Ming Zhao
Investigation: Emanuele Silvio Gentile
Methodology: Emanuele Silvio Gentile,
Kevin Hodges, Kai‐Yuan Cheng,
Linjiong Zhou
Project administration: Emanuele
Silvio Gentile, Lucas Harris, Ming Zhao
Resources: Ming Zhao
Software: Emanuele Silvio Gentile,
Lucas Harris, Kevin Hodges

© 2025. The Author(s).
This is an open access article under the
terms of the Creative Commons
Attribution License, which permits use,
distribution and reproduction in any
medium, provided the original work is
properly cited.

GENTILE ET AL.

Response of Extreme North Atlantic Midlatitude Cyclones to
a Warmer Climate in the GFDL X‐SHiELD Kilometer‐Scale
Global Storm‐Resolving Model
Emanuele Silvio Gentile1
Kai‐Yuan Cheng1

, Kevin Hodges3, Zhihong Tan1

, and Linjiong Zhou1

, Lucas Harris2

, Ming Zhao2

,

1Program in Atmospheric and Oceanic Sciences, Princeton University, Princeton, NJ, USA, 2Geophysical Fluid Dynamics
Lab, NOAA, Princeton, NJ, USA, 3University of Reading and National Centre for Atmospheric Science, Reading, UK

Abstract Using the novel kilometer‐scale global storm‐resolving model Geophysical Fluid Dynamics
Laboratory eXperimental System for High‐resolution prediction on Earth‐to‐Local Domains (X‐SHiELD), we
investigate the impact of a 4 K increase in sea surface temperatures on Northern Hemisphere midlatitude
cyclones, during the January 2020–January 2022 period. X‐SHiELD simulations reveal a poleward shift in
cyclone tracks under warming, consistent with CMIP projections. However, X‐SHiELD's high resolution and
explicit deep convection allowed for a detailed analysis of the warm and cold sectors, which are instead typically
underrepresented in traditional CMIP models. Instead, compositing the 100 most intense midlatitude cyclones
in the North Atlantic, we find that the warm sector exhibits statistically significant increases in wind speed and
precipitation of up to 15% locally per degree of warming, while changes in the cold sector are less pronounced.
This study demonstrates X‐SHiELD's potential to provide a realistic‐looking perspective into the evolving risks
posed by midlatitude cyclones in a warming climate.

Plain Language Summary In this study, we use a cutting‐edge global storm‐resolving model called
Geophysical Fluid Dynamics Laboratory eXperimental System for High‐resolution prediction on Earth‐to‐
Local Domains (X‐SHiELD) to understand how intense storms, known as midlatitude cyclones, might change
as the climate warms. Specifically, we examine how a 4°C increase in sea surface temperatures affects these
storms in the Northern Hemisphere over a 2‐year period. Our simulations show that the tracks of midlatitude
cyclones tend to shift toward the poles as temperatures rise, which is consistent with previous climate model
projections. What makes this study unique is the use of X‐SHiELD, a high‐resolution storm‐resolving model
that can simulate both the warm and cold parts of these cyclones in far greater detail than traditional models.
This allows us to observe changes that other models miss. For example, we find that the warm parts of the
cyclones experience much stronger winds and heavier rainfall, with increases by up to 15% locally in wind
speeds and in rainfall for every degree of warming. These findings suggest that as the climate warms,
midlatitude cyclones will pose greater risks, especially from their warm sectors, and highlighting the importance
of storm‐resolving models like X‐SHiELD.

1. Introduction

Midlatitude cyclones, commonly known as windstorms, are a major driver of extreme winds and precipitation
across the midlatitudes, leading to significant socio‐economic impacts, with billions of dollars in damages (Letson
et al., 2021; Little et al., 2023; Munich Re, 2002; Roberts et al., 2014; Son et al., 2024). Despite their importance,
the latest Intergovernmental Panel on Climate Change (IPCC) report highlights substantial uncertainty (medium
to low confidence) regarding projected changes in the frequency, preferred locations, and structural features of
these cyclones under future climate scenarios (IPCC, 2023). Reducing this uncertainty is crucial, and advances in
increasingly sophisticated climate models potentially provide a path forward.

Although scientific agreement on future changes in midlatitude cyclones remains uncertain, two decades of
research suggest a poleward shift in cyclone track density and intensity, with the most severe socio‐economic
impacts likely concentrated in the Northern Hemisphere midlatitude regions such as North America, the
British Isles, and Europe (Catto et al., 2019; Chang, 2017; Feser et al., 2015; Pinto et al., 2012; Priestley &
Catto, 2022; Ulbrich et al., 2013; Wang et al., 2017; Zappa et al., 2013). While the overall number of midlatitude

1 of 11

Supervision: Emanuele Silvio Gentile,
Ming Zhao
Validation: Emanuele Silvio Gentile
Visualization: Emanuele Silvio Gentile,
Kevin Hodges
Writing – original draft: Emanuele
Silvio Gentile
Writing – review & editing: Emanuele
Silvio Gentile, Ming Zhao, Zhihong Tan

Geophysical Research Letters

10.1029/2024GL112570

cyclones is projected to decrease, the strongest ones might intensify, with both winds and precipitation becoming
more extreme (Bevacqua et al., 2020; Büeler & Pfahl, 2019; Gentile et al., 2023; Priestley & Catto, 2022).

Several studies have investigated future changes in the structure of midlatitude cyclones (Catto et al., 2019;
Schultz et al., 2019), identifying three key aspects under a warmer climate: (a) increased surface latent heat flux,
amplifying positive lower‐tropospheric potential vorticity (Pfahl et al., 2015); (b) strengthening of the warm
sector (the region between the cold and warm fronts), with increases in low‐level winds and total precipitation
(Berthou et al., 2022; Manning et al., 2023; Sinclair et al., 2020); and (c) minimal changes in cold sector peak
winds (the region behind the cold front (Bengtsson et al., 2009; Gentile & Gray, 2023). However, most of these
studies relied on coarse‐resolution CMIP General Circulation Models (GCMs), which struggle to capture
mesoscale cyclone features. For example, the mesoscale cold sector of a midlatitude cyclone approximately
300 km across, is resolved by only about three grid points in a 100 km resolution CMIP GCM (Hewson &
Neu, 2015), limiting accuracy in representing the highly‐spatially and temporally varying near‐surface winds and
precipitation. The reliance of traditional GCMs on subgrid‐scale parameterizations for processes like convection
further exacerbates these limitations.

The recent development of km‐scale Global Storm‐Resolving Models (Fuhrer et al., 2018; Satoh et al., 2014,
2019; Schär et al., 2020; Stevens et al., 2019; Tomassini et al., 2023) presents an opportunity to address this issue.
These models, with their exceptionally high‐resolution and reduced reliance on physics parametrizations, provide
a more reliable foundation for assessing future cyclone changes under a warmer climate. Despite some remaining
biases (Feng et al., 2023), they have already shown promising results in simulating more realistic precipitation
patterns (Jones et al., 2023; O’Gorman et al., 2021) and capturing the precipitation response to increased Sea
Surface Temperatures (SSTs) and CO2 under warmer climate scenario (Bolot et al., 2023; Guendelman
et al., 2024). These capabilities offer an exciting opportunity to investigate how the structure of intense mid-
latitude cyclones, their rapidly‐varying near‐surface winds, and total precipitation respond to warmer climate
scenarios at kilometer‐scale, which we explore here.

In this study, we use the latest version of the cutting‐edge global storm‐resolving kilometer‐scale model,
eXperimental System for High‐resolution prediction on Earth‐to‐Local Domains (X‐SHiELD), developed by the
Geophysical Fluid Dynamics Laboratory (GFDL), running at a 3.25 km grid‐spacing, to investigate future
mesoscale changes in midlatitude cyclones. We compare the synoptic characteristics (track and intensity) and
composite means of wind and precipitation for the 100 most intense midlatitude cyclones in the North Atlantic
region between a control scenario and a warmer climate scenario, where SSTs are increased by 4K, over the
January 2020–January 2022 period. Given the exceptionally large data set generated by X‐SHiELD global
simulations, we confine our study to the extended North Atlantic region, spanning from North America to Europe,
bounded by 25‐90°N latitude and 60°W to 30°E longitude.

2. Methods

2.1. The Kilometer‐Scale Global Storm‐Resolving Model X‐SHiELD

The kilometer‐scale global storm‐resolving model X‐SHiELD, derived from the SHiELD model family (Harris
et al., 2020), is a cutting‐edge global model which operates at a horizontal resolution of approximately 3.25 km
with 79 vertical layers. X‐SHiELD employs a simplified parameterization for shallow convection (Cheng
et al., 2022), while the planetary boundary layer turbulence is modeled using the Turbulent Kinetic Energy–Eddy
Diffusivity Mass Flux (TKE‐EDMF) scheme (Han & Bretherton, 2019).

To investigate the response of intense midlatitude cyclones to a warmer climate, specifically capturing projected
future changes in their mesoscale structure, we conducted two simulations using X‐SHiELD. These span the 2‐
year period January 2020–January 2022 (with a 3‐month spin up before January 2020) and include a control run
and a warmer climate scenario.

In the control simulation, the lower boundary consists of a mixed layer ocean (MLO) nudged toward ECMWF sea
surface temperature (SST) analyses with a timescale of 15 days. While the MLO does not strictly follow the
prescribed SSTs, its interactivity captures features of an interactive ocean without increasing computational cost,
and drifts are effectively controlled (Harris et al., 2020). A recent detailed evaluation of X‐SHiELD against
observational data revealed no model drift (Guendelman et al., 2024), with local biases comparable to those in
CMIP6 models, despite the limited integration period. In the warmer climate simulation, SSTs are nudged toward

GENTILE ET AL.

2 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

Figure 1. (a) Difference in midlatitude cyclone track density (10− 6km− 2 month− 1) between the +4 K SST warmer (WARM) and control (CTRL) X‐ShiELD simulations
for the NH (shown as color shading), with control cyclone track density overlaid as fine black contours. Green points and light green points denote the centers of the 100
most intense cyclones in the control at their peak 850 hPa vorticity ( ξ850) and warmer climate simulations, respectively. The thick black line outlines the North Atlantic
sector considered. (b) Difference in midlatitude cyclone track mean intensity [10− 5s− 1] between the WARM and CTRL simulations for the NH (shown as color shading),
with cyclone track intensity in the control simulation overlaid as fine black contour.

ERA5 SSTs uniformly increased by +4K, leading to an approximate +4 K increase relative to the control
simulation SSTs. This setup may enhance baroclinicity near the sea‐ice edge, where temperatures reach 0°C,
potentially favoring cyclogenesis. With identical sea‐ice concentrations in both simulations, the cyclone activity
near the poles might be artificially enhanced. However, analysis of the 100 most intense cyclone centers, iden-
tified by their peak vorticity at maximum intensity (Figure 1a), revealed no significant shift in their distribution
near the sea‐ice edge, suggesting minimal influence of the fixed sea‐ice edge on our results (see Section 2.2 for
details on cyclone tracking).

2.2. Midlatitude Cyclone Tracking and Compositing

We tracked midlatitude cyclones using the Hodges algorithm (Hodges, 1995) applied to 3‐hourly 850 hPa relative
vorticity ( ξ850). This method better detects lower tropospheric cyclones compared to those based on mean sea
level pressure, by allowing earlier system identification and minimizing large‐scale background influence. To
reduce noise in the high‐resolution vorticity field (≈3.25 km), we coarsened it to 25 km and truncated it to T42
resolution, masking wavenumbers ≤5 to remove planetary‐scale wave effects. Cyclones were identified as
positive 850 hPa vorticity anomalies, and only those that persisted for over 48 hr, traveled at least 1,000 km, and
reached a maximum vorticity of 1 × 10− 5 s− 1 were retained.

The 100 most intense cyclones, ranked by maximum ξ850, were composited for both the control and +4K warmer
climate scenarios (Catto et al., 2010; Dacre et al., 2012; Sinclair et al., 2020). An analysis of the seasonal dis-
tribution of cyclones revealed that 88% of cyclones in both simulations occur between October and March,
highlighting their predominantly wintertime nature. However, the +4K simulation exhibits a slight increase in
summer cyclone frequency (3% vs. 1% in the control), with a corresponding decrease in spring. The range of
maximum vorticity values was analyzed for both simulations.

To analyze cyclone structure, we examined total column water vapor, 850 hPa temperature, 10‐m wind speed, and
precipitation at four lead times relative to peak intensity: − 48, − 24, 0, and +24 hr. Cyclones were mapped onto a
12° radius spherical grid centered on their 850 hPa vorticity center, using 40 radial and 360 angular points.
Cyclones were rotated to align their propagation due east, ensuring consistent compositing. Meteorological fields
were then averaged across the 100 cyclones for each lead time relative to maximum vorticity. While the 2‐year

GENTILE ET AL.

3 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

simulation duration limits the value of significance testing for total cyclone tracks, consistent with recent GSRM
studies (Bolot et al., 2023; Cheng et al., 2022; Dong et al., 2024; Gao et al., 2024; Guendelman et al., 2024; Jones
et al., 2023; Merlis et al., 2024; O’Gorman et al., 2021), we evaluate the statistical significance of differences in
the composite means of the considered meteorological fields associated with the 100 most intense cyclones
between control and warmer climate simulations using Welch's t‐test with a two‐tailed threshold of p < 0.05. The
resulting p‐values identified statistically significant grid cells, visualized with stippling on composite maps,
unless >99% of grid cells were significant, in which case this was noted in the text and stippling omitted for
clarity.

3. Results Obtained Using the Kilometer‐Scale Global Storm‐Resolving X‐SHiELD
Model

3.1. Response of Midlatitude Cyclone Tracks Density and Intensity to a Warmer Climate Scenario

The response of midlatitude cyclone tracks density and intensity in the NH to a +4K SST increase, as simulated
by the kilometer‐scale global storm‐resolving X‐SHiELD model, is shown as divergent color shading in
Figures 1a and 1b, respectively. Figure 1a illustrates that X‐SHiELD accurately captures the maximum cyclone
track density within the two primary oceanic storm tracks, the North Atlantic and North Pacific, with magnitudes
consistent with previous studies (Bengtsson et al., 2009; Dacre & Gray, 2009). The warmer climate scenario
reveals a noticeable poleward shift in the storm tracks in both the North Atlantic and North Pacific, with a marked
increase in cyclone track density on the poleward flank and a corresponding decrease equatorward. Overall, in the
warmer climate scenario the total number of midlatitude cyclones in the NH decreases by approximately 3.5%,
aligning with previous findings (Catto et al., 2019; Priestley & Catto, 2022).

Figure 1b demonstrates that cyclone intensity strengthens near the NH pole, in the warmer climate simulation,
while weakening equatorward, except for a region in the North Pacific. In the NH, regions of the Atlantic Ocean
north of the British Isles and Northern Europe, and the northern Pacific Ocean, experience increases in cyclone
intensity, with relative vorticity at 850 hPa ( ξ850) reaching up to approximately 1.0 × 10− 5s− 1. Conversely, the
southern parts of the North Atlantic and North Pacific exhibit decreases in cyclone intensity, with values as low as
− 1.0 × 10− 5s− 1, consistent with CMIP5 and CMIP6 findings (Priestley & Catto, 2022; Zappa et al., 2013).

In contrast, in the Mediterranean region, the warmer climate scenario reduces track density but shows minimal
change in track intensity. This limited sensitivity to the +4 K SST increase may reflect methodological con-
straints, such as limitations in the Hodges tracking algorithm (Hodges, 1995), which may underrepresent intense
Mediterranean cyclones like medicanes (Pantillon et al., 2024; Zappa et al., 2015). Future enhancements in
tracking methods could offer a more comprehensive understanding of their response to warming.

3.2. Response of Composite Structure of the One‐Hundred Most Intense Midlatitude Cyclones to a
Warmer Climate

Here, we investigate the mesoscale structure evolution of the 100 most intense North Atlantic midlatitude cy-
clones under both the control and +4 K SST warmer climate scenarios. The composite mean of their total column
water vapor (TCWV) and 850‐hPa temperature anomalies are shown at various stages relative to the time of
maximum vorticity. The black contours in Figure 2a show the control climate TCWV composites at − 48 hr,
characterized by a broad and well‐defined warm sector, with values exceeding 24 kg m− 2. By − 24 hr (Figure 2b),
the cold sector begins to wrap around the warm sector. At maximum vorticity (Figure 2c), TCWV in the warm
sector decreases to 16 kg m− 2, further reducing to 12 kg m− 2 in the later stages (Figure 2d), primarily due to
condensation of water vapor and subsequent precipitation, contributing to cyclone intensification through the
latent heat release.

Comparing warmer climate to the control simulation (blue shading in Figures 2a–2d), a TCWV increase is
observed at all stages of cyclone development. (To note, the differences between the warmer climate and the
control simulations are normalized by 4K, corresponding to the SST increase in warmer climate.) The most
pronounced increase occurs in the warm sector during the early development stages, − 48 to − 24 hr (Figures 2a
and 2b), reaching up to approximately 3.5 kg m− 2 per degree of SST warming (≈15% increase). In contrast, the
cold sector experiences a smaller TCWV increases (4%–6% rise or 0.5 kg m− 2) per degree of SST warming during
the early development stages (Figures 2a and 2b), primarily ahead of the warm front and poleward of the cyclone

GENTILE ET AL.

4 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

Figure 2. Composite mean TCWV of the 100 most intense cyclones in control X‐SHiELD under the control climate (black
contours, [kg m− 2]) at (a) − 48 hr, (b) − 24 hr, (c) 0 hr, and (d) +24 hr relative to the time of maximum vorticity, overlaid on
TCWV differences between the warmer +4 K SST and control climate (blue shading). Red dashed contours indicate the
difference in 850 hPa temperature anomalies between the +4 K SST and control climate. All fields are coarsened to a 25 km
resolution from their native 3.25 km resolution, and normalized by 4K SST warming. Composite cyclone centers are aligned
relative to their 850 hPa vorticity and rotated with propagation direction to the right.

center. An exception is a relatively small patch in the cold sector behind the cold front, west of the cyclone center,
with relatively larger increases of ≈10% K− 1, possibly due to the cyclone being still close to the open wave stage.
At maximum vorticity and the later stages (Figures 2c and 2d), TCWV increases in the warm sector remains
significant (1.0–1.5 kg m− 2), corresponding to a 7%–9% increase, while changes in the cold sector become
negligible in value, below 5 kg m− 2. Finally, we note that nearly all composite TCWV differences (>99% grid
cells) in Figures 2a–2d are statistically significant ( p < 0.05), so stippling is omitted for clarity.

The composite mean 850‐hPa temperature anomaly ( ˜T850) per degree of SST warming (the red‐dashed contours
in Figures 2a–2d), reveals an increase of up to 2 and 1 K per degree of global mean SST warming at − 48 hr and
− 24 hr, respectively (Figures 2a and 2b), while the cold sector shows slight decreases, ahead of the warm front,
with maximum reduction of 0.5 K. This pattern implies a strengthening of the meridional temperature gradient in
the +4K experiment. We computed the 850 hPa temperature anomaly difference by: (a) subtracting the 850 hPa

GENTILE ET AL.

5 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

spatio‐temporal temperature mean over the North Atlantic region (outlined by black boundaries in Figure 1) from
the control composite mean 850 hPa temperature, (b) repeating this procedure for the warmer climate simulation,
and (c) subtracting the control climate anomaly from the warmer climate anomaly. This analysis helps to clarify
that the observed super Clausius‐Clapeyron increase in TCWV (15%K− 1) during early cyclone intensification
stages may result from normalizing against global SST increase rather than local atmospheric temperature.
Indeed, as shown in Figure 2b, the local temperature increase ˜T850 over the warm sector exceeds the North
Atlantic mean, and the TCWV increase closely follows this temperature anomaly. At maximum vorticity and later
stages (Figures 2c and 2d), changes in the composite mean ˜T850 become much smaller, confined to within ±0.5 K
per degree of SST warming. The substantial increase in the background 850 hPa temperature anomaly gradient at
− 48 hr, and to a lesser extent at − 24 hr, shows a large increase in the warmer climate, and may be due to a shift in
cyclone location from the North American continent toward Europe. However, further exploration of additional
contributing factors lies beyond the scope of the paper.

3.3. Response of the One‐Hundred Most Intense Midlatitude Cyclone Composite Mean 10‐m Winds and
Total Precipitation

Figure 3 illustrates the evolution of the composite mean Earth‐relative 10‐m wind speed in the control climate
(black contours) and the corresponding changes in magnitude per degree of SST warming in the +4 K warmer
climate (shading). During the early stages of cyclone development, between − 48 and − 24 hr (Figures 3a and 3b),
the highest composite control mean 10‐m wind speeds, approximately 10 m s− 1, are located in the warm sector,
equatorward of the cyclone center. As the composite cyclone rapidly intensifies, the region of strongest 10‐m
wind speeds shifts to the rear of the cyclone center, while remaining equatorward, in the cold sector. At the
time of maximum vorticity (Figure 3c), the composite mean 10‐m wind speeds peak at around 25 ms− 1. However,
these peaks in the later stages of development (Figure 3d) weaken, decreasing to 16–18 ms− 1. It is important to
note that the relatively weak peak of 25 m s− 1 at maximum vorticity, despite the 3.25 km resolution of the model,
is primarily due to averaging over 100 cyclones, which smooths out localized extreme values, and it does not
represent an actual peak for individual cyclones. Additionally, the surface‐layer parameterization may contribute
to this smoothing effect, as the Earth‐relative 10‐m wind speeds are highly sensitive to near‐surface processes.

Under the +4K SST warming, the composite mean 10‐m wind speeds increase at most stages of cyclone
development. In the early stages (− 48 to − 24 hr relative to the time of maximum vorticity, Figures 3a and 3b), the
area of highest 10‐m wind speeds expands, with increases of up to 1–1.5 ms− 1 per SST degree of warming,
particularly ahead of and on the southern flank of the warm sector. Between − 24 hr and the time of maximum
vorticity, the cyclone's pressure center shifts northeastward and then eastward (see green and purple crosses in
Figures 3b and 3c), resulting in a dipole structure in the composite wind field, also suggesting an overall less
upright and more tilted vertical structure of the cyclone composites. Additionally, in the cold sector, maximum
winds shift equatorward and eastward, increasing by 0.5 ms− 1 per SST degree of warming. Both the cold and
warm sector enlarge, with a plausible mechanism being an increase in size of the cyclone composites in the
warmer climate scenario. By +24 hr (Figure 3d), changes are constrained within ≈±0.25 ms− 1, except for a
continued eastward shift of the cyclone center. All composite 10‐m wind differences in Figure 3 exceeding ±0.25
m s− 1 are statistically significant ( p < 0.05), except at +24 hr, where significance is limited to shifts near the
pressure center.

Overall, the peak composite 10‐m wind speed, located in the cold sector, increases slightly, by about 0.5 ms− 1,
representing a relative increase of less than 2%. In contrast, the warm sector experiences a more substantial in-
crease of up to 1.5 ms− 1 per SST degree of warming, corresponding to a percentage increase of up to 15%
compared to the control values.

Figure 4a shows the evolution of total hourly precipitation from − 48 to +24 hr relative to the time of maximum
vorticity. In the control climate, precipitation peaks near the warm front (see Figures 4a and 4b) in the cyclone's
warm sector, reaching 6 mm per 6 hr, at − 48 hr. This peak intensifies to 12 mm per 6 hr by − 24 hr (Figure 4b), and
expands around both the cold and warm fronts. At peak intensity (Figure 4c), precipitation decreases to 9 mm per
6 hr and stretches into a spiral band wrapping anticlockwise around the cyclone center, reflecting the organized
structure of mature cyclones. Post‐maximum vorticity (Figure 4d), precipitation weakens further, becoming
diffuse and dropping to 3 mm per 6 hr.

GENTILE ET AL.

6 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

Figure 3. As in Figure 2 but for 10‐m wind speeds. The 10‐m wind speeds are shown at their native X‐SHiELD 3.25 km
resolution. The green and the purple crosses in (b) and (c) represent the control and warmer climate cyclone composite
pressure center, respectively. Statistically significant areas ( p < 0.05) are indicated by stippled gray dots.

Under the +4 K SST warming (Figure 4), total precipitation increases during the early stages of the cyclone
lifecycle (− 48 and − 24 hr). During this period, the area of maximum precipitation shifts eastward and slightly
poleward, as highlighted by the comparison of the control (solid black) and warmer climate (dashed red) pre-
cipitation contours. This shift is accompanied by the large positive differences per SST degree of warming (1.5–
2.5 mm 6 hr− 1K− 1) east of the control precipitation peak. The peak precipitation itself intensifies by 1–1.5 mm 6
hr− 1K− 1 (Figures 4a and 4b) near the warm front, corresponding to a percentage increase of approximately 15%
and 10% per degree of SST warming at − 48 and − 24 hr, respectively. This eastward shift of peak precipitation
suggests changes in the spatial structure of cyclones under warmer conditions. At time of maximum vorticity
(Figure 4c), precipitation differences between the warmer control climates may be attributed to the frontal shifts in
precipitation. After peak vorticity, in the late stage of cyclone composite development (+24 hr Figure 4d), the
precipitation field weakens, and no appreciable changes are found in the +4 K scenario. All composite precip-
itation differences in Figure 4 exceeding ±0.5 mm 6 hr− 1K− 1 are statistically significant (p < 0.05), except at
+24 hr, where nearly all differences (<1% grid cells) are not statistically significant.

GENTILE ET AL.

7 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

Figure 4. As in Figure 2 but for total 6‐hourly precipitation [mm 6 hr− 1]. Control (solid‐black contours) and warmer climate
(red‐dashed contours) precipitation are composited at their native X‐SHiELD 3.25 km resolution, but are subsampled every 5
grid cells for visualization purposes. The shading indicates increases on composite mean total hourly precipitation
normalized by 4 K SST warming. White areas correspond to regions of precipitation decreases caused by frontal shifts.
Statistically significant areas ( p < 0.05) are indicated by stippled gray dots.

4. Conclusion

In this study, we used the high‐resolution (3.25 km) global storm‐resolving model X‐SHiELD from GFDL to
examine changes in track density, intensity, mesoscale structure, 10‐m wind speeds, and total precipitation of
midlatitude cyclones under a +4 K SST warming scenario. X‐SHiELD's explicit deep convection enabled a
detailed representation of cyclone mesoscale features, often under‐resolved in coarser CMIP models. The 2‐year
simulation results reveal a poleward shift in Northern Hemisphere cyclone tracks and intensification along the
northern edges of the Atlantic and Pacific storm tracks, in line with projections from aquaplanet and CMIP models
(Catto et al., 2019; Gentile et al., 2023; Oudar et al., 2020; Priestley & Catto, 2022; Tamarin‐Brodsky &
Kaspi, 2017; Zappa et al., 2013).

X‐SHiELD's kilometer‐scale resolution enabled detailed analysis of the composite mean structure of the 100 most
intense North Atlantic cyclones across various stages relative to their maximum vorticity. In the early

GENTILE ET AL.

8 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

development phase, the +4 K SST increase intensified precipitation and near‐surface wind speeds in the cyclone's
warm sector, a response similar to that seen in coarser‐resolution GCM simulations over the North Atlantic under
Representative Concentration Pathway RCP8.5 future climate scenario (Dolores‐Tesillos et al., 2022). TCWV
increased by approximately 15% per degree of SST warming (relative to control values), driving also more intense
warm sector total precipitation, with statistically significant increases up to 15%. These values exceed the
corresponding TCWV and total precipitation values obtained from aquaplanet simulations at a much coarser
resolution (≈10% K− 1) using OpenIFS (Sinclair et al., 2020), likely reflecting X‐SHiELD's ability to explicitly
resolve moist convection at kilometer‐scale resolution. For comparison (Jung et al., 2012), demonstrated a 6%
increase in precipitation when increasing the IFS resolution from T159 (≈ 39 km) to T1279 (≈ 16 km). Wind
speeds in the warm sector also increased by up to 15% per degree of SST warming, while changes in peak winds at
the cyclone's maximum intensity were negligible, the latter consistent with decades‐long future climate pro-
jections from ECHAM model at 100 km resolution (Bengtsson et al., 2009) which showed only a slight reduction
at most of ≈ 1m s− 1. The appearance of a statistically significant dipole structure in the near‐surface wind speed at
the cyclone peak intensity, caused by an eastward shift of the cyclone center, mirrors findings from idealized
aquaplanet simulations (Sinclair et al., 2020) and baroclinic life cycle experiments (Tierney et al., 2018).
However, our study finds stronger wind magnitudes (by approximately 1ms− 1), and, unlike Sinclair the inten-
sification of winds in our study is located slightly westward, rather than eastward.

The asymmetric response, with preferential moistening and wind intensification in the warm sector, indicates that
future cyclone‐related hazards, especially precipitation and 10‐m wind speeds, will likely concentrate in this
sector of intense cyclones. This shift has important implications for hazard distribution and forecasting. Although
mechanisms behind warm sector intensification are beyond this study's scope, stronger diabatic forcing or
enhanced meridional temperature gradients (despite approximately uniform SST warming) may contribute.
Previous studies (Kohl & O’Gorman, 2022; Pfahl et al., 2015; Stanković et al., 2024) suggest that increased
diabatic forcing enhances latent heating, strengthening lower‐tropospheric potential vorticity and intensifying the
warm conveyor belt. Future research should link specific climate feedbacks to dynamical changes in midlatitude
cyclones, enhancing interpretation of kilometer‐scale X‐SHiELD simulations.

Finally, two caveats should be noted. First, X‐SHiELD simulations did not account for the expected decline in
sea‐ice cover throughout the 21st century (Stroeve et al., 2012), as discussed in Sect. 2.1. Second, the +4 K SST
warmer climate simulation may overlook the effects of regional SST variations (Villarini & Vecchi, 2012), which
can influence cyclone tracks and intensities. However, given the challenge of projecting realistic future SST
patterns (Zhao & Knutson, 2024), prescribed SST warming remains the most robust approach to capturing the
primary signal of climate change.

Data Availability Statement

The X‐SHiELD code used in this study is available in Zenodo (Harris et al., 2022). The TRACK codebase for
cyclone tracking and compositing can be accessed at https://gitlab.act.reading.ac.uk/track/track and is discussed
in details in Bengtsson et al. (2006) and Hodges (1995). Custom codes, detailed in Materials and Methods,
implement standard techniques. Processed monthly X‐SHiELD data (2020–2021) is archived on Zenodo
(Gentile, 2024). Additional model verification plots are at https://extranet.gfdl.noaa.gov/~Alex.Kaltenbaugh/
verification/, with scripts and data in Guendelman et al. (2023).

References

Bengtsson, L., Hodges, K., & Keenlyside, N. (2009). Will extratropical storms intensify in a warmer climate? Journal of Climate, 22(9), 2276–

2301. https://doi.org/10.1175/2008jcli2678.1

Bengtsson, L., Hodges, K. I., & Roeckner, E. (2006). Storm tracks and climate change. Journal of Climate, 19(15), 3518–3543. https://doi.org/10.

1175/jcli3815.1

Berthou, S., Roberts, M., Vannière, B., Ban, N., Belušić, D., Caillaud, C., et al. (2022). Convection in future winter storms over northern Europe.

Environmental Research Letters, 17(11), 114055. https://doi.org/10.1088/1748‐9326/aca03a

Bevacqua, E., Vousdoukas, M., Zappa, G., Hodges, K., Shepherd, T. G., Maraun, D., et al. (2020). More meteorological events that drive
compound coastal flooding are projected under climate change. Communications Earth & Environment, 1, 47. https://doi.org/10.1038/s43247‐
020‐00044‐z

Bolot, M., Harris, L., Cheng, K.‐Y., Merlis, T. M., Blossey, P., Bretherton, C. S., et al. (2023). Kilometer‐scale global warming simulations and
active sensors reveal changes in tropical deep convection. npj Climate and Atmospheric Science, 6(1), 209. https://doi.org/10.1038/s41612‐
023‐00525‐w

Acknowledgments
This research was funded by the Climate
Process Team (CPT) under NSF Grant
AGS‐1916689 and NOAA Grant
NA19OAR4310363.

GENTILE ET AL.

9 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

Büeler, D., & Pfahl, S. (2019). Potential vorticity diagnostics to quantify effects of latent heating in extratropical cyclones. Part II: Application to

idealized climate change simulations. Journal of the Atmospheric Sciences, 76(7), 1885–1902. https://doi.org/10.1175/jas‐d‐18‐0342.1

Catto, J. L., Ackerley, D., Booth, J., Champion, A. J., Colle, B. A., Pfahl, S., et al. (2019). The future of midlatitude cyclones. Current Climate

Change, 5(4), 407–420. https://doi.org/10.1007/s40641‐019‐00149‐4

Catto, J. L., Shaffrey, L. C., & Hodges, K. I. (2010). Can climate models capture the structure of extratropical cyclones? Journal of Climate, 23(7),

1621–1635. https://doi.org/10.1175/2009jcli3318.1

Chang, E. (2017). Projected significant increase in the number of extreme extratropical cyclones in the Southern Hemisphere. Journal of Climate,

30(13), 4915–4935. https://doi.org/10.1175/jcli‐d‐16‐0553.1

Cheng, K., Harris, L., Bretherton, C., Merlis, T. M., Bolot, M., Zhou, L., et al. (2022). Impact of warmer sea surface temperature on the global
pattern of intense convection: Insights from a global storm resolving model. Geophysical Research Letters, 49(16), e2022GL099796. https://
doi.org/10.1029/2022gl099796

Dacre, H., & Gray, S. (2009). The spatial distribution and evolution characteristics of North Atlantic cyclones. Monthly Weather Review, 137(1),

99–115. https://doi.org/10.1175/2008mwr2491.1

Dacre, H., Hawcroft, M., Stringer, M., & Hodges, K. (2012). An extratropical cyclone atlas: A tool for illustrating cyclone structure and evolution

characteristics. Bulletin America Meteorology Social, 93(10), 1497–1502. https://doi.org/10.1175/bams‐d‐11‐00164.1

Dolores‐Tesillos, E., Teubler, F., & Pfahl, S. (2022). Future changes in North Atlantic winter cyclones in CESM‐LE – Part 1: Cyclone intensity,
potential vorticity anomalies, and horizontal wind speed. Weather and Climate Dynamics, 3(2), 429–448. https://doi.org/10.5194/wcd‐3‐429‐
2022

Dong, W., Zhao, M., Harris, L., Cheng, K., Zhou, L., & Ramaswamy, V. (2024). Contrasting response of mesoscale convective systems
occurrence over tropical land and ocean to increased sea surface temperature. Geophysical Research Letters, 51(21), e2024GL109251. https://
doi.org/10.1029/2024gl109251

Feng, Z., Leung, L. R., Hardin, J., Terai, C. R., Song, F., & Caldwell, P. (2023). Mesoscale convective systems in dyamond global convection‐

permitting simulations. Geophysical Research Letters, 50(4), e2022GL102603. https://doi.org/10.1029/2022gl102603

Feser, F., Barcikowska, M., Krueger, O., Schenk, F., Weisse, R., & Xia, L. (2015). Storminess over the north Atlantic and northwestern Europe ‐ A

review. Quarterly Journal of the Royal Meteorological Society, 141(687), 350–382. https://doi.org/10.1002/qj.2364

Fuhrer, O., Chadha, T., Hoefler, T., Kwasniewski, G., Lapillonne, X., Leutwyler, D., et al. (2018). Near‐global climate simulation at 1 km
resolution: Establishing a performance baseline on 4888 GPUs with COSMO 5.0. Geoscientific Model Development, 11(4), 1665–1681. https://
doi.org/10.5194/gmd‐11‐1665‐2018

Gao, K., Harris, L., Tong, M., Zhou, L., Chen, J.‐H., & Cheng, K. (2024). A flexible tropical cyclone vortex initialization technique for GFDL

SHiELD. Frontiers in Earth Science, 12. https://doi.org/10.3389/feart.2024.1396390

Gentile, E. S. (2024). Processed extreme composite cyclone datasets from X‐SHiELD simulations [Dataset]. Zenodo. https://doi.org/10.5281/

zenodo.14085686

Gentile, E. S., & Gray, S. L. (2023). Attribution of observed extreme marine wind speeds and associated hazards to midlatitude cyclone conveyor

belt jets near the British Isles. International Journal of Climatology, 43(6), 2735–2753. https://doi.org/10.1002/joc.7999

Gentile, E. S., Zhao, M., & Hodges, K. (2023). Poleward intensification of midlatitude extreme winds under warmer climate. npj Climate and

Atmospheric Science, 6(219). https://doi.org/10.1038/s41612‐023‐00540‐x

Guendelman, I., Merlis, T., Cheng, K.‐Y., Harris, L., Bretherton, C., Bolot, M., et al. (2023). Data for: The precipitation response to warming and
CO2 increase: A comparison of a global storm resolving model and CMIP6 models [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.
10365813

Guendelman, I., Merlis, T. M., Cheng, K.‐Y., Harris, L. M., Bretherton, C. S., Bolot, M., et al. (2024). The precipitation response to warming and
CO2 increase: A comparison of a global storm resolving model and CMIP6 models. Geophysical Research Letters, 51(7), e2023GL102603.
https://doi.org/10.1029/2023gl107008

Han, J., & Bretherton, C. S. (2019). TKE‐based moist eddy‐diffusivity mass‐flux (EDMF) parameterization for vertical turbulent mixing. Weather

and Forecasting, 34(4), 869–886. https://doi.org/10.1175/waf‐d‐18‐0146.1

Harris, L., Zhou, L., Chen, J.‐H., Gao, K., Mingjing, T., Cheng, K.‐Y., et al. (2022). X‐SHiELD codebase [Dataset]. Zenodo. Retrieved from

https://zenodo.org/records/6941034

Harris, L., Zhou, L., Lin, S., Chen, J., Chen, X., Gao, K., et al. (2020). GFDL SHiELD: A unified system for weather‐to‐seasonal prediction.

Journal of Advances in Modeling Earth Systems, 12(10), e2020MS002223. https://doi.org/10.1029/2020ms002223

Hewson, T. D., & Neu, U. (2015). Cyclones, windstorms and the IMILAST project. Tellus, 67(1), 27–128. https://doi.org/10.3402/tellusa.v67.

27128

Hodges, K. I. (1995). Feature tracking on the unit sphere. Monthly Weather Review, 123(12), 3458–3465. https://doi.org/10.1175/1520‐0493

(1995)123<3458:ftotus>2.0.co;2

IPCC. (2023). In C. W. Team, H. Lee, & J. Romero (Eds.), Climate change 2023: Synthesis report. Contribution of working groups I, II and III to

the sixth assessment report of the intergovernmental panel on climate change. IPCC.

Jones, R. W., Sanchez, C., Lewis, H., Warner, J., Webster, S., & Macholl, J. (2023). Impact of domain size on tropical precipitation within explicit

convection simulations. Geophysical Research Letters, 50(17), e2023GL104672. https://doi.org/10.1029/2023gl104672

Jung, T., Miller, M. J., Palmer, T. N., Towers, P., Wedi, N., Achuthavarier, D., et al. (2012). High‐resolution global climate simulations with the
ECMWF model in project Athena: Experimental design, model climate, and seasonal forecast skill. Journal of Climate, 25(9), 3155–3172.
https://doi.org/10.1175/jcli‐d‐11‐00265.1

Kohl, M., & O’Gorman, P. A. (2022). The diabatic rossby vortex: Growth rate, length scale, and the wave–vortex transition. Journal of the

Atmospheric Sciences, 79(10), 2739–2755. https://doi.org/10.1175/jas‐d‐22‐0022.1

Letson, F. W., Barthelmie, R. J., Hodges, K. I., & Pryor, S. C. (2021). Intense windstorms in the northeastern United States. Natural Hazards and

Earth System Sciences, 21(7), 2001–2020. https://doi.org/10.5194/nhess‐21‐2001‐2021

Little, A. S., Priestley, M. D., & Catto, J. L. (2023). Future increased risk from extratropical windstorms in northern europe. Nature Commu-

nications, 14(1), 4434. https://doi.org/10.1038/s41467‐023‐40102‐6

Manning, C., Kendon, E., Fowler, H., & Roberts, N. (2023). Projected increase in windstorm severity and contribution from sting jets over the UK

and Ireland. Weather and Climate Extremes, 40, 1–15. https://doi.org/10.1016/j.wace.2023.100562

Merlis, T., Cheng, K.‐Y., Guendelman, I., Harris, L., Bretherton, C. S., Bolot, M., et al. (2024). Climate sensitivity and relative humidity changes
in global storm‐resolving model simulations of climate change. Science Advances, 10(26), eadn5217. https://doi.org/10.1126/sciadv.adn5217

Munich Re. (2002). Winter storms in Europe (II) ‐ Analysis of 1999 losses and loss potentials. Munich Reinsurance Group.

GENTILE ET AL.

10 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2024GL112570

O’Gorman, P. A., Li, Z., Boos, W. R., & Yuval, J. (2021). Response of extreme precipitation to uniform surface warming in quasi‐global
aquaplanet simulations at high resolution. Philos. Trans. R. Soc. A Math. Phys. Eng. Sci., 379(2195), 20190543. https://doi.org/10.1098/
rsta.2019.0543

Oudar, T., Cattiaux, J., & Douville, H. (2020). Drivers of the northern extratropical eddy‐driven jet change in CMIP5 and CMIP6 models.

Geophysical Research Letters, 47(8), e2019GL086695. https://doi.org/10.1029/2019gl086695

Pantillon, F., Davolio, S., Avolio, E., Calvo‐Sancho, C., Carrió, D. S., Dafis, S., et al. (2024). The crucial representation of deep convection for the

cyclogenesis of medicane Ianos. EGUsphere, 2024(3), 1–29. https://doi.org/10.5194/wcd‐5‐1187‐2024

Pfahl, S., O’Gorman, P., & Singh, M. (2015). Extratropical cyclones in idealized simulations of changed climates. Journal of Climate, 28(23),

9373–9392. https://doi.org/10.1175/jcli‐d‐14‐00816.1

Pinto, J., Karremann, M., Born, K., Della‐Marta, P., & M, K. (2012). Loss potentials associated with European windstorms under future climate

conditions. Climate Research, 54, 1–20. https://doi.org/10.3354/cr01111

Priestley, M. D. K., & Catto, J. L. (2022). Future changes in the extratropical storm tracks and cyclone intensity, wind speed, and structure.

Weather and Climate Dynamics, 3(1), 337–360. https://doi.org/10.5194/wcd‐3‐337‐2022

Roberts, J. F., Champion, A. J., Dawkins, L. C., Hodges, K. I., Shaffrey, L. C., Stephenson, D. B., et al. (2014). The XWS open access catalogue of
extreme European windstorms from 1979 to 2012. Natural Hazards and Earth System Sciences, 14(9), 2487–2501. https://doi.org/10.5194/
nhess‐14‐2487‐2014

Satoh, M., Stevens, B., Judt, F., Khairoutdinov, M., Lin, S.‐J., Putman, W. M., & Düben, P. (2019). Global cloud‐resolving models. Current

Climate Change Reports, 5(3), 172–184. https://doi.org/10.1007/s40641‐019‐00131‐0

Satoh, M., Tomita, H., Yashiro, H., Miura, H., Kodama, C., Seiki, T., et al. (2014). The non‐hydrostatic icosahedral atmospheric model:

Description and development. Progress in Earth and Planetary Science, 1, 18. https://doi.org/10.1186/s40645‐014‐0018‐1

Schär, C., Fuhrer, O., Arteaga, A., Ban, N., Charpilloz, C., Di Girolamo, S., et al. (2020). Kilometer‐scale climate models: Prospects and

challenges. Bulletin America Meteorology Social, 101(5), E567–E587. https://doi.org/10.1175/bams‐d‐18‐0167.1

Schultz, D. M., Bosart, L., Colle, B. A., Davies, H. C., Dearden, C., Keyser, D., et al. (2019). Extratropical cyclones: A century of research on

meteorology’s centerpiece. Meteorological Monographs, 59, 16‐1–16‐56. https://doi.org/10.1175/amsmonographs‐d‐18‐0015.1

Sinclair, V. A., Rantanen, M., Haapanala, P., Räisänen, J., & Järvinen, H. (2020). The characteristics and structure of extra‐tropical cyclones in a

warmer climate. Weather and Climate Dynamics, 1, 1–25. https://doi.org/10.5194/wcd‐1‐1‐2020

Son, J.‐H., Franzke, C. L. E., & Son, S.‐W. (2024). Dynamics of extreme surface winds inside north Atlantic midlatitude cyclones. Geophysical

Research Letters, 51(14), e2024GL110330. https://doi.org/10.1029/2024gl110330

Stanković, A., Messori, G., Pinto, J. G., & Caballero, R. (2024). Large‐scale perspective on extreme near‐surface winds in the central North

Atlantic. Weather and Climate Dynamics, 5(2), 821–837. https://doi.org/10.5194/wcd‐5‐821‐2024

Stevens, B., Satoh, M., Auger, L., Biercamp, J., Bretherton, C. S., Chen, X., et al. (2019). Dyamond: The dynamics of the atmospheric general
circulation modeled on non‐hydrostatic domains. Progress in Earth and Planetary Science, 6(1), 61. https://doi.org/10.1186/s40645‐019‐
0304‐z

Stroeve, J., Kattsov, V., Barrett, A., Serreze, M., Pavlova, T., Holland, M., & Meier, W. N. (2012). Trends in arctic sea ice extent from CMIP5,

CMIP3 and observations. Geophysical Research Letters, 39(16), 1–7. https://doi.org/10.1029/2012gl052676

Tamarin‐Brodsky, T., & Kaspi, Y. (2017). Enhanced poleward propagation of storms under climate change. Nature Geoscience, 10(12), 908–913.

https://doi.org/10.1038/s41561‐017‐0001‐8

Tierney, G., Posselt, D. J., & Booth, J. F. (2018). An examination of extratropical cyclone response to changes in baroclinicity and temperature in

an idealized environment. Climate Dynamics, 51(9–10), 3829–3846. https://doi.org/10.1007/s00382‐018‐4115‐5

Tomassini, L., Willett, M., Sellar, A., Lock, A., Walters, D., Whitall, M., et al. (2023). Confronting the convective gray zone in the global
configuration of the met office unified model. Journal of Advances in Modeling Earth Systems, 15(5), e2022MS003418. https://doi.org/10.
1029/2022ms003418

Ulbrich, U., Leckebusch, G. C., Grieger, J., Schuster, M., Akperov, M., Bardin, M. Y., et al. (2013). Are greenhouse gas signals of northern
hemisphere winter extra‐tropical cyclone activity dependent on the identification and tracking algorithm? Meteorologische Zeitschrift, 22(1),
61–68. https://doi.org/10.1127/0941‐2948/2013/0420

Villarini, G., & Vecchi, G. A. (2012). Twenty‐first‐century projections of north Atlantic tropical storms from CMIP5 models. Nature Climate

Change, 2(8), 604–607. https://doi.org/10.1038/nclimate1530

Wang, J., Kim, H.‐M., & Chang, E. K. M. (2017). Changes in Northern Hemisphere winter storm tracks under the background of Arctic

amplification. Journal of Climate, 30(10), 3705–3724. https://doi.org/10.1175/jcli‐d‐16‐0650.1

Zappa, G., Hawcroft, M. K., Shaffrey, L., Black, E., & Brayshaw, D. J. (2015). Extratropical cyclones and the projected decline of winter
Mediterranean precipitation in the CMIP5 models. Climate Dynamics, 45(7–8), 1727–1738. https://doi.org/10.1007/s00382‐014‐2426‐8
Zappa, G., Shaffrey, L. C., Hodges, K. I., Sansom, P. G., & Stephenson, D. B. (2013). A multimodel assessment of future projections of north
Atlantic and European extratropical cyclones in the CMIP5 climate models. Journal of Climate, 26(16), 5846–5862. https://doi.org/10.1175/
jcli‐d‐12‐00573.1

Zhao, M., & Knutson, T. (2024). Crucial role of sea surface temperature warming patterns in near‐term high‐impact weather and climate pro-

jection. npj Climate and Atmospheric Science, 7(130), 130. https://doi.org/10.1038/s41612‐024‐00681‐7

GENTILE ET AL.

11 of 11

 19448007, 2025, 2, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL112570 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License