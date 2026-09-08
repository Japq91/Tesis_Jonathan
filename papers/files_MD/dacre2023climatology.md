RESEARCH ARTICLE
10.1029/2023JD039239

Key Points:

•

•

•

 The initial moisture content of
extratropical cyclones is removed
via precipitation within 30 hr after
cyclogenesis
 Local evaporation and moisture flux
convergence doubles the precipitating
phase of extratropical cyclones
 The feeder airstream provides a
continuous supply of moisture to
cyclones in the developing stage of
their evolution

Correspondence to:

H. F. Dacre,
h.f.dacre@reading.ac.uk

Citation:

Dacre, H. F., Martinez-Alvarado, O.,
& Hodges, K. I. (2023). Precipitation
efficiencies in a climatology of Southern
Ocean extratropical cyclones. Journal
of Geophysical Research: Atmospheres,
128, e2023JD039239. https://doi.
org/10.1029/2023JD039239

Received 11 MAY 2023
Accepted 27 NOV 2023

© 2023. The Authors.
This is an open access article under
the terms of the Creative Commons
Attribution License, which permits use,
distribution and reproduction in any
medium, provided the original work is
properly cited.

DACRE ET AL.

Precipitation Efficiencies in a Climatology of Southern Ocean
Extratropical Cyclones
, O. Martinez-Alvarado2
H. F. Dacre1

, and K. I. Hodges1,2

1Department of Meteorology, University of Reading, Reading, UK, 2National Centre for Atmospheric Science, University of
Reading, Reading, UK

Abstract  Precipitation efficiency refers to the amount of water that is lost from the atmosphere through
precipitation compared to the available water vapor in the atmosphere. This metric plays a critical role in
understanding precipitation patterns. However, calculating precipitation efficiency for extratropical cyclones
can be challenging because cyclones are dynamic and move through the atmosphere as they evolve. To
overcome this challenge, our study uses ERA5 reanalysis data to estimate precipitation efficiencies for 400
Southern Ocean cyclones, with a frame of reference that moves with the individual cyclones. Our findings
indicate that at maximum intensity, average precipitation efficiencies reach a maximum of 60%/6 hr near the
warm front where ascent rates are the largest. Typically, within 24–36 hr after cyclogenesis, all of the initial
water vapor available within 500 km of a cyclone center is lost due to precipitation. However, a cyclone's
precipitating phase is prolonged due to local evaporation and moisture flux convergence (MFC), which
replenish the moisture lost via precipitation. Close to the cyclone center, MFC provides additional moisture
from the environment into which cyclones are traveling. On average, this extends a cyclone's precipitation
phase to over 60 hr after cyclogenesis. Thus, while moisture from the genesis location is quickly removed
from the cyclone via precipitation, cyclones are replenished by moisture along their track, which doubles the
timescale  for a cyclone's precipitating phase.

Plain Language Summary  Precipitation efficiency is a measure of how much water in the
atmosphere falls as rain compared to how much is available to fall. In this study, we estimate how efficient
precipitation is for 400 cyclones in the Southern Ocean. We find that when the cyclones are strongest, about
60% of the available water vapor turns into rain every 6 hr near the warm front of the cyclone where air is rising
rapidly. Normally, within a day or two of a cyclone forming, all of the available water vapor in the cyclone gets
turned into rain. However, the rain can persist for longer because cyclones pick up more moisture as they move,
which gets turned into more rain. This can make the rain from a cyclone last on average for 60 hr, even after the
initial moisture is all gone.

1.  Introduction

The precipitation associated with extratropical cyclones can lead to extensive flooding causing damage to life,
infrastructure, crops, and property. In the subtropics cyclone intensity is a good predictor of cyclone precipita-
tion accumulation since moisture is readily available for conversion into precipitation (Pfahl & Sprenger, 2016).
However, in the extratropics, the availability of moisture is limited and so becomes an important factor in cyclone
precipitation totals. Since cyclones usually travel polewards during their lifecycle, the availability of moisture
typically reduces. Thus, an interesting feature of extratropical cyclones is that their precipitation maximum gener-
ally occurs prior to their maximum dynamical strength either due to reduced moisture availability or due to the
diabatic heating that occurs within the maximum precipitation phase further enhancing the dynamical intensity
of  cyclones  (Bengtsson  et  al.,  2009;  Booth  et  al.,  2018).  The  mean  flow  in  the  extratropics  is  approximately
zonal with most meridional transport of moisture occurring in the vicinity of extratropical cyclones. This merid-
ional transport of moisture occurs in filaments of high water vapor flux within the warm sector of extratropical
cyclones, known as atmospheric rivers (Newell et al., 1992). Sinclair and Dacre (2019) showed that at 50°S, a
cyclone's genesis latitude is the most important factor in determining the amount of moisture a cyclone transports
to this latitude, but at 65°S, genesis latitude is no longer a significant factor. In this study we will explore the
reason for this and test the hypothesis that as cyclones travel poleward the original moist air at cyclogenesis is
replaced by moisture evaporated from higher latitudes. In particular, we aim to answer the following questions.
How long would it take to deplete all of a cyclone's initial moisture via precipitation? If local evaporation or

1 of 11

Journal of Geophysical Research: Atmospheres

10.1029/2023JD039239

moisture flux convergence (MFC) into the cyclone occurs, then replenishment of the cyclone's moisture content
takes place. By how much does this moisture replenishment extend the precipitating phase of a cyclone? Finally,
from where does the moisture leading the replenishment originate?

