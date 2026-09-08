OceanEngineering216(2020)108111
Contents lists available at ScienceDirect
Ocean Engineering
journal homepage: www.elsevier.com/locate/oceaneng
Analysis of Atlantic extratropical storm tracks characteristics in 41 years of
ERA5 and CFSR/CFSv2 databases
C.B. Gramcianinova,b,*, R.M. Camposa, R. de Camargob, K.I. Hodgesc, C. Guedes Soaresa, P.
L. da Silva Diasb
aCentre for Marine Technology and Ocean Engineering (CENTEC), Instituto Superior T´ecnico, Universidade de Lisboa. Rovisco Pais, 1049-001, Lisboa, Portugal
bDepartamento de Ciˆencias Atmosf´ericas, Instituto de Astronomia, Geofísica e Ciˆencias Atmosf´ericas, Universidade de Sa˜o Paulo, Rua do Mata˜o, 1226, Cidade
Universita´ria, Sa˜o Paulo, SP, Brazil
cDepartment of Meteorology, University of Reading, Reading, United Kingdom
A R T I C L E I N F O A B S T R A C T
Keywords: This work aims to analyze and compare ERA5 and CFSR/CFSv2 data from 1979 to 2019 with 1-hourly outputs,
Cyclones regarding their ability to reproduce storm tracks and the main characteristics of cyclones at middle and high
Storm track latitudes in the North Atlantic (NA) and South Atlantic (SA) Oceans. The cyclone tracking was based on relative
Cyclogenesis
vorticity at 850 hPa and the intensity is measured using the maximum 10-m wind speed. The climatology
South Atlantic Ocean
produced for both datasets shows the main characteristics of the NA and SA storm tracks, such as seasonal
North Atlantic Ocean
variability and genesis regions. The use of 1-hourly fields improves tracking in areas with complex terrains, such
Reanalysis
as the lee of Andes (SA) and Greenland (NA). The differences in number of cyclones and their characteristics
between datasets are small. 92.7% and 93.1% of ERA5 cyclones have an identical correspondent storm in CFSR/
CFSv2, in the NA and SA respectively. Genesis and lifetime statistics show that CFSR/CFSv2 may present
inconsistency between forecast and analysis sequential time-steps. Large differences remain in the intensity
distributions, in which the CFSR/CFSv2 presents stronger cyclones than ERA5. Divergences between the datasets
decrease when the comparison is made using only CFSv2, particularly in the South Atlantic.
1. Introduction in the Atlantic Ocean from two modern reanalysis datasets are
compared, the fifth generation of reanalysis from the European Centre
Cyclones are key features of the day-to-day weather variability at for Medium-Range Weather Forecast (ECMWF; Hersbach and Dee,
middle and high latitudes. Storminess is an important risk for offshore 2016) (ERA5), and the Climate Forecast System Reanalysis (CFSR; Saha
structures and ship routing, particularly due to their associated extreme et al., 2010), and Climate Forecast System version 2 (CFSv2; Saha et al.,
winds and waves (Ponce de Leo´n and Guedes Soares, 2014, 2015; Vettor 2014) from the National Center for Environmental Prediction (NCEP).
and Guedes Soares, 2016, 2017). Safe and profitable engineering oper- Besides the analysis of these two datasets and the discussion, an
ations depend on weather forecasts and metocean statistics, the last important contribution of this work is to produce a cyclone database
being usually produced from reanalysis data produced by operational that can be used to support ocean engineering and coastal hazard esti-
centers around the world (Campos et al., 2018, 2019). Transient system mations, together with an evaluation of the main differences between
variability in the extratropics is the contributor to not only errors in the two datasets.
wind-wave forecasts but also to problems associated with the repre- Automated methods for cyclone identification and tracking have
sentation of topographic and sea surface temperature gradient effects in been developed in the past decades, due to the increase of available data
ocean models (Chelton et al., 2004). Cyclone tracks are usually obtained produced by Global Circulation Models (GCMs) and reanalyses, led by
using 6-hourly data sources, which are necessary to produce reliable the improvement of computational resources. These objective methods
cyclone tracks but are insufficient for some ocean engineering problems, are based on a Lagrangian approach that generally uses low-level
such as wave hindcast and forecast models. In this paper cyclone tracks vorticity or surface pressure criteria to identify and track cyclones (e.
* Corresponding author. Departamento de Ciˆencias Atmosf´ericas, Instituto de Astronomia, Geofísica e Ciˆencias Atmosf´ericas, Universidade de Sa˜o Paulo, Rua do
Mat˜ao, 1226, Cidade Universita´ria, Sa˜o Paulo, SP, Brazil.
E-mail address: cbgramcianinov@gmail.com (C.B. Gramcianinov).
https://doi.org/10.1016/j.oceaneng.2020.108111
Received 21 July 2020; Received in revised form 26 August 2020; Accepted 13 September 2020
Availableonline24September2020
0029-8018/©2020ElsevierLtd.Allrightsreserved.

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
g., Murray and Simmonds, 1991a, 1991b; Sinclair, 1994; Hodges, 1994, features that control the wind and wave climates.
1995). Since then, a wide set of cyclone climatologies have been pro-
duced for the Northern Hemisphere (e.g., Hoskins and Hodges, 2002), 2. Data and methods
Southern Hemisphere (e.g., Jones and Simmonds, 1993; Sinclair, 1994;
Simmonds and Keay, 2000; Hoskins and Hodges, 2005), North Atlantic 2.1. Datasets
(e.g., Pinto et al., 2005; Trigo, 2006; Dacre and Gray, 2009; Grise et al.,
2013), and South Atlantic Oceans (e.g., Mendes et al., 2010; Reboita ERA5 is the latest reanalysis produced by ECMWF, available from the
et al., 2010; Gramcianinov et al., 2019). The basic product of the Copernicus Climate Change Service (CS3). This reanalysis has been
tracking method is the collection of cyclone trajectories within a defined produced using 4D-Var data assimilation in ECMWF’s Integrated Fore-
region and period. The spatial statistic distribution of this collection of cast System (IFS), version CY41R2. The atmospheric variables used in
trajectories defines the storm track position – the preferred location of this work are on a 31 km (0.28125◦) horizontal grid with 1-hourly
cyclone propagation. outputs from 1979 to 2020. ERA5 replaces the ERA-Interim, and bene-
Following the development of GCMs, the use of analyses and rean- fits from its antecessor’s development in model physics, core dynamics
alyses was a valuable improvement to the atmosphere and ocean dy- and data assimilation. One of the most important innovations of ERA5 is
namics studies (Parker, 2016). Reanalysis products are based on a model the output of hourly analyses that can widely support risk and opera-
allied to data assimilation, and thus, can provide a complete spatial tional management in diverse sectors, such as renewable energy (e.g.,
coverage at a regular resolution. Despite the verification and validation Olauson, 2018). Moreover, Belmonte Rivas and Stoffelen (2019) found
performed by development centers (e.g., Kalnay et al., 1996; Saha et al., that ERA5 surface winds present a 20% improvement relative to
2010, 2014), it is important to evaluate the performance of these data- ERA-Interim, using ASCAT observations as verification. An overview of
sets for particular applications, such as extratropical and tropical cy- the main characteristics of ERA5 and a comparison with ERA-Interim
clones, and precipitation. Several studies have carried out can be found in Hersbach et al. (2018).
intercomparisons of storm tracks obtained from different datasets for the The CFSR is the latest version of the NCEP climate reanalysis and
whole globe (e.g., Hodges et al., 2003, 2011), Northern Hemisphere (e. covers the period from 1979–March/2011. The reanalysis was produced
g., Raible et al., 2008), North Atlantic sector (e.g., Trigo, 2006) and using a coupled atmosphere–ocean model: the NCEP Global Forecast
South Atlantic sector (Reboita et al., 2018; Crespo et al., 2020a). Hodges System (GFS) for the atmosphere and the Geophysical Fluid Dynamics
et al. (2011) compared the storm track distribution and intensity in four Laboratory Modular Ocean Model version 4 (MOM4) for the ocean (Saha
reanalysis: the Modern Era Retrospective-Reanalysis for Research and et al., 2010). The CFSv2, the operational descendant of the CFSR, was
Applications (MERRA; Rienecker et al., 2011), the 25-yr Japan Rean- released in March 2011, and it has been running operationally since
alysis (JRA25; Onogi et al., 2007), the ECMWF Interim Reanalysis then. The CFSR and CFSv2 have a horizontal native resolution of T382
(ERA-Interim; Simmons et al., 2007), and the CFSR. They found larger (~38 km) interpolated to a 0.5◦ × 0.5◦ grid. Both the reanalysis and
discrepancies between the older and newer products and attributed their analysis are produced originally in 6-hourly intervals, but a 1-hourly
findings to the improvement of data assimilation techniques and in- time series are also available from some variables and consist of the
crease of resolution. According to them, modern reanalysis inter com- analysis followed by the sequence of hourly forecasts until the next
pares better than the older ones for cyclone densities. However, analysis cycle. The hourly sequence provided might have abrupt
differences remain large between CFSR and ERA-Interim for cyclones changes in atmospheric fields every time a forecast time-step changes to
intensities, and also for densities in some regions of the Southern analysis time-step, since the last one is corrected by data assimilation.
Hemisphere. Despite this eventual inconsistency along the period, it is important to
Stopa and Cheung (2014) evaluated 30 years of wind and wave data evaluate the hourly data since these products are used for ocean engi-
from the CFSR and ERA-Interim using altimeter and buoy observations. neering applications. Moreover, it is the only way to compare
While ERA-Interim presented lower error metrics, CFSR showed a better CFSR/CFSv2 with ERA5 1-hourly data. Differences between products
performance in the upper percentiles associated with extreme events. are expected and need to be discussed to support future choices or
The large differences between datasets are generally associated with the changes.
failure in the representation of extreme events (e.g., Stopa and Cheung,
2014; Campos et al., 2018). Winds are often underestimated at some 2.2. Cyclone identification and tracking
locations, mainly in the Southern Hemisphere, due to the lack of
observational data (e.g., Stopa and Cheung, 2014). This problem con- The cyclones are identified and tracked in both reanalyses using the
tributes to the misrepresentation of cyclones, particularly the most TRACK program (Hodges, 1994, 1995; 1999) following the
intense ones, which leads to issues in wind-wave climate hindcast and pre-processing steps described in Hoskins and Hodges (2002, 2005). The
forecast (e.g., Kumar et al., 2003; Campos and Guedes Soares, 2016a, cyclonic features are identified using the relative vorticity, which is
2016b, 2017; Bakhtyar et al., 2018; Mattioli et al., 2019; Campos et al., computed using the zonal and meridional wind components at 850 hPa
2019), and storm surge estimations (e.g., Colle et al., 2010; Booth et al., in spherical coordinates to avoid latitudinal bias (Sinclair, 1997). Sin-
2016; Sebastian et al., 2019). clair (1994) highlighted the benefit of using vorticity instead of mean
Therefore, it is important to evaluate cyclone and storm track char- sea level pressure (MSLP) for the detection of cyclones in mid-latitudes,
acteristics of datasets available at high temporal resolution, since 1- where the surface pressure gradient can be strong so that cyclones
hourly fields are frequently used to support the production of wave appear without a closed isobar. For this reason, the use of vorticity al-
hindcasts and forecasts, and energy sector assessments. The main goal of lows the early identification of cyclones that would only be detected by
this study is to present and evaluate the Atlantic cyclone climatology for MSLP when intensification occurs or they move to higher latitudes. The
middle and high latitudes that can be used by research and industry vorticity field contains many small scale structures, particularly at high
applications, since there is a lack of this type of product available (e.g., resolution, which can cause problems during the identification process
Dacre et al., 2012), particularly for the South Atlantic Ocean. Therefore, and tracking on the synoptic scale. To prevent this issue and to focus on
two main questions for this study are: (1) How does the 1-hourly ERA5 synoptic scales, the vorticity is spectrally filtered by converting to the
and CFSR/CFSv2 cyclone tracks for the Atlantic storm track compare spectral representation and truncating to T42, tapering the spectral
with previously published studies?; (2) What are the main differences coefficients to smooth the data. Large-scale atmospheric features are
between the two datasets regarding the basic cyclone and storm track also removed by setting zonal wavenumbers ≤5 to zero. Hoskins and
characteristics? The analysis is focused on the mean characteristics, Hodges (2002) present more details about the filtering process.
spatial distribution and intensity of the cyclones, which are important The cyclonic features are identified by determining the local
2

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
maxima. In the Southern Hemisphere, where negative vorticity indicates threshold results in including continental lows and non-developed
cyclonic circulation, the vorticity fields are first scaled by (cid:0) 1. First, the cyclonic systems in the climatology.
central position of the cyclonic feature is determined by the grid point Figure. 1 shows the genesis and track densities of cyclonic systems
maxima that exceed a threshold of 1 ×10 (cid:0) 5 s (cid:0) 1 (1 cyclonic vorticity unit that live at least 24 h with the total displacement between 500 and 1000
(CVU)) on a polar stereographic projection. This identification threshold km. In the North Atlantic, 23% (ERA5) and 26% (CFSR/CFSv2) of the
is suitable to capture even weak cyclonic centers in the filtered vorticity cyclonic systems are excluded with the 1000 km (~10◦) displacement
field (T42), since it is smoother than the original vorticity one (e.g., threshold, while in the South Atlantic they represented a smaller portion
Hoskins and Hodges, 2002, 2005). The feature central locations are of 15% (ERA5) and 21% (CFSR/CFSv2). Although these values can be
refined by computing the off-grid maxima using B-spline interpolation considered important, the track density reveals that systems with small
and steepest descent maximization and then converted back to spherical mobility (semi-stationary) are mainly continental and thermal lows
coordinates. The tracking is initialized using a nearest neighbours search generated in complex terrain, and troughs that are generated in frontal
method. The initial set of tracks is refined by minimizing a cost function zones, without enough forcing for full-development. The genesis den-
for track smoothness, subject to adaptive constraints (Hodges, 1999), sities are smaller when compared to active cyclone genesis regions re-
that operates both forward and backward in time. The high time reso- ported in the literature (e.g., Hoskins and Hodges, 2002, 2005), and the
lution reduces ambiguity during tracking. The displacement constraint track density is restricted to the generation point revealing the small
applied is 2.0◦, except in the tropics (20◦N-20◦S) where it is set as 0.5◦. influence of the systems, which mostly do not reach the ocean.
Due to the large amount of data, the tracking was performed using Since the main interest of this work is on cyclones at middle and high
monthly files. Thus, post-processing is applied to connect tracks between latitude, for further analysis only storms that pass within the extra-
the months, using the same displacements rules described above. tropical latitudes of the South Atlantic (85◦S-25◦S, 75◦W-20◦E) and
Finally, identified systems that are not cyclones are excluded. In this North Atlantic (85◦N-25◦N, 65◦W-0◦E) are considered. The selected
step, cyclonic features, such as thermal lows, mesoscale storms, and domains include areas where subtropical cyclones occur generated both
some convergence areas are removed by considering only systems that by genuine subtropical genesis and by transition process between
last at least 24 h and that travel further than 1000 km, as used by tropical and extratropical cyclones (e.g., Guishard et al., 2009; Evans
Gramcianinov et al. (2019) for the South Atlantic Ocean. The thresholds and Braun, 2012; Gozzo et al., 2014; da Rocha et al., 2019). In this way,
are more relaxed than the ones commonly used in North Atlantic storm subtropical cyclones may be included in the set of tracks, since no
track studies (e.g., Hoskins and Hodges, 2002, 2005, 2019a, 2019b; distinction between subtropical and extratropical cyclones is made in
Hodges et al., 2011; Dacre and Gray, 2009), but this maintains consis- the present work.
tency throughout the entire Atlantic. The use of a higher minimum
lifetime threshold (e.g., 36 h or 48 h) would exclude some systems with 2.3. Cyclone diagnostics
regional importance (e.g., Gramcianinov et al., 2019, Gramcianinov
et al., 2020a). Gramcianinov et al. (2020a) considered cyclones with a The statistical analysis consists of information for the tracks,
minimum of 12 h lifetime and 500 km displacement, to include including mean lifetime of cyclones, cyclone speed, and displacement.
short-lived systems that might be important for extreme waves along the Standard seasons are used for the entire period (1979–2019): Decem-
Southern Brazilian coast. However, the use of such a low displacement ber–February (DJF), March–May (MAM), June–August (JJA), and
Fig. 1. Genesis (shaded) and track (contour) densities computed for cyclones that last at least 24 h and travel less than 1000 km for the (a) North Atlantic in ERA5
and (b) CFSR/CFSv2, and (c) South Atlantic in ERA5 and (d) CFSR/CFSv2. The density unit is cyclones/track per month per area, where the unit area is equivalent to
a 5◦spherical cap (106 km2). The track density contour are with contour interval 1 track per month per area, and the densities are calculated for 1979–2019.
3

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
September–November (SON). Spatial statistics are computed for each 3. Results
reanalysis using the spherical kernel estimator approach, described by
Hodges (1996). The differences between track and genesis densities of 3.1. Genesis and track densities
the two datasets are tested using Monte Carlo significance test (Hodges,
2008) with 1000 samples of the set of tracks for each dataset. Before the direct comparison between storms tracks in each dataset,
Maximum 10-m wind speed is used for the comparison of cyclone the climatology of the cyclones is presented, using ERA5 as a reference,
intensities. The 10-m wind speed is added to each track by a general to provide an overview of the storm track pattern and genesis variability
search for the maximum value within a 6◦ radius of cyclone centre in the North and South Atlantic Oceans.
(Bengtsson et al., 2009). This additional information is used to construct
maximum intensity distributions for both ERA5 and CFSR/CFSv2. 3.1.1. North Atlantic
Moreover, identification of matched tracks between the datasets is made The track and genesis densities in the North Atlantic domain for the
to perform a more direct comparison of the cyclone intensities. A storm entire period, boreal winter (DJF) and summer (JJA) are shown for the
is considered to be the same in ERA5 and CFSR/CFSv2 when the mean ERA5 and CFSR/CFSv2 in Fig. 2 and Fig. 3. The North Atlantic storm
separation distance between cores is less than 2◦ (geodesic) and they track is represented by the region of maximum track density [>10 cy-
overlap in time by at least 50% of their points. The criteria used here is clones (10 (cid:0) 6 km2) (cid:0) 1 (month) (cid:0) 1] extending northeastward, from the East
stricter than the one applied in Hodges et al. (2011), where the mini- of North American coast to Greenland and North Europe. A northern
mum mean separation distance was 4◦. The choice of a smaller distance path of the storm track strengthens in DJF, along the eastern side of
agrees with the focus of this work, linked to ocean engineering appli- Greenland, due to the increase in genesis activity at this location. The
cations, in which smaller differences in the system position may lead to genesis density shows four regions favourable to cyclogenesis [>2 cy-
large biases in the wind and wave fields. clones (10 (cid:0) 6 km2) (cid:0) 1 (month) (cid:0) 1]: lee of the southern Rockies (35◦N,
Fig. 2. Track densities computed for the North Atlantic in (a,c,e) ERA5 and (b,d,f) CFSR/CFSv2, considering (a,b) all period (1979–2019), (c,d) DJF, and (e,f) JJA.
The density unit is track per month per area, where the unit area is equivalent to a 5◦spherical cap (106 km2). The contour interval is 2 tracks per month per area.
4

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Fig. 3. Genesis densities computed for the North Atlantic in (a,c,e) ERA5 and (b,d,f) CFSR/CFSv2, considering (a,b) all period (1979–2019), (c,d) DJF, and (e,f) JJA.
The density unit is genesis per month per area, where the unit area is equivalent to a 5◦spherical cap (106 km2). The contour interval is 1 genesis per month per area.
102.5◦W), West Atlantic (40◦N, 75◦W), East Atlantic (centred at 50◦N, also obtained a more pronounced genesis density in Greenland.
25◦W), and in the eastern coast of Greenland.
All genesis regions within the North Atlantic domain are more active 3.1.2. South Atlantic
during the boreal winter (DJF). However, the genesis region along the Fig. 4 and Fig. 5 show the cyclone track and genesis densities in the
eastern North American coast is active all year, being a location with South Atlantic for the ERA5 and CFSR/CFSv2, computed for the whole
high baroclinicity due to the sea surface temperature gradients provided period, as well as divided into austral summer (DJF), and winter (JJA).
by the warm Gulf Stream. The surface temperature contrast does not The main South Atlantic storm track is defined by the high concentration
give only conditions to genesis but also to the intensification of pre- of systems [>10 cyclones (10 (cid:0) 6 km2) (cid:0) 1 (month) (cid:0) 1] extending from
existing cyclones and perturbations that come from the continent, west to east of the domain, between 40◦S and 55◦S. Furthermore, there
which may be generated on the lee side of the Rockies. Grise et al. (2013) is a secondary storm track [>6 cyclones (10 (cid:0) 6 km2) (cid:0) 1 (month) (cid:0) 1] that
constructed a genesis density distribution using not the first track point merges with the primary storm track, being considered a subtropical
of each cyclone but the location where storms exceeded the growth rate branch. During the austral summer (DJF), the subtropical storm track
of 2 CVU per day, and they found a major genesis density along the east spreads northward, originating between 30◦S and 35◦S, while during the
coast of North America and less at the Rockies. The genesis region at the winter this branch is concentrated in 35◦S. The winter season variability
lee of the northern Rockies and its consequent storm track density along in the South Atlantic storm track is linked to changes in active genesis
the continent (e.g., Hoskins and Hodges, 2002) does not appear in Fig. 3 regions in South America, as is possible to see in the genesis density
because these cyclones dissipate in the northeast portion of the North spatial distribution (Fig. 5).
American continent, outside the North Atlantic domain (Dacre and Gray, The genesis density for all period shows three main regions of active
2009). The genesis densities along the east Greenland coast are higher in genesis [> 2 cyclones (10 (cid:0) 6 km2) (cid:0) 1 (month) (cid:0) 1]: in Uruguay (35◦S,
Fig. 3 than in some previous studies selecting cyclones that last more 60◦W), Argentinean coast (45◦S, 65◦W), and Antarctic Peninsula (65◦S,
than 48 h (e.g., Hoskins and Hodges, 2002, 2019a, 2019b; Dacre and 60◦W). Secondary genesis regions exist in the Southeast Brazilian coast
Gray, 2009; Grise et al., 2013). Trigo (2006) used the 24 h threshold and (27◦S, 45◦W), and southeast portion of South Atlantic (centred at 45◦S,
5

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Fig. 4. Track densities computed for the South Atlantic in (a,c,e) ERA5 and (b,d,f) CFSR/CFSv2, considering (a,b) all period (1979–2019), (c,d) DJF, and (e,f) JJA.
The density unit is track per month per area, where the unit area is equivalent to a 5◦spherical cap (106 km2). The contour interval is 2 tracks per month per area.
10◦W). The former is only pronounced during the austral summer, while genesis density almost 20% larger.
the last has more genesis during the winter (e.g., Gramcianinov et al.,
2019). In South America, the genesis regions at Uruguay are more active
during JJA, while the Argentina’s genesis region is more active in DJF. 3.2. Differences between ERA5 and CFSR/CFSv2 cyclones
However, the genesis region in Argentina presents a high density of
genesis during all year [>5 cyclones (10 (cid:0) 6 km2) (cid:0) 1 (month) (cid:0) 1]. The Table 1 shows the cyclone annual and seasonal mean frequencies
genesis region in Southeast Brazilian coast and Southeast South Atlantic computed for the entire period (1979–2011). Such values are also
are more active in CFSR/CFSv2 climatology [>2 cyclones (10 (cid:0) 6 km2) (cid:0) 1 computed for the split period linked to CFSR (1979–March/2011) and
(month) (cid:0) 1] than in ERA5. CFSv2 (April/2011–2019) separately, to analyze the differences be-
The spatial distribution and seasonal variation presented in Figs. 4 tween datasets. In general, ERA5 produces more cyclones than CFSR/
and 5 are in agreement with previous studies (e.g., Hoskins and Hodges, CFSv2, which is expected due to the higher resolution of the former. The
2005; Reboita et al., 2010; Gramcianinov et al., 2019). A more direct differences between the two datasets are smaller in the North Atlantic
comparison can be made with results from Gramcianinov et al. (2019) than in the South Atlantic in all cases. In the North Atlantic, the differ-
since the system duration and displacement threshold applied are the ences in cyclone numbers are between 0.4% and 4.4%, being the lowest
same (24 h and 1000 km). They found a slightly more active genesis and largest differences detected in MAM and JJA respectively. The
region in the Southeast Brazilian coast in DJF. Furthermore, the period of JJA is the only season that CFSR/CFSv2 presents more cy-
Uruguay genesis region is much more active in the present work, with a clones than ERA5. The differences between datasets for the South
Atlantic vary from 6.3% to 2.3%. The largest difference occurs in JJA,
6

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Fig. 5. Genesis densities computed for the South Atlantic in (a,c,e) ERA5 and (b,d,f) CFSR/CFSv2, considering (a,b) all period (1979–2019), (c,d) DJF, and (e,f) JJA.
The density unit is genesis per month per area, where the unit area is equivalent to a 5◦spherical cap (106 km2). The contour interval is 1 genesis per month per area.
the most active cyclonic season. By choosing ERA5 as the reference, the (less) genesis or tracks in a location. Areas with significant differences
CFSv2 improves the cyclone representation in the South Atlantic when (p-value < 0.01) are marked with a black dot. First, for the North
compared to its predecessor, since there is a reduction of differences Atlantic, the track density difference shows that ERA5 have more storm
between CFSv2 and ERA5 when compared to CFSR and ERA5. It is not tracks than CFSR/CFSv2. The track differences do not show any dipole
possible to conclude the same for the North Atlantic, which presents a patterns that would indicate shifts between storm tracks but, instead, the
small increase or decrease of differences depending on the season. negative values are distributed all over the main North Atlantic storm
The spatial distribution and intensity differences between ERA5 and track paths from the eastern portion of the eastern USA to Iceland and
CFSR/CFSv2 are presented in the following subsections. The results the UK. However, there are some local differences in genesis density
focus on the storm track active season in each ocean basin: boreal winter comparisons. The CFSR/CFSv2 presents a more concentrated genesis
(DJF) for the North Atlantic, and austral winter (JJA) for the South along the eastern coast of North American, between 40◦N and 55◦N, and
Atlantic. offshore areas. This genesis difference along the coast generates an
eastward shift of the east of North Atlantic genesis region between the
3.2.1. Spatial distribution two datasets. The CFSR/CFSv2 also presents an active genesis region
The winter genesis and track density differences between the two closer to the UK (15◦W) than ERA5 (25◦W).
datasets are presented in Fig. 6 for the North Atlantic (DJF) and South Differences are larger in the South Atlantic, both in genesis and track
Atlantic (JJA). The difference is computed as CFSR/CFSv2 minus ERA5, densities. The track density differences show that ERA5 presents a
so positive (negative) values indicate that the CFSR/CFSv2 has more higher track density in most of the domain, particularly where the South
7

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Table 1
Mean number of cyclones tracked in ERA5 and CFSR/CFSv2 between 1979 and 2019, annual and seasonal mean. The mean are also computed for CFSR (1979–March/
2011) and CFSv2 (April/2011–2019) alone. All cyclones that pass within the extratropical latitudes of the South Atlantic (SA; 85◦S-25◦S, 75◦W-20◦E) and North
Atlantic (NA; 85◦N-25◦N, 65◦W-0◦E) Oceans were considered.
1979–2019
Annual DJF MAM JJA SON
NA ERA5 551.0 ±23.6 155.8 ±9.7 140.9 ±10.6 117.5 ±8.3 136.7 ±9.1
CFSR/CFSv2 538.7 ±21.2 152.9 ±8.1 135.2 ±11.3 118.0 ±7.9 132.7 ±8.8
SA ERA5 730.9 ±21.4 158.2 ±10.0 184.8 ±11.5 201.9 ±11.7 186.0 ±9.9
CFSR/CFSv2 698.0 ±19.7 154.2 ±9.6 177.1 ±10.6 189.3 ±10.2 177.4 ±10.0
1979–2011
Annual DJF MAM JJA SON
NA ERA5 537.8 ±72.5 154.4 ±14.8 137.7 ±16.4 117.5 ±8.7 135.8 ±8.9
CFSR 525.2 ±69.9 151.7 ±12.9 131.7 ±16.9 117.5 ±7.3 131.8 ±8.4
SA ERA5 709.2 ±100.4 155.0 ±14.1 180.9 ±24.5 200.3 ±11.8 184.6 ±10.6
CFSR 678.7 ±97.5 151.5 ±14.4 174.3 ±24.3 187.8 ±10.1 176.2 ±10.4
2011–2019
Annual DJF MAM JJA SON
NA ERA5 538.1 ±52.9 143.8 ±36.6 137.2 ±18.6 117.6 ±7.0 139.6 ±9.4
CFSv2 528.6 ±54.0 140.0 ±35.6 133.1 ±16.6 119.8 ±10.0 135.7 ±10.0
SA ERA5 729.3 ±57.9 152.4 ±33.9 178.4 ±22.3 207.7 ±9.8 190.8 ±5.1
CFSv2 691.0 ±61.2 147.1 ±30.9 167.8 ±21.6 194.6 ±9.5 181.6 ±7.6
Atlantic storm track is typically found, between 40◦S and 55◦S, 3.2.2. Cyclone intensity and additional characteristics
following the spiral pattern typical of the winter. Moreover, in the Some important cyclones characteristics are shown in Table 2 for
southwest of the domain, in the Drake Passage (55◦S and 66◦S), there is ERA5 and CFSR/CFSv2, for both oceanic basins. First, the mean initial
a pronounced difference associated with cyclones that come from the vorticity is calculated by the filtered vorticity (T42) at the time of the
South Pacific Ocean. The genesis density difference shows that the genesis in each track. The CFSR/CFSv2 presents larger initial vorticity
cyclogenesis regions over Uruguay and Argentina are more active in than ERA5, in all periods considered. The difference is larger for the
ERA5, while CFSR/CFSv2 favours genesis in the oceanic portion off of South Atlantic, where CFSR/CFSv2 cyclones are 10.4% more intense at
South America Eastern coast and Southeast of South Atlantic. The gen- the time of the genesis than cyclones in ERA5. For the North Atlantic
esis region in the Antarctic Peninsula is more active in ERA5, which are cyclones, CFSR/CFSv2 present storms 6.4% more intense than ERA5.
connected to more cyclonic perturbations coming from the South The cyclone propagation speed is similar between datasets, which is
Pacific. expected once it is mainly dictated by the large scale flow. As is possible
to see, regarding cyclones’ mean characteristics, the differences between
ERA5 and CFSR/CFSv2 are small, and not significant due to the large
Fig. 6. Densities differences in (a,b) DJF for the North Atlantic and (c,d) JJA for the South Atlantic, for the (a,c) cyclogenesis and (b,d) storm track. The density
difference unit is cyclones/track per month per area, where the unit area is equivalent to a 5◦ spherical cap (106 km2). The dots represent grid points where the
difference is significant within 99% confidence level, and the differences are CFSR/CFSv2 minus ERA5 considering 1979–2019 period.
8

