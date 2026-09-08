QuarterlyJournaloftheRoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061, January2017BDOI:10.1002/qj.2989
Objective classification of extratropical cyclogenesis
MichaelA.Graf,HeiniWernli andMichaelSprenger*
InstituteforAtmosphericandClimateScience,ETHZu¨rich,Switzerland
*Correspondenceto:M.Sprenger,InstituteforAtmosphericandClimateScience,ETHZu¨rich,Universita¨tstrasse16,8092Zu¨rich,
Switzerland.E-mail:michael.sprenger@env.ethz.ch
Extratropical cyclones experience vastly different genesis conditions at the first point of
theirtracks.Anovelmethodisintroducedtocharacterizethisvariabilityandclassifygenesis
eventsbycomputing30diagnosticvariablesthatdescribethesynoptic-scaleenvironment
of 16029 genesis events in the Northern Hemisphere extratropics, using ERA-Interim
reanalyses from 2000–2011. These variables are referred to as precursors and include
parameters characterizing upper-level forcing, low-level baroclinicity, thermodynamic
stability, surface fluxes and moist processes. The genesis events spread over a large
portionofthe30-dimensionalprecursorphasespaceandnoobviousclustersoccur,which
highlights the high variability of cyclogenesis processes and indicates that they form in a
continuum rather than a few distinct categories. A projection of the genesis events to the
first two principle components (PC) of the precursor phase space allows reduction of the
dimensionalityandintroductionofameaningfulsegmentationofthegenesiseventsinfive
classes. The first two PCs are characterized by upper-level forcing (e.g. the amplitude of
theupper-levelpotentialvorticity(PV)anomaly)andlow-troposphericdiabaticprocesses
(e.g.precipitationanddiabaticallyproducedlow-levelPV),respectively.Thefirstofthefive
classesidentifiedconstitutesthecentreofthePC1–PC2phasespaceandrepresentsaverage
conditions.Compositesrevealthatthefourclassesofeventscharacterizedbylargepositive
or negative scores of PC1 and PC2 occur in distinct and strongly differing flow regimes,
characterized by the strength of the upper-level forcing, the structure of the upper-level
jetandtheamplitudeoflow-levelmoistprocessesandbaroclinicity.Thefourclassesalso
haveclearlydifferinggeographicaldistributions.Manywell-knowncyclogenesiseventsfall
within classes characterized by strong low-level moist processes with or without strong
upper-level forcing. Also discussed are the robustness of the method and the linkage to
classicalconceptsofcycloneclassifications.
KeyWords: extratropicalcyclogenesis;objectiveclassification;principalcomponentanalysis;potentialvorticity
Received12July2015;Revised13December2016;Accepted19December2016;PublishedonlineinWileyOnlineLibrary
16February2017
1. Introduction meaningful categorizations of extratropical cyclones. Bjerknes
and Solberg (1922) proposed a conceptual life-cycle model
Adverse weather in the extratropics is in most cases related to for a prototype extratropical cyclone, which very successfully
the passage of an extratropical cyclone with its accompanying influenced meteorological education and set the standard for
fronts. Early weather analyses, based upon synoptic charts of drawingsurfaceweathercharts.Thismodelemphasizedthekey
sea-levelpressure(SLP),revealedthetransientandpropagating role of a pre-existing surface front for cyclogenesis. At about
nature of extratropical cyclones and motivated research on the same time, Ficker (1920) pointed out the important role of
the genesis, track and intensity of these important synoptic- upper-troposphericsignaturesandtheirsuperpositionwithnear-
scale atmospheric flow features. Very early examples of such surface flow features for cyclogenesis (see also Davies, 2010).
cyclone case studies are from Loomis (1841) and Shaw (1903). Thesetwostreamsofthinking,focusingoneitherthelower-or
Since then, many further studies have shown that extratropical upper-levelingredientsofdevelopingcyclones,evolvedfurtherin
cyclones are highly variable in terms of e.g. their lifetime parallelandconstitutetheconceptualbackboneformuchofthe
and propagation speed (e.g. Blender et al., 1997), maximum extratropicalcycloneresearchperformedduringthelastcentury
intensity (e.g. Hodges et al., 2011), size (e.g. Simmonds, 2000) (Davies,1997).Todayitisgenerallyacceptedthatthevariability
and their three-dimensional structure (e.g. Campa and Wernli, of observed cyclone life cycles is so large that they cannot be
2012). This high degree of variability calls for a reduction of described with a single conceptual model. This understanding
complexity by building either so-called conceptual models or prompts the question as to whether archetypical categories of
(cid:2)c 2016RoyalMeteorologicalSociety

1048 M.A.Grafetal.
cyclones exist and, if so, how they can be determined. Catto Otherdocumentedcasestudiesextendthepaletteofpotentially
(2016)recentlysummarizedmanydifferentattemptstocategorize importantprecursorsofcyclogenesisconsiderably.Theseinclude,
cyclonesbasedontheoreticalandconceptualmodelsontheone forinstance,intensesurfacefrontogenesisfortheexplosive‘Queen
sideandobservationaldatasets,e.g.satelliteimagery,ontheother ElisabethII’storm(Gyakum,1991),thecompactingofanupper-
side. levelPVdisturbanceforanotherrapidlyintensifyingstormover
A first approach is to focus on cyclones in specific regions, the North Atlantic (Lackmann et al., 1997), warm sea-surface
assuming that they form a distinct cyclone category due to the temperatureandweakstaticstabilityforsubtropicalcyclogenesis
geographical setting, for instance Mediterranean cyclones (e.g. (Evans and Guishard, 2009), low-level anomalies of equivalent
Trigoetal.,1999)andIcelandicLows(e.g.Serrezeetal.,1997), potentialtemperatureforcyclonesoverSouthAmerica(Mendes
ortocomparecharacteristicsofcyclonesdevelopingindifferent et al., 2007) and the presence of an intense upper-level jet
regions(e.g.HoskinsandHodges,2002;DacreandGray,2009; streakintheupstreamquadrantintheincipientstageofintense
CampaandWernli,2012).Analternativeclassificationisbased cyclones near Australia (Sinclair and Cong, 1992). For frontal
upon cyclone intensity or the degree of cyclone intensification, wave cyclones, several studies have investigated the mechanism
measured for instance by the temporal change of SLP along proposed by Bishop and Thorpe (1994), who suggested that
the cyclone track (Sanders and Gyakum, 1980; Binder et al., environmental deformation must be below a certain threshold
2016).Athirdapproach,whichismorecomprehensiveandless forfrontalwavestogrow(e.g.Renfrewetal.,1997;Rivalsetal.,
straightforward,istoclassifyextratropicalcyclonesaccordingto 1998;ChaboureauandThorpe,1999;Malletetal.,1999;Schemm
the environmental flow conditions at the time of their genesis andSprenger,2015).
and/or intensification. In their classical article, Petterssen and Thisbriefsummaryofselectedearlierstudiesclearlyindicates
Smebye (1971) investigated cyclogenesis events and postulated that we still lack a comprehensive investigation of the relative
two contrasting types of cyclone development, referred to as importance of various physical processes and precursor signals
typesAandB,respectively.WhereascyclonesoftypeAdevelop forthegenesisofextratropicalcyclonesindifferentregionsofthe
‘under a more or less straight upper current’, type B cyclones globe.Itisthereforetheobjectiveofthisstudytoperformsuch
occur when a ‘pre-existing upper trough, with strong vorticity an investigation, leading to a novel and objective classification
advection on its forward side, spreads over a low-level area of cyclogenesis events. Our method focuses on cyclogenesis,
of warm advection’. The latter type clearly emphasizes the key consideredasthestartingpointofacyclonetrack,usesacyclone-
roleoffinite-amplitudeupper-levelprecursorsforcyclogenesis, trackclimatologybaseduponreanalysisdata,computesalargeset
which, from a potential vorticity (PV) perspective, correspond ofpotentialcyclogenesisprecursorsinthevicinityofthegenesis
tointenseupper-troposphericpositiveanomalies(Kleinschmidt, events and applies objective statistical techniques to identify
1950;Hoskinsetal.,1985;CampaandWernli,2012;Bentleyet meaningfulcategoriesofcyclogenesis.Themethodologicalsteps
al.,2016).Manycasestudiesofcyclogenesishaveconfirmedthe areintroducedinthenextsection.Sections3and4thenintroduce
keyroleofthistypeofupper-levelPVprecursor(e.g.Bleckand andcharacterize thegenesiscategoriesandsection5providesa
Mattocks,1984;Tafferner,1990;MorganandNielsen-Gammon, discussionoftherobustnessoftheresults,thelinkagetoearlier
1998;Rossaetal.,2000;Lagouvardosetal.,2007;Iwabeandda categorizations and the relevance for individual cyclone case
Rocha,2009)andidealizednumericalmodelstudiesonbaroclinic studies.Themainconclusionsaresummarizedinsection6.
instabilityhaveusedthis‘typeBparadigm’totriggerbaroclinic
instability(e.g.MontgomeryandFarrell,1992;Scha¨randWernli, 2. Cyclogenesiseventsandtheirprecursors
1993;Wernlietal.,1998;Schemmetal.,2013).Incontrast,type
Acyclonesdevelopfirstatlowlevelswithoutaclearupper-level 2.1. Identificationofcyclogenesisevents
disturbance at the time of genesis. Such a set-up is typical for
so-calleddiabaticRossbywaves(e.g.Wernlietal.,2002;Moore Locations of cyclogenesis are identified in the present study
et al., 2008; Rivie´re et al., 2010; Boettcher and Wernli, 2011), as the initial points of cyclone tracks, which are identified in
butitisnotclearwhetherPetterssenandSmebye(1971)thought the Northern Hemisphere during 2000–2011 according to the
mainly of this relatively rare type of cyclone when describing methoddescribedinWernliandSchwierz(2006).Thismethod
type A. The twofold categorization of cyclone development by reliesonsea-levelpressure(SLP)fieldsfromERA-Interim(Deeet
Petterssen and Smebye (1971) has subsequently been extended al., 2011), interpolated on a regular grid with 1 ◦ horizontal
byDevesonetal.(2002)toincludeathirdcategoryofcyclones, resolution, and the three following steps: (i) SLP contours
type C, the dynamics of which is dominated by the effect of are identified at 0.5hPa intervals; (ii) local SLP minima are
intense latent heating and the resulting diabatic production of determinedontheregulargridandacceptedforfurtheranalysisif
positive PV anomalies in the lower to middle troposphere (see theyaresurroundedbyatleastoneclosedisobar;(iii)theaccepted
also Plant et al., 2003; Gray and Dacre, 2006; Dacre and Gray, SLP minima are then tracked and kept if the track duration is
2009).However,forcyclonesoftypeCalso,thegenesisprocessis atleast24h.Theinitialpoint(longitude,latitude,time)ofeach
stronglydeterminedbyanupper-levelPVanomaly(Plantetal., cyclonetrackfinallydefinesacyclogenesisevent.
2003). This threefold categorization highlights the importance In addition to this basic tracking methodology, several
of upper-level disturbances, surface baroclinicity and diabatic subtleties have to be considered. First, only cyclogenesis events
◦
processesinextratropicalcyclogenesis. intheextratropics(i.e.northof30 N)areconsidered,inorder
Thecurrentlyavailableclassificationsofextratropicalcyclones toexcludetropicalsystems.Furthermore,toavoidartificialSLP
areusefulforhighlightingthestronglydifferingdynamicsleading minima due to extrapolation in regions of high topography, all
to cyclone formation and intensification. However, they might minimaareneglectedwheretopographyishigherthan1500m.
notencompassthefulldiversityofcyclogenesiseventsobservedin Then, if the cyclone area at the genesis point, defined as the
natureand,duetotheirfocusonafewpre-selectedparameters, area within the outermost enclosing contour, is larger than
do not necessarily account for all physical processes involved. 2×105km2,thepointisneglected,becauseweassumethatsuch
For instance, detailed case studies emphasized the important eventsarecausedbyincorrectlyinterruptedcyclonetracksandan
precursory role of surface latent heat fluxes for intense oceanic alreadymature(i.e.large)cycloneishenceerroneouslycaptured
cyclones (e.g. Kuo et al., 1991; Gyakum and Danielson, 2000; asanewsystem.Finally,ifseverallocalminimaarelocatedwithin
Davolioetal.,2009).Incontrast,forcyclonesintheleeofhigh thesameenclosingcontour,onlythecyclogenesiseventwiththe
mountains,cold-airblockingandinteractionwiththeupper-level highestcorepressureiskept.
trough (e.g. Egger et al., 1995; Han et al., 1995; Horvath et al., Using this method, we identify 16934 cyclogenesis events in
2006) and adiabatic warming of surface air due to downslope the Northern Hemisphere extratropics during 2000–2011. As a
flows are of key importance (e.g. Thomas and Martin, 2007). caveat we mention that Neu et al. (2013) showed that different
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)
1477870x,
2017,
703,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989
by
Univ
of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[26/02/2025].
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

|     |     |     |     |     | ExtratropicalCyclogenesisClassification |     |     |     |     |     |     |     |     | 1049 |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
 1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