Several studies have performed moisture tagging using model data to quantify the contribution of subtropical
moisture to the Total Column Water Vapor (TCWV) or precipitation when atmospheric rivers reach land. The
ratio of subtropical moisture to the TCWV or precipitation at landfall is on average 25% (Hu & Dominguez, 2019),
but for individual cyclones ranges from 10% for moisture transported more than 30°N latitude from their genesis
latitude before making landfall (Sodemann & Stohl, 2013) to over 50% for moisture transported less than 15°N
latitude from their genesis latitude before making landfall (Eiras-Barca et al., 2017; Rea et al., 2023). Thus, the
contribution of sub-tropical moisture is highly variable from case-to-case but typically decreases the further the
cyclones travel from the subtropics. These studies assume that evaporation or convergence of local moisture along
the cyclone path is responsible for the remaining moisture or precipitation.

The  relative  contribution  from  evaporation  or  convergence  and  how  they  vary  as  the  cyclones  evolve  can  be
quantified using the moisture budget. The ratio of different terms in the moisture budget allows replenishment
or drying efficiencies to be determined. Precipitation efficiency (PE) refers to the ratio of the water that is lost
from the atmosphere through precipitation to the available moisture in the atmosphere. It can be calculated on a
global domain, using monthly or annual averaged values (Tuller, 1971) or for an individual moving mesoscale or
synoptic-scale feature such as a thunderstorm, tropical or extratropical cyclone using instantaneous or accumu-
lated values. There are many ways of estimating the PE depending on the method used to determine the available
moisture. These include estimates of total column water vapor (Lutz, 1977; Stewart, 1996), condensation rate
(Ferrier  et  al.,  1996;  Hobbs  et  al.,  1980),  moisture  inflow  (MFC)  (Browning  &  Harrold,  1970),  total  column
water vapor plus MFC (Guo et al., 2015), and evaporation plus MFC (Li et al., 2002). The range of methods and
variation in accumulation periods makes comparison between studies difficult. For example, Hobbs et al. (1980)
calculate precipitation efficiencies, using instantaneous precipitation and condensation rates. They find precip-
itation efficiencies of 40%–50% for a warm sector rainband and precipitation efficiencies of up to 80% in their
cold-frontal rainband. Guo et al. (2015) calculate precipitation efficiencies as the ratio of accumulated precipita-
tion over a 10 hr period to the accumulated evaporation and MFC over the same period. They estimated that the
PE was 67% in the warm sector of the cyclone they studied. While the exact numerical values in these studies
cannot be compared, studies generally agree that precipitation efficiencies are relatively high in the vicinity of
individual extratropical cyclones studied. In this study, we will extend this analysis to estimate precipitation effi-
ciencies for a whole climatology of cyclones.

High precipitation efficiencies indicate that moisture is rapidly lost from cyclones resulting in a short precipita-
tion phase. However, observations show that cyclones typically precipitate for longer than one day. Therefore,
moisture must be supplied to the cyclone to extend the precipitation phase. Previous studies investigating mois-
ture convergence near cyclones have identified the feeder airstream (FA) as an important low-level airflow for
transporting moisture into and out of the center of cyclones and thus leading to the replenishment or depletion
of moisture. It has been found that moisture at the head of an atmospheric river accelerates towards the cyclone
center in the anticyclonically turning branch of the FA, feeding moisture to the base of the warm conveyor belt
(WCB) where it then rises to form precipitation (Bui & Spengler, 2021; H. F. Dacre et al., 2019; Demirdjian
et al., 2022; Papritz et al., 2021). Conversely, moisture in the remainder of the atmospheric river travels slower
than  the  cyclone  propagation  speed  resulting  in  the  export  of  moisture  from  the  cyclone  by  the  cyclonically
turning branch of the FA (Cuckow et al., 2022; H. F. Dacre et al., 2015; Xu et al., 2022). In this study, we will
determine the extent to which low-level cyclone airflows redistribute moisture around cyclones, leading to the
increase or decrease of general precipitation efficiencies.

2.  Method

2.1.  ERA5 Data

In  this  study,  we  use  the  European  Center  for  Medium-Range  Weather  Forecasts  (ECMWF)  fifth  generation
reanalysis data set (ERA5). It provides a comprehensive view of the state of the Earth's atmosphere, land surface,
and oceans, by assimilating observational data from a variety of sources, including satellite data, weather balloons,
and weather stations (Hersbach et al., 2020). The ERA5 surface parameters used in this study are precipitation and

DACRE ET AL.

2 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseJournal of Geophysical Research: Atmospheres

10.1029/2023JD039239

evaporation. They are extracted on a latitude-longitude grid with a resolution
of 0.25° Precipitation is the combined liquid and frozen water that descends
onto the Earth's surface, comprising both large-scale precipitation and convec-
tive precipitation. Large-scale precipitation is produced by  the cloud scheme
within the ECMWF Integrated Forecasting System (IFS), which models the
formation and dissipation of clouds and large-scale precipitation as a result
of alterations in temperature, pressure, and moisture at scales larger than the
grid  box.  Convective  precipitation  is  generated  by  the  convection  scheme
in the IFS, which represents convection at scales smaller than the grid box.
Evaporation is the cumulative amount of water that has vaporized from the
Earth's  surface.  Lavers  et  al.  (2022)  evaluated  ERA5  precipitation  against
5,637  stations  observations  over  2001–2020.  They  conclude  that  globally
there is a small wet bias in ERA5 precipitation, but that errors are smallest
in winter extratropical areas. Since our study focuses on winter extratropi-
cal cyclones, we use ERA5 precipitation as a proxy for observed precipita-
tion.  Specific  humidity,  meridional  and  zonal  components   of  the  wind  are
extracted on isobaric surfaces on a longitude-latitude grid with a resolution of
0.25°. To determine moisture flux on isobaric surfaces, a 6-hourly temporal
resolution was utilized.

2.2.  Cyclone Identification

