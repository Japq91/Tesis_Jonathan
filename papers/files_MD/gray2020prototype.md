follow-on missions. Geophys. Res. Lett.  47(8):
e2020GL087291

WMO, World Glacier Monitoring Service:
Zurich, Switzerland.

Watson CW, White NJ, Church JA et al.
2015. Unabated global mean sea-level rise
over the satellite altimeter era. Nat. Clim.
Change  5: 565–568.

WGMS. 2020. in Global Glacier Change
Bulletin No. 3 (2016-2017). Zemp M,
Nussbaumer SU, Gärtner-Roer I et al. (eds).
ISC(WDS)/IUGG(IACS)/UNEP/UNESCO/

WMO. 2020. WMO Greenhouse Gas
Bulletin (GHG Bulletin) - No. 16: The State
of Greenhouse Gases in the Atmosphere
Based on Global Observations through
2019. WMO: Geneva, Switzerland.

WMO. 2021. WMO State of the Global
Climate in 2020, WMO-No. 1264. WMO:
Geneva, Switzerland.

Zemp M, Huss M, Thibert E et al. 2019.
Global glacier mass changes and their
contributions to sea-level rise from 1961
to 2016. Nature  568: 382–386.

Correspondence to: J. J. Kennedy

john.kennedy@metoffice.gov.uk

© 2021 Royal Meteorological Society

doi: 10.1002/wea.4087

G
l
o
b
a
l
a
n
d
r
e
g
i
o
n
a
l

c
l
i

m
a
t
e
i

n
2
0
2
0

Development  of  a  prototype
real-time  sting-jet  precursor  tool
for  forecasters

W
e
a
t
h
e
r
–
N
o
v
e
m
b
e
r

2
0
2
1
,

V
o
l
.

,

Suzanne  L.  Gray1
Oscar Martínez-Alvarado2  ,
Duncan  Ackerley3
Dan  Suri3
1Department of Meteorology, University

  and

of Reading, UK

2National Centre for Atmospheric
Science, and Department of
Meteorology, University of Reading, UK

3Met Office, Exeter, UK

Damaging surface winds in some European
storms  have  been  attributed  to  descend-
ing mesoscale airstreams termed sting jets.
The  development  of  a  prototype  real-time
tool  that  Met  Office  forecasters  can  use
to  identify  favourable  conditions  for  sting
jet  occurrence  in  extratropical  cyclones  is
presented.  The  motivation  is  to  improve
national severe weather warnings. We have
previously developed a convective-instabil-
ity-based  tool  to  identify  sting-jet  precur-
sors  for  research  purposes  and  applied  it
to storms in reanalyses and climate models
with insufficient spatial resolution to repre-
sent  sting  jets.  Here  we  describe  the  chal-
lenges  of  applying  this  research-derived
diagnostic  to  output  from  an  operational
forecast  system  and  demonstrate  its  use-
fulness  for  a  recent  winter  storm.  Through
close collaboration with the researchers and
forecasters  from  the  Met  Office,  the  diag-
nostic  has  been  adapted  to  work  on  out-
put from the Met Office’s operational global
ensemble forecasts as it becomes available.
Since  autumn  2019,  forecasters  have  been
able  to  view  graphical  output  informing
them whether storms impacting the UK and
Europe  (up  to  7  days  in  the  future)  have
the  precursor.  The  tool  has  already  proven

useful  in  informing  guidance  for  severe
weather  warnings,  including  those  issued
by  the  Met  Office's  impact-based  National
Severe  Weather  Warning  Service  that  goes
out to seven days ahead and is the primary
hazardous  weather  warning  service  for  the
public  and  emergency  responders.

Sting jets in extratropical
cyclones
Extratropical  cyclones  are  a  major  cause  of
hazardous  weather,  mainly  due  to  intense
or  sustained  wind,  rainfall  or  snowfall.  An
extreme  windstorms  catalogue  (Roberts
 et     al.,   2014)  lists  the  insured  losses  for  the
most devastating recent storms, as identified
by insurance experts from Willis Re. The Great
Storm  of  October  1987,  the  first  windstorm
in  which  a  sting  jet  was  formally  identified

