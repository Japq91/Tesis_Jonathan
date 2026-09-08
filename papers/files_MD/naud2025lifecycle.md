RESEARCH LETTER
10.1029/2025GL115153

Key Points:
• A new method for identifying

extratropical cyclone lifecycle‐types
(occluded vs. non‐occluded) is applied
to connect them to precipitation
• Occluded extratropical cyclones

produce more precipitation than non‐
occluded ones because they are
collectively more intense

• A unique forcing for ascent allows

more efficient precipitation production
in occluded than in non‐occluded cy-
clones of similar intensity

Supporting Information:

Supporting Information may be found in
the online version of this article.

Correspondence to:

C. M. Naud,
cn2140@columbia.edu

Citation:

Naud, C. M., Martin, J. E., Ghosh, P.,
Elsaesser, G. S., Booth, J. F., & Posselt, D.
J. (2025). Lifecycle‐type matters for
extratropical cyclone precipitation
production. Geophysical Research Letters,
52, e2025GL115153. https://doi.org/10.
1029/2025GL115153

Received 28 JAN 2025
Accepted 7 APR 2025

© 2025. The Author(s).
This is an open access article under the
terms of the Creative Commons
Attribution‐NonCommercial‐NoDerivs
License, which permits use and
distribution in any medium, provided the
original work is properly cited, the use is
non‐commercial and no modifications or
adaptations are made.

NAUD ET AL.

Lifecycle‐Type Matters for Extratropical Cyclone
Precipitation Production
Catherine M. Naud1
James F. Booth3

, and Derek J. Posselt4

, Jonathan E. Martin2

, Poushali Ghosh2

, Gregory S. Elsaesser1

,

1Applied Physics and Applied Mathematics, Columbia University/NASA‐GISS, New York, NY, USA, 2Atmospheric and
Oceanic Sciences, University of Wisconsin‐Madison, Madison, WI, USA, 3Department of Earth and Atmospheric Sciences,
City College of New York, New York, NY, USA, 4Jet Propulsion Laboratory, California Institute of Technology, Pasadena,
CA, USA

Abstract In the midlatitudes, extratropical cyclones produce the majority of winter precipitation.
Precipitation rates and accumulation depend strongly on both the cyclone intensity and the environmental
moisture amount. Using 5 years of the Integrated Multi‐satellitE Retrievals for Global Precipitation
Measurement (IMERG) product, cyclone‐centered composites of surface precipitation rates are compared
between cyclones that occlude and those that do not. Occluding cyclones produce greater surface precipitation
because they tend to be more intense. When the non‐occluding cyclones are selected such that they collectively
have similar intensity and moisture amount distributions as the occluding cyclones, precipitation rates at peak
intensity are still larger for occluding cyclones. This is because a particular type of forced, frontal‐scale, ascent
in the occluded thermal ridge, unique to occluded cyclones by virtue of their thermal structure, favors more
precipitation. The results demonstrate that life‐cycle type (i.e., achieving occlusion vs. not) matters for
precipitation production in extratropical cyclones.

Plain Language Summary The weather in the midlatitudes is driven by extratropical cyclones and
these storms produce most of the winter precipitation in the northern hemisphere. Both the intensity of the
cyclones and the amount of moisture available to them determine how much precipitation they will produce.
However, using satellite observations of precipitation averaged in cyclones, it is discovered that the lifecycle‐
type and associated structural evolution of the cyclones also impacts the precipitation production. Cyclones that
undergo occlusion are found to be associated with greater precipitation production than cyclones that do not
occlude when the comparison is controlled for similar cyclone intensity and moisture amount. This is because
the occluded cyclones are characterized by additional forcing for ascent that boosts precipitation production at
the frontal scale. Therefore lifecycle type matters for the amount of precipitation cyclones produce.

1. Introduction

Extratropical cyclones are the main weather features that provide most of the precipitation in the midlatitudes
(30–60°N/S), up to 80% in the northern hemisphere winter (Catto et al., 2012; Hawcroft et al., 2012). The pre-
cipitation amount produced within an extratropical cyclone depends mostly on the cyclone's intensity and the
amount of environmental moisture available to it (Field & Wood, 2007; Pfahl & Sprenger, 2016; Sinclair &
Catto, 2023). As a result, during its lifecycle, an extratropical cyclone will produce varying amounts of pre-
cipitation, with larger amounts earlier in its history when it is actively intensifying than later in its life. In fact,
precipitation production maximizes before peak cyclone intensity (Bengtsson et al., 2009; Michaelis et al., 2017;
Rudeva & Gulev, 2011). A possible explanation for this behavior is that the latent heat release associated with
precipitation production also intensifies the cyclone, though it should be noted that the lag between the two
maxima (in precipitation production vs. intensity) has been found to be small (Booth et al., 2018; Hawcroft
et al., 2017). Booth et al. (2018) found that the time lag is in fact caused by greater amounts of moisture available
to the cyclones earlier in their development and intensification phase, as cyclones tend to propagate poleward,
towards drier latitudes. But focusing more specifically on the warm conveyor belt region of cyclones, Heitmann
et al. (2024) find that the ascent strength maximizes at the time of maximum deepening rate, causing greater
precipitation rates prior to the time of maximum intensity. These studies all indicate that precipitation production
peaks prior to reaching peak intensity. However, another potentially important variable that has not been
examined in these previous studies is whether the cyclones are occluded or not, an example of what we hereafter