Figure 1.  Tracks of 400 most intense extratropical cyclones in the ERA5 data
set between March and September 1979–2021 with maximum intensity in the
Southern Ocean surrounding Australia (90°–180°E, 20°–60°S, red box).

Based on the study by H. Dacre et al. (2012), we have tracked the location of
the  400  most  intense  cyclones  over  a  period  of  42  years  (1979–2021)  using
the tracking algorithm developed by Hodges (1995). The tracking process was
carried out during the extended austral winter (May-September), and hourly 850 hPa relative vorticity. Since relative
vorticity is a noisy field, before performing the tracking the vorticity field is spectrally truncated to T63. T63 corre-
sponds to a resolution on a Gaussian grid of approximately 1.88° at the equator. The tracked vorticity features were
filtered to exclude short-lived (<48 hr lifetime) or stationary features (traveling <1,000 km in their lifetime) unrelated
to extratropical cyclones. Cyclogenesis is defined as the first identified point in each cyclone track. The intensity of
the cyclones was measured using the maximum T63 vorticity. The 400 most intense cyclone tracks that attain their
maximum intensity in the oceans surrounding Australia (90°–180°E, 20°–60°S) are illustrated in Figure 1. Our focus
on this region is because extratropical cyclones in this area typically occur over the ocean, and thus they are closer to
idealized aquaplanet conditions, and because there is a lack of cyclone studies conducted in the Southern Hemisphere.

2.3.  Cyclone Compositing

To extract the fields used in this study, ERA5 data was obtained at 6-hourly intervals for each of the cyclone's
locations within a 20° radius of the cyclone center. Following Catto et al. (2010), cyclone-relative composites
were generated by averaging over all cyclones, after the fields were rotated to align with the direction of travel
of each cyclone. The direction of travel was estimated using the position 6 hr earlier and 6 hr later. This rotation
is crucial because cyclones have varying propagation directions. It improves the alignment of mesoscale features
such  as  warm  and  cold  fronts,  which  can  be  smoothed  out  completely  during  compositing  if  rotation  is  not
performed. Only the 400 most intense cyclones were included in the composite, as this method assumes that all
cyclones intensify and decay at similar rates. Limiting the number of cyclones produced a more homogeneous
group with regard to their evolution but may bias the mean fields to be representative of the most intense cyclones.

2.4.  Water Vapor Budget

To investigate the role of precipitation, evaporation, and MFC in regulating the moisture content of extratropical
cyclones, we computed the individual contributions of these terms to the water vapor budget for each gridbox column
within the cyclone system. The water vapor budget in a column of air was determined by the following equation:

DACRE ET AL.

(1)

3 of 11

𝑃𝑃+𝐸𝐸+𝑀𝑀𝑀𝑀𝑀𝑀=1𝑔𝑔∫𝑝𝑝2𝑝𝑝1𝜕𝜕𝜕𝜕𝜕𝜕𝜕𝜕𝑑𝑑𝑝𝑝𝑑 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
Journal of Geophysical Research: Atmospheres

10.1029/2023JD039239

(2)

P  is  the  surface  precipitation  flux  in  units  of  kg  m −2s −1  and  is  defined  to  be  negative  in  this  study,  E  is  the
surface evaporation flux in units of kg m −2s −1 (positive values indicate evaporation and negative values indicate
condensation in this study), g is the acceleration due to gravity in units of m s −2, q is the specific humidity in
units of kg kg −1, t is time in units of seconds, and
 is the horizontal wind vector in units of m s −1. The vertically
integrated terms are integrated from p1 = 1,000 hPa to p2 = 200 hPa. The third term on the left-hand side of
Equation 1 represents the vertically integrated MFC and is given in Equation 2. The term on the right-hand side
of Equation 1 represents the vertically integrated rate of change of water vapor in the column, positive values
indicate moistening and negative values indicate drying columns of air.

2.5.  Moisture Efficiencies and Depletion Timescales

In Section 4 we calculate the moisture efficiencies over a 6-hr period at each gridpoint in the domain surrounding
the cyclone center. The PE, evaporation efficiency (EE) and MFC efficiency (MFCE) at time t are the first 3
terms in Equation 1 accumulated over a 6-hr period, divided by the TCWV at the start of the 6-hr period (t − 6).

(3)

The PE is negative and represents the percentage of TCWV removed by precipitation over 6 hr. The EE is posi-
tive, and represents the percentage of TCWV replenished by evaporation over 6 hr. The MFC efficiency can be
positive or negative and represents the percentage of TCWV either replenished or removed over 6 hr respectively,
depending on whether MFC or moisture flux divergence occurs at each location. The sum of the efficiencies is
used to determine whether the columns are moistening or drying over the 6-hr period.

In Section 6 we calculate the timescale over which the moisture in a cyclone would completely ’dry out’ due to
the accumulated precipitation integrated over a circle with radius r from the cyclone center. We refer to this as
the precipitation depletion timescale, PDT. When calculating the PDT we assume that any cloud microphysical
processes in the precipitation process, due to the addition or removal of moisture by evaporation and MFC, do not
result in significant systematic changes to the climatological PDT. The PDT is calculated relative to the TCWV
in the cyclone system at the cyclogenesis time, t0, such that;

(4)

The moisture lost from the cyclone system via precipitation may be replenished due to evaporation as the cyclone
evolves. Moisture may also be replenished or depleted from the cyclone if the MFC is positive or negative respec-
tively. Thus the general depletion timescale, GDT, is given by;

(5)

3.  Composite Cyclone Structure

In this section, we depict the composite fields of cyclones during various stages of their evolution. In general,
the cyclone lifetime is split into a developing and decaying phase (although some cyclones can undergo multiple
deepening phases). The distribution of cyclone lifetimes for the 400 cyclones in the climatology is non-Gaussian
with  a  few  cyclones  having  very  long  lifetimes,  so  we  calculate  the  mode  of  the  distribution  to  represent  the

