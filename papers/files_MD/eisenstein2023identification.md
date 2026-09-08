WeatherClim.Dynam.,4,981–999,2023
https://doi.org/10.5194/wcd-4-981-2023
©Author(s)2023.Thisworkisdistributedunder
theCreativeCommonsAttribution4.0License.
Identification of high-wind features within extratropical
cyclones using a probabilistic random forest
– Part 2: Climatology over Europe
LeaEisenstein1,BenediktSchulz2,JoaquimG.Pinto1,andPeterKnippertz1
1InstituteofMeteorologyandClimateResearch–TroposphereResearch,
KarlsruheInstituteofTechnology,Karlsruhe,Germany
2InstituteofStochastics,KarlsruheInstituteofTechnology,Karlsruhe,Germany
Correspondence:LeaEisenstein(lea.eisenstein@kit.edu)
Received:14March2023–Discussionstarted:24March2023
Revised:29September2023–Accepted:3October2023–Published:20November2023
Abstract. Strong winds associated with extratropical cy- eragethecauseofthehighestgustsaftertheCJandhasthe
clones are one of the most dangerous natural hazards in highestgustfactor.Asexpected,CFChigh-windareasshow
Europe. These high winds are mostly associated with five highlevelsofhumidityandovercastconditions.Incontrast,
mesoscale features: the warm (conveyor belt) jet (WJ); the theCSischaracterisedbysunnierconditionsinterspersedby
cold(conveyorbelt)jet(CJ);coldfrontalconvection(CFC); patchycumulusclouds,leadingtoabroadercloudcoverdis-
strongcold-sector(CS)winds;and,insomecases,thesting tributionthanforotherfeatures.TheWJproducestheweak-
jet (SJ). The timing within the cyclone’s life cycle, the lo- est windson average butaffects alarger area thanCJ. Cen-
cationrelativetothecyclonecoreandfurthercharacteristics tralEuropeismorestronglyaffectedbyWJandCFCwinds,
differbetweenthesefeaturesand,hence,likelyalsotheiras- whiletheCJusuallyoccursfarthernorthovertheNorthand
sociated forecast errors. In Part 1 of this study (Eisenstein Balticseas,northernGermany,DenmarkandsouthernScan-
etal.,2022a),weintroducedtheobjectiveandflexibleiden- dinavia. System-relative composites show that the WJ and
tification tool RAMEFI (RAndom-forest-based MEsoscale CFC tend to occur earlier in the cyclone life cycle than the
wind Feature Identification), which distinguishes between CJ and CS. Consistently, the CS is the most common cause
the WJ, CFC and CS as well as CJ and SJ combined. of high winds over eastern Europe, where cyclones tend to
RAMEFI is based on a probabilistic random forest trained occlude,representedbyanarrowingwarmsectorandweak-
on station observations of 12 storm cases over Europe. Be- ening cold front. The WJ mostly occurs within the south-
ingindependentofspatialdistribution,RAMEFIcanalsobe eastern quadrant of a cyclone bordered by the narrow CFC
applied to gridded data. Here, we use RAMEFI to compile inthewest.However,thelocationofCFCvariesgreatlybe-
a climatology over 19 extended winter seasons (October– tween cases. The CS occurs in the south-western quadrant,
March2000–2019)basedonhigh-resolutionregionalreanal- whiletheCJappearsclosertothecyclonecentre,sometimes
yses of the German Consortium for Small-scale Modelling stretchingintothesouth-easternquadrant.Thisobjectivecli-
(COSMO) model over Europe. This allows the first ever matologylargelyconfirmsprevious,moresubjectiveinvesti-
long-termobjectivestatisticalanalysisofthemesoscalewind gations but puts these into climatological context. It allows
features,includingtheiroccurrencefrequency,geographical amoredetailedanalysisoffeaturepropertiesandprovidesa
distributionandcharacteristics.ForwesternandcentralEu- solid foundation for model assessment and forecast evalua-
rope,wedemonstratethattheCSisprominentinmostwinter tioninfuturestudies.
storms,whileCFCistheleastcommoncauseofhighwinds,
bothintermsoffrequencyandaffectedarea.However,prob-
ably due to convective momentum transport, CFC is on av-
PublishedbyCopernicusPublicationsonbehalfoftheEuropeanGeosciencesUnion.

982 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
1 Introduction cold sectors are indicated by temperature-related parame-
ters.Giventhecase-to-casevariabilityintheparametersused
Highwindspeedsassociatedwithextratropicalcyclones,es- here,theRFoutputsaprobabilityoffeatureoccurrence.
peciallyduringwintertime,cancauseenormousamountsof Giventhatextratropicalcyclonesaresuchadominantfea-
damageandbelongtothemostseverenaturalhazards(Fink ture of the midlatitudes, several objective algorithms have
etal.,2009).Duringacyclone’slifetime,thestrongestwind beendevelopedforidentifyingcyclonesandtheirtracksfrom
gustscanbeinducedbydifferentairstreamsassociatedwith digitaldata,eitherreanalysisorclimatemodeldata(seeUl-
the storm (Hewson and Neu, 2015). As discussed in Part 1 brich et al., 2009, and Neu et al., 2013, for an overview).
(Eisensteinetal.,2022a)andillustratedintheirFig.1,strong Depending on the perception of what a cyclone is, various
wind gusts are mostly connected to five features: the warm variables can be used for tracking (Hoskins and Hodges,
jet(WJ),thecoldjet(CJ),thestingjet(SJ),coldfrontalcon- 2002),butthemostcommonaremeansealevelpressureand
vection (CFC) and high winds within the cold sector (CS). 850hPa relative vorticity. During winter, three local max-
The WJ is part of the early stages of the warm conveyor imaofcyclonefrequencyarefoundovertheNorthernHemi-
belt,anascendingairflowaheadofthecoldfront(Wernliand sphere, namely over the North Atlantic, North Pacific and
Davies, 1997; Eckhardt et al., 2004; Madonna et al., 2014); Mediterranean(Ulbrichetal.,2009).Whilethetwofirstre-
whileitisstillnearthesurface,itcauseshighwindswithin gions are identified for all methods, the maximum over the
thewarmsectorofacyclone.Here,wedefineCFCasthere- Mediterraneanisdependentontheresolutionofthedataset
gionof highwindsco-locatedwithprecipitation aroundthe and on the methodology used. Neu et al. (2013) compared
cold front (also if it is occurring ahead of the surface front 15 cyclone tracking methods and found significant differ-
in the case of forward-tilted fronts). In Shapiro–Keyser cy- ences in life cycle characteristics; however, a large consis-
clones(ShapiroandKeyser,1990),thewarm–orbentback tency is found for long-lived, intense cyclones. Dacre et al.
– front is usually the stronger front (Catto, 2016). Consid- (2012) describe the development and compilation of an ex-
eringrecentcasesofShapiro–Keysercyclones(e.g.Egonin tratropical cyclone atlas using 200 extreme North Atlantic
2017,Xavierin2017andFriederikein2018;seeEisenstein cyclones over a 20-year period. The atlas includes compos-
et al., 2022a), CFC appears to be more common following itesofhorizontalandverticalcyclonestructure,multiplepa-
the Norwegian cyclone model (Bjerknes, 1919). As for the rameters (e.g. cloud cover, wind and relative humidity) and
warmconveyorbelt,theCJisassociatedwiththecoldcon- cyclone evolution while also identifying the warm and cold
veyorbeltaheadofthewarmfrontandwrappingaroundthe conveyorbeltsanddryintrusions.
cyclonecentre.Incontrasttothewarmconveyorbelt,how- A climatology focusing on near-surface winds can be
ever, the cold conveyor belt, and hence the CJ, stays at low found in Laurila et al. (2021). They focus on the North At-
levelsduringitslifetime.TheSJisanairstreamdescending lanticandEuropebydefininganextremewindfactor,which
from mid-levels within the cloud head into the frontal frac- isthemonthly98thpercentiledividedbythemonthlymean
ture region of a Shapiro–Keyser cyclone (Clark and Gray, windspeed.Whiletheyfoundnolineartrendbetween1979
2018). It can cause high wind speeds slightly ahead of and and 2018, they showed that the strongest winds are mostly
earlierthantheCJifitreachesthesurface.Highwindsinthe connected with storm tracks in the winter season. This is
cold-sector region, i.e. behind CFC but not associated with consistentwiththereviewpaperofFeseretal.(2015),who
theCJorSJ,areclassifiedasCS,whichcan,forexample,in- concludedthatdecadalvariabilityisthedominantfeatureof
cludepost-CFCandwindscausedbydryintrusions(Raveh- storminessovertheregioninthelast100–150yearsandthat
RubinandCatto,2019). onlyregionalandshort-termtrendscanbeidentified.Asex-
The RAMEFI (RAndom-forest-based MEsoscale wind pected from the surface and boundary layer characteristics,
Feature Identification) method, introduced in Part 1 (Eisen- Laurila et al. (2021) also identified a distinct land–sea con-
steinetal.,2022a),focusesontheidentificationofWJ,CFC, trastinthe10mwindspeed.Thesameistrueforwindgusts,
CJ, CS and high winds associated with no feature (NF). As given, for example, the very different gust factors typically
theCJandSJhavesimilarsurfaceparametercharacteristics foundforoffshore/inlandareas(Wieringa,1973).
due to their proximity in both time and space, the SJ is in- Tothebestofourknowledge,thefirstclimatologyfocus-
cludedinthemorefrequentCJfeature.Fortheidentification, ingondifferentmesoscalewindregionswithincycloneswas
the features were subjectively labelled for 12 winter storms Parton et al. (2010), who differentiated cold frontal events,
basedonsurfaceobservations,whichwerethenusedforthe warm-sector events, tropopause folds/warm fronts, SJs and
training of a probabilistic random forest (RF). The RF can unclassifiedeventswithindatafromawind-profilingradarin
alsobeappliedtodifferentdatasets,independentofhorizon- Walesovera7-yearperiod.Accordingtothem,warm-sector
talresolution.Itlearnedphysicallyconsistentcharacteristics, events are the most common cause of strong winds (around
such as decreasing pressure ahead of the cold front, where 40%ofinstances),whilecoldfrontaleventscomprisearound
the WJ is located, and increasing pressure behind the front, 24%ofinstancesovertheinvestigatedarea,whichmaynot
where the CJ and CS are located. The most important pre- berepresentativeofcyclonesingeneral.AstudybyRivière
dictor for CFC is precipitation. Furthermore, the warm and etal.(2015)suggeststhatacycloneisdominatedbytheWJ
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 983
initsearlystagesandbytheCJlater.HewsonandNeu(2015) particularsurfaceobservationsandagriddeddataset.Fora
compiled a subjective climatology of WJs, CJs and SJs on fulldescription,werefertoPart1(Eisensteinetal.,2022a).
the basis of 29 wind storms. Note that their definition of a Fortheclimatology,wefocusontheextendedwintermonths,
WJ also includes CFC. They created an idealised concep- OctobertoMarch,including19yearsofdata.Tomakesure
tual model for the timing relative to the cyclone life cycle, thatonlywinterstormsareincludedinourclimatology,cy-
the location relative to the cyclone centre and their strength clonetracksandfurtherfiltersareused.
while also suggesting differences in further characteristics,
suchasinstability/stabilityandverticalgradientofhorizon- 2.1 Surfaceobservations
tal wind speed. In addition to these low-level jet features,
Earl et al. (2017) further distinguished various convection- TheobservationaldatasetprovidedbytheGermanWeather
induced high-wind features. Consistent with other studies, Service (DWD) includes hourly surface observations over
theyfoundthatWJsandCJsaremostcommonwhenlooking land from 2001 to mid-2020 containing five parameters:
atthehighest1%ofdailymaximumwindgusts,whileCFC mean sea level pressure (p), 2m air temperature (T), wind
andpotentialSJscommonlycausethehighest0.1%ofdaily speed at 10m (v), wind direction at 10m (d) and precipita-
maximum gusts. However, their focus was solely on winter tionamount(RR).Additionally,thepotentialtemperature(θ)
stormsovertheUK,similartoPartonetal.(2010). is computed, and θ and v are normalised by their median
Recently, some first objective approaches to identify and98thpercentilerespectively,totakethediurnalandsea-
mesoscale wind features have been developed by Manning sonal cycles as well as location-specific characteristics into
et al. (2022) and Gentile and Gray (2023). Both studies use account (θ ˜ and v˜ respectively). The median and 98th per-
thestrongthermal(andmoistureinthelatter)gradienttode- centile are computed for the specific location, time of the
tectfrontsanddefinehighwindsonthewarmsideasaWJ. day and day of the year ±10d using the available time pe-
˜
While Manning et al. (2022) identify SJs using a kinematic riod.Furthermore,temporaltendenciesofp,θ andd arecal-
˜
objective identification and define all further high winds on culated((cid:49)p,(cid:49)θ and(cid:49)d respectively)andaresimplyrepre-
the cold side of the fronts as CJs, Gentile and Gray (2023) sentedbythedifferencebetweenthecurrentandtheprevious
distinguishbetweentheCJtravellingagainstthesystemmo- hour.
tion(namedCCBa)andtheCJwrappingaroundthecyclone AsinPart1(Eisensteinetal.,2022a),weconcentrateon
centre (CCBb) following Earl et al. (2017). Thus, the latter westernandcentralEurope,morespecifically,stationswithin
resembles our definition of a CJ merged with the CS. Al- theareaof40to60◦Nand10◦Wto20◦E.Afterremoving
though Manning et al. (2022) focus on future changes and stations that measure fewer than three of the five meteoro-
GentileandGray(2023)ona9-yearclimatology,bothworks logical parameters, around 750 station reports per time step
concludethatwindsinthecoldsectortothewestandsouth remainonaverage.Fortheclimatology,weincludealltime
ofthecyclonecentrehavehigherwindspeedsthanintheWJ. steps from January 2001 to December 2019, i.e. a total of
Furthermore,GentileandGray(2023)analyseatmosphere– 114months.
ocean–wave coupling based on ocean stations and find that
theCCBbisthemostcommoncauseofhighwindswithan 2.2 COSMO-REA6
increasingproportionofCCBatothenorth-eastoftheUK.
The goal of this study is to expand and complement COSMO-REA6 is a reanalysis data set based on the
existing shorter and/or more general climatologies using German Consortium for Small-scale Modeling (COSMO)
RAMEFI, the first tool to objectively distinguish the WJ, model from the DWD computed by the Hans-Ertel-Centre
CFC, CJ and CS. With this aim, a high-resolution regional for Weather Research. The data set covers the European
reanalysisdatasetfor19extendedEuropeanwinterseasons CORDEX (Coordinated Downscaling Experiment) domain
is used. Other observational data sets are used for specific with a grid spacing of 0.055◦, i.e. roughly 6km, and uses
aspectsorascomparison.Thepaperisstructuredasfollows: ERA-Interimdata(Deeetal.,2011)asboundaryconditions.
first,webrieflyrecapitulatethedatasetsandmethodalready The reanalysis is available from 1995 to mid-2019. For a
introduced in Part 1 (Sect. 2), Sect. 3 focuses on the occur- faircomparisonofthetwodatasets,thechosentimeperiod
renceoftheidentifiedhigh-windfeatures(i.e.frequency,rel- for the climatology is as close as possible while including
ativetothecyclonecentreandcyclonelifecycle),Sect.4dis- 19extendedwinterseasonseach.Thismeansthat,although
cusses the different characteristics of the features, and con- theobservationscoverJanuary2001toDecember2019,the
clusionsaredrawninSect.5. COSMO-REA6 data for October 2000 to March 2019 are
used, i.e. with a minor shift of 3 months. In addition to the
parameters mentioned above, COSMO-REA6 allows us to
2 Dataandmethod includefurthervariables,suchaswindgustsat10m(v gust ),
specific humidity at 2m (q), relative humidity at 2m (RH)
Our approach is based on the novel RAMEFI method. This andtotalcloudcover(cc).Themodelusesaconvectionpa-
section briefly introduces the method and data sets used, in rameterisation by Tiedtke (1989) and wind gusts are esti-
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