1 of 9

Geophysical Research Letters

10.1029/2025GL115153

refer to as cyclone lifecycle‐type (Another such discrimination might be made for the Shapiro‐Keyser (1990)
cyclone lifecycle type).

Occlusions occur when the cold front encroaches upon and subsequently ascends the warm frontal surface
(Stoelinga et al., 2002), producing a 3D wedge of warm and moist air aloft and poleward of the warm front known
as the trough of warm air aloft (TROWAL; Crocker et al., 1947; Penner, 1955). The TROWAL manifests as a 3D
thermal ridge, connecting the sea‐level pressure (SLP) minimum to the peak of the warm sector, that is, the
intersection between surface cold, warm and occluded fronts (J. E. Martin, 1998a, 1998b, 1999a, 1999b; D.
Schultz and Vaughan, 2011 and references therein). The length of the associated thermal ridge increases as the
occluded cyclone progresses towards eventual decay. More specifically, Keyser et al. (1992) showed that Qs, the
along‐isentrope component of the Q‐vector (Hoskins et al., 1978), describes the rotation of ∇θ by the geostrophic
|∇θ|). Subsequently, J. Mar-
wind and does not contribute to traditional geostrophic frontogenesis (i.e.,

d
dtgeo

tin (1999b) showed that contributions to this rotation are made by both geostrophic vorticity and geostrophic
deformation. The vorticity contribution is exactly half of the Sutcliffe (1947) forcing for ascent, positive vorticity
advection by the thermal wind. He further showed that the characteristic lengthening of the occluded thermal
ridge is forced by non‐frontogenetical geostrophic deformation that, mobilized by the presence of a thermal ridge,
differentially rotates the baroclinic zones that straddle the thermal ridge. In a substantial portion of the occluded
sector, the quasi‐geostrophic (QG) vertical motion ω is attributable to this specific process, which operates
exclusively in occluded cyclones. As a result, cloud amount and precipitation are maximized in the TROWAL,
not along the surface occluded front (Grim et al., 2007; Han et al., 2007; J. Martin, 1998b; Naud et al., 2024).
Therefore, occluded cyclones can produce large amounts of precipitation, and when over land cause crippling
snow accumulations (J. E. Martin, 1998a, 1998b, 1999a, 1999b; D. M. Schultz and Mass, 1993).

Despite the importance of the presence of a thermal ridge for the overall cloud and precipitation produced in
occluded cyclones (Naud et al., 2024), it is not presently known whether the lifecycle‐type (occluding vs. non
occluding cyclones) matters for precipitation production in extratropical cyclones on average. To explore this
question,
the Integrated Multi‐satellitE Retrievals for Global Precipitation Measurement (IMERG; Huff-
man, 2020; Huffman et al., 2023) surface precipitation product and a database of cyclone tracks are combined to
explore differences in precipitation production in cyclones that occlude as compared with those that do not.

2. Data Sets and Methodology

To conduct the analysis, we use a database of extratropical cyclones and focus on a 5‐year period (2014–2018).
We consider here only northern hemisphere cyclones during the winter months (December, January, February).
The database is described below, along with the precipitation data, the methodology used to pair cyclones and
precipitation, and finally the reanalysis data used to help characterize the cyclones.

2.1. Extratropical Cyclones Selection and Subsetting

We use a publicly available database of extratropical cyclones (Naud et al., 2023) that provides the location of
cyclone centers and their corresponding minima in sea level pressure (SLP) every 6 hr from first to last detection
(hereafter referred to as a track). The algorithm of Bauer and Del Genio (2006) was used for the tracking, with
ERA‐interim sea level pressure fields as input. Neu et al. (2013) used the same reanalysis for their tracking
intercomparison exercise and deemed the resolution adequate for cyclone identifications. A new version of the
database using the more recent ERA5 reanalysis is in preparation but was not ready at the time of this analysis.
Each cyclone track is assessed to establish whether the cyclone was occluded at some point in time. Occlusion
assessment was performed using the algorithm described in Naud et al. (2023), where the identification relies on
the presence of an occluded thermal ridge. A quantitative diagnostic of this feature is computed by calculating the
divergence of the unit vector of the 1,000–500 hPa thickness gradient near the cyclone center as the system
progresses in time through its lifecycle (with convergence indicating an occluded state). We separate the cyclone
tracks that are identified as being occluded at some point in time (“Occluded Cyclones”) from those that never are
(“Non‐occluded Cyclones”).

For each track in each category, we also mark the time at which the cyclone reaches its peak intensity, defined
here as the time when the cyclone reaches its minimum in central SLP. This is used to ensure the cyclones are at a
similar stage in their lifecycle when comparing occluded to non‐occluded cyclones. While peak intensity can be

NAUD ET AL.

2 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

defined with other metrics (e.g., wind or vorticity), here we only need to ensure that the definition is consistent for
both populations. Although some cyclones might be identified as occluded only after the time of peak intensity,
they are still included in the “occluded cyclones” group. For the 2014–2018 time period, a total of 1,341 cyclones
at peak intensity were identified, 162 of which occluded (i.e., about 12% of the entire cyclone population). By
design, the occlusion identification method is conservative, implying that some cyclones categorized as non‐
occluded might in fact occlude at some point; however, the occlusion might be short‐lived or the detection
signal weak.

2.2. Precipitation Data

For surface precipitation rates, we use the Integrated Multi‐satellitE Retrievals for Global Precipitation Mea-
surement (GPM) mission (IMERG; Huffman, 2020; Huffman et al., 2023) version 7 product. This product
provides surface precipitation rates every 30 min on a 0.1° × 0.1° grid using passive microwave rainfall and
infrared data from a constellation of satellites. These different data sets are intercalibrated using the GPM core
observatory radiometer data. The “Final Run” product is further calibrated using monthly mean gauge data. For
each cyclone considered in our analysis, we collect the IMERG data in a 6‐hr‐long time window centered on the
time of cyclone identification (i.e., we aggregate the prior and post six 30‐min IMERG time steps). To pair
precipitation and cyclones, we consider a circular region of 1,500 km radius around the cyclone point of minimum
SLP. The radius was chosen as a compromise between ensuring most of the warm and cold frontal precipitation is
included (fronts can be thousands of kilometers in length and pairing is not trivial, c f. Catto et al., 2012 or
Rüdisühli et al., 2020), while avoiding including neighboring precipitating systems as much as possible. We
retain only IMERG grid cells that are within 1,500 km of each cyclone center, and then project the grid cells onto a
rectangular grid centered on the cyclone SLP minimum point (with cell projection locations based on the distance
an IMERG cell is from the cyclone center). The rectangular grid has a domain of ±1,500 km in the meridional and
zonal directions, and 400 km spatial resolution. The IMERG data is averaged in each 400 km cell, from its native
resolution. This regridding procedure is fully described in Naud et al. (2018).

2.3. Cyclone Properties

For each cyclone at peak intensity in the two categories (occluded vs. non‐occluded), we collect coincident
Modern Era Retrospective Analysis for Research and Applications version 2 (MERRA‐2; Gelaro et al., 2017)
500 hPa upward vertical velocity ω (negative where ascending) and precipitable water (PW). We project these
two fields onto a cyclone‐centered grid following the approach for IMERG precipitation data projection (see
above). Additionally, we calculate the mean PW and mean upward vertical velocity (i.e., the average only in-
cludes upward velocities) within a 1,500 km radius centered on the SLP minimum. These two numbers char-
acterize the environmental moisture and the ascent strength of the cyclones which are both important for
precipitation production. To better characterize cyclone intensity, we include calculations of the mean MERRA‐2
surface wind speed in the same circular region. To analyze the thermal structure of the cyclones, we also collect
the 700 hPa equivalent potential temperature using MERRA‐2 temperature and specific humidity fields, and use
the same regridding routine to map these fields to the cyclones.

3. Mean Precipitation Rates in the Northern Hemisphere Winter

Before we examine precipitation within the cyclones, we first examine where and to what extent cyclones
contribute to northern hemisphere winter precipitation. For this we first average IMERG DJF precipitation rates at
their native resolution for 2014–2018 in all conditions (Figure 1a). The 5‐year mean precipitation is clearly
greatest in the storm track regions of the north Atlantic and Pacific as expected (cf. Hawcroft et al., 2012). Next,
we collect IMERG precipitation rates accumulated over 6 hr centered on the times of cyclone identification (00,
06, 12, 18 UT), and compute a conditional average, where we only consider the rainfall reported within the
identified cyclone of radius 1,500 km before we calculate the 5‐year mean (i.e., we neglect all other times/lo-
cations). The 5‐year mean of IMERG precipitation rate for regions with a cyclone (Figure 1b) resembles the map
of all conditions, but the maximum in mean precipitation rate within the storm tracks is now much larger. Finally,
we average the precipitation in a similar fashion, but now, only consider IMERG pixels associated with cyclones
flagged as being occluded (Figure 1c). For these systems, the precipitation is more intense everywhere in the
storm tracks, with notably large rates in coastal regions of northern Europe, the eastern United States and Canada,
the Pacific Northwest, and northeast Asia. A map of the differences in mean precipitation rate between occluded

NAUD ET AL.

3 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

Figure 1. Mean IMERG precipitation for 2014–2018 in the northern hemisphere winter for (a) all time steps, (b) 6‐hourly periods when a cyclone is identified at the
middle time step with an area of influence defined as a 1,500 km radius centered on each cyclone's center, (c) 6‐hourly periods when an occluded cyclone is present and
(d) difference in mean precipitation between (c, b).

cyclones and all cyclones (Figure 1d) suggests that most of the storm track has more intense precipitation in the
presence of an occluded cyclone. One exception is the southern edge of the study area where precipitation is less
intense when occluded cyclones are present. This could be a result of the fact that occluded cyclones often “cut

NAUD ET AL.

4 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

Figure 2. Distribution of mean (a) PW, (b) 500 hPa ascent strength and (c) surface wind speed for occluded cyclones (solid black line), non‐occluded cyclones (dashed
black line) and the subset of non‐occluded cyclones that have a similar PW and ascent strength distributions (dashed red line) to occluded cyclones.

off” at upper tropospheric levels thereby limiting the equatorward export of cold air and the associated fronto-
genetically forced precipitation that accompanies such excursions. However, this is also an area where occluded
cyclones are rare (see Figure S1), so differences (negative and positive) are strongly impacted by a very limited
sample size.

4. Cyclone‐Centered Precipitation Composites: Occluded Versus Non‐Occluded
Cyclones at Peak Intensity

As mentioned earlier, precipitation in extratropical cyclones typically depends on the amount of environmental
moisture available to them, usually measured with PW, and on their intensity (e.g., Field & Wood, 2007; Pfahl &
Sprenger, 2016). Typically, cyclone intensity is gauged with wind speed, SLP minimum, or 850 hPa vorticity, but
here we choose the 500 hPa vertical velocity (ω) averaged across the region of ascent (for each cyclone the mean
ascent is calculated only for those pixels where ascent is occurring, as indicated by a negative value of ω500hPa).
This metric more directly characterizes the necessary lift for precipitation production. To better understand the
differences in Figure 1, we first examine the differences across occluded and non‐occluded cyclones in terms of
moisture and intensity. To do so, we need to establish a time during the lifecycle of the cyclones that is common to
both populations while being close to the period of occlusion. To satisfy these two conditions, we chose the time
of minimum in central SLP, referred to hereafter as time of peak intensity. This is not necessarily the time of
maximum precipitation or maximum ascent as discussed earlier in the introduction (Bengtsson et al., 2009; Booth
et al., 2018; Hawcroft et al., 2017; Heitmann et al., 2024; Michaelis et al., 2017; Rudeva & Gulev, 2011).

We first examine the distribution of mean cyclone‐wide PW, mean ascent strength and mean surface wind in the
occluded and non‐occluded cyclone subgroups for our subset of cyclones at peak intensity (Figure 2). Cyclones
that occlude tend to be more intense (Figure 2c), and have stronger ascent strength overall (Figure 2b). They also
display a fairly narrow distribution of PW compared to non‐occluded cyclones (Figure 2a), presumably because
they tend to occur in a narrower latitude band than the more numerous non‐occluding cyclones (Naud et al., 2023).
All three distributions suggest that precipitation would be more intense in occluded than non‐occluded cyclones,
consistent with Figure 1.

But to get a better sense of the importance of occlusion alone for precipitation production, we subset the more
numerous non‐occluded cyclones such that they have as similar as possible distributions of both ascent strength
and PW as their occluded counterparts. To do this, we arrange the non‐occluded cyclones in 1 hPa/hr‐wide ascent
strength bins and, using a random number generator, randomly remove (non‐occluded) cyclones in each ascent
strength bin until we obtain the same number as for occluded cyclones in the same ascent strength bin. We then
use this new set of non‐occluded cyclones to similarly force the PW distribution (arranged in 1 mm bins) to match
that of occluded cyclones. This is done by counting remaining non‐occluded cyclones in each PW bin and when
that number exceeds that of occluded cyclones, again apply a random number generator to remove the excess.

NAUD ET AL.

5 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

Figure 3. Cyclone‐centered composites of (a, b) IMERG precipitation, (d, e) MERRA‐2 500 hPa vertical velocity where ascending and (g, h) MERRA‐2 PW in (a, d, g)
occluded and (b, e, h) non‐occluded cyclones of similar mean PW and ascent strength when at peak intensity in the northern hemisphere winter months of 2014–2018.
Differences between occluded and non‐occluded cyclones in (c) precipitation, (f) 500 hPa vertical velocity where ascending and (i) PW. Overplotted as black contours in
(a, b) are the corresponding composites of 700 hPa Equivalent potential temperatures θe in 3 K increments from 278 K; and in (d, e, g, h) the corresponding IMERG
precipitation rates in mm/day in 2 mm/day increments from 2 to 14 mm/day.

This gives a subset of 114 non‐occluded cyclones that collectively have very similar mean PW, ascent strength
and surface wind distributions as the occluded cyclones (dashed red line in Figure 2). This is the subset we use
next for the lifecycle‐type mean precipitation rates comparison.

For both cyclone populations, composites of precipitation rates show the classic comma shape that is also present
in the ascent strength and PW composites (Figure 3), consistent with earlier work (e.g., Field & Wood, 2007;
Pfahl & Sprenger, 2016). When comparing cyclone‐centered composites of precipitation, for similar PW and
ascent strength distributions, precipitation is larger for occluded than non‐occluded cyclones (Figure 3a vs.
Figure 3b). For both types of cyclones, the maximum in precipitation appears related to the structure of the

NAUD ET AL.

6 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

700 hPa equivalent potential temperature θe spatial distribution (Figures 3a and 3b), with maxima occurring along
the thermal ridge for the occluded cyclones (Figure 3a), and along the warm front for the unoccluded ones
(Figure 3b). The difference in precipitation (Figure 3c) is therefore maximum along the occluded thermal ridge,
that is, the axis of maximum θe, evident in Figure 3a.

When examining the actual composites of 500 hPa vertical velocity (Figures 3d and 3e), while the cyclone‐wide
mean ascent is forced to be the same in the two populations, the maximum in ascent strength is larger for occluded
cyclones (up to between 2 and 4 hPa/hr difference, Figure 3f). The region of ascent is also more compact for
occluded cyclones, as revealed by a sharper decline in ascent strength from east to west than for non‐occluded
cyclones (Figure 3f). The significantly stronger ascent, also aligned along the occluded thermal ridge, is
consistent with J. Martin (1999b)'s analysis of three individual occluded cyclones that revealed strong frontal
scale ascent along the thermal ridge associated with the non‐frontogenetical geostrophic deformation, a
component of the along‐isentrope Q‐vector.

The cyclone‐centered composites of PW reveal that while on average PW is similar in the two cyclone pop-
ulations, in fact the western half of the non‐occluded cyclones is wetter, but the warm sector is slightly drier than
that for occluded cyclones. This disparity in the distribution of moisture matches the difference in ascent spatial
distribution and confirms that the warm sector is less expansive for the occluded cyclones. The frontal scale
forcing for ascent as demonstrated in J. Martin (1999b), mobilized only in the presence of the thermal ridge, is
likely responsible for the additional precipitation that distinguishes occluded from non‐occluded cyclones with
equivalent precipitable water and synoptic scale ascent.

The composites imply that occluded cyclones are more efficient at producing precipitation for a given amount of
moisture and cyclone intensity than non‐occluded cyclones, making the lifecycle‐type an important factor for
precipitation production in cyclones. To quantify the additional precipitation, we use the composites to calculate
the mean precipitation rates in a series of circular regions around the cyclone centers at radii of 500, 1,000 and
2,000 km. For occluded cyclones, the mean precipitation in each circle is: 8.9, 7.5, and 4.9 mm/hr, respectively.
For non‐occluded cyclones, we obtain: 7.1, 5.3, and 4.1 mm/hr. Regardless of the region's size, the mean pre-
cipitation rate is always greater for occluded cyclones. The greatest difference relative to non‐occluded cyclones
is achieved for the 1,000 km radius region, that includes the peak of the warm sector area, with a 42% excess in
precipitation for occluded versus non‐occluded cyclones.

5. Conclusions

Using IMERG precipitation rates and a database of extratropical cyclones, precipitation production in extra-
tropical cyclones is explored as a function of lifecycle‐type. A 5‐year mean of IMERG precipitation rates in
Northern Hemisphere winter shows that most of the precipitation is produced in extratropical cyclones, but the
mean is larger if the cyclones undergo occlusion during their lifecycles. When examining cyclone‐centered mean
precipitation rates for cyclones that have reached their peak intensity, occluding cyclones have larger rates than
non‐occluding ones. The differences are driven by the greater average intensity of occluded cyclones. But when
we force the set of non‐occluded cyclones to collectively exhibit a similar distribution of ascent strength and PW
as the set of occluded cyclones, the difference in mean cyclone‐centered precipitation rates remains: occluded
cyclones precipitate up to 42% more than non‐occluded ones.

Cyclones that occlude develop a characteristic thermal ridge that connects the SLP minimum to the peak of the
warm sector (defined as the intersection between cold, warm and occluded fronts). The development of a such a
feature mobilizes a frontal scale ascent from non‐frontogenetical deformation (J. Martin, 1999b) that underlies the
cloud and precipitation production along the axis of the thermal ridge. This thermal structure and its attendant
ascent region are entirely absent in non‐occluded cyclones. J. Martin (1999b) demonstrated this mechanism for
three separate occluded cyclones, and found that its operation had a strong correspondence with intense pre-
cipitation. In the present analysis, the observed mean precipitation in 162 NH occluded cyclones over a full 5‐
winter period is similarly maximized in the thermal ridge region. Furthermore, our results indicate that, when
controlling for mean ascent strength and moisture availability over a broad, cyclone‐centered domain, occluded
cyclones are more efficient at producing precipitation.

In this analysis, we only considered two states, occluded versus non‐occluded, but we acknowledge that there are,
of course, other factors that characterize cyclones that would matter for precipitation production. Such factors

NAUD ET AL.

7 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

might include the presence and intensity of lower and upper level forcings, the presense and strength of a warm
conveyor belt, and frontal structures (e.g., Catto, 2016; Wernli & Gray, 2024). Future work could involve a more
elaborate classification of the cyclones with combinations of multiple factors.

Overall, these results point out that lifecycle‐type needs to be taken into account when considering how a warmer
climate may change the extratropical cyclone's contribution to midlatitude precipitation. Precipitation associated
with extratropical cyclones is expected to increase in a warmer climate, mostly due to an increase in environ-
mental moisture (Yettella & Kay, 2017). Either with idealized simulations (Sinclair & Catto, 2023), or with future
climate simulations (e.g., Binder et al., 2023; Dolores‐Tesillos et al., 2022; Dolores‐Tesillos & Pfahl, 2024), the
degree to which the associated increase in latent heat release feedbacks on cyclone intensity changes with cyclone
type. However, it is not known if such additional heat release also affects the development of occlusions (Posselt
& Martin, 2004). Earth System Models can simulate the structure and evolution of occluded cyclones accurately
(Naud et al., 2025), and thus, they can serve as tools for investigating to what extent future precipitation changes
arise from perturbations in the character of precipitation (i.e., convective, including elevated, vs. stratiform
precipitation) in different lifecycle types. The present study suggests that reliable projections of mid‐latitude
wintertime precipitation changes in a warmer climate will depend upon accurate simulation of how the fre-
quency of occluded cyclones changes as warming progresses.

Data Availability Statement

tavg1_2d_slv_Nx:

The cyclone database is publicly available through https://data.giss.nasa.gov/storms/obs‐etc/. IMERG and
MERRA‐2 data can be obtained through the NASA Goddard Earth Science Data and Information Services
Center https://disc.gsfc.nasa.gov/datasets. Global Modeling and Assimilation Office (GMAO)
(2015),
MERRA‐2
2d,1‐Hourly,Time‐Averaged,Single‐Level,Assimilation,Single‐Level Di-
agnostics V5.12.4, Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES
DISC), Accessed: 01–2024, https://doi.org/10.5067/VJAFPLI1CSIV. Global Modeling and Assimilation Office
(GMAO) (2015), MERRA‐2 tavg3_3d_asm_Nv: 3d,3‐Hourly, Time‐Averaged, Model‐Level, Assimilation,
Assimilated Meteorological Fields V5.12.4, Greenbelt, MD, USA, Goddard Earth Sciences Data and Infor-
mation Services Center (GES DISC), Accessed: 01–2024, https://doi.org/10.5067/SUOQESM06LPK. Huffman
et al., 2023 Huffman, G.J., E.F. Stocker, D.T. Bolvin, E.J. Nelkin, Jackson Tan (2023), GPM IMERG Final
Precipitation L3 Half Hourly 0.1° × 0.1° V07, Greenbelt, MD, Goddard Earth Sciences Data and Information
Services Center (GES DISC), Accessed: 01–2024, https://doi.org/10.5067/GPM/IMERG/3B‐HH/07.

