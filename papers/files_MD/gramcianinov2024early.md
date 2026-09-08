International Journal of Climatology

RESEARCH ARTICLE

Early- Stage Extratropical Cyclones' Mechanisms Over
South America: RCM Added Value and Future Changes in a
Warmer Planet
Carolina B. Gramcianinov1,2
Natalia Castillo4,6

  |  Andressa A. Cardoso2,3

  |  Rosmeri P. da Rocha2

  |  Natália P. da Silva2

  |  Rosa Luna- Niño4,5

  |  Tereza Cavazos4

  |

1Institute for Coastal Systems Analysis and Modeling, Helmholtz- Zentrum Hereon, Geesthacht, Germany  |  2Departamento de Ciências Atmosféricas,
Instituto de Astronomia, Geofísica e Ciências Atmosféricas, Universidade de São Paulo, São Paulo, São Paulo, Brazil  |  3Earth System Physics, The Abdus
Salam International Centre for Theoretical Physics (ICTP), Trieste, Italy  |  4Centro de Investigación Científica y de Educación Superior de Ensenada,
Carretera Ensenada- Tijuana # 3918, Ensenada, Baja California, Mexico  |  5Center for Western Weather and Water Extremes (CW3E), Scripps Institution
of Oceanography, University of California, California, USA  |  6Department of Science Technology and Society, Scuola Universitaria Superiore IUSS,
Pavia, Italy

Correspondence: Carolina B. Gramcianinov (carolina.gramcianinov@hereon.de)

Received: 29 February 2024  |  Revised: 10 September 2024  |  Accepted: 28 October 2024

Funding: R.P.R. acknowledges the CNPq (grant nos. 430314/2018-3; 304949/2018-3) and FAPESP (grant no. 2022/05476-2).

Keywords: climate change | CMIP5 | CORDEX- CORE | cyclogenesis | extratropical cyclones | South Atlantic Ocean

ABSTRACT
Regional  climate  models  (RCMs)  from  the  CORDEX  enable  further  investigations  of  the  regional  aspects  of  climate  change
impacts in South America. Here, we assess the CORDEX- RCMs' present and future projections of extratropical cyclones, focus-
ing on their frequency, early- stage synoptic features, and added value relative to the global climate models (GCMs). Cyclones
were tracked using a common algorithm in the present (1985–2005) and future RCP8.5 scenarios (2080–2099). ERA5 reanaly-
sis was used as reference data in the present climate. Both GCMs and RCMs can identify the three major cyclone hot spots in
South America: Argentina (ARG), La Plata Basin (LPB), and the south- southeast Brazilian coast (SBR). RCMs improve GCMs'
representation of the cyclogenesis frequency, adding value by decreasing the biases (~10%). Early- stage cyclone synoptic struc-
ture also indicates RCMs' improvement of the low- level fields by presenting mesoscale structures of warm/cold advection and
moisture flux convergence/divergence in greater agreement with ERA5 (except for moisture flux divergence  for LPB). RCMs
and GCMs project a general decrease in cyclogenesis for the end of the century. For the cyclogenesis cores, GCMs' and RCMs'
projections agree on the trend signals in SBR, LPB, and ARG in austral winter and disagree in ARG in austral summer. For LPB
and SBR cyclogenesis, the RCMs and GCMs suggest a future increase in moisture flux convergence and warm advection at low
levels, while a decrease in upper level divergence is projected. This indicates a reinforcement of cyclogenesis (negative sea- level
pressure trend) in the future due to the low- level features and associated diabatic processes. For ARG, the future trends in the
mean  structure  of  cyclogenesis  are  relatively  weak.  Following  other  studies,  cyclogenesis  frequency  may  decrease;  however,
changes could occur in some important physical processes, such as low- level moisture flux convergence and warm advection,
suggesting more intense events in the future.

© 2024 Royal Meteorological Society

International Journal of Climatology, 2024; 0:1–19
https://doi.org/10.1002/joc.8683

1 of 19

1   |   Introduction

Extratropical  cyclones  (hereafter,  cyclones)  are  the  main  driv-
ers  of  weather  and  climate  variability  at  the  middle  and  high
latitudes, featuring in most extreme events over these locations
(e.g.,  Gramcianinov  et  al.  2023).  Assessing  possible  changes
in  cyclone  intensity  and  distribution  due  to  climate  change
has  been  of  utmost  importance  in  the  last  decades,  crucial  to
socio- economic  management  and  mitigation  plans  to  support
decision- makers worldwide. In South America, it should not be
different:  with  three  active  cyclogenesis  regions  (e.g.,  Reboita
et  al.  2010),  this  continent  suffers  from  even  small  changes  in
cyclone  behaviour.  From  severe  events  associated  with  strong
rainfall,  wind  storms,  high  sea  waves  and  storm  surges  along
the coast to dry periods due to the lack of them, cyclones are one
of the most important atmospheric systems influencing most of
the South America (SAM) continent.

Globally, several studies have reported a decrease in the number
of cyclones (e.g., Fyfe 2003; Geng and Sugi 2003; Catto et al. 2019),
although there is still a large uncertainty, and this behaviour can
vary regionally (Krüger et al. 2012). Geng and Sugi (2003) found
a poleward shift in the storm track, followed by a reduction in the
number  of  cyclones.  According  to  these  authors,  the  displace-
ment of the storm track to higher latitudes makes the decrease
of cyclones in mid- latitudes even more prominent. Using reanal-
ysis, Pezza and Ambrizzi (2003) also found evidence of a similar
shift pattern but with no significant trend regarding the number
of cyclones. Several authors reported the poleward shift of the
storm track, both considering global (e.g., Geng and Sugi 2003;
Bengtsson, Hodges, and Roeckner 2006; Bengtsson, Hodges, and
Keenlyside  2009; Tamarin  and  Kaspi  2017),  hemispheric  (Fyfe
2003; Grieger et al. 2014) and regional approaches (Krüger et al.
2012; Reboita et al. 2018, 2021; de Jesus et al. 2021). However,
dynamical downscaling studies have shown some complex be-
haviour of the cyclones over SAM (Reboita et al. 2018, 2021; de
Jesus et al. 2021). For instance, Reboita et al. (2021) showed that
cyclogenesis around 30° S–35° S may rise in future projections,
increasing the precipitation and winds over the central portion
of SAM.

Therefore, regional climate models (RCMs) are an important
resource  for  assessing  future  cyclone  changes,  especially  in
SAM, where cyclone development is deeply related to regional
features.  SAM  has  three  preference  regions  for  cyclogenesis:
Argentina  (ARG,  ~45° S),  La  Plata  Basin  (LPB,  ~35° S),  and
south- southeast  Brazilian  coast  (SBR,  ~30° S)  (e.g.,  Hoskins
and  Hodges  2005;  Reboita  et  al.  2010).  Analysing  these  re-
gions, Gramcianinov, Hodges, and Camargo (2019) found that
cyclogenesis  northward  of  35° S  is  strongly  associated  with
low- level thermodynamic processes in the austral summer and
upper level forcing in winter due to a strong baroclinic envi-
ronment. On the other hand, cyclone development southward
of 35° S is related to a high baroclinic environment throughout
the year with less influence of moist processes (Gramcianinov,
Hodges, and Camargo 2019; Crespo et al. 2020). The benefits
of using RCMs to represent regional processes are widely re-
ported.  In  particular,  the  cyclone  representation  over  SAM
has  improved  compared  with  coarser  resolution  global  cli-
mate  models  (GCMs),  such  as  the  ones  from  CMIP5  (e.g.,
Reboita et  al.  2010, 2018; de Jesus et  al.  2021, 2022). Most of

these  dynamical  modelling  studies  result  from  the  efforts  of
the  Coordinated  Regional  Climate  Downscaling  Experiment
(CORDEX) as part of the World Climate Research Programme
(WCRP), as described by Gutowski Jr. et al. (2016).

RCMs often simulate smaller scale processes that coarser resolu-
tion GCMs cannot resolve. Therefore, one of the key issues when
using downscaling for climate analysis is to infer if the RCM im-
proved or added value to a particular climate statistic compared
with its forcing GCM. Testing the skill of RCMs in comparison with
GCMs is the main goal of an added- value application (IPCC 2013).
The assessment of RCMs simulations depends on several factors,
such as the study area, models analysed, spatiotemporal scale, ex-
periment configuration and retrieved variables (Kumar and Dimri
2021;  Falco  et  al.  2018,  2019).  However,  the  RCMs  are  expected
to  improve  the  mesoscale  features,  especially  over  regions  with
complex topography and during extreme events (Di Luca, de Elía,
and Laprise 2012). Another important issue is whether RCMs can
improve the representation of the climate variability of large- scale
phenomena. While long- term variability can be well represented
by RCMs (Di Luca, de Elía, and Laprise 2012), some studies sug-
gest  that  some  objective  performance  index  can  degrade  large-
scale  representation  for  features  with  short- term  time  scales
(Castro,  Pielke  Sr.,  and  Leoncini  2005;  Sanchez- Gomez,  Somot,
and Déqué 2009; Di Luca, de Elía, and Laprise 2012).

Over  SAM,  it  is  known  that  regional  features  are  not  well  re-
solved  by  GCMs  (Zazulie,  Rusticucci,  and  Raga  2018),  while
some  improvement  was  shown  by  downscaling  with  RCMs
(Carril  et  al.  2012;  Solman  and  Blázquez  2019).  In  these  stud-
ies, the authors found that some enhancement can be expected
from  a  downscaling  procedure  representing  precipitation  and
near- surface  temperature.  However,  the  performance  indices
vastly varied within the chosen ensemble. Nevertheless, there is
no consensus on how well RCMs improve atmospheric features
over SAM, especially considering the lack of studies focusing on
fields directly associated with cyclones.

Even  though  many  works  report  future  changes  in  the  cyclo-
genesis  in  SAM  (e.g.,  Reboita  et  al.  2018;  de  Jesus  et  al.  2022),
there  are  still  some  uncertainties,  specifically  regarding  the
main drivers. Important mechanisms to the cyclogenesis phases,
such  as  moisture  flux,  temperature  advection,  and  upper  level
forcing, are being modified by climate change (Reboita, Crespo
et al. 2021), which can lead to changes in airflow within the cy-
clone and, therefore, justify the changes in genesis distribution
reported in SAM. In this study, we aimed to investigate the possi-
ble changes in the early- stage cyclone structure over SAM due to
climate change. This cyclone's initial phase is especially relevant
in SAM as it occurs close to the coast, severely affecting human
activities.  Considering  our  goal  and  that  RCMs  have  proven  to
be essential to cyclone studies in SAM, we established two main
scientific questions to guide this study:

•  What is the performance of the RCM compared with its forc-

ing GCM regarding cyclone development in SAM?

