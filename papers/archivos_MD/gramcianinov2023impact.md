Climate Dynamics (2023) 60:1447–1466
https://doi.org/10.1007/s00382-022-06390-2

Impact of extratropical cyclone intensity and speed on the extreme
wave trends in the Atlantic Ocean

Carolina B. Gramcianinov1,5
Pedro L. da Silva Dias1

 · Ricardo de Camargo1 · Ricardo M. Campos2,3 · C. Guedes Soares4 ·

Received: 29 September 2021 / Accepted: 14 June 2022 / Published online: 7 July 2022
© The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature 2022

Abstract
This work analyses the extratropical cyclone-related extreme waves in the ocean surface and their trends in the North and
South Atlantic Oceans. Atmospheric and ocean wave products are obtained from ERA5, from 1979 to 2020 with 1-hourly
outputs, covering 42 years with the present climate changes evaluated by the difference between the two 21-years-time
slices. The cyclones are tracked through the relative vorticity at 850 hPa and then associated with extreme wave events
using an automated scheme that searches for an extreme wave region 1500 km from the centre of the cyclone, following
criteria that exclude possible swell dominated events. The hot spot regions of cyclone-related waves occurrence found by
the method agree with previous studies and relate to the cyclogenesis region, and storm track orientation. Most cyclones
associated with extreme wave events are generated in the western boundary of the domains. The east-poleward side of the
ocean basins presents the highest density of occurrences related to the higher density of cyclone track and the dominance
of more mature stage cyclones while in the west side prevail systems on developing stages, with notable propagating fronts
and consequently, lower wind persistence. The storm track variations alone cannot explain the observed changes in the wave
occurrence during the period due to the lack of statistical confidence. However, the wave occurrence responds to changes in
the cyclone intensity, modulated by cyclone displacement speed. Regions with an increase of extreme waves are related to
the effect of more intense cyclones or cyclones with slower propagation, being the last associated with a longer interaction
of winds with the ocean surface.

1  Introduction

In the last decades, the demand to access changes on extreme
events has been increasing. From an ocean perspective,
the  study  of  natural  hazards  associated  with  anomalous

wind-generated ocean waves (hereafter only waves) is of
paramount importance to offshore and coastal activities,
with high socioeconomic impacts. Management and mainte-
nance of ships, offshore and coastal structures depend upon
knowing the current extreme wave climate and its trends

 *  Carolina B. Gramcianinov

carolina.gramcianinov@alumni.usp.br

Ricardo de Camargo
ricamarg@usp.br

Ricardo M. Campos
ricardo.campos@noaa.gov

C. Guedes Soares
c.guedes.soares@centec.tecnico.ulisboa.pt

Pedro L. da Silva Dias
pedro.dias@iag.usp.br

1  Departamento de Ciências Atmosféricas, Instituto
de Astronomia, Geofísica e Ciências Atmosféricas,
Universidade de São Paulo, Rua do Matão 1226, Cidade
Universitária, São Paulo, SP, Brazil

2  Cooperative Institute for Marine and Atmospheric Studies,
University of Miami, 4600 Rickenbacker Causeway, Miami,
FL 33149, USA

3  Atlantic Oceanographic and Meteorological Laboratory,
NOAA, 4301 Rickenbacker Causeway, Key Biscayne,
FL 33149, USA

4  Centre for Marine Technology and Ocean Engineering

(CENTEC), Instituto Superior Técnico, Universidade de
Lisboa, Rovisco Pais, 1049-001 Lisbon, Portugal

5  Present Address: Institute for Coastal Systems

Analysis and Modeling, Helmholtz-Zentrum Hereon,
Max-Planck-Straße 1, 21502 Geesthacht, Germany

Vol.:(0123456789)1 3

1448

C. B. Gramcianinov et al.

(Bitner-Gregersen et al. 2018; Bernardino et al. 2021). In
mid to high latitudes, the main drivers of wave climate are
the extratropical cyclones, which are known by their strong
winds and large fetch (e.g., da Rocha et al. 2004; Ponce de
Léon and Guedes Soares 2014, 2015; Campos et al. 2018;
Ponce de Léon and Bettencourt 2021). In this context, this
present study explores the relation between the extreme
wave climate and extratropical storm tracks in the Atlantic
Ocean, providing a new perspective of the changes in the
extreme wave events forced by these atmospheric systems.

One  of  the  challenges  regarding  wave  climate  trends
studies is that wave distribution cannot be directly related
to wind changes. The global wave climate is characterized
by large waves in high latitudes, presenting a decrease in
significant wave height (SHW) towards the equator (Young
1999). This distribution places the westerly wind belt, which
generally indicates the preferred pathway of extratropical
cyclones displacement (so-called storm track), as a wave
generator in which waves are fully coupled with the over-
layer winds (Chen et al. 2002) in a state known as wind-sea.
After leaving their generation region, these waves can travel
far distances and are able to cross ocean basins with low
energy attenuation (Alves 2006; Ardhuin et al. 2009). Such
propagating waves are called swell, which combined with
the wind-sea results in combined sea states (Guedes Soares
1984; Vettor and Guedes Soares 2020). Thus, changes in
wave climate are not a straightforward response of the local
winds (e.g., Stopa and Cheung 2014). One solution to evalu-
ate the wind-wave climate relationship would be separating
local from remote forcing waves; however, it is not a trivial
effort, especially in regions with high influence of swell and
wind-sea (Rapizo et al. 2015).

Another problem is the varying range of influence that
the cyclone structure (i.e., front positions and movement),
displacement speed, and intensity play on the extreme wave
occurrence. Even though climate state is a result of the
average of weather patterns, changes in the extreme climate
must be analysed with more caution regarding special con-
ditions that lead to extreme events. For instance, within the
extratropical wind structure, different patterns can generate
extreme waves depending on the dominant airflow. Bell et al.
(2017) found the influence of both cold and warm conveyor
belts in the extreme waves in the Northern Sea while Kita
et al. (2018) reported extreme waves in distinct portions of
the cyclones, such as along the warm front. These studies
showed that beyond the climatological pattern, extreme wave
studies also need to focus on the characteristics of the gener-
ating systems (i.e., the cyclone itself, as well as the sectors
with stronger surface winds).

There are several studies about trends and changes of
storm tracks in the current climate century (Simmonds
and Keay 2000; Fyfe 2003; Wang et al. 2006) and future
scenarios (e.g., Ulbrich et al. 2009; Catto et al. 2019) but

without a direct relation with waves. Globally, the storm
track is shifting poleward, resulting in an overall decrease
of cyclones at mid-latitudes (e.g., Fyfe 2003; Geng and
Sugi 2003). However, the change signal varies locally,
and some regions may present an increase of cyclogen-
esis, such as the southwest South Atlantic coast, between
35° S and 40° S (Reboita et al. 2018, 2020). Regarding
cyclone intensity, some studies showed the increase in the
occurrence of strong cyclones, considering different inten-
sity measurements for both the current climate (Pezza and
Ambrizzi 2003; Reboita et al. 2015) and future scenarios
(Geng and Sugi 2003; Lambert and Fyfe 2006; Bengts -
son et al. 2009). Moreover, Reboita et al. (2021) found an
increase of 13% in the occurrence of bomb cyclones in the
South Atlantic Ocean, with the worst projected scenario
(RCP8.5) presenting deeper, faster, and shorter systems.
An extratropical cyclone is called an explosive or bomb
when it experiences fast deepening over a relatively short
time, usually greater than 24 hPa in 24 h (normalized at
60° N, Sanders and Gyakum 1980). A significant positive
trend of bomb cyclones in the Southern Hemisphere (SH)
was also reported by Lim and Simmonds (2002) analysing
the NCEP2 product from 1979 to 1999.

These findings allow a glance at what may happen with
wave fields, but the extreme wave climate may not be exclu-
sively related to cyclone intensity or storm track location.
First, because of the remote partition of the wave climate,
as explained above, and secondly, because some cyclones
simply  do  not  generate  extreme  waves.  Gramcianinov
et al. (2021b) showed that around 60% of the extratropi-
cal cyclones in ERA5 are associated with SWH higher than
5 m in the Atlantic Ocean. Other factors, such as cyclone
displacement speed and fetch orientation, play a big role in
extreme wave generation and need to be taken into account
in trends and changes studies (Gramcianinov et al. 2021a).

Some recent studies faced difficulties to explain wave
trends  just  by  using  winds  or  storm  track  tendencies.
According to Young and Ribal (2019), who evaluated the
global trends of wind and waves through three satellite data-
sets between 1985 and 2018, the wind speed distribution is
broadening, with an increase in the mean, mode and percen-
tiles, but this behaviour is not followed by the wave height
distribution. The authors found a tendency of higher occur-
rences of small waves, resulting in a distribution skewed to
the left and the increase in 90th percentile waves is confined
to the Southern Ocean and North Atlantic Ocean. Moreo-
ver, Takbash and Young (2020) found a positive tendency
in wave height extremes in the SH, presenting an increase
in the centennial SWH  (SWH100) of up to 3 cm/year using
ERA5. The Northern Hemispheric trend was negative, but
generally not statistically significant. In general most of the
studies have shown an increase in wave height extremes
in the SH in the past 41 years and that this is projected to

1 3
1449

continue in the future (e.g., Dobrynin et al. 2012; Lemos
et al. 2019).

ERA5 and a comparison with ERA-Interim can be found in
Hersbach et al. (2020).