(Browning, 2004), is the second most costly of
these with an insured loss of $6.3bn (indexed
to 2012 values). Strong surface winds in extra-
tropical cyclones typically arise from the two
synoptic-scale  low-level  wind  jets  associated
with the so-called warm conveyor belt (WCB)
that  ascends  ahead  of  the  cold  front,  and
the cold conveyor belt (CCB) that wraps rear-
wards around the cyclone (Figure 1). In some
cyclones,  a  transient  (timescale  ∼  several
hours),  smaller-scale  (surface  footprints  typi-
cally <100km wide) feature termed a sting jet
also occurs (e.g. Schultz and Browning (2017)).
Sting  jets  can  lead  to  strong  surface  winds
and  gusts  in  the  dry  air  ahead  of  the  con-
vex  ‘cloud  head’  seen  in  satellite  images  of
extreme  cyclones,  such  as  that  visible  in  the
upper-left quadrant of Figure 3(b).

Sting  jets  have  been  formally  studied  in
more  than  10  cyclones  affecting  Europe

Conditional symmetric instability (CSI)
CSI  release  occurs  when  an  air  parcel  becomes  saturated  in  an  environment  that  is
stable to vertical and horizontal displacement (i.e. gravitationally and inertially stable,
respectively) but not to slantwise displacement. If gravitational or inertial instability are
present, they will be released preferentially to slantwise instability. CSI release leads to
slantwise  motions.  CSI  can  be  considered  as  equivalent  to  the  conditional  instability
that  leads  to  the  familiar  upright  convection  upon  release  but  evaluated  along  slop-
ing surfaces of geostrophic absolute momentum instead of  vertically. It exists where
surfaces  of  geostrophic  absolute  momentum  slope  less  steeply  in  the  vertical  than
surfaces of saturated equivalent potential temperature, a situation that is common in
baroclinic  zones  such  as  fronts  (Glinton  et al.,  2017).

The energy available from CSI release can be quantified using slantwise convective
available  potential  energy  (slantwise  CAPE).  CAPE  is  the  maximum  kinetic  energy
available  to  an  air  parcel  for  (upright)  convection  due  to  latent  heating  from  con-
densation.  Slantwise  CAPE  (SCAPE)  is  equivalent  to  CAPE  diagnosed  along  slanting
surfaces  of  geostrophic  absolute  momentum.  Finally,  downdraught  SCAPE  (DSCAPE)
is  the  maximum  kinetic  energy  available  to  an  air  parcel  descending  along  such
momentum surfaces due to latent cooling from the evaporation of precipitation that
is just sufficient to keep the air parcel saturated. For further explanation of CSI, please
see  Schultz  and  Schumacher  (1999)  or  Clark  and  Gray  (2018).

7
6
,

N
o
.

1
1

369

l
o
o
t

r
o
s
r
u
c
e
r
p
t
e
j
-
g
n
i
t
s
e
m

i
t
-
l
a
e
r
e
p
y
t
o
t
o
r
p
A

1
1

.
o
N

,
6
7

.
l
o
V

,
1
2
0
2

r
e
b
m
e
v
o
N
–
r
e
h
t
a
e
W

Figure 1. Conceptual model of the 3D structure of a Shapiro–Keyser cyclone showing the WCB
(red), CCB (blue) and sting jet (magenta). For each jet, the region of strong surface winds is indi-
cated by the shaded ellipse. (Source: Clark and Gray, 2018.)

(table  2  of  the  review  by  Clark  and  Gray
(2018)), and are suspected to have occurred
in  many  more.  Distinctive  cloud  features
visible  in  satellite  imagery  of  cyclones  can
indicate  a  sting  jet,  but  this  identification
is  only  possible  once  the  cyclone  is  at  the
stage  when  sting  jets  are  about  to  occur
or  actually  occurring.  At  longer  lead  times,
Met  Office  forecasters  subjectively  consider
upper-tropospheric  trough  and  jet-stream
configurations and their potential to lead to
Shapiro–Keyser-type  cyclogenesis  (Shapiro
and Keyser, 1990), as well as high-resolution
convection-permitting  model  output,1  in
considering  sting-jet  threat.  A  challenge  to
forecasters is that operational global forecast
models are currently borderline in their abil-
ity  to  resolve  sting  jets,  in  contrast  to  the
CCB  and  WCB  jets  that  are  well  resolved.
Furthermore,  the  coarser  resolution  of
ensemble operational global forecasts, used
for  probabilistic  forecasts  of  hazards,  is  not
sufficient  to  represent  sting  jets  at  all.  This
limits the ability of forecasters to predict, at
several days lead time, whether a cyclone is
likely to develop a sting jet. Here we describe
the  development  of  a  prototype  real-time
tool  that  Met  Office  forecasters  can  use  to
identify  favourable  conditions  for  sting  jet
occurrence in these ensemble forecasts.

