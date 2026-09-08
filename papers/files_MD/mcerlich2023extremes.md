RESEARCH LETTER
10.1029/2023GL104130

Key Points:

•

•

•

 We detail a new methodology to
assess precipitation extremes within
cyclone composites using a spatially
dependent precipitation threshold
 Extreme precipitation occurs
preferentially and makes up a larger
fraction of total accumulation before
cyclones reach peak intensity
 Extreme precipitation is more
constrained around the cyclone center
and weakens more rapidly over time
compared to moderate precipitation

Supporting Information:

Supporting Information may be found in
the online version of this article.

Correspondence to:

C. McErlich,
cameron.mcerlich@pg.canterbury.ac.nz

Citation:

McErlich, C., McDonald, A., Renwick,
J., & Schuddeboom, A. (2023). An
assessment of extra-tropical cyclone
precipitation extremes over the Southern
Hemisphere using ERA5. Geophysical
Research Letters, 50, e2023GL104130.
https://doi.org/10.1029/2023GL104130

Received 14 APR 2023
Accepted 27 AUG 2023

An Assessment of Extra-Tropical Cyclone Precipitation
Extremes Over the Southern Hemisphere Using ERA5
Cameron McErlich1

, and Alex Schuddeboom1

, Adrian McDonald1,2

, James Renwick3

1School of Physical and Chemical Sciences, University of Canterbury, Christchurch, New Zealand, 2Gateway Antarctica,
University of Canterbury, Christchurch, New Zealand, 3School of Geography, Victoria University of Wellington, Environment
and Earth Science, Wellington, New Zealand

Abstract  ERA5 reanalysis is used to examine extreme precipitation using a spatially dependent
precipitation threshold applied within a cyclone compositing framework. This is used to account for regional
variation in precipitation generating processes within Southern Hemisphere mid-latitude cyclones across the
cyclone lifecycle. The spatial extent of extreme precipitation is limited to a smaller region around the cyclone
center compared to non-extreme precipitation, though extreme precipitation displays a good spatial correlation
with non-extreme precipitation. Extreme precipitation occurs more often during the deepening phase of the
cyclone before it reaches peak intensity. Precipitation occurrence at the 90th and 98th percentiles reduces to
46% and 30% of the deepening value across the cyclone lifecycle, averaged over the composite. Precipitation
fraction at the 90th and 98th percentile reduces to 80% and 60% of the deepening value. Our methodology
provides a quantitative assessment of precipitation extremes both spatially and temporally, within a cyclone
compositing framework.

Plain Language Summary  Extra-tropical cyclones play a major role in the circulation within the
atmosphere, acting to transfer heat toward the poles. Here we assess the representation of extreme precipitation
within extra-tropical cyclones. By applying a threshold for precipitation that changes with geographic location,
we are able to determine how extreme precipitation varies within a cyclone-centered coordinate system. When
breaking cyclones into lifecycle stages representing deepening, peak intensity and decay, we find that extreme
precipitation occurs most often as the cyclone is developing. The area of the cyclone relevant for extremes
reduces toward the cyclone center as the threshold for determining extreme precipitation increases. Extreme
precipitation weakens at a higher rate as cyclones becomes more intense, highlighting the importance of
extremes in the growth phase of the cyclone.

1.  Introduction

Climate change is experienced by society through a variety of ways, including extreme weather events. Unlike
long term climate trends which seem distant and occur more gradually, extremes are direct and occur in every-
day life. Howe et al. (2014) suggests that people tend to accurately recall and report experiences with extreme
weather, with increasing likelihood based on proximity and magnitude of an event. The impacts extremes have
are numerous. Economic impacts include closure of roads, outages of power grids, water shut-offs, and physical
damage to buildings, bridges, crops and livestock (Jahn, 2015). Environmental impacts include coastal erosion,
changes in water supply and land coverage (Seddon et al., 2016; Seneviratne et al., 2012, 2021). Societal impacts
include food and water availability, loss of life, increasing insurance costs and changes in property values (Bell
et al., 2018; Konapala et al., 2020; Morss et al., 2011; Zscheischler et al., 2018). Extreme weather has intensified
in recent decades, and will continue to have a disproportionately large impact on the environment, society and the
economy (Seneviratne et al., 2021).

© 2023 The Authors.
This is an open access article under
the terms of the Creative Commons
Attribution-NonCommercial License,
which permits use, distribution and
reproduction in any medium, provided the
original work is properly cited and is not
used for commercial purposes.

On a global scale, precipitation extremes are predicted to increase in intensity and frequency as the climate warms
(e.g., Hirsch & Archfield, 2015; Min et al., 2011; Zhang et al., 2007). Work detailed in Kotz et al. (2022) has
recently identified that increases in extreme rainfall reduce economic growth rates. A study by Pendergrass and
Knutti (2018) investigated the uneven nature of precipitation, finding that half the annual precipitation occurs
during the wettest 12 days of the year. When assessing output from CMIP5 climate models, they also found a
shortening of the average number of days needed to reach half the annual precipitation, highlighting the increased
importance of extreme events.

MCERLICH ET AL.

1 of 10

Geophysical Research Letters

10.1029/2023GL104130