DACRE ET AL.

4 of 11

𝑀𝑀𝑀𝑀𝑀𝑀=−1𝑔𝑔∫𝑝𝑝2𝑝𝑝1∇⋅(𝑞𝑞𝑞𝑞𝑞)𝑑𝑑𝑝𝑝𝑑𝐴𝐴𝐴𝐴𝐴𝑃𝑃𝑃𝑃=𝑃𝑃𝑡𝑡𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑡𝑡−6,𝑃𝑃𝑃𝑃=𝑃𝑃𝑡𝑡𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑡𝑡−6,𝑀𝑀𝑀𝑀𝑇𝑇𝑃𝑃=𝑀𝑀𝑀𝑀𝑇𝑇𝑡𝑡𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑡𝑡−6.𝑃𝑃𝑃𝑃𝑃𝑃∑𝑡𝑡=𝑡𝑡0∫𝑟𝑟0∫3600𝑃𝑃𝑡𝑡𝑑𝑑𝑟𝑟𝑑𝑑𝑑𝑑∫𝑟𝑟0∫3600𝑃𝑃𝑇𝑇𝑇𝑇𝑇𝑇𝑡𝑡0𝑑𝑑𝑟𝑟𝑑𝑑𝑑𝑑=−1𝐺𝐺𝐺𝐺𝐺𝐺∑𝑡𝑡=𝑡𝑡0∫𝑟𝑟0∫3600(𝑃𝑃𝑡𝑡+𝐸𝐸𝑡𝑡+𝑀𝑀𝑀𝑀𝑀𝑀𝑡𝑡)𝑑𝑑𝑟𝑟𝑑𝑑𝑑𝑑∫𝑟𝑟0∫3600𝐺𝐺𝑀𝑀𝑇𝑇𝑇𝑇𝑡𝑡0𝑑𝑑𝑟𝑟𝑑𝑑𝑑𝑑=−1 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Journal of Geophysical Research: Atmospheres

10.1029/2023JD039239

Figure 2.  Evolution of cyclone centered composite fields overlaid with fronts (black). (a–c) Mean sea level pressure (hPa),
(d–f) 925 hPa Equivalent potential temperature (K), (g–i) Total column water vapor (kg m −2). Fields are shown at maximum
intensity (right column), 24 hr before maximum intensity (middle column) and 48 hr before maximum intensity (left column).
Images available from the Southern Hemisphere Storms Atlas, www.met.reading.ac.uk/∼storms.

average cyclone characteristics. The average cyclone lifetime is 102 hr and the average time for a cyclone to reach
maximum intensity after cyclogenesis is 42 hr. Since we are interested in studying the cyclone's precipitating
phase, we also calculate the time of maximum precipitation, which occurs on average 24 hr prior to maximum
intensity. To illustrate this stage of the cyclone evolution we analyze fields 48 and 24 hr prior to maximum inten-
sity, and at maximum intensity.

Figures 2a–2c illustrate the composite mean sea level pressure (mslp) evolution during the developing stage of
cyclone evolution. At 48 hr before the cyclones attain maximum intensity a trough extends toward the center of
the cyclone. There is a minimum mslp of 998 hPa at the center of the composite cyclone but the lowest pressure
within the 2,000 km radius domain is located to the south-east of the cyclone center. This is a possible parent
cyclone (H. F. Dacre & Pinto, 2020; Hoskins & Hodges, 2005) with a frontal wave cyclone developing along
the parent cyclone's trailing cold front. At 24 hr before maximum intensity, the composite cyclone has formed a
closed mslp contour. There is still a low-pressure region to the south-east of the cyclone center, but it is closer to
the cyclone of interest. Finally, at maximum intensity, the mslp at the cyclone's center has decreased by a further
15 hPa, to 970 hPa. This progression suggests that strong SH cyclones can emerge as secondary cyclones on the
trailing cold front of pre-existing primary cyclones located to the south-east of the secondary cyclone position.

Figures 2d–2f show the 925 hPa equivalent potential temperature, depicting a north-south temperature gradient
with warm air toward the equator and cooler air toward the south pole. The amplitude of the wave in the meridi-
onal temperature gradient increases as the cyclone develops. At maximum intensity the cyclonic motion associ-
ated with the cyclone has caused an overturning of the 295 K equivalent potential temperature contour suggesting
the formation of a warm seclusion as cold air wraps around to the north of the cyclone center. Overlaid on the

DACRE ET AL.

5 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseJournal of Geophysical Research: Atmospheres

10.1029/2023JD039239

925 hPa potential temperature and TCWV contours are the approximate positions of the composite cyclone cold
and  warm  fronts.  Figures  2g–2i  illustrate  the  composite  total  column  water  vapor  (TCWV)  distribution.  The
highest values of TCWV are found in the warm sector of the cyclone with a filament of high TCWV ahead of
the cyclone cold front, which is most pronounced 24 hr before maximum intensity. At maximum intensity, the
TCWV within the cyclone warm sector starts to decrease.

4.  Moisture Efficiencies

To understand the factors that influence the evolution of TCWV, we examine the water vapor budget centered
on the cyclone. We measure the change in moisture content in each column of air around the cyclone center over
a 6-hr period and express it as a percentage of the moisture content at the start of the 6-hr period. The moisture
efficiencies are described in Section 2.5 (Equation 3).