From research diagnostic tool
to operational  implementation
Model horizontal grid spacings of 10–15km
or  less  are  needed  to  resolve  sting  jets
because  they  are  associated  with  the
release  of  mesoscale  instabilities,  such  as
conditional  symmetric  instability  (CSI,  see
text  box),  that  are  only  released  for  suffi-
ciently  high  resolutions.  The  shallow  scale
of  the  descending  sting  jet  also  provides
a  constraint  on  vertical  grid  spacing  of

about  240m  in  the  mid-troposphere  for  a
12km  horizontal  grid  spacing  (Clark  and
Gray,  2018). While  high-resolution  (convec-
tion-permitting) limited domain operational
weather  forecast  models  easily  meet  these
resolution requirements, the global models
needed  for  longer-range  forecasts  struggle
or fail. While the resolution of the Met Office
operational  global  deterministic  model  is
borderline  for  resolving  sting  jets  (10km
horizontal grid spacing and 275–350m ver-
tical  level  spacing2),  the  global  configura-
tion of the operational ensemble (known as
MOGREPS-G) is too coarse (20km horizontal
grid spacing and the same vertical level set).
The presence of a sting jet can only be con-
firmed  in  sting-jet  resolving  model  output
by calculating back trajectories from a pos-
sible  sting-jet  wind  maximum.  Only  then
can  it  be  determined  whether  the  air  has
sting-jet  characteristics  and  has  descended
from  the  cloud  head  tip.

The  failure  of  global  ensemble  weather
forecast,  reanalysis  and  climate  models  to
resolve  sting  jets  indicates  that  determin-
ing their climatological characteristics is not
as  simple  as  diagnosing  them  in  model  or
reanalysis  output.  Instead,  we  have  devel-
oped  an  innovative  and  skilful  method  to
diagnose those cyclones that have a precur-
sor  for,  and  so  are  likely  to  produce,  sting
jets  (Martínez-Alvarado  et  al.,  2013).  There
are  several  mechanisms  attributed  to  sting
jet  formation,  as  synthesised  in  figure  8  of
Clark and Gray (2018). However, the strong-
est sting jets have typically been associated
with  the  release  of  mesoscale  instabilities
such as CSI. The sting-jet precursor diagnos-
tic identifies cyclones that are likely to pro-
duce  sting  jets  by  assessing  the  presence
of  this  type  of  convective  instability  in  an
analogous way to the diagnosis of large val-
ues of convective available potential energy
(CAPE)  as  a  precursor  for  thunderstorm

15-day  convection-permitting  forecasts  from  the
Met  Office’s  UK  variable  resolution  (UKV)  model
are  available  twice-daily.

370

2For  a  mid-latitude  grid  point  at  3–5km  above
sea  level.

development. We quantify the CSI that can
be  released  by  downdraughts  by  calculat-
ing downdraught slantwise CAPE (DSCAPE,
see  text  box).

The precursor diagnostic described above
has previously been applied to multidecadal
ECMWF  ERA-Interim  reanalysis  (ERA-I)  data
and  climate  model  output.  About  a  third
of  North  Atlantic  cyclones  from  ERA-I  were
found  to  have  the  precursor  (indicating
that sting jets are likely to have occurred in
these cyclones) with a higher proportion for
explosively  deepening  cyclones  (Martínez-
Alvarado  et  al.,  2012;  Hart  et  al.,  2017). The
wind risk, diagnosed from ERA-I and the cli-
mate  model  output,  associated  with  sting-
jet precursor cyclones in the current climate
was  enhanced  compared  to  cyclones  with-
out  a  precursor  even  though  sting  jets  are
not  resolved  in  the  models  or  the  reanaly-
sis. This enhancement likely occurs because
cyclones with the precursor tend to be rap-
idly  developing  cyclones  associated  with
strong  frontal  gradients  and  severe  CCB
winds. In reality, the sting jet would further
increase these wind speeds and change the
location of the strongest winds. Hence, the
precursor  provides  a  warning  flag  for  dam-
aging winds irrespective of whether a sting
jet  actually  occurs.

