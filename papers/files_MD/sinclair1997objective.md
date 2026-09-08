595
| SEPTEMBER1997 |     |     |     |     |     | SINCLAIR |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Objective Identification of Cyclones and Their Circulation Intensity, and Climatology
|     |     |     |     |     |     | MARK | R. SINCLAIR |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
NationalInstituteofWaterandAtmosphericResearch,Ltd.,Wellington,NewZealand
(Manuscriptreceived29May1996,infinalform31March1997)
ABSTRACT
Anupdatedprocedureforobjectiveidentificationandtrackingofsurfacecyclonesfromgriddedanalysesis
described. Prior smoothing of the raw data with a constant radius spatial filter is used to remove distortions
relatedtotheparticulargridconfigurationusedandtoconsistentlyadmitaknownscaleofdisturbanceoverthe
domain.Pitfallsofusingcentralpressureorvorticitytoinfercycloneintensityareillustrated,andaprocedure
for obtaining a more realistic areal measure of circulationis described.Anautomatedselectionprocedurefor
storms having specific properties is outlined. Case selection is by computer search of a database of cyclone
tracks, obtained from an application of the cyclone finding and tracking procedure to an extended series of
griddedmeansealevelpressureanalyses.
A selection of winter season cyclone statistics for both hemispheres is obtained from European Centre for
Medium-RangeWeatherForecastsanalyses.Discrepancieswithandbetweenearlierstudiesappearmorerelated
to differing cyclone detection and counting procedures than to any intrinsic variability in analysis quality or
cycloneoccurrence.Resultsarefoundinagreementwiththewidelyacceptedmanuallyproducedclimatologies
onlywhenasimilarcyclonecountingprocedureisused.Asinpreviousstudies,NorthernHemispherecyclones
form and intensify near the eastern seaboards of Asia and North America, with maximum activity near SST
gradients. They move eastward and poleward during their lives before weakening in the Gulf of Alaska and
nearIceland.SouthernHemispherecyclonesaremoreevenlydistributedaroundthehemisphere.Theytendto
form and intensify in middle latitudes, near SST gradients over open oceans, and near the eastern coasts of
South America and Australia, and decay at higher latitudes. There is some evidence that newly formed and
intensifyingcyclonesinbothhemispherespossessatighterinnerstructurethanmatureanddecayingsystems.
1. Introduction manual tracking methods are less feasible. Automated
proceduresyieldconsistent,repeatableresultsandavoid
Therearemanycircumstanceswhereitisrequiredto
thedependenceonsubjectivedecisionswhoseoutcome
objectivelyidentifycyclonesinlongseriesofnumerical
|     |     |     |     |     |     |     | may vary | from day | to  | day and | between | analysts. | As  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ------- | ------- | --------- | --- |
analyses.Cyclonestatisticsbasedonautomatedfinding
|              |     |            |      |      |         |           | multidecade | numerically        |     | analyzed                 | datasets |     | become |
| ------------ | --- | ---------- | ---- | ---- | ------- | --------- | ----------- | ------------------ | --- | ------------------------ | -------- | --- | ------ |
| and tracking |     | of centers | have | been | used to | assess or |             |                    |     |                          |          |     |        |
|              |     |            |      |      |         |           | available   | via the reanalysis |     | effortsattheNationalCen- |          |     |        |
intercomparetheperformanceofnumericalmodels(Ak-
|                                               |              |           |        |         |                 |          | ters for  | Environmental  | Prediction   |           | (NCEP)  | and    | the Eu-   |
| --------------------------------------------- | ------------ | --------- | ------ | ------- | --------------- | -------- | --------- | -------------- | ------------ | --------- | ------- | ------ | --------- |
| yildiz 1985;                                  | Lambert      | 1988;     | Le     | Treut   | and Kalnay1990; |          |           |                |              |           |         |        |           |
|                                               |              |           |        |         |                 |          | ropean    | Centre for     | Medium-Range |           | Weather |        | Forecasts |
| Murray                                        | and Simmonds |           | 1991b; | Ko¨nig  | et al.          | 1993) or | to        |                |              |           |         |        |           |
|                                               |              |           |        |         |                 |          | (ECMWF),  | the need       | for          | efficient | and     | robust | objective |
| study the                                     | cyclone      | response  | to     | natural | or simulated    | cli-     |           |                |              |           |         |        |           |
|                                               |              |           |        |         |                 |          | feature   | identification | and          | tracking  | schemes |        | becomes   |
| mate variability                              |              | (Simmonds |        | and Wu  | 1993; Kidson    | and      |           |                |              |           |         |        |           |
| Sinclair1995;MurrayandSimmonds1995).Automated |              |           |        |         |                 |          | even more | pressing.      |              |           |         |        |           |
Resultsfromobjectivecycloneidentificationschemes
| procedures     | are    | also now     | being      | used      | to understand | the       |            |             |             |               |             |             |       |
| -------------- | ------ | ------------ | ---------- | --------- | ------------- | --------- | ---------- | ----------- | ----------- | ------------- | ----------- | ----------- | ----- |
|                |        |              |            |           |               |           | are highly | dependent   | on          | the rationale |             | for cyclone | se-   |
| climatological |        | behavior     | of surface | cyclones  |               | (Jonesand |            |             |             |               |             |             |       |
|                |        |              |            |           |               |           | lection,   | as will be  | illustrated | in            | this study. | There       | is a  |
| Simmonds       | 1993;  | Sinclair     | 1995,      | hereafter | SI95),        | anti-     |            |             |             |               |             |             |       |
|                |        |              |            |           |               |           | need to    | ensure that | cyclone     | detection     |             | procedures  | yield |
| cyclones       | (Jones | and Simmonds |            | 1994;     | Sinclair      | 1996),    |            |             |             |               |             |             |       |
and midtropospheric features (Bell and Bosart 1989; realisticresultswithoutintroducingbiasormissingim-
|         |                    |     |     |        |          |        | portant    | disturbances. | For         | example,       |     | in the | Southern |
| ------- | ------------------ | --- | --- | ------ | -------- | ------ | ---------- | ------------- | ----------- | -------------- | --- | ------ | -------- |
| Lefevre | and Nielsen-Gammon |     |     | 1995). | In these | appli- |            |               |             |                |     |        |          |
|         |                    |     |     |        |          |        | Hemisphere | (SH),         | traditional | identification |     | of     | cyclones |
cationswherelargesamplesizesspanningseveralyears
|               |     |                |     |          |                 |     | as pressure | minima | overwhelmingly |     |     | locates | most cy- |
| ------------- | --- | -------------- | --- | -------- | --------------- | --- | ----------- | ------ | -------------- | --- | --- | ------- | -------- |
| are desirable |     | for meaningful |     | results, | labor-intensive |     |             |        |                |     |     |         |          |
60(cid:56)S
|     |     |     |     |     |     |     | clone activity | poleward |     | of  | (e.g., | Le Marshall | and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | --- | ------ | ----------- | --- |
Kelly1981;Lambert1988).Unfortunately,theevidence
fromsatellitestudies(StretenandTroup1973;Carleton
Correspondingauthoraddress:Dr.MarkR.Sinclair,NationalIn- 1979) and general synoptic experience (e.g., Taljaard
stituteofWaterandAtmosphericResearchLtd.,301EvansBayPa- 1967) is that SH cyclones form and intensifyinmiddle
rade,GretaPoint,P.O.Box14-901,Kilbirnie,Wellington,NewZea-
| land. |     |     |     |     |     |     | latitudesanddecayathigherlatitudes.Thediscrepancy |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
arisesbecausemanymobiledisturbancesinthe40(cid:56)–60(cid:56)
E-mail:m.sinclair@niwa.cri.nz
(cid:113)1997AmericanMeteorologicalSociety
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

596 WEATHER AND FORECASTING VOLUME12
latitudebeltgoundetectedwherethelocalpressuremin- show examples where traditional central pressure fall
imum vanishes because of a superimposedbackground criteria for diagnosing cyclogenesis are misleadingand
pressure gradient (Sinclair 1994, hereafterSI94).Thus, outline a procedure for obtaining an areal measure of
results from schemes based on pressure minimaarebi- circulation intensity that helps reduce some of these
asedinfavorofthemoreintenseand/orslower-moving discrepancies.
centers south of 60(cid:56)S. SI94 found that using cyclonic Automatedcyclonefindingandtrackingschemesare
vorticity maxima in place of pressure minima spread ideally suited to quickly and exhaustively identifying
the diagnosed zone of cyclone activity throughout a systems possessing certain characteristicsfromextend-
broader range of latitudes between 40(cid:56) and 65(cid:56)S, more ed series of numerical analyses such as the NCEP or
consistentwithsatelliteimageryandeddystudies(Tren- ECMWF reanalyses, or from GCM simulations. This
berth 1991). studywasinitiallymotivatedbyattemptstoobjectively
These ambiguities in cyclone identification arecom- select cases of SH cyclogenesis for a composite study
pounded by the scale dependence of point measuresof from a 15-yr dataset of ECMWF analyses. Unfortu-
pressure and vorticity. Fine-mesh analyses will resolve nately, selections from the database of cyclone tracks
many additional weaker disturbances while overly obtained by SI94 made solely on the basis of central
coarse analyses may amalgamate or even obliterate
vorticity ranged from tight mesoscale systems to large
smaller features that are actually important circulation
systems more than 3000 km across, making them un-
centers. In addition, geographical biasesareintroduced
suitable for compositing. In section 4, we indicatehow
where resolution varies over the analysis domain, es-
greater case to case homogeneity can be gained by in-
peciallywhenvorticityisusedtodetectcyclones.Where
cludingadditionalselectioncriteriabasedoncirculation.
cyclone behavior from different numerical models is
Finally, in section 5, we apply the methodology to a
compared, it is crucialto ensurethatdifferencesdonot
survey of the characteristics of extratropical cyclones
merely result from different grid configurations or pre-
in both hemispheres. Results are compared with those
processing procedures.Wecanonlyhaveconfidencein
from previous studies based on a manual approach.
these comparisons when a fixed scale of disturbance is
consistently admitted over the domain for all datasets
involved.
2. Cyclone identification and tracking
Finally,thereisalsoaneedforanimprovedmeasure
ofthestrengthofacycloniccirculation.Wherecyclone
a. Cyclone identification
centershavebeentracked,cycloneintensitychangesare
traditionally gauged as mean sea level (MSL) pressure
Anyobjectiveschemeforidentifyingcyclonesneeds
variations following a closed low center. In many case
tohaveasoundphysicalbasis,berobustinapplication,
studies, these central pressure falls are compared di-
andyieldrealisticresults.SI94foundthatthetraditional
rectly with various cyclogenetic forcings. Unfortunate-
use of local pressure minima to identify SH cyclones
ly,thisuseofcentralpressurecanbemisleading.Some-
resulted in a bias favoring slow-moving or intensesys-
times, large pressure falls result from rapid migration tems south of 60(cid:56)S because many more mobile centers
acrossabackgroundpressurefieldratherthanfromany
of cyclonic circulation farther north are not associated
increase in the strength of the cyclonic circulation
withapressureminimum.Byadoptingalessrestrictive
(SI95). Sanders and Gyakum (1980) also noted exam-
definition of a ‘‘cyclone’’ as any centerofcycloniccir-
ples where increases in cyclonic circulation weremod-
culation (i.e., not just closed circulations), resultswere
est, despite huge pressure falls. The alternative use of
obtainedthatwereinbetteragreementwithsatelliteand
central vorticity as a measure of cyclone strength re-
eddy studies, attesting to the improved integrity of the
ducesthisproblem(SI95),althoughitisnotdifficultto
method. Thus, cyclone identification by means of vor-
see that systems having similar central vorticity may
ticityratherthanpressureextremaisseenasanecessary
differ widely in size, structure, and apparent intensity.
standard to avoid thesebiases.Thereaderisreferredto
This paper describes an updated procedure for the
SI94 for more discussion of this point.
objectiveidentificationandtrackingofsurfacecyclones
from gridded analyses and estimating their intensity. As well as avoiding bias, use of vorticity captures
However, rather than unveiling details of yet another many additional weaker (but nonetheless, important)
scheme for tracking meteorological features, we illus- secondary rotation centers that would not be detected
tratethepitfallsofignoringtheissuesraisedaboveand as pressure minima. These disturbances may comprise
instead propose some revisions to the scheme of SI94 preliminarystagesoflarge-scalecyclonesand/orbeas-
thatresolvethesequestions.Section2reviewsthecom- sociatedwithcopiousprecipitation.Forexample,many
ponents of a robust cyclone finding and tracking pro- of the 30 polar vortices studied by Sinclair and Cong
cedure, describes a spatial smoothing step that avoids (1992) lacked a pressure mimimum yet were clearly
biasresultingfromvaryinggridspacing,andillustrates associatedwithcomma-shapedcloudsignaturesakinto
the adverse consequences of omitting this step. In sec- larger frontal cyclones and were readily identifiable as
tion 3, we explore the issue of cyclone intensity. We vorticity extrema from ECMWF analyses.
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