984 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
matedfollowingSchulzandHeise(2003)andSchulz(2008) et al., 2022a) was to evaluate whether the RF is able to re-
with a turbulent- and a convective-gust component. The liably identify the features in unseen data. Here, we want
cloud cover is based on cloud water and cloud ice; consid- to generate a climatology of the high-wind features rather
ers grid-scale, sub-grid convective and sub-grid stratiform thantestingthemethod.Hence,itisunproblematictoapply
clouds (Doms et al., 2021); and is verified using ceilome- RAMEFI to the same data that it was trained on. Instead,
ter data (Bollmeyer et al., 2015). For a detailed description we obtain an identification that mirrors the subjective iden-
ofthedataset,werefertoBollmeyeretal.(2015)andDoms tification within in these storms and is still consistent with
et al. (2021). The median and 98th percentile used for the theentireclimatologyduetothesamemodelunderlyingthe
normalisationofθ andvrespectively,areonlycomputedfor identification.
the10-yeartimeperiodfrom2005to2015duetocomputa- IncontrasttoPart1(Eisensteinetal.,2022a),RAMEFIis
tionalcost.Thedata,originallyonarotatedgrid,wereregrid- alsoappliedtooceangridpointsofCOSMO-REA6,whereit
ded to a latitude–longitude grid with a spacing of 0.0625◦, hasnotbeensystematicallyevaluated;thus,resultsshouldbe
i.e. roughly 7km, for the area of 40 to 65◦N and 10◦W to treated with some caution there. Considering that the wind
25◦E.Notethattheareashowsaneastwardextensionanda speeddistributionoverseaisbroader,the80%thresholdof
northerlyshiftcomparedwiththeobservationaldatasettoin- the98thpercentileofvresultsinmorewindyconditionsover
cludemorenorthernregionsaffectedbywinterstorms,where the ocean than over land (see Appendix A). Characteristics
theobservationaldataaresparse. of other parameters are discussed in Sect. 4. Nevertheless,
looking at various cases over the 19-year period, the ocean
2.3 RAMEFI and land do not seem to behave fundamentally differently
with respect to feature detection and their probability dis-
RAMEFI delivers a probabilistic identification of the five tributions. Exemplary cases can be accessed in the “Video
features, WJ, CFC, CJ, CS and NF, with SJ being included supplement”(Eisensteinetal.,2023b).
in the CJ. The method is based on an RF that was trained As RAMEFI provides a probabilistic identification, each
on surface observations of 12 storm cases, for which the featureisassignedaprobabilityfrom0to1.Thedistribution
windfeaturesweresubjectivelylabelled.Thesecasestudies oftheprobabilitiesforeachfeatureisshowninFig.1forboth
arepickedtocaptureahealthydiversityofcyclonedevelop- datasets.WhiletheWJandCSshowasimilardistributionin
ments and features, i.e. they include very intense and more bothdatasetswithpeaksaround48%,themaximumofthe
moderatecycloneswithdifferingstormtracks.Giventhisdi- CJslightlydiffersandislowerataround43%forCOSMO-
versityandthepromisingevaluationofthemethodinPart1 REA6and40%forobservations.Thehighestuncertaintyin
(Eisenstein et al., 2022a), we assume a reliable detection of thefeaturedetectioncanbeseenforCFC,whichshowsover-
the features in long-term data for most cyclones. Note that alllowerprobabilitieswithapeakaround33%.Thebiggest
RAMEFIfocusesonstrongwindspeeds;hence,theRFwas difference in the data sets is found for NF. COSMO-REA6
trainedandtestedonlyfor“windyconditions”,whichwede- showsapeakat50%butaplateaubetween50%and73%in
fineascaseswithv˜>0.8.InPart1(Eisensteinetal.,2022a), theobservations.ThiswillbediscussedfurtherinSect.3.1.
weusedacross-validationapproachforaproperevaluation Thisprobabilisticinformationisusedintwodifferentways:
of the method, i.e. to test the identification for each storm, firstly,weassignthefeaturewiththehighestprobabilityofa
wetrainedtheunderlyingRFontheremaining11casestud- giventimeandgridpoint,ignoringallotherprobabilities(re-
iestoavoidusingdataofthestormofinterest,resultingina ferredtoasMAXPhereafter).Secondly,weexploittheprob-
totalof12RFs.Here,however,weusetheRFtrainedonall abilistic nature of the identification by interpreting the (ac-
ofthe12casestudies(Eisensteinetal.,2022b).Further,the cumulated) feature probabilities as the expected number of
statistical evaluation of the application on COSMO-REA6 features (referred to as ACCP hereafter). The calibration of
data in Part 1 (Eisenstein et al., 2022a) demonstrates that thefeatureprobabilities,whichwascheckedinPart1(Eisen-
RAMEFI generates reliable identifications for gridded data steinetal.,2022a)ofthestudy,isacriticalconditionofthis
despitebeingtrainedonsurfaceobservations.Fordetailson approach.Thesecondapproachisparticularlyimportantfor
themethod,werefertoEisensteinetal.(2022a). featureswithlessconfidentdetection,whichmightbeunder-
RAMEFI is spatially independent, such that the output represented in the first approach, e.g. the CFC as shown in
probabilityiscomputedindividuallyforeachstationorgrid Fig.1(seealsoSect.3.1).1
point. Here, we apply RAMEFI to station observations and
COSMO-REA6dataunderwindyconditionsduringtheex-
tended winter months, regardless of whether a storm oc-
curredornot.However,welaterfiltertheoutputforcyclone
occurrence,asdiscussedinSect.2.4.Notethatthe12cases 1Asanexample,consideranidentificationof75%forrainvs.
used for training (see Eisenstein et al., 2022a) are also in- 25%fornorain.Althoughwealwaysdetectrainviathefirstap-
cluded in the data used for the climatology. The reasoning proach, rain was actually observed, on average, every fourth case
behind the cross-validation approach in Part 1 (Eisenstein (giventhattheprobabilitiesarecalibrated).
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 985
| Figure 1. | Distribution | of  | RAMEFI | probabilities |     | for each | feature |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------ | ------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
overthe19extendedwinterseasonsusingCOSMO-REA6(solid)
| and station | observation |     | data (dashed). |     | The density | is  | calculated |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | -------------- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Figure2.Cyclonetrackdensitywithrespecttothenumberofcy-
basedonsmoothedhistograms.
clonesperyearpersquareddegreeoflatitudewithintheexamined
|     |     |     |     |     |     |     |     | time period | (2000–2019). | The | blue box | represents | the study | area |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | -------- | ---------- | --------- | ---- |
andhatchingindicatesexcludedareas.
2.4 Filteringforcyclonetracks
mountainousregions,theFöhneffectmightbefalselyiden-
| In general, | RAMEFI       | can | be           | used without | any    | filters.   | How- |              |                |      |              |             |         |         |
| ----------- | ------------ | --- | ------------ | ------------ | ------ | ---------- | ---- | ------------ | -------------- | ---- | ------------ | ----------- | ------- | ------- |
|             |              |     |              |              |        |            |      | tified as    | the WJ. Hence, | such | areas        | are removed | from    | the     |
| ever, for   | a meaningful |     | climatology, |              | we aim | to exclude | high |              |                |      |              |             |         |         |
|             |              |     |              |              |        |            |      | climatology, | as indicated   | by   | the hatching | in          | Fig. 2. | We fur- |
windsnotassociatedwithextratropicalcyclonesand,hence,
therdecidedtofocusontheareaof45to65◦Nand10◦Wto
themesoscalewindfeaturesaretargetedhere.Therefore,to
25◦E,therebyincludingthemostimpactedareaoverEurope.
| filter the | gained | probabilities |     | and also | to compile |     | a storm- |     |     |     |     |     |     |     |
| ---------- | ------ | ------------- | --- | -------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Notethatthechangingzonalextentwithlatitudeisneglected
| relative analysis, |          | objectively |            | determined | cyclone |      | tracks are |                   |          |     |           |        |         |        |
| ------------------ | -------- | ----------- | ---------- | ---------- | ------- | ---- | ---------- | ----------------- | -------- | --- | --------- | ------ | ------- | ------ |
|                    |          |             |            |            |         |      |            | in this analysis. | However, |     | we do not | expect | this to | have a |
| used. The          | cyclones | are         | identified | and        | tracked | from | ERA5       |                   |          |     |           |        |         |        |
significantimpactonourmainconclusions.Weremovetime
| (Hersbach | et al., | 2020) | p data | using | an objective |     | tracking |          |             |      |           |             |        |     |
| --------- | ------- | ----- | ------ | ----- | ------------ | --- | -------- | -------- | ----------- | ---- | --------- | ----------- | ------ | --- |
|           |         |       |        |       |              |     |          | steps in | which fewer | than | 5% of all | grid points | during | the |
algorithm(MurrayandSimmonds,1991;Pintoetal.,2005).
|                                            |     |     |     |     |     |     |         | time step | are associated | with | one of | the features   | (excluding |        |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --------- | -------------- | ---- | ------ | -------------- | ---------- | ------ |
| Thealgorithmprimarilysearchesfortheminimum |     |     |     |     |     |     | p inthe |           |                |      |        |                |            |        |
|                                            |     |     |     |     |     |     |         | NF), i.e. | weak cyclones. | Time | steps  | with a cyclone |            | moving |
vicinityofa∇2pmaximum(asaproxyforvorticity)within
|     |     |     |     |     |     |     |     | through | and at least | 5% of | the area | showing | windy | condi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ----- | -------- | ------- | ----- | ------ |
aradiusof750kmtobeassignedascyclonecentres.Tofil-
|              |        |              |       |             |     |             |            | tions are    | referred to | as “stormy | time        | steps”. | Overall, | these  |
| ------------ | ------ | ------------ | ----- | ----------- | --- | ----------- | ---------- | ------------ | ----------- | ---------- | ----------- | ------- | -------- | ------ |
| ter out weak | and    | thermal      | lows, | or cyclones |     | over        | high orog- |              |             |            |             |         |          |        |
|              |        |              |       |             |     |             |            | filters lead | to 1910     | cyclones   | over around | 20000   | time     | steps, |
| raphy, we    | follow | the criteria |       | from Pinto  | et  | al. (2009). | The        |              |             |            |             |         |          |        |
whichareincludedintheanalysis.
| method | settings | used | for ERA-Interim |     | (Neu | et  | al., 2013) |     |     |     |     |     |     |     |
| ------ | -------- | ---- | --------------- | --- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
wereslightlyadaptedtohandlethehigher-spatial-resolution
data of ERA5, while the time resolution was kept at 6h in- 3 Occurrenceofhigh-windfeatures
tervals.Cyclonesmusttravelatleast1000kmandlastforat
| least 1d | to be | considered. | The | resulting | cyclone |     | tracks are |     |     |     |     |     |     |     |
| -------- | ----- | ----------- | --- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Oneofthemainaspectsofthisclimatologyistheoccurrence
then interpolated linearly to gain hourly information. The of the mesoscale wind features in time and space. As men-
| track density, | i.e. | the | number | of cyclones |     | passing | over a |     |     |     |     |     |     |     |
| -------------- | ---- | --- | ------ | ----------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
tionedinSect.1,thefeaturesdevelopduringdifferenttimes
| grid point | (Ulbrich | et  | al., 2009), | of  | all cyclones |     | within the |              |            |     |              |       |        |          |
| ---------- | -------- | --- | ----------- | --- | ------------ | --- | ---------- | ------------ | ---------- | --- | ------------ | ----- | ------ | -------- |
|            |          |     |             |     |              |     |            | in a cyclone | life cycle | and | in different | areas | of the | cyclone. |
19yearscanbeseeninFig.2.Asexpected,giventheselected Inadditiontotheoverallfrequencyofthefeaturesaswellas
studyarea(blueboxinFig.2),cyclonetrackscorresponding
diurnal,seasonalandyearlyvariations(Sect.3.1),RAMEFI
totheidentifiedfeaturestypicallytravelovertheBritishIsles furthergivesusthepossibilityofobtainingtheoccurrenceof
andtheNorthSeatowardstheBalticSea.
|       |          |        |         |       |            |     |        | the wind | features both | in an | Earth-relative | (Sect. | 3.2) | and a |
| ----- | -------- | ------ | ------- | ----- | ---------- | --- | ------ | -------- | ------------- | ----- | -------------- | ------ | ---- | ----- |
| Here, | all grid | points | showing | windy | conditions |     | in the |          |               |       |                |        |      |       |
system-relativeframework,i.e.relativetothecyclonecentre
|     | 15◦ |     |     |     |     |     | 5◦  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vicinity of in the zonal direction and −15 to in the andrelativetothecyclonelifecycle(Sect.3.3).
meridionaldirectionofthecyclonecentreandtheconsidered
areaareused,exceptthoseataltitudesabove800m,consis- 3.1 Relativeoccurrencefrequency
tentwithPart1(Eisensteinetal.,2022a).Furthermore,fol-
lowingPart1,weexcludetheBalkans,wheretopographyis Figure 3 shows the relative frequency of the wind fea-
complex and where winter storms are rare. For example, in tures for both observations (first row) and COSMO-REA6
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

986 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
(lower three rows) over all time steps and grid points sat- steinetal.,2022a)foradetaileddiscussion(Eisensteinetal.,
isfying stormy time step conditions (Sect. 2.4). While the 2022a).AstheoverallcertaintyofNFislowerforCOSMO-
left two columns show all features, including NF, the right REA6 and closer to the density of the CS and WJ (solid
twocolumnsneglectNFtofocusontheidentifiedmesoscale lines in Fig. 1), the proportion in Fig. 3f actually increases,
windfeatures.Furthermore,thefrequenciesofthemostprob- whereas the CS and WJ proportion decreases. As the pro-
ablefeature(MAXP)aredisplayednexttotheaccumulated portion of NF also substantially affects the proportions of
probabilities (ACCP), i.e. the expectation. For better com- theotherfeatures,wecompareobservationsandgriddeddata
parison between the observations and reanalysis, COSMO- withoutNFfromhereon(Fig.3g,h).Therefore,apartfrom
REA6isdisplayedforlandgridpoints,oceangridpointsand thedifferencesinNFdescribedintheprevioussentence,the
allgridpoints. largest difference between the two data sets can be seen in
As displayed in Fig. 3a, of the four mentioned features, the CJ percentage, with an increase of almost 8 percentage
theCSshowsthehighestproportion(21.5%)andisthemost points for land grid points in COSMO-REA6 and over 16
probablefeature,followedbytheWJ(withjustunder15%). percentage points for ocean grid points for MAXP. This is
TheCJreachesmerely4%,whiletheleastcommonfeature duetothefactthattheCJcommonlyoccursinnortherncon-
isCFCwithunder1%.However,NFhasaproportionofal- tinentalEurope,overtheseaandinScandinavia,i.e.regions
most 60% – almost 3 times as much as the CS. This might wherefewerstationobservationsareavailableinourdataset
be caused by missing values within the data set, which are (seeSect.3.2andFig.6e).Ontheotherhand,theCSmostly
replaced by the mean values of the variable. This compli- occursfurthersouth,i.e.fartherawayfromthecyclonecen-
catesthe distinctionbetween thefeatures, asfewer parame- tre,suchthatahigherCJpercentageleadstolowerpercent-
tersincludeinformationaboutthecurrentconditions,leading agesfortheCSinthegriddeddataoverland.TheWJ,which
tohigherprobabilitiesofNFandcausingNFtobethemost occurs more over land than over sea (cf. Fig. 3e–h and i–
probable feature more often. Indeed, Fig. 3b shows that the l), shows similar percentages for both the observations and
proportion of NF decreases by over 10 percentage points if COSMO-REA6overland.Withsimilarprobabilitydistribu-
probabilitiesforallfeaturesandnotonlythemostprobable tions for the mesoscale features for both data sets (Fig. 1),
onearetakenintoaccount.Althoughthisleadstoanincrease it is again apparent that CFC shows a higher percentage in
inallmesoscalefeatures,itisnotbythesameamount.While ACCP. Comparing sea and land grid points (cf. Fig. 3e–h
thefeatureswithoverallhigherprobabilities,namelytheWJ and i–l) finally shows that the CJ and CS occur more often
and CS as shown in Fig. 1, increase by around 10%–30%, and over a wider area over the ocean compared with CFC,
the CJ shows an increase of 73%. The CFC, which shows whichalmostexclusivelyoccursoverland,wherefrictionis
the highest uncertainty, increases by 400%, demonstrating higherandstaticstabilityislowerduringdaytime.Asmen-
the gain due to using the assigned probabilities. Neverthe- tionedbefore,theWJismorecommonoverland,around15
less,CFCisbyfartheleastcommoncauseofhighwinds. percentagepointsmoreprevalentinbothMAXPandACCP.
NeglectingNFinFig.3candddrawsthefocustothera- Finally,Fig.3m–pshowtheproportionsforallgridpoints.
tioofthemesoscalefeaturesthemselves.IntheMAXPper- Note that the number of land grid points is around 35%
spective,theCSandWJarethecauseofhighwindsinover higher than the number of ocean grid points. Overall, al-
50%and36%ofcasesrespectively,whilethemoredamag- mosthalfofwindyconditionsarecausedbytheCS,followed
ing CJ and CFC features(e.g. Hewson and Neu, 2015; Earl bytheWJandCJ,witharound30%and21%respectively.
etal.,2017)onlyshowaproportionof10.1%and1.8%re- Again, for CFC, the difference between MAXP and ACCP
spectively. However, these are also the features with lower showsaconsiderabledifferencefrom1.3%toalmost5%.To
certainty(Fig.1).Hence,fromtheACCPperspective,theCJ examine how robust these numbers are, we computed three
andCFCcometoatotalofaround19%,i.e.anincreaseof subsetsofninerandomlychosenwinterseasons.Thepropor-
around 60%. While the WJ also increases slightly, the pro- tions vary just slightly with an average of around 2% (not
portion of the CS decreases by almost 8 percentage points. shown), as is to be expected considering the small fluctua-
This suggests that the CJ and CFC mostly lose against the tions between winter seasons (see the discussion of Fig. 5
CSwithrespecttobeingthemostprobablefeature. below).
In contrast to the station observations, the proportion of Astheoverallfrequenciesaresimilar,differencesareplau-
NF is considerably lower in COSMO-REA6 data, as seen sibleinbothdatasetsandCOSMO-REA6hastheadvantage
in Fig. 3e and f. This supports the hypothesis that the high ofanhomogeneousfieldwithoutmissingparameters,wefo-
proportion of NF in observations is due to missing values, cusonthegriddeddatasetfromhereon.
as the data are of course complete for all parameters here. Figure4showstheproportionsofeachfeatureforMAXP,
Still, the proportion of NF accounts for around one-quarter analogouslytoFig.3mando(COSMO-REA6all),butonly
toone-thirdofhighwinds.Thisisduetotheseveralreasons including grid points where v˜≥1.2 (panels a and b) and
discussedbelowandinSect.3.3aswellasoverallhigherun- v˜≥1.4 (panels c and d). Note that this is only the case
certainty in uncommon cyclone development, such as dou- for around 1.5% and 0.1% of the previously included data
blefronts.ThereaderisreferredtoSect.7ofPart1(Eisen- pointsrespectively.Consideringonlyv˜≥1.2,theproportion
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 987
Figure3.Relativefrequencyoffeaturesforstationobservations(a–d),COSMO-REA6landgridpoints(e–h),COSMO-REA6oceangrid
points(i–l)andallCOSMO-REA6gridpoints(m–p)forthemostprobablefeature(MAXP;a,e,i,m,c,g,k,o)andaccumulatedprobabilities
(ACCP;b,f,j,n,d,h,l,p).ThefirsttwocolumnsincludeNF,whileitisneglectedinthelattertwoduetoitshighfrequency.
Figure4.AsinFig.3mando(COSMO-REA6all;MAXP)butforgridpointswith(a,b)v˜≥1.2and(c,d)v˜≥1.4.
ofNFdecreasesbyover75%(Fig.4a),whereasitdecreases for v˜≥1.4. Consistent with Earl et al. (2017), CFC shows
to almost 0% if only grid points with v˜≥1.4 are included an even stronger increase with over 300% and over 600%
(Fig.4c).Thissuggeststhathigherwindswithinthevicinity respectively.Theseresultsareconsistentwiththewindchar-
ofacyclonearemostlyassociatedwithoneoftheintroduced acteristics, as will be discussed in Sect. 4. Meanwhile, the
features.WhenNFisneglected,theCSproportionisreduced proportionoftheWJdecreasesbyabout10%,asitusually
by45%–58%(Fig.4b,d);thissuggeststhat,althoughitaf- causes weaker winds compared with the CJ and CFC (e.g.
fects a large area, it is less common for the CS to be the HewsonandNeu,2015;Earletal.,2017).
causeofextremewinds.Incontrast,themoredamagingfea- ThediscussedproportionsinFig.3dependnotonlyonthe
tures (the CJ and CFC) show an increased proportion. The occurrenceofthefeaturebutalsoonitssize.Figure5shows
CJ shows an increase of about 69% for v˜≥1.2 and 111% the seasonal and interannual evolution of stormy time steps
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

988 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
and the occurrence of each respective feature. This is com- (NAO; e.g. Wanner et al., 2001), which describes the large-
putedasthesumofstormytimestepsduringwhichacertain scalecirculationovertheNorthAtlanticandoriginallyrepre-
featureisdetectedtobethemostprobablefeatureinatleast sentsthepressuredifferencebetweenIcelandandtheAzores
100gridpointsovertheinvestigationdomain,normalisedby (Hurrell, 1995). For our study area, slightly positive NAO
thenumberofstormytimesteps.Thus,thismeasureisinde- values facilitate stormy conditions, as the typical cyclone
pendentofthenumberofgridpointsinwhichthefeatureis paths for such NAO conditions correspond to tracks over
identified. the British Isles and the North and the Baltic seas. Accord-
Looking at all stormy time steps of the investigation pe- ingly, most peaks are associated with positive NAO phases.
riod(leftsideofFig.5),itisevidentthatNF(greydot)oc- Furthermore, quieter winter seasons consistent with the lit-
curssomewhereinthedomainforpracticallyeverymoment erature,suchas2010–2011(e.g.Santosetal.,2013;Laurila
in time. The same holds for the CS (orange dot) with only etal.,2021),canbefound.With2009–2010beingaparticu-
marginally lower frequencies. Both the CJ (blue) and WJ larlycoldwinterseason(Wangetal.,2010),theoccurrence
(red) occur in over 80% of stormy time steps, with slightly ofdetectedWJsislowercomparedwithotherwinters,while
highervaluesfortheCJ.Togetherwiththelowerproportion theCJshowsapeak.ThepeaksoftheWJandCFCin2015–
oftheCJcomparedwiththeWJ,asseeninallpanelsofFig.3 2016areconsistentwiththewinterseasonbeingparticularly
exceptpanelsi–l(overtheocean),thissuggeststhattheCJis wetandwarm,asdiscussedinMcCarthyetal.(2016).Again,
onaverageasmallerfeaturethantheWJ.Theleastfrequent NFandtheCSoccurtoofrequentlytodetectaninterannual
feature (with around 43%) is CFC (green), contributing to cycle.Overall,allfeatureshavenocorrelationoraveryweak
thelowproportionsinallpanelsinFig.3. positive correlation with the number of stormy time steps
Withrespecttothemeanseasonalcycle,theblacklinein (0%–10%).ThecoefficientofvarianceislowestfortheCS
themiddlesectionofFig.5showsthatNovemberandMarch andstormytimesteps(with41%)andhighestforCFC(with
| aretheleaststormymonthsduringourinvestigationperiodof |     |     |     |     |     |     | 54%). |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2000to2019withapeakinJanuaryinbetween.Thisiscon- With respect to long-term trends, a slight decline is ev-
sistentwiththecyclonetrackdensityplotsshowninFig.B1. ident, consistent with the overall decrease in the number of
Somewhat surprisingly, October shows the highest number winterstormsinawarmingclimate(Cattoetal.,2019).How-
of stormy time steps of all months. On long-term average, ever,giventhatourinvestigationperiodcoversonly19years,
themajorityofstormsoccurbetweenDecemberandFebru- aMann–Kendalltest(significancelevelof0.05;Hussainand
ary; thus, the 98th percentile of wind speeds is highest for Mahmud, 2019) did not indicate statistical significance in
thatperiodandlowertowardsautumnandspring,consistent anyofthetimeseries.
| with Feser | et al. | (2015) | and Laurila | et  | al. (2021). | However, |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | ----------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
the recent 2 decades shows a larger number of noteworthy 3.2 Earth-relativestatistics
stormsinOctober(e.g.Christianin2013,Xavierin2017and
|                            |        |           |      |                       |        |                | An Earth-relative |          | framework | enables | us to | learn    | which re- |
| -------------------------- | ------ | --------- | ---- | --------------------- | ------ | -------------- | ----------------- | -------- | --------- | ------- | ----- | -------- | --------- |
| Herwartin2017)comparedwith |        |           |      | November,whichleadsto |        |                |                   |          |           |         |       |          |           |
|                            |        |           |      |                       |        |                | gions are         | commonly | affected  | by      | which | feature. | Figure 6  |
| a larger                   | number | of stormy | time | steps                 | in the | 19 years. This |                   |          |           |         |       |          |           |
showsageographicdistributionoftherelativefrequencyof
| difference | might | be further | enhanced |     | by the | slightly lower |     |     |     |     |     |     |     |
| ---------- | ----- | ---------- | -------- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
98th percentile of v in October compared with November. NFandthefourmesoscalewindfeatures(MAXP)aswellas
ofoverallwindyconditions.AnanalogousplotforACCPcan
| The higher | frequency | is  | consistent | with | October | showing a |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ---------- | ---- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
befoundintheAppendixBshowingoverallsimilarproper-
slightlyhighercyclonedensitythanNovember(Fig.B1a,b).
0.5◦×0.5◦
|              |     |                |     |           |     |                 | ties (Fig. | B2). Results | are | displayed | on  |     | boxes, |
| ------------ | --- | -------------- | --- | --------- | --- | --------------- | ---------- | ------------ | --- | --------- | --- | --- | ------ |
| With respect | to  | the individual |     | features, | the | rather rare CFC |            |              |     |           |     |     |        |
therebyaggregatingover16gridpoints.
hasamarkedseasonalcyclewithanapparentpeakinDecem-
v˜
ber and January. The WJ has a smaller relative peak during The number of windy conditions, i.e. exceeding 0.8, in
±15◦
|     |     |     |     |     |     |     | proximity | to the | cyclone | centre | (within | in  | the zonal |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------- | ------ | ------- | --- | --------- |
peakwintermonths.WhiletherelativefrequencyoftheCJis
|     |     |     |     |     |     |     | direction | and −15 | to 5◦ in | the meridional |     | direction) | is dis- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------- | -------------- | --- | ---------- | ------- |
onlyslightlyhigherthanfortheWJ,itsfrequencyincreases
withthewinterpassing,leadingtoamaximumofover90% played in Fig. 6a. This criterion leads to the highest num-
|                        |     |     | ˜                            |     |     |     | bersovertheNorthSea,Denmark,northernGermanyandthe |     |     |     |     |     |     |
| ---------------------- | --- | --- | ---------------------------- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| inMarch.Recallthattheθ |     |     | predictorisanormalisedparam- |     |     |     |                                                   |     |     |     |     |     |     |
BalticSea,i.e.southofthemaximumtrackdensityshownin
| eter, such | that | a cooling | Arctic | with | a progressing | winter |                                                    |     |     |     |     |     |     |
| ---------- | ---- | --------- | ------ | ---- | ------------- | ------ | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |      |           |        |      |               | ˜      | Fig.2.Furthermore,choosingathresholdof80%ofthe98th |     |     |     |     |     |     |
andpossiblymorecold-airoutbreaks,i.e.lowervaluesofθ,
|     |     |     |     |     |     |     | percentile | results | in more | windy | conditions | over | the ocean |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ----- | ---------- | ---- | --------- |
mightleadtohighernumbersofhigh-windeventsbeingal-
locatedtotheCJ–andtotheCS.BothNFandtheCSareso (seeFig.A1);hence,theabsolutefrequenciesofeachfeature
|     |     |     |     |     |     |     | are normalised | by  | the number | of  | exceedances | for | each grid |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ----------- | --- | --------- |
frequentthatanannualcycleisnotevidentinthisanalysis.
|               |           |           |       |          |           |                 | point. Due | to orographic |      | effects | and higher      | noise     | in these |
| ------------- | --------- | --------- | ----- | -------- | --------- | --------------- | ---------- | ------------- | ---- | ------- | --------------- | --------- | -------- |
| Finally,      | the right | section   | of    | Fig. 5   | shows     | the interannual |            |               |      |         |                 |           |          |
|               |           |           |       |          |           |                 | regions,   | we exclude    | grid | points  | above 800m      | (hatching | in       |
| evolution     | of stormy | time      | steps | and wind | features. | Overall,        |            |               |      |         |                 |           |          |
|               |           |           |       |          |           |                 | Fig. 6)    | and the area  | east | of the  | Alps, including |           | Hungary, |
| lower numbers |           | of stormy | time  | steps,   | such      | as 2002–2003,   |            |               |      |         |                 |           |          |
2005–2006,2009–2010,2010–2011and2012–2013arecon- Slovenia and the Balkans. Note that the frequencies of NF,
WJ,CFC,CJandCSaddupto1.
sistentwithnegativevaluesoftheNorthAtlanticOscillation
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 989
Figure 5. Number of stormy time steps (black line and right axis) and number of time steps in which the feature occurs divided by the
numberofstormytimesteps(leftaxis)foralltimesteps(left),eachmonth(middle)andeachwinterseason(right).
Figure6.Relativefrequencyof(a)windyconditions,(b)NF,(c)WJ,(d)CFC,(e)CJand(f)CS.Panels(b)–(f)arenormalisedbypanel(a).
Resultsaredisplayedon0.5 ◦×0.5 ◦ boxes.Hatchingindicatesgridpointswithanaltitudeabove800m(dots)andexcludedareaseastofthe
Alps(lines).
Figure 6b shows that NF is most common, with a rela- andtheCarpathianMountains,leadingtohigherfrequencies
tive frequency of around 50% in the periphery of the area, of NF in these regions. Over western and central Europe,
i.e. north and further south of the most common cyclone highwindsareusuallyclosertothecyclonecentre,suchthat
paths and wind footprints. Although areas of high orogra- they are mostly associated with one of the mesoscale fea-
phy are removed, their effects can still be seen upstream tures.
when the mostly westerly winds encounter mountain barri- The WJ occurs mostly over western Europe with rela-
ers, such as the Scandinavian Mountains, the Western Alps tivefrequenciesofalmost40%anddecreasesoverGermany
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

990 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
| (Fig. 6c)     | downto 20% | over   | Poland.    | Thisis | consistent | with       |     |     |     |     |     |
| ------------- | ---------- | ------ | ---------- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- |
| an occurrence | early      | in the | life cycle | when   | the        | cyclone is |     |     |     |     |     |
stillinthewesternregions.Thehigherfrequencyeastofthe
ScandinavianMountainsshouldbetreatedwithcaution,asit
mightbecausedbyorographysuchastheFöhneffectwhen
acyclonecrossesthemountains.Moreover,aland–seacon-
| trast is visible, | which | is weaker | in  | ACCP | (Fig. | B2). A pos- |     |     |     |     |     |
| ----------------- | ----- | --------- | --- | ---- | ----- | ----------- | --- | --- | --- | --- | --- |
sibleexplanationforthisisthedifferentthermalcharacteris-
| tics of the                                         | land and     | ocean,         | such as | daytime | heating | leading |     |     |     |     |     |
| --------------------------------------------------- | ------------ | -------------- | ------- | ------- | ------- | ------- | --- | --- | --- | --- | --- |
| todifferencesinθ.Hence,ifjusttrainedoverland,RAMEFI | ˜            |                |         |         |         |         |     |     |     |     |     |
| might have                                          | difficulties | distinguishing |         | the     | WJ from | the CS  |     |     |     |     |     |
overseainambiguoussituations.However,lookingatexem-
plarywinterstormcases,wherefeaturesarewelldeveloped,
adifferenceinthedetectionoveroceanandlandgridpoints
isnotevident(Eisensteinetal.,2023b).
| CFC | shows low | frequencies |     | (under | 4%) | for MAXP |     |     |     |     |     |
| --- | --------- | ----------- | --- | ------ | --- | -------- | --- | --- | --- | --- | --- |
(Fig.6d),whilevaluesaretwiceashighforACCP(Fig.B2d)
duetothelowercertaintyofthefeature(Fig.1),asdiscussed
| in Sect. | 3.1. However, | a distinct | land–sea |     | contrast | is visible |     |     |     |     |     |
| -------- | ------------- | ---------- | -------- | --- | -------- | ---------- | --- | --- | --- | --- | --- |
inboth,whereCFCseemstobealmostexclusivelydetected
overland.Thismightbeduetolandeffects,suchasfrictional
convergenceandlandsurfacesbeingheatedupmorestrongly
| than over  | ocean during    | the        | day, leading |             | to the   | destabilisa- |              |            |                |                      |                  |
| ---------- | --------------- | ---------- | ------------ | ----------- | -------- | ------------ | ------------ | ---------- | -------------- | -------------------- | ---------------- |
| tion of    | the atmosphere. | Moreover,  |              | CFC         | develops | slightly     | Figure       | 7.         |                |                      |                  |
|            |                 |            |              |             |          |              |              | Occurrence | of the         | identified mesoscale | wind features    |
| later than | the WJ when     | the        | cold front   | intensifies |          | (Sect. 3.3   |              |            |                |                      |                  |
|            |                 |            |              |             |          |              | (a) relative | to the     | cyclone centre | – including          | NF in grey – and |
| and Fig.   | 7b). Note       | the patchy | behaviour    |             | over     | land, possi- |              |            |                |                      |                  |
(b)relativetothecyclonelifecycle.Thecontoursinpanel(a)show
bly caused by local small-scale effects due to, among other the area with the most feature occurrences, including 25% (filled
things, surface roughness and orography. Distinct maxima contours)and50%(outercontours)ofthedetectedfeatures.Black
circlesshowthedistancetothecyclonecentrein250kmincrements
| are found | east of or | over mountainous |     | regions, |     | such as the |     |     |     |     |     |
| --------- | ---------- | ---------------- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- |
◦
Scottish Highlands and the Scandinavian Mountains. Here, using50 Nasareferencelatitude.
again,resultsgivenbyRAMEFIshouldbetreatedwithcau-
tion.Asorographycaninduceconvection,CFCmightbede-
tectedwithouttheoccurrenceofacoldfrontbutwherehigh 3.3 System-relativestatistics
windspeedsareassociatedwithastrongpressuregradientor
otherfeaturescombinedwithorographicconvection. For the system-relative framework, we concentrate on the
Asexpected,theoccurrenceoftheCJ(Fig.6e)maximises areawithin±15◦ inthezonaldirectionand−15and+5◦ in
in the northern half of the domain, much farther north than themeridionaldirectionofthecyclonecentre.Thistranslates
fortheWJ(Fig.6c),withadistinctfootprintoverthenorth- toaround±1073kminthezonaldirectionat50◦latitudeand
ernBritishIsles,theNorthSeaandtheBalticSea.Overthe 1670and557kminthesouthernandnortherndirectionsre-
BritishIsles,whereintensecyclonesaremorefrequentthan spectively.Figure7showsacompositeoverthe19extended
over the North Sea (not shown), the CJ shows a maximum winterseasonsfrom2000to2019relativetothecyclonecen-
ofover20%.Overall,theCJoccursmainlyovertheseaand tre(Fig.7a)andlifecycle(Fig.7b).
coastalareas(althoughRAMEFIwastrainedoverland). With respect to the mean spatial distribution, the WJ
The CS shows high values in the Bay of Biscay, where mostly occurs within the south-eastern quadrant of a cy-
other features are rarely detected, and a rather abrupt drop clone,consistentwithconceptualmodels(seeFig.1inPart1;
over France in the east (Fig. 6f). Along with the opposite Eisensteinetal.,2022a).AsshowninFig.7a,theWJusually
patterns for the WJ, this suggests a possible false detection hasadistanceof250to1500kmfromthecentre.CFCoccurs
insomecases.Asexplainedabove,wesuspectsomesystem- around3–5◦farthertothewest,i.e.upstreamwithrespectto
aticallydifferentbehaviourbetweenthelandandoceantobe a westerly flow and also slightly shifted to the north, closer
atleastpartlyresponsibleforthis.AsecondpeakintheCS to the cyclone centre. As CFC is a relatively small elon-
canbefoundovereasternEurope,wheremostotherfeatures gatedandnarrowfeature(asisthefrontitself),thelocationis
have already weakened at that late stage in the cyclone life hardertopinpointoversomanycases,andthelocationvaries
cycle.Overall,theCSoccursfurthersouththantheCJand, themostfromcasetocasecomparedwiththeotherfeatures.
thus,fartherawayfromthecyclonecentre. Thus,althoughCFCoverlapswithotherfeaturesstatistically,
|     |     |     |     |     |     |     | this should | usually | not be | the case for individual | cyclones. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------ | ----------------------- | --------- |
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 991
Figure8.AsinFig.7abutfordifferenttimesrelativetothecyclonelifecycle,i.e.timeofmaximumdepth:(a)−24to−22h,(b)−12to
−10h,(c)0to2hand(d)12to14h.
TheCJissituatedsouthtosouth-westofthecyclonecentre clude,consistentwithHewsonandNeu(2015).WhiletheCJ
withsomestatisticaloverlapwithCFC.Itoccursclosertothe occurrencedecreasesfaster,theCSremainsforlonger.Over-
centrethantheCS,whichdominatesthesouth-westquadrant all,50%oftheCJandCSeventsoccurwithin−8and10h
and can have a distance of up to 1500km from the cyclone andwithin−8and14hrespectively.
centre.The25%shadedareaforNFissplitintotwopatches. When combining both composites, we can see how the
ThemajorityofNFisdetectedsouthtosouth-eastofthecy- featuresoccurindifferentlocationsduringthecyclone’slife
clonecentre,mostlycoincidingwiththeWJbutextendingits cycle. This is displayed for four exemplary time slots in
reach to the north and south-west. The northern part of this Fig.8.Ananimationshowingalltimeslotsfrom24hbefore
patchislocatedintheareaofthewarmfrontandispossibly to24hafterthetimeofmaximumdepthcanbeaccessedin
connectedwiththeCCBa,asdiscussedinEarletal.(2017) the Video supplement (Eisenstein et al., 2023b). A total of
andGentileandGray(2023).Asecond,smallerpatchcanbe 24h before the time of maximum depth, only the WJ and
foundtothenorth-westofthecyclonecentre.Inthisregion, CFC appear in the composite: the round maximum of the
theCJusuallyoccursbeforeitiswrappedaroundthecyclone WJlocatedsouthtosouth-eastofthecyclonecentreandthe
centre.AstheCJfollowsthebendingofthefront,thewind CFCwithamorenorth-tosouth-elongatedmaximumcloser
directiondiffersfromtheCJlateron,whenitwrapsaround to the cyclone centre (Fig. 8a). The CJ and CS develop in
the centre, such that RAMEFI does not identify this part of the following hours to the south-west of the cyclone cen-
the CJ. However, high wind speeds in this area are usually tre, while the size of the WJ increases, as shown 12h later
onlycausedbyverystrongCJs,astherelativemovementof (Fig. 8b). The area of CFC also increases, but the increase
theairinthisareaisagainstthecyclonemotion,weakening in width is probably rather due to the variation in location
the Earth-relative wind speed, particularly for fast-moving thananincreaseinsize.Aroundthetimeofmaximumdepth,
weaker cyclones (Eisenstein et al., 2020). As shown in Ap- asshowninFig.8c,theWJareadecreasesandshiftsfarther
pendix B, the relative frequency of the features shows that awayfromthecentreinasouth-easterndirection,nowwitha
NFmostlyoccursinthenorth-easternquadrant,whereother strongerwest–eastorientation.TheCJhasincreasedinsize
features are rare and where windy conditions are less com- and now stretches across both southern quadrants, whereas
mon(Fig.B3). theCSfillsmostofthesouth-easternquadrant.Furthermore,
Figure 7b shows the relative frequency of the four NF covers most of the area overlapping with all other fea-
mesoscalewindfeaturesthroughoutthelifetimeoftheparent tures. As mentioned above, the area north to north-east of
cyclonefrom2dbeforeuntil2dafterthetimeofmaximum the cyclone centre, which does not overlap with any of the
depth,i.e.thedeepestpressureminimumduringacyclone’s mesoscale features, corresponds to the CCBa, as described
life cycle (marked as 0 in Fig. 7b). The WJ is the first fea- in Earl et al. (2017) and Gentile and Gray (2023). A total
ture to develop, with a maximum at −6h. A total of 50% of 12h after time of maximum depth (Fig. 8d), the WJ and
ofthedetectedWJgridpointsoccurbetween−18handthe CFC have mostly vanished, while the CJ and CS are much
timeofmaximumdepth.Withasmalloffsetofaround2–3h, diminishedinsize.
theCFCfollows,consistentwithitsmorewesternlocationin Overall,theseresultsaremostlyconsistentwithidealised
Fig.7a.Thepeakisslightlylowerataround−4h,and50% schematicsandconceptualmodelsintheliterature(e.g.Hew-
ofCFCpointsaredetectedbetween−16and6h.Contraryto sonandNeu,2015,theirFig.1).However,theverylargeset
Hewson and Neu (2015), the CJ develops several hours be- of differing cyclone development information in our com-
fore thetime ofmaximum depth. However,the peaksof CJ prehensive data set is able to show a larger variety. As our
andCSarearoundthetimeofmaximumdepth,eventhough studydomainistoosmalltocoverthewholelifecycleofthe
thepeakofCSislower.TheWJandCFChavealreadybe- investigatedcyclones,especiallytheearlystagesofafeature
gan to decrease at that time, as the warm air begins to oc- mightbemissed,suchthatananalysisoffeaturedurationand
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

992 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
comparisonwiththeliterature(e.g.HewsonandNeu,2015) ocean,thegustfactordifferssignificantlybetweenlandand
isnotmeaningful.Overtheinvestigationdomain,theWJ,CJ sea(Bornetal.,2012),withlessfrictionandothercausesof
and CS have a broadly similar duration, with an average of turbulenceoverthesealeadingtoaweakerincreaseingust
around 20h (not shown). In contrast, the smaller and rarer speedscomparedwithwindspeeds(Fig.B4a,b,c).
CFCappearsforonlyhalfaslong,withanaverageofaround Withrespecttomoistureandcloudvariables,CFCshows
11h(notshown). thehighestvaluesofspecificandrelativehumidity,followed
by the WJ in the warm sector, CJ and CS (Fig. 9d, e).
The CS may also include high winds caused by dry in-
4 Characteristicsofhigh-windfeatures trusions (Raveh-Rubin and Catto, 2019; Catto and Raveh-
Rubin,2019),leadingtooveralldrierconditionsforthisfea-
Using RAMEFI over a 19-year time period also allows us ture. Moreover, especially the SJ, which is included in the
to analyse the distributions of selected meteorological pa- CJ feature here, occurs in the dry-slot area. Following the
rametersforeachfeature,i.e.tocharacterisemeteorological Clausius–Clapeyron relation,it is also intuitivethat warmer
conditions. By construction, the eight parameters used for temperaturesenablehighervaluesofq.Consistently,allfea-
thetrainingofRAMEFI(Sect.2.3)behaveasalreadydocu- tures have lower q values and higher RH values over land.
mented in Part 1; therefore, they are not displayed here and Figure 9f shows the total cloud cover. While stratocumulus
are only briefly discussed. Instead, we concentrate on wind andstratuscloudsarecommoninthewarmsectoraheadof
speed(v)andgusts(v ),thegustfactor(g ),specificand thecoldfront,cloudlessareascanstillbefoundfortheWJin
gust v
relative humidity (q and RH, respectively) and total cloud contrastwithCFC.BoththeCJandCSshowawidedistribu-
cover(cc).Figure9showsboxplotsfortheseparametersfor tion.WhiletheCJappearsatthetipofthecloudhead,partly
allgridpoints,whileadistinctionbetweenlandandseagrid belowandslightlyaheadofit,allowingforbothcloudyand
pointscanbefoundinAppendixB(Fig.B4). cloudless conditions, the CS is often associated with post-
Withrespecttop(notshown),theCJhasthedeepestpres- CFC periods and, thus, conditions comprising a mixture of
sureduetoitslocationclosesttothecyclonecentre,whereas cloudlessskiesandshowers.Attimes,NFisdetectedalong
WJandCSshowhighervalues.IncontrasttoFig.10inPart1 the warm front (Fig. 7), which is characterised by cloudy
(Eisensteinetal.,2022a),theCShasnosecondpeakatlow conditionsbutcanalsoshowlowerccvaluesinotherareas,
p, which was due to the exceptionally deep storm Sabine e.g.inthewarmsector.
(February 2020) included in the training. This is not the
case here, and even if it was included, it would carry much
less weight in a composite of almost 20 years. As it is usu-
ally ahead of the cold front, the WJ shows falling pressure, 5 Conclusions
while pressure rises in the CS and CJ areas. Furthermore,
˜
theWJandCFCshowwarmerθ comparedwithCJandCS Damaging winds accompanying extratropical cyclones can
(notshown).RRvaluesover1mmh−1areonlycommonfor becausedbyseveralmesoscalefeatureswithdifferentchar-
CFC. CFC is characterised by slightly positive (cid:49)d values, acteristicsand,thus,differingforecasterrorsanddamagepo-
whilehardlyanywindshiftisfoundfortheWJ,CJandCS. tentials.Toanalysethesedifferences,wedevelopedanovel,
As seen in Fig. 9a, v is usually highest for the CJ, with objective and flexible probabilistic identification tool called
the median being around 15ms−1 and the 99th percentile RAMEFI (RAndom-forest-based MEsoscale wind Feature
being over 25ms−1, making it the most common cause of Identification), as recently introduced in Part 1 of this work
high winds(e.g. Hewsonand Neu,2015; Gentileand Gray, (Eisenstein et al., 2022a). The method is trained on the ba-
2023). While the CS and WJ show similar 99th percentiles sisofsurfaceobservationsfor12stormcases;however,due
ataround23ms−1,themedianoftheWJataround10ms−1 tospatialindependenceandtheremovaloflocation-specific
isabout3ms−1 lowerthanthemedianoftheCS.NFhasa effects,oncetrained,itcanbeappliedtogriddeddatawith-
slightlyhighermedianthantheCSbutasimilarmeanvalue. outanymodification.Here,RAMEFIisusedtocompilethe
ThelowestvaluesarefoundforCFC,withamedianofunder – to the best of our knowledge – first ever long-term objec-
10ms−1.Naturally,v overtheoceanisconsiderablyhigher tive climatology of the four wind features WJ, CJ, CS and
than over land (Fig. B4), affecting the overall v depending CFCbasedonstationobservationsandahigh-resolutionre-
onhowoftenthefeaturesoccuroverlandorocean(Figs.3e– analysis data set (COSMO-REA6) for a time period of 19
l, 6). v shows similar behaviour for the CJ, CS, WJ and extended winter seasons, i.e. October to March. Using the
gust
NF.However,CFCshowsthesecondhighestgusts,withup reanalysisdataalsoallowsfortheinvestigationofoceangrid
to 35ms−1 (Fig. 9b). This leads to the highest g , which points.Althoughasystematicvalidation,asdoneforlandin
v
simply displays the ratio between v and v, reaching 3 in Part1,isnotperformedforoceanareas,asubjectiveinspec-
gust
thecaseofCFC(Fig.9c).Thisisnotsurprising,asconvec- tionofseveralcasesduringtheanalysedtimeperioddidnot
tion is associated with high instability and turbulence. Al- revealfundamentaldifferences.However,duetothedifferent
thoughbothwindandgustspeedsaremuchhigheroverthe shapeofthewindspeeddistribution,thethresholdofv˜>0.8
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 993
Figure9.Boxplotsofeachfeaturefor(a)v,(b)vgust,(c)gv,(d)q,(e)RHand(f)cc.Broaderboxesshowthe25thto75thpercentile,thinner
boxespresentthe10thto90thpercentile,andwhiskersshowthe1stand99thpercentile.Linesanddotsindicatethemediansandthemeans
respectively.
usedtodefinewindyconditionsresultsinmorefrequentoc- – mostlycloudyconditions,butthewarmsectorallowed
| currenceovertheoceanthanoverland. |          |             |          |         |          |             | forratherhumidconditions. |          |      |            |              |     |         |
| --------------------------------- | -------- | ----------- | -------- | ------- | -------- | ----------- | ------------------------- | -------- | ---- | ---------- | ------------ | --- | ------- |
| The considered                    |          | area        | includes | western | and      | central Eu- |                           |          |      |            |              |     |         |
|                                   |          |             |          |         |          |             | The main                  | findings | with | respect to | cold frontal |     | convec- |
| rope but                          | excludes | grid points | above    | 800m    | altitude | and the     |                           |          |      |            |              |     |         |
tion(CFC)wereasfollows:
| Balkans. | Focusing | on  | grid points | with | windy | conditions |     |     |     |     |     |     |     |
| -------- | -------- | --- | ----------- | ---- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
withinthevicinityofacyclonecentre,i.e.±15◦inthezonal
|     |     |     |     |     |     |     | – associated | with | heavy | precipitation, | a shift | in wind | di- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ----- | -------------- | ------- | ------- | --- |
+5◦
| direction | and −15 | and | in  | the meridional |     | direction, we |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
rectionandcoolingtemperatures;
| determined | the | relative | frequency | of mesoscale |     | wind fea- |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tures in both an Earth-relative and cyclone-relative frame- – anarrowfeaturealongthecoldfront,theleastcommon
work. Furthermore, distinctive characteristics of the wind featureandalocationthatvariesconsiderablyfromcase
| (wind speed, | v;  | gust speed, | v    | ; and gust | factor, | g ) and | tocase; |     |     |     |     |     |     |
| ------------ | --- | ----------- | ---- | ---------- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
|              |     |             | gust |            |         | v       |         |     |     |     |     |     |     |
humidityparameters(specifichumidity,q;relativehumidity,
– occursalmostexclusivelyoverlandwhere,forexample,
| RH; and | cloud | cover, cc) | were | investigated. | The | main find- |     |     |     |     |     |     |     |
| ------- | ----- | ---------- | ---- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
daytimeheatingandfrictionalconvergencecanstrongly
ingsoftheclimatologicalanalysisfortheindividualfeatures
|     |     |     |     |     |     |     | enhance | the | development | of convection |     | along the | cold |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ------------- | --- | --------- | ---- |
arenowoutlined.
Themainfindingswithrespecttothewarmjet(WJ)were front,andisalsodetectedparticularlyaroundmountain-
ousareas(sometimesorographictriggeringindependent
asfollows:
ofcoldfront);
| – characterised                                  |     | by decreasing |     | p, warm | temperatures, | al- |           |        |        |       |          |      |       |
| ------------------------------------------------ | --- | ------------- | --- | ------- | ------------- | --- | --------- | ------ | ------ | ----- | -------- | ---- | ----- |
|                                                  |     |               |     |         |               |     | – highest | g with | rather | low v | and high | v    | up to |
| mostnoprecipitationandmostlysouth-westerlywinds; |     |               |     |         |               |     |           | v      |        |       |          | gust |       |
35ms−1orhigherinextremecases;
– firsttooccurwithinthesouth-easternquadrantofacy-
clone,withapeakaround6hbeforethetimeofmaxi- – highestvaluesofq,RHandccconnectedwithconvec-
tion.
mumdepth;
Themainfindingswithrespecttothecoldjet(CJ)wereas
– detectedmostlyoverlandinmorethan80%ofstormy
follows:
timesteps;
– showsincreasingbutoveralldeepestp,westerlywinds
| – most | common | over | the southern | UK, | France, | Benelux |     |     |     |     |     |     |     |
| ------ | ------ | ---- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
andcoldtemperatures;
statesandGermany;
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

994 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
– more frequent over sea than over land in over 80% of explore the potential of feature-dependent post-processing.
stormytimesteps,mostlyaffectingthenorthernUK,the This will ultimately show whether the differences in stabil-
North and Baltic seas, Scandinavia, and northern Ger- ity,turbulence,andshallowanddeepconvectionbetweenthe
many; featuresdoinfactleadtodifferentphysicalerrorcharacteris-
ticsthatcanbecorrectedstatisticallyinamoretargetedway,
| – smaller | feature | than | the | WJ, occurring |     | close | to the cy- |     |     |     |     |     |
| --------- | ------- | ---- | --- | ------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
helpingtoimprovewindandgustforecastsandwarnings.
clonecentre,firsttothesouth-westandlatertothesouth
ofit;
|     |     |     |     |     |     |     |     | AppendixA: | Winddistribution |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | --- | --- | --- |
– usuallythecauseofthehighestwindsandgusts;
|     |     |     |     |     |     |     |     | In Part 1 | (Eisenstein | et al., | 2022a) of this | work, a threshold |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------- | -------------- | ----------------- |
– cloudyconditionsbelowthecloudheadanddrieratthe
of80%ofthe98thpercentileofhighwindspeedswasintro-
tipofthecloudheadindry-slotregion.
ducedtodefinewindyconditions.WhilethefocusofPart1
| The main | findings |     | with respect | to  | the cold | sector | (CS) |     |     |     |     |     |
| -------- | -------- | --- | ------------ | --- | -------- | ------ | ---- | --- | --- | --- | --- | --- |
wasonstations/gridpointsoverland,wealsoincludeocean
wereasfollows: gridpointsintheclimatology.However,duetovaryingfric-
tion,orographyandheatingofthesurface,amongotherfac-
– associatedwithcoldtemperatures,westerlywinds,and
tors,thewinddistributionovertheoceanhasafundamentally
increasingandhigherpcomparedwiththeCJ;
|     |     |     |     |     |     |     |     | different | form compared | with | that over | land (e.g. Wieringa, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ---- | --------- | -------------------- |
– occurs in almost all winter storms and time steps and 1973;Bornetal.,2012),asdisplayedforexemplarylocations
affectsarelativelylargeareainthesouth-westernquad- inFig.A1.Therighttailofthedistributionshowsconsider-
ablystrongerwinds,leadingtoahighernumberoftimesteps
rantofacyclone;
exceeding80%ofthe98thpercentile.Overall,thethreshold
– lasttodecayand,thus,themostcommoncauseofhigh
|     |     |     |     |     |     |     |     | is exceeded | around | 45% | more often over | the ocean com- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --------------- | -------------- |
windsovereasternEurope; paredwithoverland.Nevertheless,toallowafaircompari-
son,wenormalisetheoccurrencebythenumberoftimesteps
– sunnierconditionswithpatchesofpost-cold-frontcon-
withwindyconditions.
vection;
– overalldrierconditionsduetodryintrusion.
Thelocationsofthefeaturesrelativetothecyclonecentre
foundinthisclimatologyaremostlyconsistentwithconcep-
tualmodelsbasedoncasestudiesorsubjectiveidentification
(seeFig.1ofEisensteinetal.,2022a).Whilepreviouslitera-
turesuggeststhatacycloneisfirstdominatedbytheWJand
| then by     | the CJ      | (e.g. Hewson  |           | and Neu, | 2015;   | Rivière       | et al., |     |     |     |     |     |
| ----------- | ----------- | ------------- | --------- | -------- | ------- | ------------- | ------- | --- | --- | --- | --- | --- |
| 2015), this | climatology |               | further   | revealed | the     | occurrence    | of      |     |     |     |     |     |
| CFC during  | early       | developmental |           | stages   | and     | the dominance |         |     |     |     |     |     |
| of the CS   | in later    | stages.       | Moreover, |          | further | wind          | and hu- |     |     |     |     |     |
midityparametercharacteristicsshowmostlyconsistentbe-
FigureA1.DistributionofvfortwooceangridpointsintheNorth
| haviour | compared | to that | outlined | in  | previous | studies | (e.g. |     |     |     |     |     |
| ------- | -------- | ------- | -------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- |
Atlantic(darkblue)andtheNorthSea(lightblue)andthreeland
| Hewson | and Neu, | 2015; | Earl | et al., | 2017). | The large | num- |     |     |     |     |     |
| ------ | -------- | ----- | ---- | ------- | ------ | --------- | ---- | --- | --- | --- | --- | --- |
gridpointsclosetoBordeaux(darkred),Paris(red)andBerlin(or-
berofstormsinvestigatedhelpedtorevealthelargevariabil-
ange)respectively.Dottedlinesmarkthe98thpercentileanddashed
ity in the location of CFC in a system-relative framework, linesrepresent80%ofthe98thpercentile.
| similar to | the | blurring | of frontal | boundaries |     | in composites |     |     |     |     |     |     |
| ---------- | --- | -------- | ---------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
discussedinDacreetal.(2012).Otherdifferencescompared
| with the | literature | include | the | time of | occurrence | of  | the CJ, |     |     |     |     |     |
| -------- | ---------- | ------- | --- | ------- | ---------- | --- | ------- | --- | --- | --- | --- | --- |
severalhoursbeforethetimeofmaximumdepth,incontrast
| to Hewson        | and | Neu (2015). |           | Overall, | RAMEFI      | allows          | for a  |     |     |     |     |     |
| ---------------- | --- | ----------- | --------- | -------- | ----------- | --------------- | ------ | --- | --- | --- | --- | --- |
| more objective   |     | and more    | thorough  | analysis |             | and description |        |     |     |     |     |     |
| of the mesoscale |     | wind        | features. | This     | climatology |                 | demon- |     |     |     |     |     |
stratestheapplicabilityofRAMEFIforlongertimeperiods
anddatathatitwasnottrainedon.Thenewdatasetcanserve
| the community |     | as a climatological |     | reference |     | for case | stud- |     |     |     |     |     |
| ------------- | --- | ------------------- | --- | --------- | --- | -------- | ----- | --- | --- | --- | --- | --- |
iesorincombinationwithotherobjectiveclimatologies(e.g.
Sprengeretal.,2017).Infuturework,weplantousethiscli-
matologyforafeature-specificforecasterroranalysisandto
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 995
AppendixB: Furtherfigures
FigureB1.AsinFig.2butforeachmonthconsideredintheclimatology.
FigureB2.AsinFig.6butforACCP.
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

996 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
FigureB3.AsinFig.7butdividedbythenumberofwindyconditions.
FigureB4.AsinFig.9butwithland(solidboxplots)andsea(dashedboxplots)gridpointsseparated.
Codeavailability. RAMEFI is available at https://gitlab.physik. Dataavailability. COSMO-REA6 data are available from https:
uni-muenchen.de/Lea.Eisenstein/ramefi (Eisenstein et al., 2022c), //reanalysis.meteo.uni-bonn.de(Hans-Ertel-CentreforWeatherRe-
where it will be updated in future studies, and is archived at search, 2019). The observation data over Europe were provided
https://doi.org/10.5281/zenodo.6541303 (Eisenstein et al., 2022b) by DWD for this work and cannot be made freely available; the
atthetimeofthesubmissionofPart1(Eisensteinetal.,2022a). readerisadvisedtocontacttheDWDdirectlyregardingthesedata
(klima.vertrieb@dwd.de).ValuesoftheNAOphasesareprovided
by the Climate Prediction Center at the National Oceanic Atmo-
sphericAdministration(NOAA,2023).TheoutputofRAMEFIas
wellasfilestofiltertheoutput(asdescribedinSect.2.4)areavail-
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 997
| able at https://doi.org/10.5281/zenodo.8370478 |     |     |     |     | (Eisenstein | et al., | References |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | ----------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
2023a).
|                  |     |       |            |         |           |     | Bjerknes, | J.: On | the | Structure | of                            | Moving | Cyclones, | Mon. |
| ---------------- | --- | ----- | ---------- | ------- | --------- | --- | --------- | ------ | --- | --------- | ----------------------------- | ------ | --------- | ---- |
|                  |     |       |            |         |           |     | Weather   | Rev.,  | 47, | 95–99,    | https://doi.org/10.1175/1520- |        |           |      |
| Videosupplement. | The | video | supplement | showing | exemplary |     |           |        |     |           |                               |        |           |      |
winter storms occurring within our studied time period and 0493(1919)47<95:otsomc>2.0.co;2,1919.
an animation of system-relative occurrences over time rel- Bollmeyer, C., Keller, J. D., Ohlwein, C., Wahl, S., Crewell, S.,
|          |             |            |     |           |          |     | Friederichs, | P., | Hense, | A., Keune, | J., | Kneifel, | S., Pscheidt, | I., |
| -------- | ----------- | ---------- | --- | --------- | -------- | --- | ------------ | --- | ------ | ---------- | --- | -------- | ------------- | --- |
| ative to | the cyclone | life cycle | can | be freely | accessed | at  |              |     |        |            |     |          |               |     |
Redl,S.,andSteinke,S.:Towardsahigh-resolutionregionalre-
https://doi.org/10.5281/zenodo.7729357(Eisensteinetal.,2023b).
analysisfortheEuropeanCORDEXdomain,Q.J.Roy.Meteo-
rol.Soc.,141,1–15,https://doi.org/10.1002/qj.2486,2015.
|                      |     |                                      |     |     |     |     | Born, K., | Ludwig, | P., and | Pinto, | J. G.: | Wind | gust estimation | for |
| -------------------- | --- | ------------------------------------ | --- | --- | --- | --- | --------- | ------- | ------- | ------ | ------ | ---- | --------------- | --- |
| Authorcontributions. |     | LEcompiledandevaluatedtheclimatology |     |     |     |     |           |         |         |        |        |      |                 |     |
Mid-Europeanwinterstorms:Towardsaprobabilisticview,Tel-
andwrotetheoriginalmanuscript.BScomputedthefeatureproba-
|     |     |     |     |     |     |     | lus A, | 64, 17471, | https://doi.org/10.3402/tellusa.v64i0.17471, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------------------------------------------- | --- | --- | --- | --- | --- |
bilitiesandgaveadviceonthestatisticalanalysis.PKdesignedthe
2012.
overallproject,acquiredthefundingandcoordinatedthescientific
|          |         |                   |     |     |            |         | Catto, J. | L.: Extratropical |     | cyclone | classification |     | and its | use, Rev. |
| -------- | ------- | ----------------- | --- | --- | ---------- | ------- | --------- | ----------------- | --- | ------- | -------------- | --- | ------- | --------- |
| work. PK | and JGP | jointly supervise | the | PhD | of LE. All | authors |           |                   |     |         |                |     |         |           |
Geophys.,54,486–520,https://doi.org/10.1002/2016RG000519,
contributedtodiscussionsandtextrevisions.
2016.
|     |     |     |     |     |     |     | Catto, J. | L. and  | Raveh-Rubin, |            | S.: Climatology |      | and dynamics  | of   |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------ | ---------- | --------------- | ---- | ------------- | ---- |
|     |     |     |     |     |     |     | the link  | between | dry          | intrusions | and             | cold | fronts during | win- |
Competinginterests. Atleastoneofthe(co-)authorsisamember ter. Part I: global climatology, Clim. Dynam., 53, 1873–1892,
oftheeditorialboardofWeatherandClimateDynamics.Thepeer-
https://doi.org/10.1007/s00382-019-04745-w,2019.
reviewprocesswasguidedbyanindependenteditor,andtheauthors
Catto,J.L.,Ackerley,D.,Booth,J.F.,Champion,A.J.,Colle,B.A.,
alsohavenoothercompetingintereststodeclare.
Pfahl,S.,Pinto,J.G.,Quinting,J.F.,andSeiler,C.:TheFuture
ofMidlatitudeCyclones,Curr.Clim.ChangeRep.,5,407–420,
https://doi.org/10.1007/s40641-019-00149-4,2019.
| Disclaimer.  | Publisher’s | note:             | Copernicus | Publications |              | remains |           |           |       |         |           |         |               |          |
| ------------ | ----------- | ----------------- | ---------- | ------------ | ------------ | ------- | --------- | --------- | ----- | ------- | --------- | ------- | ------------- | -------- |
|              |             |                   |            |              |              |         | Clark, P. | A. and    | Gray, | S. L.:  | Sting     | jets in | extratropical | cy-      |
| neutral with | regard      | to jurisdictional | claims     | made         | in the text, | pub-    |           |           |       |         |           |         |               |          |
|              |             |                   |            |              |              |         | clones:   | a review, | Q.    | J. Roy. | Meteorol. | Soc.,   | 144,          | 943–969, |
lishedmaps,institutionalaffiliations,oranyothergeographicalrep- https://doi.org/10.1002/qj.3267,2018.
resentationinthispaper.WhileCopernicusPublicationsmakesev- Dacre,H.F.,Hawcroft,M.K.,Stringer,M.A.,andHodges,K.I.:
eryefforttoincludeappropriateplacenames,thefinalresponsibility An Extratropical Cyclone Atlas: A Tool for Illustrating Cy-
lieswiththeauthors.
|     |     |     |     |     |     |     | clone      | Structure | and Evolution |                                    | Characteristics, |     | B. Am. | Meteo- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------- | ---------------------------------- | ---------------- | --- | ------ | ------ |
|     |     |     |     |     |     |     | rol. Soc., | 93,       | 1497–1502,    | https://doi.org/10.1175/BAMS-D-11- |                  |     |        |        |
00164.1,2012.
Acknowledgements. Theresearchleadingtotheresultsinthispa- Dee, D. P., Uppala, S. M., Simmons, A. J., Berrisford, P., Poli,
per has been accomplished within the “Dynamical feature-based P.,Kobayashi,S.,Andrae,U.,Balmaseda,M.A.,Balsamo,G.,
ensemble postprocessing of wind gusts within European winter Bauer,P.,Bechtold,P.,Beljaars,A.C.,vandeBerg,L.,Bidlot,J.,
storms”C5projectofthe“WavestoWeather”TransregionalCol- Bormann,N.,Delsol,C.,Dragani,R.,Fuentes,M.,Geer,A.J.,
laborativeResearchCentre(grantno.SFB/TRR165)fundedbythe Haimberger, L., Healy, S. B., Hersbach, H., Hólm, E. V., Isak-
German Science Foundation (DFG). Joaquim G. Pinto thanks the sen,L.,Kållberg,P.,Köhler,M.,Matricardi,M.,Mcnally,A.P.,
AXA Research Fund for support. The authors are grateful to Se- Monge-Sanz, B. M., Morcrette, J. J., Park, B. K., Peubey, C.,
bastianTrepte(DWD)andOlivierMestre(MétéoFrance)forpro- de Rosnay, P., Tavolato, C., Thépaut, J. N., and Vitart, F.: The
vidingthesurfaceobservationsdataset,toRobertRedl(LMU)for ERA-Interim reanalysis: configuration and performance of the
preprocessingthedata,andtoTing-ChenChen(KIT)forthecom- data assimilation system, Q. J. Roy. Meteorol. Soc., 137, 553–
putation of the cyclone tracks and helpful scripts. Further thanks 597,https://doi.org/10.1002/QJ.828,2011.
gotoSebastianLerch(KIT)formanyusefuldiscussionsandhelp- Doms, G., Förstner, J., Heise, E., Herzog, H.-J., Mironov, D.,
fulcommentsintheframeworkofC5.Theauthorsalsoacknowl- Raschendorfer, M., Reinhardt, T., Ritter, B., Schrodin, R.,
edgeSuzanneL.Grayandananonymousreviewerfortheirvaluable Schulz, J.-P., and Vogel, G.: Consortium for Small-Scale
comments,whichhelpedtoimprovethisarticle. Modelling A Description of the Nonhydrostatic Regional
|     |     |     |     |     |     |     | COSMO-Model |     | Part | II Physical |     | Parameterizations, |     | DWD, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ----------- | --- | ------------------ | --- | ---- |
https://doi.org/10.5676/DWD_pub/nwv/cosmo-doc_6.00_II,
2021.
| Financialsupport. | This | research | has | been | supported | by the |     |     |     |     |     |     |     |     |
| ----------------- | ---- | -------- | --- | ---- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Deutsche Forschungsgemeinschaft (grant no. SFB/TRR 165) and Earl,N.,Dorling,S.,Starks,M.,andFinch,R.:Subsynoptic-scale
theAXAResearchFund. features associated with extreme surface gusts in UK extrat-
|     |     |     |     |     |     |     | ropical | cyclone | events, | Geophys. | Res. | Lett., | 44, | 3932–3940, |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | -------- | ---- | ------ | --- | ---------- |
https://doi.org/10.1002/2017GL073124,2017.
|                  |                                       |     |     |     |     |     | Eckhardt, | S., Stohl, | A., | Wernli, | H., James, | P., | Forster, | C., and |
| ---------------- | ------------------------------------- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | ---------- | --- | -------- | ------- |
| Reviewstatement. | ThispaperwaseditedbyGwendalRivièreand |     |     |     |     |     |           |            |     |         |            |     |          |         |
reviewedbySuzanneL.Grayandoneanonymousreferee. Spichtinger, N.: A 15-year climatology of warm conveyor
|     |     |     |     |     |     |     | belts, | J. Climate, | 17, | 218–237, | https://doi.org/10.1175/1520- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | -------- | ----------------------------- | --- | --- | --- |
0442(2004)017<0218:AYCOWC>2.0.CO;2,2004.
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023