Extra-tropical cyclones (hereafter referred to as cyclones) are key components of the atmospheric general circula-
tion due to their ability to transport large quantities of heat, moisture, and momentum. Cyclones are an important
contributor to extreme weather events as their passage is associated with strong winds, precipitation, and temper-
ature changes (Papritz et al., 2014). Studies quantifying cyclone-associated precipitation find that up to 90% of
precipitation  in  the  mid-latitude  storm  tracks  is  associated  with  frontal  systems  and  their  associated  cyclones
(Catto et al., 2012; Hawcroft et al., 2012). Further studies (Catto & Pfahl, 2013; Dowdy & Catto, 2017; Pfahl
& Wernli, 2012; Utsumi et al., 2017) have also shown a high percentage of precipitation extremes are directly
related to cyclones. Dowdy and Catto (2017) show that the conjunction of cyclones, and features such as fronts
and thunderstorms can mean that attribution of precipitation to one feature is ambiguous. However, they also
identify that the combination of cyclones and their associated fronts are the largest contributor to extreme precip-
itation over mid- and high-latitudes across the Southern Hemisphere.

In this study we use a regionally dependent precipitation threshold to classify precipitation extremes relative to
the cyclone centre, based on the intensity of precipitation (see McErlich et al., 2023). Cyclone composites for
both  average  and  extreme  precipitation  are  calculated  using  ERA5  reanalysis  over  the  Southern  Hemisphere.
Composites are then partitioned into different stages of the cyclone lifecycle to assess the spatial and temporal
evolution  of  precipitation  extremes.  The  rate  at  which  extremes  precipitation  changes  throughout  the  cyclone
lifecycle is then quantified.

2.  Data Sets and Methods

2.1.  ERA5

We use output from the ERA5 reanalysis (Hersbach et al., 2020) to identify cyclones over the Southern Hemi-
sphere for the years 1980–2019 inclusive. ERA5 is available on a 0.25° latitude/longitude grid and at an hourly
temporal resolution, which was sampled at a three hourly interval in this study. Previous work (McDonald &
Cairns, 2020; McErlich et al., 2023) shows that ERA5 is consistent with a number of satellite and reanalysis data
sets for determining precipitation. Work by Lavers et al. (2022) evaluating ERA5 precipitation biases globally
found the smallest errors occur over the mid-latitudes in winter relative to station data. The small errors at these
latitudes were attributed to precipitation being produced by extra-tropical cyclones, and that these processes are
well resolved within ERA5.

2.2.  Cyclone Tracking and Compositing Methodology

Work by Crawford and Serreze (2016) introduces and details the mean sea level pressure (MSLP) based cyclone
tracking  algorithm  used  in  this  study,  which  has  also  been  used  in  a  number  of  further  studies  (Crawford
et al., 2020; Crawford & Serreze, 2017; Hell et al., 2020; Koyama et al., 2017). A detailed explanation of the
cyclone tracking algorithm used can be found in Crawford and Serreze (2016), but the main steps are briefly
detailed.

Local minima in the ERA5 MSLP field are used to identify cyclone centers between 1980 and 2019. A radius-based
threshold is used to indicate whether it is a closed low pressure system, and thus can be characterized as a cyclone.
If the average MSLP difference between the identified cyclone center and a 1,000 km radius circle is greater than
7.5 hPa, then the center is retained. A maximum propagation speed of 150 km/hr is used to join related low pres-
sure centers into continuous cyclone tracks. Criteria are also applied to reject systems that have a lifespan shorter
than 24 hr, a track length less than 100 km, or do not spend some part of their lifetime at latitudes south of 30°S.
The location of identified cyclone tracks are in agreement with previous research analyzing Southern hemisphere
cyclone tracks (e.g., Bengtsson et al., 2006; Hodges et al., 2011; Hoskins & Hodges, 2005).

Identified cyclone centers are then used to produce cyclone composites, following methodology similar to Catto
et al. (2010). Data is extracted in a 2,000 km radius centered on each cyclone center. Cyclone composites are
calculated using a radius of 2,000 km, which is commonly used in previous work (e.g., Booth et al., 2018; Field &
Wood, 2007; Field et al., 2008; Naud et al., 2012). Individual composites are then rotated so that the direction of
propagation of the cyclone is chosen to be traveling eastward. Given the zonal westerly winds over the Southern
Ocean many cyclones require little rotation. This step approximately aligns the position of the warm/cold fronts
and the area of warm, moist air associated with them. While not all fronts will be at the same position relative
to the direction of the cyclone, this rotation acts to focus the structure of the composite (Govekar et al., 2011).

MCERLICH ET AL.

2 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

2.3.  Analysis of Cyclone Lifecycle

To better understand changes in precipitation as the cyclone evolves, we partition the cyclones into three distinct
developmental phases. We classify cyclones relative to the time of their peak intensity, which is defined as the
time of maximum difference between the edge pressure and central pressure of the cyclone. The edge pressure
of  the  cyclone  is  determined  using  the  last  closed  isobar  around  the  cyclone  center.  Note  that  in  rare  cases
where a closed cyclone center is not identified, the radius and depth of the cyclone may be underestimated. We
define  three phases to represent periods of deepening, peak intensity and decay within the cyclone. The phase of
peak intensity is defined as 6 hr either side of the time of peak intensity. The deepening phase is defined as meas-
urements between 6 and 18 hr previous to the time of peak intensity. The decay phase is defined as measurements
between 6 and 18 hr after the time of peak intensity.

In order to partition the cyclones into phases of deepening, peak intensity, and decay, a further criterion based
 , scaled by latitude ϕ, was also assessed. Cyclone tracks were kept if the deep-