597
| SEPTEMBER1997 |     |     |     |     |     | SINCLAIR |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
FIG.1.(a) SectionoftheECMWFgridoverthehighlatitudesoftheSouthPacificOcean,withgridpointsshownascrosses.(b)MSL
pressure (solid), drawn every 5 hpa and geostrophic vorticity (dashed, every 2 CVU) for 0000 UTC 6 May 1993 as computed without
preprocessing. (c) As in (b) except after application of Cressman spatial smoother withr of 500 km (one CVU (cid:53) (cid:50)1 (cid:51) 10(cid:50)5s(cid:50)1in the
o
SHand1(cid:51)10(cid:50)5s(cid:50)1intheNH).
1) SPATIAL averages geopotential data at each grid point with all
SMOOTHING
(cid:44)
|     |     |     |     |     |     |     | neighboring |     | grid points | at a | distance | r   | r (here | 500 |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ---- | -------- | --- | ------- | --- |
Because of the scale dependence of vorticity, addi- (cid:50) (cid:49) o
|            |                                        |     |         |        |       |         | km)      | using | weights of     | (r2           | r2)/(r2 | r2).      | At a distance |       |
| ---------- | -------------------------------------- | --- | ------- | ------ | ----- | ------- | -------- | ----- | -------------- | ------------- | ------- | --------- | ------------- | ----- |
| tionalbias | canbeintroducedwheregridresolutionvar- |     |         |        |       |         |          |       |                | o             | o       |           |               |       |
|            |                                        |     |         |        |       |         | of 0.58r |       | (289 km), this | Gaussian-like |         | weighting |               | falls |
| ies over   | the domain                             | or  | between | grids. | It is | crucial | to       | o     |                |               |         |           |               |       |
to0.5.Thisconstant-radiussmoothingresultsinamajor
ensurethatresultsarenotunwittinglydegradedbythese
|          |          |      |        |            |     |           | reduction |            | in the detail | at high | latitudes. |      | For example, |     |
| -------- | -------- | ---- | ------ | ---------- | --- | --------- | --------- | ---------- | ------------- | ------- | ---------- | ---- | ------------ | --- |
| effects. | There is | also | a need | to control | the | scale and |           |            |               |         |            |      |              |     |
|          |          |      |        |            |     |           | the       | unsmoothed | analyses      | in      | Fig. 1b    | show | the complex  |     |
numberofdisturbancesadmittedascyclones.Fine-mesh 65(cid:56)S, 175(cid:56)W
|     |     |     |     |     |     |     | cyclone | in  | the Ross Sea | near |     |     | to comprise |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---- | --- | --- | ----------- | --- |
analysesmayresolve1alargenumberofcloselyspaced
threecloselyspacedvortices.However,thesemergeinto
| extrema,        | while     | overly    | coarse      | analyses  | may        | merge or   |          |        |             |          |           |           |      |         |
| --------------- | --------- | --------- | ----------- | --------- | ---------- | ---------- | -------- | ------ | ----------- | -------- | --------- | --------- | ---- | ------- |
|                 |           |           |             |           |            |            | a single | vortex | as a result | of       | smoothing | (Fig.     | 1c). | Al-     |
| even obliterate |           | distinct  | circulation |           | centers.   | Spatial    |          |        |             |          |           |           |      |         |
|                 |           |           |             |           |            |            | though   | these  | centers     | possibly | represent | important |      | fea-    |
| smoothing       | should    | therefore |             | be used   | to control | the        |          |        |             |          |           |           |      |         |
|                 |           |           |             |           |            |            | tures    | such   | as frontal  | waves,   | localized | heating,  |      | or sec- |
| amount          | of detail | included  | and         | to ensure | the        | consistent |          |        |             |          |           |           |      |         |
ondarycenters,mostsynopticianswouldregardthelow
| application | of a | fixed | length | scale over | each | grid used. |     |     |     |     |     |     |     |     |
| ----------- | ---- | ----- | ------ | ---------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
(asanalyzedinFig.1c)asasinglecyclone.Othermore
Analysesof1000-hPageopotentialfromECMWFon
|                        |                                |        |          |             |             |         | distinct | vortices    | are retained |         | as separate | features.  |         |         |
| ---------------------- | ------------------------------ | ------ | -------- | ----------- | ----------- | ------- | -------- | ----------- | ------------ | ------- | ----------- | ---------- | ------- | ------- |
| a 2.5(cid:56) (cid:51) | 2.5(cid:56) latitude–longitude |        |          | grid        | (Fig. 1a)   | areused |          |             |              |         |             |            |         |         |
|                        |                                |        |          |             |             |         | Clearly, |             | the choice   | of an   | averaging   | radius     | is      | subjec- |
| to illustrate          | some                           | of the | pitfalls | of omitting | thiscrucial |         |          |             |              |         |             |            |         |         |
|                        |                                |        |          |             |             |         | tive     | and depends | on the       | context | of          | the study. | Smaller |         |
step.InFig.1b,MSLpressureandgeostrophicvorticity
|              |            |       |           |      |                 |     | values  | tend      | to retain | large   | additional | weaker    | vorticity   |       |
| ------------ | ---------- | ----- | --------- | ---- | --------------- | --- | ------- | --------- | --------- | ------- | ---------- | --------- | ----------- | ----- |
| are computed | from       | these | analyses  |      | and contoured   | di- |         |           |           |         |            |           |             |       |
|              |            |       |           |      |                 |     | centers | not       | normally  | thought | of as      | cyclones. |             | Where |
| rectly on    | this grid. | The   | increased | fine | detailtowardthe |     |         |           |           |         |            |           |             |       |
|              |            |       |           |      |                 |     | smaller | secondary | centers   | are     | important  | to        | the studyin |       |
poleisaresultofthedecreasingeast–westgridspacing.
|                  |           |               |      |           |           |          | question         | (say, | as initial    | stages     | of larger-scale |          | cyclones    |         |
| ---------------- | --------- | ------------- | ---- | --------- | --------- | -------- | ---------------- | ----- | ------------- | ---------- | --------------- | -------- | ----------- | ------- |
| As the           | vorticity | is derived    | from | the       | Laplacian | of the   |                  |       |               |            |                 |          |             |         |
|                  |           |               |      |           |           |          | or precipitation |       | systems),     | they       | should          | be       | retained    | by      |
| pressure         | field, it | is especially |      | sensitive | to the    | variable |                  |       |               |            |                 |          |             |         |
|                  |           |               |      |           |           |          | choice           | of    | a smaller r   | . However, | if              | the goal | of          | feature |
| grid resolution. |           |               |      |           |           |          |                  |       | o             |            |                 |          |             |         |
|                  |           |               |      |           |           |          | identification   |       | is to examine |            | ‘‘cyclones,’’   | it       | is probably |         |
InFig.1c,aspatialsmootherhasbeenappliedbefore
|             |     |          |         |          |     |         | appropriate |     | to smooth | with | a larger | r , as | in Fig. | 1c. |
| ----------- | --- | -------- | ------- | -------- | --- | ------- | ----------- | --- | --------- | ---- | -------- | ------ | ------- | --- |
| contouring. | The | smoother | follows | Cressman |     | (1959). | It          |     |           |      |          | o      |         |     |
2) LOCATION
|     |     |     |     |     |     |     |     |     | OF CYCLONIC |     | VORTICITY |     | MAXIMA |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | --- | ------ | --- |
1Analysis quality and availability of credible observations will Following the application of Cressman smoothingto
determinetherealismofthesedisturbances. the geopotential data, cyclones are identified as local
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

598 WEATHER AND FORECASTING VOLUME12
FIG. 2. Counts month(cid:50)1 of vorticity extrema exceeding 1 CVU falling within 555 km (5(cid:56) lat) of each grid point for the SH during
May–October 1990. (a) As computed directly on ECMWF grid with a contour interval of 10, with values exceeding 30 shaded. (b) As
obtainedfollowinginterpolationtoapolarstereographicprojection,contoursevery4,values(cid:46)10shaded.(c)Asobtainedafterapplication
ofCressmansmootherwithr of500km,every5,(cid:46)10shaded.Seetextformoredetails.
o
maxima of cyclonic gradient wind vorticity ((cid:122) ) ex- before computing vorticity, while in Fig. 2c Cressman
gr
ceedingsomethreshold.Gradientwindratherthangeo- smoothing with an r of 500 km is used.
o
strophicvorticityisusedbecausethegradientwindrep- Itisnotsurprisingthattherawdataadmitsincreased
resents a marked improvement over the geostrophic as numbers of vortices at high latitudes (Fig. 2a) on ac-
an approximation to the real wind. Whereactualwinds countofthedecreasinggridspacingthere.Ontheother
atsomelevelabovethesurfacelayerareavailable,these hand, the grid spacing for the polar stereographic do-
could be used in place of gradient winds. The method main (Fig. 2b) decreases toward the equator—at 60(cid:56)
of approximating gradient wind used here is described latitude it is 1.24 times that at 30(cid:56). This results in a
in the appendix. A bicubic spline fit to the (cid:122) fieldwas smallbiasfavoringcyclonedetectionatlowerlatitudes.
gr
used to identify extrema more accurately between grid Theconstant-radiusCressmansmoothingyieldsaresult
points, as described in SI94. Because many of the cy- (Fig. 2c) between these extremes but closer to Fig. 2b.
clones located in this way were not associated with a Provided r exceeds the largest gridspacingofthedata
o
closedcirculation(apressureminimum),theassociated domain, this fixed-radius smoothing removes any lati-
pressure was determined by interpolating the pressure tudinal bias over the grid and consistently admits only
field (computed from the1000-hPa geopotential)tothe spatialvariationsaboveacertainfixedlengthscale.En-
location of the (cid:122) center. suring this consistency is crucial for meaningful com-
gr
parisons of cyclone characteristics between different
models.
3) SENSITIVITY TO SMOOTHING STRATEGY
Figure2illustratesthedramaticconsequencesforthe
b. Tracking
detection of cyclones when grid configuration and
smoothingstrategiesarevaried.TheSHisusedbecause Tracking of centersenablescyclonemotionandin-
of the relative lack of complications from landmasses. tensification rates to be identified and allows consid-
Each panel shows the geographical distribution of SH eration of cyclone life cycles, as in SI95. It also en-
cyclonesduringMay–October1990asderivedfromthe ables a database of cyclone tracks to be constructed
same ECMWF data but with differing preprocessing. from which examples can be readily selected for fur-
Cyclones are counted as derived from ECMWF data ther analysis, such as for case or composite studies,
available twice daily. Vorticity extrema exceeding 1 as outlined in section 4 below. Tracking uses an al-
CVU((cid:50)1(cid:51)10(cid:50)5s(cid:50)1inSH,1(cid:51)10(cid:50)5s(cid:50)1inNH)falling gorithm first developed by Murray and Simmonds
within555km(5(cid:56)latitude)ofeachgridpointhavebeen (1991a) and modified by SI94. For eachcenter,apre-
counted,andtheresultscontouredforthesame6-month diction of the location, pressure, and vorticity at the
period. Near land,stationaryfeaturessuchasheatlows next track position is made from past motion, pres-
and lee troughs have been excluded using a procedure sure, and vorticity tendency. To start a track, these
that will be outlined later. In Fig. 2a, cyclones are ob- predictions are based on climatology. Next, a match
tained directly from the ECMWF data on the latitude– is attempted between each of these predictions and
longitude grid without preprocessing. In Fig. 2b, data the set of nearby centers found at the next analysis
have been interpolated to a polar stereographic projec- time (12 h later for ECMWF). The ensemble of suc-
tion and smoothed with a 25-point filter (Bleck 1965) cessful matches chosen is the one that minimizes a
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

