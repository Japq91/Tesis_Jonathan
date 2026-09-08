OpEN

DATA DEsCRIpTOR

North atlantic Extratropical
Cyclone tracks and Lagrangian-
Derived Moisture Uptake Dataset

Patricia Coll-Hidalgo
Raquel Nieto1 & Luis Gimeno1

 1 ✉, Luis Gimeno-Sotelo1, José Carlos Fernández-alvarez1,2,

Extratropical cyclones (EtCs) are the focus of many open questions, spanning from weather to
climate and from local to global scales. the relationship between moisture uptake and precipitation
over different mesoscale ETC structures remains poorly understood. The availability of moisture
parameters to the scientific community through tracer dispersion models benefits the representation
of the processes involving moisture, the dynamics of EtCs and the understanding of the associated
meteorological fields. In this study, we present a database for North Atlantic ETC tracks and a
Lagrangian-Derived Moisture Uptake Dataset, both of which are derived from dynamically downscaled
ERA5 reanalysis data. We provide moisture parameters such as the total moisture uptake and its vertical
distribution by layer, and shapefiles of ETC structures, to facilitate further studies in this area. Our data
have been thoroughly validated to ensure that the storm tracks and their characteristics are accurately
represented in the model without distortion. additionally, we conduct a series of experiments to
demonstrate the rigour and quality of the methods employed to generate the data.

Background & Summary
An extratropical cyclone (ETC), also referred to as an extratropical low- or mid-latitude cyclone, is a large-scale,
low-pressure weather system that plays an important role in global atmospheric circulation by providing, trans-
porting, and redistributing energy and moisture1. The track, frequency, variability and intensity of ETCs signifi-
cantly influence daily weather conditions and even determine the climate at mid-latitudes2–5.

ETCs and their associated complex mesoscale structures are identified as notable contributors to the weather
and climate in extratropics, accounting for up to 90% of the total precipitation, often accompanied by extreme
precipitation5–7, or compound precipitation and wind extremes combined events8–10. The economic conse-
quences of ETCs can be substantial, impacting infrastructure, agriculture, and businesses11,12. In 2022, ETC
Eunice13,14 incurred total economic losses of US$6.2 billion, making it the costliest storm since ETC Xynthia
in 201013–15. The sequence of windstorms from February 16 to 21, 2022—including ETCs Dudley, Eunice, and
Franklin—resulted in losses totaling US$4.7 billion16,17.

The beneficial impact of ETCs should also be considered. The renewable energy sector, such as hydropower
generation and wind energy, highly depends on their occurrence18–21. Conversely, both types of energy are often
combined in a given region, and the variability in the size of ETCs (arising from their large spatial scale) signif-
icantly determines the atmospheric conditions in different parts within the same energy system. These fluctua-
tions pose a risk to the stability of the power net, as sudden weather changes can affect the reliability of energy
generation and transmission18,22.

The study of ETC is hampered by several problems, mainly due to the lack of observational databases, mak-
ing it difficult to assess reference data. Moreover, uncertainty arises in fundamental aspects such as the detection,
tracking, and delineation of the cyclone extent or shape. Tracking algorithms based on gridded data encom-
pass a variety of approaches23, ranging from physics-based criteria, such as the sea-level pressure minimum, to
dynamic-based criteria, such as the vorticity, with detection capabilities that notably differ, introducing biases24.
Additionally, the ETCs rainfall-generating structures and atmospheric conditions vary significantly, as do
the drivers of precipitation occurrence25–28. Recently, Papritz et al.29 provided a noteworthy perspective by

1centro de investigación Mariña, Universidade de Vigo, environmental Physics Laboratory (ePhysLab), campus As
Lagoas s/n, 32004, Ourense, Spain. 2Galicia Supercomputing center (ceSGA), Santiago de compostela, españa.
✉e-mail: patricia.coll@uvigo.gal

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1

www.nature.com/scientificdatainvestigating the sources and transport pathways of precipitating vapour during the cold season associated with
deep cyclones over the North Atlantic Ocean (NATL). They identified a critical gap in understanding the influ-
ence of long-range moisture transport on ETC precipitation. Their findings indicate that the water budget for
precipitation occurring in dynamic settings outside the ETC radius is crucial for assessing interactions within
ETCs and moisture transport from the subtropics and tropics.

The precipitation structure associated with ETCs30 is influenced by several mesoscale features, including
fronts31,32 and post-cold-frontal regions33,34. Additionally, specific ETC-relative flow patterns, such as the warm
conveyor belt (WCB), can significantly enhance precipitation7,35,36. The WCB, characterized as an upward air-
stream of warm, moist air originating from the warm sector of an ETC37, transports substantial amounts of
water vapour from the boundary layer into the upper troposphere38. Most of the motion is parallel to the cold
front; about 70% of WCBs are associated with cold fronts in winter35. However, as the WCB ascends, it develops
rearward- and forward-sloping structures39. Pfahl et al.40 found that over 60% of extreme precipitation events in
storm-track regions are related to WCBs. Additionally, Papritz et al.29 highlighted that during the intensification
phase of extratropical cyclones, WCB particles account for approximately 15–35% of all precipitating air mass
trajectories within a given radius.

Within this context of mesoscale features, the computation of diagnostic variables related to ETCs and their
transported moisture fields involves rigorous methodologies. One of the most relevant techniques for tracking
the trajectories associated with a given weather system is the Lagrangian framework41. This methodology entails
discretizing the atmospheric column associated with cyclones into parcels, tracking their trajectories, and mon-
itoring changes in the moisture content. For such small-scale applications, Lagrangian particle tracking models
such as the FLEXible PARTicle (FLEXPART) model42–45, coupled with mesoscale models such as the Weather
Research and Forecasting (WRF) model46 (FLEXPART-WRF47), provide several advantages options for physical
scheme implementations, particularly in the boundary layer dynamic.

In this study, we developed the ExCyclone-TRAMO database (EXtratropical CYCLONE TRAcks and
MOisture), derived from high-resolution data, to support climatological research on ETC moisture uptake and
its relationship with dynamic atmospheric structures. The ExCyclone-TRAMO dataset was constructed from
data obtained by dynamic downscaling of ERA5 data48 using the WRF model46. The database covers ETCs over
the NATL during extended winter seasons from October to April 1985 to 2022. The ETC moisture database is
intrinsically linked to a comprehensive database of all the positional characteristics, sizes and tracks of each
system. Our dataset includes individual shape files of ECs. These masks define the regions used to delineate the
ETC throughout its lifecycle, incorporating the cyclone radius, WCB-related areas, and a theoretical boundary
that encompasses a broader extent of the ETC circulation within a spiral shape, which is very similar to the
conceptual morphology of ECs.

The technical, educational, and research applicability of the ExCyclone-TRAMO database is reinforced by
the innovations it offers. This dataset, derived from a WRF model configuration capable of downscaling climate
data49, serves as a benchmark for similar studies and enhances the understanding of ETC dynamics. The dataset
includes masks for the ETC target regions, capturing a wide range of features associated with these cyclones.
Future studies that aim to conceptualise and capture these features using neural networks could leverage our
results as a comparative reference. Furthermore, researchers will have access to free data, enabling them to man-
age and analyze the information according to their specific needs. Additionally, the moisture uptake associated
with cyclone precipitation is documented in NETCDF4 files. These files provide 6-hourly data on daily moisture
uptake and the vertical stratification of tracer particles in the target region. This represents a significant advance
in the study of moisture uptake at different levels and the mechanisms involved.

Methods
A comprehensive approach was employed to generate a 6-hourly dataset, which included qualitative cyclone
track characteristics, two-dimensional masks of cyclone radius, WCB-related areas, and square root spiral cap-
turing the ETC structure, and moisture uptake-related variables. The steps involved in this process are summa-
rized as follows:

  1.  ERA5 data were dynamically downscaled using the WRF model.
  2.  ETCs were detected and tracked using the WRF outputs.
  3.  At each time step of the ETC life cycle, key parameters such as radius, the Eulerian footprint of WCB

occurrence, and a root square spiral centred on the system were calculated.

  4.  WRF simulations were subsequently used to run the Lagrangian FLEXPART-WRF dispersion model, ena-
bling the identification of moisture uptake parameters, with the identified masks serving as target regions.

Figure 1 illustrates the sequential methodology employed in this study, with further details on the method-

ology and models provided in the following sections.

Model configuration.
In this study, we employed WRF (v4.2) simulations initialized and forced at bound-
aries every 6 h with the latest reanalysis dataset ERA5 (hereafter referred to as WRF). Our simulations, accessi-
ble upon request within the Environmental Physics Laboratory (EPhysLab) group, consist of 40 vertical levels
and a horizontal resolution of 20 km. The simulation domain (Fig. 2) covers the NATL basin and its surround-
ings, ensuring to encompass geographic regions identified as continental cyclogenesis hotspots based on rea-
nalysis and global climate models, primarily following the work of Hodges et al.50, Neu et al.24, Poan et al.51, and
Gramcianinov et al.52.

In all simulations, time continuity over the 1985–2022 period was preserved, and a 1-month spin-up period
was used. The chosen parameters include the WSM6 microphysics scheme53, the Yonsei University planetary

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

