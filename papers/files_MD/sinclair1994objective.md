--- PAGE 01 ---
Ocroper 1994 SINCLAIR 2239

An Objective Cyclone Climatology for the Southern Hemisphere

Mark R. SINCLAIR
National Institute of Water and Atmospheric Research Ltd., Wellington, New Zealand

(Manuscript received 1 September 1993, in final form 21 December 1993)

ABSTRACT

An objective method is developed and used to derive a climatology of centers of cyclonic vorticity for the
Southern Hemisphere , based on twice-daily European Centre for Medium-Range Weather Forecasts (ECMWF)
1000-hPa analyses during 1980-86. These centers were computed as local minima of geostrophic relative
vorticity C, extending previous studies based on pressure minima. This use of C, avoids a bias favoring slower
and/or deeper cyclones that occurs when pressure is used and includes a large number of additional mobile
vorticity centers in the 45°-55°S band that are missed where a local pressure minimum cannot be found. An
automated tracking algorithm similar to that of Murray and Simmonds is used to match predicted location,
pressure, and ¢, from previous track history with available centers.

Large numbers of €, centers were found south of 60°S and near the midlatitude continents, as in previous
studies. These were a mixture of migratory centers and other fixed topographic features. The maxima around
Antarctica may include many spurious centers that are artifacts of a fictitious surface anticyclone over the elevated
continent. Maxima around East Antarctica were located near katabatic-prone stations. Large counts near the
three midlatitude landmasses were mostly heat lows and lee troughs. These stationary orographic features were
eliminated to retain just the traveling disturbances that dominate the weather and climate of the region. These
mobile centers were distributed much more uniformly. When centers were counted just once per grid square per
cyclone, the resulting ‘‘track density’? maximized year-round in a belt near 50°S rather than within the cyclone
‘*sraveyard’’ of the circumpolar trough, in good agreement with baroclinic storm tracks obtained elsewhere
from eddy statistics. A second maximum associated with the subtropical jet was found during winter and spring
near 40°S in the New Zealand—Pacific sector. Intense cyclones, stratified by ¢,, occurred most frequently in
winter near New Zealand, east of South America, and in the southern Indian Ocean. An apparent increase in
cyclone numbers in early 1983 coincided with the introduction of envelope orography at the ECMWF.

J. Introduction ima of mean sea level (MSL) pressure. Despite limita-
; ee . . tions imposed by lack of data and time-consuming man-
Migratory cyclonic circulation systems and their as- yal techniques, these early results have withstood the test
sociated fronts account for much of the weather in mid- of time. They show maximum cyclone occurrence around
latitudes. These systems occur in preferred geographi- the Antarctic coast, over the midlatitude continents in
cal areas and vary in intensity, frequency, and distri- summer, and over the Andes. The continental maxima
bution during the year. The passage. of cyclones and _ include large numbers of heat lows, lee troughs, and spu-
anticyclones accounts for most of the midlatitude at- joys centers caused by erroneous pressure reduction to
mospheric variability on 2- to 8-day timescales in the ea level (Taljaard 1967). Later, synoptic charts were
upper troposphere (Trenberth 1991). These baroclinic — gypplemented by the subjective evaluation of satellite im-
eddies help to maintain the mean structure of the at- agery (Streten and Troup 1973; Guymer 1978; Carleton
mosphere, which, at the same time, provides a favor- 1979; Le Marshall and Kelly 1981).

able basic state for their growth. Another motivation for determining cyclone clima-
Since cyclones are such an important component of the tology is to assess the performance of numerical mod-
climate, considerable effort has been spent in determining es. Leary (1971) and Silverberg and Bosart (1982)
their spatial and temporal distribution and relating these examined the behavior of cyclones in operational nu-
to the observed general circulation. Early climatologies merical models operated by the National Meteorolog-
for the Southern Hemisphere (SH) were obtained from ical Center (NMC). These studies revealed model bi-
manually prepared charts (Karelsky 1963; van Loon  ases in cyclone intensity, deepening rate, and track. A
1965; Taljaard 1967). Cyclones were identified as min- similar study by Akyildiz (1985) compared errors in
cyclone development and track in the European Centre
for Medium-Range Weather Forecasts (ECMWF)

Corresponding author address: Dr. Mark R. Sinclair, National In- gridpoint and spectral models. . .
stitute of Water and Atmospheric Research, 30 Salamanca Road, The mean distribution, movement, and intensity of
Wellington, New Zealand. cyclones are part of the climatology that should be re-

© 1994 American Meteorological Society

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 02 ---
2240

produced by general circulation models (GCMs). Such
evaluations of GCMs have been performed by Manabe
and Terpstra (1974), Lambert (1988), Le Treut and
Kalnay (1990), and Murray and Simmonds (1991b).
Cyclone climatologies prepared from GCM simula-
tions based on climate change scenarios can reveal pos-
sible regional changes in cyclone occurrence and in-
tensity (e.g., Mullan and Renwick 1990). Simmonds
and Wu (1993) compared the cyclone climatologies of
GCM runs with and without Antarctic sea ice.

Over recent years, the quality of global operational
numerical analyses has improved through advances in
objective data assimilation technology and use of new
data sources like drifting buoys and satellite soundings
(Trenberth and Olson 1988). Accordingly, automated
techniques based on these analyses are superseding
manual methods for obtaining cyclone statistics. One
advantage of numerical finding and tracking over man-
ual methods is repeatability. Greater efficiency enables
longer series of operational analyses to be used to es-
tablish a more definitive climatology. Examples of ob-
jectively prepared climatologies include Lambert
(1988), who produced cyclone occurrence statistics
from a 5-yr run of the Canadian Climate Centre GCM
and compared them with statistics based on ECMWF
analyses; Alpert et al. (1990), who used an objective
method to look at tracks in the Mediterranean area; Le
Treut and Kalnay (1990), who computed global cy-
clone occurrence for two First GARP (Global Atmo-
spheric Research Program) Global Experiment special
observing periods; and Murray and Simmonds
(1991b), who tracked SH cyclones occurring in
a GCM.

Cyclone activity may also be deduced from eddy sta-
tistics. Within this context, the term storm track, first
used by Blackmon et al. (1977), has come to mean an
elongated region of maximum variance of geopotential
height, bandpass filtered to include only fluctuations
with periods less than about a week. Trenberth (1991)
found that storm tracks remained near 50°S year-round
and were strongest in the south Indian Ocean sector.
This is at variance with the traditional cyclone clima-
tologies described earlier, which place the greatest
numbers of SH cyclones near Antarctica and near the
midilatitude landmasses.

Satellite imagery has also been used to measure cy-
clone activity. Cyclonic cloud vortices as observed by
satellite are found to occur throughout the 40°-60°S
latitude band (Streten and Troup 1973; Carleton 1979)
rather than just near the SH continents. These studies
reveal that most developing vortices occur north of
55°S, with mostly mature and dissipating systems pole-
ward of this.

The huge differences between traditional methods
based on pressure minima, and satellite and eddy sta-
tistics, may stem from disparate methods of defining
and counting cyclones. Traditional statistics include
large numbers of heat or orographic troughs near con-

MONTHLY WEATHER REVIEW

VOLUME 122

tinents that do not feature in eddy statistics or satellite
imagery and miss other mobile cyclones for which a
pressure minimum does not exist. A major goal of this
study is to resolve these discrepancies.

In this study, an automated technique is used to de-
termine the spatial and temporal distribution of centers
of cyclonic circulation in the SH from twice-daily anal-
yses from ECMWF during 1980—86. In contrast with
previous climatologies based on pressure minima, local
minima of geostrophic relative vorticity C, computed
from the 1000-hPa geopotential analyses are used. This
has the potential to include additional mobile centers
in the 45°—55°S latitude band for which pressure min-
ima do not exist. Center locations are then formed into
tracks using a method based on Murray and Simmonds
(1991ta, hereafter MS). The scheme selects new track
positions on the basis of continuity of movement and
cyclone intensity. Formation of centers into tracks en-
ables cyclone motion, deepening rates, and preferred
locations of genesis and lysis to be determined.

The finding and tracking methodology is described
in the next section. This will be followed by a presen-
tation and discussion of results in section 3. Section 4
summarizes results and presents conclusions.

2. Methodology
a. Data source and preprocessing