599
| SEPTEMBER1997 |     |     |     | SINCLAIR |     |     |     |     |     |
| ------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
FIG.3.MSLpressure(solid)andcyclonic(cid:122) (dashed)fortheindicatedtimes.Areasofgradientwindexceeding18and25ms(cid:50)1are
gr
shaded.(a)–(c)MSLpressureisdrawnevery5hPa,vorticityevery1CVU;(d)–(f)theseare10hPaand4CVU.
weightedsumofabsolutedeparturesofposition,pres- sity. Unfortunately, these point measuresoftenfailto
sure,andvorticityfromthepredictedvalues.Formore represent the true strength of a cyclonic circulation
details, see Murray and Simmonds (1991a)and SI94. or its variation with time, as we now illustrate.
| c. Elimination | of orographic | features |     |     |            |                |         |     |     |
| -------------- | ------------- | -------- | --- | --- | ---------- | -------------- | ------- | --- | --- |
|                |               |          |     |     | a. Failure | of traditional | methods |     |     |
Nearland,manyquasi-stationaryorographicfeatures
|     |     |     |     |     | Figure | 3 features two | situations | where central | pres- |
| --- | --- | --- | --- | --- | ------ | -------------- | ---------- | ------------- | ----- |
aredetected.Thesearisefromfeaturessuchasheatlows
|                  |          |             |                  |     | sure tendency | misrepresents | cyclone | intensity | change. |
| ---------------- | -------- | ----------- | ---------------- | --- | ------------- | ------------- | ------- | --------- | ------- |
| and lee troughs, | and from | uncertainty | in extrapolating |     |               |               |         |           |         |
to 1000 hPa over high terrain. The tracking revealed Although cyclogenesis is commonly associated with
thattheseremainedanchoredtolandmasses.Theywere fallingcentralpressure,thisisnotalwaysthecase.Fig-
|            |                                     |          |       |        | ures 3a–c        | shows a cyclone | south      | of Australia | whose         |
| ---------- | ----------------------------------- | -------- | ----- | ------ | ---------------- | --------------- | ---------- | ------------ | ------------- |
| eliminated | by requiring cyclones               | spending | their | entire |                  |                 |            |              |               |
|            |                                     |          |       |        | central pressure | initially       | rose about | 5 hPa        | in 12 h as it |
| lifeoveror | within500kmoflandtohaveatotaltrans- |          |       |        |                  |                 |            |              |               |
lation of at least 1200 km. This mobility requirement migrated equatorward about a larger parent low to the
hadlittleeffectonsystemsmigratingtoorfromadjacent south. Despite the rising pressure, the area of cyclonic
| seas.         |            |          |     |     | vorticity   | and gradient flow | about      | it strengthened | and        |
| ------------- | ---------- | -------- | --- | --- | ----------- | ----------------- | ---------- | --------------- | ---------- |
|               |            |          |     |     | expanded.   | These circulation | increases  | continued       | as the     |
|               |            |          |     |     | low turned  | southeastward     | (Fig. 3c). |                 |            |
| 3. Estimation | of cyclone | strength |     |     |             |                   |            |                 |            |
|               |            |          |     |     | Conversely, | rapidly falling   | pressure   | does            | not always |
Onceacyclonehasbeenidentifiedandtracked,the indicate cyclogenesis. The area and strength of the cy-
resulting series of central MSL pressure or vorticity clonic circulation in Figs. 3d–f remained more or less
estimates are generally used to gauge cyclone inten- constant during a period of central pressure falls ex-
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

600
|     |     |            |             |                | WEATHER          | AND                     | FORECASTING              |                    |              |           |                   | VOLUME12 |     |
| --- | --- | ---------- | ----------- | -------------- | ---------------- | ----------------------- | ------------------------ | ------------------ | ------------ | --------- | ----------------- | -------- | --- |
|     |     | F .        | 4 . M S L   | p r e s s ur e | , (cid:122) (e v | e ry 2 C V U            | ), a n d g ra d i en t w | i n d ,a s         | fo r F ig s. | 3c a n d  | 3 d e x c e pt    | o n      |     |
|     |     | I G        |             |                | g r              |                         |                          |                    |              |           |                   |          |     |
|     |     | ap o l a r | g r id o fr | a d i u s (    | a ), ( b ) 1 5   | (cid:56) lat itu d e (1 | 6 6 6 k m ) a n d ( c)   | , (d ) 2 5(cid:56) | ( 27 7 8     | km ), a t | t h et i m e s an | d        |     |
locationsindicatedwitheachplot.
ceeding1Bergeron2(B).Inthiscase,therapidpressure sphere (NH) involving weaker central vorticity are
falls occurred as the circulation system moved quickly showninFigs.4cand4d.Thefirst(Fig.4c)wasaweak
toward a region of lower background pressure. Based disturbance(cid:44)1500kmindiameter,whiletheother(Fig.
on mean conditions for August as averaged from 15 yr 4d) was a major circulation system (cid:46)4000 km across,
(cid:59)3
of twice-daily ECMWF data (not shown), the clima- despite a central vorticity of only CVU. Again,
tological MSL pressure difference along its path (be- based solely on central vorticity, these two systems
tween Figs. 3d and 3f) is 25 hPa, which is exactly the would be gauged as being of similar strength!
| 24-h pressure | fall       | between      | these | two          | times.            |            |                |     |            |     |             |     |     |
| ------------- | ---------- | ------------ | ----- | ------------ | ----------------- | ---------- | -------------- | --- | ---------- | --- | ----------- | --- | --- |
| The use       | of central | vorticity    |       | as a measure |                   | of cyclone |                |     |            |     |             |     |     |
|               |            |              |       |              |                   |            | b. Calculation |     | of cyclone |     | circulation |     |     |
| strength      | is also    | problematic. |       | Figures      | 4a and            | 4b show    |                |     |            |     |             |     |     |
| two cyclones  | having     | similar      |       | central      | vorticityofaround |            |                |     |            |     |             |     |     |
Circulation,equivalenttotheareaenclosedbyacurve
| 11–12 CVU.           | However, |     | the system | in           | Fig. 4b       | involving  |           |          |           |      |          |         |           |
| -------------------- | -------- | --- | ---------- | ------------ | ------------- | ---------- | --------- | -------- | --------- | ---- | -------- | ------- | --------- |
|                      |          |     |            |              |               |            | times the | mean     | vorticity | over | the area | (or the | line in-  |
| a larger circulation |          | and | winds      | (cid:46)25 m | s(cid:50)1 is | clearlythe |           |          |           |      |          |         |           |
|                      |          |     |            |              |               |            | tegral of | velocity | around    | the  | boundary | of the  | area), is |
moreintense.Furthermore,atransformationfromasys-
|     |     |     |     |     |     |     | a more | realistic | measure | of  | cyclone | strength becauseit |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------- | --- | ------- | ------------------ | --- |
temlikeFig.4atoFig.4bwouldberegardedasamajor
|              |        |         |     |         |     |             | takes into | account | both | the | size and | rotation rateofthe |     |
| ------------ | ------ | ------- | --- | ------- | --- | ----------- | ---------- | ------- | ---- | --- | -------- | ------------------ | --- |
| cyclogenesis | event, | despite | the | absence | of  | any central |            |         |      |     |          |                    |     |
system.Themaindifficultywithcirculationcalculations
| vorticity | change. | Examples |     | from the | Northern | Hemi- |     |     |     |     |     |     |     |
| --------- | ------- | -------- | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
liesindefiningtheregionofcyclonicairflowassociated
|     |     |     |     |     |     |     | with each | vortex. | This   | possibly | explains  | why      | suchcal- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | -------- | --------- | -------- | -------- |
|     |     |     |     |     |     |     | culations | are     | seldom | made.    | The outer | boundary | of a     |
21 Bergeron (cid:53) (24 hPa day(cid:50)1) (cid:51) (sin(cid:102)/sin60(cid:56)), where (cid:102)is the cyclone could be defined by the zero (or some other)
latitudeofthecyclonecenter(SandersandGyakum1980). contour of vorticity. While this definition is workable
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

