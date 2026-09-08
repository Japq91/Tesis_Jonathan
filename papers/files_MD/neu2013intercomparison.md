IMILAST
A Community Effort to Intercompare Extratropical
Cyclone Detection and Tracking Algorithms
by Urs NeU, Mirseid G. Akperov, NiNA belleNbAUM, rAsMUs beNestAd, richArd bleNder,
rodriGo cAbAllero, ANGelA cocozzA, heleN F. dAcre, yANG FeNG, klAUs FrAedrich,
JeNs GrieGer, serGey GUlev, JohN hANley, tiM hewsoN, MAsArU iNAtsU, keviN keAy, sArAh F. kew,
iNA kiNdeM, GreGor c. leckebUsch, MArGAridA l. r. liberAto, piero lioNello, iGor i. Mokhov,
JoAqUiM G. piNto, christoph c. rAible, MArco reAle, iriNA rUdevA, MAreike schUster,
iAN siMMoNds, MArk siNclAir, MichAel spreNGer, NAtAliA d. tiliNiNA, isAbel F. triGo,
sveN Ulbrich, Uwe Ulbrich, XiAolAN l. wANG, ANd heiNi werNli
An intercomparison experiment involving 15 commonly used detection and tracking
algorithms for extratropical cyclones reveals those cyclone characteristics that are robust
between different schemes and those that differ markedly.
E
xtratropical cyclones are fundamental Identifying and tracking extratropical cyclones
meteorological features and play a key role in might seem, superficially, to be a straightforward
a broad range of weather phenomena. They are activity, but in reality it is very challenging. In this
a central component maintaining the global atmo- regard it is useful to compare the situation with
spheric energy, moisture, and momentum budgets. tropical cyclones, which possess characteristics that
They are on the one hand responsible for an im- make them relatively easy to identify and track: they
portant part of our water supply, and on the other occur rarely (making misassociation unlikely), are
are intimately linked with many natural hazards generally symmetric and slow moving, and have
affecting the middle and high latitudes (wind damage, a relatively unambiguous structure. Extratropical
precipitation-related flooding, storm surges, and cyclones are in a sense the “opposite”: they are much
marine storminess). Thus, it is important to provide more common, can range greatly in shape and struc-
for society an accurate diagnosis of cyclone activity, ture (are often asymmetric), differ rather more in size
which includes a baseline climatology of extratropical (with diameters ranging from about 100 to well over
storms (e.g., Hoskins and Hodges 2002) and also 1,000 km), and have translational velocities that can
estimates of likely future changes therein. While vary greatly. Identifying the same physical feature
future changes in some cyclone characteristics such at different times (i.e., tracking) is also complicated
as the total number of cyclones might be small, major by the fact that a single cyclone will sometimes split
signals may still be expected in specific characteristics into separate features, and sometimes two will merge
such as regional storm frequency, intensity, and loca- into one. Furthermore, extratropical cyclones occur
tion (e.g., Leckebusch et al. 2006; Wang et al. 2006; in very diverse synoptic situations, with some being
Löptien et al. 2008; Bengtsson et al. 2009; Pinto et al. confined to lower-tropospheric levels and others
2009; Raible et al. 2010; Schneidereit et al. 2010). extending through great depth. This great complexity
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 529
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