Geopotential at 1000 hPa taken from twice-daily
ECMWE analyses at 0000 and 1200 UTC from 1980
to 1986 were used for this study. An important issue is
the realism of these analyses over the SH. Analysis
quality over the southern oceans has improved to such
an extent that there is now good correspondence on a
day-to-day basis between analyzed ascent and vorticity
features and actual cloud systems and centers of rota-
tion observed in satellite imagery (Sinclair and Cong
1992). These improvements stem from use of aircraft
data, remotely sensed cloud-drift winds, temperature
and moisture soundings, and advances in objective data
assimilation technology. Although analysis uncertainty
still persists, ECMWF analyses are the preferred data-
set for SH studies (Trenberth and Olson 1988).

During the period covered by this study, numerous
changes have been made to the analysis—forecast sys-
tem at ECMWF. These include major changes to the
model itself and its resolution, initialization scheme,
and physical parameterizations (Trenberth and Olson
1988). Probably the change having the greatest impact
occurred in April 1983 when the ECMWF model
changed from a gridpoint model to a spectral model
with envelope orography. This model change led to an
increase in the number of cyclones analyzed near land,
as will be shown later.

The ECMWF data are on a 2.5° X 2.5° latitude—
longitude grid. These were first interpolated onto a 63
Xx 63 polar stereographic grid centered on the South

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 03 ---
OcroBer 1994

Pole in order to avoid problems near the pole where
the east-west grid spacing on the latitude—longitude
grid approaches zero. This computational domain con-
tained the region south of 30°S and had a maximum
grid spacing of 2.66° latitude at the pole. Following
remapping, values were smoothed with a 25-point filter
(Bleck 1965) to remove noise resulting from the inter-
polation. This filter, which uses values two grid inter-
vals away from a given grid point, eliminates noise at
twice the grid spacing with minimal effect at only
slightly longer scales. If not removed, this small-scale
noise would lead to spurious centers of €,. These spu-
rious centers arise because ¢, is related to the Laplacian
of the pressure field, which increases as 1/L?, where L
is the characteristic scale of the pressure perturbations.
This filtering only slightly reduced the magnitude of
the smallest disturbances, with minimal effect other-
wise.

b. Cyclone finding

In this study, centers (minima) of cyclonic ¢, are
used to locate cyclonic disturbances. This has a phys-
ical basis, since the center of rotation is better related
to vorticity than the pressure minimum. Thus, C, cen-
ters should correlate better with vortices seen in satel-
lite imagery. Although the term cyclone is generally
used to denote closed pressure centers, we will use the
term here rather loosely to mean any center of mini-
mum C,. Use of C, also provides a measure of cyclone
intensity, unavailable from pressure alone.

There is, however, a more compelling reason to use
vorticity instead of pressure to locate cyclones. It can
be shown that two important biases occur where pres-
sure minima are used. The problem is illustrated in Fig.
1. In panel (a), the pressure pattern corresponding to
a stationary circular region of cyclonic geostrophic vor-
ticity is shown. When a modest zonal geostrophic wind
is added without changing (,, the local pressure mini-
mum (marked with an ‘*‘L’’) migrates slightly to pole-
ward of the cyclonic ¢, maximum (marked with a
heavy dot in Figs. 1b-d). This is similar to the pole-
ward shift in the position of the Northern Hemisphere
(NH) baroclinic storm track noted by Wallace et al.
(1988) when fluctuations of geopotential are used in
place of the streamfunction to define the storm track.
A strengthening of the westerly component increases
the poleward displacement of the pressure minimum
(Fig. 1c). However, for an even stronger westerly com-
ponent (or a weaker vorticity center), the pressure min-
imum vanishes altogether (Fig. 1d). This final panel is
characteristic of mobile disturbances, especially at
early stages of development.

Figure | shows that use of minimum MSL pressure
to locate cyclones produces a small displacement of the
cyclone position toward lower pressure. This may be
important in studies that relate cyclone locations to fea-
tures of the climatological mean flow (e.g., Trenberth

SINCLAIR

2241

1991). Of greater impact, however, is the tendency to
favor deeper and/or slower-moving systems and to
completely miss many mobile systems where a local
minimum cannot be found (e.g., Fig. Id). For these
mobile cyclones, pressure minima may not appear until
after considerable cyclogenesis and/or slowing has al-
ready occurred. Thus, statistics based on pressure min-
ima tend to be biased toward the main cyclone ‘‘grave-
yards’’ (the circumpolar trough in the SH and the Ice-
landic and Aleutian regions for the NH), where
cyclones are intense and the mean basic flow is weak.
Since cyclonic disturbances in the SH are generally
quite mobile over most of the hemisphere, this bias may
be substantial.
Geostrophic relative vorticity ¢, is computed from
the 1000-hPa geopotential ® as
2,
10 = | a

_if_1 o'@ | 1 0%
Ge =F (acosd)? A? a? Og?

where two small terms, u, tan(@)/a and u, cot(¢)/a,
have been neglected. Equatorward of about 75°, neglect
of these terms generally causes an error of less than 1
x 10~“* s~'. Bicubic splines were used to compute the
derivatives in (1). This use of cubic splines to depict
C. as a smoothly varying surface takes account of the
variation between grid points, enabling extrema to be
located more accurately between grid points, as dis-
cussed by MS. In addition, the second-order derivatives
in (1) are computed with less truncation error than for
finite differences. Where cyclone positions are located
just at grid points (as would occur with a simple com-
parison of grid values), resulting tracks would have a
jerky checkerboard motion.

A ¢, minimum is deemed to be nearby if the value
at a grid point is smaller than any of the four surround-
ing points. A search is then made within each such grid
cell for the more precise location of the minimum,
which is determined to an accuracy of 0.1 times the
grid spacing. This search is made by successive sub-
division of the cel} until the desired accuracy is at-
tained.

One goal of this study is to determine the impact of
using C, in place of pressure. To enable this, locations
of pressure minima were also obtained. A cyclone (de-
fined as above from ¢,) was deemed to be closed if it
was the closest center to a pressure minimum and less
than 5° latitude from it. This designated almost all pres-
sure minima as closed centers but located the center
slightly displaced from the actual pressure minimum.
Cyclone location is thus defined consistently as the lo-
cation of ¢, minima, whereas MS located a cyclone at
the pressure minimum where such a minimum exists,
but at a C, center otherwise.

To be included, ¢, at the center had to be less than
—2 X 10~ s7!. This admitted about 50% more centers
than the ‘‘concavity”’ criterion applied by MS, consis-
tent with the smaller grid spacing used here, since the

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 04 ---
2242

MONTHLY WEATHER REVIEW

VOLUME 122

b 10l2
1006 1008 1010
1004
1006
1004
Cc 1016 ie 1024
1014 — 1020 7
ae ee _
SS E=—SS 1012 | | 1016
—7-~ 1016 { { i012 ——
loos | } 1008 wu
L 1006 | | 1004 —
1004 | } 1000
1002 J > 29986

1000

392

Fic. 1. Mlustration of the relation between C, and pressure for a Cartesian plane in the SH. (a) Pressure,
drawn every 1 hPa, corresponding to a stationary circular region of negative C,. (b) As for (a) but with an
additional irrotational westerly geostrophic flow added. The location of the C, minimum is marked with a
heavy dot, while an ‘‘L’’ marks the pressure minimum. (c) As for (b) but with twice the westerly flow
added. (d) As for (b) but with three times the westerly flow added and a contour interval of 2 hPa. In this

last panel a pressure minimum does not exist.

magnitude of , depends on grid spacing. This thresh-
old for inclusion was made more restrictive (more neg-
ative) over land to reduce the overheads of handling
huge numbers of weak orographic features. First, an
amount z,/300 x 10-5 s7' (z, is terrain elevation in
meters ) was subtracted to reduce the potential impact
of spurious ¢, centers caused by erroneous pressure re-
duction to sea level. Heat lows over land were restricted
during warmer months by subtracting a further 2.0
cos’[max(1.6a, 90)} X 1075s~', where a = |
— 23.5 cos[{2(m — 1)/12]] is the noon solar zenith
angle for month m at latitude @. Despite this filtering,
a large number of orographic features are retained. Fi-
nally, centers were restricted north of 30° to eliminate
spurious weak perturbations in the pressure field in the
tropics unlikely to be associated with migratory cy-
clones.

