RESEARCH LETTER
10.1029/2021GL096708

Key Points:

•

•

•

 The strength of cyclone wind speeds
are underestimated by CMIP6 models
 HighResMIP models represent the
structure and intensity of cyclones
better than CMIP6 models
 Elements of the large-scale
environment surrounding cyclones
are not improved in HighResMIP
simulations

Supporting Information:

Supporting Information may be found in
the online version of this article.

Correspondence to:

M. D. K. Priestley,
m.priestley@exeter.ac.uk

Citation:

Priestley, M. D. K., & Catto, J. L. (2022).
Improved representation of extratropical
cyclone structure in HighResMIP
models. Geophysical Research Letters,
49, e2021GL096708. https://doi.
org/10.1029/2021GL096708

Received 28 OCT 2021
Accepted 14 FEB 2022

© 2022. The Authors.
This is an open access article under
the terms of the Creative Commons
Attribution License, which permits use,
distribution and reproduction in any
medium, provided the original work is
properly cited.

PRIESTLEY AND CATTO

Improved Representation of Extratropical Cyclone Structure
in HighResMIP Models
Matthew D. K. Priestley1

 and Jennifer L. Catto1

1College of Engineering, Mathematics and Physical Sciences, University of Exeter, Exeter, UK

Abstract  General circulation models are broadly able to capture the shape and structure of extratropical
cyclones. Increased atmospheric resolution has been shown to improve the representation of cyclone structure.
However, the intensity of cyclones, and the strength of their winds, are commonly underestimated in models.
Using a cyclone compositing technique applied to the new generation HighResMIP and CMIP6 models, the
representation of cyclone wind speeds and airstreams is quantified. CMIP6 models are able to capture the
structure of cyclones, however winds associated with various airstreams within the cyclones are too weak.
HighResMIP models show considerable improvements, with a majority of cyclone-scale biases present in
the CMIP6 models reduced in both winter and summer seasons in the Northern and Southern hemispheres.
HighResMIP and CMIP6 models have similar biases on the large-scale, with both struggling to represent the
width of the upper-level jet.

Plain Language Summary  In order for accurate predictions of the future climate to be made,
models must be tested to see if they reproduce features in an accurate way. In this study, we have tested the
ability of climate models to represent the intensity and structure of extratropical cyclones. Previously, climate
models with a higher resolution have performed better at representing the structure of these cyclones, however
most models tend to fail to capture the intensity. Our results demonstrate that models do still struggle to capture
the intensity of cyclones, with wind speeds being too weak. However, cyclones simulated by the highest
resolution models do a much better job at simulating the intensity of the cyclones, and the strength of the wind
speeds within them. In order to study features within extratropical cyclones accurately, high resolution models
must be used.

1.  Introduction

General Circulation Models (GCMs) are commonly capable of reproducing the structural features of extratropical
cyclones (ETCs; Booth et al., 2018; Catto et al., 2010; Hawcroft et al., 2016). An accurate representation of ETCs
is important in GCMs for current and future risk assessment as they are commonly associated with extreme wind
(Browning, 2004), precipitation (Pfahl & Wernli, 2012), and waves (Catto & Dowdy, 2021). ETC structure is
commonly viewed from an airstream (conveyor belt) perspective, with three main features. The first is the warm
conveyor belt (WCB; Harrold, 1973), which is a stream of warm moist air ascending in the warm sector of ETCs.
Second, the cold conveyor belt (CCB; Carlson, 1980; Schultz, 2001) is often confined to the lower troposphere
and travels in the opposite direction to cyclone propagation. Finally, the dry intrusion (DI; Browning, 1997) is a
dry air stream that descends from the upper troposphere or lower stratosphere (Raveh-Rubin, 2017), behind the
cold front. For a more thorough review of cyclone airstreams and structure the readers are directed to Catto (2016)
and Schultz et al. (2019).

ETCs  are  commonly  evaluated  using  cyclone  centered  composites  (Bengtsson  et  al.,  2007,  2009;  Booth
et al., 2018; Catto et al., 2010; Dacre et al., 2012; Field & Wood, 2007; Kodama et al., 2019; Sinclair et al., 2020).
Compositing  methods  have  revealed  that  many  features  of  ETCs  are  well  represented  in  GCMs  (Bengtsson
et al., 2007; Booth et al., 2018; Catto et al., 2010; Govekar et al., 2014; Kodama et al., 2019). However, the wind
speed strength is commonly underestimated (Govekar et al., 2014; Naud et al., 2010). Previous studies have often
only considered individual models or a single hemisphere/region. There is a need to perform a systematic multi-
model evaluation of cyclone wind speeds associated with the various airstreams in both hemispheres.

The  new  generation  of  models  from  the  sixth  phase  of  the  Coupled  Model  Intercomparison  Project  (CMIP6;
Eyring et al., 2016) tend to have higher resolutions than previously studied CMIP5 and CMIP3 models. Increas-
ing atmospheric resolution has previously improved the simulation of cyclone intensity (Booth et al., 2018; Colle

1 of 10

Geophysical Research Letters

10.1029/2021GL096708

et al., 2013; Jung et al., 2012; Willison et al., 2013), however, the highest resolution CMIP6 models still under-
estimate  intensity  relative  to  numerous  reanalyzes  (Priestley  et  al.,  2020).  CMIP6  models  possess  horizontal
atmospheric resolution between 100 and 250 km (Taylor et al., 2017), yet current modeling capabilities allow
for simulations with 25–50 km resolution, with these models participating in the HighResMIP project (Haarsma
et  al.,  2016).  HighResMIP  models  have  shown  improvements  in  the  representation  of  blocking  (Schiemann
et  al.,  2020),  simulated  tropical  cyclone  intensity  and  frequency  (Roberts  et  al.,  2020),  and  in  the  number  of
explosive ETCs (Jiaxiang et al., 2020). It is hoped that any biases in ETC simulation in CMIP6, will be removed,
or significantly reduced, in HighResMIP models.