•  What  are  the  changes  in  the  early- stage  structure  of
the  cyclones  towards  the  end  of  the  century  under  the
(RCP8.5)
Representative  Concentration  Pathway  8.5
scenario?

2 of 19

International Journal of Climatology, 2024

The  document  follows  with  Section  2,  where  we  describe  the
RCMs and GCMs used in the analysis and the reanalysis used as
reference. Also, in Section 2, the cyclone identification process
and tracking are described together with the diagnostics used
to obtain the cyclones' distribution, intensity, and structure. In
Section 3, the results are presented, followed by the discussion
in Section 4. Finally, the conclusion and final comments can be
found in Section 5.

2   |   Data and Methods

2.1   |   Reanalysis and Models

ERA5 is the fifth generation of reanalysis from the European
Centre  for  Medium- Range  Weather  Forecast  (ECMWF;
Hersbach et al. 2020), produced with the ECMWF's Integrated
Forecast  System  (IFS),  version  CY41R2,  using  4D- Var  data
assimilation.  ERA5  benefits  from  the  new  developments  in
model physics, dynamic core and data assimilation techniques,
overcoming  the  performance  of  its  predecessor,  the  ERA-
Interim.  The  ERA5  atmospheric  variables  used  in  this  work
are  on  0.25°  horizontal  grids  every  6 h.  In  the  present  study,
ERA5 provides the reference for the model evaluation in the
present climate (PC), considering that due to the high perfor-
mance and advanced data assimilation, it relies closely on the
observations (Belmonte Rivas and Stoffelen 2019). Regarding
cyclone's  climatology,  ERA5  determines  cyclone  structure
well across the cyclone lifecycle (McErlich et al. 2023) and can
represent the three main genesis regions in the SAM and the
basic  storm- track  characteristics  (Gramcianinov  et  al. 2020).
Despite that, it is important to note that ERA5 is a modelling
product and presents biases compared with observations, par-
ticularly  for  water- related  variables,  that  play  an  important
role in cyclone intensification mechanisms (Naud et al. 2020;
McErlich et al. 2023).

The  downscaling  simulations  used  in  this  work  were  ob-
tained through the RegCM4.7 as part of the CORDEX- CORE
programme (Gutowski Jr. et al. 2016; Giorgi et al. 2022). This
version of RegCM4 solves the atmospheric dynamic equations
in  the  hydrostatic  configuration  in  sigma- vertical  coordinate
levels  (Giorgi  et  al.  2012).  The  RegCM4.7  simulations  were
nested  independently  in  two  GCMs  of  the  Coupled  Model
Intercomparison Project Phase 5 (CMIP5; Taylor, Stouffer, and
Meehl  2012):  HadGEM- ES2  (hereafter,  just  called  HadGEM;

TABLE 1    |    Datasets used in the present study.

Martin  et  al.  2011)  and  MPI- ESM- MR  (MPI;  Giorgetta
et al. 2013). These driver GCMs were also evaluated, allowing
a coherent analysis of the improvement with their respective
downscaling.  From  the  available  experiments  in  the  CMIP5
and CORDEX- CORE, we used the historical (1950–2005) and
future  (2006–2100)  period  under  the  RCP8.5,  which  is  the
most extreme emission scenario under global warming (Riahi
et al. 2011). Two time slices were also used to compare the end
of each period, defined here as PC from 1985 to 2005 and far
future (FF) from 2080 to 2099. Table 1 details the periods and
simulations, including information on the resolution and insti-
tutions involved.

The CORDEX and CMIP5 data were obtained through the nodes
maintained by the Earth System Grid Federation (ESGF), while
the ERA5 was obtained through the Copernicus Climate Change
Service (CS3, 2017). The variables used are the mean sea level
pressure (MSLP), temperature at 850 hPa, wind components at
850  and  200 hPa,  geopotential  at  500 hPa  and  specific  humid-
ity at 850 hPa. The geopotential height and specific humidity at
these levels were not available for the GCMs in the CMIP5 data
portal, so they were interpolated from the GCM native vertical
levels (hybrid in the HadGEM and sigma in the MPI) to isobaric
levels using the hypsometric equation. The same was applied to
the wind at 200 hPa of the MPI experiment. Furthermore, with
these  basic  variables,  we  computed  the  divergence  at  200 hPa,
temperature advection at 850 hPa, and moisture flux and mois-
ture flux divergence at 850 hPa.

2.2   |   Cyclone Tracking

The  cyclonic  features  are  identified  and  tracked  using  the
TRACK algorithm (Hodges 1994, 1995, 1999), which considers
the  relative  vorticity  from  the  winds  at  850 hPa.  However,  the
vorticity field is noisy, and its magnitude is strictly related to the
resolution of the source data, demanding a pre- processing step.
Following the method developed by Hoskins and Hodges (2002),
a  spectral  filter  was  used  to  remove  small  and  large- scale  pat-
terns  from  the  relative  vorticity  field.  Originally,  the  method
retains  features  with  the  wavenumber  between  5  and  42  con-
sidering  a  global  grid;  thus,  some  adaptations  were  made  to
apply  the  filter  in  a  limited  area.  The  spectral  filter  was  built
through the Fast Fourier transform using the equivalent spatial
distance of the zonal wavenumbers, calculated by the equation
L = 2𝜋Rcos𝜑 ∕ k  (where  R  is  the  Earth  radius, 𝜑  is  the  latitude

Name

ERA5

HadGEM- ES2

MPI- ESM- MR

RegHad

RegMPI

Institution

Resolution

Periods

RCM

Driver GCM

ECMWFa

MOHCb

MPIc

ICTPd

ICTPd

0.25° × 0.25°

1985–2005

—

1.875° × 1.25°

1985–2005

2080–2099

1.875 × 1.875°

1985–2005

2080–2099

—

—

—

—

—

—

0.22° × 0.22°

1985–2005

2080–2099

RegCM4.7

HadGEM2- ES

0.22° × 0.22°

1985–2005

2080–2099

RegCM4.7

MPI- ESM- MR

aEuropean Centre for Medium- Range Weather Forecasts.
bMet Office Hadley Centre, UK.
cMax Planck Institute, Germany.
dAbdus Salam International Centre for Theoretical Physics, Italy.

3 of 19

and k is the wavenumber). Therefore, we retained scales between
8000 and 950 km in the vorticity field. To maintain the consis-
tency between reanalysis, RCMs and GCMs, 850 hPa wind fields
were  passed  through  bilinear  interpolation  to  a  regular  0.25°
grid  before  the  vorticity  computation,  following  ERA5  resolu-
tion. The filtering and tracking were done to the same area for
all models (91° W—27° W; 55° S—0°) to avoid disparities due to
method differences.

The TRACK scheme identifies cyclonic features by image seg-
mentation, using the relative vorticity threshold of −1 × 10−5 s−1
to  find  first  the  minimum  regions  (objects)  and  then  the  cen-
tre  of  minima  (features),  which  are  refined  to  consider  lo-
cation  off- grid.  After  the  identification  step,  the  tracking  is
performed  in  two  phases:  at  first,  the  features  are  connected
by the nearest neighbour search; secondly, the track is refined
and  smoothed  through  a  cost  function  considering  adaptive
constraints  (Hodges  1999).  These  constraints  are  essential  in
the tracking process since they avoid ambiguous and spurious
tracks,  bounding  the  cyclone's  displacement  speed  and  direc-
tion in certain regions and conditions. Gramcianinov, Hodges,
and  Camargo  (2019)  defined  specific  parameter  values  for  the
tracking  in  SAM  to  avoid  most  of  the  spurious  connection  of
orographic  and  thermal  lows  to  early- stage  cyclones,  which
were  used  in  the  present  work  (see  Table  1  in  Gramcianinov,
Hodges, and Camargo 2019). Moreover, only cyclones that live
more than 24 h and move further than 500 km were considered
for the current analysis.

Despite  the  constraints  and  filters  described  above,  the  track-
ing method is still sensitive to the data source and method. The
tracking algorithm is biased regarding the cyclone position, par-
ticularly the initial stages (Neu et al. 2013; Roebber, Grise, and
Gyakum  2023).  Nevertheless,  tracking  tools  have  been  widely
used to compare datasets objectively and enable the analysis of
cyclones and storm tracks on large amounts of data produced by
reanalysis and models.

2.3   |   Cyclone Statistics and Intensity Diagnostic

Spatial  statistics  of  cyclogenesis  distribution  were  computed
using  the  spherical  kernel  estimator  approach  (Hodges  1996).
The density is computed as a probability density function (PDF)
directly on the sphere using spherical nonparametric estimators
with local kernel functions, which makes the estimation much
more suitable for large datasets. More details about the method
can be found in Hodges (1996).

Other  fields  are  incorporated  into  the  tracks  for  the  intensity
analysis.  Besides  the  minimum  relative  vorticity  used  by  the
tracking,  the  maximum  wind  speed  and  the  minimum  MSLP
associated with the cyclone centre are used. They are obtained
by searching for the maximum and minimum values within 6°
and  5°  radius  of  the  cyclone's  centre  (Bengtsson,  Hodges,  and
Keenlyside  2009).  With  this  information,  the  density  distribu-
tions of maximum 10- m height wind intensity were calculated.
All the analyses are done for the austral summer (December to
February, DJF) and winter (June to August, JJA).

2.4   |   Composites

Composites were made for each preferred genesis region defined
according  to  the  density  distribution  to  understand  the  cyclone
structure. Centred composite better suits the purpose of analys-
ing  the  cyclone  structure  by  enhancing  the  air- flows  and  fea-
tures within the cyclone influence ratio (e.g., Catto, Shaffrey, and
Hodges 2010; Hodges, Lee, and Bengtsson 2011; Gozzo et al. 2014;
Gramcianinov, Hodges, and Camargo 2019). The composites were
made using a box (40° latitude and 40° longitude) centred at each
cyclone's centre to sample all variables. At first, all datasets were
interpolated to the same horizontal regular grid with 0.5° latitude
and 0.5° longitude. Then, the sampling was conducted using the
centred  box  to  build  up  the  composite  using  the  average  of  the
samples. Although the sampling was done at the time of the gen-
esis (0 h) and 12 h later (+12 h), only the latter is shown. At +12 h,
the cyclone acting mechanisms are still the same as those related
to the time of genesis but enhanced. In this way, we considered
this  time  step  part  of  the  genesis  stage  as  it  presents  the  mech-
anisms for establishing the extratropical cyclone. Some previous
works also define cyclogenesis as a developing stage rather than
only the first time step detected by the algorithm (e.g., Dacre and
Gray 2009; Grise, Son, and Gyakum 2013).