on the deepening rate

ening rate changed from positive (indicating strengthening) during the deepening phase to negative (indicating
weakening) during the decay phase. Cyclone tracks that pass this criterion are masked to only include data within
the previously defined cyclone phases. Tracks without measurements 18 hr before and after the point of peak
intensity are rejected, causing a minimum cyclone lifespan of 36 hr within the subset of cyclone tracks used in
this analysis. This criterion still meant that over 35,000 cyclones were used in our composites.

2.4.  Identification of Precipitation Extremes Associated With Cyclones

In order to identify regions of the cyclone that correspond to precipitation extremes, we use a methodology intro-
duced in McErlich et al. (2023). This produces regionally dependent thresholds for extreme precipitation which are
then applied to a cyclone compositing framework. First, a gridded spatial map of precipitation wet-day frequency
is produced using a 1 mm/day threshold over the Southern Hemisphere. This threshold is commonly used within
the community (Polade et al., 2014; Schär et al., 2016) and is also used in a number of extreme precipitation
indices as defined by the Expert Team on Climate Change Detection and Indices (ETCCDI; Zhang et al., 2011).

Second,  rainfall  data  from  grid  points  with  the  same  wet-day  frequency  are  grouped  together.  Precipitation
data from these regions is aggregated to produce cumulative distributions of precipitation intensity. McErlich
et  al.  (2023)  establishes  this  methodology  forms  coherent  precipitation  groupings,  even  though  it  connects
spatially disparate regions together. The variability within wet-day frequency regions has also been shown to be
comparable to that within geographic regions.

Third, wet-day frequency regions are identified within the cyclone composites using the geographic grid position
of the cyclone centers, as determined by the tracking algorithm. This allows for precipitation around the cyclone
composite to be compared to the precipitation intensity distributions to assess if it is extreme or not for that grid point.

Finally, precipitation is masked to remove data below the nth percentile value of the precipitation intensity distri-
bution. Because the nth percentile value changes depending on the wet-day frequency, we account for changes in
the underlying processes that generate precipitation.

Setting this threshold to the upper tail of the precipitation distribution determines cyclone composites for the extremes.
Here we assess both the 90th and the 98th percentiles allowing us to examine two different definitions of precipita-
tion extremes. Using a percentile threshold is established within previous literature assessing precipitation extremes
related to cyclones (Catto & Dowdy, 2021; Messmer & Simmonds, 2021). We also mask precipitation by a 1 mm
per day wet-day threshold (Zhang et al., 2011) and 50th percentile value. While not indicative of extremes, these sets
of composites provide data which the extreme composites can be compared with, allowing us to understand unique
features associated with extreme precipitation. We note that the wet-day frequency has a narrower range (see Figure 1;
McErlich et al., 2023) over the Southern Ocean where the concentration of cyclones is the highest. This means there
will be less variability in the extreme precipitation thresholds over the Southern Ocean than for global analysis.

3.  Results

Figure  1  shows  the  occurrence  of  precipitation  for  the  wet-day  precipitation,  50th,  90th,  and  98th  percen-
tile  masked  composites  in  the  cyclone  centered  coordinate  system.  Here  precipitation  occurrence  is  defined,

MCERLICH ET AL.

3 of 10

𝐴𝐴(𝜕𝜕𝜕𝜕𝜕𝜕𝜕𝜕sin(60)sin(𝜙𝜙)) 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

Figure 1.  ERA5 cyclone composites of precipitation occurrence between 1980 and 2019 partitioned into the deepening, peak intensity and decay phases for (a–c)
wet-day precipitation (d–f) 50th percentile masked precipitation (g–i) 90th percentile masked precipitation (k–l) 98th percentile masked precipitation. Black points
indicate maximum occurrence at a given distance from the cyclone center, up to a radius of 1,000 km, to highlight rotation.

MCERLICH ET AL.

4 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

determined as a whole across each masked subset of composites using their respective thresholds. To highlight
the changes in the structure, each set of composites are shown on different color scales. Because of the rotation
applied to the cyclone composites, the top of the composites may not align with north, so cardinal directions are
not used to describe cyclone features.

Figures 1a–1c show precipitation occurrence for wet-day precipitation is greatest during the deepening phase,
with rates up to 100% relative to the cyclone. Occurrence then decreases slightly throughout the cyclone lifecy-
cle. Given the potential for significant diabatic heating/latent heat release during the deepening phase (Binder
et al., 2016; Ludwig et al., 2014; Messmer & Simmonds, 2021; Wernli et al., 2002), this is not an unexpected
result. The spatial structure shows high precipitation occurrence about the cyclone center that extends in a tail
toward the left side of the composite. This matches regions of high precipitation intensity in previous studies
(Field & Wood, 2007; Pfahl & Sprenger, 2016), which have shown a connection between cyclone intensity and
moisture  availability.  Maximum  precipitation  occurrence  at  a  given  distance  from  the  cyclone  center  is  also
plotted out to a radius of 1,000 km, and identifies that this tail rotates clockwise throughout the lifecycle. This
highlights the warm sector described in idealized models, identifying changes in the position of the warm and
cold  fronts  as  the  cyclone  evolves.  Note  that  because  we  examine  cyclones  over  the  Southern  Hemisphere,  a
clockwise rotation is cyclonic.