Figures 3a–3c show that during the early stage of the cyclone's lifecycle, the PE is greater than −12%/6 hr close to
the cyclone center. The PE increases as the cyclone intensifies, reaching a maximum of −60%/6 hr along the bent
back warm front surrounding the cyclone center at maximum intensity (Figure 3c). This is consistent with the
precipitation efficiencies calculated by Guo et al. (2015). Precipitation efficiencies of −12%/6 hr to −24%/6 hr
also extend 1,000 km away from the cyclone center in a comma shaped pattern aligned with the cold front. The
EE is smaller than the largest PE, but the area of moderate evaporation efficiencies (12%–24%/6 hr) is much more
extensive and is located behind the cold front in the cyclone's cold sector (Figures 3d–3f).

The evolution of MFC efficiency is shown in Figures 3g–3i. During the early stage of the cyclone's evolution
(48 hr before maximum intensity) columns behind the cold front experience up to 10% drying every 6 hr, while
columns ahead of the cold front become up to 10% moister every 6 hr (Figure 3g). Decomposition of the MFC
into terms related to advection and divergence of the flow (not shown) reveals that this dipole structure occurs
because during the early stage of the cyclone's evolution the cold front moves faster than the cyclone, causing
relative advection of the cold front moisture gradient. However, close to the cyclone center, positive MFC effi-
ciency is observed throughout the cyclone's development, reaching a maximum of 55%/6 hr at maximum inten-
sity (Figure 3i). Close to the cyclone center (within 500 km) on average 14% of the moisture converges into the
cyclone every 6 hr due to MFC, offsetting the −25%/6 hr moisture lost via precipitation. The MFC decomposition
(not shown) reveals that this MFC occurs because during the developing stage of cyclone evolution, the cyclone
velocity is faster than the environmental wind velocity at low levels, leading to mass convergence along the cold
front airmass boundary, particularly where the cold front is perpendicular to the direction of cyclone velocity
(which is left to right in the rotated composite cyclones). Therefore, MFC at the tip of the filament of high TCWV
in the warm sector extends the filament in the direction of cyclone propagation, which is typically toward the
poles. Therefore, MFC occurring close to the cyclone center (at the head of the atmospheric river), extends the
filament of high TCWV in the direction of cyclone propagation.

The sum of positive MFC efficiency and EE at the at the tip of the filament of high TCWV offsets the large
negative PE resulting in decreases in TCWV of approximately −4% over 6 hr (Figures 3k and 3l). Along the
remainder of the atmospheric river the MFC efficiency is negative since moisture diverges out of these columns,
thus enhancing the drying caused by precipitation as the cyclone reaches maximum intensity.

5.  Cyclone Airflows

In  this  section,  we  examine  the  vertically  integrated  water  vapor  transport  (IVT)  to  determine  the  low-level
cyclone airflows responsible for the flux of moisture. Where IVT is calculated using Equation 6,

IVT is vertically integrated from p1 = 1,000 hPa to p2 = 200 hPa. q is the specific humidity in units of kg kg −1,
g  is  the  acceleration  due  to  gravity  in  units  of  m  s −2  and
  is  the  horizontal  wind  vector  in  units  of  m  s −1.
Figures 4a–4c illustrate the Earth-relative IVT. The warm sector of the cyclone, where moisture is highest and
the cold front low-level jet is located, has the largest Earth-relative IVT. The cyan color in Figures 4a–4d corre-
sponds to IVT >250 kg m −1 s −1, which is typically used to identify atmospheric rivers. Therefore, even in this

(6)

DACRE ET AL.

6 of 11

⃗𝐼𝐼𝐼𝐼𝐼𝐼=−1𝑔𝑔∫𝑝𝑝2𝑝𝑝1𝑞𝑞⃗𝑞𝑞𝑞𝑞𝑝𝑝𝑞𝐴𝐴𝐴𝐴𝐴 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
Journal of Geophysical Research: Atmospheres

10.1029/2023JD039239

Figure 3.  Evolution of cyclone centered composite terms in the moisture budget expressed as a percentage of the initial
moisture content for a 6-hr period (%/6 hr). (a–c) Precipitation efficiency, (d–f) evaporation efficiency, (g)–(i) Moisture flux
convergence efficiency and total moisture efficiency.

composite cyclone, an atmospheric river extends along the cold front. The IVT vectors show that moisture in the
atmospheric river is transported polewards in a south-eastwards direction.

To  assess  the  origin  of  moisture  converging  into  the  center  of  the  cyclone  it  is  necessary  to  compute  the
cyclone-relative  winds  by  subtracting  the  cyclone's  propagation  velocity  from  the  Earth-relative  winds.  The
composite cyclone-relative IVT during the developing stage of the cyclone evolution is shown in Figures 4d–4f.
At the head of the atmospheric river (white/gray boxes in Figure 4), the cyclone-relative vertically integrated
moisture flux has a component toward the cyclone center from the direction in which the cyclone is moving.

DACRE ET AL.

7 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseJournal of Geophysical Research: Atmospheres

10.1029/2023JD039239

Figure 4.  Evolution of cyclone centered composite vertically integrated moisture transport (kg m −1 s −1) using (a–c)
Earth-relative winds and (d–f) cyclone relative winds. IVT flux (vectors) and IVT magnitude (filled contours). White/gray
boxes indicate the head and tail of the atmospheric river. Gray circles indicate radial distances 500 and 1,000 km from the
cyclone center. Panels (j–l) are schematics showing the cyclone-relative low-level moist airflows at different stages of the
composite cyclone evolution. Cold conveyor belt (CCB), warm conveyor belt (WCB) and feeder airstream (FA).

Further from the cyclone center along the tail of the atmospheric river, the direction of the cyclone-relative IVT
flux vectors is opposite to the Earth-relative IVT. This reversal occurs because the low-level winds are typically
slower than the moving cyclone. Thus the atmospheric river consists of a head, where the moisture flux has a
component toward the cyclone center and a tail where the moisture flux has a component away from the cyclone
center. The FA is the low-level cyclone airflow responsible for this partition (Figures 4j and 4k).