References

Bauer, M., & Del Genio, A. D. (2006). Composite analysis of winter cyclones in a GCM: Influence on climatological humidity. Journal of

Climate, 19(9), 1652–1672. https://doi.org/10.1175/jcli3690.1

Bengtsson, L., Hodges, K. I., & Keenlyside, N. (2009). Will extratropical storms intensify in a warmer climate? Journal of Climate, 22(9), 2276–

2301. https://doi.org/10.1175/2008JCLI2678.1

Binder, H., Joos, H., Sprenger, M., & Wernli, H. (2023). Warm conveyor belts in present‐day and future climate simulations – Part 2: Role of
potential vorticity production for cyclone intensification. Weather and Climate Dynamics, 4(1), 19–37. https://doi.org/10.5194/wcd‐4‐19‐2023
Booth, J. F., Naud, C. M., & Jeyaratnam, J. (2018). Extratropical cyclone precipitation life cycles: A satellite‐based analysis. Geophysical

Research Letters, 45(16), 8647–8654. https://doi.org/10.1029/2018GL078977

Catto, J. L. (2016). Extratropical cyclone classification and its use in climate studies. Reviews of Geophysics, 54(2), 486–520. https://doi.org/10.

1002/2016RG000519

Catto, J. L., Jakob, C., Berry, G., & Nicholls, N. (2012). Relating global precipitation to atmospheric fronts. Geophysical Research Letters, 39(10),