Looking at the 50th percentile masked composites, Figures 1d–1f similarly shows highest precipitation occur-
rence during the deepening phase, of up to 80%, before decreasing in later lifecycle stages. The spatial region
associated with high occurrences shows a reduced extent from that seen in Figures 1a–1c, with a more pronounced
comma structure in the upper left quadrant of the cyclone. Comparable patterns are observed when looking at
the  90th  percentile  masked  cyclone  composites  for  extreme  precipitation  occurrence  (Figures  1g–1i)  and  the
98th percentile masked composites (Figures 1j–1l). Precipitation occurrence is again greatest during deepening,
before rotating clockwise and decreasing during the peak intensity and decay phases. A further reduction in the
spatial extent of high occurrence regions from Figures 1d–1f is observed, such that the occurrence of precipita-
tion extremes outside the comma is very low. For the 90th percentile precipitation extremes rarely occur within
the drier poleward region of the cyclone; for the 98th percentile precipitation extremes rarely occur outside of  the
comma structure.

To examine extreme precipitation from a different perspective, the fraction of the total precipitation associated
with each threshold is derived in Figure 2. First, the total precipitation accumulation across the cyclone compos-
ite is determined (see Figure S1). Second, the precipitation accumulation associated with each set of masked
composite subsets is determined, using the various precipitation thresholds. Thee precipitation fraction is then
defined as the ratio of precipitation accumulation associated with a given masked composite subset and the total
accumulated precipitation. For the wet-day percentiles, this accumulation is determined using a 1 mm per day
threshold. The nth percentile threshold is used for the 50th, 90th, and 98th percentile masked cyclone composites.
Figure 2 shows precipitation fraction calculated across the wet-day precipitation and 50th, 90th, and 98th percen-
tile masked composites. Note the different colour scales on each row of subplots used to distinguish structure.

Figures 2a–2c show the highest precipitation fraction is concentrated in the comma region of the cyclone compos-
ite and in the warm equatorward region of the cyclone. Precipitation fraction is greatest during the deepening
phase,  then  decreases  and  rotates  clockwise  during  the  peak  intensity  and  decay  phases.  The  area  of  lowest
precipitation fraction occurs in the cold poleward region of the composite, where more of the rainfall is below
the 1 mm wet-day threshold suggesting a region dominated by drizzle. An almost identical pattern is seen for the
50th percentiles masked composites on Figures 2d–2f. These results agree with the spatial pattern of high and low
precipitation seen within previous cyclone compositing work (e.g., Booth et al., 2018; Catto et al., 2012; Field &
Wood, 2007; Naud et al., 2020).

When  looking  at  the  precipitation  fraction  for  the  90th  percentile  masked  composites,  Figures  2g–2i  show  a
decrease compared to the 50th percentile threshold as would be expected. The fraction of the total precipitation
linked to events above this threshold are still highest during the deepening phase, but the greatest precipitation
fraction (almost 80%) is lower compared to Figures 2a and 2d. That up to 80% of precipitation is associated with
the top 10% of the precipitation distribution highlights the importance of cyclones for extreme precipitation in
general. Plotted lines of maximum precipitation fraction show a clockwise rotation throughout the cyclone evolu-
tion, as the precipitation fraction weakens. When applying the strictest threshold and masking by the 98th percen-
tile  value,  Figures  2j–2l  show  a  further  decrease  in  precipitation  fraction.  Though,  the  greatest  precipitation

MCERLICH ET AL.

5 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

Figure 2.  ERA5 cyclone composites of precipitation fraction between 1980 and 2019 partitioned into the deepening, peak intensity and decay phases for (a–c) wet-day
precipitation (d–f) 50th percentile masked precipitation (g–i) 90th percentile masked precipitation (k–l) 98th percentile masked precipitation. Black points indicate
maximum occurrence at a given distance from the cyclone center, up to a radius of 1,000 km, to highlight rotation.

MCERLICH ET AL.

6 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

Figure 3.  (a) Pairwise Pearson correlation coefficients for precipitation occurrence across the cyclone lifecycle (b) same
as (a) but for precipitation fraction (c) Precipitation occurrence averages across the cyclone lifecycle (d) same as (c) but
for precipitation fraction. The bracketed percentages for (c and d) indicate precipitation averages as a proportion of the
corresponding deepening phase value.

fraction  is  close  to  50%  and  occurs  during  the  deepening  phase,  before  a  reduction  and  clockwise  rotation  is
seen similar to Figures 2g–2i. Precipitation fraction shows the smallest spatial extent, being most concentrated
within  the comma region of near the cyclone center.

Results observed for the precipitation occurrence and fraction show similarities in structure between the masked
cyclone  composites.  Figures  3a  and  3b  show  the  Pearson  correlation  coefficients  for  precipitation  across
the  cyclone  composites  as  shown  on  Figures  1  and  2.  Correlation  is  calculated  pairwise  between  each  set  of
cyclone  composites, spatially across the composite. For example, the first row of Figure 3a correlates precip-
itation occurrence for the cyclone composites for all wet days (Figures 1a–1c) with those masked by the 50th
percentile value (Figures 1d–1f). This is done individually for each phase of the cyclone lifecycle. Figures 1 and 2
also show that precipitation is greatest during the deepening phase, and then weakens as the cyclone evolves,
which agrees with previous work (Booth et al., 2018). However, the rate at which this weakening happens differs
between the wet-day precipitation, 50th, 90th and 98th masked cyclone composites. To investigate the similarities
between the cyclone composites and to quantify this weakening, the average value for each subset of composites
is  shown  across  the  cyclone  lifecycle  on  Figures  3c  and  3d.  The  bracketed  percentages  indicate  precipitation
averages as a proportion of the corresponding deepening phase value.

