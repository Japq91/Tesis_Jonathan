| JULY2018 |     |     |     | LIANG | ET AL. |     |     |     |     |     | 1505 |
| -------- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | ---- |
A Multivariate Empirical Orthogonal Function Method to Construct Nitrate Maps
|     |     |     |     | in the Southern | Ocean |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------- | ----- | --- | --- | --- | --- | --- | --- |
YU-CHIAOLIANG
DepartmentofEarthSystemScience,UniversityofCalifornia,Irvine,Irvine,California
MATTHEWR.MAZLOFFANDISABELLAROSSO
ScrippsInstitutionofOceanography,UniversityofCalifornia,SanDiego,LaJolla,California
SHIH-WEIFANGANDJIN-YIYU
DepartmentofEarthSystemScience,UniversityofCalifornia,Irvine,Irvine,California
(Manuscriptreceived7February2018,infinalform30April2018)
ABSTRACT
TheabilitytoconstructnitratemapsintheSouthernOcean(SO)fromsparseobservationsisimportantfor
marinebiogeochemistryresearch,asitoffersageographicalestimateofbiologicalproductivity.Thegoalof
thisstudyistoinfertheskillofconstructedSOnitratemapsusingvaryingdatasamplingstrategies.The
mappingmethodusesmultivariateempiricalorthogonalfunctions(MEOFs)constructedfromnitrate,sa-
linity,andpotentialtemperature(N-S-T)fieldsfromabiogeochemicalgeneralcirculationmodelsimulation
SyntheticN-S-TdatasetsarecreatedbysamplingmodeledN-S-Tfieldsinspecificregions,determinedeither
byrandomselectionorbyselectingregionsoveracertainthresholdofnitratetemporalvariances.Thefirst
500MEOFmodes,determinedbytheircapabilitytoreconstructtheoriginalN-S-Tfields,areprojectedonto
these synthetic N-S-T data to construct time-varying nitrate maps. Normalized root-mean-square errors
(NRMSEs)arecalculatedbetweentheconstructednitratemapsandtheoriginalmodeledfieldsfordifferent
samplingstrategies.Thesamplingstrategyaccordingtonitratevariancesisshowntoyieldmapswithlower
NRMSEsthanmappingadoptingrandomsampling.A k-meansclustermethodthatconsidersthe N-S-T
combinedvariancestoidentifykeyregionstoinsertdataismosteffectiveinreducingthemappingerrors.
Thesefindingsarefurtherquantifiedbyaseriesofmappingerroranalysesthatalsoaddressthesignificanceof
data sampling density. The results provide a sampling framework to prioritize the deployment of bio-
geochemicalArgofloatsforconstructingnitratemaps.
1. Introduction indicator of the net community production (Arrigo
2005;Munroetal.2015;Plantetal.2016;Johnsonetal.
2
| Nitrate, | mostly in its dissolved |     | form NO | , is an es- |                                                  |     |     |     |     |     |     |
| -------- | ----------------------- | --- | ------- | ----------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|          |                         |     |         | 3           | 2017).Johnsonetal.(2017)estimatedthattheannually |     |     |     |     |     |     |
sentialelementforsupplyingandsustainingmarinebi-
|     |     |     |     |     | averaged | net community |     | production | in  | the Southern |     |
| --- | --- | --- | --- | --- | -------- | ------------- | --- | ---------- | --- | ------------ | --- |
ologicalproductivityintheglobaloceans(Mooreetal.
21,
|                    |                   |           |       |             | Ocean (SO) | is 1.3     | PgCyr  | which         | accounts | for         | about |
| ------------------ | ----------------- | --------- | ----- | ----------- | ---------- | ---------- | ------ | ------------- | -------- | ----------- | ----- |
| 2013). The         | amount of nitrate | serves    | as an | important   |            |            |        |               |          |             |       |
|                    |                   |           |       |             | 13% of     | the global | annual | net community |          | production. |       |
| limiting nutrient, | alteringthe       | structure | and   | function of |            |            |        |               |          |             |       |
Therefore,constructingcomprehensive,accuratenitrate
| phytoplankton | communities | (Dugdale | and | Goering |     |     |     |     |     |     |     |
| ------------- | ----------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
mapsoffersgeographicalestimatesofbioproductivityto
1967;Churchetal.2000;Mooreetal.2013);andstudies
|                             |     |               |     |        | help understand | the | marine | biogeochemical |     | state | and |
| --------------------------- | --- | ------------- | --- | ------ | --------------- | --- | ------ | -------------- | --- | ----- | --- |
| havebeensuggestedtoregulate |     | thestrengthof |     | thebi- |                 |     |        |                |     |       |     |
subsequentimpactsonglobalclimate.
| ological pump | (Elderfield | 2006, | chapter | 6; Ducklow |     |     |     |     |     |     |     |
| ------------- | ----------- | ----- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
IntheSO,thelarge-scalenitratedistributionislargely
| et al. 2001;  | Ardyna et al.  | 2017), which | is a      | pivotal part |                     |              |        |           |             |           |      |
| ------------- | -------------- | ------------ | --------- | ------------ | ------------------- | ------------ | ------ | --------- | ----------- | --------- | ---- |
|               |                |              |           |              | determined          | by lateral   | and    | vertical  | transport   | processes |      |
| of the global | biogeochemical | cycles       | (Deppeler | and          |                     |              |        |           |             |           |      |
|               |                |              |           |              | (WilliamsandFollows |              | 2003). | Letscher  | etal.(2016) |           | es-  |
| Davidson      | 2017 Nitrate   | drawdown     | is also   | a good       |                     |              |        |           |             |           |      |
|               |                |              |           |              | timated             | that 17%–20% | of     | the total | nitrate     | in the    | low- |
latitudeSOregionsistransportedbynutrient-richwater
Correspondingauthor:Yu-ChiaoLiang,yuchiaol@uci.edu masses from high latitudes. Verdy and Mazloff (2017)
DOI:10.1175/JTECH-D-18-0018.1
(cid:1)2018AmericanMeteorologicalSociety.Forinformationregardingreuseofthiscontentandgeneralcopyrightinformation,consulttheAMSCopyright
Policy(www.ametsoc.org/PUBSReuseLicenses).

1506 JOURNAL OF ATMOSPHERIC AND OCEANIC TECHNOLOGY VOLUME35
recently made a consistent transport estimate using an (De Mey and Robinson 1987; Fukumori and Wunsch
SObiogeochemicalstateestimate.Otherstudies,based 1991), and reconstruct sea surface temperatures with
on in situ observations, found that the Antarctic Cir- the assistance of chlorophyll-a and wind fields from
cumpolar Current can carry a great amount of nitrate satellite observations (Alvera-Azcárate et al. 2007).
into downstream areas to cause abrupt phytoplankton However, the applicability of the MEOF method
blooms (Hoppe et al. 2015). As for vertical nitrate for constructing SO nitrate maps has not yet been
transport,thebiologicalpumpmechanismiscapableof investigated.
exchanging nitrate between the surface and interior Furthermore,samplingstrategiesdeterminingobser-
ocean (Williams and Follows 2003; Elderfield 2006, vational requirements to construct maps target spatial
chapter 6). Because advective transport processes also correlation structure, but they often neglect the fact
redistributeotherproperties(e.g.,salinityandpotential that temporal variance is extremely heterogeneous
temperature),thereexistcertainlarge-scalecorrespon- (Dormann et al. 2007; Wang et al. 2012). The im-
dencesbetweenthesepropertiesandnitratefields,such plementation of the MEOF method considering both
as the nitrate–potential temperature relationship iden- the spatial and temporal information may allow im-
tifiedbyIshizuandRichards(2013).Thesespatialcor- proved mapping of nitrate. The goal of this study is to
respondences shed light on the possibility to inform applytheMEOFmethodtoconstructSOnitratemaps
SO nitrate information with the assistance of other andtoassessoptimaldatasamplingstrategiesaddress-
tracerfields. ingbothsignalstructureandamplitude.
ThemajorchallengeofconstructingSOnitratemaps In section 2 we describe the biogeochemical general
is the scarcity of in situ measurements. However, the circulation model used in this study that provides
situationisimproving.TheSouthernOceanCarbonand the reference nitrate–salinity–potential temperature
Climate Observations and Modeling (SOCCOM) pro- (N-S-T)fieldsforthemappingtaskandfurtheranalyses.
gram recently reported that 31 profiling floats carrying The basics of the MEOF calculations and k-means
nitrate sensors have successfully transmitted 40 com- cluster method are also introduced. Section 3 presents
plete nitrate annual cycles (Johnson et al. 2017), and theprocedureandexplainshowwesampleN-S-Tdata
additional float deployments are being carried out. andconstructSOnitratemaps,accompaniedwithase-
Multiplemethodsandtechniqueshavebeendeveloped riesofmappingerrorandsamplingdensityanalyses.In
to reconstruct fields in regions with sparse observa- section4wediscusstheresultsandcaveatsinthecontext
tional data, such as optimal interpolation (Reynolds ofprioritizingdeploymentofinsitumeasurements,such
and Smith 1994; Schneider 2001), model-based gap- asbiogeochemicalArgofloats,tobestinformmapping
fillingtechniques(e.g.,dataassimilation;Stammeretal. ofSOnitrate.
2002;WunschandHeimbach2007;Mazloffetal.2010;
Verdy and Mazloff 2017), and empirical orthogonal
function(EOF)-basedmethods(e.g.,Smithetal.1996; 2. Modelandmethodology
Kaplan et al. 1997; Beckers and Rixen 2003; Alvera-
a. Biogeochemicalgeneralcirculationmodel
Azcárateetal.2005;KondrashovandGhil2006;Alvera-
Azcárate et al. 2007; Alvera-Azcárate et al. 2011; Thebiogeochemicalgeneralcirculationmodel(GCM)
Nikolaidisetal.2014;Alvera-Azcárateetal.2016).The used in this study to provide the reference nitrate, sa-
EOF-based methods, in particular, show advantages linity, and potential temperature (temperature herein-
overtheothermethodsintermsofeaseofimplementation after)fieldsistheMITgcm(Marshalletal.1997)coupled
and accuracy relative to computational costs (Alvera- to the modified Biogeochemistry with Light, Iron,
Azcárateetal.2005). Nutrients, and Gas (BLING) model (Galbraith et al.
ThemultivariateEOF(MEOF)method,avariantof 2010).Aseaicecomponentisalsoincluded(Loschetal.
thearchetypalEOFmethod,hasbeenwidelyusedfor 2010). This biogeochemical GCM setup has been ap-
investigating large-scale atmospheric and oceanic plied to estimate SO dynamical and biogeochemical
coupled variability structures because of its salient states(VerdyandMazloff2017).Themodeldomainis
ability to incorporate different variables with their 788–308S at 1/38 resolution with a Mercator projection,
combinedvariances(Xueetal.2000;Sparnocchiaetal. andthentheresolutiontelescopestoacoarserresolution
2003; Wheeler and Hendon 2004, Alvera-Azcárate from308Stotheequator.Theverticalz-coordinategrid
etal.2007).TheMEOFmethodhasalsobeenapplied has52layerswithvariedthicknessfromabout4matthe
to reconstruct maps with the assistance of several re- surface to 400m at depth. The bathymetry is derived
latedfields.Forexample,theMEOFmethodhasbeen fromETOP01(AmanteandEakins2009).Forthiswork
used to synthesize temperature–salinity information we consider an analysis domain spanning 64.88–30.48S,

| JULY2018      |     |           |     |               |     | LIANG     | ET AL. |     |     |     |     |     | 1507 |
| ------------- | --- | --------- | --- | ------------- | --- | --------- | ------ | --- | --- | --- | --- | --- | ---- |
|               |     |           |     |               |     |           |        | 2   |     |     |     | 3   |      |
| and subsample |     | the model | on  | a Mercator    |     | grid with | 28     |     |     | ... | ... |     |      |
|               |     |           |     |               |     |           |        |     | N N |     | N   |     |      |
|               |     |           |     |               |     | 1:18      |        | 6   | 1,1 | 1,2 | 1,n | 7   |      |
| resolution    | in  | longitude | and | approximately |     | in lati-  |        | 6   | .   | .   | .   | 7   |      |
|               |     |           |     |               |     |           |        | 6   | .   | .   | .   | 7   |      |
tude.Thesamplespacingrangesfrom96kmat64:88Sto 6 . . ... ... . 7
| 190kmat30:48S.                                  |     |     |            |     |         |          |     | 6   |         | ... | ...   | 7   |     |
| ----------------------------------------------- | --- | --- | ---------- | --- | ------- | -------- | --- | --- | ------- | --- | ----- | --- | --- |
|                                                 |     |     |            |     |         |          |     | 6N  | N       |     | N     | 7   |     |
|                                                 |     |     |            |     |         |          |     | 6   | m,1 m,2 |     | m,n7  |     |     |
| The biogeochemical                              |     |     | component, |     | adapted | from the |     | 6   |         |     |       | 7   |     |
|                                                 |     |     |            |     |         |          |     | 6   | S S     | ... | ... S | 7   |     |
|                                                 |     |     |            |     |         |          |     | 6   | 1,1 1,2 |     | 1,n   | 7   |     |
| originalBLINGmodel(Galbraithetal.2010),includes |     |     |            |     |         |          |     | 6   | .       | .   | .     | 7   |     |
|                                                 |     |     |            |     |         |          |     | 6   | .       | .   | .     | 7   |     |
nitrogen cycling and phytoplankton dynamics (Verdy 6 . . ... ... . 7 ,
| andMazloff2017).Evolutionsandinteractionsofeight |         |        |                   |     |     |          |     | 6   |         |     |       | 7   |     |
| ------------------------------------------------ | ------- | ------ | ----------------- | --- | --- | -------- | --- | --- | ------- | --- | ----- | --- | --- |
|                                                  |         |        |                   |     |     |          |     | 6S  | S       | ... | ... S | 7   |     |
|                                                  |         |        |                   |     |     |          |     | 6   | m,1 m,2 |     | m,n   | 7   |     |
| prognostic                                       | tracers | [i.e., | inorganic/organic |     |     | forms of |     | 6   |         |     |       | 7   |     |
|                                                  |         |        |                   |     |     |          |     | 6   | T T     | ... | ... T | 7   |     |
nitrogen and phosphorus, dissolved inorganic carbon 6 1,1 1,2 1,n 7
|     |     |     |     |     |     |     |     | 6   |     |     |     | 7   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 6   | . . | . . | . . | 7   |     |
(DIC), alkalinity, oxygen, and iron] are calculated in . . ... ... .
|            |          |               |            |     |                |         |       | 4            |         |          |           | 5   |           |
| ---------- | -------- | ------------- | ---------- | --- | -------------- | ------- | ----- | ------------ | ------- | -------- | --------- | --- | --------- |
| the model, |          | representing  | important  |     | biogeochemical |         |       |              |         |          |           |     |           |
|            |          |               |            |     |                |         |       |              | T T     | ...      | ... T     |     |           |
|            |          |               |            |     |                |         |       |              | m,1 m,2 |          | m,n       |     |           |
| processes, | such     | as the        | conversion |     | between        | DIC and |       |              |         |          |           |     |           |
| organic    | matters, | phytoplankton |            |     | evolution,     | and net |       |              |         |          |           |     |           |
|            |          |               |            |     |                |         | where | m represents |         | the grid | points of | the | reference |
communityproduction(VerdyandMazloff2017;Rosso N-S-Tfieldswithlandpointscropped;nisthetotaltime
etal.2017).
|                                               |      |             |     |          |             |             | steps;  | and the | superscript | T denotes    | transpose |                | of the |
| --------------------------------------------- | ---- | ----------- | --- | -------- | ----------- | ----------- | ------- | ------- | ----------- | ------------ | --------- | -------------- | ------ |
| A number                                      |      | of datasets | are | utilized | to initiate | and to      |         |         |             |              |           |                |        |
|                                               |      |             |     |          |             |             | matrix. | Then    | we perform  | the singular |           | value decompo- |        |
| forcethebiogeochemicalGCM.Theatmosphericstate |      |             |     |          |             |             |         |         |             | X            |           |                |        |
|                                               |      |             |     |          |             |             | sition  | (SVD)   | method      | on to        | isolate   | the spatial    | and    |
| is obtained                                   | from | ERA-Interim |     | products |             | (Dee et al. |         |         |             |              |           |                |        |
temporalMEOFinformationinUandV
| 2011). The | initial | biogeochemical |     |     | tracer fields | are de- |     |     |     |     |     |     |     |
| ---------- | ------- | -------------- | --- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
rived from the Global Ocean Data Analysis Project, UDVT5X, (1)
| version | 2 (GLODAPv2), |     | climatology |     | (Lauvset | et al. |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ----------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
whereDisadiagonalmatrix,inwhichthediagonalel-
2016;Keyetal.2015);theWorldOceanAtlas2013cli-
matologies(Garciaetal.2013a,b);andacoupledmodel ements(i.e.,D )representtheeigenvaluesaccordingto
ii
|            |      |        |         |     |               |       | the rank | in  | amplitude | (from largest | to  | smallest). | We  |
| ---------- | ---- | ------ | ------- | --- | ------------- | ----- | -------- | --- | --------- | ------------- | --- | ---------- | --- |
| simulation | with | BLING, | version | 2   | (E. Galbraith | 2013, |          |     |           |               |     |            |     |
personal communication). The river and Antarctic determine the MEOF mode (spatial pattern) and its
|            |           |     |             |               |      |             | principal | component  |     | (PC; time | information)  |     | from the  |
| ---------- | --------- | --- | ----------- | ------------- | ---- | ----------- | --------- | ---------- | --- | --------- | ------------- | --- | --------- |
| freshwater | discharge |     | are derived |               | from | continental |           |            |     |           |               |     |           |
|            |           |     |             |               |      |             | vector    | components | in  | U and V,  | respectively, |     | according |
| freshwater | products  | of  | Dai         | and Trenberth |      | (2002) and  |           |            |     |           |               |     |           |
totheamplitudeoftheircorrespondingeigenvaluesThe
| Hammond | and | Jones | (2016). | The | model | is run for |     |     |     |     |     |     |     |
| ------- | --- | ----- | ------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
percentageofvarianceaccountedforbytheithMEOF
130yearswithatimestepof1hbyloopingthe2005–14
modeiscalculatedas
| forcing | conditions. | The | N-S-T | fields | in the | latter 60-yr |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ----- | ------ | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
period (i.e., model years 71–130) are used in our ana- D2/trace(DDT)3100%,
(2)
| lyses. Monthly |     | averaged | fields | are | output | for di- |     |     | ii  |     |     |     |     |
| -------------- | --- | -------- | ------ | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
agnostics.WeuseonlytheN-S-Tfieldsat100-mdepth, wheretrace(DDT)isthesumofalldiagonalelementsin
whichisapproximatelytheaveragedepthofnutrocline DDT.Aswehave720timerecords,weobtain720MEOF
in the SO (not shown). The simulated N-S-T fields are modes. We examine the spatial characteristics of the
usedasthereferenceN-S-Tfieldsinthefollowingana- leadingMEOFmodesinsection3.Aschematicchartto
lyses. The N-S-T anomaly fields are calculated by sub- clarifythedetailsoftheMEOFcalculationisshownin
| tractingthemonthlymeanfieldsoverthe60-yranalysis |      |              |     |               |     |          | Fig.1(step1). |     |     |     |     |     |     |
| ------------------------------------------------ | ---- | ------------ | --- | ------------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- |
| period,                                          | thus | representing |     | the departure |     | from the |               |     |     |     |     |     |     |
c. k-meansclustermethod
| seasonal | cycle. |     |     |     |     |     |     |         |         |        |             |     |           |
| -------- | ------ | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ----------- | --- | --------- |
|          |        |     |     |     |     |     | The | k-means | cluster | method | is designed | to  | partition |
b. MEOFmethod
|     |     |     |     |     |     |     | one or | multiple | datasets | into k | clusters | in which | each |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | ------ | -------- | -------- | ---- |
In this study we adopt the MEOF approach to con- datum is assigned to a certain cluster according to the
nearestmean(HartiganandWong1979).Formally,its
| struct SO | nitrate | maps | and | consider | sets | of synthetic |     |     |     |     |     |     |     |
| --------- | ------- | ---- | --- | -------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
N-S-T data in order to evaluate the method and sam- algorithmaimstominimizethesumofsquareddistances
pling strategy. Here we briefly summarize the pro- between the data and the mean within each cluster
cedures of the MEOF calculation. First, the N-S-T (Forgy 1965; MacQueen 1967; Hartigan and Wong
anomaly fields are divided by their total (spatial and 1979),whichcanbeformulatedas
| temporal)standarddeviations[s |     |     |     | 50:00107(molN2m |     | 22), |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|                               |     |     |     | N               |     |      |     |     |     | k   |     |     |     |
s 50:0984 (psu), s 50:405 (8C)] and transformed into (cid:1) (cid:1)kx2mk2,
| S                     |     | T   |     |     |     |     |     |     | argmin |        |     |     | (3) |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- |
| adatamatrixXoftheform |     |     |     |     |     |     |     |     | S      | i51x2S | i   |     |     |
i

| 1508 |     | JOURNAL | OF  | ATMOSPHERIC |     | AND OCEANIC | TECHNOLOGY |     |     | VOLUME35 |     |
| ---- | --- | ------- | --- | ----------- | --- | ----------- | ---------- | --- | --- | -------- | --- |
FIG.1.SchematicoftheMEOFmodecalculation,samplingprocesses,andmapconstructionusedinthisstudy.
wherexisthedataandm isthemeanofdataincluster and M represents the number of variables (three: ni-
i
S.Becauseofitseaseofimplementationandrelatively trate, salinity, and temperature). The array is then
i
clusteredwithanagglomerativehierarchicalclustering
| smaller | computation | and | storage | costs compared |     | to  |     |     |     |     |     |
| ------- | ----------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
other clustering methods (Hartigan and Wong 1979; model (Hartigan and Wong 1979). We set the cluster
|         |           |            |         |         |        | number as | five, meaning | five clusters |     | or groups | are |
| ------- | --------- | ---------- | ------- | ------- | ------ | --------- | ------------- | ------------- | --- | --------- | --- |
| Firdaus | and Uddin | 2015), the | k-means | cluster | method |           |               |               |     |           |     |
has served as a prototype of unsupervised learning al- determinedbasedontheN-S-Tvariances.Themodelis
gorithms and has been successfully applied to many iterated until it reaches a convergence criterion of
relativetolerancelessthan0.0001[definedwithregard
| problems | associated | with categorization |     | or  | regression |     |     |     |     |     |     |
| -------- | ---------- | ------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(Shirkhorshidi et al. 2014). In marine biogeochemical to the magnitude calculated in Eq. (3)], or 300 maxi-
|     |     |     |     |     |     | mum iteration | steps. The | k-means | algorithm |     | is per- |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | ------- | --------- | --- | ------- |
studies,ithasbeenusedtoexplorecommonfeaturesor
relationships between different fields in regional and formed10times,andthebestresultintermsofsmallest
global oceans (e.g., D’Ortenzio and Ribera d’Alcalà relative tolerance is selected as the final clusters. The
|     |     |     |     |     |     | resulting | five clusters divide | the | SO domain | into | five |
| --- | --- | --- | --- | --- | --- | --------- | -------------------- | --- | --------- | ---- | ---- |
2009;D’Ortenzioetal.2012;Lacouretal.2015;Mayot
et al. 2016; Ardyna et al. 2017). For example, Ardyna subregions, which are used to determine the k-means
|                   |      | k-means       |               |         |        | samplingstrategyinlateranalysesandarediscussedin |     |     |     |     |     |
| ----------------- | ---- | ------------- | ------------- | ------- | ------ | ------------------------------------------------ | --- | --- | --- | --- | --- |
| et al. (2017)     | used | the           |               | cluster | method | on                                               |     |     |     |     |     |
| satellite-derived |      | chlorophyll-a | concentration |         | data   | to section3.                                     |     |     |     |     |     |
define bioregions in the SO, each of which contains After five SO subregions are determined by the
k-meansclustermethod,weperformtheKruskal–Wallis
uniquebiogeochemicalphenology.
Inthisstudyweusethek-meansclusterfromaPython Htest(KruskalandWallis1952),withanullhypothesis
machine learning package, called scikit-learn, v0.19.0 thatassumesthemediansofeachgrouparethesame,to
(Pedregosaetal.2011,alsoseedetailsonthescikit-learn informwhethertheseregionsaresignificantlydifferent
official website: http://scikit-learn.org/stable/modules/ in their N-S-T mean variance fields. Significant results
generated/sklearn.cluster.KMeans.html). We take log are found, as all p values are far less than 0.0001, in-
withbase10ontheN-S-Tvariances(seeFigs.2d–f)and dicating at least one region differs from all others in
organizethemintoanarray[i.e.,xinEq.(3)]withsize termsofN-S-Tmeanvariances.Themeanvariancesfor
N3M,whereNisthegridsizeoftheSOdomain(4857)
eachregionaresummarizedinTable1.

| JULY2018 |     | LIANG | ET AL. |     |     |     | 1509 |
| -------- | --- | ----- | ------ | --- | --- | --- | ---- |
FIG.2.Themapsofthemean(a)nitrate,(b)salinity,and(c)potentialtemperaturefieldsat100mfromthebiogeochemicalGCM.
(d)–(f)Asin(a)–(c),butforvarianceinlog scale.Ineachpaneltheblackcurvecirclinglow-latitudeoceansrepresentstheSubantarctic
10
FrontaccordingtoOrsietal.1995.
3. ConstructionofSOnitratemaps characterizedbyanevidentnorth–southstructurewith
highvalueslocatedsouthoftheSubantarcticFront(the
a. MEOFanalysis
|     |     |     | black curve | in Fig. 2) | and low values | to the | north. |
| --- | --- | --- | ----------- | ---------- | -------------- | ------ | ------ |
We perform the MEOF analysis on the reference Similargeographicalfeaturescanbeseenintheannual
N-S-T fields simulated by the biogeochemical GCM meansalinityandtemperaturefieldsbutwithlowand
over the 60-yr period (i.e., model years 71–130; see high values reversed with latitudes (Figs. 2b,c). The
section2afordetails)toconstructSOnitratemaps.We spatialcorrespondencesbetweenmeanN-S-Tfieldsin
first investigate the mean and variance characteristics theSOreflectthefactthattheyarelargelydetermined
of the reference N-S-T fields. Figures 2a–2c show the by similar large-scale physical processes. It is also
N-S-TmeanvaluesintheSO.Themeannitratefieldis notedthattheirmeridionalgradients(i.e.,north–south
TABLE1.Geographicinformation,N-S-Tvariances,andNRMSEreductionrateofeachK-region.
|     | K1  | K2  | K3  | K4  | K5  | Randomselection |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- |
GridNo.a
|     | 430 | 987 | 1337 | 1135 | 968 |     | —   |
| --- | --- | --- | ---- | ---- | --- | --- | --- |
Area(km2)
|     | 12264539 | 27441742 | 18734790 | 15978503 | 23490489 |     | —   |
| --- | -------- | -------- | -------- | -------- | -------- | --- | --- |
Nmeanvariance(molN2m23) 3:8931026 1:5331026 2:6131026 1:3231026 6:5131027
—
|                    | 7:2131022 | 2:0231022 | 3:2831023 | 1:8331023 | 7:0231023 |           |     |
| ------------------ | --------- | --------- | --------- | --------- | --------- | --------- | --- |
| Smeanvariance(psu) |           |           |           |           |           |           | —   |
| Tmeanvariance(8C)  |           | 3:0831021 | 1:2931021 | 6:1231021 | 1:0531021 |           |     |
|                    | 1.11      |           |           |           |           |           | —   |
|                    | 5.2831024 | 2.1931024 | 1.7131024 | 8.8931025 | 8.8931025 | 1.8231024 |     |
NNRMSEreductionrate
|     | 8.2131024 | 2.4231024 | 9.9931025 | 5.6931025 | 8.5531025 | 1.9831024 |     |
| --- | --------- | --------- | --------- | --------- | --------- | --------- | --- |
SNRMSEreductionrate
|     | 7.8931024 | 2.2331024 | 1.0931024 | 6.0031025 | 7.9831025 | 1.9931024 |     |
| --- | --------- | --------- | --------- | --------- | --------- | --------- | --- |
TNRMSEreductionrate
aOnegridcellcoversapproximately28(longitude)31.18(latitude)’27192km2.

1510 JOURNAL OF ATMOSPHERIC AND OCEANIC TECHNOLOGY VOLUME35
FIG.3.ThefirstfiveleadingMEOFmodes.(toptobottom)ThemapsarethespatialpatternsoftheMEOFmodesassociatedwith(top)
nitrate, (middle) salinity, and (bottom) temperature fields. The green boxes (658–508S, 1508–808W) in the first column denote the
Bellingshausen–AmundsenSearegions.TheblackcurveisasinFig.2.
changes)arenotuniformthroughoutthelatitudes,but explains a large portion of the N-S-T variability in the
theyappearsharperinthe508–608Slatitudebandthat latitudes near the Subantarctic Front, but differences
approximately coincides with the Subantarctic Front either in background gradients or as a result of bio-
(theblackcurveinFigs.2a–c).Comparisonswiththese geochemical processes are significant in the subpolar
modeled mean features and the N-S-T mean fields regions.
showninrecentstudies(e.g.,VerdyandMazloff2017; WenextperformtheMEOFanalysisovertherefer-
Rosso et al. 2017) indicate that the biogeochemical ence N-S-T fields and obtain 720 MEOF modes (see
GCM used in this study reasonably captures the dis- section2bandFig.1,step1,fordetails)forthenitrate
tinctivelarge-scaleN-S-TfeaturesintheSO. map construction. Figure 3 demonstrates the spatial
The large-scale similarities can also be found in the patterns of the leading five MEOF modes, which com-
N-S-Tvariancemaps(inlog scale;Figs.2d,e).Partic- bine toexplain 36% of thetotal N-S-T combined vari-
10
ularlyhighnitratevariancescollocatewithhighsalinity ance. The N-S-T patterns of the first MEOF mode
and temperature variances at the confluence of the captureimportantfeaturesandshowresemblanceswith
Brazil and Malvinas Currents off the Argentine coast eachotheratlowlatitudes(seethefirstcolumnpanelsin
and its downstream areas (Figs. 2d–f). These colloca- Fig. 3), particularly at theconfluence of theBrazil and
tionsimplypartsofthehighN-S-Tvariancesaresourced Malvinas Currents, and in the downstream regions
from the fluctuations and instabilities of the Sub- where the positive nitrate anomalies and out-of-phase
antarctic Front (black curve in Figs. 2d–f), which was salinity and temperature anomalies are collocated. In
also reported by a recent study (Ferrari et al. 2017). contrast,theN-S-Tpatternsdonotresembleeachother
However, mismatches of the N-S-T variance structure in higher latitudes. In the Bellingshausen–Amundsen
appear in high latitudes, poleward of approximately Sea regions (green boxes in the first column panels in
608S, where patterns of nitrate variance do not closely Fig.3)theanomalypatternofstrongpositivetempera-
resemblethepatternsofsalinityandtemperaturevari- ture signals differs from those of moderate negative
ances. The results imply that the ocean dynamics nitrate and salinity patterns. These latitude-dependent

| JULY2018 |     |     | LIANG | ET AL. |     | 1511 |
| -------- | --- | --- | ----- | ------ | --- | ---- |
FIG.4.Theconstructednitrateanomalymapsusingthefirst(a)5,(b)50,(c)100,(d)500,and(e)720MEOFmodesinAugustof
arandommodelyear.TheblackcurveisasinFig.2.(f)TheNRMSEsbetweeneachconstructednitratemapandthereferencenitrate
anomalyfields(cyanline).Alsoshownin(f)aretheNRMSEsforthesalinity(greenline)andtemperaturefields(magentaline).
similaritiesanddifferencesseemtobethegeneralfea- field (N ) and the reference nitrate field (N ). The
|     |     |     |     | map |     | ref |
| --- | --- | --- | --- | --- | --- | --- |
tures of the other four MEOF modes (shown in the NRMSEfornitratemapsisdefinedas
secondtofifthcolumnpanelsinFig.3)andotherlower-
rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
| orderMEOFmodes(notshown). |     |     |     |     | (cid:1) |     |
| ------------------------- | --- | --- | --- | --- | ------- | --- |
(N 2N )23cos(u)
|                                              |                    |              |          |        | m a p r e f                                                                                                    | i     |
| -------------------------------------------- | ------------------ | ------------ | -------- | ------ | -------------------------------------------------------------------------------------------------------------- | ----- |
| Toevaluatetherelationshipsbetweenthenumberof |                    |              |          |        | t,irffiffiffi                                                                                                  |       |
|                                              |                    |              |          | NRMSE5 | ffiffiffi ffi ffiffiffiffiffiffiffiffiffiffiffiffi ffi ffi ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi | , (4) |
| MEOF modes                                   | and the capability | to reproduce | the ref- |        | (cid:1)                                                                                                        |       |
(N )23cos(u)
|                                                |     |     |     |     | ref i |     |
| ---------------------------------------------- | --- | --- | --- | --- | ----- | --- |
| erencenitrateanomalyfield,weshowthesnapshotsof |     |     |     |     | t,i   |     |
themappednitrateanomaliesforonerandomAugustin
thebiogeochemicalGCMsimulationfromusingthefirst where t, i indicate the time step and the spatial grid
point,respectively;andu
fiveMEOFmodestousingtotal720modes(Figs.4a–e). i isthelatitudeatgridi(rad).
The more MEOF modes are used, the more detailed Figure4fshowsthenitrateNRMSEswithanincreasing
featuresofnitrateanomaliesaremanifested.Takingthe number of MEOF modes used in recovering therefer-
anomalies at the Brazil–Malvinas confluence and its ence nitrate anomaly field (cyan line). The first five
downstream regions as an example, when we use only MEOFmodesresultinabout0.81NRMSE(36%vari-
five MEOF modes, the reproduced nitrate anomalies anceexplained),whichisgreatlyreducedtoabout0.092
show two parallel, out-of-phase anomaly bands ex- (99% variance explained) using 500 modes. A similar
tendingfromthecoastalregionintotheSouthAtlantic reductionofNRMSEscanalsobefoundforrecovering
(Fig. 4a), whereas themeandering structures of nitrate salinity and temperature fields (green and magenta
anomalies become evident when using more MEOF lines, respectively, in Fig. 4f). We chose to use 500
modes(Figs.4b–e). MEOF modes for the following nitrate map construc-
Thecapabilityofcapturingthedetailscanbequanti- tion, as this number is sufficient to reduce the N-S-T
fied by examining the normalized root-mean-square NRMSEstolessthan0.1andtoexplainmorethan99%
errors(NRMSEs)betweenthemappednitrateanomaly ofthetotalN-S-Tcombinedvariance.

| 1512 |     | JOURNAL |     | OF ATMOSPHERIC |     |     | AND OCEANIC | TECHNOLOGY |     | VOLUME35 |
| ---- | --- | ------- | --- | -------------- | --- | --- | ----------- | ---------- | --- | -------- |
b. Samplingstrategiesandnitratemapconstruction
ThenitratevarianceishighlyheterogeneousintheSO
domainasshowninFig.2d.Likewise,thespatialstruc-
turesofvariabilityarenotisotropicascanbeseenfrom
| the MEOF   | modes        | in Figs.  | 3 and | 4. It follows |     | that ob-  |     |     |     |     |
| ---------- | ------------ | --------- | ----- | ------------- | --- | --------- | --- | --- | --- | --- |
| servations | in different | locations |       | have varying  |     | levels of |     |     |     |     |
informationcontent.Toinvestigatethishypothesis,we
| create synthetic |             | N-S-T            | datasets | according  |            | to three |     |     |     |     |
| ---------------- | ----------- | ---------------- | -------- | ---------- | ---------- | -------- | --- | --- | --- | --- |
| sampling         | strategies: | 1)               | random   | selection, | 2)         | certain  |     |     |     |     |
| thresholds       | of          | nitrate variance | (N-var   | strategy), |            | and 3)   |     |     |     |     |
| the k-means      | cluster     | method           | (k-means |            | strategy). | The      |     |     |     |     |
samplingstrategiesarelistedinFig.1(step2)forclar-
ification.WeapplytheMEOFanalysistothesesynthetic
datatoreconstructSOnitratemapsandtocomparethe
maps to the reference fields to assess these sampling FIG.5.ColorshadingdenotesthefivesubregionsoftheSOdo-
strategies(seeFig.1,steps3and4). maindeterminedbythek-meansclustermethod.Thenumberof
Figure5showsfiveSOsubregionswithcolormarkings mappinggridpointsincludedineachsubregionisdenotedinthe
parenthesesnexttothecolorbar.TheblackcurveisasinFig.2.
determinedbythek-meansclustermethod(seesection
2cforclusterdetails).TheK1regioninred,containing
430gridpoints(;12264539km2),largelycoincideswith
|            |          |         |      |       |     |          | perfectly sampled | in each | grid over a 60-yr | period; in |
| ---------- | -------- | ------- | ---- | ----- | --- | -------- | ----------------- | ------- | ----------------- | ---------- |
| high N-S-T | variance | regions | that | cover | the | northern |                   |         |                   |            |
otherwords,nogapsintimeareconsidered.
areasoftheSubantarcticFrontextendingfromthecoast
|     |     |     |     |     |     |     | The random | selection strategy, | as expected, | inserts |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------- | ------------ | ------- |
of Argentina toward the coast of South Africa and re- data with no specific spatial preferences (Fig. 6a). The
| gions surrounding |     | the Australian |     | continent. |     | The K2 |     |     |     |     |
| ----------------- | --- | -------------- | --- | ---------- | --- | ------ | --- | --- | --- | --- |
inserteddataarespreadthroughouttheregionwithouta
region in dark yellow, containing 987 grid points specific structure. On the contrary, the 430 N-S-T data
| (;27441742km2), |     | covers | low-latitude |     | regions | outside |                 |                 |              |           |
| --------------- | --- | ------ | ------------ | --- | ------- | ------- | --------------- | --------------- | ------------ | --------- |
|                 |     |        |              |     |         |         | are distributed | in a structured | manner using | the N-var |
theK1area.TheK3andK4regionsingreenandlight
andk-meansstrategies(Figs.6b,c).TheN-varsampling
blue,respectively,containing1337and1135gridpoints, strategy exhibits data grouping in the Davis Sea–
| respectively | (;18734790km2 |     |     | and ;15978503km2), |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Dumontd’UrvilleSearegions(redboxinFig.6b),atthe
together encompass almost all low N-S-T variance re- Brazil–Malvinas confluence and its downstream region
| gions poleward |     | of the Subantarctic |     | Front | (inside | the |     |     |     |     |
| -------------- | --- | ------------------- | --- | ----- | ------- | --- | --- | --- | --- | --- |
(magentaboxinFig.6b),andinthesoutheasternIndian
blackcurveinFig.5).TheK5regioninblue,containing Ocean (black box in Fig. 6b). Similar data placements
968gridpoints(;23490489km2),coverswideareasin are adopted by the k-means strategy, but the inserted
| the South | Pacific | where | relatively | low | N-S-T | variance |     |     |     |     |
| --------- | ------- | ----- | ---------- | --- | ----- | -------- | --- | --- | --- | --- |
dataconcentratesinlow-latituderegions(magentaand
regions are located. The five SO subregions from the blackboxesinFig.6c)ratherthaninhigh-latitudeDavis
| k-means | cluster | method determines |     | the | k-means | strat- |     |     |     |     |
| ------- | ------- | ----------------- | --- | --- | ------- | ------ | --- | --- | --- | --- |
Sea–Dumontd’UrvilleSearegions(redboxinFig.6c).
egy to assess the importance of sampling locations in TheN-S-Tdataareinsertedinonebandextendingfrom
mapconstruction.Thegridnumber,areacoverage,and the Brazil–Malvinas confluence to South Africa, co-
meanN-S-TvariancesofeachKregionaresummarized
incidingwiththeregionnorthoftheSubantarcticFront
inTable1. in the South Atlantic sector, and in another band ex-
| We determine |     | the random |     | selection | strategy | and |              |                  |        |               |
| ------------ | --- | ---------- | --- | --------- | -------- | --- | ------------ | ---------------- | ------ | ------------- |
|              |     |            |     |           |          |     | tending from | the southeastern | region | of the Indian |
N-varstrategywithcertainthresholdvaluesofthenitrate OceantowardtheAustralianwestcoast.
variancethatgiverisetothesamenumberofgridpoints Weprojectthe500MEOFmodesontothesynthetic
| as each | of the | K1–5 regions. | For | example, | when | com- |     |     |     |     |
| ------- | ------ | ------------- | --- | -------- | ---- | ---- | --- | --- | --- | --- |
N-S-Tdatasetsbasedonthethreesamplingstrategiesin
paringstrategiestotheK1region(Fig.6c),werandomly order to estimate the PCs that represent the temporal
select430gridpointsovertheSOdomain(Fig.6a).We variations of each MEOF mode (PC0 in Fig. 1, step 3).
also determined that there are 430 grid points with ni- WetreateachMEOFmodeequallywithoutperforming
trate variance larger than 3.2436 31026 (molN2m 22) anyweightingtoconsideronlythespatialheterogeneity
and used this as our threshold to determine the N-var for each mode. Thus, we are assuming the primary
strategy(Fig.6b).Thus,ourthreesamplingstrategiesall spatial modes of variability of the N-S-T fields are
haveanequalamountofsyntheticN-S-Tdata.Itisnoted known, and we are using the partially sampled N-S-T
that we assume the synthesized N-S-T datasets are anomaly fields to derive their time variability. The