Table1.
Listofprecursorswithabbreviation(Abbrev.),associatedsignal(Signal)andstatisticalvaluesofthenormalizedclimatologicalanomalies(Std,Mean,Skew).
IncolumnSignal,the(+/−)signmeansthatinthecyclogenesisareatheaverageabove/belowthemedianiscalculated(seetextfordetails).
| Shortdescriptionofprecursor |     |     |     |     |     | Abbrev. |     | Signal |     | Std |     | Mean |     | Skew |
| --------------------------- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- | ---- | --- | ---- |
Upper-levelPV(averagedbetween600and200hPa) PVup + 0.93(5) 0.73 0.60
| Geopotentialheightat500hPa                |     |     |     |     |     | Z500   |     |     | −   | 0.90    |     | −0.63    |     | −0.03 |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------- | --- | -------- | --- | ----- |
|                                           |     |     |     |     |     |        |     |     | −   |         |     | −0.78    |     | −0.66 |
| Anomalyofgeopotentialheightat500hPa       |     |     |     |     |     | ZANOM  |     |     |     | 0.94(4) |     |          |     |       |
|                                           |     |     |     |     |     |        |     |     | −   |         |     | −1.34(2) |     | −1.21 |
| Low-levelcontributiontoQGverticalmotion   |     |     |     |     |     | qgωbot |     |     |     | 0.85    |     |          |     |       |
|                                           |     |     |     |     |     |        |     |     | −   |         |     | −1.37(1) |     | −1.24 |
| Upper-levelcontributiontoQGverticalmotion |     |     |     |     |     | qgωtop |     |     |     | 1.07(3) |     |          |     |       |
| Windspeedaveragedbetween500and100hPa      |     |     |     |     |     | VELJET |     |     | +   | 0.88    |     | 0.57     |     | 0.44  |
| Troposphericstaticstability               |     |     |     |     |     | N2     |     |     | −   | 0.72    |     | −0.82    |     | 0.11  |
TROPO
Differenceofpot.temperaturebetweensurfaceand700hPa (cid:3)θSFC700 − 0.74 −0.66 0.24
| Mixed-layerCAPE                  |     |     |     |     |     | CAPE   |     |     | +   | 1.08(2) |     | 0.45 |     | 4.42(2) |
| -------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------- | --- | ---- | --- | ------- |
| Eadygrowthrateinlowertroposphere |     |     |     |     |     | EADY   |     |     | +   | 0.83    |     | 0.94 |     | 0.36    |
| Eadygrowthrateinuppertroposphere |     |     |     |     |     | EADYup |     |     | +   | 0.78    |     | 0.64 |     | 0.51    |
Horizontaltemperaturegradientat850hPa |∇θ850 | + 0.81 1.08(5) 0.55
Horizontaltemperatureadvectionat850hPa TADV850 + 0.64 0.86 1.32(5)
−0.13
| Equivalentpotentialtemperatureat850hPa |     |     |     |     |     | θe850   |     |     | +   | 0.76 |     | 0.86 |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ---- | --- | ---- | --- | --- |
|                                        |     |     |     |     |     | |∇θe850 | |   |     |     |      |     |      |     |     |
Horizontalgradientofequivalentpot.temperatureat850hPa + 0.76 1.03 0.62
| Environmentaldeformationat850hPa |     |     |     |     |     | DEF |     |     | +   | 0.84 |     | 1.09(4) |     | 0.86 |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------- | --- | ---- |
Petterssenfrontogenesisfunctionat850hPa FGEN850 + 0.87 1.02 1.86(3)
| Anomalyofthe850hPatemperature |     |     |     |     |     | TPERT |     |     | +   | 0.81 |     | 0.88 |     | 0.13 |
| ----------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ---- | --- | ---- | --- | ---- |
Low-levelPV(averagedbetween1000and600hPa) PVlow + 0.93(5) 0.99 0.19
| Verticallyintegratedwatervapour |     |     |     |     |     | Qint |     |     | +   | 0.92 |     | 0.98 |     | 0.37 |
| ------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | ---- | --- | ---- |
Surfaceprecipitationduring6hbeforecyclogenesis RR6h + 1.53(1) 1.33(3) 1.64(4)
| Timeperiodsincemoistureuptake |     |     |     |     |     | UPTTIM |     |     | +   | 0.52 |     | 0.66 |     | −0.12 |
| ----------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- | --- | ---- | --- | ----- |
Differenceofpot.temperaturein48hback.trajectories TRAdθ48 + 0.63 0.92 0.71
|                                          |     |     |     |     |     |         |     |     | −   |      |     | −0.99 |     |      |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ---- | --- | ----- | --- | ---- |
| Pressuredifferencein48hback.trajectories |     |     |     |     |     | TRAdP48 |     |     |     | 0.46 |     |       |     | 0.95 |
Maximumchangeofpot.temperaturein48hback.trajectories TRAdθMX + 0.53 0.99 0.39
|     |     |     |     |     |     |     |     |     | −   |     |     | −1.06 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
Maximumpressuredifferencein48hback.trajectories TRAdPMX 0.55 0.43
| Sensibleheatfluxatsurface |     |     |     |     |     | SSHF |     |     | +   | 0.66 |     | 0.60 |     | −0.17    |
| ------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | ---- | --- | -------- |
| Latentheatfluxatsurface   |     |     |     |     |     | SLHF |     |     | +   | 0.58 |     | 0.62 |     | −0.23    |
| Skintemperature           |     |     |     |     |     | SKT  |     |     | +   | 0.78 |     | 0.54 |     | −4.68(1) |
Stdshowsthestandarddeviation,MeanthearithmeticmeanandSkewtheskewnessofthenormalizedclimatologicalanomalies.Forreasonsofcomparability,none
oftheprecursordistributionsislog-transformedforthecalculationofstatisticalvalues.Thetopfivehighestabsolutevaluesareindicatedwithboldlettersandthe
rankingisshowninbrackets.
trackingalgorithmsgenerallyagreewellduringtheintensification (iii) How shall the precursors be normalized for an objective
andmaturephasesofacyclone’slifecycle,butdifferencesexist classification?
during the early cyclogenesis phase. Our cyclone identification (iv) Howshouldwetreatfieldswithadipolarstructure?
andtrackingapproachtendstoidentifycycloneslaterthansome
otherschemes(which,forexample,arebasedonvorticitymaxima In response to question (i) above, an area average within
at 850hPa: Hodges, 1999), due to the requirement that closed a broad region surrounding each cyclone is used to represent
thesynoptic-scaleenvironmentassociatedwitheachcyclogenesis
SLPcontoursalreadyexistatthetimeofcyclogenesis.
event.Anexampleofthisisshownforcyclone‘Klaus’,locatedat
44 ◦ N,29 ◦ Wat0600UTCon23January2009.Figure1showsthe
2.2. Precursordefinitionandnormalization
|     |     |     |     |     |     |     | upper-level |     | PV (PV | ) within | a 20 | ◦×20 | ◦ region | surrounding |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | -------- | ---- | ---- | -------- | ----------- |
up
|     |     |     |     |     |     |     | the location |     | of cyclogenesis. |     | Only | a weak | PV  | signal occurs |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------- | --- | ---- | ------ | --- | ------------- |
up
| In order | to classify | the | 16934 | cyclogenesis | events, | a set of | 30  |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ----- | ------------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
exactlyatthegenesisposition;however,adistincttrough,i.e.a
diagnosticvariablesthatdescribethesynoptic-scaleenvironment
|             |      |         |                |     |          |             | positivePV | up     | signal,islocatedtothewest.Toaccountforthis,all |            |        |          |     |              |
| ----------- | ---- | ------- | -------------- | --- | -------- | ----------- | ---------- | ------ | ---------------------------------------------- | ---------- | ------ | -------- | --- | ------------ |
| surrounding | each | cyclone | are calculated |     | from the | ERA-Interim |            |        |                                                |            |        |          |     |              |
|             |      |         |                |     |          |             | precursor  | fields | are                                            | considered | within | a circle | of  | radius 500km |
dataset.Thesevariablesarereferredtoasprecursors;theyarelisted
|     |     |     |     |     |     |     | around | the | genesis | position | (from | now | on referred | to as the |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------- | -------- | ----- | --- | ----------- | --------- |
inTable1anddescribedingreaterdetailintheSupplementary cyclogenesisarea;seedashedcircleinFigure1).
Material.Theprecursorswereselectedafteranin-depthliterature In response to questions (ii) and (iii) above, we decided to
| review on  | case | studies   | of extratropical |           | cyclones. | The chosen      |                |            |         |                |         |            |            |            |
| ---------- | ---- | --------- | ---------------- | --------- | --------- | --------------- | -------------- | ---------- | ------- | -------------- | ------- | ---------- | ---------- | ---------- |
|            |      |           |                  |           |           |                 | use normalized |            | anomaly | fields.        | More    | precisely, | anomaly    | fields     |
| precursors | were | mentioned | in at            | least one | study     | as relevant for |                |            |         |                |         |            |            |            |
|            |      |           |                  |           |           |                 | were           | calculated | as      | the difference | between |            | the actual | fields and |
thegenesisoftheevent.Theyincludedynamicalflowfeaturesat
|     |     |     |     |     |     |     | climatology, |     | which | we calculated |     | at a given | time | t as a 30day |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ------------- | --- | ---------- | ---- | ------------ |
upperandlowerlevels(e.g.upperandlow-levelPV),parameters runningaveragefromt−15daystot+15daysinthe12years
related to baroclinicity, fronts and static stability and other considered(2000–2011).Thisanomalyfieldisthennormalized
thermodynamicparameters. by the standard deviation of the climatology (i.e. the standard
| All 30 | precursors |     | have been | calculated |     | for all 16934 |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | --------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
deviationiscalculatedfromthe12yearlyrunningmeanvalues).
| cyclogenesis | events. | With | regard | to this | technical | procedure, |     |     |     |     |     |     |     |     |
| ------------ | ------- | ---- | ------ | ------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ThisprocedureisshowninFigure1forcycloneKlaus:panel(a)
someaspectsdeserveamoredetaileddiscussion. shows the climatological distribution of PV (black contours)
up
|     |     |     |     |     |     |     | andpanel(b)thenormalizedanddimensionlessPV |     |     |     |     |     |     | anomaly. |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- |
up
(i) What is a reasonable approach to represent a two- The trough to the west of the genesis event, which is believed
dimensional field in the environment of a genesis event toplayanimportantrole,appearsasastrongpositiveanomaly
(e.g.upper-levelPV)byascalarvalue?
|     |     |     |     |     |     |     | of PV | up , with | an amplitude |     | of almost | 3 standard |     | deviations of |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ------------ | --- | --------- | ---------- | --- | ------------- |
(ii) Isitmoremeaningfultoconsideractualfieldsordeviations the interannual variability. Because we normalize with local
fromclimatology(i.e.anomalies)? standard deviations (instead of uniform spatially averaged
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

1050 M.A.Grafetal.
(a) (b)
2.25 6 8 10 980 945 9 5 0 9 5 5 9 6 9 0 6 5 9 7 0 97 98 5 0 3 4 4 5 . . 5 5
1.25
4 9 7 2
3
.5 2 3 99
9
0
85 980 5970
1
2
.5 1.75 1 2
995
1
1.5 1000 0.5
1.5 995 1005 0
1010
−0.5
1 1015
−1
1020
0.5 −1.5
0.5
0 .7
5 0.2
1025
1 −
−
2
2
.5 0
0 1030 2 5 −3
−3.5
−0.2 −4
−4.5 0.5
−0.5
Figure1.CyclogenesisofextratropicalcycloneKlausat44◦N,29◦Wat0600UTCon23January2009.Thecyclogenesisislocatedinthecentreofthedomain(marked
withablackcross);thehorizontaldomainextends2000kmineachdirection(correspondingto20◦attheEquator).(a)Upper-levelPVatcyclogenesis(inpvu)is
colour-shadedandthecorrespondingclimatologyshowninblackcontours.(b)Normalizedupper-levelPVanomalyiscolour-shaded,wherenormalizationisrelative
toa30dayrunningmean(seetextfordetails),andsea-levelpressure(inhPa)isshownasblackcontours.Inbothpanels,thebluecircledefinesthecyclogenesisarea
aroundthecyclogenesispoint.
standard deviation), this approach attributes more weight to
parametersthatexhibitparticularlystrongvariabilityneargenesis
events. Some precursors have a strongly skewed distribution:
surface precipitation during 6h before cyclogenesis (RR ),
6h
the Petterssen frontogenesis function at 850hPa (FGEN )
850
and mixed-layer CAPE (CAPE); they are log-transformed after
the normalization to obtain a more symmetric normal-like
distribution.
Figure 1(b) illustrates the challenge associated with question
(iv)above.Thetrough–ridgepatterninthegenesisregionleads
to a dipolar structure with strongly positive values to the west
andnegativevaluestotheeast.However,consideringthetypeB
paradigm (see introduction) we are interested in the amplitude
of the upper-level positive PV anomaly and therefore not in a
simple spatial average of the normalized PV anomaly field in
the cyclogenesis area. We therefore decided to average only the
positiveornegativeanomalyvaluesinthegenesisareaforeach
parameter. More precisely, the method applied in this study
is first to consider the precursor values at all grid points in
the cyclogenesis area and to determine their median value. For
eachfield,theaverageoverallgridpointseitherabove(med+)
or below (med−) the median is chosen as the final precursor
signal. To decide which of the two options is more reasonable, Figure2.Distribution of PVup(med−) (blue) and PVup(med+) (red) for all
we considered the statistics of the (med+) and (med−) values. c d y is c t l r o i g b e u n ti e o s n is s. e T v h en e t s s i . gn T a h l e PV bl u u p e (m ( e r d ed − ) ) d is a c sh al e c d ula li t n e e d s a s s h t o h w em th ea e n m of ea a n llP o V f u t p h v e al t u w e o s
As an example, Figure 2 shows the distribution and mean of inthecyclogenesisareabelowthemedianandcorrespondinglyforPVup(med+)
PV up (med+) (red) and PV up (med−) (blue) for all cyclogenesis (seetextfordetails).Theblackdashedlinemarksthepositionofzeroanomaly.
events. The former distribution deviates more strongly from
zero and therefore PV (med+) is chosen as the parameter
up the precursors is handled reasonably well by the classification
representing the PV precursor. In Table 1, the choice of the
up
(med+)valuesismarkedwitha+symbol.Forsomeparameters approachdescribedinsection3.
(seeTable1),(med−)isthemoreappropriatechoice,e.g.forthe
geopotential height at 500hPa (Z ), which makes sense given 2.3. Statisticaldistributionofprecursors
500
theexpectedanti-correlationofPV andZ .
up 500
At least 20 grid points of each precursor field have to be Here,somerelevantcharacteristicsoftheprecursordistributions
computable within the cyclogenesis area, otherwise the whole areconsidered:(i)thegeneralformofthedistribution,e.g.their
cyclogenesis event is removed from the list. Non-computable skewness; (ii) the spread of the distribution; and (iii) the shift
grid points can occur, for instance, if the calculation of quasi- oftheprecursorsignalfromitsclimatologicalmean.Remember
geostrophic(QG)forcingforverticalmotiondoesnotconverge thatwenormalizedtheprecursorswithrespecttoaclimatological
numerically,oriftheconsideredfield,e.g.temperatureat850hPa, distributionandthereforeitisinterestingtodeterminewhether
is missing because of topography. Due to these reasons, 905 genesiseventsshowsubstantialdeviationsfromthisclimatology.
eventscouldnotbeconsideredfortheclassification,resultingin Anobjectiveclassificationschemewillfavouranyprecursorthat
aprecursordatasetfor16029cyclogenesisevents. exhibits a considerable spread over all cyclogenesis events. In
Finally, note that the precursors do not all describe well- this sense, these basic statistics of the precursor distributions
separated physical processes: some parameters correlate or can already point to their potential relevance in the objective
be attributed to similar forcing mechanisms. This aspect of classification.
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)
1477870x,
2017,
703, Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989
by
Univ
of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[26/02/2025].
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

|     |     |     |     | ExtratropicalCyclogenesisClassification |     |     |     |     |     |     |     |     |     | 1051 |
| --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
 1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     |      | (a)        |      |     |     | (b)            |     | qgω |     |     |     |     |     |
