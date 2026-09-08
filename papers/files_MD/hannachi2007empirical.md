INTERNATIONALJOURNALOFCLIMATOLOGY
Int.J.Climatol.27:1119–1152(2007)
Publishedonline22May2007inWileyInterScience
(www.interscience.wiley.com)DOI:10.1002/joc.1499
Review
| Empirical |     |     | orthogonal  |            |     | functions      | and |       | related    |     | techniques |     | in  |
| --------- | --- | --- | ----------- | ---------- | --- | -------------- | --- | ----- | ---------- | --- | ---------- | --- | --- |
|           |     |     | atmospheric |            |     | science:       |     | A     | review     |     |            |     |     |
|           |     |     | A.          | Hannachi,* |     | I. T. Jolliffe | and | D. B. | Stephenson |     |            |     |     |
DepartmentofMeteorology,UniversityofReading,ReadingRG66BB,UK
Abstract:
Climateandweatherconstituteatypicalexamplewherehighdimensionalandcomplexphenomenameet.Theatmospheric
systemistheresultofhighlycomplexinteractionsbetweenmanydegreesoffreedomormodes.Inordertogaininsightin
understanding the dynamical/physical behaviour involved it is useful to attempt to understand their interactions in terms
ofamuchsmallernumberofprominentmodesofvariability.Thishasledtothedevelopmentbyatmosphericresearchers
of methods that give a space display and a time display of large space-time atmospheric data.
Empiricalorthogonalfunctions(EOFs)werefirstusedinmeteorologyinthelate1940s.Themethod,whichdecomposes
a space-time field into spatial patterns and associated time indices, contributed much in advancing our knowledge of the
atmosphere.However,sincetheatmospherecontainsallsortsoffeatures,e.g.stationaryandpropagating,EOFsareunable
toprovideafullpicture.Forexample,EOFstend,ingeneral,tobedifficulttointerpretbecauseoftheirgeometricproperties,
such as their global feature, and their orthogonality in space and time. To obtain more localised features, modifications,
e.g.rotatedEOFs(REOFs),havebeenintroduced.Atthesametime,becausethesemethodscannotdealwithpropagating
features, since they only use spatial correlation of the field, it was necessary to use both spatial and time information in
order to identify such features. Extended and complex EOFs were introduced to serve that purpose.
BecauseoftheimportanceofEOFsandcloselyrelatedmethodsinatmosphericscience,andbecausetheexistingreviews
of the subject are slightlyout of date, there seems to be a need to update our knowledge by including new developments
that could not be presented in previous reviews. This review proposes to achieve precisely this goal. The basic theory of
themaintypesofEOFsisreviewed,andawiderangeofapplicationsusingvariousdatasetsarealsoprovided. Copyright
|  2007 | Royal | MeteorologicalSociety |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ----- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
empirical orthogonalfunctions; simplified EOFs; extended EOFs; complex EOFs; North AtlanticOscillation;
KEYWORDS
|     | Madden | Julian | oscillation;Quasi-biennialoscillation |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | ------ | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Received4May2006;Revised22December2006;Accepted27December2006
INTRODUCTION characterised by non-linearity and high dimensionality.
Consequently,achallengingtaskistofindwaystoreduce
| Climate | is regarded | as the | aggregation |     | of (random) | daily |     |     |     |     |     |     |     |
| ------- | ----------- | ------ | ----------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
thedimensionalityofthesystemtoafewmodesifpossi-
| weather, | and as | pointed | out by | Lorenz | (1970), | climate |     |     |     |     |     |     |     |
| -------- | ------ | ------- | ------ | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
ble.Afurther,yetchallenging,taskistolinkthesemodes
| may be           | defined,     | in mathematical |            | terms,     | as the | collection  |           |                  |            |     |             |       |          |
| ---------------- | ------------ | --------------- | ---------- | ---------- | ------ | ----------- | --------- | ---------------- | ---------- | --- | ----------- | ----- | -------- |
|                  |              |                 |            |            |        |             | to the    | dynamics/physics |            | of  | the system. |       |          |
| of all long-term |              | statistical     | properties | of         | the    | atmospheric |           |                  |            |     |             |       |          |
|                  |              |                 |            |            |        |             | Empirical |                  | orthogonal |     | function    | (EOF) | analysis |
| state. It        | is therefore | the             | long-term  | statistics |        | of weather. |           |                  |            |     |             |       |          |
(Fukuoka,1951;Lorenz,1956)isamongthemostwidely
| Heinlein   | (1973)  | says ‘climate |                 | is what | we    | expect but  |                 |       |               |         |             |             |            |
| ---------- | ------- | ------------- | --------------- | ------- | ----- | ----------- | --------------- | ----- | ------------- | ------- | ----------- | ----------- | ---------- |
|            |         |               |                 |         |       |             | and extensively |       | used          | methods | in          | atmospheric | science.   |
| weather    | is what | we get’       | (this quotation |         | is in | the section |                 |       |               |         |             |             |            |
|            |         |               |                 |         |       |             | The method      |       | is in essence | an      | exploratory | (i.e.       | non-model  |
| ‘More from | the     | Notebooks     | of              | Lazarus | Long’ | of Robert   |                 |       |               |         |             |             |            |
|            |         |               |                 |         |       |             | orientated)     | tool, | which         | allows  | a time      | display     | anda space |
A.Heinlein’snovel,butsomesources,however,attribute
|           |          |                 |     |        |     |            | display | of the | space-time |     | field that | may | be useful to |
| --------- | -------- | --------------- | --- | ------ | --- | ---------- | ------- | ------ | ---------- | --- | ---------- | --- | ------------ |
| it to the | American | writer/lecturer |     | Samuel |     | L. Clemens |         |        |            |     |            |     |              |
known by the pen name Mark Twain (1835–1910)). Cli- the atmospheric scientist. The existence of fast and effi-
cientalgorithmsalsohelpeditswidespreaduse.EOFsare
| mate variations |     | are also | the result | of  | exceedingly | com- |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ---------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
plex non-linear interactions between very many degrees multipurpose and have been used for example in dimen-
|            |     |        |              |     |     |             | sionality | reduction | and          | patterns  | extraction. |                 |          |
| ---------- | --- | ------ | ------------ | --- | --- | ----------- | --------- | --------- | ------------ | --------- | ----------- | --------------- | -------- |
| of freedom | or  | modes. | Both weather |     | and | climate are |           |           |              |           |             |                 |          |
|            |     |        |              |     |     |             | Since     | the       | early review | of        | Kutzbach    | (1967)          | on EOFs, |
|            |     |        |              |     |     |             | and apart | from      | a few        | textbooks |             | (Preisendorfer, | 1988;    |
*Correspondence to:A.Hannachi,DepartmentofMeteorology, King von Storch and Zwiers, 1999; Jolliffe, 2002; Wilks,
| Abdulaziz | University, | PO Box | 80208, | Jeddah | 21589, | Saudi Arabia. |     |     |     |     |     |     |     |
| --------- | ----------- | ------ | ------ | ------ | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
E-mail:ahannachi@kau.edu.sa 2006),thesubjecthasnotbeensystematicallyreviewedin
Copyright2007RoyalMeteorologicalSociety

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1120
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
|                 |     |         |            |     |            |             | i.e. EOF | elements, | that | are identically | zero, | resulting | in  |
| --------------- | --- | ------- | ---------- | --- | ---------- | ----------- | -------- | --------- | ---- | --------------- | ----- | --------- | --- |
| the atmospheric |     | science | literature |     | to address | the various |          |           |      |                 |       |           |     |
recentdevelopmentsinthefield.Giventheimportanceof localised structures without any rotation.
EOFsandrelatedmethodsinclimateresearch,webelieve EOFs and REOFs are mainly based on using the spa-
that the limited literature reviews on the subject do not tial correlation of the field, an important feature of cli-
meet the need of climate researchers. This introductory mate data. Auto- and cross-correlation in time between
review on EOFs is a contribution to fill in this gap, grid points, however, are ignored in those techniques.
but is by no means exhaustive. Further references and Extended EOF analysis (Weareand Nasstrom, 1982) is a
more detailed material on the subject will be provided techniquethatattemptstoincorporateboththespatialand
as we go through the text. The manuscript is intended the temporal correlation. The method has, since its intro-
for research students and also researchers starting in the duction, becomea useful tool to extractdynamicalstruc-
field of weather/climate analysis, and can be used for ture, e.g. trends, oscillations, propagating structures, and
educational purpose. to filter data (Broomhead and King, 1986a,b; Fraedrich,
Given any space-time meteorological field, EOF anal- 1986a,b; Kimoto etal., 1991; Plaut and Vautard, 1994).
ysis finds a set of orthogonal spatial patterns along with Another related method that attempts to find propa-
a set of associated uncorrelated time series or principal gating patterns is complex Hilbert empirical orthogonal
components(PCs).Thegeometricalconstraintscharacter- function (HEOF) analysis. The frequencydomain empir-
ising EOFs and PCs can be very useful in practice since ical orthogonal function (FDEOF) method finds EOFs
the covariance matrix of any subset of retained PCs is based on the cross-spectrum matrix averaged over a
| always diagonal. |     | These | same | constraints, |     | however, can |          |       |           |               |     |                |     |
| ---------------- | --- | ----- | ---- | ------------ | --- | ------------ | -------- | ----- | --------- | ------------- | --- | -------------- | --- |
|                  |     |       |      |              |     |              | specific | small | frequency | band (Wallace |     | and Dickinson, |     |
also be restrictive in other contexts. Take spatial orthog- 1972; Wallace, 1972; Brillinger, 1981). FDEOFs gener-
onality, for instance. Because it is a global property, alise conventional EOFs in the sense that the covariance
the orthogonality constraint can cause the EOFs to have matrix used for EOFs is only related to the real part
structures over most of the domain and with significant of the cross-spectrum matrix and hence does not use
| amplitude, | when | in fact | one | expects | the patterns | to be |           |             |      |             |     |                |     |
| ---------- | ---- | ------- | --- | ------- | ------------ | ----- | --------- | ----------- | ---- | ----------- | --- | -------------- | --- |
|            |      |         |     |         |              |       | the whole | information | from | the complex |     | cross-spectrum |     |
morelocalised.Horel(1981),forexample,pointsoutthat matrix.TheHEOFmethod(Rasmussonetal.,1981;Bar-
if the first EOF has a constant sign over its domain then nett, 1983; Horel, 1984; von Storch and Zwiers, 1999)
the second one will generally have both signs with the is an alternative to FDEOFs and uses the Hilbert, or
zerolinegoingthroughthemaximaofthefirstEOF.This quadrature transform of the field. This transform allows
also yields the problem of domain-dependence and non- HEOFs to deal with propagating structures/waves in the
locality(Horel,1981;Richman,1986,1987).Theseprob- time domain using complexified fields.
lems can cause difficulties in interpreting the obtained Themanuscriptreviewstheexploratory methodsmen-
| patterns | (Ambaum | etal., | 2001, | 2002; | Dommenget | and |               |         |       |            |     |        |       |
| -------- | ------- | ------ | ----- | ----- | --------- | --- | ------------- | ------- | ----- | ---------- | --- | ------ | ----- |
|          |         |        |       |       |           |     | tioned above. | Various | other | extensions | to  | EOF/PC | anal- |
Latif, 2002; Jolliffe etal., 2003) becausephysical modes ysis are briefly discussed toward the end, and refer-
are not necessarily orthogonal. Normal modes derived, ences are provided for further details. Other methods
for example, from linearised dynamical/physical models, such as principal oscillation patterns (POPs) and princi-
suchasbarotropicmodels(Simmonsetal.,1983)arenot pal interaction patterns, which are model-orientated, i.e.
| orthogonal | since | physical | processesare |     | not | uncorrelated. |                  |     |         |         |           |       |       |
| ---------- | ----- | -------- | ------------ | --- | --- | ------------- | ---------------- | --- | ------- | ------- | --------- | ----- | ----- |
|            |       |          |              |     |     |               | non-exploratory, |     | methods | are not | discussed | here. | Also, |
The previous prevailing difficulties associated with methods involving covariability between two or more
interpreting EOFs have led researchers to develop tools fields such as in coupled patterns, e.g. canonical correla-
to overcome these difficulties. Linear transformations of tion analysis (Bretherton et al., 1992), are not presented
EOFs, based on rotation, have been introduced and yield here. The manuscript is organised as follows. Section 2
| the concept | of  | rotated | empirical |     | orthogonal | functions |         |             |     |           |             |     |      |
| ----------- | --- | ------- | --------- | --- | ---------- | --------- | ------- | ----------- | --- | --------- | ----------- | --- | ---- |
|             |     |         |           |     |            |           | reviews | the concept | of  | EOFs with | application | to  | win- |
(REOFs) (Horel, 1981; Richman, 1981, 1986; Cheng ter monthly sea level pressure (SLP) reanalyses. Section
et al., 1995, Xinhua and Dunkerton 1995). The REOF 3 presents ways of simplification of EOFs, focussing
| method | yields | in general | localised |     | structures | by com- |           |         |                |       |      |             |     |
| ------ | ------ | ---------- | --------- | --- | ---------- | ------- | --------- | ------- | -------------- | ----- | ---- | ----------- | --- |
|        |        |            |           |     |            |         | mainly on | rotated | and simplified | EOFs, | with | application |     |
promising some of the EOFs’ geometric properties such towinterSLP.ExtendedEOFswithapplicationtooutgo-
| as orthogonality. |     | Rotation | attempts |     | to yield | simpler pat- |          |      |           |           |           |            |     |
| ----------------- | --- | -------- | -------- | --- | -------- | ------------ | -------- | ---- | --------- | --------- | --------- | ---------- | --- |
|                   |     |          |          |     |          |              | ing long | wave | radiation | (OLR) are | presented | in section |     |
terns than EOFs. In rotation various decisions have to 4 while section 5 deals with complex EOFs with appli-
be made. For instance, the rotation, or simplicity, cri- cation to the quasi-biennial oscillation (QBO). Section 6
| terion is | not unique. |     | In addition, |     | the number | of EOFs |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------------ | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
brieflydiscussesvariousotherextensionstoEOFanalysis
used for rotation cannot be fixed a priori but remains including very recent ones. A summary and conclusions
arbitrary. Other alternatives to rotation have been pro- are presented in the final section.
| posed. A    | particularly |         | interesting | one,     | simplified | EOFs,  |     |     |     |     |     |     |     |
| ----------- | ------------ | ------- | ----------- | -------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| is a method | based        | on      | the least   | absolute | shrinkage  | and    |     |     |     |     |     |     |     |
| selection   | operator     | (LASSO) |             | approach | introduced | in the |     |     |     |     |     |     |     |
EOFS
| context | of regression |     | by Tibshirani |     | (1996)     | and adapted |            |            |     |     |     |     |     |
| ------- | ------------- | --- | ------------- | --- | ---------- | ----------- | ---------- | ---------- | --- | --- | --- | --- | --- |
|         |               |     |               |     |            |             | Historical | background |     |     |     |     |     |
| to EOFs | by Jolliffe   | et  | al. (2003).   |     | The method | attempts    |            |            |     |     |     |     |     |
to achieve simultaneously the desirable property of large EOFs have been used in atmospheric science since the
variance and simplicity. The method can yield loadings, late 1940’s by Obukhov (1947, 1960), Fukuoka (1951),
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1121
Lorenz (1956), and Kutzbach (1967). See, for exam- Data formatting
ple, Craddock (1973) for a discussion of eigenanal-
We suppose that we have a gridded data set composed
ysis in meteorology. Since then EOFs have become
ofaspace-timefieldX(t,s)representingthevalueofthe
popular analysis tools and are widely used in climate
field X, such as SLP, at time t and spatial position s.
research. EOF techniques have their roots in social sci- The value of the field at discrete time t and grid point
i
ence, and go back to Pearson (1902), and later to s is denoted x for i =1,...,n and j =1,...p. The
j ij
Hotelling (1933, 1935) who introduced principal com- observed field is then represented by the data matrix:
ponentanalysis(PCA),themorecommonnameforEOF
 