Only  cyclones  with  central  vorticity  below  the  25th  percentile
were  used  to  build  the  composites.  The  percentile  was  com-
puted using the systems' filtered relative vorticity at 850 hPa (see
Section  2.2)  at  the  time  step  of  the  composite  sampling,  thus,
12 h after the genesis. The selection of the strong cyclones allows
a clearer visualisation of the pattern since genesis mechanisms
are enhanced. The intensity threshold was chosen based on the
distribution of the minimum filtered vorticity at the centre of the
cyclone. Using the 25th percentile for the central vorticity allows
the  selection  of  intense  systems,  keeping  enough  samples  to  a
statistically robust composite and analysis of all genesis regions.

2.5   |   Bias and Future Change Calculations

The bias is commonly used to measure model performance and
consists  of  the  simple  difference  between  the  PC  (of  the  RCM
or GCM) simulation and reference dataset (PC—ERA5). Despite
the bias calculations being done for each model, the model- mean
ensemble  summarises  the  information.  In  this  case,  model-
mean ensemble differences (or changes) are possible because we
are not interested in investigating individual differences but the
overall result of the GCM and RCM signals. Thus, the average
of GCM was done considering HadGEM- PC and MPI- PC, while
the  RCM- mean  ensemble  considered  the  two  corresponding
downscaling simulations.

Following the same idea, the future changes were calculated by
the  difference  between  the  FF  and  PC.  This  subtraction  order
results in a positive (negative) signal for increasing (decreasing)
the variable in the future. First, the changes for each model were
calculated  and  then  gathered  into  GCM-   and  RCM- mean  en-
sembles, similar to the bias. For bias and changes, the statistical
significance at 95% confidence level is expressed by the t- test for
the differences between each pair of models.

4 of 19

International Journal of Climatology, 2024

3   |   Results

3.1   |   Present Climate

3.1.1   |   Genesis Density and Intensity

The cyclogenesis density for ERA5 reveals the three preferred
regions  for  genesis  in  the  SAM,  as  indicated  by  the  density
cores  in  the  summer  (Figure  1a)  and  winter  (Figure  1d),
especially  in  the  Argentinian  coast  (ARG).  Despite  some
small  variations,  these  regions  are  reported  by  many  studies
(e.g.,  Hoskins  and  Hodges  2005;  Reboita  et  al.  2010;  Crespo
et  al.  2020).  The  exact  location  of  these  regions  may  change
according to the tracking method and density estimation pa-
rameters.  Despite  the  seasonal  variability  of  the  cyclogene-
sis  activity  in  SAM,  we  defined  four  fixed  boxes  to  compute
the  statistics  and  three  for  the  composites,  even  if  a  genesis
region  presents  high- density  values  only  in  one  season.  The
fixed  boxes  facilitate  comparing  the  seasons  and  different
periods  and  support  the  comparison  between  models  once
they  are  defined  considering  the  reference  dataset.  The  four
boxes  defined  are  highlighted  in  Figure  1a,d,  corresponding
to the regions: (1) South American domain (SAM) (15° S–55° S;
30° W–75° W);  (2)  southern- southeastern  Brazilian  coast
(SBR) (22.5° S–37.5° S; 40° W–55° W); (3) La Plata Basin (LPB)
(22.5° S–37.5° S; 55° W–70° W) and (4) Argentina coast (ARG)

(37.5° S–55° S;  57.5° W–72.5° W).  The  first  box  represents  the
entire domain used to evaluate the genesis in South America
and  was  not  considered  in  the  analysis  of  the  composite.
Gramcianinov, Hodges, and Camargo (2019), using the same
tracking  method  and  density  estimation  parameters,  found
similar  genesis  regions  for  the  NCEP- CFSR  reanalysis  (Saha
et al. 2010) between 1979 and 2010. Comparing the three re-
gions, ARG presents the highest genesis density in all seasons
but  with  slightly  larger  values  in  the  summer.  Cyclogenesis
in  the  LPB  is  more  active  in  winter,  and  SBR  presents  more
genesis in its northern (southern) portion in summer (winter).
The seasonal variability is also synthesised in Figure 2, which
shows the frequency of genesis in DJF and JJA in each region
for each simulation. The annual and seasonal means for each
region can be found in Table S1.

Both  GCMs  and  RCMs  underestimated  the  number  of  cy-
clogenesis  events  in  most  parts  of  the  domain,  as  seen  in
the  seasonal  mean  (Figure  2a)  and  the  genesis  density  bias
(Figure  1b,c,e,f).  However,  this  underestimation  is  less  than
10%  in  the  RCMs  and  GCMs  and  is  not  homogeneous  in  the
entire domain (Figure 2a and Table S1). The cyclogenesis den-
sities  for  each  model  are  shown  in  Figure  S1.  In  some  loca-
tions,  the  GCMs  and  RCMs  present  even  more  genesis  than
the reference, such as in ARG for both GCMs. ARG is a loca-
tion with a large bias caused by the models' shifts in the main

FIGURE 1    |    Mean seasonal cyclogenesis density for (a) DJF and (d) JJA from ERA5, and present climate (1985–2005) mean bias for (b, e) GCM-
mean bias (PC—ERA5), and (c, f) RCM- mean bias (PC—ERA5). The unit of genesis density is cyclones per month per 5° spherical cap (~106 km2).
Density and bias are also contoured (dashed line) by 1 density unit. Grey markers represent where the bias signal agrees among each group of models.
The genesis regions marked with rectangles are La Plata Basin (LPB), the southern Brazilian coast (SBR), and the Argentinian coast (ARG). [Colour
figure can be viewed at wileyonlinelibrary.com]

5 of 19

3.1.2   |   Cyclone Structure

In this section, the synoptic structure of the cyclone was an-
alysed using a set of composites of variables from the upper,
middle, and lower levels of the atmosphere for each cyclogene-
sis region. From Figures 5–7, the composites present the verti-
cal structure of the atmosphere, with winds and its divergence
at 200 hPa, moisture flux (and its divergence) at 850 hPa and
geopotential at 500 hPa, and winds and temperature advection
at  850 hPa  for  ERA5,  GCMs  and  RCMs.  We  chose  the  most
active season for each genesis region to construct the compos-
ites  since  the  patterns  are  similar  to  the  other  seasons,  but
in  the  active  season,  there  are  stronger  fields.  Moreover,  the
composites  of  cyclones  at  12 h  after  the  time  of  genesis  were
selected  due  to  their  more  organised  structures  (than  at  0 h)
since  the  vorticity- based  tracking  detects  cyclonic  perturba-
tions that can still be very weak, resulting in very smoothed
initial fields.

3.1.2.1   |   Overview  of  the  Cyclones'  Development  in
Each  Region.  We  begin  the  cyclone's  development  over-
view  from  the  low  to  the  upper  levels  (Figures  4–6).  As  it  is
possible  to  note,  the  cyclones  in  SBR  (Figure  4a)  and  LPB
(Figure  5a)  present  a  warm  advection  to  the  east  of  the  cen-
tre  stronger  than  the  cold  advection  to  the  west,  which  is
associated  with  intense  northwesterly  winds.  In  SBR,  this
flow  is  associated  with  the  South  Atlantic  Subtropical  High
(SASH)  in  the  east,  while  in  LPB,  it  results  from  the  com-
bination  of  SASH  (northerly  winds)  and  the  South  America
low- level  jet  (SALLJ)  in  the  northeast  quadrant  (e.g.,  Gozzo
et  al.  2017).  On  the  other  hand,  the  ARG  cyclones  show  a
strong  zonal  dipole  of  cold  to  the  west  and  warm  advection
to  the  east  of  the  centre  (Figure  6a).  Northwesterly  winds
are transporting the warm air, while the stronger cold advec-
tion is influenced by the southwesterly winds carrying polar
air from Antarctica. The more intense advection in the ARG
composite reflects the amplification of a baroclinic low- level
wave,  which  results  in  stronger  cyclones  (central  pressure
of 993 hPa) in the MSLP field.

The low- level moisture flux is stronger in the SBR and LPB cy-
clones compared with ARG, due to the influence of the SASH
in the former and the SALLJ in the latter (Figures 4–6d). These
circulation  patterns  bring  moisture  from  the  ocean  and  the
Amazon region, respectively, contributing to the moisture flux
convergence  (negative  divergence)  in  the  centre- eastern  sector
of the cyclone. In ARG, more intense moisture flux convergence
occupies  a  smaller  area  on  the  eastern  side  of  the  cyclone,  in-
dicating that moisture availability plays a minor role in the cy-
clone's  development,  as  discussed  by  Gramcianinov,  Hodges,
and Camargo (2019). At the middle level, the trough is located
westward of the cyclone centre, contributing to further surface
cyclone deepening; this pattern is well- defined in the LPB and
ARG  composites  (Figures  5–6d).  SBR  also  presents  a  smaller
trough  at  500 hPa  upstream  of  the  cyclone  centre,  giving  dy-
namical support to the low- level convergence and, thus, to the
cyclone development (Figure 4d).

At upper levels, the stronger divergence downstream of the cy-
clone centre (Figures 4–6g) is one of the major dynamical support
to further the cyclone development, contributing to the upward

FIGURE  2    |    (a)  Present  climate  (1985–2005)  seasonal  mean  of
cyclogenesis (bars) and standard deviation (black lines) in each region
(see  a)  for  each  dataset.  (b)  Relative  (%)  of  change  in  the  FF  period
related  to  PC  period  in  each  season  and  region,  following  the  same
legend presented in panel (a). The diamond symbol in (b) indicates t- test
statistically significant changes at 95% confidence level. [Colour figure
can be viewed at wileyonlinelibrary.com]

genesis  density  core.  While  ERA5  presents  a  higher  genesis
density between 40° S and 55° S, the GCMs show the density
core shifted southward (centred around 50° S; Figure S1), and
the RCMs present a genesis density more spread towards both
south and north (from 35° S to 55° S) of the domain. The ARG
region  also  shows  large  differences  among  the  GCMs  since
the  genesis  density  for  the  MPI  is  more  concentrated  in  the
southern edge of the continent (~52° S) in both seasons. Also,
MPI has a slightly higher density in winter in the LPB region,
around 38° S, which is not observed in HadGEM.

The bias signal agreement between the RCM simulations is larger
than between their respective GCM drivers, revealing a potential
dominance of the regional model in the simulations. This is par-
ticularly true for regions where regional features play a big role in
circulation, such as on the lee side of the Andes Mountains and
at the land- ocean boundaries. The bias considering the seasonal
mean  of  genesis  (Figure  2a;  Table  S1)  is  smaller  in  the  RCMs
than the GCMs in most of the cyclogenesis cores, except in LPB.
However,  it  is  important  to  note  that  the  RCMs'  biases  are  not
high (±10%; see Table S1) and are within the expected biases for
this kind of system (Reboita et al. 2010).