L10805. https://doi.org/10.1029/2012GL051736

Crocker, A., Godson, W. L., & Penner, C. M. (1947). Frontal contour charts. Journal of the Atmospheric Sciences, 4(3), 95–99. https://doi.org/10.

1175/1520‐0469(1947)004<0095:fccbpo>2.0.co;2

Dolores‐Tesillos, E., & Pfahl, S. (2024). Future changes in North Atlantic winter cyclones in CESM‐LE – Part 2: A Lagrangian analysis. Weather

and Climate Dynamics, 5(1), 163–179. https://doi.org/10.5194/wcd‐5‐163‐2024

Dolores‐Tesillos, E., Teubler, F., & Pfahl, S. (2022). Future changes in North Atlantic winter cyclones in CESM‐LE – Part 1: Cyclone intensity,
potential vorticity anomalies, and horizontal wind speed. Weather and Climate Dynamics, 3(2), 429–448. https://doi.org/10.5194/wcd‐3‐429‐
2022

Field, P. R., & Wood, R. (2007). Precipitation and cloud structure in midlatitude cyclones. Journal of Climate, 20(2), 233–254. https://doi.org/10.

1175/JCLI3998.1

Gelaro, R., McCarty, W., Suarez, M. J., Todling, R., Molod, A., Takacs, L., et al. (2017). The Modern‐Era Retrospective analysis for Research and