A map showing all the cyclonic positions found for
one day is shown in Fig. 2. In this figure, there are 14
closed centers (marked with a ‘‘C’’) and 42 open cen-
ters (marked with an ‘‘X’’). These open centers
would be missed in a finding scheme involving just
pressure minima. Details for a smaller area near New
Zealand are shown in Fig. 3. Many of the open centers
have similar €, to the closed center within the trough
just east of New Zealand. Since these open centers are
also associated with strong troughs, it is desirable to
include them in the statistics as well. Note that the
pressure minimum is located south of the associated
vorticity center, similar to the situation depicted in
Fig. lc. Clearly, if the pressure minimum itself were
used to locate closed centers, a track containing a mix-
ture of open and closed centers would tend to be er-
ratic.

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 05 ---
OcTOBER 1994

Fic. 2. MSL pressure, drawn every 10 hPa, for 0000 UTC 1 August
1984. Locations of all the €, minima found are marked. Closed cen-
ters associated with a nearby local pressure minimum are marked
with a ‘‘C,’’ and all others with an ‘‘X.”’

The use of vorticity may have certain disadvantages.
Vorticity extrema are more sensitive to analysis errors,
Also, the method may have a tendency to include elon-
gated geostrophic shear or curvature zones not gener-
ally thought of as cyclones. For example, centers near
40°S, 171°W and 52°S, 171°W in Fig. 3 are part of a
narrow zone of cyclonic vorticity probably containing
a front. However, these frontal zones are frequently a
locus for cyclogenesis.

The finding algorithm saves the cyclone position,
time, center C,, and MSL pressure, and whether the
cyclone is open or closed. These parameters can be
used to determine the geographical distribution of cy-
clones and the annual or secular variation of cyclone
numbers. However, construction of cyclone tracks fur-
ther enables cyclone motion, deepening rates, and lo-
cations of cyclone formation, intensification, and dis-
Sipation to be determined. Cyclone statistics can also
be stratified on the basis of these parameters.

c. Tracking

Cyclone tracking is performed by attempting to
match cyclones at the current time r with centers ob-
tained for the following analysis time t + dr. The al-
gorithm closely follows MS. For each cyclone at the

current time a prediction of the location, pressure, and |

vorticity for a next-track position is made, based on
past motion, pressure, and vorticity tendency. Then, a
match is attempted with each of these predictions from

SINCLAIR

2243

centers actually available at the next analysis time. This
match generally minimizes the position, pressure, and
vorticity departures from the predicted next-track
values.

The estimated position vector for the next-track po-
sition r., is based on a weighted combination of pre-
vious displacement r(t) -- r(t — 26r) and an indepen-
dent estimate of cyclone velocity V,,; that is,

wrlr(t) — r(t — 26t))}
2

+ (1 — Wa) Vavdt. (2)

Here, V,, is the geostrophic wind averaged over 3°, w,,
is a weight less than 1, and r(¢ — 26t) is the position
vector two times ago [except for the third-track point
where only r(t) and r(t — 6t) are available]. This use
of the mean vector motion over the previous two times
smooths the effect of previous erratic motion. Murray
and Simmonds (1991a) use a similar formula [ their Eq.
(10)] except that just the one previous position is used
and their V,, was a climatological steering current. To
start the track from the first-track position, predictions
are made solely on the basis of V,, by setting w,, to
zero in (2). Use here of the basic surface flow to start
the track could be improved by building up a steering
climatology for the dataset by means of successive it-
erations of the scheme, as in MS.

The choice of w,, quantifies the degree of reliance on
past motion. If analyses were available, say, every
hour, w,, would be set close to 1, as tracking based on
past motion would be almost unambiguous. For 12-h
analyses, past motion is not as reliable an indicator of
future motion, and some independent estimate of steer-
ing (V,,) needs to be taken into account. For w,,, the
value 0.6 was used, consistent with the value of 0.36
used by MS for 24-h analyses, raised to the power 12/
24 as suggested by their Eq. (12).

Teg (ft + 6t) = r(t) +

~—\

Fic. 3. As for Fig. 2 except cyclonic ¢,, drawn every 2 x 107° s7!.
MSL pressure drawn every 5 hPa.

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 06 ---
2244

The predicted pressure for the next-track point is

Pea(t + 6t) = p(t) + wolp(t) ~ p(t 68), (3)

as in MS [their Eq. (11)], with w, = 0.55, consistent
with the value of 0.3 used by MS for 24-h analyses.

One refinement to the method of MS is the additional
use here of vorticity predictions:

Con (t + dt) = C(t) + w C(t) — Cr - 6t)], (4)

where w, is 0.55. This requires new-track positions to
exhibit continuity of vorticity in addition to motion and
pressure. Individual pressure and €, maps revealed that
there were sometimes several vorticity centers within a
single complex low pressure area, although at similar
pressure these centers often had widely varying vortic-
ity. Requiring continuity of ¢, by means of (4) helped
to prevent the scheme accepting a center involving an
unrealistic jump in track vorticity.

The values given to the weights w,,, w,, and w, can,
in principle, be revised from the resulting statistics.
These values are consistent with the values used by
MS, who attempted to optimize results by minimizing
the variance of the error (the difference between the
actual and predicted track property ) with respect to the
weights. Murray and Simmonds (1991a) determined
“‘true’’ tracks by extracting GCM results every 3 h over
a 10-day test period. At this output resolution, the as-
sociation of successive positions is almost unambig-
uous. Performance of the tracking scheme at 24-h
resolution. was then evaluated against the 3-h track-
ing. Unfortunately, higher-resolution data, independent
analyses, or satellite imagery were not available for this
study. However, in several trial runs of the scheme,
results were not overly sensitive to small (20%) vari-
ations in these weights.

For each of the cyclones at time f, a search is made
for all candidate next-track positions from all the cen-
ters found at time ¢ + df within a 9° latitude radius circle
from the next-track position predicted by (2). A prob-
ability of association,

8d? + (Sp/1.7)? + (66/0.85)?
9? ,