In this study we address three questions:

1.   Do CMIP6 models capture the structure and spatial extent of ETCs at the surface?
2.   Are cyclone airstreams structurally captured by CMIP6 models and are they of sufficient strength?
3.   What structural features are improved in HighResMIP models relative to CMIP6?

2.  Data & Methods

Throughout  this  study,  analysis  will  be  performed  on  the  December,  January,  February  (DJF)  and  June,  July,
August (JJA) periods, representing the Northern Hemisphere (NH) winter and summer, and the Southern Hemi-
sphere (SH) summer and winter respectively. All analysis will be conducted for the 1979–2014 period. The base-
line data set used for the model evaluation is the ERA5 reanalysis (Hersbach et al., 2020).

2.1.  CMIP6

The CMIP6 models used in this analysis are from the coupled historical simulations from the DECK set of exper-
iments (Eyring et al., 2016). Models were used that provided zonal (u) and meridional (v) wind at 850-hPa and
250-hPa, as well as mean sea level pressure (MSLP, psl) at 6-hourly resolution. Whenever modeling centers have
provided more than one model, a maximum of two models from that center are used in order to not over-weight a
modeling group in the model mean. In cases when two models are used, they must have either different nominal
resolutions for the atmospheric component or different atmospheric models (Taylor et al., 2017). This assumes
that the model simulations are not overly similar. The CMIP6 models have nominal atmospheric resolution of
either 100-km, 250-km, or 500-km resolution. In total 27 models are used from 20 model centers (see Table S1
in Supporting Information S1).

2.2.  HighResMIP

The higher resolution set of model simulations are taken from the HighResMIP hist-1950 experiment (Haarsma
et al., 2016) and all are fully coupled with identical forcings to the historical experiments. A majority of the High-
ResMIP models have nominal atmospheric resolutions that are higher than the CMIP6 models, at 25-km, 50-km,
or 100-km. In addition to the high resolution models, all modeling centers also provide a lower resolution model.
These models are useful to directly identify the impact of resolution, have nominal resolutions comparable to the
CMIP6 ensemble, and generally have grid spacing at least twice that of their high resolution counterpart. In total
6 high resolution models (and 6 low resolution counterparts) from 6 different modeling centers are used (Table
S2 in Supporting Information S1).

2.3.  Cyclone Identification, Tracking, and Compositing

Cyclones are identified and tracked using the method of Hodges (1994, 1995, 1999) applied to 850-hPa relative
vorticity. To be consistent with models of varying input resolution, and to remove the small-scales of the vorticity
field, data are first spectrally truncated to T42, with wavenumbers less than 5 also removed. Tracks are initialized
using a nearest neighbor approach and then smoothed via the minimization of a cost function. To ensure only
well developed and long-lived, mobile cyclones are analyzed, tracks must exist for at least 48 hr, have a maximum
vorticity of least 1 × 10 −5 s −1, and travel more than 1000-km from the point of origin.

The  cyclone  compositing  technique  used  is  from  Bengtsson  et  al.  (2007);  Bengtsson  et  al.  (2009);  Catto
et al. (2010); Dacre et al. (2012); Sinclai et al. (2020). In order to focus on similar, well developed cyclones.

PRIESTLEY AND CATTO

2 of 10

Geophysical Research Letters

10.1029/2021GL096708

Figure 1.  Composites of mean sea level pressure in the northern hemisphere for December, January, February (a–d) and June, July, August (e–h). Composites
are shown for ERA5 (a,e) with contours every 4-hPa. Biases relative to ERA5 are shown for the CMIP6 (b,f) and HighResMIP models (c,g). Differences between
HighResMIP and CMIP6 are shown in (d,h). Stippling in panels indicates where there is 80% model agreement on the sign of the bias. Units are hPa.

Only cyclones that are in the top 10% of the distribution for peak cyclonic vorticity are analyzed. For ERA5 this
equates to an average of 48.1 and 42.8 cyclones per season in the NH for DJF and JJA respectively. Composites
are produced for each season year of each model. For each season, hemisphere, and model, a unique vorticity
threshold is calculated for the 1979–2014 period to account for seasonality and model variability. To account for
variances in cyclone propagation, all fields are rotated and aligned such that all cyclones are traveling from west
to east. Composites of MSLP and winds are created at the time of peak vorticity for a 20° region surrounding the
cyclone and centered on the track point. Wind speed composites (and the u and v components) at 850-hPa and
250-hPa are examined in a system relative perspective, whereby the propagation speed of the cyclone (calculated
as the speed of the rotated cyclone from west to east) is subtracted from the wind speed to identify the winds
associated with the cyclone and therefore removing variability introduced from differing propagation speeds in
the different model groups (Figure S1 in Supporting Information S1).

3.  Results

3.1.  Surface Structure