By maximum intensity the strength of the atmospheric river has reduced since the TCWV in the warm sector
reduces  significantly  as  the  cyclones  travel  toward  the  South  pole  (Figure 4c).  The  velocity  of  the  cyclone  is
now similar to the atmospheric flow in which it is embedded so the cyclone-relative IVT in the warm sector is
small (Figure 4f). The largest cyclone-relative IVT is found wrapping around the cyclone center, co-located with
the bent-back warm front. The low-level cyclone airflow resulting in this moisture flux is known as the cold
conveyor belt (CCB) (Carlson, 1980). The CCB is located on the poleward side of the cyclone center. This air is
cold and dense and thus the CCB airflow has a low potential temperature and is found in the lower-troposphere
(not shown). The CCB wraps cyclonically around the cyclone center and leads to the emergence of the rearward
traveling  (with  respect  to  the  cyclone  motion)  cloud  head.  The  mid-level  cyclone  airflow  contributing  to  the
largest cyclone-relative IVT is known as the WCB (Browning, 1971). The WCB is a warm and moist airflow that
originates on the equatorward side of the cyclone center. This airflow ascends along a sloping isentropic surface
over the warm front to the mid and upper-levels of the atmosphere where it cools and releases moisture forming

DACRE ET AL.

8 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseJournal of Geophysical Research: Atmospheres

10.1029/2023JD039239

Figure 5.  Composite cumulative moisture efficiency terms for 400 SH extratropical cyclones relative to the TCWV at the cyclogenesis location. The individual
terms are integrated over an area surrounding the cyclone center with radius (a) 500 km and (b) 1,000 km. Cumulative precipitation efficiency (blue), evaporation
efficiency (orange), moisture flux convergence efficiency (green) and total budget (red). The total budget is equal to the sum of the individual moisture efficiencies. The
precipitation and general depletion timescales correspond to the times at which the blue and red bars cross the dashed line.

clouds and precipitation. One branch of the WCB turns cyclonically at mid-levels and contributes to the upper-
part of the cyclones cloud head (not shown) (Figure 4l).

6.  Depletion and Replenishment

In this section, we determine how long it would take for all of the column moisture at the cyclogenesis time to
be lost due to precipitation. The cyclogenesis time corresponds to the first point of each individual cyclone track
where the 850 hPa relative vorticity exceeds 1 × 10 −5s −1. Figure 5a shows the mean cumulative PE integrated
within 500 km of the cyclone center (blue bars) for increasing accumulation times. The time at which this equals
−100% is equivalent to the PDT (Equation 4). Close to the cyclone center the average PDT is between 24 and
36 hr indicating that if there were no replenishment of moisture the center of the cyclone would completely dry
out on a timescale of approximately 30 hr from the genesis time. The cumulative EE integrated within 500 km of
the cyclone center (orange bar) is initially relatively small, but increases fairly linearly with time. Thus the inte-
grated evaporation close to the cyclone center replenishes on average 33% of the moisture lost due to precipitation
over the first 36 hr and continues to replenish the moisture throughout the cyclone evolution. The cumulative
MFC efficiency close to the cyclone center (green bars) is positive close to the cyclone center and it replenishes
on average 24% of moisture lost due to precipitation over the first 36 hr. The general depletion timescale, GDT,
(sum of the blue, orange and green bars) is shown in the red bar. The time at which this equals −100% is equiva-
lent to the general depletion timescale (Equation 5). The result of replenishment of moisture via evaporation and
MFC as the cyclone travels extends the time taken for the cyclone center to dry out from 30 hr to between 60 and
72 hr. Thus, on average, local evaporation and MFC more than doubles the precipitating phase near the cyclone
center. This ensures that there is sufficient moisture for precipitation by the time cyclones have traveled from their
genesis location to their location at maximum intensity.

Figure 5b shows the average cumulative PE integrated within 1,000 km of the cyclone center. The cumulative
PE (blue bars) grows at a slower rate than when integrated over 500 km since high precipitation is concentrated
close to the cyclone center. As a result the PDT is longer for this larger area between 48 and 60 hr. The cumulative
EE integrated within 1,000 km of the cyclone center is positive and increases throughout the cyclone lifecycle,
replenishing  approximately  50%  of  the  moisture  over  the  first  36  hr  after  the  genesis  time.  Interestingly,  the
cumulative MFC efficiency term is negative when integrated over this 1,000 km area. This implies that there is
divergence of moisture from the cyclone depleting the moisture available for precipitation. Over the first 36 hr
4% of moisture diverges from the 1,000 km surrounding the cyclone. This occurs largely because the cyclone is
traveling faster than the flow in which it is embedded. This divergence of moisture is consistent with Figures 4j

DACRE ET AL.

9 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseJournal of Geophysical Research: Atmospheres

10.1029/2023JD039239

and 4k which show the low-level cyclone-relative airflows during the developing stages of the cyclone evolution.
The cyclonically turning branch of the feeder-airstream acts to export moisture from the cyclone center, acceler-
ating the general depletion timescale within the tail of the atmospheric river. The system relative IVT (Figures 4d
and 4e) suggest that evaporation behind the cold front is not available to the cyclone to extend its precipitating
phase. Therefore, it should be noted that including the contribution from evaporation in this region will likely
result in a slight overestimation of the GDT.

7.  Conclusions