Here we describe the implementation of a
prototype software tool, based on the sting-
jet  precursor  diagnostic,  running  in  near-
real  time  on  output  from  the  operational
MOGREPS-G system and providing forecast-
ers with graphical outputs. The MOGREPS-G
ensemble  is  used  as  it  provides  probabil-
istic  information  from  36  equally  probable
forecasts  created  by  combining  two,  time-
lagged,  18-member  ensembles.  The  com-
position of the project team, two university
researchers  who  led  the  development  of
the  precursor  diagnostic  and  a  researcher
(a  Chief  Operational
and
Meteorologist)  both  from  the  Met  Office,
was  key  to  the  project  success.  The  chal-
lenges  involved  (algorithm  speedup,  algo-
rithm  implementation  and  engagement
with  forecasters)  are  now  described.

forecaster

Algorithm speedup
The  algorithm  to  detect  sting-jet  precursors
in model output follows Martínez-Alvarado et
al. (2012) and comprises three major steps: (1)
tracking extratropical cyclones, (2) extracting
meteorological fields around tracked cyclone
centres and re-gridding them onto a rotated
grid, centred around the cyclone centres, with
a grid spacing of 0.5° × 0.5° and (3) computing
sting-jet  precursors.  Cyclones  with  sufficient
DSCAPE  in  the  cloud  head  are  diagnosed  as
having  a  sting-jet  precursor.  The  bottleneck
is the calculation of DSCAPE in the third step
where  atmospheric  soundings  along  slant-
wise,  descending  surfaces  of  constant  abso-
lute  momentum  are  calculated. To  speed  up

the  calculation  for  operational  implementa-
tion,  we  adapted  an  estimated  formula  that
uses vertical atmospheric soundings to derive
SCAPE (as used in the CSI climatology by Chen
et  al.  (2018))  in  order  to  calculate  DSCAPE.
Comparison  of  precursor  regions  calculated
using  the  slantwise  and  vertical  calculations
found  greater  DSCAPE  magnitudes  from  the
vertical  calculations,  leading  to  an  increased
likelihood of sting-jet precursor diagnosis, but
very  similar  spatial  patterns,  i.e.  DSCAPE  was
diagnosed in the same regions of the tested
cyclones.  The  vertical-calculation  method
was  used  to  predict  sting-jet  precursors
diagnosed  using  the  slantwise-calculation
method  for  130  cyclones  from  9  months  of
climate  model  data.  This  prediction  yielded
hit  and  false  alarm  rates  of  0.925  and  0.312,
respectively,  demonstrating  that  the  two
methods  are  acceptably  consistent  in  their
identification of the precursor.

Algorithm implementation
Porting  the  code  from  the  University  of
Reading  system,  where  it  had  been  devel-
oped,  to  the  Met  Office  required  the  fol-
lowing  steps.  First,  translation  of  parts  of
the  code  from  MATLAB  to  Python.  Second,
ensuring  consistency  between  the  ver-
sions  and  features  of  the  tracking  algo-
rithm  (TRACK  developed  by  Hodges  (1994))
between the University of Reading and Met
Office  versions.  Third,  enhancement  of  the
model  output  fields  to  include  all  fields
required  for  the  diagnostic:  horizontal  wind
components, potential temperature, specific
humidity and non-dimensional (Exner) pres-
sure  on  model  levels,  as  well  as  orography,
mean sea-level pressure and 850hPa relative
vorticity pre-smoothed to T42 resolution (i.e.
truncated  to  total  wavenumber  42,  about
310km  resolution  at  the  equator)  which  is
required  as  an  input  to  the  tracking  algo-
rithm.  Fourth,  implementation  of  scripts  to
move  the  required  outputs  from  the  opera-
tional  forecasts  to  a  separate  location  for
processing  as  soon  as  they  are  available
(typically  10–14  hours  after  the  forecast  is
initiated)  and  before  they  are  automatically
deleted  (about  24  hours  after  generation).
Finally, automation of the sequence of steps
described above. This porting was only possi-
ble through close collaboration and iterative
problem solving between the Met Office and
University  of  Reading  researchers  and  cur-
rently,  at  the  time  of  writing,  the  algorithm
runs on the 18-member MOGREPS-G ensem-
bles initiated daily at 0000 and 1200  utc.