| --- | --- | ---- | ---------- | ---- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |            | EADY |     |     |                |     |     | top |     |     |     |     |
|     |     | 1600 |            |      |     |     | 1600           |     |     |     |     |     |     |     |
|     |     |      | min: −1.47 |      |     |     | min: −8.81     |     |     |     |     |     |     |     |
|     |     | 1400 |            |      |     |     | 1400           |     |     |     |     |     |     |     |
|     |     |      | mean: 0.94 |      |     |     | mean: −1.37    |     |     |     |     |     |     |     |
|     |     | 1200 | max: 5.21  |      |     |     | 1200 max: 2.17 |     |     |     |     |     |     |     |
|     |     | 1000 | std: 0.83  |      |     |     | std: 1.07      |     |     |     |     |     |     |     |
1000
|     |     | 800 |     |     |     |     | 800 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 600 |     |     |     |     | 600 |     |     |     |     |     |     |     |
|     |     | 400 |     |     |     |     | 400 |     |     |     |     |     |     |     |
|     |     | 200 |     |     |     |     | 200 |     |     |     |     |     |     |     |
0
0
|     |     | −6  | −4 −2 | 0   | 2   | 4 6 | −6  | −4 −2 |     | 0 2 | 4   | 6   |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Figure3.Statistical distribution of the normalized anomalies for a selection of precursors: (a) Eady growth rate, defined as EADY(med+); (b) upper-level
contributiontoQGverticalmotion,definedasqgωtop(med−).Additionally,ineachpanelthefollowingvaluesaregiven:minimum,maximum,meanandstandard
deviation.
Most precursors show a unimodal normal-like statistical (qgω and qgω , respectively), the horizontal temperature
|     |     |     |     |     |     |     | top |     | bot |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distribution (two examples are shown in Figure 3). The Eady gradient at 850hPa (|∇θ |), the environmental deformation
850
growthrateinthelowertroposphere(EADY)hasarathersmall at 850hPa (DEF) and RR ; (ii) CAPE and skin temperature
6h
skewnessof0.36(Table1),whichreflectsthenormal-likeshape (SKT) exhibit a particularly strong skewness, followed by
|     |     |     |     |     |     |     | intermediate | skewness |     | for T | ,   | FGEN | and | RR ; and |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ----- | --- | ---- | --- | -------- |
ofthedistributionwithaslightlylongertailforpositivevalues. ADV850 850 6h
The mean of EADY is positive (0.94), which indicates that (iii) the largest spread is found for RR 6h , CAPE, qgω top ,
genesis typically occurs where and when the Eady growth rate the anomaly of geopotential height at 500hPa (Z ANOM ) and
| isanomalouslystrong,asphysicallyexpected.However,itmust |     |     |     |     |     |     | PV . |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
up
bekeptinmindthatourmethodtodefinetheprecursorsignal
| introduces | a slight | bias, | because it is defined |     | as EADY(med+) |     |     |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | --------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3. Thebiplotanddefinitionofcyclogenesisclasses
(seesection2.2).Finally,thestandarddeviation(0.83)indicates
that,quantitatively,thissignalcandifferstronglyfromeventto The aim of this section is twofold. First, the first two principal
event and that some genesis events occur where and when this components (PC) of the 30-dimensional precursor phase space
parameterisbelowclimatology. are used to define five distinct classes objectively. Secondly,
| As a | second | example, | Figure 3(b) | shows | the upper-level |     |            |                |     |     |        |         |            |        |
| ---- | ------ | -------- | ----------- | ----- | --------------- | --- | ---------- | -------------- | --- | --- | ------ | ------- | ---------- | ------ |
|      |        |          |             |       |                 |     | a physical | interpretation |     | is  | sought | for the | projection | of the |
contribution to QG vertical motion (qgω top ), with pronounced precursorsonthesetwoPCs.
negativeskewness(−1.24),ameannegativevalue(−1.37)anda
significantstandarddeviation(1.07).Again,themainlynegative 3.1. Principalcomponentanalysis(PCA)
valuesofthisprecursorareinfluencedbyourchoicetoconsider
the(med−)values(seeTable1).Whatcanbelearnedfromthe
APCAisperformed(Pearson,1901;Hotelling,1933),basedona
distributionisthat,inalmostallcases,aregionwithforcingfor singularvaluedecomposition.Eachgenesiseventisrepresentedas
upwardmotionisfoundinthecyclogenesisareaandthisupward apointina30-dimensionalphasespace,wherethe30dimensions
forcing can be strong, with values reaching six climatological correspond to the (normalized) precursors. Accordingly, the
standard deviations. As for EADY, the considerable spread of 16029genesiseventsconstituteapointcloudinthisphasespace.
qgω (standarddeviationof1.07)indicatesthatthisparameter
| top |     |     |     |     |     |     | ThePCAredefinesthecoordinateaxesinsuchawaythatmost |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
mightbeofimportanceforthelaterclassification.
|     |     |     |     |     |     |     | of the variance |     | of the | point cloud | is  | found | along the | first PCA |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ----------- | --- | ----- | --------- | --------- |
Table1alsoliststhestatisticalmeasuresforallotherprecursors. axis (PC1). The second PCA axis (PC2) is then chosen such
It is worth highlighting the following general aspect. If a that it maximizes variance in the subspace orthogonal to PC1,
precursor has a very small standard deviation, this implies that and so on for the other 28 PCA axes. These redefined PCA
the (normalized) precursor signal is very similar for all genesis axes can be expressed as linear combinations of the original
| events. This | is  | the case, | e.g., for the surface | heat | fluxes | (SSHF |             |       |        |     |        |                |     |             |
| ------------ | --- | --------- | --------------------- | ---- | ------ | ----- | ----------- | ----- | ------ | --- | ------ | -------------- | --- | ----------- |
|              |     |           |                       |      |        |       | precursors, | which | allows | the | PCs to | be interpreted |     | in terms of |
and SLHF) and the change of potential temperature along 48h the original precursors. Formally, the projection of a genesis
backward trajectories (TRAdθ 48 ; three-dimensional kinematic point onto the ith PC, the so-called score si, can be written
| trajectories | have    | been calculated | with             | the tool | introduced  | by  | asfollows: |     |     |     |     |     |     |     |
| ------------ | ------- | --------------- | ---------------- | -------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Wernli and   | Davies, | 1997).          | These precursors | can      | be relevant | for |            |     |     |     |     |     |     |     |
cyclogenesis; however, the objective classification introduced in (cid:2)Np
section 3.1 by design focuses on precursors that are relevant si = λi ·Y . (1)
|     |     |     |     |     |     |     |     |     |     |     | j   | j   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for the variability of genesis events. It is also insightful to j=1
| compare | the mean | and standard | deviation | values. | If the | mean |     |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --------- | ------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
isclearlylargerthanthestandarddeviation,theprecursorsignal Here, N p denotes the dimension of the precursor space (30)
nearly always has the same sign. As an example, the horizontal and Y is a vector containing the N p precursor values for one
temperatureadvectionat850hPa(T )hasameanof0.86 genesis event. λi is the so-called loading of the jth precursor in
|     |     |     | ADV850 |     |     |     |     |     | j   |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and a standard deviation of 0.64, i.e. genesis goes along with thedirectionoftheithPC.AnadvantageofsuchaPCAapproach
enhancedtemperatureadvectioncomparedwithclimatologyin isthatitenablesreductionofthediscussiontoonlythefirstfew
(almost) all cases. On the other hand, PV can be higher or PCs,inparticulariftheyexplainalargefractionofthevariance
up
| lower than | the | corresponding | climatological | value, | because | the | inthedataset. |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | -------------- | ------ | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
standard deviation is larger (0.93) than the mean (0.73). Some In this study, we consider the projection of all cyclogenesis
further interesting conclusions from Table 1 are as follows: (i) s1 s2
|     |     |     |     |     |     |     | events on | to the | first | two PCA | axes, | i.e. | (PC1) and | (PC2), |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | ------- | ----- | ---- | --------- | ------ |
particularly strong deviations from the mean are found for the which corresponds to a reduction of the 30-dimensional initial
upper-level and low-level contributions to QG vertical motion precursorspacetoasimplertwo-dimensionalspace.Ofcourse,
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

1052 M.A.Grafetal.  1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     | 10  |     |     |     |     |     |     |   5 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.75
4.5
8
|     |     |     | B   |     |     |                   | B     |     |      |     |
| --- | --- | --- | --- | --- | --- | ----------------- | ----- | --- | ---- | --- |
|     |     |     |     |     |     | PV                |       |     | 4.25 |     |
|     |     |     | dry |     |     | up                | moist |     |      |     |
|     |     |     |     |     |     | Z                 |       |     | 4    |     |
500
6
3.75
|     |     |     |     |     |     | Z               |     |         | 3.5 |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --- | --- |
|     |     |     |     |     |     | ANOM            | qgω |         |     |     |
top
|     |     | 4   |     |     | Δθ  |     |     |     | 3.25 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
SFC700
3
2.75
qgω
|     |     | 2CP 2 |     |     |                                            |     | bot |     |     |     |
| --- | --- | ----- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
|     |     |       |     |     | 5                    12                    |     |     |     | 2.5 |     |
13
|     |     |     |     |     |                       | 1 1                                                            |                          |     | 2.25 |     |
| --- | --- | --- | --- | --- | --------------------- | -------------------------------------------------------------- | ------------------------ | --- | ---- | --- |
|     |     |     |     |     |                       | 2                 1                                            | RR 6h                    |     |      |     |
|     |     | 0   |     |     | M                     |                                                                |                          |     |      |     |
|     |     |     |     |     |                       | DEF                                                            |                          |     | 2    |     |
|     |     |     |     |     |                       | 9   1  0           E       A     D       Y                     |                          |     |      |     |
|     |     |     |     |     | 3                     |                                                                |                          |     | 1.75 |     |
6                     8
|     |     | −2  |     |     |              | T  8  5 0     P     V                      |                     |     | 1.5  |     |
| --- | --- | --- | --- | --- | ------------ | ------------------------------------------ | ------------------- | --- | ---- | --- |
|     |     |     |     |     | 4            |              7               A    D   V    | l o w               |     |      |     |
|     |     |     |     |     |              | |∇θ                                        | |                   |     |      |     |
|     |     |     |     |     |              |                                            | 850                 |     | 1.25 |     |
|     |     |     |     |     |              | |∇θ                                        | |                   |     |      |     |
e850
1
|     |     | −4  |     |     |     | θ                    |     |     |      |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---- | --- |
|     |     |     |     |     |     | e850                 |     |     | 0.75 |     |
|     |     |     | A   |     |     | T PERT               | A   |     |      |     |
0.5
|     |     |     | dry |     |     | Qint               m   |     | oist |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | ---- | --- | --- |
−6
0.25

|     |     |     | −6  | −4 −2 | 0   | 2 4 | 6   | 8 10 |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | ---- | --- | --- |
PC1
Figure4.The density of cyclogenesis events (multiplied by 100) in the principal component space is colour-shaded. Each grey dot corresponds to an outlier
cyclogenesisevent,withthePC1andPC2scoresascoordinates.Theredlinesrepresentthecoefficients(loadings)oftheprecursors,allowingthenewPC1andPC2
axestobeinterpretedintermsoftheoriginalprecursors(seetext).Ifthecoefficientspointtowardspositive(negative)anomalies,theyhaveared(blue)dotattheend.
ThemostimportantprecursorsarelabelledwithabbreviationsdefinedinTable1.Theothersarelabelledwithnumbers:1=TRAdPMX,2=TRAdP48,3=UPTTIM,
4=SKT,5=N 2 ,6=SLHF,7=SSHF,8=EADYup,9=VELJET10=FGEN850,11=TRAdθMX,12=TRAdθ48,13=CAPE.
T ROPO
the reduced data set only captures part of the variability of all 3.2. Physicalinterpretationofthebiplot
| genesis events. | Here, | PC1 and | PC2 explain | 22.3% | and 18.9% |     |     |     |     |     |
| --------------- | ----- | ------- | ----------- | ----- | --------- | --- | --- | --- | --- | --- |
ofthetotalvariance,respectively.PC3andPC4aresignificantly Wenowconsidertheredprecursorvectorsinthebiplot(Figure
| less important, | with an | explained | variance | of 10.2% | and 8.5%, |                  |            |          |            |             |
| --------------- | ------- | --------- | -------- | -------- | --------- | ---------------- | ---------- | -------- | ---------- | ----------- |
|                 |         |           |          |          |           | 4). Long vectors | contribute | strongly | to PC1 and | PC2 and the |
respectively. Because of this gap in explained variance between relationship between two precursors is given by the scalar
the first two and the other PCs, it is meaningful to consider productoftheirvectors.Orthogonalvectorsareessentiallylinearly
only the first two. This reduction to two dimensions facilitates independent and (anti-)parallel vectors are strongly (anti-)
the classification and further characterization of the classes correlated.Notethatalltheseinferencesdependontheexplained
considerably. varianceofthefirsttwoPCs.Thehigheritis,themoreaccurate
Figure 4 is the key plot of our PCA. The horizontal axes thegiveninterpretationoftheprecursorvectors(Gabriel,1971,
| correspond | to PC1 and | PC2, | respectively, | the | colour shading | 1972). |     |     |     |     |
| ---------- | ---------- | ---- | ------------- | --- | -------------- | ------ | --- | --- | --- | --- |
describesthedensityofcyclogenesiseventsinPC1andPC2space ImportantprecursorsinthedirectionofPC1areRR ,PV ,
6h low
and the grey dots represent outlier genesis events (according |∇θ |,DEF,thehorizontalgradientoftheequivalentpotential
850
|     |     |     |     |     |     | temperatureat850hPa(|∇θ |     |     | |)andEADY.Theyareallrelated |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --------------------------- | --- |
to their PC1 and PC2 scores). Each precursor is shown by a e850
radial vector (in red). Its direction indicates the direction of toeitherlatentheatreleaseorlow-levelbaroclinicity,indicating
maximum correlation with the first two PCs and the squared that high values of PC1 are strongly associated with latent heat
length of the vectors represents approximately the variance of release along an intense low-level baroclinic zone. Important
thecorrespondingprecursor.Thisvisualizationisreferredtoas precursorsinthedirectionofPC2arePV ,Z andZ ,i.e.
|     |     |     |     |     |     |     |     |     | up 500 | ANOM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- |
abiplot(Gabriel,1971;Jolliffe,2002)andinterpretedinthenext precursorsdirectlyrelatedtothestrengthofcyclonicupper-level
paragraph. First, however, we note that no obvious clusters are flowanomalies.Thisfairlycleardistinctionbetweenlow-leveland
discernible in the density plot of genesis events, which would upper-levelprecursorsisapromisingresultofouranalysisandnot
havebeenfacilitatingthedefinitionofclasses.Therefore,itisto somethingthatcouldbeexpectedapriori.Hence,thevariability
beacceptedthattheclasseswewilldefinearenotcharacterized betweencyclogenesiseventsisdeterminedmoststronglybythe
by well-defined borders. Physically, this indicates that nature varyingstrengthoflow-levelbaroclinicityandlatentheatingon
provides a rather continuous spectrum of cyclogenesis events. the one hand and upper-level disturbances on the other hand.
ThebluelinesinFigure4denotethefiveclasses.Wedecidedto Interestingly, the vectors for QG forcing for ascent, qgω and
top
selectfirsta‘middleclass’M,whichcontainsthe20%(n = 3206 qgω , are rather long and point in a direction between the
bot
in absolute numbers) of all events that are closest to the cloud axes PC1 and PC2, i.e. they are about equally correlated with
mean. The other four classes correspond to the four quadrants parametersofbaroclinicityandupper-leveldisturbances(which
=
outsideclassM.TheyarereferredtoasclassesA (n 3509), theoreticallywouldbeexpected).Also,thefactthatqgω aligns
|     |     |     |     | dry |     |     |     |     |     | top |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A (n = 3244),B (n = 3160)andB (n = 2910).As more with PC2 and qgω with PC1 agrees well with the fact
| moist |     | dry |     | moist |     |     |     | bot |     |     |
| ----- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
willbediscussedbelow,theAandBclassessharesimilaritieswith that PC1 is more strongly determined by low-level and PC2 by
theclassicalcategorizationbyPetterssenandSmebye(1971)and upper-levelprecursors.
the moist and dry classes are characterized by strong and weak Another remarkable result is that PV up and PV low are nearly
moistprocesses,respectively. orthogonaltoeachother,whichmeansthattheyareessentially
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