The present work applies a cyclone feature-based analysis
(Lagrangian) to relate this extratropical system to extreme
wave events in the Atlantic Ocean. Each cyclone associated
with an extreme event is selected to build a set of statisti-
cal analyses regarding the cyclone-wave characteristics. The
main goal is to investigate the trends in the cyclone-related
waves, building a climatology of these extreme events for
the last 42 years. This article is guided by three main ques-
tions: (1) What is the distribution of extratropical cyclones
that most affect the extreme wave climate in the Atlantic
Ocean?; (2) Which are the main characteristics of these
cyclone-related waves?; and (3) Are there some significant
trends in the storm track and wave events in the last decades?
The  document  presents  a  description  of  datasets  and
methods used in Sect. 2, including the key procedures of
extreme wave definition and its association with cyclones.
Section 3 shows the results, which are discussed in Sect. 4.
Finally, the conclusion and recommendations are made in
Sect. 5.

2   Data and methods

2.1   ERA5

ERA5 is the fifth generation of reanalysis from the European
Centre  for  Medium-Range  Weather  Forecast  (ECMWF;
Hersbach et al. 2020), produced with the ECMWF’s Inte-
grated  Forecast  System  (IFS),  version  CY41R2,  using
4D-Var data assimilation. The atmospheric and wave vari-
ables used in this work are on 0.28° and 0.36° horizontal
grids, respectively. The data were used with 1-hourly outputs
from 1979 to 2020 and obtained through the Copernicus
Climate Change Service (C3S) (2017).

ERA5 presents several improvements regarding its pre-
decessor, the ERAInterim, including development in model
physics, core dynamics and data assimilation. Using ASCAT
observation as a reference, Belmonte Rivas and Stoffelen
(2019)  showed  that  ERA5  surface  winds  present  a  20%
improvement relative to ERA-Interim. Gramcianinov et al.
(2020a) compared the Atlantic Ocean’s storm track charac-
teristics for ERA5 and CFSR/CFSv2 from 1979 to 2019.
These authors found that despite both datasets presenting
cyclones’ climatology in agreement with past studies, the
1-hourly ERA5 produces more continuous track and fewer
tracking issues in continental and coastal regions. Consider-
ing the wave parameters, Takbash and Young (2020) ana-
lysed the magnitude and spatial distribution of mean and
extreme wave parameters and found that ERA5 presents a
good agreement with estimations from altimeter and buoy
data. Further information about the main characteristics of

2.2   Cyclones dataset

The cyclone tracks are obtained from the “Atlantic extrat-
ropical cyclone tracks database” (AETC) available at Gram-
cianinov et al. (2020b). The AETC uses the TRACK pro-
gram (Hodges 1994, 1995, 1999) to identify and track the
cyclones, following the method described in Hoskins and
Hodges (2002, 2005). A detailed explanation of the method,
tracking setup, and evaluation can be found in Gramciani-
nov et al. (2020a), although some relevant details are given
in this section. The AETC tracks produced using 1-hourly
ERA5 fields are used in this study. CFSR and ERA5 present
similar storm track spatial patterns and characteristics, but
the use of hourly fields may produce broken tracks to CFSR.
The cyclonic features are identified using the relative vor-
ticity at 850 hPa, which is recommended for the detection
of cyclones in middle latitudes (Sinclair 1994). Mid-latitude
strong surface pressure gradient usually masks cyclones,
therefore, hindering their detection when using mean sea
level pressure (MSLP) fields for the tracking. The target sys-
tems are mainly extratropical cyclones, retained by a spectral
filter applied during the pre-processing steps. Some sub-
tropical systems can be retained as well, depending on their
size. However, in this work, no distinction is made between
these two types of systems as the interest is in any cyclone
that can generate extreme waves in the extratropical region.
AETC includes cyclones that last at least 24 h, travel further
than 1000 km, and pass within the extratropical latitudes of
the South Atlantic (85° S–25° S, 75° W–20° E) and North
Atlantic (85° N–25° N, 65° W–0° E) at any moment of their
lifecycle.

2.3   Extreme wave definition

The definition of an extreme relies on a threshold that can be
established either by fixed values or percentiles. In this work,
extreme percentiles are used to select wave events by apply-
ing a spatial approach adapted from Gramcianinov et al.
(2020c). The 90th, 95th, and 99th percentiles are obtained
through the distribution of the maximum SWH of each event
in the time series for each grid point. The definition of a
time window is essential to guarantee the independence of
each SWH peak. To simplify the procedure to use for a large
domain a fixed time window is adopted. Several authors used
48 h (e.g., Caires and Sterl 2005; Meucci et al. 2020), but to
short time windows tend to bias the percentiles in subtropi-
cal latitudes since in this location the frequency of systems is
smaller. Tests on finding a suitable time window were made,
following the autocorrelation method applied by Gramciani-
nov et al. (2020c), resulting in the value of 96 h. In this

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 31450

C. B. Gramcianinov et al.

way, the peaks used for the maximum SWH distribution are
selected considering a minimal interval of 96 h between the
peaks. The extreme percentiles obtained for the North and
South Atlantic basins in the summer and winter can be found
in Figs. A1 and A2 of the Supplementary Material.

After  selecting  the  percentiles,  the  points  above  the
threshold in each time frame are grouped into regions that
are afterwards associated with a cyclone track. The centre
of mass of each extreme wave region is used in the search
and connection with the cyclone centre. The method requires
some adaptation from the original one since its applica-
tion to a larger domain can result in a spurious association
between cyclones and extreme waves. Three assumptions
are made to restrict the association and to guarantee that the
extreme wave is influenced by the local wind, as indicated
hereafter.

1.  The extreme event is associated with the cyclone that
exists at least 1 day before the extreme region. This cri-
terion is important to avoid the association of secondary
cyclones to the wave extremes generated by a parental
cyclone—considering that waves need a time scale of
days to develop even for the highest wind speeds (Has-
selmann et al. 1973; Ardhuin and Orfila 2018).

2.  To avoid the inclusion of swell dominated extremes con-
sideration is given to extreme points in which the sig-
nificant height of wind waves (SHWW, given by ERA5)
corresponds to more than 50% of the SWH. While the
SWH  is  calculated  using  the  integral  over  all  two-
dimensional wave spectrum, the SHWW uses only the
wind-sea wave spectrum obtained by only considering
the components of the two-dimensional wave spectrum
that are still under the influence of the local wind. Sepa-
rating swell from wind-sea is not trivial, especially in a
high wave generation environment such as the Southern
Ocean (Rapizo et al. 2015), which is partially covered by
the present domain. Other approaches, such as establish-
ing a minimum value for the difference between wind
and peak wave direction (e.g., 90° by Rapizo et al. 2015)
it is not practicable in such a high-resolution grid. Inter-
action between remote propagating and local waves can
remain but focusing on extreme percentiles also helps
the exclusion of swell dominated cases.

3.  The  cyclone  centre  is  associated  only  if  it  is  within
1500 km from the centre of mass of the extreme wave
region. The cyclone-related waves are then defined in
this work as an extreme wave region associated with a
local cyclone by the method described above.

2.4   Cyclone‑related wave parameters

Several cyclone parameters are calculated using the track
information provided by the AETC dataset. The maximum

10-m wind speed is added to each track by a general search
for the maximum value within a 6° radius of the cyclone
centre (Bengtsson et al. 2009) and is used as a measure of
cyclone intensity together with the vorticity. The centre of
the cyclone along the track is also used to calculate cyclone
displacement  and  the  distance  and  the  relative  position
between cyclone and extreme wave regions. The entire track
information of the cyclone is used to produce the storm track
statistics.

Mean parameters of the cyclone-related waves are used
to compute statistics, producing distribution maps of mean
SWH  (SWHmean), maximum SWH  (SWHmax), mean wave
direction, mean 10-m wind direction, and others. These
parameters  are  obtained  directly  from  the  ERA5  prod-
ucts, and the value associated with each case is the average
between all points in the extreme regions (i.e., that over-
passes the extreme percentile).

Spatial statistics of cyclone-related wave parameters,
cyclone genesis and track distribution are computed using
the spherical kernel estimator approach (Hodges 1996). The
maps are built using the position of the centre of mass of the
extreme wave region while the cyclone spatial statistics uses
the centre of the cyclones. The tendencies are calculated
through differences between the two 21 years’ time slices
in the whole period and were tested using the Monte Carlo
significance test (Hodges 2008) with 1000 samples of the set
of tracks for each period.

The results focus on the winter and summer for each basin
once they represent two opposite states in the annual cycle.
To the North Atlantic analysis, the boreal summer is defined
as June, July, and August (JJA) and the winter as Decem-
ber, January, and February (DJF). To the South Atlantic,
the austral summer and winter are defined as DJF and JJA,
respectively.

3   Results

3.1   Extreme wave events

The cyclone-related extreme wave distribution obtained
based  on  different  percentiles  is  presented  in  terms  of
density in Figs. 1 and 2, which may be interpreted as the
frequency in which a location (area = 5° spherical caps) is
affected by extreme waves in a month, not distinguishing the
same event along the time axis. This means that long events
also contribute to high densities.

In the North Atlantic (Fig. 1), there are three hot spots for
extreme wave events located on the northeastern USA coast,
south of Greenland, and northwest of the British Islands.
The last two regions are highlighted in all percentiles. How-
ever, the US coast becomes more evident in more extreme
thresholds (Fig. 1c–f), in both seasons. The winter presents

1 3
1451

Fig. 1   Density of extreme wave
events associated with cyclone
(shaded) in the North Atlantic
Ocean: in the boreal (a, c)
winter (DJF) and (b, d) summer
(JJA) for the (a, b) 90th, (c, d)
95th, and (e, f) 99th percentiles
of waves events. Density unit
is the occurrence of extreme
wave regions per month per
area, where the area is  106km2
(∼ 5° spherical cap). Density
is contoured by the double of
coloured level intervals

higher densities than the summer, especially in the hot spots
further north. In the summer, the high density near the Brit-
ish Islands shifts slightly southward. One can note that the
distribution of events is highly concentrated between 45° N
and 70° N during the winter, despite the zonal maximum
around 60°N. This pattern is a consequence of the large
fetches produced by the extratropical winter storms between
North America and Europe, which is distinct from the wider
spread events observed in the South Atlantic (Fig. 2).