JULY2018 LIANG ET AL. 1513
FIG.6.ThecyandotsdenotethelocationswherethereferenceN-S-Tfieldsaresampledaccordingto(a)randomselection,(b)N-var,
and(c)k-meansstrategies.ThecolorshadingsrepresentthenitrateanomalyfieldinAugustofarandommodelyear.(d)–(f)Thecon-
structednitratemapsforthatAugust.(g)–(i)MapsshowingthespatialdistributionofnitrateNRMSEs.Ineachpanelthemagentabox
denotestheconfluenceoftheBrazilandMalvinasCurrentsanddownstreamintotheSouthAtlanticandIndiansectorregions(608W–
608Eand498–388S);theredboxdenotestheDavisSea–Dumontd’UrvilleSearegions(808–1408Eand658–508S);theblackboxdenotesthe
southeasternregionoftheIndianOcean(688–1158Eand408–308S);andthegreenboxdenotesaSouthPacificregion(1358–1208Wand
558–308S)wherenosamplingdataareaddedbythek-meansandN-varstrategies.
nitrate maps are then constructed by taking the dot inserted. These regions are again the Brazil–Malvinas
productoftheestimatedPCsandtheMEOFmodes(see confluence and downstream region, the Davis Sea–
X inFig.1,step3). Dumont d’Urville Sea regions, and the southeastern
map
Figure6dshowstheconstructednitrateanomalymap Indian Ocean, coinciding with where large NRMSEs
byrandomselectionstrategy,whichcaptureslittleofthe appear using the random selection strategy. The
structure of the reference nitrate anomaly field. The k-meansstrategyalsoshowsskillinrecoveringtheref-
NRMSEs[calculatedfollowingEq.(4)butateachgrid erence nitrate anomaly field (Fig. 6f), significantly re-
point] are large (Fig. 6g), particularly in the Brazil– ducing NRMSEs (Fig. 6i) in the South Atlantic and
Malvinasconfluenceanddownstreamregions(magenta IndianOceansectorsinparticular,butleavesrelatively
box),theDavisSea–Dumontd’UrvilleSearegions(red large NRMSEs in high-latitude Davis Sea–Dumont
box), and thesoutheastern region of theIndian Ocean d’Urville Sea regions where the K1 region does not
(blackbox).TheN-varstrategy,ontheotherhand,re- sample (red box in Fig. 6i). However, overall, the
covers some details of the reference nitrate field with k-meansstrategyhasthesmallestNRMSEwithavalue
comparable magnitudes (Fig. 6e) and greatly reduces of 0.77, while the N-var strategy gives 0.79 and the
nitrateNRMSEs(Fig.6h)intheregionswheredataare randomsamplingstrategygives0.92.