In  this  study  we  evaluate  the  composite  structure  of  a  climatology  of  400  Southern  Ocean  extratropical
cyclones  and  estimate  their  precipitation  efficiencies.  We  find  that,  on  average,  the  cyclones'  maximum
precipitation  occurs  24  hr  prior  to  maximum  dynamical  intensity.  At  this  time  there  is  a  filament  of  high
TCWV  aligned  with  the  composite  cyclone  cold  front  and  a  well-defined  maximum  in  IVT  within  warm
sector. The PE (ratio of 6-hourly precipitation accumulation to TCWV at the start of the 6-hr window) is larg-
est close to the cyclone center and increases as the cyclone intensifies reaching a maximum of −60%/6 hr at
maximum intensity. We determine how long it would take to deplete all of a cyclone's initial moisture supply.
If there were no replenishment of moisture along the cyclone's track then we find that within 500 km of the
cyclone center all of the initial moisture content would be lost due to precipitation within 24–36 hr (averaged
over 400 SH cyclones). However, close to the cyclone center both evaporation and MFC into the center of the
cyclone replenishes the moisture lost via precipitation. This extends the precipitating phase of the cyclone
from  24-36  hr  to  60–72  hr  after  cyclogenesis.  During  the  developing  stage  of  cyclone  evolution,  moisture
flux into the center of the cyclone originates ahead of the cyclone and is swept up by the cyclone as it travels
through the moist environment. At the cold front some of this moisture is transported toward the center of
the cyclone by the anticyclonic branch of the FA. During the mature stage of cyclone evolution the cyclone
propagation speed reduces and moisture flux toward the cyclone center occurs to the south of the cyclone in
the low-level CCB airstream. Further from the cyclone center (>500 km) moisture diverges out of the cyclone
enhancing the drying caused by precipitation. In the tail of the atmospheric river moisture is transported away
from the center of the cyclone by the cyclonic branch of the FA and is left behind to form the atmospheric
river footprint.

Data Availability Statement

The composite fields associated with over 400 Southern Ocean extratropical cyclones are freely available via the
Extratropical Cyclone Atlas (H. Dacre et al., 2011).

References
Bengtsson,  L.,  Hodges,  K.  I.,  &  Keenlyside,  N.  (2009).  Will  extratropical  storms  intensify  in  a  warmer  climate?  Journal  of  Climate,  22(9),

2276–2301. https://doi.org/10.1175/2008jcli2678.1

Booth,  J.  F.,  Naud,  C.  M.,  &  Jeyaratnam,  J.  (2018).  Extratropical  cyclone  precipitation  life  cycles:  A  satellite-based  analysis.  Geophysical

Research Letters, 45(16), 8647–8654. https://doi.org/10.1029/2018gl078977

Browning,  K.  (1971).  Radar  measurements  of  air  motion  near  fronts.  Weather,  26(8),  320–340.  https://doi.org/10.1002/j.1477-8696.1971.

tb07416.x

Browning, K., & Harrold, T. (1970). Air motion and precipitation growth at a cold front. Quarterly Journal of the Royal Meteorological Society,

96(409), 369–389. https://doi.org/10.1002/qj.49709640903

Bui, H., & Spengler, T. (2021). On the influence of sea surface temperature distributions on the development of extratropical cyclones. Journal

of the Atmospheric Sciences, 78(4), 1173–1188. https://doi.org/10.1175/jas-d-20-0137.1

Carlson, T. N. (1980). Airflow through midlatitude cyclones and the comma cloud pattern. Monthly Weather Review, 108(10), 1498–1509. https://

doi.org/10.1175/1520-0493(1980)108<1498:atmcat>2.0.co;2

Catto, J. L., Shaffrey, L. C., & Hodges, K. I. (2010). Can climate models capture the structure of extratropical cyclones? Journal of Climate, 23(7),

1621–1635. https://doi.org/10.1175/2009jcli3318.1

Cuckow,  S.,  Dacre,  H.  F.,  &  Martínez-Alvarado,  O.  (2022).  Moisture  transport  contributing  to  precipitation  at  the  centre  of  storm  Bronagh.

Weather, 77(6), 196–201. https://doi.org/10.1002/wea.4212

Dacre, H., Hawcroft, M., Stringer, M., & Hodges, K. (2011). Extratropical cyclone atlas [Dataset]. https://www.met.rdg.ac.uk/∼storms
Dacre, H., Hawcroft, M., Stringer, M., & Hodges, K. (2012). An extratropical cyclone atlas: A tool for illustrating cyclone structure and evolution

characteristics. Bulletin of the American Meteorological Society, 93(10), 1497–1502. https://doi.org/10.1175/bams-d-11-00164.1

Dacre, H. F., Clark, P. A., Martinez-Alvarado, O., Stringer, M. A., & Lavers, D. A. (2015). How do atmospheric rivers form? Bulletin of the

American Meteorological Society, 96(8), 1243–1255. https://doi.org/10.1175/bams-d-14-00031.1

Dacre, H. F., Martínez-Alvarado, O., & Mbengue, C. O. (2019). Linking atmospheric rivers and warm conveyor belt airflows. Journal of Hydro-

meteorology, 20(6), 1183–1196. https://doi.org/10.1175/jhm-d-18-0175.1

Acknowledgments
H. F. Dacre, O. Martinez-Alvarado, and
K. I. Hodges were supported by a Science
and Technology Facilities Council
(STFC) (Grant ST/X000087/1).

DACRE ET AL.

10 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseJournal of Geophysical Research: Atmospheres

10.1029/2023JD039239

Dacre, H. F., & Pinto, J. G. (2020). Serial clustering of extratropical cyclones: A review of where, when and why it occurs. npj Climate and

Atmospheric Science, 3(1), 48. https://doi.org/10.1038/s41612-020-00152-9

Demirdjian, R., Doyle, J. D., Finocchio, P. M., & Reynolds, C. A. (2022). On the influence of surface latent heat fluxes on idealized extratropical

cyclones. Journal of the Atmospheric Sciences, 79(9), 2229–2242. https://doi.org/10.1175/jas-d-22-0035.1