The South Atlantic presents a more zonal distributed
event occurrence (Fig. 2), with a high density between 40°
S and 55° S and similar densities range in both seasons, even
though the summer presents slightly less event occurrence.
The Drake Passage (DKP) and its surroundings, in the east-
ern boundary of the domain, present higher densities in all
percentiles for both seasons. However, it is possible to note
that the high density shifts southeastward with the increase

of the percentile. This region is known for the high waves
and bad navigation conditions (e.g., Campos et al. 2020). In
the winter, the southwestern South Atlantic (swSA), between
50° S and 35° S along the South American coast, appears as
a hotspot of events, which is more evident in the 99th per-
centile. In fact, the swSA generally presents higher density
than other locations at the same latitude, showing a density
distribution skewed to the west, especially in the summer.

Cyclone-related  wave  events  dominate  the  overall
extreme wave distribution, being responsible for more than
65% of the events in most of the study domains (see Sup-
plementary Figs. A3 and A4). The direct effect of cyclones
in the wave climate increases according to the percentiles
but is relatively small in the high-latitude and east-side of
the ocean basins (e.g., Portugal and Morocco coasts in the
NA and South African and Namibian coasts in the SA). An
important remark is that is difficult to estimate how much

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 3C. B. Gramcianinov et al.

1452

Fig. 2   Density of extreme wave
events associated with cyclone
(shaded) in the South Atlantic
Ocean: in the austral (a, c)
summer (DJF) and (b, d) winter
(JJA) for the (a, b) 90th, (c, d)
95th, and (e, f) 99th percentiles
of waves events. Density unit
is the occurrence of extreme
wave regions per month per
area, where the area is  106  km2
(∼ 5° spherical cap). Density
is contoured by the double of
coloured level intervals

cyclone-generated waves account for SWH field, i.e., in
the SWH percentiles, due to the superposing of wind-sea
and swell. Even trying to separate our events from swell
dominated events during the cyclone-related event selection,
superposing still exists in some cases. However, it is possible
to see that regions reported to be swell dominant appear with
a low percentage (< 60%) of cyclone-related wave events,
such as the coast of Portugal, Greenland, Brazil, and South
Africa.

3.2   Cyclones associated with extreme waves

Table 1 presents the annual mean of cyclones associated
with extreme waves for each domain, season, and percentile.
In the 1979–2020 period, the NA presented 38 and 17.5
cyclones per year related to the 90th percentile wave occur-
rence, for the boreal winter (DJF) and summer, respectively,
which corresponds to 24.4% and 14.9% of the cyclones in

these seasons. The percentages of wave-associated cyclones
follow the reduction of the cyclones in more extreme per-
centiles, with almost double the cyclones in the winter than
in the summer. In the SA, differences between the austral
summer (DJF) and winter (JJA) are not so evident. Between
1979 and 2020, the SA presented 32.5 and 39.2 associated
cyclones per year for the summer and winter, considering
the 90th percentile waves. The percentage of associated
cyclones in the summer is slightly larger than in the winter,
even though the former presents a lower annual mean.

Cyclone genesis and track densities computed for the
cyclones associated with extreme waves are presented in
Figs. 3 and 4 for the North Atlantic and South Atlantic,
respectively. In the North Atlantic, the genesis densities
show three main genesis regions: lee of the southern Rock-
ies Mountains (35° N, 102.5° W; RKM), USA northeast-
ern coast (40° N, 75° W, USC), and Central East Atlantic
(centred at 55° N, 30° W, CEA). North Atlantic storm track

1 3
Table 1   Annual mean of
cyclones for the different
analyzed periods

1453

Basin and
season

NA

DJF

NA

JJA

SA

DJF

SA

JJA

Period

Climatology

Number of associated cyclones and percentage

90th

95th

99th

1979–2020
1979–1999
2000–2020
1979–2020
1979–1999
2000–2020
1979–2020
1979–1999
2000–2020
1979–2020
1979–1999
2000–2020

156.0 ± 9.6
156.3 ± 10.6
156.0 ± 8.8
117.6 ± 8.2
120.1 ± 7.1
115.0 ± 3.7
154.0 ± 9.2
151.2 ± 8.2
156.9 ± 9.1
195.4 ± 10.9
193.5 ± 9.6
197.2 ± 12.1

38.0 ± 5.1 (24.4%)
37.8 ± 5.0 (24.4%)
38.2 ± 5.3 (24.5%)
17.5 ± 3.4 (14.9%)
17.6 ± 3.1 (14.6%)
17.5 ± 3.7 (15.2%)
32.5 ± 6.1 (21.1%)
29.6 ± 5.8 (19.6%)
35.3 ± 5.2 (22.3%)
39.2 ± 6.0 (20.0%)
36.3 ± 4.8 (18.8%)
42.0 ± 5.8 (21.3%)

25.6 ± 5.1 (16.4%)
25.3 ± 5.0 (16.2%)
25.9 ± 5.2 (16.6%)
11.2 ± 2.7 (9.5%)
11.0 ± 2.6 (9.1%)
11.4 ± 2.8 (9.9%)
21.1 ± 5.2 (13.7%)
19.8 ± 4.8 (13.1%)
22.4 ± 5.3 (14.3%)
24.4 ± 4.8 (12.5%)
23.4 ± 4.2 (12.1%)
25.4 ± 5.2 (12.9%)

9.7 ± 3.1 (6.2%)
10.0 ± 2.7 (6.4%)
9.4 ± 3.6 (6.0%)
4.9 ± 1.8 (4.2%)
4.8 ± 2.1 (4.0%)
5.0 ± 1.4 (4.4%)
8.3 ± 3.0 (5.4%)
8.1 ± 2.7 (5.4%)
8.5 ± 3.3 (5.4%)
9.2 ± 2.7 (4.7%)
9.5 ± 2.7 (4.9%)
8.8 ± 2.6 (4.5%)

The climatology values are for all cyclones in the database and associated cyclones indicate only systems
related  to  extreme  waves,  according  to  the  percentil  used  to  the  selection  of  the  wave  regions.  The  per-
centage for each percentile is calculated in relation to climatology. Values are presented separately for the
North Atlantic (NA) and South Atlantic (SA), as well for the DJF and JJA

climatology (Dacre and Gray 2009; Hoskins and Hodges
2002, 2019) presents four cyclogenesis regions, with high
genesis activity on the eastern coast of Greenland—a region
that is less relevant to cyclone-related waves according to
Fig. 3. The cyclonic activity in the North Atlantic is more
intense in the boreal winter (DJF), which reflects in the
climatological genesis and track densities distribution. In
the winter, the three genesis regions are present while only
RKM and USC are relevant during the summer.

Regarding the percentiles, the USC gains even more rel-
evance with the increase of percentile when compared to
the other regions. The North Atlantic storm track presents
a northeast orientation across the basin (e.g., Hoskins and
Hodges 2002; Gramcianinov et al. 2020a), which is also
reproduced by the selected cyclones (Fig. 3). Two regions
present high track density and their importance changes
according to the season and percentile. During the winter,
there is a main storm track along the northeastern USA
coast,  followed  by  a  secondary  branch  in  the  Northeast
North Atlantic (NNA). The secondary storm track loses its
signal in higher percentiles, indicating that a big part of the
cyclones associated with extreme events in the basin comes
through the USA coast in this season. The summer has a
dispersed and weak storm track, but the large densities occur
poleward, covering the NNA region.

In the South Atlantic (Fig. 4), the cyclogenesis concen-
trates along the South American south and central coast,
following the three main genesis regions reported by the
literature (e.g., Hoskins and Hodges 2005; Gramcianinov
et al. 2019, 2020a). In the austral winter (JJA), the genesis
region around 30° S in La Plata Basin (LPB) are more
active, but the genesis over Argentina (ARG) is usually

the largest over the whole year. However, the genesis den-
sity in the LPB region overpasses the ARG region in the
higher percentiles (Fig. 4d, f). These two genesis regions
also appear in the summer densities distribution, with the
ARG genesis activity leading in all percentiles. Moreover,
in the 90th percentile (Fig. 4a) a genesis density higher
than 1 cyclone per season appears covering a region up to
25° S, along the Southeast Brazilian coast (SBR), which
is usually associated with subtropical cyclogenesis and
transitions (Gozzo et al. 2014; da Rocha et al. 2019; de
Jesus et al. 2020). The track density reflects the genesis
density, showing the displacement of the cyclone eastward
with a slight tilt poleward, a typical characteristic of the
South Atlantic’s storm track (Hoskins and Hodges 2005).
However, when comparing to the climatology (Gramciani-
nov et al. 2020a), it is possible to see that the subtropical
path of the storm track is more evident in Fig. 4, due to
the large relevance of cyclones generated at LPB and SBR
associated with the extreme wave climate.

The intensity and speed distribution of the cyclones asso-
ciated with extremes are presented as their deviation from
the climatology for the same period in Fig. 5. Due to similar-
ity, only the results for the 90th are presented. The cyclones
associated with extreme waves are more intense regarding
the wind speed at 10-m (Fig. 5a–d). The distribution of this
intensification follows the storm track behaviour, reaching
lower latitudes in the winter when the cyclone track density
is spread. These cyclones are generally slower than clima-
tology as is possible to see by the dominance of negative
values in Fig. 5e–g. The speed difference is smaller and can
be even positive in the main storm track position where the
upper-level jet is stronger, driving the cyclone propagation.

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 3C. B. Gramcianinov et al.

1454

Fig. 3   Cyclone track (shaded)
and genesis (contoured) densi-
ties associated with extreme
waves in the North Atlantic
Ocean: in the boreal (a, c, e)
winter (DJF) and (b, d, f) sum-
mer (JJA) for the (a, b) 90th, (c,
d) 95th, and (c, d) 99th percen-
tiles of waves events. Density
unit is cyclone per season per
area, where the area is  106  km2
(∼ 5° spherical cap). Cyclo-
genesis density is contoured by
(a–d) 0.5 and (e, f) 0.2 units