2

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 1  The methodology used in this investigation.

Fig. 2  Simulation domains of the WRF (red contour) and FLEXPART-WRF models (green contour).

boundary layer scheme54, the revised MM5 surface layer scheme55, the United Noah Land Surface Model56, the
short and longwave RRTMG schemes57, and the Kain-Fritsch ensemble cluster scheme58. In addition, spectral
nudging was applied to waves longer than 1,000 km to avoid distortion of the large-scale circulation within
the regional model domain59. This configuration has been extensively utilized and assessed for climatic model
downscaling and reanalysis of ERA5 data in our area of interest49,60–63.

The Lagrangian FLEXPART-WRF model v3.3.247 was also used in this study. This model entails the use of
mesoscale model outputs to initiate a Lagrangian dispersion of active moisture tracers (particles). The model
generates new output files that contain information on the concentration of the released particles (in this
case, air masses), specifically domain-filling trajectories in the simulated atmosphere. Under this scenario, the
FLEXPART-WRF model was driven by the WRF dataset, using a time step of 6 hours. In the simulations, the
atmosphere was divided into approximately 2 million air parcels, which were evenly distributed throughout the
domain and advected in time by the WRF 3D wind field. The number of particles was selected to ensure a more
balanced distribution at each grid point and vertical level49,61.

The FLEXPART-WRF simulations incorporate activated subgrid terrain effect parametrization and include
convection options throughout the process [see Supplementary Material in 48]. In the model, the vertical veloc-
ity based on divergence is used to represent vertical motion. The model incorporates a diagnosed turbulence
scheme to account for turbulent effects. In this configuration, turbulence is treated using the Hanna scheme,
which is specifically designed to function with an activated convection scheme64). The Hanna scheme considers
various boundary layer parameters, including the PBL height, Monin-Obukhov length, convective velocity scale,
roughness length, and friction velocity47. For the WRF model described above, the FLEXPART-WRF model is
operated at a spatial resolution of 20 km. The configuration was validated against global FLEXPART results fitted
with ERA5 data, as documented in49,60,61. This process enhanced the confidence in the model configuration.

EC Detection and tracking methodology.  Storm track identification is a complex task, both for physical
reasons, as there are many influencing factors such as the surface roughness, planetary-scale stationary waves,
and intrinsic ETC dynamics (Schultz et al.65, for a review), and for computational reasons, as there are different
tracking algorithm methods and gridded data resolutions24. This has resulted in a variety of previous ETC track
datasets24,52,66 with a lack of consensus and uncertainties in the tracks. Each new ETC dataset study acknowledges
the benefits (or lack thereof) of the proposed methodology, considering both spatial and temporal representa-
tions of the data, but refrains from declaring any as universally good or bad.

In this study, cyclone tracks were constructed by connecting successively detected minimum centres within
the MSLP field. First, we prefiltered potential centres in the MSLP field as locations where the MSLP anomaly,

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

3

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 3  Track of an ETC over the North Atlantic basin during the winter season of 2001–2002, from February 8
to February 12. This corresponds to case number 029 of 2002 in the dataset. The data (in mmdd/hh format) are
shown in boxes, along with the mean sea level pressure (MSLP, in hPa) at the centre and the radius of the ETC
(in km). The red signal indicates the minimum MSLP reached by the storm.

i.e., the difference between the current MSLP and the average over the previous 14 days, reaches a minimum
lower than −3 hPa (adapted from Bacmeister et al.67). Later, the final centres satisfied the criterion of repre-
senting a local minimum among eight neighbouring grid points. To track the systems, we identified the closest
match for each centre within a restricted radius of 1,000 km among the recognized cyclone centres six hours
later68–70. If multiple centers are identified within the critical distance, the point with the lowest MSLP is selected
as the cyclone center at the second time step.

To eliminate other cyclonic features, such as mesoscale storms, convergence areas, and thermal lows, the
track was excluded from the datasets if the lifetime of the ETC was less than 48 h and the displacement of the
system did not exceed 1,000 km52. This methodology was implemented in the CyTRACK program71, which has
been validated over the NATL region against a large set of previous methods for detecting and tracking using
ERA5 reanalysis data.

In addition, we discarded those systems whose centre never reached the domain in the NATL basin between
25°N and 60°N and 100°W and 5°W. Additionally, a structural distinction was made between cold-core, asym-
metrical (frontal) systems and warm-core, axisymmetric systems, following the cyclone phase-space method-
ology72,73. We examine systems that undergo extratropical transition (ET) based on the definition provided
by Evans and Hart73. The onset of ET is identified when the thermal asymmetry parameter (B) exceeds 10 m,
indicating a significant thickness asymmetry in the system. The completion of ET is determined by detecting a
transition to a cold-core thermal wind field. Specifically, ET is considered complete when the low-level thermal
wind parameter first becomes negative. Systems that do not exhibit any of these characteristics at any point in
their lifecycle are excluded from the database (a total of 34 systems were removed). Seventy-six systems devel-
oped a cold core but did not reach a frontal stage, and 102 systems, despite being asymmetric, did not develop a
cold core. Systems that completed ET (747 in total) are listed in a companion file in the repository. None of the
aforementioned systems were excluded from the ExCyclone-TRAMO database, as we recognize the variability
that different pathways for identifying ET can entail. Further analysis of ET is available in the Supplementary
Material.

Figure 3 shows the tracking of an ETC case that occurred in February 2002 to demonstrate the functionalities
of the database. This EC, which occurred in 2002, is case number 029 in our database, hereafter referred to as
EC02902.

EC shape modelling.
In this study, we defined three types of masks for each ETC to delineate the areas influ-
enced by the system dynamics. To provide a comprehensive understanding of our methodology, we first present
an overview of the procedure, which is detailed in the subsequent sections. We initially delimited a radius centred
on the core of the EC. We then defined the area of influence of the WCB airstream, a mechanism extensively
studied for detection in gridded datasets. This type of research has been conducted over time from different per-
spectives, from particle-to-particle ascent rate analysis 74,75 and regression models76,77 to the latest method—con-
volutional neural network (CNN) models78,79. In a more ambitious step to shape the EC, we included an extended,
nonsymmetric area encompassing a wide range of characteristics. This approach was primarily influenced by con-
ceptual models and a straightforward computation method: a square root spiral. The database can be expanded
and rendered as complex as needed to adapt its applicability.

The three definitions used to delimit ETCs (radius, WCB, and spiral) provide a solid basis for further mete-
orological analysis and are used here to compute the related moisture parameters in the database. The detailed
calculation criteria are outlined in the following sections.

Radius estimation.  We estimated the ETC radius using the method outlined by Rudeva and Gulev80, which
relies on the contour of the last closed isobar. First, we generated a pattern with 36 radial legs centred on the

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

4

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 4  ETC shape modelling for case 029 that occurred in February 2002 (EC02902) over the North Atlantic
(NATL) basin: (a) Elements that intervene in radius estimation80 based on mean sea level pressure (MSLP) WRF
outputs (brown contours) for 9 February 2002 at 0600 UTC EC. The red cross denotes the centre of the cyclone.
The red dotted lines indicate the radial legs, the black contours denote the minimum critical MSLP interpolated
at each leg, and the green area denotes the triangle formed. The blue circumference represents the area within
the last closed isobar (shaded in grey), with the purple line indicating the radius of the circumference. (b) Text
box indicating the date and time for the centres of EC02902 plotted along its track, with the radius (in blue
dashed lines) on each date. The probabilities of occurrence for the WCB stages at 0.15, 0.3, and 0.45 are shown
in contours. The inflow stage is shown in red, while the ascent stages are depicted in blue, and the outflow stage
is shown in green.

P WCB inflow

WCB ascent

WCB outflow

1

2

3

4

5

700 hPa thickness advection

850 hPa relative vorticity

300 hPa relative humidity

850 hPa meridional moisture flux

700 hPa relative humidity

300 hPa irrotational wind speed

1,000 hPa moisture flux convergence 300 hPa thickness advection

500 hPa static stability

500 hPa moist potential vorticity

500 hPa meridional moisture flux

300 hPa relative vorticity

24 h later predicted conditional
probability of WCB ascent

30-d running mean trajectory based on the
climatological WCB occurrence frequency

24 h earlier predicted conditional
probability of WCB ascent

Table 1.  Predictors for the WCB inflow, ascent, and outflow CNN models79.

low-pressure system. Each leg extended 2,000 km from the origin, spaced at 10-degree angular intervals. For
each leg, we determined the critical value of the MSLP by identifying the position of the zero-tended first radial
derivative. The minimum critical MSLP value was interpreted as the value of the last closed isobar, which was
subsequently interpolated along each leg. The consecutive points along the last closed isobar and the centre of
the ETC form triangles with known areas. The sum of all these areas was then assumed as the area of virtual
circumference, and its radius was considered the effective radius of the cyclone. The elements described in this
procedure are shown in Fig. 4a for case EC02902 on 9 February 2002 at 0600 UTC.