reveals why there is no single commonly agreed upon for example, regarding trends in cyclone intensity.
scientific definition of what an extratropical cyclone Raible et al. (2008), for example, demonstrated that
is, and also why there exists a range of ideas and three different algorithms applied to the same input
concepts regarding how to identify and track them. data showed similar interannual variability but con-
It could be argued that an in-depth manual siderable differences in total cyclone numbers. While
reanalysis of cyclone trajectories based on weather this comparison showed similar trend patterns in the
maps reconstructed using all available data (e.g., Atlantic, trends found for the Pacific even differed
Hewson et al. 2000) would provide the best tracks. in sign. Indeed, method-associated uncertainties
However, given the lack of data in some regions and in some cases are quite large, such that equivalent
the complexity of cyclone development, such activi- scientific studies may find contradictory climate
ties inevitably involve some subjective choices being change signals even when using identical input data
made by the analyst. So there is no accepted single (Trigo 2006; Ulbrich et al. 2009). Therefore, it is
“truth” regarding specific cyclone tracks. Moreover, crucial to know those aspects for which the results
while careful manual tracking might nonetheless are robust with regard to the method used, and those
be considered optimal, for quantifying the behavior aspects for which there will be large method-related
of all cyclones over many decades it is clearly not uncertainties. The project Intercomparison of Mid
feasible, and the application of automated detection Latitude Storm Diagnostics (IMILAST) is the first
and tracking methods to reanalysis data—the thrust comprehensive assessment focusing on this method-
of this paper—is indispensable. related uncertainty.
Although automated schemes are objective
and reproducible, they are based on different STRATEGY AND METHODS. Over the last
understandings of what best characterizes a cyclone. two decades, many numerical identification and
Application of different algorithms provides results tracking algorithms have been developed (Murray
that are remarkably similar in some aspects but and Simmonds 1991; Hodges 1995; Serreze 1995;
may be very different in others. Thus, depending on Blender et al. 1997; Sinclair 1997; Simmonds et al.
what one is looking for, the selection of a particular 1999; Lionello et al. 2002; Benestad and Chen 2006;
method can significantly affect one’s conclusions, Trigo 2006; Wernli and Schwierz 2006; Akperov
AFFILIATIONS: NeU—ProClim, Swiss Academy of Sciences, Dom Luiz, University of Lisbon, Lisbon, and School of Sciences
Bern, Switzerland; Akperov ANd Mokhov—A.M. Obukhov Institute and Technology, University of Trás-os-Montes and Alto Douro
of Atmospheric Physics, Russian Academy of Sciences, Moscow, (UTAD), Vila Real, Portugal; lioNello—Di.S.Te.B.A., University of
Russia; belleNbAUM, piNto, ANd Ulbrich—Institute of Geophysics Salento, and CMCC, EuroMediterranea Center on Climate Change,
and Meteorology, University of Cologne, Cologne, Germany; Lecce, Italy; rAible—Climate and Environmental Physics, and
beNestAd—Norwegian Meteorological Institute, Oslo, Norway; Oeschger Center for Climate Change Research, University of Bern,
bleNder ANd FrAedrich—Institute of Meteorology, University Bern, Switzerland; rUdevA—P. P. Shirshov Institute of Oceanology,
of Hamburg, Hamburg, Germany; cAbAllero ANd hANley— Russian Academy of Sciences, Moscow, Russia, and School of
Department of Meteorology, Stockholm University, Stockholm, Earth Sciences, University of Melbourne, Melbourne, Victoria,
Sweden; cocozzA ANd reAle—Di.S.Te.B.A., University of Salento, Australia; siMMoNds—School of Earth Sciences, University of
Lecce, Italy; dAcre—Department of Meteorology, University of Melbourne, Melbourne, Victoria, Australia; siNclAir—Embry-Riddle
Reading, Reading, United Kingdom; FeNG ANd wANG—Climate Aeronautical University, Prescott, Arizona; spreNGer ANd werNli—
Research Division, Environment Canada, Toronto, Ontario, Canada; Institute for Atmospheric and Climate Science, ETH Zurich, Zurich,
GrieGer, schUster, ANd Ulbrich—Institute of Meteorology, Freie Switzerland; triGo—Instituto Dom Luiz, University of Lisbon, and
Universität Berlin, Berlin, Germany; GUlev ANd tiliNiNA—P. P. Institute of Meteorology I. P., Lisbon, Portugal
Shirshov Institute of Oceanology, Russian Academy of Sciences, CORRESPONDING AUTHOR: Urs Neu, ProClim, Swiss Academy
and Moscow State University, Moscow, Russia; hewsoN—European of Sciences, Schwarztorstrasse 9 CH-3007 Bern, Switzerland
Centre for Medium-Range Weather Forecasts, Reading, and Met E-mail: urs.neu@scnat.ch
Office, Exeter, United Kingdom; iNAtsU—Graduate School of Sci-
The abstract for this article can be found in this issue, following the table
ence, Hokkaido University, Sapporo, Japan; keAy—School of Earth
of contents.
Sciences, University of Melbourne, and Bureau of Meteorology,
DOI:10.1175/BAMS-D-11-00154.1
Melbourne, Victoria, Australia; kew—Royal Netherlands
Meteorological Institute, De Bilt, Netherlands; kiNdeM—Bjerknes Supplements A and B to this article are available online (10.1175/BAMS-
Centre for Climate Research, Bergen, Norway; leckebUsch—School D-11-00154.2)
of Geography, Earth and Environmental Sciences, University of
In final form 31 August 2012
Birmingham, Birmingham, United Kingdom; liberAto—Instituto
©2013 American Meteorological Society
530 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

et al. 2007; Rudeva and Gulev 2007; Inatsu 2009; that uses 12-hourly data) for a 20-yr period from
Kew et al. 2010; Hewson and Titley 2010; Hanley and 1 January 1989 to 31 March 2009.
Caballero 2012). According to different perceptions Besides being related to method differences, track
of what a cyclone is, tracking may be performed uncertainty can also arise from reanalysis inad-
utilizing a number of atmospheric variables equacies. However, this aspect has been discussed
(Hoskins and Hodges 2002). One of the most widely elsewhere in the literature (e.g., Wang et al. 2006;
discussed algorithmic differences relates to the Benestad and Chen 2006; Raible et al. 2008; Hodges
choice of mean sea level pressure (MSLP) or lower- et al. 2011) and is not analyzed here.
tropospheric vorticity as a basic identification/ While full descriptions of the methods involved in
tracking metric (e.g., Sinclair 1994; Hodges et al. this intercomparison are presented in earlier publica-
2003; Rudeva and Gulev 2007; Ulbrich et al. 2009). tions, Table 1 provides a brief outline and supplement
These options reflect the different characteristics A (“General description of the different methods par-
that one might focus on when examining cyclones: ticipating in the intercomparison”; available online
while vorticity is more focused on the wind field and at http://dx.doi.org/10.1175/BAMS-D-11-00154.2) a
contains more information on the high-frequency more extensive overview of method characteristics.
synoptic scale, central pressure is linked to the mass Methods differ in a number of aspects, including,
field and represents the low-frequency scale better for example, variables used for cyclone identification
(Hodges et al. 2003). This can lead, for example, to
different estimated positions of the cyclone center, DEFINITIONS RELATED TO CYCLONES
since in a westerly airflow the vorticity-based center
AND TRACKING
can sometimes be located a few hundred kilometers
equatorward of the related pressure minimum Cyclone: There is no accepted universal definition of
(Sinclair 1994). On other occasions different features what a cyclone is or where its exact position is. In
are identified, because mobile vorticity centers are this study, “cyclone” refers to a point (the cyclone
not necessarily associated with a pressure minimum. “center”) identified on the Earth’s surface at a certain
time through different approaches, often by searching
There are many other metrics for assessing cyclone
for a minimum of MSLP or a maximum of lower-
activity, as discussed, for example, by Raible et al.
tropospheric cyclonic vorticity.
(2008) and Ulbrich et al. (2009).
Track: A cyclone track consists of a series of cyclones
To quantify the impact on extratropical storm
identified in sequential time steps at adjacent
analysis of using different methods, an intercom- locations, which are deemed to represent the same
parison experiment was initiated. In the first activity, physical feature in reality.
on which the results presented in this paper are Number of cyclones: Count of cyclone tracks over a
based, all participating groups computed cyclone certain region (globe, hemisphere, etc.).
Cyclone center counts: The numbers of cyclone
tracks (for definitions, see sidebar) for the same
centers identified at each time step, summed over all
period using the same input—the European Centre
time steps (in this study, only including cyclones that
for Medium-Range Weather Forecasts (ECMWF)
make up tracks with lifetime ≥24 h).
Interim Re-Analysis (ERA-Interim) dataset (Dee Cyclone center density: Percentage of cyclone
et al. 2011).1 Space–time resolution of the input data occurrence per time step and per unit area of
may have a significant impact on cyclone statistics (1000 km2). For example, if at a grid location the
(Blender and Schubert 2000; Pinto et al. 2005; Jung cyclone center density is 10%, then in an area of
1000 km × 1000 km in 100 time steps we find 10
et al. 2006), and high resolution is essential to help
cyclones. A value >100% means there is more than
capture the full life cycles of cyclones and to ensure
one cyclone per time step in that area on average
that even small cyclonic windstorms can be identi-
(synonymous with cyclone frequency).
fied (Pinto et al. 2005; Hewson and Titley 2010). Track density: Number of tracks passing a grid cell
For this first intercomparison activity, for reasons (with repeated entries of the same track being
of availability, we used 1.5° spatial resolution and counted as one).
6-hourly temporal resolution (except for one method
1 The key criteria for selecting this input dataset were that it be based on a state-of-the-art model (gridded reanalysis dataset)
with a four-dimensional variational data assimilation (4DVAR) scheme, be easy to access, and have a high spatial resolution.
Recent intercomparisons (Allen et al. 2010; Hodges et al. 2011) have demonstrated that cyclone characteristics in ERA-Interim
are quite comparable with those revealed by, for example, Modern Era Retrospective-Analysis (MERRA) and National Centers
for Environmental Prediction–Climate Forecast System Reanalysis (NCEP–CFSR).
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 531
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

(MSLP, vorticity, etc.), the cyclone identification pro- argue for standardization is data preprocessing, as
cedures themselves, elimination criteria (thresholds) performed in some methods, since such steps can
to filter out weak or “artificial” low pressure systems lead, for example, to smoothing, which influences
(e.g., by requiring a minimum travel distance), and the results. However, preprocessing is performed
algorithms to combine the cyclone centers into a with different purposes in mind, as, for example,
track. In addition to there being disparities between addressing inhomogeneous grid field size when using
the algorithms due to different concepts of a cyclone, latitude–longitude grids, and is therefore difficult
differences in methods also relate to some degree to standardize. Furthermore, preprocessing is only
to the different kinds of phenomena the original one of many choices and is an integral part of some
authors wanted to study. For an intercomparison of algorithms. Note finally that some methods originally
different algorithms, it would be desirable to distin- focused on very different regions. One could argue
guish between these two origins of differences and that this might be a criterion for noninclusion, but
compare only algorithms that address precisely the given that the fundamental physics of extratropical
same problem. However, this distinction is not clear cyclones is similar everywhere we did not exclude
cut, because algorithm settings (e.g., a threshold for on this basis.
minimum pressure gradient) could have been intro- All the schemes participating in this intercompari-
duced to match a corresponding cyclone definition son are in common use. In that sense our comparison
(i.e., if the definition contains a gradient threshold) or is of most value when they are used in their “standard
just to eliminate shallow heat lows. Thus, in our inter- form” (excepting some adaptations made to accom-
comparison we included methods designed to search modate the input data resolution). Therefore, we
for extratropical cyclones in general, but excluded did not apply any far-reaching standardization. The
algorithms that were clearly designed for very specific slight downside is that this approach may increase
types (e.g., looking for extreme cyclones only or for the difficulty of understanding the reasons behind
polar lows) to prevent a possible exaggeration of discrepancies in cyclone climatologies. Moreover,
method differences. A further area where one could it is difficult to quantify the full range of impacts
Table 1. Different methods and some key characteristics: “variable used” (MSLP: mean sea level pressure;
VORT: vorticity or Laplacian of MSLP; VORT Z850: vorticity at 850 hPa as computed by ERA-Interim;
Z850: geopotential height at 850 hPa; grad.: gradient of MSLP; min: minimum), and “terrain filtering”
(>1000 m; all cyclones positioned over terrain higher than 1,000 m MSL are eliminated).
Code* Main references for method description Variable used Terrain filtering
M02 Murray and Simmonds (1991), Pinto et al. (2005) MSLP (min), VORT >1500 m
M03 Benestad and Chen (2006) MSLP (min, grad.) none
M06 Hewson et al. (1997), Hewson and Titley (2010) MSLP (min), VORT, wind, fronts Terrain-following
M08 Trigo (2006) MSLP (min, grad.) none
M09 Serreze (1995), Wang et al. (2006) MSLP (min, grad.), VORT none
M10 Murray and Simmonds (1991), Simmonds et al. (2008) MSLP (min), VORT >1000 m
M12 Zolina and Gulev (2002), Rudeva and Gulev (2007) MSLP (min) none
M13 Hanley and Caballero (2012) MSLP (min) >1500 m
M14 Kew et al. (2010) Z850 (min, contour) none
M15 Blender et al. (1997), Raible et al. (2008) MSLP (min) >1000 m
M16 Lionello et al. (2002) MSLP (min) none
M18 Sinclair (1994, 1997) Z850 VORT >1000 m
M20 Wernli and Schwierz (2006) MSLP (min) >1500 m
M21 Inatsu (2009) Z850 VORT none
M22 Bardin and Polonsky (2005), Akperov et al. (2007) MSLP (min, contour) none
*Code numbers were assigned at the beginning of the project to research groups interested in participation. A few groups
have not (yet) contributed a dataset, and others have since ceased activities in cyclone tracking. Furthermore, some groups
use almost identical algorithms, in which case duplicates have been removed. The original code assignment was retained to
guarantee compatibility of publications for the whole project duration. Therefore, code numbers are not continuous.
532 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

from method differences and search for reasons at would be needed. Such sensitivity studies are foreseen
the same time. For the latter, sensitivity studies that, as a next step in the IMILAST project.
for example, change parameter settings in a specific However, we did standardize one aspect
method and compare the corresponding results throughout—namely, a minimum lifetime. This was
Fig. 1. Total cyclone center density in the NH for cyclones lasting 24 h or more (percentage of cyclone
occurrence per time step and area of 1000 km2; see sidebar) for all detection and tracking methods in
DJF. The results of methods M03, M09, and M14 (which extrapolate the input data to a higher resolu-
tion for their calculation) are interpolated to the 1.5° × 1.5° grid.
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 533
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

fixed to 24 h for all methods (i.e., to be retained a threshold would increase the number of cyclones
cyclone has to exist for a minimum of five 6-hourly considerably and a longer one would decrease it.
time steps, or three 12-hourly time steps for method The inclusion or exclusion of cyclones over elevated
M06). This standardization was seen as permissible topography has not been standardized a priori
and desirable because in most methods the lifetime because this is an integral part of some methods and
threshold is a parameter of arbitrary choice with not necessarily problem oriented. However, for com-
a rather straightforward impact: a shorter lifetime parisons of hemispheric statistics (see sections below)
Fig. 2. As in Fig. 1, but for the SH in JJA.
534 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

a standardized set of track data where cyclones over with lowest central pressure in each hemisphere and at
mountainous terrain were eliminated a posteriori has each time step (if the number initially detected exceeds
been used. We did not introduce any other standard- 25). Test calculations for a period of 100 days with
ization, as this would not have been straightforward different settings subsequently showed that a higher
and indeed was seen as rather arbitrary. cutoff value of 50 instead of 25 cyclones approximately
In the following we compare and analyze the track doubled the number of cyclones detected, which shows
datasets derived by the 15 different methods, focusing that the cutoff threshold of 25 indeed considerably
on a number of important cyclone characteristics: reduces the number of detected cyclones.
climatological frequency (section “Climatology of Although methods M02 and M10 are both based
midlatitude cyclone characteristics”), life cycle aspects on the algorithm of Murray and Simmonds (1991),
(section “Cyclone life cycle characteristics”), case they include different updates and parameter settings
studies (section “Case studies”), and interannual vari- (Pinto et al. 2005; Simmonds et al. 2008) and do
ability and trends (section “Interannual variability and not show a strong level of agreement that we might
trends”). A short discussion concludes this paper. As expect. How far the differences in parameter settings
stated above we have no best-track datasets to define are related to the fact that the two algorithms were
truth in this study. Therefore, the study cannot assess developed for different hemispheres is not clear
any kind of “quality” of individual methods, so the (since cyclones are the same physical phenomenon
reader should view results accordingly and not be in both hemispheres) and has to be evaluated. Large
prejudiced for or against method(s) exhibiting outlier deviations are apparent between the various methods
behavior. The purpose of this experiment is to assess over mountain areas. This is mainly because there
the range of variability for different cyclone charac- are different strategies for dealing with mountains;
teristics and to highlight the robustness of different in some methods, for example, such regions are
characteristics with regard to method differences. excluded a priori.
Despite qualitatively consistent spatial patterns
CLIMATOLOGY OF MIDLATITUDE across different methods, quantitative differences in
CYCLONE CHARACTERISTICS. In this sec- the total numbers of extratropical cyclones are rela-
tion we examine some aspects of cyclone climatologies tively large in both hemispheres. For the NH, total
obtained from the different detection and tracking numbers range from about 6,000 (M03) to 21,000
methods. Figures 1 and 2 present the spatial patterns (M18) during winter [December–February (DJF);
of cyclone center density (or cyclone frequency) for first row in Table 2]. In summer [June–August (JJA);
each method for the winter season of each hemi- first column in Table 2] the range is between about
sphere. Overall, a qualitative agreement in the spatial 5,000 (M03) and 28,000 (M09). Interestingly, the sea-
structures is found, as all methods identify the major sonal (winter to summer) changes vary quite strongly
oceanic cyclone activity areas east of Greenland and between methods. Some methods increase the number
along the Scandinavian coast line, the two centers in of cyclones from winter to summer by more than
the North Pacific in the Northern Hemisphere (NH), 50%, whereas others decrease it by a few percent. Both
and regional maxima in the Indian Ocean sector, the discrepancies are related to differences in algorithms
Amundsen Sea, and the Drake Passage in the Southern that are not easy to disentangle. One factor is the
Hemisphere (SH). In contrast, there are noteworthy extent to which shallow cyclones (of which some can
discrepancies throughout the Mediterranean, which is be attributed to summertime heat lows) are excluded.
of particular societal relevance given the high popula- This influences both the total number of cyclones
tion density here. Some specific differences between found and the seasonal changes. Other factors are, for
individual methods can be explained—for example, a example, the inclusion or exclusion of so-called open
somewhat smoother pattern in M21 due to the nature systems (without closed pressure contours), which
of the preprocessing prior to the cyclone identification influences primarily the total number, or the choice
and tracking. Any kind of smoothing of input data has of a minimum distance between two cyclone centers,
a similar effect as using lower-resolution data. Different which influences the total number but might also
studies have shown that using lower-resolution data influence the difference between summer and winter
in general decreases the number of detected cyclones because cyclones tend to be larger in winter.
(e.g., Blender and Schubert 2000; Pinto et al. 2005). In the SH, somewhat smaller ranges and devia-
The generally low numbers detected by method M03 tions of total numbers are found (Table 3, first row
relate mainly to one aspect of its unique approach: the and column for summer and winter, respectively).
application of a cutoff to retain only the 25 cyclones More cyclone tracks are on average detected in austral
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 535
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

Table 2. Number of cyclones in the NH (30°–90°N) for summer (JJA, first column) and winter (DJF, first
row) detected by each method, and track agreement between methods for summer (lower-left triangular
matrix) and winter (top-right triangular matrix). Values denote a nominal percentage agreement (relative
to the lower number of tracks produced by the two methods) when both methods detect a track at a
similar place and time (see supplement B “Method of track-to-track comparison” for more details).
Values ≥50% are shaded (blue for winter, red for summer) with dark shading for ≥70%. In deriving this
table, mountain areas (>1,500 m MSL) have been excluded.
Method JJA M02 M03 M06 M08 M09 M10 M12 M13 M14 M15 M16 M18 M20 M21 M22
DJF ×100 147 57 205 95 168 111 124 72 70 120 111 214 158 105 102
| M02 123 | 100 68 | 53 65  | 52 60  | 53 67  | 66 61  | 57 50  | 45 39  | 59  |
| ------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | --- |
| M03 51  | 52 100 | 72 68  | 74 67  | 66 54  | 50 69  | 65 68  | 67 41  | 63  |
| M06 207 | 51 63  | 100 68 | 49 65  | 59 71  | 66 60  | 60 44  | 45 61  | 61  |
| M08 125 | 40 61  | 56 100 | 80 63  | 67 67  | 64 70  | 69 62  | 70 35  | 65  |
| M09 285 | 55 73  | 48 77  | 100 66 | 66 75  | 74 71  | 77 45  | 60 38  | 80  |
| M10 99  | 38 52  | 62 57  | 71 100 | 55 64  | 60 58  | 55 63  | 55 34  | 55  |
| M12 282 | 51 62  | 44 65  | 50 60  | 100 71 | 65 56  | 64 50  | 58 31  | 62  |
| M13 82  | 46 46  | 61 59  | 74 47  | 68 100 | 53 68  | 68 65  | 67 39  | 69  |
| M14 82  | 48 43  | 60 59  | 76 45  | 71 45  | 100 66 | 70 65  | 68 39  | 65  |
| M15 132 | 47 62  | 50 53  | 69 50  | 59 55  | 55 100 | 57 55  | 57 36  | 61  |
| M16 155 | 44 60  | 49 61  | 74 56  | 66 61  | 66 51  | 100 56 | 69 33  | 69  |
| M18 183 | 39 54  | 42 43  | 40 57  | 41 50  | 52 40  | 40 100 | 42 48  | 57  |
| M20 236 | 50 65  | 42 67  | 60 62  | 53 66  | 71 58  | 67 38  | 100 35 | 72  |
| M21 87  | 42 52  | 61 57  | 68 58  | 58 44  | 44 56  | 55 55  | 59 100 | 32  |
| M22 147 | 39 44  | 48 37  | 52 33  | 47 42  | 47 39  | 38 32  | 46 35  | 100 |
Table 3. As in Table 2, but for the SH (30°–90°S).
Method JJA M02 M03 M06 M08 M09 M10 M12 M13 M14 M15 M16 M18 M20 M21 M22
| DJF ×100 | 89 43  | 177 91 | 129 104 | 154 60 | 58 88  | 88 222 | 113 77 | 72  |
| -------- | ------ | ------ | ------- | ------ | ------ | ------ | ------ | --- |
| M02 133  | 100 60 | 56 51  | 57 55   | 54 55  | 57 56  | 48 59  | 49 37  | 56  |
| M03 38   | 54 100 | 70 63  | 71 65   | 57 44  | 47 69  | 55 72  | 60 39  | 54  |
| M06 204  | 55 77  | 100 62 | 54 63   | 41 63  | 66 65  | 58 50  | 51 68  | 66  |
| M08 91   | 44 70  | 70 100 | 75 61   | 65 64  | 68 65  | 60 60  | 62 37  | 71  |
| M09 120  | 39 77  | 62 79  | 100 61  | 57 70  | 74 76  | 73 51  | 64 40  | 81  |
| M10 120  | 37 72  | 65 66  | 58 100  | 53 56  | 62 59  | 55 66  | 51 41  | 63  |
| M12 108  | 41 61  | 59 63  | 63 55   | 100 68 | 73 62  | 71 42  | 60 40  | 71  |
| M13 59   | 59 42  | 72 54  | 57 56   | 57 100 | 53 61  | 62 61  | 62 35  | 61  |
| M14 61   | 54 55  | 74 74  | 79 70   | 68 46  | 100 63 | 65 67  | 69 38  | 65  |
| M15 111  | 42 79  | 65 74  | 72 73   | 59 57  | 74 100 | 56 64  | 60 39  | 66  |
| M16 86   | 46 61  | 68 67  | 77 63   | 66 52  | 71 69  | 100 56 | 64 34  | 69  |
| M18 244  | 45 80  | 51 67  | 61 68   | 58 64  | 73 64  | 65 100 | 50 55  | 63  |
| M20 101  | 40 66  | 61 65  | 70 56   | 56 53  | 72 63  | 66 59  | 100 36 | 71  |
| M21 103  | 41 73  | 66 62  | 62 60   | 49 52  | 73 61  | 60 67  | 53 100 | 34  |
| M22 78   | 47 63  | 71 73  | 82 69   | 69 52  | 71 75  | 73 69  | 71 66  | 100 |
winter than in austral summer (by 9 out of the 15  In Tables 2 and 3 we show the results of a track-
schemes), probably because heat lows play a more  by-track comparison following the approach of
minor role in the SH due to reduced landmass. Blender and Schubert (2000) (for a description see
536 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

supplement B “Method of track-to-track comparison,” (minimum central pressure), lifetime, and propa-
available online at http://dx.doi.org/10.1175/BAMS- gation speed for the respective winter season in
D-11-00154.2) that matches up individual cyclone tra- both hemispheres. The distribution of intensities
jectories generated by the different methods. Overall, (Figs. 3a,b) does not exhibit particularly large
the matching rate ranges from roughly 50% to 70%. variations across methods. The largest variability
This seems reasonable in view of the differences in occurs for the weakest category. The application of
the methods’ approaches. The lower matching values a statistical [Kolmogorov–Smirnov (k–s)] test shows
for M21 might be again attributable to its preprocess- that in the NH four schemes (M02, M03, M13, and
ing of the input data. It is
worth noting that M06,
which is the only method
using 12-hourly input data,
exhibits “average” match-
ing relative to all other
methods, suggesting that
the larger time resolution
does not produce particu-
larly large differences. On
the other hand, methods
M02 and M10, both based
on the same initial algo-
rithm, do not exhibit par-
ticularly high matching
rates. This shows that dif-
ferences between methods
cannot be immediately
attributed to specific
method features but are
more likely the result of a
complex interplay between
the different approaches,
the different threshold
parameters used, and the
different thresholds applied
with those parameters.
In general, the methods
agree better for winter
cyclones than for summer
cyclones in both hemi-
spheres. Part of the reason Fig. 3. Normalized distribution and statistical spread between methods of
different cyclone life cycle characteristics, in box–whisker format: (a),(b)
for this might be that
cyclone intensity (= minimum central pressure), (c),(d) lifetime, and (e),(f)
cyclones in winter are
speed (= mean propagation speed of cyclone center) for the (left) NH (DJF)
deeper and thus more easily
and (right) SH (JJA) winter season (box–whisker plots). Each bar indicates the
detected. fraction of cyclones detected in the parameter range denoted by the x-axis
labels on either side. The horizontal line indicates the mode of all methods
CYCLONE LIFE CYCLE and the box the standard deviation; the whiskers extend to the maximum
CHARACTERISTICS. and minimum values. For example, in the upper-left panel, the bar between
970 and 980 hPa indicates that on average about 10% (= fraction of 0.10 indi-
In this section, we look at
cated on the y axis) of the cyclones detected in NH winter have a minimum
statistics of the life cycles
central pressure between 970 and 980 hPa. The standard deviation of this
of the detected cyclones.
value between methods is 8%–13%; the values for all methods are between
Figure 3 shows the normal- 6% and 15%. The tails of the distributions beyond the given ranges are not
ized occurrence distribu- shown; they include, for example, extreme values, which are of importance
tions of cyclone intensity but require special analysis.
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 537
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

M18) have maximum intensity distributions that are stage and, thus, demonstrate potentially a somewhat
significantly different (95% level) from those of the longer lifetime. However, a robust corresponding
other methods. In the SH only two of them (M02 and pattern discriminating methods using vorticity or
M18) have distributions that are significantly differ- MSLP could not be detected in the analysis (not
ent from the others. shown). On the other hand, if the reason was related
The percentage of “deep” cyclones (defined as to the identification of short-living local depressions,
those with core pressure <960 hPa in the NH and one would expect the three methods producing high
<950 hPa in the SH, with the different thresholds fractions of short-living cyclones to be among those
reflecting deeper cyclones seen generally in SH) with high numbers of shallow cyclones, but this is
compared to the total number varies from 2% to only the case for one of the three.
8% (M18 and M22, respectively) in NH winter, and Moreover, there is also the possibility that some
from 4% to 12% (M18 and M13, respectively) in the methods connect features that are actually not the
SH winter. The low percentage of deep cyclones in same physical entity, which would artificially skew
method M18 can be explained by the highest overall the lifetime distribution toward longer lifetimes.
winter number of detected cyclones by this method The distribution of the mean propagation
(see Tables 2 and 3), since methods generally have velocities (Figs. 3e,f) also shows somewhat higher
better skill in identifying deep cyclones compared variance in the classes of lower velocities. Some
to shallow ones. Therefore, high numbers in certain strange behavior is also apparent for very high system
methods might plausibly originate from there being velocities (beyond about 80 km h–1; not shown).
higher numbers of moderate and shallow cyclones. Note that in extreme cases cyclones can move at
However, while this reasoning seems adequate over 110 km h–1. Differences in the distributions of
for M18, this result does not apply generally. For propagation velocities might be partly associated
example, only a few methods showing the highest with the tendency of some schemes to terminate the
fraction of very weak cyclones demonstrate high trajectories when rapid cyclone translation occurs,
total numbers at the same time. Thus, there must be which is a known problem in many algorithms.
other important method-related influences on this Different tracking approaches, both those looking
distribution. Moreover, the exclusion of cyclones for the nearest neighbors in a defined distance as well
over mountainous terrain does not result in statisti- as those extrapolating cyclone velocities, can miss
cally significant changes in the distributions (not fast-moving cyclones. In the first case this is due to
shown). One exception to this picture was a slight cyclones moving farther than the predefined distance,
shift toward deeper cyclones, especially in winter, and in the second case due to rapid acceleration or
as we would expect since cyclones over high terrain deceleration of cyclones. Some fast-moving cyclones,
are shallower in general. by virtue of being associated with stronger upper-level
The analysis of the lifetime distribution jets, are more likely, because of energy conversions,
(Figs. 3c,d) also shows the largest spread for short- to give rise to an extreme windstorm, so the correct
living cyclones. Those schemes (M03, M09, and handling of system velocities is clearly important.
M21) that produce a high percentage of short-living Identification of the specific features of different
transients (1–2 day) in both NH and SH winter might, algorithms responsible for the above is a challenging
for example, be (i) more restrictive in capturing the task and is left for future in-depth analysis.
first and/or the last stages of cyclone lifespan or (ii)
tend to repeatedly produce tracks associated with CASE STUDIES. In section “Climatology of
short-living local and often weak depressions. For midlatitude cyclone characteristics” we showed that
those methods showing remarkably smaller counts track-to-track matching rates for different schemes
of short-living cyclones and higher fractions of are in most cases at the 50%–70% level. In this section,
longer-living transients (M02 in NH and SH, M12 two case studies, one from each hemisphere, are
and M14 in NH), the respective opposite might apply. analyzed in detail to assess the performance of the
However, there is no evidence from our results that different tracking algorithms for two fast-developing,
either of the two suggested reasons above are a major high-impact storms.
factor: on the one hand, if the main reason for more The first case is the NH storm “Klaus,” which hit
short-living cyclones were related to the identifica- southwestern Europe in late January 2009 (Liberato
tion of cyclones at an early stage, one would expect et al. 2011; Bertotti et al. 2012) with particularly strong
that the schemes using relative vorticity would be impacts over northern Spain and southwestern
more skillful in identifying cyclones at a very early France. The cyclone developed over the subtropical
538 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

North Atlantic Ocean on 21–22 January 2009, moved 25 January, where the system was characterized by
eastward embedded in the strong westerly flow, and two pressure minima: one located over southern
underwent explosive development during 23 January France and a deeper one over the Gulf of Genoa
2009. The storm then moved rapidly into the Bay of (Liberato et al. 2011; see Fig. 4d). At this stage, some
Biscay and then propagated further to the western methods started to follow different minima when
Mediterranean. building the tracks, resulting in the spread of trajecto-
Most methods agree well in the identification of ries and central core pressure as displayed in Figs. 4b
the positions of this storm throughout most of its life and 4c. This is likely due to method differences in the
cycle (Fig. 4a), particularly during the phase of explo- tracking procedure. However, the “choice” of which
sive development and its propagation into the western cyclone to follow in the case of splitting of cyclones or
Mediterranean on 23 and 24 January. However, there in case of generation of a new cyclone near an existing
are some significant differences in the details of the one made by an automated algorithm is not clear, and
life cycle, for example, in lifetime: many methods do differences will always occur.
not identify a cyclone track at the earlier stage of the With most methods, the storm exhibited deep-
development (22 January), and there is substantial ening rates of 35 hPa (24 h)–1 during its maturing
disagreement in the lysis (dissolution of the cyclone) stage. Although all methods except for one agree
position. In particular, the earliest identification of on the time of the minimum central pressure, the
the storm is at 0000 UTC 22 January (by method corresponding values vary within a range of 9 hPa
M02), and the latest is on 0600 UTC 27 January (M16). (965.5–974.5 hPa). The reasons for this lie partially
Considerable differences were found in the exact in the preprocessing of the input data, and also the
location of the cyclone positions over the western and manner in which a scheme interpolates to the location
central Mediterranean (Fig. 4b), resulting in different of the lowest pressure. For example, the preprocessing
minimum central pressures (Fig. 4c). in M21 that leads to smoothing may be of importance
Discrepancies in the cyclone positions appear in areas with weak large-scale pressure gradients like
mainly between 1200 UTC 24 January and 1800 UTC the Mediterranean.
Fig. 4. Detailed track comparison for NH storm Klaus (22–27 Jan 2009). The tracks of available methods are
shown in different colors (see legend). (a) Complete track, (b) detail for the Alpine/north Mediterranean area,
and (c) core pressure evolution. (d) The weather chart shows the synoptic situation on 0000 UTC 25 Jan with
two cyclones over the Mediterranean.
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 539
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

The second selected case study (Fig. 5) involves a its reintensification (Fig. 5b). A large disagreement
deep cyclonic storm that affected southwest Western between the methods appears on 26 May, where some
Australia and southeast Australia in late May 1994. tracks start to follow a path toward New Zealand
It induced high winds and significant rainfall during (M03, M10, M18, and M21) while some others turn
23 and 24 May 1994. Over the next days the cyclone to the south. As in the first case study, the handling
moved southeastward across the Great Australian of this splitting (see Fig. 5b) by the methods might
Bight. On 24 and 25 May a strong cold front associ- be quite sensitive and can be induced by only minor
ated with the cyclone caused a large dust storm that algorithm differences.
affected parts of South Australia, New South Wales, Figure 5c displays the central core pressure between
and Victoria (McInnes and Hubbert 1996; Trewin 0000 UTC 22 and 0000 UTC 29 May of different
2002). methods. Generally, its evolution is similar among the
The cyclone was successfully tracked by all different methods. However, after the period of the
methods (Fig. 5a). A drop in central pressure of most intense development at 0600 UTC 24 May, the
about 30 hPa (24 h)–1 was consistently captured by minimum central pressure differs by 10 hPa (between
the different schemes from 0600 UTC 23 May to 961.9 hPa in M08 and 971.6 hPa in M06; interpolated
0600 UTC 24 May. All algorithms also perform simi- in time for M06). For the second pressure minimum
larly during the intense phase (23–26 May), although during reintensification on 1200 UTC 26 May the
differences in positions span about two grid lengths spread of 3.5 hPa is smaller, ranging between 961.8 hPa
(relative to input data resolution; ~300 km). There (M08) and 965.3 hPa (M06).
are much larger differences in general at the stages For these two examples all methods agree in the
of genesis and lysis. For instance, M02 captures a replication of the main segment of the track of a large
storm earliest, while M20 and M22 follow a track cyclone, associated with the mature stage including
for longest during storm decay. Most methods iden- explosive development. However, large scheme-to-
tify the storm track from 26 to 29 May 1994 after scheme differences in both position and central core
Fig. 5. Detailed track comparison for an SH storm (unnamed; 22–29 May 1994). The available methods are
shown in different colors (see legend). (a) Complete track, (b) detail for the central section of the track, and
(c) core pressure evolution. (d) The weather chart shows the synoptic situation at the time after the splitting
of the tracks on 0000 UTC 27 May.
540 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

pressure exist during the genesis and the dissolution INTERANNUAL VARIABILITY AND
phases, showing that the end-to-end tracking of high- TRENDS. Past and future trends in cyclone char-
impact weather systems has many nontrivial aspects. acteristics are an important issue in the discussion of
Future work will reveal if for other cases the explosive climate change impacts. In this context, the knowl-
development phase is captured equally well, as this edge of interannual and decadal variability is indis-
may not always be the case. pensable for assessing the importance of observed or
Fig. 6. Time series of (a),(b) NH and (c),(d) SH cyclone center counts in NH (DJF) and SH (JJA) winter, respec-
tively. Deep cyclones here are those with core pressure ≤980 hPa (only for methods that output cyclone core
pressure; for “deep cyclones” only time steps where the pressure is ≤980 hPa are counted). Note that for M06
cyclone counts have been doubled to account for its unique 12-h time step.
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 541
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

projected trends. Although a comprehensive diag- deep cyclones. The source of the particularly high
nosis of long-term trends versus natural variability number of deep cyclones in M02 might be associ-
is not possible in our study, given the short 20-yr ated with the deeper core pressures detected by M02
dataset used, it is important to quantify whether an compared to other methods. The specific reason for
overall agreement (or disagreement) of the trend sign that will be further analyzed in future work. Figure 6
and magnitude as well as interannual variability over demonstrates a striking similarity in the year-to-year
this time interval exists between different tracking variability between methods, especially for deep
schemes. This provides information on the robust- cyclones. Interannual variations of cyclone counts,
ness against method uncertainties of long-term trend in percentage terms, thus seem to depend very little
signals detected in studies using a single method. on the method chosen.
Time series of hemispheric seasonal cyclone center The analysis of the 20-yr trends of seasonal hemi-
counts for the NH and SH winter season are shown in spheric cyclone center counts shows that in the NH
Fig. 6. Note that “count” here means all centers found most methods identify a significant increase in the
at any time step (see sidebar). Complementary to the total number of cyclone centers (Fig. 7a) over the
discussion in section “Climatology of midlatitude 1989–2009 period, but with considerable quantita-
cyclone characteristics,” Fig. 6 shows that although tive differences. The number of deep cyclone centers,
the scheme-to-scheme spread in total numbers of however, consistently decreases (although mostly
cyclones is wide, different methods are rather robust insignificantly) with all methods (Fig. 7b), with a
in counting deep cyclones throughout the 20-yr somewhat smaller spread between methods than
period, albeit with two outliers in both hemispheres for total numbers. In the SH, all but one method
(M02 and M03, Figs. 6b and 6d). The reason for find positive trends for total cyclone center counts,
these outliers at first sight seems to be the high and as well as a weak (mostly statistically insignificant)
the low overall numbers. However, as we argued increase in the number of deep cyclone centers in
earlier, the correlation between total numbers and austral summer (Figs. 7c,d). The spread between trend
the number of deep cyclones is low, because we estimates derived from different methods is gener-
expect all algorithms to detect deep cyclones more ally larger in the SH than in the NH, and SH trends
effectively. In case of M03, the restriction of the estimated by different methods for the same season
number of cyclones per analysis (which selects the could have opposite signs.
25 strongest cyclones per time step) seems to reduce Hemispherically averaged trends do not provide
not only the overall number but also the number of information about regional shifts of cyclone
Fig. 7. Trends (per year, in % of the mean; least squares estimates) in time series of (a) NH total cyclone center
counts, (b) NH deep cyclone center (core pressure ≤980 hPa) counts, (c) SH total cyclone center counts, and
(d) SH deep cyclone center counts in DJF and JJA (series shown in Fig. 6). The error bars represent the 95%
confidence range of the trend estimate (a trend is significant at 5% level if the error bar does not include zero).
542 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

occurrence. Because of their regional importance, methods) of track density for the NH (Figs. 8a,b) and
we also investigated spatial patterns of trends in SH (Figs. 8c,d; contour lines). The agreement between
winter track density. Figure 8 shows the winter trend the methods is analyzed by examining the number of
patterns of the multimethod ensemble (average of all methods that exhibit a significant positive (Figs. 8a,c)
Fig. 8. Geographical patterns of 20-yr winter trends of cyclone track density. The color scale represents the
number of methods with a significant (a) positive and (b) negative relative trend (significance level of p > 90%)
in the Northern Hemisphere (DJF); the contour lines represent the magnitude of the method ensemble-mean
relative trend (in % change per year, of the average yearly track density). (c),(d) As in (a) and (b), respectively,
but for SH (JJA).
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 543
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

and negative (Figs. 8b,d) trend sign, respectively (color expected result, since intense cyclones show distinct
scale). In the NH, several regions show a relatively values for most variables that different methods might
large ensemble trend (contour lines), for example, over use for identification, and thus they will be captured
the Atlantic (negative; Fig. 8b), central Europe, and by most methods. Thus, the identification of intense
the northeast Pacific (positive; Fig. 8a). The closest cyclones and the part of their life cycle with intense
agreement between methods was found in these development looks to be most robust with respect
areas of most distinct signals where a high number of to choice of the method. However, even for these
methods show a significant positive or negative trend, intense events, there can be significant differences in
respectively (Figs. 8a,b), and all methods show the life cycle characteristics, in particular during genesis
same sign of trend (not shown). In the SH, ensemble and lysis phases of the cyclones and, related to these,
trends in cyclone track density reveal regions with lifetime. Furthermore, the robustness of estimates of
strong positive signals (Fig. 8c) in the Atlantic sector cyclone propagation speed is a concern, since there is
(60°W–0° at around 40°–50°S), in the Indian Ocean a hint that some schemes might not recognize rapid
sector (about 90°E, 45°–55°S), and north of the Ross movement. This will be investigated in future work.
Sea. As in the NH, regions with strong ensemble With respect to numbers of cyclones, a qualitative
trends coincide with regions of a close method-to- “pattern matching” agreement between methods is
method agreement with high numbers of methods obtained in terms of interannual variability and in
with a corresponding significant trend (Figs. 8c,d), geographical distribution, although there are some
and all methods exhibiting the same trend sign. In important differences in certain regions, notably the
regions where the ensemble trend is weak, trends may Mediterranean. Differences in absolute total numbers
often differ in sign across methods, but, reassuringly, of cyclones are particularly large and imply caution
there are very few areas where there are methods that when comparing corresponding results from studies
exhibit significant trends with opposite sign. using single but different methods. Analysis of life
Large areas with significant trends of the same cycle characteristics in general shows a reasonable
sign across the methods present evidence for the agreement. The largest spread in the frequency dis-
presence of physically meaningful regional trend tributions was found for short-living, shallow, and
signals, because (i) there is overwhelming method slowly moving cyclones, whose detection is more
consistency and (ii) large structures are unlikely to sensitive to the choice of scheme. Differences in the
be generated by noise alone, whereas small areas distributions are generally larger in the NH than in
of significant trends could occur by chance. The the SH and are larger over parts of continents (e.g.,
comparison of the method agreement in trend sign Europe, North America, the Mediterranean), which
between track density, cyclone genesis, and lysis (not are regions of high interest because storm impacts
shown) indicates that signals detected for the field of are high there.
track density are more consistent than for genesis and An important result specifically relevant to the
lysis locations. The location of the beginning or end of analysis of climate change impacts is the qualitative
a track is thus more sensitive to the cyclone identifica- consistency shown for geographical linear trend
tion method used, as suggested earlier in the paper. patterns, where regions with strong trends show a
good agreement, at least in sign, over most methods.
DISCUSSION AND CONCLUSIONS. This is an important consideration when trying to
Fifteen cyclone detection and tracking methods are disentangle genuine trends in cyclone activity from
compared using the same input dataset in order to natural variability and method uncertainty, and
assess their similarities and differences. For cyclone accordingly trying to quantify the statistical sig-
characteristics, for which the results from different nificance of any long-term trends being highlighted
methods are robust, estimates from a single method (Hodges 2008; Löptien et al. 2008; Della-Marta and
can be taken with a certain confidence. Consistency Pinto 2009; Sienz et al. 2010).
across the methods is generally higher for deep (or Another key result is that it has so far proved
strong) cyclones than for shallow ones. This conclu- difficult to clearly associate differences in the iden-
sion seems to hold also for cyclone frequency and tified cyclone characteristics with features of the
life cycle, as well as for characteristics of interannual different schemes. In a few cases, outlier behavior
variability and trends. In the two cyclone case studies can be explained by specific features of certain
consistency across methods was best for the most methods, like the preprocessing in method M21 or
intense part of the life cycles, rather than the periods the restriction of the number of cyclones in method
of development and lysis. To some extent this is an M03. In general, and somewhat surprisingly, we have
544 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

found little evidence of clustering of cyclone statis- will be undertaken in the next phase of this ongoing
tics according to algorithm features (e.g., vorticity project. For now, IMILAST provides the commu-
schemes vs. MSLP schemes). Also, we see no detect- nity with a unique, comprehensive, and updatable
able outlier performance for the sole method using database for analyzing the performance of cyclone
a lower time resolution (M06) and no significantly tracking algorithms. We anticipate that further
better agreement in the results of two algorithms analysis of regional features, of other cyclone char-
that are based on the same original method (M02 acteristics, and other case studies will involve a still
and M10). Furthermore, in the two case studies four wider community. Not all existing algorithms are
methods clearly show shallower cyclones than the included in this paper; for example, the algorithm
others, though the algorithms are unrelated. This all from Hodges et al. (1995) is missing, but we hope to
indicates that the documented differences result from add more in further work.
a complex interplay between different aspects of each There are many future developments that could
method. Threshold settings for identifying centers are play a positive role in improving our knowledge
believed to be one key aspect, while the algorithms of cyclone climatology, for the benefit of society.
that build tracks, and the pre- or postprocessing of One would be generating a “best-track dataset” for
input and output data also are very relevant. extreme extratropical cyclones, as already exists for
When dealing with the complex and multifac- tropical cyclones. This would be a good basis for the
eted character of these synoptic features, this study next step within IMILAST, which is to extend the
has shown that an ensemble of cyclone schemes has comparison of method-related differences for a set of
the potential to extract the key relevant features. extreme cyclones (i.e., a set of further case studies).
Nevertheless, some findings might look some- Others would be to improve reanalysis datasets to the
what discouraging in view of the importance of point where they are better able to represent fine-scale
extratropical cyclones and their impact, but this structures of extratropical cyclones, or the exten-
has to be expected given the complexity of these sion of cyclone identification schemes to examine
features. Since there is no universal agreement upon vertical structures of cyclones (e.g., Dacre et al. 2012;
cyclone definition, we cannot “judge” the algo- Kouroutzoglou et al. 2012; Čampa and Wernli 2012).
rithms or say that a specific one delivers “incorrect” These developments will require concerted interna-
results. They are all “right” in some sense. The many tional efforts for realization.
different approaches each have their own strengths
and weaknesses, and each brings valuable perspec- ACKNOWLEDGMENTS. We thank Swiss Re for
tives to bear. They are all based on a similar physi- sponsoring the project (coordination office and workshops)
cal understanding of complex processes, but deal and ECWMF for providing the input data of ERA Interim.
with this in different ways. However, this makes it C. C. Raible is supported by NCCR Climate, funded by the
somewhat problematic for users of such results; they Swiss National Science Foundation. M. L. R. Liberato was
may lack guidance when assessing the results from supported by the project STORMEx (FCOMP-01-0124-
different studies using different schemes, especially FEDER-019524), funded by FCT and cofunded by FEDER.
if the results contradict each other. In this sense, the N. Bellenbaum, J. G. Pinto, and S. Ulbrich thank AON
findings of this study constitute important informa- Benfield Impact Forecasting for support over the EUWS
tion for the interpretation of results of any extratropi- project. J. Grieger and M. Schuster are supported by the
cal cyclone analysis that uses only one identification DFG project SACAI (DFG-LE1865/1–3). M. G. Akperov
and tracking algorithm. In particular, our study and I. I. Mokhov are supported by the Russian Ministry of
shows which aspects of cyclone identification and Education and Science (11.519.11.5004). We appreciate the
tracking are likely to be independent of the method lead authorship of C. C. Raible, S. Gulev, J. G. Pinto, G. C.
used (and thus deserve higher confidence) and which Leckebusch, and X. L. Wang, respectively, for the different
aspects should be treated with caution. Thus, if using analysis sections of this paper.
a single method, one should be aware of the sensitivity
of results to the method, in particular with respect
REFERENCES
to total cyclone counts and the role of weak cyclones
in the statistics. Akperov, M. G., M. Yu, E. Bardin, M. Volodin, G. S.
Diagnosing the key reasons for differences in Golitsyn, and I. I. Mokhov, 2007: Probability dis-
portrayed characteristics will involve more detailed tributions for cyclones and anticyclones from the
study, especially sensitivity studies for specific pa- NCEP/NCAR reanalysis data and the INM RAS cli-
rameters with a number of individual methods, and mate model. Izv., Atmos. Oceanic Phys., 43, 705–712.
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 545
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

Allen, J. T., A. B. Pezza, and M. T. Black, 2010: Explosive Hodges, K. I., 1995: Feature tracking on the unit sphere.
cyclogenesis: A global climatology comparing mul- Mon. Wea. Rev., 123, 3458–3465.
tiple reanalyses. J. Climate, 23, 6468–6484. —, 2008: Confidence intervals and significance tests
Bardin, M. Yu., and A. B. Polonsky, 2005: North Atlantic for spherical data derived from feature tracking.
oscillation and synoptic variability in the European- Mon. Wea. Rev., 136, 1758–1777.
Atlantic region in winter. Izv., Atmos. Oceanic Phys., —, B. J. Hoskins, J. Boyle, and C. Thorncroft, 2003:
41, 127–136. A comparison of recent reanalysis datasets using
Benestad, R. E., and D. Chen, 2006: The use of a objective feature tracking: Storm tracks and tropi-
calculus-based cyclone identification method for cal easterly waves. Mon. Wea. Rev., 131, 2012–2037.
generating storm statistics. Tellus, 58A, 473–486. —, R. W. Lee, and L. Bengtsson, 2011: A comparison
Bengtsson, L., K. I. Hodges, and N. Keenlyside, 2009: of extratropical cyclones in recent reanalyses ERA-
Will extratropical storms intensify in a warmer Interim, NASA MERRA, NCEP CFSR, and JRA-25.
climate? J. Climate, 22, 2276–2301. J. Climate, 24, 4888–4906.
Bertotti, L., and Coauthors, 2012: Performance of dif- Hoskins, B. J., and K. I. Hodges, 2002: New perspectives
ferent forecast systems in an exceptional storm in the on the Northern Hemisphere winter storm tracks.
Western Mediterranean Sea. Quart. J. Roy. Meteor. J. Atmos. Sci., 59, 1041–1061.
Soc., 138, 34–55. Inatsu, M., 2009: The neighbor enclosed area tracking
Blender, R., and M. Schubert, 2000: Cyclone tracking algorithm for extratropical wintertime cyclones.
in different spatial and temporal resolutions. Mon. Atmos. Sci. Lett., 10, 267–272.
Wea. Rev., 128, 377–384. Jung, T., S. K. Gulev, I. Rudeva, and V. Soloviov, 2006:
—, K. Fraedrich, and F. Lunkeit, 1997: Identification of Sensitivity of extratropical cyclone characteristics to
cyclone-track regimes in the North Atlantic. Quart. horizontal resolution in the ECMWF model. Quart.
J. Roy. Meteor. Soc., 123, 727–741. J. Roy. Meteor. Soc., 132, 1839–1858.
Čampa, J., and H. Wernli, 2012: A PV perspective on Kew, S. F., M. Sprenger, and H. C. Davies, 2010: Potential
the vertical structure of mature midlatitude cy- vorticity anomalies of the lowermost stratosphere:
clones in the Northern Hemisphere. J. Atmos. Sci., A 10-yr winter climatology. Mon. Wea. Rev., 138,
69, 725–740. 1234–1249.
Dacre, H. F., M. K. Hawcroft, M. A. Stringer, and K. I. Kouroutzoglou, J., H. A. I. Flocas, K. Keay, I. Simmonds,
Hodges, 2012: An extratropical cyclone atlas: A tool and M. Hatzaki, 2012: On the vertical structure of
for illustrating cyclone structure and evolution. Bull. Mediterranean explosive cyclones. Theor. Appl.
Amer. Meteor. Soc., 93, 1497–1502. Climatol., 110, 155–176, doi:10.1007/s00704-012-
Dee, D. P., and Coauthors, 2011: The ERA-Interim 0620-3.
reanalysis: Configuration and performance of the Leckebusch, G. C., B. Koffi, U. Ulbrich, J. G. Pinto,
data assimilation system. Quart. J. Roy. Meteor. Soc., T. Spangehl, and S. Zacharias, 2006: Analysis of
137, 1972–1990. frequency and intensity of winter storm events in
Della-Marta, P. M., and J. G. Pinto, 2009: Statistical un- Europe on synoptic and regional scales from a mul-
certainty of changes in winter storms over the North timodel perspective. Climate Res., 31, 59–74.
Atlantic and Europe in an ensemble of transient Liberato, M. R. L., J. G. Pinto, I. F. Trigo, and R. M. Trigo,
climate simulations. Geophys. Res. Lett., 36, L14703, 2011: Klaus—An exceptional winter storm over north-
doi:10.1029/2009GL038557. ern Iberia and southern France. Weather, 66, 330–334.
Hanley, J., and R. Caballero, 2012: Objective identifica- Lionello, P., F. Dalan, and E. Elvini, 2002: Cyclones in the
tion and tracking of multicentre cyclones in the ERA- Mediterranean region: The present and the doubled
Interim reanalysis data set. Quart. J. Roy. Meteor. CO climate scenarios. Climate Res., 22, 147–159.
2
Soc., 138, 612–625. Löptien, U., O. Zolina, S. K. Gulev, M. Latif, and
Hewson, T. D., 1997: Objective identification of frontal V. Soloviov, 2008: Cyclone life cycle characteristics
wave cyclones. Meteor. Appl., 4, 311–315. over the Northern Hemisphere in coupled GCMs.
—, and H. A. Titley, 2010: Objective identification, Climate Dyn., 31, 507–532.
typing and tracking of the complete life-cycles of McInnes, K. L., and G. D. Hubbert, 1996: Extreme
cyclonic features at high spatial resolution. Meteor. events and the impact of climate change on Victoria’s
Appl., 17, 355–381. coastline. Environment Protection Authority, State
—, G. C. Craig, and C. Claud, 2000: Evolution and Government of Victoria Publ. 488, 69 pp.
mesoscale structure of a polar low outbreak. Quart. Murray, R. J., and I. Simmonds, 1991: A numerical
J. Roy. Meteor. Soc., 126, 1031–1063. scheme for tracking cyclone centers from digital data.
546 | APRIL 2013
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

Part I: Development and operation of the scheme. Simmonds, I., R. J. Murray, and R. M. Leighton, 1999:
Aust. Meteor. Mag., 39, 155–166. A refinement of cyclone tracking methods with data
Pinto, J. G., T. Spangehl, U. Ulbrich, and P. Speth, 2005: from FROST. Aust. Meteor. Mag., Special Issue, 35–49.
Sensitivities of a cyclone detection and tracking —, C. Burke, and K. Keay, 2008: Arctic climate
algorithm: Individual tracks and climatology. change as manifest in cyclone behavior. J. Climate,
Meteor. Z, 14, 823–838. 21, 5777–5796.
—, S. Zacharias, A. H. Fink, G. C. Leckebusch, and Sinclair, M. R., 1994: An objective cyclone climatology
U. Ulbrich, 2009: Factors contributing to the develop- for the Southern Hemisphere. Mon. Wea. Rev., 122,
ment of extreme North Atlantic cyclones and their 2239–2256.
relation with the NAO. Climate Dyn., 32, 711–737. —, 1997: Objective identification of cyclones and their
Raible, C. C., P. M. Della-Marta, C. Schwierz, H. Wernli, circulation intensity, and climatology. Wea. Forecast-
and R. Blender, 2008: Northern Hemisphere extra- ing, 12, 591–608.
tropical cyclones: A comparison of detection and Trewin, B., 2002: Charts from the past—24 May, 1994.
tracking methods and different reanalyses. Mon. Bull. Aust. Meteor. Ocean. Soc., 17, 74.
Wea. Rev., 136, 880–897. Trigo, I. F., 2006: Climatology and interannual vari-
—, B. Ziv, H. Saaroni, and M. Wild, 2010: Winter ability of storm-tracks in the Euro-Atlantic sector:
synoptic-scale variability over the Mediterranean A comparison between ERA-40 and NCEP/NCAR
Basin under future climate conditions as simulated reanalyses. Climate Dyn., 26, 127–143.
by the ECHAM5. Climate Dyn., 35, 473–488. Ulbrich, U., G. C. Leckebusch, and J. G. Pinto, 2009:
Rudeva, I., and S. K. Gulev, 2007: Climatology of cyclone Extra-tropical cyclones in the present and future
size characteristics and their changes during the climate: A review. Theor. Appl. Climatol., 96, 117–131.
cyclone life cycle. Mon. Wea. Rev., 135, 2568–2587. Wang, X. L., V. R. Swail, and F. W. Zwiers, 2006: Clima-
Schneidereit, A., R. Blende, and K. Fraedrich, 2010: A tology and changes of extratropical cyclone activity:
radius–depth model for midlatitude cyclones in re- Comparison of ERA-40 with NCEP/NCAR reanaly-
analysis data and simulations. Quart. J. Roy. Meteor. sis for 1958–2001. J. Climate, 19, 3145–3166.
Soc., 136, 50–60. Wernli, H., and C. Schwierz, 2006: Surface cyclones in
Serreze, M. C., 1995: Climatological aspects of cyclone the ERA-40 dataset (1958–2001). Part I: Novel iden-
development and decay in the Arctic. Atmos.–Ocean, tification method and global climatology. J. Atmos.
33, 1–23. Sci., 63, 2486–2507.
Sienz, F., A. Schneidereit, R. Blender, K. Fraedrich, and Zolina, O., and S. K. Gulev, 2002: Improving accuracy
F. Lunkeit, 2010: Extreme value statistics for North of mapping cyclone numbers and frequencies. Mon.
Atlantic cyclones. Tellus, 62A, 347–360. Wea. Rev., 130, 748–759.
Educators, students, and weather enthusiasts! A glossary
of over 3000 terms on weather and climate designed
specifically for a general audience! Produced under the
GLOSSARY Project ATMOSPHERE initiative, the development of
The Glossary of Weather and Climate was inspired by
OF WEATHER increasing contemporary interest in the atmosphere and
global change. The objective of the glossary is to provide
AND CLIMATE a readily understandable, up-to-date reference for terms
that are frequently used in discussions or descriptions
.
editedbyiraw geer of meteorological and climatological phenomena. In
addition, the glossary includes definitions of related
oceanic and hydrologic terms.
©1996 American Meteorological Society. Available in both hardcover and
softcover, B&W, 272 pages, $26.95 list/$21.00 member (softcover); $34.95
(hardcover) plus shipping and handling. Order online at www.ametsoc.
org/amsbookstore. Please send prepaid orders to Order Department,
American Meteorological Society, 45 Beacon St., Boston, MA 02108-3693.
AMERICAN METEOROLOGICAL SOCIETY APRIL 2013 | 547
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC

AMS MEMBERS
GIVE A GREAT GIF T
AT A GREAT PRICE
Looking for the perfect
present for the weather
enthusiast in your life?
Want to make a valuable
contribution to your local library
or community college? Send a
subscription to Weatherwise
magazine (6 issues) for just
$24.95*—That’s nearly 50% off the
list price!
Written for a general
audience, offers
a colorful and nontechnical
look at recent discoveries in
meteorology and climatology.
Check out the latest table of
contents at www.weatherwise.org.
Want your own?
Then order a personal subscription
at the same great price.
Contact Member Services by e-mail at amsmem@ametsoc.org or by phone at
617-226-3998 to place all of your orders today!
*Cost for delivery outside of the U.S. is $40.95. Weatherwise is available to AMS Members through a cooperative agreement
with Taylor & Francis Group LLC, the publishers of Weatherwise.
Unauthenticated | Downloaded 04/14/26 06:12 PM UTC