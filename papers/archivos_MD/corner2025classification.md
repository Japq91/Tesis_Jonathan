Nat.HazardsEarthSyst.Sci.,25,207–229,2025
https://doi.org/10.5194/nhess-25-207-2025
©Author(s)2025.Thisworkisdistributedunder
theCreativeCommonsAttribution4.0License.
Classification of North Atlantic and European extratropical cyclones
| using | multiple | measures | of  | intensity |     |     |     |     |     |     |
| ----- | -------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- |
JoonaCornér1,ClémentBouvier1,BenjaminDoiteau2,3,FlorianPantillon2,andVictoriaA.Sinclair1
1InstituteforAtmosphericandEarthSystemResearch/Physics,FacultyofScience,
UniversityofHelsinki,Helsinki,Finland
2Laboratoired’Aérologie,UniversitédeToulouse,CNRS,UPS,IRD,Toulouse,France
3CNRM,UniversitédeToulouse,Météo-France,CNRS,Toulouse,France
Correspondence:JoonaCornér(joona.corner@helsinki.fi)
Received:10June2024–Discussionstarted:26June2024
Revised:25September2024–Accepted:10November2024–Published:13January2025
Abstract. The question of how to quantify the intensity of ity of a set of investigated impactful storms (17 out of 21),
extratropical cyclones (ETCs) does not have a simple an- whichdemonstratestheabilityofthemethodtoidentifypo-
swer. To offer some perspective on this issue, we analyse tentiallydamagingETCs.
| multiple    | measures of      | intensity for North | Atlantic | and Eu- |     |     |     |     |     |     |
| ----------- | ---------------- | ------------------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
| ropean ETCs | for the extended | winter season       | between  | 1979    |     |     |     |     |     |     |
and2022usingERA5reanalysisdata.Themostrelevantin-
1 Introduction
tensitymeasuresareidentifiedbyinvestigatingrelationships
betweenthemandbyperformingasparseprincipalcompo-
|     |     |     |     |     | Extratropical | cyclones | (ETCs), | also | referred | to as mid- |
| --- | --- | --- | --- | --- | ------------- | -------- | ------- | ---- | -------- | ---------- |
nentanalysisonthesetofmeasures.Weshowthatdynamical
intensity measures correlate strongly with each other, while latitude cyclones or low-pressure systems, constitute a sub-
|     |     |     |     |     | stantial | part of the atmospheric |     | circulation |     | in the mid- |
| --- | --- | --- | --- | --- | -------- | ----------------------- | --- | ----------- | --- | ----------- |
correlationsareweakerforimpact-relevantmeasures.Based
|     |     |     |     |     | latitudes | and transport | large amounts | of  | heat, | moisture, and |
| --- | --- | --- | --- | --- | --------- | ------------- | ------------- | --- | ----- | ------------- |
onthecorrelationsandthesparseprincipalcomponentanal-
ysis, we find that five intensity measures, namely 850hPa momentum polewards (Hartmann, 2015). ETCs are also re-
sponsibleformostoftheday-to-dayvariabilityinweatherin
| relative | vorticity, 850hPa | wind speed, | wind footprint, | pre- |     |     |     |     |     |     |
| -------- | ----------------- | ----------- | --------------- | ---- | --- | --- | --- | --- | --- | --- |
cipitation,andastormseverityindex,describeETCintensity themid-latitudesandarethedynamicalcauseformostofthe
comprehensivelyandnon-redundantly.Usingthesefivemea- precipitation(Hawcroftetal.,2012).Furthermore,themost
extremeETCscanbeassociatedwithheavyprecipitationand
suresasinput,weobjectivelyclassifytheETCswithaclus-
ter analysis based on a Gaussian mixture model. The clus- strongwindsresponsibleforflooding,landslides,damageto
infrastructure,ordiverseeconomiclosses.
| ter analysis | is able to  | produce four clusters | between    | which      |        |              |       |           |          |           |
| ------------ | ----------- | --------------------- | ---------- | ---------- | ------ | ------------ | ----- | --------- | -------- | --------- |
|              |             |                       |            |            | No two | ETCs are the | same, | and there | is great | variabil- |
| ETCs differ  | in terms of | their intensity,      | life cycle | character- |        |              |       |           |          |           |
istics such as deepening rate and lifetime, and geographical ity in their shape, size, lifetime, and intensity (Nielsen and
|           |                 |             |                |       | Dole, 1992). | Thus, many | attempts | of  | classifications | have |
| --------- | --------------- | ----------- | -------------- | ----- | ------------ | ---------- | -------- | --- | --------------- | ---- |
| location. | A fourth of all | ETCs belong | to the weakest | clus- |              |            |          |     |                 |      |
ter and occur mostly over Europe and in the Mediterranean been made and have often been driven by the desire to bet-
|     |     |     |     |     | ter understand | the development |     | or the | structure | of certain |
| --- | --- | --- | --- | --- | -------------- | --------------- | --- | ------ | --------- | ---------- |
area.NearlyhalfofallETCsbelongtotheaverage-intensity
|     |     |     |     |     | types of | ETCs. For example, | Zillman |     | and Price | (1972) and |
| --- | --- | --- | --- | --- | -------- | ------------------ | ------- | --- | --------- | ---------- |
clusterandoccurmostlyatthenortheasternpartsofthemain
NorthAtlanticstormtrack.AfifthofallETCsbelongtothe Browning (1990) classified ETCs based on their cloud pat-
terns,whereasFieldandWood(2007)groupedETCsbased
| second most | intense cluster | and occur mostly | at  | the start of |     |     |     |     |     |     |
| ----------- | --------------- | ---------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
the North Atlantic storm track. Finally, less than a 10th of ontheirlow-levelwindspeedandtheirwatervapourpathin
|     |     |     |     |     | an attempt | to understand | ETC | precipitation. | Attempts | have |
| --- | --- | --- | --- | --- | ---------- | ------------- | --- | -------------- | -------- | ---- |
allETCsbelongtothemostintenseclusterandoccuralmost
|     |     |     |     |     | also been | made to classify | ETCs | by  | their dynamical | forc- |
| --- | --- | --- | --- | --- | --------- | ---------------- | ---- | --- | --------------- | ----- |
equallyeverywhere.Thislastclusterincludesaclearmajor-
ing.Forexample,Thorncroftetal.(1993)andSchultzetal.
PublishedbyCopernicusPublicationsonbehalfoftheEuropeanGeosciencesUnion.

208 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
(1998)separatedETCsthatdevelopindifferentbackground ysisdatasetsbecauseETCsdifferintheunderlyingmodels,
flows,whereasPetterssenandSmebye(1971),Devesonetal. data assimilation methods, or the spatial and temporal res-
(2002), and Dacre and Gray (2009) grouped ETCs that are olution of the reanalyses (Wang et al., 2016). Furthermore,
dominatedeitherbylow-levelthermaladvectionorbyupper- bycomparingETCsinhistoricalsimulationstoETCsinre-
level vorticity advection. However, perhaps the most com- analysis datasets, it is possible to determine how accurately
monapproachtogrouporclassifyETCsisbasedonamea- climate models reproduce the current climate (Catto et al.,
sure of their intensity. Previous studies have grouped ETCs 2010;Priestleyetal.,2020).
eitherbytheirmaximum850hParelativevorticity(VO),of- Up to now, most studies have only quantified ETC inten-
tenfocusingonthestrongeststorms(e.g.Cattoetal.,2010; sityusingasinglemetric,or,ifmorethanonehasbeencon-
Sinclair et al., 2020), or by the decrease in minimum mean sidered, they have been used independently of each other.
sea level pressure (MSLP) over a 24h period, again com- Thismayresultinsomeinformationbeingomitted,aseach
monly focusing on the most rapidly deepening storms (e.g. metriconlygivesinformationaboutoneaspectofETCs.For
SandersandGyakum,1980;Reboitaetal.,2021). example, two ETCs with the same minimum MSLP may
Quantifying the intensity of any given ETC in a concise haveconsiderablydifferentwindgustsassociatedwiththem
yetaccuratemanneris,however,achallengingtask.Meteo- or be very different in size (Sinclair, 1997). Considering a
rologistsandclimatescientistshavefacedthischallengefor vastnumberanddiversityofmeasureswouldlikelygivean
many decades, and as such many methods and diagnostics in-depthdescriptionofallETCs,butthiswouldbecomeim-
exist, but there is no clear “correct” way or “best” diagnos- practicaltodealwith,hardtovisualize,andchallengingfor
tic. The most common metrics used to quantify ETC inten- forecastersandresearcherstoeasilycomprehend.Therefore,
sity,MSLPandVO,describethesynoptic-scaledynamicsof an optimal balance should be sought. In this context, auto-
theETCsandarestronglyrelatedtothehorizontalpressure mated and objective methods need to be applied to group
gradientandlarge-scalewinds.Historically,MSLPhasbeen ETCsusingmorethanonemetricorthespatialvariationin
provided by records from surface stations, while nowadays avariable.Forthispurpose,machinelearningmethodshave
VO is also commonly available from large gridded datasets gainedpopularityinrecentyearsduetotheirpredictiveand
suchasreanalyses.However,inmanycases,neitherthemin- classification abilities (e.g. Catto, 2018; Sinclair and Catto,
imumMSLPnormaximumVOcorrelateswellwiththeim- 2023;Wangetal.,2024).Ofthemanywaystoclassifymete-
pacts of a given ETC (e.g. Field and Wood, 2007; Roberts orologicaldatasets,unsupervisedlearning(i.e.clustering)is
et al., 2014; Sinclair and Catto, 2023). This is mainly due oftenprioritizedtogroupelementsofthedatasetwithoutany
to the presence of mesoscale features such as fronts, low- a priori knowledge. One such method is the Gaussian mix-
level jets, and convergence bands which strongly influence ture model (GMM) which has been used in meteorological
the wind and precipitation fields (Hewson and Neu, 2015). applications before (e.g. Vrac et al., 2005; Watanabe et al.,
Therefore,impact-relevantmetricswhichhavenodirectthe- 2020)butnotwidelyinthecontextofETCs.
oretical link to the traditional dynamically based metrics of ThepurposeofthestudyistoclassifyETCsusingmultiple
MSLP and VO have been introduced. Such metrics include measuresofintensity.Thefirstaimistoidentifyhowanum-
precipitationratesandaccumulations(Hawcroftetal.,2012), berofcommonlyusedETCintensitymeasuresrelatetoeach
sizes of wind footprints (Roberts et al., 2014), and storm other and then to identify the optimal metrics which, when
severityindices(Leckebuschetal.,2008a). consideredtogether,fullydescribetheintensityofETCs.The
Thoughchallenging,quantifyingtheintensityofETCsis second aim is to classify the wintertime ETCs in the North
crucial for climate studies. Firstly, many studies have used Atlantic and in the European region based on this subset of
reanalysisdatasetstoquantitativelydescribethestateofthe intensitymeasuresandtoquantifythecharacteristicsofeach
currentclimateintermsofnumber,location,andintensityof cluster.Thelastaimofthisstudyistoshowwheresomeof
ETCs (e.g. Hoskins and Hodges, 2002; Rudeva and Gulev, thepreviouslystudiedhigh-impactETCsoccurinourphase
2007; Jeglum et al., 2010; Laurila et al., 2021a). Secondly, spaceofintensityandETCclassification.
amanageablenumberofmetricswhichareeasytocompute Thepaperisstructuredasfollows.Section2explainshow
(concisemetrics)areneededtoidentifywhetheranytrendsin the dataset of ETC tracks and intensity measures was cre-
ETCintensityhavealreadyoccurredormaydointhefuture ated.Section3describesthemethodsusedintheanalysisof
as the climate changes. For example, simulations from the the data. Section 4 contains the results of the study which
Coupled Model Intercomparison Project (CMIP) have been are then discussed in Sect. 5. Finally, Sect. 6 concludes the
extensivelyanalysedtodeterminehowtheintensityofETCs results.
may change in the future (e.g. Zappa et al., 2013b; Colle
et al., 2013; Seiler and Zwiers, 2016; Chang, 2018; Priest-
ley and Catto, 2022; Dolores-Tesillos et al., 2022). Thirdly,
concise metrics of ETC intensity enable the comparison of
the representation of ETCs in different datasets. For exam-
ple, ETC climatologies can differ between different reanal-
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 209
2 CreationofETCintensitydataset
2.1 ERA5reanalysis
| ERA5 (Hersbach   |         | et al.,    | 2020)     | is an    | open-access |             | global |     |     |     |     |     |     |     |
| ---------------- | ------- | ---------- | --------- | -------- | ----------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| reanalysis       | dataset | provided   | by        | the      | European    | Centre      | for    |     |     |     |     |     |     |     |
| Medium-range     |         | Weather    | Forecasts | (ECMWF). |             | It has      | a hor- |     |     |     |     |     |     |     |
| izontal spectral |         | resolution | of        | T L 639, | which       | corresponds | to     |     |     |     |     |     |     |     |
| a grid spacing   | of      | 0.28°/31km |           | at the   | Equator     | on the      | native |     |     |     |     |     |     |     |
regularGaussiangridofERA5.WeuseERA5pressurelevel
dataandselectedsurfacefieldswith3-hourlyresolutionfrom
1979–2022tobothcreateETCtracks(Sect.2.2)andextract
theETCintensitymeasures(Sect.2.3).
2.2 ETCtracking Figure 1. Climatology of ETC track density for the 43 October–
|     |     |     |     |     |     |     |     | March seasons | in areas, | where | on average | at least | one track | per |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ----- | ---------- | -------- | --------- | --- |
ETC tracks are identified with the objective feature track- 5°sphericalcap(∼106km2)occursperseason.Themagentabox
boundedby80°W,40°E,30°N,and75°Nshowstheareainside
ingsoftwareTRACK(Hodges,1994,1995,1999b).TRACK
uses a Lagrangian approach of tracking individual cyclones whichtheETCsneedtohavetheirmaximumT42VO.Thehatching
|                |         |     |            |       |     |           |      | indicates | areas where the | average | monthly | mean | value of | surface |
| -------------- | ------- | --- | ---------- | ----- | --- | --------- | ---- | --------- | --------------- | ------- | ------- | ---- | -------- | ------- |
| by identifying | extrema |     | in a given | field | and | following | them |           |                 |         |         |      |          |         |
pressurebetweenOctober1979andMarch2022isbelow850hPa
throughtime.TotrackETCs,weusethe3-hourlyVOfieldat
andthetracksmaythereforebenon-physical.
thenativehorizontalresolutionofERA5whichisfirsttrun-
| cated to            | T42 spectral | resolution  |      | (310km  | at   | the Equator) | to        |           |                |       |        |           |        |       |
| ------------------- | ------------ | ----------- | ---- | ------- | ---- | ------------ | --------- | --------- | -------------- | ----- | ------ | --------- | ------ | ----- |
| exclude small-scale |              | features    | and  | ensure  | that | only         | synoptic- |           |                |       |        |           |        |       |
|                     |              |             |      |         |      |              |           | along the | North Atlantic | storm | track, | beginning | at the | east- |
| scale ETCs          | are          | identified. | Wave | numbers | less | than         | five are  |           |                |       |        |           |        |       |
erncoastofNorthAmericaandextendingnortheastwardto-
alsoremovedtofilteroutplanetary-scalewaves.Forthere-
|         |               |     |       |        |                |     |        | wards northern | Europe. | A local | maximum |     | in track | density |
| ------- | ------------- | --- | ----- | ------ | -------------- | --- | ------ | -------------- | ------- | ------- | ------- | --- | -------- | ------- |
| maining | wave numbers, |     | local | maxima | are identified |     | in the |                |         |         |         |     |          |         |
canalsobeseenintheMediterraneanbasin.Thisisdespite
| filtered VO | field | and a | nearest-neighbour |     | approach |     | is used |     |     |     |     |     |     |     |
| ----------- | ----- | ----- | ----------------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
thefactthatthetrackingalgorithmweuseandthefilterswe
| to connect | them | into ETC | tracks. | TRACK | produces |     | output |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ------- | ----- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
appliedaremoredesignedtoidentifyETCsinthemainstorm
whichconsistsofthehorizontallocation(longitudeandlat-
|            |           |     |         |     |        |          |      | tracks than | in the Mediterranean, |     | where | ETCs | tend | to be |
| ---------- | --------- | --- | ------- | --- | ------ | -------- | ---- | ----------- | --------------------- | --- | ----- | ---- | ---- | ----- |
| itude) and | magnitude | of  | the T42 | VO  | maxima | for each | time |             |                       |     |       |      |      |       |
smallerandshorter-lived(Campinsetal.,2011).Similardis-
stepineachETCtrack.
|     |     |     |     |     |     |     |     | tributions | of track density | during | winter | (DJF) | were | identi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ------ | ------ | ----- | ---- | ------- |
WefurtherfiltertheETCtracksusingthefollowingcrite-
fiedpreviouslybyPriestleyetal.(2020)inhistoricalCMIP6
ria:
simulationsandbyHoskinsandHodges(2002)inECMWF
1. Toexcludestationaryandshort-livedsystems,thetracks analyses using the same tracking algorithm. Campins et al.
(2011),AragãoandPorcù(2022),andDoiteauetal.(2024),
needtobeatleast1000kmlongandlastforatleast2d
(16timestepsinthe3-hourlydata). who focused on the Mediterranean region, determined the
GulfofGenoaasthelocationofmaximumtrackdensitydur-
2. Weaksystemsareexcludedbyusingaminimumthresh- ing DJF, whereas we have a maximum over the Tyrrhenian
oldof1×10−5s−1fortheT42VO.
Sea.Thisdifferencecanbeexplainedbythesensitivityofthe
trackingmethodinthisparticularbasin(seeFlaounasetal.,
| 3. Like | in Sinclair | and | Catto | (2023), | the | maximum | T42 |           |                    |     |             |        |           |     |
| ------- | ----------- | --- | ----- | ------- | --- | ------- | --- | --------- | ------------------ | --- | ----------- | ------ | --------- | --- |
|         |             |     |       |         |     |         |     | 2023, for | details). However, |     | the overall | number | of tracks | in  |
VOofthetrackmustoccur24haftergenesis(thefirst
theMediterraneanareainthesepreviousstudiesisinagree-
timestep)orlater.
mentwithourdistribution.
| 4. The | maximum | T42 | VO needs | to  | occur | inside | the area |                       |     |     |     |     |     |     |
| ------ | ------- | --- | -------- | --- | ----- | ------ | -------- | --------------------- | --- | --- | --- | --- | --- | --- |
|        |         |     |          |     |       |        |          | 2.3 Intensitymeasures |     |     |     |     |     |     |
80°Wto40°Einlongitudeand30°Nto75°Ninlati-
tude(themagentaboxinFig.1).
WeuseERA5reanalysisdatatocreateasetofintensitymea-
Intotal,inthe43extendedwinterswefind7361tracksmeet- suresforthetrackedETCs.Wereducetheamountofdatato
ingthesecriteria. obtainonevalueperintensitymeasurepertrack.Allthein-
Statistical diagnostic fields of ETC tracks, such as track tensitymeasurescanbecalculatedfromanyotherreanalysis
| density, are | calculated | by  | using | spherical | kernel | estimators |     | dataset. |     |     |     |     |     |     |
| ------------ | ---------- | --- | ----- | --------- | ------ | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
providedbyTRACK(Hodges,1996,1999a,2008).Figure1 Theintensitymeasurescanbedividedintotwocategories.
shows the climatology of track density of the 7361 ETC Thefirstcategoryconsistsofdynamicalmeasureswhichde-
tracks. In Fig. 1 we see that track density is the largest scribe physical aspects of ETCs and can be obtained from
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