3.3   Cyclone‑related waves characteristics

The spatial distributions of cyclone-related wave’s charac-
teristics were analysed only for the 90th (Figs. 6, 7) due to
the similarity with the other percentiles. Moreover, the 90th
percentile was selected because the higher number of cases
in this percentile allows more robust estimations of the spa-
tial patterns and trends (Sect. 3.4).

The  SWHmean and  SWHmax associated with the cyclones
(Fig. 6) follow the climatological pattern of both basins, with
smaller values equatorward (Young 1999; Vinoth and Young
2011). The exception is in the North Atlantic for the summer
(JJA, Fig. 6b, f), which presents slightly high values west-
ward of the domain, probably due to the influence of USC
cyclones (Fig. 3). Despite that, for NA winter (DJF) and SA,
both  SWHmean and  SWHmax follow the orientation of the
storm track (Figs. 3, 4), with the large values poleward in the

middle east side of the domains, overlapping the downwind
of the storm track (Ponce de Léon and Bettencourt 2021).

The mean wave direction of the events (Fig. 7a–d) pre-
sents a prevalence of W (240°–300°) and SW (210°–240°)
waves  in  the  major  part  of  the  NA  and  SA.  In  the  NA
(Fig. 7a, b), extreme events with mean wave direction from
S (150°–210°), SE (120°–150°), and E (60°–120°) occur
in the USC and Greenland’s surroundings, especially in
the summer (JJA). Around 35°N, near the Portuguese and
North Africa coast, the cyclone-related mean wave direc-
tion changes from W in the winter (DJF) to S and SE in
the summer (JJA). Seasonal variability of the mean wave
direction of the cases is also observed in the SA (Fig. 7c, d),
where it is possible to find extreme waves propagating from
S and SW in the Argentina, Uruguay, and Southern Brazil
coasts and SE and E in the SBR. The mean 10-m wind direc-
tion distributions associated with the cyclone-related waves

1 3
1455

Fig. 4   Cyclone track (shaded)
and genesis (contoured) densi-
ties associated with extreme
waves in the South Atlantic
Ocean: in the austral (a, c, e)
summer (DJF) and (b, d, f) win-
ter (JJA) for the (a, b) 90th, (c,
d) 95th, and (c, d) 99th percen-
tiles of waves events. Density
unit is cyclone per season per
area, where the area is  106  km2
(∼ 5° spherical cap). Cyclo-
genesis density is contoured by
(a–d) 0.5 and (e, f) 0.2 units

present the same pattern and can be found in Fig. A5 of the
Supplementary Material.

Regarding the cyclone sector where the wave extreme
occurs (Fig. 7e–h), one can observe that in the NA, most of
the events in mid-latitudes occur in the S, SW sector of the
cyclone, in agreement with the dominant wave and wind
mean direction (Fig. 7e, f). In mature and early-occlusion
stages, typical of the mid-Atlantic and NNA storm track,
this sector of the cyclone is dominated by the cold conveyor
belt, located behind the cold front. In the SA (Fig. 7g, h),
the analogous situation is observed with the wave extremes
occurring mainly in the W and NW sector of the cyclone.
However, a comment may be made in the SBR region during
the summer (DJF), where the extreme events occur mainly
in the E sector of the cyclone with the mean wave direction

from E and SE, which indicate the influence of the warm
conveyor belt in this location, as observed by Gramcianinov
et al. (2020c). Along the Southern Brazilian coast, but in
winter, the dominant sector is W/NW, with the mean wave
direction and 10-m wind direction from S and SW, in agree-
ment with Gramcianinov et al. (2021a). According to these
authors, yet during the winter, there is a prevalence of the
cold conveyor belt in early to mature-stage cyclones, and
the extreme waves occurred in the downwind of the cyclone
fetch along the coast.

3.4   Changes in 42 years of reanalysis

Considering the annual means presented in Table 1 for the
two 21-year time slices, it is noticeable a slight increase

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 31456

C. B. Gramcianinov et al.

Fig. 5   Differences between cyclone climatology and cyclones associated with extreme waves regarding their (a–d) maximum 10-m winds (m/s)
and (e–h) displacement speed (m/s) in the NA (left) and SA (right)

Fig. 6   Distribution maps of (a–d) mean and (e–h) maximum SWH (m) of the 90th percentile cyclone-related waves for the NA and SA in the (a,
c, e, g) DJF and (b, d, f, h) JJA. The contour lines are the standard deviation in 0.5 intervals

or decrease in cyclone number associated with extreme
waves, depending on the season. However, the changes
are not significant compared to the standard deviation of
the annual mean. NA presents an increase in the associ-
ated cyclones in the boreal winter (DJF) in the 90th and
95th percentiles, but a decrease in the 99th. In the summer
(JJA) the increase occurs in the 95th and 99th percentiles.
In the austral winter (JJA), SA also presents an increase in
the cyclones associated with the 90th and 95th percentiles
waves, with a decrease in the higher percentile. However,

in the summer (DJF) there is a general increase of associ-
ated cyclones in all percentiles for the SA.

Figures 8 and 9 present the trends in the cyclone-related
wave occurrence, representing the changes between the
two  21-year  time  slices,  for  the  NA  and  SA.  The  ten-
dency of the 99th percentile is not presented due to the
lack of statistical confidence, as explained in the last sec-
tion. In general, the trends are very heterogeneous within
the domains and between summer and winter. Moreover,
although the signal pattern is mostly similar between the

1 3
1457

Fig. 7   Distribution  maps  of  (a–d)  mean  wave  direction  of  the  cases
and  (e–h)  cyclone  sector  where  the  extreme  wave  occurred  (relative
to the center of the cyclone). The contour lines are the standard devia-

tion in 30° intervals. The NA (left) and SA (right) maps are presented
in the (a, c, e, g) DJF and (b, d, f, h) JJA considering 90th percentile
cyclone-related waves

Fig. 8   Changes in the cyclone-
related wave occurrence in the
North Atlantic based on the (a,
b) 90th and (c, d) 95th percen-
tiles for the (a, c) DJF and (b,
d) JJA. Changes are computed
based on the difference between
2020–2000 and 1979–1999
periods. Significant differences
(p value < 0.1, t test) are marked
with black dots

extreme percentiles, its relative importance varies depend-
ing on the percentile.

North Atlantic winter tendencies (DJF, Fig. 8a, c) show a
decrease in the occurrence of extreme cyclone-related wave
occurrence in the NNA, northward of Ireland and British
Island. The region of high occurrence south of Greenland
(Fig. 1) presents an eastward shift, with the events affecting

more the eastern coast of the country. Offshore of the north-
eastern coast of the USA there is an increase in the occur-
rence of these events. There is also a slight increase of events
in a band that overlaps North of Spain and Portugal but only
in the 90th percentile. The 95th cyclone-related wave occur-
rence presents a decrease in this region. A very different pat-
tern can be found in the summer (JJA, Fig. 8b, d), where an

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 31458

Fig. 9   Changes in the cyclone-
related wave occurrence in the
South Atlantic based on the (a,
b) 90th and (c, d) 95th percen-
tiles for the (a, c) DJF and (b,
d) JJA. Changes are computed
based on the difference between
2020–2000 and 1979–1999
periods. Significant differences
(p value < 0.1, t test) are marked
with black dots

C. B. Gramcianinov et al.

increase in the occurrence of events over the NNA is noted,
covering not only the north but also the west sea offshore
Ireland and British Island. The eastward shift of the occur-
rence hot spot in Greenland is also observed, as well in the
north of Spain. For the summer, there is a weak decrease of
events on the northeastern USA coast.

Relative changes in the occurrence of cyclone-related
waves are smaller in the SA, but interesting patterns can
be observed. In the summer (DJF, Fig. 9a, c) most of the
domain presents an increase in the occurrence of events,
highlighting  the  region  offshore  South  American  coast,
from 50° S to 20° S, the region nearby Drake Passage, and
between 45° S and 55° S in the southeast of SA. The South
African coast presents a small but significant decrease in
event densities. For the winter (JJA, Fig. 9b, d) changes,
there  is  still  an  increase  in  the  South  American  coast,
but from 50° S to 40° S and only for the 90th percentile.
Between 40° S and 20° S, offshore Brazilian coast, there is
a decrease in the event density. The east portion of the Drake
Passage also presents an increase, but smaller than in the
summer. African coast, between 30° S and 20° S, present a
significant increase of cases.

The cyclone track density changes show an overall pole-
ward increase in the storm track associated with extreme
waves (Figs. 10, 11), but with a lack of statistical signifi-
cance. The differences are only significant in some points in
the middle of the South Atlantic for the tracks based on the

90th percentile (95th percentile is not shown since it does not
have any significant change). Despite that, the track changes
are presented even to the NA to support further discussion
about other changes in cyclone-related wave occurrence. In
the NA (Fig. 10), the largest change occurs in the boreal
winter (DJF), when the track density increases on the USA
coast. In the summer (JJA), the NA storm track strength in
the mid-to-eastern oceanic portion, which may be related to
the increase in the cyclone-related wave density in the north
portion of British Island. In the SA (Fig. 11), it is possible
to observe a poleward shift of the associated cyclone tracks,
similar to the reported general storm track behaviour in the
last decades (e.g., Fyfe 2003). However, in the SBR there
is a slight increase in the cyclone track densities, probably
indicating short duration cyclones with local effect.

Cyclone intensity based on the vorticity at 850 hPa and
displacement speed changes have spatially heterogeneous
distribution denoting the challenge of feature distribution
analysis. NA (Fig. 10c, d) shows a slight increase in the
cyclone intensity in mid-latitudes in the boreal winter (DJF),
while in the summer (JJA) a general negative sign prevails,
except by the western European coast. In the SA (Fig. 11c,
d), the winter (JJA) presents an increase in the associated
cyclones in the middle of the basin. In the summer (DJF)
there is a decrease of intensity in the middle and eastern
portion of the domain while it is possible to see an inten-
sification in the SBR region. The cyclone speed increases