is ascribed to each of the possible matches. Here, 6d,
ép, and 6€ are, respectively, the distance, pressure, and
vorticity departures of the candidate center from ry,
Pes, and C.. in units of degrees latitude, hectopascals,
and 10~* s~'. The highest match probabilities occur for
candidate centers having location, pressure, and vortic-
ity closest to the predictions Fee, Pex, and Cex. No match
is made where P < 0. Because éd, 6p, and 6 appear
squared in (5), an excessive departure from predicted
in any one of the center properties will greatly reduce
the likelihood of a match. The weights given to ép and
6 mean that a pressure (vorticity) departure of 1.7 hPa
(0.85 X 107° s7') has the same effect as a éd of 1°
latitude. These relative weightings were determined by

P=10- (5)

MONTHLY WEATHER REVIEW

VOLUME 122

estimating average departures for successfully formed
tracks for limited trials. The denominator in (5) re-
quires that P = O when the ‘‘radius of departure’’ in
square brackets exceeds the equivalent of 9° latitude.

Usually, there are several centers at time ¢ that can
match with several candidate next-track positions at
time t + dt. Since each position can be used only once,
a P of 1.0 for a particular match does not guarantee
that association, especially if use of the two positions
involved precludes several other matches. All possible
matches are thus permuted to find the ensemble of
matched pairs having the highest total probability. The
process is described in more detail in MS.

A cyclone at time ¢ for which no match at time ¢ + ét
can be found by this process is deemed to be the end
of a track. Although other candidate centers may be
nearby, they require unrealistic jumps in path, pressure,
or vorticity to be added to the track. Thus, a track may
have only one point. Local variations in cyclone num-
bers from day to day also result in ‘‘orphan’’ centers.
Sometimes, a track may end following a period of cy-
clone intensification because a suitable vorticity center
cannot be found at the next analysis time. Clearly, some
aspect of such an intense cyclone continues, but as a
new cyclone track that starts with large cyclonic vor-
ticity and decays with time. For example, at cyclone
maturity, an original ¢, center may lose its identity,
although the environment remains highly cyclonic. Of-
ten, a new center forms nearby, perhaps as a wave on
the associated front to the north or as a reorganization
within the low pressure area. This new center is not
linked to the previous track by the tracking scheme
because it requires a sudden change in track. Analysis
uncertainty may also interrupt tracks part way through
cyclone evolution. For these reasons, there is no guar-
antee that the first point in each track represents the
position of cyclone formation or of cyclogenesis.

For these reasons, similar studies that assume the
first-track point to be the location of cyclone formation
or cyclogenesis are likely to be in error. Start points
include a mix of true incipient developments with other
more mature centers. In the present method, the (, val-
ues associated with each track point can be used to
determine the locations of formation or cyclogenesis
with more certainty. Use of pressure alone gives no
indication of cyclone intensity.

Figure 4 shows a series of MSL pressure analyses,
with cyclonic C, added, for a typical cyclone as tracked
crossing the south Indian Ocean during September—
October 1984. During the first two times, no pressure
minimum was found, although C, minima were present
at the center of the plot (but were below the threshold
for contouring). Following cyclogenesis, a local pres-
sure minimum appeared in the third panel, disappeared
in the fourth, and then reappeared for the rest of the
sequence. If a cyclone were defined as a pressure min-
imum, the first few stages of this development would
have been missed. Had this mobile cyclone remained

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 07 ---
OcroBer 1994

122 FRI 28-SEP-84
WSL press (hPo)

00Z SAT 29-SEP-84
USL press {hPo)

Radius = 12
4358 25.56

Radius = 12
4845 37,5E

2Z SUN 30-SEP-34
MSL press (hPa)

002 MON 01-OCT-84
WSL press (hPo)

Radius = 12
49S 82.96

Radius = 12
49.35 93.66

SENCLAIR

2245

00Z SUN 30-SEP~84
MSL press (hPa)
—

j2Z SAT 29-SEP-84
WSL press (hPo)

Radius = 12
4TAS GLE

Radius = 12
48.45 52.46

002 TUE 02~0CT-84
WSL press (hPo)

12Z WON 01-OCT-84
MSL press (hPa)

Radius = 12
52.78 105.9

Radius = 12
58.95 12.68

Fic. 4. Development of a cyclone in the southern Indian Ocean between 1200 UTC 28 September and 0000 UTC 2 October 1984.
MSL pressure (solid) is drawn every 5 hPa, with cyclonic €, (dashed) every 5 X 10-> s~! added.

weak, it may have been missed altogether. By identi-
fying cyclones at an early stage of development, gen-
esis locations are more accurately determined.

Cyclone tracks, 1984, Mnth:Sep, mov.>30

<2 | Tex: 3 wused=58 Bos: sel: sseoucecesl

Fic. 5. Cyclone tracks for all cyclones moving a distance greater
than 30° of latitude during September 1984. Dots are drawn at cy-
clone locations every 12 h.

Cyclone tracks computed for all cyclones moving a
distance greater than 30° of latitude (about 3330 km)
during September 1984 are shown in Fig. 5. From this
very small subset of the 7-yr dataset, it is apparent that
most cyclones move toward the east or southeast. Al-
though the tracking tries to minimize abrupt changes,
erratic cyclone motion still sometimes occurs. This may
indicate natural variability due to transient influences
of nearby systems, or it may reflect analysis uncertainty
or deficiencies in the tracking algorithm.

d. Measures of cyclone occurrence

Two measures of cyclone occurrence are used in this
study. Cyclone density is defined as the number of C,
centers per unit area. This simply counts the number of
centers falling within a 5° latitude radius circle centered
on each grid point, so it does not require cyclone po-
sitions to be formed into tracks. When a large number
of cyclones from several years are considered, cyclone
density becomes proportional to the time a given point
can be expected to be under cyclonic influence. As
such, it may be related to other meteorological param-
eters associated with cyclones, such as cloudiness or
rainfall.

Over the computational domain, which is the region
poleward of 30°S, grid points are spaced between about
2.0° and 2.66° latitude apart. Thus, a given cyclone may
be counted at several adjacent grid points within the 5°
circle, resulting in some smoothing of patterns. This

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 08 ---
2246

MONTHLY WEATHER REVIEW

VOLUME 122

Cyclone density (F per 5 box}, 1980-1986, Nnths:DJF

d=13785 x 2,used=46472

Cyclone density (f per 5° box), 1980-1986, Mnths:JJA

Fic. 6. Cyclone density for all cyclones for (a) December, January, and February, and (b) June, July, and August for 1980-86. Cyclones
are counted as numbers of centers per 5° latitude radius circle. The contour interval is 100, with light (medium) shading for counts greater

than 400 (600).

averaging ensures continuity of patterns in poorly rep-
resented areas and reduces noise. Interpolation of track
points to 6-h spacing was an option to ensure that fas-
ter-moving cyclones were counted at all grid points be-
_ tween their 12-h positions. When time. interpolation
was used, counts Were normalized to 12-h values for
contouring.

This use of circular averaging geometry avoids the
problems associated with counting cyclones in rectan-
gular latitude—longitude boxes, as is done in virtually
all previous studies. According to Taylor (1986), even
when the resulting statistics are corrected for the lati-
tudinal change in box area, such counts retain bias in
favor of certain directions. The use of time interpola-
tion further reduces a bias against. faster-moving
storms. ,

A second measure of cyclone occurrence, here called
track density, measures the number of cyclones passing
within a certain distance (5° latitude) of a given point.
Here, a counter is incremented at each grid point lying
in the path of a cyclone. This requires cyclones to be
formed into tracks. The path of the cyclone is defined
to be the area swept out by the 10° wide ribbon centered
on the track. To obtain such a path of near-constant
width, time interpolation is usually required. This mea-
sure differs from cyclone density in that only one count
can be made per grid point pér cyclone track, thus re-
ducing the counts for slow-moving systems. When
computed for a large number of cyclones over a long
time period, this statistic becomes proportional to the

long-term probability that a cyclone will pass within 5°
of a given point. For a smaller averaging domain, pat-
terns become noisy, especially in poorly represented
areas, Presumably, for longer data series, narrower rib-
bons could be considered.

e. Mean cyclone motion

Since cyclones are formed into tracks, it is possible
to compute the mean vector translation velocity at each
grid point for tracks having more than one point. These
velocities were computed from the coordinates of the
track points using centered time differencing.

f. Stratification of cyclones

Since the MSL pressure and C, for each track point
is saved, cyclone statistics can be stratified by intensity
(as measured by either pressure or vorticity), intensi-
fication rate, or length of track. In addition, statistics
based on just certain portions of a track can be com-
piled. Some of these stratifications will be illustrated in
the following section.

3. Results

a. Mean overall cyclone density

For the 7 years, an- overall total of 210 005 centers
of cyclonic vorticity were ‘found from the twice-daily
ECMWF analyses. This represents an average of 41

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 09 ---
OcTOBER 1994

SINCLAIR

2247

Mean motion (ms”), 80-86, Mnths:DUF, 6h interp

~ ose , AY

Ry YY VIN S/S YN

sel Trx=13785Pes=46472 used Trx=8409,Pos=75583 )

Mean motion {ms"), 80-86, Mnths:JJA, 6h interp
~~ NS

NCS

gel: | Trx=2067

Pos=57723_uned:\ Trx=i1248,Pos=85350,

Fic. 7. Average motion vectors for the centers in Fig. 6. The magnitude of these mean vectors,
drawn every 5 m s—' is added, with values greater than 10 and 15 ms~' shaded.

centers per analysis over the domain. The distribution
of these cyclones during two seasons, summer and win-
ter, is shown in Fig. 6. This reveals maxima of cyclone
occurrence near the three continental landmasses
around Antarctica and in the New Zealand region.
Overall, the largest numbers of cyclones were found
during the winter period when 57 723 centers were
found (45 per analysis), compared with just 46 472 (37
per analysis) for the summer period.

The maxima over the three midlatitude SH land-
masses dominate the statistics during both seasons. The
summer maxima over Australia (Fig. 6a) have no
counterpart in winter (Fig. 6b), suggesting these to be
largely heat lows. However, the twin maxima over Af-
rica and the Andes appear during both summer and
winter. This year-round occurrence and the fact that
these maxima straddle elevated terrain suggests that lee
troughs within alternating easterlies and westerlies may
contribute to these maxima. Murray and Simmonds
(1991a) attribute a similar cyclone distribution over
South America to unrealistic reduction of pressure to
sea level from stations at high elevation over the Andes.

Seven extrema of cyclone occurrence around Ant-
arctica occur within the two Antarctic embayments,
near 30°, 75°, 115°, and 155°E, and a broader maximum
west of the Antarctic Peninsula. These seven maxima,
also noted in previous studies (Lambert 1988; Taljaard
1967), persist during both seasons but with greatest
numbers in winter (Fig. 6b). Additional winter maxima
extend along 40°S across New Zealand into the Pacific,
in the south Indian Ocean near 45°—50°S, and southeast

of South America. Minimum cyclone occurrence is
found in winter in a broad region near 50°S to the south
of New Zealand. Another feature, previously noted by
Taljaard (1967), is the relative infrequency of cyclones
near 40°S off the east coast of South America.

The results in Fig. 6, based on modern numerical
analyses incorporating much remotely sensed data over
the southern oceans, are similar to those from previous
studies based on manual analyses (Taljaard 1967; van
Loon et al. 1972). Despite a lack of data, these early
results have withstood the test of time. Figure 6 is also
similar to results from more recent studies based on
numerical analyses (Lambert 1988; Murray and Sim-
monds 1991b). However, Fig. 6 exhibits a much higher
relative occurrence at lower latitudes than these pre-
vious studies based on pressure minima. For example,
winter cyclone counts in Fig. 6b near New Zealand are
about 70% of those around Antarctica, whereas the cor-
responding fractions in Murray and Simmonds’s
(1991b) Fig. 2b and Lambert’s (1988) Fig. 3 are less
than about 25%. A winter maximum near 47°S in the
southern Indian Ocean (Fig. 6b) is also absent in pre-
vious studies. This shift toward lower latitudes largely
stems from use of ¢, in place of minimum pressure, as
will be shown.

Mean cyclone motion (Fig. 7) is toward the east,
with a small poleward component in lower latitudes of
the Pacific and south of Australasia. Mean translation
speed is greatest near 50°S, exceeding 15 m 57! in the
south Indian Ocean year-round. Cyclone mobility in-
creases in winter (Fig. 7b), especially northeast of New

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 10 ---
2248

Cyclone density ( per 5° box), 1980-1986

MONTHLY WEATHER REVIEW

VOLUME 122

Grography_(m)_

Meon MSL pressure for 1984 (hPa)

Ld 1000 Ns
4010
990 80s N
980
990 70S
1000
&
4 Zz

1020 $90.

1010

Ug:

990

990 : -
1000
NN 1000 ~~ 990 5 4

Fic. 8..Variations in cyclones around Antarctica. (a) Cyclone density for all months during 1980—86, drawn every 500 per 5° circle,

(b) orography, z, every 500 m; (c) V7z,, every 5 X 107" m

Zealand. Figure 7 broadly resembles mean flow pat-
terns in the midtroposphere [cf. Figs. 5.2 and 5.3 in van
Loon et al. (1972)]. Finally, the mean translation speed
associated with the very high cyclone densities near
Antarctica and over the three midlatitude continents is
close to zero. This supports the earlier assertion that
many of the ‘‘cyclones’’ that dominate the mean sta-
tistics in Fig. 6 are stationary features caused by sum-
mer heating and other orographic effects.

~?; and (d) average MSL pressure, every 5 hPa, for 1984.

b. The maxima near Antarctica

Although the seven regions of maximum cyclone
frequency around Antarctica in Fig. 6 also dominate
previous SH cyclone climatologies, no explanation has
ever been offered. We propose several factors that may
explain these maxima.

Figure 8a shows these maxima in more detail. Those
around East Antarctica occur near 30°, 75°, 115°, and

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 11 ---
OctToBER 1994

155°E, about 10°—20° of longitude east of the coastal
stations Novolazarevskaya (70°46'S, 11°49’E), Maw-
son (67°36'S, 62°53'E), Mirny (66°33'S, 93°01'E),
and Dumont D’ Urville (66°42’S, 140°00’E), respec-
tively. Each of these stations is prone to strong kata-
batic winds (Mather and Miller 1966), resulting in a
high frequency of southeast gales (Schwerdtfeger
1970). As these katabatic events are often localized,
they do not always imply a commensurate pressure gra-
dient. The frequent placement of a low nearby to ac-
count for these winds may contribute to the four cy-
clone density maxima in Fig. 8a.

The high-latitude variability of cyclone density in
Fig. 8a is related to the topography of the Antarctic
landmass (Fig. 8b). Taljaard (1967) observed that
maximum (minimum) cyclone numbers occurred near
embayments (promontories ) in the Antarctic coastline
but he did not offer any explanation. It has been sug-
gested that confluence zones within the persistent Ant-
arctic katabatic wind regime contribute to cyclogenesis
in these regions (Carleton 1992). These zones of max-
imum katabatic wind strength occur near the western
edge of topographic embayments (Parish 1988). Ka-
tabatic winds have been implicated in mesoscale cy-
clogenesis off the coast (Bromwich 1991). Numerical
simulations by Parish (1992) show that where these
wind maxima reach relatively warm open water, dia-
batic heating contributes to low-level depressions (see
his Fig. 10d) at precisely the seven locations of cyclone
maxima in Fig. 8a. The persistent wind maxima also
help to open polynyas (Kurtz and Bromwich 1983) that
maintain heat and moisture to cyclones in these regions.
Mechoso (1980) also suggests that the slopes of the
Antarctic plateau can be a locus for cyclogenesis.

There is a striking resemblance between the cyclone
variations in Fig. 8a and the positive Laplacian of to-
pographic height around Antarctica (Fig. 8c). This
may reflect the similarity between average MSL pres-
sure (Fig. 8d) and Antarctic topography (Fig. 8b). This
similarity exists because the strength of the surface in-
version is a strong function of height (Schwerdtfeger
1970), meaning lower temperatures are used to reduce
surface pressure to sea level over the inland plateau.
Because pressure reduction to sea level is meaningless
over the polar plateau, this inland anticyclone is fic-
tional. Thus, many of the C, minima in the equally fic-
tional geostrophic flow around this high may be spu-
rious.

c. Removal of cyclones caused by local orographic
effects

It has been suggested above that a large number of
the cyclonic centers included in Fig. 6 and in previous
cyclone studies are the result of local orographic ef-
fects. Near Antarctica, these effects include strong ka-
tabatic winds and erroneous pressure reductions to sea
level, whereas summer continental heating and lee
troughing effects are important in midlatitudes.

SINCLAIR

2249

Although these orographic features dominate the cy-
clone statistics in Fig. 6, their contribution to the
weather and climate is likely to be small. Midlatitude
heat lows and lee troughs have limited vertical extent
and are not associated with deep cloud or precipitation.
Occasionally, these features develop into deeper cy-
clones and move offshore, forming part of the track of
a more mobile system. Similarly, the katabatic winds
and the intense continental anticyclone on which the
maxima around Antarctica depend are confined to lay-
ers nearest the surface (Mather and Miller 1967).

Since the cyclone centers resulting from orographic
effects are largely fixed in relation to topography, their
contribution to the statistics may be reduced by just
including centers that exhibit-some mobility. Accord-
ingly, cyclones moving a total distance less than 10°
latitude were eliminated from the statistics. The cy-
clones so rejected (shown in Fig. 9) represent close to
50% of the total cyclones in Fig. 6. Figure 9 shows that
this mobility test mostly removes cyclones from the
continental and Antarctic regions discussed above, as
well as a few from other oceanic regions. Rejected cy-
clones away from land may represent truly stationary
systems, although it is rare for an oceanic cyclone to
go through the stages of genesis, development, and dis-
sipation without some net displacement. More likely,
the nonmobile oceanic cyclones in Fig. 9 are ephemeral
cyclones or centers that could not be fitted into tracks.
This last group probably includes centers that are ‘‘or-
phaned’’ by day-to-day variations in cyclone numbers
and/or by analysis uncertainty.

Any attempt to draw meaningful boundaries between
mobile weather-producing cyclones and centers result-
ing solely from shallow orographic effects is admit-
tedly arbitrary. It is likely that a few of the ephemeral
or slower-moving systems eliminated (Fig. 9) repre-
sent genuine cyclones. However, although the rejected
cyclones in Fig. 9 constitute about half of all cyclones
found, their elimination is justified by noting that their
distribution in Fig. 9 bears little relationship to the
baroclinic storm tracks or associated midtroposphere
eddy transports computed by Trenberth (1991) and
others. .

It is important to realize that this mobility require-
ment does not exclude cyclones that are stationary dur-
ing even a major part of their life. For example, slow-
moving cyclones near the Antarctic coast are included
where they are the final stages of cyclones that have
formed and deepened in midlatitudes, as is commonly
the case (van Loon et al. 1972). Likewise, lee cyclones
that eventually move offshore are also included.

d. Cyclone density for mobile cyclones

After eliminating nonmobile centers, a total of
42 452 centers (actual plus interpolated) were found
for summer, with 50772 for winter. This equates to
about 17 centers per analysis for summer and 20 for

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 12 ---
2250

Cyclone density ({ per 5 box), 1980-1986, Mnths:DUF, mov.<i0

MONTHLY WEATHER REVIEW

VOLUME 122

eda¥0679 a 2,used=2 3693)

Trxt_sel=)3783

Cyclone density (f per 5° box), 1980-1986, Mnths:JJA, mov.<10

y |. 405

“a

Soe

074)
Gh
ye

ie
2)