C.B. Gramcianinov et al.                                                                                                                                                                                           O  c e  a  n   E n  g  i n e  e r  i n g   216(2020)108111
Table 2
Mean characteristics of cyclones for ERA5 and CFSR/CFSv2 (1979–2019), and computed for CFSR (1979–March/2011) and CFSv2 (April/2011–2019) separately.
Initial vorticity is the filtered relative vorticity at the time of genesis, and is scaled by (cid:0) 1 in South Atlantic. Displacement is computed using the first and the last track
point. All cyclones that pass within the extratropical latitudes of the South Atlantic (SA; 85◦S-25◦S, 75◦W-20◦E) and North Atlantic (NA; 85◦N-25◦N, 65◦W-0◦E) Oceans
were considered.
1979–2019
Initial vorticity (CVU)  Lifetime (days)  Displacement (m)  Speed (km h(cid:0)1)
| NA  | ERA5  | 2.7 ±1.4  | 4.4 ±3.0  | 2928.5 ±1582.2  | 9.6 ±4.7  |
| --- | ----- | --------- | --------- | --------------- | --------- |
|     |       | 2.8 ±1.5  | 4.0 ±2.6  | 2767.8 ±1467.6  | 9.8 ±4.6  |
CFSR/CFSv2
| SA  | ERA5        | 2.9 ±1.5  | 3.9 ±2.6  | 3712.0 ±2157.9  | 13.2 ±5.3    |
| --- | ----------- | --------- | --------- | --------------- | ------------ |
|     | CFSR/CFSv2  | 3.2 ±1.6  | 3.3 ±2.1  | 3228.3 ±1855.6  | 13.3 ±5.3    |
1979–2011
Initial vorticity (CVU)  Lifetime (days)  Displacement (m)  Speed (km h¡1)
| NA  | ERA5  | 2.7 ±1.4  | 4.4 ±2.9  | 2919.2 ±1569.4  | 9.6 ±4.6  |
| --- | ----- | --------- | --------- | --------------- | --------- |
|     |       | 2.9 ±1.5  | 4.0 ±2.6  | 2750.6 ±1452.6  | 9.8 ±4.6  |
CFSR
|     |       | 2.9 ±1.5  | 3.9 ±2.6  | 3688.0 ±2146.9  | 13.2 ±5.3    |
| --- | ----- | --------- | --------- | --------------- | ------------ |
| SA  | ERA5  |           |           |                 |              |
|     | CFSR  | 3.3 ±1.6  | 3.2 ±2.1  | 3155.5 ±1799.8  | 13.3 ±5.3    |
2011–2019
Initial vorticity (CVU)  Lifetime (days)  Displacement (m)  Speed (km h¡1)
| NA  | ERA5  | 2.7 ±1.5  | 4.5 ±3.1  | 2962.5 ±1628.0  | 9.6 ±4.8  |
| --- | ----- | --------- | --------- | --------------- | --------- |
|     |       | 2.8 ±1.6  | 4.1 ±2.7  | 2830.7 ±1519.6  | 9.8 ±4.7  |
CFSv2
|     |        | 3.0 ±1.5  | 4.0 ±2.7  | 3797.7 ±2194.7  | 13.3 ±5.4   |
| --- | ------ | --------- | --------- | --------------- | ----------- |
| SA  | ERA5   |           |           |                 |             |
|     | CFSv2  | 3.2 ±1.6  | 3.6 ±2.3  | 3490.3 ±2022.5  | 13.4 ±5.3   |
variance.  period is shifted to the right, and has a more pronounced tail to the right
Analyzing CFSR and CFSv2 separately, the differences compared to  side of maximum wind speed axis.
ERA5 decrease in version 2. Despite the large standard deviation, the
| mean values indicate that ERA5 cyclones seem to live longer and move  |     |     | 4. Discussion  |     |     |
| --------------------------------------------------------------------- | --- | --- | -------------- | --- | --- |
further than CFSR/CFSv2 ones. To investigate further the duration and
displacement differences between the two datasets the histograms of  The cyclone climatologies covering 41-years produced from ERA5
those cyclones characteristics are presented in Fig. 7. In fact, the lifetime  and CFSR/CFSv2 are in good agreement with past studies for the North
and displacement distributions show that CFSR/CFSv2 presents a larger  Atlantic (e.g., Hoskins and Hodges, 2002, 2019a; Trigo, 2006; Dacre and
portion of small-distance and short-life cyclones when compared to  Gray, 2009) and South Atlantic Oceans (e.g., Hoskins and Hodges, 2005;
ERA5.  Gramcianinov et al., 2019). Differences in genesis and track densities
The intensity distributions are shown in Fig. 8 for both the North  between the present and past studies are expected, particularly due to
Atlantic (DJF) and South Atlantic (JJA) in two periods: from 1979 to  the use of distinct cyclone tracking methods, domains, and thresholds
2019, and April/2011 to 2019, the last referring to CFSv2 solely. Fig. 8  that define whether a cyclonic feature is a cyclone or not (Pinto et al.,
| also shows the intensity distribution of the matched tracks between  |     |     | 2005).  |     |     |
| -------------------------------------------------------------------- | --- | --- | ------- | --- | --- |
datasets. The percentage of matched tracks between ERA5 and CFSR/  The climatologies presented in this work show a higher cyclone
CFSv2 can be found in Table 3. The maximum 10-m wind speed distri- density than Hoskins and Hodges (2002, 2005), Dacre and Gray (2009),
bution for all cyclones shows that the CFSR/CFSv2 presents more  and Grise et al. (2013), since these authors remove from their clima-
intense cyclones than ERA5, as its distribution is shifted to the right. The  tology cyclones that live less than 48 h, which represent a large portion
mean maximum surface winds and percentiles of the distributions are  of the systems in this study (Fig. 7). However, when compared to Trigo
displayed in Table 4. CFSR/CFSv2 presents a higher mean and percen- (2006) and Gramcianinov et al. (2019), which also used the 24 h as
tiles, and the differences between the datasets are larger for the South  cyclone lifetime threshold, the densities presented in this work are
Atlantic than North Atlantic. Additionally, the CFSv2 has a broader  comparable (Figs. 2–5).
distribution when compared to ERA5, although this is more evident in  Genesis density in regions such as Greenland, in the North Atlantic,
the North Atlantic.  and the southeastern Brazilian coast, in the South Atlantic, seem to be
The same behaviour was observed by Hodges et al. (2011) when they  enhanced by the addition of short-lived cyclones included in the statis-
compared CFSR and ERA-Interim. The tendency of CFSR/CFSv2 to  tics. These regions are also highlighted when a smaller displacement
simulate more intense storms is reported by previous studies (Hodges  threshold is applied (Fig. 1). Crespo et al. (2020b) showed five genesis
et al., 2011; Stopa and Cheung, 2014; Gramcianinov et al., 2020b). The  region in South America without the application of any displacement
matching storms distribution reveals more about the dissimilarities be- threshold, contrasting the three well-known cyclogenetic regions (Hos-
tween the datasets since it compares the same storm simulated in each  kins and Hodges, 2005; Reboita et al., 2010; Gramcianinov et al., 2019).
one. The intensity distribution of the matched tracks is very similar to  The use of displacement threshold is necessary to avoid the inclusion of
the distribution obtained with all tracks, due to the high correspondence  thermal and continental lows in the climatology, which may not develop
| percentage between datasets (Table 3). Even for the matching cyclones  |     |     | into a cyclone.  |     |     |
| ---------------------------------------------------------------------- | --- | --- | ---------------- | --- | --- |
distributions, CFSR/CFSv2 cyclones are more intense than ERA5 ones,  Another source of discrepancies between the present and previous
reinforcing its tendency to simulate stronger storms. Analysing CFSR  studies is the use of 1-hourly tracking, since most climatologies are
alone (not shown) does not change this behaviour, but the intensity  constructed based on 6-hourly atmospheric fields. The improved time-
distributions computed for CFSv2 and ERA5 between April/2011 and  resolution tracking can result in slight differences in genesis position,
2019, present a slight increase in cyclones intensity in relation to the  such as can be observed on the East South American coast. Despite the
mean and past distribution. The distribution computed for the end of the  same tracking method and thresholds, this work present a higher genesis
9

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Fig. 7. Histograms of cyclones (a,b) lifetime (days), and (c,d) displacement (km). for the (a,c) North Atlantic and (b,d) South Atlantic Oceans. The histograms were
computed considering the whole 1979–2019 period for the ERA5 (black) and CFSR/CFSv2 (grey).
Fig. 8. Cyclone’s maximum 10-m wind speed (m s (cid:0)1) distribution for the (a,b) North Atlantic in DJF, and (c,d) South Atlantic in JJA, considering the period between
(a,c) 1979 and 2019, and (b,d) April/2011 and 2019. ERA5 distributions are in black, and CFSR/CFSv2 are in red. The dashed lines are the distributions computed for
the matched cyclones in each dataset. The y-axis is cyclone per month. (For interpretation of the references to colour in this figure legend, the reader is referred to the
Web version of this article.)
10

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Table 3 compared to other older and coarser resolution reanalysis. Both ERA5
Percentage of the number of matched tracks for ERA5 and CFSR/CFSv2 and CFSR/CFSv2 are considered to be high-resolution global products,
(1979–2019), CFSR (1979–March/2011), and CFSv2 (April/2011–2019). and state of the art for analysis and reanalysis methodology.
Similar tracks are obtained in DJF for the North Atlantic (NA), and JJA for the The most pronounced difference is in the intensity distribution,
South Atlantic (SA) Oceans. which shows more intense cyclones in CFSR/CFSv2 than in ERA5. The
1979–2019 1979–2011 2011–2019 CFS family present a tendency to represent more intense cyclones, winds
NA ERA5 92.7% 91.9% 87.1% and, consequently waves, as reported by several works (e.g., Hodges
CFSR/CFSv2 96.0% 94.9% 91.1% et al., 2011; Stopa and Cheung, 2014; Gramcianinov et al., 2020b).
SA ERA5 93.1% 91.8% 89.2% There are no significant difference between ERA5 and CFSR/CFSv2
CFSR/CFSv2 96.5% 95.4% 91.8% when mean maximum wind speed is considered, but the differences
increase in the higher percentiles of the distributions (Table 4). The
density in Uruguay and a smaller density in the Southeast Brazilian coast 10-m wind components are diagnostic variables, and their computation
than Gramcianinov et al. (2019), which can be associated with the depends on the different boundary layers models component of each
identification of cyclones at earlier lifecycle stages with the use of dataset. Even so, these parameters are widely used in oceanography and
1-hourly tracking, instead of 6-hourly. Gramcianinov et al. (2019) used ocean engineering studies and the evaluation of cyclone intensity by
an artificial orographic barrier to impose an Andes constraint to their these fields is of great value.
tracking method, which could influence the genesis region position in This study shows that the differences between ERA5 and CFSR/
their work. CFSv2 are larger for the South Atlantic than North Atlantic. Other
Regarding the main differences between the two data sets, ERA5 comparison studies found the same behaviour (e.g., Hodges et al., 2003,
presents 3.7% more cyclones than CFSR/CFSv2 (45.2 cyclones per year), 2011; Stopa and Cheung, 2014). However, there is a decrease of dis-
which can be related to the higher resolution of the former. The higher crepancies between ERA5 and the more recent CFSv2 when compared to
amount of cyclones in the ERA5 impacts the spatial distribution differ- CFSR, particularly in the South Atlantic Ocean. The decrease in differ-
ences both in the North Atlantic and South Atlantic. The track density ences between datasets in recent years reflects the improvement of the
difference shows a homogeneous distribution in the major part of both models and increase in data availability as discussed by Hodges et al.
domains and does not reveal a shift between the tracks of the two (2010).
datasets. The direct relation between model resolution and the number The storm tracks for ERA5 and CFSR/CFSv2 used to produce the
of detected cyclones are indicated in many studies (e.g., Bengtsson et al., climatologies presented in this work are available in a data repository at
2006). The impact of resolution is affected by the orography represen- https://doi.org/10.17632/kwcvfr52hp.1. Moreover, a more frequently
tation and small-scale processes important to genesis and growth. updated version can be found at ftp://masterftp.iag.usp.br/EXWAV. The
Therefore, the T42 filtering before the identification process and provided product consists of the set of monthly tracks files that contain
tracking does not completely exclude the effects of the resolution on the the positional information of cyclones.
representation of cyclones in ERA5.
Cyclogenesis density differences show that CFSR/CFSv2 favours 5. Conclusions
genesis off coast and above the ocean sector, which induce a bias in the
genesis region along East of the North American coast and Southwest of This study evaluates and compares the cyclone climatologies for
South American coast when compared to ERA5. This meridional shift in ERA5 and CFSR/CFSv2 at middle and high latitudes. First, the perfor-
genesis regions may also be related to resolution, once the best repre- mance of 1-hourly ERA5 and CFSR/CFSv2 tracking in reproducing the
sentation of orography, land contrast and sea surface temperature can Atlantic storm tracks is analysed regarding the past literature. Then, the
lead to early cyclone detection (e.g., Bengtsson et al., 2006) in the ERA5. two climatologies are compared to determine the main differences be-
However, the differences in genesis densities are evidence of differences tween them regarding the basics of storm track characteristics.
in the track lengths between the two datasets. ERA5 presents cyclones The storm tracks are in good agreement with past studies, both to
that lived longer and travel further than CFSR/CFSv2 (Fig. 7), which can North Atlantic (e.g., Hoskins and Hodges, 2002; Trigo, 2006; Dacre and
be addressed to the inconsistency between forecast and analysis Gray, 2009; Grise et al., 2013), and South Atlantic Oceans (e.g., Gan and
sequential time-steps. Abrupt changes in atmospheric patterns between Rao, 1991; Mendes et al., 2010; Reboita et al., 2010; Gramcianinov
the forecast and analysis time-step can interrupt a track, breaking a et al., 2019; Crespo et al., 2020b). The main North Atlantic and South
unique cyclone track into two. This continuity issue in CFSR/CFSv2 Atlantic storm track characteristics, such as the spiral pattern poleward,
influences its genesis density, and also its stronger initial vorticity, since seasonal variability, and latitudinal range are represented, as well as the
a broken track leads to a new track that starts in a more mature stage of well-known genesis regions within these ocean basins. The use of hourly
the cyclone. fields brings benefits to the tracking, particularly in areas with complex
Cyclone annual mean and mean characteristics, such as displacement terrains, such as the lee of Andes Cordillera in the South America, and
speed and initial vorticity are similar between the two datasets, and East of Greenland in the North Atlantic.
their differences are less than 1 standard deviation. Moreover, the track Differences between datasets show that ERA5 has 3.7% more cy-
correspondence between the two datasets is high, being higher than 90% clones than CFSR/CFSv2, which can be related to the finer resolution (e.
to the whole period. In Hodges et al. (2011), the differences between g., Bengtsson et al., 2006). However, cyclone annual mean and mean
more recent datasets (ERA-Interim and CFSR) are smaller when characteristics (e.g., displacement speed) are similar between the two
Table 4
Mean maximum 10-m wind speed (m s (cid:0)1) and percentiles of cyclones for ERA5 and CFSR/CFSv2 (1979–2019) in DJF for the North Atlantic (NA), and JJA for the South
Atlantic (SA) Oceans. Matched cyclones are identical storms find in both datasets.
ERA5 CFSR/CFSv2
mean 50% 90% 95% mean 50% 90% 95%
NA all 21.4 ±5.1 21.1 28.2 30.1 23.9 ±6.4 23.7 32.5 35.0
matched 21.5 ±5.1 21.2 28.3 30.2 24.0 ±6.4 23.8 32.6 35.0
SA all 21.2 ±4.8 21.0 27.3 29.3 23.4 ±4.8 23.3 30.2 32.1
matched 21.2 ±4.8 21.0 27.4 29.3 23.4 ±5.3 23.4 30.2 32.2
11

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
datasets, and 90% of the tracks correspond between them. An important Belmonte Rivas, M., Stoffelen, A., 2019. Characterizing ERA-Interim and ERA5 surface
difference between ERA5 and CFSR/CFSv2 are the shifts in genesis wind biases using ASCAT. Ocean Sci. 15, 831–852. https://doi.org/10.5194/os-15-
831-2019.
density along the eastern coast, both in North and South America, which Bengtsson, L., Hodges, K.I., Keenlyside, N., 2009. Will extratropical storms intensify in a
can be an indication of resolution impact in cyclone development in warmer climate? J. Clim. 22, 2276–2301. https://doi.org/10.1175/
regions with complex orography, and temperature gradient. Further- 2008JCLI2678.1.
Bengtsson, L., Hodges, K.I., Roeckner, E., 2006. Storm tracks and climate change. J. Clim.
more, continuity issues in CFSR/CFSv2 due to jumps that might occur 19, 3518–3543. https://doi.org/10.1175/JCLI3815.1.
when forecast time-steps change to analysis time-steps can lead to Booth, J.F., Rieder, H.E., Kushnir, Y., 2016. Comparing hurricane and extratropical storm
broken tracks, and thus, differences between the two datasets, particu- surge for the Mid-Atlantic and Northeast Coast of the United States for 1979-2013.
Environ. Res. Lett. 11 (9) https://doi.org/10.1088/1748-9326/11/9/094004.
larly related to genesis statistics and cyclone duration lifecycle.
Campos, R.M., Guedes Soares, C., 2016a. Comparison of HIPOCAS and ERA wind and
Other relevant differences between ERA5 and CFSR/CFSv2 are the wave reanalysis in the north Atlantic Ocean. Ocean Eng. 112, 320–334. https://doi.
intensity distributions, particularly in the higher percentile of maximum org/10.1016/j.oceaneng.2015.12.028.
Campos, R.M., Guedes Soares, C., 2016b. Comparison and assessment of three wave
10-m wind speed. The CFSR/CFSv2 dataset presents more intense cy-
hindcasts in the north Atlantic Ocean. J. Oper. Oceanogr. 9 (1), 26–44. https://doi.
clones than ERA5 and this behaviour persists even when CFSR and org/10.1080/1755876X.2016.1200249.
CFSv2 are evaluated separately. Other studies have already reported the Campos, R.M., Guedes Soares, C., 2017. Assessment of three wind reanalysis in the north
Atlantic Ocean. J. Oper. Oceanogr. 10 (1), 30–44. https://doi.org/10.1080/
ability of CFSR (Hodges et al., 2011; Stopa and Cheung, 2014) and
1755876X.2016.1253328.
CFSv2 (e.g., Gramcianinov et al., 2020b) to represent more extreme Campos, R.M., Alves, J.H.G.M., Guedes Soares, C., Guimaraes, L.G., Parente, C.E., 2018.
wind speed values. It is remarkable that in most of the analyses per- Extreme wind-wave modeling and analysis in the south Atlantic Ocean. Ocean
formed in this work, the differences between datasets decrease when Model. 124, 75–93. https://doi.org/10.1016/j.ocemod.2018.02.002.
Campos, R.M., Guedes Soares, C., Alves, J.H.G.M., Parente, C.E., Guimaraes, L.G., 2019.
CFSv2 period is analysed separately, revealing rather a bias correction in Regional long-term extreme wave analysis using hindcast data from the South
the operational version of CFS or an increase of available data and Atlantic Ocean. Ocean Eng. 179, 202–212. https://doi.org/10.1016/j.
improvement of data assimilation method. In fact, the discrepancies oceaneng.2019.03.023.
Chelton, D.B., Schlax, M.G., Freilich, M.H., Milliff, R.F., 2004. Satellite measurements
reduction is more pronounced in the South Atlantic, which reinforces reveal persistent small-scale features in ocean winds. Science 303, 978–983. https://
the role of data assimilation process in the convergence of the two doi.org/10.1126/science.1091901.
datasets (e.g., Hodges et al., 2011; Stopa and Cheung, 2014). Colle, B.A., Rojowsky, K., Buonaito, F., 2010. New York city storm surges: climatology
and an analysis of the wind and cyclone evolution. J. Appl. Meteorol. Climatol. 49
(1), 85–100. https://doi.org/10.1175/2009JAMC2189.1.
CRediT authorship contribution statement Copernicus Climate Change Service (C3S), 2017. ERA5: Fifth Generation of ECMWF
Atmospheric Reanalyses of the Global Climate. Copernicus Climate Change Service
Climate Data Store (CDS). July, 2019.
C.B. Gramcianinov: Conceptualization, Formal analysis, Method-
Crespo, N.M., da Rocha, R.P., De Jesus, E.M., 2020a. Cyclones density and characteristics
ology, Validation, Visualization, Writing - original draft. R.M. Campos: in different reanalyses dataset over South America. In: EGU General Assembly 2020.
Conceptualization, Methodology, Writing - review & editing. R. de https://doi.org/10.5194/egusphere-egu2020-11316. Online, 4-8 May 2020,
Camargo: Methodology, Validation, Writing - review & editing. K.I. EGU2020-11316.
Crespo, N.M., da Rocha, R.P., Sprenger, M., Wernli, H., 2020b. A potential vorticity
Hodges: Methodology, Writing - review & editing. C. Guedes Soares: perspective on cyclogenesis over center-eastern South America. Int. J. Climatol. 1–16
Writing - review & editing, Supervision. P.L. da Silva Dias: Writing - https://doi.org/10.1002/joc.6644.
review & editing, Supervision. Dacr N e, o r H th .F . A , t G la r n a t y i , c S c . y L c ., l o 2 n 0 e 0 s 9 . . M T o h n e . W sp e a a ti t a h l e d r i R st e r v ib . u 1 t 3 io 7 n , 9 a 9 n – d 1 1 ev 5 o . l h u t t t i p o s n :/ c / h d a o r i a .o c r t g e / ri 1 s 0 ti . c 1 s 1 o 7 f 5 /
2008MWR2491.1.
Dacre, H.F., Hawcroft, M.K., Stringer, M.A., Hodges, K.I., 2012. An extratropical cyclone
Declaration of competing interest atlas a tool for illustrating cyclone structure and evolution characteristics. Bull. Am.
Meteorol. Soc. 93, 1497–1502. https://doi.org/10.1175/BAMS-D-11-00164.1.
The authors declare that they have no known competing financial da Rocha, R.P., Reboita, M.S., Gozzo, L.F., Dutra, L.M.M., de Jesus, E.M., 2019.
Subtropical cyclones over the oceanic basins: a review. Ann. N. Y. Acad. Sci. 1436,
interests or personal relationships that could have appeared to influence 138–156. https://doi.org/10.1111/nyas.13927.
the work reported in this paper. Evans, J.L., Braun, A., 2012. A climatology of subtropical cyclones in the south atlantic.
J. Clim. 25, 7328–7340. https://doi.org/10.1175/JCLI-D-11-00212.1.
Gan, M.A., Rao, V.B., 1991. Surface cyclogenesis over South America. Mon. Weather Rev.
Acknowledgments 119, 1293–1302. https://doi.org/10.1175/1520-0493(1991)119<1293:
SCOSA>2.0.CO;2.
This work is part of the project “Extreme wind and wave modeling Gozzo, L.F., da Rocha, R.P., Reboita, M.S., Sugahara, S., 2014. Subtropical cyclones over
the southwestern South Atlantic: climatological aspects and case study. J. Clim. 27,
and statistics in the Atlantic Ocean” (EXWAV) funded by the Portuguese 8543–8562. https://doi.org/10.1175/JCLI-D-14-00149.1.
Foundation for Science and Technology (Fundaça˜o para a Ciˆencia e Gramcianinov, C.B., Campos, R.M., Guedes Soares, C., Camargo, R., 2020a. Extreme
Tecnologia – FCT) under contract PTDC/EAM-OCE/31325/2017 waves generated by cyclonic winds in the western portion of the South Atlantic
RD0504, and by the S˜ao Paulo Research Foundation (FAPESP) grant Ocean. Ocean Eng. 213, 107745. https://doi.org/10.1016/j.oceaneng.2020.107745.
Gramcianinov, Campos, R.M., Guedes Soares, C., Camargo, R., 2020b. Comparison
#2018/08057–5. This work contributes to the Strategic Research Plan of between ERA5 and CFS datasets of extratropical cyclones associated with extreme
the Centre for Marine Technology and Ocean Engineering (CENTEC), wave events in the Atlantic Ocean. In: Proceedings of the 29th International
Conference on Offshore Mechanics and Arctic Engineering, Online, 3-7 August,
which is financed by the Portuguese Foundation for Science and Tech-
2020. ASME paper OMAE-18488.
nology (Fundaç˜ao para a Ciˆencia e Tecnologia - FCT) under contract Gramcianinov, C.B., Hodges, K.I., Camargo, R., 2019. The properties and genesis
UIDB/UIDP/00134/2020. C.B.G. holds a FAPESP post-doc scholarship environments of South Atlantic cyclones. Clim. Dynam. 53, 4115–4140. https://doi.
grant #2020/01416–0. The authors would like to acknowledge the org/10.1007/s00382-019-04778-1.
Grise, K.M., Son, S.W., Gyakum, J.R., 2013. Intraseasonal and interannual variability in
NCEP and ECMWF for providing the atmospheric and wave data for the north american storm tracks and its relationship to equatorial pacific variability.
study. The ERA5 products were generated using Copernicus Climate Mon. Weather Rev. 141, 3610–3625. https://doi.org/10.1175/MWR-D-12-00322.1.
Guishard, M.P., Evans, J.L., Hart, R.E., 2009. Atlantic subtropical storms. Part II:
Change Service Information [2019]. This study used the high-
Climatology. J. Clim. 22, 3574–3594. https://doi.org/10.1175/2008JCLI2346.1.
performance computing resources of the SDumont supercomputer (htt Hersbach, H., Dee, D., 2016. ERA5 Reanalysis Is in Production, 147. ECMWF Newsletter,
p://sdumont.lncc.br), which is provided by the National Laboratory Reading, UK. ECMWF.
for Scientific Computing (LNCC/MCTI, Brazil). Hersbach, H., Bell, B., Berrisford, P., Hor´anyi, A., Sabater, J.M., Nicolas, J., Radu, R.,
Schepers, D., Simmons, A., Soci, C., Dee, D., 2018. Global reanalysis: goodbye ERA-
Interim, hello ERA5. ECMWF Newsl 17–24. https://doi.org/10.21957/vf291hehd7.
References Hodges, K.I., 1994. A general method for tracking analysis and its application to
meteorological data. Mon. Weather Rev. 122, 2573–2586. https://doi.org/10.1175/
1520-0493(1994)122<2573:AGMFTA>2.0.CO;2.
Bakhtyar, R., Orton, P.M., Marsooli, R., Miller, J.K., 2018. Rapid wave modeling of
severe historical extratropical cyclones off the Northeastern United States. Ocean
Eng. 159, 315–332. https://doi.org/10.1016/j.oceaneng.2018.04.037.
12

C.B. Gramcianinov et al. O c e a n E n g i n e e r i n g 216(2020)108111
Hodges, K.I., 1995. Feature tracking on the unit sphere. Mon. Weather Rev. 123, Ponce de Leon, S., Guedes Soares, C., 2014. Extreme wave parameters under North
3458–3465. https://doi.org/10.1175/1520-0493(1995)123<3458:FTOTUS>2.0. Atlantic extratropical cyclones. Ocean Model. 81, 78–88. https://doi.org/10.1016/j.
CO;2. ocemod.2014.07.005.
Hodges, K.I., 1996. Spherical nonparametric estimators applied to the UGAMP model Ponce de Leon, S., Guedes Soares, C., 2015. Hindcast of extreme sea states in North
integration for AMIP. Mon. Weather Rev. 124, 2914–2932. https://doi.org/ atlantic extratropical storms. Ocean Dynam. 65 (2), 241–254. https://doi.org/
10.1175/1520-0493(1996)124<2914:SNEATT>2.0.CO;2. 10.1007/s10236-014-0794-6.
Hodges, K.I., 1999. Adaptive constraints for feature tracking. Mon. Weather Rev. 127, Raible, C.C., Della-Marta, P.M., Schwierz, C., Wernli, H., Blender, R., 2008. Northern
1362–1373. https://doi.org/10.1175/1520-0493(1999)127<1362:ACFFT>2.0.CO; hemisphere extratropical cyclones: a comparison of detection and tracking methods
2. and different reanalyses. Mon. Weather Rev. 136, 880–897. https://doi.org/
Hodges, K.I., 2008. Confidence intervals and significance tests for spherical data derived 10.1175/2007MWR2143.1.
from feature tracking. Mon. Weather Rev. 136, 1758–1777. https://doi.org/ Reboita, M.S., da Rocha, R.P., Ambrizzi, T., Sugahara, S., 2010. South Atlantic Ocean
10.1175/2007MWR2299.1. cyclogenesis climatology simulated by regional climate model (RegCM3). Clim.
Hodges, K.I., Hoskins, B.J., Boyle, J., Thorncroft, C., 2003. A comparison of recent Dynam. 35, 1331–1347. https://doi.org/10.1007/s00382-009-0668-7.
reanalysis datasets using objective feature tracking: storm tracks and tropical Reboita, M.S., da Rocha, R.P., de Souza, M.R., Llopart, M., 2018. Extratropical cyclones
easterly waves. Mon. Weather Rev. 131, 2012–2037. https://doi.org/10.1175/1520- over the southwestern South Atlantic ocean: HadGEM2-ES and RegCM4 projections.
0493(2003)131<2012:ACORRD>2.0.CO;2. Int. J. Climatol. 38, 2866–2879. https://doi.org/10.1002/joc.5468.
Hodges, K.I., Lee, R.W., Bengtsson, L., 2011. A comparison of extratropical cyclones in Rienecker, M.M., Suarez, M.J., Gelaro, R., Todling, R., Bacmeister, J., Liu, E.,
recent reanalyses ERA-Interim, NASA MERRA, NCEP CFSR, and JRA-25. J. Clim. 24, Bosilovich, M.G., Schubert, S.D., Takacs, L., Kim, G., Bloom, S., Chen, J., Collins, D.,
4888–4906. https://doi.org/10.1175/2011JCLI4097.1. Conaty, A., da Silva, A., Gu, W., Joiner, J., Koster, R.D., Lucchesi, R., Molod, A.,
Hoskins, B.J., Hodges, K.I., 2002. New perspectives on the northern hemisphere winter Owens, T., Pawson, S., Pegion, P., Redder, C.R., Reichle, R., Robertson, F.R.,
storm tracks. J. Atmos. Sci. 59, 1041–1061. https://doi.org/10.1175/1520-0469 Ruddick, A.G., Sienkiewicz, M., Woollen, J., 2011. MERRA: NASA’s modern-Era
(2002)059<1041:NPOTNH>2.0.CO;2. Retrospective analysis for research and applications. J. Clim. 24, 3624–3648.
Hoskins, B.J., Hodges, K.I., 2005. A new perspective on southern hemisphere storm Saha, S., Moorthi, S., Pan, H., Wu, X., Wang, J., Nadiga, S., Tripp, P., Kistler, R.,
tracks. J. Clim. 18, 4108–4129. https://doi.org/10.1175/JCLI3570.1. Woollen, J., Behringer, D., Liu, H., Stokes, D., Grumbine, R., Gayno, G., Wang, J.,
Hoskins, B.J., Hodges, K.I., 2019a. The annual cycle of Northern Hemisphere storm Hou, Y., Chuang, H., Juang, H.H., Sela, J., Iredell, M., Treadon, R., Kleist, D.,
tracks. Part I: Seasons. J. Clim. 32, 1743–1760. https://doi.org/10.1175/JCLI-D-17- Delst, P. Van, Keyser, D., Derber, J., Ek, M., Meng, J., Wei, H., Yang, R., Lord, S.,
0870.1. Dool, H. van den, Kumar, A., Wang, W., Long, C., Chelliah, M., Xue, Y., Huang, B.,
Hoskins, B.J., Hodges, K.I., 2019b. The annual cycle of Northern Hemisphere storm Schemm, J., Ebisuzaki, W., Lin, R., Xie, P., Chen, M., Zhou, S., Higgins, W., Zou, C.,
tracks. Part II: regional detail. J. Clim. 32, 1761–1775. https://doi.org/10.1175/ Liu, Q., Chen, Y., Han, Y., Cucurull, L., Reynolds, R.W., Rutledge, G., Goldberg, M.,
JCLI-D-17-0871.1. 2010. The NCEP climate forecast system reanalysis. Bull. Am. Meteorol. Soc. 91,
Jones, D.A., Simmonds, I., 1993. A climatology of Southern Hemisphere extratropical 1015–1058. https://doi.org/10.1175/2010BAMS3001.1.
cyclones. Clim. Dynam. 9, 131–145. https://doi.org/10.1007/BF00209750. Saha, S., Moorthi, S., Wu, X., Wang, J., Nadiga, S., Tripp, P., Behringer, D., Hou, Y.,
Kalnay, E., Kanamitsu, M., Kistler, R., Collins, W., Deaven, D., Gandin, L., Iredell, M., Chuang, H., Iredell, M., Ek, M., Meng, J., Yang, R., Mendez, M.P., Dool, H. van den,
Saha, S., White, G., Woollen, J., Zhu, Y., Chelliah, M., Ebisuzaki, W., Higgins, W., Zhang, Q., Wang, W., Chen, M., Becker, E., 2014. The NCEP climate forecast system
Janowiak, J., Mo, K.C., Ropelewski, C., Wang, J., Leetmaa, A., Reynolds, R., version 2. J. Clim. 27, 2185–2208. https://doi.org/10.1175/JCLI-D-12-00823.1.
Jenne, R., Joseph, D., 1996. The NCEP/NCAR 40-year reanalysis project. Bull. Am. Sebastian, M., Behera, M.R., Murty, P.L.N., 2019. Storm surge hydrodynamics at a
Meteorol. Soc. 77, 437–472. https://doi.org/10.1175/1520-0477(1996)077<0437: concave coast due to varying approach angles of cyclone. Ocean. Eng. 191 https://
TNYRP>2.0.CO;2. doi.org/10.1016/j.oceaneng.2019.106437.
Kumar, V.S., Mandal, S., Kumar, K.A., 2003. Estimation of wind speed and wave height Simmonds, I., Keay, K., 2000. Mean southern hemisphere extratropical cyclone behavior
during cyclones. Ocean Eng. 30, 2239–2253. https://doi.org/10.1016/S0029-8018 in the 40-year NCEP-NCAR reanalysis. J. Clim. 13, 873–885. https://doi.org/
(03)00076-3. 10.1175/1520-0442(2000)013<0873:MSHECB>2.0.CO;2.
Mattioli, M., De Masi, G., Drago, M., 2019. Evaluating extreme cyclonic sea states. Ocean Simmons, A., Uppala, S., Dee, D., Kobayashi, S., 2007. ERA-interim: New ECMWF
Eng. 194, 106639. https://doi.org/10.1016/j.oceaneng.2019.106639. Reanalysis Products from 1989 Onwards, 110. ECMWF Newsletter, Reading, UK,
Mendes, D., Souza, E.P., Marengo, J.A., Mendes, M.C.D., 2010. Climatology of pp. 25–35. ECMWF.
extratropical cyclones over the South American-southern oceans sector. Theor. Appl. Sinclair, M.R., 1994. An objective cyclone climatology for the Southern Hemisphere.
Climatol. 100, 239–250. https://doi.org/10.1007/s00704-009-0161-6. Mon. Weather Rev. 122, 2239–2256.
Murray, R.J., Simmonds, I., 1991a. A numerical scheme for tracking cyclone centres from Sinclair, M.R., 1997. Objective identification of cyclones and their circulation intensity,
digital data Part I: development and operation of the scheme. Aust. Meteorol. Mag. and climatology. Weather Forecast. 12, 595–612. https://doi.org/10.1175/1520-
39, 155–166. 0434(1997)012<0595:OIOCAT>2.0.CO;2.
Murray, R.J., Simmonds, I., 1991b. A numerical scheme for tracking cyclone centres Stopa, J.E., Cheung, K.F., 2014. Intercomparison of wind and wave data from the
from digital data. Part II: application to January and July general circulation model ECMWF reanalysis Interim and the NCEP climate forecast system reanalysis. Ocean
simulations. Aust. Meteorol. Mag. 39, 155–166. Model. 75, 65–83.
Olauson, J., 2018. ERA5: the new champion of wind power modelling? Renew. Energy Trigo, I.F., 2006. Climatology and interannual variability of storm-tracks in the Euro-
126, 322–331. https://doi.org/10.1016/j.renene.2018.03.056. Atlantic sector: a comparison between ERA-40 and NCEP/NCAR reanalyses. Clim.
Onogi, K., Tsutsui, J., Koide, H., Sakamoto, M., Kobayashi, S., Hatsushika, H., Dynam. 26, 127–143. https://doi.org/10.1007/s00382-005-0065-9.
Matsumoto, T., Yamazaki, N., Kamahori, H., Takahashi, K., Kadokura, S., Wada, K., Vettor, R., Guedes Soares, C., 2016. Rough weather avoidance effect on the wave climate
Kato, K., Oyama, R., Ose, T., Mannoji, N., Taira, R., 2007. The JRA-25 reanalysis. experienced by oceangoing vessels. Appl. Ocean Res. 59, 606–615. https://doi.org/
J. Meteorol. Soc. Japan. Ser. II 85, 369–432. https://doi.org/10.2151/jmsj.85.369. 10.1016/j.apor.2016.06.004.
Parker, W.S., 2016. Reanalyses and observations: what’s the Difference? Bull. Am. Vettor, R., Guedes Soares, C., 2017. Characterization of the expected weather conditions
Meteorol. Soc. 97, 1565–1572. https://doi.org/10.1175/BAMS-D-14-00226.1. in the main European coastal traffic routes. Ocean Eng. 140, 244–257. https://doi.
Pinto, J.G., Spangehl, T., Ulbrich, U., Speth, P., 2005. Sensitivities of a cyclone detection org/10.1016/j.oceaneng.2017.05.027.
and tracking algorithm: individual tracks and climatology. Meteorol. Z. 14, 823–838.
https://doi.org/10.1127/0941-2948/2005/0068.
13