For evaluating the surface structure and shape of ETCs, MSLP is used. In NH DJF the composite cyclone has a
10°-15° radius from the cyclone center (shown by the outer closed contour), which is well captured by the CMIP6
models  (Figures  1a  and  1b).  However,  ETCs  tend  to  be  too  shallow  with  a  minimum  pressure  of  970.1  hPa,
compared  to  968.3  hPa  in  ERA5  (p  <  0.05).  Models  tend  to  vary  considerably  in  their  surface  structure  and
cyclone depth (Figure S2 in Supporting Information S1), hence the limited consensus in Figure 1b. HighResMIP
models  tend  to  have  a  lower  MSLP  minimum  than  CMIP6  models,  with  an  average  simulated  minimum  of
967 hPa (Figure 1c), which is significantly deeper than ERA5 (p < 0.05). Furthermore, MSLP in HighResMIP
models is lower across most of the cyclone area, particularly to the north. This is mainly a result of the CMCC-
CM2-VHR4 model (Figure S3 in Supporting Information S1) simulating ETCs that are too deep by over 5 hPa
and  also  being  situated  in  a  meridional  pressure  gradient  that  is  considerably  stronger  than  any  of  the  other
models.

PRIESTLEY AND CATTO

3 of 10

Geophysical Research Letters

10.1029/2021GL096708

For  both  model  groups  the  sign  of  the  MSLP  bias  is  not  robust  across  models  at  the  cyclone  center,  or  the
surrounding  10°.  Examining  the  biases  individually  (Figures  S2,  S3  in  Supporting  Information  S1)  there  is
considerable variation in the MSLP  biases suggesting  that cyclone shape and surface structure  is  very model
dependent. Despite this, HighResMIP models do simulate robustly deeper MSLP than CMIP6, indicating the
influence of higher resolution. Furthermore, comparing the low and high resolution versions of HighResMIP (not
shown) also confirms that the higher resolution models systematically simulate ETCs with deeper MSLP, even
when excluding the outlier CMCC models (968.4 hPa low-res and 967 hPa high-res).

In JJA the average cyclone is smaller than in DJF and the closed contour area lies within ∼5° of the cyclone center
(Figure 1e). The minimum MSLP in ERA5 is 986.1 hPa, and therefore substantially weaker than in DJF. As in
DJF, the CMIP6 models struggle to capture the depth of the ETCs, with the minimum MSLP being significantly
too  high  (p  <  0.05)  with  an  average  of  988.3  hPa  (Figure  1f).  ETCs  in  the  HighResMIP  models  (Figures  1g
and 1h) simulate an average minimum MSLP of 986.3 hPa, which is not significantly different from ERA5. As
in DJF the direct impact of resolution is notable when comparing the HighResMIP models to their lower resolu-
tion counterparts, which have significantly lower minimum MSLP (p < 0.01), with an average of 987.9 hPa (not
shown).

In the SH (Figure S4 in Supporting Information S1) ETC size and structure is more consistent between the two
seasons than in the NH. With regards to the minimum MSLP a similar pattern of biases is seen as in the NH.
CMIP6 model ETCs are too shallow by 0.75–1.5 hPa, while HighResMIP models simulate a composite cyclone
that is up to 0.5 hPa too deep. Furthermore, there is continued evidence that CMIP6 models have a different and
variable structure of the MSLP field compared to ERA5, with lower pressures and variable signs of bias away
from the cyclone center, which is suggestive of a broader meridional extent of the cyclone and possible wider
trough in which the cyclones are situated. This is a feature that is largely reduced in the HighResMIP models,
although models are still inconsistent in the sign of bias (Figures S4d, S4h in Supporting Information S1).

3.2.  Lower Tropospheric Winds

The CCB (Carlson, 1980; Schultz, 2001) can be identified in cyclone composites of system relative winds at
850-hPa (Figure 2a) traveling rearwards relative to cyclone propagation, polewards of the center. In ERA5 the
peak  wind  speed  in  this  region  is  above  35  m  s −1  in  NH  DJF  (Figure  2a)  and  at  least  24.5  m  s −1  in  NH  JJA
(Figure 2e). CMIP6 models robustly underestimate the strength of this airstream by over 2 m s −1 across large
areas  poleward  and  rearward  of  the  cyclone  within  5°  of  the  cyclone  center  (Figure  2b),  consistent  with  the
weaker pressure gradient (Figure 1). This bias is largest on the westward flank of the cyclone where the CCB
tends to fully wrap around the cyclone, forming the low level jet (Schultz, 2001). In the HighResMIP models
there is a slight under-estimation to the northeast of the cyclone center, however, there is a large improvement
compared to CMIP6 on the western flank (Figure 2c), indicating an improvement in the CCB and low-level jet
representation in HighResMIP models (Figure 2d). The lower resolution variants of the HighResMIP models are
characterized by the same pattern of biases (not shown) but with a magnitude that is between the HighResMIP
and full compliment of CMIP6 models, further demonstrating the direct impact of improved resolution.

In  JJA  (Figures  2d–2h)  a  very  consistent  pattern  emerges,  with  CMIP6  models  robustly  underestimating  the
wind  strength  in  the  lower  troposphere,  with  minimal  biases  in  the  HighResMIP  models  (Figures  2f–2h).  In
JJA, due to the weaker nature of the cyclones the cyclonic wrapping of air is less apparent in the difference field
(Figures 2f–2h), with biases that are more symmetric around the cyclone center. In the earth relative perspective
(Figure S5 in Supporting Information S1) similar differences between model groups are evident, but due to the
additional component of the winds due to cyclone propagation, only the bias associated with the wrapping of the
CCB on the rear flank of the cyclones is evident.