Applications, version 2 (MERRA‐2). Journal of Climate, 30(14), 5419–5454. https://doi.org/10.1175/jcli‐d‐16‐0758.1

Grim, J. A., Rauber, R. M., Ramamurthy, M. K., Jewett, B. F., & Han, M. (2007). High‐resolution observations of the Trowal‐Warm‐frontal region

of two continental winter cyclones. Monthly Weather Review, 135(5), 1629–1646. https://doi.org/10.1175/MWR3378.1

Han, M., Rauber, R. M., Ramamurthy, M. K., Jewett, B. F., & Grim, J. A. (2007). Mesoscale dynamics of the TROWAL and warm‐frontal regions

of two continental winter cyclones. Monthly Weather Review, 135(5), 1647–1670. https://doi.org/10.1175/MWR3377.1

Acknowledgments
The work was funded by the NASA
CloudSat‐CALIPSO science team
recompete program, Grant
80NSSC20K0085. CMN and DJP received
additional funding from the NASA
Modeling, Analysis and Prediction (MAP)
program, Grant 80NSSC21K1728, and
NASA Precipitation Measurement Mission
Grant 80NSSC22K0602, and GSE from
the NASA Program and APAM‐GISS
Cooperative Agreement
80NSSC18M0133, NASA Precipitation
Measurement Missions Grant
80NSSC22K0609, and the NASA PolSIR
project (80LARC24CA001). A portion of
this research was conducted at the Jet
Propulsion Laboratory, California Institute
of Technology, under a contract with the
National Aeronautics and Space
Administration (NASA)
80NM0018D0004.