1514 JOURNAL OF ATMOSPHERIC AND OCEANIC TECHNOLOGY VOLUME35
FIG.7.(a)ThenitrateNRMSEswithonlytemperature(magentaline),salinity(greenline),andnitrate(cyanline)dataaddedaccording
toarandomselectionstrategy.(e),(i)Asin(a),butaccordingtotheN-varandk-meansstrategies,respectively.(b)–(d)Thenitrate
NRMSEs with fixed amounts of temperature, salinity, and nitrate added, while variedamounts of the other two fields are inserted
accordingtotherandomselectionstrategy.(f)–(h),(j)–(l)Asin(b)–(d),butaccordingtotheN-varandk-meansstrategies,respectively.
We further investigate the capability of the k-means Fig. 7a, adding nitrate data (cyan line) gives rise to
and N-varstrategies in reconstructing SOnitratemaps smaller nitrate NRMSEs than adding the other two
inregionswherenodataareinserted.Wecalculatethe fields(magentaandgreenlines)asexpected.Theresults
area-averagedNRMSEsovertheregionmarkedbythe also reflect that even with no nitrate data added, the
green box in Fig. 6 and find that smaller NRMSEs use nitrate mapping errors can be reduced by adding tem-
the k-means strategy (0.086) and the N-var strategy peratureorsalinitydataonlybecauseofthecapabilityof
(0.090)thanthosethatusetherandomsamplingstrategy theMEOFmethodtorecoveronefieldwithinformation
(0.095),whichhas16datasamplesintheregion.These from other fields. We also notice that the nitrate
findings not only show the mapping strength of the NRMSEsarereducedlinearlywithanincreasingnum-
MEOF method that uses sampling data to reconstruct berofdataadded,implyingthattherandomnessinthe
nitratemapsoutsidesamplingareasbutalsorevealthat sampling processes can be transformed as linear map-
an organized sampling strategy can better recover the ping error reduction of the MEOF analyses. However,
reference nitrate field in regions where no data are in- thelinearbehaviorofnitratemappingerrorsdisappears
sertedthanrandomselectionstrategy. when we adopt the N-var strategy (Fig. 7e). NRMSEs
Tosystematicallyevaluatethenitratemappingerrors arereducedfasteratfirstandthenasymptoteasmore
and their relationships with adding various amounts of data are inserted. Different from the other sam-
N-S-T fields, we perform a series of nitrate NRMSE plingstrategies,thek-meansstrategyexhibitslarger
analyses (Fig. 7). We first consider adding data to re- NRMSEs, insertingonly nitrate data thanonly salinity
gions following the three sampling strategies but sam- ortemperaturedataintoK1orK1–2regions,butitre-
pling only one field and calculating the corresponding sults in smaller NRMSEs when adding more regions
nitrateNRMSEs(Figs.7a,e,i).Again,thesameamount (Fig. 7i). Such behavior of nitrate mapping errors is
ofdataissampledineachsetoferrorcalculationsforthe possiblycausedbythek-meansclustermethodaimingto
three sampling strategies to make fair comparisons. In capture the greatest variance overall, which does not