Biases for DJF and JJA in the SH (Figure S6 in Supporting Information S1) are almost identical to NH DJF, with
a magnitude of biases in CMIP6 and HighResMIP that reflects those identified in the NH. Despite improvements
in the representation of MSLP minima and lower tropospheric winds in HighResMIP, there are minimal improve-
ments in the structural bias of cyclone track density relative to CMIP6 (Priestley et al., 2020) for NH DJF (Figure
S7 in Supporting Information S1) or any other season in either hemisphere, suggesting that these improvements
are not due to different geographical locations of the cyclones.

PRIESTLEY AND CATTO

4 of 10

Geophysical Research Letters

10.1029/2021GL096708

Figure 2.  Composites of 850-hPa system relative wind speed in the northern hemisphere for December, January, February (a–d) and June, July, August (e–h).
Composites are shown for ERA5 (a,e). Biases relative to ERA5 are shown for the standard CMIP6 models (b,f) and the HighResMIP models (c,g). Differences between
HighResMIP and CMIP6 are shown in (d,h). Units are m s −1. The green (70°-110° anticlockwise from due East) and yellow (160°–200°) sectors in (b) are those used
for the analysis in Figure 3. Stippling in panels indicates where there is 80% model agreement on the sign of the bias.

3.3.  CCB Variability

To  quantify  variability  across  the  models  a  Gaussian  kernel  density  estimation  of  the  maximum  wind  speed
and its distance from cyclone center in two sectors at 850-hPa for each seasonal composite cyclone has been
performed. The first sector focuses on the winds on the poleward flank of the cyclone, and the second on the bias
associated with the wrapping around of the CCB to form the low-level jet on the rear flank (green and yellow
sectors in Figure 2b). Focusing on the maxima of the 850-hPa wind speeds, there are two clusters in the ERA5
data (Figure 3a), which are mainly a result of the 0.5° composite resolution. The largest is ∼3° from the center
with speeds of ∼35.5 m s −1 and the second situated ∼3.5° from the center, with weaker winds. In CMIP6 models
most of the cyclones have maxima too far from the cyclone center and too weak by over 1 m s −1 (as in Figure 2b).
The HighResMIP models capture both the ERA5 clusters, although tend to have a higher proportion of data in the
weaker and more distant cluster. There is also a peak even further from the cyclone center with even weaker winds
in CMIP6. This suggests that if models simulate a circulation that is too weak, it is also too far from the cyclone
center and that only a small number of cyclones (<10%) in CMIP6 simulate the strongest winds sufficiently close
to the cyclone center.

In JJA (Figure 3b) a similar pattern is evident, however HighResMIP models tend to have a higher proportion of
cyclones with a circulation close to the cyclone center. However, they are still too weak by ∼1 m s −1 (as noted in
Figure 2c). A majority of cyclones in CMIP6 have too weak and distant circulations, although ∼20% do simulate
the correct distance/wind speed. Conversely, a similar proportion are also considerably further from the center
and too weak.

On the rear flank of the cyclones in DJF (Figure 3c) there are two groupings in ERA5 at 3° and 3.5° from the
cyclone center with speeds of ∼30 m s −1. The HighResMIP models reproduce this distribution very well and
capture both groups (as in Figure 2). Some CMIP6 cyclones (∼5%) do capture the intensity distance maxima
of ERA5 and HighResMIP, however the majority of CMIP6 cyclones have maximum winds too far from the
cyclone center and too weak relative to both HighResMIP and ERA5. Furthermore, there is a grouping of ∼30%
of CMIP6 cyclones that are substantially further from the cyclone center (∼ 4.75°) and too weak by 3–5 m s −1.

PRIESTLEY AND CATTO

5 of 10

Geophysical Research Letters

10.1029/2021GL096708

Figure 3.  Gaussian kernel density estimation (KDE) of scattered maximum wind speed against its distance from the cyclone center for sectors from (a–b) 70°-110°
and (c–d) 160°-200° in (a,c) December, January, February and (b,d) June, July, August for the northern hemisphere. KDEs are shown for ERA5 (black), CMIP6
(orange) and HighResMIP (blue). Crosses indicate the maximum density of each KDE. Degrees for the sectors are moving anticlockwise around the cyclone, with 0°
representing East and are illustrated in Figure 2b. Contours levels are from 0.05 to 0.95 in intervals of 0.15.

This indicates that for CMIP6 models that fail to capture the strength of the wind speeds, the associated airstream
will be situated further from the cyclone center (r = −0.57). These patterns and groupings continue to be evident
in JJA (Figure 3d), with performances of HighResMIP and CMIP6 models being similar to DJF.

3.4.  Upper Tropospheric Winds