210 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
thereanalysiswithnoorminimalpost-processing.Thesec- asthemaximumwithin6geodesicdegrees,butunlikeforthe
ond category consists of what we call impact-relevant mea- other three wind variables, we do not use an instantaneous
sures. These are diagnostic variables which are designed to value.Windgustishighlyvariableintime,andthereforewe
quantifytheaspectsofETCsthatpossiblyhavesocietalim- takethemaximumvalueoftheprevious3h.AsforMSLPa,
pacts. We emphasize that the impact-relevant measures do variousvalueswereexploredfortheradiusoftheareaforall
not necessarily directly translate into impacts but are based windspeedmeasures(notshown).
onvariableswhichquantifytheETCfeaturesthathavebeen
foundtocausethemostdamagetoinfrastructure. 2.3.2 Impact-relevantmeasures
Allintensitymeasuresandthedetailsofhowtheyarepro-
The first impact-relevant intensity measure is based on pre-
duced are described in detail in the following subsections
cipitation, which is an hourly accumulated field in ERA5.
(Sect.2.3.1and2.3.2),andthemeasuresaresummarizedin
We sum precipitation values over 3h to correspond to our
Table 1. Most of the variables are on the native ERA5 grid
timeintervalanddefineaprecipitationdiagnostic(PRECIP)
with the horizontal resolution of 0.28°. The exceptions are
as the average precipitation rate within an area, with a defi-
850hPa wind speed and 10m wind speed, which are on a
nitionadaptedfromSinclairandCatto(2023):
0.25°regularlongitude–latitudegrid.Thisissolelybecause
we already had these data locally available. However, this
1 (cid:88) m
difference in resolution is small and very unlikely to affect PRECIP= P A , (1)
i i
A
theresults. T i=1
whereP isthe3-hourlyprecipitationrateatgridpointi,A
2.3.1 Dynamicalmeasures i i
is the area of the grid point, m is the number of grid points
in which P exceeds a specific threshold value, and A is
ThebaselinefortheintensitymeasuresisVO,awidelyused i T
the total area of the m grid points. The precipitation is con-
measureofETCintensity.WeuseVOattheT42resolution
sidered and averaged only within a specific geodesic radius
directlyfromtheoutputofTRACK.Forthesakeofsimplic-
around the ETC centre. We use the same values as Sinclair
ity,werefertothelocationoftheVOmaximumastheETC
and Catto (2023) adapted to our grid and time resolution,
centre,althoughthephysicalcentreoftheETCisnotneces-
i.e. a geodesic radius of 12° and a minimum precipitation
sarilylocatedexactlyatthesamepoint.
rateof0.5mm(3h)−1.
ThenextdynamicalvariableweincludeisbasedonMSLP,
Next,weconstructawindfootprintdiagnostictomeasure
which along with VO is a widely used measure of ETC in-
theareaoftheETCwindfield.Thewindfootprint(WFP)is
tensity (e.g. Priestley et al., 2020). To account for the ef-
definedas
fect of the background environment on the MSLP values
(i.e. large-scale temporal variations and climatological de- m
(cid:88)
pendence of latitude; Anderson et al., 2003), we subtract a WFP= A i , (2)
monthlymeanvaluefromtheMSLPfieldtoobtainanMSLP i=1
anomaly(MSLPa).WeusetheMSLPafieldtofindthenear-
where A is the area of grid point i and m is the number
i
est local minimum around the VO maximum. This is done
of grid points within a given radius from the ETC centre in
byusingbilinearsplineinterpolationandasteepest-descent
which the 3-hourly maximum of 10m wind gust exceeds a
methodwithTRACK.ThelocalminimumMSLPaisfound
specificthreshold.Ageodesicradiusof10°wasfoundtobe
inside a circle centred around the VO maximum and has a
the best compromise for capturing winds associated with a
radius of 6 geodesic degrees (equivalent to about 670km).
givenETCfromanareaaslargeaspossiblewithoutcontam-
Variousvaluesweretestedfortheradius,and6geodesicde-
inating the WFP with winds related to neighbouring ETCs
grees was discovered to be the most suitable (not shown).
(see Fig. S2). For the threshold, we use a relatively small
This value is also used by e.g. Li et al. (2014). Most of the valueof15ms−1tohaveanon-zeroWFPformoderateETCs
MSLPa minima are within 100km of the VO maxima, and
as well. The value was chosen by considering thresholds
very few values are actually found at a distance of 670km
usedbyvariousnationalweatherservicesinEuropetoissue
(seeFig.S1intheSupplement).Forasmallnumber(3%)of
the lowest-level (yellow) wind warnings over land. In Fin-
maximumVOvalues,TRACKisunabletofindanassociated landthisvalueis15ms−1 insummerand20ms−1 inwinter
MSLPavalue.TheseETCsareomittedfromthedataset.
(FMI, 2018), whereas the corresponding values in Norway
Finally, we include winds from multiple levels as dy- are 17 and 19ms−1 (METNorway, 2021). In Ireland this
namical intensity measures. For a comprehensive overview value is 25ms−1 (MetÉireann, 2024), whereas in Germany
of winds associated with ETCs, we include the maximum the threshold is 14ms−1 (DWD, 2015). The low threshold
windspeedat850hPa(WS850),925hPa(WS925),and10m
selectedhereisalsojustifiedbasedonthefactthatinERA5,
(WS10)within6geodesicdegreesfromtheVOcentre,ara-
the wind gust may be underestimated in some areas (Chen
dius also used by Zappa et al. (2013a) and Gramcianinov
etal.,2024;Minolaetal.,2020).
etal.(2020).Wealsoincludethewindgustsat10m(FG10)
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 211
Table1.Summaryofall11intensitymeasures.Thecolumnsarethefullname,abbreviatedname,thetypeofvalueextracted,themaximum
distancefromtheVOmaximum(ingeodesicdegrees)towhichthevaluesaresearchedfor,andtimestepwithrespecttothetimeofVO
maximum(inhours).Thehorizontallineseparatesthemeasuresintodynamicalandimpact-relevantones.
|     |     | Measure                     |     |     |     | Abbreviation |     | Type                |     |     | Distance Timestep |     |     |
| --- | --- | --------------------------- | --- | --- | --- | ------------ | --- | ------------------- | --- | --- | ----------------- | --- | --- |
|     |     | 850hParelativevorticity     |     |     |     | VO           |     | MaximumT42          |     |     | 0 0               |     |     |
|     |     | Meansealevelpressureanomaly |     |     |     | MSLPa        |     | Nearestlocalminimum |     |     | 6 0               |     |     |
|     |     | 850hPawindspeed             |     |     |     | WS850        |     | Maximum             |     |     | 6 0               |     |     |
|     |     | 925hPawindspeed             |     |     |     | WS925        |     | Maximum             |     |     | 6 0               |     |     |
|     |     | 10mwindspeed                |     |     |     | WS10         |     | Maximum             |     |     | 6 0               |     |     |
|     |     | 10mwindgust                 |     |     |     | FG10         |     | Maximum             |     |     | 6 0               |     |     |
Avg.where≥0.5mm(3h)−1
|     |     | Precipitation |     |     |     | PRECIP |     |     |     |     | 12 −12 |     |     |
| --- | --- | ------------- | --- | --- | --- | ------ | --- | --- | --- | --- | ------ | --- | --- |
Accumulatedprecipitation PRECIPacc Avg.where≥0.5mm(3h)−1 12 Accumulated
|     |     |                    |     |     |     |     |     | Areawheregust≥15ms |     | −1  |      |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | ------------------ | --- | --- | ---- | --- | --- |
|     |     | Windfootprint      |     |     |     | WFP |     |                    |     |     | 10 0 |     |     |
|     |     | Stormseverityindex |     |     |     | SSI |     | Sumoverarea        |     |     | 10 0 |     |     |
Accumulatedstormseverityindex SSIacc Sumoverarea 10 Time-integrated
Finally,weincludeastormseverityindex(SSI)toquantify by implementing a fixed minimum threshold. For impactful
thepossibleimpactfromwindassociatedwithETCs.Differ- events in the Mediterranean region, Nissen et al. (2010) re-
ent SSI metrics have been previously used to successfully quired a minimum duration of 18h and minimum affected
areaofaround36000km2.Wedonotuseaminimumwind
| estimate |     | the societal | impact | of  | ETCs (Klawa |     | and Ulbrich, |     |     |     |     |     |     |
| -------- | --- | ------------ | ------ | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
2003; Pinto et al., 2007; Leckebusch et al., 2007). We use gustorareathresholdfortheSSI,sincesuchanapproachis
anSSImetricadaptedfromLeckebuschetal.(2008a).Here, alreadyevaluatedbytheWFP,whichisbasedonafixedgust
| SSIiscalculatedateachgridpointwithinacircularareawith |     |     |     |     |     |     |     | threshold. |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
afixedradiusaroundtheETCcentrethroughouttheETClife For each ETC track, we restrict the analysis to only one
cycle.OurdefinitionofSSIisasfollows: time step per intensity measure. For all intensity measures
|     |     |     |     |     |     |     |     | other than | PRECIP, | the | value at the | time of maximum | VO  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | ------------ | --------------- | --- |
m
1 (cid:88) v i along the track is chosen, since the maximum value of the
| SSI= |     |     | max(0, | −1)3A | ,   |     |     | (3)                                                |     |     |     |     |     |
| ---- | --- | --- | ------ | ----- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
|      | A   |     | v      |       | i   |     |     |                                                    |     |     |     |     |     |
|      |     | ref |        | 98,i  |     |     |     | intensitymeasuresalsooccursatthesametimeoratthead- |     |     |     |     |     |
i=1
jacenttimesteponaverage(seeFig.S5).Themaximumpre-
| wherev | i   | isthemaximum10mwindgustwithin3handv |     |     |     |     |     | 98,i |     |     |     |     |     |
| ------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
cipitationrateoccursonaverage12hbeforethetimeofmax-
istheclimatological98thpercentilevalueof10mwindgust
|     |     |     |     |     |     |     |     | imum VO | (see Fig. | S5f). | For this reason, | PRECIP | is evalu- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----- | ---------------- | ------ | --------- |
atgridpointi,A i istheareaofthegridpoint,misthenum- atedatthistimestep.
| ber | of grid | points | within | a certain | geodesic | radius | from | the |     |     |     |     |     |
| --- | ------- | ------ | ------ | --------- | -------- | ------ | ---- | --- | --- | --- | --- | --- | --- |
WealsoincludeaccumulatedversionsofPRECIPandSSI.
| ETC | centre, | and | A is | the area | of the | largest | point in | the                                                 |     |     |     |     |     |
| --- | ------- | --- | ---- | -------- | ------ | ------- | -------- | --------------------------------------------------- | --- | --- | --- | --- | --- |
|     |         |     | ref  |          |        |         |          | Weconstructanaccumulatedprecipitationmeasure(PRECI- |     |     |     |     |     |
grid (at the Equator). Scaling SSI values with the relative Pacc) by summing together all PRECIP values along each
| area | of each | grid | point | ensures | that an | ETC | is considered |           |                |     |             |          |          |
| ---- | ------- | ---- | ----- | ------- | ------- | --- | ------------- | --------- | -------------- | --- | ----------- | -------- | -------- |
|      |         |      |       |         |         |     |               | track and | an accumulated |     | SSI measure | (SSIacc) | by time- |
moreseverebecausetheimpactedareaislarger,independent integratingsuccessiveSSIvaluesalongeachtrack.
| of  | latitude. | We  | use a geodesic |     | radius of | 10° to | compute | the |     |     |     |     |     |
| --- | --------- | --- | -------------- | --- | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
SSI.Thisvaluewasdiscoveredtobethemostsuitablebased
| onasimilaranalysisastheoneperformedfortheWFP(see |     |     |     |     |     |     |     | 3 Methods |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
Fig.S4).
|       | The climatology |      | of 10m  | wind | gust     | is calculated | for       | the                     |     |     |     |     |     |
| ----- | --------------- | ---- | ------- | ---- | -------- | ------------- | --------- | ----------------------- | --- | --- | --- | --- | --- |
|       |                 |      |         |      |          |               |           | 3.1 Correlationanalysis |     |     |     |     |     |
| whole | period          | from | October | 1979 | to March | 2022,         | including |                         |     |     |     |     |     |
the summer months as well. We include summer months in We use two different correlation metrics to quantify co-
theclimatologysincethejustificationforusingthe98thper- occurrencerelationshipsbetweentheintensitymeasures.The
centileasathresholdforthewindgustisbasedonthefind- firstoneisthewidelyusedPearson’scorrelationcoefficient,
ingthatdamagefromwindsoccurslocallyon2%ofalldays r,whichevaluateslineardependence.Thesecondoneismu-
(Palutikof and Skellern, 1991). In some regions (e.g. parts tual information (MI), which we use to quantify non-linear
of Scandinavia, in the Mediterranean, or southeastern Eu- dependencies. MI is a measure of dependence between two
rope)theclimatological98thpercentilevaluesof10mwind randomvariablesbasedontheirjointandmarginalentropies
gust are quite small (Fig. S3) and unlikely to cause severe (CoverandThomas,2006).Inotherwords,itquantifieshow
damage. Karremann et al. (2014) avoided this discrepancy much information can be obtained about one random vari-
between the definition of SSI and actual wind gust values able by observing another random variable. MI has values
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