The  frequency  distributions  of  the  maximum  10- m  wind
speed associated with the early stages of cyclones (0–12 h) are
presented  in  Figure  3.  The  GCMs  tend  to  underestimate  the
wind intensity in all regions, presenting weaker systems than
ERA5 and the RCMs, as depicted by the distributions skewed
to  the  left.  The  wind  speed  underestimation  by  the  GCMs  is
stronger in LPB. The RCMs are generally closer to the ERA5
wind speed distribution but with an overestimation of the cy-
clones' winds, as depicted by the high probability in the right-
hand  tail.  Bengtsson,  Hodges,  and  Roeckner  (2006)  discuss
the direct relation between the model resolution and cyclone
intensity, which can explain the stronger winds in the higher
resolution  simulations  in  some  locations.  However,  further
investigation  is  needed  to  understand  what  mechanisms  are
intensifying the cyclones in the RCMs.

6 of 19

International Journal of Climatology, 2024

FIGURE 3    |    Present climate (1985–2005) seasonal frequency distribution of the maximum 10- m wind speed (m/s) associated with the cyclones
during the first +12 h of their lifecycle in the present climate for: (a, d) ARG, (b, e) LPB, and (c, f) SBR genesis regions in the (a–c) austral winter and
(d–f) summer. [Colour figure can be viewed at wileyonlinelibrary.com]

air  motion  in  the  warm  sector  and,  as  a  consequence,  enhanc-
ing the low- level moisture flux convergence (Figures 4–6d). This
upper level mechanism is stronger in the SBR and LPB regions
than  in  ARG.  Nevertheless,  the  upper  level  jet  location  relative
to the centre of the surface cyclone is strictly associated with the
divergence. According to the composites, the cyclones developing
in the SBR and LPB are associated with the equatorward entrance
of the upper level jet stream, which supports strong upper level
divergence  (Figures  4  and  5g).  This  pattern  was  also  found  by
Crespo  et  al.  (2020)  when  analysing  the  upper  level  jet  stream
anomalies during the cyclogenesis around the same latitude. The
stronger upper level divergence is coupled to the low- level con-
vergence in SBR and LPB (Figures 4 and 5d), revealing the impor-
tance of the upper level forcing to the genesis therein.

3.1.2.2   |   RCM  and  GCM  Characteristics  and  Differ-
ences.  After the brief characterisation of the most important
forcings  for  cyclone  development  in  each  region,  Figures  4–6
also  present  the  models'  performances  in  reproducing  these
fields. The RCM spatial pattern shows a general improvement
(relative to the GCMs) in all fields. Starting with the temperature
advection in SBR, the GCM- mean underestimates cold (western
side) and warm (eastern side) advections and has a weaker sur-
face  cyclone  than  ERA5  and  the  RCM- mean  (Figures  4–6a,c).
The GCM- mean underestimated the moisture flux convergence
in  the  eastern  cyclone  centre,  while  the  RCM- mean  depicts
a  pattern  and  intensity  closer  to  ERA5  (Figure  4d–f).  Mov-
ing  to  the  middle  and  upper  levels,  the  RCM- mean  shows  an
enhanced  upper  tropospheric  divergence  at  200  and  a  500 hPa

7 of 19

FIGURE  4    |    Mean  composites  in  the  present  climate  (1985–2005)  of  ERA5  (first  column),  GCM  (middle  column),  and  RCM  (last  column)
circulation fields during austral summer cyclogenesis (after +12 h of genesis) in SBR. First row (a–c) temperature advection (K day−1; shaded) and
winds (m/s; vector) at 850 hPa, and mean sea level pressure (hPa; dashed contour); the middle row (d–e) moisture flux ([g kg−1][m s−1]; vector) and
convergence (g kg−1 s−1; shaded) at 850 hPa, and geopotential at 500 hPa (gpm; contour); bottom row (g–i) divergence (10−5 s−1; shaded) and winds
(m/s; vector and contour) at 200 hPa. [Colour figure can be viewed at wileyonlinelibrary.com]

trough closer to the surface cyclone than the GCM- mean in SBR
(Figure  4d–i),  supporting  the  more  intense  surface  cyclone  in
the RCM- mean (Figure 4b,c).

For LPB, the RCM- mean cyclone is also stronger regarding its
central MSLP (1011 hPa) than the GCM- mean (1013 hPa), and
the  former  is  in  greater  agreement  with  ERA5  (Figure  5a,b).

8 of 19

International Journal of Climatology, 2024

FIGURE 5    |    The same as Figure 4, but for the LPB cyclones in the austral winter (JJA). [Colour figure can be viewed at wileyonlinelibrary.com]

According to Figure 5, this is mainly supported by the RCM-
mean's stronger warm and cold air advection at low levels than
other forcings (moisture flux convergence and upper level di-
vergence).  Composites  for  ARG  cyclones  show  the  cold  and
warm advection improvement by the RCM- mean, as indicated
by  the  greater  proximity  to  the  cyclone  centre  as  in  ERA5
(Figure  6a–c).  The  warm- cold  sectors  of  the  ARG  cyclones

also  present  an  improvement  in  representing  the  moisture
flux  convergence–divergence (Figure 6d–f), which can explain
the  frequency  distribution  of  maximum  10- m  wind  speed
(Figure 3d). For the upper level divergence (Figure 6g–i), there
is similarity between the GCM- mean and the RCM- mean, with
less indication of an added value of the RCMs, at least for this
variable.

9 of 19

FIGURE 6    |    The same as Figure 4, but for ARG cyclones in DJF. [Colour figure can be viewed at wileyonlinelibrary.com]

3.2   |   Future Climate: Frequency and Synoptic
Patterns

3.2.1   |   Frequency Trends

In the FF, it is projected an overall decrease of cyclogenesis in
the domain, as seen by the dominant blue colours in Figure 7,
and  the  predominance  of  negative  significant  trends  in  most

subdomains and seasons (Figure 2b). The GCM- mean projec-
tions agree with a decrease between 1.2 and 2.4 cyclones per
month  in  the  ARG  region  in  the  summer  (Figure  7a),  while
the  RCM- mean  shows  a  different  pattern  with  weak  positive
trends  in  most  portions  of  ARG  (Figure  7b).  The  opposite
behaviour  between  GCM- mean  and  RCM- mean  in  the  ARG
region in the summer is also evident in the relative trends in-
tegrated over the region (Figure 2b). In the winter, the density

10 of 19

International Journal of Climatology, 2024

FIGURE 7    |    Future change (FF—PC) of the cyclogenesis density in (a, b) DJF and (c, d) JJA for the (a, c) GCM- mean and (b, d) RCM- mean. The
density unit is genesis per month per 5° spherical cap (~106 km2). The model- mean cyclogenesis in the PC (dashed line) is contoured by 1 density unit.
Grey markers represent where the change signal agrees among each member of the ensemble. [Colour figure can be viewed at wileyonlinelibrary.
com]

change spatial pattern indicates a decrease of cyclogenesis in
the centre- northern portion of the ARG region, which is stron-
ger in the RCM- mean (Figure 8c,d). The disagreement among
projections  in  ARG  is  driven  by  GCMs,  with  the  HadGEM
and  RegHad  projecting  a  decrease  in  genesis  while  MPI  and
RegMPI  present  positive  and  neutral  changes,  respectively
(Figures 2b and S2).

In winter, there is a positive trend in the LPB with different spa-
tial patterns among the GCM- mean and RCM- mean (Figure 7).

While the RCM- mean projects a genesis increase over the conti-
nent (at ~62° W–25° S), in the GCMs, a weaker increasing genesis
is located southeastward, over Uruguay (centred ~58° W–32° S).
Looking at the percentual trends for individual projections inte-
grated in the LPB, only RegHad projects a general decrease and
increase in the number of genesis, respectively, in DJF and JJA
(Figure  2b).  The  SBR  region  presents  a  general  negative  trend
of  genesis  in  both  seasons,  which  is  more  prominent  in  DJF,
with  a  signal  agreement  between  RCM- mean  and  GCM- mean
(Figures 2b and 7).

11 of 19

FIGURE 8    |    Far- future changes in cyclones in SBR for the (a–c) GCM- mean (FF—PC) and (d–f) RCM- mean (FF—PC) for DJF at +12 h after the
time of genesis. First column (a, d) temperature advection (K day−1; shaded) and winds (m/s; vector) at 850 hPa, and mean sea level pressure (hPa;
dashed contour); middle column (b, e) the moisture flux ([g kg−1][m s−1]; vector) and convergence (g kg−1 s−1; shaded) at 850 hPa, and geopotential at
500 hPa (gpm; contour); and last column (c, f) divergence (10–5 s−1; shaded) and winds (m/s; vector and contour) at 200 hPa. Hachures mark where
the change signal is significant (t- test; p ≤ 0.05). [Colour figure can be viewed at wileyonlinelibrary.com]

3.2.2   |   Synoptic Patterns

The future changes in the cyclone synoptic structure were an-
alysed  by  calculating  the  differences  (FF  minus  PC)  for  the
set  of  composites  at  different  atmospheric  levels,  as  shown  in
Figures 8–10. Even though the composite changes have a similar
spatial pattern in summer and winter, we only show the same
season analysed in the PC (Figures 4–6).

Summer  presents  a  predominance  of  negative  cyclogenesis
density  changes  for  GCM- mean  and  RCM- mean  (Figure  7).
However, the RCM- mean and GCM- mean composites project an
increase in the warm advection and moisture flux convergence
at low levels in the east/northeast sides of the cyclones (Figure 8).
The  moisture  flux  convergence  is  also  enhanced  to  the  north-
east of the cyclone centre, presenting a strengthening of the an-
ticyclonic circulation to the east that is more pronounced in the
RCM- mean (Figure 8). As discussed previously, this circulation
resembles the influence of the SASH, which plays an important
role as a moisture and heat source for the genesis at SBR. The
strengthening of SASH in FF scenarios is a recurrent feature in

mean- field trends (Krüger et al. 2012; Reboita et al. 2019). The
upper  level  pattern  projects  a  decrease  in  cyclogenesis  mecha-
nisms  through  strongly  weakening  the  upper  level  divergence
above the surface cyclone. This weakening is better defined in
the  GCM- mean  than  the  RCM- mean  (Figure  8c,f).  Therefore,
low- level (thermal advection and moisture flux) trends indicate
changes that favour more intense cyclones in line with the pro-
jected decrease in sea- level pressure (Figure 8a,d). In contrast,
the trend of upper level divergence decreases in the equatorial
jet entrance, which acts in the opposite direction (Figure 8c,f).
This last feature predominates at mid upper levels such that the
decrease in MSLP is not accompanied by a decrease in geopoten-
tial height at 500 hPa (Figure 8b,d).

LPB cyclogenesis density changes in DJF indicate a weak neg-
ative trend in the genesis density, while for JJA, it is weak and
positive (Figures 2–7). Similar to the changes in the SBR region,
in  LPB,  there  is  an  increase  in  the  warm  advection  and  mois-
ture flux convergence at 850 hPa, with a more defined signal in
the  GCM- mean  than  RCM- mean  (Figure  9a–e).  The  moisture
flux convergence is reinforced by northerly flow intensification