In the upper-troposphere (250-hPa) ETCs are commonly characterized by reduced ascent on their equatorward
and forward flanks relative to lower levels (Figure S8 in Supporting Information S1), with a more horizontal flow
that is associated with the outflow of the WCB near the tropopause (Dacre et al., 2012; Sinclair et al., 2020).
Two branches of the WCB are commonly identifiable that turn cyclonically and anticyclonically (Browning &
Roberts, 1994; Thorncroft et al., 1993) and diverge in the upper troposphere (as in Catto et al., 2010). The domi-
nant feature identified in the system relative winds in ERA5 (Figures 4a and 4e) is the upper-level jet, which has
a maximum speed of at least 50 m s −1 in DJF and rotates cyclonically around the cyclone from the northwest to
the southern flank. A similar picture is present in JJA (Figure 4e), except with a weaker jet that has a maximum
of over 30 m s −1. The overall circulation is cyclonic around the center, however, anticyclonic motion is evident to
the southeast of the cyclone center that is associated with the WCB outflow.

The CMIP6 models robustly underestimate wind speeds immediately southeast and east of the cyclone center
in DJF by up to 3.6 m s −1 (Figure 4b). This bias is located close to the region of maximum ascent (Figure S8 in

PRIESTLEY AND CATTO

6 of 10

Geophysical Research Letters

10.1029/2021GL096708

Figure 4.  As Figure 2 but for system relative wind speeds at 250-hPa.

Supporting Information S1). This bias, coupled with the models underestimating lower-level convergence and
upper-level divergence (Figure S9 in Supporting Information S1) in the region of maximum ascent (Figure S8 in
Supporting Information S1) suggests that the ascending WCB is incorrectly represented in the CMIP6 models.

One dominant feature in the CMIP6 composites (Figure 4b) is a positive bias 5°-15° equatorward of the cyclone
of up to 3.6 m s −1. This is a result of the jet being too broad and is largely driven by an overly strong zonal compo-
nent of the wind (Figure S10 in Supporting Information S1), indicating errors in the large-scale jet structure.
However, this feature is outside the core cyclone area (as identified in Figure 1a) so the bias is not directly related
to the cyclones.

The  HighResMIP  models  feature  considerably  reduced  biases  to  the  south  and  east  of  the  cyclone  center
(Figures  4c  and  4d).  Therefore,  higher  resolution  is  likely  contributing  to  an  improved  representation  of  the
ascending  branch  of  the  cyclones  and  the  increased  upper-level  divergence  relative  to  CMIP6  (Figure  S9h  in
Supporting  Information  S1)  implies  stronger  vertical  velocities.  The  HighResMIP  models  also  over-estimate
winds 5°-15° equatorward of the ETCs, associated with a too broad zonal component of the jet (Figure S10c in
Supporting Information S1), suggesting that this bias is not improved with additional atmospheric resolution.
Furthermore, both HighResMIP and CMIP6 models feature an under-estimation of wind speeds to the north-
west of the cyclone in the cold sector. This is a region where winds are northerly and is commonly associated
with the origins of the descending DI and therefore the region of descent within the cyclone may be incorrectly
represented.

One bias that is only evident when isolating the different wind components is the models' failure to represent
the anticyclonic turning of winds to the southeast of cyclones. The northerly wind is robustly under-estimated
by over 3.6 m s −1, with no improvement notable in the HighResMIP models (Figure S11 in Supporting Infor-
mation S1). This bias does not appear in the full wind due to the overly strong zonal component of the wind that
characterizes the equatorward side of the cyclone. Consequently, the wind speed appears correct in this sector, but
the orientation of the wind vectors is incorrect and the large-scale flow is overly zonal (consistent with Priestley
et al., 2020).

In JJA the models have similar characteristics to DJF (Figures 4f–4h). The broader zonal component of the wind
is still present, but considerably weaker in JJA (Figures 4f and 4g), and therefore the band of increased wind

PRIESTLEY AND CATTO

7 of 10

Geophysical Research Letters

10.1029/2021GL096708

speeds to the south of the cyclone is less clear. CMIP6 models continue to robustly underestimate the strength
of  the  winds  to  the  southeast  and  east  of  the  cyclone  center,  with  HighResMIP  improved  relative  to  CMIP6
(Figures 4g and 4h). The anticyclonic circulation to the southeast of cyclones is less evident in JJA as cyclones
are weaker. However, both CMIP6 and HighResMIP continue to have biases associated with the anticyclonic part
of the circulation (Figure S11 in Supporting Information S1).

All biases present in the NH are identifiable with similar magnitudes and locations in the SH (Figure S12 in
Supporting Information S1). The zonal component of the jet continues to be too broad and the winds associated
with  the  WCB  outflow  are  too  weak  in  CMIP6  models,  with  improvements  notable  in  HighResMIP  models.
Furthermore, all models insufficiently represent the anticyclonic flow to the northeast of cyclones.

4.  Discussion and Conclusions

In this study the benefits of high resolution modeling on simulating ETC structure and circulation are explored
and quantified using the HighResMIP and CMIP6 models. The main conclusions are as follows:

1.   CMIP6 models generally capture the features of ETCs, however the shape and structure of the surface cyclone

is very model dependent, and cyclone wind speeds throughout the troposphere tend to be too weak.

2.   HighResMIP models decrease most of the biases in CMIP6 models at the cyclone scale. Wind speeds in the

lower and upper troposphere are stronger and surface pressures deeper.

3.   Large-scale  features  of  the  cyclone  environment  are  not  improved  with  increased  resolution.  These  are  an
overly broad and zonal jet, and an insufficient anticyclonic turning of the flow to the southeast of cyclones in
the upper-troposphere.