NAUD ET AL.

8 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons LicenseGeophysical Research Letters

10.1029/2025GL115153

Hawcroft, M., Dacre, H., Forbes, R., Hodges, K., Shaffrey, L., & Stein, T. (2017). Using satellite and reanalysis data to evaluate the representation
of latent heating in extratropical cyclones in a Climate Model. Climate Dynamics, 48(7–8), 2255–2278. https://doi.org/10.1007/s00382‐016‐
3204‐6

Hawcroft, M. K., Shaffrey, L. C., Hodges, K. I., & Dacre, H. F. (2012). How much northern hemisphere precipitation is associated with

extratropical cyclones? Geophysical Research Letters, 39(24), L24809. https://doi.org/10.1029/2012GL053866

Heitmann, K., Sprenger, M., Binder, H., Wernli, H., & Joos, H. (2024). Warm conveyor belt characteristics and impacts along the life cycle of
extratropical cyclones: Case studies and climatological analysis based on ERA5. Weather and Climate Dynamics, 5(2), 537–557. https://doi.
org/10.5194/wcd‐5‐537‐2024

Hoskins, B. J., Draghici, I., & Davies, H. C. (1978). A new look at the w‐equation. Quarterly Journal of the Royal Meteorological Society,

104(439), 31–38. https://doi.org/10.1002/qj.49710443903