1 3
1459

Fig. 10   Changes in the North
Atlantic cyclone (a, b) track
density (tracks per season per
 106  km2), (c, d) vorticity at
850 hPa  (105  s−1), and speed
(m/s) in the (a, c, e) DJF and
(b, d, f) JJA related to the 90th
percentile. Significant differ-
ences (p value < 0.1) are marked
with black dots. Regions with
track density smaller than 0.3
cyclones per season are not
plotted. Black contoured lines
have the double of shaded
intervals

present an increase in the NA winter (DJF) in mid-latitudes
near the western European coast and USC (Fig. 10e). In the
summer (JJA) there is a significant slowdown of cyclones
over the NNA region (Fig. 10f).

The SA cyclones associated with extreme waves present
an increase in their displacement speed in the major part of
the domain in both seasons (Fig. 11e, f), except between 30°
S and 20° S in the western portion of the basin. The overall
increase in the cyclone speed may be related to the inten-
sification of upper-level jets reported in some studies (e.g.,
Reboita et al. 2018). An important remark is that cyclones
move according to the upper-level circulation rather than the
surface winds (e.g., Hoskins and Hodges 2002, 2019), which
reflects the difference between cyclone intensity and speed
distribution maps. A cyclone embedded in the upper-level
jet tends to move faster than detached cyclones.

4   Discussion

4.1   Extreme waves and the extratropical storm

track

The cyclone-related waves, defined here as the extreme wave
regions  directly  associated  with  cyclones,  present  well-
defined occurrence hot spots and the observed seasonal vari-
ability can be related to the storm track shifts. The seasonal
variability is stronger in the NA, with much more events in
the boreal winter (DJF) than in the summer (JJA). In the
two ocean basins the cyclones associated with the extreme
waves are generated preferentially in the western boundary,
where the orography and warm ocean currents support their
development (e.g., Grise et al. 2013; Gramcianinov et al.
2019). These cyclones travel to the east tilting poleward

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 3C. B. Gramcianinov et al.

1460

Fig. 11   Changes in the South
Atlantic cyclone (a, b) track
density (tracks per season per
 106  km2), (c, d) vorticity at
850 hPa  (105  s−1), and speed
(m/s) in the (a, c, e) DJF and
(b, d, f) JJA related to the 90th
percentile. Significant differ-
ences (p value < 0.1) are marked
with black dots. Regions with
track density smaller than 0.3
cyclones per season are not
plotted. Black contoured lines
have the double of shaded
intervals

promoting extreme waves along the storm track and mainly
in its downwind end, as reported by past studies (e.g., Ponce
de Léon and Bettencourt 2021; Ponce de Léon and Guedes
Soares 2021).

During the cyclone early stages, its development and
intensification processes affect the positions of the fronts
depending on the relative dominance of different air fluxes
within the cyclones (e.g., warm and cold conveyor belts).

In this way, despite the cyclonic activity surrounding
genesis regions, the lack of directional persistence of the
winds and limited fetch size results in less extreme waves
in the western sector of the domain. On the other hand, on
the eastern portion where mature cyclones prevail, already

fully developed, travelling eastward with more stable fetches
relative to the cyclone displacement. The large size, inten-
sity and stable structure of these advanced-stage cyclones
allow the development of a large fetch with more stabilized
wind direction when compared to the cyclogenetic regions
(Fig. 7), resulting in higher waves (Fig. 6) and large occur-
rences of extremes in the eastern boundary of the domain,
close to the exit of the storm track. The relation between
the higher waves in the mid-eastern part of NA, the storm
track and the large fetch provided by mature cyclones agree
with previous studies that established this location as wind-
sea dominated (Stopa and Cheung 2014) and highly influ-
enced by extratropical cyclones (e.g., Ponce de Leon and

1 3
Bettencourt 2021). However, the north of the British Island,
usually considered swell dominant due to the diminishing of
the wind- correlation (Stopa and Cheung 2014) and the pres-
ence of longer waves (Young 1999), appears in the results as
relevant to the cyclone-related wave climate, revealing also
an important local forcing.

The mid-oceanic genesis regions reported by Dacre and
Gray (2009) for the NA and Gramcianinov et al. (2019) for
the SA play little influence on extreme wave generation due
to the lack of time interaction with ocean surface, reinforcing
the importance of cyclone lifecycle stage to extreme wave
generation. One important point in the SA is that the LPB
genesis region, which is responsible for producing most of
the cyclone-related waves in the austral winter (JJA), also
plays a big role in the summer (DJF) events, even not being
very active in this season (e.g., Gan and Rao 1991; Crespo
et al. 2021). Another cyclogenetic region associated with
wave extreme is the SBR, which is active in the austral sum-
mer (DJF) and where subtropical genesis and transitions
between cyclone types are reported (e.g., Gozzo et al. 2014;
da Rocha et al. 2019). The relation of SBR and LPB genesis
with cyclone-related extreme waves within the SA domain
can be related to the development of slower and/or stronger
cyclones in subtropical latitudes, with the influence of high
humidity income and warmer Brazilian Current (e.g., Gozzo
et al. 2017).

The cyclones associated with extreme wave events pre-
sent higher intensity regarding the vorticity and 10-m wind
speed (Fig. 4a–d). The direct relation between wind intensity
is expected by the Hasselman relation, which shows that
the wave growth directly correlates with the wind speed.
The increase of SWH is also time-dependent, and the strong
winds alone are not sufficient to fully developed extreme
waves. Thus, the cyclone speed displacement also appears
as a valuable parameter in our results, particularly in the
regions outside the westerly belts in both hemispheres. In
this location between 35° S and 20° S (SA) and 55° N and
70° N (NA) the cyclone’s speed is generally smaller than the
climatology (Fig. 4e–h), which affect the occurrence of the
cyclone-related waves, either by producing higher waves or
by elongating the duration of the events.

On average, extreme wave events tend to occur in the
cold sector of the extratropical cyclone, to the westward of
its centre, where it is located the cold conveyor belt. How-
ever, as mentioned before, the cyclone lifecycle stage may
change this location according to the relative position of
the cold and warm fronts. In regions nearby cyclogenesis,
such as the swSA and USC, extreme waves can take place
in the warm sector of the cyclone (eastern side, Fig. 7e–h),
being  influenced  by  the  strong  warm  advection  during
the cyclone development. The relative importance of the
cold and warm conveyor belt has been explored by previ-
ous works (Bell et al. 2017; Kita et al. 2018; Gramcianinov

1461

et al. 2020c; Ponce de Léon and Bettencourt 2021) and it
can lead to different perspectives of extreme wave genera-
tion within the extratropical cyclones. In agreement with
Gramcianinov et al. (2020c, 2021a), it is observed that the
SBR presents a high influence of the warm conveyor belt in
the summer (Fig. 7g), which may not generate waves that
propagate towards the coast, but can severely influence the
wave climate offshore, where there are oil exploitation and
navigation activities.

4.2   Changes in the cyclone‑related waves

The changes in the cyclone-related extreme wave occurrence
cannot be fully explained by the storm track trends reflect-
ing the complex mechanisms behind extreme wave climate
patterns. The results showed a link between the changes in
extreme wave occurrence and the cyclones characteristics,
such as intensity and displacement speed; a summary of this
relation is schematically presented in Fig. 12. The discussion
of the changes focused on the regions with high cyclone-
related  wave  density  (Figs.  1,  2)  and  significant  large
changes (Figs. 8, 9) according to the 90th percentile analysis
(significant results). In general, for both basins, there was an
increase in the occurrence of extreme waves associated with
cyclones, which is indicated by the changes in the number
of cyclones (Table 1), storm track (Figs. 10a, b, 11a, b), and
cyclone-related extreme waves (Figs. 8a, b, 9a, b), although
the signal is not always statistically significant.

The NA present four regions of important changes in
the cyclone-related extreme wave occurrence: eastern USA
coast, Greenland, north of the British Islands, and west
European coast. Despite the inclusion of the storm track
changes in this discussion, more focus has been given to
other parameters since the track density differences between
the periods were not significant at any point in the NA. In
the boreal winter (DJF), the strengthening of the storm track
at the Eastern US coast may affect the extreme wave occur-
rence in this region and east-northeastward, including the
west European coast between 40° N and 50° N (Fig. 8a).
The changes showed that the cyclones developing in the
USC and acting within 35° N and 50° N became stronger as
well, which led to more extreme waves despite the observed
increase in the cyclone speed over these regions. Further
north in the domain, the East Greenland coast and British
Islands are affected by the slight increase of the secondary
storm track (not statistically significant). However, the for-
mer region presents an increase in wave occurrence due to
the increase in cyclone intensity while the latter has weaker
cyclones, presenting a decrease. Besides the cyclone inten-
sity regulation, the summer pattern (JJA) showed a new ele-
ment which was the effect of the decrease in the cyclone
speed to the extreme wave occurrence. In the eastern Green-
land coast and British Islands, the decreased displacement

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 3C. B. Gramcianinov et al.

1462

Fig. 12   Summary scheme of
changes in the (a, b) North and
(c, d) Atlantic cyclone-related
extreme waves in present
climate and their main driving
mechanisms regarding storm
track characteristics. The
hot-spots are defined by back
boxes filled with light red and
blue for increase and decrease
of extreme wave occurrence,
respectively. Upward (down-
ward) arrows indicate increase
(decrease) of cyclone intensity
(purple) and displacement speed
(green) while the dots show
non-significant signal

speed counterbalanced the cyclone weakening, elongating
the cyclone’s wind interaction with the ocean surface.