Despite  improvements  in  the  representation  of  a  majority  of  the  cyclone  features  in  the  winter  and  summer
seasons of the NH and SH, there are minimal improvements in the geographical distribution of cyclones in High-
ResMIP models relative to CMIP6 (Figure S7 in Supporting Information S1). Generally, all biases associated
with the CCB and the inflow and ascent of the WCB in CMIP6 are reduced, and are associated with a deeper
surface cyclone, in HighResMIP. Previous studies such as Bengtsson et al. (2009) and Booth et al. (2018) found
improved representation of cyclones with higher resolution, and the HighResMIP models have been noted to have
considerable benefits compared to standard resolution CMIP6 models in terms of explosive ETC wind speed and
tropical cyclone intensity (Jiaxiang et al., 2020; Roberts et al., 2020), which we add further evidence to in this
study, with the models offering improvements over their lower resolution counterparts. Improved resolution has
also shown to be important in future projections, with higher resolution models projecting greater storminess in
the North Atlantic by the end of the century (Grist et al., 2021). Therefore, a key research directive should be to
assess what processes associated with higher resolution are driving the improvements in HighResMIP models.

Associated with the negative wind speed biases and underestimation of divergence in the WCB outflow region in
CMIP6 models (and subsequent improvement in HighResMIP) it is likely that ascent rates are too weak in CMIP6
models (as in Naud et al., 2010; Govekar et al., 2014), or that the outflow is at the wrong level or ascent in the
wrong place. Too weak ascent is a common problem in models which often have insufficient representation of
diabatic processes and strong temperature gradients (Willison et al., 2013), which contribute to the ascent in the
WCB (Kuo et al., 1991). As HighResMIP models likely offer an improved representation of diabatic processes it
is likely that there are also improvements in the ascent rate of the WCBs relative to CMIP6.

CMIP6 models have variable performance for the strength of simulated wind speeds. When wind speeds are too
weak the associated airstreams tend to be further from the cyclone center, and likely broader than in ERA5 and
HighResMIP.  Overall,  the  structure  and  circulation  biases  in  CMIP6  are  somewhat  similar  to  other  modeling
studies, with CMIP6 models simulating the correct features at the correct vertical levels within the cyclone (Catto
et al., 2010; Kodama et al., 2019; Sinclair et al., 2020). Models particularly struggle in reproducing the structure
of the surface cyclone and the associated MSLP depth, with a variety of structures evident across both the CMIP6
and HighResMIP models. As MSLP is strongly influenced by large-scale patterns (Hoskins & Hodges, 2002) it
is unlikely to provide consistent results with regards to cyclone size, surface structure/shape, or peak intensity.

HighResMIP models show improvements over CMIP6 and their lower resolution counterparts on the cyclone
scale, yet do not reduce biases on the large-scale, such as the overly broad and zonal jet, the reduced anticyclonic

PRIESTLEY AND CATTO

8 of 10

Acknowledgments
M. D. K. Priestley and J. L. Catto are
supported by the Natural Environment
Research Council (NERC) grant NE/
S004645/1. We would like to thank the
two anonymous reviewers, whose helpful
and constructive feedback helped improve
this manuscript.

Geophysical Research Letters

10.1029/2021GL096708

turning of air associated with the WCB near the tropopause, and the equatorward flow of air behind the cold front
that may associated with the DI and insufficient descent. Errors associated with the WCB turning may be linked
to the representation of the stratosphere and its interaction with the troposphere. None of the HighResMIP models
have an increase in vertical resolution compared to their standard resolution models, and therefore are not likely
to feature improvements in stratosphere-troposphere interactions. Increases in vertical resolution may be required
to aid the improvements noted with horizontal resolution.

Data Availability Statement