601
| SEPTEMBER1997 |     |     | SINCLAIR |               |                |     |           |              |     |
| ------------- | --- | --- | -------- | ------------- | -------------- | --- | --------- | ------------ | --- |
|               |     |     |          | for discrete, | well-separated |     | vortices, | it is common | for |
severalcentersofrotationtoexistwithinabroadregion
|     |     |     |     | of cyclonic | rotation. | Such | a situation | is illustrated | in  |
| --- | --- | --- | --- | ----------- | --------- | ---- | ----------- | -------------- | --- |
Fig.5a.Here,‘‘closed’’centersaremarkedwitha‘‘C’’
|     |     |     |     | where the      | vorticity      | center  | occurs within | 300            | km of a  |
| --- | --- | --- | --- | -------------- | -------------- | ------- | ------------- | -------------- | -------- |
|     |     |     |     | local pressure | minimum.       | All     | other         | (open) centers | are      |
|     |     |     |     | marked         | with an ‘‘X.’’ | In all, | the complex   | low            | pressure |
systeminFig.5acontainssixrotationcenters.Ourtask
|     |     |     |     | is to allocate | a domain | to each. |            |           |     |
| --- | --- | --- | --- | -------------- | -------- | -------- | ---------- | --------- | --- |
|     |     |     |     | The procedure  | assumes  | that     | the region | belonging | to  |
eachvortexjustcoverstheregionofdecreasingcyclonic
vorticitysurroundingeachmaximum.Startingfromthe
|     |     |     |     | location      | of the cyclonic | vorticity                     | maximum,asearchis |                |            |
| --- | --- | --- | --- | ------------- | --------------- | ----------------------------- | ----------------- | -------------- | ---------- |
|     |     |     |     | made radially | outward         | for thelocationwhereeitherthe |                   |                |            |
|     |     |     |     | vorticity     | becomes         | zero or                       | the radial        | vorticity      | gradient   |
|     |     |     |     | changes       | sign, whichever | occurs                        | first             | (i.e., is      | closest to |
|     |     |     |     | the center).  | Interpolation   | is                            | based on          | a continuous   | bi-        |
|     |     |     |     | cubic spline  | fit to          | the vorticity                 | field.            | This procedure | is         |
|     |     |     |     | repeated      | every few       | degrees                       | of azimuth        | around         | a com-     |
pletecircleand,thelocationsoftheboundarypointsso
|     |     |     |     | found, saved.       | For                   | this procedure,   | a            | radial grid       | spacing   |
| --- | --- | --- | --- | ------------------- | --------------------- | ----------------- | ------------ | ----------------- | --------- |
|     |     |     |     | (cid:68)r           |                       |                   | 1(cid:56)    |                   |           |
|     |     |     |     | of 111              | km (equivalent        |                   | to latitude) | and               | an azi-   |
|     |     |     |     |                     |                       | (cid:68)(cid:117) |              | (20(cid:56))      |           |
|     |     |     |     | muthal              | increment             | of 0.34906        | radians      |                   | were      |
|     |     |     |     | used. An            | overly coarse         | polar             | grid         | tended to         | produce   |
|     |     |     |     | erratic boundaries, |                       | while a           | finer grid   | resulted          | in an un- |
|     |     |     |     | acceptable          | increase              | in processing     | time.        | To avoid          | very      |
|     |     |     |     | narrow              | elongations           | such as           | might occur  | along             | fronts,   |
|     |     |     |     | boundary            | points were           | only              | permitted    | to change         | radius    |
|     |     |     |     | by r/3 km           | (20(cid:56))(cid:50)1 | azimuth,          | while to     | avoid overlapping |           |
|     |     |     |     | domains,            | vertices              | that fell         | inside an    | adjacent          | domain    |
|     |     |     |     | were relocated      | radially              | inward            | to the       | first point       | outside   |
|     |     |     |     | the neighboring     | domain.               |                   |              |                   |           |
|     |     |     |     | The                 | cyclone domains       | obtained          | by           | this method       | are       |
|     |     |     |     | shown in            | Fig. 5b. Here,        | an                | r of 500     | km has been       | used      |
o
|     |     |     |     | for the     | spatial smoothing. |             | Because | of the finite | grid |
| --- | --- | --- | --- | ----------- | ------------------ | ----------- | ------- | ------------- | ---- |
|     |     |     |     | increments, | there is           | some slight | overlap | between       | some |
adjacentboundarylinesegments(butnotvertices).Cir-
|     |     |     |     | culation             | was computed                                                     | for | each cyclone | by  | summing |
| --- | --- | --- | --- | -------------------- | ---------------------------------------------------------------- | --- | ------------ | --- | ------- |
|     |     |     |     | theproduct|(cid:122) | |r(cid:68)r(cid:68)(cid:117)overeach(r,(cid:117))pointintheshad- |     |              |     |         |
gr
|     |     |     |     | ed domain, | where | r is the | radial distance | from | the cy- |
| --- | --- | --- | --- | ---------- | ----- | -------- | --------------- | ---- | ------- |
clonecenterand(cid:68)rand(cid:68)(cid:117)aretheradialandazimuthal
|     |     |     |     | increments, | respectively. | The | circulation | values | ob- |
| --- | --- | --- | --- | ----------- | ------------- | --- | ----------- | ------ | --- |
tainedforeachregionareplottedinunitsof107m2s(cid:50)1,
|     |     |     |     | or circulation  | units         | (CU).           | A circulation           | of 10              | CU is |
| --- | --- | --- | --- | --------------- | ------------- | --------------- | ----------------------- | ------------------ | ----- |
|     |     |     |     | roughly         | equivalent    | to a tangential | wind                    | component          | of    |
|     |     |     |     | 10 m s(cid:50)1 | at a radius   | of 1600         | km or                   | a mean vorticityof |       |
|     |     |     |     | around          | 1.25 CVU      | over the        | same circular           | area.              |       |
|     |     |     |     | The effect      | of increasing |                 | r isshowninFig.5c.Here, |                    |       |
o
anr of1000kmhasbeenused.Thisresultsinmerging
o
|                    |                |                      |                   | of the three | vortices        | near    | New Zealand | into               | a single |
| ------------------ | -------------- | -------------------- | ----------------- | ------------ | --------------- | ------- | ----------- | ------------------ | -------- |
|                    |                |                      |                   | circulation  | of strength     | 7.3 CU. | Theother    | threevortices      |          |
| FIG. 5. (a)        | MSL pressure   | (solid, every 5 hPa) | and cyclonic geo- |              |                 |         |             |                    |          |
|                    |                |                      |                   | remained     | intact. Because | it      | involves    | spatial averaging, |          |
| strophic vorticity | (dashed, every | 1 CVU) for           | 0000 UTC 1 August |              |                 |         |             |                    |          |
circulationislessdependentoneffectiveresolutionthan
| 1984. Cyclonic    | vorticity maxima | have been marked | ‘‘C’’ (closed        |                 |         |     |          |                  |     |
| ----------------- | ---------------- | ---------------- | -------------------- | --------------- | ------- | --- | -------- | ---------------- | --- |
|                   |                  |                  |                      | point measures. | Despite | the | doubling | of the smoothing |     |
| center associated | with a pressure  | minimum) or      | ‘‘X’’ (open center). |                 |         |     |          |                  |     |
Contourlabelshavebeenomittedforclarity.(b)Asin(a)butwith radius, the circulation for the three vortices south of
domains for each circulation system outlined and shaded, and cir- NewZealanddecreasedbyanaverageoflessthan20%
| culationvaluesinCUincludedforeachregion,forr |     |     | (cid:53)500km.(c) |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
(cid:53)1000km. o while their central (point) vorticities fell by an average
Asfor(b)exceptr
|     | o   |     |     | of 40%. |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

602
|     |     |      |          |                 | WEATHER      | AND             | FORECASTING          |                         |              |         |            |     | VOLUME12 |
| --- | --- | ---- | -------- | --------------- | ------------ | --------------- | -------------------- | ----------------------- | ------------ | ------- | ---------- | --- | -------- |
|     |     | F IG | .6 . M S | L p r e ss u re | ( s o li d , | e v er y 10 h P | a ) a n d c y c lo n | ic (cid:122) ( d a s he | d , ev e r y | 2 C V U | )fo r 12 0 | 0   |          |
gr
|     |     | UT C | 7 J ul y 1      | 98 9 , w i th | c i r cu l a ti | o n d om ai n | s a n d v a lu e s a d | de d , a s i n | F ig . 5 , f or | (a ) r (cid:53) | 5 00 k | m   |     |
| --- | --- | ---- | --------------- | ------------- | --------------- | ------------- | ---------------------- | -------------- | --------------- | --------------- | ------ | --- | --- |
|     |     |      | (cid:53)1000km. |               |                 |               |                        |                |                 | o               |        |     |     |
and(b)r
o
In Fig. 6, vortex domains with associatedcirculation 4. Case selection from a cyclone database
| estimates | are        | shown for      | the entire  | hemispherefor1200 |               |       |                |              |               |              |        |          |            |
| --------- | ---------- | -------------- | ----------- | ----------------- | ------------- | ----- | -------------- | ------------ | ------------- | ------------ | ------ | -------- | ---------- |
|           |            |                |             |                   |               |       | The            | availability | of a          | database     | of     | cyclone  | tracks can |
| UTC 7     | July 1989. | A particularly |             | intense           | 932-hPa       | low   |                |              |               |              |        |          |            |
|           |            |                |             |                   |               |       | greatly        | simplify     | the selection |              | ofpast | storms   | forcaseor  |
| south of  | Africa     | has a          | circulation | of                | 19.1 CU       | for r | of             |              |               |              |        |          |            |
|           |            |                |             |                   |               | o     | climatological |              | studies.      | For example, |        | cyclones | having     |
| 500 km    | (Fig.      | 6a) and 17.3   | CU          | for r             | (cid:53) 1000 | km (F | ig.            |              |               |              |        |          |            |
o
6b).Otherlessintensesystemshave smallercirculation certain intensity characteristics in common are needed
values.ThreecirculationsinFig.6aofstrength8.4,2.1, for composite studies (e.g., Sanders 1986; Manobianco
1989;Gyakumetal.1992;BullockandGyakum1993).
| and 0.9 | CU in | the southeast | Pacific |     | mergeintoasingle |     |     |     |     |     |     |     |     |
| ------- | ----- | ------------- | ------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
70(cid:56)S, 100(cid:56)W Automated techniques can expedite the case selection
| 9.9-CU | vortex | centered | near |     |     | at coarser |         |             |           |     |        |             |     |
| ------ | ------ | -------- | ---- | --- | --- | ---------- | ------- | ----------- | --------- | --- | ------ | ----------- | --- |
|        |        |          |      |     |     |            | process | by avoiding | laborious |     | manual | examination | of  |
resolution(Fig.6b).Thisindicatesthatsomeambiguity
remains about what actually constitutes a cyclone. At thousands of synoptic charts while yielding consistent,
| finer resolution, |     | a single | large | circulation | system | may | repeatable | results. |     |     |     |     |     |
| ----------------- | --- | -------- | ----- | ----------- | ------ | --- | ---------- | -------- | --- | --- | --- | --- | --- |
Inthissection,weoutlineanautomatedcaseselection
| break up | into | several circulation. |     | In  | addition, | temporal |     |     |     |     |     |     |     |
| -------- | ---- | -------------------- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
rationaleforexhaustivelyselectingcyclonespossessing
| discontinuities |     | may arise | where | a new | secondary | de- |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ----- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
velopment divides a cyclone into two circulations. specifiedintensityandgeographicalcharacteristics.Our
|     |     |     |     |     |     |     | task may | be to                                       | list all | particularly |     | intense | winter cy- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------------------------------- | -------- | ------------ | --- | ------- | ---------- |
|     |     |     |     |     |     |     | clones   | (say,thosewhosecirculationattainedatleast20 |          |              |     |         |            |
c. Circulation estimates for Figs. 3 and 4 CU or whose central pressure fell below 960 hPa) for
|             |     |           |          |     |           |       | the western | North | Atlantic | (say, | bounded | by90(cid:56)–30(cid:56)E, |     |
| ----------- | --- | --------- | -------- | --- | --------- | ----- | ----------- | ----- | -------- | ----- | ------- | ------------------------- | --- |
| Circulation |     | estimates | obtained | as  | described | above |             |       |          |       |         |                           |     |
30(cid:56)–60(cid:56)N)
were found to better represent the circulation strength and during November–April for the years
for the situations depicted in Figs. 3 and 4. For the 1950–95.Alternatively,wemaywantalistingofrapidly
situation in Figs. 3a–c, circulation increased from 5.3 intensifying cyclones (e.g., those which deepen faster
|     |     |     |     |     |     |     | than 1 | B or whose | circulation |     | increases | faster | than 6 |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ----------- | --- | --------- | ------ | ------ |
CUthrough7.6CU(Fig.3b)to9.3CU(Fig.3c),despite
day(cid:50)1)
the rising central pressure. Conversely, the circulation CU for the same region.
for the storm in Figs. 3d–f remained remarkably con- Case selection is made from a database of cyclone
stant(between12.5and12.8CU)inspiteofthe25-hPa tracks, obtained via the methodology described in this
fall in central pressure. Likewise, the pairs of cyclones paper. For each cyclone as tracked, the date, latitude,
longitude,pressure,vorticity,andcirculationarearchived
| in Fig. | 4 having | similar | central | vorticity |     | had widely |     |     |     |     |     |     |     |
| ------- | -------- | ------- | ------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
differing circulation:5.7and13.7CU,respectively,for for each track point. Selections are made from the da-
Figs. 4a and 4b, and 3.7 and 14.3 CU for Figs. 4c and tabase by computer by searchingfortrackpointshaving
4d. Thus, for the cases illustrated, the disparities as- the desiredproperties.Acyclonedatabaseinterfacepro-
sociated with point measures of pressure and vorticity gram called TRAXis used to provideavarietyoffilters
have been avoided by use of circulation. for cyclone properties. Cyclones can be selected on the
In conclusion, circulation estimates show promisein basis of any combination of pressure, vorticity, circula-
avoidingthediscrepanciesassociatedwithusingcentral tion, movement, geographical location, position intrack
pressureorvorticitytoestimatecyclonestrength.How- (start, end, or nth), track length (time or distance), and
ever, caution must be exercised in interpreting circu- timecharacteristics.Outputcanbeintheformofcontour
lation changes following a system within which new maps of accumulated statistics as in Fig. 2, or as histo-
secondary centers form. gramsofcycloneproperties(asinSI95),orastextlistings
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