Pairwise  spatial  correlations  for  precipitation  occurrence  (Figure  3a)  show  strong  agreement  between  each
masked composites subset. Correlation is strongest during the deepening phase in all cases. Correlation is lowest
between the wet-day precipitation and 90/98th percentile masked composites, but still strong within the deep-
ening phase. When comparing the wet-day precipitation/50th percentiles and 90th/98th percentiles, the spatial
correlation remains consistently high across the cyclone lifecycle. When looking at the precipitation fraction, the
pairwise correlation shows a similar pattern to that observed for the precipitation occurrence.

Looking at the average precipitation occurrence across the cyclone (Figure 3c), not only do the extremes have
lower occurrence that the non-extreme precipitation, but drop off significantly faster. The wet-day precipitation

MCERLICH ET AL.

7 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

and 50th percentile masked composites decrease to 90% and 81% of the deepening value during the decay phase,
respectively. The 90th and 98th percentile composites decrease to 46% and 30% of the deepening value during
the decay phase, respectively. This indicates as you increase the threshold for determining extremes, they will
be disproportionately experienced during the deepening phase, as the occurrence weakens greatly by the decay
phase. Averages for the precipitation fraction (Figure 3d) display a similar pattern. The 90th and 98th percentile
masked composites decrease to 80% and 65% of the deepening value, respectively, while the wet-day precipita-
tion and 50th percentile masked composites decrease negligibly. This highlights that as you increase the threshold
for the extremes the deepening phase becomes more important, as a lower proportion of the total precipitation
experienced in future cyclone phases can be defined as extreme.

4.  Discussion and Conclusion

Using a spatially dependent threshold for precipitation, we have developed a simple methodology to assess the
contribution  to  accumulation  and  the  occurrence  of  precipitation  extremes  by  masking  data  within  a  cyclone
compositing  framework.  This  methodology  is  based  on  grouping  regions  of  similar  precipitation  frequency
together, which have been shown to be influenced by the same underlying dynamic and thermodynamic precip-
itation processes (McErlich et al., 2023). This averages regions of each cyclone that are determined as extreme,
with all lower precipitation measurements being masked out. Therefore, it is unlikely that results shown are repre-
sentative of a single cyclone, but instead present an aggregated picture of the behavior of precipitation extremes.

While  some  past  studies  investigate  precipitation  extremes  and  how  they  connect  to  cyclones  (e.g.,  Catto  &
Dowdy,  2021;  Messmer  &  Simmonds,  2021;  Pepler  &  Dowdy,  2020;  Pfahl  &  Wernli,  2012),  they  tend  to
assess precipitation spatially rather than using a cyclone composite framework. The exception being Pepler and
Dowdy (2020), who created cyclone composites over a region over the Australian East Coast for times of maxi-
mum precipitation within tracks. This study is thus the first assessment of extremes in a cyclone composite frame-
work across the Southern hemisphere mid-latitudes, which examines extremes relative to the cyclone lifecycle.

Here we see that the greatest precipitation occurrence and fraction of total precipitation occur before the cyclone
reaches its peak intensity. The precipitation accumulation (Figure S1) is also greatest during the deepening phase,
meaning precipitation extremes will be experienced most acutely during the deepening phase. For both the 90th
and 98th percentile masked composites, the precipitation occurrence and fraction is greatest during the deepening
phase and then decays slightly as the cyclone evolves. While studies have shown support for the concept that the
release of latent heating associated with precipitation leads to the intensification of a cyclone (Binder et al., 2016;
Ludwig et al., 2014; Messmer & Simmonds, 2021; Wernli et al., 2002), Booth et al. (2018) found that the lag
between peak precipitation and peak cyclone intensity was a result of the amount of precipitable water in the
cyclone environment.

Figures 3c and 3d show that precipitation occurrence and precipitation fraction weakens at a faster rate as you
increase from the 90th to 98th percentile of precipitation. This suggests a larger diabatic heating and subsequent
intensification of the cyclone from extreme precipitation events. Figures 3c and 3d also shows that the precipi-
tation occurrence shows a larger change from the deepening to the decay phase than the precipitation fraction at
every extreme threshold. This suggests that during the decay phase a larger amount of rainfall is associated with
a smaller number of extreme events.

Looking at the spatial pattern of precipitation within cyclone composites, Figures 1 and 2 show that as you apply
a stricter threshold to mask precipitation there is a reduction in the spatial extent of both high precipitation occur-
rence and fraction. As you move toward the extremes, precipitation is more concentrated toward the center of the
cyclone within the comma region linked to the warm conveyor belt. Catto and Pfahl (2013) have shown that fronts
are important for extreme precipitation. Results seen on Figures 1 and 2 are likely related to frontal regions within
the cyclone, which constrain where extreme precipitation occurs.

Figures 3a and 3b show that for the precipitation occurrence and fraction, the 90th and 98th percentile masked
composites show strong spatial correlation across all states of the cyclone lifecycle. The wet-day precipitation and
50th and 90th/98th percentile masked cyclone composites shows strong agreement for precipitation occurrence
and fraction during the deepening and peak intensity phases, but weaker agreement during the decay phase. These
correlations show that the spatial regions of the cyclone where precipitation extremes are important remain simi-
lar across the cyclone lifecycle, suggesting that knowing the median precipitation pattern could provide insight