In this dataset, the ELIAS2.0 CNN model79 was employed to delineate the WCB masks. The
WCB footprints.
successful application of this CNN model has been demonstrated for datasets with diverse spatial and temporal
resolutions, including those with a resolution as fine as 13 km81. The WCB physical predictors needed as input
data for ELIAS2.0 (Table 1) were derived from our WRF output. The variables used are the temperature, geopo-
tential height, specific humidity, and horizontal wind component fields. Before implementing the CNN models,
we projected the predictors from the WRF outputs onto a regular 1° × 1° latitude-longitude grid. The final layer
of the CNN was activated using a sigmoid function, which produced outputs ranging from 0 to 1.

These outputs can be interpreted as conditional probabilities, with our primary focus on probabilities exceed-
ing 0.05. This lower threshold was chosen to encompass larger potential areas of WCB occurrence, conform-
ing with our objective of providing the moisture uptake parameter for precipitating particles involved in this
dynamic flow. Figure 4b shows the probabilities of the inflow, ascent, and outflow contours corresponding to
the stages of the WCB for the days of EC02902 occurrence. We associate a WCB stage area with a cyclone at
each time step when the probability value exceeded 0.05 at a given grid point enclosed by the identified cyclone
area. Although ELIAS2.0 comprises models for each stage of the WCB, including inflow, ascent, and outflow
footprints, we integrated all these areas into one to provide a comprehensive view of the overall structure in our
final shape files.

When considering probability traces of WCB occurrence, it is essential to adjust its area of occurrence as
closely as possible according to the conceptualization and understanding of the interaction between this mecha-
nism and ETCs39,65. This necessity drives us to define the cyclone area as a broader region that includes the WCB
and the core of the low-level pressure regime.

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

5

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 5  ETC shape modelling for the EC02902 case on February 8, 2002, at 1200 UTC over the North Atlantic
(NATL) basin. In (a), the background shows the WRF outputs, including the mean sea level pressure (MSLP) in
hPa (red contours), 2-m wind vectors in m/s, and 6-hourly accumulated precipitation fields shaded in mm
(shaded). Additionally, the 925 hPa equivalent potential temperature (θe) is represented by purple lines at 290,
310, and 315 K. (b) The background shows a geostationary infrared channel brightness temperature from
GridSat-B1 climate data. The contour lines denote the WCB probability occurrence stages of inflow (in red),
ascent (in blue), and outflow (in green) at 0.15. The dashed blue lines indicate the radius, while a yellow marker
denotes the centre of the EC. The square root spiral shape is outlined in brown.

Square root spiral.  To delineate the ETC shape that includes the mentioned structures, the WCB and the radius
around the core of the cyclone, we defined it as a region characterized by the vertices of a discrete square root
spiral.

Following Gautschi82, to produce the vertices of the spiral

( )
T n

=

ing equations:

T n
,
n

=

0,1,2

…

, we employed the follow-

|

| =T
n

n

|

+T
n

1

− | =
T
n

1

(1)

(2)

where n reaches up to 17, after which all subsequent lines intersect part of the figure already drawn.

In the MSLP field, the angles and hypotenuses of the spiral were adjusted to facilitate dynamic sizing, thereby
accommodating variations in cyclone dimensions. In a reference polar system centred on the ETC position, a
spiral and its new vertices were created by introducing a factor <f> related to the original (standard) length.
This factor <f> enables the adaptation of each geometry to the pressure drop induced by the cyclonic system
and accounts for the case-to-case variability. The mean extension of the pressure decrease attributed to the ETC
can  be  approximated  by  averaging  the  distances  from  the  ETC  centre  over  which  the  criterion
 is satisfied. Moreover, <k> and <k-1> are grid locations, and 150 km spatial steps are
−
<−
MSLP MSLP
0
k 1
saved in 36 radial legs spaced at 10° angles.

k

Figure 5a shows the spiral pattern of EC02902 on February 8 at 1800 UTC. The spiral encloses the latitudes
where the WCB areas are identified, as shown in Fig. 5b. The resulting area is well suited for representing the
central structure of the cyclone, comma patterns, fronts, warm sector, and EC-related structures, as is also shown
in the infrared channel (IR) satellite image in Fig. 5b. In addition, regarding the meteorological fields, the spiral
encompasses the closed circulation towards the centre of minimum pressure values, the 6-hour accumulated
precipitation pattern, and the curvature in the equivalent potential temperature field and agrees with the 2-m
wind behaviour.

Moisture uptake analysis.  Once the position and shape of the ETC have been determined and using the
trajectories simulated by the FLEXPART-WRF model, we can select air parcels of the atmospheric vertical col-
umn within each ETC to perform Lagrangian analysis of the water balance of these parcels involved in the EC.

We applied a Lagrangian moisture source diagnostic method developed by Sodemann et al.83 and coded it
into the TRansport Of water VApor (TROVA) tool84. Based on the methodology of Stohl and James42,85, to
account for the net moisture losses and gains in humidity (E - P) over gridded area A along the track of the air
masses, Sodemann et al.83 applied certain constraints to the modelled air particles to efficiently quantify mois-
ture sources for precipitation. Notably, (E - P) for the trajectories of i particles over area A can be calculated as
follows:

E

− =
P

∑

i
i

=

0

(
e

−

p

)
i

A

(
e

−

p

)

=

m

i

dq

dt

(3)

(4)

where  −e

(

p

)  accounts for changes in the specific humidity (q) of each air particle (i) of a constant mass (Eq. 4).

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

6

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 6  Moisture uptake patterns for EC02902 during its genesis phase on February 8, 2002 at 1200 UTC (ETC
centre marked in red) for the target region defined as: (a) radius, (b) warm conveyor belt (WCB), and (c) spiral.
The corresponding vertical cross sections along the red line of the moisture uptake field are shown in panels (d–f).

In our analysis, we filtered particles within the target regions (radius, WCB and spiral) to include only those
that precipitate. Precipitating particles were defined as those whose specific humidity decreased by more than
0.1 g/kg before reaching the target region, following the method of Läderach and Sodemann86.

Notably, <dt> denotes a 6-hour interval, constituting one of the 40 steps needed to complete the 10-day
backward particle path, the usual time (mean time life of water vapour in the atmosphere) to follow them back-
wards in studies of source‒sink moisture relationships41,87,88. Subsequently, we accumulated moisture uptake
along the parcel trajectories, deducing precipitation en route, as outlined by Sodemann et al.83. Therefore, the
decrease in the specific humidity proportionally accounted for all moisture uptake preceding the precipitation
event.

This methodology has been applied in previous studies to investigate moisture sources for different weather
systems, including ETCs29,89 and Mediterranean cyclones66. It has also been used to examine larger-scale trans-
port phenomena, such as the East Asian monsoon90.

Figure 6a,c,e show the moisture uptake patterns for EC02902 at its genesis, its radius, WCB, and spiral target
regions, respectively. Figure 6b,d,f show cross sections of the moisture uptake field. Differences are observed
in the intensity of moisture uptake, geographical extent of the sources, and vertical gains, consistent with the
different shapes of the target regions and given the larger number of particles represented by the larger areas.

Furthermore, to identify moisture drivers, we computed the 6-hourly (eastwards and northwards) vertically
integrated moisture flux (VIMFx and VIMFy, as expressed in Eq. 5) and the integrated water vapour column
(IWVC, Eq. 6) from the WRF outputs.

VIMF VIMF
,
(
y
x

)

=

IWVC

=

−

1
g

−

1
g

P

t∫

P
s

q