12 of 19

International Journal of Climatology, 2024

FIGURE 9    |    The same as in Figure 8, but for the LPB in JJA. [Colour figure can be viewed at wileyonlinelibrary.com]

towards  the  cyclone's  centre,  as  expected  from  the  influence
of the SALLJ in the region. The composites also reinforce cold
air  advection  advancing  to  the  east  sector  of  cyclones,  which
is  stronger  in  the  RCM- mean  (Figure  9a,b).  The  upper  level
changes also reveal a decrease in the mass divergence in a large
area  near  the  trough,  which  is  generally  more  intense  in  the
RCM- mean than in the GCM- mean fields (Figure 9). As in SBR,
for  LPB,  the  low- level  forcing  acts  in  the  opposite  direction  of
the upper level forcing, with consequent decreases of MSLP in
most of the domain that is not accompanied by the decrease of
geopotential height at 500 hPa (Figure 9).

Finally, the ARG composites trend for the summer is shown in
Figure 10; during this season, the GCM- mean presents a decrease
in cyclogenesis (Figure 7c) and the RCM- mean indicates a weak
increase in the region (Figure 7b). At low levels, the composites
present a slight increase of moisture flux, with weak impacts in
its convergence to the northeast of cyclone centre (Figure 10b,e).
There  is  a  general  projection  of  increasing  warm  and  cold  ad-
vection,  with  the  cold  (warm)  air  advancing  to  the  cyclone's
warm (cold) sector. The RCM- mean and GCM- mean composites
have  similar  trend  signals  for  both  moisture  flux  and  its  con-
vergence  and  the  warm  and  cold  advection  (Figure  10a,b,d,e).
At  upper  levels,  the  GCM- mean  and  RCM- mean  trends  reveal
a small increase in the mass divergence eastward of the cyclone

centre, being stronger in the former. In general, the changes in
the variables are relatively weaker compared with mean values
in  the  PC  (Figure  6),  which  may  explain  the  difference  in  the
RCM- mean  and  GCM- mean  divergent  trends  signal  for  cyclo-
genesis frequency in ARG (Figures 2b and 7). Note that the ARG
composites have noisy fields, particularly at the middle level in
their southern edge, probably due to the CORDEX- SAM domain
boundary available to track cyclones.

4   |   Discussion

The discussion is divided into two parts, following the scientific
questions established in the introduction: the RCM added value
and the projected future changes.

4.1   |   Added Value of RegCM Simulations

For most assessed metrics (density, composite and trends), the
RCM- mean  provides  greater  agreement  with  ERA5  reanalysis
than  the  GCM- mean.  The  increase  in  the  resolution  is  com-
monly  related  to  the  representation  of  more  cyclones  in  the
model  (e.g.,  Bengtsson,  Hodges,  and  Roeckner  2006).  Even
with  the  application  of  filters  in  the  vorticity  field  during  the

13 of 19

FIGURE 10    |    The same as in Figure 8, but for the ARG in DJF. [Colour figure can be viewed at wileyonlinelibrary.com]

tracking  pre- processing,  the  features  produced  by  the  model
resolution improvements, such as orography, remain to be iden-
tified and tracked. These address the decrease and inversion of
the  bias  signal  between  40° S  and  20° S  (Figure  1),  since  the
genesis in this band is directly affected by the lee effect of the
Andes Cordillera (Gan and Rao 1994; Vera et al. 2006; Reboita,
da  Rocha,  and  Ambrizzi  2012).  The  mountain  chain  in  SAM
plays an important role by interacting with mid and upper level
perturbations.  It  also  acts  by  channelling  warm  and  moist  air
from the tropics to the subtropics through the low- level jet. For
the composites, the RCM- mean's performance is better than the
GCM- mean in most of the fields analysed, showing more meso-
scale structure (as ERA5) near the cyclone centres as indicated
by warm/cold advection and moisture flux convergence/diver-
gence (east/northeast side) at low levels. The exception occurs
for moisture flux divergence in LPB. The moisture and warm air
reduce the low- level stability, playing a big role in cyclone devel-
opment in the LPB and SBR regions (Vera et al. 2006; Reboita,
da  Rocha,  and  Ambrizzi  2012;  Gramcianinov,  Hodges,  and
Camargo 2019). Thus, besides improving the cyclogenesis struc-
ture  due  to  the  increase  in  the  orography  representation,  the
RCM allows heat and moisture to play an enhanced role in cy-
clone development by refining physical processes. The increase
of resolution again matters, but more specific parameterizations,

with a proper setting for regional applications, probably play a
major role in the improvement of the processes such as inter-
actions in the lower level boundary layer, cloud formation, and
microphysics  (Déqué  et  al.  2005;  Prein  et  al. 2016;  Casanueva
et  al.  2016;  Lucas- Picher,  Laprise,  and Winger  2017).  Still,  for
SBR  and  LPB,  the  RCM- mean  also  improves  mid- upper  level
fields, as indicated by the greater agreement with ERA5 for the
location/intensity of the trough at 500 hPa and the upper level
divergence for SBR cyclones. All these features are indications
of RCM- mean added value around the cyclone centre, resulting
in smaller biases for surface cyclone intensity in LPB and SBR
(Figures 4c and 5c). Moreover, the added- value analysis shows
that  improving  the  low- level  circulation  processes  also  affects
the ARG cyclone, with more intense winds associated with cy-
clones over that region.

The  joint  bias  and  added  value  analysis  give  us  more  insights
into  the  mechanisms  prevailing  in  the  GCM  and  RCM- derived
cyclones.  Our  results  showed  that  the  GCMs  present  a  smaller
bias in the middle and upper level composites, indicating that the
mechanisms at these levels are the main driver of cyclogenesis in
these models, which justifies the similar or smaller number of sys-
tems in their simulation. In other words, GCMs cannot represent
many cyclones that result from the amplification of a perturbation

14 of 19

International Journal of Climatology, 2024

due  to  low- level  thermodynamics  processes  as  expected  due  to
their resolution. This impacts the number of cyclones, especially
in the LPB and ARG region, and the intensity of the cyclones in
the GCM experiments. Following the concepts given by Deveson,
Browning, and Hewson (2002), the cyclones can be classified by
their forcing mechanisms as type ‘A’, for the dominance of lower
level forcing, type ‘B’ when upper level mechanisms are dominant
or type ‘C’, when perturbations are amplified by low- level diabat-
ically induced potential vorticity anomalies, which can be led by
strong latent heat release in the moist convection. Although this
classification is simple, it can be helpful to understand the added
value  and  the  differences  between  the  RCMs  and  GCMs.  Our
findings indicate that GCMs are more capable of reproducing type
B cyclones than others. This affects all subdomains, including the
ARG  region,  where  the  low- level  baroclinicity  and  temperature
advection are essential to reduce the low- level stability during cy-
clone development (Gramcianinov, Hodges, and Camargo 2019;
Crespo et al. 2020). Note that an upper level forcing is important
to ARG cyclogenesis (e.g., Crespo et al. 2020), but its effect alone
would not be enough to simulate cyclone development in that re-
gion accurately.

Nevertheless,  despite  improving  the  resolution  and  physical
processes, the RCMs still present a bias that may compromise
the  assessment  of  future  changes.  As  mentioned,  the  RCM-
mean  improves  the  regional  feature  representation  through
increased  resolution  and  better  parameterization  schemes.
However,  the  RCM- mean  negative  bias  in  the  frequency
of  cyclones  centred  close  to  47oS  (inside  the  ARG  core;  see
Figure 1c,f) is still relatively large. One reason would be that
the  limited  grid  compromises  the  eastward  propagation  of
mid and upper level waves in the western edge of the domain.
The needed relaxation within the borders could influence the
number of perturbation entrances in the domain and attenu-
ate them. This would affect the cyclogenesis all over the RCM
domain, mainly in ARG. LPB and SBR regions present other
mechanisms  leading  to  genesis  related  to  the  moisture  and
heat  fluxes.  ARG  is  strongly  affected  by  the  mid- upper  lev-
els  propagation  perturbations  and  their  interaction  with  the
Andes  Mountain  once  it  allows  the  increase  of  the  entrance
of  cold  air  above  the  continent  (e.g.,  Gan  and  Rao  1994).
Gramcianinov,  Hodges,  and  Camargo  (2019)  showed  that
the  strong  cold  advection  during  ARG  cyclone  development
decreases  the  static  stability  at  low  levels  since  it  occurs
above  the  warmer  land  surface,  particularly  in  the  summer.
Moreover,  Crespo  et  al.  (2020)  found  that  ARG  is  the  region
with  the  highest  frequency  of  potential  vorticity  streamers
 associated  with  cyclogenesis,  indicating  its  contribution  to
the upward motion during cyclone development, especially in
the summer.

Nevertheless, it is important to highlight that added- value assess-
ments are not trivial and can present many limitations. Previous
studies  (Coppola  et  al.  2014;  Feser  2006;  Giorgi  et  al.  2014;
Mishra, Sahany, and Salunke 2017) have shown that the added
value may deteriorate large- scale features associated with local
processes  where  it  is  expected  improvement,  such  as  in  warm
advection and moisture flux convergence regions. Especially if
the field is closely related to large- scale phenomena and remote
sources (i.e., SASH and upper level jet), and the regional model
cannot maintain them.

4.2   |   South American Cyclones' Future Changes

The future changes analysis showed a decrease in the number
of  cyclones  in  the  domain  following  several  works  that  also
found a reduction of systems in the middle latitudes (de Jesus
et  al.  2022;  Reboita,  Reale  et  al.  2021).  However,  the  spatial
distribution  of  changes  in  the  RCM- mean  genesis  reveals  an
increase  in  the  cyclones  in  some  locations,  such  as  ARG  in
summer and LPB in winter. Regarding the GCMs, the decrease
of cyclones in the latitude band between 40° S and 55° S, which
includes the ARG cyclones, is large in summer. According to
the  atmospheric  composites,  this  decrease  in  the  frequency
occurs even under more favourable low levels of air tempera-
ture advection and moisture flux convergence. However, com-
pared with mean values in the PC, these changes are relatively
weaker,  which  cannot  explain  the  divergent  signal  trends  in
the frequency of the projected systems by the RCM- mean and
the GCM- mean (Figure 2).