ExtratropicalCyclogenesisClassification 1053
(a)
all
0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2 2.2 2.4 2.6 2.8 3 3.2 3.4 3.6 3.8 4
90
M (b) 85
80
75
70
65
60
55
50
45
40
35
300 100 200 300 400 500 600 700 800
90
A 85
dry 80
75
70
65
60
55
50
45
40
35
300 100 200 300 400 500 600 700 800
90
B 85
dry 80 75
70
65
60
55
50
45
40
35
300 100 200 300 400 500 600 700 800
90
A 85
moist 80
75
70
65
60
55
50
45
40
35
300 100 200 300 400 500 600 700 800
90
B 85
moist 80
75
70
65
60
55
50
45
40
35
300 100 200 300 400 500 600 700 800
0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1
Figure5.(a)Densitymapofcyclogenesiseventsduring2000–2011(valuesincolourscorrespondtothenumberofcycloneswithinacircleof500kmradius).(b)
Fractionofcyclogenesisdensityinthedifferentclasses(incolours).Thesumoverallclassesisone.Thehistogramsontherightshowthenumberofcyclogenesiscases
indifferentlatitudebins.
statistically uncorrelated and can be regarded as independent (Figure 5). Preferred locations of cyclogenesis are found, e.g.
elements of cyclogenesis. Of course, other precursor pairs are downstream of the Rocky Mountains and Greenland, between
stronglycorrelated:e.g.,asexpected,Z ,Z andPV .As the Alps and the northern part of the Mediterranean and in
500 ANOM up
afinalexample,considertheprecursorofthetroposphericstatic the North Atlantic and North Pacific storm track regions, in
stability(N2 ;label5inFigure4):Itisphysicallyplausiblethat particulartheirwesternparts. TROPO
itisalmostparalleltotheotherstabilityprecursorthatrepresents Class M does not show particularly preferred regions of
thedifferenceofpotentialtemperaturebetweenthesurfaceand cyclogenesis compared with the overall climatology. This
700hPa ((cid:3) SFC700 ), because both precursors are related to static is expected, because M cyclones are non-extreme in all
stability, even if (cid:3) SFC700 only considers the lower troposphere. characteristics, by definition. In contrast, the frequency of class
TheybothpointinthedirectionofPV up ,indicatingthatastrong A dry cyclogenesis is considerably reduced in the oceanic basins,
upper-levelPVanomalygoesalongwithasubstantialreduction reflecting that latent heat release is not an important precursor
ofstaticstabilitybeneath(notethatPV up hasa‘+’signal,whereas inthisclass.A dry cyclonesaremorefrequentovermountainous bothstabilitymeasureshavea‘−’signal;seeTable1).
terrain,e.g.overtheRockyMountains,GreenlandandinCentral
Asia,indicatingthatmanyclassA eventslikelyrepresentcases
dry
3.3. Geographicaldistribution ofleecyclogenesis.InclassB ,cyclogenesisoccursfurthernorth
dry
compared with A . This shift becomes particularly apparent
dry
In this subsection, we consider the geographical density of all over the continents. B cyclones are relatively frequent in dry
cyclogenesiseventsandtheirdistributionamongthefiveclasses some oceanic regions, e.g. south of Alaska, near the southern
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)
1477870x,
2017,
703,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989
by
Univ
of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[26/02/2025].
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
by the
applicable
Creative
Commons
License

1054 M.A.Grafetal.  1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     | (a) |     |     |     |     |     | (b) |     |     |     |      |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     |     |     |     | 3   |     |     |     |     | 0.9  |     |     |
|     |     | M   |     |     |     |     |     | M   |     |     |     | 0.85 |     |     |
2.75
0.8
2.5
0.75
2.25
0.7
|     |     |     |     |     |     |     | 2   |     |     |     |     | 0.65 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
1.75
0.6
|     |     |     |     |     |     |     | 1.5  |     |     |     |     | 0.55 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- |
|     |     |     |     |     |     |     | 1.25 |     |     |     |     | 0.5  |     |     |
0.45
1
0.4
0.75
0.35
0.5
0.3
|     |     | σ =   0 . 9 1        |     |     |     |     |      | σ                      |     |     |     |        |     |     |
| --- | --- | -------------------- | --- | --- | --- | --- | ---- | ---------------------- | --- | --- | --- | ------ | --- | --- |
|     |     | 1                    |     |     |     |     | 0.25 | 1 =   0 . 3 2          |     |     |     | 0 . 25 |     |     |
|     |     | σ =   3 . 6 4 × 10–2 |     |     |     |     |      | σ =   2 . 8 1  × 10–10 |     |     |     |        |     |     |
|     |     | 2                    |     |     |     |     | 0    | 2                      |     |     |     |        |     |     |
0 . 2
|     |     | (c) |     |     |     |     |     | (d) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
32
1.5
30
|     |     | M   |     |     |     |     |     | M   |     | 15  |     | 1.4 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
28
1.3
26
1.2
24
|     |     |     |     |     |     |     |     |     |     |     | 20  | 1.1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
22
1
20
0.9
18
0.8
16
|     |     |     |     |     |     |     | 14  |     |     |     |     | 0.7 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | 12  |     |     |     |     | 0.6 |     |     |
|     |     |     |     |     |     |     | 10  |     |     |     |     | 0.5 |     |     |
|     |     |     |     |     |     |     | 8   |     |     |     |     | 0.4 |     |     |
|     |     |     |     |     |     |     | 6   |     |     |     |     | 0.3 |     |     |
25
|     |     |                |     |     |     |     | 4   |                      |     |     |     | 0 . 2 |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ----- | --- | --- |
|     |     | σ =   1 1 .6 6 |     |     |     |     |     | σ =   0 .4 7  × 10–5 |     |     |     |       |     |     |
|     |     | 1              |     |     |     |     | 2   | 1                    |     |     |     | 0 . 1 |     |     |
|     |     | σ =   2 .4 5   |     |     |     |     |     | σ =   1 7 .2 4       |     |     |     |       |     |     |
|     |     | 2              |     |     |     |     | 0   | 2                    |     |     | 20  |       |     |     |
0
Figure6.Compositesofthemiddleclass.Theblackcrossmarksthepositionofthecyclogenesispointandthebluedashedringdefinesthecyclogenesisarea.(a)
Upper-levelPV(PVup,inpvu)iscolour-shadedandtheblackcontoursrepresentupper-levelinducedQGverticalmotion(qgωtop)instepsof10−2Pas−1.Blue
andblacklinesindicateascendinganddescendingmotion,respectively.(b)Low-levelPV(PVlow,inpvu)iscolour-shadedandPetterssen’sfrontogenesisfunction
(FGEN850)isrepresentedasbluesolidlinesinstepsof0.5×10−10Km−1s−1,beginningwith1×10−10Km−1s−1.Thethinblacklineshowssea-levelpressurein
2hPasteps.(c)Verticalintegratedwatervapour(Qint,inmm)iscolour-shadedandtheblackcontoursrepresentthesix-hourlytotalsurfaceprecipitation(RR6h)in
stepsof1mm.(d)Eadygrowthrate(EADY)iscolour-shadedin10−5s−1andtheblackcontoursshowthehorizontalwindspeedaveragedoverrange100–500hPa
(VELJET)inms−1.σ1/σ2arethestandarddeviationsofthecolour-shaded/contourvaluesatexactlythecyclogenesislocation.
tip of Greenland and in the eastern Mediterranean. For class precursor fields not discussed in this section can be found in
| A , the | North | Atlantic | and North | Pacific | storm | tracks | stand | FileS1. |     |     |     |     |     |     |
| ------- | ----- | -------- | --------- | ------- | ----- | ------ | ----- | ------- | --- | --- | --- | --- | --- | --- |
moist
| out. In orographic                     |       | regions,             | e.g. | in the | Mediterranean |              | or over |                                      |     |     |     |     |     |     |
| -------------------------------------- | ----- | -------------------- | ---- | ------ | ------------- | ------------ | ------- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| theRockymountains,thefrequencyofclassA |       |                      |      |        |               | cyclogenesis |         |                                      |     |     |     |     |     |     |
|                                        |       |                      |      |        |               | moist        |         | 4.1. Characteristicsofthemiddleclass |     |     |     |     |     |     |
| is reduced.                            | Class | A moist cyclogenesis |      | is     | more          | prevalent    | in the  |                                      |     |     |     |     |     |     |
western North Atlantic than e.g. class B dry cyclones and is Bydefinition,classM ischaracterizedbylowabsolutevaluesof
frequentovertheeasternUSandaroundtheYellowSea.Finally, bothPC1andPC2,whichimpliesnotparticularlystrongorweak
| class B | cyclogenesis | occurs | considerably |     | more | often | in the |     |     |     |     |     |     |     |
| ------- | ------------ | ------ | ------------ | --- | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
moist values of upper-level forcing, low-level diabatic processes and
| southeastern   | parts | of the North   | Atlantic |       | and North | Pacific      | and |                |             |           |           |              |            |       |
| -------------- | ----- | -------------- | -------- | ----- | --------- | ------------ | --- | -------------- | ----------- | --------- | --------- | ------------ | ---------- | ----- |
|                |       |                |          |       |           |              |     | baroclinicity. | In this     | sense, we | consider  | these events | as average |       |
| in the western |       | Mediterranean. | In       | these | regions,  | anticyclonic |     |                |             |           |           |              |            |       |
|                |       |                |          |       |           |              |     | cyclogenesis   | situations. | Eight     | precursor | composites   | are        | shown |
Rossby-wavebreakingandtheformationofupper-levelPVcut- in Figure 6. In all composites, the cyclogenesis event is located
offs is frequent (e.g. Wernli and Sprenger, 2007), which is in in the centre (marked with a cross) and the domain extends
agreementwiththestronglypositiveupper-levelPVanomaliesin about 2000km in the four horizontal directions. Note that the
thiscategory. composites do not show the normalized precursor fields (as in
|     |     |     |     |     |     |     |     | Figure 1(b)), | but rather | the | full fields | (as in Figure | 1(a)), | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ----------- | ------------- | ------ | --- |
4. Characterizationofclasses facilitatephysicalinterpretation.
|     |     |     |     |     |     |     |     | Figure6(a)showsPV |     | withavalueofabout1.5pvunearthe |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------------------ | --- | --- | --- | --- |
up
Intheprevioussection,fiveclassesofcyclogenesisweredefinedin locationofcyclogenesis.Inadditiontothebackgroundmeridional
termsofthefirsttwoprincipalcomponentsofthe30-dimensional gradientofPV (reflectingtheincreaseoftheCoriolisparameter
up
precursor phase space. A first physical interpretation of the towardsthepole),adistinctpositiveupper-levelPVanomaly(or
different classes was given by means of the biplot (see Figure PVtrough)isdiscernibleupstream(totheleft)ofthecyclogenesis
4).Inparticular,itwasshownthattheclassesclearlydifferwith event.Downstream,aPVridgeprevails,leadingtoasignificant
respecttotheamplitudeoftheupper-levelprecursors,aswellas zonalPVgradientnearthelocationofcyclogenesis.Notethatthe
low-level moist processes and baroclinicity. In this section, the PVtroughisessentiallynorth-southoriented.Thisupper-levelPV
classcharacteristicsareanalyzedfurtherwithcompositesofthe structureinducesmid-troposphericandlow-levelverticallifting,
spatialstructureoftheprecursorfields.Westartwithageneral as confirmed by the pattern of qgω (Figure 6(a)). On the
top
characterizationofthemainprecursorsfieldsforthemiddleclass upstreamsideofthePVtrough,thereisQGforcingfordescent,
and then proceed with a comparison of the main precursors whileonitsdownstreamsidethereisstrongforcingforvertical
for the four edge classes. The composites of the less important liftingwithamaximumexactlyoverthecyclogenesislocation.
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

|     |     |     |     |     | ExtratropicalCyclogenesisClassification |     |     |     |     |     |     |     |     |     | 1055 |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
 1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     |                  |     |     |     |     | 3    |       |              |     |     |     | 3    |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | ---- | ----- | ------------ | --- | --- | --- | ---- | --- | --- |