JULY2018 LIANG ET AL. 1515
FIG.8.(a)NitrateNRMSEsagainstthenumberofdataaddedinindividualregionsdeterminedbythek-means(solidlines),N-var
(dashedlines),andrandomselection(blackline)strategies.(b),(c)Asin(a),butforsalinityandtemperatureNRMSEs,respectively.
(d)–(f)Asin(a)–(c),butdataarecumulativelyaddedoverthedifferentregions.AllpanelsshowtheaverageArgofloatnumbersdeployed
intheSOfor2008–15(solidgreenline),withtheshadingshowingthestandarddeviation;andthenumberofArgofloatsneededtomeet
thestatedgoalofonefloatevery300km3300km(dashedgreenverticallines).
necessarily lead to the greatest constraints on the incorporates the salinity and temperature information
MEOF method when one has only a single data type. toreduceNRMSEs.Theabovementionedmappinger-
These results show that both the k-means and N-var roranalysesindicatethatthek-meansandN-varstrat-
strategies perform better in reducing mapping errors egies outperform the random selection strategy, while
thanrandomselectionstrategy. the k-means strategy better utilizes the salinity and
Further insights can be gained by generalizing the temperature information to reduce nitrate mapping
resultsinFigs.7a,7e,and7ibycoloringNRMSEscal- errors.
culated by holding the amount of a certain variable Wenextexaminetherelativeimportanceofinserting
constant and varying the other two. Figure 7j, for ex- allN-S-Tdatainregionsdeterminedbythethreesam-
ample,showsthenitrateNRMSEchangeswithdiffering plingstrategiesintothereconstructedmaps.Thefinding
amountsofnitrate(signifiedonthexaxis)andsalinity that adding data randomly results in an approximately
(signified on the y axis) data inserted throughout the linearNRMSEreductionrate(Figs.7a–d)impliesthat
K1–5regionswhenafixedamountoftemperaturedata wecanusethisrate(orslope)withdataaddedrandomly
(2754 data points) are inserted into the K1–3 regions. in one region as a first-order measure for its relative
Comparing the NRMSEs in Fig. 7 verifies that the importance. In other words, the faster the error re-
k-meansandN-varstrategiesresultinsmallerNRMSEs ductionrate(orsteeperslope)isinoneregionwithdata
and faster error reduction rates relative to random se- randomly added, the more important the region is. As
lectionstrategies.Wealsofindthataddingsalinityand such,weaddN-S-TdatarandomlytotheK1–5regions
temperaturedatatendstoreducenitratemappingerrors individuallyandshowthecorrespondingnitrateNRMSEs
morewhenusingthek-meansstrategythanfortheother againstthenumberofaddeddata(Fig.8a).Whenadd-
strategies(cf.Figs.7d,h,l).Thisreflectsthatthek-means ing 0–430 data to the K1 region, we find that the
cluster method adopts a sampling strategy that also NRMSEsdropfastfrom1.0toabout0.77(theredsolid

1516 JOURNAL OF ATMOSPHERIC AND OCEANIC TECHNOLOGY VOLUME35
line in Fig. 8a). However, adding 430 data to the K2 in high-variance regions. These results are consistent
regiondropsNRMSEtoonlyabout0.91(thebluesolid withthoseshowninFigs.8a–c.
lineinFig.8a).Theirdifferentslopesalsorevealthatin TheabovementionedexaminationsofN-S-Tmapping
order to obtain the same effect of reducing nitrate error reduction rates within different regions deter-
NRMSEtoabout0.77,approximately987dataneedto minedbythesamplingstrategiesquantifymappingerror
be addedtothe K2 region, butonlyabout 430 datato reductionviaaddingdataandinformingthesignificance
the K1 region. This result clearly shows the error re- of sampling density and distribution. The results high-
duction rate in the K2 region is slower than in the K1 light that having greater data density in high-variance
region,anditindicatestheK2regionislessimportant regions(e.g.,theK1andK2regions)ismoreimportant
than the K1 region for constraining the mapping. than in low-variance regions for constructing nitrate
Likewise,astheerrorreductionratesaremuchslower (andsalinityandtemperature)maps.
fortheK3,K4,andK5regions(magenta,cyan,anddark
yellowsolidlinesinFig.8a),theyalsoplaylessimpor-
4. Summaryanddiscussion
tant roles than the K1 and K2 regions in reducing
mappingerrors.TheapproximatedNRMSEreduction This study employs the MEOF method to construct
ratesineachK-regionfortheN-S-Tfieldsaresumma- SOnitratemapsusingN-S-Tcombineddatasetsfroma
rizedinTable1. state-of-the-artbiogechemicalGCM.Anassessmentof
Although adding data to regions determined by the the MEOF method skill in estimating the reference
N-var strategy gives rise to similar NRMSE reduction modeled nitrate field suggests that using the first 500
ratesasdeterminedbythek-meansstrategyfornitrate MEOF modes sufficiently recovers 99% of the model
field (solid and dashed lines in Fig. 8a), discrepancies signal.ToassessanoptimalwaytosampleN-S-Tdatain
becomeevidentfortheratesassociatedwithsalinityand theSO,wecreatesyntheticN-S-Tdatasetsviasampling
temperaturefields(solidanddashedlinesinFigs.8b,c). reference N-S-T anomaly fields in regions determined
Thek-meansstrategyoutperformstheN-varstrategyin byeitherrandomselection,acertainthresholdofnitrate
reducingsalinityandtemperaturemappingerrors,par- variance, or a k-means cluster method. The first 500
ticularlyinthehighnitratevarianceregions(i.e.,K1–2 MEOF modes are then projected onto these synthetic
andVar1–2regions).Theresultssupportthoseshownin N-S-T datasets to construct the SO nitrate maps. The
Fig. 7 and further indicates that when targeting high skillintheconstructedmapsissystematicallyexamined
nitrate variance regions, the k-means strategy not only with a series of error analyses. The examination of
maintains similar performance as the N-var strategy in mapping error reduction rates of each region de-
reducing nitrate mapping errors but also better re- terminedbythesesamplingstrategiesrevealstheirrel-
constructssalinityandtemperaturemaps. ative importance and addresses the significance of
To further examine whether the mapping error re- sampling data density within each region. The results
duction rate of one K-region is affected by the data conclude that sampling strategies considering nitrate
inserted into other regions (i.e., the independence be- variance structure yield more mapping skill than un-
tween each K-region), we add N-S-T data sequentially structured random selection strategy. The k-means
totheK1–K5regionsandcalculateNRMSEs(Figs.8d–f). strategy further utilizes the salinity and temperature
Thatis,werandomlyadddatatotheK1regionuntil430 informationtoreducethemappingerrors.TheMEOF
datafillitandthenrandomlyadddatatotheK2region method together with the k-means sampling strategy
until987datafillit,andsoon.Wefindthemappingerror suggestsaframeworktoprioritizedeploymentofinsitu
reductionratesofoneregiondonotchangewhenN-S-T measurements, such as biogeochemical Argo floats, to
data have been added in other regions. For example, sample important nitrate spatiotemporal variations in
thereductionrateofnitratemappingerroraddedinthe theSOandtoconstructaccuratenitratemaps.
K2 region individually (i.e., the solid blue line in Ourfindingsindicatethatthek-meansstrategygives
Fig. 8a) does not change when the K1 region has first rise to better N-S-T maps (Figs. 8d–f), but it does not
been filled up with 430 data (i.e., the solid blue line introduce a fundamentally different sampling strategy
segmentinFig.8d).Thisresultconfirmsthattheeffects from that considering solely nitrate variance. To elab-
of inserting data into different regions to reduce oratethispoint,weperformthek-meansclustermethod
NRMSEs are independent of each other. Such in- on a nitrate variance field only and obtain similar
dependence can also be found in the N-var sampling grouping regions (not shown) as those determined by
strategy (dashed lines in Figs. 8d–f). However, the theN-varstrategy.Thisimpliesthatthek-meansstrat-
NRMSEsarehigherinmagnitudeanddropslowerthan egy will perform similarly as the N-var strategy if con-
thoseassociatedwiththek-meansstrategy,particularly sidering only the nitrate variance. Thus, our findings