The same pattern can be extended to the SA, with its
western portion presenting this counterbalance between
intensity and speed in the summer (DJF). In the SA four
regions are highlighted with important changes: the South-
ern Brazilian coast, western SA, Drake Passage, and south-
eastern SA. Changes in the SA storm track are statistically
significant between 40° S and 55° S, revealing an increase
in the track density therein. The increase in the cyclonic
activity in this band influences especially the Drake Passage
and eastern portion of the domain, potentially increasing the
extreme wave occurrence in these regions. The exception is
the southeastern SA, where the extreme wave occurrence
decreases due to the weakening of the cyclone acting in that
region in the winter (JJA).

Besides the high number of criteria used along this work
to obtain robust results, some limitations must be held to the
discussion above. The relations made between cyclone char-
acteristics and extreme wave regions considered a distance
of 10° to 5° between them. Despite the use of 1500 km (15°)
to link these features, the previous analysis showed that the
distance is still within 200–700 km radius from the cyclone
centre (Gramcianinov et al. 2021a), which allows the local
interpretation of the results made in this work. However,
the direct relation between the cyclone and wave distribu-
tions used can be set as a limitation of this work, since some
fields present heterogeneous change signals, making chal-
lenging the interpretation (i.e., the scale of the change signal
is smaller than 5°). To attenuate this problem, only some
regions are discussed, highlighted by their significant signal,
location, and extreme wave occurrence. Furthermore, it is

important to remember that the method applied has removed
the swell from the wave signal and the discussion considered
only cyclone-related wave events, forced locally. Although
some remote signals can still be retained, it is not dominant
and does not influence the discussion.

The difference between the two 21-year time slices is
used in the present work as a proxy of the change within
the entire period. However, it is not possible to conclude
if the obtained signal is driven by climate change or dif-
ferences  in  multi-decadal  atmospheric  oscillations.  The
global wave climate varies according to interannual climate
variations and teleconnections in both hemispheres (Wang
et al. 2008; Hemer et al. 2010; Godoi et al. 2020; Godoi and
Torres Junior 2020; Sasaki et al. 2021). With a time slice
of ~ 20 years, shorter interannual time-scales variability,
such El-Nino Southern Oscillation (ENSO) and even part of
Southern Annular Mode (SAM) is expected to be excluded.
However, long-term variabilities in decadal scales, such as
North Atlantic Oscillation (NAO), and Atlantic Multidecadal
Oscillation (AMO) may influence the changes reported here.
Nevertheless, it is relevant to access these changes to have a
better overview of what is happening in the present climate
to improve the analysis of the possible future scenarios.

5   Conclusion

The feature-based analysis applied in this work gave new
insights into cyclone related wave climate distribution
and characteristics. The results confirm and reinforce the
findings in many extreme wave climatology studies (e.g.,
Vinoth and Young 2011) and cyclone-related studies in the

1 3
North Atlantic Ocean (Takbash et al. 2019; Ponce de Léon
and Bettencourt 2021; Gramcianinov et al. 2021b) and
South Atlantic Ocean (Gramcianinov et al. 2020c, 2021a).
The novelty of the present work relies on the direct link
between cyclones and extreme wave events to add informa-
tion and justify the observed distributions and trends of the
extreme wave climate.

The hot-spot regions of cyclone-related waves occur-
rence resemble the locations that present high extreme sta-
tistics when using the traditional approach (i.e., extreme-
value  analyses,  Vinoth  and  Young 2011;  Campos  and
Guedes Soares 2016a, b; Campos et al. 2019; Takbash and
Young 2020), such as the downwind end of the storm track
due to accumulation of cyclone related fetches and wind
intensity. However, it is important to note that the western
sector of both domains also presents relevant cases, asso-
ciated with the intensification stages of cyclones. These
cyclone-related waves occur close to cyclogenesis regions
in the western boundary of the basins, affecting off eastern
South American and USA coasts—where such investiga-
tion cannot be neglected once these locations have high
socio-economic value.

The cyclone lifecycle phase has been shown to play a
big role in the extreme wave occurrence and SWH dis-
tributions. In the early stages, strong winds are expected
due to the cyclone development processes having enough
intensity to generate extreme waves. However, the move-
ments of the fronts in this phase contribute to a fast change
of wind direction compromising the fetch persistence. On
the other hand, in the middle of the storm track, cyclones
in  mature  stages  prevail,  combining  intensity  and  a
more stable structure to generate a large fetch. Besides,
cyclones associated with extreme waves are more intense,
as expected, and present slower displacement speed when
compared to the climatology, promoting extreme waves not
just by the wind intensity but also due to the longer time
of interaction between this wind and the ocean surface.

Considering 42 years, the changes in the distribution
of cyclone-related events and cyclones characteristics are
linked in different ways, and they result not only from the
storm track position but also from a combination of fac-
tors. It is expected that changes in the storm track orienta-
tion play a big role in the cyclone-related wave climate.
However, the results do not present significant changes
in the storm track in most of the domains. Instead, the
balance between the cyclone speed and intensity dictated
the extreme wave changes. The local increase in cyclone
intensity leads to an increase in the wave extremes, but
the decrease of intensity does not necessarily result in
a decrease of the waves (Fig. 12). In this situation, the
cyclone speed behaves as a modulator: if the cyclones are
somewhere slower, they counterbalance the weakness by

1463

increasing the time of interaction between wind and ocean
surface, i.e., wind persistence, increasing or elongating
extreme wave events.

Despite the relatively small changes in cyclone-related
extreme waves (up to 7.5 occurrences per month per area),
the impact on the ocean and coastal activities are consid-
erable, especially considering the 42 years-time interval.
The statistics based on individual events applied in this
work provide valuable information to assess trends and
future  changes,  giving  more  insights  about  changes  in
the weather systems rather than overall climate change
patterns.

Supplementary Information  The online version contains supplemen-
tary material available at https:// doi. org/ 10. 1007/ s00382- 022- 06390-2.

Acknowledgements  The  authors  acknowledge  the  anonymous
reviewer, who helped us to improve this article. This work is part
of the project “Extreme wind and wave modelling and statistics in
the Atlantic Ocean” (EXWAV) funded by the São Paulo Research
Foundation (FAPESP) Grant #2018/08057-5 and by the Portuguese
Foundation for Science and Technology (Fundação para a Ciência
e Tecnologia—FCT) under contract PTDC/EAM-OCE/31325/2017
RD0504. This work contributes to the Strategic Research Plan of the
Centre for Marine Technology and Ocean Engineering (CENTEC),
which  is  financed  by  the  Portuguese  Foundation  for  Science  and
Technology (Fundação para a Ciência e Tecnologia—FCT) under
contract UIDB/UIDP/00134/2020. C.B.G. was funded by a FAPESP
postdoc scholarship Grant #2020/01416-0. R.M.C. is funded by the
Cooperative Institute for Marine and Atmospheric Studies (CIMAS),
a Cooperative Institute of the University of Miami and the National
Oceanic and Atmospheric Administration, cooperative Agreement
NA20OAR4320472.  The  authors  would  like  to  acknowledge  the
ECMWF for providing the atmospheric and wave data for the study.
The ERA5 products were generated using Copernicus Climate Change
Service Information [2019]. This study used the high-performance
computing resources of the SDumont supercomputer (http:// sdumo nt.
lncc. br), which is provided by the National Laboratory for Scientific
Computing (LNCC/MCTI, Brazil).

Author contributions  CBG conceptualization, formal analysis, meth-
odology, visualization, writing—original draft. RC and RMC concep-
tualization, methodology, writing—review and editing. PLSD and CGS
writing—review and editing, supervision.

Funding  Grant  #2018/08057-5,  São  Paulo  Research  Foundation
(FAPESP); Grant #2020/01416-0, São Paulo Research Foundation
(FAPESP); contract PTDC/EAM-OCE/31325/2017, Fundação para
a Ciência e Tecnologia—FCT; contract UIDB/UIDP/00134/2020,
Fundação para a Ciência e Tecnologia—FCT.

Availability of data and material  The ERA5 products were obtained
with Copernicus Climate Change Service (C3S) (2017) (https:// cds.
clima te. coper nicus. eu/, last access: June 2021). The Cyclone tracks
used in this study are available at “Atlantic extratropical cyclone tracks
databases” (https:// data. mende ley. com/ datas ets/ kwcvf r52hp/5; Gram-
cianinov et al. 2020b). The cyclone track associated with extreme wave
events obtained in this study can be shared upon request by email.

Code availability  The codes used in Sect. 3.3 can be shared upon
request by email.

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 31464

Declarations

Conflict of interest  The authors declare that they have no conflict of
interest.

References

Alves JHG (2006) Numerical modeling of ocean swell contributions
to the global wind-wave climate. Ocean Model 11(1–2):98–122.
https:// doi. org/ 10. 1016/j. ocemod. 2004. 11. 007

Ardhuin F, Orfila A (2018) Wind waves. New Front Oper Oceanogr,

pp 393–422. https:// doi. org/ 10. 17125/ gov20 18. ch14

Ardhuin F, Chapron B, Collard F (2009) Observation of swell dissipa-
tion across oceans. Geophys Res Lett 36(6):1–5. https:// doi. org/
10. 1029/ 2008G L0370 30. https:// arxiv. org/ abs/ 0809. 2497

Bell RJ, Gray SL, Jones OP (2017) North Atlantic storm driving of
extreme wave heights in the North Sea. J Geophys Res Ocean
122(4):3253–3268. https:// doi. org/ 10. 1002/ 2016J C0125 01
Belmonte Rivas M, Stoffelen A (2019) Characterizing ERA-Interim
and  ERA5  surface  wind  biases  using  ASCAT.  Ocean  Sci
15(3):831–852. https:// doi. org/ 10. 5194/ os- 15- 831- 2019