|     |     | B                |     |     |     |     |      | B     |              |     |     |     |      |     |     |
|     |     |                  |     |     |     |     | 2.75 |       |              |     |     |     | 2.75 |     |     |
|     |     | dry              |     |     |     |     |      | moist |              |     |     |     |      |     |     |
|     |     |                  |     |     |     |     | 2.5  |       |              |     |     |     | 2.5  |     |     |
|     |     |                  |     |     |     |     | 2.25 |       |              |     |     |     | 2.25 |     |     |
|     |     |                  |     |     |     |     | 2    |       |              |     |     |     | 2    |     |     |
|     |     |                  |     |     |     |     | 1.75 |       |              |     |     |     | 1.75 |     |     |
|     |     |                  |     |     |     |     | 1.5  |       |              |     |     |     | 1.5  |     |     |
|     |     |                  |     |     |     |     | 1.25 |       |              |     |     |     | 1.25 |     |     |
|     |     |                  |     |     |     |     | 1    |       |              |     |     |     | 1    |     |     |
|     |     |                  |     |     |     |     | 0.75 |       |              |     |     |     | 0.75 |     |     |
|     |     | σ                |     |     |     |     | 0.5  | σ     |              |     |     |     | 0.5  |     |     |
|     |     | = 1.04           |     |     |     |     |      |       | = 1.07       |     |     |     |      |     |     |
|     |     | σ 1 = 4.16× 10−2 |     |     |     |     | 0.25 | σ 1   | = 7.28× 10−2 |     |     |     | 0.25 |     |     |
|     |     | 2                |     |     |     |     |      | 2     |              |     |     |     |      |     |     |
|     |     |                  |     |     |     |     | 0    |       |              |     |     |     | 0    |     |     |
|     |     |                  |     |     |     |     | 3    |       |              |     |     |     | 3    |     |     |
|     |     | A                |     |     |     |     |      | A     |              |     |     |     |      |     |     |
|     |     | dry              |     |     |     |     | 2.75 | moist |              |     |     |     | 2.75 |     |     |
|     |     |                  |     |     |     |     | 2.5  |       |              |     |     |     | 2.5  |     |     |
|     |     |                  |     |     |     |     | 2.25 |       |              |     |     |     | 2.25 |     |     |
|     |     |                  |     |     |     |     | 2    |       |              |     |     |     | 2    |     |     |
|     |     |                  |     |     |     |     | 1.75 |       |              |     |     |     | 1.75 |     |     |
|     |     |                  |     |     |     |     | 1.5  |       |              |     |     |     | 1.5  |     |     |
|     |     |                  |     |     |     |     | 1.25 |       |              |     |     |     | 1.25 |     |     |
|     |     |                  |     |     |     |     | 1    |       |              |     |     |     | 1    |     |     |
|     |     |                  |     |     |     |     | 0.75 |       |              |     |     |     | 0.75 |     |     |
|     |     | σ                |     |     |     |     | 0.5  | σ     |              |     |     |     | 0.5  |     |     |
|     |     | = 0.68           |     |     |     |     |      |       | = 0.84       |     |     |     |      |     |     |
|     |     | 1 = 1.94× 10−2   |     |     |     |     | 0.25 | 1     | = 4.17× 10−2 |     |     |     | 0.25 |     |     |
|     |     | σ                |     |     |     |     |      | σ     |              |     |     |     |      |     |     |
|     |     | 2                |     |     |     |     |      | 2     |              |     |     |     |      |     |     |
|     |     |                  |     |     |     |     | 0    |       |              |     |     |     | 0    |     |     |
Figure7.PVup(incolour)andqgωtop(contours)asinFigure6(a),butfortheedgeclassesAdry,Amoist,BdryandBmoist.
The low-level precursors PV and FGEN are shown 4.2. Characteristicsofedgeclasses
|                 |                |           |              | low        |            | 850        |              |       |              |             |                                     |        |         |           |          |
| --------------- | -------------- | --------- | ------------ | ---------- | ---------- | ---------- | ------------ | ----- | ------------ | ----------- | ----------------------------------- | ------ | ------- | --------- | -------- |
| in Figure       | 6(b).          | Again,    | a meridional |            | background |            | PV gradient  |       |              |             |                                     |        |         |           |          |
| is discernible, |                | of course | now          | exhibiting |            | typical    | tropospheric |       |              |             |                                     |        |         |           |          |
|                 |                |           |              |            |            |            |              | We    | now consider | composite   |                                     | fields | for the | four edge | classes: |
| PV values       | (≈0.4–0.7pvu). |           | The          | PV         | gradient   | is zonally | rather       |       |              |             |                                     |        |         |           |          |
|                 |                |           |              |            |            |            |              | A dry | ,B dry ,A    | moist ,andB | moist .Compositesofthemostimportant |        |         |           |          |
unperturbed, except for the region very close to cyclogenesis, precursors will be shown for each of these four classes, inter-
where PV attains values that are twice as large as in the compared,aswellascomparedtoclassM.Thearrangementof
surrounding.WeinterpretthisdistinctPVsignalasdiabatically panelsinFigures7–10issuchthatitcorrespondstothequadrants
| produced,     | associated |     | with latent |     | heat release | due     | to cloud |        |        |             |           |         |     |                |      |
| ------------- | ---------- | --- | ----------- | --- | ------------ | ------- | -------- | ------ | ------ | ----------- | --------- | ------- | --- | -------------- | ---- |
|               |            |     |             |     |              |         |          | of the | biplot | (Figure 4). | A concise | summary |     | for each class | will |
| condensation. | FGEN       |     | attains     | a   | distinct     | maximum | slightly |        |        |             |           |         |     |                |      |
850 be provided in the conclusions. Note again that the precursor
| northeast | of cyclogenesis, |     | in  | the region | where | a warm | front | is  |     |     |     |     |     |     |     |
| --------- | ---------------- | --- | --- | ---------- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
compositesnotdiscussedinthissectioncanbefoundinFileS1.
likelytoform.Notethatitisnotclearwhetherthisfrontogenesis
| is a prerequisite |     | of cyclogenesis |     | or  | rather | an  | effect of the |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------- | --- | --- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
4.2.1. Upper-levelPVandQGforcingforascent
| cyclonic | circulation | acting | on  | the background |     | baroclinicity. |     | In  |     |     |     |     |     |     |     |
| -------- | ----------- | ------ | --- | -------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesameregion,low-levelwarmairadvection(notshown)isalso
|     |     |     |     |     |     |     |     | Figure7showscompositesofPV |     |     |     | andgqω |     | foralledgeclasses |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ------ | --- | ----------------- | --- |
enhanced.Again,thiscandirectlyimpactthecyclonebutalsobe up top
(seeFigure6(a)forclassM).OnlyaweakPVsignalisdiscernible
signalofthecycloniccirculationitself.
|           |      |            |     |            |     |              |      | forclassA | dry | ,wherecyclogenesisislocatedtotheeastofaweak |     |     |     |     |     |
| --------- | ---- | ---------- | --- | ---------- | --- | ------------ | ---- | --------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
| In Figure | 6(c) | vertically |     | integrated |     | water vapour | Qint |           |     |                                             |     |     |     |     |     |
PVtroughorevenwithinaweakPVridge.ThisPVstructuregoes
| and surface | precipitation |      | in       | the 6h | before | cyclogenesis | RR       | 6h    |               |                       |       |           |        |                   |     |
| ----------- | ------------- | ---- | -------- | ------ | ------ | ------------ | -------- | ----- | ------------- | --------------------- | ----- | --------- | ------ | ----------------- | --- |
|             |               |      |          |        |        |              |          | along | with          | nearly no upper-level |       | forcing   | for    | lifting. Compared |     |
| are shown.  | Also          | Qint | features | a      | clear  | meridional   | gradient |       |               |                       |       |           |        |                   |     |
|             |               |      |          |        |        |              |          | with  | the composite | of                    | class | M (Figure | 6(a)), | the upper-level   |     |
correspondingtothebackgroundtemperaturedecreasetowards
|     |     |     |     |     |     |     |     | disturbanceinclassA |     |     | ismuchweaker.Ofcourse,theseresults |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
thepole.InterestingforcyclogenesisisthedistortionoftheQint dry
contours near the center: A tongue of enhanced Qint extends are in full agreement with the biplot (Figure 4), because the
|     |     |     |     |     |     |     |     | vectorsforPV |     | andqgω | arepointingawayfromthequadrant |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------------------------------ | --- | --- | --- | --- |
from the south over the cyclogenesis region and the highest up top
|                                                         |       |        |      |                  |     |     |               | ofclassA |       | .            |         |     |          |          |         |
| ------------------------------------------------------- | ----- | ------ | ---- | ---------------- | --- | --- | ------------- | -------- | ----- | ------------ | ------- | --- | -------- | -------- | ------- |
| values are                                              | found | to the | east | of cyclogenesis. |     | For | RR 6h a local |          | dry   |              |         |     |          |          |         |
|                                                         |       |        |      |                  |     |     |               | The      | class | B is located | beneath | a   | distinct | cyclonic | anomaly |
| maximumoccursnearthecyclogenesislocation,whichcoincides |       |        |      |                  |     |     |               |          |       | dry          |         |     |          |          |         |
wellwiththeenhancedlow-levelPV(Figure6(b)).Thissuggests ofPV up ,whichstronglyresemblesaPVcut-off.Itsmaximumis
thediabaticoriginofthelow-levelPVmaximumshownviaPV . foundslightlytothewestofthecyclogenesisanditisembedded
low
Finally,Figure6(d)depictstheEadygrowthrateinthelower inaratherbroadPVtrough.ThisstrongPV signalisinperfect
up
|             |         |     |         |     |          |        |          | agreement | with | the biplot | in  | Figure | 4, where | the PV | vector |
| ----------- | ------- | --- | ------- | --- | -------- | ------ | -------- | --------- | ---- | ---------- | --- | ------ | -------- | ------ | ------ |
| troposphere | (EADY). |     | An area | of  | enhanced | values | is found |           |      |            |     |        |          | up     |        |
pointsintotheBhalf-plane.Thisisalsothecasefortheqgω
immediatelynorthofthecyclogenesislocation.Thisimpliesthat top
onaveragecyclogenesisdoesnotoccurwhereEADY hasalocal signal, which is fairly moderate, although a dipole in vertical
maximum but further south. Additionally, VELJET reveals an forcingisassociatedwiththePVmaximum.Cyclogenesisinclass
upper-leveljetstreak(>30ms −1)southwestofthecyclogenesis B coincides fairly well with the maximum forcing for ascent.
dry
|     |     |     |     |     |     |     |     | Figure | 4 shows | that N2 |     | is relatively | small | (not | shown), |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------- | --- | ------------- | ----- | ---- | ------- |
location.Accordingly,cyclogenesisinthemiddleclasstakesplace TROPO
intheleftexitregionofthisjetstreak,i.e.,inaregionthatiswell whichcanbeexpectedbeneathastrongpositiveupper-levelPV
| knownasfavorableforcyclogenesis. |     |     |     |     |     |     |     | anomaly. |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

1056 M.A.Grafetal.  1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|                    | 0.9                | 0.9   |
| ------------------ | ------------------ | ----- |
|                    |                    |       |
| B                  | B                  |       |
| dry                | 0.85 moist         | 0.85  |
|                    | 0.8                | 0.8   |
|                    | 0.75               | 0.75  |
|                    | 0.7                | 0.7   |
|                    | 0.65               | 0.65  |
|                    | 0.6                | 0.6   |
|                    | 0.55               | 0.55  |
|                    | 0.5                | 0.5   |
|                    | 0.45               | 0.45  |
|                    | 0.4                | 0.4   |
|                    | 0.35               | 0.35  |
| σ                  | 0.3 σ              | 0.3   |
| = 0.34             | = 0.30             |       |
| σ 1 = 2.03 × 10−10 | σ 1 = 3.86 × 10−10 |       |
|                    | 0.25               | 0.25  |
| 2                  | 2                  |       |
|                    | 0.2                | 0.2   |
|                    |   0.9              |   0.9 |
| A                  | 0.85 A             | 0.85  |
dry moist
|                   | 0.8                   | 0.8  |
| ----------------- | --------------------- | ---- |
|                   | 0.75                  | 0.75 |
|                   | 0.7                   | 0.7  |
|                   | 0.65                  | 0.65 |
|                   | 0.6                   | 0.6  |
|                   | 0.55                  | 0.55 |
|                   | 0.5                   | 0.5  |
|                   | 0.45                  | 0.45 |
|                   | 0.4                   | 0.4  |
|                   | 0.35                  | 0.35 |
| σ = 0.37          | 0.3 σ = 0.35          | 0.3  |
| 1                 | 1                     |      |
| σ = 2.42 × 10−10  | 0.25 σ = 4.72 × 10−10 | 0.25 |
| 2                 | 0.2 2                 | 0.2  |
|                   |                       |      |
Figure8.PVlow(incolour),FGEN850(solidbluecontour)andsea-levelpressure(thinsolidlines)asinFigure6(b),butfortheedgeclassesAdry,Amoist,Bdryand
Bmoist.
|     | 32   | 32  |
| --- | ---- | --- |
|     |      |     |
| B   | 30 B | 30  |
dry moist
|          | 28        | 28  |
| -------- | --------- | --- |
|          | 26        | 26  |
|          | 24        | 24  |
|          | 22        | 22  |
|          | 20        | 20  |
|          | 18        | 18  |
|          | 16        | 16  |
|          | 14        | 14  |
|          | 12        | 12  |
|          | 10        | 10  |
|          | 8         | 8   |
|          | 6         | 6   |
| σ = 8.34 | σ = 10.51 |     |
| 1        | 4 1       | 4   |
| σ        | σ         |     |
| = 1.20   | 2 = 3.38  | 2   |
2 2
|     | 0    | 0   |
| --- | ---- | --- |
|     | 32   | 32  |
|     |      |     |
| A   | 30 A | 30  |
dry moist
|           | 28        | 28  |
| --------- | --------- | --- |
|           | 26        | 26  |
|           | 24        | 24  |
|           | 22        | 22  |
|           | 20        | 20  |
|           | 18        | 18  |
|           | 16        | 16  |
|           | 14        | 14  |
|           | 12        | 12  |
|           | 10        | 10  |
|           | 8         | 8   |
|           | 6         | 6   |
| σ = 11.16 | σ = 12.14 |     |
|           | 4         | 4   |
1 1
| σ = 1.39 | 2 σ = 4.06 | 2   |
| -------- | ---------- | --- |
2 2
|     | 0   | 0   |
| --- | --- | --- |
Figure9.Qint(incolour)andRR6h(contours)asininFigure6(c),butfortheedgeclassesAdry,Amoist,BdryandBmoist.
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

|     |     |     | ExtratropicalCyclogenesisClassification |     |     |     |     |     |     |     |     |     |     | 1057 |
| --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
 1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     |     |     |     |   1.5 |     |       |     |     |     |     |   1.5 |     |     |