MCERLICH ET AL.

8 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseAcknowledgments
We would like to acknowledge funding
from the Ministry of Business, Innovation
and Employment (MBIE), New Zealand,
through the Whakahura project (Grant
RTVU1906). Open access publishing
facilitated by University of Canterbury,
as part of the Wiley - University of
Canterbury agreement via the Council of
Australian University Librarians.

Geophysical Research Letters

10.1029/2023GL104130

into the upper tail of the distributions, at least for the precipitation occurrence and fraction. This is consistent with
results seen in McErlich et al. (2023), that determined a strong correlation between wet-day frequency and many
precipitation-related extreme climate indices.

This work has determined the spatial structure of extreme precipitation relative to cyclone centers, and provided
a quantification of how these extremes change as the cyclone evolves. However, the underlying processes that
determine precipitation have not been assessed to provide a physical justification for results seen in this work.
McErlich  et  al.  (2023)  has  shown  that  vertical  velocity  and  convective  available  potential  energy  are  impor-
tant  drivers  of  global  precipitation  and  that  precipitation  is  determined,  in  part,  by  the  occurrence  of  these
precipitation-generating processes. Pepler and Dowdy (2020) determine that deep moist convective precipitation
related to convective available potential energy occurs preferentially in the warm sector of cyclones. Their work
also shows that convective precipitation is important in weaker cyclones which lack the deep vertical structure
more commonly associated with extreme impacts. Future work will examine these processes to determine how
they influence the behavior of precipitation and precipitation extremes in cyclones through their lifecycle.

Data Availability Statement

The ERA5 reanalysis products  were  obtained  from  the Copernicus  Climate  Data  Store  (C3S, 2017)  available
at  https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels.  Data  used  to  visualise  the
figures is available at https://doi.org/10.5281/zenodo.7787118, publishsed on Zenodo (McErlich, 2023).

References
Bell, J. E., Brown, C. L., Conlon, K., Herring, S., Kunkel, K. E., Lawrimore, J., et al. (2018). Changes in extreme events and the potential impacts
on human health. Journal of the Air & Waste Management Association, 68(4), 265–287. https://doi.org/10.1080/10962247.2017.1401017
Bengtsson,  L.,  Hodges,  K.  I.,  &  Roeckner,  E.  (2006).  Storm  tracks  and  climate  change.  Journal  of  Climate,  19(15),  3518–3543.  https://doi.

org/10.1175/JCLI3815.1

Binder, H., Boettcher, M., Joos, H., & Wernli, H. (2016). The role of warm conveyor belts for the intensification of extratropical cyclones in

Northern Hemisphere winter. Journal of the Atmospheric Sciences, 73(10), 3997–4020. https://doi.org/10.1175/JAS-D-15-0302.1

Booth,  J.  F.,  Naud,  C.  M.,  &  Jeyaratnam,  J.  (2018).  Extratropical  cyclone  precipitation  life  cycles:  A  satellite-based  analysis.  Geophysical

Research Letters, 45(16), 8647–8654. https://doi.org/10.1029/2018GL078977

C3S. (2017). ERA5: Fifth generation of ECMWF atmospheric reanalyses of the global climate [Dataset]. C3S. Retrieved from https://cds.climate.

copernicus.eu/cdsapp#!/home

Catto, J. L., & Dowdy, A. (2021). Understanding compound hazards from a weather system perspective. Weather and Climate Extremes, 32,

100313. https://doi.org/10.1016/j.wace.2021.100313

Catto, J. L., Jakob, C., Berry, G., & Nicholls, N. (2012). Relating global precipitation to atmospheric fronts. Geophysical Research Letters, 39(10),

L10805. https://doi.org/10.1029/2012GL051736

Catto, J. L., & Pfahl, S. (2013). The importance of fronts for extreme precipitation. Journal of Geophysical Research: Atmospheres, 118(19),

10791–10801. https://doi.org/10.1002/jgrd.50852

Catto, J. L., Shaffrey, L. C., & Hodges, K. I. (2010). Can climate models capture the structure of extratropical cyclones? Journal of Climate, 23(7),

1621–1635. https://doi.org/10.1175/2009JCLI3318.1

Crawford, A. D., Alley, K. E., Cooke, A. M., & Serreze, M. C. (2020). Synoptic climatology of rain-on-snow events in Alaska. Monthly Weather

Review, 148(3), 1275–1295. https://doi.org/10.1175/MWR-D-19-0311.1

Crawford, A. D., & Serreze, M. C. (2016). Does the summer arctic frontal zone influence Arctic Ocean cyclone activity? Journal of Climate,

29(13), 4977–4993. https://doi.org/10.1175/JCLI-D-15-0755.1

Crawford, A. D., & Serreze, M. C. (2017). Projected changes in the Arctic frontal zone and summer Arctic cyclone activity in the CESM large

ensemble. Journal of Climate, 30(24), 9847–9869. https://doi.org/10.1175/JCLI-D-17-0296.1

Dowdy, A. J., & Catto, J. L. (2017). Extreme weather caused by concurrent cyclone, front and thunderstorm occurrences. Scientific Reports, 7(1),