Bengtsson  L, Hodges KI, Keenlyside  N  (2009)  Will extratropical
storms intensify in a warmer climate? J Clim 22(9):2276–2301.
https:// doi. org/ 10. 1175/ 2008J CLI26 78.1.  https:// arxiv. org/ abs/
95010 47 [cond-mat]

Bernardino M, Goncalves M, Guedes Soares C (2021) Marine climate
projections toward the end of the twenty-first century in the north
Atlantic. J Offshore Mech Arct Eng. https:// doi. org/ 10. 1115/1.
40506 98

Bitner-Gregersen EM, Vanem E, Gramstad O et al (2018) Climate
change and safe design of ship structures. Ocean Eng 149:226–
237. https:// doi. org/ 10. 1016/j. ocean eng. 2017. 12. 023

Caires S, Sterl A (2005) 100-year return value estimates for ocean wind
speed and significant wave height from the ERA-40 data. J Clim
18(7):1032–1048. https:// doi. org/ 10. 1175/ JCLI- 3312.1

Campos RM, Guedes Soares C (2016a) Comparison and assessment of
three wave hindcasts in the North Atlantic Ocean. J Oper Ocean-
ogr 9(1):26–44. https:// doi. org/ 10. 1080/ 17558 76x. 2016. 12002 49
Campos RM, Guedes Soares C (2016b) Comparison of HIPOCAS
and ERA wind and wave reanalyses in the North Atlantic Ocean.
Ocean Eng 112:320–334. https:// doi. org/ 10. 1016/j. ocean eng.
2015. 12. 028

Campos RM, Alves JH, Guedes Soares C et al (2018) Extreme wind-
wave modeling and analysis in the South Atlantic ocean. Ocean
Model  124(August  2017):75–93.  https:// doi. org/ 10. 1016/j.
ocemod. 2018. 02. 002

Campos RM, Guedes Soares C, Alves JH et al (2019) Regional long-
term extreme wave analysis using hindcast data from the South
Atlantic Ocean. Ocean Eng 179(March):202–212. https:// doi. org/
10. 1016/j. ocean eng. 2019. 03. 023

Campos RM, D’Agostini A, Franca BRL et al (2020) Extreme wind
and wave predictability from operational forecasts at the drake
passage. J Offshore Mech Arct Eng. DOI 10(1115/1):4048151
Catto JL, Ackerley D, Booth JF et al (2019) The future of midlatitude
cyclones. Curr Clim Chang Rep 5(4):407–420. https:// doi. org/ 10.
1007/ s40641- 019- 00149-4

Chen G, Chapron B, Ezraty R et al (2002) A global view of swell and
wind sea climate in the ocean by satellite altimeter and scatterom-
eter. J Atmos Ocean Technol 19(11):1849–1859. https:// doi. org/
10. 1175/ 1520- 0426(2002) 019h1 849: AGVOS Ai2.0. CO;2

Copernicus Climate Change Service (C3S) (2017) ERA5: fifth genera-
tion of ECMWF atmospheric reanalyses of the global climate.
Copernicus Climate Change Service Climate Data Store (CDS).

C. B. Gramcianinov et al.

https:// cds. clima te. coper  nicus. eu/ cdsapp# !/ home. Accessed 20
Jan 2021

Crespo NM, da Rocha RP, Sprenger M et al (2021) A potential vorticity
perspective on cyclogenesis over centre-eastern South America.
Int J Climatol 41(1):663–678

da Rocha RP, Sugahara S, da Silveira RB (2004) Sea Waves generated
by extratropical cyclones in the south Atlantic ocean: hindcast and
validation against altimeter data. Weather Forecast 19(2):398–
410. https:// doi. org/ 10. 1175/ 1520- 0434(2004) 019h0 398: swgbe
ci2.0. co;2

da  Rocha  RP,  Reboita  MS,  Gozzo  LF  et  al  (2019)  Subtropical
cyclones over the oceanic basins: a review. Ann N Y Acad Sci
1436(1):138–156. https:// doi. org/ 10. 1111/ nyas. 13927

Dacre HF, Gray SL (2009) The spatial distribution and evolution
characteristics of North Atlantic cyclones. Mon Weather Rev
137(1):99–115. https:// doi. org/ 10. 1175/ 2008M WR2491.1
de Jesus EM, da Rocha RP, Crespo NM et al (2020) Multi-model cli-
mate projections of the main cyclogenesis hot-spots and associ-
ated winds over the eastern coast of south America. Clim Dyn
56(1–2):537–557. https:// doi. org/ 10. 1007/ s00382- 020- 05490-1

Dobrynin M, Murawsky J, Yang S (2012) Evolution of the global wind
wave climate in CMIP5 experiments. Geophys Res Lett 39(17):2–
7. https:// doi. org/ 10. 1029/ 2012G L0528 43

Fyfe JC (2003) Extratropical Southern Hemisphere cyclones: harbin-
gers of climate change? J Clim 16(17):2802–2805. https:// doi. org/
10. 1175/ 1520- 0442(2003) 016h2 802: ESHCH Oi2.0. CO;2

Gan MA, Rao VB (1991) Surface cyclogenesis over South America.
Mon Weather Rev 119(5):1293–1302. https:// doi. org/ 10. 1175/
1520- 0493(1991) 119h1 293: SCOSA i2.0. CO;2

Geng Q, Sugi M (2003) Possible change of extratropical cyclone activ-
ity due to enhanced greenhouse gases and sulfate aerosols—study
with a high-resolution AGCM. J Clim 16(13):2262–2274. https://
doi. org/ 10. 1175/ 1520- 0442(2003) 16h22 62: PCOEC Ai2.0. CO;2
Godoi VA, Torres Junior AR (2020) A global analysis of austral sum-
mer ocean wave variability during SAM–ENSO phase combina-
tions. Clim Dyn 54(9–10):3991–4004. https:// doi. org/ 10. 1007/
s00382- 020- 05217-2

Godoi VA, de Andrade FM, Durrant TH et al (2020) What happens
to the ocean surface gravity waves when ENSO and MJO phases
combine during the extended boreal winter? Clim Dyn 54(3–
4):1407–1424. https:// doi. org/ 10. 1007/ s00382- 019- 05065-9
Gozzo LF, da Rocha RP, Reboita MS et al (2014) Subtropical cyclones
over the southwestern South Atlantic: climatological aspects and
case study. J Clim 27(22):8543–8562. https:// doi. org/ 10. 1175/
JCLI-D- 14- 00149.1

Gozzo LF, da Rocha RP, Gimeno L et al (2017) Climatology and
numerical case study of moisture sources associated with subtrop-
ical cyclogenesis over the southwestern Atlantic Ocean. J Geophys
Res 122(11):5636–5653. https:// doi. org/ 10. 1002/ 2016J D0257 64
Gramcianinov CB, Hodges KI, Camargo R (2019) The properties
and genesis environments of South Atlantic cyclones. Clim Dyn
53(7–8):4115–4140. https:// doi. org/ 10. 1007/ s00382- 019- 04778-1
Gramcianinov CB, Campos RM, de Camargo R et al (2020a) Analysis
of Atlantic extratropical storm tracks characteristics in 41 years
of ERA5 and CFSR/CFSv2 databases. Ocean Eng 216(108):111.
https:// doi. org/ 10. 1016/j. ocean eng. 2020. 108111

Gramcianinov CB, Campos RM, de Camargo R, et al. (2020b) Atlan-
tic extratropical cyclone tracks in 41 years of ERA5 and CFSR/
CFSv2 databases. Mendeley Data V4. https:// doi. org/ 10. 17632/
kwcvf r52hp.4

Gramcianinov  CB,  Campos  RM,  Guedes  Soares  C  et  al  (2020c)
Extreme waves generated by cyclonic winds in the western portion
of the South Atlantic Ocean. Ocean Eng 213(1):107745. https://
doi. org/ 10. 1016/j. ocean eng. 2020c. 107745

Gramcianinov CB, Campos RM, de Camargo R et al (2021a) Relation
between cyclone evolution and fetch associated with extreme wave

1 3
events in the South Atlantic Ocean. J Offshore Mech Arct Eng
2A–2020:1–27. https:// doi. org/ 10. 1115/1. 40510 38

Gramcianinov CB, Campos RM, Guedes Soares C et al (2021b) Distri-
bution and characteristics of extreme waves generated by extrat-
ropical cyclones in the North Atlantic Ocean. In: Guedes Soares
C, Santos TA (eds) Developments in maritime technology and
engineering. Taylor and Francis, London, pp 797–804

Grise KM, Son SW, Gyakum JR (2013) Intraseasonal and interannual
variability in north American storm tracks and its relationship to
equatorial pacific variability. Mon Weather Rev 141(10):3610–
3625. https:// doi. org/ 10. 1175/ MWR-D- 12- 00322.1

Guedes Soares C (1984) Representation of double-peaked sea wave
spectra. Ocean Eng 11(2):185–207. https:// doi. org/ 10. 1016/ 0029-
8018(84) 90019-2

Hasselmann K, Barnett TP, Bouws E et al (1973) Measurements of
windwave growth and swell decay during the Joint North Sea
wave project (JONSWAP). Deutches Hydrographisches Institut
Zeit A8:1–95

Hemer MA, Church JA, Hunter JR (2010) Variability and trends in the
directional wave climate of the southern hemisphere. Int J Clima-
tol 30(4):475–491. https:// doi. org/ 10. 1002/ joc. 1900

Hersbach H, Bell B, Berrisford P et al (2020) The ERA5 global rea-
nalysis. Q J R Meteorol Soc 146(730):1999–2049. https:// doi. org/
10. 1002/ qj. 3803

Hodges KI (1994) A general method for tracking analysis and its appli-
cation to meteorological data. Mon Weather Rev 122(11):2573–
2586.  https:// doi. org/ 10. 1175/ 1520- 0493(1994) 122h2 573:
AGMFT Ai2.0. CO;2