| --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- | --- | --- | ----- | --- | --- |
|     | B   |     |     |     |       | B   |       |     |     |     |     |       |     |     |
|     |     | dry |     |     | 1.4   |     | moist |     |     |     |     | 1.4   |     |     |
|     |     |     |     |     | 1.3   |     |       |     |     |     |     | 1.3   |     |     |
5
|     |     |     |     |     | 1.2 |     |     |     | 1   |     |     | 1.2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 5
|     |     |     |     |     | 1.1 |     |     |     |     | 20  |     | 1.1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 1   |     |     |     |     |     |     | 1   |     |     |
20
|     |     |     |     |     | 0.9 |     |     |     |     |     |     | 0.9 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 0.8 |     | 25  |     |     |     |     | 0.8 |     |     |
25
|     |            |                 |     |     | 0.7   |      |               |     |     |     |     | 0.7   |     |     |
| --- | ---------- | --------------- | --- | --- | ----- | ---- | ------------- | --- | --- | --- | --- | ----- | --- | --- |
|     |            |                 |     |     | 0.6   |      |               |     |     |     |     | 0.6   |     |     |
|     |            |                 |     |     | 0.5   |      |               |     |     |     |     | 0.5   |     |     |
|     |            |                 |     |     | 0.4   |      |               | 35  |     |     |     | 0.4   |     |     |
|     |            |                 |     |     | 0.3   | 25   |               | 30  |     |     |     | 0.3   |     |     |
|     | σ          | = 0.44 × 10−530 |     |     | 0.2   | σ    | = 0.50 × 10−5 |     |     |     |     | 0.2   |     |     |
|     | 1          |                 |     | 25  |       | 1    |               |     |     |     |     |       |     |     |
|     | 2σ5= 14.75 |                 |     |     | 0.1   | σ    |               |     |     |     |     | 0.1   |     |     |
|     |            |                 |     |     |       |      | = 16.11       |     |     |     | 20  |       |     |     |
|     | 2          |                 |     |     |       | 2 02 |               |     |     |     |     |       |     |     |
|     |            |                 |     |     | 0     |      |               |     |     |     |     | 0     |     |     |
|     |            |                 | 15  |     |   1.5 |      |               |     |     |     |     |   1.5 |     |     |
|     | A          |                 |     |     |       | A    |               |     | 15  |     |     |       |     |     |
|     |            |                 |     |     | 1.4   |      |               |     |     |     |     | 1.4   |     |     |
|     |            | dry             |     |     |       |      | moist         |     |     |     |     |       |     |     |
|     |            |                 |     |     | 1.3   |      |               |     |     | 20  |     | 1.3   |     |     |
|     |            |                 |     |     | 1.2   |      |               |     |     |     |     | 1.2   |     |     |
20
|     |     |     |     |     | 1.1 |     |     |     |     |     |     | 1.1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 1   |     |     |     |     |     |     | 1   |     |     |
|     |     |     |     |     | 0.9 |     |     | 25  |     |     |     | 0.9 |     |     |
|     |     |     |     |     | 0.8 |     |     |     |     |     |     | 0.8 |     |     |
|     |     |     |     |     | 0.7 |     | 30  |     |     |     |     | 0.7 |     |     |
|     |     |     |     |     | 0.6 |     |     |     |     |     |     | 0.6 |     |     |
3 0
|     |     |     |     |     | 0.5 |     |     |     |     |     |     | 0.5 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|     |     |               |     |     | 0.4   |     |                |     |     |     | 0   | 0.4   |     |     |
| --- | --- | ------------- | --- | --- | ----- | --- | -------------- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |               |     | 0   | 0 . 3 |     |                |     |     |     |     | 0 . 3 |     |     |
|     |     |               |     | 2   |       | σ2  | 5              |     |     |     |     |       |     |     |
|     | σ   | = 0.43 × 10−5 |     |     | 0 . 2 |     | =  0.50 × 10−5 |     |     |     |     | 0 . 2 |     |     |
|     | 1   |               |     |     |       | 1   |                |     |     |     |     |       |     |     |
|     | σ   |               |     |     |       | σ   |                |     |     |     |     |       |     |     |
|     |     | = 16.02       |     |     | 0.1   |     | = 18.36        |     |     |     |     | 0.1   |     |     |
|     | 2   |               |     |     |       | 2   |                |     |     |     |     |       |     |     |
|     |     |               |     |     | 0     |     |                |     |     |     |     | 0     |     |     |
Figure10.EADY(incolour)andVELJET(contours)asininFigure6(d),butfortheedgeclassesAdry,Amoist,BdryandBmoist.
ThestrongestPV up signalisfoundforclassB moist .Cyclogenesis cyclogenesis.Asecond,althoughweaker,maximumofFGEN 850
developsonthedownstreamsideofapronounced,rathernarrow islocatedtothesouthwest.Theoverallpatternisreminiscentof
PV trough, exhibiting strong PV gradients at cyclogenesis. The awarmandcoldfront,respectively,suggestingthatcyclogenesis
strongPVsignalisassociatedwithacorrespondinglystrongsignal occursnearalocalminimumofagenerallystronglyfrontogenetic
in qgω . Indeed, the maximum amplitude of this field, nearly region.TheSLPpatternshowsadipolewithasurfaceanticyclone
top
perfectly located at cyclogenesis, is several times larger than for totheeastofthegenesislocation.Thispointstothepotentialrole
alltheotherclasses.Asforallclasses,theascendingbranchofthe ofwarm-airadvection,inlinewiththebiplotinFigure4,where
qgω dipoleisconsiderablystrongerthanthedescendingbranch T points to the quadrant of A . For class B , the
| top |     |     |     |     |     | ADV850 |     |     |     |     | moist |     | moist |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ----- | --- | ----- | --- |
on the upstream side of the narrow PV trough. From Figure 4, low-levelfieldsareverysimilar.However,herethePV signal
low
weexpectthisclasstohavesimilartroposphericstabilitiesasclass almostcoincideswiththePV anomaly(Figure7),leadingtoa
up
B .
dry particularlystrongverticalcouplingofthetwoPVanomalies.The
Finally, we discuss class A moist , where cyclogenesis is again SLPcompositeofB moist hasthestrongestcycloneandaweaker
locateddownstreamofapositivePV up anomaly.AsforA dry ,the downstreamanticyclonethaninA .
moist
tiltbetweenthesurfacecycloneandthePV signalisfairlylarge. From Figure 8, it is evident that PV differs significantly
|     |     |     | up  |     |     |     |     |     |     |     |     | low |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A pronounced ridge prevails east of the cyclogenesis location. between the dry and moist classes, due to the differing degrees
Withrespecttoqgω ,thisclassisassociatedwithweakerforcing of latent heat release in clouds. This is confirmed by the fields
top
| forascentthanclassB |     | ,butmuchstrongerthanforA |     |     | .   |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
moist dry showninFigure9.Asexpected,Qint showsastrongsouthward
|     |     |     |     |     |     | gradientforallclasses.A |     |     | dry | showsaweakpositivedisturbanceof |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- |
4.2.2. Low-levelandmoistprocesses QintatthecyclogenesislocationandalmostzerovaluesofRR .
6h
|     |     |     |     |     |     | ClassB | isverysimilartoclassA |       |        |          | intermsofQintandRR |             |          | ,   |
| --- | --- | --- | --- | --- | --- | ------ | --------------------- | ----- | ------ | -------- | ------------------ | ----------- | -------- | --- |
|     |     |     |     |     |     |        | dry                   |       |        |          | dry                |             |          | 6h  |
|     |     |     |     |     |     | with   | generally             | lower | values | of Qint, | due                | to the more | poleward |     |
Figure8showslowtroposphericstructures(seeFigure6(b)for
classM).ForclassA dry ,onlyaveryweakpositivePV low anomaly cyclogenesispositions(Figure5).Theslightlystrongersignalof
is superimposed on a background meridional PV gradient. RR 6h isconsistentwithastrongerQGforcingforascentinB dry
Similarly,FGEN alsoexhibitsaweaksignalnortheastofA thaninA (Figure7).
|     | 850 |     |     |     | dry |     | dry |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cyclogenesis.Bothsignalsindicateonlyweaklow-levelprocesses From Figure 4, we expect similar values of RR for classes
6h
forthesegenesisevents,whichisinlinewithFigure4.ClassB is A and B , but differences in Qint, because the Qint
|     |     |     |     |     | dry | moist  |        | moist |       |       |     |           |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ------ | ----- | ----- | ----- | --- | --------- | --- | --- |
|     |     |     |     |     |     | vector | points | into  | the A | class | and | away from | the | B   |
verysimilartoA dry ,withveryweaksignalsofPV low andFGEN 850 . moist moist
TheonlynoteworthydifferencesareanenhancedbackgroundPV class.Indeed,thecompositesinFigure9revealstronglypositive
gradientforB andthepresenceofseveralclosedSLPcontours anomalies of Qint and RR 6h at cyclogenesis. For class B moist ,
dry
inthecomposite. cyclogenesisoccursatthenortherntipofthehigh-Qint tongue
For class A , the situation changes significantly. A rather (similartothetwodrycategories).Adistinctdifferenceofthetwo
moist
strong and small-scale cyclonic PV anomaly is present very moistclassesistheorientationoftheQint tongueandtheclear
low
|     |     |     |     |     |     | local | maximum | of  | Qint to | the southeast |     | of A | cyclogenesis. |     |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --- | ------- | ------------- | --- | ---- | ------------- | --- |
close to the cyclogenesis location, indicating that diabatic moist
processesplayanimportantrole.Furthermore,thisclassshows Furthermore,theabsolutevaluesofQ int arehigherforA moist than
| thehighestvaluesofFGEN |     | ,withamaximumslightlynorthof |     |     |     | forB | .     |     |     |     |     |     |     |     |
| ---------------------- | --- | ---------------------------- | --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
|                        |     | 850                          |     |     |     |      | moist |     |     |     |     |     |     |     |
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