Neutral and positive signals of genesis density are found around
30° S  but  with  some  divergence  between  models.  In  the  com-
posites,  the  LPB  and  SBR  cyclones  project  stronger  warm  ad-
vection, and moisture flux and its convergence at low levels in
their warm sector, within circulation patterns that resemble the
reinforcement of the SALLJ and SASH, respectively. At upper
levels,  the  projections  indicate  a  decrease  in  mass  divergence
near the cyclone centre. While low- level forcing could be more
favourable for more intense surface cyclones (as shown by the
decrease  of  surface  pressure),  the  mid- upper  level  features
(weakening  of  the  trough  at  500 hPa  and  mass  divergence  at
200 hPa) would act in opposite directions. This indicates a fu-
ture change in the vertical structure of cyclones as well as the
predominance  of  low  levels  forcing  for  more  intense  cyclones
in LPB and SBR, which is in line with the mean environment
for explosive cyclones in the Southern Hemisphere discussed by
Reboita, Crespo et al. (2021) under a scenario with more avail-
able moisture on a warmer planet.

5   |   Conclusions

CORDEX- SAM RCM projections for the South America domain
and  its  driving  GCMs  were  used  to  assess  RCP8.5  future  pro-
jection of extratropical cyclones frequency, associated synoptic
features  and  RCMs  added  value.  Cyclones  were  tracked  using
a  common  algorithm  in  the  present  (1985–2005)  and  future
(2080–2099)  scenarios,  and  ERA5  reanalysis  was  used  as  the
reference data for PC evaluation.

In the PC, the spatial pattern of cyclogenesis density simulated
by RCMs and GCMs agrees with ERA5 reanalysis, reproducing
the  three  main  observed  cyclogenesis  regions  (ARG,  LPB,  and
SBR). The biases are predominantly negative but relatively small
for  each  cyclogenesis  core  (~10%),  in  agreement  with  Reboita
et al. (2010). The RCMs added value to the GCMs for each season,
as they presented a smaller genesis bias, except in the LPB region,
where RCMs showed cyclogenesis underestimation.

For  cyclone  synoptic  structure,  the  composites  indicate  that
the RCMs represent the cyclone developing mechanisms and,
thus, their structure, with greater similarity to the reference

15 of 19

reanalysis  (ERA5).  The  added  value  in  the  performance  can
be  explained  by  the  increase  in  the  resolution  and  a  better
representation  of  the  parameterized  physical  processes.  The
improvement in these forcing mechanisms leads to a few more
cyclones in the RCM- mean than in the GCM- mean and a de-
crease in the genesis density bias over the domain. Cyclogenesis
in some SAM core regions is strongly related to moisture and
heat  transport,  which  is  expected  to  be  enhanced  by  a  more
accurate  orography  representation  and  parameterizations  of
physical  processes  (interactions  surface- atmosphere,  micro-
physics  and  cloud  formation,  among  others)  in  RCMs.  Our
findings  show  an  improvement  of  low- level  fields  as  RCMs
presented, near the cyclone centres, the associated mesoscale
structure of warm and cold advection and moisture flux con-
vergence and divergence (east/northeast side) in greater agree-
ment with ERA5 than the GCM- mean (except for the moisture
flux divergence in LPB cyclones). This is an important added
value of RCMs to the GCMs fields, as pointed out in the review
paper by Giorgi (2019).

At the end of the century, RCMs and GCMs project a general de-
crease of cyclones in the SAM domain, in agreement with pre-
vious works (e.g., Reboita et al. 2018, 2021; de Jesus et al. 2021).
For  the  cyclogenesis  regions,  there  is  greater  agreement  be-
tween  GCMs  and  RCMs  concerning  the  signal  of  the  future
trend of cyclones being greater in SBR, LPB and ARG in austral
winter. In contrast, in ARG, they project different trends in aus-
tral summer.

As revealed by the composite differences, the synoptic struc-
ture  of  cyclones  in  the  future  also  presents  some  changes.
Around  30° S,  the  RCMs  and  GCMs  project  stronger  low-
level  mechanisms  that  lead  to  cyclone  development,  such  as
a  future  increase  in  moisture  flux  convergence  and  warm
advection. At the same time, the upper level mass divergence
associated  with  cyclones  decreases  in  FF.  While  low- level
forcing  is  projected  to  be  favourable  to  more  intense  surface
cyclones  (as  shown  by  the  decrease  of  surface  pressure),  the
mid- upper level features (weakening of the trough at 500 hPa
and of the mass divergence at 200 hPa) will act in opposite di-
rections. These changes are clear for cyclones of SBR and LPB.
Therefore,  these  cyclones'  intensification  (negative  trend  in
MSLP)  in  FF  could  occur  as  a  function  of  the  reinforcement
of low- level features and associated diabatic processes, as also
found  by  Reboita,  Crespo  et  al.  (2021)  for  explosive  cyclones
in the Southern Hemisphere. For cyclones in the ARG region,
the projected future trends in their drivers (low- level moisture
flux  and  temperature  advection,  mid- upper  level  winds,  and
troughs) are relatively weaker compared with mean values in
the  PC,  which  complicates  the  evaluation  of  different  trends
for  the  cyclogenesis  frequency  in  austral  summer  in  RCMs
(positive) and GCMs (negative).

Considering the added value of RCMs in representing cyclones
in  the  SAM  domain,  future  work  could  investigate  the  added
value of the CMIP6 GCMS that supported the High- Resolution
Model
(HighResMIP;  Haarsma
et al. 2016) having similar horizontal resolution (~25 km) as the
current CORDEX RCMs.

Intercomparison  Project

Author Contributions

Carolina  B.  Gramcianinov:  conceptualization,  investigation,  meth-
odology,  writing  –  original  draft,  writing  –  review  and  editing,  visu-
alization,  formal  analysis.  Andressa  A.  Cardoso:  conceptualization,
investigation,  methodology,  formal  analysis,  writing  –  original  draft,
writing – review and editing. Natália P. da Silva: conceptualization,
writing – review and editing, formal analysis. Rosa Luna- Niño: con-
ceptualization,  visualization,  writing  –  review  and  editing.  Natalia
Castillo: conceptualization, visualization, writing – review and editing.
Tereza Cavazos: writing – review and editing, supervision. Rosmeri
P. da Rocha: supervision, writing – review and editing, formal analysis.

Acknowledgements