⋅

)
u v dp
( ,

P
t

∫

P
s

qdp

(5)

(6)

Vertical integration was conducted across pressure levels (p) from the surface (Ps) to the uppermost level
(Pt = 300 hPa), where q denotes the specific humidity, g is the gravitational acceleration, and (u, v) denotes the
horizontal zonal and meridional wind fields.

Data Records
The ExCyclone-TRAMO dataset is publicly accessible at https://doi.org/10.5281/zenodo.1384437891, where
detailed guidelines are provided, including a thorough description of the files, variables, and scripts needed for
reproducing analyses or managing the data, as outlined in this data description.

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

7

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 7  ExCyclone-TRAMO dataset directory structure.

The last update date of the repository contains information on the tracks of 11,177 ETC cases over the
Atlantic. Information on masks (EC target regions) and descriptive variables of the moisture uptake measure-
ments is available for the 237 most intense ETC cases (based on depth—defined as the difference between the
central minimum pressure and the pressure of the outermost closed isobar—), and this information is docu-
mented in the database and stored in the <EC_NATL_int_1985_2022.dat> file.

The dataset is organized within folders for each year from 1985 to 2022. Within each year, there are sub-
folders named according to the following convention: mm_seasoninfo (mm=month). The provided seasonal
information indicates whether the month corresponds to the winter season of the year folder or a previous year,
providing a benchmark for code interpretation.

Inside each monthly folder, there are subfolders named according to an index corresponding to each ETC
case in that year. The order is determined by the chronological formation of ECs, with each index represented by
a three-digit number. Within each ETC subfolder, files include track data, and, where applicable, mask data and
moisture uptake variables. The inclusion of mask data and moisture uptake variables is based on the information
in the EC_NATL_int_1985_2022.dat file, which identifies the most intense cases. Figure 7 shows a schematic of
the allocation of repository directories.

Track data file (track_idx.dat):

The ‘.dat’ file contains a header in the following format:

NATL0091985, where NATL is standard for all cases, indicating the North Atlantic basin. The number of

lines corresponds to the ETC lifetime in 6-hour time steps, which are coded as follows:

19850105, 18, 43.96, −62.53, 967.133, 996.137, 1041.71,

The rows correspond to the following:

yyyymmdd: Date in year-month-day format

•
•	 hh (in UTC): Hour in Coordinated Universal Time
latitude (degrees north): Latitude in degrees north
•
•
longitude (degrees west): Longitude in degrees west
•	 MSLP (hPa): Mean sea level pressure in hectopascals (hPa)
•	 Radius (km): Cyclone radius in kilometres (km)
•	 Last closed isobar (hPa): Pressure at the last closed isobar in hectopascals (hPa)
T)
•	 Low-level thermal wind parameter (VL
T)
•	 High-level thermal wind parameter (VU
•	 The thermal asymmetry parameter (B)

Mask data file (type-mask_idx.nc):

The “type-mask” attribute can take the following names: “radius”, “spiral”, or “wcb”. These names correspond
to the decided shapes for representing the cyclone in the meteorological data. It is a binary output where a value
of 1 indicates the “true” mask.

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

8

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 8  Probability density of ETCs in the North Atlantic (NATL) domain during extended winters from 1985
to 2022 within each 1° × 1° bin. The top panel shows the entire lifetime of ETCs; the middle panel displays
the genesis moment; and the bottom panel depicts the peak intensity stages. Panels (a–c) present the ERA5
reanalysis data, while panels (d–f) show the WRF data.

Moisture Uptake Variables file (type-mask):

The ‘type-mask’ (‘radius’, ‘spiral’ or ‘wcb’) folder contains the resultant moisture uptake files for each type of
mask. It is crucial to note that different particles were used in water budget analysis for each mask. Therefore, it
is important to carefully match the desired results with the chosen mask.

Each NetCDF file in the folder corresponds to the output of a masked variable from the ‘typemask_idx.nc’
file. They are labelled based on the date of cyclone position analysis in yyyymmddhh format, followed by the ‘.nc’
extension. These files contain the daily variable <E‒P> in either 10-day backward analysis or integrated form,
along with the stratified field in layers from the surface to 100 hPa.

technical Validation
Strom track properties.  Our study specifically focuses on precipitation associated with regions where ETCs
occur, highlighting the importance of evaluating the detection and representation of these systems in the WRF
model as a necessary prerequisite.

The configuration of the WRF model for the NATL with a 20-km horizontal resolution was previously vali-
dated for the 1985–2014 period by Fernández-Alvarez et al.49,60,61 using ERA5 data. Additionally, the ETC track-
ing tool (CyTRACK) that was employed in our workflow was validated against other methods and storm tracks24
by Pérez-Alarcón et al.71. However, to assess the accuracy of our cases and ensure the preservation of storm
track characteristics, we compared the resulting high-resolution ExCyclone-TRAMO dataset to the ERA5 data.
Therefore, the tracking algorithm was applied to the ERA5 reanalysis data and the downscaled ERA5 data by the
WRF for the winter seasons over the NATL, and the results were highly consistent. For the ERA5 data, the mean
number of ETC systems per year was 119.0 ± 7.13, and for the WRF data, the value was 106.5 ± 15.28.

Figure 8 shows the track density probabilities within each 1° × 1° bin for the ETCs entire lifetime, at the moment of
genesis, and peak intensity stages (maximum of MSLP is reached). For both datasets the NATL storm tracks (Fig. 8a,d)
show a region of maximum track density extending northeastward from the eastern coast of North America to
Greenland and northern Europe, in concordance with previous studies using other reanalysis or ERA5-based vortic-
ity fields50,52. Additionally, the storm track derived from the WRF simulations (Fig. 8d) reveals a widespread proba-
bility of occurrence across the NATL, which decreases for tracks occurring solely in the December-January-February
(DJF) period (Fig. S2). Tracks of ETCs that reached a depth of at least 35 hPa in the DJF period show high consistency
in track densities between datasets (Fig. S3), particularly along the east coast of the USA.

The genesis, or initial identification of ETCs centers (Fig. 8e), also shows a maximum over the Mediterranean
and a secondary peak in the southernmost part of the east coast of the USA. A dominant ‘entrance’ for ETCs is
observed along 25°N over the western Atlantic and the Gulf of Mexico, indicating the tropical nature of some
cases. Continental genesis regions are found near the Alberta Clippers in western Canada and Colorado in the
midwest USA. These regions are underestimated in the WRF simulations compared to ERA5 data (Fig. 8e),
which likely accounts for the higher track density observed in continental areas between 35° and 45°N in
the ERA5 dataset (Fig. 8a). Differences in cyclone genesis density in mountain lee regions are evident and

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

9

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 9  Distribution of the storm track properties from 1985 to 2022. The red lines denote the ERA5 data, and
the blue lines denote the WRF data.

significant, particularly during specific October-November-March-April periods (Fig. S4). However, these dif-
ferences are generally reconciled when only the deeper systems are considered (Fig. S5), leading to more similar
track densities in continental regions across the datasets.

The proximity of the domain boundary to the lee region can significantly impact the accuracy of cyclone
simulations, as edge effects near the boundary may distort the representation of cyclone genesis and intensity.
Cyclones that do not exhibit a well-defined closed isobar can be dificult to detect early using tracking algorithms
based on MSLP. However, this limitation does not preclude the possibility of identifying such systems later
during re-intensification when their features become more distinct and detectable. For example, the density of
cyclonegenesis in the northeastern region near Colorado, extending towards the Great Lakes region—typical
region of the ETC intensification noted by Xiao et al.92—shows higher genesis densities in the WRF model and
comparable peaks in intensity. However, this model does not capture all cyclones that are initially unidentified,
resulting in variations in genesis densities within the core of the storm track.

Figure 9 shows the distributions of several ETC properties for both the ERA5 and ExCyclone-TRAMO data-
sets. We selected and analysed those properties provided in our track repository. The distributions of the lati-
tudinal (Fig. 9a) and longitudinal (Fig. 9b) centre positions confirm those described in track density analysis.
Notably, the WRF model tends to overestimate ETC density in the region between 20°W and 5°W longitude,
south of 35°N latitude (Fig. 9a,b). This overestimation aligns with areas of higher track densities during the
transitional months of October, November, March, and April (Fig. S4). Furthermore, the ET analysis (Fig. S1)
highlights this region (20°W to 5°W) as favorable for ET processes, underscoring its tropical-like characteris-
tics. A reduction in the intensity of the North Atlantic Subtropical High (NASH) is known that is linked to an
increased frequency of tropical cyclones (TCs) in the subtropical North Atlantic, as well as a greater occurrence
of recurving TCs93,94. In the WRF outputs, the duration of the ETCs was accurately captured, as demonstrated
by the lifespan distribution in Fig. 9c. The distribution of the minimum MSLP attained by the ETCs (Fig. 9d)
revealed two peaks in the ERA5 data, which were observed at approximately 970 and 1015 hPa. In contrast, the
ExCyclone-TRAMO dataset revealed recurring cases at approximately 960, 980, and 1010 hPa, where generally
more intense occurrences were associated with lower MSLP (slightly higher densities). This trend may be driven
by the physical parametrizations that favour stronger convective systems. The radius of the ETC remained rel-
atively consistent between the ERA5 and ExCyclone-TRAMO datasets, which is expected given the similarities
in dataset resolutions (Fig. 9e).

Water budget parameters.  We have provided a concise overview of the computed parameters related to
moisture uptake calculated via the Lagrangian approach. We have also included a comparison with WRF-derived
diagnostic variables, such as the mean integrated water vapor column (IWVC) and the vertically integrated mois-
ture flux (VIMF). While these variables alone are not enough to quantify moisture uptake, they help to improve
our understanding of the processes involved in moisture transport.

We revisited the case of EC02902, this time focusing on its peak intensity stage. Figure 10 shows the inte-
grated moisture uptake over the 24 hours preceding the peak intensity. Figure 10a–c correspond to moisture
uptake of those particles within the different target regions that shape the EC, namely, the radius, WCB, and
spiral, respectively. Figure 10d shows the IWVC and VIMF during the same period.

The observed moisture patterns (Fig. 10a–c) closely conform with a northwesterly flux that converges
between 25°N and 40°N, originating from sources such as the Gulf of Mexico and continental North America

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1 0

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 10  Moisture uptake (mm/day) from FLEXPART-WRF, integrated over the 24 hours leading up to the
peak intensity of EC02902 on February 10, 2002 at 1200 UTC, for the following target regions: (a) radius, (b)
WCB, and (c) spiral. The red markers indicate the center of the ETC. Panel (d) shows the integrated water
vapor column (IWVC, kg/m², shaded) and the vertically integrated moisture flux (VIMF, kg/ms, represented by
arrows).

(Fig. 10d). We observed variations in the moisture uptake intensity throughout the target regions on the order
of tens of mm/day. In the radial target area (Fig. 10a), the smallest sources, such as the Gulf of Mexico and the
Florida Strait, exhibited lower contributions, as they are far from this target region. This emphasizes the impor-
tance of the Lagrangian water budget-derived database and subsequent meticulous studies of moisture uptake
of particles in the target regions, as this database can substantially incorporate various dynamic and thermody-
namic components.

Figure 11 shows the integrated moisture uptake for only the radius target area and along the entire path for
two case studies (IDs: 071/2005, 069/2006). The selection was made without any specific focus on the cases in
terms of their impacts or intensity characteristics. The primary interest was that the system had a continuous
track deployed over the North Atlantic to evaluate moisture sources and moisture convergence throughout its
lifecycle. Moisture uptake occurs near the cyclone tracks (Fig. 11a,b), resembling previously identified moisture
sources for ETC radial target regions29,89, which is consistent with a northwesterly moisture flux (Fig. 11c,f).

Some of the water vapour captured in parcels may subsequently precipitate or remain in the atmosphere95.
While moisture uptake cannot be directly equated to the precipitation amount within the target area, we expect
to observe a correlation between moisture uptake from our Lagrangian approach and precipitation. Figure 12
presents a comparison between the 6-hour accumulated precipitation within the target regions and the mois-
ture uptake by particles associated with this precipitation, measured 6 hours prior to reaching the target region.
The total precipitation data were derived from the WRF outputs. Figure 12a displays the correlation for each
ETC case, evaluated over their entire life cycle. Figure 12b,c,d depict the variables comparison maded every
6 hours, with each interval representing the average of all cyclones whose lifetime reaches that time. However,
it is important to note that the number of cases per interval varies (Fig. 12b,c,d dashed black line), as not all
cyclones exhibit the same lifetime. In Fig. 12a, positive correlations are observed between the variables, with
greater variability noted in the WCB target regions. The WCB context complicates moisture source attribution
due to rapid ascent, where precipitation is reflected as variations in specific humidity. The correlation coefficients
(r_Spearman = 0.990, 0.995, and 0.994 for the radius, WCB, and spiral regions, respectively) in Fig. 12b–d indi-
cate statistically significant strong positive relationships (p <0.001) between the variables analyzed at different
time intervals.

To thoroughly validate our ExCyclone-TRAMO dataset, we compared the outputs of the FLEXPART-WRF
model with those of the FLEXPART-ERA5 model. A more detailed analysis can be found in Fernández-Alvarez61.
We conducted an analysis of landfalling events over the Iberian Peninsula (IP), located to the east of the
North Atlantic basin, during the period from 1985 to 2022. For this analysis, we filtered cases from both the
ExCyclone-TRAMO and ERA5 datasets. Figure S6 illustrates the distribution of three key features—radius,
MSLP, and depth—for both datasets, as visualized using box-and-whisker plots. These features were employed
to select cases that met specific criteria: radius and depth values exceeding the 75th percentile (Q75) and MSLP
values above the 25th percentile (Q25). The quantile thresholds were derived from the ERA5 dataset, which
provided extreme Q25 and Q75 values relative to the ExCyclone-TRAMO dataset.

The probability densities of landfall are shown in Fig. 13a for the ERA5 reanalysis dataset and Fig. 13b for
the ExCyclone-TRAMO. The locations of density estimates were consistent, although small discrepancies were
found along the probabilities in the Mediterranean coast and the southern part of the IP. These differences are
to be expected, given that the filtering methodology is primarily based on the physical characteristics of storms

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1 1

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 11  Two case studies of integrated moisture uptake for a radius target region over the entire lifecycle. The
upper row shows case ID 071 of 2005, ranging from March 21 at 0600 UTC to March 27 at 0000 UTC. The
bottom row illustrates case ID 069 of 2006, covering the period from March 20 at 0000 UTC to March 26 at 0600
UTC. In (a,b) is the moisture uptake (mm/day), and red markers represent the ETC pathway. Panels (c,d) show
the IWVC (shaded, in kg/m2) and VIMF (represented by arrows, in kg/ms), respectively. Panels (e,f) show the
VIMF (shaded) and VIMF (arrows) modules, respectively.

Fig. 12  Comparison of 6-hour accumulated WRF precipitation within the target regions and moisture uptake
(from FLEXPART-WRF) by particles associated with this precipitation, measured 6 hours prior to reaching the
target region. (a) Box-whisker plots showing the correlation values of these variables evaluated over the entire
life cycle of the ETCs. Panels (b–d) display the series of moisture uptake (solid blue line) and 6-hour WRF
total precipitation (solid red line) computed for the radius, WCB, and spiral target regions, respectively. The
black dashed line indicates the ETC contribution at each step. The moisture uptake is the grid-level sum of the
resulting parameter field for each target.

within a given area. Consequently, this analysis is particularly sensitive to differences in grid resolution, steering
flow and large-scale atmospheric conditions between the ERA5 and WRF models.

Overall, the locations of the densities were consistent, with a higher maximum observed over the southern

IP in the WRF simulations.

Additionally, Fig. 13c,d show composites of the moisture uptake field for all ETCs centred on the radius target
region derived from the ERA5 reanalysis data and WRF outputs, respectively. This target region is designed to
ensure homogeneity for our comparison, focusing on the radial core of the ETCs and excluding structures that
could introduce significant variations due to large-scale influences such as fronts, thus minimizing variability.

The FLEXPART-WRF model outputs (Fig. 13d) exhibit a more intense pattern than the FLEXPART-ERA5
model outputs (Fig. 13c). There is notable agreement in the extent of the main moisture uptake, which does not
exceed 3,000 km to the western boundary and 2,000 km to the eastern boundary. For the most remote moisture

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1 2

www.nature.com/scientificdatawww.nature.com/scientificdata/Fig. 13  For filtered ETCs that made landfall over the IP: Density probability within each 1° × 1° bin from (a) the
ERA5 dataset and (b) the WRF dataset. Moisture uptake composites derived from (c) FLEXPART-ERA5 and (d)
the FLEXPART-WRF model. In (e), a zoomed-in of the first 3,000 km view of Panel (d). In (f), the module of the
vertically integrated moisture flux (VIMF, kg/ms) is shaded, and its vectorial representation is shown (arrows).
The filtering procedure is detailed in the text.

contribution areas, i.e., beyond 2,000 km, moisture uptake extends towards the west‒northwest, with values
below 3 mm/day. Near the centre, for the FLEXPART-WRF data (Fig. 13d), the pattern is slightly broader, with
maximum values varying between 4 and 8 mm/day, exceding that of the ERA5 data (Fig. 13c) by nearly 4 mm/day.
By zooming into the WRF pattern (Fig. 13e), it is observed that it corresponds reasonably well to the
VIMF field (Fig. 13f), which was composited and averaged as the moisture uptake pattern. The expanded view
(Fig. 13e) reveals that the maximum moisture uptake has a larger longitudinal extension than that of the ERA5
reanalysis data (Fig. 13c). Moreover, a more intense uptake is observed in the northeast quadrant (Fig. 13e),
reaching values between 4 and 5 mm/day.

Usage Notes
At  the  repository  supplementary  website  https://github.com/ECMOISTDATABASE/North-Atlantic-
Extratropical-Cyclones-database, script example_case.py contain functions for reading information from the
track ‘.dat’ files and masking ‘.nc’ files. These scripts allow us to reproduce the figures presented in this paper.

Instruction guide:

1-Clone the Repository: The repository should be cloned to the local machine. In the terminal or command
prompt, the following command should be executed:

git clone https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database.git

2-Access the Example Case Directory: Navigate to the Example_case_029_2002 directory within the cloned
repository.

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

13

www.nature.com/scientificdatawww.nature.com/scientificdata/3-Ensure Python Dependencies: The necessary Python dependencies should be ensured to be installed. If not,
create the Conda environment by executing the following commands:

conda env create -f Ecdatasetenv.yml
conda activate Ecdatasetenv

4-Update the Path in the Example Script: Open the example_case.py script and locate line 176. Update the path
direction to the content of the moisture uptake .zip file according to the local directory structure.

5-Execute the Python Code: Execute the Python code within example_case.py to reproduce the figures.

Loop the Script (Optional): The script can optionally be looped to reproduce the results for the other cases or
types of masks.

Code availability
The ExCyclone-TRAMO dataset is publicly accessible at https://doi.org/10.5281/zenodo.13844378. Example
code to read and process the dataset can be found at https://github.com/ECMOISTDATABASE/North-Atlantic-
Extratropical-Cyclones-database/tree/main/Example_case_029_2002. The ERA5 reanalysis was freely retrieved
from https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset. The WRF and WRF-FLEXPART models
can be downloaded from https://www2.mmm.ucar.edu/wrf/users/download/get_source.html and https://www.
flexpart.eu/wiki/FpRoadmap, respectively. The ELIAS 2.0 version, code to process the input data for the models,
and post-processing scripts are provided via the repository at https://git.scc.kit.edu/nk2448/wcbmetric_v2.git
and archived on Zenodo (https://doi.org/10.5281/zenodo.5154980). The TROVA codes and executable are stored
in the permanent link https://github.com/tramo-ephyslab/TROVA-master. CyTRACK can be found at https://
github.com/apalarcon/CyTRACK.

Received: 12 June 2024; Accepted: 5 November 2024;
Published: 20 November 2024

References
1.  Chang, E. K. M., Lee, S., Swanson, K. L. Storm Track Dynamics. J. Climate. 15, 2163–2183, 10.1175/1520-0442015<02163:STD>2.0.CO;2

(2002).

2. Raible, C. C., Yoshimori, M., Stocker, T. F. & Casty, C. Extreme midlatitude cyclones and their implications for precipitation and
wind speed extremes in simulations of the maunder minimum versus present day conditions. Clim. Dyn. 28, 409–423, https://doi.
org/10.1007/s00382-006-0188-7 (2007).

3. Ulbrich, U., Leckebusch, G. C. & Pinto, J. G. Extra-tropical cyclones in the present and future climate: a review. Theor. Appl. Climatol.

96, 117–131, https://doi.org/10.1007/s00704-008-0083-8 (2009).

4. Schwierz, C. et al. Modelling European winter wind storm losses in current and future climate. Clim. Change 101, 485–514, https://

doi.org/10.1007/s10584-009-9712-1 (2010).

5. Owen, L. E., Catto, J. L., Stephenson, D. B. & Dunstone, N. J. Compound precipitation and wind extremes over Europe and their
relationship to extratropical cyclones. Weather. Clim. Extremes 33, 100342, https://doi.org/10.1016/j.wace.2021.100342 (2021).
6. Catto, J. L., Jakob, C., Berry, G., & Nicholls, N. Relating global precipitation to atmospheric fronts. Geophys. Res. Lett. 39, (2012).
7. Hawcroft, M. K., Shaffrey, L., Hodges, K. & Dacre, H. How much Northern Hemisphere precipitation is associated with extratropical

cyclones? Geophys. Res. Lett. 39, L24809, https://doi.org/10.1029/2012GL053866 (2012).

8. Papritz, L. et al. The role of extratropical cyclones and fronts for Southern Ocean freshwater fluxes. J. Climate 27, 6205–6224, https://

doi.org/10.1175/JCLI-D-13-00409.1 (2014).

9. Martius, O., Pfahl, S. & Chevalier, C. A global quantification of compound precipitation and wind extremes. Geophys. Res. Lett. 43,

7709–7717, https://doi.org/10.1002/2016GL070017 (2016).

 10. Utsumi, N., Kim, H., Kanae, S. & Oki, T. Relative contributions of weather systems to mean and extreme global precipitation. J.

Geophys. Res. Atmos. 122, 152–167, https://doi.org/10.1002/2016JD025222 (2017).

 11. Narita, D., Tol, R. S. & Anthoff, D. Economic costs of extratropical storms under climate change: an application of FUND. J. Environ.

Plann. Manage. 53, 371–384, https://doi.org/10.1080/09640561003613138 (2010).

 12. Roberts, J. F. et al. The XWS open access catalogue of extreme European windstorms from 1979 to 2012. Nat. Hazards Earth Syst. Sci.

14, 2487–2501, https://doi.org/10.5194/nhess-14-2487-2014 (2014).

 13. Volonté, A. et al. Strong surface winds in Storm Eunice. Part 1: storm overview and indications of sting-jet activity from observations

and model data. Weather 79, 40–45, https://doi.org/10.1002/wea.4402 (2024).

 14. Volonté, A., Gray, S. L., Clark, P. A., Martínez-Alvarado, O. & Ackerley, D. Strong surface winds in Storm Eunice. Part 2: airstream

analysis. Weather 79, 54–59, https://doi.org/10.1002/wea.4401 (2024).

 15. André, C., Monfort, D., Bouzit, M. & Vinchon, C. Contribution of insurance data to cost assessment of coastal flood damage to
residential buildings: insights gained from Johanna (2008) and Xynthia (2010) storm events. Nat. Hazards Earth Syst. Sci. 13,
2003–2012, https://doi.org/10.5194/nhess-13-2003-2013 (2013).

 16. Kendon, M. Storms Dudley, Eunice and Franklin, February 2022. Technical report. Met Office. https://www.metoffice.gov.uk/
binaries/content/assets/metofficegovuk/pdf/weather/learn-about/uk-past-events/interesting/2022/2022_02_storms_dudley_
eunice_franklin.pdf (2022).

 17. AON. Weather, climate & catastrophe insight. Available from: https://www.aon.com/weather-climate-catastrophe/index.aspx

[Accessed 15th May 2024].

 18. Steiner, A. et al. Critical weather situations for renewable energies–Part A: Cyclone detection for wind power. Renew. Energy 101,

41–50, https://doi.org/10.1016/j.renene.2016.08.013 (2017).

 19. Perera, A. T. D. et al. Quantifying the impacts of climate change and extreme climate events on energy systems. Nat Energy 5,

150–159, https://doi.org/10.1038/s41560-020-0558-0 (2020).

 20. Van der Wiel, K. et al. The influence of weather regimes on European renewable energy production and demand. Environ. Res. Lett.

14, 094010 (2019).

 21. Rapella, L., Faranda, D., Gaetani, M., Drobinski, P. & Ginesta, M. Climate change on extreme winds already affects off-shore wind

power availability in Europe. Environ. Res. Lett. 18, 034040, https://doi.org/10.1088/1748-9326/acbdb2 (2023).

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1 4

www.nature.com/scientificdatawww.nature.com/scientificdata/ 22.  Gonçalves, A. C., Costoya, X., Nieto, R. & Liberato, M. L. Extreme weather events on energy systems: a comprehensive review on
impacts, mitigation, and adaptation measures. Sustain. Energy Res. 11, 4, https://doi.org/10.1186/s40807-023-00097-6 (2024).
 23.  Bourdin, S., Fromang, S., Dulac, W., Cattiaux, J. & Chauvin, F. Intercomparison of four tropical cyclones detection algorithms on

ERA5. Geosci. Model Dev. 15, 6759–6786, https://doi.org/10.5194/egusphere-2022-179 (2022).

 24.  Neu, U. et al. IMILAST: a community effort to intercompare extratropical cyclone detection and tracking algorithms. Bull. Amer.

Meteor. Soc. 94, 529–547, https://doi.org/10.1175/BAMS-D-11-00154.1 (2013).

 25.  Naud, C. M., Ghosh, P., Martin, J. E., Elsaesser, G. S. & Posselt, D. J. A CloudSat–CALIPSO view of cloud and precipitation in the

occluded quadrants of extratropical cyclones. Q. J. R. Meteorol. Soc. 150, 1336–1356, https://doi.org/10.1002/qj.4648 (2024).

 26.  Jones, E., Parfitt, R. & Wing, A. A. Development of frontal boundaries during the extratropical transition of tropical cyclones. Q. J.

R. Meteorol. Soc. 150, 995–1011, https://doi.org/10.1002/qj.4633 (2024).

 27.  McErlich, C., McDonald, A., Renwick, J. & Schuddeboom, A. An assessment of extratropical cyclone precipitation extremes over the

Southern Hemisphere using ERA5. Geophys. Res. Lett. 50, e2023GL104130, https://doi.org/10.1029/2023GL104130 (2023).

 28.  McErlich, C. et al. Positive correlation between wet-day frequency and intensity linked to universal precipitation drivers. Nat.

Geosci. 16, 410–415, https://doi.org/10.1038/s41561-023-01177-4 (2023).

 29.  Papritz, L., Aemisegger, F. & Wernli, H. Sources and Transport Pathways of Precipitating Waters in Cold-Season Deep North

Atlantic Cyclones. J. Atmos. Sci. 78, 3349–3368, https://doi.org/10.1175/JAS-D-21-0105.1 (2021).

 30.  Houze, R. A. Jr. Cloud Dynamics. 2nd ed. Elsevier/Academic Press, 432 pp (2014).
 31.  Schultz, D. M. A review of cold fronts with prefrontal troughs and wind shifts. Mon. Wea. Rev. 133, 2449–2472, https://doi.

org/10.1175/MWR2987.1 (2005).

 32.  Hoskins, B. J., & N. V. West. Baroclinic waves and frontogenesis. Part II: Uniform potential vorticity jet flows—Cold and warm

fronts. J. Atmos. Sci., 36, 1663–1680, 10.1175/1520-0469(1979)036<1663:BWAFPI>2.0.CO;2 (1979).

 33.  Persson, G., Hare, J. E., Fairall, C. W. & Otto, W. D. Air–sea interaction processes in warm and cold sectors of extratropical cyclonic

storms observed during FASTEX. Q. J. R. Meteorol. Soc. 131, 877–912, https://doi.org/10.1256/qj.03.181 (2005).

 34.  Matejka, T. J., Houze, R. A. Jr & Hobbs, P. V. Microphysics and dynamics of clouds associated with mesoscale rainbands in

extratropical cyclones. Q. J. R. Meteorol. Soc. 106, 29–56 (1980).

 35.  Catto, J. L., Madonna, E., Joos, H., Rudeva, I. & Simmonds, I. Global relationship between fronts and warm conveyor belts and the

impact on extreme precipitation. J. of Climate 28, 8411–8429, https://doi.org/10.1175/JCLI-D-15-0171.1 (2015).

 36.  Pfahl, S. & Wernli, H. Quantifying the relevance of cyclones for precipitation extremes. J. Climate 25, 6770–6780, https://doi.

org/10.1175/JCLI-D-11-00705.1 (2012).

 37.  Carlson,  T.  N.  Airflow  through  midlatitude  cyclones  and  the  comma  cloud  pattern. Mon.  Wea.  Rev.,  108,  1498–1509,

10.1175/1520-0493(1980)108<1498:ATMCAT>2.0.CO;2 (1980).

 38.  Eckhardt, S. et al. A 15-year climatology of warm conveyor belts. J. Climate, 17, 218–237, 10.1175/1520-0442(2004)017

<0218:AYCOWC>2.0.CO;2 (2004).

 39.  Clark, P. A. & Gray, S. L. Sting jets in extratropical cyclones: a review. Q J R Meteorol Soc. 144, 943–969, https://doi.org/10.1002/

qj.3267 (2018).

 40.  Pfahl, S., Madonna, E., Boettcher, M., Joos, H. & Wernli, H. Warm conveyor belts in the ERA-Interim Dataset (1979–2010). Part II:

Moisture origin and relevance for precipitation. J. Climate 27, 27–40, https://doi.org/10.1175/JCLI-D-13-00223.1 (2014).

 41.  Gimeno, L. et al. The residence time of water vapour in the atmosphere. Nat. Rev. Earth Environ. 2, 558–569, https://doi.org/10.1038/

s43017-021-00181-9 (2021).

 42.  Stohl, A., Forster, C., Frank, A., Seibert, P. & Wotawa, G. The Lagrangian particle dispersion model FLEXPART version 6.2. Atmos.

Chem. Phys. 5, 2461–2474 (2005).

 43.  Stohl, C., Stohl, M. & Leonardi, P. M. Digital age| Managing opacity: Information visibility and the paradox of transparency in the

digital age. Int. J. Commun. 10, 15 (2016).

 44.  Pisso, I. et al. The Lagrangian particle dispersion model FLEXPART version 10.4. Geosci. Model Dev. 12, 4955–4997, https://doi.

org/10.5194/gmd-12-4955-2019 (2019).

 45.  Zhang, M. et al. On the moisture transport regimes for extreme precipitation over North China. Atmos. Res. 300, 107254, https://doi.

org/10.1016/j.atmosres.2024.107254 (2024).

 46.  Skamarock, W., et al A Description of the Advanced Research WRF Version 3, Technical Report, 113, https://doi.org/10.5065/

D6DZ069T (2008).

 47.  Brioude, J. et al. The Lagrangian particle dispersion model FLEXPART-WRF version 3.1. Geosci. Model Dev. 6, 1889–1904, https://

doi.org/10.5194/gmd-6-1889-2013 (2013).

 48.  Hersbach, H. et al. The ERA5 global reanalysis. Quarterly J. Royal Meteorol. Soc. 146, 1999–2049. https://doi.org/10.1002/qj.3803
 49.  Fernández-Alvarez, J. C., Vázquez, M., Pérez-Alarcón, A., Nieto, R. & Gimeno, L. Comparison of Moisture Sources and Sinks
Estimated with Different Versions of FLEXPART and FLEXPART-WRF Models Forced with ECMWF Reanalysis Data. J.
Hydrometeor. 24, 221–239, https://doi.org/10.1175/JHM-D-22-0018.1 (2023).

 50.  Hodges, K. I., Lee, R. W. & Bengtsson, L. A comparison of extratropical cyclones in recent reanalyses ERA-Interim, NASA MERRA,

NCEP CFSR, and JRA-25. J. Climate 24, 4888–4906, https://doi.org/10.1175/2011JCLI4097.1 (2011).

 51.  Poan, E. D. et al. Investigating added value of regional climate modeling in North American winter storm track simulations. Clim

Dyn 50, 1799–1818, https://doi.org/10.1007/s00382-017-3723-9 (2018).

 52.  Gramcianinov, C. B. et al. Analysis of Atlantic extratropical storm tracks characteristics in 41 years of ERA5 and CFSR/CFSv2

databases. Ocean Eng. 216, 108111, https://doi.org/10.1016/j.oceaneng.2020.108111 (2020).

 53.  Hong, S. Y. & Lim, J. O. J. The WRF single-moment 6-class microphysics scheme (WSM6). Asia-Pacific J. Atmos. Sci. 42, 129–151

(2006).

 54.  Hong, S. Y. A new stable boundary layer mixing scheme and its impact on the simulated East Asian summer monsoon, Quart. J. Roy.

Meteor. Soc. 136(651), 1481–1496, https://doi.org/10.1002/Qj.665 (2010).

 55.  Jiménez, P. A. et al. A revised scheme for the WRF surface layer formulation. Mon. Weather Rev. 140, 898–918, https://doi.

org/10.1175/MWR-D-11-00056.1 (2012).

 56.  Tewari, M. et al. Implementation and verification of the unified NOAH land surface model in the WRF model (Formerly Paper
Number 17.5). In Proceedings of the 20th conference on weather analysis and forecasting/16th conference on numerical weather
prediction, Seattle, WA, USA (Vol. 14, 2004, January). https://ams.confex.com/ams/84Annual/techprogram/paper_69061.htm.
 57.  Iacono, M. J. et al. Radiative forcing by long-lived greenhouse gases: Calculations with the AER radiative transfer models. J. Geophys.

Res. 113, D13103, https://doi.org/10.1029/2008JD009944 (2008).

 58.  Kain, J. S. The Kain–Fritsch convective parameterization: an update. J. Appl. Meteorol. 43, 170–181, 10.11751520-0450(2004)043

<0170:TKCPAU>2.0.CO;2 (2004).

 59.  Miguez-Macho, G., Stenchikov, G. L. & Robock, A. Spectral nudging to eliminate the effects of domain position and geometry in

regional climate model simulations. J. Geophys. Res. 109, D13104, https://doi.org/10.1029/2003JD004495 (2004).

 60.  Fernández-Alvarez, J. C. et al. Projected changes in atmospheric moisture transport contributions associated with climate warming

in the North Atlantic. Nat Commun. 14, 6476, https://doi.org/10.1038/s41467-023-41915-1 (2023).

 61.  Fernández-Alvarez, J. C. et al. Changes in moisture sources of atmospheric rivers landfalling the Iberian Peninsula with WRF-

FLEXPART. J. Geophys. Res. Atmos. 128, e2022JD037612, https://doi.org/10.1029/2022JD037612 (2023).

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1 5

www.nature.com/scientificdatawww.nature.com/scientificdata/ 62.  Insua-Costa, D. & Miguez-Macho, G. A new moisture tagging capability in the Weather Research and Forecasting model:
Formulation, validation and application to the 2014 Great Lake-effect snowstorm. Earth Syst. Dyn. 9, 167–185, https://doi.
org/10.5194/esd-9-167-2018 (2018).

 63.  Insua-Costa, D., Miguez-Macho, G. & Llasat, M. C. Local and remote moisture sources for extreme precipitation: A study of the two
catastrophic 1982 western Mediterranean episodes. Nat. Hazards Earth Syst. Sci. 23, 3885–3900, https://doi.org/10.5194/hess-23-
3885-2019 (2019).

 64.  Hanna, S. R. Concentration fluctuations in a smoke plume. Atmos. Environ. (1967) 18, 1091–1106, https://doi.org/10.1016/0004-

6981(84)90141-0 (1984).

 65.  Schultz, D. M. et al. Extratropical cyclones: A century of research on meteorology’s centerpiece. Meteorological monographs 59, 16–1,

https://doi.org/10.1175/AMSMONOGRAPHS-D-18-0015.1 (2019).

 66.  Flaounas, E. et al. A composite approach to produce reference datasets for extratropical cyclone tracks: application to Mediterranean

cyclones. Weather Clim. Dynam. 4, 639–661, https://doi.org/10.5194/wcd-4-639-2023 (2023).

 67.  Bacmeister, J. T. et al. Exploratory high-resolution climate simulations using the Community Atmosphere Model (CAM). J. Climate

27, 3073–3099, https://doi.org/10.1175/JCLI-D-13-00387.1 (2014).

 68.  Blender, R., Fraedrich, K. & Lunkeit, F. Identification of cyclone‐track regimes in the North Atlantic. Quarterly J. Royal Meteorol. Soc.

123, 727–741, https://doi.org/10.1002/qj.49712353910 (1997).

 69.  Raible, C. C., Della-Marta, P. M., Schwierz, C., Wernli, H. & Blender, R. Northern Hemisphere extratropical cyclones: A comparison
of detection and tracking methods and different reanalyses. Mon. Wea. Rev. 136, 880–897, https://doi.org/10.1175/2007MWR2143.1
(2008).

 70.  Wernli, H. & Schwierz, C. Surface cyclones in the ERA-40 dataset (1958–2001). Part I: Novel identification method and global

climatology. J. Atmos. Sci. 63, 2486–2507, https://doi.org/10.1175/JAS3766.1 (2006).

 71.  Pérez-Alarcón, A., Coll-Hidalgo, P., Trigo, R. M., Nieto, R. & Gimeno, L. CyTRACK: An open-source and user-friendly python

toolbox for detecting and tracking cyclones. Environ. Model. Softw. 176, 106027 (2024).

 72.  Evans, J. L., & Hart, R. E. Objective indicators of the life cycle evolution of extratropical transition for Atlantic tropical cyclones.

Monthly Weather Review, 131, 909-925, 10.1175/1520-0493(2003)131<0909:OIOTLC>2.0.CO;2 (2003).

 73.  Hart, R. E.  A  cyclone  phase  space derived from  thermal wind and thermal asymmetry. Mon.  Wea.  Rev.  131, 585–616,

10.1175/1520-0493(2003)131<0585:ACPSDF>2.0.CO;2 (2003).

 74.  Madonna, E., Wernli, H., Joos, H., Martius, O. Warm conveyor belts in the ERA-Interim Dataset (1979–2010). Part I: Climatology

and potential vorticity evolution. J. Climate 27, 3–26, https://doi.org/10.1175/JCLI-D-12-00720.1 (2014).

 75.  Sprenger, N., Lee, L. Y., De Castro, C. A., Steenhout, P. & Thakkar, S. K. Longitudinal change of selected human milk oligosaccharides
and association to infants’ growth, an observatory, single centre, longitudinal cohort study. PloS one 12, e0171814, https://doi.
org/10.1371/journal.pone.0171814 (2017).

 76.  Quinting, J. F. & Grams, C. M. Toward a Systematic Evaluation of Warm Conveyor Belts in Numerical Weather Prediction and
Climate Models. Part I: Predictor Selection and Logistic Regression Model. J. Atmos. Sci. 78, 1465–1485, https://doi.org/10.1175/
JAS-D-20-0139.1 (2021).

 77.  Wandel, J., Quinting, J. F. & Grams, C. M. Toward a Systematic Evaluation of Warm Conveyor Belts in Numerical Weather Prediction
and Climate Models. Part II: Verification of Operational Reforecasts. J. Atmos. Sci. 78, 3965–3982, https://doi.org/10.1175/
JAS-D-20-0385.1 (2021).

 78.  Ronneberger, O., Fischer, P., & Brox, T. U-net: Convolutional networks for biomedical image segmentation. In Medical image
computing and computer-assisted intervention–MICCAI 2015: 18th international conference, Munich, Germany, October 5-9, 2015,
proceedings, part III 18, 234-241, Springer International Publishing. https://doi.org/10.1007/978-3-319-24574-4_28 (2015).

 79.  Quinting, J. F. & Grams, C. M. EuLerian Identification of ascending AirStreams (ELIAS 2.0) in numerical weather prediction and
climate models – Part 1: Development of deep learning model. Geosci. Model Dev. 15, 715–730, https://doi.org/10.5194/gmd-15-
715-2022 (2022).

 80.  Rudeva, I. & Gulev, S. K. Climatology of cyclone size characteristics and their changes during the cyclone life cycle. Mon. Wea. Rev.

135, 2568–2587, https://doi.org/10.1175/MWR3420.1 (2007).

 81.  Quinting, J. F., Grams, C. M., Oertel, A. & Pickl, M. EuLerian Identification of ascending AirStreams (ELIAS 2.0) in numerical
weather prediction and climate models – Part 2: Model application to different datasets. Geosci. Model Dev. 15, 731–744, https://doi.
org/10.5194/gmd-15-731-2022 (2022).

 82.  Gautschi, W. The spiral of Theodorus, numerical analysis, and special functions. J. Comput. Appl. Math. 235, 1042–1052, https://doi.org/10.1016/j.

cam.2009.11.054 (2010).

 83.  Sodemann, H., Schwierz, C. & Wernli, H. Interannual variability of Greenland winter precipitation sources: Lagrangian moisture
diagnostic and North Atlantic Oscillation influence. J. Geophysical Res.: Atmospheres 113, D03107, https://doi.org/10.1029/
2007JD008503 (2008).

 84.  Fernández-Alvarez, J. C., Pérez-Alarcón, A., Nieto, R. & Gimeno, L. TROVA: TRansport of water VApor. SoftwareX. 20, 101228,

https://doi.org/10.1016/j.softx.2022.101228 (2022).

 85.  Stohl, A., James, P. A. Lagrangian analysis of the atmospheric branch of the global water cycle. Part I: Method description, validation, and
demonstration  for  the  August  2002  flooding  in  central  Europe.  J.  Hydrometeor.  5,  656–678,  10.1175/1525-7541(2004)005
<0656:ALAOTA>2.0.CO;2 (2004).

 86.  Läderach, A. & Sodemann, H. A revised picture of the atmospheric moisture residence time. Geophys. Res. Lett. 43, 924–933, https://

doi.org/10.1002/2015GL067449 (2016).

 87.  Numaguti, A. Origin and recycling processes of precipitating water over the Eurasian continent: Experiments using an atmospheric

general circulation model. J. Geophys. Res. 104, 1957–1972, https://doi.org/10.1029/1998JD200026 (1999).

 88.  van der Ent, R. J. & Tuinenburg, O. A. The residence time of water in the atmosphere revisited. Hydrol. Earth Syst. Sci. 21, 779–790,

https://doi.org/10.5194/hess-21-779-2017 (2017).

 89.  Coll-Hidalgo, P. et al. Assessing target areas for precipitating moisture source analysis of extratropical cyclones: An analysis based

on case studies. Atmos. Res. 310, 107628, https://doi.org/10.1016/j.atmosres.2024.107628 (2024).

 90.  Baker, A. J. et al. Seasonality of westerly moisture transport in the East Asian summer monsoon and its implications for interpreting

precipitation δ18O. J. Geophys. Res. Atmos. 120, 5850–5862, https://doi.org/10.1002/2014JD022919 (2015).

 91.  Coll-Hidalgo, P., Gimeno-Sotelo, L., Nieto, R., Fernández-Alvarez, J. C. & Gimeno, L. North Atlantic Extratropical Cyclone Tracks

and Lagrangian-Derived Moisture Uptake Dataset I. Zenodo https://doi.org/10.5281/zenodo.13844378 (2024).

 92.  Xiao, C., Lofgren, B. M. & Wang, J. WRF-based assessment of the Great Lakes’ impact on cold season synoptic cyclones. Atmos. Res.

214, 189–203, https://doi.org/10.1016/j.atmosres.2018.07.020 (2018).

 93.  Sainsbury, E. M. et al. What Governs the Interannual Variability of Recurving North Atlantic Tropical Cyclones? J. Climate 35,

3627–364, https://doi.org/10.1175/JCLI-D-21-0712.1 (2022).

 94.  Kossin, J. P., Camargo, S. J. & Sitkowsk, M. Climate modulation of North Atlantic hurricane tracks. J. Climate 23, 3057–3076, https://

doi.org/10.1175/2010JCLI3497.1 (2010).

 95.  Cohen, C. & McCaul, E. W. Further results on the sensitivity of simulated storm precipitation efficiency to environmental

temperature. Mon. Wea. Rev. 135, 1671–1684, https://doi.org/10.1175/MWR3380.1 (2007).

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

1 6

www.nature.com/scientificdatawww.nature.com/scientificdata/acknowledgements
P.C.-H. acknowledge the support from the Xunta de Galicia (Galician Regional Government), the «Programa de
axudas á etapa pre doutoral da Xunta de Galicia (Consellería de Cultura, Educación, Formación Profesional e
Universidades)» under contract ED481A-2022/128. L.G.-S. was supported by a ‘Ministerio de Ciencia, Innovación
y Universidades’ PhD grant (reference: PRE2022-101497). J.C.F.-A. thanks the support from the Xunta de
Galicia (Axencia Galega de Innovación) under the Postdoctoral grant IN606B2024/016. EPhysLab members are
supported by the SETESTRELO project (grant no. PID2021-122314OB-I00) funded by the Ministerio de Ciencia,
Innovación y Universidades, Spain (MICIU/AEI/10.13039/501100011033), Xunta de Galicia under the Project
ED431C2021/44 (Programa de Consolidación e Estructuración de Unidades de Investigación Competitivas
(Grupos de Referencia Competitiva) and Consellería de Cultura, Educación e Universidade), and by the
European Union “ERDF A way of making Europe”, “NextGenerationEU”/PRTR. This work has also been possible
thanks to the computing resources and technical support provided by CESGA (Centro de Supercomputación de
Galicia) and RES (Red Española de Supercomputación).

author contributions
P. Coll-Hidalgo: Conceptualization, Methodology, Investigation, Software, Visualization, Writing—original
draft. L. Gimeno-Sotelo: Software, Methodology, Writing—review and editing. J.C. Fernández-Alvarez: Software,
Methodology. R. Nieto, and L. Gimeno: Conceptualization, Methodology, Supervision, Writing—review and
editing, Funding Acquisition.

Competing interests
The authors declare no competing interests.

additional information
Supplementary information The online version contains supplementary material available at https://doi.org/
10.1038/s41597-024-04091-5.

Correspondence and requests for materials should be addressed to P.C.-H.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribu-
tion and reproduction in any medium or format, as long as you give appropriate credit to the original author(s)
and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed mate-
rial. You do not have permission under this licence to share adapted material derived from this article or parts of
it. The images or other third party material in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2024, modified publication 2026

Scientific Data | (2024) 11:1258 | https://doi.org/10.1038/s41597-024-04091-5

17

www.nature.com/scientificdatawww.nature.com/scientificdata/