Eiras-Barca,  J.,  Dominguez,  F.,  Hu,  H.,  Garaboa-Paz,  D.,  &  Miguez-Macho,  G.  (2017).  Evaluation  of  the  moisture  sources  in  two  extreme
landfalling atmospheric river events using an Eulerian WRF tracers tool. Earth System Dynamics, 8(4), 1247–1261. https://doi.org/10.5194/
esd-8-1247-2017

Ferrier, B. S., Simpson, J., & Tao, W.-K. (1996). Factors responsible for precipitation efficiencies in midlatitude and tropical squall simulations.

Monthly Weather Review, 124(10), 2100–2125. https://doi.org/10.1175/1520-0493(1996)124<2100:frfpei>2.0.co;2

Guo, C., Xiao, H., Yang, H., & Tang, Q. (2015). Observation and modeling analyses of the macro-and microphysical characteristics of a heavy

rain storm in Beijing. Atmospheric Research, 156, 125–141. https://doi.org/10.1016/j.atmosres.2015.01.007

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz-Sabater, J., et al. (2020). The ERA5 global reanalysis. Quarterly Journal

of the Royal Meteorological Society, 146(730), 1999–2049. https://doi.org/10.1002/qj.3803

Hobbs, P. V., Matejka, T. J., Herzegh, P. H., Locatelli, J. D., & Houze, R. A. (1980). The mesoscale and microscale structure and organization of
clouds and precipitation in midlatitude cyclones. I: A case study of a cold front. Journal of the Atmospheric Sciences, 37(3), 568–596. https://
doi.org/10.1175/1520-0469(1980)037<0568:tmamsa>2.0.co;2

Hodges,  K.

(1995).  Feature

tracking  on

the  unit

sphere.  Monthly  Weather  Review,  123(12),  3458–3465.  https://doi.

org/10.1175/1520-0493(1995)123<3458:ftotus>2.0.co;2

Hoskins, B. J., & Hodges, K. I. (2005). A new perspective on Southern Hemisphere storm tracks. Journal of Climate, 18(20), 4108–4129. https://

doi.org/10.1175/jcli3570.1

Hu, H., & Dominguez, F. (2019). Understanding the role of tropical moisture in atmospheric rivers. Journal of Geophysical Research: Atmos-

pheres, 124(24), 13826–13842. https://doi.org/10.1029/2019jd030867

Lavers, D. A., Simmons, A., Vamborg, F., & Rodwell, M. J. (2022). An evaluation of ERA5 precipitation for climate monitoring. Quarterly

Journal of the Royal Meteorological Society, 148(748), 3152–3165. https://doi.org/10.1002/qj.4351

Li, X., Sui, C.-H., & Lau, K.-M. (2002). Precipitation efficiency in the tropical deep convective regime: A 2-D cloud resolving modeling study.

Journal of the Meteorological Society of Japan. Ser. II, 80(2), 205–212. https://doi.org/10.2151/jmsj.80.205
Lutz, J. T. (1977). Precipitation efficiency under varying atmospheric conditions. Geographical Bulletin, 14, 16.
Newell, R. E., Newell, N. E., Zhu, Y., & Scott, C. (1992). Tropospheric rivers? A pilot study. Geophysical Research Letters, 19(24), 2401–2404.

https://doi.org/10.1029/92gl02916

Papritz, L., Aemisegger, F., & Wernli, H. (2021). Sources and transport pathways of precipitating waters in cold-season deep North Atlantic

cyclones. Journal of the Atmospheric Sciences, 78(10), 3349–3368. https://doi.org/10.1175/jas-d-21-0105.1

Pfahl, S., & Sprenger, M. (2016). On the relationship between extratropical cyclone precipitation and intensity. Geophysical Research Letters,

43(4), 1752–1758. https://doi.org/10.1002/2016gl068018

Rea, D., Rauber, R. M., Hu, H., Tessendorf, S. A., Nesbitt, S. W., Jewett, B. F., & Zaremba, T. J. (2023). The contribution of subtropical moisture
within an atmospheric river on moisture flux, cloud structure, and precipitation over the Salmon River Mountains of Idaho using moisture
tracers. Journal of Geophysical Research: Atmospheres, 128(6), e2022JD037727. https://doi.org/10.1029/2022jd037727

Sinclair, V., & Dacre, H. (2019). Which extratropical cyclones contribute most to the transport of moisture in the Southern Hemisphere? Journal

of Geophysical Research: Atmospheres, 124(5), 2525–2545. https://doi.org/10.1029/2018jd028766

Sodemann, H., & Stohl, A. (2013). Moisture origin and meridional transport in atmospheric rivers and their association with multiple cyclones.

Monthly Weather Review, 141(8), 2850–2868. https://doi.org/10.1175/mwr-d-12-00256.1

Stewart, R. E. (1996). Extratropical cyclones: Their mesoscale structure, precipitation and role in the transport of water. In Radiation and water

in the climate system: Remote measurements (pp. 129–148). Springer.

Tuller,  S.  E.  (1971).  The  world  distribution  of  annual  precipitation  efficiency.  Journal  of  Geography,  70(4),  219–223.  https://doi.

org/10.1080/00221347108981623

Xu,  G.,  Wang,  L.,  Chang,  P.,  Ma,  X.,  &  Wang,  S.  (2022).  Improving  the  understanding  of  atmospheric  river  water  vapor  transport  using  a
three-dimensional  straightened  composite  analysis.  Journal  of  Geophysical  Research:  Atmospheres,  127(11),  e2021JD036159.  https://doi.
org/10.1029/2021jd036159

DACRE ET AL.

11 of 11

 21698996, 2023, 24, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JD039239 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License