| JULY2018 |     |     |     |     |     | LIANG | ET AL. |     |     |     |     | 1517 |
| -------- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | ---- |
emphasize the significance of utilizing as much in- reduce nitrate NRMSE to 0.62, salinity NRMSE to
formationasisavailable,whichhereincludestheN-S-T 0.46,andtemperature NRMSEto0.49.Thesefindings
combinedvariances,whenconstructingmaps. reveal the potential capability of the Argo float array
One caveat to address is that this study does not to reconstruct SO N-S-T maps adopting the k-means
| considertheresolutioneffectsofthemappinggrid.Ifthe |     |     |     |     |     |     | strategy. |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
gridresolutiondoublestoapproximately1830:58inthe TheabovementionedcomparisonssuggestthatArgo
SOdomain,thendataredundancybetweengridpoints floats should be deployed densely where the N-S-T
would likely become an issue and would need to be combinedvarianceishighandsparselywherethevari-
anceislow,ratherthanjustachievinguniform300km3
consideredfortheoptimalsamplingstrategy.Itisworth
assessingdecorrelationscales(Mazloffetal.2018)and 300kmspatialcoverage.Thisstudyfindsthattargeting
performingsensitivityanalysesofvariousgridmapping high N-S-T combined variance is key to improving the
resolutions. These assessments may help identify the capability of the MEOF method to construct skilled
optimal number of inserted N-S-T data within specific nitrate maps. However, in practice only 30% of Argo
regions, revealing where increased resolution does not floats (i.e., about 326 floats in the nominal float de-
furtherimprovethemappingskill. ployment) are likely to be equipped with biogeo-
Itisalsonotedthatthisstudyassumesthestatisticsof chemical sensors (Johnson and Claustre 2016). Such
the N-S-T fields are perfectly known. In our analyses observationallimitationsstresstheimportanceofusing
thereisnomappingerrorinducedbyinaccuraciesinthe other biogeochemical variables, such as salinity and
MEOF modes. The degree that numerical models can temperature information, of which Fig. 7 may provide
provide accurate variance and covariance information usefulinsights.Inaddition,somestudiesshowedglobal
of oceanic N-S-T fields must be assessed. Another ca- nitrate fields can be estimated using chlorophyll-a, sea
veatisthattheanalysesarecarriedoutonlywithN-S-T surface temperatures, and mixed layer depth fields
fieldsat100m.Relationshipsmaydifferatotherdepths, (Switzeretal.2003;Arteagaetal.2015).Mergingthese
andthismustbealsoassessed.Finally,wenotethatour fieldsandotherobservablesintotheMEOFcalculation
calculations assume the N-S-T time series at each ob- and k-means sampling strategy may also improve our
servationlocationisuninterrupted.Floatsarelimitedby capability to construct more accurate and informative
| batterylife,andareaffectedbysevereweatherevents, |     |     |     |     |     |     | SOnitratemaps. |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
variationsofprevailingoceancurrentsandseaicecover,
| sensor malfunction, |     | and | interventions |     | of signal | trans- |                  |     |     |              |         |       |
| ------------------- | --- | --- | ------------- | --- | --------- | ------ | ---------------- | --- | --- | ------------ | ------- | ----- |
|                     |     |     |               |     |           |        | Acknowledgments. |     | We  | thank Editor | William | Emery |
mission (Johnson et al. 2017; Briggs et al. 2018). As- and one anonymous reviewer, whose comments and
| sessing the | impact | of  | spatiotemporal | heterogeneity |     | on  |             |        |            |      |             |      |
| ----------- | ------ | --- | -------------- | ------------- | --- | --- | ----------- | ------ | ---------- | ---- | ----------- | ---- |
|             |        |     |                |               |     |     | suggestions | helped | to improve | this | manuscript. | This |
observationalcoverageisleftforfuturework. work is supported by NSF’s Climate and Large-scale
ThisstudyisbasedonsyntheticN-S-Tdatasetsfroma
DynamicsProgramunderGrantAGS-1505145andthe
| biogeochemical |     | GCM | simulation. | In  | practice, | only | a   |     |     |     |     |     |
| -------------- | --- | --- | ----------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- |
SouthernOceanCarbonandClimateObservationsand
limited number of in situ measurements, such as bio- Modeling (SOCCOM) project, which is supported by
| geochemical | Argo | floats, | can | be deployed | in  | the SO |              |         |            |       |       |       |
| ----------- | ---- | ------- | --- | ----------- | --- | ------ | ------------ | ------- | ---------- | ----- | ----- | ----- |
|             |      |         |     |             |     |        | the National | Science | Foundation | (NSF) | under | Award |
(e.g., Johnson et al. 2017). We survey Argo float data PLR-1425989.TheArgofloatinformationduring2008–
duringthe2008–15periodfromtheglobaldatacenters
|     |     |     |     |     |     |     | 15 period | are obtained | from | the | global | data centers |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ---- | --- | ------ | ------------ |
(ftp://usgodae.org/pub/outgoing/argo;ftp://ftp.ifremer.fr/
(\url{ftp://usgodae.org/pub/outgoing/argo};\url{ftp://ftp.
ifremer/argo)andfindthatanaverageof8896112Argo
|     |     |     |     |     |     |     | ifremer.fr/ifremer/argo}). |     |     | The Subantartic |     | Front infor- |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --------------- | --- | ------------ |
floatsweredeployedintheoceanssouthof308Ssince
mationisobtainedfromNASA’sGlobalChangeMaster
| 2005. This                                    | amount  | of          | Argo floats, | denoted   |         | as solid | Directory. |     |            |     |     |     |
| --------------------------------------------- | ------- | ----------- | ------------ | --------- | ------- | -------- | ---------- | --- | ---------- | --- | --- | --- |
| green vertical                                |         | lines (with | gray         | shadings) | in Fig. | 8, can   |            |     |            |     |     |     |
| fill out                                      | all the | K1 region   | and          | half of   | the K2  | region,  |            |     |            |     |     |     |
| andthusreducenitrateNRMSEto0.66,salinityNRMSE |         |             |              |           |         |          |            |     | REFERENCES |     |     |     |
to0.52,andtemperatureNRMSEto0.54.Wealsomark
Alvera-Azcárate,A.,A.Barth,M.Rixen,andJ.-M.Beckers,2005:
| the nominal | Argo | density | goal | of 300km | 3   | 300km |     |     |     |     |     |     |
| ----------- | ---- | ------- | ---- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- |
Reconstructionofincompleteoceanographicdatasetsusing
resolution (i.e., coverage area per float; Johnson and empirical orthogonal functions: Application to the Adriatic
Claustre 2016) or about 1088 Argo floats deployed in Seasurfacetemperature.OceanModell.,9,325–346,https://
approximately35833608SO doi.org/10.1016/j.ocemod.2004.08.001.
| the |     |     |     | domain | asshownby |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
——,——,J.-M.Beckers,andR.H.Weisberg,2007:Multivariate
thedashedverticalgreenlinesinFig.8.IfthisArgogoal
|              |      |     |                     |     |       |       | reconstruction |     | of missing     | data in sea | surface     | temperature, |
| ------------ | ---- | --- | ------------------- | --- | ----- | ----- | -------------- | --- | -------------- | ----------- | ----------- | ------------ |
| is achieved, | then | the | in situ measurement |     | could | cover |                |     |                |             |             |              |
|              |      |     |                     |     |       |       | chlorophyll,   | and | wind satellite | fields.     | J. Geophys. | Res., 112,   |
the K1 region and more than half the K2 region, and C03008,https://doi.org/10.1029/2006JC003660.