998 L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2
Eisenstein,L.,Pantillon,F.,andKnippertz,P.:Dynamicsofsting-jet mos. Sci., 59, 1041–1061, https://doi.org/10.1175/1520-
stormEgonovercontinentalEurope:Impactofsurfaceproperties 0469(2002)059<1041:NPOTNH>2.0.CO;2,2002.
andmodelresolution,Q.J.Roy.Meteorol.Soc.,146,186–210, Hurrell,J.W.:DecadalTrendsintheNorthAtlanticOscillation:Re-
https://doi.org/10.1002/qj.3666,2020. gional Temperatures and Precipitation, Science, 269, 676–679,
Eisenstein, L., Schulz, B., Quadir, G. A., Pinto, J. G., and Knip- https://doi.org/10.1126/science.269.5224.676,1995.
pertz, P.: Identification of high-wind features within extratrop- Hussain, M. and Mahmud, I.: pyMannKendall: a python package
ical cyclones using a probabilistic random forest – Part 1: fornonparametricMannKendallfamilyoftrendtests,J.Open
Methodandcasestudies,WeatherClim.Dynam.,3,1157–1182, Source Softw., 4, 1556, https://doi.org/10.21105/joss.01556,
https://doi.org/10.5194/wcd-3-1157-2022,2022a. 2019.
Eisenstein, L., Schulz, B., Quadir, G. A., Pinto, J. G., and Laurila,T.K.,Sinclair,V.A.,andGregow,H.:Climatology,vari-
Knippertz, P.: RAMEFI (RAndom-forest based MEsoscale ability,andtrendsinnear-surfacewindspeedsovertheNorthAt-
wind Feature Identification), Zenodo [code and data set], lanticandEuropeduring1979–2018basedonERA5,Int.J.Cli-
https://doi.org/10.5281/zenodo.6541303,2022b. matol.,41,2253–2278,https://doi.org/10.1002/joc.6957,2021.
Eisenstein,L.,Schulz,B.,Qadir,G.A.,Pinto,J.G.,andKnippertz, Madonna, E., Wernli, H., Joos, H., and Martius, O.: Warm Con-
P.: RAMEFI, gitlab [code and data set], https://gitlab.physik. veyorBeltsintheERA-InterimDataset(1979–2010).PartI:Cli-
uni-muenchen.de/Lea.Eisenstein/ramefi (last access: 9 Novem- matologyandPotentialVorticityEvolution,J.Climate,27,3–26,
ber2023),2022c. https://doi.org/10.1175/JCLI-D-12-00720.1,2014.
Eisenstein,L.,Schulz,B.,Pinto,J.G.,andKnippertz,P.:Identifica- Manning,C.,Kendon,E.J.,Fowler,H.J.,Roberts,N.M.,Berthou,
tionofhigh-windfeatureswithinextratropicalcyclonesusinga S.,Suri,D.,andRoberts,M.J.:Extremewindstormsandsting
probabilisticrandomforest–Part2:Climatology–Dataset,Zen- jets in convection-permitting climate simulations over Europe,
odo[dataset],https://doi.org/10.5281/zenodo.8370478,2023a. Clim. Dynam., 58, 2387–2404, https://doi.org/10.1007/s00382-
Eisenstein, L., Schulz, B., Pinto, J. G., and Knippertz, P.: 021-06011-4,2022.
Identification of high-wind features within extratropical cy- McCarthy, M., Spillane, S., Walsh, S., and Kendon, M.:
clones using a probabilistic random forest – Part 2: Cli- The meteorology of the exceptional winter of 2015/2016
matology – Video Supplement, Zenodo [video supplement] across the UK and Ireland, Weather, 71, 305–313,
https://doi.org/10.5281/zenodo.7729357,2023b. https://doi.org/10.1002/wea.2823,2016.
Feser, F., Barcikowska, M., Krueger, O., Schenk, F., Weisse, R., Murray,R.J.andSimmonds,I.:Anumericalschemefortracking
andXia,L.:StorminessovertheNorthAtlanticandnorthwest- cyclonecentresfromdigitaldata.PartI:Developmentandoper-
ernEurope–Areview,Q.J.Roy.Meteorol.Soc.,141,350–382, ationofthescheme,Aust.Meteorol.Mag.,39,155–166,1991.
https://doi.org/10.1002/QJ.2364,2015. Neu,U.,Akperov,M.G.,Bellenbaum,N.,Benestad,R.,Blender,
Fink, A. H., Brücher, T., Ermert, V., Krüger, A., and Pinto, J. G.: R.,Caballero,R.,Cocozza,A.,Dacre,H.F.,Feng,Y.,Fraedrich,
TheEuropeanstormKyrillinJanuary2007:synopticevolution, K., Grieger, J., Gulev, S., Hanley, J., Hewson, T., Inatsu, M.,
meteorological impacts and some considerations with respect Keay, K., Kew, S. F., Kindem, I., Leckebusch, G. C., Liberato,
to climate change, Nat. Hazards Earth Syst. Sci., 9, 405–423, M.L.R.,Lionello,P.,Mokhov,I.I.,Pinto,J.G.,Raible,C.C.,
https://doi.org/10.5194/nhess-9-405-2009,2009. Reale,M.,Rudeva,I.,Schuster,M.,Simmonds,I.,Sinclair,M.,
Gentile,E.S.andGray,S.L.:Attributionofobservedextremema- Sprenger,M.,Tilinina,N.D.,Trigo,I.F.,Ulbrich,S.,Ulbrich,
rinewindspeedsandassociatedhazardstomidlatitudecyclone U.,Wang,X.L.,Wernli,H.,Neu,U.,Akperov,M.G.,Bellen-
conveyor belt jets near the British Isles, Int. J. Climatol., 43, baum,N.,Benestad,R.,Blender,R.,Caballero,R.,Cocozza,A.,
2735–2753,https://doi.org/10.1002/joc.7999,2023. Dacre,H.F.,Feng,Y.,Fraedrich,K.,Grieger,J.,Gulev,S.,Han-
Hans-Ertel-Centre for Weather Research: COSMO Regional ley, J., Hewson, T., Inatsu, M., Keay, K., Kew, S. F., Kindem,
Reanalysis, https://reanalysis.meteo.uni-bonn.de (last access: I.,Leckebusch,G.C.,Liberato,M.L.R.,Lionello,P.,Mokhov,
27April2022),2019. I. I., Pinto, J. G., Raible, C. C., Reale, M., Rudeva, I., Schus-
Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A., ter,M.,Simmonds,I.,Sinclair,M.,Sprenger,M.,Tilinina,N.D.,
Muñoz-Sabater,J.,Nicolas,J.,Peubey,C.,Radu,R.,Schepers, Trigo, I. F., Ulbrich, S., Ulbrich, U., Wang, X. L., and Wernli,
D.,Simmons,A.,Soci,C.,Abdalla,S.,Abellan,X.,Balsamo,G., H.:IMILAST:ACommunityEfforttoIntercompareExtratrop-
Bechtold,P.,Biavati,G.,Bidlot,J.,Bonavita,M.,DeChiara,G., ical Cyclone Detection and Tracking Algorithms, B. Am. Me-
Dahlgren,P.,Dee,D.,Diamantakis,M.,Dragani,R.,Flemming, teorol.Soc.,94,529–547,https://doi.org/10.1175/BAMS-D-11-
J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L., Healy, 00154.1,2013.
S., Hogan, R. J., Hólm, E., Janisková, M., Keeley, S., Laloy- NOAA: Climate Prediction Center – Teleconnection North
aux,P.,Lopez,P.,Lupu,C.,Radnoti,G.,deRosnay,P.,Rozum, Atlantic Oscillation, https://www.cpc.ncep.noaa.gov/products/
I., Vamborg, F., Villaume, S., and Thépaut, J.-N.: The ERA5 precip/CWlink/pna/nao.shtml(lastaccess:9March2023),2023.
global reanalysis, Q. J. Roy. Meteorol. Soc., 146, 1999–2049, Parton, G., Dore, A., and Vaughan, G.: A climatology of mid-
https://doi.org/10.1002/qj.3803,2020. tropospheric mesoscale strong wind events as observed by
Hewson, T. D. and Neu, U.: Cyclones, windstorms the MST radar, Aberystwyth, Meteorol. Appl., 17, 340–354,
and the IMILAST project, Tellus A, 67, 27128, https://doi.org/10.1002/met.203,2010.
https://doi.org/10.3402/tellusa.v67.27128,2015. Pinto, J. G., Spangehl, T., Ulbrich, U., and Speth, P.: Sen-
Hoskins, B. J. and Hodges, K. I.: New Perspectives on sitivities of a cyclone detection and tracking algorithm: in-
the Northern Hemisphere Winter Storm Tracks, J. At- dividual tracks and climatology, Meteorol. Z., 14, 823–838,
https://doi.org/10.1127/0941-2948/2005/0068,2005.
WeatherClim.Dynam.,4,981–999,2023 https://doi.org/10.5194/wcd-4-981-2023