analysis.EOFs,however,arenotrestrictedtomultivariate x 11 x 12 ... x 1p
s e t x a t t r i a s c ti t c io s n or (F at u m ku o n sp a h g e a ri a c n s d ci K en o c o e n s t . z T , h 1 e 9 y 70 e ) xte a n n d d t t o he fe a a n tu a r l e - X =(x 1 ,x 2 ,...,x n )T =    x . . 21 x . . 22 .. . . . x 2 . . p    (2)
. . . .
ysis of stochastic fields in the mathematical literature
x x ... x
where they are known under the name Karhunen-Loe`ve n1 n2 np
basis functions (Loe`ve, 1978). The original aim of EOFs wherex =(x ,x ,...x )T,t =1,...n,representsthe
t t1 t2 tp
(Obukhov, 1947; Fukuoka, 1951; Lorenz, 1956) was to map, or the value of the field at time t. Let us denote by
achieveadecompositionofacontinuousspace-timefield x the time average of the field at the i’th spatial grid
.i
X(t,s),wheret andsdenoterespectivelytimeandspatial point. This time average is given by:
position, as
(cid:1)n
1
x = x . (3)
.i ki
(cid:1)M n
k=1
X(t,s)= c (t)u (s), (1)
k k
k=1 The climatology of the field is defined by
1
where M is the number of modes contained in the field, x=(x .1 ,...,x .p )= n 1T n X (4)
using an optimal set of basis functions of space u (s) k
and expansion functions of time c k (t). In practice the where 1 n =(1,...1)T is the (column) vector of length
EOF/PCAtechniqueaimsatfindinganewsetofvariables n containing only ones. The anomaly field, or departure
that capture most of the observed variance from the data fromtheclimatologyisdefinedat(t,s ),t =1,...n,and
k
through linear combinations of the original variables. k =1,...p, by:
The EOF terminology is due to Lorenz (1956) who
applied it in a forecasting project at the Massachusetts x t (cid:1) k =x tk −x .k (5)
Institute of Technology. The method, however, had been
applied in meteorology a decade earlier by Obukhov or in matrix form:
(cid:8) (cid:9)
(1947) for smoothing purposes, and was mentioned by
1
Fukuoka (1951) in a forecasting context, see Craddock X (cid:1) =X−1 n x= I n − n 1 n 1T n X =HX (6)
(1973) for a little further historical account. In addition
tosmoothingandprediction,EOFshavealsobeenusedto where I is the n×n identity matrix, and H is the
n
reduce the large number of variables of the original data centring matrix of order n (Mardia etal., 1979). To keep
toafewvariables,butwithoutcompromisingmuchofthe the notation simple, from now on and unless otherwise
variabilityof thedata (e.g.HannachiandO’Neill,2001.) stated,thedashin(6) willbedroppedandX willsimply
RecentlyEOFanalysishasbeenusedtoextractindividual denote the anomaly data matrix.
modes of variability that can be physically relevant such
as the Arctic Oscillation (AO), (Pavan et al., 2000), Formulation andcomputation of EOFs
known as teleconnections (Angstro¨m, 1935; Bjerknes,
We present below a description of how to obtain EOFs,
1969;WallaceandGutzler,1981;WallaceandThompson
andformoredetailsthereaderisreferred,forexample,to
2002, etc.) Today, EOF methods are commonly used in
vonStorch(1995),vonStorchandZwiers(1999),Jolliffe
mostmeteorologicalcentrestocompareobservationsand
(2002), and Wilks (2006). Once the anomaly data matrix
reanalyses to climate model simulations.
(6) is determined, the sample covariance matrix is then
EOFs have been extensively studied in the literature,
defined by:
andforadetailedanalysisthereaderisreferredtothefol- 1
S = XTX, (7)
lowing textbooks, mostly orientated toward atmospheric n
science applications: Preisendorfer (1988), von Storch
which contains the covariances s , i,j =1,...p, and Zwiers (1999), and Wilks (2006). For more general ij
between the time series of the field at any pair of grid
applicationofPCAanalysis,thereaderisreferred,e.g.to
points (s ,s ), i.e.
the textbooks by Seal (1967), Morrison (1976), Ander- i j
son (1984), Chatfield and Collins (1989), Mardia etal.
(cid:1)n
1
(1979), Krzanowski (2000), Jackson (1991), and Jolliffe s =[S] = x x . (8)
ij ij ti tj
(2002) and more references therein. n
t=1
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1122
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
|                                                 |     |     |     |     |     |     | Thematrix(cid:2)isdiagonal,i.e.(cid:2)=Diag(λ |     |     |     |           |     | ,λ  | ,...,λ ). |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --------- | --- | --- | --------- |
| TheaimofEOFanalysis/PCAistofinduncorrelatedlin- |     |     |     |     |     |     |                                               |     |     |     |           |     | 1   | 2 r       |
|                                                 |     |     |     |     |     |     |                                               |     |     |     | ≥λ ≥...≥λ |     | ≥0  |           |
ear combinations of the different variables that explain The diagonal elements λ of (cid:2) are
|     |     |     |     |     |     |     |     |     |     | 1   | 2   |     | r   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
maximum variance, that is to find a unit-length direction the singular values of X. The columns a ,...,a of A,
|      |     |     |     |     |     |     |     |     |     |     |     |     | 1   | r   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| u=(u |     | )T  |     |     |     |     |     |     |     |     |     |     |     |     |
1 ,...,u p such that Xu has maximum variabil- and u 1 ,...,u r of U are respectively the left and right
ity. This readily yields: singular vectors of the data matrix X. There are other
|     |     |            |     |       |     |     | ways                                                | to express | the | SVD | but (14) | provides |     | a compact |
| --- | --- | ---------- | --- | ----- | --- | --- | --------------------------------------------------- | ---------- | --- | --- | -------- | -------- | --- | --------- |
|     |     | max(uTSu), |     | uTu=1 |     |     |                                                     |            |     |     |          |          |     |           |
|     |     |            |     | s.t.  |     | (9) | representationbecauseitdropsunnecessaryzerosingular |            |     |     |          |          |     |           |
values.
√
| The EOFs | are | therefore | obtained | as  | the solution | to the |     |             |     |        |        |     |             |     |
| -------- | --- | --------- | -------- | --- | ------------ | ------ | --- | ----------- | --- | ------ | ------ | --- | ----------- | --- |
|          |     |           |          |     |              |        | The | application |     | of the | SVD to | the | data matrix | nX  |
eigenvalue problem: yields for the covariance matrix (7) the decomposition:
|     |     |     | Su=λ2u |     |     | (10) |     |     |     | =U(cid:2)2UT, |     |     |     |      |
| --- | --- | --- | ------ | --- | --- | ---- | --- | --- | --- | ------------- | --- | --- | --- | ---- |
|     |     |     |        |     |     |      |     |     |     | S             |     |     |     | (15) |
Thek’thEOFissimplythek’theigenvectoru ofS.The =Diag(λ2,λ2,...,λ2)
|               |            |        |     |           | k       |     | where      | (cid:2)2 |      |        |               | and        | where  | the singu- |
| ------------- | ---------- | ------ | --- | --------- | ------- | --- | ---------- | -------- | ---- | ------ | ------------- | ---------- | ------ | ---------- |
| corresponding | eigenvalue |        | λ2, | k =1,...p | is then |     |            |          |      | 1 2    | r             |            |        |            |
|               |            |        | k   |           |         |     | lar values | have     | been | sorted | in            | decreasing | order. | Note       |
|               |            |        |     | 1         |         |     | that the   | constant | n    | has    | been absorbed |            | by the | diagonal   |
|               |            | λ2 =uT |     | = ||Xu    | ||2     |     |            |          |      |        |               |            |        |            |
Su (11) matrix (cid:2)2. The EOFs u ,...u and the PCs a ,...a
|     |     | k   | k k | n   | k   |     |               |     |           |     | 1 r  |          |         | 1 r    |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ---- | -------- | ------- | ------ |
|     |     |     |     |     |     |     | are therefore |     | the right | and | left | singular | vectors | of the |
and hence gives a measure of the variance of the data data matrix anomaly X. Note that for the decomposition
accounted for in the direction u . After finding the (14) to be efficient in computation the data matrix X has
k
eigen elements of the sample covariance matrix S in tobetransposedtoyieldmin(n,p)asitsfirstdimension.
(9), the eigenvalues are normally sorted in decreasing The EOFs are therefore orthogonal and the PCs uncor-
orderasλ2 ≥λ2...≥λ2.Itisusualtowritethevariance related, and this is a major characteristic of conventional
|     | 1   | 2   | p   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accounted for in percentage as: EOFs.Theorthogonalityisausefulpropertysinceitpro-
|     |     |     |     |     |     |     | vides | a complete | basis | forthe | datamatrix. |     | Equation | (14) |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ----- | ------ | ----------- | --- | -------- | ---- |
100λ2
|     |     |     |     | k%. |     |     | yields | in fact | the decomposition: |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------------------ | --- | --- | --- | --- | --- |
(12)
(cid:1)p
|     |     |     | λ2  |     |     |     |     |     |     |     | (cid:1)r |     |     |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- |
|     |     |     |     | k   |     |     |     |     |     | =   |          | uT. |     |      |
|     |     |     |     |     |     |     |     |     |     | X   | λ a      |     |     | (16) |
|     |     |     | k=1 |     |     |     |     |     |     |     | k k      | k   |     |      |
k=1
| The projectionof |     | the anomalyfieldX |     |     | onto the | k’thEOF |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------------- | --- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
=(u )T, =Xu Component-wise, the previous decomposition expresses
| u k | k1 ,u k2 ,...,u | kp  | i.e. | a k | k is the | k’th PC |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | ---- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
=(x
whose elements a , t =1,...n, are given by: the map x ,x ,...,x )T of the field X at time t
|     |     | tk  |     |     |     |     |     | t   | t1  | t2  | tp  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by
|     |     |     | (cid:1)p |       |     |      |     |     |     |     | (cid:1)r |     |     |      |
| --- | --- | --- | -------- | ----- | --- | ---- | --- | --- | --- | --- | -------- | --- | --- | ---- |
|     |     | a   | =        | x u   | .   | (13) |     |     |     | x = | λ a      | u   |     | (17) |
|     |     | tk  |          | tj kj |     |      |     |     |     | t   | k tk     | k   |     |      |
|     |     |     | j=1      |       |     |      |     |     |     |     | k=1      |     |     |      |
So the k’th eigenvalue λ2 represents the variance of where a tk is the element of the k’th PC a k at time t.
k
the k’th PC a =(a ,a ,...a )T. The relationship Note again the link between Eq (17), which is simply
|         |         | k 1k | 2k     | nk  |               |     |            |      |     |          |       |      |     |     |
| ------- | ------- | ---- | ------ | --- | ------------- | --- | ---------- | ---- | --- | -------- | ----- | ---- | --- | --- |
|         |         |      |        |     |               |     | the vector | form | of  | Eq (13), | to Eq | (1). |     |     |
| between | Eq (13) | and  | Eq (1) | can | now be noted. | The |            |      |     |          |       |      |     |     |
time function c (t) and the space function u (s) in Equation (17) is particularly useful when EOFs are
|         |             | k   |          |      |                       | k   |      |           |     |                |     |        |       |          |
| ------- | ----------- | --- | -------- | ---- | --------------------- | --- | ---- | --------- | --- | -------------- | --- | ------ | ----- | -------- |
|         |             |     |          |      |                       |     | used | to reduce | the | dimensionality |     | of the | data. | This can |
| (1) are | represented | by  | x tj and | u kj | in (13) respectively. |     |      |           |     |                |     |        |       |          |
In various literatures the EOFs are also known as the be achieved simply by truncating the above sum by
PCloadings,andsometimessimplyPCs.ThePCsonthe keeping, say, the first M terms where M is generally
|     |     |     |     |     |     |     | muchsmaller |     | thanthe | rankr | of X. | Thereis | nouniversal |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ----- | ----- | ------- | ----------- | --- |
otherhandarealsoknownasEOFexpansioncoefficients,
EOF amplitudes, PC time series, and PC scores. In this rule, however, for truncation, and the choice of M is in
|     |     |     |     |     |     |     | generalarbitrary.Inpracticethe |     |     |     | truncationorder |     |     | is often |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --------------- | --- | --- | -------- |
manuscriptweusetheterminologyEOFsandPCsforthe
spatial and temporal patterns respectively. obtained by fixing the amount of represented variance,
In practice we do not need to compute the covariance e.g. 80%, and choosing the set of the M leading EOFs
|           |                                        |     |     |     |     |     | that explain |     | altogether | at  | least this | amount | of  | variance. |
| --------- | -------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ---------- | ------ | --- | --------- |
| matrix(7) | andsolvetheeigenvalueproblem(10).Weuse |     |     |     |     |     |              |     |            |     |            |        |     |           |
a powerful tool from linear algebra namely the singular The spectrum of the covariance matrix S composed of
|                     |     |     |        |        |         |       | the eigenvalues |     | λ2,...,λ2 |     | provides | information |     | on the |
| ------------------- | --- | --- | ------ | ------ | ------- | ----- | --------------- | --- | --------- | --- | -------- | ----------- | --- | ------ |
| value decomposition |     |     | (SVD), | (Golub | and van | Loan, |                 |     | 1         |     | r        |             |     |        |
n×p
1996). Any data matrix X can be decomposed as: distribution of power(energy)asa function of scale,and
|     |     |     |     |     |     |     | on the | separation/degeneracy |     |     | of  | the EOF | patterns. | For |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------------- | --- | --- | --- | ------- | --------- | --- |
X =A(cid:2)UT. (14) example,high/lowpowerareassociatedrespectivelywith
low/highfrequencyvariability.Hencelowfrequencyand
In(14)AandU arerespectivelyn×r andr ×p unitary large scale patterns tend to capture most of the variance
matrices, i.e. UTU =ATA=I where r ≤min(n,p) is observedinthesystem.Thenon-degeneracyoftheeigen-
r
the rank of X and I is the identity matrix of order r. spectrumisparticularlyanimportantpropertyandcanbe
r
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1123
veryuseful wheninterpreting EOFs. For example, if two with the same Fourier spectrum as the original data.
ormoreeigenvaluesaredegenerate,i.e.indistinguishable Uncertainties on the data can even be incorporated into
withintheiruncertainties,thenthecorrespondingpatterns theEOFmachinery(e.g.Thacker,1996.)Theuncertainty
domixthepopulationcounterpartsarbitrarily.Moreover, intheeigenvaluesisusefulwhenattemptingtophysically
their actual structures may not be particularly interesting interpret a pattern or in dimension reduction or when
since any linear combination of these patterns is as sig- one is looking for a break in the spectrum (Overland
nificantaseachoneofthem.Therearealwaysexceptions and Preisendorfer, 1982). For example to keep the
as will become clear in later sections, but the message leading three EOFs to reduce the dimensionality it is
should be clear. recommendedthatthethirdeigenvalueshould notbetoo
The investigation of the degeneracy of the covariance close to the fourth or higher eigenvalues.
matrixspectrumrequiresameasureofuncertaintyofeach
eigenvaluethatreflectssamplingandthisisquitedifficult Application
to get. This uncertainty is normally based on asymptotic We have applied EOFs to winter monthly SLP over the
results of the previous eigenvalue problem (10) in the Northern Hemisphere (NH). The data come from the
limitoflargesamples(Anderson,1963).Inpracticethere National Center for Environmental Prediction/National
are mainly two ways to compute the uncertainty of the CenterforAtmosphericResearch(NCEP/NCAR)reanal-
eigenvalues and/or the eigenvectors of S. The first one yses (Kalnay etal., 1996; Kistler etal., 2001). They are
is based on asymptotic results (Girshick, 1939; Lawley, available on a 2.5°×2.5° regular grid, and span the
1956) summarised by a rule of thumb (North etal., periodJanuary1948toDecember2000.Themeanannual
1982): cycle is first calculated by averaging the monthly data
(cid:10) over the years, then subtracted from the data to yield
2
(cid:3)λ2 ∼λ2 SLP anomalies. We are only interested in analysing the
k k n ∗ winter season defined by December to February (DJF).
(cid:3)λ2 Thedataarethereforeobtainedbyconcatenatingthewin-
(cid:3)u k ∼ λ2− k λ2 u j (18) ter monthly means for all years. Finally a weighting by
j k the square root of the cosine of the corresponding lat-
where λ2 is the closest eigenvalue to λ2, and n∗ is itude is applied to each grid point to account for the
j k converging longitudes poleward. The data over the NH
the number of independent observations in the sample,
north of 20°N are used to compute EOFs. Note that the
also known as the effective sample size, or the number
examplespresentedherehavealsobeenusedinHannachi
of degrees of freedom (Trenberth, 1984; Thie´baux and
etal. (2006).
Zwiers,1984).Forex(cid:8)ample(cid:10),the(cid:9)95%confidenceinterval
Figure 1 shows the spectrum of the covariance matrix
of λ2 k is given by λ2 k 1± n 2 ∗ . The effective sample along with their standard errors as given by the first
equation of (18) with sample size n=3×52=156.
size of a time series of length n involves in general
The leading two eigenvalues seem nondegenerate and
the autocorrelation structure of the series. Fo(cid:11)r example,
thesumoftheautocorrelationfunction,1+2 ρ(k), separated from the rest, but overall the spectrum looks
k≥1
in general smooth, which makes truncation difficult.
provides a measure of the decorrelation time, and an
estimate(cid:12)of n∗ is given by (Thie´bau(cid:13)x and Zwiers, 1984); Figure 2 shows the first two EOFs. These EOFs explain
n∗ =n 1+2
(cid:11)
n−1(1−k/n)ρ(k)
−1
.
k=1
Eigenvalue spectrum
Another alternative is to use Monte Carlo simulations,
(seefor example Bjo¨rnssonandVenegas1997). This can 30
be achieved by forming surrogate data by resampling a
part of the data using randomisation. An example would 25
be to randomly select a subsample and apply EOFs,
then select another subsample etc. This operation, which 20
can be repeated many times, yields various realisations
15
of the eigenelements from which one can estimate
the uncertainties. Another example would be to fix a
10
subset of variables then scramble them by breaking the
chronological order then apply EOFs, and so on. Further
5
Monte Carlo alternatives exist to assess uncertainty on
the spectrum of the covariance matrix. One could for
0
example scramble blocks of the data, for example two- 0 10 20 30 40
or three-year blocks of monthly data keeping thus some Rank
parts of the autocorrelation structure, (e.g. Peng and Fife
1996). To keep the whole autocorrelation structure of
the data the phase randomisation method (Kaplan and
Glass, 1995) can be used. The method generates data
)%(
eulavnegiE
Figure1.Spectrum,inpercentage,ofthecovariancematrixofwinter
monthly (DJF) SLP. Verticalbars show approximate 95% confidence
limitsgivenbytheruleofthumb(18).Onlytheleading40eigenvalues
areshown.
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1124
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
(a) EOF1 (21%) Figure 4 shows the autocorrelations of PC1 (4a) and
PC2(4b)ofDJFSLP.Notethatthedataaremonthly,and
notseasonalmeans.Theautocorrelationsindicateashort
|     |     |     | 1   |     |     |     | memory                                 | behaviour |       | with one | or     | two months |     | lag. There |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --------- | ----- | -------- | ------ | ---------- | --- | ---------- |
|     |     |     |     |     |     |     | seemstobeasmallautocorrelationaround24 |           |       |          |        |            |     | monthslag  |
|     |     |     |     |     |     |     | in PC1                                 | (Figure   | 4(a)) | and      | around | 17 months  |     | lag in PC2 |
2
1
|     |     |     |     |     |     |     | (Figure | 4(b)). | From | this limited |     | sample | it is | difficult to |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---- | ------------ | --- | ------ | ----- | ------------ |
1
knowtheexactoriginoftheseautocorrelations.However,
-1
|     |     |     |     |     |     |     | it is possible |       | that the | previous |        | autocorrelation |         | observed |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | -------- | -------- | ------ | --------------- | ------- | -------- |
|     |     |     |     |     |     |     | in PC1         | could | be due   | to the   | effect | of              | El Nino | Southern |
Oscillation(ENSO)cycle,andthatobservedinPC2could
-2
|     |     | -1  |     |     | -1  |     |        |        |            |            |            |             |             |        |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ---------- | ---------- | ---------- | ----------- | ----------- | ------ |
|     |     |     | -2  |     |     |     | be the | effect | of the     | QBO        | (Trenberth | and         | Shin,       | 1984). |
|     |     |     |     |     |     |     | There  | is     | an ongoing | debate     | within     |             | the climate | com-   |
|     |     |     | -3  | -3  |     |     |        |        |            |            |            |             |             |        |
|     |     | 1   |     |     |     |     | munity | on     | whether    | the Arctic |            | Oscillation | (Figure     | 2(a))  |
-4
|     |     |     |     | -2  |     |     | or the   | North | Atlantic       | Oscillation |        | is the | most | physically- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------------- | ----------- | ------ | ------ | ---- | ----------- |
|     |     |     | -2  | -1  |     |     |          |       |                |             |        |        |      |             |
|     |     | 2   |     |     |     |     | relevant | mode  | of variability |             | of the | NH     | SLP. | Because of  |
1 3 1 the nature of the method, this debate cannot be resolved
|     |     |     | 3   | 2   |     |     |       |      |        |      |        |         |            |      |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------ | ---- | ------ | ------- | ---------- | ---- |
|     |     |     |     |     |     |     | using | EOFs | alone. | EOFs | have a | serious | difficulty | when |
2
|     |     |     |     |     |     |     | it comes | to     | interpretation. |                  | For example, |      | because           | of the     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------------- | ---------------- | ------------ | ---- | ----------------- | ---------- |
|     |     |     |     |     |     |     | spatial  | and/or | temporal        | autocorrelation, |              |      | the coherent-like |            |
|     |     |     |     |     |     |     | large    | scale  | EOF patterns    |                  | obtained     | only | reflect           | the effect |
(b) EOF2 (13%)
|     |     |     |     |     |     |     | of the              | correlations |      | of neighbouring |        | grid-points. |                 | Various      |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | ------------ | ---- | --------------- | ------ | ------------ | --------------- | ------------ |
|     |     |     |     |     |     |     | methods             | have         | been | proposed        | to     | ease         | this difficulty | and          |
|     |     |     |     |     |     |     | aid interpretation. |              | In   | this            | review | we present   |                 | two alterna- |
|     |     | 1   | 2   |     |     |     |                     |              |      |                 |        |              |                 |              |
4 1 tives, the first one is familiar to climate researchers and
|     |     | 3   | 5   |     |     |     |                                                  |     |            |     |     |          |     |           |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | ---------- | --- | --- | -------- | --- | --------- |
|     |     |     | 67  |     |     |     | isbasedonrotation,andthesecondone,simplifiedEOFs |     |            |     |     |          |     |           |
|     |     |     | 6   | 3   |     |     | approach,                                        | is  | relatively | new | and | is based | on  | the LASSO |
23
|     |     |     | 5   |     |     |     | approach. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
4
|     |     | 1   | 2   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-1
|     |     |     | 1   |     |     | -1  |     |     |                |     |     |         |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------- | --- | --- |
|     |     |     |     |     |     |     |     |     | SIMPLIFICATION |     |     | METHODS |     |     |
1
|     |     |     |     |     |     | -1  | Rotation       | of  | EOFs              | is perhaps |          | the most    | used    | method      |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------------- | ---------- | -------- | ----------- | ------- | ----------- |
|     | 1   |     |     |     |     |     | in atmospheric |     | science           | due        | in       | part        | to its  | simplicity. |
|     |     |     |     |     |     |     | Simplified     |     | EOFs method       |            | provides | also        | another | useful      |
|     |     |     |     | 1   |     |     | and new        | way | of simplification |            |          | in addition |         | to its nice |
-2
- 1 -3 -1 formulation and natural link to EOFs. Both of these
-1
|     |     |     | -2  |     |     |     | methods | are   | discussed      | below.  | See               | also | Hannachi           | et al.    |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | -------------- | ------- | ----------------- | ---- | ------------------ | --------- |
|     |     |     |     |     |     |     | (2006), | which | is principally |         | devoted           |      | to simplification. |           |
|     |     |     |     |     |     |     | Other   | less  | known          | methods | of simplification |      |                    | have been |
proposed.Thesemethodswillbediscussedbrieflytoward
|     |     |     |     |     |     |     | the end | of  | this section | with | references |     | provided | for the |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---- | ---------- | --- | -------- | ------- |
Figure2.Thefirst(a)andthesecond(b)EOFsofDJFmonthlymean
| SLP. | Positive contours |     | solid, negative | contours | dashed. | EOFs have | interested | readers. |     |     |     |     |     |     |
| ---- | ----------------- | --- | --------------- | -------- | ------- | --------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
beenmultipliedby100.
Rotated EOFs
respectively 21% and 13% of the total (monthly winter) What is it and why?. Spatial orthogonality and tempo-
variance. EOF 1 (2a) shows a high over the North Pole ral uncorrelation of EOFs and PCs respectively impose
| and | two low | centres | over the | Mediterranean-North |     | East |        |     |          |                  |     |     |     |           |
| --- | ------- | ------- | -------- | ------------------- | --- | ---- | ------ | --- | -------- | ---------------- | --- | --- | --- | --------- |
|     |         |         |          |                     |     |      | limits | on  | physical | interpretability |     | of  | EOF | patterns. |
Atlantic and over the North Pacific. This is the familiar This is because physical processes are not independent,
AO mode (Thompson and Wallace, 1998, 2000; Wallace and therefore physical modes are expected in general
and Thompson 2002). EOF2 (2b) shows two separated to be non-orthogonal. As an example, normal modes
centresofoppositesignsovertheNorthPacificandNorth derived from linearised physical models, such as the
East Atlantic respectively. Figure 3 shows the first two etal.,
|     |     |     |     |     |     |     | barotropic | vorticity |     | equation | (Simmons |     |     | 1983) are |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------- | -------- | --- | --- | --------- |
PCs associated with the leading two EOFs. These PCs non-orthogonal. Furthermore, EOFs tend to be depen-
areuncorrelatedatzero-lagbutnot atother lags.A trend dent on the size andshape of the data domain (Richman,
signature canbenotedinboththePCs.Thisisagaindue 1986). For instance, the first EOF pattern tends to have
to the way EOFs process the data. In fact, EOFs do not wavenumber one sitting on the whole domain. The sec-
look for trends, and if there is one then it is likely that it ond EOF, on the other hand, tends to have wavenumber
will be spread over more than one PC. two and be orthogonal to EOF1 regardless of the nature
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1125
EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE
(a) DJF sea level pressure PC1
2
1
1CP
0
−1
−2
|     |     |     | Jan50 | Jan60 | Jan70 | Jan80 | Jan90 |     | Jan00 |     |     |     |
| --- | --- | --- | ----- | ----- | ----- | ----- | ----- | --- | ----- | --- | --- | --- |
Time
(b) DJF sea level pressure PC2
2
1
2CP 0
−1
−2
|     |     |     | Jan50 | Jan60 | Jan70 | Jan80 | Jan90 |     | Jan00 |     |     |     |
| --- | --- | --- | ----- | ----- | ----- | ----- | ----- | --- | ----- | --- | --- | --- |
Time
Figure3.TheleadingtwoscaledPCscorrespondingtotheleadingtwoEOFsofFigure2.
(a) Autocorrelation of PC1 of the physical process involved in producing the data,
|     |     |     |     |     |     | and this | applies in | general | to subsequent |     | EOFs. |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | ------------- | --- | ----- | --- |
1
Tohelpovercomethesedifficultiesandgaineasyinter-
|     |     |     |     |     |     | pretation, | a number | of  | methods | have | been | proposed. |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------- | ---- | ---- | --------- |
0.8
|     |     |     |     |     |     | Among       | these methods, | REOFs,  |        | based     | simply | on rotat- |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------- | ------ | --------- | ------ | --------- |
|     | 0.6 |     |     |     |     | ing the EOF | patterns,      | seems   | to be  | the most  | widely | used      |
|     |     |     |     |     |     | method      | in atmospheric | science | mainly | becauseof |        | its rel-  |
)τ( ρ 0.4
|     |     |     |     |     |     | ative simplicity. | REOF       |     | techniques | have      | been  | adopted |
| --- | --- | --- | --- | --- | --- | ----------------- | ---------- | --- | ---------- | --------- | ----- | ------- |
|     |     |     |     |     |     | by atmospheric    | scientists |     | since      | the early | 1980s | (Horel, |
0.2
|     |     |     |     |     |     | 1981; Richman,  | 1981,               | 1986; | Jolliffe, |          | 1987).  | The tech- |
| --- | --- | --- | --- | --- | --- | --------------- | ------------------- | ----- | --------- | -------- | ------- | --------- |
|     | 0   |     |     |     |     | nique, however, | is                  | much  | older and | was      | known   | in factor |
|     |     |     |     |     |     | analysis        | as factor rotation, |       | and       | has been | applied | exten-    |
−0.2
sivelyinsocialscience(Carroll,1953;Kaiser,1958).The
|     |     |     |     |     |     | main objectives | of  | REOFs | are to: |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ------- | --- | --- | --- |
|     | 0   | 10  | 20  | 30  | 40  |                 |     |       |         |     |     |     |
Lag τ (months)
•
|     |     |     |     |     |     | alleviate | the strong |     | constraints | of  | EOFs, | namely |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- | --- | ----- | ------ |
(b) Autocorrelation of PC2 orthogonality/uncorrelation of EOFs/PCs, and domain
|     |     |     |     |     |     | dependenceof | EOF | patterns(seee.g.Dommengetand |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------------------- | --- | --- | --- | --- |
1
Latif, 2002),
|     |     |     |     |     |     | • obtain | simple structures, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | --- | --- | --- |
0.8
•
|     |     |     |     |     |     | ease the | interpretation |     | of obtained | patterns. |     |     |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ----------- | --------- | --- | --- |
0.6
|     |     |     |     |     |     | Formulation | andcomputation |     | of  | REOFs |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | --- | ----- | --- | --- |
)τ( ρ
0.4
|     |     |     |     |     |     | Rotation       | of the EOF | patterns |                 | can systematically |     | alter    |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | -------- | --------------- | ------------------ | --- | -------- |
|     |     |     |     |     |     | the structures | of         | EOFs.    | By constraining |                    | the | rotation |
0.2
|     |     |     |     |     |     | to maximise | a simplicity |       | criterion | the | REOF   | patterns |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | ----- | --------- | --- | ------ | -------- |
|     | 0   |     |     |     |     | can be      | made simple. | Given | a         | p×m | matrix | U =      |
m
|     |     |     |     |     |     | (u 1 ,u 2 ,...u | m ) of | the leading |     | m EOFs | (or | loadings), |
| --- | --- | --- | --- | --- | --- | --------------- | ------ | ----------- | --- | ------ | --- | ---------- |
−0.2
|     |     |     |     |     |     | the rotation | is formally |     | achieved | by seeking |     | an m×m |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | -------- | ---------- | --- | ------ |
0 10 20 30 40 rotation matrix R to construct the REOFs B according
Lag τ (months)
to:
|     |     |     |     |     |     |     |     | B   | =U R, |     |     | (19) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- |
m
| Figure | 4. Autocorrelation | functions | of  | DJF SLP PC1 | and PC | 2.  |     |     |     |     |     |     |
| ------ | ------------------ | --------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Horizontallinesshowapproximate95%confidencelimits.
|     |     |     |     |     |     | where R     | is either   | R or   | (RT)−1 | depending | on  | the type |
| --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------ | ------ | --------- | --- | -------- |
|     |     |     |     |     |     | of rotation | as detailed | below. | The    | criterion | for | choosing |
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc

1126 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
the rotation matrix R is what constitutes the rotation Because of the orthogonality property (21) required by
algorithm or the simplicity criterion, and is expressed by R, the REOFs matrix also satisfies BTB =I when
m
the maximisation problem: the (unscaled) EOFs are rotated, and the sum of the
squaredelementsofB isconstant.ThereforetheQUAR-
maxf(U R) (20)
m TIMAX simply boils down to maximising the fourth
over a specifiedsubset or class of m×m square rotation order moment of the loadings, hence the term QUAR-
matrices R. The functional f() represents the rotation TIMAX:
 
criterion. Note that besides rotating the EOFs U as in
m (cid:1)m (cid:1)p
(19), one could equally rotate the EOFs scaled by the max  f(B)= 1 b4  (24)
square root of the corresponding eigenvalues, i.e. using mp jk
U (cid:2) , where (cid:2) =(λ ,...,λ ) is the diagonal matrix k=1j=1
m m m 1 m
containingtheleadingsingularvalues.Alternatively,one
Eq (22) or (24) are then to be optimised subject to the
canalsorotatePCsinstead.Variousrotationcriteriaexist
orthogonality constraint (21). VARIMAX is in general
intheliterature(Richman,1986;Harman,1976;Reyment
preferred to the QUARTIMAX because it is slightly
and Jo¨reskog, 1996). Richman (1986), for example, lists
less sensitive to changes in the number of variables
more than ten simplicity criteria. Broadly speaking there
(Richman, 1986), although the difference in practice is
aretwolargefamiliesofrotation:orthogonalandoblique
not significant.
rotations.
b. Oblique rotation
a. Orthogonal rotation
Here the rotation matrix R is chosen to be non-
In orthogonal rotation (Kaiser, 1958; Jennrich, 2001)
orthogonal (Harman, 1976; Kiers, 1994; Jennrich, 2002)
the rotation matrix R in (19) is chosen to be orthogonal, normalised to have unit-length columns, and where R=
and R=R. The problem is to solve (20) subject to the
(RT)−1. The oblique rotation matrix is obtained by
condition:
solving (20) subject to the previous constraints. Among
RRT =RTR =I (21)
m the familiar examples of oblique criteria one finds the
where I is the m×m identity matrix. QUARTIMIN (Carroll, 1953; Harman, 1976), which m
The most well-known and used rotation algorithm is corresponds to the following criterion:
the VARIMAXcriterion(Kaiser,1958). Letus designate
(cid:1)(cid:1)
by b ij , i =1,...p, and j =1,...m, the elements of f(B)= 1 b2 b2 . (25)
the REOFs matrix B in (19), i.e. b =[B] , then the 4 kr ks ij ij r(cid:7)=s k
VARIMAX orthogonal rotation maximises a simplicity
criterion according to: Illustration. We have applied both orthogonal and
     oblique rotations to the (unscaled) EOFs and the EOFs
2

(cid:1)m

(cid:1)p (cid:1)p
 scaled by the corresponding singular values. We have maxf(B)= p b4 − b2   (22)
jk jk therefore four cases to be discussed: (i) orthogonal rota-
k=1 j=1 j=1
tion of EOFs, (ii) orthogonal rotation of scaled EOFs,
(iii)obliquerotationofEOFs,and(iv)obliquerotationof
where m is the number of EOFschosenfor rotation. The
scaled EOFs. Various rotation criteria have been applied,
quantityinsidethesquarebracketsin(22)isproportional
but we focus our discussion on the results obtained from
tothe(spatial)varianceofthesquareoftherotatedvector
b =(b ,...,b )T. Therefore VARIMAX attempts to three criteria, namely VARIMAX, QUARTIMAX, and
k 1k pk
QUARTIMIN. The discussion also includes the effect of
simplify the structure of the patterns by pushing the
loadings coefficients towards zero, or ±1. In some changing the number m of EOFs to be rotated, (see also
Hannachi et al. 2006).
cases, the loadings of the REOFs B are weighted by
The first observation is that orthogonal rotation is the communalities of the different variables (Walsh and
Richman,1981).Thecommunalitiesh2,j =1,...p,are more efficient, computationally, than oblique rotation,
j (cid:11) directly proportional to the sum of squares, m u2 , due to matrix inversion in the latter. Using various
of the loadings for a particular variable. Hence k i = f 1 C j = k rotation criteria and various values of the parameter m,
Diag(U UT)−1/2, then in the weighted or normalised we have found that case (i) and (iii) give virtually the
m m same result. Figure 5 shows a scatter plot of rotated
VARIMAX, the matrix B as used in (22) is simply
loadings using VARIMAX versus QUARTIMIN for
replaced by BC. This normalisation is generally used
m=30. A similar feature has also been obtained with
to reduce the bias toward the first EOF with the largest
other criteria (not shown). This seems to indicate that
eigenvalue.
orthogonal/oblique rotation of (unscaled) EOFs is a
Another familiar orthogonal rotation method is based
robustfeature.Unfortunately,thisisnottrue.Therotated
on the QUARTIMAX criterion. It seeks to maximise the
patterns change as m changes. For example, when we
variance of the patterns:
  rotate 3 EOFs, the NAO and the North Pacific patterns
(cid:1)m (cid:1)p (cid:1)m (cid:1)p 2 emerge as the most prominent patterns with associated
1 1 f(B)=  b2 − b2  . (23) time series having leading variances. As m increases,
mp jk mp jk
k=1j=1 k=1j=1 however,thesefeaturesdisappearprogressivelyinfavour
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on [03/02/2026].
See
the Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1127
EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE
|     |     |     | VARIMAX vs QUARTIMIN |     |     |     |     |     |     |     | (a) REOF1 |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
0.3
0.2
sFOER NIMITRAUQ
-1
0.1
1
|     | 0    |     |     |     |     |     |     |     |     |     | 2     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |      |     |     |     |     |     |     |     |     | 1   | 3     | 1   |     |
|     |      |     |     |     |     |     |     |     |     |     | 4 3 2 |     |     |
|     | −0.1 |     |     |     |     |     |     |     |     | 2 5 |       |     |     |
-2
|     |     |     |     |     |     |     |     |     |     |     |     | -3  | -1  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-1 -2
|     |     |     |     |     |     |     |     |     | -1  | -3  | -4 -4 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
−0.2
|     | −0.2 |     | −0.1 | 0   | 0.1 |     | 0.2 | 0.3 |     | -2  |     | -1  |     |
| --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
-2
-1
VARIMAX REOFs
| Figure | 5. Scatter | plot | of VARIMAX |     | REOFs | versus | QUARTIMIN |     |     |     |     |     |     |
| ------ | ---------- | ---- | ---------- | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- |
REOFsusingm=30EOFs.Scatterwithnegativeslopescorresponds
(b) REOF3
tosimilarREOFsbutwithoppositesign.
| of         | other    | structures | with         | smaller | scales.  | Figures    | 6             | and 7 |     |     |     |     |     |
| ---------- | -------- | ---------- | ------------ | ------- | -------- | ---------- | ------------- | ----- | --- | --- | --- | --- | --- |
| show       | examples | of         | VARIMAX      |         | REOFs    | using      | respectively  |       |     |     |     |     |     |
| m=6        |          | m=20.      |              |         |          |            |               |       |     |     |     |     |     |
|            | and      |            | These        |         | patterns | have       | been selected |       |     |     |     |     |     |
| visually   | so       | to be      | as close     | as      | possible | to         | familiar      | large |     |     |     |     |     |
| scale      | modes    | of         | variability. | Note    | that     | as m       | increases     | the   |     |     |     |     |     |
| patterns   |          | become     | more         | and     | more     | localised. | This          | non-  |     |     |     |     |     |
| invariance |          | of the     | leading      | rotated |          | patterns   | to changes    |       |     |     | -1  |     |     |
|            |          |            |              |         |          |            |               |       |     |     | -1  | -2  |     |
-2
| in       | m can | be explained |                 | by the | fact  | that in    | the | rotation |     |        |     |     |     |
| -------- | ----- | ------------ | --------------- | ------ | ----- | ---------- | --- | -------- | --- | ------ | --- | --- | --- |
|          |       |              |                 |        |       |            |     |          | 1   | -4-5-6 |     |     |     |
| process, | there | is           | no preferential |        | order | or varying |     | weights  |     |        |     |     |     |
|          |       |              |                 |        |       |            |     |          |     | 1      |     | -4  |     |
attached to the EOFs. All the EOFs are equivalent, since 2 - 5 -3 -1
- 2
|     |     |     |     |     |     |     |     |     |     | 2 5 | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
no variance is included, and the final solution is only 3 4 2
4
| dictated | by       | condition | (20).        |     |             |         |             |         |     |     |     |     |     |
| -------- | -------- | --------- | ------------ | --- | ----------- | ------- | ----------- | ------- | --- | --- | --- | --- | --- |
|          |          |           |              |     |             |         |             |         |     | 1   |     | 1   |     |
| To       | overcome |           | the previous |     | difficulty, | the     | alternative | is      |     |     |     |     |     |
| to       | weigh    | the EOFs  | by           | the | square      | root of | the         | associ- |     |     |     |     |     |
ated eigenvalues. In this case the norm-squared of each (c) REOF4
| (scaled)EOFis |     |     | preciselythe |     | varianceofthe |     | correspond- |     |     |     |     |     |     |
| ------------- | --- | --- | ------------ | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
-1
| ing | time | series. | This automatically |     |     | yields | case (ii) | when |     |     |     |     |     |
| --- | ---- | ------- | ------------------ | --- | --- | ------ | --------- | ---- | --- | --- | --- | --- | --- |
1 32
5 4
| the | rotation | is orthogonal, |     | which |     | we discuss | now. | As  |     | 6   |     |     |     |
| --- | -------- | -------------- | --- | ----- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
-1
| would | be            | expected, | this       | case | produces | leading |         | REOFs |     |     | 8   |     |     |
| ----- | ------------- | --------- | ---------- | ---- | -------- | ------- | ------- | ----- | --- | --- | --- | --- | --- |
|       |               |           |            |      |          |         |         |       |     | 6   | 7   | 1   |     |
| that  | are invariant |           | to changes |      | in m.    | This is | because | low   |     | 2 5 |     |     |     |
4
|        |      |            |     |      |        |         |        |      |     | 1 3 | 32  |     | -1  |
| ------ | ---- | ---------- | --- | ---- | ------ | ------- | ------ | ---- | --- | --- | --- | --- | --- |
| ranked | EOFs | contribute |     | less | to the | leading | REOFs. | Note |     |     |     |     |     |
-1
| also | that | because | of orthogonality |     |     | the order | of  | rotated |     | 1   |     |     |     |
| ---- | ---- | ------- | ---------------- | --- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- |
-1
| patterns | is       | provided      | by  | their      | squared        | norms,      | which | play   |     |     |     |     |     |
| -------- | -------- | ------------- | --- | ---------- | -------------- | ----------- | ----- | ------ | --- | --- | --- | --- | --- |
| the      | role     | of associated |     | variances. | These          | ‘variances’ |       | are    |     |     |     |     |     |
| not,     | however, | additive      |     | because    | the associated |             | time  | series | 1   |     |     |     |     |
2 1
| XB                      | are not | uncorrelated. |         | There                      | is            | no non-trivial |              | rota- |     |     |     |     |     |
| ----------------------- | ------- | ------------- | ------- | -------------------------- | ------------- | -------------- | ------------ | ----- | --- | --- | --- | --- | --- |
| tion                    | that    | conserves     | spatial |                            | orthogonality |                | and temporal |       |     |     |     |     |     |
| uncorrelatedness.Figure |         |               |         | 8showstheleadingthreeVARI- |               |                |              |       |     |     |     |     |     |
m=20
| MAX | REOFs | using     |         |     | identified | respectively |               | as  |     |     |     |     |     |
| --- | ----- | --------- | ------- | --- | ---------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- |
| the | NAO,  | the North | Pacific |     | pattern,   | and          | the Scandina- |     |     |     |     |     |     |
vian pattern (Barnston and Livezey, 1987). The same Figure 6. Three VARIMAX rotated EOFs using the leading 6 DJF
result is obtained for the leading QUARTIMAX REOFs. SLP EOFs showing the first (a), the third, NAO, (b), and the fourth,
This invariance property breaks down for low-ranked NorthPacificpattern,(c).Theorderisfixedusingthevariancesofthe
|         |           |     |             |     |      | m=30, |     | corresponding | time | series. Positive | contours | solid, | negative contours |
| ------- | --------- | --- | ----------- | --- | ---- | ----- | --- | ------------- | ---- | ---------------- | -------- | ------ | ----------------- |
| rotated | patterns. |     | For example |     | when |       | the | lead-         |      |                  |          |        |                   |
dashed.Loadingshavebeenmultipliedby100asinFigure2.
| ing       | 15 REOFs |            | are similar | between |       | the two | orthogonal |     |     |     |     |     |     |
| --------- | -------- | ---------- | ----------- | ------- | ----- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
| rotations |          | used here. |             |         |       |         |            |     |     |     |     |     |     |
| For       | the      | last case  | (iv)        | we have | found | thatthe | algorithm  |     |     |     |     |     |     |
runs into convergence problems due to bad conditioning in the orthogonal rotation since orthogonal matrices are
in the matrix inversion process. This does not happen easily obtained using SVD.
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1128
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
| (a) REOF1 |     |     | (a) REOF 1 (m=20) |     |
| --------- | --- | --- | ----------------- | --- |
-1
1 1
-1-2
1
2 2
10
| 1      | -1  |     |     | 10  |
| ------ | --- | --- | --- | --- |
| -1 123 | 1   |     |     |     |
1
|     | 4 3 |     |          | 30    |
| --- | --- | --- | -------- | ----- |
| -1  | -1  |     | -10 5    | 010   |
| 2   |     |     | 2 0 60   | 0 2   |
|     |     |     | 70       | 4 0   |
|     | 1   |     | 10       |       |
|     |     |     | -20 4030 | - 1 0 |
|     | -1  |     |          | - 2 0 |
|     |     |     | -30      | -10   |
1
1 0
|     |     |     | -10 -20 -30 | -   |
| --- | --- | --- | ----------- | --- |
-20
| (b) REOF6 |     |     | (b) REOF 2 (m=20) |     |
| --------- | --- | --- | ----------------- | --- |
10
20
50 3 0
| -2  |     |     |     | 4 0 |
| --- | --- | --- | --- | --- |
30 60
0
|     |     |     | 1 4 80 70 | 10  |
| --- | --- | --- | --------- | --- |
|     |     |     | 0 4050 60 | 20  |
20
30
2
1 0
-10
-4 -1
-2 0
2
-2
2
| 4 2 |     |     | 1   |     |
| --- | --- | --- | --- | --- |
0
| 6 4 |     |     | -10 |     |
| --- | --- | --- | --- | --- |
8
-2
-2
| (c) REOF10 |     |     | (c) REOF 3 (m=20) |     |
| ---------- | --- | --- | ----------------- | --- |
2
| 6   | 2   |     |     |     |
| --- | --- | --- | --- | --- |
| 8   | 4   |     |     |     |
4
8 10
4 6
| 2 -2 |     |     |     |     |
| ---- | --- | --- | --- | --- |
-2
10
0
- 1
2 0
10 2030
| 2   |     |     |     | 60  |
| --- | --- | --- | --- | --- |
0
4
|     |     |     | 10  | 5 0 030 |
| --- | --- | --- | --- | ------- |
20 4 10
-10
-10
-20
Figure 7. Same as in Figure6 but with m=20. The orders of the Figure 8. The leading three VARIMAX REOFs obtained using the
patternsare1(a),6(b),and10(c). leading m=20 EOFsscaledby the square root of the corresponding
eigenvalues.Loadingshavebeenmultipliedby100asinFigure2.
Simplified EOFs
|     |     | (2002) point | out that concentrating | the EOF coefficients |
| --- | --- | ------------ | ---------------------- | -------------------- |
±1
Background. REOFs have been introduced mainly to close to 0 or is not the only possible definition
improveinterpretationthroughobtainingsimplerpatterns of simplicity. For example a pattern with only ones is
than EOFs. Building objective simplicity criteria, how- simple though it could rarely by of much interest in
ever, turns out to be a difficult problem. Jolliffe et al. atmosphericscience.AlthoughREOFsattempttoachieve
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1129
this using a simple and practical criterion they have a In addition, to achieve simplicity the lasso technique
number of difficultieswhichmakethe method quite con- requires the following extra constraint to be satisfied
troversial (Richman, 1986, 1987; Jolliffe, 1987, 1995; (Jolliffe et al., 2003):
Mestas-Nun˜ez, 2000).
When we apply the rotation procedure we are usually
(cid:1)d
||u || = |u |=uTsign(u )≤τ (28)
faced with the following questions: k 1 kj k k
j=1
• how to fix the number of EOFs or PCs to be rotated?
for some tunable threshold parameter τ. In (28)
• what type of rotation, e.g. orthogonal or oblique,
sign(u )=(sign(u ),...,sign(u ))T is the sign of u .
should be used? k k1 kp k
The following properties can be easily verified:
• whichofthelargenumberofsimplicitycriteriashould
be used? and • No solution exists for the optimisation problem
• how to chose the normalisation constraint (Jolliffe,
(26–28) when τ <1.
√
1995)? • any simplified u satisfies ||u ||≤ p
√ k k
• for τ ≥ p, u , k =1,...,p are simply the EOFs.
Although the results of the previous section shed k
some light on which rotation criterion to choose, namely
ThelastpropertyindicatesthatEOFsareaparticularcase
orthogonalrotationofscaledEOFs,thereisstilltheissue
of simplified EOFs.
of non-invariance of the low-ranked rotated patterns for
The numerical solution to Eqs (26)–(28) is presented
large m. A simplification technique that retains some in Trendafilov and Jolliffe (2005) who applied it to a
of the useful properties of EOFs has been proposed by
small problem, and Hannachi et al. (2006) who applied
Jolliffe etal. (2003) as an alternative to rotation. This
ittotheNHSLPasisdonehere.Theapproachoffinding
technique is simplified EOFs and is described next.
the k’th SEOF u is based on integrating the following
k
system of ordinary differential equations (ODEs):
LASSO-based simplified EOFs. Various simplification
techniques have been suggested to obtain simple struc- d
u =(I −u uT)∇F(k)(u ) (29)
tures (e.g. Chapter 11 of Jolliffe 2002). Most of these dt k d k k µ k
techniques attempt to reduce the two stages of rotated
PCA into just one step. Here we discuss a particularly forwardintimefor“sufficiently”longtimeintervalusing
interesting method of simplicity that is rooted in regres- suitably chosen initial conditions (e.g. Hir. and Smale
sion analysis. A common problem that arises in multiple 1974). In Eq (29) the function F µ (k) is defined by:
linear regression is the instability of regression coeffi-
1
cientsbecauseofcolinearityorhighdimensionality. Tib- F (u )= uTSu −µH(uT tanh(γu )−τ) (30)
shirani(1996)hasinvestigatedthisproblemandproposed µ k 2 k k k k
atechniqueknownastheLASSO.TheLASSOapproach
with H(x)= 1 x(1+tanhγx), µ and γ are fixed large
attempts to shrink some regression coefficients exactly 2
positive numbers, and the matrix S given by:
to zero, hence implicitly selecting variables. The same k
idea was adapted in the PCA context by Jolliffe etal. (cid:20) (cid:21) (cid:20) (cid:21)
(cid:1)k−1 (cid:1)k−1
(2003)wholabelledit‘SimplifiedComponentTechnique- S = I − uuT S I − uuT . (31)
LASSO’(SCoTLASS).ForbrevitywerefertotheSCoT- k d l l d l l
l=0 l=0
LASS EOF method as simplified EOFs (SEOFs), but it
should be borne in mind that this is not the only form of Hence the k’th SEOF u is the limit, when t →∞, of
k
simplicity(seeJolliffe2002).Jolliffeetal.(2003)applied the solution to eq (29), i.e. the stationary solution to the
the method to a toy example, and Hannachi etal. (2006) sameequation.Intheapplicationsectionbelowwefollow
appliedit to a moderatelylargeclimate dataset, the same Hannachietal. (2006)towhichthereaderisreferredfor
one as here. more details and further references.
The SEOF method attempts to use the main properties
of EOFs and REOFs simultaneously by successively Application. WehavecomputedtheSEOFsoftheDJF
maximising variance and constraining the patterns to be monthly NH SLP field for various values of the thresh-
orthogonal and simple. Simplicity here means that the old parameter τ from 8 to 30. For a given value of the
loadings of each pattern have either small, i.e. close threshold parameter τ the SEOFs are obtained by inte-
to zero, or large, i.e. close to one, magnitude and gratingeq (29)forwardintimeusingMATLABfunction
no intermediate values. The objective of SEOFs is to ODES15, which can solve stiff ODEs. The constants γ
seek directions u =(u ,u ,...,u )T, k =1,...,p and µ are fixed as in Trendafilov and Jolliffe (2005) and
k k1 k2 kp
maximising: Hannachietal.(2006)to1000and800respectively.The
F(u )=uTSu (26) solution is found to be virtually invariant to changes in
k k k
those parameters. In fact, these parameters are not part
subject to of the problem, and their role is pretty universal, (see
uTu =δ . (27) Hannachi et al. 2006 for computational details). We also
k l kl
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1130
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
|     |     | (a) SEOF1 (τ=8) |     |     |     |     |     | (a) SEOF1 (τ=18) |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
−4
0.03
|     |     | −0.03 | −8 −4 |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.03
124
|     |     | 20  | 8   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 4   |     | 16  |     |     |     |     |     |     |     |     |     |
8 1 6
|     |     | 1               | 2 4  |     |     |     |     |                  |     |     |     |     |
| --- | --- | --------------- | ---- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
|     |     | 0.03            | 0.03 |     |     |     |     |                  |     |     |     |     |
|     |     | (b) SEOF2 (τ=8) |      |     |     |     |     | (b) SEOF2 (τ=18) |     |     |     |     |
0.03
4
2
1 16
|     | 4   | 8   | 8       |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 1   | 20 0.03 |     |     |     |     |     |     |     |     |     |
0 8 6
.0 |     | 3   |     | 12  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4
−
0.03
3
0
0.
−
=18.
Figure 9. The leading SEOF1 (a)and SEOF2 (b)obtained for a Figure10.AsinFigure9butforτ
=8.
| threshold | parameterτ |     | Regions of zeroloadings |     | are shaded. | The |     |     |     |     |     |     |
| --------- | ---------- | --- | ----------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
patternshavebeenmultipliedby100asinFigure2.
|     |     |     |     |     |     | enlargement | compared |      | to Figure | 9.    | When τ      | reaches 26 |
| --- | --- | --- | --- | --- | --- | ----------- | -------- | ---- | --------- | ----- | ----------- | ---------- |
|     |     |     |     |     |     | the leading | SEOFs    | (not | shown)    | start | to converge | to         |
followHannachietal.(2006)bycomputingthefewlead-
|            |       |      |               |     | 5°×5°, | the corresponding |     | E OFs | patterns. | Hannachi | etal. | (2006) |
| ---------- | ----- | ---- | ------------- | --- | ------ | ----------------- | --- | ----- | --------- | -------- | ----- | ------ |
| ing SEOFs, | using | only | a coarse grid | of  |        | and by            |     | √     |           |          |       |        |
≤ 1
using the same example. find that for τ p, the variances of the time series
2
|        |         |     |               |      |     | corresponding |     | to the | leading | two | SEOFs are | not too |
| ------ | ------- | --- | ------------- | ---- | --- | ------------- | --- | ------ | ------- | --- | --------- | ------- |
| Figure | 9 shows | the | leading SEOF1 | (9a) | and | SEOF2         |     |        |         |     |           |         |
(9b) for τ =8. Regions where the loadings are zero are different.Thismayexplainwhythesimplepatternsfound
|         |        |              |       |         |         | by SEOFs | method | appear | combined |     | in a single | pattern |
| ------- | ------ | ------------ | ----- | ------- | ------- | -------- | ------ | ------ | -------- | --- | ----------- | ------- |
| shaded. | Figure | 9(a) clearly | shows | the NAO | pattern | with     |        |        |          |     |             |         |
itsdistinctivedipolarstructure(Hurrell,1996;Thompson when using EOF analysis (Figure 2(a)).
et al., 2000; Hurrell etal., 2003) whereas Figure 9(b) The third SEOF pattern is found to represent the
τ
shows the North Pacific pattern, a monopolar structure Scandinavian √ pattern for smaller than approximately
1
centered over the North mid-Pacific. As τ increases p. Figure 11 shows SEOF3 for τ =12 and τ =16.
2
the shaded regions in Figure 9 shrink and the patterns Forthelattervalueofthethresholdparameterthepattern
become more and more non-local. Figure 10 shows the becomes nearly hemispheric with the emergence of a
leading two SEOFs for τ =18, where one can still see third centre over the North Atlantic basin, and is close
the NAO and North Pacific patterns but with structure to EOF3(notshown). Note in particular the resemblance
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1131
EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE
|     |     | SEOF 3 (τ = 12) |     |     |     |     |     | Ratio var(SPC1)/var(PC1) versus τ |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
1.2
1.1
1
)1CP(rav/)1CPS(raV
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
|     |     |     |     |     |     |     | 5   | 10  |     | 15  | 20  | 25  |     | 30  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Threshold parameter τ
|     |     |     |     |     |     | Figure12.VarianceratioofSPC1tothatofPC1versus |     |     |     |     |     |     | thesimplicity |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
parameterτ.
|     |     |                 |     |     |     | compared   |       | to EOFs           | or REOFs    | when               | the       | number   | of      | EOFs    |
| --- | --- | --------------- | --- | --- | --- | ---------- | ----- | ----------------- | ----------- | ------------------ | --------- | -------- | ------- | ------- |
|     |     | SEOF 3 (τ = 16) |     |     |     | selected   | for   | rotation          | is not      | very               | large.    |          |         |         |
|     |     |                 |     |     |     | Otherforms |       | of simplification |             |                    |           |          |         |         |
|     |     |                 |     |     |     | Various    | other | methods           |             | of simplifications |           |          | have    | been    |
|     |     |                 |     |     |     | proposed   | in    | the PCA           | literature. |                    | Most      | of these | methods |         |
|     |     |                 |     |     |     | impose     | extra | constraints       |             | on the             | variables |          | in a    | similar |
|     |     |                 |     |     |     | manner     | to    | the SEOF          | method.     |                    | In a      | number   | of      | those   |
techniquestheloadingsarerestrictedtobeintegerstaking
|     |     |     |     |     |     | the         | values | 0, and    | ±1 (Hausmann, |        | 1982.) |             | Vines | (2000) |
| --- | --- | --- | --- | --- | --- | ----------- | ------ | --------- | ------------- | ------ | ------ | ----------- | ----- | ------ |
|     |     |     |     |     |     | also        | uses   | a similar | procedure     |        | that   | she labels  |       | simple |
|     |     |     |     |     |     | components. |        | The       | method        | starts | from   | the natural | basis | of     |
thevariables-spaceandproceedsbyorthogonallyrotating
|     |     |     |     |     |     | them | pairwise | such | that | the | variance | of  | the pair | is  |
| --- | --- | --- | --- | --- | --- | ---- | -------- | ---- | ---- | --- | -------- | --- | -------- | --- |
increasedandsimplicitypreserved.Thelatterisachieved
|     |     |     |     |     |     | by choosing |     | angles | that yield | vectors |     | whose | components |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ---------- | ------- | --- | ----- | ---------- | --- |
areproportionaltointegers.SeeSun(2005)foradetailed
analysisofsimplecomponentanalysiswithanaccountof
thevariousalgorithmsused.TheSEOFmethodpresented
|                    |     |              |     |                         |     | above   | is  | rather an | extension    |     | of these | discrete      |     | values |
| ------------------ | --- | ------------ | --- | ----------------------- | --- | ------- | --- | --------- | ------------ | --- | -------- | ------------- | --- | ------ |
|                    |     |              |     |                         |     | methods | in  | that the  | coefficients |     | can      | vary smoothly |     | and    |
| Figure11.SEOF3forτ |     | =12(top)andτ |     | =16(bottom).Thepatterns |     |         |     |           |              |     |          |               |     |        |
havebeenmultipliedby100asinFigure9. notberestrictedtointegers.Green(1977),Bibby(1980),
andJackson(1991)presentanotherwayofsimplification
basedonconsideringtheusualPCs,thenproceedtotheir
| betweenSEOF3correspondingtoτ |     |     |     | =12(Figure | 11)and |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
‘simplification’byroundingthemtothefirstdigit(Green,
REOF3 shown in Figure 6(c). As τ decreases further, 1977;Bibby,1980)andalsototheclosestinteger(Bibby,
| the patterns    | seem    | to             | keep         | their structure | except that     |       |           |             |            |             |                |                    |        |       |
| --------------- | ------- | -------------- | ------------ | --------------- | --------------- | ----- | --------- | ----------- | ---------- | ----------- | -------------- | ------------------ | ------ | ----- |
|                 |         |                |              |                 |                 | 1980; | Jackson,  | 1991).      |            |             |                |                    |        |       |
| they become     | smaller |                | in spatial   | extent,         | and of course   |       |           |             |            |             |                |                    |        |       |
|                 |         |                |              |                 |                 | A     | different | alternative |            | to rotation |                | and simplification |        |       |
| lose variance.  | The     | loss           | in variance, | however,        | is justified    |       |           |             |            |             |                |                    |        |       |
|                 |         |                |              |                 |                 | was   | presented | by          | Van den    | Dool        | etal.          | (2000),            |        | which |
| by the increase |         | in simplicity. |              | Figure 12       | shows the ratio |       |           |             |            |             |                |                    |        |       |
|                 |         |                |              |                 |                 | they  | label     | empirical   | orthogonal |             | teleconnection |                    | (EOT). |       |
between the variances of the times series corresponding Themethodproceedsasf(cid:11)ollows.Thegridpoints isfirst
j
to SEOF1 and EOF1 respectively versus the parameter p corr2(s
|     |     |     |     |     |     | obtained | that | maximises |     |     |     | ,s )var(s |     | ). The |
| --- | --- | --- | --- | --- | --- | -------- | ---- | --------- | --- | --- | --- | --------- | --- | ------ |
τ. Figure 12 indicates that convergence to EOFs starts k=1 j k k
|     | √   |     |     |     |     | first | EOT | is then | obtained | as the | regression |     | coefficient |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------- | -------- | ------ | ---------- | --- | ----------- | --- |
2
| around τ | =   | p.  |     |     |     |         |     |      |         |           |      |         |     |      |
| -------- | --- | --- | --- | --- | --- | ------- | --- | ---- | ------- | --------- | ---- | ------- | --- | ---- |
|          | 3   |     |     |     |     | between | the | grid | s j and | all other | grid | points. | The | next |
SEOF patterns seem to produce invariant features EOTisobtainedinasimilarway,usingtheresidualsfrom
vis-a-vis changes in the threshold parameter for τ < theseparateregressionusedforEOT1,andareorthogonal
| √   |     |     |     |     | √   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   |     |     |     |     | = 1 |     |     |     |     |     |     |     |     |     |
p. Hannachi et al. (2006) propose τ p to be to the previous EOT. The EOT method is not as simple
| 2   |     |     |     |     | 3   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a reasonably good choice, regarding balance between as the other methods of simplification, but Van den Dool
variance maximisation and locality or simplicity. The etal.(2000)arguethatithelpsthephysicalinterpretation
method, however, is more expensive, computationally, of the patterns. Jolliffe (2002) points out that the first
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1132
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
EOTisacompromisebetweenthefirstprincipalvariables The parameter M in Eq (32) is known as windowlength
obtained using the covariance and correlation matrices. or delay parameter. This parameter is also known as
Although simplification methods have been presented embedding dimension, a concept that is rooted in the
asawaytoovercomethedrawbacksofEOFstoyieldper- theoryofdynamicalsystems(e.g.Takens1981),andhas
hapsphysicallyrelevantpatterns,suchasteleconnections, to be chosen beforehand. The lagged covariance matrix
the problem remains, however, whether teleconnections Cofthisnewlyformedmulti-channeltimeseriesisgiven
| exist and | if they | do, | how they | can | be identified |     | (Jolliffe, | by: |     |     |     |     |     |     |
| --------- | ------- | --- | -------- | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
2002; Dommenget and Latif, 2002)? Rotation and other n−(cid:1)M+1
1
|     |     |     |     |     |     |     |     |     |     | C=  |     | w wT | .   | (33) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- |
simplification procedures remain after all simple mathe- n−m+1 t t
| matical | tools that | may | or may | not | speak | the language |     | of  |     |     |     | t=1 |     |     |
| ------- | ---------- | --- | ------ | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
nature.Section6discussespossiblealternativestoevalu-
|               |     |                  |     |     |                        |     |     | Periodic | signals | are then | identified | through | the existence |     |
| ------------- | --- | ---------------- | --- | --- | ---------------------- | --- | --- | -------- | ------- | -------- | ---------- | ------- | ------------- | --- |
| ate EOFsandto |     | identifypossible |     |     | teleconnectionpatterns |     |     |          |         |          |            |         |               |     |
ofpairsofdegenerateeigenvaluesofC,thatareseparated
| from observed |     | climate | data. |     |     |     |     |          |      |        |           |          |                |     |
| ------------- | --- | ------- | ----- | --- | --- | --- | --- | -------- | ---- | ------ | --------- | -------- | -------------- | --- |
|               |     |         |       |     |     |     |     | from the | rest | of the | spectrum. | When the | single-channel |     |
C
|     |     |     |     |     |     |     |     | time series | is  | stationary | the auto-covariance |     | matrix | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | ------------------- | --- | ------ | --- |
EXTENDED EOFS Eq (33) has a Toeplitz structure, that is constant over the
diagonals,andisknowntohaveusefulproperties(seee.g.
Background
|     |     |     |     |     |     |     |     | Graybill | 1969). | The | sample estimate, | however, |     | will not |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | ---------------- | -------- | --- | -------- |
The previous sections have dealt with patterns that max- have an exactly Toeplitz structure unless it is imposed.
imise variance using spatial correlation structures pro- The method can also be applied to nonstationary time
vided by the covariance matrix. The matrix uses only series, (see e.g. Elsner and Tsonis 1996, and Golyandina
simultaneousinformation(intime)betweendifferentgrid et al.2001)forfurtherdetails.Themultivariateextension
points, but forgets about any lagged information. Since of this method yields the EEOFs or MSSA, and is
lagged correlations constitute an important characteristic detailed next. The next two sections provide a technical
feature of climate data, it is important to incorporate this background of EEOFs. In section 4.4 we have chosen
informationintotheanalysis.Animportantmethodusing to apply the method to identify the Madden-Julian
such information is based on extended empirical orthog- oscillation (MJO). This is because the MJO is well
onal function (EEOF). EEOFs constitute an extension studied and well documented in the literature since it
of the traditional EOF technique to deal not only with was first identified by Madden and Julian (1972) using
| spatial- | but also | with | temporal | correlations |     | observed |     | in       |             |     |     |     |     |     |
| -------- | -------- | ---- | -------- | ------------ | --- | -------- | --- | -------- | ----------- | --- | --- | --- | --- | --- |
|          |          |      |          |              |     |          |     | spectral | techniques. |     |     |     |     |     |
weather/climatedata.Themethodwasfirstintroducedby
WeareandNasstrom(1982)whoappliedittothe300-mb
|           |           |     |          |             |       |             |           | Definition | andcomputation |     | of          | EEOFs |        |         |
| --------- | --------- | --- | -------- | ----------- | ----- | ----------- | --------- | ---------- | -------------- | --- | ----------- | ----- | ------ | ------- |
| relative  | vorticity | to  | identify | propagating |       | structures. |           |            |                |     |             |       |        |         |
|           |           |     |          |             |       |             |           | In EEOF    | analysis       | the | atmospheric | state | vector | at time |
| A similar | approach  |     | was      | developed   | later | to          | deal with |            |                |     |             |       |        |         |
|           |           |     |          |             |       |             |           |            | =(x            |     | =1,...,n,   |       |        |         |
dynamical reconstruction of low order chaotic systems t, i.e. x t t1 ,...x tp ), t used in traditional
|     |     |     |     |     |     |     |     | EOF, is | extended | to  | include temporal | information |     | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ---------------- | ----------- | --- | --- |
byBroomheadandKing(1986a,b)whocalleditsingular
systemanalysis(SSA).AtthesametimeFraedrich(1986)
=(x
also used the same approach to compute dimensions x t t1 ,...x t+M−1,1 ,x t2 ,...x t+M−1,2 ,...
| of chaotic | attractors |     | from | climate | data. | SSA | was also |     |     |       |     |     |     |      |
| ---------- | ---------- | --- | ---- | ------- | ----- | --- | -------- | --- | --- | ----- | --- | --- | --- | ---- |
|            |            |     |      |         |       |     |          |     | x   | ,...x | )   |     |     | (34) |
used to find oscillations from climate records (Vautard t,p t+M−1,p
et al.,1992).Itwasextendedtodealwithmultivariate,or
|     |     |     |     |     |     |     |     |     | =1,...,n−M |     | +1. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
multichannel,(MSSA)timeseries(BroomheadandKing, with t The new data matrix now
|          |      |             |     |      |           |      |     | takes the | form |     |    |    |     |     |
| -------- | ---- | ----------- | --- | ---- | --------- | ---- | --- | --------- | ---- | --- | --- | --- | --- | --- |
| 1986a,b) | in a | way similar | to  | EEOF | analysis. | MSSA | (or |           |      |     |     |     |     |     |
x 1
| EEOF) | was applied |     | later by | Kimoto | etal. | (1991) | and |     |     |     |     |     |     |     |
| ----- | ----------- | --- | -------- | ------ | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|       |             |     |          |        |       |        |     |     |     |     |  x |    |     |     |
Plaut and Vautard (1994) to find propagating structures X= 2 
|     |     |     |     |     |     |     |     |     |     |     |  . |    |     | (35) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
.
| from 500-mb |        | heights    | reanalyses. |     |      |      |         |     |     |     | .       |     |     |     |
| ----------- | ------ | ---------- | ----------- | --- | ---- | ---- | ------- | --- | --- | --- | ------- | --- | --- | --- |
| The         | use of | the lagged | information |     | from | time | series, |     |     |     | x n−M+1 |     |     |     |
e.g.laggedauto-covariancematrix,tofindpropagatingor
periodic signals, goes back to the middle of the century It is now clear from (34) that time is incorporated in the
with Whittle (1951) and a few others. The method has statevectorsidebysidewiththespatialdimension.Ifwe
| been applied | to          | observed | time        | series     | first      | by Basilevsky |                 | denote | by  |         |          |         |     |      |
| ------------ | ----------- | -------- | ----------- | ---------- | ---------- | ------------- | --------------- | ------ | --- | ------- | -------- | ------- | --- | ---- |
| and Hum      | (1979)      | to       | find an     | embedded   |            | periodic      | signal          |        |     |         |          |         |     |      |
| i n th e d   | a t a . I n | th e     | o ne -d i m | en s i o n | a l c a se | th e          | p r o c e d ure |        |     |         |          |         |     |      |
|              |             |          |             |            |            |               |                 |        |     | x s =(x | ,x ...x  |         | )   | (36) |
|              |             |          |             |            |            |               |                 |        |     | t       | ts t+1,s | t+M−1,s |     |      |
| i s a s f o  | ll o w s .  | G i ve   | n a s i ng  | le - c h   | a n n e l  | tim e         | s e r i e s w   | ,      |     |         |          |         |     |      |
t
t =1,2,...n,themethodconsistsfirstinconstructingan
=1,2,...n−M +1, then the extended state vector (34) is written in a similar
| M-dimensional |       | time       | series | w t , t |       |     |      |         |                  |     |             |              |     |      |
| ------------- | ----- | ---------- | ------ | ------- | ----- | --- | ---- | ------- | ---------------- | --- | ----------- | ------------ | --- | ---- |
|               |       |            |        |         |       |     |      | form to | the conventional |     | state       | vector, i.e. |     |      |
| using the     | delay | coordinate | as     |         |       |     |      |         |                  |     |             |              |     |      |
|               |       | =(w        |        |         |       | )T. |      |         |                  | =(x | 1,x 2,...,x | p)           |     |      |
|               | w     |            | ,w t+1 | ,...,w  | t+M−1 |     | (32) |         |                  | x   |             |              |     | (37) |
|               |       | t          | t      |         |       |     |      |         |                  | t   | t t         | t            |     |      |
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1133
except that now the elements xk, k =1,...p, of this Thisformisexactlyequivalentto(38)sinceitisobtained
t
grandstatevector(Equation 37)arethemselvestemporal- from (38) by a permutation of the columns as
lagged values. The data matrix X in (36) now takes the
form X 1 =XP (44)
 
x1 x2 ... xp where P =(p ), i,j =1,...Mp, is a permutation
1 1 1 ij
X= . . . . . .  (38) matrix (which is orthogonal, i.e. PPT =PTP =I, and
. . .
x1 x2 ... xp contains exactly 1 in every line and every column and
n−M+1 n−M+1 n−M+1 zeros elsewhere) given by
which is again similar to the traditional data matrix X in
p =δ (45)
(2) except that now its elements are (temporal) vectors. ij i,α
The vector xs in (36) is normally referred to as the (cid:22) (cid:23)
t j
delayed vector obtained from the time series (x t s), t = where α is a function of j given by α =rM + p +1
1,...n of the field value at grid point s. The new data where j −1≡r(p), and [x] is the integer part of x.
matrix(38)isnowoforder(n−M +1)×pM whichis The covariance matrix (39) represents a conventional
significantly larger than the original matrix dimension. version based on the grand data matrix (38). This is the
We suppose that X in (38) has been centered and trajectorymatrixmethod(BroomheadandKing,1986a,b;
weighted. The covariance matrix of (37) is: Ghilet al.,2002).One couldalsocompute analternative
grand block ‘covariance’ matrix T=(T ) whose blocks
  ij
C 11 C 12 ... C 1p T ij ,i,j,=1,...p representlaggedcovariancesbetween
(cid:1) = n−M 1 +1 XTX=    C . .
.
21 C . .
.
22 ... C . .
.
2p    g an ri d d V p a o u i t n a t r s d ( i 19 a 9 n 4 d ) w j. ho T c h o is ns v id e e r r s e io d n th i e s lo u n s g ed est b p y os P si l b au le t
segment of each channel (grid point) to compute the
C C ... C
p1 p2 pp (39) elements of each block T ij . The use of this (Toeplitz)
where each C , 1≤i,j ≤p is a lagged covariance version to compute EEOFs can result in a big matrix,
ij
matrix between gridpoint i and gridpoint j, given by: which can be computationally expensive to diagonalise.
The conventional (trajectory) version, however, can use
n−(cid:1)M+1 SVD efficiently particularly when the sample size n is
1
C = xiTxj. (40) much smaller than the original number of variables p. ij n−M +1 t t
t=1 EEOFs are the EOFs of the extended data matrix (35)
or (38), i.e. the eigenvectors of the grand covariance
Other alternatives to compute C ij also exist and they matrix (cid:1) givenin(39).Theycanbeobtaineddirectlyby
are related to the way the lagged covariance between computing the eigenvalues/eigenvectorsof (39). Alterna-
two time series is computed (see e.g. Priestley 1981 and tively, one can use SVD of the grand data matrix X in
Jenkins and Watts 1968). If the multivariate time series (38) in a similar way to (14). Note that now we have
is stationary, then the population version of each block d =MP new variables, i.e. the number of columns of
matrixof(39)issymmetricToeplitz.Thesampleversion the grand data matrix. The SVD of (38) yields:
C from (39) is nearly symmetric Toeplitz for large
ij
sample size. The symmetric grand covariance matrix (cid:1) X=V(cid:9)UT (46)
is not in general Toeplitz because the different blocs
represent covariances between different pairs of grid where the d×d matrix U =(u )=(u ,u ,...,u )
ij 1 2 d
points.Analternativeformofthedatamatrixisprovided represents the matrix of the Mp extended EOFs or right
by writing the state vector (34) in the form singularvectorsofX.Thediagonalmatrix(cid:9)containsthe
singular values θ ,...θ of X, and V =(v ,v ,...,v )
1 d 1 2 d
x t =(x t1 ,...x t,p ,x t+1,1 ,...x t+1,p ,... isthematrixoftheleftsingularvectorsorextendedPC’s
where the k’th extended PC is v =(v (1),...,v (n−
x t+M−1,1 ,...x t+M−1,p ) (41) M +1))T. These extended EOFs k and P k Cs can be k used
to filter the data by removing the contribution from
that is
nonsignificant components and also for reconstruction x t =(x t ,x t+1 ,...,x t+M−1 ) (42) purposes as detailed below
wherex =(x ,...,x )isthestatevectorattimet,t =
t t1 tp Data filtering and oscillation reconstruction
1,...n−M +1. Hence the matrix (38) now takes the
TheextendedEOFsU canbeusedasafilterexactlylike
following alternative form, used by Weare and Nasstrom
EOFs. For instance the SVD decomposition (46) yields
(1982):
the expansion of each row x of X in (38)
t
 
x x ... x
X 1 = . . .
1
. . .
2
. . .
M
 (43) xT =
(cid:1)d
θ v (t)u (47)
t k k k
x n−M+1 x n−M+2 ... x n k=1
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

1134 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
for t =1,...n−M +1, or in terms of the original Ghiletal.,2002).Thereconstructedcomponentscanalso
variables x , see Eq (42), as be restricted to any subset of the eigen elements of the
t
grand data matrix (38). For example to reconstruct the
(cid:1)d time series associated with oscillatory eigen elements,
xT = θ v (t)uj (48)
t+j−1 k k k i.e. a pair of degenerate eigenvalues, the subset K in the
k=1
sum (51) is limited to that pair.
for j =1,...M, and where The reconstructed multivariate time series y t , t =
1,...n, can represent the reconstructed (or filtered)
uj k =(u j,k ,u j+M,k ,...,u (p−1)M,k )T. (49) valuesoftheoriginalfieldattheoriginalpgridpoints.In
general, however, the number of grid points is too large
Note that the expression of the vector uj depends on the to warrant an eigen-decomposition of the grand data, or
k
covariance, matrix. In this case a dimension reduction
formofthedatamatrix.Theonegivenabovecorresponds
to (38), whereas when the data matrix X 1 is used in (46) of the data is first applied by using say the leading p 0
one gets PCs and then applying a MSSA to these retained PCs.
In this case the dimension of X becomes (n−M +1)×
uj k =(u (j−1)p+1,k ,u (j−1)p+2,k ,...,u jp,k )T (50) Mp 0 , which may be made considerably smaller than the
original dimension. To get the reconstructed space-time
Note also that when we filter out higher EEOFs, expres- field one can then use the reconstructed PCs (RPCs) in
sion (48) is to be truncated to the required order d 1 <d. conjunction with the p 0 leading EOFs.
Theexpansion(48)isexactbyconstruction.However, EEOFs can be efficient in detecting propagating struc-
very often one wants to truncate it by keeping a much tures. However, there are cases where the interpretation
smaller number of EEOFs for filtering purposes. This of individual EEOFs can be difficult and should be done
happens for instance when one reconstructs the field with care (Chen and Harr, 1993). This happens partic-
components from a single EEOF, or a pair of EEOFs ularly when the data contain a strong standing wave.
corresponding for example to an oscillation. When this Monahan et al. (1999) show that if the lag chosen in
happens,theobtainedexpansiondoesnotgiveacomplete EEOF analysisistoo closeto thefirstzeroof thesample
picture. This is because when (48) is truncated to a autocorrelationfunctionofthestandingwavetimeseries,
smaller subset K of EEOFs giving: then the wave signal obtained from EEOF can be sub-
(cid:1) stantially degraded and the interpretation can be difficult
yT = θ v (t)uj, (51) and misleading.
t+j−1 k k k
k in K
Application to outgoing long waveradiation
wherey =(y ,...,y )isthefilteredorreconstructed
t t,1 t,p
statespacevector,thenoneobtainsamultivaluefunction. The EEOF method is applied here to identify the MJO.
For example, for t =1 and j =2, one gets one value The MJO, an eastward propagating planetary-scale wave
of y and for t =2 and j =1 one gets another value of tropical convective anomalies, is a well-established
t,1
of y . This also occurs with single channel SSA. This dominant mode of intra-seasonal tropical variability, and
t,1
occursbecauseEEOFshavetimelaggedcomponents.To hence constitutes a convenient test-bed. The oscillation
get a single reconstructed value we can simply take the has a quite broad band with a period between about 40
average of those multiple values, but one could equally and 60 days (Knutson and Weickmann, 1987; Hendon
construct a ‘better’ weighted average. The number of and Salby, 1994; Madden and Julian, 1994). It has been
multiple values dependson the value of time t =1,...n identifiedfromvariousfieldssuchaszonalanddivergent
(thesenumberscanbeobtainedbyconstructinganM ×n wind, SLP, and OLR in the tropics (Madden and Julian,
array A=(a ) with entries a =t −j +1, then all 1972; Kiladis and Weickmann, 1992), and here we jt jt
entries that are nonpositive or greater than n−M +1 choose to use OLR. For details on the mechanisms
aretobeequatedtozero,andfinallyforeachtime t take involved in MJO the reader is referred, for example,
all the indices j with positive entries).The reconstructed to Hendon and Salby (1994), Matthews (2000), and
variables using a subset K of EEOFs are then easily Krishnamurthi et al. (2003). The OLR data used here
obtained from (51) by come from NCEP/NCAR reanalyses over the tropical
 (cid:11) (cid:11) region from 30°S to 30°N. This analysis focuses on a
 1 t