Huffman, G. J. (2020). Algorithm Theoretical Basis Document (ATBD) version 5.2 NASA Global Precipitation Measurement (GPM) Integrated
MULTI‐SATELLITE RETRieval for GPM (IMERG). Retrieved from https://gpm.nasa.gov/sites/default/files/2020‐05/IMERG_ATBD_V06.
3.pdf

Huffman, G. J., Stocker, E. F., Bolvin, D. T., Nelkin, E. J., & Tan, J. (2023). GPM IMERG final precipitation L3 half hourly 0.1 degree x 0.1
degree V07. Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/IMERG/3B‐HH/07
Keyser, D., Schmidt, B. D., & Duffy, D. G. (1992). Quasigeostrophic vertical motions diagnosed from along‐ and across‐isentrope components of

the Q‐vector. Monthly Weather Review, 120(5), 731–741. https://doi.org/10.1175/1520‐0493(1992)120<0731:qvmdfa>2.0.co;2

Martin, J. E. (1998a). The structure and evolution of a continental winter cyclone. Part I: Frontal structure and the occlusion process. Monthly

Weather Review, 126(2), 303–328. https://doi.org/10.1175/1520‐0493(1998)126<0303:tsaeoa>2.0.co;2

Martin, J. E. (1998b). The structure and evolution of a continental winter cyclone. Part II: Frontal forcing of an extreme snow event. Monthly

Weather Review, 126(2), 329–348. https://doi.org/10.1175/1520‐0493(1998)126<0329:tsaeoa>2.0.co;2

Martin, J. E. (1999a). Quasi‐geostrophic forcing of ascent in the occluded sector of cyclones and the Trowal Airstream. Monthly Weather Review,

127(1), 70–88. https://doi.org/10.1175/1520‐0493(1999)127<0070:qfoait>2.0.co;2

Martin, J. E. (1999b). The separate roles of geostrophic vorticity and deformation in the mid‐latitude occlusion process. Monthly Weather Review,

127(10), 2404–2418. https://doi.org/10.1175/1520‐0493(1999)127<2404:tsrogv>2.0.co;2

Michaelis, A. C., Willison, J., Lackmann, G. M., & Robinson, W. A. (2017). Changes in winter North Atlantic extratropical cyclones in high‐
resolution regional Pseudo‐Global warming simulations. Journal of Climate, 30(17), 6905–6925. https://doi.org/10.1175/JCLI‐D‐16‐0697.1
Naud, C. M., Booth, J. F., Lebsock, M., & Grecu, M. (2018). Observational constraint for precipitation in extratropical cyclones: Sensitivity to