ERA5  reanalysis  is  available  from  the  Copernicus  Climate  Change  Service  Climate  Data  Store  (https://doi.
org/10.24381/cds.bd0915c6). CMIP6 and HighResMIP data is publicly available through the Earth System Grid
Federation (https://esgf-node.llnl.gov/projects/cmip6/). The CMIP6 and HighResMIP models used in this study
are listed in Tables S1 and S2 respectively of the Supporting Information. The cyclone tracking and compositing
algorithm TRACK is available on request from Kevin Hodges at https://gitlab.act.reading.ac.uk/track/track.

References
Bengtsson, L., Hodges, K. I., Esch, M., Keenlyside, N., Kornblueh, L., Luo, J.-J., & Yamagata, T. (2007). How may tropical cyclones change in
a warmer climate? Tellus A: Dynamic Meteorology and Oceanography, 59(4), 539–561. https://doi.org/10.1111/j.1600-0870.2007.00251.x
Bengtsson,  L.,  Hodges,  K.  I.,  &  Keenlyside,  N.  (2009).  Will  extratropical  storms  intensify  in  a  warmer  climate?  Journal  of  Climate,  22(9),

2276–2301. https://doi.org/10.1175/2008JCLI2678.1

Booth, J. F., Naud, C. M., & Willison, J. (2018). Evaluation of extratropical cyclone precipitation in the North Atlantic basin: An analysis of

ERA-interim, WRF, and two CMIP5 models. Journal of Climate, 31(6), 2345–2360. https://doi.org/10.1175/JCLI-D-17-0308.1

Browning,  K.  A.  (1997).  The  dry  intrusion  perspective  of  extra-tropical  cyclone  development.  Meteorological  Applications,  4(4),  317–324.

https://doi.org/10.1017/S1350482797000613

Browning, K. A. (2004). The sting at the end of the tail: Damaging winds associated with extratropical cyclones. Quarterly Journal of the Royal

Meteorological Society, 130(597), 375–399. https://doi.org/10.1256/qj.02.143

Browning, K. A., & Roberts, N. M. (1994). Structure of a frontal cyclone. Quarterly Journal of the Royal Meteorological Society, 120(520),

1535–1557. https://doi.org/10.1002/qj.49712052006

Carlson, T. N. (1980). Airflow through midlatitude cyclones and the comma cloud pattern. Monthly Weather Review. 108, 1498–1509. https://doi.

org/10.1175/1520-0493(1980)108<1498:atmcat>2.0.co;2

Catto,  J.  L.  (2016).  Extratropical  cyclone  classification  and  its  use  in  climate  studies.  Reviews  of  Geophysics,  54(2),  486–520.  https://doi.

org/10.1002/2016RG000519

Catto, J. L., & Dowdy, A. (2021). Understanding compound hazards from a weather system perspective. Weather and Climate Extremes, 32,

100313. https://doi.org/10.1016/j.wace.2021.100313

Catto, J. L., Shaffrey, L. C., & Hodges, K. I. (2010). Can climate models capture the structure of extratropical cyclones? Journal of Climate, 23(7),

1621–1635. https://doi.org/10.1175/2009JCLI3318.1

Colle, B. A., Zhang, Z., Lombardo, K. A., Chang, E., Liu, P., & Zhang, M. (2013). Historical evaluation and future prediction of eastern North
American and western Atlantic extratropical cyclones in the CMIP5 models during the cool season. Journal of Climate, 26(18), 6882–6903.
https://doi.org/10.1175/JCLI-D-12-00498.1

Dacre, H. F., Hawcroft, M. K., Stringer, M. A., & Hodges, K. I. (2012). An extratropical cyclone Atlas: A tool for illustrating cyclone structure and
evolution characteristics. Bulletin of the American Meteorological Society, 93(10), 1497–1502. https://doi.org/10.1175/BAMS-D-11-00164.1
Eyring, V., Bony, S., Meehl, G. A., Senior, C. A., Stevens, B., Stouffer, R. J., & Taylor, K. E. (2016). Overview of the coupled model Inter-
comparison project phase 6 (CMIP6) experimental design and organization. Geoscientific Model Development, 9(5), 1937–1958. https://doi.
org/10.5194/gmd-9-1937-2016

Field,  P.  R.,  &  Wood,  R.  (2007).  Precipitation  and  cloud  structure  in  midlatitude  cyclones.  Journal  of  Climate,  20(2),  233–254.  https://doi.

org/10.1175/JCLI3998.1

Govekar, P. D., Jakob, C., & Catto, J. (2014). The relationship between clouds and dynamics in Southern Hemisphere extratropical cyclones in the
real world and a climate model. Journal of Geophysical Research: Atmospheres, 119(11), 6609–6628. https://doi.org/10.1002/2013JD020699
Grist,  J.  P.,  Josey,  S.  A.,  Sinha,  B.,  Catto,  J.  L.,  Roberts,  M.  J.,  &  Coward,  A.  C.  (2021).  Future  evolution  of  an  eddy  rich  ocean  associated
with  enhanced  east  Atlantic  storminess  in  a  coupled  model  projection.  Geophysical  Research  Letters,  48(7),  e2021GL092719.  https://doi.
org/10.1029/2021GL092719

Haarsma, R. J., Roberts, M. J., Vidale, P. L., Senior, C. A., Bellucci, A., Bao, Q., et al. (2016). High resolution model Intercomparison project

(HighResMIP v1.0) for CMIP6. Geoscientific Model Development, 9(11), 4185–4208. https://doi.org/10.5194/gmd-9-4185-2016

Harrold, T. W. (1973). Mechanisms influencing the distribution of precipitation within baroclinic disturbances. Quarterly Journal of the Royal

Meteorological Society, 99(420), 232–251. https://doi.org/10.1002/qj.49709942003

Hawcroft, M. K., Shaffrey, L. C., Hodges, K. I., & Dacre, H. F. (2016). Can climate models represent the precipitation associated with extratrop-

ical cyclones? Climate Dynamics, 47(3), 679–695. https://doi.org/10.1007/s00382-015-2863-z

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz-Sabater, J., et al. (2020). The ERA5 global reanalysis. Quarterly Journal

of the Royal Meteorological Society, 146(730), 1999–2049. https://doi.org/10.1002/qj.3803

Hodges, K. I. (1994). A general method for tracking analysis and its application to meteorological data. Monthly Weather Review. 122, 2573–

2586. https://doi.org/10.1175/1520-0493(1994)122<2573:agmfta>2.0.co;2

Hodges,  K.

I.

(1995).  Feature

tracking  on

the  unit

sphere.  Monthly  Weather  Review.  123,  3458–3465.  https://doi.

org/10.1175/1520-0493(1995)123<3458:ftotus>2.0.co;2

Hodges,  K.

for
org/10.1175/1520-0493(1999)127<1362:acfft>2.0.co;2

(1999).  Adaptive  constraints

I.

feature

tracking.  Monthly  Weather  Review.  127,  1362–1373.  https://doi.

PRIESTLEY AND CATTO

9 of 10

Geophysical Research Letters

10.1029/2021GL096708

Hoskins, B. J., & Hodges, K. I. (2002). New perspectives on the Northern hemisphere winter storm tracks. Journal of the Atmospheric Sciences.

59, 1041–1061. https://doi.org/10.1175/1520-0469(2002)059<1041:npotnh>2.0.co;2

Jiaxiang, G., Shoshiro, M., Roberts, M. J., Haarsma, R., Putrasahan, D., Roberts, C. D., et al. (2020). Influence of model resolution on bomb cyclones
revealed  by  HighResMIP-PRIMAVERA  simulations.  Environmental  Research  Letters,  15(8),  084001.  https://doi.org/10.1088/1748-9326/
ab88fa

Jung, T., Miller, M. J., Palmer, T. N., Towers, P., Wedi, N., Achuthavarier, D., et al. (2012). High-resolution global climate simulations with the
ECMWF model in project athena: Experimental design, model climate, and seasonal forecast skill. Journal of Climate, 25(9), 3155–3172.
https://doi.org/10.1175/JCLI-D-11-00265.1

Kodama, C., Stevens, B., Mauritsen, T., Seiki, T., & Satoh, M. (2019). A new perspective for future precipitation change from intense extratrop-

ical cyclones. Geophysical Research Letters, 46(21), 12435–12444. https://doi.org/10.1029/2019GL084001

Kuo, Y., Shapiro, M. A., & Donall, E. G. (1991). The interaction between baroclinic and diabatic processes in a numerical simulation of a rapidly
intensifying extratropical marine cyclone. Monthly Weather Review. (Vol. 119, pp. 368–384). https://doi.org/10.1175/1520-0493(1991)119<
0368:tibbad>2.0.co;2

Naud, C. M., Genio, A. D. D., Bauer, M., & Kovari, W. (2010). Cloud vertical distribution across warm and cold fronts in CloudSat-CALIPSO

data and a general circulation model. Journal of Climate, 23(12), 3397–3415. https://doi.org/10.1175/2010JCLI3282.1

Pfahl, S., & Wernli, H. (2012). Quantifying the relevance of cyclones for precipitation extremes. Journal of Climate, 25(19), 6770–6780. https://

doi.org/10.1175/JCLI-D-11-00705.1

Priestley, M. D. K., Ackerley, D., Catto, J. L., Hodges, K. I., McDonald, R. E., & Lee, R. W. (2020). An overview of the extratropical storm tracks

in CMIP6 historical simulations. Journal of Climate, 33(15), 6315–6343. https://doi.org/10.1175/JCLI-D-19-0928.1

Raveh-Rubin, S. (2017). Dry intrusions: Lagrangian climatology and dynamical impact on the planetary boundary layer. Journal of Climate,

30(17), 6661–6682. https://doi.org/10.1175/JCLI-D-16-0782.1

Roberts,  M.  J.,  Camp,  J.,  Seddon,  J.,  Vidale,  P.  L.,  Hodges,  K.,  Vanniere,  B.,  et  al.  (2020).  Impact  of  model  resolution  on  tropical  cyclone
simulation  using  the  HighResMIP-PRIMAVERA  multimodel  ensemble.  Journal  of  Climate,  33(7),  2557–2583.  https://doi.org/10.1175/
JCLI-D-19-0639.1

Schiemann, R., Athanasiadis, P., Barriopedro, D., Doblas-Reyes, F., Lohmann, K., Roberts, M. J., et al. (2020). Northern hemisphere blocking
simulation in current climate models: Evaluating progress from the climate model Intercomparison project phase 5 to 6 and sensitivity to
resolution. Weather and Climate Dynamics, 1(1), 277–292. https://doi.org/10.5194/wcd-1-277-2020

Schultz, D. M. (2001). Reexamining the cold conveyor belt. Monthly Weather Review. 129, 2205–2225. https://doi.org/10.1175/1520-0493(200

1)129<2205:rtccb>2.0.co;2