1058 M.A.Grafetal.  1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|     |     |     |     |     |     |     |     | PV low ,RR | 6h andQint,wereused.Figure11revealsaverysimilar |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
6 B PV         B patterntotheoriginalbiplot;however,withthevectorsrotated
|     |     |     |     |     | up  |     |     | ◦   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dry moist by 20 clockwise. This rotation might occur because, in this
lower-dimensionalphasespace,PC1andPC2areassociatedwith
4
|     |     |     |     |     |     | qgω |     | asimilarexplainedvariance.Inordertocomparetheclassesof |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
top
|     |     |     |     |     |     |     |     | the full dataset | with | the | reduced | one, the | class borders |     | are also |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --- | ------- | -------- | ------------- | --- | -------- |
2
rotated.Withthisrotation,70%oftheeventsareclassifiedinthe
samewayaswiththefullsetofprecursors.Ascanbenoticedin
0
Figure11,thehighestdensityofdifferentlyclassifiedeventsoccurs
2CP close to the class borders. This indicates that the characteristics
−2 RR 6h         of the first two principal components and of the classification
|     |     |     |     |     |     |     |     | are fairly | robust, | i.e. they | can essentially |     | be reproduced |     | even |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --------- | --------------- | --- | ------------- | --- | ---- |
−4 PV low        with a strongly reduced set of precursors. In other words, this
briefsensitivitystudyindicatesthatconsideringmanyprecursors,
wheresomeofthemeventuallyturnouttobeoflowimportance,
−6
|     | A   |     |     | QINT           | A     |     |     | doesnotimpedeameaningfulclassification.            |      |            |             |     |        |             |     |
| --- | --- | --- | --- | -------------- | ----- | --- | --- | -------------------------------------------------- | ---- | ---------- | ----------- | --- | ------ | ----------- | --- |
|     | dry |     |     |                | moist |     |     |                                                    |      |            |             |     |        |             |     |
|     |     |     |     |                |       |     |     | We also                                            | note | that, with | the reduced |     | set of | precursors, | the |
| −8  |     |     |     |                |       |     |     | explainedvarianceofPC1andPC2amountsto73.8%,whichis |      |            |             |     |        |             |     |
considerablyhigherthatintheoriginalclassificationwith41.2%.
| −10 |     |     |     |     |     |     |     | Thiscanbeexplainedbythelowerdimensionalityofthephase |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | −5  |     | 0   |     | 5   |     | 10  |                                                      |     |     |     |     |     |     |     |
space,suchthatmorevariancemustberepresentedbythefirst
PC1
twoPCs.
Figure11.Biplotwithreducednumberofprecursors.Theredlinesrepresentthe
coefficientsoftheprecursors.Iftheypointtowardspositive(negative)anomalies, 5.2. Comparisonwithpreviousclassifications
theyhaveared(blue)dotattheend.Theyarelabelledwiththeabbreviations
listedinTable1.Thecrossesdeterminethescoresandtheircoloursrepresentthe
First,thequestionarisesastohowthisclassificationcompareswith
originalclassification(yellow=Bdry,blue=Bmoist,green=Adry,red=Amoist,
theschemebyPetterssenandSmebye(1971).Itisimportantto
grey=M).Thebluesolidlinesdefinetheclassbordersoftheclassificationwitha
reducednumberofprecursors.
notethattheirclassificationalsoconsidersthetemporalevolution
ofcyclones,incontrasttoourapproach,whichfocusesonflow
structuresatthetimeofgenesisonly.SincePetterssenandSmebye
4.2.3. Measuresofbaroclinicity
(1971)donotreferexplicitlytomoistdynamicalprocesses,their
|     |     |     |     |     |     |     |     | classification | focuses | more | on our | PC2. | Instead | of two | distinct |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ---- | ------ | ---- | ------- | ------ | -------- |
Finally,Figure10showstwomeasuresofbaroclinicity:theEady categories, we find a rather gradual transition from cyclones
| growth | rate EADY | and | upper-level | jet | velocity | VELJET. | Class |     |     |     |     |     |     |     |     |
| ------ | --------- | --- | ----------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thatdevelopwithaweakupper-leveltrough(similartotypeA)
A exhibitsmoderatevaluesofEADY,withaweakbutdistinct
| dry                                          |     |     |     |        |      |           |     | tothosethatdevelopdownstreamofapronouncedupper-level |     |          |              |     |           |      |        |
| -------------------------------------------- | --- | --- | --- | ------ | ---- | --------- | --- | ---------------------------------------------------- | --- | -------- | ------------ | --- | --------- | ---- | ------ |
| maximumnorthofthecyclogenesislocation.VELJET |     |     |     |        |      | hasfairly |     |                                                      |     |          |              |     |           |      |        |
|                                              |     |     |     |        |      |           |     | trough (similar                                      | to  | type B). | Cyclogenesis |     | with very | weak | upper- |
|                                              |     |     |     | (∼20ms | −1). |           |     |                                                      |     |          |              |     |           |      |        |
uniform and moderate values The absence of a level forcing (type A) is very rare and occurs in extreme cases
well-defined jet streak is consistent with the weak values of of class A associated with strongly negative values of PC2
moist
qgω (Figure7).B exhibitsthelowestvaluesofEADY ofall (e.g., cyclone ‘Kyrill’; see below). In agreement with Petterssen
| top |     | dry |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classes. VELJET, however, shows a strong meridional gradient andSmebye(1971),fortheseevents,baroclinicity(e.g.EADY)is
| andadistinctmaximumof30ms |     |     |     | −1 relativelyfarsouthofB |     |     |     |                                                            |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                           |     |     |     |                          |     |     | dry | particularlystrong.Moreover,cyclogenesiswithnegativevalues |     |     |     |     |     |     |     |
cyclogenesis.
|                                                |     |     |     |     |     |       |       | of PC1 occurs | in                   | an area | where | the upper-level |               | QG forcing | is       |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ----- | ----- | ------------- | -------------------- | ------- | ----- | --------------- | ------------- | ---------- | -------- |
| Thesituationclearlychangesforthemoistclasses.A |     |     |     |     |     |       | shows |               |                      |         |       |                 |               |            |          |
|                                                |     |     |     |     |     | moist |       | weak. The     | later classification |         | by    | Deveson         | et al. (2002) |            | included |
the highest values of EADY just northwest of the cyclogenesis a third type, C, for which moist processes are also essential.
location. The region of enhanced values of EADY is elongated Type C cyclones also have a pronounced upper-level forcing
fromsouthwesttonortheast.Inthesameregion,highvaluesof and therefore are likely similar to our events in class B . In
moist
| VELJET | occur.ThereforecyclogenesisinclassA |     |     |     |     | takesplace |     |                                                        |     |     |     |     |     |     |     |
| ------ | ----------------------------------- | --- | --- | --- | --- | ---------- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|        |                                     |     |     |     |     | moist      |     | summary,theexistingABCcategorizationisnotunlikethemore |     |     |     |     |     |     |     |
justbeneaththejetstreakcentre.ValuesofEADYareabitweaker
|       |           |         |     |               |     |                |     | extreme | cases in | our classes | A moist | (type | A), B dry | (type | B) and |
| ----- | --------- | ------- | --- | ------------- | --- | -------------- | --- | ------- | -------- | ----------- | ------- | ----- | --------- | ----- | ------ |
| for B | , but the | maximum | is  | again located | to  | the northwest. |     |         |          |             |         |       |           |       |        |
moist B (type C). However, a very important result of this study
moist
As before, the VELJET signal is interesting, mainly because of isthat,ifconsideringahigh-dimensionalprecursorphasespace,
−1)
the very high values (>35ms southwest of cyclogenesis, cyclogenesis events form a continuum and not a set of distinct
indicatingthatcyclogenesisoccursintheleftexitofajetstreak. types. This continuum has such a large spread that the four
Thisisinlinewiththeverystrongupper-levelforcingfoundfor
|     |     |     |     |     |     |     |     | outer classes | nevertheless |     | have strongly |     | differing | and physically |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --- | ------------- | --- | --------- | -------------- | --- |
thisclass(Figure7).
distinguishablecharacteristics.
5. Discussion 5.3. Classificationofselectedcyclogenesisevents
| In this | section, | we discuss | several | aspects | of our | method | and |           |       |         |         |        |         |              |     |
| ------- | -------- | ---------- | ------- | ------- | ------ | ------ | --- | --------- | ----- | ------- | ------- | ------ | ------- | ------------ | --- |
|         |          |            |         |         |        |        |     | Figure 12 | shows | the PC1 | and PC2 | scores | of some | subjectively |     |
results.First,thequestionisaddressedastotherobustnessofthe selected and generally well-known cyclone events. They are
classificationwithrespecttothenumberofprecursors.Thenthe listed in Table 2 and, where available, references are given to
identifiedclassesofcyclogenesisarecomparedqualitativelywith studies describing these events. Most of these genesis events
theclassificationschemebyPetterssenandSmebye(1971),before
|     |     |     |     |     |     |     |     | are associated | with | enhanced | values | of  | PC1, i.e. | intense | low- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | -------- | ------ | --- | --------- | ------- | ---- |
wediscussthegenesisclassificationforaselectionofwell-known
|     |     |     |     |     |     |     |     | level moist | processes. | Exceptions |     | are the | cases ‘Dry’ | (B  | dry ) and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---------- | --- | ------- | ----------- | --- | --------- |
cyclones.
|     |     |     |     |     |     |     |     | ‘Algeria’ | (A ), with | negative | values | of  | PC1. | The conditions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | -------- | ------ | --- | ---- | -------------- | --- |
dry
duringcyclogenesis,investigatedinthisstudy,cannotbedirectly
5.1. Reproducibilityofclassificationwithfewprecursors attributedtothefuturecycloneevolution;adetailedinvestigation
|     |     |     |     |     |     |     |     | of the linkage | between |     | genesis conditions |     | and | the subsequent |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --- | ------------------ | --- | --- | -------------- | --- |
Thesensitivityoftheclassificationhasbeentestedwithastrongly life-cycle would be an interesting route for future research.
reduced set of precursors. To this end, only very important The complexity of this linkage is illustrated by the selected
precursors(accordingtothebiplotinFigure4),i.e.qgω ,PV , events: ‘Algeria’, a cyclone associated with heavy precipitation
|     |     |     |     |     |     | top | up  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

|     |     |     |     |     | ExtratropicalCyclogenesisClassification |     |     |     |     |     |     |     |     | 1059 |
| --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
 1477870x, 2017, 703, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989 by Univ of Sao Paulo - Brazil, Wiley Online Library on [26/02/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
10 representupper-levelforcingsandlower-leveldiabaticprocesses,
|     |     |     |     |     |     |       | respectively. |              | Moist   | processes            | (including | diabatically  |                     | produced   |
| --- | --- | --- | --- | --- | --- | ----- | ------------- | ------------ | ------- | -------------------- | ---------- | ------------- | ------------------- | ---------- |
|     |     |     |     |     |     |       | low-level     |              | PV) and | upper-level          |            | PV are        | almost uncorrelated |            |
| 8   | B   |     |     |     |     | B     |               |              |         |                      |            |               |                     |            |
|     |     |     |     |     |     |       | and           | characterize |         | the first            | two        | principle     | components          | of the     |
|     | dry |     |     |     |     | moist |               |              |         |                      |            |               |                     |            |
|     |     |     |     |     |     |       | precursor     |              | phase   | space. Baroclinicity |            | is correlated |                     | with moist |
6
|     |     |     |     |     |     |     | processes, |     | but less | variable. | The | QG upper-level |     | forcing for |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --------- | --- | -------------- | --- | ----------- |
WCB ascent correlates equally with upper-level PV and baroclinicity,
4
|     |     |     |     |     |     |     | which | agrees | nicely | with | the theoretical |     | understanding | that |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ------ | ---- | --------------- | --- | ------------- | ---- |
Dry
Rolf baroclinicity and flow changes along isentropes determine the
Snow
2CP 2 amplitudeoftheQGforcingforascent.Itisinterestingthatour
objectiveapproachidentifiesupper-levelPVandmoistprocesses
M
0 as the most variable precursors of extratropical cyclogenesis,
Brig
UK Oct K la u s corroboratingresultsfrommanycasestudiesandclimatological
|     |     | Algeria |     |     | Presi de n t |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−2 Eric a  I OP4 analyses, which highlighted the key role of these dry and moist
|     |     |     |     | D R W  | M a rtin  |     |             |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | Lothar | Xynt hi a |     | parameters. |     |     |     |     |     |     |     |
Wedividedthephasespaceintofiveequallypopulatedclasses
−4
Kyrill and termed the outer classes as A dry /A moist and B dry /B moist . The
|     | A   |     |     |     |     | A   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dry moist AB terminology is a reference to the classical Petterssen and
−6
Smebye(1971)classification,withcomparativelyweak(A)versus
−6 −4 −2 0 2 4 6 8 10 strong(B)upper-levelflowanomaliesnearcyclogenesis.Dryand
moistindicatethatsomegenesiseventsoccurinfairlydryregions
PC1
withweak/noprecipitationanddiabaticlow-levelPVproduction
Figure12.BiplotwithselectedcyclogenesiscaseslistedinTable2(reddots).The
|     |     |     |     |     |     |     | and | others | occur | in a | region | where | vertically | integrated |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---- | ------ | ----- | ---------- | ---------- |
greydotsrepresentthescoresofallcyclogenesisevents.Thebluesolidlinesdefine
|     |     |     |     |     |     |     | moisture |     | has a local | maximum |     | and latent | heating | associated |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | ------- | --- | ---------- | ------- | ---------- |
theclassbordersoftheclassification(asinFigure4).
|                                               |          |         |      |          |            |          | with           | intense | precipitation  |            | leads | to a pronounced | cyclonic            | PV  |
| --------------------------------------------- | -------- | ------- | ---- | -------- | ---------- | -------- | -------------- | ------- | -------------- | ---------- | ----- | --------------- | ------------------- | --- |
|                                               |          |         |      |          |            |          | anomaly        |         | at low levels. | Composites |       | of the          | genesis environment |     |
| andfloodingintheareaofAlgiers,appearsinclassA |          |         |      |          |            | ,whereas |                |         |                |            |       |                 |                     |     |
|                                               |          |         |      |          |            | dry      | for            | the     | five classes   | shows      | that  | they can        | be characterized    | as  |
| most other                                    | cyclones | with    | high | impact   | are in one | of the   | moist follows. |         |                |            |       |                 |                     |     |
| classes (e.g.                                 | ‘Brig’,  | related | to a | damaging | flood      | event    | in the         |         |                |            |       |                 |                     |     |
Southern Alps, ‘Rolf’, which caused heavy precipitation in the • A : cyclogenesis occurs in a region with very weak QG
dry
Mediterranean,‘Lothar’,producingstronglydamagingwindsin upper-level forcing for ascent beneath a shallow upper-
CentralEurope,and‘Snow’,associatedwithhighamountsofwet levelridge,moderatebaroclinicity,moderatehumiditybut
snowovernorthernGermany).
noprecipitation.
•
|     |     |     |     |     |     |     |     | A moist | : cyclogenesis |     | occurs | downstream | of a | large-scale |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------ | ---------- | ---- | ----------- |
6. Conclusions upper-leveltroughwithmoderateQGupper-levelforcing
attheaxisofanupper-leveljetandatthepolewardedgeof
averymoistlow-levelairmass.Baroclinicityisverystrong,
| This study | introduced |     | a novel | approach | to classify | events | of  |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------- | -------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
extratropicalcyclogenesis.Comparedwithpreviousapproaches, as are precipitation and the amplitude of the cyclonic
which were based on the physical understanding of the key low-levelPVanomaly.
•
precursor fields, our approach is more objective in the sense B : cyclogenesis occurs downstream of an upper-level
dry
that it includes a large set of potential precursors and then cut-off-like flow situation with moderate QG upper-
determines statistically those that show the largest variability level forcing in a typically dry environment and weak
baroclinicity.
| across a | large ensemble |     | of 16029 | genesis | events. | Our analysis |     |     |     |     |     |     |     |     |
| -------- | -------------- | --- | -------- | ------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
•
indicates that no obvious cyclone clustering occurs within the B moist : cyclogenesis occurs at the downstream flank of a
30-dimensional precursor phase space. However, a projection pronouncedandcomparativelynarrowupper-leveltrough
of all 16029 cyclogenesis events on the first two PCs of the withverystrongQGforcingforascentattheleftexitofan
precursor phase space allows for a meaningful separation of intensejetstreak.Humidityismoderate,precipitationand
cyclones into five classes. The first two PCs (PC1 and PC2) low-leveldiabaticPVproductionarestrong.
Table2. Tablewithaselectionofextratropicalcyclogenesiscases.
| Name |     | Abbrev. |     | Paper |     |     |     | Lat/Lon |     | tgen |     | Class | pgen | pmin |
| ---- | --- | ------- | --- | ----- | --- | --- | --- | ------- | --- | ---- | --- | ----- | ---- | ---- |
President’sdaystorm President Whitakeretal.(1988) 33◦N78◦W 1979/02/190000UTC Amoist 1018.4 979.6
UKOctoberstorm UKOct HoskinsandBerrisford(1988) 32◦N72◦W 1987/10/121200UTC Amoist 1008.6 958.7
EricaIOP4 EricaIOP4 NeimanandShapiro(1993) 36◦N75◦W 1989/01/011800UTC Amoist 1013.3 967.5
Brigflood Brig Massacandetal.(1998) 37◦N01◦E 1993/09/220600UTC Amoist 1011.0 1001.1
Lothar Lothar Wernlietal.(2002) 37◦N63◦W 1999/12/240600UTC Amoist 1010.9 976.5
46◦N24◦W
| Martin |     | Martin |     | -   |     |     |     |     | 1999/12/270000UTC |     |     | Amoist | 1000.5 | 969.8 |
| ------ | --- | ------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------ | ------ | ----- |
35◦N01◦E
Algeria Algeria Tripolietal.(2005) 2001/11/051200UTC Adry 1018.6 1018.1
66◦N09◦E
| Dryevent |     | Dry |     | -   |     |     |     |     | 2002/10/200600UTC |     |     | Bdry | 1002.7 | 1002.7 |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ---- | ------ | ------ |
59◦N10◦E
Snowevent Snow FrickandWernli(2012) 2005/11/241800UTC Bmoist 989.8 974.1
32◦N78◦W
DRW DRW BoettcherandWernli(2011) 2005/12/181200UTC Amoist 1017.7 975.8
44◦N61◦W
Kyrill Kyrill Finketal.(2009) 2007/01/160600UTC Amoist 1002.6 964.0
Klaus Klaus Liberatoetal.(2011) 44◦N29◦W 2009/01/230600UTC Amoist 994.2 967.5
WCB WCB JoosandWernli(2012) 45◦N23◦W 2009/01/290600UTC Bmoist 987.7 972.9
Xynthia Xynthia Ludwigetal.(2014) 26◦N41◦W 2010/02/241800UTC Amoist 1012.7 969.0
| Rolf |     | Rolf |     | -   |     |     | 41◦N00◦E |     | 2011/11/041800UTC |     |     | Bmoist | 995.3 | 995.3 |
| ---- | --- | ---- | --- | --- | --- | --- | -------- | --- | ----------------- | --- | --- | ------ | ----- | ----- |
ThecolumnNamecontainsthenameorashortdescriptionoftheeventandthecolumnAbbrev.theabbreviationthatisusedinFigure12.Papershowsoneselected
referenceforthiscase.Lat/Londenotesthegeographicallocationofthecyclogenesisandtgenitsdateandtime.Classshowstheassignedclass.pgenindicatesSLPin
thecyclonecentreduringgenesisandpmintheminimumSLPalongthewholetrack.
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)

1060 M.A.Grafetal.
• M: the fifth class represents genesis events with average References
characteristics. For events in this class, none of the main
precursorsisparticularlystrongorweak. BentleyAM,KeyserD,BosartLF.2016.Adynamicallybasedclimatologyof
subtropicalcyclonesthatundergotropicaltransitionintheNorthAtlantic
Mostofthewell-knownandhigh-impactcyclonesconsideredin basin.Mon.WeatherRev.144:2049–2068.
thisstudy(theUSPresident’sDaycyclone,ERICAIOP4,theUK BinderH,BoettcherM,JoosH,WernliH.2016.Theroleofwarmconveyorbelts
OctoberstormandtheEuropeanwindstormsLothar,Klausand fortheintensificationofextratropicalcyclonesinNorthernHemisphere
Xynthia) belong to class A , i.e. the class with, on average, winter.J.Atmos.Sci.73:3997–4020.
moist
BishopCH,ThorpeAJ.1994.Frontalwavestabilityduringmoistdeformation
thehighestvaluesofbaroclinicityandverticallyintegratedwater
frontogenesis.PartII:Thesuppressionofnonlinearwavedevelopment.J.
vapour. Note that our classification only considered cyclones Atmos.Sci.51:874–888.
at the time of genesis and an analysis of how the evolution BjerknesJ,SolbergH.1922.Lifecycleofcyclonesandthepolarfronttheoryof
of cyclones projects on our parameter phase space would be a atmosphericcirculation.Geophys.Publ.3:1–18.
potentially attractive extension of this study. Another valuable Bleck R, Mattocks C. 1984. A preliminary analysis of the role of potential
vorticityonAlpineleecyclogenesis.Contrib.Atmos.Phys.57:357–368.
extension could be to investigate cyclogenesis in the Southern
BlenderR,FraedrichK,LunkeitF.1997.Identificationofcyclone-trackregimes
Hemispherealsoandindifferentseasons.
intheNorthAtlantic.Q.J.R.Meteorol.Soc.123:727–741.
Finally, we comment on the limitations of our approach
BoettcherM,WernliH.2011.LifecyclestudyofadiabaticRossbywaveas
and the resulting classification. The limitations mainly concern a precursor to rapid cyclogenesis in the North Atlantic – dynamics and
(i) the accuracy of the dataset, (ii) sensitivity to the cyclone- forecastperformance.Mon.WeatherRev.139:1861–1878.
tracking scheme, (iii) the choice of precursor parameters and Campa J, Wernli H. 2012. A PV perspective on the vertical structure of
maturemidlatitudecyclonesintheNorthernHemisphere.J.Atmos.Sci.69:
(iv) the classification. Our results are based on ERA-Interim, 725–740.
one of the widely used state-of-the-art reanalysis datasets. Still,
CattoJ.2016.Extratropicalcycloneclassificationanditsuseinclimatestudies.
potential small-scale flow structures are not captured by this Rev.Geophys.54:486–520.
dataset(becauseitsresolutionistoocoarse)andthereforecannot Chaboureau JP, Thorpe AJ. 1999. Frontogenesis and the development of
be identified as a potential precursor. We defined ‘genesis’ as secondarywavecyclonesinFASTEX.Q.J.R.Meteorol.Soc.125:925–940.
DacreHF,GraySL.2009.Thespatialdistributionandevolutioncharacteristics
thefirstpointofacyclonetrackandthereforeoursetofgenesis
ofNorthAtlanticcyclones.Mon.WeatherRev.137:99–115.
eventsdependsonthecycloneidentificationandtrackingscheme
DaviesHC.1997.Emergenceofthemainstreamcyclogenesistheories.Meteorol.
utilized.ThetrackingintercomparisonstudybyNeuetal.(2013) Z.6:261–274.
showedthatmostcyclone-trackingschemesagreefairlywellfor DaviesHC.2010.Anearlyandperceptiveconceptofcyclogenesis.Meteorol.Z.
intense cyclones during the central period of their life cycle. 19:513–517.
However, the early and late phases of a cyclone, i.e. the phases DavolioS,MigliettaM,MoscatelloA,PacificoF,BuzziA,RotunnoR.2009.
Numericalforecastandanalysisofatropical-likecycloneintheIonianSea.
near genesis and lysis, are more sensitive and depend on the
Nat.HazardsEarthSyst.Sci.9:551–562.
tracking technique adopted. Therefore, an alternative tracking
DeeDP,UppalaSM,SimmonsAJ,BerrisfordP,PoliP,KobayashiS,Andrae
scheme (e.g. a scheme that tracks low-level relative vorticity U,BalmasedaMA,BalsamoG,BauerP,BechtoldP,BeljaarsACM,van
maxima) might cause cyclones to have a slightly different time deBergL,BidlotJ,BormannN,DelsolC,DraganiR,FuentesM,Geer
and location of cyclogenesis. It might be an interesting task for AJ,HaimbergerL,HealySB,HersbachH,Ho´lmEV,IsaksenL,Ka˚llberg
P,Ko¨hlerM,MatricardiM,McNallyAP,Monge-SanzBM,MorcretteJ-J,
future research to test the sensitivity of the genesis conditions
ParkB-K,PeubeyC,deRosnayP,TavolatoC,The´pautJ-N,VitartF.2011.
identifiedtothechoiceoftrackingscheme–however,giventhat TheERA-Interimreanalysis:Configurationandperformanceofthedata
ourmaingenesisregionsareinverygoodagreementwithother assimilationsystem.Q.J.R.Meteorol.Soc.137:553–597.
cycloneclimatologies,weareconvincedthatourgenesislocations DevesonACL,BrowningKA,HewsonTD.2002.AclassificationofFASTEX
cyclones using a height-attributable quasi-geostrophic vertical-motion
are meaningful for the classification exercise adopted. A brief
diagnostic.Q.J.R.Meteorol.Soc.128:93–117.
sensitivitytestpresentedinsection5revealedthatomittingsome
Egger J, Alpert P, Tafferner A, Ziv B. 1995. Numerical experiments on the
ofthelessimportantprecursorswouldnotchangetheresultsof genesisofSharavcyclones:Idealizedsimulations.TellusA47:162–174.
thepresentstudysubstantially.Moredifficulttoassessiswhether EvansJL,GuishardMP.2009.Atlanticsubtropicalstorms.PartI:Diagnostic
or not we missed any important precursors in our analysis. criteriaandcompositeanalysis.Mon.WeatherRev.137:2065–2080.
This cannot be excluded, but given the large set of precursors FickerH.1920.DerEinflussderAlpenaufFallgebietedesLuftdrucksunddie
EntwicklungvonDepressionenu¨berdemMittelmeer.(Theinfluenceofthe
and the thorough literature search, we regard this as unlikely.
Alpsonareasoffallingairpressureandthedevelopmentofdepressionsover
Finally, there is also some subjectivity in our classification. The theMediterraneanSea).Meteorol.Z.37:350–363.Translatedandeditedby
numberofclassesissomehowarbitrary,butfiveappearstobea VolkenE,Bro¨nnimannS.Meteorol.Z.19:489–500.
sensiblechoice,giventhatthecompositesrevealstronglydiffering Fink AH, Bru¨cher T, Ermert V, Kru¨ger A, Pinto JG. 2009. The European
stormKyrillinJanuary2007:Synopticevolution,meteorologicalimpacts
structures.Thewaytheclasseswereconstructed(divisionofthe
andsomeconsiderationswithrespecttoclimatechange.Nat.HazardsEarth
PC1–PC2 phase space) in more or less equal segments is a
Syst.Sci.9:405–423.
pragmatic and somehow objective approach, given that there FrickC,WernliH.2012.Acasestudyofhigh-impactwetsnowfallinnorthwest
are no well-defined a priori clusters in the phase space. It is Germany(25–27November2005):Observations,dynamics,andforecast
importanttobeawareofthelimitationsofandspecificchoices performance.WeatherandForecasting27:1217–1234.
GabrielKR.1971.Thebiplotgraphicdisplayofmatriceswithapplicationto madeinourapproach,whichneverthelessprovidesanimportant
principalcomponentanalysis.Biometrika58:453–467.
step forward in understanding the main factors that determine
Gabriel KR. 1972. Analysis of meteorological data by means of canonical
thelargevariabilityofcyclogenesisintheNorthernHemisphere decompositionandbiplots.J.Appl.Meteorol.11:1071–1077.
extratropics. GraySL,DacreHF.2006.Classifyingdynamicalforcingmechanismsusinga
height-attributableclimatology.Q.J.R.Meteorol.Soc.132:1119–1137.
GyakumJR.1991.Meteorologicalprecursorstotheexplosiveintensification Acknowledgements
oftheQEIIstorm.Mon.WeatherRev.119:1105–1131.
Gyakum JR, Danielson RE. 2000. Analysis of meteorological precursors to
We thank the anonymous reviewers for their constructive and ordinary and explosive cyclogenesis in the Western North Pacific. Mon.
very helpful comments and MeteoSwiss for granting access to WeatherRev.128:851–863.
theECMWFreanalysisdata.MGacknowledgesfundingfromthe Han W, Chen SJ, Egger J. 1995. Altai–Sayan lee cyclogenesis: Numerical
simulations.Meteorol.Atmos.Phys.55:125–134.
ETHresearchgrantETH-2010-2.
HodgesK.1999.Adaptiveconstraintsforfeaturetracking.Mon.WeatherRev.
127:1362–1373.
Supportinginformation HodgesKI,LeeR,BengtssonL.2011.Acomparisonofextratropicalcyclonesin
recentreanalysesERA-Interim,NASAMERRA,NCEPCFSR,andJRA-25.
J.Clim.24:4888–4906.
Thefollowingsupportinginformationisavailableaspartofthe
HorvathK,FitaL,RomeroR,Ivancan-PicekB.2006.Anumericalstudyofthe
onlinearticle: firstphaseofadeepMediterraneancyclone:Cyclogenesisintheleeofthe
FileS1.Detaileddescriptionandcompositesofprecursors. AtlasMountains.Meteorol.Z.15:133–146.
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)
1477870x,
2017,
703,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989
by
Univ
of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[26/02/2025].
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