fo (cid:11) r
j t =
1
1
≤ (cid:11) t
K
≤
θ k
M
v k (
−
t −
1
j +1)uj k 5
D
-
e
y
c
e
e
a
m
r
b
p
e
e
r
r
,
io
2
d
00
o
0
f
.
d
F
a
i
i
g
ly
ur
d
e
a
1
ta
3
f
s
r
h
o
o
m
ws
1
t
J
h
a
e
nu
O
a
L
ry
R
, 1
fi
9
e
9
ld
6
o
to
n
3
2
1
5
1 M θ v (t −j +1)uj December 1996. Note the low-value regions particularly
yT = M j=1 K k k k
t 
n−
fo
1
r
t +
M
1
≤
(cid:11)
t
j M
≤
=t−
n
n
−
+M
M
(cid:11)
+
K
1
θ k v k (t −j +1)uj k
o
co
v
n
e
v
r
e
t
c
h
ti
e
on
w
,
a
a
r
n
m
d t
p
o
oo
a
l,
le
a
s
n
ser
ar
e
e
x
a
ten
o
t
f
o
l
v
ar
e
g
r
e
th
a
e
nd
Am
in
a
t
z
e
o
n
n
si
i
v
an
e
for n−M +2≤t ≤n and tropical African regions. The OLR data are not very
(52) homogeneous, and have a quite complicated variability
Note that these reconstructions can also be obtained in as well as seasonality. To illustrate this complication,
a least square sense (see, e.g. Vautard etal., 1992, and Figure 14 shows the OLR time series at four different
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1135
315
298
281
30° N 264
247
230
0° 213
196
179
30° S 0° 60° E 120° E 180° E 120° W 60° W 0° 162
145
128
111
94
Figure13.OLRdistribution(w/m2)overthetropicsonthe25-Dec-1996.
300
200
100
)2−mw(
RLO
OLR (Equator, 122.5°E)
300
200
100
)2−mw(
RLO
OLR (Equator, 20°W)
300
200
100
)2−mw(
RLO
OLR (Equator, 117.5°W)
400
300
200
100
01/01/96 01/01/97 01/01/98 01/01/99 01/01/00 01/01/01
Time
)2−mw(
RLO
OLR (30°N, 40°E)
Figure14.TimeseriesofOLR(wm−2)atfourdifferentlocations.
locations. A clear indication of nonstationarity of the winter time compared to other seasons. Before applying
timesseriesisobvious.Noteforexamplethehighvalues EEOF analysis, the data were first subjected to an EOF
at the equator and 122.5°E in northern winter 1997/98. analysistoreducethedimensionofthedata.Theleading
This period correspondsto a strong El-Nin˜o eventwhere 10 EOFs/PCs of the anomaly field with respect to the
theconvectionshiftseastwardtothemid-Pacificallowing long term average (climatology) were retained for the
more long wave radiation to be lost to space over the analysis. Figure 15 shows the leading EOF mode. This
maritime continent. A decrease of OLR accompanied by pattern explains about 15% of the total variability and
a strong variability can also be seen during the same is associated with the seasonal cycle. Figure 15 clearly
period at 20°W on the Equator (Figure 14). This is due indicates that the seasonal cycle is mostly explained by
to the lower surface pressure over the Tropical Atlantic the Inter Tropical Convergence Zone (ITCZ) and some
ocean during El-Nin˜o, compared to normal conditions, monsoonal activities.
see e.g. Webster and Chang (1988) or Holton (1992, Thefirst10EOFs/PCsusedfortheEEOF/MSSAanal-
Figure 11.10.) Note also the strong seasonal component ysis together explain about 32% of the total variability.
at 30°N, with a particular stronger variability in the A window length corresponding to M =80 days is used
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1136
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
5
4
3
30° N
2
1
0°
0
−1
−2
30° S
|     |     |     | 0°  | 60° E |     | 120° E  | 180° E | 120° W |     | 60° W | 0°  | −3  |     |     |
| --- | --- | --- | --- | ----- | --- | ------- | ------ | ------ | --- | ----- | --- | --- | --- | --- |
−4
−5
−6
Figure15.TheleadingEOFofOLRanomalies.Unitsarearbitrary.
|     |     |     |     |     |     |     | length | of  | the seasonal |     | cycle. Despite |     | this, the | first two |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------ | --- | -------------- | --- | --------- | --------- |
Eigenvalue spectrum
extendedPCs(EPCs)showapairofsinewavesperfectly
)%( eulavnegiE
|     | 10  |     |     |      |     |       | inquadrature,andrepresenttheseasonalcycle.Figure |             |            |                 |                |              |                   | 17         |
| --- | --- | --- | --- | ---- | --- | ----- | ------------------------------------------------ | ----------- | ---------- | --------------- | -------------- | ------------ | ----------------- | ---------- |
|     |     |     |     |      |     |       | shows                                            | in          | fact the   | raw PC1         | along          | with         | the reconstructed |            |
|     | 5   |     |     |      |     |       | or                                               | smoothed    | PC1.       | The             | reconstruction |              | is based          | on (52)    |
|     |     |     |     |      |     |       | using                                            | the         | leading    | 5 EPCs.         |                |              |                   |            |
|     | 0   |     |     |      |     |       | Beside                                           |             | the annual | cycle,          | the            | (degenerate) |                   | fourth and |
|     | 0   | 10  | 20  | 30   |     | 40 50 |                                                  |             |            |                 |                |              |                   |            |
|     |     |     |     |      |     |       | fifth                                            | eigenvalues |            | constitute      | also           | another      | oscillatory       | pair       |
|     |     |     |     | Rank |     |       | corresponding                                    |             | to         | the semi-annual |                | cycle.       | This degeneracy   |            |
|     |     |     |     |      |     |       | can                                              | be seen     | by using   | the             | rule of        | thumb        | (18) but          | without    |
Figure16.Spectrumofthegrandcovariancematrix(39).Approximate
|     |     |     |     |     |     |     | serial | correlation. |     | The | left panel | of  | Figure | 18 shows |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --- | ---------- | --- | ------ | -------- |
standarderrorsarederivedfrom(18)usinganeffectivesamplesizeof
|     |     |     |     |     |     |     | a time | plot | of  | EPC4 | and EPC5 | whereas |     | the phase |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | ---- | -------- | ------- | --- | --------- |
116.
|     |           |           |             |       |      |            | diagram |             | of EPC4    | versus | EPC5    | is shown | in    | the right |
| --- | --------- | --------- | ----------- | ----- | ---- | ---------- | ------- | ----------- | ---------- | ------ | ------- | -------- | ----- | --------- |
|     |           |           |             |       |      |            | panel   | of          | Figure 18. | The    | figure  | clearly  | shows | the semi- |
| to  | construct | the grand | data matrix | (38). | This | choice was |         |             |            |        |         |          |       |           |
|     |           |           |             |       |      |            | annual  | oscillation |            | (SAO)  | in OLR. | The      | phase | diagram   |
motivatedbythedesiretocapturetheMJOidentifiedfirst (rightpanel)alsoshowstheSAOwithslightirregularities
byMaddenandJulian(1971).Thischoicealsoavoidsthe due to interannual variability. The next oscillatory pair
problem of interpretation in the presence of a standing corresponds to the 8th and 9th eigenvalues (Figure 16).
wave (Monahan etal., 1999). The extended (grand) data This pair of (nearly) equal eigenvalues corresponds to
| matrix | is       | then factorised | using                 | SVD. | Figure | 16 shows          |     |          |      |     |             |     |          |          |
| ------ | -------- | --------------- | --------------------- | ---- | ------ | ----------------- | --- | -------- | ---- | --- | ----------- | --- | -------- | -------- |
|        |          |                 |                       |      |        |                   | the | familiar | MJO, | and | corresponds | to  | a period | of about |
| the    | spectrum | of the          | grandcovariancematrix |      |        | (cid:1) (39). The | 50  | days.    |      |     |             |     |          |          |
standard errors are obtained using (18) with a heuristic Figure 19 shows extended EOF 8 along 10°N as a
effectivesample size of 116, correspondingto a decorre- functionoftimelag.Thissortofdiagramwherethespace
lation lag of 15 days. andtimeaxesareshownisknownasHo¨vmollerdiagram.
The first two eigenvalues of the spectrum (Figure 16) Figure 19 shows clearly the eastward moving oscillation
correspond to the oscillation of the seasonal cycle. They with an average phase speed around 7°/day, making
donotlooknearlyequalandwellseparatedfromtherest the wave travel from west to east in roughly 50 days,
s−1
of the spectrum, however, and this is due to the choice i.e. approximately 9 m as observed in Knutson and
of the window length, which is much smaller than the Weickmann (1987). This is also comparable to the speed
Raw and reconstructed PC1
0.03
0.02
0.01
1 CP
0
−0.01
−0.02
−0.03
−0.04
|     |     | 01/01/96 |     | 01/01/97 |     | 01/01/98 |     | 01/01/99 |     |     | 01/01/00 |     |     |     |
| --- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | --- | -------- | --- | --- | --- |
Time
Figure17.TimeseriesofrawandreconstructedPC1.
Copyright2007RoyalMeteorologicalSociety
Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1137
0.05
0
−0.05
01/01/96 01/01/98 01/01/00
Time
CP
dednetxE
Extended PCs 4 and 5
0.05
0
−0.05
−0.05 0 0.05
5
CP
dednetxE
EPC4 vs EPC5
Extended PC 4
Figure18.TimeplotofEPC4(−)andEPC5(−)(leftpanel)andphasediagramofEPC4versus EPC5(rightpanel).
80 90
75
70
60
60 45
30
50
15
40 0
−15
30
−30
20
−45
−60
10
−75
−90
0 50 100 150 200 250 300 350
Longitude
emiT
Extended EOF 8 along 10°N
Figure19.ExtendedEOF8along10°Nasafunctionoftimelag.Unitsarbitrary.
of the Kelevin wave, obtained as a radiating response 8th EEOF/EPC. The figure shows clearly the oscillation
and propagating away from the convective anomaly, by with varying amplitude. Note in particular the strong
HendonandSalby(1994).Figure 20showsthetime plot oscillationduringwinter1997versus theweakoscillation
oftheextendedPCs8and9alongwiththephasediagram fromwintertoearlyautumn1998.Thesamebehaviouris
of EPC 8 versus EPC 9. The EPCs are oscillating in also observed in the phase diagram in the RPC 6 versus
quadrature, with a period of about 50 days and with RPC 7 (Figure 22).
varying intensity. The power spectrum of EPC8 (not Since EOF analysis does not focus on a particular
shown) peaks around 50 days with a slight broad band frequency band, one would expect MJO to project
structure. onto more than one PC. In fact, MJO is found to
The MJO can be found in the reconstructed PCs project onto various PCs but with differing energies
using the extended EOFs/PCs. Figure 21, for example, (amplitudes). For instance SSA analysis of single PCs
shows a time plot of the reconstructed PC2 using the reveals that MJO is mostly present in higher PCs, e.g.
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1138
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
|     |     |     | Extended PCs 8 and 9 |     |     |     |     |     |     | EPC8 vs EPC9 |     |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
0.06
0.06
0.04
0.04
|     |     | CP dednetxE |     |     |     |     | 9 CP dednetxE | 0.02 |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
0.02
0
0
−0.02
−0.02
−0.04
−0.04
|     |     | −0.06 |     |      |       |     |     | −0.06 |       |               |     |      |     |     |
| --- | --- | ----- | --- | ---- | ----- | --- | --- | ----- | ----- | ------------- | --- | ---- | --- | --- |
|     |     | −0.08 |     |      |       |     |     | −0.08 |       |               |     |      |     |     |
|     |     |       |     |      |       |     |     | −0.1  | −0.05 |               |     |      |     |     |
|     |     | Jan96 |     |      | Jan97 |     |     |       |       |               | 0   | 0.05 | 0.1 |     |
|     |     |       |     | Time |       |     |     |       |       | Extended PC 8 |     |      |     |     |
Figure20.ExtendedPCs8and9(leftpanel)andphasediagramofEPC8versus EPC9(rightpanel).
x 10−3
Reconstructed PC2 from extended EOF 8
8
6
4
2
2 CPR
0
−2
−4
−6
|     |     | 01/01/96 |     | 01/01/97 |     | 01/01/98 |     | 01/01/99 |     |     | 01/01/00 |     |     |     |
| --- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | --- | --- | -------- | --- | --- | --- |
Time
Figure21.ReconstructedPC2usingextendedEOF/PC8.
RPC6 versus RPC7 The reconstructed or filtered PCs allow a reconstruc-
|     | 0.015 |     |     |     |     |     | tion  | of  | the original | space-time |     | OLR    | field.        | Figure 24 |
| --- | ----- | --- | --- | --- | --- | --- | ----- | --- | ------------ | ---------- | --- | ------ | ------------- | --------- |
|     |       |     |     |     |     |     | shows | a   | Ho¨vmoller   | diagram    |     | of the | reconstructed | OLR       |
0.01
|     |     |     |     |     |     |     | field | from | 3 March, | 1997 | to 14 | May, | 1997, at | 5°N using |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | -------- | ---- | ----- | ---- | -------- | --------- |
theMJO-relatedextendedEOFs/PCs8and9.Therecon-
0.005
|     |     |     |     |     |     |     | structed |     | PCs 1–8 | (Figure | 23) | are used | in  | conjunction |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | ------- | --- | -------- | --- | ----------- |
7CPR
|     |     |     |     |     |     |     | with | the | EOFs as | in (17), | but | with the | sum | truncated to |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------- | -------- | --- | -------- | --- | ------------ |
0
theleading8EOFs,togettheMJOreconstructedfield.It
−0.005 is very important to note here that a similar diagram, but
|     |       |     |     |     |     |     | using                                               | the    | raw data, | does     | not | reveal any | feature, | and the |
| --- | ----- | --- | --- | --- | --- | --- | --------------------------------------------------- | ------ | --------- | -------- | --- | ---------- | -------- | ------- |
|     | −0.01 |     |     |     |     |     | picture(notshown)looksnoisyandfeatureless.Itisclear |        |           |          |     |            |          |         |
|     |       |     |     |     |     |     | from                                                | Figure | 24        | that MJO | is  | triggered  | around   | 25–30°E |
−0.015 over the African jet region. It reaches its mature stage
|     |     | −0.02 −0.01 |     | 0   | 0.01 | 0.02 |      |     |        |       |        |        |        |            |
| --- | --- | ----------- | --- | --- | ---- | ---- | ---- | --- | ------ | ----- | ------ | ------ | ------ | ---------- |
|     |     |             |     |     |      |      | over | the | Indian | ocean | in the | Bay of | Bengal | and starts |
RPC6
todecaythereafter.TheMJObecomesparticularlydamp
near150°Eovertheconvectiveregioninthewarmpool.
| Figure | 22. | Phase diagram | of reconstructed | PC6 | versus | reconstructed |        |     |       |          |            |     |        |            |
| ------ | --- | ------------- | ---------------- | --- | ------ | ------------- | ------ | --- | ----- | -------- | ---------- | --- | ------ | ---------- |
|        |     |               | PC7.             |     |        |               | Figure | 24  | shows | also the | dispersive |     | nature | of the MJO |
withastrongerphasespeedduringthegrowthphasecom-
|           |                  |                    |             |            |              |           | pared | to  | that observed   |     | during | the decay | phase. |     |
| --------- | ---------------- | ------------------ | ----------- | ---------- | ------------ | --------- | ----- | --- | --------------- | --- | ------ | --------- | ------ | --- |
| PCs       | 6 and            | 7. This            | observation | is also    | revealed     | from      |       |     |                 |     |        |           |        |     |
| analysing |                  | the reconstructed  |             | PC’s using | the          | extended  |       |     |                 |     |        |           |        |     |
| EOFs/PCs  |                  | 8 and 9 associated |             | with the   | oscillation. | This      |       |     |                 |     |        |           |        |     |
|           |                  |                    |             |            |              |           |       |     | COMPLEX/HILBERT |     |        | EOFS      |        |     |
| is        | well illustrated | in                 | Figure      | 23, which  | shows        | the first |       |     |                 |     |        |           |        |     |
Background
| 8   | reconstructed | PCs. | Reconstructed |     | PCs 5–8 | are the |     |     |     |     |     |     |     |     |
| --- | ------------- | ---- | ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
most energetic components representing MJO. Note in Conventional EOF analysis can be applied to a single
particular the weak projection of MJO onto the first PC, space-time fieldor a combination of fields.EOF analysis
which represents only the seasonal cycle. finds “stationary” patterns in the sense that they are not
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1139
EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE
Reconstructed PC1 to 8 from extended EOFs 8 & 9
RPC1
RPC2
RPC3
|     |     | 0.01 |     |     |     |     |     |     |     |     | RPC4 |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
RPC5
RPC6
RPC7
RPC8
0.005
8 ot 1CPR
0
−0.005
−0.01
|     |     | 01/01/96 |     | 02/01/96 |     | 03/01/96 |     | 04/01/96 | 05/01/96 |     |     |     |     |
| --- | --- | -------- | --- | -------- | --- | -------- | --- | -------- | -------- | --- | --- | --- | --- |
Time
Figure23.ReconstructedPCs1to8usingextendedEOFs/PCs8and9.
Reconstructed OLR using extended EOFs 8 and 9 at 5°N (wm−2)
25
10/05/97
20
02/05/97
|     |     | 24/04/97 |     |     |     |     |     |     |     |     | 15  |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
16/04/97
10
08/04/97
5
31/03/97
emiT
0
23/03/97
|     |     | 15/03/97 |     |     |     |     |     |     |     |     | −5  |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 07/03/97 |     |     |     |     |     |     |     |     | −10 |     |     |
27/02/97
−15
19/02/97
−20
11/02/97
|     |     | 03/02/97 |     |     |     |     |     |     |     |     | −25 |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |          | 0   | 50  | 100 | 150 | 200 | 250 | 300 | 350 |     |     |     |
Longitude
Figure24.ReconstructedOLRfieldusingreconstructedEOFs/PCs1to8showninFigure23.
evolving. It yields a varying time series for any obtained and y t will yield the same covariance, i.e.
| EOF pattern,      | which          | means       | that         | the spatial | EOF     | pattern |                |          |             |         |         |           |         |
| ----------------- | -------------- | ----------- | ------------ | ----------- | ------- | ------- | -------------- | -------- | ----------- | ------- | ------- | --------- | ------- |
|                   |                |             |              |             |         |         |                | =cov(x   |             | )=cov(x |         |           |         |
|                   |                |             |              |             |         |         |                | ρ xy     | t ,y        | t       | π(t)    | ,y π(t) ) | (53)    |
| will only         | decrease       | or increase | in           | magnitude   | whereas | the     |                |          |             |         |         |           |         |
| spatial structure |                | remains     | the same.    | Because     | EOFs    | are     |                |          |             |         |         |           |         |
|                   |                |             |              |             |         |         | where          | π is any | permutation | of      | the set | of time   | indices |
| based on          | (simultaneous) |             | covariances, |             | the way | time    | is {1,2,...n}. |          |             |         |         |           |         |
arranged is irrelevant. In fact, if x and y , t =1,...n, This automatically means that any propagating struc-
|     |     |     |     | t   | t   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aretwo univariate time seriesthen any permutation of x ture in the field will not be captured by EOFs. We have
t
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc

1140 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
seen in the previous section that EEOFs can extractsuch λ2,...λ2. The complex amplitude of the kth EOF is the
1 p
information in the time domain by analysing a relatively kth complex principal component (CPC)e , and is given
k
large data matrix. In addition, one has to fix a priori by:
the lag-window. There are also other ways, such as POP e =Uu ∗ (58)
k k
analysis (e.g. von Storch and Zwiers 1999), that can find
these structures. Here we review another method simi- This immediately yields the non-correlation between the
lar to EOF analysis but based on the complexified field. CPCs:
The method does not explicitly involve the lagged infor- e ∗Te =λ2δ . (59)
k l k kl
mation, hence avoiding the use of a similar grand data
matrix to that of EEOFs, and also avoiding the problem
Complex EOFs and associated complex PCs can also be
of choosing the lag-window. obtainedusingtheSVDofU.AnyCEOFu hasapattern
k
It is known that any wave can be expressed using
amplitude and phase. The phase and amplitude at each
complex representation as:
grid are obtained using the real and imaginary parts of
the loadings.
x(t)=aeiωt+φ (54)
ThismethodofdoingCEOFsseemstohavebeenorig-
inally appliedbyKunduandAllen(1976)tothevelocity
where a is the wave amplitude and ω and φ are respec-
field of the Oregon coastal current. The conventional
tively its frequency and phase shift (at the origin). Com-
CEOFs are similar to conventional EOFs in the sense
plex empirical orthogonal functions (CEOFs) are based
that time ordering is irrelevant, and hence the method
on this representation. There are, in principle, two ways
is mostly useful to capture covarying spatial patterns
to perform complex EOFs, namely ‘conventional’ com-
between the two fields.
plexEOFsand‘Hilbert’EOFs.Whenwedealwithapair
of associated climate fields then conventional complex
Single field. If one is dealing with a single field
EOFs are obtained. HEOFs correspond to the case when x =(x ,...,x )T, t =1,2...n, such as sea surface
wedealwithasinglevariable,i.e.singlefield,andwhere t t1 tp
temperature,andoneisinterestedinpropagatingpatterns
we are interested in finding propagating patterns. In this
one canstill use the conventional complex EOFsapplied
case the field has to be complexified by introducing an
to the complexified field obtained from a pair of lagged
imaginary part, which is a transform of the actual field.
variables (x t ,x t+τ ) for some chosen lag τ. The complex
field is defined by:
Conventional complex EOFs
Pairs of scalar fields. The method is similar to conven- y t =x t +ix t+τ . (60)
tional EOFs except that it is applied to the complex
field obtained from a pair of associated variables such
This is a natural way to define a homogeneous complex-
as the zonal and meridional components u and v of the
ified field using lagged information. The corresponding
windfieldU=(u,v)(KunduandAllen,1976;Hardyand
complexdatamatrixdefinedfrom(60)isthengivenatat
Walton, 1978; Salstein etal., 1983; Brink and Muench, eachgridpoints l andeachtimet byY tl =(x tl +ix t+τ,l ).
1986;vonStorchandZwiers,1999;Preisendorfer,1988). The obtained complex data matrix Y =(Y ) can then be
The wind field U =U(t,s), defined at each location s, tl
tl l l submitted to the same complex EOF analysis as in the
l =1,...p,andtimet,t =1,...n,canbewrittenusing
previous section.
a compact complex form as:
The obtained CEOFs provide the propagating struc-
tures and the corresponding CPCs provide the phase
U =u(t,s)+iv(t,s)=u +iv . (55)
tl l l tl tl information. This procedure is based on the choice of
the lag time τ, which reflects the characteristic time of
Thecomplexcovariancematrixisobtainedusingthedata
thepropagatingfeature.Ingeneral,however,thisparame-
matrix U=(U ), and is given by:
tl terisnotpreciselyknown,andrequiressomeexperience.
Thechoiceofthisparameterremains,inpractice,subject
1
S = U∗TU, (56) tosomearbitrariness.Toavoidthisdifficultyinchoosing
n−1
the lag in the time domain, the Hilbert transform pro-
The elements s , k,l =1,...p, of S in (56) are given videsanalternative,basedonphaseshiftinthefrequency
kl
by: domain. This is presented next.
(cid:1)n
1
s = U∗ U (57) kl n tk tl Complex Hilbert EOFs
t=1
Frequency domain EOFs. It appears that the earliest
where (∗) is the complex conjugate operator. The introduction of complex EOFs in an atmospheric context
(complex) covariance matrix (56) is Hermitian, i.e. dates back to the early seventies with Wallace and
S∗T =S, and is therefore diagonalisable. The matrix Dickinson on frequency domain EOFs (FDEOFs). Their
has therefore a set of orthonormal complex eigenvectors workstimulated theintroductionlaterofHEOFs,andwe
U =(u ,...u ), and a real non-negative eigenspectrum start by reviewing FDEOFs first. The spectrum gives a
1 p
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1141
measure of the contribution to the variance across the reddish, FDEOF analysis may be cumbersome in prac-
whole frequency range. EOF analysis in the frequency tice (Horel, 1984). This is particularly the case if the
domain (Wallace and Dickinson, 1972; Wallace, 1972; power spectrum of an EOF is spread, for example, over
Johnson and McPhaden, 1993; see also Brillinger 1981 a wide frequency band, requiring an averaging of the
for details) attempts to analyse propagating disturbances cross-spectrumoverthiswidefrequencyrange,wherethe
by concentrating on a specific frequency-band allowing theory behind FDEOFs is no longer applicable (Wallace
thus the decomposition of variance in this band while and Dickinson, 1972). This difficulty has resulted in the
retaining phase relationships between locations. methodbeingabandonedinclimateresearchinfavourof
FDEOFs are based on performing an eigenanalysis of HEOFs described next.
thecross-spectrummatrixcalculatedinasmallfrequency
band. Let u(ω) be the Fourier transform (FT) of the Complex Hilbert EOFs. An elegant alternative to
(centered) field x t , t =1,...n at frequency ω, i.e. FDEOFs is the complex EOFs in the time domain
introduced into atmospheric science by Rasmusson etal.
(cid:1)n
u(ω)= √ 1 x e −iωt (61) (1981)usingHilbertsingulardecomposition.Themethod
n t was refined later by Barnett (1983) and applied to
t=1
the monsoon (Barnett, 1984a,b), atmospheric angular
The cross-spectral matrix at ω is (cid:14) (ω)=u(ω)u(ω)T, momentum (Anderson and Rosen, 1983), the QBO in xx northern hemispheric SLP (Trenberth and Shin, 1984),
and can be written in terms of the lagged covariance
andcoastaloceancurrents(MerrifieldandWinant,1989).
matrix
(cid:1)n−τ The method is based on the Hilbert transform and is
1
S xx (τ)=
n
x t xT t+τ (62) therefore referred to as HEOF analysis.
t=1 Let x
t
=(x
t1
,...,x
tp
)T, t =1,...n, be a scalar field,
with Fourier representation:
as:
(cid:1) (cid:1)
(cid:14) xx (ω)= S xx (τ)e −iωτ =(cid:14) x R x (ω)+(cid:14) x I x (ω). (63) x t = a(ω) cosωt +b(ω) sinωt (66)
τ ω
The real part of the cross-spectrum, (cid:14)R(ω), is the where a(ω) and b(ω) are vector Fourier coefficients.
xx co-spectrum, and the imaginary part, (cid:14)I (ω), is the Since propagating disturbances require complex repre- xx
quadrature spectrum. Note that the covariance matrix of sentation as in (54), Eq (66) can be transformed to yield
the field satisfies the general (complex) Fourier decomposition:
(cid:28) (cid:28)
S =
ωN
(cid:14) (ω)dω =2
ωN
(cid:14) R (ω)dω, (64) y =
(cid:1)
c(ω) e −iωt (67) xx xx t
−ωN 0 ω
where ω N = 2(cid:3) 1 t is the Nyquist frequency and (cid:3)t is where precisely Re(y t )=x t , and c(ω)=a(ω)+ib(ω).
the time interval between observations. Therefore the The new complex field y =(y ,...y )T can therefore
t t1 tp
spectrum gives a measure of the contribution to the be written as:
variance across the whole frequency range. The average y =x +iH(x ). (68)
t t t
of the cross-spectral matrix over the frequency band
[ω ,ω ] is given by
0 1 The imaginary part of y is given by:
t
(cid:28)
ω1
(cid:1) C = (cid:14) (ω)dω (65)
xx H(x )= b(ω)cosωt −a(ω)sinωt, (69)
ω0 t
ω
and provides a measure of the contribution to the
covariance matrix in that frequency band. and is precisely the Hilbert transform, or quadrature
Now since waves are coherent structures with consis- function of the scalar field x and is seen to represent
t π
tent phase relationship at various lags, and given that a simple phase shift by in time. In fact, it can be seen
2
FDEOFs represent patterns that are uniform across a thattheHilberttransform,consideredasafilter,removes
frequency band, the leading FDEOF provides coherent the zero frequency without affecting the modulus of all
structures with most wave variance. The FDEOFs are the others, and is as such a unit gain filter. Note that
thenobtainedastheEOFsofC,(seeBrillinger1981)for if the time series (66) contains only one frequency then
moredetails.JohnsonandMcPhaden(1993)haveapplied the Hilbert transform is simply proportional to the time
FDEOFs to study the spatial structure of intraseasonal derivative of the time series. Therefore, locally in the
Kelvin wave structure in the Equatorial Pacific ocean. frequency domain H(x ) provides information about the
t
They identified coherent wave structures with periods of rate of change of x with respect to time t. In formal
t
59–125 days. Because most spectra of climate data look terms the Hilbert transform of a continuous time series
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of Sao
Paulo
-
Brazil,
Wiley
Online
Library
on [03/02/2026].
See
the Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

1142 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
x(t) (Thomas, 1969; Brillinger, 1981) is defined by the The HEOFs u , k =1,...p, are then obtained as the
k
convolution eigenvectors of the Hermitian covariance matrix
(cid:28)
(cid:1)n
1 x(u) 1
H(x(t))=
π t −u
du (70) S
yy
=
n
y
t
y ∗
t
T =2(S
xx
+iSH(x)x ), (75)
k=1
where the integral is taken to mean the Cauchy principal where SH(x)x is the cross-covariance matrix between
value. In the discrete case the Hilbert transform can be H(x ) and x . They can be obtained also as the right
t t
derived, in time domain, by applying a rectangular rule complex singular vectors of the data matrix Y =(y ).
tk
to (70) to yield (Kress and Martensen, 1970; see also The uncorrelated complex principal components (CPCs)
Weideman, 1995) z , for k =1,...p, are then obtained similarly to (58).
k
From this decomposition we also get the spatial ampli-
2 (cid:1)∞ x(t +(2k+1)h)) tude and phase functions respectively:
H(x(t)) ≈ (71)
π k=−∞ 2k+1 a k =u k • (cid:29) u ∗ k =Dia (cid:30) g(u k u ∗ k T)
Im(u )
where h is the step size. When Eq (71) is applied to a θ k =atan k (76)
Re(u ) discrete time series x , t =0,±1,..., one gets (see also k
t
Bloomfield and Davis, 1994; and von Storch and Zwiers where the vector product and division are performed
1999): component-wise, and where Re() and Im() represent
respectively the real and imaginary parts. Similarly, one
H(x )= 2 (cid:1)∞ x t+2k+1 also gets the temporal amplitude and phase functions as:
t π 2k+1
k=−∞ b =z •z ∗ =Diag(z z ∗T)
(cid:1) k k (cid:29)k (cid:30) k k
2 1 = π 2k+1 (x t+2k+1 −x t−2k−1 ). (72) φ k =atan Im(z k ) , (77)
k≥0 Re(z k )
The function θ gives information on the relative phase. In practice, various methods exist to compute the finite k
For “simple” fields, its spatial derivative provides a
Hilbert transform. For a scalar field x of finite length
t measure of the local wavenumber. Its interpretation
n, the Hilbert transform H(x ) can be estimated using t for moderately complex fileds/waves can be difficult
the discret(cid:22)e F(cid:23)T (69) in which ω becomes ω
k
= 2π
n
k ,
(Wallace, 1972), and can be made easier by applying a
k =1,... n 2 . Alternatively, H(x t ) can be obtained by priorfiltering(Barnett,1983).Alsoforsimplewaves,the
truncatingtheinfinitesuminEq (72).Thistruncationcan time derivative of the temporal phase gives a measure of
also be written using a convolution or a linear filter as the instantaneous frequency. Note that the phase speed
(see e.g. Hannan, 1970): of the wave at time t and position x can be measured by
θ
k(x).
φ
(cid:1)L k T (t h ) e covariance matrix S in (75) can be shown to be
H(x t )= α k x t−k (73) related to the cross spectrum yy matrix
k=−L
(cid:1)(cid:1)n−k
1
with the filter weights (cid:14) yy (ω)= n y t+τ y ∗ t Teiωτ (78)
τ t=1
2 πk
α = sin2 . (74) according to:
k kπ 2
(cid:28) (cid:28)
ωN ωN
Barnett (1983) found that 7≤L≤25 provides adequate S yy = (cid:14) yy (ω)dω =4 (cid:14) xx (ω)dω (79)
values for L. For example for L=23 the frequency −ωN 0
response function is a band pass filter with periods Because the covariance matrix S is only related to
xx
between 6 and 190 time units with a particular excel- the co-spectrum (cid:14)R, it is clear that conventional EOFs
xx
lent response obtained between 19 and 42 time units do not take into consideration the quadrature part of
(Trenberth and Shin, 1984). The Hilbert transform has the cross-spectrum matrix. Using therefore the cross-
also been extended to vector fields, i.e. two or more spectrum matrix, as given by (79), it is seen that HEOFs
fields, through concatenation of the respective complexi- generalise conventional EOFs.
fiedfields(Barnett,1983).Another interestingmethod to It is also clear from (79) that HEOFs are equiva-
compute Hilbert transform of a time series is presented lent to FDEOFs with the cross-spectrum integrated over
byWeideman(1995),usingaseriesexpansioninrational all frequencies. Note that the frequency band of inter-
eigenfunctions of the Hilbert transform operator (70). est can be controlled by prior smoothing. Horel (1984)
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on [03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1143
EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE
pointsoutthatHEOFscanfailtodetectirregularlyoccur- (a) January-mean zonal wind (ms−1)
| ring progressive |            | waves | (see | also   | Merrifield | and    | Winant |     | 1   |     |     |     |     | 50  |
| ---------------- | ---------- | ----- | ---- | ------ | ---------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| 1989).           | Merrifield | and   | Guza | (1990) | have       | showed | that   |     |     |     |     |     |     |     |
40
| complex     | EOF | analysis       | in the | time | domain       | HEOFs | is not |     |     |     |     |     |     | 30  |
| ----------- | --- | -------------- | ------ | ---- | ------------ | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
| appropriate | for | non-dispersive |        | and  | broad-banded |       | waves  |     |     |     |     |     |     | 20  |
)bm( erusserP 10
| inwavenumber(cid:3)κ                                   |     | relativetothelargestseparationmea- |     |     |     |     |     |     |     |     |     |     |     | 10  |
| ------------------------------------------------------ | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sured(arraysize(cid:3)x).InfactMerrifieldandGuza(1990) |     |                                    |     |     |     |     |     |     |     |     |     |     |     | 0   |
(seealsoJohnsonandMcPhaden1993),identified(cid:3)κ(cid:3)x 50 −10
−20
| as the | main | parameter | causing |     | spread | of propagating |     |     | 100 |     |     |     |     |     |
| ------ | ---- | --------- | ------- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
−30
variabilityintomorethanoneHEOFmode,andthelarger
|                |     |             |     |      |          |     |           |     | 250   |             |     |           |      | −40 |
| -------------- | --- | ----------- | --- | ---- | -------- | --- | --------- | --- | ----- | ----------- | --- | --------- | ---- | --- |
| the parameter, |     | the smaller | the | data | variance | is  | captured. |     |       |             |     |           |      |     |
|                |     |             |     |      |          |     |           |     | 500   |             |     |           |      | −50 |
|                |     |             |     |      |          |     |           |     | 1000  |             |     |           |      | −60 |
|                |     |             |     |      |          |     |           |     | −90 S | −60 S −30 S |     |           |      |     |
| Application    |     |             |     |      |          |     |           |     |       |             | EQ  | 30 N 60 N | 90 N |     |
Latitude
| In this | section | we  | apply | HEOFs | to  | the QBO | using |     |     |     |     |     |     |     |
| ------- | ------- | --- | ----- | ----- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
stratospheric zonal winds. The section is divided into (b) July-mean zonal wind (ms−1)
|                  |     |        |       |     |          |     |          |     | 1   |     |     |     |     | 100 |
| ---------------- | --- | ------ | ----- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| two subsections. |     | In the | first | we  | describe | the | data and |     |     |     |     |     |     |     |
90
| the zonal | wind, | and in | the second |     | subsection | we  | present |     |     |     |     |     |     |     |
| --------- | ----- | ------ | ---------- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
80
70
the application.
60
|     |     |     |     |     |     |     |     |     | )bm( erusserP 10 |     |     |     |     | 50  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
40
| Structure | of  | the zonal | wind. | The | data | used | here are |     |     |     |     |     |     |     |
| --------- | --- | --------- | ----- | --- | ---- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
30
| taken from | the | European | Reanalyses |     | (ERA40), |     | which |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ---------- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|            |     |          |            |     |          |     |       |     | 50  |     |     |     |     | 20  |
10
| come from | the         | European |          | Centre | for         | Medium | Range     |     |     |     |     |     |     |     |
| --------- | ----------- | -------- | -------- | ------ | ----------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
|           |             |          |          |        |             |        |           |     | 100 |     |     |     |     | 0   |
| Weather   | Forecasting |          | (ECMWF), |        | and consist |        | of tropo- |     |     |     |     |     |     | −10 |
spheric and stratospheric monthly zonal wind. The data 250 −20
|              |     |           | 2.5°×2.5° |     |            |     |         |     |     |     |     |     |     | −30 |
| ------------ | --- | --------- | --------- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| are provided | on  | a regular |           |     | horizontal |     | grid on |     | 500 |     |     |     |     | −40 |
23 vertical pressure levels from 1000 mb to 1 mb. The 1000 −50
|           |     |        |         |      |     |          |       |     | −90 S | −60 S −30 S |     |           |      |     |
| --------- | --- | ------ | ------- | ---- | --- | -------- | ----- | --- | ----- | ----------- | --- | --------- | ---- | --- |
|           |     |        |         |      |     |          |       |     |       |             | EQ  | 30 N 60 N | 90 N |     |
| data span | the | period | January | 1958 | to  | December | 2001. |     |       |             |     |           |      |     |
Latitude
| Stratosphericanduppertropospheric |     |     |     |     | zonalwindstendto |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
benearlyzonallysymmetric.Wehavethereforefocussed
Figure25.ClimatologyofECMWFzonalmeanzonalwindforJanuary
only on the zonal-mean zonal wind, which we also refer (a), and July (b). The period of observation spans the years 1958
| to (for simplicity) |      | as     | zonal        | wind hereafter. |       |           |         |     |     | throughto2001. |     |     |     |     |
| ------------------- | ---- | ------ | ------------ | --------------- | ----- | --------- | ------- | --- | --- | -------------- | --- | --- | --- | --- |
| Zonal               | wind | in the | stratosphere |                 | has a | different | pattern |     |     |                |     |     |     |     |
of variability to that in the troposphere for various These stratospheric winds have been known since the
reasons, not least the fact that the stratosphere is a 19th century when the German meteorologist A. Berson
free atmosphere, i.e. far from land/sea influence, e.g. found them in 1908 through balloon measurements, and
friction;addtothisthesmallerdensityofthestratosphere, were known as Berson westerlies (Baldwin et al., 2001).
and the forcing effect of vertically propagating Rossby It was only in the 1950s that alternating winds were
and gravity waves. Figure 25 shows the climatology known to exist (Palmer, 1954; Graystone, 1959). These
of the zonal wind for January (25a) and July (25b). changesinstratosphericwindsaremerelyduetoseasonal
| Various | features | can | be noted | from | Figure | 25. | First, the | variations. |     |     |     |     |     |     |
| ------- | -------- | --- | -------- | ---- | ------ | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
tropospheric upper westerly jets can be seen in both To remove the effect of seasonality, we first calculate
| hemispheres | around |     | 250 mb. | In  | January, | the | Northern |     |             |        |       |         |            |      |
| ----------- | ------ | --- | ------- | --- | -------- | --- | -------- | --- | ----------- | ------ | ----- | ------- | ---------- | ---- |
|             |        |     |         |     |          |     |          | the | mean annual | cycle, | which | is then | subtracted | from |
Hemispheric (NH) jet is only slightly stronger than the data to give the anomalies. When seasonal variations
its Southern Hemispheric (SH) counterpart. In July, are removed, the picture becomes different. Figure 26
however, the NH jet has weakened and the SH jet shows the variance of the zonal wind anomalies over the
becomes much stronger. The SH jet is more active and observed period. Most of the variance is concentrated
| stronger | than | the NH | one due | in  | part to | the absence |     | of     |          |             |      |      |               |     |
| -------- | ---- | ------ | ------- | --- | ------- | ----------- | --- | ------ | -------- | ----------- | ---- | ---- | ------------- | --- |
|          |      |        |         |     |         |             |     | around | a narrow | latitudinal | band | from | approximately |     |
boundary layer friction caused by land/mountains. In the 15°S to 15°N, and extending from around 70 mb up to
stratosphere,however,theflowisentirelydifferent.Here the 1 mb level. This region is of great importance to cli-
one can see both the easterly and the westerly flows. mate researchers working on the stratosphere. Figure 27
During NH winter, stratospheric westerly flow is over shows a time-height plot of the zonal wind anomalies at
most extratropical NH and shows basically the polar the Equator from January 1994 to December 2001.
vortex whereas SH stratospheric flow is mostly easterly. Acleardownwardpropagatingsignalcanbeseenfrom
During NH summer the picture is reversed. Again, Figure 27. The propagation region is between around
over the SH, stratospheric westerly reaching 100 m/s is 3 mb and 70 mb, which is the approximate height of
much stronger than its NH analogue (around 40 m/s). the tropopause at the equator. The descent speed is
Stratospheric easterlies, on the other hand, have nearly variable and is roughly between 1 and 1.4 km/month.
thesamemagnitude,around50 m/sonbothhemispheres. The alternating wind region at any given vertical level
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc

1144 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
1 301
251
10 201
151
50
100 101
250
51
500
1000 1
−90 S −60 S −30 S EQ 30 N 60 N 90 N
Latitude
)bm(
erusserP
Zonal wind anomalies variance (m2/s2)
Figure26.Varianceofmonthlyzonalmeanzonalwindanomaliesfor
theobservedperiod.
1 42
36
30
24
10 18
12
6
50 0
100 −6
−12
250 −18
500 −24
1000 −30
Jan 92 Jan 94 Jan 96 Jan 98 Jan 00
Time
)bm(
erusserP
Eigenvalue spectrum
100
80
60
40
20
0
0 5 10 15 20 25 30
Rank
Zonal wind anomalies (m/s)
Figure27.Ho¨vmollerplotofequatorialzonalmeanzonalwindanoma-
lies at various vertical levels for the period January 1992–December
2001.
between 3 mb and 70 mb also varies, with a period
between about 24 and 34 months. This quasi-oscillation
has become known as the QBO, a term that was coined
by Angell and Korshover (1964), but the quasi-biennial
periodicity and the downward propagation were only
discoveredalittleearlierbyEbdon(1960)andReedet al.
(1961). For reviews of the QBO, see Maruyama (1997)
and Labitzke and van Loon (1999), and Baldwin et al.
(2001) and references therein.
Hilbert EOF analysis of zonal wind. Since most vari-
abilityoftheQBOisconcentratedaroundtheEquatorwe
have focussed on the mean zonal wind anomalies over
the latitudinal band between 15S and 15N at all pres-
surelevels.TheHilberttransformeddataareobtainedby
computing the Hilbert transform of the field at each grid
point, then forming the complexified field according to
Eq (68).TheHilberttransformiscomputedusingEq (69)
via afastFT, whichwefoundmore efficient,interms of
CPU time, than the time domain transform (Eq 73). The
eigenvalues spectra and corresponding eigenvectors are
computed using the SVD (Eq 14) of the complex data
)%(
eulavnegiE
Figure 28. Spectrum of the covariance matrix S yy, Equation(75), of
zonalmeanzonalwindanomalies.Verticalbarsrepresentapproximate
95% limits using the rule of thumb (18) with a heuristic sample size
of100.
matrix Y obtained from the complexified field (68). The
CEOFs and corresponding CPCs are respectively given
bytheleftandrightcomplexsingularvectorsofthecom-
plex data matrix Y.
Figure 28showsthespectrumofthecovariancematrix
S = 1 YY∗T,Eq (75),whereonlytheleading30eigen-
yy n
values, expressedin percentagerepresentedvariance,are
shown.Theuncertaintiesontheeigenvaluesareobtained
using the rule of thumb (18) with a heuristic sample size
of 100. It is difficult to talk about the number of degrees
of freedom here because of the strong autocorrelation
due to the presence of the QBO cycle, but the point here
is simply to stress the leading role of the first eigen-
value. It is clear that the first eigenvalue, to which we
restrict our discussion here, is well separated from the
restofthespectrumandexplainsasubstantial amountof
variance. Figure 29 shows the real (29a) and the imag-
inary (29b) parts of CEOF1 respectively. The leading
CEOF (Figure 29) is composed of a pair of patterns in
quadrature, an indication of the propagating nature of
the patterns as is shown later using the corresponding
complex principal component CPC1. The direction of
propagation is also given by the axis linking the low
and high centers of actions.
Figure 30 shows the real and imaginary parts of the
leading CPC (30a), the phase portrait (30b) of CPC1
and the power spectrum of its real part (30c). The
real and imaginary parts are in quadrature and show
a near periodic signal (Figure 30(a),(b)) reflecting the
propagation of the corresponding pattern. The period is
also shown in the power spectrum (Figure 30(c)) to be
around30–32 months. Notethat,forthisparticularcase,
ifaconventionalEOFanalysiswereperformedinstead,a
degenerate leading pair of eigenvalues would have been
obtained, and whose EOFs would be similar to those
showninFigure 29,andsimilarlyforthePCs.Ingeneral,
however,thismightnotbethecaseparticularlywhenthe
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1145
1 12
10
8
6
10
4
2
50 0
−2
100
−4
250 −6
500 −8
1000 −10
−15 S 15 N
Latitude
)bm(
erusserP
(a) CEOF1 (real part) of zonal wind
1 12
10
8
6
10
4
2
50 0
−2 100
−4
250 −6
500 −8
1000 −10 −15 S 15 N
Latitude
)bm(
erusserP
on the other hand, tends to be not very easy to interpret
(Wallace, 1972; Barnett, 1983). Here, however, because
of the unambiguous wave propagation the interpretation
ismadeeasy.Figure 31(b)showsbandedstructuresfrom
1 mb down to around 50 mb, below which there is no
propagation.
Thebandedstructurebetween1 mbandaround50 mb
indicates the direction of propagation of the disturbance
wherethephaseofthewavechangesbetween−180° and
+180° in the course of a complete cycle. There are two
main regions; the first one is between 1 mb and around
5 mb and corresponds to a first cycle, and the second
one is between 5 mb and 25 mb and also corresponds
to another cycle. These apparent cycles are associated
withsmalldisturbancesthatcanbeseenintherawzonal
(b) CEOF1 (imaginary part) of zonal wind
wind anomalies (Figure 27) and give the impression that
thewavegrowsanddecaysinthe firstregionthengrows
and decays again in the second region.
Similarly, the temporal amplitude and phase have also
been computed according to Eq (77). Figure 32 shows
the temporal amplitude (32a) and temporal phase (32b)
of CPC1for the period January1992 to December2001.
Thetemporalamplitude (Figure 32(a))givesinformation
on how the wave amplitude varies with time, see also
the phase portrait (Figure 30(b)). It can be seen, for
example from Figure 32(a) that the amplitude is largest
in the middle of the wave life cycle. The temporal phase
(Figure 32(b)), on the other hand, gives information on
the phase of the wave of the zonal wind anomalies as
Figure29.Real(a)andimaginary(b)partsofcomplexEOF1ofzonal a function of time. For nearly every (quasi-biennial) life
meanzonalwind. cycle the phase is nearly quasi-linear, whose (constant)
slope, or time derivative provides a measure of the
scaleofthepropagatingfeatureisnotwellseparatedfrom instantaneous frequency.
the rest. The first complex EOF/PC can be used to filter the
Table I shows the percentage of the cumulative vari- propagating QBO signal. Figure 33 shows the filtered
ance accounted for by the leading one to ten eigenvalues anomalies using the leading CEOF/CPC for the period
of the EOFs and CEOFs, respectively. This Table can be January 1992 to December 2001. The downward prop-
used to compare the efficiency of the CEOF method at agating signal is now clear, with a speed of roughly
reducing the dimension of the data to that of the EOF 1 km/month. The wave amplitude varies slightly with
method, particularlyfor the few leading patternsbecause time. One can also note sometimes that the propagat-
of the existence of a propagating structure. One recalls ingbandscanhavemorethanonemaximum,leavingthe
that the time coefficients of EOFs are uncorrelated but impression that the downward propagating disturbance
not at non-zero lags. For example, the first two conven- can grow and decay more than once, a point that has
tional PCs will be lagged correlated, hence EOFs would been noted earlier, and which yields the actual structure
fail at efficiently reducing the data dimension compared of the spatial phase (Figure 31(b)).
to CEOFs when using the same number of EOFs and
CEOFs, when there is a propagating feature. Note, how-
ever,thatthe CEOFsaretwice asbig. Soingeneral,e.g.
OTHER EXTENSIONS OF EOFS
with no propagating disturbance, CEOFs would be less
efficient than EOFs unless they carry at least twice the We have only discussed a relatively small number of
information on average. the many techniques related to EOF analysis, but we
Spatial amplitude and phase of the leading CEOF are have concentrated mainly on those that are most useful
computedfollowingEq (76).Figure 31showsthespatial in atmospheric science. The EOF method has also been
amplitude (31a) and the spatial phase (31b) of CEOF1. extended to deal with cyclostationarity. This is the case
Figure 31(a) shows a clear indication of the maximum when the data contain for example a seasonal cycle. A
wave activity around 25 mb on the Equator. It also cyclostationary EOF method was presented by Kim and
shows the asymmetry in the amplitude gradient, which Huang (1996) and Kim and North (1999). The method
is stronger in the lower part of the region where the is based on EOFs of concatenated vector amplitudes
propagationisinhibited.Thespatialphase(Figure 31(b)), obtainedfromaFT of thedata. Jolliffe (2002)points out
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

1146 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
0.06
0.04
0.02
0
−0.02
−0.04
−0.06
Jan60 Jan65 Jan70 Jan75 Jan80 Jan85 Jan90 Jan95 Jan00
1
CPC
(a) Complex PC1: Real and imaginary parts
(b) Phase portrait of CPC1
0.08
0.06
0.04
0.02
0
−0.02
−0.04
−0.06
−0.1 −0.05 0 0.05 0.1
)1
CPC(
gamI
0.05
0.04
0.03
0.02
0.01
0
0 50 100 150 200
Real (CPC 1) Period (months)
rewoP
real
imag
(c) Spectrum of real(CPC1)
Figure30.RealandimaginarypartsofcomplexPC1(a),phaseportraitofCPC1(b),andpowerspectrumoftherealpartofCPC1(c).
TableI. Thecumulativeexplainedvariance(explainedvarianceoftheEOFsandHEOFsofthezonalmeanzonalwindanomalies.
Leading eigenvalues 1 2 3 4 5 6 7 8 9 10
EOFs 39.4 76.8 84.5 90.0 92.3 93.9 95.0 96.0 96.6 97.0
HEOFs 71.32 81.3 89.0 91.8 93.7 94.9 95.8 96.6 97.3 97.8
thatthemethodislesstransparentinitsjustificationthan analysis is to fix the atmospheric variables and perform
cyclostationary POP analysis (Blumenthal, 1991; von EOF analysis on the other pair. This yields the so-called
Storchet al.,1995.)KimandWu(1999)describeanother S-modeanalysiswhenlocationsareidentifiedasvariables
EOF method dealing with periodicity in general, which andtimesasobservations,ortheT-modeanalysisforthe
they label periodically extended empirical orthogonal reverse,(seeJolliffe2002forfurtherdiscussionsandref-
functions (PXEOFs). PXEOFs are the eigenvectors of a erences).Furtherextension of EOF/PC analysis hasbeen
largecovariancematrix,whichisderivedbydividingthe proposed for various other types of data. For example
dataintoanumberofperiodicsegmentsandtreatingthem when the data are curves one obtains functional PCA
as different variables. The method is akin to extended (RamseyandSilverman,1997),andinvolvessolutionsto
EOF analysis, but differs from it in that averages in an eigenvalue problem of integro-differential type.
PXEOFs are performed over times at the same point The EOF method has also been extended to deal
within each block across blocks. with trends. Recently, Hannachi (2007) has presented an
Ordinary EOF analysis can be extended to the case EOF-based method to identify trends in gridded climate
where the data consist, for example, of two or more data. The method is based on an eigenanalysis of the
groups, and more layers such as different time periods. correlation/covariance matrix of time positions from the
This type of analysis has led to the concept of three- sorted data. Trend EOFs (TEOFs) are then identified
mode (see, e.g. Magnus and Neudecker, 1995) or multi- as the EOFs associated with the leading non-degenerate
ple group PCA. In the atmospheric science context, the eigenvalues of the matrix obtained using correlations
‘three’ in three-mode refers to the indices spanning the between time positions of the sorted data. Because the
data, namely spatial locations, times, and set of atmo- TEOFs are not in the data state space, the data are
spheric variables respectively. Note also that in the gen- first projected onto the TEOFs and the obtained time
eral three-mode PCA, time need not be ordered nor be series are then regressed back onto the data to yield
equally spaced. Spatial locations and atmospheric vari- the trend patterns. The method, which has been applied
ablescanbegroupedtogetherandordinaryEOFanalysis to various low-order systems and to reanalyses data,
can be applied. A common approach in weather/climate provides a systematic decomposition of the data into
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1147
EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE
(a) Spatial amplitude of complex EOF1 Filtered equatorial zonal wind (ms−1)
|     | 1   |     |     |     |     | 15  |     |     | 1   |     |     |     |     | 35  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
30
13
25
20
11
|     | )bm( erusserP 10 |     |     |     |     |     |     | )bm( erusserP | 10  |     |     |     |     | 15  |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
|     |                  |     |     |     |     | 9   |     |               |     |     |     |     |     | 10  |
5
0
|     | 50  |     |     |     |     | 7   |     |     | 50  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−5
100
|     |     |     |     |     |     | 5   |     | 100 |     |     |     |     |     | −10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−15
|     | 250 |     |     |     |     |     |     | 250 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 3   |     |     |     |     |     |     |     | −20 |
|     | 500 |     |     |     |     |     |     | 500 |     |     |     |     |     | −25 |
−30
|     | 1000  |     |          |     |      | 1   |     | 1000 |               |        |        |        |     |     |
| --- | ----- | --- | -------- | --- | ---- | --- | --- | ---- | ------------- | ------ | ------ | ------ | --- | --- |
|     | -15 S |     |          |     | 15 N |     |     |      | Jan 92 Jan 94 | Jan 96 | Jan 98 | Jan 00 |     |     |
|     |       |     | Latitude |     |      |     |     |      |               |        | Time   |        |     |     |
(b) Spatial phase of complex EOF1 Figure 33. Filtered zonal mean zonal wind anomalies for the period
|     | 1   |     |     |     |     | 90  |         |               |     |      |       |             |             |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ---- | ----- | ----------- | ----------- | --- |
|     |     |     |     |     |     |     | January | 1992–December |     | 2001 | using | the leading | complex EOF | and |
75
thecorrespondingcomplexPC.
60
45
|     | )bm( erusserP |     |     |     |     | 30  |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
15
0
|     |     |     |     |     |     |     | boundary |     | layer (see | Hannachi | 2007 | for more | details). |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | -------- | ---- | -------- | --------- | --- |
|     | 50  |     |     |     |     | −15 |          |     |            |          |      |          |           |     |
Itismentionedinsection3thatsimplificationmethods,
−30
100
|     |     |     |     |     |     | −45 | e.g.                                              | rotation, | aim | to find | physically | relevant | patterns | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --------- | --- | ------- | ---------- | -------- | -------- | --- |
|     | 250 |     |     |     |     | −60 | whichteleconnectionsaregoodexamples.Thesetelecon- |           |     |         |            |          |          |     |
|     | 500 |     |     |     |     | −75 |                                                   |           |     |         |            |          |          |     |
nectionsareingeneralassumedtobethecoherentpartof
−90
1000 the data. This assumption is implicit in the general inter-
|     | 15 S |     |     |     | 15 N |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Latitude pretation of EOFs based on a factor analysis approach
|        |             |           |        |         |             |         | (Jolliffe, |     | 2002;      | Dommenget | and  | Latif, 2002.)  | Further-   |     |
| ------ | ----------- | --------- | ------ | ------- | ----------- | ------- | ---------- | --- | ---------- | --------- | ---- | -------------- | ---------- | --- |
| Figure | 31. Spatial | amplitude | (a)and | spatial | phase (b)of | complex |            |     |            |           |      |                |            |     |
|        |             |           |        |         |             |         | more,      | it  | has become | clear     | that | in many recent | investiga- |     |
EOF1.
tionstheleadingEOFpatternsareofteninterpretedasthe
|     |              |          |          |     |                 |     | leading |      | teleconnections | (Thompson      |     | and     | Wallace,      | 1998, |
| --- | ------------ | -------- | -------- | --- | --------------- | --- | ------- | ---- | --------------- | -------------- | --- | ------- | ------------- | ----- |
|     |              |          |          |     |                 |     | 2000;   | Saji | et al.,         | 1999; Thompson |     | et al., | 2000; Wallace |       |
| a   | small number | of trend | patterns |     | and a remaining | set |         |      |                 |                |     |         |               |       |
with no trend when at least two grid points contain a and Thompson, 2002.) As pointed out in Jolliffe (2002)
trend.TheapplicationtoNCEP/NCARSLP,forexample, and Dommenget and Latif (2002), however, it is unclear
clearlyyieldstwotrendpatterns;theNAO(Hurrelletal., howtoidentifygenuineteleconnections.Inaddition,sim-
2003) and the Siberian High (Panagiotopoulos etal., plificationprocedureslikerotationmayormaynotleadto
2005.) The Siberian High is particularly interesting; it teleconnections.Inthiscontextstochasticnullhypotheses
wasnot capturedin previous studies using various forms areperhapsthe correcttools forassessingandevaluating
etal.
ofconventionalEOFsbecauseofitslocaltrendcharacter, climate modes of variability. Cahalan (1996) pre-
and also because of its confinement to the planetary sented a spatial first order autoregressive model, AR(1),
(a) Temporal amplitude of complex PC 1
0.06
edutilpmA 0.05
0.04
0.03
|     |     |     | Jan92 |     | Jan94 | Jan96 |     | Jan98 |     | Jan00 |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- |
(b) Temporal phase of complex PC 1
100
esahP
0
−100
|     |     |     | Jan92 |     | Jan94 | Jan96 |     | Jan98 |     | Jan00 |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- |
Figure32.Temporalamplitude(a)andtemporalphase(b)ofcomplexCPC1betweenJanuary1992throughtoDecember2001.
Copyright2007RoyalMeteorologicalSociety
|     |     |     |     |     |     |     |     |     |     |     | Int.J.Climatol.27:1119–1152 |     |     | (2007) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------ |
DOI:10.1002/joc

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1148
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
|           |             |     |               |           |       |     | shows the          | familiar       | and | debatable     | AO        | pattern.     | The  | spec- |
| --------- | ----------- | --- | ------------- | --------- | ----- | --- | ------------------ | -------------- | --- | ------------- | --------- | ------------ | ---- | ----- |
| as a null | hypothesis. |     | The following | diffusion | model |     |                    |                |     |               |           |              |      |       |
|           |             |     |               |           |       |     | trum of            | the covariance |     | matrix        | indicates | that         | this | EOF   |
|           |             | d   |               |           |       |     | is non-degenerate, |                | but | the remaining |           | EOF patterns |      | look  |
u=−λu+ν∇2u+f
(80)
dt t degenerate and yields therefore difficulties in interpreta-
tion.
has been considered by various authors such as Leung Next we have reviewed REOFs, which have been
and North (1991) to study the variability of a simplified introduced to overcome some of the previous drawbacks
atmospheric model, and North (1984) to compare EOFs related to orthogonality/uncorrelatedness of EOFs/PCs
and normal modes. In Eq. (80) λ and ν are damping respectivelyandalsointerpretation.Themethodattempts
and diffusion parameters respectively, and f is a spatial to rotate a fixed number of EOF patterns using either
t
andtemporalwhitenoiseforcing.Theisotropicdiffusion an orthogonal or oblique rotation matrix subject to max-
process (80), which is an extension of the simple AR(1) imising a simplicity criterion. The EOFs can be either
model, has recently been used by Dommenget (2007) as unscaled or scaled by the square root of the associ-
a null hypothesis for climate modes of variability. To ated eigenvalues. Various criteria exist in the literature,
separate possible teleconnections from a homogeneous but the overall result is that all rotations can be classi-
diffusive noise background the model is first fitted fied into four classes: (i) orthogonal rotation of EOFs,
to the observed data then the leading EOFs of the (ii) orthogonal rotation of EOFs scaled by the square
| obtained | model | compared |     | to the EOFs | of the | data. |         |                |     |              |       |         |          |     |
| -------- | ----- | -------- | --- | ----------- | ------ | ----- | ------- | -------------- | --- | ------------ | ----- | ------- | -------- | --- |
|          |       |          |     |             |        |       | root of | the associated |     | eigenvalues, | (iii) | oblique | rotation |     |
Dommenget (2007) applied the test to various observed of EOFs, and (iv) oblique rotation of scaled EOFs. In
fields and showed that the leading Tropical Pacific sea thisstudywehaveappliedvariousrotationtypes/criteria,
surface temperature (SST) and most NH large scale but the discussion was mainly focussed on three crite-
SLPstructurearesignificantlydifferentfromanisotropic ria, namely orthogonal VARIMAX, QUARTIMAX, and
diffusionprocess,whereastheTropicalIndianOceanSST
|     |     |     |     |     |     |     | oblique | QUARTIMIN. |     | The results | of  | rotation | applied | to  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --- | -------- | ------- | --- |
variability seems to be well described by such a process. SLP EOFs indicate that (i) and (iii) give similar results,
Other models could also be envisaged to deal with non- but the rotated patterns are sensitively dependent on the
diffusive fields such as SLP, (see e.g. Gerber and Vallis number m of EOFs selected for rotation. Case (ii) is
2005,andDommenget(2007)formoredetailsandfurther found to give similar results across a range of criteria,
references).
|     |     |     |     |     |     |     | but for | large | m the similarity |     | between | the | low ranked |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------------- | --- | ------- | --- | ---------- | --- |
The previous EOF/PC methods are linear in the sense REOFs across the various criteria cannot be guaranteed.
that they involve solving an eigenvalue problem. Non- Finally,case(iv)isfoundtobethemostunstable.There-
linear extensions of EOFs have also been proposed in fore orthogonal rotation of scaled EOFs seems to offer
the literature. The most well known examples are non- the most robust rotation.
| linear PCA,e.g.Monahan(2001), |     |     |     | andHsieh(2001), |     | and |            |       |     |            |        |      |           |     |
| ----------------------------- | --- | --- | --- | --------------- | --- | --- | ---------- | ----- | --- | ---------- | ------ | ---- | --------- | --- |
|                               |     |     |     |                 |     |     | Simplified | EOFs, | a   | competitor | to the | REOF | approach, |     |
independentcomponentanalysis, e.g.Hyva¨rinenandOja has also been reviewed. The method makes use of some
(2000).Thesemethodsarecomputing-powerhungry,and
|              |         |     |        |            |        |         | useful properties |            | of EOFs        | and | REOFs | simultaneously. |          | It  |
| ------------ | ------- | --- | ------ | ---------- | ------ | ------- | ----------------- | ---------- | -------------- | --- | ----- | --------------- | -------- | --- |
| the obtained | results |     | depend | in general | on the | descent |                   |            |                |     |       |                 |          |     |
|              |         |     |        |            |        |         | attempts          | to achieve | simultaneously |     |       | successive      | variance |     |
algorithm used to minimise the chosen (non-quadratic) maximisation, spatial orthogonality of EOFs, and sim-
costfunction.
|     |     |     |     |     |     |     | plicity of    | REOFs.  | This    | is achieved | by          | solving    | the        | same |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------- | ----------- | ----------- | ---------- | ---------- | ---- |
|     |     |     |     |     |     |     | eigenvalue    | problem | of      | EOFs        | but with    | anextra    | constraint |      |
|     |     |     |     |     |     |     | of simplicity | that    | depends | on          | a threshold | parameter. |            | The  |
SUMMARY AND CONCLUSION obtainedoptimisationisnon-quadraticandinvolvesusing
|              |     |         |            |                 |         |         | advanced  | numerical | methods     |     | based     | on numerical |       | solu- |
| ------------ | --- | ------- | ---------- | --------------- | ------- | ------- | --------- | --------- | ----------- | --- | --------- | ------------ | ----- | ----- |
| We presented |     | in this | manuscript | an introductory |         | review  |           |           |             |     |           |              |       |       |
|              |     |         |            |                 |         |         | t√ions of | ODEs.     | A threshold |     | parameter | of the       | order | of    |
| of the state | of  | the art | of using   | EOFs and        | closely | related |           |           |             |     |           |              |       |       |
p
methods as a means to find prominent patterns of vari- ,wherep isthenumberofvariables,isfoundtopro-
3
videareasonablebalancebetweenvariancemaximisation
| ability, | smoothing | and | reducing | the high | dimensionality |     |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | -------- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of large scale climate variables, and reconstructing par- and simplicity of the patterns. The leading three SEOF
patternsareidentifiedrespectivelyastheNAO,theNorth
| ticularly | revealing | patterns. |     | The review | has focussed | on  |     |     |     |     |     |     |     |     |
| --------- | --------- | --------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
five different methods based on EOFs to analyse various Pacific, and the Scandinavian patterns. The obtained pat-
climate data. The methods considered here are conven- terns have invariant structures vis-a-vis changes in the
tional EOFs, REOFs, simplified EOFs, extended EOFs, threshold parameter. For example when this parameter
and complex/Hilbert EOFs. gets smaller the patterns keep their structures but their
WebeganbyreviewingtheconventionalEOFsmethod. spatial extension gets reduced. The method, however, is
In particular we have highlighted its benefits, such as computationally intensive but can still be very useful to
easy computation, efficient data reduction, and useful gaininsightifweareparticularlyinterestedintheleading
geometric properties. We have also presented its major few patterns for interpretation.
drawbacks, such as predictable relations between EOFs, Extended EOFs (or MSSA) are presented as a way to
and physical interpretability. The method has been illus- overcome some of the shortcomings of EOFs, namely
tratedwithwintermonthlySLP.TheleadingEOFpattern the use of only spatial correlation. MSSA makes use of
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1149
spatial as well as temporal correlation by extending the Angstro¨mA. 1935. Teleconnections of climatic changes in present
familiarstatevectorbyincludingexplicitlythetimeinfor- time.GeografiskaAnnaler17:243–258.
BaldwinMP, GrayLG, DunkertonTJ, HamiltonK, HaynesPH,
mation after choosing the delay parameter. The method RandelWJ, HoltonJR, AlexanderMJ, HirotaI, HorinouchiT,
can be used as a tool to filter the data, isolate a trend, JonesDBA,KinnersleyJS,MarquardtC,SaoK,TakahasiM.2001.
Thequasi-biennialoscillation.ReviewinGeophysics39:179–229.
or even separate an oscillatory component buried in the
BarnettTP. 1983. Interaction of the monsoon and pacific trade wind
noisydata.Wehaveillustratedtheapproachwith5 years system at interannual time scales. Part I: The equatorial case.
of daily OLR data. We have in particular identified the MonthlyWeatherReview111:756–773.
BarnettTP. 1984a. Interaction of the monsoon and the Pacific trade
seasonalcycle andthe semi-annual oscillation. The MJO
windsystemsatinterannualtimescales.PartII:Thetropicalband.
was also identified from the spectrum of the extended MonthlyWeatherReview112:2380–2387.
data matrix. Various characteristics of MJO have also BarnettTP. 1984b. Interaction of the monsoon and the Pacific trade
windsystemsatinterannualtimescales.PartIII:Apartialanatomyof
been identified such as the most active region of growth
theSouthernOscillation.MonthlyWeatherReview112:2388–2400.
and decay phase, approximate period, and phase speed. BarnstonAG, LivezeyBE. 1987. Classification, seasonality, and
The complex EOFs method constitutes another persistence of low-frequency atmospheric circulation patterns.
MonthlyWeatherReview115:1083–1126.
approach used to identify propagating disturbances.
BasilevskyA, HumPJ. 1979. Karhunen-Loe`ve analysis of historical
Unlike EEOFs, complex EOFs use complex formulation time series with application to Plantation birth in Jamaica. Journal
ofpropagatingwavesandinvolvetheHilberttransformof oftheAmericanStatisticalAssociation74:284–290.
BjerknesJ. 1969. Atmospheric teleconnections from the equatorial
thefieldtoformthecomplexifiedfieldwithnoparameter
Pacific.MonthlyWeatherReview97:163–172.
tofix.ComplexHEOFsofECMWFmonthlyzonal-mean Bjo¨rnssonH, VenegasSA. 1997. A Manual for EOF and SVD
zonal wind from January 1958 to December 2001 have Analyses of Climate Data. Report No 97-1, Department of
Atmospheric and Oceanic Sciences and Centre for Climate and been calculated. Complex EOFs/PCs have been used to
GlobalChangeResearch,McGillUniversity.52.
filter the data and reduce their dimension. The QBO BibbyJ.1980.Someeffectsofroundingoptimalestimates.SankhyaB
propagatingsignalhasbeenfilteredoutusingtheleading 42:165–178.
BloomfieldP, DavisJM. 1994. Orthogonal rotation of complex
complex EOF/PC. Spatial as well as temporal amplitude
principal components. International Journal of Climatology 14:
and phase associated with CEOF1/CPC1 have also 759–775.
been computed and help in interpreting the downward BlumenthalMB. 1991. Predictability of a coupled ocean-atmosphere
model.JournalofClimate4:766–784.
propagating QBO signal.
BrethertonCS, SmithC, WallaceJM. 1992. An intercomparison of
We have discussed briefly some other extensions of methods for finding coupled patterns in climate data. Journal of
EOFs including cyclostationary, PXEOFs, the S-mode Climate5:541–560.
BrillingerDR.1981. TimeSeries-Data:AnalysisandTheory.Holden-
EOF analysis, trend EOFs, and nonlinear extensions of
Day:SanFrancisco,CA.
PCA. We have also discussed the methods used to sepa- BrinkKH, MuenchRD. 1986. Circulation in the point conception-
ratepossibleteleconnectionsfromthemerehomogeneous Santa Barbara channel region. Journal of Geophysical Research C
91:877–895.
diffusion process background. These extensions are not BroomheadDS,KingGP.1986a.Extractingqualitativedynamicsfrom
treated in detail, but we have provided references for experimentaldata.PhysicaD20:217–236.
interested readers. BroomheadDS, KingGP. 1986b. On the qualitative analysis of
experimental dynamical systems. In Nonlinear Phenomena and
Chaos,SarkarS(ed).AdamHilger:Bristol;113–144.
CahalanRF, WhartonLE, WuW-L. 1996. Empirical orthogonal
Acknowledgements
functionsofmonthlyprecipitationandtemperatureovertheUnited
Statesandhomogeneousstochasticmodels.JournalofGeophysical
ThisworkwassupportedbytheNERCCentreforGlobal
Research101:26309–26318.
Atmospheric Modeling (CGAM) at the Department of CarrollJB. 1953. An analytical solution for approximating simple
Meteorology, the University of Reading. We thank Dr I. structureinfactoranalysis.Psychometrika18:23–38.
CraddockJM. 1973. Problems and prospects for eigenvector analysis
Oliveira for her comments on a previous version of the inmeteorology.TheStatistician22:133–145.
paper,DrC.FerroforpointingtousHeinlein’sreference, ChatfieldC, CollinsAJ. 1989. Introduction to Multivariate Analysis.
ChapmanandHall:London.
and Dr D. Dommenget for bringing to our attentin his
ChenJ-M, HarrPA. 1993. Interpretation of Extended Empirical
workonEOFevaluation.Wealsothankonereviewerfor OrthogonalFunction(EEOF)analysis.MonthlyWeatherReview121:
his/her comments that helped improve the manuscript. 2631–2636.
ChengX,NitscheG,WallaceJM.1995.Robustnessoflow-frequency
circulation patterns derived from EOF and rotated EOF analysis.
References JournalofClimate8:1709–1720.
DommengetD.2007.EvaluatingEOFmodesagainstastochasticnull
AmbaumMHP,HoskinsBJ, StephensonDB. 2001. Arcticoscillation hypothesis.ClimateDynamics28:517–531.
orNorthAtlanticOscillation?JournalofClimate14:3495–3507. DommengetD,LatifM.2002.Acautionarynoteontheinterpretation
AmbaumMHP, HoskinsBJ, StephensonDB. 2002. Corrigendum: ofEOFs.JournalofClimate15:216–225.
arctic oscillation or North Atlantic Oscillation? JournalofClimate EbdonRA. 1960. Notes on the wind flow at 50mb in tropical and
15:553. subtropicalregionsinJanuary1957andin1958.QuarterlyJournal
AndersonTW. 1963. Asymptotic theory for principle component oftheRoyalMeteorologicalSociety86:540–542.
analysis.AnnalsofMathematicalStatistics34:122–148. ElsnerJB,TsonisAA.1996.SingularSpectrumAnalysis:ANewTool
AndersonTW. 1984. An Introduction to Multivariate Statistical inTimeseriesAnalysis.PlenumPress:NewYork.
Analysis,2ndedn.JohnWiley:NewYork. FraedrichK.1986. Estimatingthedimensions ofweatherandclimate
AndersonJR, RosenRD. 1983. The latitude-height structure of attractors.JournaloftheAtmosphericSciences43:419–432.
40–50day variations in atmospheric angular momentum. Journal FukunagaK,KoontzWLG.1970.ApplicationoftheKarhunen-Loe`ve
oftheAtmosphericSciences40:1584–1591. expansion to feature selection and ordering. IEEETransactions on
AngellJK, KorshoverJ. 1964. Quasi-biennial variations in tempera- ComputersC-19:311–318.
ture,totalozone,andtropopauseheight.JournaloftheAtmospheric FukuokaA. 1951. A Study of 10-day Forecast (A Synthetic Report),
Sciences21:479–492. Vol.XXII.TheGeophysicalMagazine:Tokyo;177–218.
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

1150 A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
GerberEP, VallisGK. 2005. A stochastic model for the spatial JohnsonES, McPhadenMJ. 1993. Structure of intraseasonal Kelvin
structure of annular patterns of variability and the North Atlantic waves in the equatorial Pacific Ocean. Journal of Physical
oscillation.JournalofClimate18:2102–2118. Oceanography23:608–625.
GhilM, AllenMR, DettingerMD, IdeK, KondrashovD, MannME, JolliffeIT. 1987. Rotation of principal components: some comments.
RobertsonAW, SaundersA, TianY, VaradiF, YiouP. 2002. JournalofClimatology7:507–510.
Advanced spectral methods for climatic time series. Reviews of JolliffeIT. 1995. Rotation of principal components: choice of
Geophysics40:1.1–1.41. normalizationconstraints.JournalofAppliedStatistics22:29–35.
GirshickMA.1939.Onthesamplingtheoryofrootsofdeterminantal JolliffeIT. 2002. Principal Component Analysis, 2nd edn. Springer:
equations.AnnalsofMathematicalStatistics43:128–136. NewYork.
GolubGH, van LoanCF. 1996. Matrix Computation. John Hopkins JolliffeIT, UddinM, VinesSK. 2002. Simplified EOFs-three
UniversityPress:Baltimore,MD. alternativestoretain.ClimateResearch20:271–279.
GolyandinaNE,NekrutinVV,ZhigljavskyAA.2001.AnalysisofTime JolliffeIT,TrendafilovNT,UddinM.2003.AModifiedprincipalcom-
Series Structure. SSA and Related Techniques. Chapman and Hall: ponent technique based on the LASSO. Journal of Computational
BocaRaton,FL. andGraphicalStatistics12:531–547.
GraybillFA. 1969. Introduction to Matrices with Application in KaiserHF.1958. Thevarimaxcriterionforanalyticrotation infactor
Statistics.Wadsworth:Belmont,CA. analysis.Psychometrika23:187–200.
GraystoneP.1959.Meteorologicalofficediscussion-tropicalmeteorol- KalnayE, KanamitsuM, KistlerR, CollinsW, DeavenD, GandinL,
ogy.MeteorologicalMagazine88:113–119. IredellM, SahaS, WhiteG, WoollenJ, ZhuY, ChelliahM,
GreenBF.1977.Parametersensitivityinmultivariatemethods.Journal EbisuzakiW, HigginsW, JanowiakJ, MoKC, RopelewskiC,
ofMultivariateBehavioralResearch12:263–287. WangJ, LeetmaA, ReynoldsB, JenneR, JosephD. 1996. The
HannachiA.2007.Patternhuntinginclimate:anewmethodforfinding NCEP/NCAR 40-year reanalysis project. Bulletin of the American
trendsingriddedclimatedata.InternationalJournalofClimatology MeteorologicalSociety77:437–471.
27:1–15. KaplanD, GlassL. 1995. Understanding Nonlinear Dynamics.
HannachiA, JolliffeIT, StephensonDB, TrendafilovN. 2006. In Springer-Verlag:NewYork.
search of simple structures in climate: simplifying EOFs. KiersHAL. 1994. Simplimax: oblique rotation to an optimal target
InternationalJournalofClimatology26:7–28. withsimplestructure.Psychometrika59:567–579.
HannachiA, O’NeillA. 2001. Atmospheric multiple equilibria and KiladisGN, WeickmannKM. 1992. Circulation anomalies associated
non-Gaussianbehaviourinmodelsimulations.QuarterlyJournalof with tropical convection during northern winter. Monthly Weather
theRoyalMeteorologicalSociety127:939–958. Review120:1900–1923.
HannanEJ.1970.MultipleTimeSeries.JohnWiley:NewYork. KimK-W, HuangJ. 1996. EOFs of one-dimensional cyclostationary
HardyDM, WaltonJJ. 1978. Principal components analysis of time series: computations, examples, and stochastic modelling.
vector wind measurements. Journal of Applied Meteorology 17: JournaloftheAtmosphericSciences53:1007–1017.
1153–1162. KimK-W, WuQ. 1999. A comparison study of EOF techniques:
HarmanHH. 1976. ModernFactorAnalysis, 3rd edn. The University analysis of nonstationary data with periodic statistics. Journal of
ofChicagoPress:Chicago,IL. Climate12:185–199.
HausmannR.1982.Constrainedmultivariateanalysis.InOptimisation KimK-W, NorthGR. 1999. EOF-based linear prediction algorithm:
inStatistics,ZanckisSH,RustagiJS(eds).North-Holland:Amster- examples.JournalofClimate12:2076–2092.
dam;137–151. KimotoM,GhilM,MoKC.1991.Spatialstructureoftheextratropical
HeinleinRA. 1973. Time Enough for Love. New English Library: 40-dayoscillation.Proceedingsofthe8thConferenceonAtmospheric
London. andOceanicwavesandStability,AmericanMeteorologicalSociety:
HendonHH, SalbyML. 1994. The life cycle of the madden-Julian Boston,MA;115–116.
oscillation.JournaloftheAtmosphericSciences51:2225–2237. KistlerR, KalnayE, CollinsW, SahaS, WhiteG, WoollenJ,
HirschMW, SmaleS. 1974. Differential Equations, Dynamical ChelliahJ,EbisuzakiW,KanamitsuM,KouksyV,vandenDoolH,
Systems,andLinearAlgebra.AcademicPress:London. JenneR, FiorinoM. 2001. The NCEP-NCAR 50-year reanalysis:
HoltonJR. 1992. An Introduction to Dynamic Meteorology, 3rd edn. monthly means CD-ROM and documentation. Bulletin of the
AcademicPress:London. AmericanMeteorologicalSociety82:247–267.
HorelJD. 1981. A rotated principal component analysis of the KnutsonTR, WeickmannKM. 1987. 30–60day atmospheric oscilla-
interannual variability of the Northern Hemisphere 500mb height tion:compositelifecyclesofconvectionandcirculationanomalies.
field.MonthlyWeatherReview109:2080–2092. MonthlyWeatherReview115:1407–1436.
HorelJD. 1984. Complex principal component analysis: theory KressR, MartensenE. 1970. Anwendung der rechteckregel auf die
and examples. Journal of Climate and Applied Meteorology 23: reelleHilbertransformationmitunendlichemintervall.Zeitschriftfu¨r
1660–1673. AngewandteMathematikundMechanik50:61–64.
HotellingH. 1933. Analysis of a complex of statistical variables KrishnamurthiTN,ChakrabortyDR,CubuckuN,StefanovaL,Vijaya
into principal components. Journal of Educational Psychology 24: KumarTSV. 2003. A mechanism of the madden-Julian oscillation
417–520. basedoninteractionsinthefrequencydomain.QuarterlyJournalof
HotellingH. 1935. The most predictable criterion. Journal of theRoyalMeteorologicalSociety129:2559–2590.
EducationalPsychology26:139–142. KrzanowskiWJ. 2000. Principles of Multivariate Analysis: A User’s
HsiehWW. 2001. Nonlinear principal component analysis by neural Perspective,2ndedn.OxfordUniversityPress:Oxford.
networks.Tellus53A:599–615. KunduPK,AllenJS.1976.Somethree-dimensionalcharacteristicsof
HurrellJW. 1996. Influence of variations in extratropical wintertime low-frequencycurrentfluctuationsneartheOregoncoast.Journalof
teleconnections on Northern Hemisphere temperature. Geophysical PhysicalOceanography6:181–199.
ResearchLetter23:665–668. KutzbachJE. 1967. Empirical eigenvectors of sea-level pressure,
HurrellJW,KushnirY,OttersenG,VisbeckM.2003.Anoverviewof surface temperature and precipitation complexes over North
the North Atlantic Oscillation. In The North Atlantic Oscillation, America.JournalofAppliedMeteorology6:791–802.
Climate Significance and Environmental Impact, Geophysical LabitzkeK, van LoonH. 1999. The Stratosphere. Springer-Verlag:
Monograph 134, HurrellJW, KushnirY, OttersenG, VisbeckM NewYork.
(eds).AmericanGeophysicalUnion:Washington,DC;1–35. LawleyDN. 1956. Tests of significance for the latent roots of
Hyva¨rinenA, OjaE. 2000. Independent component analysis. Algo- covarianceandcorrelationmatrices.Biometrika43:128–136.
rithmsandapplications.NeuralNetworks13:4–5. LeungL-Y, NorthGR. 1991. Atmospheric variability on a zonally
JacksonJE. 1991. A User’s Guide to Principal Components. Wiley: symmetriclandplanet.JournalofClimate4:753–765.
NewYork. Loe`veM.1978. ProbabilityTheory, Vol.2,4th edn. Springer Verlag:
JenkinsJM, WattsDG. 1968. Spectral Analysis and its Applications. NewYork.
Holden-Day:SanFrancisco,CA. LorenzEN. 1956. Empirical Orthogonal Functions and Statistical
JennrichRI.2001.Asimplegeneralprocedurefororthogonalrotation. Weather Prediction. Technical report, Statistical Forecast Project
Psychometrika66:289–306. Report1,DepofMeteor,MIT:49.
JennrichRI. 2002. A simple general procedure for oblique rotation. LorenzEN.1970.Climatechangeasamathematicalproblem.Journal
Psychometrika67:7–19. ofAppliedMeteorology9:325–329.
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

EOFSANDRELATEDTECHNIQUESINATMOSPHERICSCIENCE 1151
MaddenRA,JulianPR.1971.Detectionofa40–50dayoscillationin ReymentRA, Jo¨reskogKG. 1996. Applied Factor Analysis in the
the zonal wind in the tropical Pacific. Journal of the Atmospheric NaturalSciences.CambridgeUniversityPress:Cambridge.
Sciences28:702–708. RichmanMB. 1981. Obliquely rotated principal components: an
MaddenRA, JulianPR. 1972. Description of global-scale circulation improved meteorologicalmaptyping technique. JournalofApplied
cells in the tropics with a 40–50day period. Journal of the Meteorology20:1145–1159.
AtmosphericSciences29:1109–1123. RichmanMB. 1986. Rotation of principal components. Journal of
MaddenRA,JulianPR.1994. Observations ofthe 40-50-day tropical Climatology6:293–335.
oscillation-areview.MonthlyWeatherReview122:814–837. RichmanMB.1987.Rotationofprincipalcomponents:areply.Journal
MagnusJR, NeudeckerH. 1995. Matrix Differential Calculus with ofClimatology7:511–520.
Applications inStatistics and Econometrics. John Wiley and Sons: SajiNH, GoswamiBN, VinayachandranPN, YamagataT. 1999. A
Chichester. dipolemodeinthetropicalIndianOcean.Nature401:360–363.
MardiaKV, KentJT, BibbyJM. 1979. Multivariate Analysis. SalsteinDA, RosenRD, PeixotoJP. 1983. Modes of variability in
AcademicPress:London. annualhemisphericwatervapor andtransportfields.Journalofthe
MaruyamaT. 1997. The quasi-biennial oscillation (QBO) and AtmosphericSciences40:788–803.
equatorial waves-a historical review. Papers in Meteorology and SealHL. 1967. Multivariate Statistical Analysis for Biologists.
Geophysics47:1–17. Methuen:London.
MatthewsAJ. 2000. Propagation mechanisms for the madden-Julian SimmonsAJ, WallaceJM, BranstatorGW. 1983. Barotropic wave
oscillation. Quarterly Journal of the Royal Meteorological Society propagationandinstability,andatmosphericteleconnectionpatterns.
126:2637–2651. JournaloftheAtmosphericSciences40:1363–1392.
MerrifieldMA, WinantCD. 1989. Shelf circulation in the gulf of SunL. 2005. Simple Principal Components. PhD thesis. Department
California: a description of the variability. Journal ofGeophysical of Statistics, Faculty of Mathematics and Computing, The Open
Research94:18133–18160. University,Milton,Keynes.
MerrifieldMA, GuzaRT. 1990. Detecting propagating signals with TakensF. 1981. Detecting strange attractors in turbulence. In
complexempiricalorthogonalfunctions:acautionarynote.Journal Dynamical Systems and Turbulence. Lecture Notes in Mathematics
ofPhysicalOceanography20:1628–1633. 898, RandD, YoungLS (eds). Springer-Verlag: New York;
Mestas-Nun˜ezAM.2000.Orthogonalitypropertiesofrotatedempirical 366–381.
modes.InternationalJournalofClimatology20:1509–1516.
ThackerWC. 1996. Metric-based principal components. Tellus 46A:
MonahanAH.2001.Nonlinearprincipalcomponentanalysis:tropical
584–592.
indo-pacificseasurfacetemperatureandsealevelpressure.Journal
Thiie´bauxHJ,ZwiersFW.1984.Theinterpretationandestimationof
ofClimate14:219–233.
effectivesamplesizes.JournalofClimateandAppliedMeteorology
MonahanAH, TangangFT, HsiehWW. 1999. A potential problem
23:800–811.
with extended EOF analysis of standing wave fields. Atmosphere-
ThomasJB. 1969. An Introduction to Statistical Communication
Ocean3:241–254.
Theory.Wiley:NewYork.
MorrisonDF. 1976. Multivariate Statistical Methods, 2nd edn. ThompsonDWJ,WallaceJM.1998.TheArcticoscillationsignaturein
McGraw-Hill:NewYork.
wintertime geopotential height and temperature fields. Geophysical
NorthGR. 1984. Empirical orthogonal functions and normal modes.
ResearchLetters25:1297–1300.
JournaloftheAtmosphericSciences41:879–887.
ThompsonDWJ, WallaceJM. 2000. Annular modes in the extratrop-
NorthGR,BellTL,CahalanRF,MoengFJ.1982.Samplingerrorsin
ical circulation. Part I: Month-to-month variability. JournalofCli-
the estimation of empirical orthogonal functions. Monthly Weather
mate13:1000–1016.
Review110:699–706.
ThompsonDWJ, WallaceJM, HegerlGC. 2000. Annular modes in
ObukhovAM. 1947. Statistically homogeneous fields on a sphere.
theextratropicalcirculation,PartII:Trends.JournalofClimate13:
UspethiMathematicheskikhNauk2:196–198.
1018–1036.
ObukhovAM. 1960. The statistically orthogonal expansion of
TibshiraniR. 1996. Regression shrinkage and selection via the lasso.
empiricalfunctions.BulletinoftheAcademyofSciencesoftheUSSR.
JournaloftheRoyalStatisticalSocietyB58:267–288.
GeophysicsSeries(EnglishTransl.)1:288–291.
TrenberthKE.1984.Someeffectsoffinitesamplesizeandpersistence
OverlandJE,PreisendorferRW.1982.Asignificancetestforprincipal
in meteorological statistics. Part I: Autocorrelations. Monthly
components applied to a cyclone climatology. Monthly Weather
WeatherReview112:2359–2368.
Review110:1–4.
TrenberthKE, ShinW-TK. 1984. Quasi-biennial fluctuations is sea
PalmerCE.1954.Thegeneralcirculationbetween200mband10mb
level pressures over the Northern Hemisphere. Monthly Weather
overtheequatorialPacific.Weather9:3541–3549.
Review111:761–777.
PanagiotopoulosF, ShahgedanovaM, HannachiA, StephensonDB.
TrendafilovNT, JolliffeIT. 2005. Numerical solution of the
2005. Observed trends and teleconnections of the Siberian high:
a recently declining center of action. Journal of Climate 18: SCoTLASS.ComputtionalStatisticsandDataAnalysis50:242–253.
1411–1422. VandenDoolHM,SahaS,JohanssonA.2000. Empiricalorthogonal
PavanV, TibaldiS, BrankovichC. 2000. Seasonal prediction of teleconnections.JournalofClimate13:1421–1435.
blocking frequency: results from winter ensemble experiments. VautardR,YiouP,GhilM.1992.Singularspectrumanalysis:atoolkit
Quarterly Journal of the Royal Meteorological Society 126: forshort,noisychaoticsignals.PhysicaD58:95–126.
2125–2142. VinesSK. 2000. Simple principal components. Applied Statistics 49:
PearsonK.1902.Onlinesandplanesofclosestfittosystemsofpoints 441–451.
inspace.PhilosophiclMagazine2:559–572. von StorchH. 1995. Spatial Patterns: EOFs and CCA. In Analysis
PengS,FifeG.1996.Thecoupledpatternsbetweensealevelpressure of Climate Variability: Application of Statistical Techniques, von
and sea surface temperature in the mid-latitude North Atlantic. StorchH,NavarraA(eds).SpringerVerlag:Berlin;227–257.
JournalofClimate9:1824–1839. von StorchH, ZwiersFW. 1999. Statistical Analysis in Climate
PlautG, VautardR. 1994. Spells of low-frequency oscillations and Research.CambridgeUniversityPress:Cambridge.
weather regimes in the northern hemisphere. Journal of the von StorchH, Bu¨rgerG, SchnurR, StorchJ-S. 1995. Principal
AtmosphericSciences51:210–236. oscillationpatterns.Areview.JournalofClimate8:377–400.
PreisendorferRW.1988.PrincipalComponentAnalysisinMeteorology WallaceJM. 1972. Empiricalorthogonal representation of time series
andOceanography.Elsevier:Amsterdam. inthefrequencydomain.PartII:Applicationtothestudyoftropical
PriestleyMB.1981.SpectralAnalysisofTimeSeries.Academic-Press: wavedisturbances.JournalofAppliedMeteorology11:893–900.
London. WallaceJM,DickinsonRE.1972.Empiricalorthogonalrepresentation
RamseyJD,SilvermanBW.1997.FunctionalDataAnalysis.Springer of time series in the frequency domain. Part I: Theoretical
Verlag:NewYork. consideration.JournalofAppliedMeteorology11:887–892.
RasmussonEM, ArkinPA, ChenW-Y, JalickeeJB. 1981. Biennial WallaceJM, GutzlerDS. 1981. Teleconnections in the geopotential
variationsinsurfacetemperatureovertheUnitedStatesasrevealed height field during the Northern Hemisphere winter. Monthly
bysingulardecomposition.MonthlyWeatherReview109:587–598. WeatherReview109:784–812.
ReedRJ, CampbellWJ, RasmussenLA, RogersRG. 1961. Evidence WallaceJM, ThompsonDWJ. 2002. The Pacific Center of Action of
of a downward propagating annual wind reversal in the equatorial theNorthernHemisphereannularmode:realorartifact?Journalof
stratosphere.JournalofGeophysicalResearch66:813–818. Climate15:1987–1991.
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152 (2007)
DOI:10.1002/joc
10970088,
2007,
9,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[03/02/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10970088, 2007, 9, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.1499 by University Of Sao Paulo - Brazil, Wiley Online Library on [03/02/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1152
A.HANNACHI,I.T.JOLLIFFEANDD.B.STEPHENSON
WalshJE,RichmanMB.1981.Seasonalityintheassociationsbetween WeidemanJAC. 1995. Computing the Hilbert transform on the real
surface temperatures over the United States and the North Pacific line.MathematicsofComputation64:745–762.
Ocean.MonthlyWeatherReview109:767–783. WhittleP. 1951. Hypothesis Testing in Time Series. Almqvist and
| WeareBC, NasstromJS. | 1982. Examples | of extended empirical | Wicksell:Upsala. |
| -------------------- | -------------- | --------------------- | ---------------- |
orthogonal function analysis. Monthly Weather Review 110: WilksDS.2006.StatisticalMethodsintheAtmosphericSciences,2nd
| 481–485. |     |     | edn.AcademicPress:Amsterdam. |
| -------- | --- | --- | ---------------------------- |
WebsterPJ, ChangH-R. 1988. Equatorial energy accumulation and XinhuaC,DunkertonTJ.1995.Orthogonalrotationofspatialpatterns
emanationregions:Impactsofazonallyvaryingbasicstate.Journal derived from singular value decomposition analysis. Journal of
| oftheAtmosphericSciences45:803–829. |     |     | Climate8:2631–2643. |
| ----------------------------------- | --- | --- | ------------------- |
Copyright2007RoyalMeteorologicalSociety Int.J.Climatol.27:1119–1152(2007)
DOI:10.1002/joc