603
| SEPTEMBER1997 |     |     |     |     |     | SINCLAIR |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
ofcycloneshavingthedesiredproperties.Cyclonetracks vorticity above a threshold. The imposition of require-
andcentralpressureorvorticitytracescanalsobeplotted. ments on both vorticity and circulation seems to result
Although the TRAX software is interfaced to site- in greater case to case homogeneity for these intense
| specific | graphics | packages, | the | heart of | the software |     | is storms. |     |     |     |     |     |
| -------- | -------- | --------- | --- | -------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
the simple logic for cyclone selection. Time filters are Of course, this limited sample is just a guide to pos-
| applied | first. Cyclones | can | be selected |     | on the | basis of |     |     |     |     |     |     |
| ------- | --------------- | --- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
siblecaseselectioncriteria.Othercycloneareaorshape
year(s)and/ormonth(s).Othertimefilterscanbeadded parameters are readily obtainable as by-productsof the
as neccessary. For example, one could selectjustthose circulation calculations.Additionalquantitiesderivable
periods where the Southern Oscillation index (SOI) is from the MSL pressure field such as geostrophic or
betweenspecifiedboundsbyinterfacingwithadatabase gradientwindstreamfunction,kineticenergy,orangular
| of monthly | SOI | values. | In the | study | of Kidson | and |     |     |     |     |     |     |
| ---------- | --- | ------- | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
momentumcanreadilybecomputedforeachtrackpoint
Sinclair (1995), composites of cyclone statistics were and included as additional parameters in the cyclone
accumulated for episodes of persistent regional geo- database. Where multilevel gridded data are available,
potential height anomalies. Geographic filters can be other parameters related to(say)orientationorstrength
| applied | to select | cyclones | within | latitude–longitude |     |     |     |     |     |     |     |     |
| ------- | --------- | -------- | ------ | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ofpotentialvorticityextrema,jetstreaks,orfrontalchar-
boundsorthosepassingwithinaspecifieddistancefrom
acteristicscouldalsobeincluded,dependingonthegoal
| a specified | point. | This last | feature | can | be used | to con- | of the study. |     |     |     |     |     |
| ----------- | ------ | --------- | ------- | --- | ------- | ------- | ------------- | --- | --- | --- | --- | --- |
struct time series of cyclone activity for specific loca- Forcyclogenesisstudies,variousstagesinacyclone’s
tions. Cyclone translation velocity, computed from the life can be objectively identified from vorticity or cir-
trackcoordinates,canbeusedtoselectcyclonesmoving
|                 |           |     |        |        |        |         | culation variations,                             | as in     | SI95. Figure        | 8   | shows | the for- |
| --------------- | --------- | --- | ------ | ------ | ------ | ------- | ------------------------------------------------ | --------- | ------------------- | --- | ----- | -------- |
| in a particular | direction |     | and/or | faster | than a | certain |                                                  |           |                     |     |       |          |
|                 |           |     |        |        |        |         | mation, development,                             | maturity, | anddecaystagesofthe |     |       |          |
| speed.          |           |     |        |        |        |         | threestormsinFigs.7i–k.Here,formationwasthefirst |           |                     |     |       |          |
Selection criteria for composite studies need to be track point (or the beginning of circulation increases
carefully chosen to ensure a reasonable degree of case whereaweakdisturbanceexistedforseveraldaysbefore
| to case | homogeneity.    | We        | have | already     | seen how | cases |                |             |                |     |              |      |
| ------- | --------------- | --------- | ---- | ----------- | -------- | ----- | -------------- | ----------- | -------------- | --- | ------------ | ---- |
|         |                 |           |      |             |          |       | intensifying), | development | (decay)        | was | the time     | when |
| having  | similar central | vorticity |      | can possess | rather   | dif-  |                |             |                |     |              |      |
|         |                 |           |      |             |          |       | the cyclonic   | circulation | was increasing |     | (decreasing) |      |
ferent structure (Fig. 4). Figure 7 shows examples of mostrapidly,whilematuritywasthestageofmaximum
intensecyclonesnearNewZealand,objectivelyselected circulation.Compositesbasedonalargenumberofcy-
usingthreedifferentmeasuresofcycloneintensity:cen-
|                |           |     |     |         |       |          | clones can | then be constructed | for | eachlifecyclestage |     |     |
| -------------- | --------- | --- | --- | ------- | ----- | -------- | ---------- | ------------------- | --- | ------------------ | --- | --- |
| tral vorticity | exceeding | 12  | CVU | (panels | a–d), | circula- |            |                     |     |                    |     |     |
todeterminepersistentbasicfeatures,asinManobianco
| tion exceeding | 14  | CU (panels | e–h),      | and | both | vorticity |            |              |              |     |     |     |
| -------------- | --- | ---------- | ---------- | --- | ---- | --------- | ---------- | ------------ | ------------ | --- | --- | --- |
|                |     |            |            |     |      |           | (1989) and | Sinclair and | Cong (1992). |     |     |     |
| (cid:46)10     |     |            | (cid:46)10 |     |      |           |            |              |              |     |     |     |
CVU and circulation CU (panels i–l). These We have shown how an automated cyclone finding,
selectionsweremadeexhaustivelyforaregionbounded tracking, and case selection rationale can greatly facil-
| by 30(cid:56)–50(cid:56)S | and | 150(cid:56)E–150(cid:56)W |     | from | ECMWF | data |           |                       |     |      |              |     |
| ------------------------- | --- | ------------------------- | --- | ---- | ----- | ---- | --------- | --------------------- | --- | ---- | ------------ | --- |
|                           |     |                           |     |      |       |      | itate the | selection of cyclones | for | case | or composite |     |
spanning1980–94.Inthisinstance,theTRAXsoftware
studiesfromalongseriesofgriddedanalyses.However,
| generated | a list file | containing |     | the track | coordinates, |     |     |     |     |     |     |     |
| --------- | ----------- | ---------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
itshouldbenotedthatobjectivecaseselectiondoesnot
times, and other properties of all cyclones having the reduce the need for careful synoptic appraisal of each
desiredcharacteristics.Thisfilewasthenreadbyaplot-
|                                             |             |                                        |                 |      |           |          | case selected. |             |     |     |     |     |
| ------------------------------------------- | ----------- | -------------------------------------- | --------------- | ---- | --------- | -------- | -------------- | ----------- | --- | --- | --- | --- |
| ting program                                | to produce  |                                        | Fig. 7.         |      |           |          |                |             |     |     |     |     |
| Included                                    | in Fig.     | 7 are                                  | gradient        | wind | isotachs  | and      |                |             |     |     |     |     |
| contours                                    | of gradient | wind                                   | streamfunction, |      | (cid:99), | obtained |                |             |     |     |     |     |
|                                             |             |                                        |                 |      |           |          | 5. Cyclone     | climatology |     |     |     |     |
| bysolving(cid:44)2(cid:99)(cid:53)(cid:122) |             | for(cid:99)bysuccessiveoverrelaxation. |                 |      |           |          |                |             |     |     |     |     |
gr
This allows easier comparison for cyclonesatdifferent One means of assessing any objective procedure for
latitudes, since, unlike pressure or geopotential, the (cid:99) tracking meteorological features is to compare results
field corresponding to a given wind field is latitude in- with the old, time-honored manual approach. In this
dependent. Contours of (cid:99)are scaled by 2(cid:86) sin((cid:50)60(cid:56))/ section, a selection of winter season cyclone statistics
(10g)((cid:50)1.2874(cid:51)10(cid:50)6)tocorrespondwithgeopotential for both hemispheres is obtained via the methodology
60(cid:56)S.
height in dam at outlined in this paper and compared with previous re-
Intensecyclonesselectedsolelyonthebasisofstrong sults.Onlyabriefsurveyoftheclimatologicalbehavior
centralvorticity(Figs.7a–d)tendtobesmallandtight, of cyclones will be presented here. Moredetailedanal-
withsomevariabilityinsizeasinFig.4.Incomparison, ysis, discussion, and interpretation of results will be
|          |                   |     |     |           |          |      | saved for | a future study. |     |     |     |     |
| -------- | ----------------- | --- | --- | --------- | -------- | ---- | --------- | --------------- | --- | --- | --- | --- |
| the four | storms possessing |     | the | strongest | cyclonic | cir- |           |                 |     |     |     |     |
culation (Figs. 7e–h) are much larger systems having For this survey, twice-daily ECMWF 1000-hPageo-
more open centers with weaker central vorticity.These potential analyses during 1980–94 (SH) and 1980–87
appear to represent cyclones at a more mature stage of (NH)areused.ThesearefirstsmoothedwithaCressman
development than those in Figs. 7a–d and vary some- smoother(r (cid:53)500km)andcyclonesidentifiedasmax-
o
(cid:122)
what in the extent of strong gradient flow. The bottom ima of cyclonic exceeding 1 CVU and tracked, as
gr
row shows systems having both circulation and central outlinedearlier.Quasi-stationaryorographicfeaturesare
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

604
|     |     |     | WEATHER AND | FORECASTING |     |     | VOLUME12 |
| --- | --- | --- | ----------- | ----------- | --- | --- | -------- |
F . 7 . G r a d i en t wi n d s tr e a m f u n c ti o n (s o l i d , e v er y 5 eq u iv a l e n td a m ) , c y c lo n ic (cid:122) ( da s h e d , ev e ry 2 C V U ), a n d g r a di e nt w i n d (cid:46) 1 8 a n d
| IG  |     |     |     |     | g r |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
25 m s (cid:50) 1 (s h a d e d ) on a 2 0 (cid:56) la t i tu d e r a d i us p o l a r g r id a t the lo c a ti o n s in d ic a t e d b e lo w e a c h p l o t f or th e in di ca te d ti m e s, f o r 1 2 in te n s e cy c lo n e s
nearNewZealand,selectedfromthedatabasefromthefollowingcriteria:(a)–(d)central(cid:122) (cid:46)12CVU,(e)–(h)circulation(cid:46)14CU,and
| (i)–(l)(cid:122) (cid:46)10CVUandcirculation(cid:46)10CU. |     |     |     |     | gr  |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
gr
theUrals(near80(cid:56)E),andnear
removedandonlycycloneslasting2ormoredays(four the the Rockies, east of
or more analyses) are considered. the Caspian Sea. In all these details, Fig. 9a is quite
|     |     |     |     | similar to | Fig. 2a of Whittaker | and Horn | (1984), based |
| --- | --- | --- | --- | ---------- | -------------------- | -------- | ------------- |
onmanualanalysesandtracking.Somedifferencesexist
| a. Northern | Hemisphere |     |     |                 |              |                |           |
| ----------- | ---------- | --- | --- | --------------- | ------------ | -------------- | --------- |
|             |            |     |     | over the middle | latitudes of | Asia, a region | where MSL |
Figure 9 shows a range of cyclone statistics for the pressure fields are complicated by mountainous terrain
NH winter (October–March). In Fig. 9a, a count ofcy- anduncertainpressurereductionstosealevel,andwhere
clonetrackspassingwithin5(cid:56)latitude(555km)ofeach data was missing during part of the analysis period in
grid point (‘‘track density’’) is obtained by counting Whittaker and Horn’s study.
centers just once per cyclone for each grid point. This Over thewest-centralPacific,bothFig.9aandWhit-
measure of cyclone activity is similar to that used by taker and Horn (1984) indicate maximum cyclone ac-
tivitynear40(cid:56)N.However,Gyakumetal.(1989),using
| Whittaker | and Horn (1984) | and indicates | twoprincipal |     |     |     |     |
| --------- | --------------- | ------------- | ------------ | --- | --- | --- | --- |
regions of cyclone activity; one extending from near a simple count of centers, found highest cyclone fre-
JapantowardtheGulfofAlaskaandtheotherspiraling quenciesbetween50(cid:56)and65(cid:56)N,withlocalizedmaxima
poleward from east of North America toward Iceland in the Gulf of Alaska and near Kamchatka Peninsula.
and the Arctic Ocean. Otherlocalizedmaximaareseen Figure10showsthatthedifferencesbetweenthesestud-
over the Mediterranean Sea, the Great Lakes, east of ies are consistent with the differing methods used to
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