ExtratropicalCyclogenesisClassification 1061
HoskinsBJ,BerrisfordP.1988.Apotentialvorticityperspectiveofthestorm PetterssenS,SmebyeSJ.1971.Onthedevelopmentofextratropicalcyclones.
of15–16October1987.Weather43:122–129. Q.J.R.Meteorol.Soc.97:457–482.
HoskinsBJ,HodgesKI.2002.NewperspectivesontheNorthernHemisphere PlantRS,CraigGC,GraySL.2003.Onathreefoldclassificationofextratropical
winterstormtracks.J.Atmos.Sci.59:1041–1061. cyclones.Q.J.R.Meteorol.Soc.129:1653–1675.
HoskinsBJ,McIntyreME,RobertsonAW.1985.Ontheuseandsignificance RenfrewIA,ThorpeAJ,BishopCH.1997.Theroleoftheenvironmentalflow
ofisentropicpotentialvorticitymaps.Q.J.R.Meteorol.Soc.111:877–946. inthedevelopmentofsecondaryfrontalcyclones.Q.J.R.Meteorol.Soc.
HotellingH.1933.Analysisofacomplexofstatisticalvariablesintoprincipal 123:1653–1675.
components.J.Educ.Psychol.24:417. RivalsH,CammasJP,RenfrewIA.1998.Secondarycyclogenesis:Theinitiation
IwabeCMN,daRochaRP.2009.Aneventofstratosphericairintrusionand phaseofafrontalwaveobservedovertheeasternAtlantic.Q.J.R.Meteorol.
itsassociatedsecondarysurfacecyclogenesisovertheSouthAtlanticOcean. Soc.124:243–267.
J.Geophys.Res.114:D09101,doi:10.1029/2008JD011119. Rivie´re G, Arbogast P, Maynard K, Joly A. 2010. The essential ingredients
JolliffeIT.2002.PrincipalComponentAnalysis.Springer:NewYork. leadingtotheexplosivegrowthstageoftheEuropeanwindstormLotharof
JoosH,WernliH.2012.Influenceofmicrophysicalprocessesonthepotential Christmas1999.Q.J.R.Meteorol.Soc.136:638–652.
vorticity development in a warm conveyor belt: A case-study with the RossaAM,WernliH,DaviesHC.2000.Growthanddecayofanextratropical
limited-areamodelCOSMO.Q.J.R.Meteorol.Soc.138:407–418. cyclone’sPV-tower.Meteorol.Atmos.Phys.73:139–156.
KleinschmidtE.1950.U¨berAufbauundEntstehungvonZyklonen(1.Teil). SandersF,GyakumJR.1980.Synoptic-dynamicclimatologyofthe‘bomb’.
Meteorol.Rundsch.3:1–6. Mon.WeatherRev.108:1589–1606.
KuoYH,ReedRJ,Low-NamS.1991.Effectsofsurfaceenergyfluxesduring Scha¨r C, Wernli H. 1993. Structure and evolution of an isolated semi-
theearlydevelopmentandrapidintensificationstagesofsevenexplosive geostrophiccyclone.Q.J.R.Meteorol.Soc.119:57–90.
cyclonesovertheAtlantic(ERICA).Mon.WeatherRev.125:457–476. Schemm S, Sprenger M. 2015. Frontal-wave cyclogenesis in the North
LackmannGM,KeyserD,BosartLF.1997.Acharacteristiclifecycleofupper- Atlantic – a climatological characterisation. Q. J. R. Meteorol. Soc. 141:
tropospheric cyclogenetic precursors during the experiment on rapidly 2989–3005.
intensifyingcyclonesovertheAtlantic(ERICA).Mon.WeatherRev.125: SchemmS,WernliH,PapritzL.2013.Warmconveyorbeltsinidealizedmoist
2729–2758. baroclinicwavesimulations.J.Atmos.Sci.70:627–652.
LagouvardosK,KotroniV,DeferE.2007.The21–22January2004explosive SerrezeMC,CarseF,BarryRG,RogersJC.1997.Icelandiclowcycloneactivity:
cyclogenesisovertheAegeanSea:Observationsandmodelanalysis.Q.J.R. climatologicalfeatures,linkageswiththeNAO,andrelationshipswithrecent
Meteorol.Soc.125:3415–3437. changesintheNorthernHemispherecirculation.J.Clim.10:453–464.
LiberatoML,PintoJG,TrigoIF,TrigoRM.2011.Klaus–anexceptionalwinter ShawWN.1903.ThemeteorologicalaspectsofthestormofFebruary26-27,
stormoverNorthernIberiaandSouthernFrance.Weather66:330–334. 1903.Q.J.R.Meteorol.Soc.29:233–264.
LoomisE.1841.OnthestormwhichwasexperiencedthroughouttheUnited SimmondsI.2000.SizechangesoverthelifeofsealevelcyclonesintheNCEP
Statesaboutthe20thofDecember,1836.Trans.Am.Philos.Soc.7:125–163. reanalysis.Mon.WeatherRev.128:4118–4125.
LudwigP,PintoJG,ReyersM,GraySL.2014.TheroleofanomalousSST SinclairMR,CongX.1992.PolarairstreamcyclogenesisintheAustralasian
andsurfacefluxesoverthesoutheasternNorthAtlanticintheexplosive region:AcompositestudyusingECMWFanalyses.Mon.WeatherRev.120:
developmentofwindstormXynthia.Q.J.R.Meteorol.Soc.140:1729–1741. 1950–1972.
MalletI,ArbogastP,BaehrC,CammasJP,MascartP.1999.Effectsoflow-level TaffernerA.1990.Leecyclogenesisresultingfromthecombinedoutbreakof
precursorandfrontalstabilityoncyclogenesisduringFASTEXIOP17.Q.J. coldairandpotentialvorticityagainsttheAlps.Meteorol.Atmos.Phys.43:
R.Meteorol.Soc.125:3415–3437. 31–47.
MassacandAC,WernliH,DaviesHC.1998.Heavyprecipitationonthealpine ThomasBC,MartinJE.2007.Asynopticclimatologyandcompositeanalyse
southside:Anupper-levelprecursor.Geophys.Res.Lett.25:1435–1438. oftheAlbertaclipper.WeatherandForecasting22:315–333.
Mendes D, Souza EP, Trigo IF, Miranda P. 2007. On precursors of South TrigoIF,DaviesTD,BiggGR.1999.Objectiveclimatologyofcyclonesinthe
Americancyclogenesis.TellusA59:114–121,doi:10.1029/98GL50869. Mediterraneanregion.J.Clim.12:1685–1696.
Montgomery MT, Farrell BF. 1992. Polar low dynamics. J. Atmos. Sci. 49: TripoliG,MedagliaC,DietrichS,MugnaiA,PanegrossiG,PinoriS,SmithE.
2484–2505. 2005.The9–10November2001Algerianflood:Anumericalstudy.Bull.
Moore RW, Montgomery MT, Farrell BF. 2008. The integral role of a Am.Meteorol.Soc.86:1229–1235.
diabaticRossbyvortexinaheavysnowfallevent.Mon.WeatherRev.136: Wernli H, Davies HC. 1997. A Lagrangian-based analysis of extratropical
1878–1897. cyclones.I:Themethodandsomeapplications.Q.J.R.Meteorol.Soc.123:
MorganMC,Nielsen-GammonJW.1998.Usingtropopausemapstodiagnose 467–489.
midlatitudeweathersystems.Mon.WeatherRev.126:2555–2579. WernliH,SchwierzC.2006.SurfacecyclonesintheERA-40dataset(1958-
NeimanPJ,ShapiroMA.1993.Thelifecycleofanextratropicalmarinecyclone. 2001).PartI:Novelidentificationmethodandglobalclimatology.J.Atmos.
PartI:Frontal-cycloneevolutionandthermodynamicair–seainteraction. Sci.63:2486–2507.
Mon.WeatherRev.121:2153–2176. Wernli H, Sprenger M. 2007. Identification and ERA-15 climatology of
NeuU,AkperovMG,BellenbaumN,BenestadRS,BlenderR,CaballeroR, potentialvorticitystreamersandcutoffsneartheextratropicaltropopause.
Cocozza A, Dacre HF, Feng Y, Fraedrich K, Grieger J, Gulev S, Hanley J.Atmos.Sci.64:1569–1586.
J, Hewson T, Inatsu M, Keay K, Kew SF, Kindem I, Leckebusch GC, Wernli H, Fehlmann R, Lu¨thi D. 1998. The effect of barotropic shear on
Liberato MLR, Lionello P, Mokhov II, Pinto JG, Raible CC, Reale M, upper-levelinducedcyclogenesis:Semigeostrophicandprimitiveequation
RudevaI,SchusterM,SimmondsI,SinclairM,SprengerM,TilininaND, numericalsimulations.J.Atmos.Sci.55:2080–2094.
TrigoIF,UlbrichS,UlbrichU,WangXL,WernliH.2013.IMILAST–a Wernli H, Dirren S, Liniger MA, Zillig M. 2002. Dynamical aspects of the
community effort to intercompare extratropical cyclone detection and lifecycle of the winter storm Lothar (24–26 December 1999). Q. J. R.
tracking algorithms: Assessing method-related uncertainties. Bull. Am. Meteorol.Soc.128:405–429.
Meteorol.Soc.94:529–547. WhitakerJS,UccelliniLW,BrillKF.1988.Amodel-baseddiagnosticstudyof
PearsonK.1901.Onlinesandplanesofclosestfittosystemsofpointsinspace. therapiddevelopmentphaseofthePresidents’sDaycyclone.Mon.Weather
Philos.Mag.Ser.2:559–572. Rev.116:2337–2365.
(cid:2)c 2016RoyalMeteorologicalSociety Q.J.R.Meteorol.Soc.143:1047–1061(2017)
1477870x,
2017,
703,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.2989
by
Univ
of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[26/02/2025].
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