Engagement with forecasters
Met  Office  forecasters  routinely  look  at  vari-
ous model outputs from both the Met Office
and other operational centres to inform their
weather  guidance,  including,  for  example,
diagnosed  cyclone  tracks  from  ensembles,

A
p
r
o
t
o
t
y
p
e
r
e
a
l
-
t
i

m
e
s
t
i
n
g
-
j
e
t
p
r
e
c
u
r
s
o
r

t
o
o
l

W
e
a
t
h
e
r
–
N
o
v
e
m
b
e
r

2
0
2
1
,

V
o
l
.

7
6
,

N
o
.

1
1

Figure 2. Sample graphical sting-jet precursor output for forecasters: 5-day forecast valid at 0000  utc
13 January 2020. (a) Ensemble-based probability of sting-jet precursor for greater than 20 CSI points
(on a 0.5° × 0.5°grid) within 200km (shaded). The CSI points are all within 1000km of a cyclone
centre and constitute sets whose centroids are within 700km of a cyclone centre in the cloud head
sector and with moisture available for the instability to be released. (b) Locations of the centroids of
sets of CSI points (coloured circles); the sizes of the circles are proportional to the number of points
in the set (10–60 grid points within 200km of each centroid). Overlain on both plots are the cyclone
tracks of all the storms identified during the period (dark red lines) and the mean sea-level pressure
(black contours every 5hPa) at the verification time from the control ensemble member. The plus
symbols along the tracks indicate the locations of the cyclone centres at the verification time colour-
coded by ensemble member (with matching colours for the CSI centroids in (b)).

in  addition  to  the  direct  model  outputs.
Chief  Met  Office  Operational  Meteorologist
(and co-author) Dan Suri was involved in the
development  of  the  proposal  that  funded
this  work  and  introduced  the  other  Chief
and  Deputy  Chief  Met  Office  Operational
Meteorologists  to  the  new  sting-jet  precur-
sor  diagnostic.  The  graphical  outputs  show
cyclone tracks and ensemble sting-jet precur-
sor probability in two ways: (i) over the entire
forecast (akin to the strike probabilities often
presented for tropical cyclone forecasts) and
(ii)  as  snapshots  available  throughout  each

forecast (both for a given forecast base time).
The example in Figure 2 shows snapshots of
both the ensemble-based probabilities of the
presence  of  the  sting-jet  precursor  (Figure
2(a))  and  the  precursor  in  individual  mem-
bers (Figure 2(b)). The plots are accessed via
an  internal  Met  Office  web  page,  and  the
domain  and  map  projection  were  selected
to  be  consistent  with  other  images  rou-
tinely  used  by  the  forecasters.  Users  can  flip
between  different  forecast  base  times  and
snapshot  times  and  can  choose  the  mini-
mum size (in 0.5° × 0.5° boxes) of the region

371

l
o
o
t

r
o
s
r
u
c
e
r
p
t
e
j
-
g
n
i
t
s
e
m

i
t
-
l
a
e
r
e
p
y
t
o
t
o
r
p
A

1
1

.
o
N

,
6
7

.
l
o
V

,
1
2
0
2

r
e
b
m
e
v
o
N
–
r
e
h
t
a
e
W

Figure 3. (a) Met Office analysis chart and (b) infra-red satellite imagery at 0000  utc 13 January
2020 with region of cloud banding indicated by the ellipse. Analysis chart is Crown copyright;
satellite imagery is from EUMETSAT (2020).