SEPTEMBER1997 SINCLAIR 605
FIG.8.MSLpressure(solid,every5hPa),cyclonic(cid:122)
gr
(dashed,every2CVU),andgradientwind(cid:46)18and25ms(cid:50)1(shaded)ona15(cid:56)
latituderadiuspolargridatthelocationsandtimeindicatedneareachplotforthreecasesofcyclogenesis.Fourstagesofdevelopmentare
shown:genesis(a),(e),(i),development(b),(f),(j),maturity(c),(g),(k),anddecay(d),(h),(l).Seetextformoredetails.
countcyclones.InFig.10a,cyclonesarecountedusing volvingapplicationofanidenticalmethodologytopre-
trackdensity,asinWhittakerandHorn(1984)(andFig. vious datasets is outside the scope of this study.
9a),whereasasimplecountofallcenterswithoutregard Average cyclone motion vectors are included inFig.
totracking(‘‘systemdensity’’)yieldsadistribution(Fig. 9a. Cyclones are most mobile over the western Pacific
10b) close to that in Fig. 1 of Gyakum et al. (1989). near35(cid:56)Nandbetween40(cid:56)and50(cid:56)NoverNorthAmer-
Increased counts at higher latitudes in Fig. 10b and in ica and the western Atlantic. Cyclones have a mean
Gyakumetal.(1989)arisebecausemorethanonecount poleward component of motion in the Gulf of Alaska
pertrackisallowed,givingextraweighttoslower-mov- and in the North Atlantic and an equatorward compo-
ing systems in the Gulf of Alaska. Although changes nent east of the Rockies.
in data coverage and intrinsic cyclone variability from Instances of cyclone formation (Fig. 9b) are defined
year to year also contribute to differences between the as all first track points having circulation weaker than
earlierstudies,thesesourcesofvariabilityappearsmall- 3 CU for cyclones ultimately attaining at least that in-
er, as the year to year standard deviation (not shown) tensity as tracked. As discussed in SI95, this definition
overthe7yrconsideredhereamountstolessthan20% excludescyclonesthatremainweakduringtheirlife,as
of the contoured values in Fig. 9a, Other factors such well as those that already haveconsiderablecirculation
as the present use of a Cressman smoother and the 1 at the first track point. Favored genesis areas include
CVU threshold for detecting a cyclone will also affect the warm waters of the Kuroshio Current and Gulf
these comparisons. A more rigorous comparison in- Stream on the upstream equatorward flank of themean
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

606 WEATHER AND FORECASTING VOLUME12
FIG.9.CyclonestatisticsfortheNorthernHemispherewinter(October–March),fortheyears
1980–86.(a)Cyclonetrackdensity,drawnevery1center(5(cid:56)latcircle)(cid:50)1month(cid:50)1,withaverage
cyclone translation vectors added (the vector to the left represents 10 m s(cid:50)1). Count of (b)
formation locations, every 0.2 (5(cid:56) circle)(cid:50)1 month(cid:50)1, with SST gradient maxima exceeding 8(cid:56)
and10(cid:56)C(1000km)(cid:50)1added(shaded);(c)cyclogenesislocations,every0.5(5(cid:56)circle)(cid:50)1month(cid:50)1,
withSSTgradientsasin(b);(d)cyclolysislocations,every0.5(5(cid:56)circle)(cid:50)1month(cid:50)1;(e)central
vorticitychanges(cid:46)4CVU,every0.2(5(cid:56)circle)(cid:50)1month(cid:50)1;(f)centralpressurefalls(cid:46)1Bergeron,
every0.5(5(cid:56)circle)(cid:50)1(month)(cid:50)1;and(g)tight(thick,solid)andopen(thinsolid)vortices,every
0.2(5(cid:56)circle)(cid:50)1month(cid:50)1,withcontourlabelsremovedforclarity.The‘‘Trx’’and‘‘Pos’’values
at the top right of each panel refer, respectively, to the numbers of cyclones (as tracked) and
positions(centers)usedforeachplot.
SST gradient maxima (shaded) near the eastern sea- (1976),WhittakerandHorn(1984),andRoebber(1984)
boards of Asia and North America. Other formation havealsonotedthattheregionsofstrongSSTgradients
regionsarefoundnearthedateline,eastoftheCanadian are conducive in a climatological sense to the devel-
RockiesandtheTibetanPlateau,overthewesternMed- opmentofmaritimecyclones.Cycloysis(Fig.9d)occurs
iterranean Sea, and near the Caspian Sea.Theseresults well downstream from formation and development
are consistent with formation locations obtained man- regions, and at higher latitudes (near 60(cid:56)N), with max-
ually by Whittaker and Horn (1984), Roebber (1984), ima in the Gulf of Alaska and near Iceland.
and Gyakum et al. (1989), where they are discussedin The geographical distribution of rapid cyclogenesis
more detail. events basedonthreedifferentintensitychangecriteria
Wintercyclogenesisoccurrences(Fig.9c)wereiden- areshown in Figs. 9e–g. Panel eshowsthedistribution
tified similarly to SI95 as instances where central vor- ofthe658instanceswherethecentralvorticityincrease
ticity increased faster than 2 CVU day(cid:50)1. Intensifying following a storm exceeded 4 CVU day(cid:50)1.Asformore
cyclones arefound with highestfrequencyintwoelon- moderate cyclogenesis events (Fig. 9c), rapidly inten-
gatedzonesextendingdownstreamfromthecorrespond- sifying cyclones are found in highest numbers on the
inggenesisregionsovertheeasternseaboards,adjacent equatorward flank of the maximum climatologicalSST
tothemaximumSSTgradientsintheseregions.Colucci gradient near the warm Kuroshio and Gulf Streamcur-
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

607
| SEPTEMBER1997 |     |     | SINCLAIR |     |     |     |     |     |     |     |
| ------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
FIG.9.(Continued)
|     |     |     |     | rents, with     | an       | additional   | smaller | frequency              |           | maximum   |
| --- | --- | --- | --- | --------------- | -------- | ------------ | ------- | ---------------------- | --------- | --------- |
|     |     |     |     | off the Pacific |          | coast of     | Canada. | The thresholdvorticity |           |           |
|     |     |     |     | change          | used for | Fig. 9e      | was     | chosen to              | yield     | a similar |
|     |     |     |     | sample          | size to  | cases having | a       | pressure               | deepening | rate      |
(cid:46)1B.Thegeographicaldistributionoftheserapiddee-
|     |     |     |     | peners is | shown | in Fig. | 9f. They | occur | slightly | down- |
| --- | --- | --- | --- | --------- | ----- | ------- | -------- | ----- | -------- | ----- |
streamfromlocationsofstrongestvorticitychange(Fig.
|     |     |     |     | 9e) and          | have a       | distribution                                     | similar       | to                   | that of      | ‘‘bombs’’  |
| --- | --- | --- | --- | ---------------- | ------------ | ------------------------------------------------ | ------------- | -------------------- | ------------ | ---------- |
|     |     |     |     | obtained         | by Roebber   | (1984)                                           | and           | Gyakumet             |              | al.(1989). |
|     |     |     |     | Instances        | of           | circulationincreases(cid:46)6CUday(cid:50)1(Fig. |               |                      |              |            |
|     |     |     |     | 9g) occur        | even         | farther                                          | downstream    | from                 | the          | region of  |
|     |     |     |     | vorticity        | increases    | and                                              | pressure      | falls,               | especially   | in the     |
|     |     |     |     | Pacific,         | suggesting   | that                                             | strengthening |                      | of the       | low-level  |
|     |     |     |     | cyclonic         | flow over    | a wider                                          | area          | occurs               | somewhat     | later      |
|     |     |     |     | in the cyclone’s |              | life. This                                       | has           | possible             | implications | on         |
|     |     |     |     | mean cyclone     |              | structure.                                       | Figure9h      | indicatesthattighter |              |            |
|     |     |     |     | vortices         | (those       | possessing                                       | large         | central              | vorticity    | to cir-    |
|     |     |     |     | culation         | ratios)      | as analyzed                                      | by            | the ECMWF            |              | are most   |
|     |     |     |     | frequent         | near eastern | seaboards,while‘‘open’’systems                   |               |                      |              |            |
|     |     |     |     | possessing       | moderate     | or                                               | strong        | circulation          | but          | compar-    |
|     |     |     |     | atively          | weak inner   | vorticity                                        |               | (like Figs.          | 4d           | and 7e–h)  |
occurwelldownstream:intheGulfofAlaska,southeast
| FIG. 10. Cyclone | statistics | for a portion of the North | Pacific, for |     |     |     |     |     |     |     |
| ---------------- | ---------- | -------------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
October–Marchfor1980–86.(a)Trackdensity,every2(5(cid:56)-latradius of Greenland, and in the Arctic Ocean. Of course, the
circle)(cid:50)1(month)(cid:50)1.(b)Asin(a)exceptsystemdensity. present smoothed ECMWF analysescannotresolvethe
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