data sources. Journal of Applied Meteorology and Climatology, 57(4), 991–1009. https://doi.org/10.1175/JAMC‐D‐17‐0289.1

Naud, C. M., Elsaesser, G. S., Martin, J. E., Ghosh, P., Posselt, D. J., & Booth, J. F. (2025). How well does an Earth Sytem Model represent the

occlusion of extratropical cyclones? Journal of Climate. in press. https://doi.org/10.1175/JCLI‐D‐24‐0252.1

Naud, C. M., Ghosh, P., Martin, J. E., Elsaesser, G. S., & Posselt, D. J. (2024). A CloudSat‐CALIPSO view of cloud and precipitation in the
occluded quadrants of extratropical cyclones. Quarterly Journal of the Royal Meteorological Society, 150(760), 1336–1356. https://doi.org/10.
1002/qj.4648

Naud, C. M., Martin, J. E., Ghosh, P., Elsaesser, G. S., & Posselt, D. J. (2023). Automated identification of occluded sectors in midlatitude
cyclones: Method and some climatological applications. The Quarterly Journal of the Royal Meteorological Society, 149(754), 1990–2010.
https://doi.org/10.1002/qj.4491

Neu, U., Akperov, M. G., Bellenbaum, N., Benestad, R., Blender, R., Caballero, R., et al. (2013). IMILAST‐a community effort to intercompare
extratropical cyclone detection and tracking algorithms. Bulletin America Meteorology Social, 94, 529–547. https://doi.org/10.1175/BAMS‐D‐
11‐00154.1

Penner, C. (1955). A three‐front model for synoptic analyses. Quart. J. Roy. Meteor. Soc., 81(347), 89–91. https://doi.org/10.1002/qj.

49708134710

Pfahl, S., & Sprenger, M. (2016). On the relationship between extratropical cyclone precipitation and intensity. Geophysical Research Letters,

43(4), 1752–1758. https://doi.org/10.1002/2016GL068018

Posselt, D. J., & Martin, J. E. (2004). The effect of latent heat release on the evolution of a warm occluded thermal structure. Monthly Weather

Review, 132(2), 578–599. https://doi.org/10.1175/1520‐0493(2004)132<0578:teolhr>2.0.co;2

Rudeva, I., & Gulev, S. K. (2011). Composite analysis of North Atlantic extratropical cyclones in NCEP‐NCAR reanalysis data. Monthly Weather

Review, 139(5), 1419–1446. https://doi.org/10.1175/2010MWR3294.1

Rüdisühli, S., Sprenger, M., Leutwyler, D., Schär, C., & Wernli, H. (2020). Attribution of precipitation to cyclones and fronts over Europe in a

kilometer‐scale regional climate simulation. Weather and Climate Dynamics, 1(2), 675–699. https://doi.org/10.5194/wcd‐1‐675‐2020

Schultz, D. M., & Mass, C. F. (1993). The occlusion process in a midlatitude cyclone over land. Monthly Weather Review, 121(4), 918–940.

https://doi.org/10.1175/1520‐0493(1993)121<0918:topiam>2.0.co;2

Schultz, D. M., & Vaughan, G. (2011). Occluded fronts and the occlusion process: A fresh look at conventional wisdom. Bulletin America

Meteorology Social, 92(4), 443–466. https://doi.org/10.1175/2010bams3057.1

Shapiro, M. A., & Keyser, D. (1990). Fronts, jet streams and the tropopause. In C. W. Newton & E. O. Holopainen (Eds.), Extratropical cyclones:

The Erik Palmén Memorial volume (pp. 167–191). American Meteorological Society.

Sinclair, V. A., & Catto, J. L. (2023). The relationship between extra‐tropical cyclone intensity and precipitation in idealised current and future

climates. Weather and Climate Dynamics, 4(3), 567–589. https://doi.org/10.5194/wcd‐4‐567‐2023

Stoelinga, M. T., Locatelli, J. D., & Hobbs, P. V. (2002). Warm occlusions, cold occlusions and forward tilting cold fronts. Bulletin America

Meteorology Social, 83(5), 709–721. https://doi.org/10.1175/1520‐0477(2002)083<0709:wocoaf>2.3.co;2

Sutcliffe, R. (1947). A contribution to the problem of development. Quarterly Journal of the Royal Meteorological Society, 73(317–318), 370–

383. https://doi.org/10.1002/qj.49707331710

Wernli, H., & Gray, S. L. (2024). The importance of Diabatic processes for the dynamics of synoptic‐scale extratropical weather systems – A

review. Weather and Climate Dynamics, 5(4), 129901408. https://doi.org/10.5194/wcd‐5‐1299‐2024

Yettella, V., & Kay, J. E. (2017). How will precipitation change in extratropical cyclones as the planet warms? Insight from a large initial condition

Climate Model ensemble. Climate Dynamics, 49(5–6), 1765–1781. https://doi.org/10.1007/s00382‐016‐3410.2

NAUD ET AL.

9 of 9

 19448007, 2025, 8, Downloaded from https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025GL115153 by University Of Sao Paulo - Brazil, Wiley Online Library on [28/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License