Hodges KI (1995) Feature tracking on the unit sphere. Mon Weather

Rev  123(12):3458–3465.  https:// doi. org/ 10. 1175/ 1520-
0493(1995) 123h3 458: FTOTU Si2.0. CO;2

Hodges  KI  (1996)  Spherical  nonparametric  estimators  applied  to
the UGAMP model integration for AMIP. Mon Weather Rev
124(12):2914–2932. https:// doi. org/ 10. 1175/ 1520- 0493(1996)
124h2 914: SNEAT Ti2.0. CO;2

Hodges KI (1999) Adaptative constraints for feature tracking. Mon
Weather  Rev  127:1362–1373. https:// doi. org/ 10. 4324/ 97813
15658 032

Hodges  KI  (2008)  Confidence  intervals  and  significance  tests  for
spherical data derived from feature tracking. Mon Weather Rev
136(5):1758–1777. https:// doi. org/ 10. 1175/ 2007M WR2299.1
Hoskins BJ, Hodges KI (2002) New perspectives on the northern hemi-
sphere winter storm tracks. J Atmos Sci 59(6):1041–1061. https://
doi. org/ 10. 1175/ 1520- 0469(2002) 059h1 041: NPOTN Hi2.0. CO;2
Hoskins BJ, Hodges KI (2005) A new perspective on southern hemi-
sphere storm tracks. J Clim 18(20):4108–4129. https:// doi. org/ 10.
1175/ JCLI3 570.1. https:// arxiv. org/ abs/ joc. 1492 [10.1002]
Hoskins BJ, Hodges KI (2019) The annual cycle of Northern Hemi-
sphere storm tracks. Part I: seasons. J Clim 32(6):1743–1760.
https:// doi. org/ 10. 1175/ JCLI-D- 17- 0870.1

Kita  Y,  Waseda  T,  Webb  A  (2018)  Development  of  waves  under
explosive  cyclones  in  the  Northwestern  Pacific.  Ocean  Dyn
68(10):1403–1418. https:// doi. org/ 10. 1007/ s10236- 018- 1195-z

Lambert SJ, Fyfe JC (2006) Changes in winter cyclone frequencies
and strengths simulated in enhanced greenhouse warming experi-
ments: results from the models participating in the IPCC diagnos-
tic exercise. Clim Dyn 26(7–8):713–728. https:// doi. org/ 10. 1007/
s00382- 006- 0110-3

Lemos G, Semedo A, Dobrynin M et al (2019) Mid-twenty-first cen-
tury global wave climate projections: results from a dynamic
CMIP5 based ensemble. Glob Planet Change 172:69–87. https://
doi. org/ 10. 1016/j. glopl acha. 2018. 09. 011

Lim EP, Simmonds I (2002) explosive cyclone development in the
southern hemisphere and a comparison with northern hemisphere
events. Mon Weather Rev 130(9):2188–2209. https:// doi. org/ 10.
1175/ 1520- 0493(2002) 130h2 188: ecdit si2.0. co;2

1465

Meucci A, Young IR, Hemer M et al (2020) Projected 21st century
changes in extreme wind-wave events. Sci Adv 6(24):eaaz7295.
https:// doi. org/ 10. 1126/ sciadv. aaz72 95

Pezza AB, Ambrizzi T (2003) Variability of southern hemisphere
cyclone  and  anticyclone  behavior:  further  analysis.  J  Clim
16:1075–1083. https:// doi. org/ 10. 1175/ 1520- 0442(2003) 016h1
075: VOSHC Ai2.0. CO;2

Ponce de Léon S, Bettencourt J (2021) Composite analysis of North
Atlantic extra-tropical cyclone waves from satellite altimetry
observations.  Adv  Sp  Res  68(2):762–772. https:// doi. org/ 10.
1016/j. asr. 2019. 07. 021

Ponce de Léon S, Guedes Soares C (2014) Extreme wave parameters
under North Atlantic extratropical cyclones. Ocean Model 81:78–
88. https:// doi. org/ 10. 1016/j. ocemod. 2014. 07. 005

Ponce  de  Léon  S,  Guedes  Soares  C  (2015)  Hindcast  of  extreme
sea states in North Atlantic extratropical storms. Ocean Dyn
65(2):241–254. https:// doi. org/ 10. 1007/ s10236- 014- 0794-6
Ponce de Léon S, Guedes Soares C (2021) Numerical modelling of the
effects of the gulf stream on the wave characteristics. J Mar Sci
Eng 9(1):42. https:// doi. org/ 10. 3390/ jmse9 010042

Rapizo H, Babanin AV, Schulz E et al (2015) Observation of wind-
waves from a moored buoy in the Southern Ocean. Ocean Dyn
65(9–10):1275–1288. https:// doi. org/ 10. 1007/ s10236- 015- 0873-3
Reboita MS, da Rocha RP, Ambrizzi T et al (2015) Trend and telecon-
nection patterns in the climatology of extratropical cyclones over
the Southern Hemisphere. Clim Dyn 45(7–8):1929–1944. https://
doi. org/ 10. 1007/ s00382- 014- 2447-3

Reboita MS, da Rocha RP, de Souza MR et al (2018) Extratropical
cyclones over the southwestern South Atlantic Ocean: HadGEM2-
ES and RegCM4 projections. Int J Climatol 38(6):2866–2879.
https:// doi. org/ 10. 1002/ joc. 5468

Reboita MS, Reale M, da Rocha RP et al (2020) Future changes in the
wintertime cyclonic activity over the CORDEX-CORE South-
ern Hemisphere domains in a multi-model approach. Clim Dyn
57(5–6):1533–1549. https:// doi. org/ 10. 1007/ s00382- 020- 05317-z
Reboita MS, Crespo NM, Torres JA et al (2021) Future changes in
winter explosive cyclones over the Southern Hemisphere domains
from the CORDEX-CORE ensemble. Clim Dyn. https:// doi. org/
10. 1007/ s00382- 021- 05867-w

Sanders F, Gyakum JR (1980) Synoptic-dynamic climatology of the
“bomb.” Mon Weather Rev 108(10):1589–1606. https:// doi. org/
10. 1175/ 1520- 0493(1980) 108h1 589: sdcot i2.0. co;2

Sasaki DK, Gramcianinov CB, Castro B et al (2021) Intraseasonal
variability of ocean surface wind waves in the western south
Atlantic: the role of cyclones and the pacific south American pat-
tern. Weather Clim Dyn 2(4):1149–1166. https:// doi. org/ 10. 5194/
wcd-2- 1149- 2021

Simmonds I, Keay K (2000) Mean Southern Hemisphere extratropical
cyclone behavior in the 40-year NCEP-NCAR reanalysis. J Clim
13(5):873–885. https:// doi. org/ 10. 1175/ 1520- 0442(2000) 013h0
873: MSHEC Bi2.0. CO;2

Sinclair MR (1994) An objective cyclone climatology for the Southern
Hemisphere.https:// doi. org/ 10. 1175/ 1520- 0493(1994) 122h2 239:
AOCCF Ti2.0. CO;2

Stopa JE, Cheung KF (2014) Intercomparison of wind and wave data
from the ECMWF reanalysis Interim and the NCEP climate fore-
cast system reanalysis. Ocean Model 75:65–83. https:// doi. org/ 10.
1016/j. ocemod. 2013. 12. 006

Takbash A, Young IR (2020) Long-term and seasonal trends in global
wave height extremes derived from ERA-5 reanalysis data. J Mar
Sci Eng 8(12):1–16. https:// doi. org/ 10. 3390/ jmse8 121015
Takbash A, Young IR, Breivik Ø (2019) Global wind speed and wave
height extremes derived from long-duration satellite records. J
Clim 32(1):109–126. https:// doi. org/ 10. 1175/ JCLI-D- 18- 0520.1
Ulbrich U, Leckebusch GC, Pinto JG (2009) Extra-tropical cyclones
in the present and future climate: a review. Theor Appl Climatol

Impact of extratropical cyclone intensity and speed on the extreme wave trends in the Atlantic…1 3

1466

C. B. Gramcianinov et al.

96(1–2):117–131. https:// doi. org/ 10. 1007/ s00704- 008- 0083-8,
https:// arxiv. org/ abs/ 96051 03 [cs]

Vettor R, Guedes Soares C (2020) A global view on bimodal wave
spectra  and  crossing  seas  from  ERA-interim.  Ocean  Eng
210(107):439. https:// doi. org/ 10. 1016/j. ocean eng. 2020. 107439

Vinoth J, Young IR (2011) global estimates of extreme wind speed and
wave height. J Clim 24(6):1647–1665. https:// doi. org/ 10. 1175/
2010J CLI36 80.1

Wang XL, Swail VR, Zwiers FW (2006) Climatology and changes of
extratropical cyclone activity: comparison of ERA-40 with NCEP-
NCAR  reanalysis  for  1958–2001.  J  Clim  19(13):3145–3166.
https:// doi. org/ 10. 1175/ JCLI3 781.1

Wang XL, Swail VR, Zwiers FW et al (2008) Detection of external
influence  on  trends  of  atmospheric  storminess  and  northern
oceans wave heights. Clim Dyn 32(2–3):189–203. https:// doi.
org/ 10. 1007/ s00382- 008- 0442-2

Young IR (1999) Seasonal variability of the global ocean wind and
wave climate. Int J Climatol 19(9):931–950. https:// doi. org/ 10.
1002/ (SICI) 1097- 0088(199907) 19: 9h931:: AID- JOC41 2i3.0.
CO;2-O

Young IR, Ribal A (2019) Multiplatform evaluation of global trends in
wind speed and wave height. Science (80-) 364(6440):548–552.
https:// doi. org/ 10. 1126/ scien ce. aav95 27

Publisher's  Note  Springer  Nature  remains  neutral  with  regard  to
jurisdictional claims in published maps and institutional affiliations.

1 3