1518 JOURNAL OF ATMOSPHERIC AND OCEANIC TECHNOLOGY VOLUME35
——,——,D.Sirjacobs,F.Lenartz,andJ.-M.Beckers,2011:Data Ducklow,H.W.,D.K.Steinberg,andK.O.Buesseler,2001:Upper
InterpolatingEmpiricalOrthogonalFunctions(DINEOF):A oceancarbonexportandthebiologicalpump.Oceanography,
toolforgeophysicaldataanalyses.Mediterr.Mar.Sci.,12(3), 14(4),50–58,https://doi.org/10.5670/oceanog.2001.06.
5–11,https://doi.org/10.12681/mms.64. Dugdale, R. C., and J. J. Goering, 1967: Uptake of new and
——,——,G.Parard,andJ.-M.Beckers,2016:AnalysisofSMOS regenerated forms of nitrogen in primary productivity.
seasurfacesalinitydatausingDINEOF.RemoteSens.Envi- Limnol. Oceanogr., 12, 196–206, https://doi.org/10.4319/
ron.,180,137–145,https://doi.org/10.1016/j.rse.2016.02.044. lo.1967.12.2.0196.
Amante,C.,andB.Eakins,2009:ETOPO1GlobalReliefModel Elderfield H., Ed., 2006: The Oceans and Marine Geochemistry.
converted to PanMap layer format. NOAA National Geo- TreatiseonGeochemistry,Vol.6,Pergamon,664pp.
physicalDataCenter,accessed7February2018,https://doi.org/ Ferrari,R.,C.Artana,M.Saraceno,A.R.Piola,andC.Provost,
10.1594/PANGAEA.769615. 2017: Satellite altimetry and current-meter velocities in the
Ardyna,M.,H.Claustre,J.Sallee,F.D’Ovidio,B.Gentili,G.van MalvinasCurrentat418S:Comparisonsandmodesofvaria-
Dijken,F.D’Ortenzio,andK.R.Arrigo,2017:Delineating tions.J.Geophys.Res.Oceans,122,9572–9590,https://doi.org/
environmental control of phytoplankton biomass and phe- 10.1002/2017JC013340.
nologyintheSouthernOcean.Geophys.Res.Lett.,44,5016– Firdaus,S.,andM.A.Uddin,2015:Asurveyonclusteringalgo-
5024,https://doi.org/10.1002/2016GL072428. rithmsandcomplexityanalysis.Int.J.Comput.Sci.Issues,12
Arrigo,K.R.,2005:Marinemicroorganismsandglobalnutrientcy- (2),62–85.
cles.Nature,437,349–355,https://doi.org/10.1038/nature04159. Forgy, E., 1965: Cluster analysis of multivariate data: Efficiency
Arteaga,L.,M.Pahlow,andA.Oschlies,2015:Globalmonthlysea versusinterpretabilitymodels.Biometrics,21,768–769.
surface nitrate fields estimated from remotely sensed sea Fukumori,I.,andC.Wunsch,1991:Efficientrepresentationofthe
surface temperature, chlorophyll, and modeled mixed layer NorthAtlantichydrographicandchemicaldistributions.Prog.
depth. Geophys. Res. Lett., 42, 1130–1138, https://doi.org/ Oceanogr.,27,111–195,https://doi.org/10.1016/0079-6611(91)
10.1002/2014GL062937. 90015-E.
Beckers, J.-M., and M. Rixen, 2003: EOF calculations and data Galbraith, E. D., A. Gnanadesikan, J. P. Dunne, and M. R.
filling from incomplete oceanographic datasets. J. Atmos. Hiscock,2010:Regionalimpactsofiron-lightcolimitationina
OceanicTechnol.,20,1839–1856,https://doi.org/10.1175/1520- global biogeochemical model. Biogeosciences, 7, 1043–1064,
0426(2003)020,1839:ECADFF.2.0.CO;2. https://doi.org/10.5194/bg-7-1043-2010.
Briggs,E.M.,T.R.Martz,L.D.Talley,M.R.Mazloff,andK.S. Garcia,H.E.,andCoauthors,2013a:DissolvedOxygen,Apparent
Johnson,2018:Physicalandbiologicaldriversofbiogeochemi- Oxygen Utilization, and Oxygen Saturation. Vol. 3, World
caltracerswithintheseasonalseaicezoneoftheSouthernOcean OceanAtlas2013,NOAAAtlasNESDIS75,27pp.,https://
from profiling floats. J. Geophys. Res. Oceans, 123, 746–758, doi.org/10.7289/V5XG9P2W.
https://doi.org/10.1002/2017JC012846. ——, R. A. Locarnini, T. P. Boyer, J. I. Antonov, O. Baranova,
Church,M.J.,D.A.Hutchins,andH.W.Ducklow,2000:Limi- M.M.Zweng,J.R.Reagan,andD.R.Johnson,2013b:Dis-
tationofbacterialgrowthbydissolvedorganicmatterandiron solvedInorganicNutrients(Phosphate,Nitrate,Silicate).Vol.4,
inthe SouthernOcean.Appl.Environ.Microbiol., 66, 455– WorldOcean Atlas2013, NOAA Atlas NESDIS 76, 25 pp.,
466,https://doi.org/10.1128/AEM.66.2.455-466.2000. https://doi.org/10.7289/V5J67DWD.
Dai, A., and K. E. Trenberth, 2002: Estimates of freshwater Hammond,M.D.,andD.C.Jones,2016:Freshwaterfluxfromice
dischargefromcontinents:Latitudinalandseasonalvaria- sheet melting and iceberg calving in the Southern Ocean.
tions.J.Hydrometeor.,3,660–687,https://doi.org/10.1175/ Geosci.DataJ.,3,60–62,https://doi.org/10.1002/gdj3.43.
1525-7541(2002)003,0660:EOFDFC.2.0.CO;2. Hartigan, J. A., and M. A. Wong, 1979: Algorithm AS 136: A
Dee, D. P., and Coauthors, 2011: The ERA-Interim reanalysis: k-meansclusteringalgorithm.Appl.Stat.,28,100–108,https://
Configurationandperformanceofthedataassimilationsys- doi.org/10.2307/2346830.
tem.Quart.J.Roy.Meteor.Soc.,137,553–597,https://doi.org/ Hoppe, C. J. M., and Coauthors, 2015: Controls of primary
10.1002/qj.828. production in two phytoplankton blooms in the Antarctic
DeMey,P.,andA.R.Robinson,1987:Assimilationofaltimeter CircumpolarCurrent.DeepSeaRes.II,138,63–73,https://
eddy fields in a limited-area quasi-geostrophic model. doi.org/10.1016/j.dsr2.2015.10.005.
J.Phys.Oceanogr.,17,2280–2293,https://doi.org/10.1175/ Ishizu,M.,andK.J.Richards,2013:Relationshipbetweenoxygen,
1520-0485(1987)017,2280:AOAEFI.2.0.CO;2. nitrate,andphosphateintheworldoceanbasedonpotential
Deppeler,S.L.,andA.T.Davidson,2017:SouthernOceanphy- temperature.J.Geophys.Res.Oceans,118,3586–3594,https://
toplankton in a changing climate. Front. Mar. Sci., 4, 40, doi.org/10.1002/jgrc.20249.
https://doi.org/10.3389/fmars.2017.00040. Johnson, K. S., and H. Claustre, 2016: The scientific rationale,
Dormann, C. F., and Coauthors, 2007: Methods to account for designandimplementationplanfor abiogeochemical-Argo
spatialautocorrelationintheanalysisofspeciesdistributional floatarray.K.JohnsonandH.Claustre,Eds.,Biogeochemical-
data: A review. Ecography, 30, 609–628, https://doi.org/ ArgoPlanningGroup,58pp.,https://doi.org/10.13155/46601.
10.1111/j.2007.0906-7590.05171.x. ——,J.N.Plant,J.P.Dunne,L.D.Talley,andJ.L.Sarmiento,
D’Ortenzio,F.,andM.Riberad’Alcalà,2009:Onthetrophicre- 2017:AnnualnitratedrawdownobservedbySOCCOMpro-
gimes of the Mediterranean Sea: A satellite analysis. Bio- filing floats and the relationship to annual net community
geosciences,6,139–148,https://doi.org/10.5194/bg-6-139-2009. production.J.Geophys.Res.Oceans,122,6668–6683,https://
——, D. Antoine, E. Martinez, and M. Ribera d’Alcalà, 2012: doi.org/10.1002/2017JC012839.
Phenologicalchangesofoceanicphytoplanktoninthe1980s Kaplan,A.,Y.Kushnir,M.A.Cane,andM.B.Blumenthal,1997:
and 2000s as revealed by remotely sensed ocean-color ob- Reduced space optimal analysis for historical data sets:
servations.GlobalBiogeochem.Cycles,26,GB4003,https:// 136 years of Atlanticsea surfacetemperatures. J. Geophys.
doi.org/10.1029/2011GB004269. Res.,102,27835–27860,https://doi.org/10.1029/97JC01734.