We would like to thank Reviewers for their valuable comments and sug-
gestions, which helped us in improving the quality of the manuscript.
This collaborative research is the product of a capacity-building activity
organized  by  CORDEX-WCRP  to  promote  collaborative  activities  and
networking and to enhance the capacity to document scientific research
in Central America the Caribbean, and South America with a focus on
specific regional climate phenomena (http://www.cima.fcen.uba.ar/cor-
dex-2020/ ).  We acknowledge the World Climate Research Programme’s
Working  Group  on  Regional  Climate,  and  the  Working  Group  on
Coupled  Modelling,  former  coordinating  body  of  CORDEX  and  re-
sponsible panel for CMIP5. We also thank the climate modeling groups
(listed in Table 1) for producing and making their model output avail-
able.  We  also  acknowledge  the  Earth  System  Grid  Federation  (ESGF)
infrastructure,  an  international  effort  led  by  the  U.S.  Department  of
Energy’s  Program  for  Climate  Model  Diagnosis  and  Intercomparison,
the European Network for Earth System Modelling and other partners
in the Global Organisation for Earth System SciencePortals (GO-ESSP).
This  project  took  advantage  of  MetPy  software  developed  by  UCAR/
NSF  Unidata  (https://doi.org/10.5065/D6WW7G29).  C.B.G.  is  funded
by  the  Helmholtz  European  Partnership  ‘Research  Capacity  Building
for  Healthy,  productive  and  Resilient  Seas’  (SEA-ReCap,  grant  no.
PIE-0025).  R.P.R.  acknowledges  the  CNPq  (grant  nos.  430314/2018-3;
304949/2018-3) and FAPESP (grant no. 2022/05476-2).

Conflicts of Interest

The authors declare no conflicts of interest.

Data Availability Statement

The ERA5 products were generated using Copernicus Climate Change
Service  Information  (2021)  https:// cds. clima te. coper nicus. eu.  The
GCMs and RCMs used in this work are available in the Earth System
Grid Federation (ESGF) platform https:// esgf. llnl. gov.

References

Belmonte  Rivas,  M.,  and  A.  Stoffelen.  2019.  “Characterizing  ERA-
Interim and ERA5 Surface Wind Biases Using ASCAT.” Ocean Science
15, no. 3: 831–852. https:// doi. org/ 10. 5194/ os-  15-  831-  2019.

Bengtsson, L., K. I. Hodges, and N. Keenlyside. 2009. “Will Extratropical
Storms Intensify in a Warmer Climate?” Journal of Climate 22: 2276–
2301. https:// doi. org/ 10. 1175/ 2008j cli26 78. 1.

Bengtsson, L., K. I. Hodges, and E. Roeckner. 2006. “Storm Tracks and
Climate Change.” Journal of Climate 19: 3518–3543. https:// doi. org/ 10.
1175/ jcli3 815. 1.

Carril, A. F., C. G. Menéndez, A. R. C. Remedio, et al. 2012. “Performance
of a Multi- RCM Ensemble for South Eastern South America.” Climate
Dynamics 39: 2747–2768. https:// doi. org/ 10. 1007/ s0038 2-  012-  1573-  z.

16 of 19

International Journal of Climatology, 2024

Casanueva, A., S. Kotlarski, S. Herrera, et al. 2016. “Daily Precipitation
Statistics  in  a  EURO- CORDEX  RCM  Ensemble:  Added  Value  of  Raw
and  Bias- Corrected  High- Resolution  Simulations.”  Climate  Dynamics
47: 719–737. https:// doi. org/ 10. 1007/ s0038 2-  015-  2865-  x.

Gan,  M.  A.,  and  V.  B.  Rao.  1994.  “The  Influence  of  the  Andes
Cordillera on Transient Disturbances.” Monthly Weather Review 122:
1141–1157.  https:// doi. org/ 10. 1175/ 1520-  0493(1994) 122< 1141: tiota c>
2.0. co; 2.

Castro,  C.  L.,  R.  A.  Pielke  Sr.,  and  G.  Leoncini.  2005.  “Dynamical
Downscaling:  Assessment  of  Value  Retained  and  Added  Using  the
Regional Atmospheric Modeling System (RAMS).” Journal of Geophysical
Research: Atmospheres 110: D05108. https:// doi. org/ 10. 1029/ 2004j d004721.

Catto,  J.  L.,  D.  Ackerley,  J.  F.  Booth,  et  al.  2019.  “The  Future  of
Midlatitude  Cyclones.”  Current  Climate  Change  Reports  5:  407–420.
https:// doi. org/ 10. 1007/ s4064 1-  019-  00149 -  4.

Catto, J. L., L. C. Shaffrey, and K. I. Hodges. 2010. “Can Climate Models
Capture the Structure of Extratropical Cyclones?” Journal of Climate 23:
1621–1635. https:// doi. org/ 10. 1175/ 2009j cli33 18. 1.

Coppola,  E.,  F.  Giorgi,  F.  Raffaele,  et  al.  2014.  “Present  and  Future
Climatologies  in  the  Phase  I  CREMA  Experiment.”  Climatic  Change
125: 23–38. https:// doi. org/ 10. 1007/ s1058 4-  014-  1137-  9.

Crespo,  N.  M.,  R.  P.  da  Rocha,  M.  Sprenger,  and  H.  Wernli.  2020.  “A
Potential  Vorticity  Perspective  on  Cyclogenesis  Over  Centre- Eastern
South  America.”  International  Journal  of  Climatology  41:  663–678.
https:// doi. org/ 10. 1002/ joc. 6644.

Dacre,  H.  F.,  and  S.  L.  Gray.  2009.  “The  Spatial  Distribution  and
Evolution Characteristics of North Atlantic Cyclones.” Monthly Weather
Review 137: 99–115. https:// doi. org/ 10. 1175/ 2008m wr2491. 1.

de  Jesus,  E.  M.,  R.  P.  da  Rocha,  N.  M.  Crespo,  M.  S.  Reboita,  and  L.
F.  Gozzo.  2021.  “Multi- Model  Climate  Projections  of  the  Main
Cyclogenesis Hot- Spots and Associated Winds Over the Eastern Coast
of  South  America.”  Climate  Dynamics  56:  537–557.  https:// doi. org/ 10.
1007/ s0038 2-  020-  05490 -   1.

de  Jesus,  E.  M.,  R.  P.  da  Rocha,  N.  M.  Crespo,  M.  S.  Reboita,  and  L.
F.  Gozzo.  2022.  “Future  Climate  Trends  of  Subtropical  Cyclones
in  the  South  Atlantic  Basin  in  an  Ensemble  of  Global  and  Regional
Projections.” Climate Dynamics 58: 1221–1236. https:// doi. org/ 10. 1007/
s0038 2-  021-  05958  -  8.

Déqué, M., R. G. Jones, M. Wild, et al. 2005. “Global High Resolution
Versus Limited Area Model Climate Change Projections Over Europe:
Quantifying  Confidence  Level  From  PRUDENCE  Results.”  Climate
Dynamics 25: 653–670. https:// doi. org/ 10. 1007/ s0038 2-  005-  0052-  1.

Deveson,  A.  C.  L.,  K.  A.  Browning,  and  T.  D.  Hewson.  2002.  “A
Classification of FASTEX Cyclones Using a Height- Attributable Quasi-
Geostrophic Vertical- Motion Diagnostic.” Quarterly Journal of the Royal
Meteorological Society 128: 93–117. https:// doi. org/ 10. 1256/ 00359 00026
0498806.

Di Luca, A., R. de Elía, and R. Laprise. 2012. “Potential for Added Value
in Precipitation Simulated by High- Resolution Nested Regional Climate
Models  and  Observations.”  Climate  Dynamics  38:  1229–1247.  https://
doi. org/ 10. 1007/ s0038 2-  011-  1068-  3.

Falco,  M.,  A.  F.  Carril,  L.  Z.  X.  Li,  C.  Cabrelli,  and  C.  G.  Menéndez.
2019. “The Potential Added Value of Regional Climate Models in South
America  Using  a  Multiresolution  Approach.”  Climate  Dynamics  54:
1553–1569. https:// doi. org/ 10. 1007/ s0038 2-  019-  05073 -  9.

Falco, M., A. F. Carril, C. G. Menéndez, P. G. Zaninelli, and L. Z. X. Li.
2018. “Assessment of CORDEX Simulations Over South America: Added
Value on Seasonal Climatology and Resolution Considerations.” Climate
Dynamics 52: 4771–4786. https:// doi. org/ 10. 1007/ s0038 2-  018-  4412-  z.

Feser,  F.  2006.  “Enhanced  Detectability  of  Added  Value  in  Limited-
Area  Model  Results  Separated  Into  Different  Spatial  Scales.”  Monthly
Weather Review 134: 2180–2190. https:// doi. org/ 10. 1175/ mwr31 83. 1.

Fyfe,  J.  C.  2003.  “Extratropical  Southern  Hemisphere  Cyclones:
Harbingers  of  Climate  Change?”  Journal  of  Climate  16:  2802–2805.
https:// doi. org/ 10. 1175/ 1520-  0442(2003) 016< 2802: eshch o> 2.0. co; 2.

Geng, Q., and M. Sugi. 2003. “Possible Change of Extratropical Cyclone
Activity  due  to  Enhanced  Greenhouse  Gases  and  Sulfate  Aerosols—
Study  With  a  High- Resolution  AGCM.”  Journal  of  Climate  16:  2262–
2274.
https:// doi. org/ 10. 1175/ 1520-  0442(2003) 16< 2262: pcoec a>
2.0. co; 2.

Giorgetta,  M.  A.,  J.  Jungclaus,  C.  H.  Reick,  et  al.  2013.  “Climate  and
Carbon  Cycle  Changes  From  1850  to  2100  in  MPI- ESM  Simulations
for  the  Coupled  Model  Intercomparison  Project  Phase  5.”  Journal  of
Advances in Modeling Earth Systems 5: 572–597. https:// doi. org/ 10. 1002/
jame. 20038 .

Giorgi,  F.  2019.  “Thirty  Years  of  Regional  Climate  Modeling:  Where
Are  We  and  Where  Are  we  Going  Next?”.  Journal  of  Geophysical
Research:  Atmospheres  124:  5696–5723.  https://doi.org/10.1016/j.
oceaneng.2020.107745 .

Giorgi, F., E. Coppola, D. Jacob, et al. 2022. “The CORDEX- CORE EXP- I
Initiative: Description and Highlight Results From the Initial Analysis.”
Bulletin of the American Meteorological Society 103: E293–E310. https://
doi. org/ 10. 1175/ bams-  d-  21-  0119. 1.

Giorgi, F., E. Coppola, F. Raffaele, et al. 2014. “Changes in Extremes and
Hydroclimatic Regimes in the CREMA Ensemble Projections.” Climatic
Change 125: 39–51. https:// doi. org/ 10. 1007/ s1058 4-  014-  1117-  0.

Giorgi,  F.,  E.  Coppola,  F.  Solmon,  et  al.  2012.  “RegCM4:  Model
Description and Preliminary Tests Over Multiple CORDEX Domains.”
Climate Research 52: 7–29. https:// doi. org/ 10. 3354/ cr01018.

Gozzo,  L.  F.,  R.  P.  da  Rocha,  L.  Gimeno,  and  A.  Drumond.  2017.
“Climatology and Numerical Case Study of Moisture Sources Associated
With Subtropical Cyclogenesis Over the Southwestern Atlantic Ocean.”
Journal of Geophysical Research: Atmospheres 122: 5636–5653. https://
doi. org/ 10. 1002/ 2016j d025764.

Gozzo,  L.  F.,  R.  P.  da  Rocha,  M.  S.  Reboita,  and  S.  Sugahara.  2014.
the  Southwestern  South  Atlantic:
“Subtropical  Cyclones  Over
Climatological Aspects and Case Study.” Journal of Climate 27: 8543–
8562. https:// doi. org/ 10. 1175/ jcli-  d-  14-  00149. 1.

Gramcianinov,  C.  B.,  R.  M.  Campos,  R.  de  Camargo,  K.  I.  Hodges,
C.  Guedes  Soares,  and  P.  L.  da  Silva  Dias.  2020.  “Analysis  of  Atlantic
Extratropical  Storm  Tracks  Characteristics  in  41 Years  of  ERA5  and
CFSR/CFSv2  Databases.”  Ocean  Engineering  216:  108111.  https:// doi.
org/ 10. 1016/j. ocean eng. 2020. 108111.

Gramcianinov, C. B., R. de Camargo, R. M. Campos, and P. L. da Silva
Dias. 2023. “Impact of Extratropical Cyclone Intensity and Speed on the
Extreme  Wave  Trends  in  the  Atlantic  Ocean.”  Climate  Dynamics  60:
1447–1466. https:// doi. org/ 10. 1007/ s0038 2-  022-  06390 -  2.

Gramcianinov,  C.  B.,  K.  I.  Hodges,  and  R.  Camargo.  2019.  “The
Properties  and  Genesis  Environments  of  South  Atlantic  Cyclones.”
Climate  Dynamics  53:  4115–4140.  https:// doi. org/ 10. 1007/ s0038 2-  019-
04778 -  1.

Grieger, J., G. C. Leckebusch, M. G. Donat, M. Schuster, and U. Ulbrich.
2014.  “Southern  Hemisphere  Winter  Cyclone  Activity  Under  Recent
and Future Climate Conditions in Multi- Model AOGCM Simulations.”
International Journal of Climatology 34: 3400–3416. https:// doi. org/ 10.
1002/ joc. 3917.

Grise,  K.  M.,  S.  Son,  and  J.  R.  Gyakum.  2013.  “Intraseasonal  and
Interannual  Variability  in  North  American  Storm  Tracks  and  Its
Relationship to Equatorial Pacific Variability.” Monthly Weather Review
141, no. 10: 3610–3625. https:// doi. org/ 10. 1175/ MWR-  D-  12-  00322. 1.

Gutowski, W. J., Jr., F. Giorgi, B. Timbal, et al. 2016. “WCRP COordinated
Regional Downscaling EXperiment (CORDEX): A Diagnostic MIP for

17 of 19

CMIP6.”  Geoscientific  Model  Development  9:  4087–4095.  https:// doi.
org/ 10. 5194/ gmd-  9-  4087-  2016.

Downscaling?”  Theoretical  and  Applied  Climatology  133:  1133–1141.
https:// doi. org/ 10. 1007/ s0070 4-  017-  2237-  z.

Haarsma, R. J., M. J. Roberts, P. L. Vidale, et al. 2016. “High Resolution
Model  Intercomparison  Project  (HighResMIP  v1.0)  for  CMIP6.”
Geoscientific Model Development 9: 4185–4208. https:// doi. org/ 10. 5194/
gmd-  9-  4185-  2016.

Naud,  C.  M.,  J.  Jeyaratnam,  J.  F.  Booth,  M.  Zhao,  and  A.  Gettelman.
2020.  “Evaluation  of  Modeled  Precipitation  in  Oceanic  Extratropical
Cyclones Using IMERG.” Journal of Climate 33: 95–113. https:// doi. org/
10. 1175/ JCLI-  D-  19-  0369. 1.

Hersbach,  H.,  B.  Bell,  P.  Berrisford,  et  al.  2020.  “The  ERA5  Global
Reanalysis.” Quarterly Journal of the Royal Meteorological Society 146:
1999–2049. https:// doi. org/ 10. 1002/ qj. 3803.

Hodges,  K.  I.  1994.  “A  General  Method  for  Tracking  Analysis  and  Its
Application  to  Meteorological  Data.”  Monthly  Weather  Review  122:
2573–2586. https:// doi. org/ 10. 1175/ 1520-  0493(1994) 122< 2573: agmft a>
2.0. co; 2.

Hodges,  K.  I.  1995.  “Feature  Tracking  on  the  Unit  Sphere.”  Monthly
Weather  Review
3458–3465.  https:// doi. org/ 10. 1175/ 1520-
0493(1995) 123< 3458: ftotu s> 2.0. co; 2.

123:

Hodges,  K.  I.  1996.  “Spherical  Nonparametric  Estimators  Applied  to  the
UGAMP Model Integration for AMIP.” Monthly Weather Review 124: 2914–
2932. https:// doi. org/ 10. 1175/ 1520-  0493(1996) 124< 2914: sneat t> 2.0. co; 2.

Hodges,  K.  I.  1999.  “Adaptive  Constraints  for  Feature  Tracking.”
Monthly Weather Review 127: 1362–1373. https:// doi. org/ 10. 1175/ 1520-
0493(1999) 127< 1362: acfft > 2.0. co; 2.

Hodges,  K.  I.,  R.  W.  Lee,  and  L.  Bengtsson.  2011.  “A  Comparison  of
Extratropical  Cyclones  in  Recent  Reanalyses  ERA- Interim,  NASA
MERRA, NCEP CFSR, and JRA- 25.” Journal of Climate 24: 4888–4906.
https:// doi. org/ 10. 1175/ 2011j cli40 97. 1.

Hoskins,  B.  J.,  and  K.  I.  Hodges.  2002.  “New  Perspectives  on  the
Northern Hemisphere Winter Storm Tracks.” Journal of the Atmospheric
Sciences  59:  1041–1061.  https:// doi. org/ 10. 1175/ 1520-  0469(2002) 059<
1041: NPOTN H> 2.0. CO; 2.

Hoskins, B. J., and K. I. Hodges. 2005. “A New Perspective on Southern
Hemisphere Storm Tracks.” Journal of Climate 18: 4108–4129.  https://
doi. org/ 10. 1175/ jcli3 570. 1.

IPCC.  2013.  “Climate  Change  2013:  The  Physical  Science  Basis.”  In
Contribution  of  Working  Group  I  to  the  Fifth  Assessment  Report  of  the
Intergovernmental  Panel  on  Climate  Change,  edited  by  T.  F.,  Stocker,
D.  Qin,  G.-K.  Plattner,  M.  Tignor,  S.K.  Allen,  J.  Boschung,  A.  Nauels,
Y.  Xia,  V.  Bex  and  P.  M.  Midgley,  1535.  New  York,  NY:  Cambridge
University Press.

Krüger,  L.  F.,  R.  P.  da  Rocha,  M.  S.  Reboita,  and  T.  Ambrizzi.  2012.
“RegCM3 Nested in HadAM3 Scenarios A2 and B2: Projected Changes
in Extratropical Cyclogenesis, Temperature and Precipitation Over the
South Atlantic Ocean.” Climatic Change 113: 599–621. https:// doi. org/
10. 1007/ s1058 4-  011-  0374-  4.

Neu,  U.,  M.  G.  Akperov,  N.  Bellenbaum,  et  al.  2013.  “IMILAST:  A
Community Effort to Intercompare Extratropical Cyclone Detection and
Tracking  Algorithms.”  Bulletin  of  the  American  Meteorological  Society
94, no. 4: 529–547. https:// doi. org/ 10. 1175/ BAMS-  D-  11-  00154. 1.

Pezza, A. B., and T. Ambrizzi. 2003. “Variability of Southern Hemisphere
Cyclone  and  Anticyclone  Behavior:  Further  Analysis.”  Journal  of
Climate  16:  1075–1083.  https:// doi. org/ 10. 1175/ 1520-  0442(2003) 016<
1075: voshc a> 2.0. co; 2.

Prein, A. F., A. Gobiet, H. Truhetz, et al. 2016. “Precipitation in the EURO-
CORDEX  0.11̊  and  0.44̊  Simulations:  High  Resolution,  High  Benefits?”
Climate Dynamics 46: 383–412. https:// doi. org/ 10. 1007/ s0038 2-  015-  2589-  y.

Reboita,  M.  S.,  T.  Ambrizzi,  B.  A.  Silva,  R.  F.  Pinheiro,  and  R.  P.  da
Rocha. 2019. “The South Atlantic Subtropical Anticyclone: Present and
Future Climate.” Frontiers in Earth Science 7: 8. https:// doi. org/ 10. 3389/
feart. 2019. 00008 .

Reboita, M. S., N. M. Crespo, J. A. Torres, et al. 2021. “Future Changes
in Winter Explosive Cyclones Over the Southern Hemisphere Domains
From  the  CORDEX- CORE  Ensemble.”  Climate  Dynamics  57:  3303–
3322. https:// doi. org/ 10. 1007/ s0038 2-  021-  05867 -  w.

Reboita, M. S., R. P. da Rocha, and T. Ambrizzi. 2012. “Dynamic and
Climatological Features of Cyclonic Developments Over Southwestern
South  Atlantic  Ocean.”  In  Horizons  in  Earth  Science  Research,  vol.  6.
Hauppauge: Nova Science Publishers.

Reboita,  M.  S.,  R.  P.  da  Rocha,  T.  Ambrizzi,  and  S.  Sugahara.  2010.
“South Atlantic Ocean Cyclogenesis Climatology Simulated by Regional
Climate  Model  (RegCM3).”  Climate  Dynamics  35:  1331–1347.  https://
doi. org/ 10. 1007/ s0038 2-  009-  0668-  7.

Reboita, M. S., R. P. da Rocha, M. R. de Souza, and M. Llopart. 2018.
“Extratropical Cyclones Over the Southwestern South Atlantic Ocean:
HadGEM2- ES  and  RegCM4  Projections.”  International  Journal  of
Climatology 38: 2866–2879. https:// doi. org/ 10. 1002/ joc. 5468.

Reboita, M. S., M. Reale, R. P. da Rocha, et al. 2021. “Future Changes in
the Wintertime Cyclonic Activity Over the CORDEX- CORE Southern
Hemisphere Domains in a Multi- Model Approach.” Climate Dynamics
57: 1533–1549. https:// doi. org/ 10. 1007/ s0038 2-  020-  05317 -  z.

Riahi,  K.,  S.  Rao,  V.  Krey,  et  al.  2011.  “RCP  8.5—A  Scenario  of
Comparatively High Greenhouse Gas Emissions.” Climatic Change 109:
33–57. https:// doi. org/ 10. 1007/ s1058 4-  011-  0149-  y.

Kumar,  D.,  and  A.  P.  Dimri.  2021.  “Context  of  the  Added  Value  in
Coupled  Atmosphere- Land  RegCM4–CLM4.5  in  the  Simulation  of
Indian Summer Monsoon.” Climate Dynamics 56: 259–274. https:// doi.
org/ 10. 1007/ s0038 2-  020-  05481 -  2.

Roebber, P. J., K. M. Grise, and J. R. Gyakum. 2023. “The Histories of
Well- Documented  Maritime  Cyclones  as  Portrayed  by  an  Automated
Tracking  Method.”  Monthly  Weather  Review  151:  2905–2924.  https://
doi. org/ 10. 1175/ MWR-  D-  22-  0287. 1.

Lucas- Picher, P., R. Laprise, and K. Winger. 2017. “Evidence of Added
Value in North American Regional Climate Model Hindcast Simulations
Using Ever- Increasing Horizontal Resolutions.” Climate Dynamics 48:
2611–2633. https:// doi. org/ 10. 1007/ s0038 2-  016-  3227-  z.

The  HadGEM2  Development  Team:  Martin,  G.  M.,  N.  Bellouin,  W.  J.
Collins, et al. 2011. “The HadGEM2 Family of met Office Unified Model
Climate Configurations.” Geoscientific Model Development Discussion 4:
723–757. https:// doi. org/ 10. 5194/ gmd-  4-  723-  2011.

McErlich,  C.,  A.  McDonald,  J.  Renwick,  and  A.  Schuddeboom.  2023.
“An  Assessment  of  Southern  Hemisphere  Extratropical  Cyclones  in
ERA5  Using  WindSat.”  Journal  of  Geophysical  Research:  Atmospheres
128: e2023JD038554. https:// doi. org/ 10. 1029/ 2023J D038554.

Mishra,  S.  K.,  S.  Sahany,  and  P.  Salunke.  2017.  “CMIP5  vs.  CORDEX
Over  the  Indian  Region:  How  Much  Do  We  Benefit  From  Dynamical

Saha, S., S. Moorthi, H.- L. Pan, et al. 2010. “The NCEP Climate Forecast
System Reanalysis.” Bulletin of the American Meteorological Society 91:
1015–1058. https:// doi. org/ 10. 1175/ 2010b ams30 01. 1.

Sanchez- Gomez,  E.,  S.  Somot,  and  M.  Déqué.  2009.  “Ability  of  an
Ensemble of Regional Climate Models to Reproduce Weather Regimes
Over Europe- Atlantic During the Period 1961–2000.” Climate Dynamics
33: 723–736. https:// doi. org/ 10. 1007/ s0038 2-  008-  0502-  7.

Solman, S. A., and J. Blázquez. 2019. “Multiscale Precipitation Variability
Over  South  America:  Analysis  of  the  Added  Value  of  CORDEX  RCM
Simulations.” Climate Dynamics 53: 1547–1565. https:// doi. org/ 10. 1007/
s0038 2-  019-  04689 -  1.

Tamarin,  T.,  and  Y.  Kaspi.  2017.  “The  Poleward  Shift  of  Storm  Tracks
Under Global Warming: A Lagrangian Perspective.” Geophysical Research
Letters 44: 10,666–10,674. https:// doi. org/ 10. 1002/ 2017g l073633.

18 of 19

International Journal of Climatology, 2024

Taylor,  K.  E.,  R.  J.  Stouffer,  and  G.  A.  Meehl.  2012.  “An  Overview
of  CMIP5  and  the  Experiment  Design.”  Bulletin  of  the  American
Meteorological  Society  93:  485–498.  https:// doi. org/ 10. 1175/ bams-  d-  11-
00094. 1.

Vera, C., G. Silvestri B. Liebmann and P. González. 2006. “Climate change
scenarios  for  seasonal  precipitation  in  South  America  From  IPCC-AR4
models, Geophys.” Geophysical Research Letters, 33: L13707. https:// doi.
org/10.1029/2006GL025759.

Zazulie, N., M. Rusticucci, and G. B. Raga. 2018. “Regional Climate of
the Subtropical Central Andes Using High- Resolution CMIP5 Models.
Part  II:  Future  Projections  for  the  Twenty- First  Century.”  Climate
Dynamics 51: 2913–2925. https:// doi. org/ 10. 1007/ s0038 2-  017-  4056-  4.

Supporting Information

Additional  supporting  information  can  be  found  online  in  the
Supporting Information section.

19 of 19