40359. https://doi.org/10.1038/srep40359

Field, P. R., Gettelman, A., Neale, R. B., Wood, R., Rasch, P. J., & Morrison, H. (2008). Midlatitude cyclone compositing to constrain climate

model behavior using satellite observations. Journal of Climate, 21(22), 5887–5903. https://doi.org/10.1175/2008JCLI2235.1

Field,  P.  R.,  &  Wood,  R.  (2007).  Precipitation  and  cloud  structure  in  midlatitude  cyclones.  Journal  of  Climate,  20(2),  233–254.

https://doi.org/10.1175/JCLI3998.1

Govekar, P. D., Jakob, C., Reeder, M. J., & Haynes, J. (2011). The three-dimensional distribution of clouds around Southern Hemisphere extrat-

ropical cyclones. Geophysical Research Letters, 38(21), L21805. https://doi.org/10.1029/2011GL049091

Hawcroft,  M.,  Shaffrey,  L.,  Hodges,  K.,  &  Dacre,  H.  (2012).  How  much  Northern  Hemisphere  precipitation  is  associated  with  extratropical

cyclones? Geophysical Research Letters, 39(24), 24809. https://doi.org/10.1029/2012GL053866

Hell, M. C., Gille, S. T., Cornuelle, B. D., Miller, A. J., Bromirski, P. D., & Crawford, A. D. (2020). Estimating Southern Ocean storm positions

with seismic observations. Journal of Geophysical Research: Oceans, 125(4), e2019JC015898. https://doi.org/10.1029/2019JC015898

Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., Muñoz-Sabater, J., et al. (2020). The ERA5 global reanalysis. Quarterly Journal

of the Royal Meteorological Society, 146(730), 1999–2049. https://doi.org/10.1002/qj.3803

Hirsch, R. M., & Archfield, S. A. (2015). Not higher but more often. Nature Climate Change, 5(3), 198–199. https://doi.org/10.1038/nclimate2551
Hodges, K. I., Lee, R. W., & Bengtsson, L. (2011). A comparison of extratropical cyclones in recent reanalyses ERA-Interim, NASA MERRA,

NCEP CFSR, and JRA-25. Journal of Climate, 24(18), 4888–4906. https://doi.org/10.1175/2011JCLI4097.1

Hoskins, B. J., & Hodges, K. I. (2005). A new perspective on Southern Hemisphere storm tracks. Journal of Climate, 18(20), 4108–4129. https://

doi.org/10.1175/JCLI3570.1

MCERLICH ET AL.

9 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2023GL104130

Howe, P. D., Boudet, H., Leiserowitz, A., & Maibach, E. W. (2014). Mapping the shadow of experience of extreme weather events. Climatic

Change, 127(2), 381–389. https://doi.org/10.1007/s10584-014-1253-6

Jahn, M. (2015). Economics of extreme weather events: Terminology and regional impact models. Weather and Climate Extremes, 10, 29–39.

https://doi.org/10.1016/j.wace.2015.08.005

Konapala, G., Mishra, A. K., Wada, Y., & Mann, M. E. (2020). Climate change will affect global water availability through compounding changes
in seasonal precipitation and evaporation [Journal Article]. Nature Communications, 11(1), 3044. https://doi.org/10.1038/s41467-020-16757-w
Kotz, M., Levermann, A., & Wenz, L. (2022). The effect of rainfall changes on economic production. Nature, 601(7892), 223–227. https://doi.

org/10.1038/s41586-021-04283-8

Koyama, T., Stroeve, J., Cassano, J., & Crawford, A. (2017). Sea ice loss and Arctic cyclone activity from 1979 to 2014. Journal of Climate,

30(12), 4735–4754. https://doi.org/10.1175/JCLI-D-16-0542.1

Lavers, D. A., Simmons, A., Vamborg, F., & Rodwell, M. J. (2022). An evaluation of ERA5 precipitation for climate monitoring. Quarterly

Journal of the Royal Meteorological Society, 148(748), 3152–3165. https://doi.org/10.1002/qj.4351

Ludwig, P., Pinto, J. G., Reyers, M., & Gray, S. L. (2014). The role of anomalous SST and surface fluxes over the southeastern North Atlantic in
the explosive development of windstorm Xynthia. Quarterly Journal of the Royal Meteorological Society, 140(682), 1729–1741. https://doi.
org/10.1002/qj.2253

McDonald, A. J., & Cairns, L. H. (2020). A new method to evaluate reanalyses using synoptic patterns: An example application in the Ross Sea/

Ross Ice Shelf Region. Earth and Space Science, 7(1), e2019EA000794. https://doi.org/10.1029/2019EA000794

McErlich,  C.  (2023).  ERA5  cyclone  extremes  data:  March  20,  2023  release  (Version  1.0)  [Dataset].  Zenodo.  https://doi.org/10.5281/

zenodo.7787119

McErlich, C., McDonald, A., Schuddeboom, A., Vishwanathan, G., Renwick, J., & Rana, S. (2023). Positive correlation between wet-day frequency

and intensity linked to universal precipitation drivers. Nature Geoscience, 16(5), 410–415. https://doi.org/10.1038/s41561-023-01177-4

Messmer,  M.,  &  Simmonds,  I.  (2021).  Global  analysis  of  cyclone-induced  compound  precipitation  and  wind  extreme  events.  Weather  and