212 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
∞),
in the interval [0, but it can be converted into a corre- cluster may be represented as a multidimensional Gaussian
lationcoefficient,ρ,bynormalizingittoarange[0,1].The probabilitydensityfunctionextendingthroughoutthewhole
normalizationiscomputedusingthePythonpackageennemi featurespace,inourcasethesmallsubsetofintensitymea-
(Laarneetal.,2021,2022)asfollows: suresproducedbythesPCAanalysis.Themaindrawbackof
theGMMisthatthenumberofclustershastobeinput,and
(cid:112)
| ρ= 1−exp(−2MI). |     |     |     |     |     | (4) |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theoptimalnumberofclusterscannotbeknowninadvance.
|     |     |     |     |     |     |     | The elbow | method | is used | to  | disambiguate | this | choice | and |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------- | --- | ------------ | ---- | ------ | --- |
Using two different kinds of correlation metrics is bene- select the number of clusters which (1) maximizes Silhou-
| ficial because | in addition | to  | quantifying | the | strength | of the |            |            |     |           |       |     |          |     |
| -------------- | ----------- | --- | ----------- | --- | -------- | ------ | ---------- | ---------- | --- | --------- | ----- | --- | -------- | --- |
|                |             |     |             |     |          |        | ette score | (Shahapure | and | Nicholas, | 2020) | and | (2) does | not |
relationship,wecanlearnaboutitstypeaswell.BecauseMI
fallintheover-fittinglearningplateau(i.e.whentheSilhou-
isabletoquantifynon-linearrelationshipsinadditiontolin-
ettescoreisconstant).Inotherwords,theoptimalnumberof
| earones,similarvaluesofr |     |     | andρ indicatealinearrelation- |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
clustersisthecaseavoidingbothunder-andover-fitting.
shipbetweentwovariables,whereashigherρ thanr values We use the GMM (scikit-learn’s GaussianMixture; Pe-
indicatearelationshipwithanon-linearcomponent.
dregosaetal.,2011)onthereducedsubsetofintensitymea-
|     |     |     |     |     |     |     | sures selected |     | by our sPCA | method. | To  | choose | the | correct |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------- | --- | ------ | --- | ------- |
3.2 Principalcomponentanalysis
numberofclusterstobefound,wefirstusetheelbowmethod
|     |     |     |     |     |     |     | to select | two values | to  | test before | the over-fitting |     | plateau | is  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- | ---------------- | --- | ------- | --- |
Principalcomponentanalysis(PCA)aimstofindanorthog-
|             |                |     |                |     |              |      | reached, | as shown | in Fig. | S6. | Then, we | use | the following |     |
| ----------- | -------------- | --- | -------------- | --- | ------------ | ---- | -------- | -------- | ------- | --- | -------- | --- | ------------- | --- |
| onal linear | transformation |     | that maximizes |     | the variance | pro- |          |          |         |     |          |     |               |     |
jectedontoeachofthenewlyfoundaxes.Thismethodisused stability test to refine our decision to one value. Our stabil-
|     |     |     |     |     |     |     | ity test aims | to  | verify if | the clusters’ | centroids |     | predicted | by  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------------- | --------- | --- | --------- | --- |
inallfieldsofscience,includingmeteorology(Statheropou-
severalinstancesoftheGMMareintercomparable.Wefirst
| los et al., | 1998; Nagendra |     | and Khare, | 2003), | and | has also |         |               |     |          |         |     |           |      |
| ----------- | -------------- | --- | ---------- | ------ | --- | -------- | ------- | ------------- | --- | -------- | ------- | --- | --------- | ---- |
|             |                |     |            |        |     |          | compute | the Euclidean |     | distance | between | the | reference | cen- |
beenappliedinstudiesoncyclones(Louetal.,2012;Nakajo
|     |     |     |     |     |     |     | troids and | the | centroids | predicted | by 1000 | other | instances. |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --------- | ------- | ----- | ---------- | --- |
etal.,2014;Chenetal.,2019).Oneofthemainfeaturesof
PCA is its ability to reduce the dimensionality of a given Then, the arguments of the minimum of the Euclidean dis-
tancesaretakenforeachpredictedclusters.Ifthearguments
problembyignoringtheaxesexplaininganegligibleamount
|     |     |     |     |     |     |     | of the minimum |     | are not | repeating, | it means |     | a permutation |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ---------- | -------- | --- | ------------- | --- |
oftheoriginalvariance.However,oneofitsmaindrawbacks
oftheclustersisabletosuccessfullycomparetwoinstances
istheinterpretabilityoftheresultsaseachaxisisexpressed
|             |             |     |              |         |        |       | of the GMM. | In  | other | words, | we test the | sensitivity |     | of our |
| ----------- | ----------- | --- | ------------ | ------- | ------ | ----- | ----------- | --- | ----- | ------ | ----------- | ----------- | --- | ------ |
| by a linear | combination | of  | the original | feature | space, | often |             |     |       |        |             |             |     |        |
mobilizing the entire space. Sparse PCA (sPCA) alleviates cluster analysis to the chosen number of clusters. A stabil-
ityscorehasbeendefinedastheaveragenumberofclusters
thisissuebyproposingaPCAwithsparseloadings,i.e.set-
whicharenotintercomparablebetweentwoinstancesofthe
| ting some | of the coefficients |     | in the | linear | expression | of the |     |     |     |     |     |     |     |     |
| --------- | ------------------- | --- | ------ | ------ | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
GMM.Thus,astabilityscoreofzeroisconsideredoptimal.
| PCA’s axes | to zero | (Zou et | al., 2006; | Zou | and Xue, | 2018). |     |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | ---------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
StabilityscoresareshowninTableS1intheSupplement.As
| However, | sPCA is a | lossy | compression | technique |     | with an |     |     |     |     |     |     |     |     |
| -------- | --------- | ----- | ----------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
n=4
importantdependencyonthedimensionoftheprojectivehy- a result, we select as our optimal number of clusters
|     |     |     |     |     |     |     | as this value | falls | in the | elbow | criteria | and has | the | lowest |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------ | ----- | -------- | ------- | --- | ------ |
perplane.
stabilityscore.
| Consequently,  | in  | this study | we            | will | guide the      | sPCA |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ------------- | ---- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| by a classical | PCA | analysis   | (respectively |      | scikit-learn’s |      |     |     |     |     |     |     |     |     |
SparsePCAandPCA;Pedregosaetal.,2011).Weapplythe
| PCA to estimate | the                   | explained | variance | against  | the       | number | 4 Results |     |     |     |     |     |     |     |
| --------------- | --------------------- | --------- | -------- | -------- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| ofprincipal     | components(PCs).Then, |           |          | weselect | thenumber |        |           |     |     |     |     |     |     |     |
4.1 Relationshipsbetweenintensitymeasures
| of components | which       | explains   | more       | than    | 90% of   | the vari- |               |        |               |           |                |               |           |     |
| ------------- | ----------- | ---------- | ---------- | ------- | -------- | --------- | ------------- | ------ | ------------- | --------- | -------------- | ------------- | --------- | --- |
| ance. This    | number of   | components |            | is then | used as  | the main  |               |        |               |           |                |               |           |     |
|               |             |            |            |         |          |           | Distributions | of     | all 11        | intensity | measures       |               | are shown | in  |
| parameter     | of the sPCA | and        | is applied | to      | the same | dataset.  |               |        |               |           |                |               |           |     |
|               |             |            |            |         |          |           | Fig. 2.       | We see | in Fig.       | 2a–f      | that the       | dynamical     | intensity |     |
| Therefore,    | we minimize | the        | risk of    | losing  | too much | infor-    |               |        |               |           |                |               |           |     |
|               |             |            |            |         |          |           | measures      | have   | Gaussian-like |           | distributions. | Distributions |           | of  |
mationwithPCAbyconservingasatisfyinginterpretability
|     |     |     |     |     |     |     | VO, MSLPa, | and | WS850 | (Fig. | 2a–c) | are slightly | skewed |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ----- | ----- | ------------ | ------ | --- |
withsPCA.BasedonthecorrelationsandthesPCAresults,
weselectareducedsubsetofintensitymeasurestouseasin- towards more intense values, whereas WS925, WS10, and
FG10havemoresymmetricdistributions(Fig.2d–f).Similar
putfortheclusteranalysis.Thissubsetisconceivedtoreduce
distributionsforthesemeasureshavebeenpreviouslyfound
informationredundancywhilstmaintainingtheinterpretabil-
|     |     |     |     |     |     |     | by e.g. | Bengtsson | et al. | (2006, | 2009), Zappa |     | et al. (2013a), |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ------ | ------------ | --- | --------------- | --- |
ityoftheoriginalsetofmeasures.
|     |     |     |     |     |     |     | and Gramcianinov |     | et al. | (2020). | Compared |     | to the dynam- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------- | -------- | --- | ------------- | --- |
3.3 Clusteranalysis ical intensity measures, the distributions of the impact-
|     |     |     |     |     |     |     | relevant | measures | are | much less | Gaussian-like |     | (Fig. | 2g–k). |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --------- | ------------- | --- | ----- | ------ |
A cluster analysis using the GMM aims to fit several mul- Out of these, PRECIP has the most Gaussian-like distribu-
tivariate Gaussian distributions to a dataset. As such, each tion (Fig. 2g) but is more positively skewed than any of the
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 213
dynamical measures’ distributions. With a slightly different sures in the first group. This can be explained by the dif-
definition, Zappa et al. (2013b) found a similar distribution ferent shapes of the distributions in Fig. 2. For both SSI
forprecipitation.ThedistributionofPRECIPacc(Fig.2h)is and precipitation measures, the largest values of Pearson’s
evenmorepositivelyskewedthanthatofPRECIPasthedif- r (around 0.5) are between the corresponding accumulated
ferencesbetweenETCsareemphasizedwiththeaddedeffect and instantaneous versions. For any of the measures in the
ofthedurationofthetrack.WFP(Fig.2i)hasaverydifferent second group, the strongest correlation with a measure in
distributiontotheotherintensitymetricswithalargepeakat the first group is between PRECIP and VO, with a value
thesmallerendofthedistributionandisveryflatalmostun- of r =0.47. This may be explained by precipitation-related
til the largest values. Only around 80 ETCs have a WFP of diabatic heating producing a low-level potential vorticity
zero(notshown),whichmeansthatthefirstbinhasthemost anomaly which feeds back to the 850hPa relative vorticity
ETCswithnon-zeroWFP.TheWFPvaluesdecreaserapidly (DavisandEmanuel,1991).
atthelargeendofthedistributionastheradiusthresholdis Correlations between SSI and precipitation measures are
reached (the theoretical maximum value of WFP is around the weakest in terms of r and among the weakest in terms
3.9×106km2).TheshapesoftheSSIdistributionsareeven
|     |     |     |     |     |     |     |     | ofρ.Forthesemeasures,theρ |     |     |     | valuesareconsistentlylarger |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- |
moreextreme(Fig.2j–k,shownonsemi-logaxes).Thecube thanr values,andthedifferenceislargerthanformeasures
ofthewindexceedanceinEq.(3)forSSIemphasizesdiffer- inthefirstgroup.Therelationshipsarethusmorenon-linear.
ences between small and large values. Therefore, there are ThedifferenceisalsolargerforSSIthanprecipitationmea-
many very small values and few large values. For example, sures.Thisisnotunexpectedgiventhehighlynon-Gaussian
thereareoutlierETCsinwhichthevaluesofSSIandSSIacc distribution of the SSI measures. However, the ρ values are
aremorethantwicethevalueofthenextlargestone.These stillnotaslargeasforthefirstgroup,withthestrongestcor-
outlierETCsarethe1993StormoftheCentury(Huoetal., relationcoefficientsfromMIbetweenFG10andSSIhaving
| 1995) and | ex-hurricane |     | Wilma | (Pasch | et al., | 2006), | respec- | ρ=0.71. |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ----- | ------ | ------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tively.
|                |     |             |     |             |              |     |        | 4.2 PCAandsparsePCA |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | ----------- | ------------ | --- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| We investigate |     | the Pearson |     | correlation | coefficients |     | (r) in |                     |     |     |     |     |     |     |     |
Fig.3aandcorrelationcoefficientsfromMI(ρ)inFig.3bfor
relationshipsbetweenall11intensitymeasures.Therelation- TheresultofthePCAisobtainedwiththe11intensitymea-
suresasinput(Fig.4).Theweightsoftheintensitymeasures
shipscanberoughlydividedintotwogroupsbasedontheir
|     |     |     |     |     |     |     |     | in the first | four | PCs (Fig. | 4b–e) | indicate | that | there | are mul- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | ----- | -------- | ---- | ----- | -------- |
strength:thefirstgroupcontainsthesixdynamicalmeasures
|          |         |        |     |         |     |         |          | tiple measures |     | with a   | contribution | of    | similar  | magnitude | in  |
| -------- | ------- | ------ | --- | ------- | --- | ------- | -------- | -------------- | --- | -------- | ------------ | ----- | -------- | --------- | --- |
| and WFP, | and the | second | one | the two | SSI | and two | precipi- |                |     |          |              |       |          |           |     |
|          |         |        |     |         |     |         |          | each PC.       | For | example, | in the       | first | PC (Fig. | 4b) WFP   | has |
tationmeasures.AllthePearsoncorrelationsarestatistically
significant(notshown). thelargestweight,butVO,MSLPa,andallwindspeedmea-
|               |              |          |              |         |             |           |            | sures have  | similar,  | non-negligible |          | weight.     | In    | Fig. 4a,  | which     |
| ------------- | ------------ | -------- | ------------ | ------- | ----------- | --------- | ---------- | ----------- | --------- | -------------- | -------- | ----------- | ----- | --------- | --------- |
| Correlations  |              | between  | all measures |         | in the      | group     | consist-   |             |           |                |          |             |       |           |           |
|               |              |          |              |         |             |           |            | shows ETCs  | projected |                | onto the | first       | three | PCs of    | the PCA   |
| ing of the    | dynamical    | measures |              | and WFP | are         | strong,   | with a     |             |           |                |          |             |       |           |           |
|               |              |          |              |         |             |           |            | space, this | can       | be seen        | in the   | even spread |       | of points | all over  |
| Pearson’s     | r of         | at least | 0.7 for      | every   | combination |           | (Fig. 3a). |             |           |                |          |             |       |           |           |
|               |              |          |              |         |             |           |            | the axes.   | Based     | on the         | result   | of the      | PCA,  | it is not | straight- |
| The strongest | correlations |          | are          | between | the         | four wind | speed      |             |           |                |          |             |       |           |           |
measures (WS850, WS925, WS10, and FG10). A particu- forward to determine which intensity measures have redun-
dancybetweenthemandwhichdonot.Therefore,itisdiffi-
| larly strong | correlation |     | is between | WS10 | and | FG10, | with a |     |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | ---------- | ---- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
culttouseonlythePCAfordimensionalityreductioninthe
| Pearson’sr | of0.97.Thisissurprising,giventhatintheInte- |     |     |     |     |     |     |          |          |          |     |         |     |           |           |
| ---------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | --- | ------- | --- | --------- | --------- |
|            |                                             |     |     |     |     |     |     | original | dataset. | However, | we  | can use | the | fact that | the first |
gratedForecastSystem,whichisusedtoproduceERA5,the
|     |     |     |     |     |     |     |     | four PCs | of the | PCA contain |     | 94% of | explained | variance | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --- | ------ | --------- | -------- | --- |
parameterizationforwindgustsincludesatermtorepresent
the contribution of convective downdraughts and a term to the dataset to constrain the sPCA. The result of the sPCA
|             |         |            |     |             |     |         |      | constrained | to  | 4 PCs with | the | 11 intensity |     | measures | as in- |
| ----------- | ------- | ---------- | --- | ----------- | --- | ------- | ---- | ----------- | --- | ---------- | --- | ------------ | --- | -------- | ------ |
| account for | surface | roughness, |     | in addition | to  | the 10m | wind |             |     |            |     |              |     |          |        |
putisshowninFig.5.AsopposedtotheresultofthePCA,
speedterm(BechtoldandBidlot,2009).Theverystrongcor-
relation between WS10 and FG10 found here indicates that now each of the four PCs consists almost completely of ei-
|     |     |     |     |     |     |     |     | ther a single | intensity |     | measure | or a | group | of similar | inten- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ------- | ---- | ----- | ---------- | ------ |
theconvectivedowndraughtsandsurfacefrictioncontribute
|     |     |     |     |     |     |     |     | sity measures. |     | We see | this in | their | larger weight | compared |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------- | ----- | ------------- | -------- | --- |
aminimalamounttothewindgustsinETCsinERA5.The
|         |              |     |           |       |             |     |         | to the other | measures, |     | which | have a | weight | close | to or ex- |
| ------- | ------------ | --- | --------- | ----- | ----------- | --- | ------- | ------------ | --------- | --- | ----- | ------ | ------ | ----- | --------- |
| weakest | correlations | in  | the first | group | of measures |     | are be- |              |           |     |       |        |        |       |           |
actlyzerointhesamePC(Fig.5b–e).ThePCscantherefore
| tween MSLPa |     | and the | wind | speed | measures, | with | r val- |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ---- | ----- | --------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
uesbetween0.71and0.76.CorrelationcoefficientsfromMI be labelled as mainly consisting of (1) the four dynamical
|     |     |     |     |     |     |     |     | wind speed | measures | (WS850, |     | WS925, | WS10, | and | FG10), |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------- | --- | ------ | ----- | --- | ------ |
(Fig.3b)areconsistently,yetonlyslightly,largerthanPear-
|     |     |     |     |     |     |     |     | (2) PRECIP, | (3) | WFP, | and (4) | VO and | MSLPa. | Minor | con- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ------- | ------ | ------ | ----- | ---- |
son’sr forthemeasuresinthefirstgroup.Thesmalldiffer-
tributionsintermsofweightcomefrom(1)VO,(2)PRECI-
| ences between |     | the two | correlation | coefficients |     | suggest | that |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ----------- | ------------ | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
PaccandVO,(3)WS10andFG10,and(4)WS850.Theonly
therelationshipsarelinear.
Relationshipsofthemeasuresinthesecondgroup,SSIand measureswhichhavenoweightinanyofthePCsarethetwo
SSImeasures.
| precipitation | measures, |     | are weaker | than | those | of  | the mea- |     |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ---------- | ---- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

214 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
Figure2.Distributionsofintensitymeasuresattheselectedtimesalongthetracks(seetextinSect.2.3andTable1fordetails).Notethat
panels(j)and(k)areshownonthelogarithmicyaxes.
Figure3.(a)Pearson’sr and(b)MIcorrelationcoefficientsρ fortheETCintensitymeasures.AllvaluesofPearson’sr involvingMSLPa
arenegative,butanabsolutevalueisshownforthemtoaidcomparisonwithothercoefficients.
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 215
Figure 4. (a) ETCs projected onto the PCA space. PC1 and PC2 are the horizontal and vertical axes, respectively, and PC3 is shown in
colours.Insetinthebottomleftcornershowscumulativeproportionofexplainedvariance(percent)asafunctionofnumberofPCs.Inset
inthebottomrightcornershowsloadingsofPC1andPC2asvectors.(b–e)WeightsofinputmeasuresinthefirstfourPCs.Weightswith
largermagnitudesindicatemorecontributionofthespecificintensitymeasuretothePC.Thenumbersinparenthesesindicatetheproportion
oftotalexplainedvarianceinagivenPC.
Figure5.(a)ETCsprojectedontothesPCAspace.PC1andPC2arethehorizontalandverticalaxes,respectively,andPC3isshownin
colours.InsetinthebottomrightcornershowsloadingsofPC1andPC2asvectors.Thepercentagesindicatehowlargeaproportionofall
tracksfallsintoeachsector(onwhichsideofthemean,i.e.negativeorpositivevalueofPC).Thelabels“calm”and“windy”,“dry”and
“rainy”,and“small”and“big”refertothequalitativeinterpretationofPC1,PC2,andPC3,respectively.(b–e)Weightsofinputmeasuresin
thefourPCs.
The PCs now have a straightforward physical interpreta- (the smallest Euclidean distance from origin) has a WS850
tion,andwecanlabeltheaxesinthesPCAspaceaccording value of 30.2ms−1, PRECIP of 2.3mm(3h)−1, WFP of
to ETC features quantified by the most important intensity 1.7×106km2, and VO of 6.8×10−5s−1. Compared to the
measures in the PCs (e.g. windiness). In Fig. 5a the ETCs projectionofthePCAspaceinFig.4a,theETCsfallintothe
are shown projected onto the first three PCs of the sPCA sPCAspacemuchlesssymmetrically.Thestrongcorrelation
spaceinwhichPC1goesfrom“calm”to“windy”,PC2goes betweenthewindspeeds(PC1)andWFP(PC3)isevidentas
from“dry”to“rainy”,andPC3goesfrom“small”to“big”. mostofthetracksareonthesamesideofthemeanofthePC
For reference, the most “average” ETC in the sPCA space (value 0) for PC1 and PC3 (either calm and small or windy
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

216 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
and big). Precipitation (PC2) has a weaker correlation with 4.3.1 ETCintensitymeasures
thewindsandWFP,whichcanbeseeninthemoreevendis-
tribution of positive and negative PC3 values on either side Distributions of all 11 intensity measures for ETCs in each
ofthePC2meanthanofthePC1mean.However,morethan of the clusters are shown in Fig. 6. For each intensity mea-
halfoftheETCs(56%)areinsectorsinwhichallthethree sure,thedistributionsaresignificantlydifferentbetweenthe
PCsareonthesamesideofthemean,i.e.inthequalitative four clusters at the 5% level based on the Mann–Whitney
binaryrepresentationofthesPCAspaceeithercalm,dry,and U test (Mann and Whitney, 1947, not shown). The shapes
small(32%)orwindy,rainy,andbig(24%). of the intensity measures’ distributions in different clusters
WeusetheresultofthesPCAtoreducethenumberofnec- arelargelysimilarinnaturetothefulldistributionsshownin
essary intensity measures in the dataset for the comprehen- Fig. 2. For example, in each cluster the distribution of VO
sivedescriptionofETCintensity.Despitestrongcorrelations isGaussian-like(Fig.6a).Intermsofboththemeanandthe
betweenthewinds,WFP,andVO,weretainthemseparately median, the average magnitude of VO in the clusters in de-
in the reduced set as they appear each on their own in the creasingorderisHighSSI,Intense,AvgMST,andWeak.All
sPCA.Wechoosetokeepfiveintensitymeasuresinthefinal distributionsofWS850(Fig.6b)andWS10(Fig.6h)arealso
setforthecomprehensiveandnon-redundantrepresentation Gaussian-likewithsimilarshapesbetweentheclusters.The
ofETCintensity. order of the average magnitudes is the same as for VO. For
MSLPa(Fig.6f)andWS925(Fig.6g)theshapesofHighSSI,
1. WS850.Allfourwindspeedmeasuresarehighlycorre- Intense,andAvgMSTdistributionsaremoresimilarbetween
latedwitheachotherandgroupedinPC1ofthesPCA. eachotherthanforthepreviouslymentionedintensitymea-
WS850ischosenbecauseofitslinktoVOinPC4. sures. However, the order of the average magnitudes of the
intensitymeasuresisthesame.Finally,clustersHighSSIand
2. PRECIP.PRECIPisfromsPCA. Intensebothhavebroad,non-Gaussiandistributionswithal-
mostflattops(Fig.6i).Theorderoftheaveragemagnitudes
3. WFP.WFPisfromsPCA. is,however,thesameasfortheotherdynamicalmeasures.
Like the full distributions in Fig. 2, the distributions of
4. VO. VO is from sPCA. It is preferred over MSLPa be- the impact-relevant intensity measures in the clusters are
causeofitsminorweightinPC1andPC2. lessGaussian-likethanthoseofthedynamicalmeasures.In
the distributions of WFP for the different clusters, the or-
5. SSI. Although SSI has zero weight in sPCA, it is in- der of average magnitudes is the same as in the dynami-
cluded since it is weakly correlated with the other in- cal measures, but there is more overlap between the three
tensitymeasuresandhasamorenon-linearrelationship most intense clusters (Fig. 6d). For PRECIP, clusters Weak
withthem.Itcanthereforebeusedtobetterseparatethe andAvgMSThavenarrowGaussian-likedistributions,while
featurespace(non-linearly). distributions of clusters Intense and HighSSI are positively
skewed (Fig. 6c). The PRECIP distributions largely over-
4.3 Clusteranalysis lap,especiallybetweenclustersIntenseandHighSSI.Infact,
PRECIP is the only intensity measure for which the mean
The cluster analysis was performed using the method de- valueisthelargestforclusterIntenseinsteadofclusterHigh-
scribed in Sect. 3.3 with the reduced set of intensity mea- SSI. SSI distributions of clusters Weak and AvgMST heav-
suresidentifiedinSect.4.2asinput.Thenumberofclusters ily overlap and comprise most of the smallest SSI values
was chosen to be four. Each ETC is assigned into the most (Fig. 6e). There is little overlap with the other two clusters,
probableclusterbasedonthemultivariateGaussianprobabil- asmostSSIvaluesinclusterIntensearelargerthananyvalue
itydensitydistribution.Theclustersarenamedbasedonthe inthetwoweakerclusters(WeakandAvgMST),andalmost
average magnitudes of the input measures and the average allvaluesinclusterHighSSIarelargerthananyvalueinthe
geographicallocationsofETCsinthem.Theseareexplained other three clusters. These three distinct ranges of SSI val-
indetailinthefollowingsections.Thefourobtainedclusters ues areprobably aneffect ofthe highlyskewed distribution
aredenotedas ofSSI,andtheyindicatethatSSIcreatesalotofseparation
between the clusters. For SSIacc there is a clear separation
1. HighSSI (proportion of total ETCs in the cluster: between the mean values in the clusters, but there is much
8.57%) moreoverlapbetweendistributionsthanforSSI.
2. Intense(21.46%) 4.3.2 ETCcharacteristics
3. AvgMST(averagemainstormtrack,44.42%)and In addition to the intensity measures, we compare vari-
ous ETC characteristics between the four clusters. Figure 7
4. Weak(25.54%). showsthedistributionsoflatitudeofgenesis,meridionaldis-
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 217
Figure6.ProbabilitydensitiesoftheintensitymeasuresinETCclusters.Thelegendineachpanelisorderedbasedonthemeansofthe
distributionsfromlargesttosmallest.Notethatpanels(e)and(k)areshownonlogarithmicaxes.
placement (latitude of lysis minus latitude of genesis), lati- on average in cluster HighSSI with a peak around 25°.
tudeofmaximumVO,deepeningrate(differenceinMSLPa Slightly smaller displacements are found in clusters Intense
24h before and at time of minimum MSLPa), lifetime, and and AvgMST, while cluster Weak has the most negative
mean displacement speed (averaged over the whole life cy- displacement values (i.e. equatorward displacement) with a
cle)ofETCsinthefourclusters.Ingeneral,comparedtothe peak in the distribution around −5°. This causes ETCs in
intensity measures, the distributions of ETC characteristics cluster Weak to have the smallest latitude of maximum VO
havemoreoverlapbetweentheclusters.Aswasthesituation onaverage,withapeakaround35°(Fig.7c).AlthoughETCs
withtheintensitymeasures,inalmostallETCcharacteristics inclustersHighSSIandIntensehaveonaveragealowerlati-
clustersHighSSIandIntensehavethemostsimilardistribu- tudeofgenesiscomparedtoclusterWeak,theirlargermerid-
tions between each other. Despite this, all distributions are ionaldisplacementcausesthemtohaveonaverageahigher
statisticallydifferentatasignificancelevelofatleast5%in latitude of maximum VO. In contrast, despite the slightly
a Mann–Whitney U test, except for the latitude of genesis smallermeridionaldisplacementvaluescomparedtoclusters
ofclustersHighSSIandIntense(notshown).Thisindicates HighSSI and Intense, the highest latitudes of genesis cause
that cluster analysis based on intensity measures is able to ETCsinclusterAvgMSTtohaveonaveragethehighestlati-
identifyETCswhicharedifferentintermsoftheirlifecycle tudeofmaximumVO,withapeakinthedistributionaround
characteristicsinadditiontotheirintensity.Thesedifferences 60°N.
aredescribedindetailinthefollowingparagraphs. All the distributions of deepening rate (Fig. 7d), lifetime
The distributions of genesis latitude overlap consider- (Fig. 7e), and mean speed (Fig. 7f) are skewed to the right.
ably between the clusters, and they all peak around 40°N All of them also have the same order of average magnitude
(Fig.7a).Comparedtothelatitudeofgenesis,thereismore betweentheclusters:(1)HighSSI,(2)Intense,(3)AvgMST,
variation between clusters in the meridional displacement and (4) Weak. This order is the same as in most of the in-
of ETCs (Fig. 7b). The largest meridional displacement is tensity measures in Fig. 6 as well as meridional displace-
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

218 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
Figure7.ProbabilitydensitiesoftheETCcharacteristicsfortheclusters.Thelegendineachpanelisorderedbasedonthemeansofthe
distributionsfromlargesttosmallest.
ment(Fig.7b).Anexplanationforthissimilarityontheorder seaareas(Laurilaetal.,2021b).However,itdoesnotexplain
ofaveragemagnitudebetweenintensityandthecharacteris- the small SSI values, which depend on local FG10 values
ticsisthat,forexample,higherwindspeedstendtorelateto insteadofanabsolutethreshold.
higherdisplacementspeeds,whilelargerdeepeningratesare From a qualitative perspective, the occurrence areas of
likelytoresultindeeperETCsintermsofMSLPa. ETCsinclusterAvgMST(Fig.8c)areamirrorimageofthe
|     |     |     |     |     |     |     | ones in | cluster Weak. |     | As the name | suggests, | ETCs | in clus- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ----------- | --------- | ---- | -------- |
4.3.3 GeographicaldistributionofETCs
|     |     |     |     |     |     |     | ter AvgMST | mostly  | occur     | along | the main | storm | track with |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --------- | ----- | -------- | ----- | ---------- |
|     |     |     |     |     |     |     | a maximum  | between | Greenland | and   | Iceland. | In    | Fig. 9 we  |
Figure8showsthegeographicaldistributionofETCsinthe
seethatovertheNorthAtlanticOceanmostETCsareinthis
differentclusterscomparedtothefullclimatology,andFig.9
cluster,especiallyinthe“Arctic”areawheretheirproportion
shows the proportion of ETCs in each cluster in the boxes is more than 60%. However, we also see that in Europe al-
| shown in | Fig. 8e, | which | offers more | insight | into the | geo- |     |     |     |     |     |     |     |
| -------- | -------- | ----- | ----------- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
mosthalfofETCsareinclusterAvgMST.Ingeneral,ETCs
graphicaldistribution.InFig.8dweseethatETCsincluster inthisclusteroccurmoreinthenorthernpartsofthedomain
WeakaremostlyabsentfromthemainNorthAtlanticstorm
andarelargelyabsentsouthof45°N.Thiscanbeseenalso
trackarea(thesouthwesttonortheasttiltedareaoflargetrack
|     |     |     |     |     |     |     | in the northernmost |     | values | of genesis | latitude | (Fig. | 7a) and |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------ | ---------- | -------- | ----- | ------- |
densitiesintheNorthAtlanticinFig.8e).Theyareinversely latitudeofmaximumVO(Fig.7c).
themostabundantintheMediterraneanbasin.Mediterranean
ETCsinclusterIntensehaveamaximumintrackdensity
| cyclones  | are generally |              | smaller and   | have     | shorter life  | cycles |             |             |           |               |              |           |               |
| --------- | ------------- | ------------ | ------------- | -------- | ------------- | ------ | ----------- | ----------- | --------- | ------------- | ------------ | --------- | ------------- |
|           |               |              |               |          |               |        | over the    | eastern     | coast     | of the United | States       | (Fig.     | 8b). Most     |
| than ETCs | in            | other larger | basins        | (Campins | et al.,       | 2011), |             |             |           |               |              |           |               |
|           |               |              |               |          |               |        | of them     | occur at    | the start | of the        | storm track. | Elsewhere | in            |
| which may | explain       | the          | larger number | of       | Weak cyclones | in     |             |             |           |               |              |           |               |
|           |               |              |               |          |               |        | the domain, | differences |           | are small     | compared     | to        | the full cli- |
thisregionastheirWFPstendtobesmaller.Thehighdensity matology.ThelocationofthetracksinclusterIntensepartly
| of cluster | Weak | ETCs | in the Mediterranean |     | is also consis- |     |          |           |               |        |     |      |              |
| ---------- | ---- | ---- | -------------------- | --- | --------------- | --- | -------- | --------- | ------------- | ------ | --- | ---- | ------------ |
|            |      |      |                      |     |                 |     | explains | the large | precipitation | values | in  | many | of its ETCs, |
tentwithsmallvaluesoflatitudeofmaximumVO(Fig.7c)
astheyoccurinthesouthwesternpartsofthedomainatthe
and meridional displacement (Fig. 7b), given the location start of the storm track, which is an area with large ETC-
andorientationoftheMediterraneanbasin.Inadditiontothe
|     |     |     |     |     |     |     | associated | precipitation |     | (Hawcroft | et al., | 2012), | and over |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --------- | ------- | ------ | -------- |
Mediterranean basin, ETCs in cluster Weak comprise most oceans where surface moisture is abundant. Finally, Fig. 9
ofthetracksincontinentalEurope(Fig.8d).Theoccurrence
showsthatalsoapproximately20%ofMediterraneanETCs
| in this area | also | explains | the smaller | WFP | values, as | near- |     |     |     |     |     |     |     |
| ------------ | ---- | -------- | ----------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
surfacewindspeedsandgustsareloweroverlandthanover
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 219
Figure8.(a–d)Anomaliesoftrackdensityintheclusterscomparedto(e)thefullclimatology.Trackdensitiesarecalculatedseparatelyfor
theclusters;normalizedbymultiplyingthemwithNtot/Nc,whereNc isthenumberoftracksinaclusterandNtot isthetotalnumberof
tracks;andthetrackdensityofthefullclimatologysubtractedfromthem.Thepercentagesinparenthesesindicatetheproportionofalltracks
ineachcluster.
|     |     |     |     | Intense,         | the highest    | track      | densities | occur        | at the    | start of the |
| --- | --- | --- | --- | ---------------- | -------------- | ---------- | --------- | ------------ | --------- | ------------ |
|     |     |     |     | storm track.     | However,       | the        | area of   | higher       | track     | density ex-  |
|     |     |     |     | tends more       | to the         | northeast  | along     | the storm    | track     | (i.e. over   |
|     |     |     |     | Ireland,         | Great Britain, | and        | southern  | Scandinavia) |           | than in      |
|     |     |     |     | cluster Intense, | but            | the values | in this   | area         | are more  | discon-      |
|     |     |     |     | tinuous          | with multiple  | local      | maxima,   | which        | is likely | due to       |
theeffectofnormalization.Thenormalizationalsoobscures
|     |     |     |     | the fact | that each | area in | Fig. 9 has | a similar | proportion | of  |
| --- | --- | --- | --- | -------- | --------- | ------- | ---------- | --------- | ---------- | --- |
clusterHighSSIETCs(around10%).
4.3.4 TemporaloccurrenceofETCs
|     |     |     |     | We investigate | the | temporal | occurrence |     | of the total | number |
| --- | --- | --- | --- | -------------- | --- | -------- | ---------- | --- | ------------ | ------ |
ofETCsandthenumberofETCsineachclusterwithatrend
|     |     |     |     | analysis. | First, time | series | of ETC | occurrence |     | in each ex- |
| --- | --- | --- | --- | --------- | ----------- | ------ | ------ | ---------- | --- | ----------- |
tendedwinteraresmoothedbytakinga5-yearrunningmean.
|                      |                 |            |                | A Mann–Kendall |     | test (Mann, | 1945; | Kendall, | 1970) | is per- |
| -------------------- | --------------- | ---------- | -------------- | -------------- | --- | ----------- | ----- | -------- | ----- | ------- |
| Figure 9. Proportion | of ETCs in each | cluster in | the area boxes |                |     |             |       |          |       |         |
showninFig.8e.TheoccurrenceareaofanETCisallocatedbased formed on these smoothed time series to detect trends us-
ingthePythonpackagepyMannKendall(HussainandMah-
onitslocationattimeofmaximumVO.Thevaluesarenormalized
bythenumberofETCsoccurringineachbox,whichisshownby mud,2019).Wefindthatthereisnotrendinthetotalnumber
thenumbersatthetopofthebars.Thus,thefourbarsforeacharea of ETCs within the study period (not shown). The time se-
sum up to one. Explanations for the abbreviations are as follows: ries of the number of ETCs in each cluster and the results
WAtliswesternNorthAtlantic,EAtliseasternNorthAtlantic,Eur
|     |     |     |     | of the Mann–Kendall |     | test | are shown | in  | Fig. 10. | There is |
| --- | --- | --- | --- | ------------------- | --- | ---- | --------- | --- | -------- | -------- |
isEurope,andMedisMediterranean. largeinterannualvariabilityinthenumberofETCspersea-
|     |     |     |     | son, especially | in    | clusters     | Intense | (Fig. | 10b) and   | AvgMST  |
| --- | --- | --- | --- | --------------- | ----- | ------------ | ------- | ----- | ---------- | ------- |
|     |     |     |     | (Fig. 10c),     | which | is a similar | result  | to    | that found | by Lau- |
belongtoclusterIntense,indicatingthatstrongETCsdode- rilaetal.(2021a).Theslopeofthetrendispositiveinclus-
terHighSSI(0.024ETCyr−1;Fig.10a)andnegativeinclus-
velopinthisregion.
Due to the small size of cluster HighSSI (8.57% of all ter AvgMST (−0.073ETCyr−1; Fig. 10c), but these trends
tracks), the normalization of the track density by the total are not statistically significant. In contrast, statistically sig-
numberoftracksinthefullclimatologyaffectsthedistribu- nificant (at 1% significance level) increasing and decreas-
tiongreatly,withindividualtrackshavingalargercontribu- ingtrendsareidentifiedinclustersIntense(0.104ETCyr−1;
(−0.080ETCyr−1;
tion than in the other clusters. Despite this, the distribution Fig. 10b) and Weak Fig. 10d), respec-
oftrackdensityinclusterHighSSI(Fig.8a)lookslikewhat tively.Tounderstandwhy,wecomputedthetrendsinall11
one would expect based on its similarity to cluster Intense intensitymeasuresforallETCs(notshown).PRECIP,PRE-
in terms of intensity and ETC characteristics. As in cluster CIPacc, and SSIacc have significantly increasing trends (at
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

220 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
the5%level),whilenoneoftheotherintensitymeasureshas There are a couple of reasons why most of the selected
atrend.TheincreaseinthenumberofclusterIntenseETCs, stormsaremoreextremeintermsofwind(PC1)thanprecip-
which have the highest PRECIP values on average and the itation(PC2).Firstly,themajoritycomefromtheXWScata-
largestPRECIPaccvaluesforsingleETCs,isthusconsistent logue(Robertsetal.,2014),inwhichthestormsareselected
with the increasing trend in precipitation in all ETCs. We usingwind-baseddiagnostics.Secondly,ETCswiththehigh-
can therefore say that within our study period, the intensity estPC2values,andthusthemostprecipitation,occurmostly
ofETCshasincreasedmostlyintermsofprecipitation. over the ocean, where their effects are not felt and storms
do not get named. Thirdly, in our dataset ETCs which do
4.4 CasestudyETCs have high precipitation values over land areas occur mostly
overNorthAmerica.Thisisdemonstratedbythepresenceof
Inadditiontothestatisticalapproach,weinvestigatetheclus-
three North American storms in the top right corner of the
ters in terms of individual ETCs. We select named ETCs
sPCA space in Fig. 11: ex-hurricanes Noel and Wilma and
which mainly affected Europe and either occur in the Ex-
the northeaster 1993 Storm of the Century. The remaining
treme Wind Storms (XWS) catalogue (Roberts et al., 2014)
selected storms with high PC2 values, Xynthia and Vivian,
oralistofstrongstormsinFinlandmaintainedbytheFinnish
had compound impacts with both heavy rainfall and strong
Meteorological Institute (FMI, 2024) or are well-known in-
winds.
tense Mediterranean cyclones. The 21 selected ETCs are
listedinTable2,andtheirtracksareshowninFig.S7.Fig-
ure11showsthesestormsprojectedontothefirsttwoPCsof
5 Discussion
thesPCAspaceandcolouredbyeithertheircluster(Fig.11a)
orthevalueofPC3ofthesPCA(Fig.11b).
Similar classes of ETCs have been found with cluster anal-
Figure 11a shows that cluster HighSSI is disproportion-
ysismethodsinpreviousstudies.Blenderetal.(1997)used
ately represented in the set of named storms. Out of the 21
k-meansclusteringandfoundthreeclustersofNorthAtlantic
storms,17areassignedtoclusterHighSSIdespiteitconsist-
ETCtrackorientations:stationary,northeastward,andzonal.
ing of less than 10% of all ETC tracks in the dataset. The
Qualitatively,ourfindingsmatchtheirswell.Theirstationary
fourstormswhichdonotbelongtoclusterHighSSI(Apollo,
ETCsoccurredmostlyintheMediterranean,Greenland,and
Aapeli, Vivian, and Qendresa) have the smallest SSI values
northernCanadaand,asthenamesuggests,hadsmallpropa-
of the 21 case studies, which cannot be seen in the PCs in
gationspeeds.ThisissimilartoourclusterWeak.Likewise,
Fig.5.Thesefourareamongthefivestormswiththesmall-
theirnortheastwardETCsaresimilartoourclustersHighSSI
estPC4valuesofthe21casestudies,whichmeanstheyhave
and Intense, with large meridional displacements and prop-
lowVOand/orhighMSLPavalues(notshown).InFig.11b
agation speeds. While their zonal ETCs match our cluster
weseethatmostofthe21stormsfallclosetothemeanvalue
AvgMST in terms of the more moderate meridional move-
of PC2, meaning that they have near-average precipitation.
ment, their zonal tracks are not concentrated at the end of
Most storms which affected Europe are relatively close to
thestormtrackinthenortheasternAtlanticlikeourAvgMST
one another in the sPCA (e.g. Anatol, Kyrill, and Ulli), ex-
ETCs are. In addition to the similarity in track orientations,
ceptforVivian,Xynthia,andApollowhichhadmoreprecipi-
ETCsintheirclustershadsimilaraverageintensitiestoours.
tationand/orlowerwindspeeds.AlthoughclusterHighSSIis
In terms of geopotential height at 1000hPa (Z ), their
1000
overwhelminglythemostcommonclusteramongthenamed
stationary ETCs had on average the weakest Z gradi-
1000
storms, only 9 of the 21 storms have a positive value in all
ent (comparable to low-level winds) and the highest Z
1000
four PCs (e.g. Christian/St.Jude has negative PC2 and PC3
(comparable to MSLP), while northeastward ETCs had the
values and a small PC4 value but still is a HighSSI storm).
strongestZ gradientandthelowestZ values.
1000 1000
Thisdemonstratestheneedtousemorethanonemeasureto
Similarly, Gaffney et al. (2007) performed cluster analy-
quantifyETCintensity.
sis on North Atlantic ETC tracks with regression mixture
At the same time, there is only one storm, Medicane
models, which are probabilistic methods like GMMs. Like
Apollo, which has a negative PC1 value, i.e. smaller than
Blenderetal.(1997),theyfoundclusterswithnortheastward
average wind speed, and a PC3 close to the negative end,
and zonal track orientations. They, however, identified also
i.e. small WFP. Apollo, however, has the sixth-largest PC2
a cluster with northward track orientations but did not find
value of the 21 case study ETCs, which is to be expected
aclusterofstationaryETCtracks.Theirnorthward-oriented
sincemostofthedamagewascausedbyprecipitationrather
cluster tracks were mostly found near the eastern coast of
than wind. Apollo belongs to cluster Weak, since the clus-
North America and were among the most intense ETCs in
teranalysisdiscriminatesintensitymorebasedonwindthan
terms of MSLP. This indicates that the northward-oriented
precipitation(cf.e.g.Fig.6bandc).However,thismayalso
trackscouldcontainmanyofthesametracksasourclusters
be due to the underestimation of the intensity of medicanes
HighSSIandIntense(e.g.post-tropicalcyclones).Theyalso
inERA5(Pantillonetal.,2024).
foundthatthenortheastward-orientedETCswerethefastest-
moving,whiletheyfoundnosignificantdifferencesinETC
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 221
Figure10.TemporaltrendsofthenumberofETCsineachcluster.ThesolidlinesshowthenumberofETCsineachextendedwinterseason,
andthedashedlinesshow5-yearrunningmeans.Thedash-dottedlinesshowtheslopesofthetrendofthe5-yearrunningmeansfroma
Mann–Kendall test. The trend is given by the equation y=ax+b, where y is ETC count, x is the year minus 1979, a is the slope (in
ETCyr
−1),andbistheinterceptin1979(innumberofETCs).Notethattheverticalaxeshavedifferentscalesineachpanel.
Figure11.CasestudystormsinthesPCAspace,colouredby(a)theirpredictedclusterand(b)theirPC3value.SeeTable2forabbreviations
ofstormnames.
lifetime between any of the clusters. This result is different tified six large-scale flow patterns over Europe which they
from ours, as we found a link between average dynamical used to classify winter storm situations with k-means clus-
intensityandETCspeedandlifetime. tering.Of55identifiedpressurepatternclusters,4wereclas-
Leckebusch et al. (2008b) used similar methods to those sified as primary storm clusters. These primary storm clus-
weusedtorelatelarge-scaleflowpatternstodifferenttypes ters were associated with more extreme ETCs, as 72% of
ofETCs.FromaPCAperformedonaZ fieldtheyiden- 46importantEuropeanwinterstormsoccurredduringthese
1000
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

222 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
Table 2. The named case study ETCs included in Fig. 11. The columns are the name of the ETC, abbreviation used in Fig. 11, time of
occurrence,theareatheETCmostlyaffected,andareferencestudyfortheETC.
| Name           | Abbrev. Occurrence | Affectedarea   | Reference          |     |     |
| -------------- | ------------------ | -------------- | ------------------ | --- | --- |
| Aapeli/Alfrida | AA Jan2019         | NorthernEurope | ECMWF(2021)        |     |     |
| Anatol         | ANA Dec1999        | NorthernEurope | Ulbrichetal.(2001) |     |     |
Andrea(secondary) AND Jan2012 Mediterranean Kouroutzoglouetal.(2013)
| Apollo/Nearchus | AP Oct2021 | Mediterranean | Mennaetal.(2023) |     |     |
| --------------- | ---------- | ------------- | ---------------- | --- | --- |
Christian/St.Jude CH Oct2013 NorthwesternEurope Hewsonetal.(2014)
Dagmar/Patrick/Tapani DAG Dec2011 NorthernEurope WeijenborgandSpengler(2020)
Daria/Burns’DayStorm DAR Jan1990 NorthwesternEurope McCallum(1990)
Erwin/Gudrun ER Jan2005 NorthwesternEurope Suursaaretal.(2006),Baker(2009)
| Fabien | FA Dec2019 | Mediterranean | Stojanovicetal.(2021) |     |     |
| ------ | ---------- | ------------- | --------------------- | --- | --- |
| Julia  | JU Feb2012 | Mediterranean | Metheniti(2012)       |     |     |
Klaus KL Jan2009 SouthwesternEurope Liberatoetal.(2011),Bertottietal.(2012)
| Kyrill | KY Jan2007 | WesternEurope | Finketal.(2009) |     |     |
| ------ | ---------- | ------------- | --------------- | --- | --- |
Lothar LO Dec1999 WesternEurope Ulbrichetal.(2001),Wernlietal.(2002)
Ex-hurricaneNoel NO Nov2007 EasternNorthAmerica Brennanetal.(2009)
Qendresa QE Nov2014 CentralMediterranean Coll-Hidalgoetal.(2022)
1993StormoftheCentury SO Mar1993 EasternNorthAmerica Huoetal.(1995)
Ulli UL Jan2012 NorthwesternEurope Foxetal.(2012),SmartandBrowning(2014)
| Vivian | VI Feb1990 | WesternEurope | Schüeppetal.(1994) |     |     |
| ------ | ---------- | ------------- | ------------------ | --- | --- |
Ex-hurricaneWilma WI Oct.2005 EasternNorthAmerica Paschetal.(2006)
| Xaver | XA Dec2013 | NorthernEurope | Hewsonetal.(2014) |     |     |
| ----- | ---------- | -------------- | ----------------- | --- | --- |
Xynthia XY Feb2010 WesternEurope Liberatoetal.(2013),Ludwigetal.(2014)
clusters,whiletheoverallrelativefrequencyofoccurrenceof Besson et al. (2021) investigated dry-dynamic forcing of
the four clusters was only 5%. This result is reminiscent of northern hemispheric ETCs by studying their Eady growth
ourfindingthatthemajorityofwell-knownimpactfulstorms rateandupper-level-inducedquasi-geostrophicascent.They
are found in cluster HighSSI despite its small proportion of defined four categories of ETC forcing by selecting values
| allETCs. |     | attheextremecornersofatwo-dimensionalphasespacede- |     |     |     |
| -------- | --- | -------------------------------------------------- | --- | --- | --- |
Othershavealsopreviouslyusedphasespacesconsisting termined by the two variables. They found that these four
ofdifferentvariablestocategorizeETCs.Manyhavesubjec- categoriesofETCforcingoccurindifferentgeographicalar-
tively divided phase spaces into various parts and analysed eas and lead to ETCs which differ in their deepening rates
ETCs in each part of the phase space separately. Graf et al. and have differences in their upper-level structure. Similar-
(2017) performed PCA on 30 ETC precursors to classify ities between their categories and our clusters can be seen
northern hemispheric cyclogenesis events. Although they inthelinkbetweenETCdeepeningratesandoccurrencear-
foundnoobviousclustersinthecontinuousphasespacede- eas of the four categories of ETC forcing. For example, a
termined by the genesis events,they were able to formulate combinationofthetwoforcingmechanismsleadingtolarge
five ETC classes by using the first two components of the deepeningratesisfoundmostlyatthestartoftheNorthAt-
PCA.ThefirstPCdeterminedwhetheranETCgenesiswas lantic storm track (see clusters HighSSI and Intense), while
characterizedbystrongorweakmoistprocesses,andthesec- combinations leading to the smallest deepening rates occur
ond PC split the genesis events based on the type of forc- moreatthesouthernandsoutheasternpartsoftheNorthAt-
ingmechanisms,asinPetterssenandSmebye(1971).Their lantic (see cluster Weak). Deepening rates in between these
PCA classification was robust to the number of input fea- extremesareassociatedwithacombinationofforcingmech-
tures, with5 precursors producingsimilar results tothe ini- anismswhichoccursmostlyinthenorthernpartsoftheNorth
tial 30. They also determined that a majority (67%) of in- Atlantic with a maximum density between Greenland and
vestigatedwell-knownETCsbelongedtoasingleclass.Fur- Iceland (see cluster AvgMST). Similar analyses were done
thermore, all four case study ETCs that are shared between by Binder et al. (2016) and Binder et al. (2023), who de-
theirandourstudies(Klaus,Kyrill,Lothar,andXynthia)be- terminedthreecategoriesofETCintensificationfornorthern
longedtothisclass,whileinourinvestigationtheywereall hemisphericETCsfromaphasespaceofETCdeepeningrate
found in cluster HighSSI. While they note that their analy- andlow-levelwarmconveyorbeltairmass.
siscannotbeusedtodirectlyattributecyclogenesiseventsto While these types of analyses are suitable for studying
specificcycloneevolution,thisisaninterestingresult. theprecursorsandforcingmechanismsofETCs,wedemon-
|     |     | strate that | the classification | of ETCs based | on their inten- |
| --- | --- | ----------- | ------------------ | ------------- | --------------- |
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 223
sitybenefitsfromanaddedlevelofobjectivityviatheclus- isthatthecriteriausedfortheETCtrackingareoptimizedfor
teranalysis.Thiscanbeseenintheoverlapbetweenthein- theNorthAtlantic.Therefore,someMediterraneanETCsare
tensity measure distributions for different clusters in Fig. 6. excluded from our set of tracks since they can be more sta-
Despitethisoverlapintroducedbytheobjectivemethod,our tionary,haveshorterlifetimes,andhavetheirmaximumvor-
clusterscanbeatleastqualitativelylinkedtoclassesofETCs ticity within the first 24h. Flaounas et al. (2023) compared
obtained with more subjective methods as described above. 10 ETC tracking algorithms in the Mediterranean area, one
Infact,apossiblecourseoffuturestudyistheidentification of which was TRACK. In their comparison, TRACK pro-
of thevariability in theETC precursors andforcing mecha- duced the longest lifetimes and largest propagation speeds
nismswithinourclusters.Webelievethatthisformofanaly- for ETCs in the Mediterranean. Despite these limitations,
sis,whichlinkstheintensityandrelevanceforimpactstothe our study brings valuable new knowledge on which inten-
genesisenvironmentofETCs,wouldofferanewperspective sity measures should be used to comprehensively and non-
ontheclassificationofETClifecyclesandpossiblyimprove redundantlyquantifytheintensityofETCs.
thepredictabilityofETCintensity.
Aninvestigationofwell-knowncasestudyETCsshowed
that proportionally,the majority of impactfulstorms belong 6 Conclusions
toclusterHighSSI(17outof21).Thishighlightstheability
of the cluster analysis to identify intense storms. However, We created a dataset of extratropical cyclone (ETC) inten-
wecannotsaythatallETCsinclusterHighSSIareimpactful sitymeasuresfor43extendedwintersofNorthAtlanticand
ordamaging.Inadditiontothestatisticalnatureoftheclus- EuropeanETCtracksandperformedsparseprincipalcompo-
teranalysis,thisisduetothefactthatapartfromSSI,which nentanalysis(sPCA)toidentifythemeasureswhichexplain
is based on local climatological values, the impact-relevant mostofthevariabilityinthedataset.Usingtheresultsofthe
intensitymeasuresdonotdiscriminatebetweenlandandsea sPCA and correlations between the intensity measures, we
areas.ETCshaveonaveragelargerWFPvaluesand/ormore determined five measures for the comprehensive and non-
precipitationovertheoceanandontheeasterncoastofNorth redundant representation of ETC intensity: 850hPa relative
America(Hawcroftetal.,2012;Laurilaetal.,2021b),which vorticity, 850hPa wind speed, wind footprint, precipitation,
inevitablyleadstosomenon-impactfulETCsbeingclassified andastormseverityindex(SSI).
asIntenseorHighSSI.ItalsoexplainswhymanyEuropean Our analysis shows that while there is strong correlation
stormsinFig.11havebelow-averageprecipitationandwhy between different dynamical ETC intensity measures, there
Medicane Apollo is classified as a cluster Weak storm. On is a much weaker link between the dynamical intensity and
theotherhand,theanalysisshowedthatSSI,whichdoesnot impact-relevant measures. A correlation of similar strength
bydefinitionhavelargervaluesoverseathanland,isanim- betweenwindspeedandprecipitationwasfoundpreviously
portantmeasureindeterminingtheclusterofanETCwhose byPfahlandSprenger(2016),whodeterminedacorrelation
otherintensitymeasureshaveclosetoaveragevalues.How- coefficient of 0.36. Therefore, when using ETC intensity as
ever, SSI alone cannot be used to identify impactful storms a broad term, i.e. including the impacts as well as the me-
sinceitisrelevantforimpactsduetowindonly,whileother teorological intensity in the definition, we need to consider
factors in ETCs such as precipitation can also cause signif- the non-linear and weakly correlated relationship between
icant damage (e.g. Medicane Apollo). This emphasizes the the two and use more thanone or two measures to describe
factthatmultipleintensitymeasuresshouldbeusedtoquan- the intensity. We recommend studies which aim to quantify
tifytheintensityofETCs. futurechangesinETCintensitytoconsiderthefivevariables
A limitation of our study is the use of only one data wedetermined.
source (ERA5) and one ETC tracking algorithm (TRACK). Weusedthesefiveintensitymeasuresasinputtoacluster
Firstly, the representation of ETCs has been found to vary analysis performed with a Gaussian mixture model (GMM)
between reanalysis datasets (Hodges et al., 2011; Wang to create classes of ETCs. We found four clusters in which
et al., 2016). Secondly, ERA5 underestimates precipitation ETCs are significantly different in terms of their intensity.
andstronglow-levelwindsinsomeareas(Chenetal.,2024; ClusterWeakhasonaveragetheweakestETCs(25.54%of
Minola et al., 2020). This underestimation may cause our allETCs),clusterAvgMSTcontainsaverage-intensityETCs
precipitation or wind distributions to be too narrow, which (44.42%),andclustersIntenseandHighSSIarecomposedof
may have an effect on the cluster analysis through, for ex- more intense ETCs (21.46% and 8.57%, respectively). For
ample, creating more overlap in precipitation between the all intensity measures except for precipitation, the clusters
clusters than without the bias. Thirdly, earlier studies have areinthesamerelativeorderintermsofaveragemagnitude:
shownthatETCclimatologiesmaydifferindistributionsand HighSSI, Intense, AvgMST, and Weak. However, the clus-
trends due to sensitivity to the tracking algorithm because ters are not discrete in the feature space defined by the in-
using different variables and thresholds leads to identifying tensitymeasuressincethereisoverlapinthedistributionsof
differentcategoriesofETCs(Raibleetal.,2008;Neuetal., theintensitymeasuresbetweentheclusters.Themostover-
2013;Flaounasetal.,2023).Anotherlimitationofourstudy lap is between clusters Intense and HighSSI. This overlap,
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

224 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
the small size of cluster HighSSI, and the large SSI values whenensemblepredictionsystemsarekeytoproduceprob-
initsETCsindicatethatclusterHighSSI,whichcontainsthe abilistic forecasts and vast amounts of data. Being able to
mostextremeandpotentiallyimpactfulETCs,isasubsetof identifyETCs ineach ensemblememberand computetheir
cluster Intense. Of all intensity measures, there is the least intensityallowsforanaccurateestimateoftheuncertaintyin
overlapbetweenclustersinthedistributionsoftheSSI.This, howstrongandhowpotentiallyimpactfulaspecificETCwill
alongwiththefactthatalargemajorityofthenamedimpact- be.Furthermore,thisallowsavastamountofinformationto
ful storms considered in this study (17 out of 21) belong to be condensed to a level that is manageable for operational
cluster HighSSI despite the cluster accounting for less than forecasters,whooftenareworkingundertimepressure.
| 10% of | all ETCs, suggests | that | SSI | is useful | in  | identifying |     |     |     |     |     |     |     |     |
| ------ | ------------------ | ---- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
impactfulETCs,whichisinagreementwithpreviousstudies
Codeanddataavailability.
(Klawa and Ulbrich, 2003; Leckebusch et al., 2007, 2008a; ERA5 reanalysis data were down-
Donatetal.,2011). loaded from the Copernicus Climate Change Service (Hersbach
The clusters are different in terms of their characteristics etal.,2017)(https://doi.org/10.24381/cds.143582cf).Allprocessed
dataandPythoncodeareavailableinaZenodorepository(Cornér
andgeographicallocationofoccurrenceaswell.Theaverage
etal.,2024)(https://doi.org/10.5281/zenodo.11384417).
intensityofETCsintheclusterscanbequalitativelylinkedto
| their deepening | rate, lifetime, |     | and mean | propagation |     | speed. |     |     |     |     |     |     |     |     |
| --------------- | --------------- | --- | -------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
TheweakerETCsoccurmorefrequentlyinEuropeandinthe
|     |     |     |     |     |     |     | Supplement. | Thesupplementrelatedtothisarticleisavailableon- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
MediterraneanbasinthanovertheAtlanticOcean,butHigh-
lineat:https://doi.org/10.5194/nhess-25-207-2025-supplement.
| SSI ETCs  | are almost as  | frequent       | everywhere |              | when | normal- |     |     |     |     |     |     |     |     |
| --------- | -------------- | -------------- | ---------- | ------------ | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ized with | respect to the | climatological |            | distribution |      | of ETC  |     |     |     |     |     |     |     |     |
occurrence.ThenumberofETCsinclusterIntenseincreased
|           |                |     |        |     |      |            | Authorcontributions. |        | JC,          | CB, | and VAS | all contributed | to       | the de- |
| --------- | -------------- | --- | ------ | --- | ---- | ---------- | -------------------- | ------ | ------------ | --- | ------- | --------------- | -------- | ------- |
| from 1979 | to 2022, while | the | number | of  | ETCs | in cluster |                      |        |              |     |         |                 |          |         |
|           |                |     |        |     |      |            | sign of the          | study. | JC performed |     | most of | the data        | analysis | and vi- |
Weakdecreased,whichismostlycausedbyapositivetrend
|     |     |     |     |     |     |     | sualization. | JC, CB, | and | VAS all | contributed | to  | the interpretation |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------- | ----------- | --- | ------------------ | --- |
in precipitation. This increasing trend in ETC precipitation oftheresults.BDcontributedtothedefinitionandanalysisofthe
is in agreement with Li et al. (2014), who compared a re- storm severity index. FP and BD contributed to the analysis over
cent warmer period (in average sea surface temperature) as theMediterraneanregion.JCwroteSects.2,4,5,and6.CBwrote
ananalogueoffutureclimatechangetoanearlierbaseperiod Sect.3.VASandFPwroteSect.1.Allauthorsreviewedandedited
and found that while precipitation was larger in the warmer themanuscript.VASsecuredfundingforthestudy.
| period than | the base period, | there | was | no  | consistent | change |     |     |     |     |     |     |     |     |
| ----------- | ---------------- | ----- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
invorticityorwindspeed.Thereisalsoasignificantincrease
in accumulated SSI (SSIacc) which, without an increase in Competinginterests. Thecontactauthorhasdeclaredthatnoneof
theauthorshasanycompetinginterests.
| maximum     | wind gusts | at 10m | (FG10), | can    | be explained | by       |     |     |     |     |     |     |     |     |
| ----------- | ---------- | ------ | ------- | ------ | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| an increase | in extreme | wind   | gust    | values | in North     | Atlantic |     |     |     |     |     |     |     |     |
ETCsfrom1979to2021foundbyKarwatetal.(2022).
|     |     |     |     |     |     |     | Disclaimer. | Publisher’s |     | note: | Copernicus | Publications |     | remains |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----- | ---------- | ------------ | --- | ------- |
OurobjectiveclassificationofETCsbasedontheirinten-
|     |     |     |     |     |     |     | neutral with | regard | to jurisdictional |     | claims | made | in the text, | pub- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------------- | --- | ------ | ---- | ------------ | ---- |
sityoffersanewperspectiveonthemultitudeofETCclassi-
lishedmaps,institutionalaffiliations,oranyothergeographicalrep-
ficationsreviewedinCatto(2016).Ourclassificationisper- resentationinthispaper.WhileCopernicusPublicationsmakesev-
| formed using | variables | which | are available |     | or easy | to com- |     |     |     |     |     |     |     |     |
| ------------ | --------- | ----- | ------------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
eryefforttoincludeappropriateplacenames,thefinalresponsibility
| pute from | both model      | and reanalysis |         | data.   | Both | the sPCA    | lieswiththeauthors. |     |     |     |     |     |     |     |
| --------- | --------------- | -------------- | ------- | ------- | ---- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| model and | the GMM         | instance       | trained | with    | our  | dataset are |                     |     |     |     |     |     |     |     |
| provided  | as downloadable | Python         |         | objects | in a | repository  |                     |     |     |     |     |     |     |     |
(Cornér et al., 2024). For any dataset including ETC tracks Acknowledgements. We wish to thank Kevin Hodges for provid-
andanassociatedvalueofeachoftheintensitymeasuresper ingthecyclonetrackingsoftwareTRACKandsupportinitsset-up
track,thesPCAmodelcanbeusedtoprojectETCsontothe and running, as well as four anonymous reviewers for their con-
structivecommentsthathelpedimprovethepaper.Weacknowledge
sPCAspaceshowninFig5a.Moreover,topredicttheclus-
ter of each ETC in the same or a similar dataset, the GMM CSC–ITCentreforScience,Finland,forcomputationalresources
|          |                  |     |      |           |          |        | and ECMWF | for | producing | ERA5 | reanalysis. |     | This research | is a |
| -------- | ---------------- | --- | ---- | --------- | -------- | ------ | --------- | --- | --------- | ---- | ----------- | --- | ------------- | ---- |
| instance | can be used with | the | five | intensity | measures | listed |           |     |           |      |             |     |               |      |
contributiontotheCOSTActionCA19109“MedCyclones:Euro-
| above as | input. Building | on  | the work | of  | Bengtsson | et al. |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | -------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
peanNetworkforMediterraneanCyclonesinweatherandclimate”.
(2009)andChampionetal.(2011),whostudiedtheintensity
JoonaCornérwaspartlyfundedbytheUniversityofHelsinkiDoc-
andextremeweatherfromETCsinfutureclimates,utilizing
|     |     |     |     |     |     |     | toral School. | Benjamin |     | Doiteau | was funded | by  | Région Occitanie |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | ------- | ---------- | --- | ---------------- | --- |
thiskindofclassificationinclimateprojectionstudiescould
|     |     |     |     |     |     |     | and Météo-France |     | through | project | PREVIMED. |     | This study | uses |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------- | --------- | --- | ---------- | ---- |
giveinsightintohowdifferentkindsofETCsrespondtocli- scientificcolourmaps(Crameri,2023)topreventvisualdistortion
matechange.Inadditiontoclimateapplications,quantifying ofthedataandexclusionofreaderswithcolourvisiondeficiencies.
theintensityofETCsisalsoimportantintermsofnumerical
weatherprediction.Thisisespeciallytrueinthecurrentage,
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 225
Financialsupport. This research has been supported by the Browning, K. A.: Organization of clouds and precipitation in
ResearchCouncilofFinland(grantno.338615). extratropical cyclones, in: Extratropical Cyclones, The Erik
|     |     |     |     |     |     |     | Palmén | Memorial | Volume, | Amer. | Meteor. | Soc., | 129–154, |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------- | ----- | ------- | ----- | -------- |
Open-accessfundingwasprovidedbytheHelsinki https://doi.org/10.1007/978-1-944970-33-8_8,1990.
UniversityLibrary. Campins,J.,Genovés,A.,Picornell,M.A.,andJansà,A.:Clima-
tologyofMediterraneancyclonesusingtheERA-40dataset,Int.
|     |     |     |     |     |     |     | J. Climatol., | 31, | 1596–1614, | https://doi.org/10.1002/joc.2183, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | --------------------------------- | --- | --- | --- |
2011.
| Reviewstatement. |     | ThispaperwaseditedbyJoaquimG.Pintoand |     |     |     |     |        |        |               |         |                |     |         |
| ---------------- | --- | ------------------------------------- | --- | --- | --- | --- | ------ | ------ | ------------- | ------- | -------------- | --- | ------- |
|                  |     |                                       |     |     |     |     | Catto, | J. L.: | Extratropical | cyclone | classification |     | and its |
reviewedbyfouranonymousreferees.
|     |     |     |     |     |     |     | use | in climate | studies, | Rev. | Geophys., | 54, | 486–520, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | --------- | --- | -------- |
https://doi.org/10.1002/2016RG000519,2016.
|     |     |     |     |     |     |     | Catto, J. | L.: A | New Method | to  | Objectively | Classify | Extra- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---------- | --- | ----------- | -------- | ------ |
References tropical Cyclones for Climate Studies: Testing in the
|           |             |     |            |          |     |          | Southwest | Pacific | Region, | J.  | Climate, | 31, | 4683–4704, |
| --------- | ----------- | --- | ---------- | -------- | --- | -------- | --------- | ------- | ------- | --- | -------- | --- | ---------- |
| Anderson, | D., Hodges, |     | K. I., and | Hoskins, | B.  | J.: Sen- |           |         |         |     |          |     |            |
https://doi.org/10.1175/JCLI-D-17-0746.1,2018.
| sitivity | of Feature-Based |     | Analysis | Methods |     | of Storm |     |     |     |     |     |     |     |
| -------- | ---------------- | --- | -------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Catto,J.L.,Shaffrey,L.C.,andHodges,K.I.:Canclimatemodels
Tracks to the Form of Background Field Removal, Mon. capture the structure of extratropical cyclones?, J. Climate, 23,
Weather Rev., 131, 565–573, https://doi.org/10.1175/1520- 1621–1635,https://doi.org/10.1175/2009JCLI3318.1,2010.
0493(2003)131<0565:SOFBAM>2.0.CO;2,2003. Champion, A. J., Hodges, K. I., Bengtsson, L. O., Keenly-
Aragão, L. and Porcù, F.: Cyclonic activity in the Mediter- side, N. S., and Esch, M.: Impact of increasing resolution
| ranean | region | from | a high-resolution |     | perspective | using |       |        |         |            |         |      |          |
| ------ | ------ | ---- | ----------------- | --- | ----------- | ----- | ----- | ------ | ------- | ---------- | ------- | ---- | -------- |
|        |        |      |                   |     |             |       | and a | warmer | climate | on extreme | weather | from | Northern |
ECMWF ERA5 dataset, Clim. Dynam., 58, 1293–1310, Hemisphere extratropical cyclones, Tellus A, 63, 893–906,
https://doi.org/10.1007/s00382-021-05963-x,2022. https://doi.org/10.1111/j.1600-0870.2011.00538.x,2011.
Baker, L.: Sting jets in severe northern European wind storms, Chang, E. K.-M.: CMIP5 Projected Change in Northern Hemi-
Weather,64,143–148,https://doi.org/10.1002/wea.397,2009. sphere Winter Cyclones with Associated Extreme Winds,
| Bechtold, | P. and | Bidlot, | J.-R.:      | Parametrization |      | of con- |              |     |            |                                    |     |     |     |
| --------- | ------ | ------- | ----------- | --------------- | ---- | ------- | ------------ | --- | ---------- | ---------------------------------- | --- | --- | --- |
|           |        |         |             |                 |      |         | J. Climate,  | 31, | 6527–6542, | https://doi.org/10.1175/JCLI-D-17- |     |     |     |
| vective   | gusts, | ECMWF   | Newsletter, |                 | 119, | 15–18,  | 0899.1,2018. |     |            |                                    |     |     |     |
https://doi.org/10.21957/kfr42kfp8c,2009. Chen, G., Chen, Z., Zhou, F., Yu, X., Zhang, H., and Zhu, L.: A
Bengtsson, L., Hodges, K. I., and Roeckner, E.: Storm semisuperviseddeeplearningframeworkfortropicalcyclonein-
Tracks and Climate Change, J. Climate, 19, 3518–3543, tensityestimation,in:201910thInternationalWorkshoponthe
https://doi.org/10.1175/JCLI3815.1,2006.
AnalysisofMultitemporalRemoteSensingImagesMulti-Temp,
Bengtsson,L.,Hodges,K.I.,andKeenlyside,N.:Willextratropi- IEEE, 1–4, https://doi.org/10.1109/Multi-Temp.2019.8866970,
| calstormsintensifyinawarmerclimate?,J.Climate,22,2276– |     |     |     |     |     |     | 2019. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2301,https://doi.org/10.1175/2008JCLI2678.1,2009. Chen,T.-C.,Collet,F.,andDiLuca,A.:EvaluationofERA5pre-
Bertotti,L.,Bidlot,J.-R.,Bunney,C.,Cavaleri,L.,DelliPasseri,L., cipitationand10-mwindspeedassociatedwithextratropicalcy-
Gomez,M.,Lefèvre,J.-M.,Paccagnella,T.,Torrisi,L.,Valentini,
clonesusingstationdataoverNorthAmerica,Int.J.Climatol.,
A., and Vocino, A.: Performance of different forecast systems 44,729–747,https://doi.org/10.1002/joc.8339,2024.
in an exceptional storm in the Western Mediterranean Sea, Q. Coll-Hidalgo, P., Pérez-Alarcón, A., and Nieto, R.: Moisture
J.Roy.Meteor.Soc.,138,34–55,https://doi.org/10.1002/qj.892, Sources for the Precipitation of Tropical-like Cyclones in the
2012. Mediterranean Sea: A Case of Study, Atmosphere, 13, 1327,
Besson, P., Fischer, L. J., Schemm, S., and Sprenger, M.: A https://doi.org/10.3390/atmos13081327,2022.
| global analysis |     | of the | dry-dynamic | forcing | during | cyclone |     |     |     |     |     |     |     |
| --------------- | --- | ------ | ----------- | ------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
Colle,B.A.,Zhang,Z.,Lombardo,K.A.,Chang,E.,Liu,P.,and
growth and propagation, Weather Clim. Dynam., 2, 991–1009, Zhang,M.:HistoricalEvaluationandFuturePredictionofEast-
https://doi.org/10.5194/wcd-2-991-2021,2021. ernNorthAmericanandWesternAtlanticExtratropicalCyclones
Binder, H., Boettcher, M., Joos, H., and Wernli, H.: The Role of in the CMIP5 Models during the Cool Season, J. Climate, 26,
WarmConveyorBeltsfortheIntensificationofExtratropicalCy- 6882–6903,https://doi.org/10.1175/JCLI-D-12-00498.1,2013.
clonesinNorthernHemisphereWinter,J.Atmos.Sci.,73,3997–
|     |     |     |     |     |     |     | Cornér, | J., Bouvier, | C., | Doiteau, | B., Pantillon, |     | F., and Sin- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | -------- | -------------- | --- | ------------ |
4020,https://doi.org/10.1175/JAS-D-15-0302.1,2016. clair, V. A.: Classification of North Atlantic and Euro-
Binder, H., Joos, H., Sprenger, M., and Wernli, H.: Warm con- pean extratropical cyclones using multiple measures of inten-
veyorbeltsinpresent-dayandfutureclimatesimulations–Part2: sity: Data and Python code, Zenodo [data set] and [code],
Roleofpotentialvorticityproductionforcycloneintensification, https://doi.org/10.5281/zenodo.11384417,2024.
| Weather | Clim. | Dynam., | 4, 19–37, | https://doi.org/10.5194/wcd- |     |     |           |        |         |                 |     |             |         |
| ------- | ----- | ------- | --------- | ---------------------------- | --- | --- | --------- | ------ | ------- | --------------- | --- | ----------- | ------- |
|         |       |         |           |                              |     |     | Cover, T. | M. and | Thomas, | J. A.: Elements | of  | information | theory, |
4-19-2023,2023. Wiley-Interscience,Hoboken,N.J,2ndedn.,ISBN0471748811,
Blender, R., Fraedrich, K., and Lunkeit, F.: Identification of https://doi.org/10.1002/047174882X,2006.
cyclone-trackregimesintheNorthAtlantic,Q.J.Roy.Meteor. Crameri, F.: Scientific colour maps, Zenodo [code],
Soc., 123, 727–741, https://doi.org/10.1002/qj.49712353910, https://doi.org/10.5281/zenodo.8409685,2023.
1997.
Dacre,H.F.andGray,S.L.:Thespatialdistributionandevolution
Brennan,M.J.,Knabb,R.D.,Mainelli,M.,andKimberlain,T.B.: characteristics of North Atlantic cyclones, Mon. Weather Rev.,
Atlantic Hurricane Season of 2007, Mon. Weather Rev., 137, 137,99–115,https://doi.org/10.1175/2008MWR2491.1,2009.
4061–4088,https://doi.org/10.1175/2009MWR2995.1,2009.
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

226 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
Davis, C. A. and Emanuel, K. A.: Potential Vor- ing regression mixture models, Clim. Dynam., 29, 423–440,
ticity Diagnostics of Cyclogenesis, Mon. Weather https://doi.org/10.1007/s00382-007-0235-z,2007.
Rev., 119, 1929–1953, https://doi.org/10.1175/1520- Graf, M. A., Wernli, H., and Sprenger, M.: Objective classifica-
0493(1991)119<1929:PVDOC>2.0.CO;2,1991. tionofextratropicalcyclogenesis,Q.J.Roy.Meteorol.Soc.,143,
Deveson, A., Browning, K., and Hewson, T.: A classification of 1047–1061,https://doi.org/10.1002/qj.2989,2017.
FASTEXcyclonesusingaheight-attributablequasi-geostrophic Gramcianinov, C., Campos, R., de Camargo, R., Hodges, K.,
vertical-motiondiagnostic,Q.J.Roy.Meteor.Soc.,128,93–117, Guedes Soares, C., and da Silva Dias, P.: Analysis of At-
https://doi.org/10.1256/00359000260498806,2002. lantic extratropical storm tracks characteristics in 41 years of
Doiteau,B.,Pantillon,F.,Plu,M.,Descamps,L.,andRieutord,T.: ERA5 and CFSR/CFSv2 databases, Ocean Eng., 216, 108111,
SystematicevaluationofthepredictabilityofdifferentMediter- https://doi.org/10.1016/j.oceaneng.2020.108111,2020.
ranean cyclone categories, Weather Clim. Dynam., 5, 1409– Hartmann, D. L.: Global Physical Climatology, vol. 103, Else-
1427,https://doi.org/10.5194/wcd-5-1409-2024,2024. vier, ISBN 978-0-12-328531-7, https://doi.org/10.1016/C2009-
Dolores-Tesillos, E., Teubler, F., and Pfahl, S.: Future changes 0-00030-0,2015.
in North Atlantic winter cyclones in CESM-LE – Part 1: Hawcroft,M.K.,Shaffrey,L.C.,Hodges,K.I.,andDacre,H.F.:
Cyclone intensity, potential vorticity anomalies, and hori- How much Northern Hemisphere precipitation is associated
zontal wind speed, Weather Clim. Dynam., 3, 429–448, with extratropical cyclones?, Geophys. Res. Lett., 39, L24809,
https://doi.org/10.5194/wcd-3-429-2022,2022. https://doi.org/10.1029/2012GL053866,2012.
Donat, M. G., Leckebusch, G. C., Wild, S., and Ulbrich, U.: Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
Future changes in European winter storm losses and ex- Muñoz-Sabater,J.,Nicolas,J.,Peubey,C.,Radu,R.,Schepers,
treme wind speeds inferred from GCM and RCM multi-model D.,Simmons,A.,Soci,C.,Abdalla,S.,Abellan,X.,Balsamo,G.,
simulations, Nat. Hazards Earth Syst. Sci., 11, 1351–1370, Bechtold,P.,Biavati,G.,Bidlot,J.,Bonavita,M.,DeChiara,G.,
https://doi.org/10.5194/nhess-11-1351-2011,2011. Dahlgren,P.,Dee,D.,Diamantakis,M.,Dragani,R.,Flemming,
DWD:WetterundKlima–DeutscherWetterdienst–Gemeindewar- J.,Forbes,R.,Fuentes,M.,Geer,A.,Haimberger,L.,Healy,S.,
nungenaktuell–Warnkriterien,https://www.dwd.de/DE/wetter/ Hogan,R.J.,Hólm,E.,Janisková,M.,Keeley,S.,Laloyaux,P.,
warnungen_aktuell/kriterien/warnkriterien.html?nn=605882 Lopez,P.,Lupu,C.,Radnoti,G.,deRosnay,P.,Rozum,I.,Vam-
(lastaccess:7May2024),2015. borg,F.,Villaume,S.,andThépaut,J.-N.:CompleteERA5from
ECMWF: 201901 – Windstorm – Alfrida/Aapeli, https: 1940:FifthgenerationofECMWFatmosphericreanalysesofthe
//confluence.ecmwf.int/pages/viewpage.action?pageId= globalclimate,CopernicusClimateChangeService(C3S)Data
129123779(lastaccess:24May2024),2021. Store (CDS) [data set], https://doi.org/10.24381/cds.143582cf,
Field, P. R. and Wood, R.: Precipitation and cloud struc- 2017.
ture in midlatitude cyclones, J. Climate, 20, 233–254, Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Horányi, A.,
https://doi.org/10.1175/JCLI3998.1,2007. Muñoz-Sabater,J.,Nicolas,J.,Peubey,C.,Radu,R.,Schepers,
Fink, A. H., Brücher, T., Ermert, V., Krüger, A., and Pinto, J. G.: D., Simmons, A., Soci, C., Abdalla, S., Abellan, X., Balsamo,
TheEuropeanstormKyrillinJanuary2007:synopticevolution, G.,Bechtold,P.,Biavati,G.,Bidlot,J.,Bonavita,M.,DeChiara,
meteorological impacts and some considerations with respect G.,Dahlgren,P.,Dee,D.,Diamantakis,M.,Dragani,R.,Flem-
to climate change, Nat. Hazards Earth Syst. Sci., 9, 405–423, ming, J., Forbes, R., Fuentes, M., Geer, A., Haimberger, L.,
https://doi.org/10.5194/nhess-9-405-2009,2009. Healy, S., Hogan, R. J., Hólm, E., Janisková, M., Keeley, S.,
Flaounas, E., Aragão, L., Bernini, L., Dafis, S., Doiteau, B., Laloyaux, P., Lopez, P., Lupu, C., Radnoti, G., de Rosnay, P.,
Flocas, H., Gray, S. L., Karwat, A., Kouroutzoglou, J., Li- Rozum, I., Vamborg, F., Villaume, S., and Thépaut, J.-N.: The
onello, P., Miglietta, M. M., Pantillon, F., Pasquero, C., Pat- ERA5 global reanalysis, Q. J. Roy. Meteor. Soc., 146, 1999–
lakas,P.,Picornell,M.Á.,Porcù,F.,Priestley,M.D.K.,Reale, 2049,https://doi.org/10.1002/qj.3803,2020.
M., Roberts, M. J., Saaroni, H., Sandler, D., Scoccimarro, E., Hewson,T.,Magnusson,L.,Breivik,O.,Prates,F.,Tsonevsky,I.,
Sprenger, M., and Ziv, B.: A composite approach to produce anddeVries,J.:WindstormsinnorthwestEuropeinlate2013,
reference datasets for extratropical cyclone tracks: application ECMWFNewsletter,139,122–128,2014.
toMediterraneancyclones,WeatherClim.Dynam.,4,639–661, Hewson, T. D. and Neu, U.: Cyclones, windstorms
https://doi.org/10.5194/wcd-4-639-2023,2023. and the IMILAST project, Tellus A, 67, 27128,
FMI: Tuulivaroituksia niin maalle kuin merelle, https://www. https://doi.org/10.3402/tellusa.v67.27128,2015.
ilmatieteenlaitos.fi/tuulivaroitukset (last access: 7 May 2024), Hodges, K. I.: A General Method for Tracking Analy-
2018. sis and Its Application to Meteorological Data, Mon.
FMI: Merkittäviä myrskyjä ja rajuilmoja Suomessa, https://www. Weather Rev., 122, 2573–2586, https://doi.org/10.1175/1520-
ilmatieteenlaitos.fi/merkittavia-myrskyja-suomessa(lastaccess: 0493(1994)122<2573:AGMFTA>2.0.CO;2,1994.
22May2024),2024. Hodges, K. I.: Feature Tracking on the Unit Sphere, Mon.
Fox, A., Sherwin, R., and Ralston, F.: Lessons learnt at the Weather Rev., 123, 3458–3465, https://doi.org/10.1175/1520-
Met Office from the Great Storm of 1987 – a compari- 0493(1995)123<3458:FTOTUS>2.0.CO;2,1995.
son with recent strong wind events, Weather, 67, 268–273, Hodges, K. I.: Spherical Nonparametric Estimators Ap-
https://doi.org/10.1002/wea.1981,2012. plied to the UGAMP Model Integration for AMIP, Mon.
Gaffney, S. J., Robertson, A. W., Smyth, P., Camargo, S. J., and Weather Rev., 124, 2914–2932, https://doi.org/10.1175/1520-
Ghil, M.: Probabilistic clustering of extratropical cyclones us- 0493(1996)124<2914:SNEATT>2.0.CO;2,1996.
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 227
Hodges, K. I.: Extension of Spherical Nonparametric Estima- Laurila, T. K., Gregow, H., Cornér, J., and Sinclair, V. A.: Char-
tors to Nonisotropic Kernels: An Oceanographic Application, acteristics of extratropical cyclones and precursors to wind-
Mon.WeatherRev.,127,214–227,https://doi.org/10.1175/1520- storms in northern Europe, Weather Clim. Dynam., 2, 1111–
0493(1999)127<0214:EOSNET>2.0.CO;2,1999a. 1130,https://doi.org/10.5194/wcd-2-1111-2021,2021a.
Hodges, K. I.: Adaptive Constraints for Feature Tracking, Mon. Laurila,T.K.,Sinclair,V.A.,andGregow,H.:Climatology,vari-
Weather Rev., 127, 1362–1373, https://doi.org/10.1175/1520- ability,andtrendsinnear-surfacewindspeedsovertheNorthAt-
0493(1999)127<1362:ACFFT>2.0.CO;2,1999b. lanticandEuropeduring1979–2018basedonERA5,Int.J.Cli-
Hodges, K. I.: Confidence Intervals and Signifi- matol.,41,2253–2278,https://doi.org/10.1002/joc.6957,2021b.
cance Tests for Spherical Data Derived from Fea- Leckebusch, G. C., Ulbrich, U., Fröhlich, L., and Pinto, J. G.:
ture Tracking, Mon. Weather Rev., 136, 1758–1777, Property loss potentials for European midlatitude storms
https://doi.org/10.1175/2007MWR2299.1,2008. in a changing climate, Geophys. Res. Lett., 34, L05703,
Hodges,K.I.,Lee,R.W.,andBengtsson,L.:AComparisonofEx- https://doi.org/10.1029/2006GL027663,2007.
tratropicalCyclonesinRecentReanalysesERA-Interim,NASA Leckebusch, G. C., Renggli, D., and Ulbrich, U.: Development
MERRA,NCEPCFSR,andJRA-25,J.Climate,24,4888–4906, and application of an objective storm severity measure for
https://doi.org/10.1175/2011JCLI4097.1,2011. the Northeast Atlantic region, Meteorol. Z., 17, 575–587,
Hoskins, B. J. and Hodges, K. I.: New Perspectives on https://doi.org/10.1127/0941-2948/2008/0323,2008a.
the Northern Hemisphere Winter Storm Tracks, J. At- Leckebusch, G. C., Weimer, A., Pinto, J. G., Reyers, M., and
mos. Sci., 59, 1041–1061, https://doi.org/10.1175/1520- Speth,P.:ExtremewindstormsoverEuropeinpresentandfu-
0469(2002)059<1041:NPOTNH>2.0.CO;2,2002. tureclimate:aclusteranalysisapproach,Meteorol.Z.,17,67–
Huo, Z., Zhang, D.-L., Gyakum, J., and Staniforth, A.: A Di- 82,https://doi.org/10.1127/0941-2948/2008/0266,2008b.
agnostic Analysis of the Superstorm of March 1993, Mon. Li, M., Woollings, T., Hodges, K., and Masato, G.: Ex-
Weather Rev., 123, 1740–1761, https://doi.org/10.1175/1520- tratropical cyclones in a warmer, moister climate: A re-
0493(1995)123<1740:ADAOTS>2.0.CO;2,1995. cent Atlantic analogue, Geophys. Res. Lett., 41, 8594–8601,
Hussain, M. M. and Mahmud, I.: pyMannKendall: a python https://doi.org/10.1002/2014GL062186,2014.
package for non parametric Mann Kendall family of Liberato,M.L.R.,Pinto,J.G.,Trigo,I.F.,andTrigo,R.M.:Klaus
trend tests, Journal of Open Source Software, 4, 1556, –anexceptionalwinterstormovernorthernIberiaandsouthern
https://doi.org/10.21105/joss.01556,2019. France,Weather,66,330–334,https://doi.org/10.1002/wea.755,
Jeglum, M. E., Steenburgh, W. J., Lee, T. P., and Bosart, 2011.
L. F.: Multi-reanalysis climatology of intermoun- Liberato, M. L. R., Pinto, J. G., Trigo, R. M., Ludwig, P.,
tain cyclones, Mon. Weather Rev., 138, 4035–4053, Ordóñez, P., Yuen, D., and Trigo, I. F.: Explosive develop-
https://doi.org/10.1175/2010MWR3432.1,2010. ment of winter storm Xynthia over the subtropical North At-
Karremann, M. K., Pinto, J. G., Reyers, M., and Klawa, M.: Re- lantic Ocean, Nat. Hazards Earth Syst. Sci., 13, 2239–2251,
turn periods of losses associated with European windstorm se- https://doi.org/10.5194/nhess-13-2239-2013,2013.
ries in a changing climate, Environ. Res. Lett., 9, 124016, Lou, W.-p., Chen, H.-y., Qiu, X.-f., Tang, Q.-y., and Zheng,
https://doi.org/10.1088/1748-9326/9/12/124016,2014. F.: Assessment of economic losses from tropical cyclone
Karwat,A.,Franzke,C.L.E.,andBlender,R.:Long-TermTrends disasters based on PCA-BP, Nat. Hazards, 60, 819–829,
of Northern Hemispheric Winter Cyclones in the Extended https://doi.org/10.1007/s11069-011-9881-x,2012.
ERA5 Reanalysis, J. Geophys. Res., 127, e2022JD036952, Ludwig, P., Pinto, J. G., Reyers, M., and Gray, S. L.: The
https://doi.org/10.1029/2022JD036952,2022. role of anomalous SST and surface fluxes over the south-
Kendall, M. G.: Rank Correlation Methods, Griffin, London, 4th eastern North Atlantic in the explosive development of wind-
edn.,ISBN9780852641996,1970. storm Xynthia, Q. J. Roy. Meteor. Soc., 140, 1729–1741,
Klawa, M. and Ulbrich, U.: A model for the estimation of https://doi.org/10.1002/qj.2253,2014.
storm losses and the identification of severe winter storms Mann, H. B.: Nonparametric tests against trend, Econometrica,
in Germany, Nat. Hazards Earth Syst. Sci., 3, 725–732, 245–259,https://doi.org/10.2307/1907187,1945.
https://doi.org/10.5194/nhess-3-725-2003,2003. Mann, H. B. and Whitney, D. R.: On a Test of Whether
Kouroutzoglou,J.,Flocas,H.A.,Hatzaki,M.,Keay,K.,Simmonds, one of Two Random Variables is Stochastically
I.,andMavroudis,A.:Identificationofthedevelopmentmecha- Larger than the Other, Ann. Math. Stat., 18, 50–60,
nismsofanexplosivecycloneinthecentralMediterraneanwith https://doi.org/10.1214/aoms/1177730491,1947.
the aid of the MSG satellite images, in: Proc. Spie., edited by: McCallum, E.: The Burns’ Day Storm, 25 January 1990,
Hadjimitsis,D.G.,Themistocleous,K.,Michaelides,S.,andPa- Weather, 45, 166–173, https://doi.org/10.1002/j.1477-
padavid,G.,vol.8795,87951S,InternationalSocietyforOptics 8696.1990.tb05607.x,1990.
andPhotonics,SPIE,https://doi.org/10.1117/12.2027584,2013. Menna, M., Martellucci, R., Reale, M., Cossarini, G., Salon, S.,
Laarne, P., Zaidan, M. A., and Nieminen, T.: ennemi: Non-linear Notarstefano,G.,Mauri,E.,Poulain,P.-M.,Gallo,A.,andSoli-
correlation detection with mutual information, Soft. X, 14, doro,C.:Acasestudyofimpactsofanextremeweathersystem
100686,https://doi.org/10.1016/j.softx.2021.100686,2021. ontheMediterraneanSeacirculationfeatures:MedicaneApollo
Laarne, P., Amnell, E., Zaidan, M. A., Mikkonen, S., and (2021),Sci.Rep.,13,3870,https://doi.org/10.1038/s41598-023-
Nieminen, T.: Exploring Non-Linear Dependencies in Atmo- 29942-w,2023.
spheric Data with Mutual Information, Atmosphere, 13, 1046,
https://doi.org/10.3390/atmos13071046,2022.
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025

228 J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity
MetÉireann: Weather warnings explanation – Met Éireann Python, J. Mach. Learn. Res., 12, 2825–2830, http://jmlr.org/
– The Irish Meteorological Service, https://www.met.ie/ papers/v12/pedregosa11a.html(lastaccess:24May2024),2011.
weather-warnings(lastaccess:7May2024),2024. Petterssen, S. and Smebye, S.: On the development of ex-
Metheniti, K.: A case of Rapid Cyclogenesis over Ionian tratropical cyclones, Q. J. Roy. Meteor. Soc., 97, 457–482,
Sea on February 6th, 2012, https://user.eumetsat.int/s3/ https://doi.org/10.1002/qj.49709741407,1971.
eup-strapi-media/pdf_il_12_02_06_6753093e86.pdf (last Pfahl,S.andSprenger,M.:Ontherelationshipbetweenextratrop-
access:24May2024),2012. icalcycloneprecipitationandintensity,Geophys.Res.Lett.,43,
METNorway: Vind over land, https://www.met.no/ 1752–1758,https://doi.org/10.1002/2016GL068018,2016.
vaer-og-klima/ekstremvaervarsler-og-andre-farevarsler/ Pinto, J. G., Fröhlich, E. L., Leckebusch, G. C., and Ulbrich,
vaerfenomener-som-kan-gi-farevarsel-fra-met/vind-over-land U.: Changing European storm loss potentials under modified
(lastaccess:7May2024),2021. climate conditions according to ensemble simulations of the
Minola, L., Zhang, F., Azorin-Molina, C., Pirooz, A. S., Flay, ECHAM5/MPI-OM1 GCM, Nat. Hazards Earth Syst. Sci., 7,
R., Hersbach, H., and Chen, D.: Near-surface mean and 165–175,https://doi.org/10.5194/nhess-7-165-2007,2007.
gust wind speeds in ERA5 across Sweden: towards an im- Priestley, M. D. K. and Catto, J. L.: Future changes in
proved gust parametrization, Clim. Dynam., 55, 887–907, the extratropical storm tracks and cyclone intensity, wind
https://doi.org/10.1007/s00382-020-05302-6,2020. speed, and structure, Weather Clim. Dynam., 3, 337–360,
Nagendra, S. S. and Khare, M.: Principal component analysis https://doi.org/10.5194/wcd-3-337-2022,2022.
of urban traffic characteristics and meteorological data, Trans- Priestley,M.D.,Ackerley,D.,Catto,J.L.,Hodges,K.I.,McDon-
port Res. D-Tr. E, 8, 285–297, https://doi.org/10.1016/S1361- ald,R.E.,andLee,R.W.:Anoverviewoftheextratropicalstorm
9209(03)00006-3,2003. tracks in CMIP6 historical simulations, J. Climate, 33, 6315–
Nakajo,S.,Mori,N.,Yasuda,T.,andMase,H.:Globalstochastic 6343,https://doi.org/10.1175/JCLI-D-19-0928.1,2020.
tropical cyclone model based on principal component analysis Raible, C. C., Della-Marta, P. M., Schwierz, C., Wernli, H.,
and cluster analysis, J. Appl. Meteorol. Clim., 53, 1547–1577, and Blender, R.: Northern Hemisphere Extratropical Cy-
https://doi.org/10.1175/JAMC-D-13-08.1,2014. clones: A Comparison of Detection and Tracking Methods
Neu,U.,Akperov,M.G.,Bellenbaum,N.,Benestad,R.,Blender, and Different Reanalyses, Mon. Weather Rev., 136, 880–897,
R.,Caballero,R.,Cocozza,A.,Dacre,H.F.,Feng,Y.,Fraedrich, https://doi.org/10.1175/2007MWR2143.1,2008.
K.,etal.:IMILAST:Acommunityefforttointercompareextra- Reboita,M.S.,Crespo,N.M.,Torres,J.A.,Reale,M.,Porfírioda
tropicalcyclonedetectionandtrackingalgorithms,B.Am.Me- Rocha,R.,Giorgi,F.,andCoppola,E.:Futurechangesinwinter
teorol.Soc.,94,529–547,https://doi.org/10.1175/BAMS-D-11- explosivecyclonesovertheSouthernHemispheredomainsfrom
00154.1,2013. theCORDEX-COREensemble,Clim.Dynam.,57,3303–3322,
Nielsen, J. W. and Dole, R. M.: A survey of extratropi- https://doi.org/10.1007/s00382-021-05867-w,2021.
cal cyclone characteristics during GALE, Mon. Weather Roberts,J.F.,Champion,A.J.,Dawkins,L.C.,Hodges,K.I.,Shaf-
Rev., 120, 1156–1168, https://doi.org/10.1175/1520- frey,L.C.,Stephenson,D.B.,Stringer,M.A.,Thornton,H.E.,
0493(1992)120<1156:ASOECC>2.0.CO;2,1992. and Youngman, B. D.: The XWS open access catalogue of ex-
Nissen, K. M., Leckebusch, G. C., Pinto, J. G., Renggli, D., Ul- treme European windstorms from 1979 to 2012, Nat. Hazards
brich, S., and Ulbrich, U.: Cyclones causing wind storms in Earth Syst. Sci., 14, 2487–2501, https://doi.org/10.5194/nhess-
the Mediterranean: characteristics, trends and links to large- 14-2487-2014,2014.
scale patterns, Nat. Hazards Earth Syst. Sci., 10, 1379–1391, Rudeva, I. and Gulev, S. K.: Climatology of cyclone
https://doi.org/10.5194/nhess-10-1379-2010,2010. size characteristics and their changes during the cy-
Palutikof,J.P.andSkellern,A.R.:StormSeverityoverBritain:a clone life cycle, Mon. Weather Rev., 135, 2568–2587,
ReporttoCommercialUnionGeneralInsurance,Tech.rep.,Cli- https://doi.org/10.1175/MWR3420.1,2007.
maticResearchUnit,SchoolofEnvironmentalSciences,Univer- Sanders, F. and Gyakum, J. R.: Synoptic-dynamic
sityofEastAnglia,Norwich,UK,1991. climatology of the “bomb”, Mon. Weather Rev.,
Pantillon,F.,Davolio,S.,Avolio,E.,Calvo-Sancho,C.,Carrió,D. 108, 1589–1606, https://doi.org/10.1175/1520-
S., Dafis, S., Gentile, E. S., Gonzalez-Aleman, J. J., Gray, S., 0493(1980)108<1589:SDCOT>2.0.CO;2,1980.
Miglietta,M.M.,Patlakas,P.,Pytharoulis,I.,Ricard,D.,Ricchi, Schüepp,M.,Schiesser,H.H.,Huntrieser,H.,Scherrer,H.U.,and
A.,Sanchez,C.,andFlaounas,E.:Thecrucialrepresentationof Schmidtke,H.:Thewinterstorm“Vivian”of27February1990:
deepconvectionforthecyclogenesisofMedicaneIanos,Weather Aboutthemeteorologicaldevelopment,windforcesanddamage
Clim. Dynam., 5, 1187–1205, https://doi.org/10.5194/wcd-5- situation in the forests of Switzerland, Theor. Appl. Climatol.,
1187-2024,2024. 49,183–200,https://doi.org/10.1007/BF00865533,1994.
Pasch,R.J.,Blake,E.S.,Cobb,H.D.,andRoberts,D.P.:Tropical Schultz, D. M., Keyser, D., and Bosart, L. F.: The ef-
cyclone report: Hurricane Wilma 15–25 October 2005, https:// fect of large-scale flow on low-level frontal structure
www.nhc.noaa.gov/data/tcr/AL252005_Wilma.pdf (last access: and evolution in midlatitude cyclones, Mon. Weather
24May2024),2006. Rev., 126, 1767–1791, https://doi.org/10.1175/1520-
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, 0493(1998)126<1767:TEOLSF>2.0.CO;2,1998.
B.,Grisel,O.,Blondel,M.,Prettenhofer,P.,Weiss,R.,Dubourg, Seiler,C.andZwiers,F.W.:Howwillclimatechangeaffectexplo-
V.,Vanderplas,J.,Passos,A.,Cournapeau,D.,Brucher,M.,Per- sive cyclones in the extratropics of the Northern Hemisphere?,
rot, M., and Duchesnay, E.: Scikit-learn: Machine Learning in Clim. Dynam., 46, 3633–3644, https://doi.org/10.1007/s00382-
015-2791-y,2016.
Nat.HazardsEarthSyst.Sci.,25,207–229,2025 https://doi.org/10.5194/nhess-25-207-2025

J.Cornéretal.:Classificationofextratropicalcyclonesusingmultiplemeasuresofintensity 229
Shahapure, K. R. and Nicholas, C.: Cluster Quality Analysis Us- Wang, J., Chen, L., and Li, S.: Characteristics of spring Mon-
ing Silhouette Score, in: 2020 IEEE 7th International Confer- golian cyclones in the recent 70 years: Background circula-
ence on Data Science and Advanced Analytics (DSAA), 747– tions and weather influences, Int. J. Climatol., 44, 328–343,
748,https://doi.org/10.1109/DSAA49011.2020.00096,2020. https://doi.org/10.1002/joc.8342,2024.
Sinclair, M. R.: Objective Identification of Cyclones and Wang, X. L., Feng, Y., Chan, R., and Isaac, V.: Inter-
Their Circulation Intensity, and Climatology, Weather comparison of extra-tropical cyclone activity in nine
Forecast., 12, 595–612, https://doi.org/10.1175/1520- reanalysis datasets, Atmos. Res., 181, 133–153,
0434(1997)012<0595:OIOCAT>2.0.CO;2,1997. https://doi.org/10.1016/j.atmosres.2016.06.010,2016.
Sinclair, V. A. and Catto, J. L.: The relationship between extra- Watanabe, T., Takenaka, H., and Nohara, D.: Framework of fore-
tropical cyclone intensity and precipitation in idealised cur- cast verification of surface solar irradiance from a numeri-
rent and future climates, Weather Clim. Dynam., 4, 567–589, cal weather prediction model using classification with a Gaus-
https://doi.org/10.5194/wcd-4-567-2023,2023. sian mixture model, Earth Space Sci., 7, e2020EA001260,
Sinclair,V.A.,Rantanen,M.,Haapanala,P.,Räisänen,J.,andJärvi- https://doi.org/10.1029/2020EA001260,2020.
nen, H.: The characteristics and structure of extra-tropical cy- Weijenborg, C. and Spengler, T.: Diabatic Heating as a Path-
clones in a warmer climate, Weather Clim. Dynam., 1, 1–25, way for Cyclone Clustering Encompassing the Extreme
https://doi.org/10.5194/wcd-1-1-2020,2020. Storm Dagmar, Geophys. Res. Lett., 47, e2019GL085777,
Smart, D. J. and Browning, K. A.: Attribution of strong winds to https://doi.org/10.1029/2019GL085777,2020.
acoldconveyorbeltandstingjet,Q.J.Roy.Meteor.Soc.,140, Wernli, H., Dirren, S., Liniger, M. A., and Zillig, M.: Dynami-
595–610,https://doi.org/10.1002/qj.2162,2014. cal aspects of the life cycle of the winter storm “Lothar” (24–
Statheropoulos,M.,Vassiliadis,N.,andPappa,A.:Principalcom- 26 December 1999), Q. J. Roy. Meteor. Soc., 128, 405–429,
ponentandcanonicalcorrelationanalysisforexaminingairpol- https://doi.org/10.1256/003590002321042036,2002.
lutionandmeteorologicaldata,Atmos.Environ.,32,1087–1095, Zappa, G., Shaffrey, L. C., and Hodges, K. I.: The Ability of
https://doi.org/10.1016/S1352-2310(97)00377-4,1998. CMIP5 Models to Simulate North Atlantic Extratropical Cy-
Stojanovic, M., Gonçalves, A., Sorí, R., Vázquez, M., Ramos, clones,J.Climate,26,5379–5396,https://doi.org/10.1175/JCLI-
A.M.,Nieto,R.,Gimeno,L.,andLiberato,M.L.R.:Consec- D-12-00501.1,2013a.
utiveExtratropicalCyclonesDaniel,ElsaandFabien,andTheir Zappa, G., Shaffrey, L. C., Hodges, K. I., Sansom, P. G., and
ImpactontheHydrologicalCycleofMainlandPortugal,Water, Stephenson, D. B.: A Multimodel Assessment of Future Pro-
13,1476,https://doi.org/10.3390/w13111476,2021. jectionsofNorthAtlanticandEuropeanExtratropicalCyclones
Suursaar,Ü.,Kullas,T.,Otsmann,M.,Saaremäe,I.,Kuik,J.,and in the CMIP5 Climate Models, J. Climate, 26, 5846–5862,
Merilain, M.: Cyclone Gudrun in January 2005 and modelling https://doi.org/10.1175/JCLI-D-12-00573.1,2013b.
its hydrodynamic consequences in the Estonian coastal waters, Zillman, J. W. and Price, P. G.: On the thermal structure of ma-
BorealEnviron.Res.,11,143–159,2006. ture Southern Ocean cyclones, Aust. Meteorol. Mag., 20, 34–
Thorncroft,C.,Hoskins,B.,andMcIntyre,M.:Twoparadigmsof 48, https://cir.nii.ac.jp/crid/1572261549005376128 (last access:
baroclinic-wave life-cycle behaviour, Q. J. Roy. Meteor. Soc., 24May2024),1972.
119,17–55,https://doi.org/10.1002/qj.49711950903,1993. Zou, H. and Xue, L.: A selective overview of sparse prin-
Ulbrich,U.,Fink,A.,Klawa,M.,andPinto,J.G.:Threeextreme cipal component analysis, P. IEEE, 106, 1311–1320,
storms over Europe in December 1999, Weather, 56, 70–80, https://doi.org/10.1109/JPROC.2018.2846588,2018.
https://doi.org/10.1002/j.1477-8696.2001.tb06540.x,2001. Zou, H., Hastie, T., and Tibshirani, R.: Sparse principal com-
Vrac, M., Chédin, A., and Diday, E.: Clustering a Global ponent analysis, J. Comput. Graph. Stat., 15, 265–286,
Field of Atmospheric Profiles by Mixture Decomposi- https://doi.org/10.1198/106186006X113430,2006.
tion of Copulas, J. Atmos. Ocean Tech., 22, 1445–1459,
https://doi.org/10.1175/JTECH1795.1,2005.
https://doi.org/10.5194/nhess-25-207-2025 Nat.HazardsEarthSyst.Sci.,25,207–229,2025