we

5 269
ask wt 400\\ :
Js ANS) aa

Fic. 9. As for Fig. 6 except for cyclones moving a total distance less than 10° of latitude. The contour interval is 100.

winter. Because cyclones moving faster than 13 m s7!

traverse more than 5° latitude in 12 h, 6-h time inter-
polation was used and the resulting counts halved. This
improved the coherence of patterns a little and slightly
increased the counts within the belt of greatest cyclone
mobility near 50°S.

Results (Fig. 10) show a much more uniform dis-
tribution of cyclones around the hemisphere compared

with Fig. 6. Maxima over the continents and near Ant-
arctica are almost eliminated, confirming these to be
hear-stationary topographic features. The more uni-
form distribution in the Antarctic region results from
the virtual elimination of the seven high-latitude max-
ima there. .

In summer (Fig. 10a), maximum cyclone density is
found between about 50° and 65°S. Maxima over west-

Cyclone density (f per 5' box), 1980~1986, Mnths:DUF, mov.>10, 6h interp

BS used=3106_Pos:\sel=79(59,used=42482)

Cyclone density (# per 5 box), 1980-1986, Mnths:WJA, mov.>10, 6h interp

Fic. 10. As for Fig. 6 except for cyclones moving a total distance greater than 10° of latitude. Six-hour time interpolation is used.
The contour interval is 50, and values greater than 200 (250) are shaded (heavily).

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 13 ---
OcTOBER 1994

ern Australia and South America are composed of heat
lows and orographic troughs not expunged by the mo-
bility requirement, as these vanished when a 20° net
displacement was required, although at considerable
expense of cyclone counts elsewhere. North of 40°S,
highest summer cyclone counts are found in the Tas-
man Sea, near 150°W, east of South America and east
of Madagascar. Regions west of the three continents
show minimum cyclone occurrence. The local maxi-
mum north of New Zealand contains many warm-cored
systems of tropical origin, which maximize in that re-
gion (Streten and Troup 1973).

During winter (Fig. 10b), more cyclones appear at
lower latitudes. In the Pacific sector, the zone of great-
est cyclone occurrence splits into two bands——one near
40°S, and the other near 65°S—separated by a zone of
minimum cyclone occurrence southeast of New Zea-
land. In the southeast Indian Ocean, uniformly high
cyclone counts are found in a broad zone south of 40°S.

e. Comparison with statistics of closed centers

Statistics for closed centers (centers involving pres-
sure minima) were also computed. Only 68 170 (or
about 32%) of the 210 005 centers found during the 7-
yt period were found to be closed. Hence, our use of
€, in place of pressure minima has resulted in a three-
fold increase in the number of cyclones included.

The distribution of closed centers (Fig. 11) is
skewed toward high latitudes in comparison with Fig.
10. For example, the winter cyclone density (Fig. 11b)
in the southeast Indian Ocean decreases rapidly from

: Cyclone density (# per 5 box), 1980-1986, Mnths:DJF, closed, mov.>10, 6h interp

SINCLAIR

2251

more than 120 centers per 5° circle near 58°S to less
than 60 near 40°S. This contrasts with almost no me-
ridional decrease in cyclone density for the same region
in Fig. 10b. Although more ¢, centers occur overall in
winter (Fig. 10b) than in summer (Fig. 10a), the num-
ber of closed centers is largest in summer (Fig. 11b),
consistent with the decreased warm-season cyclone
mobility (Fig. 7).

Figure 12 shows the distribution of open centers.
These constitute 68% of the €, centers in Fig. 10 and
represent traveling disturbances that would be omitted
in climatologies based solely on minimum pressure
(e.g., Fig. 11}. Numbers of these open centers gener-
ally maximize in regions of greatest cyclone mobility
about and north of 50°S (cf. Fig. 7), where the stronger
mean flow requires a larger perturbation to form a
closed streamline. It is these additional open centers
that tend to shift the cyclone distribution equatorward
when , is used.

f. Distribution of intense cyclones

The distribution of cyclones having a central vor-
ticity less than —15 X 107° s~' is shown in Fig. 13.
The frequency of these intense cyclones is greatest
during winter (Fig. 13b), maximizing in the Tasman
Sea and near 40°S over the South Atlantic Ocean.
Other maxima occur east of New Zealand and
throughout the Indian Ocean sector. High counts over
South America are possible artifacts of erroneous
pressure reductions to sea level over the Andes as sug-
gested by MS, as they vanish here when the mobility

k C ) 40 =

Cyclone density (# per S' box), 1980-1986, Mnths:JA, closed, mov.>10, Sh interp

40

v7

Tre: sel=206 §=3822 Pos:

74,used=17 229)

Fic. 11. As for Fig. 10 except for closed centers. The contour interval is 20, and values greater than 80 (120) are shaded (heavily).

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 14 ---
2252

MONTHLY WEATHER REVIEW

VOLUME 122

Cyclone density (f per 5° box), 1980-1986, Mnths:DJF, open, mov.>10

ny OX

On SS
(LL
- ae J}
Lg C
ay ~ Trfs_sel=137B5 ure 5006 Pos:\sein46472,used=13376!

Cyclone_density (# per 5° box}, 1980-1986, Mnths:JJA, open, mov.>10

Fic. 12. As for Fig. 10 except for cyclones not associated with a local pressure minimum. The contour interval is 50,
; and values greater than 150 (200) are shaded (heavily).

requirement is increased to 20° of translation. Also,
they have no counterpart in satellite-based climatol-
ogies (e.g., Carleton 1979) or eddy studies (Trenberth
1991). During summer (Fig. 13a), intense storms
chiefly occur southeast of South America and in the
south Indian Ocean.

g. Cyclone track density—Annual variation

Cyclone track densities for mobile cyclones for the
four seasons are shown in Fig. 14. Here, cyclone track
density is a measure of the number of cyclones passing
within 5° latitude of each grid box. Greatest track den-
sity occurs in a well-defined midlatitude belt near 50°S,
a northward shift from the corresponding cyclone den-
. sity maximum (Fig. 10). This shift is caused by count-
ing slower-moving centers only once per grid point,
reducing the relative counts for slower-moving systems
within the circumpolar trough.

The summer pattern (Fig. 14a) shows a single zone
of maximum track density centered fairly uniformly
near 50°-55°S, in reasonable agreement with Tren-
berth’s January 300-hPa s(z) (his Fig. 6). Trenberth’s
stronger southern Indian Ocean maximum is consistent
with the high frequency of strong cyclones there (Fig.
13a), which contribute larger geopotential fluctuations
to s(z). North of 40°S, cyclones occur more frequently

east of South America and in the Pacific near 150°W. -

Reduced cyclone occurrence is observed west of the
three continental landmasses, especially South Amer-
ica. Some of these longitudinal variations probably re-

flect the role of ocean currents, as warmer (cooler) con-
ditions prevail east (west) of these continents.

During the autumn months (Fig. 14b), there is a sub-
stantial increase in track density north of 40°S in the
Pacific sector. There is also an increase in overall num-
bers of mobile cyclones, from 3108 tracked cyclones
during summer to 3932 during autumn. However, the
maximum track density remains near 50°—55°S.

The most marked changes are apparent during the
winter months (Fig. 14c). Cyclone numbers peak to a
3-month total of 4720 cyclones tracked. In the Pacific
sector, there is a well-defined split in the track density,
with one branch extending eastward along 40°-—45°S
from near New Zealand to South America, and another
high-latitude branch just’ south of 60°S. These two
branches are related to the double-jet structure east of
Australia. On average, the subtropical jet (STJ) extends
near 30°S across Australia and the southwest Pacific,
while the polar jet maximizes near 60°S (van Loon et
al. 1972). Between these two systems, there is a pro-
nounced 200-hPa isotach minimum near 50°S south of
New Zealand. Storm tracks are closely linked with
these features, mostly via jet-related baroclinity (Tren-
berth 1991). While maximum cyclone occurrence in
both Figs. 10b and 14c is located near the polar jet, it
is about 10° south of the STJ in the Pacific sector. Pa-:
cific cyclones are either associated with transient pole-
ward excursions of the STJ or are persistently located
well to the south of that jet.

In spring (Fig. 14c), cyclone numbers (4279) are only
slightly less than in winter. There is still a hint of the 40°S

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 15 ---
OCTOBER 1994

SINCLAIR

2253

Cyctone density (f per 5° box), 1980-1986, Nnths:DJFM, mov.>10, 6h interp, ¢<-15

9073;d5ed2277 Pox sel=196479,used=934)

track density maximum just east of New Zealand, con-
sistent with persistence of the STJ into September (Tren-
berth 1991). Another relative maximum over the south-
em Australia coast is probably due to a baroclinic zone
that forms along this coast from differential diabatic heat-
ing between the southern oceans, which are at their
coldest during spring, and the rapid spring warm-up of
the Australian landmass. This maximum does not appear
at any other time of year. There is a hint of a simmlar but
weaker relative maximum over southern Africa.

Despite these seasonal variations, the frequency and
distribution of SH cyclones remain remarkably uniform
during the year when compared with cyclones in the
NH. There, cyclones exhibit huge regional variations
caused by land—sea differences (Petterssen 1956),
with activity weakening and shifting poleward during
the northern summer (Whittaker and Horn 1983). In
contrast, Fig. 14 reveals much greater zonal symmetry
for the SH, with minimal latitudinal shift in track den-
sity maxima through the seasons (apart from the ap-
pearance of the South Pacific split in winter). Further-
more, cyclone numbers (Fig. 15) for the regions south
of 45°S comprising most of the cyclones exhibit little
annual variation. These results are consistent with
Trenberth (1991), who concluded that storm track ac-
tivity was remarkably uniform throughout the year.

North of 45°S, SH cyclone numbers (thick line in Fig.
15) in winter are almost double those in summer. This
broad winter maximum persists from May through to Oc-
tober, consistent with the presence and duration of the

Cyclone density (# per 5° box), 1980-1986, Mnths:JJAS, mov.>10, Gh interp, ¢<-15

3,0s60=588 ‘o 77 ,used=2035}

(t

Fic. 13. Cyclone density for cyclones having central ¢, < —15 X 107*s7' for (a) December, January, February, and March, and (b)
June, July, August, and September for 1980~86 for cyclones moving a total distance greater than 10° of latitude. Six-hour interpolation is
used. The contour interval is 5, with values greater than 10 (20) shaded (heavily).

STJ and increased meridional temperature gradient at
these latitudes (Trenberth 1991). A smaller, additional
spring maximum in cyclone activity is evident south
of 60°S.

h. Secular trends

The trend in cyclone numbers during the 7-yr period
studied is depicted in Fig. 16. A notable feature of this
plot is the sudden increase in total cyclone numbers
(top curve) during early 1983. This coincides with a
change in the ECMWF model from a 15-level 1.875°
grid point to a 16-level T63 spectral model with en-
velope orography. This change occurred in April 1983.
These and other changes to the ECMWF model are
discussed by Trenberth and Olson (1988).

The sudden increase in cyclone numbers during
1983 is confined to cyclones moving a distance less
than 20° latitude (middle curve in Fig. 16). These in-
clude many quasi-stationary orographic features, which
have a marked winter—spring peak, despite being offset
by summer heat lows (see Fig. 9). This corresponds
with the increased strength and extent of the westerlies,
leading to a greater incidence of lee troughing. Their
sudden increase during 1983 is probably due to the ef-
fective increase in the height of the orography used by
the ECMWF model when envelope orography was in-
troduced. This would enhance the frequency and inten-
sity of lee troughs and other orographic phenomena.

In contrast, very little change occurs in the numbers
of remaining mobile cyclones (bottom curve in Fig.

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 16 ---
2254

MONTHLY WEATHER REVIEW

VOLUME 122

Track density (# passing < 5), 1980-1986, Mnths:DJF, mov.>10, 6h interp

5 Track density (f possing < 5), 1980-1986, Mnths:MAM, mov.>t0, 6h interp

x: sel=13785 used=3108 ‘a 9 used=42452)

ae p
2B2ustd=5932 un

5 Track density (# passing < 5), 1980-1986, Mnths:JJA, mov.>10, 6h interp

oy Track density (# passing < 5°), 1980-1986, Nnths:SON, mov.>10, 6h interp

2 sela177.

o0=4278 Pos:\ selmB9964 used=50481)

Fic. 14. Cyclone track density for (a) December, January, and February; (b) March, April, and May; (c) June, July, and August;
and (d) September, October, and November, for cyclones moving a total distance greater than 10° of latitude.

16). These have a much smaller annual cycle in com-

parison with the top two curves, with only a very slight —

overall increase in cyclone numbers during the 7-yr
period studied. oo
4, Summary and conclusions

An automated method has been described and used
to determine the frequency and location of centers of

cyclonic vorticity in the SH from a 7-yr sequence of
twice-daily ECMWF 1000-hPa analyses. This use of
local €, minima differs from previous cyclone clima-
tologies based on pressure minima that tend to favor
slow-moving or more intense systems. It was shown
that use of €, added large numbers of mobile vortices
in the 45°—55°S band for which pressure minima did
not exist, and generally identifies cyclones at an earlier
stage.

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 17 ---
Ocroper 1994

Cyclone numbers, 1980-1986, mov > 10

SINCLAIR

4000

3500 F 008

3000 F

2500 F
WH45

2000 F
60~805

Ly

{500

Number of cyclones

4000

T

500 F

Month

Fic. 15. Annual variation of cyclone numbers (per month) in three
latitude bands for cyclones moving a total distance greater than 10°
of latitude.

Simple counts of ¢, minima were dominated by max-
ima of cyclone occurrence around Antarctica and near
the midlatitude continents, in substantial agreement
with previous studies. However, relatively more counts
were found at lower latitudes as a consequence of using
¢, in place of pressure. The ‘‘cyclones’’ constituting
the continental maxima that dominated the statistics
were found to have near-zero mean motion, suggesting
a topographic origin. These quasi-stationary orographic
features composed around half of all centers. Maxima
near South America, Africa, and Australia were com-
posed of large numbers of stationary heat lows and lee
troughs.

Variations in cyclone density around Antarctica
were found to be correlated with the Laplacian of ter-
rain height. This raises suspicions that many of the sea
level centers found near Antarctica here and in previous
studies are artifacts of a fictitious MSL anticyclone over
the elevated continent that tends to resemble the topo-
graphic height. The maxima around Antarctica also oc-
cur near katabatic wind confluences, often implicated
in cyclogenesis (Carleton 1992).

A major conclusion from this study is that many of
the cyclones found here (e.g., Fig. 6) and in earlier
studies are quasi-stationary and possibly spurious oro-
graphic features of little importance to the SH climate.
The maxima over the midlatitude continents and near
Antarctica that dominate these climatologies are almost
uncorrelated with regions of atmospheric variability re-
sulting from the passage of cyclones and anticyclones
(Trenberth 1991). When these orographic features
were removed from the statistics, the distribution of
remaining migratory cyclones (Fig. 10) was much
more uniform. A calculation of track density, where
centers were counted just once per grid point per cy-
clone yielded maximum cyclone activity near 50°S
year-round rather than within the cyclone graveyard of

2255

the circumpolar trough, in excellent agreement with
baroclinic storm tracks obtained by Trenberth (1991).
A second maximum associated with the subtropical jet
occurred during winter and spring near 40°S in the New
Zealand—Pacific sector.

A similar derivation of cyclone statistics for a higher
level (say 700 or 500 hPa) would eliminate the prob-
lems posed by shallow topographic perturbations and
meaningless pressure reductions to MSL. However, af-
ter eliminating topographic features, track densities
based on 1000-hPa analyses are remarkably similar to
fields of 300-hPa variability computed by Trenberth
(1991). Despite inherent differences between 300-hPa
atmospheric variability and surface cyclone activity,
this similarity suggests that meaningful boundaries
have been drawn here between migratory weather-pro-
ducing cyclones and fixed orographic features.

The continuing widespread practice of manually an-
alyzing MSL charts ensures an ongoing interest in cy-
clone statistics at this level, despite these drawbacks.
Manual analysis has the potential for more accurate
placement of vorticity centers than objective analyses
through careful identification of cloud vortices seen in
satellite imagery. Observed cloud vortices are often
misplaced or even omitted by numerical analyses over
maritime regions. The methodology described here
could be used to compare the statistics of cyclones de-
picted in numerical analyses with those derived by
manually tracking vorticity centers observed in satellite
imagery. This would provide an independent measure
of analysis skill and avoid the ‘‘incestuous’’ practice
of evaluating model prognoses against model analyses.

Since atmospheric variability arises from both highs
and lows, it is desirable to also examine the contribu-
tion from anticyclones——also of interest in their own
right. The identification and tracking method described

Cyclone numbers, 1980-1986

3500 5
3000 f
2500 |
2000 f

1500 F

Number of cyclones

1000 fF

500

0 { \ 1 4 an an
80 8 82 83 84 85 86
Year

Fic. 16. Trend in cyclone numbers (per month) for atl cyclones
(top curve) —those moving a total distance less than 20° of latitude
(middle curve) and those moving greater than 10° (bottom curve).

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

--- PAGE 18 ---
2256

here has the advantages of being objective and readily
extendible to tracking anticyclones.

Work has started to extend these results using a 10-
yr database of ECMWF analyses to determine preferred
formation and cyclogenesis locations of SH cyclones.
Methods based on pressure minima cannot detect cy-
clone formation, because the first-track position is not
necessarily the formation location. These locations can
be derived only with confidence using vorticity. as a
measure of cyclone intensity.

In summary, a methodology for establishing cyclone
statistics has been described. It has been shown that

results are highly dependent on the rationale for se- .

lecting and counting cyclones. By avoiding stationary
cyclones associated with topography, a contemporary
climatology of the weather-producing cyclones impor-
tant to the general circulation of the SH has been ob-
tained. In addition, the method can be used to assess
the performance of numerical models and to determine
possible regional impacts of global climate change. The
technique is readily extendible to other datasets, other
phenomena, and other geographical regions.

Acknowledgments. This work was supported by the
New Zealand Foundation for Research, Science and
Technology Contract CO1227.

REFERENCES

Akyildiz, V., 1985: Systematic errors in the behaviour of cyclones in
the ECMWF operational models. Tellus, 37A, 297-308.

Alpert, P., B. U. Neeman, and Y. Shay-el, 1990: Intermonthly vari-
ability of cyclone tracks in the Mediterranean. J. Climate, 3,
1474-1478.

Blackmon, M. L., J. M. Wallace, N. C. Lau, and S. L. Mullen, 1977:
An observational study of the Northern Hemisphere wintertime
circulation. J. Atmos. Sci., 34, 1040-1053.

Bleck, R., 1965: Lineare Approximationsmethodem zur Bestimmung
ein-und zweidimensionaler numerischer Filter des dynamischen
Meteorologie. Institut fur Theoretische Meteorologie der Freien
Universitat Berlin.

Bromwich, D. H., 1991: Mesoscale cyclogenesis over the south-west-
ern Ross Sea linked to strong katabatic winds. Mon. Wea. Rev.,
119, 1736-1752.

Carleton, A. M., 1979: A synoptic climatology of satellite-observed
extratropical cyclone activity for the Southern Hemisphere win-
ter. Arch. Meteor. Geophys. Bioklimatol., B, 27, 265—279.

——--, 1992: Synoptic interactions between Antarctica and lower lat-
itudes. Aust. Meteor. Mag., 40, 129-147.

Guymer, L. B., 1978: Operational application of satellite imagery to
-synoptic analysis in the Southern Hemisphere. Tech. Rep. No.
29, Bureau of Meteorology, Australia, 83 pp.

Karelsky, S., 1963: Geographical distribution of pressure in the cen-
tres of surface lows and highs in the Australian region in January
and July, 1952~1963. Aust. Meteor. Mag., 43, 15-23.

Kurtz, D. D., and D. H. Bromwich, 1983: Satellite observed behav-
iour of the Terra Nova Bay polynya. J. Geophys. Res., 18, 9717-
9722. ;

Lambert, S. J., 1988: A cyclone climatology of the Canadian Climate
Centre general circulation model. J. Climate, 1, 109~115.
Leary, C., 1971: Systematic errors in operational National Meteoro-
logical Center primitive-equation surface prognoses. Mon. Wea.

Reyv., 99, 409-413.

Le Marshall, J. F., and G. A. M. Kelly, 1981: A January and July
climatology of the Southern Hemisphere based on daily numer-
ical analyses 1973-77. Aust. Meteor. Mag., 29, 115-123.

MONTHLY WEATHER REVIEW

VOLUME 122

Le Treut, H., and E. Kalnay, 1990: Comparison of observed and
simulated cyclone frequency distribution as determined by an
objective method. Asmosfera, 3, 57-71. ‘

Manabe, S., and T. Terpstra, 1974: The effects of mountains on the
general circulation of the atmosphere as identified by numerical
experiments. J. Atmos. Sci., 31, 3-42.

Mather, K. B., and G. S. Miller, 1967: Notes on topographic factors
affecting the surface wind in Antarctica, with special reference
to katabatic winds (and bibliography). University of Alaska
Tech. Rep. U.A.G. R-189, 63 pp.

Mechoso, C. R., 1980: The atmospheric circulation around Antarc-
tica: Linear stability and finite-amplitude interactions with mi-
grating cyclones. J. Atmos. Sci., 37, 2209-2233.

Mullan, A. B., and J. A. Renwick, 1990: Climate change in the New
Zealand region inferred from general circulation models. New
Zealand Meteorological Service Report, 142 pp.

Murray, R. J., and I. Simmonds, 1991a: A numerical scheme for

tracking cyclone centres from digital data. Part : Development

and operation of the scheme. Aust. Meteor. Mag., 39, 155-166.

, and , 199ib: A numerical scheme for tracking cyclone

centres from digital data. Part H: Application to January and

July general circulation model simulations. Aust. Meteor. Mag.,

39, 167-180.

Parish, T. R., 1988: Surface winds over the Antarctic continent: A
review. Rev. Geophys., 26, 169-180.

———, 1992: On the interaction between Antarctic katabatic winds
and tropospheric motions in the high southern latitudes. Aust.
Meteor. Mag., 40, 149-167.

Petterssen, S., 1956: Weather Analysis and Forecasting. Vol. 1. Mo-
tion and Motion Systems. McGraw-Hill, 428 pp.

Schwerdtfeger, W., 1970: The climate of the Antarctic. World Survey
of Climatology. Vol. 14. Climates of the Polar Regions. S. Or-
vig, Ed., Elsevier, 370 pp.

Silverberg, S. R., and L. F. Bosart, 1982: An analysis of systematic
cyclone errors in the NMC LFM II model during the 1978-79
cool season. Mon. Wea. Rev., 110, 254~271.

Simmonds, I., and X. Wu, 1993: Winter Antarctic sea ice and extra-
tropical cyclone activity. WMO/TD-No. 533, 7.37~7.39.
Sinclair, M. R., and X. Cong, 1992: Polar air stream cyclogenesis in
the Australasian region: A composite study using ECMWF anal-

yses. Mon. Wea. Rev., 120, 1950-1972.

Streten, N. A., 1973: Some characteristics of satellite-observed bands
of persistent cloudiness over the Southern Hemisphere. Mon.
Wea, Rev., 101, 486-495.

~——, and A. J. Troup, 1973: A synoptic climatology of satellite
observed cloud vortices over the Southern Hemisphere. Quart.
J. Roy. Meteor. Soc., 99, 56-72.

’ Taljaard, J. J., 1967: Development, distribution and movement of

cyclones and anticyclones in the Southern Hemisphere during
the IGY. J. Appl. Meteor., 6, 973-987.

Taylor, K. E., 1986: An analysis of the biases in traditional cyclone
frequency maps. Mon. Wea. Rev., 114, 1481-1490.

Trenberth, K. E., 1991: Storm tracks in the Southern Hemisphere. J.
Atmos. Sci., 48, 2159~2178.

——, and J. G. Olson, 1988: An evaluation and intercomparison of
global analyses from the National Meteorological Center and
the European Centre for Medium-Range Weather Forecasts.
Bull. Amer. Meteor. Soc., 69, 1047~1057.

van Loon, H., 1965: A climatological study of the atmospheric cir-
culation in the Southern Hemisphere during the IGY, Part I: 1
July 1957-31 March 1958. J. Appl. Meteor., 4, 479-491.

——, J.J. Taljaard, T. Sasamori, J. London, D. V. Hoyt, K. Labitzke,
and C. W. Newton, 1972: Meteorology of the Southern Hemi-
sphere. Meteor. Monogr., No. 13, Amer. Meteor. Soc., 263 pp.

Wallace, J. M., G.-H. Lim, and M. L. Blackmon, 1988: Relationship
between cyclone tracks, anticyclone tracks, and baroclinic
waveguides. J. Atmos. Sci., 45, 439-462.

Whittaker, L. M., and L. H. Horn, 1983: Northern Hemisphere ex-
tratropical cyclone activity for four mid-season months. J. Cli-
matol., 4, 297-310.

Unauthenticated | Downloaded 11/09/23 01:34 AM UTC