Climate Extremes, 32, 100324. https://doi.org/10.1016/j.wace.2021.100324

Min, S.-K., Zhang, X., Zwiers, F. W., & Hegerl, G. C. (2011). Human contribution to more-intense precipitation extremes. Nature, 470(7334),

378–381. https://doi.org/10.1038/nature09763

Morss,  R.  E.,  Wilhelmi,  O.  V.,  Meehl,  G.  A.,  &  Dilling,  L.  (2011).  Improving  societal  outcomes  of  extreme  weather  in  a  changing  climate:
An integrated perspective. Annual Review of Environment and Resources, 36, 1–25. https://doi.org/10.1146/annurev-environ-060809-100145
Naud, C. M., Jeyaratnam, J., Booth, J. F., Zhao, M., & Gettelman, A. (2020). Evaluation of modeled precipitation in oceanic extratropical cyclones

using IMERG. Journal of Climate, 33(1), 95–113. https://doi.org/10.1175/JCLI-D-19-0369.1

Naud, C. M., Posselt, D. J., & van den Heever, S. C. (2012). Observational analysis of cloud and precipitation in midlatitude cyclones: Northern

versus Southern Hemisphere warm fronts. Journal of Climate, 25(14), 5135–5151. https://doi.org/10.1175/JCLI-D-11-00569.1

Papritz, L., Pfahl, S., Rudeva, I., Simmonds, I., Sodemann, H., & Wernli, H. (2014). The role of extratropical cyclones and fronts for southern

ocean freshwater fluxes. Journal of Climate, 27(16), 6205–6224. https://doi.org/10.1175/JCLI-D-13-00409.1

Pendergrass, A. G., & Knutti, R. (2018). The uneven nature of daily precipitation and its change. Geophysical Research Letters, 45(21), 11980–

11988. https://doi.org/10.1029/2018GL080298

Pepler,  A.,  & Dowdy, A.  (2020). A three-dimensional perspective on  extratropical  cyclone impacts. Journal of Climate, 33(13), 5635–5649.

https://doi.org/10.1175/JCLI-D-19-0445.1

Pfahl, S., & Sprenger, M. (2016). On the relationship between extratropical cyclone precipitation and intensity. Geophysical Research Letters,

43(4), 1752–1758. https://doi.org/10.1002/2016GL068018

Pfahl, S., & Wernli, H. (2012). Quantifying the relevance of cyclones for precipitation extremes. Journal of Climate, 25(19), 6770–6780. https://

doi.org/10.1175/JCLI-D-11-00705.1

Polade, S. D., Pierce, D. W., Cayan, D. R., Gershunov, A., & Dettinger, M. D. (2014). The key role of dry days in changing regional climate and

precipitation regimes. Scientific Reports, 4(1), 4364. https://doi.org/10.1038/srep04364

Schär, C., Ban, N., Fischer, E. M., Rajczak, J., Schmidli, J., Frei, C., et al. (2016). Percentile indices for assessing changes in heavy precipitation

events. Climatic Change, 137(1), 201–216. https://doi.org/10.1007/s10584-016-1669-2

Seddon, A. W. R., Macias-Fauria, M., Long, P. R., Benz, D., & Willis, K. J. (2016). Sensitivity of global terrestrial ecosystems to climate varia-

bility. Nature, 531(7593), 229–232. https://doi.org/10.1038/nature16986

Seneviratne, S., Nicholls, N., Easterling, D., Goodess, C., Kanae, J. K., Luo, Y., et al. (2012). In C. Field, et al. (Eds.), Changes in climate extremes

and their impacts on the natural physical environment. Cambridge University Press.

Seneviratne, S., Zhang, X., Adnan, M., Badi, W., Dereczynsk, C., Luca, A. D., et al. (2021). In V. Masson-Delmotte, et al. (Eds.), Weather and

climate extreme events in a changing climate. Cambridge University Press.

Utsumi, N., Kim, H., Kanae, S., & Oki, T. (2017). Relative contributions of weather systems to mean and extreme global precipitation. Journal

of Geophysical Research: Atmospheres, 122(1), 152–167. https://doi.org/10.1002/2016JD025222

Wernli, H., Dirren, S., Liniger, M. A., & Zillig, M. (2002). Dynamical aspects of the life cycle of the winter storm “Lothar” (24–26 December

1999). Quarterly Journal of the Royal Meteorological Society, 128(580), 405–429. https://doi.org/10.1256/003590002321042036

Zhang, X., Alexander, L., Hegerl, G. C., Jones, P., Tank, A. K., Peterson, T. C., et al. (2011). Indices for monitoring changes in extremes based on

daily temperature and precipitation data. WIREs Climate Change, 2(6), 851–870. https://doi.org/10.1002/wcc.147

Zhang, X., Zwiers, F. W., Hegerl, G. C., Lambert, F. H., Gillett, N. P., Solomon, S., et al. (2007). Detection of human influence on twentieth-century

precipitation trends. Nature, 448(7152), 461–465. https://doi.org/10.1038/nature06025

Zscheischler, J., Westra, S., van den Hurk, B. J. J. M., Seneviratne, S. I., Ward, P. J., Pitman, A., et al. (2018). Future climate risk from compound

events. Nature Climate Change, 8(6), 469–477. https://doi.org/10.1038/s41558-018-0156-3

MCERLICH ET AL.

10 of 10

 19448007, 2023, 17, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023GL104130 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License