L.Eisensteinetal.:Identificationofhigh-windfeatureswithinextratropicalcyclones–Part2 999
Pinto,J.G.,Zacharias,S.,Fink,A.H.,Leckebusch,G.C.,andUl- Sprenger, M., Fragkoulidis, G., Binder, H., Croci-Maspoli, M.,
brich, U.: Factors contributing to the development of extreme Graf, P., Grams, C. M., Knippertz, P., Madonna, E., Schemm,
North Atlantic cyclones and their relationship with the NAO, S.,Škerlak,B.,andWernli,H.:GlobalClimatologiesofEulerian
Clim.Dynam.,32,711–737,https://doi.org/10.1007/s00382-008- and Lagrangian Flow Features based on ERA-Interim, B. Am.
0396-4,2009. Meteorol.Soc.,98,1739–1748,https://doi.org/10.1175/BAMS-
Raveh-Rubin, S. and Catto, J. L.: Climatology and dynamics of D-15-00299.1,2017.
the link between dry intrusions and cold fronts during win- Tiedtke, M.: A Comprehensive Mass Flux Scheme for Cumulus
ter,PartII:Front-centredperspective,Clim.Dynam.,53,1893– ParametrizationinLarge-ScaleModels,Mon.WeatherRev.,117,
1909,https://doi.org/10.1007/s00382-019-04793-2,2019. 1779–1800,1989.
Rivière,G.,Arbogast,P.,andJoly,A.:Eddykineticenergyredistri- Ulbrich,U.,Leckebusch,G.C.,andPinto,J.G.:Extra-tropicalcy-
butionwithinwindstormsKlausandFriedhelm,Q.J.Roy.Mete- clonesinthepresentandfutureclimate:Areview,in:Theoretical
orol.Soc.,141,925–938,https://doi.org/10.1002/qj.2412,2015. and Applied Climatology, vol. 96, Springer, Vienna, 117–131,
Santos,J.A.,Woollings,T.,andPinto,J.G.:AretheWinters2010 https://doi.org/10.1007/s00704-008-0083-8,2009.
and2012ArchetypesExhibitingExtremeOppositeBehaviorof Wang, C., Liu, H., and Lee, S.-K.: The record-breaking
theNorthAtlanticJetStream?,Mon.WeatherRev.,141,3626– cold temperatures during the winter of 2009/2010 in the
3640,https://doi.org/10.1175/MWR-D-13-00024.1,2013. Northern Hemisphere, Atmos. Sci. Lett., 11, 161–168,
Schulz, J.-P.: Revision of the Turbulent Gust Diagnostics in the https://doi.org/10.1002/asl.278,2010.
COSMO Model, COSMO Newsletter 8, 17–22, http://www. Wanner,H.,Brönnimann,S.,Casty,C.,Gyalistras,D.,Luterbacher,
cosmo-model.org/(lastaccess:9November2023),2008. J.,Schmutz,C.,Stephenson,D.B.,andXoplaki,E.:NorthAt-
Schulz, J.-P. and Heise, E.: A new scheme for diagnosing near- lantic oscillation – Concepts and studies, Surv. Geophys., 22,
surface convective gusts, COSMO Newsletter 3, http://www. 321–381,https://doi.org/10.1023/A:1014217317898,2001.
cosmo-model.org/(lastaccess:9November2023),2003. Wernli, H. and Davies, H. C.: A Lagrangian-based analy-
Shapiro, M. A. and Keyser, D.: Fronts, Jet Streams and the sis of extratropical cyclones. I: The method and some
Tropopause,in:ExtratropicalCyclones:TheErikPalmenmemo- applications, Q. J. Roy. Meteorol. Soc., 123, 467–489,
rial volume, edited by: Newton, C. W. and Holopainen, https://doi.org/10.1256/smsqj.53810,1997.
E. O., American Meteorological Society, 167–191, ISBN 978- Wieringa, J.: Gust factors over open water and built-
9991125718,1990. up country, Bound.-Lay. Meteorol., 3, 424–441,
https://doi.org/10.1007/BF01034986,1973.
https://doi.org/10.5194/wcd-4-981-2023 WeatherClim.Dynam.,4,981–999,2023