Figure 4. Sting-jet diagnosis from 18-hour operational deterministic model forecast valid at 0100
utc 13 January 2020: (a) map of 800hPa horizontal wind speed (colour), selected 800hPa wet-bulb
potential temperature contours (blue), 700hPa relative humidity (stippled exceeding 90%) and
mean sea-level pressure (black contours every 4hPa with 960, 980, 1000 and 1020hPa contours
thickened), insert shows a zoom of the region within the black box; (b) vertical cross-section
between A and B marked in (a) and connected by a thin line (30–15°W at 52.4°N) showing the
same fields (except mean sea-level pressure) and with jets labelled; (c) 10m wind gusts with
800hPa wet-bulb potential temperature (as in (a)). The black box in (a) encloses the sting jet and
frontal fracture region and is the region from which back trajectories were calculated, and the
colour bar applies to all three panels.

required to meet the precursor instability cri-
teria  (20,  30  or  40  grid  points  within  200km
from each location on the map). Forecasters
can use the graphical outputs to objectively
assess the potential for winds to be stronger
than  the  model  predicts  due  to  a  sting  jet.
They can then use this assessment alongside
other  diagnostics  and  some  sense  of  cali-
bration  after  experiencing  multiple  events.
This  approach  contrasts  with  the  subjec-
tive  assessment  based  on  the  likelihood  of
Shapiro–Keyser cyclogenesis used previously.

Case example: Storm Brendan
Several  cyclones  impacting  the  United
Kingdom have been flagged by the precur-
sor diagnostic since its routine implementa-
tion. Here we illustrate the behaviour of the

372

diagnostic  in  a  single  case;  detailed  analy-
sis  of  the  characteristics  of  the  precursor
and  its  association  with  extreme  surface
winds  and  gusts  is  left  to  a  future  study.
Although  observational  evidence  for  sting
jets  over  the  ocean  is  usually  limited  to
indicative cloud features in satellite imagery
and,  when  available,  near-surface  winds
from  scatterometers,  short-range  sting-jet
resolving  model  forecasts  can  also  be  used
to  determine  whether  a  sting  jet  occurred
in  a  cyclone.  Strong  winds  associated  with
Storm Brendan affected the United Kingdom
on 13 January 2020. As Brendan approached
northwest Scotland and then turned north-
wards  towards  southern  Iceland,  the  Met
Office  issued  a  yellow  wind  warning  for
northwestern parts of the United Kingdom.
The  strongest  low-level  gusts  were  over

northern  and  western  Scotland  and  often
exceeded 60kn (with a maximum of 76kn at
South Uist (Kendon, 2020)), causing disrup-
tion to transport and power supplies. Storm
Brendan deepened explosively as it crossed
the  North  Atlantic  with  a  24-hour  central
mean sea-level pressure drop of 49hPa from
997hPa at 0600 utc 12 January to 948hPa at
0600 utc 13 January (according to Met Office
analyses).  Cloud  banding  is  visible  within
the  tip  of  the  cloud  head  that  lies  along
the analysed bent-back front at 0000 utc on
13  January  (Figure  3)  and  was  even  more
clearly  evident  at  2100  utc  on  12  January
(not  shown).  Although  analysed  accord-
ing  to  the  Norwegian  conceptual  cyclone
model, a frontal fracture region is evident in
the forecast wet-bulb potential temperature
field  at  this  time  (within  the  black  box  in
Figure  4(a)).  This  fracture  and  the  further
deepening  of  the  storm  indicate  that  the
cyclone is in stage III of evolution according
to  the  Shapiro–Keyser  conceptual  model
(Shapiro and Keyser, 1990), the stage when
sting  jets  typically  occur.

Aided  by  longer-lead  time  forecast  out-
put,  Met  Office  internal  guidance  signalled
the  potential  for  a  deep,  impactful  wind-
storm  to  affect  the  British  Isles  6  or  7 days
in  advance.  Even  at  a  lead  time  of  5 days,
the  ensemble-based  diagnostic  indicated
greater  than  30%  probability  of  a  sting-jet
precursor  existing  to  the  southwest  of  the
cyclone  centre  (i.e.  in  the  tip  of  the  cloud
head)  at  0000  utc  13  January  (Figure  2(a)).
This  high  probability  is  a  consequence  of
strong  agreement  among  the  ensemble
members  in  the  position  of  Storm  Brendan
and the location of its associated precursor
region  (Figure  2(b)).  The  precursor  reveals
suitable  antecedent  conditions  for  sting
jets  in  the  5-day  forecast  valid  at  this  time.
Analysis  of  the  67  equivalent  images  avail-
able  for  5-day  forecasts  from  December
2019–February  2020  reveals  similar  coher-
ent  regions  exceeding  30%  probability
near marine cyclone centres within a North
Atlantic–European  domain  on  8  additional
days  (relating  to  six  cyclones).  Hence,  such
high  probabilities  occur  relatively  infre-
quently.