608
|     |     | WEATHER | AND | FORECASTING |     |     |     |     | VOLUME12 |
| --- | --- | ------- | --- | ----------- | --- | --- | --- | --- | -------- |
FIG.11.AsforFig.9exceptforSouthernHemispherewinter(April–September)during1980–
6(cid:56) 8(cid:56)C
|     | 94. SST gradients | exceeding | and (1000 | km)(cid:50)1 | are shaded | in panels | (b)–(d). | Contour |     |
| --- | ----------------- | --------- | --------- | ------------ | ---------- | --------- | -------- | ------- | --- |
intervals[number(5(cid:56)latradiuscircle)(cid:50)1(month)(cid:50)1]are(a)1,(b)0.2,(c),(d)0.3,(e)0.05,(f),(g)
0.1,and(h)0.2.
extremeinnercorepressuregradientsthatoccurincon- b. Southern Hemisphere
| junction with | ‘‘coiled spring’’ | developments       | (Rogers   |     |           |     |               |              |            |
| ------------- | ----------------- | ------------------ | --------- | --- | --------- | --- | ------------- | ------------ | ---------- |
|               |                   |                    |           | An  | identical | set | of statistics | is presented | for the SH |
| and Bosart    | 1991). Another    | caveat is that the | tightness |     |           |     |               |              |            |
of a particular center may be also linked to the avail- (Fig. 11). Track density (Fig. 11a) maximizes between
50(cid:56) 60(cid:56)S
ablility ofobservationsnear itscenteraswellastoany and in the Atlantic and Indian Ocean sectors,
intrinsic structure. Nevertheless,Fig.9hisatleastcon- and south of 60(cid:56)S in the Pacific, with a broader sec-
|     |     |     |     | ondary | maximum | spanning |     | the Pacific | near 40(cid:56)S, con- |
| --- | --- | --- | --- | ------ | ------- | -------- | --- | ----------- | ---------------------- |
sistentwithothercircumstantialevidence(e.g.,Reedet
al. 1988) linking stronger inner pressuregradientswith sistent with similar results obtained by SI94 and SI95.
50(cid:56)S
diabatic heating effects over the warm waters of the Cyclones are most mobile around in the Indian
GulfStreamandKuroshioCurrent.Incontrast,‘‘broad- Ocean sector. In comparison with the NH, the cyclone
er’’ systems having comparatively weak innervorticity distribution of the SH exhibits a high degree of zonal
symmetry.Acountofcenterswithoutregardtotracking
| appear to | represent mature systems | in a state | of decay, |     |     |     |     |     |     |
| --------- | ------------------------ | ---------- | --------- | --- | --- | --- | --- | --- | --- |
occurring as they do in cyclolytic regions (cf. Fig. 9d) (not shown) highlights the slower-moving cyclones
and over colder water. across New Zealand and the central Pacific, and those
| Insummary,NHcyclonestendtoformoverthewarm |     |     |     | south | of 60(cid:56)S. |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | ----- | --------------- | --- | --- | --- | --- |
waters of the Kuroshio Current and Gulf Stream and In comparison with SI94 and SI95, Fig. 11a depicts
intensify near the region of strongest SST gradient as ashifttowardhigherlatitudes.ThisisbecauseSI94and
comparatively tight vortices. During their lives, they SI95accumulatedstatisticsonapolarstereographicdo-
migrate eastward and poleward and expand in area be- main without prior Cressman smoothing, favoring cy-
fore slowing and decaying in the Gulf of Alaska and clone detection at lower latitudeswheregrid spacingis
|               |     |     |     |         |       |         | 30(cid:56)S |           | 60(cid:56)S). |
| ------------- | --- | --- | --- | ------- | ----- | ------- | ----------- | --------- | ------------- |
| near Iceland. |     |     |     | smaller | (grid | spacing | at          | is 0.8 of | that at       |
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

SEPTEMBER1997 SINCLAIR 609
FIG.11.(Continued)
However, this bias is smaller than the substantialhigh- tensifying to all cyclones) is coincident with it (not
latitude bias in previous studies based on detection of shown). Dissipation locations (Fig. 11d) are over-
cyclones as pressure minima. As found by SI94, these whelmingly found poleward of 60(cid:56)S, a region largely
studies exclude many mobile vorticity centers between covered with sea ice in winter and spring.
45(cid:56)and55(cid:56)Swhileincludinglargenumbersofspurious Rapidlyintensifyingcyclones(Fig.11e)aremostfre-
orographic features near Antarctica. This again rein- quenteastofSouthAmerica,southeastofAfrica,inthe
forcestheneedtoensurethatthemethodsusedtoiden- TasmanSea,andacrossthePacificnear35(cid:56)S,asinSI95.
tify cyclones do not introduce bias. In contrast, rapid deepeners (Fig. 11f) areentirelycon-
Favored genesis locations (Fig. 11b) include eastern fined to poleward of 40(cid:56)S, with a preference for the
coastsofAustraliaandSouthAmerica,acrosstheIndian Indian Ocean sector. As discussed by SI95, these dif-
Ocean near the maximum SST gradient near 40(cid:56)S, and ferences between the distribution of developing cy-
in a broad region spanning the subtropical Pacific be- clones as inferred from vorticity tendencies and those
tween30(cid:56)and40(cid:56)S,asinSI95.Cyclogenesis(Fig.11c) obtainedfromcentralpressurechangearepartlyrelated
ismostprevalentdownstreamfromtheseregions,max- to the unique climatological pressure field of the SH.
imizingeastofSouthAmerica,inabandextendingfrom Many instances of rapidly falling pressure are, in fact,
southeast of Africa into the high latitudes of the South artifacts of rapid poleward migration across the back-
Pacific, and throughout the middle latitudes of the Pa- ground mean pressure field (e.g., Figs. 3d–f).
cific sector. A relative minimum extendsacrossthePa- Largest circulation increases (Fig. 11g) occur near
cificnear50(cid:56)S.Thedouble-occurrencemaximuminthe 60(cid:56)S. This is possibly due to the fact that cyclones in
Pacific is thought to be related to theuniquedouble-jet this region merge with the semipermanent climatolog-
structure of the winter upper troposphere (SI95). Al- ical circumpolar trough, which involves considerable
thoughthelargestnumbersofintensifyingcyclonesare cyclonic circulation, even in its time-averaged state.
found poleward of the strongest SST gradients in the Tightervortices(Fig.11h)tendtooccurwithinthemain
Indian Ocean sector, the highest fraction (ratio of in- cyclogenetic regions (cf. Fig. 11c), while more open
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

610 WEATHER AND FORECASTING VOLUME12
centers are found near 60(cid:56)S. These results, of course, al. 1991;Thorncroftet al.1993),oradherencetovar-
are subject to analysis uncertainty over these southern ious conceptual models (Bjerknes and Solberg 1922;
oceans. Shapiro and Keyser 1990). Automated case selection
This brief examination of SH cyclones, based on 15 from objectively derived track data incorporating
years of data, extends the results of SI95 based on a such parameters at each track point as are germane
shorter series of ECMWF analyses. The results in Fig. to such classifications will increasingly be needed to
11,basedontheupdatedmethodology,confirmtheprin- assist with the huge task of assessing the relativeim-
cipalfindingsofSI94andSI95,despitethelow-latitude portance of these paradigms for different regions of
biasin thosestudies.ThereaderisreferredtoSI95and the globe.
the references therein for more detailed discussionand Finally, we have applied the methodology to obtain
interpretation of the climatological behavior of SH cy- a synoptic climatology for winter season cyclones in
clones. both hemispheres. Because the analyzed geographical
distributionofcyclonesissensitivetothecyclonecount-
ing procedure, results in good agreement with previ-
6. Concluding remarks
ouslypublishedNHworkbasedonthetraditionalman-
Thisstudyhasexaminedsomeoftheissuesassociated ual approach are only found when care is taken to use
with objectively identifying cyclones from numerical a methodology consistent with the earlier studies. Dis-
analyses. Modifications to the cyclone finding meth- crepancies between earlier studies appear to primarily
odology of SI94 result in a cyclone database free from resultfromdifferentcountingmethods,althoughintrin-
distortions arising from variations in grid spacing over sicstormtrackvariabilityandchangesinanalysisqual-
the domain. This is accomplished by prior smoothing ityanddatacoverageundoubtedlyalsocontribute.This
of the raw data using a constant radius Cressman-type finding reinforces a basic contention of this study: that
spatial smoother to ensure that a known scale of dis- care needsto be taken to ensurethataconsistentmeth-
turbanceisconsistentlyadmittedoverthedomain.This odology is used when comparing results fromdifferent
consistencyiscrucialwherethegoalistolookatsmall datasets.Theproceduresoutlinedinthispaperwillhelp
differences between cyclone behavior in different da- to ensure this consistency.
tasets (e.g., different GCMs). The present results, based on state-of-the-art opera-
Cyclones are identified as local maxima of cyclonic tional numerical analyses that incorporate remotely
vorticity to eliminate a further bias favoring slower- sensed data not used in earlier manual studies, have
movingormoreintensecyclonesthatoccurswhenpres- confirmed the general picture of cyclone life cycles
sureminimaareused.Orographicfeaturesnotnormally found in previous studies. Northern Hemisphere cy-
thought of as cyclones are also removed. A new pro- clones form and intensify near theeasternseaboardsof
cedure for estimating circulation is described. This as- Asia and North America, with activity focused on the
sesses cyclone strength on the basis of both size and regionsofstrongestSSTgradient.Theymoveeastward
rotation rate, thus avoiding incongruitiesthatoccasion- andpolewardduringtheirlivesbeforeweakeninginthe
ally arise with point measures such as central pressure twoprincipalNHcyclonegraveyards:theGulfofAlas-
or vorticity. Finally, an automated tracking scheme is ka and southeast of Greenland. In comparison, SH cy-
usedtogenerateadatabaseofcyclonetrackscontaining clones are more evenly distributed around the hemi-
center coordinates, pressure, vorticity, and circulation sphere. They tend to form and intensify in middle lat-
at each track point. itudes,especiallynearSSTgradientsoveropenoceans,
We have sketched an objective procedure for se- and near the eastern coasts of South AmericaandAus-
lecting cases from a cyclone track database obtained tralia, and decay at higher latitudes. There is some ev-
from an extended series of gridded MSL pressure idence that newly formed and intensifying cyclones in
charts. This avoids laborious manual examination of both hemispheres possess a tighter inner structurethan
thousands of synoptic charts to find suitable storms. mature and decaying systems.
Case selection is instead done by computer search of Thanks to the reanalysis efforts going on at NCEP
the databaseforcycloneshavingspecifiedproperties. andECMWF,highqualitymultidecadedatasetsofnu-
Selectionscanbeonthebasisofyear,month,location, merically analyzed data are now becoming available.
intensity (e.g., central pressure, vorticity or circula- We hope to construct weather system tracks from
tion), stage of development, and from intensity these datasets to establish a benchline contemporary
change characteristics. climatology that will advance our understanding of
Individual case studies based on intensive obser- the behavior of these circulation systems and how
vational campaigns have revealed the rich palette of they respond to and influence climate variability.
cyclone structures and life cycles found in nature. Workisabouttocommenceonobtainingcyclonesta-
There is now a growing effort to bring much of this tistics from a GCM to assess its ability in replicating
work together by attempting to classify cyclones on contemporary weather system behavior and to iden-
thebasisofcloudsignatures(e.g.,Evansetal.1994), tify possible shifts in storm characteristics under cli-
precursorsynoptic-scaleflowpatterns(e.g.,Davieset matechangescenarios.Inthistask,itwillbeessential
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

SEPTEMBER1997 SINCLAIR 611
to ensure that small differencesbetweendifferentda- APPENDIX
tasets are not artifacts of the cyclone finding meth-
Calculation of Gradient Wind Vorticity
odology.Objectiveproceduressuchasdescribedhere
will make all these tasks efficient and will ensure
Becausethegradientwindrepresentsanimprovement
consistent, robust results. over the geostrophic as an approximation to the real
wind,weestimatethegradientwindfieldanddetermine
Acknowledgments. Gridded atmospheric analyses itsvorticity.Thisestimateisbasedonthegradientwind
were provided by the ECMWF, while the SST datain equation
Figs. 9 and 11 were provided by the NCEP. Critical KV2 (cid:49) fV (cid:53) fV , (A1)
comments from three anonymous reviewers are ap- g
preciated, as they led to a substantially improved where V(V ) is the gradient (geostrophic) wind, f is the
g
manuscript.ThisworkwassupportedbytheNewZea- Coriolis parameter, and K the curvature of the parcel
land Foundation for Research, Science and Technol- trajectory.Here,wehaveapproximatedKbytheisobar
ogy. curvature, computed (after Trenberth 1977) as
(cid:93)2(cid:70)/(cid:93)x2((cid:93)(cid:70)/(cid:93)y)2 (cid:50) 2((cid:93)(cid:70)/(cid:93)x)((cid:93)(cid:70)/(cid:93)y)(cid:93)2(cid:70)/(cid:93)x(cid:93)y (cid:49) (cid:93)2(cid:70)/(cid:93)y2((cid:93)(cid:70)/(cid:93)x)2
, (A2)
[((cid:93)(cid:70)/(cid:93)x)2 (cid:49) ((cid:93)(cid:70)/(cid:93)y)2]3/2
where (cid:70) is the geopotential, (cid:93)/(cid:93)x is approximated as (over each grid point of each analysis) with (cid:122)obtained
(1/a cos(cid:102))(cid:93)/(cid:93)(cid:108), and (cid:93)/(cid:93)y is (cid:93)/a (cid:93)(cid:102)((cid:102), (cid:108)are latitude, directlyfromUandV.Asimilarcomparisonwasmade
longitude in radians, and a is the mean earth radius). for geostrophic vorticity, (cid:122). Cressman smoothing was
g
Cycloniccurvatureispositive(negative)intheNH(SH) as specified in section 2. Despite the approximations
andhasunitspermeter.Thesolutiontechniquefor(A1) inherent in the calculation of gradient winds, average
uses an iterative technique, where V is used as a first (cid:122) estimates were closer to (cid:122)than (cid:122) values, with an
g gr g
guess, V to V in a rearranged version of (A1), overall rms difference between (cid:122) and (cid:122)of 0.68 CVU
1 gr
V (cid:53) V /(1 (cid:49) KV /f). (A3) comparedto0.79for(cid:122) g .Whenthecomparisonwasmade
n g n(cid:50)1 for just cyclonic values, the rms difference for (cid:122) was
g
Here, the quantity KV /f in (A3) is constrained to lie morethan1CVUcomparedwithjust0.76CVUfor(cid:122) .
between(cid:50)0.25and0.5 n , (cid:50) l 1 imitingthegradientwindspeed In regions where cyclonic vorticity (cid:46)5 CVU (cf. Fig g s r .
tobetween2V /3and4V /3,withsmaller(larger)values 1 and 8), (cid:122) systematically overestimated (cid:122)by nearly3
g g g
for cyclonic (anticyclonic) flow. These limitswereem- CVU compared with just 1 CVU for (cid:122) , with rms dif-
gr
piricallyfoundtoyieldclosestagreementwithobserved ferencesof3.2and1.3,respectively.Thus,thegradient
wind in another dataset containing U and V in addition wind approximation as used here appears to yield im-
to H (see below). For the spatially smoothed dataused proved vorticity estimates over geostrophic values, es-
here,theselimitswereonlyoccasionallyreachedinthe pecially in the environs of cyclones, as applied in this
subtropics. For normal-gradient wind balance, the the- study.
oretical range is between zero and 2V , with the upper
g
limit required for real solutions to (A1). The vorticity
of the gradient wind, (cid:122) , was then calculated as REFERENCES
gr
(cid:122) (cid:53) (cid:93)v/(cid:93)x (cid:50) (cid:93)u/(cid:93)y (cid:49) u tan(cid:102)/a, (A4)
gr Akyildiz, V., 1985: Systematic errors in the behaviour of cyclones
where u and (cid:121)are the eastward and northward com- intheECMWFoperationalmodels.Tellus,37A,297–308.
Bell,G.D.,andL.F.Bosart,1989:A15-yearclimatologyofNorthern
ponentsofthegradientwind.Centereddifferenceswere
Hemisphere 500-mb closed cyclone and anticyclone centers.
used to compute the derivatives, with calculationslim- Mon.Wea.Rev.,117,2142–2163.
ited to poleward of 20(cid:56) latitude. Bjerknes, J., and H. Solberg, 1922: Life cycle of cyclones and the
This algorithm was evaluated by comparing (cid:122) , as polar front theory of atmospheric circulation.Geofys. Publ., 3
obtainedabove,withvorticity,(cid:122),obtaineddirectly g f r rom (1),1–18.
Bleck,R.,1965:Linearapproximationsfordeterminingoneandtwo-
contemporaneous U and Vanalyses.Comparisonswere dimensionalnumericalfiltersindynamicalmeteorology(inGer-
based on a set of 258 gridded 1000-hPa ECMWFanal- man). [Available from Institute for Theoretical Meteorology,
yses during 1990. These contained U and V in addition FreeUniversityofBerlin,Berlin,Germany.]
to H on the 2.5(cid:56) (cid:51) 2.5(cid:56) grid over a region bounded by Bullock, T. A., and J. R. Gyakum, 1993: Adiagnosticstudyof cy-
clogenesis in the western North Pacific.Mon. Wea. Rev., 121,
20(cid:56)–60(cid:56)S and 130(cid:56)E–130(cid:56)W. Gradient wind vorticity
65–75.
was computed as outlined abovefromH andcompared Carleton,A.M.,1979:Asynopticclimatologyofsatellite-observed
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC

612
|     |     |     |     | WEATHER | AND | FORECASTING |     |     |     |     |     | VOLUME12 |
| --- | --- | --- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | -------- |
extratropicalcycloneactivityfortheSouthernHemispherewin- tions in Arctic Winter sea ice. J. Geophys. Res., 100C, 4791–
| ter.Arch.Meteor.Geophys.Bioklimatol.B,27,265–279. |     |     |     |     |     | 4806. |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Colucci, S. J., 1976: Winter cyclone frequencies over the eastern Reed,R.J.,A.J.Simmons,M.D.Albright,andP.Unden,1988:The
United States and adjacent western Atlantic 1964–73. Bull. roleoflatentheatreleaseinexplosivecyclogenesis:Threeex-
Amer.Meteor.Soc.,57,548–553. amples based on ECMWF operational forecasts. Wea. Fore-
| Cressman, | G. P., | 1959: An | operational | objective | analysis system. | casting,3,217–229. |     |     |     |     |     |     |
| --------- | ------ | -------- | ----------- | --------- | ---------------- | ------------------ | --- | --- | --- | --- | --- | --- |
Mon.Wea.Rev.,87,367–374. Roebber,P.J.,1984:Statisticalanalysisandupdatedclimatologyof
Davies,H.C.,C.Scha¨r,andH.Wernli,1991:Thepaletteoffronts explosivecyclones.Mon.Wea.Rev.,112,1577–1589.
and cyclones within a baroclinic wave development.J. Atmos. Rogers,E.,andL.F.Bosart,1991:Adiagnosticstudyoftwointense
| Sci.,48,1666–1688. |     |     |     |     |     | oceaniccyclones.Mon.Wea.Rev.,119,965–996. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
Evans,M.S.,D.Keyser,L.F.Bosart,andG.M.Lackmann,1994: Sanders,F.,1986:Explosivecyclogenesisinthewest-centralNorth
Asatellite-derivedclassificationschemeforrapidmaritimecy- AtlanticOcean,1981–84.PartI:Compositestructureandmean
clogenesis.Mon.Wea.Rev.,122,1381–1416. behavior.Mon.Wea.Rev.,114,1781–1794.
Gyakum, J. R., Anderson, R. H. Grumm, and E. L. Gruner, 1989: ,andJ.R.Gyakum,1980:Synoptic-dynamicclimatologyofthe
‘‘bomb.’’Mon.Wea.Rev.,108,1589–1606.
NorthPacificcoldseasonsurfacecycloneactivity:1975–1983.
|     |     |     |     |     |     | Shapiro, M. | A., and | D. Keyser, | 1990: | Fronts, | jet streams, | and the |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------- | ----- | ------- | ------------ | ------- |
Mon.Wea.Rev.,117,1141–1155.
,P.J.Roebber,andT.A.Bullock,1992:Theroleofantecedent tropopause.ExtratropicalCyclones,TheErikPalme´nMemorial
surface vorticity development as a conditioning process in ex- Volume,C.W.NewtonandE.O.Holopainen,Eds.,Amer.Me-
| plosive | cyclone | intensification. | Mon. | Wea. | Rev., 120, 1465– | teor.Soc.,167–191. |         |        |               |           |     |             |
| ------- | ------- | ---------------- | ---- | ---- | ---------------- | ------------------ | ------- | ------ | ------------- | --------- | --- | ----------- |
|         |         |                  |      |      |                  | Simmonds,          | I., and | X. Wu, | 1993: Cyclone | behaviour |     | response to |
1489.
|           |         |              |       |               |             | changes | in winter | Southern | Hemisphere |     | sea ice | concentration. |
| --------- | ------- | ------------ | ----- | ------------- | ----------- | ------- | --------- | -------- | ---------- | --- | ------- | -------------- |
| Jones, D. | A., and | I. Simmonds, | 1993: | A climatology | of Southern |         |           |          |            |     |         |                |
Hemisphereextratropicalcyclones.ClimateDyn.,9,131–145. Quart.J.Roy.Meteor.Soc.,119,1121–1148.
, and , 1994: A climatology of Southern Hemisphere an- Sinclair, M. R., 1994: An objective cyclone climatology for the
SouthernHemisphere.Mon.Wea.Rev.,122,2239–2256.
ticyclones.ClimateDyn.,10,333–348.
|     |     |     |     |     |     | , 1995: | A climatology |     | of cyclogenesis | for | the SouthernHemi- |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --------------- | --- | ----------------- | --- |
Kidson,J.W.,andM.R.Sinclair,1995:Theinfluenceofpersistent
sphere.Mon.Wea.Rev.,123,1601–1619.
anomaliesonSouthernHemispherestormtracks.J.Climate,8,
|     |     |     |     |     |     | , 1996: | A climatology |     | of anticyclones |     | and blocking | for the |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | --------------- | --- | ------------ | ------- |
1938–1950.
Ko¨nig,W.,R.Sausen,andF.Sielmann,1993:Objectiveidentification SouthernHemisphere.Mon.Wea.Rev.,124,245–263.
,andX.Cong,1992:PolarairstreamcyclogenesisintheAus-
ofcyclonesinGCMsimulations.J.Climate,6,2217–2231.
|     |     |     |     |     |     | tralasian | region: | A composite | study | using | ECMWF | analyses. |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ----------- | ----- | ----- | ----- | --------- |
Lambert,S.J.,1988:AcycloneclimatologyoftheCanadianClimate
Mon.Wea.Rev.,120,1950–1972.
CentreGeneralCirculationModel.J.Climate,1,109–115.
|     |     |     |     |     |     | Streten, N. | A., and | A. J. | Troup, 1973: | A synoptic |     | climatology of |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ----- | ------------ | ---------- | --- | -------------- |
Lefevre, R. J., and J. W. Nielsen-Gammon,1995:Anobjectivecli- satelliteobservedcloudvorticesovertheSouthernHemisphere.
matologyofmobiletroughsintheNorthernHemisphere.Tellus,
Quart.J.Roy.Meteor.Soc.,99,56–72.
47A,638–655.
|              |        |           |           |         |                  | Taljaard, | J. J., 1967: | Development, |        | distribution | and        | movement of |
| ------------ | ------ | --------- | --------- | ------- | ---------------- | --------- | ------------ | ------------ | ------ | ------------ | ---------- | ----------- |
| Le Marshall, | J. F., | and G. A. | M. Kelly, | 1981: A | January and July |           |              |              |        |              |            |             |
|              |        |           |           |         |                  | cyclones  | and          | anticyclones | in the | Southern     | Hemisphere | during      |
climatologyoftheSouthernHemispherebasedondailynumer-
theIGY.J.Appl.Meteor.,6,973–987.
icalanalyses1973–77.Aust.Meteor.Mag.,29,115–123. Thorncroft, C. D., B. J. Hoskins, and M. E. McIntyre, 1993: Two
Le Treut, H., and E. Kalnay: 1990: Comparison of observed and paradigmsofbaroclinicwavelife-cyclebehavior.Quart.J.Roy.
| simulated | cyclone | frequency | distribution | as  | determined by | an  |     |     |     |     |     |     |
| --------- | ------- | --------- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Meteor.Soc.,119,17–55.
objectivemethod.Atmosfera,3,57–71.
Trenberth,K.E.,1977:Objectivenumericalanalysisofgeopotential
Manobianco, J., 1989: Explosive East Coast cyclogenesis over the heightfieldsinNewZealand.NewZealandMeteorologicalSer-
west-central North Atlantic Ocean: Acomposite study derived vice Tech. Information Circular 158, 21 pp. [Available from
fromECMWFoperationalanalyses.Mon.Wea.Rev.,117,2365– MetService,P.O.Box722,Wellington,NewZealand.]
2383.
,1991:StormtracksintheSouthernHemisphere.J.Atmos.Sci.,
| Murray, | R. J., and | I. Simmonds, | 1991a: | A numerical | scheme for |     |     |     |     |     |     |     |
| ------- | ---------- | ------------ | ------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
48,2159–2178.
trackingcyclonecentresfromdigitaldata.PartI:Development ,1992:GlobalanalysesfromECMWFandatlasof1000to10
andoperationofthescheme.Aust.Meteor.Mag.,39,155–166. mb circulation statistics. NCAR Tech. Note NCAR/TN-
, and , 1991b: A numerical scheme for tracking cyclone 373(cid:49)STR, 191 pp. [Available from NCAR, P.O. Box 3000,
| centres | from | digital data. | Part II: | Application | to January and | Boulder,CO80307.] |     |     |     |     |     |     |
| ------- | ---- | ------------- | -------- | ----------- | -------------- | ----------------- | --- | --- | --- | --- | --- | --- |
Julygeneralcirculationmodelsimulations.Aust.Meteor.Mag., Whittaker, L. M., and L. H. Horn, 1984: Northern Hemisphere ex-
39,167–180. tratropicalcycloneactivityforfourmid-seasonmonths.J.Cli-
| ,and | ,1995:Responsesofclimateandcyclonestoreduc- |     |     |     |     | matol.,4,297–310. |     |     |     |     |     |     |
| ---- | ------------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Unauthenticated | Downloaded 11/09/23 01:35 AM UTC