JULY2018 LIANG ET AL. 1519
Key,R.M.,andCoauthors,2015:GlobalOceanDataAnalysis Pedregosa,F.,andCoauthors,2011:Scikit-learn:Machinelearning
Project,version2(GLODAPv2).OakRidgeNationalLab- inPython.J.Mach.Learn.Res.,12,2825–2830.
oratoryCarbonDioxideInformationAnalysisCenter,accessed Plant,J.N.,K.S.Johnson,C.M.Sakamoto,H.W.Jannasch,L.J.
7February2018,doi:10.3334/CDIAC/OTG.NDP093_GLODAPv2. Coletti, S. C. Riser, and D. D. Swift, 2016: Net community
Kondrashov, D., and M. Ghil, 2006: Spatio-temporal filling of productionatOceanStationPapaobservedwithnitrateand
missing points in geophysical data sets. Nonlinear Processes oxygensensorsonprofilingfloats.GlobalBiogeochem.Cycles,
Geophys.,13,151–159,https://doi.org/10.5194/npg-13-151-2006. 30,859–879,https://doi.org/10.1002/2015GB005349.
Kruskal, W. H., and W. A. Wallis, 1952: Use of ranks in one- Reynolds, R. W., and T. M. Smith, 1994: Improved global sea
criterionvarianceanalysis.J.Amer.Stat.Assoc.,47,583–621, surface temperature analyses using optimum interpolation.
https://doi.org/10.1080/01621459.1952.10483441. J.Climate,7,929–948,https://doi.org/10.1175/1520-0442(1994)
Lacour,L.,H.Claustre,L.Prieur,andF.D’Ortenzio,2015:Phy- 007,0929:IGSSTA.2.0.CO;2.
toplanktonbiomasscyclesintheNorthAtlanticsubpolargyre: Rosso,I.,M.R.Mazloff,A.Verdy,andL.D.Talley,2017:Space
AsimilarmechanismfortwodifferentbloomsintheLabrador and time variability of the Southern Ocean carbon budget.
Sea. Geophys. Res. Lett., 42, 5403–5410, https://doi.org/ J. Geophys. Res. Oceans, 122, 7407–7432, https://doi.org/
10.1002/2015GL064540. 10.1002/2016JC012646.
Lauvset, S. K., and Coauthors, 2016: A new global interior ocean Schneider,T.,2001:Analysisofincompleteclimatedata:Estima-
mapped climatology: The 18 3 18 GLODAP version 2. tionofmeanvaluesandcovariancematricesandimputationof
Earth Syst. Sci. Data, 8, 325–340, https://doi.org/10.5194/ missingvalues.J.Climate,14,853–871,https://doi.org/10.1175/
essd-8-325-2016. 1520-0442(2001)014,0853:AOICDE.2.0.CO;2.
Letscher,R.T.,F.Primeau,andJ.K.Moore,2016:Nutrientbudgets Shirkhorshidi,A.S.,S.Aghabozorgi,T.Y.Wah,andT.Herawan,
inthesubtropicaloceangyresdominatedbylateraltransport. 2014: Big data clustering: A review. Computational Science
Nat.Geosci.,9,815–819,https://doi.org/10.1038/ngeo2812. andItsApplications—ICCSA2014,B.Murganteetal.,Eds.,
Losch, M., D. Menemenlis, J.-M. Campin, P. Heimbach, and LectureNotesinComputerScience,Vol.8583,Springer,707–
C.Hill,2010:Ontheformulationofsea-icemodels.Part1: 720,https://doi.org/10.1007/978-3-319-09156-3_49.
Effectsof differentsolverimplementations andparameteri- Smith,T.M.,R.W.Reynolds,R.E.Livezey,andD.C.Stokes,
zations. Ocean Modell., 33, 129–144, https://doi.org/10.1016/ 1996: Reconstruction of historical sea surface tempera-
j.ocemod.2009.12.008. turesusingempiricalorthogonalfunctions.J.Climate,9,
MacQueen,J.,1967:Somemethodsforclassificationandanalysis 1403–1420,https://doi.org/10.1175/1520-0442(1996)009,1403:
of multivariate observations. Statistics, L. M. Le Cam and ROHSST.2.0.CO;2.
J. Neyman, Eds., Vol. 1, Proceedings of the Fifth Berkeley Sparnocchia, S., N. Pinardi, and E. Demirov, 2003: Multivariate
SymposiumonMathematicalStatisticsandProbability,Uni- empiricalorthogonalfunctionanalysisoftheupperthermo-
versityofCaliforniaPress,281–297. cline structure of the Mediterranean Sea from observations
Marshall,J.,A.Adcroft,C.Hill,L.Perelman,andC.Heisey,1997: andmodelsimulations.Ann.Geophys.,21,167–187,https://
A finite-volume, incompressible Navier Stokes model for doi.org/10.5194/angeo-21-167-2003.
studiesoftheoceanonparallelcomputers.J.Geophys.Res., Stammer,D.,andCoauthors,2002:Globaloceancirculationdur-
102,5753–5766,https://doi.org/10.1029/96JC02775. ing 1992–1997, estimated from ocean observations and a
Mayot, N., F. D’Ortenzio, M. R. D’Alcal(cid:2)a, H. Lavigne, and generalcirculationmodel.J.Geophys.Res.,107,3118,https://
H.Claustre,2016:InterannualvariabilityoftheMediterranean doi.org/10.1029/2001JC000888.
trophic regimes from ocean color satellites. Biogeosciences, Switzer,A.C.,D.Kamykowski,andS.-J.Zentara,2003:Mapping
13,1901–1917,https://doi.org/10.5194/bg-13-1901-2016. nitrateintheglobaloceanusingremotelysensedseasurface
Mazloff, M. R., P. Heimbach, and C. Wunsch, 2010: An eddy- temperature. J. Geophys. Res., 108, 3280, https://doi.org/
permittingSouthernOceanstateestimate.J.Phys.Oceanogr., 10.1029/2000JC000444.
40,880–899,https://doi.org/10.1175/2009JPO4236.1. Verdy,A.,andM.R.Mazloff,2017:Adataassimilatingmodelfor
——, B. Cornuelle, S. Gille, and A. Verdy, 2018: Correlation estimatingSouthernOceanbiogeochemistry.J.Geophys.Res.
lengthsforestimatingthelarge-scalecarbonandheatcontent Oceans,122,6968–6988,https://doi.org/10.1002/2016JC012650.
oftheSouthernOcean.J.Geophys.Res.Oceans,123,883–901, Wang, J.-F.,A. Stein, B.-B. Gao,and Y. Ge, 2012:A reviewof
https://doi.org/10.1002/2017JC013408. spatial sampling. Spat. Stat., 2, 1–14, https://doi.org/10.1016/
Moore, C. M., and Coauthors, 2013: Processes and patterns of j.spasta.2012.08.001.
oceanicnutrientlimitation.Nat.Geosci.,6,701–710,https:// Wheeler,M.C.,andH.H.Hendon,2004:Anall-seasonreal-time
doi.org/10.1038/ngeo1765. multivariateMJOindex:Developmentofanindexformoni-
Munro,D.R.,andCoauthors,2015:Estimatesofnetcommunity toringandprediction.Mon.Wea.Rev.,132,1917–1932,https://
productionintheSouthernOceandeterminedfromtimese- doi.org/10.1175/1520-0493(2004)132,1917:AARMMI.2.0.CO;2.
riesobservations(2002–2011)ofnutrients,dissolvedinorganic Williams, R. G., and M. J. Follows, 2003: Physical transport of
carbon,andsurfaceoceanpCO inDrakePassage.Deep-Sea nutrients and the maintenance of biological production.
2
Res.II,114,49–63,https://doi.org/10.1016/j.dsr2.2014.12.014. Ocean Biogeochemistry, Global Change—The IGBP Series,
Nikolaidis,A.,G.Georgiou,D.Hadjimitsis,andE.Akylas,2014: Springer,19–51,https://doi.org/10.1007/978-3-642-55844-3_3.
Fillinginmissingsea-surfacetemperaturesatellitedataover Wunsch,C.,andP.Heimbach,2007:Practicalglobaloceanicstate
theEasternMediterraneanSeausingtheDINEOFalgorithm. estimation. Physica D, 230, 197–208, https://doi.org/10.1016/
OpenGeosci.,6,27–41,https://doi.org/10.2478/s13533-012-0148-1. j.physd.2006.09.040.
Orsi,A.H.,T.Whitworth,andW.D.Nowlin,1995:Ontheme- Xue, Y., A. Leetmaa, and M. Ji, 2000: ENSO prediction with
ridionalextentandfrontsoftheAntarcticCircumpolarCur- Markov models: The impact of sea level. J. Climate, 13,
rent. Deep-Sea Res. I, 42, 641–673, https://doi.org/10.1016/ 849–871, https://doi.org/10.1175/1520-0442(2000)013,0849:
0967-0637(95)00021-W. EPWMMT.2.0.CO;2.