Some evidence for the existence of a sting
jet  in  reality  comes  from  short-range  oper-
ational  deterministic  model  output:  unlike
the ensemble model configuration, the reso-
lution  of  the  deterministic  configuration  is
borderline for resolving sting jets. The 800hPa
wind speed reveals a small, localised region
of enhanced strength in the frontal fracture
region to the south of the cyclone centre (in
the  box  marked  in  Figure  4(a)).  This  region
is distinct from the WCB jet found ahead of
the  cold  front  and  two  other  small  regions
of  enhanced  winds  found  in  the  colder  air
to the south and southwest of the enhanced
frontal  fracture  winds.  A  short-range  fore-
cast has been analysed so that back trajecto-

ries can be calculated. Back trajectories (not
shown)  from  the  marked  region  indicate  a
coherent set of trajectories that descend by
about  100hPa  over  6  hours  while  acceler-
ating,  drying  slightly  and  conserving  wet-
bulb  potential  temperature  until  the  final
2  hours:  these  trajectories  are  consist-
ent  with  a  weak  sting  jet.  A  cross-section
through the storm (Figure 4(b)) reveals four
distinct  wind  jets:  three  lower-tropospheric
jets  consistent  with  the  CCB,  a  sting  jet  (SJ:
in  the  frontal  fracture  region  with  weak
wet-bulb  potential  temperature  gradients)
and  the  WCB,  and  one  upper-tropospheric
jet  (ULJ)  centred  at  about  400hPa.  While
the  CCB  and WCB  jets  are  entirely  in  cloud
(indicated by the stippling), the sting jet lies
partially in the dry air in the dry slot region
of the cyclone. The sting-jet core exceeding
40ms−1 is at about 800hPa, but strong winds
extend  towards  the  surface  and  are  asso-
ciated  with  enhanced  surface  wind  gusts
that  exceed  those  associated  with  the WCB
(Figure  4(c)).  Satellite-derived  winds  (from
the Advanced Scatterometer, ASCAT, on the
EUMETSAT  METOP  satellite,  not  shown)  are
consistent  with  the  model  forecast,  with
surface  winds  exceeding  55kn  (~28ms−1)
directly  south  of  the  cyclone  centre  in  the
swath  available  from  a  few  hours  prior  to
the  time  shown  in  Figure  4;  however,  the
CCB and SJ cannot be distinguished in these
observations. The sting jet in Storm Brendan
no  longer  existed  when  the  storm  affected
the United Kingdom. However, although the
sting  jet  was  not  the  cause  of  the  damage
in the United Kingdom, the precursor diag-
nostic warned forecasters that a storm with
strong  winds  including  a  possible  sting  jet
could  be  approaching  the  United  Kingdom
5 days ahead. This storm also demonstrated
proof  of  concept  in  a  storm  season  which,
although  active,  did  not  have  many  storms
with  sting-jet  potential.

Outlook
The  behaviour  and  usefulness  to  forecast-
ers  of  the  sting-jet  precursor  diagnostic,
and  the  way  in  which  the  output  is  pre-
sented, needs to be evaluated over a period
including  several  high  impact  storms.  Of
particular  use  will  be  forecaster  evaluation

of  the  most  appropriate  size  to  consider
for the sting-jet precursor region. Once this
evaluation  and  calibration  stage  has  been
completed,  this  diagnostic  will  be  refined
and remain available to the Met Office fore-
casting  community  for  whom  it  will  pro-
vide  an  objective  method  of  identifying
additional  details  of  potentially  damaging
windstorms,  especially  in  the  medium-
range  forecast  period. This  will  aid  a  num-
ber  of  Met  Office  forecasting   efforts  such
as wind warnings across multiple customer
groups,   including  the  National  Severe
Weather Warning Service (Neal et al., 2014)
and  cross-organisational  initiatives  such  as
European  storm  naming.  The  data  gener-
ated are also a potential resource for future
research as some diagnostics are being per-
manently  saved  at  the  Met  Office.