Schultz, D. M., Bosart, L. F., Colle, B. A., Davies, H. C., Dearden, C., Keyser, D., et al. (2019). Extratropical cyclones: A century of research on

meteorology’s centerpiece. Meteorological Monographs, 59, 16–116. https://doi.org/10.1175/AMSMONOGRAPHS-D-18-0015.1.56

Sinclair, V. A., Rantanen, M., Haapanala, P., Räisänen, J., & Järvinen, H. (2020). The characteristics and structure of extra-tropical cyclones in a

warmer climate. Weather and Climate Dynamics, 1(1), 1–25. https://doi.org/10.5194/wcd-1-1-2020

Taylor, K. E., Juckes, M., Balaji, V., Cinquini, L., Denvil, S., Durack, P. J., et al. (2017). CMIP6 global attributes, DRS, filenames, directory
structure and, CV’s (Tech. Rep. No. v6.2.6). Retrieved from https://goo.gl/v1drZl: Program for Climate Model Diagnosis and Intercomparison
Thorncroft, C. D., Hoskins, B. J., & McIntyre, M. E. (1993). Two paradigms of baroclinic-wave life-cycle behaviour. Quarterly Journal of the

Royal Meteorological Society, 119(509), 17–55. https://doi.org/10.1002/qj.49711950903

Willison, J., Robinson, W. A., & Lackmann, G. M. (2013). The importance of resolving mesoscale latent heating in the North Atlantic storm track.

Journal of the Atmospheric Sciences, 70(7), 2234–2250. https://doi.org/10.1175/JAS-D-12-0226.1

PRIESTLEY AND CATTO

10 of 10