Acknowledgements
The authors gratefully acknowledge the assis-
tance  provided  by  Kevin  Hodges  (University
of Reading) on the use of his cyclone tracking
algorithm  and  Simon Thompson  (Met  Office)
for implementing the additional output fields
required in the operational MOGREPS-G output.
Code  to  calculate  DSCAPE  from  vertical  pro-
files is available from github at https://github.
com/omartineza/csisounding.  Precursor  tool
outputs  and  the  operational  global  forecast
outputs  used  are  archived  at  the  Met  Office.
Please contact the authors for details.

SLG and OM-A were funded by the NERC
(Natural Environment Research Council) UK
Climate  Resilience  programme  (grant  refer-
ence NE/S016384/1). DA is supported by the
Joint  BEIS/Defra  Met  Office  Hadley  Centre
Climate  Programme  (GA01101).

Glinton MR, Gray SL, Chagnon JM et al.
2017. Modulation of precipitation by
conditional symmetric instability release.
Atmos. Res.  185: 186–201.

Hart NCG, Gray SL, Clark PA. 2017. Sting-
jet windstorms over the North Atlantic:
climatology and contribution to extreme
wind risk. J. Clim.  30: 5455–5471.

Hodges KI. 1994. A general method for
tracking analysis and its application to
meteorological data. Mon. Weather Rev.
122: 2573–2586.

Kendon, M. 2020. Storms Atiyah (December
2019) and Brendan (January 2020). https://
www.metoffice.gov.uk/binaries/content/
assets/metofficegovuk/pdf/weather/
learn-about/uk-past-events/interest-
ing/2020/2020_01_storm_brendan.pdf.

Martínez-Alvarado O, Gray SL, Catto
JL et al. 2012. Sting jets in intense winter
North-Atlantic windstorms. Environ. Res.
Lett.  7: 024014

Martínez-Alvarado O, Gray SL, Clark PA
et al. 2013. Objective detection of sting
jets in low-resolution datasets. Meteorol.
Appl.  20: 41–55.

Neal RA, Boyle P, Grahame N et al. 2014.
Ensemble based first guess support towards
a risk-based severe weather warning service.
Meteorol. Appl.  21: 563–577.

Roberts JF, Champion AJ, Dawkins LC
et al. 2014. The XWS open access cata-
logue of extreme European windstorms
from 1979 to 2012. Nat. Hazards Earth Syst.
Sci.  14: 2487–2501.

Schultz DM, Browning KA. 2017. What is
a sting jet? Weather  72: 63–66.

Schultz DM, Schumacher PN. 1999. The use
and misuse of conditional symmetric insta-
bility. Mon. Weather Rev.  127: 2709–2732.

Shapiro MA, Keyser D. 1990. Fronts, jet
streams and the tropopause, in Extratropical
Cyclones. Newton CW, Holopainen EO (eds).
American Meteorological Society: Boston,
MA, pp 167-191.

References

Browning KA. 2004. The sting at the
end of the tail: damaging winds associ-
ated with extratropical cyclones. Q. J. R.
Meteorol. Soc.  130: 375–399.

Chen T-C, Yau MK, Kirshbaum DJ. 2018.
Assessment of conditional symmetric
instability from global reanalysis data. J.
Atmos. Sci.  75: 2425–2443.

Clark PA, Gray SL. 2018. Sting jets in
extratropical cyclones: a review. Q. J. R.
Meteorol. Soc.  144: 943–969.

Correspondence to:  S. L. Gray

s.l.gray@reading.ac.uk

© 2020 The Authors. Weather published by
John Wiley & Sons Ltd on behalf of the Royal
Meteorological Society

This is an open access article under the terms
of the Creative Commons Attribution License,
which permits use, distribution and reproduc-
tion in any medium, provided the original
work is properly cited.

doi: 10.1002/wea.3889

A
p
r
o
t
o
t
y
p
e
r
e
a
l
-
t
i

m
e
s
t
i
n
g
-
j
e
t
p
r
e
c
u
r
s
o
r

t
o
o
l

W
e
a
t
h
e
r
–
N
o
v
e
m
b
e
r

2
0
2
1
,

V
o
l
.

7
6
,

N
o
.

1
1

373

