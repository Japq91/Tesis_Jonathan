1JANUARY2020 NAUD ET AL. 95
Evaluation of Modeled Precipitation in Oceanic Extratropical Cyclones Using IMERG
CATHERINEM.NAUD
AppliedPhysicsandAppliedMathematics,ColumbiaUniversity/NASAGISS,NewYork,NewYork
JEYAVINOTHJEYARATNAMANDJAMESF.BOOTH
EarthandAtmosphericSciences,CityUniversityofNewYork,CityCollegeandtheGraduateCenter,NewYork,NewYork
MINGZHAO
NOAA/GeophysicalFluidDynamicsLaboratory,Princeton,NewJersey
ANDREWGETTELMAN
NationalCenterforAtmosphericResearch,Boulder,Colorado
(Manuscriptreceived23May2019,infinalform13August2019)
ABSTRACT
Usingahigh-spatial-andhigh-temporal-resolutionprecipitationdataset,IntegratedMulti-satelliteRetrievals
forGPM(IMERG),extratropicalcycloneprecipitationisevaluatedintworeanalysesandtwoclimatemodels.
Basedoncyclone-centeredcomposites,allfourmodelsoverestimateprecipitationinthewesternsubsidingand
dry side of the cyclones, and underestimate the precipitation in the eastern ascending and moist side. By
decomposingthecompositesintofrequencyofoccurrenceandintensity(meanprecipitationratewhenpre-
cipitating),theanalysisrevealsatendencyforallfourmodelstooverestimatefrequencyandunderestimate
intensity,withtheformerissuedominatinginthewesternhalfandthelatterintheeasternhalfofthecyclones.
Differencesinfrequencyarestronglydependentoncycloneenvironmentalmoisture,whilethedifferencesin
intensityarestronglyimpactedbythestrengthofascentwithinthecyclone.Therearesomeuncertaintiesas-
sociatedwiththeobservations:IMERGmightunderreportfrozenprecipitationandpossiblyexaggerateratesin
vigorouslyascendingregions.Nevertheless,theanalysissuggeststhatallmodelsproduceextratropicalcyclone
precipitationtoooftenandtoolightly.Thesebiaseshaveconsequenceswhenevaluatingthechangesinpre-
cipitationcharacteristicswithchangesincycloneproperties:themodelsdisagreeonthemagnitudeofthechange
inprecipitationintensitywithachangeinenvironmentalmoistureandinprecipitationfrequencywithachange
incyclonestrength.Thiscomplicatesaccuratepredictionsofprecipitationchangesinachangingclimate.
1. Introduction precipitation, and yet, because of the sheer number of
processes involved forits production and their nonlinear
Overthepastseveralyears,considerableefforthasbeen
nature,itisalsoadifficultparametertoevaluate(Tapiador
putintofindingnewwaysofevaluatinggeneralcirculation
etal.2019).
modelssothatcompensatingerrorscanbeavoidedandthe
Precipitation in the midlatitudes is predominantly
underlyingprocessesthatmightcauseuncertaintiescanbe
produced in extratropical cyclones (Hawcroft et al.
better isolated. Among the quantities that are important
2012),andthereforeanumberoftechniquestoestimate
foramodeltorepresentaccurately,onethatstandsoutis
precipitation in the cyclones have been proposed. Of
interestherearecyclone-centeredcomposites.Initially
Supplementalinformationrelatedtothispaperisavailableat introduced for cloud types by Lau and Crane (1995),
the Journals Online website: https://doi.org/10.1175/JCLI-D-19- they have been extensively used as well to provide
0369.s1. information on precipitation processes in cyclones
(Field and Wood 2007; Wong et al. 2018), on how
Correspondingauthor:CatherineM.Naud,cn2140@columbia.edu these processes might evolve in a changing climate
DOI:10.1175/JCLI-D-19-0369.1
(cid:1)2019AmericanMeteorologicalSociety.Forinformationregardingreuseofthiscontentandgeneralcopyrightinformation,consulttheAMSCopyright
Policy(www.ametsoc.org/PUBSReuseLicenses).
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

96 JOURNAL OF CLIMATE VOLUME33
(Bengtssonetal.2009;Cattoetal.2011),andonhow 4 (AM4; Zhao et al. 2018). For the comparison, we
well they are represented in general circulation focus on the mean precipitation in the cyclones (an
models (GCMs) (Bauer and Del Genio 2006; Field average of events including those with zero precipi-
et al. 2008, 2011; Catto et al. 2010; Hawcroft et al. tationrates),aswellasonthefrequencyofoccurrence
2016, 2017; Yettella and Kay 2017; Booth et al. of precipitation (fraction of the precipitating events
2018a). The cyclone-centered view allows us to sep- outofallevents)andthemeanratewhenprecipitating
arate areas of ascent from subsidence as well as re- (an average of only precipitating events). By decom-
gionsofcold/dryandwarm/moistair.Thisprovidesa posing precipitation this way, we can identify whether
natural delineation between different precipitation theperformanceofthemodelsvis-à-vistheobservations
conducive regimes. There have been a number of fortotalprecipitationisaffectedbycompensatingerrors
studies that have used precipitation in cyclones to in frequency and intensity. In addition to comparing
evaluate model performance (e.g., Booth et al. 2018a), models and observations, we discuss the potential un-
but none has decomposed the mean precipitation into certainties associated with the observations that might
thefrequencyofoccurrenceandmeanprecipitationrate explain some of the differences. Then we investigate
when precipitating specifically in a cyclone-centered howchangesincyclonepropertiesrelatetochangesin
frame of reference. This distinction is important be- the precipitation characteristics for the observations
cause the impact of a light and frequent rain event is and the models. We discuss the implications of our
differentfromtheimpactofaneventwithintermittent resultsforthemodelrepresentationofthesensitivityof
heavy rain, while producing on average the same precipitationtochangesinenvironmentalconditionsin
amountatthesurface.Relatedtothis,modelsdesigned extratropicalcyclones.
forclimatechangepredictionsneedtoaccuratelyrepre-
sent the sensitivity of precipitation to changes in envi-
2. Dataandmethodology
ronmentalconditions,intermsoftotalamountsbutalso
separatelyintermsoffrequenciesandrates. Thestudyisfocusedonthelatituderange308–608in
Because compositing on cyclones includes a large bothhemispheres,andincludesobservationsinallseasons
number of cases at high temporal resolution, rela- fromMarch2014toDecember2017.Herewedescribethe
tivelyshortperiodsofobservationscanbeused.This observations,models,andthemethodemployedtocom-
means that recently launched missions such as the paremodelstoobservations.
Global Precipitation Measurement mission (GPM;
a. ObservationsofprecipitationwiththeIMERG
Hou et al. 2014), which includes a dual-frequency
product
precipitation radar on board the Core Observatory sat-
ellite (Skofronick-Jackson et al. 2017), can already be Precipitationobservationsareobtainedwiththeversion
utilized.Therefore,inthisstudy,weusethehigh-spatial- 5IMERG‘‘finalrun’’product(availablewitha4-month
resolution (0.18 3 0.18) and high-temporal-resolution delay for research applications; Huffman et al. 2017),
(30min) Integrated Multi-satellite Retrievals for GPM whichprovidesgriddedprecipitationratesataresolution
product (IMERG; Huffman et al. 2017) to explore the of0.18 30.183 30minupto;658N/S.Precipitationesti-
performanceoffourdistinctmodelsfortheirrepresen- matesareobtainedfromthemergingofpassivemicrowave
tation of precipitation characteristics in extratropical radiometer observations from theGlobal Precipitation
cyclones. While a reanalysis is highly constrained for Measurement(Skofronick-Jacksonetal.2017)constel-
its thermodynamics fields through data assimilation, lationofsatellites.TheGPMCoreObservatoryisused
it relies on modeling for its representation of precipi- as a standard reference to intercalibrate the individu-
tation. Therefore, we refer to the two reanalyses ex- al radiometers in the constellation. A summary of the
amined herein as models. These reanalyses are the variousstepsinvolvedintheproductionoftheIMERG
Modern-Era Retrospective Analysis for Research and precipitationestimatesisgiveninTanetal.(2017)along
Applications,version2(MERRA-2;Gelaroetal.2017), witha discussion ofuncertainties at different temporal
andtheEuropeanCentreforMedium-RangeWeather and spatial resolution, and a full description of the al-
Forecastsinterimreanalysis(ERA-Interim;Deeetal. gorithmisavailableinHuffmanetal.(2017).Asimple
2011). The other two models are free-running GCMs, wet-bulb-temperature test is applied to separate liquid
the latest National Center for Atmospheric Research fromicephasetoprovideaprobabilityofliquidphase
model(NCAR)CommunityAtmosphereModel,version precipitationaswell(Huffmanetal.2017).InNaudetal.
6 (CAM6; e.g., Gettelman et al. 2018), and a develop- (2018),wefoundagoodagreementbetweenIMERGand
ment version of the latest Geophysical Fluid Dynam- CloudSat(Stephensetal.2002;Haynesetal.2009)for
ics Laboratory (GFDL) Atmosphere Model, version precipitationinextratropicalcyclones,withamaximum
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

| 1JANUARY2020 |     |     |     | NAUD | ET AL. |     |     |     |     | 97  |
| ------------ | --- | --- | --- | ---- | ------ | --- | --- | --- | --- | --- |
TABLE1.ModelcharacteristicsandestimatedminimumprecipitationrateforIMERGbasedonTanetal.(2017)fora1.258318final
spatialresolution.
Minimumprecipitation
Model Originalspatialresolution Timeaveraging Epoch rate(mmh21)
| MERRA-2     |     | 0.625830.58  |     |     | 1-hmean       | 2014–16 |     |     | 0.013 |     |
| ----------- | --- | ------------ | --- | --- | ------------- | ------- | --- | --- | ----- | --- |
| ERA-Interim |     | 18318        |     |     | 6-hmean       | 2014–15 |     |     | 0.005 |     |
| GFDL        |     | 1.258318     |     |     | 6-hmean       | 2008–12 |     |     | 0.005 |     |
| CAM6        |     | 1.25830.9438 |     |     | Instantaneous | 2010–14 |     |     | 0.018 |     |
difference within 0.02mmh 21. While IMERG and and a development version of the GFDL AM4 model
CloudSat reportedsimilarfrequenciesoflight,medium, [seeZhaoetal.(2018)foradetaileddescriptionofthe
andintenseprecipitation,thedifferenceinprecipitation operational version, AM4.0] referred to here as de-
rates within the cyclones was found to change in sign vAM4 to distinguish it from the operational AM4.0
dependingontheamountofenvironmental(i.e.,cyclone- version.MoredetailsonCAM6arealsoavailableonthe
local) precipitable water (PW). The IMERG product development site (http://www.cesm.ucar.edu/working_
reported greater precipitation rates than CloudSat groups/Atmosphere/development/). Both atmosphere-
21differenceinprecipitationaveragedina
| (;0.04mmh |     |     |     |     | only integrations | of  | the CAM6 | and | devAM4 | are |
| --------- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | ------ | --- |
1500-km region centered on the cyclones) in moist en- forced with climatological sea surface temperatures
.
vironments (PW 19mm) and lower precipitation over a 5-yr period (2010–14 for CAM6, 2008–12 for
rates (up to 0.07mmh 21 difference) in dry (PW , devAM4)andoutputprecipitation,sealevelpressure,
, ,
11mm) and moderately moist (11 PW 19mm) precipitablewater,and500-hPaverticalvelocitiesevery
environments (Naud et al. 2018). That analysis 6h. CAM6 provides instantaneous surface precipitation
providesabenchmarktoevaluatethemagnitudeand rateswhereasdevAM4providesa6-hourlymean.
importance of biases between models and IMERG As indicated in Table 1, while the observations are
precipitation. Overall, with its high temporal resolu- availablefor2014–17atthetimeofthisstudy,thefree-
tionandglobalcoverage,IMERGoffersamuchlarger running GCMs are available for differing periods. Be-
sample despite its relatively shorter observing period causetheyarefreerunning,theGCMcyclonesarenot
thanCloudSat,ismoreaccurate[seeNaudetal.(2018) coincidentintimeorspacewiththoseinthereanalysis.
for details] than the current version of the combined Byusinga5-yrperiod,weensurethatwehaveenough
GPM core mission precipitation product (Grecu et al. cyclones to obtain a climatologically adequate repre-
2016), and is better suited to track cyclones than the sentation of the cyclone precipitation, and therefore
daily Global Precipitation Climatology Project dataset limit the impact of interannual variability (e.g., Naud
(Huffmanetal.2001).Therefore,itistheidealdataset et al. 2018). For the two reanalyses, because we can
forthismodelevaluation. matchtheobservedcyclonesinspaceandtime,shorter
|     |     |     |     |     | periods | can be used. | Based | on the | availability | of  |
| --- | --- | --- | --- | --- | ------- | ------------ | ----- | ------ | ------------ | --- |
b. Reanalysesandfree-runningGCM
|     |     |     |     |     | reanalysis | output at the | time | of this | work, | 2014–16 |
| --- | --- | --- | --- | --- | ---------- | ------------- | ---- | ------- | ----- | ------- |
precipitationproducts
|     |     |     |     |     | and 2014–15 | were used | instead | for | MERRA-2 | and |
| --- | --- | --- | --- | --- | ----------- | --------- | ------- | --- | ------- | --- |
Forthereanalyses,weuseMERRA-2totalprecipitation ERA-Interim,respectively.
| rates and | snowfall, and | ERA-Interim | total precipitation |     |     |     |     |     |     |     |
| --------- | ------------- | ----------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
c. Adjustingtheprecipitationproducts
| rates. In Naud | et al. | (2018), the cyclone-centered |     | total |     |     |     |     |     |     |
| -------------- | ------ | ---------------------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
forcomparison
| precipitation | composites | from both | reanalyses | were |     |     |     |     |     |     |
| ------------- | ---------- | --------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
found to be very close to IMERG/CloudSat estimates, Becausewewanttocompareprecipitationfrequency
withthemeanprecipitationinaradiusof1500kmfrom of occurrence and rain rates when raining from obser-
21
the storm centers within 0.01mmh from the obser- vationproductswithmodeledestimates,itisparamount
vations.However,thefrequencyofoccurrenceormean to ensure that the spatial and temporal resolution
intensity (i.e., rate when precipitating) was not tested of both precipitation products is identical. For this
andtheagreementmightbetheresultofcompensating firststep,weimposethesamespatialresolutiontoall
| errors. |     |     |     |     | models | and IMERG. | We chose | a 1.258 | 3 18 | spatial |
| ------- | --- | --- | --- | --- | ------ | ---------- | -------- | ------- | ---- | ------- |
Forthefree-runningGCMs,weusethelatestversion resolutionforthecomparison.However,eachmodel
oftheNCARmodel,CAM6,whichisslatedtobepart hasitsowntemporalresolutionandfrequencyofoutput
ofthenextCMIPexercise[seeGettelmanetal.(2018) (meanoveraperiodorinstantaneousoutput)andthus
for a description of basic physics parameterizations], IMERGneedstobeseparatelyadjustedforthisaswell.
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

98 JOURNAL OF CLIMATE VOLUME33
We therefore average IMERG products over different snapshotisobtained.Consequently,multipleoccurrences
timescalestomatchthemodeledprecipitation:6-hourly ofthesamesystematdifferenttimesareincludedinthe
mean, 1-hourly mean, and instantaneous (see Table 1 analysis. We then construct composites of total pre-
fordetails). cipitation, frequency, and mean rate using the cyclone
The second step accounts for the limited sensitivity center(i.e.,minimuminsealevelpressure)asananchor
tolightprecipitationofanyobservationaldataset.While in a cyclone-centered equal area grid of 100-km spatial
models can technically report precipitation rates over resolution.Thesamecyclonelocationdatabaseisused
aninfiniterangeofintensity,observationaldatasetsrely to construct cyclone-centered composites of precipi-
on instruments that have a finite detectability limit. In tation using IMERG, MERRA-2, and ERA-Interim
the case of IMERG, Tan et al. (2017)provide a useful precipitationproducts.Forthefree-runningGCMs,the
formulatoderivetheminimumdetectableandreliable same MCMS cyclone detection algorithm is applied to
precipitation rate for any spatial and temporal reso- theirrespectiveSLPproducts.
lution after regridding. IMERG and modeled precipi- The cyclone-centered square grid spans 61500km
tation rates that are less than this minimum threshold (north–south and east–west of the low) and each
are set to 0mmh 21 to ensure that two sets have com- 100km3 100km cell ispopulated by 1) the numberof
parable sensitivity to light rain before the comparison datapointsthatfallinthisgridcellbasedonthedistance
is conducted (see Table 1 for the threshold used for between the original grid cell and the center of the cy-
eachmodel). clone,2)thenumberofthesedatapointsthatdohavea
In this study, we are interested in oceanic cyclones precipitation retrieval/product, 3) the number of these
andprecipitationovertheopenocean.Forthis,weonly datapointsthatdohaveaprecipitationrate.0mmh 21,
selectcycloneswithacenter(locationoftheminimum and4)whattheaccumulatedrateis.Anexampleofthe
in sealevelpressure)overtheocean,but thisdoes not projection of the gridded precipitation products into a
preventthesurroundingareatoincludelandorseaice. cyclonecenteredgridisshowninNaudetal.(2018).
Because IMERG does not provide precipitation infor- Finally, using all cyclones in the database and the
mationpolewardofapproximately658N/S,weimposea regridded precipitation products, we construct com-
conservativecutoffat608N/Slatitudeinallmodels(i.e., posites by superimposing the cyclone centers found
none of the grid cells outside of 608S–608N are used, inthetwohemispheresbetween308and608latitude
regardlessofwherethestormcentersarefound)sowe over the ocean. These composites provide in each
find very littleimpact fromsea ice. For thereanalyses, 100km 3 100km grid cell: the mean precipitation
we only use the precipitation rates where and when PwhenP$0mmh 21,themeanprecipitationratewhen
IMERG is available, so the cutoff is included by con- P.0mmh 21(thereafterreferredtoasintensity),and
struct.UsingMERRA-2forwhichwehaveinformation thefrequencyofoccurrenceofprecipitation(hereafter
onboth landandseaice presencein eachgridcell, we referred to as frequency), that is, the ratio of the total
testedtheimpactontheprecipitationofincludingver- number of occurrences of P . 0mmh 21 to the total
susdiscardinggridcellswherelandorseaiceispresent. number of data points with P $ 0mmh 21 across all
Noimpactfromseaicewasfound.Landcanbepresent cyclones.Insomepreviousstudiesarotationofthecy-
in various sectors of the cyclones but on average has a cloneswasappliedpriortocompositingtoalignspecific
rather negligible impact, if any. Therefore, even when featuresandalleviatethesmoothingeffectofaveraging
informationonsurfacetypeisnotavailable,ourresults very disparate systems. This rotation was necessary to
are not affected by possible contamination by land be able to relate surface properties to cyclone pre-
surfaces. cipitation (e.g., Rudeva and Gulev 2011), to compare
reanalysis to GCM dynamical features within cyclones
d. Compositingmethod
(e.g., Catto et al. 2010), or to explore frontal features
The analysis herein is focused on extratropical cy- (Govekaretal.2011;Naudetal.2012).Herenorotation
clones, and we use the center of the cyclones as an is deemed necessary as we are only interested in the
anchortoaverageprecipitationpropertiesinbothob- overall spatial distribution of precipitation in all cy-
servationsandmodels.Todothis,weuseadatabaseof clonesofallages.
cyclonelocations,obtainedusingtheModeling,Anal- Toobtaininformationonthecyclonesthemselves,we
ysisandPrediction(MAP)ClimatologyofMidlatitude calculatecyclone-widedomainaveragesasinFieldand
Storminess (MCMS) tracking algorithm (Bauer et al. Wood(2007).Forthis,noregriddingisusedbecausethe
2016) applied to 6-hourly sea level pressures. Each analysis is focused on bulk characteristics. We collect
6-hourly cyclone snapshot is thereafter referred to as a gridded MERRA-2 products for the observations
‘‘cyclone,’’regardlessofwhenduringthecyclonelifethis and reanalyses, and modeled fields for the GCMs of
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 99
precipitablewater(PW)andverticalvelocityat500hPa motions(i.e.,subsidencetothewestversusascentto
and average them in a circular area of 1500-km radius the east as indicated with the 500-hPa vertical velocity
centered on the point of minimum SLP. For vertical composites in Figs. 1c, 1g, 1k,and 1o). In otherwords,
velocities, we only average data points where it is as- the models tend to underestimate precipitation in the
cending (negative in pressure coordinates), again in a region of ascent where it is relatively heavy, but over-
1500-km circle. By only including ascent, we obtain a estimateprecipitationinthesubsidenceregionwhereit
moredirect relationtocyclonestrengththanifthede- is intermittent and light. The relative difference com-
scending region (positive in pressure coordinates) was posites(i.e.,differencenormalizedbytheIMERGcom-
included in the average. This gives information on the posites;rightcolumninFig.1)indicatethattherelative
environmentalmoistureamountavailabletothecyclone bias in the subsidence region is larger than that in the
anditsdynamicalstrength.Tofurtherhelpcharacterize ascent region. Because composites involve averaging,
thecorrespondencebetweenthecyclonedynamicsand the possibility exists that the biases are related to dif-
precipitation, we also composited 500-hPa vertical ve- ferencesinextreme,suchasthepresenceofoutliersin
locityfromeachmodelinacyclone-centeredpolargrid, thecyclonedatabasethatmighthavealargeimpacton
using the same cyclones that are in the precipitation thedifferencesbutarenotthenorm.Therefore,wealso
composites. examine the distributions of precipitation within the
cyclones,forallcyclones,asreportedwithIMERGand
all four models (Fig. 2). The distributions are overall
3. Precipitationinextratropicalcyclones:Models
similarinshape,confirmingthatthedifferencesinthe
versusIMERG
composites are not influenced by extremes: all four
Using cyclone-centered composites of precipitation modelstendtoproducelightprecipitationmoreoften
characteristics,wefirstcomparethefourmodelstothe than reported by IMERG, regardless of time averag-
IMERGproduct. ing,andproduceheavyprecipitationlessoften.These
differences were found to be significantly larger than
a. Evaluationofmodeledcyclone-centeredmean
the variability in IMERG intensity for each intensity
precipitationagainstIMERG
bin.Next,weexploreifthebiasescomefromdifferences
All four models produce a cyclone-centered spatial inthefrequencyofprecipitationorfromtheprecipita-
distributionofprecipitationsimilartoobserved(Fig.1): tionintensity,orboth.
1) a maximum ;250km poleward and east of the cy-
b. Precipitationintensityandfrequency
clone center that extends equatorward and to the east
inacommashapeand2)aminimumtothewestofthe For models and IMERG, there is a maximum in fre-
low pressure center. Because of the different temporal quencyofprecipitationaroundthecenterofthecyclones,
resolutions of the model data (and hence different av- and the frequency diminishes away from the center
eragingofIMERGforthecomparisons;seesection2), (Fig.3).Allfourmodelstestedherepredictafrequency
therearevariationsinthemagnitudeof themaximum ofprecipitationthatislargerthanreportedbyIMERG
in precipitation, with slightly larger values when using everywhereinthecyclonearea.OnlyCAM6(Fig.3m)
6-hourlymeanthan1-hmeanorinstantaneousvalues.This retainsthecommashapethatisreportedwithIMERG
isclearlyvisibleintheIMERGcomposites(Figs.1b,f,j,n), (Figs.3b,f,j,n);allothermodelspredictarathercircular
with the IMERG average used in comparison with spatialdistribution.Thisbiasinthespatialpatterninthe
ERA-Interim and GFDL (6-h mean) similar to one models may possibly be a result of the time averaging
another but slightly different from the IMERG com- of the output. Recall that we aggregate the 30-min in-
positesusedforcomparisonwithMERRA-2(1-hmean) stantaneousIMERGdataintoa6-haverage,butitstill
andCAM6(instantaneous).Thereareslightdifferences startsasinstantaneousdataratherthananaccumulated
betweenthe IMERG composites using 6-hourly mean, sum that is averaged. The difference in precipitation
because to match ERA-Interim only two years of cy- frequency is relatively smaller in the region of ascent
clones areused whereas a whole 5-yr periodisused to than in the cold sector to the west of the low. This is
matchtheGFDLepochlength. demonstrated with both the absolute and relative dif-
Thecompositesofthedifferencebetweeneachmodel ferencecomposites(Figs.3c,d,g,h,k,l,o,p).Theregionof
and IMERG show a consistent picture: the models ascent is an area where precipitation happens fre-
slightly overestimateprecipitation tothewest ofthe quently across cyclones, whereas it is intermittent in
lowandunderestimateprecipitationtotheeastofthe the cold sector, and therefore the magnitude of the
lowwhencomparedtoIMERG.Thesignofthebias differences in frequency reflect these contrasting
changes with the sign of the mean cyclone vertical characteristics.
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

100 JOURNAL OF CLIMATE VOLUME33
FIG.1.(left)Cyclone-centeredcompositesofmeanprecipitationratesfrommodels,(middleleft)correspondingaveragedIMERGat
differenttemporalresolution,(middleright)differencebetweenthetwo,and(right)differencerelativetoIMERGfor(a)–(d)MERRA-2,
(e)–(h)ERA-Interim,(i)–(l)GFDLdevAM4,and(m)–(p)CAM6.AllmodelsandIMERGarefirstaveragedinthesameglobal1.258318
resolutiongridbeforethecompositesareconstructed.Theplussignindicatesthecyclonecenter;themeanincludesbothNorthernand
SouthernHemispherecyclones,thelatterhavingbeenflippedalongthenorth–southaxistomatchtheirNorthernHemispherecoun-
terparts.Cyclone-centeredcompositesof500-hPaverticalvelocityareshownasblackcontours,withnegativevaluessetassolidcontours
andpositivevaluessetasdashedcontoursfor(c)MERRA-2,(g)ERA-Interim,(k)GFDLdevAM4,and(o)CAM6.
Conversely, all models predict a lower precipitation in the entire cyclonic region, it appears that the dif-
intensitythanIMERGinmostofthecyclonearea,while ference in total precipitation in the ascent region is
retaining the comma-shape pattern in the region of dominated by weaker precipitation intensity in models
maximum rates in the composite (Fig. 4). The abso- compared to IMERG (Fig. 4), while in the subsidence
lutedifferenceindicatesagreaterbiastotheeastthan regionthedifferenceintotalprecipitationisdominated
the west of the low (Figs. 4c,g,k,o), which is to some by a greater frequency (Fig. 3). This suggests that the
extent also shown by the relative difference com- differencesarecausedbypotentiallydifferentprocesses;
posites,albeitwithamaximumdifferenceinintensity therefore,wenextinvestigatetheimpactofthecyclone
inthepolarhalfofthecoldsector. propertiesonthesedifferences.
Overall,whileallfourmodelsaresystematicallygiv- The cyclone properties used are 1) the cyclone-wide
inglowerintensityandhigherfrequenciesthanIMERG meanprecipitablewaterand2)themeanoftheascending
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

| 1JANUARY2020 |     |     | NAUD | ET AL. |     |     |     |     |     | 101 |
| ------------ | --- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- |
butwilldiscussthegeneralityoftheresultsfortheother
models(figuresforthesemodelsareinthesupplemental
material).
a. ComparisonofMERRA-2andIMERG
cycloneprecipitationasafunctionofPW
andascentstrength
|     |     |     |     | We classify     |            | the cyclones |         | based    | on their     | 1500-km-      |
| --- | --- | --- | --- | --------------- | ---------- | ------------ | ------- | -------- | ------------ | ------------- |
|     |     |     |     | radius mean     | PW         | (using       | 11mm    | to       | separate     | dry and       |
|     |     |     |     | medium          | cyclones   | and          | 19mm    | to       | separate     | medium        |
|     |     |     |     | and wet         | cyclones)  | and          | their   | mean     | ascent       | strength (us- |
|     |     |     |     | 26.8hPah        | 21         |              |         |          |              |               |
|     |     |     |     | ing             |            | to separate  |         | strong   | and moderate | cy-           |
|     |     |     |     | clones and      | 24.7hPah   |              | 21 to   | separate | moderate     | and           |
|     |     |     |     | weak cyclones). |            | These        | three   | PW       | and          | three ascent  |
|     |     |     |     | strength        | categories | were         | defined | by       | dividing     | the en-       |
|     |     |     |     | tire cyclone    | database   |              | for     | 2006–16  | into         | equal pop-    |
|     |     |     |     | ulation         | subsets    | (Naud        | et al.  | 2017).   | Combining    | these         |
FIG.2.Frequencydistributionofprecipitationintensitywithin
|           |                             |          |             | PW and | ascent | strength | categories |     | we  | obtain nine |
| --------- | --------------------------- | -------- | ----------- | ------ | ------ | -------- | ---------- | --- | --- | ----------- |
| cyclones, | for all cyclones, according | to IMERG | (solid) and |        |        |          |            |     |     |             |
(a)MERRA-2,(b)ERA-Interim,(c)devAM4,and(d)CAM6 subsetsofthecyclonedatabaseandexploretheimpact
(dashed).
|     |     |     |     | of these                | two parameters |     | on  | the precipitation |         | intensity |
| --- | --- | --- | --- | ----------------------- | -------------- | --- | --- | ----------------- | ------- | --------- |
|     |     |     |     | usingIMERG(Fig.5).Inthe |                |     |     | ascent            | region, | bothPW    |
vertical velocities (ascent strength). Precipitation in and ascent strength enhance precipitation intensity as
cycloneswasshowntodependonbothenvironmental theyincrease,whilemuchmoresubtlechangesoccurin
moisture amount and cyclone dynamics using surface thecoldsector.Whiletheimpactoftherebeingdifferent
windspeed(FieldandWood2007;PfahlandSprenger amounts of cyclone-centered PW is mainly visible as a
2016). Here, to characterize the cyclone strength, we change in the composite-mean precipitation intensity
chooseverticalvelocitiesintheascentregionbecause near the center of the cyclones, changes in the ascent
itrelatesdirectlytotheproductionofprecipitationas strengthaffectthesizeofthecommaregionandtherest
in warm conveyor belts (e.g., Eckhardt et al. 2004). ofthewarmsectoraswell.Similarly,frequencyofpre-
Using the cyclone-centered bulk averages obtained cipitation increases with ascent strength in most of the
fromMERRA-2,weexaminedtherelationshipbetween cyclone area but with the maximum increase at the
cyclonemeanascentstrengthandPW,andthecorrela- center (Fig. 6). It also increases at the center with in-
tion is small (r 5 20.14). Similarly, using all the grid creasing environmental PW, but the changes are less
pointswithinindividualcycloneswefindnocorrelation clearinotherpartsofthecyclones:thereisatendency
betweenPWandverticalvelocityat500hPa,foreither foraregionofrelativelygreaterfrequencyatthetailofthe
ascending or subsiding regions. This lack of a relation- commatomovefromeast to west as PW increases on
shiplikelyrelatestothefactthatcyclonestendtotravel the equator side of the low, but this is not seen for
poleward (i.e., to drier regions) as their circulation in- strong cyclones. Similar sensitivities are also found
tensifies.Boothetal.(2018b)showthatthisfactexplains whenusingthemodeledprecipitationcharacteristics;
whythereisatimelagbetweentheinstantofmaximum however, there are differences that might have im-
in precipitation and the instant of maximum cyclone portantimplicationsforunderstandingthemodelbiases.
intensityforextratropicalcyclonelifecycles.Thisresult First,thedifferenceinprecipitationintensitybetween
isconsistentwiththenegativecorrelationbetweenPW MERRA-2 and IMERG is strongly modulated by the
and surface winds found by Field and Wood (2007). strengthoftheascent(Fig.7):thebiasisratheruniform
Giventhesepriorresults,andtheweakcorrelationbe- in most of the cyclone area, with a maximum in the
tween PW and ascent strength, we use both factors to regionofascent,whichincreasesascyclonestrength
conditionallysortthecyclones. increases,regardlessoftheamountofmoistureinthe
|     |     |     |     | cyclone    | environment. |     | In fact,   | the | sensitivity | of the      |
| --- | --- | --- | --- | ---------- | ------------ | --- | ---------- | --- | ----------- | ----------- |
|     |     |     |     | difference | in intensity |     | to changes |     | in PW       | is not that |
4. Theimpactofcyclonepropertieson
|     |     |     |     | clear. Similar |     | results | are found | for | the other | models |
| --- | --- | --- | --- | -------------- | --- | ------- | --------- | --- | --------- | ------ |
precipitationdifferences
(seetheonlinesupplementalmaterial).However,the
Forthispartoftheinvestigation,wefocusoncomparing relativedifferenceinprecipitationintensitynormalized
IMERG and MERRA-2 to simplify the presentation, withIMERGintensityrevealsnosystematicchangesin
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

102 JOURNAL OF CLIMATE VOLUME33
FIG.3.(left)Cyclone-centeredcompositeofprecipitationfrequencyfrommodels,(middleleft)corresponding averagedIMERG,
(middleright)differencebetweenthetwo,and(right)differencerelativetoIMERGfor(a)–(d)MERRA-2,(e)–(h)ERA-Interim,(i)–(l)
GFDL devAM4, and (m)–(p) CAM6. The plus sign indicates the cyclone center; the mean includes both Northern and Southern
Hemispherecyclones,thelatterhavingbeenflippedalongthenorth–southaxistomatchtheirNorthernHemispherecounterparts.
biaswithstormstrengthorPW(notshown),suggesting tendstobelargestonthepolewardsideofthecoldsector,
that,assumingIMERGintensityreportingisnotbiased weobservethatinthecaseofthelowestPWcategory,the
itself,modelssystematicallyunderestimateprecipitation bias is largest at the center of the cyclones whenthe cy-
intensity,regardlessofcyclonecharacteristics. clonesareweak.IfIMERGdetectionsareassumedtobe
Incontrast,themodelbiasinfrequencyofprecipitation correct (more on this later), these results suggest that
is largest in the cold sector, and the difference there de- models might overproduce precipitation in cold and dry
creasesasPWincreases(Fig.8).Awayfromtheregionof regionsofthecyclones,especiallyifthecyclonesareweak.
ascent,thedifferencesshowlittledependencyoncyclone These results are found to be similar for all models
strength.Atthecenterofcyclonesandinthecommare- tested here (figures available in the supplemental ma-
gion,thedifferencedependsonbothPWandascent,and terial):apropensitytopredictlowerintensityinstrong
decreasesasbothparametersincrease.Infact,thediffer- cyclones’regionsofascent,andlargerfrequencyincold
ence near the center is minimized in the strongest and sectors, especially in dry environments. Assuming in-
wettestcyclones,andmaximizedinweakanddrycyclones. stead that the models are in fact correct, since they all
WhilethebiasofMERRA-2precipitatingtoofrequently show a similar bias, these results entail that IMERG
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 103
FIG.4.(left)Cyclone-centeredcompositesoftheprecipitationintensityfrommodels,(middleleft)correspondingaveragedIMERG,
(middleright)differencebetweenthetwo,and(right)differencerelativetoIMERGfor(a)–(d)MERRA-2,(e)–(h)ERA-Interim,(i)–(l)
GFDL devAM4, and (m)–(p) CAM6. The plus sign indicates the cyclone center; the mean includes both Northern and Southern
Hemispherecyclones,thelatterhavingbeenflippedalongthenorth–southaxistomatchtheirNorthernHemispherecounterparts.
mightoverestimateprecipitationintensityinregions threshold for precipitation rate. The CloudSat pre-
where it is heavy, and underestimate frequency of cipitation detection product has been found to be
precipitation in cold and dry environments. So next quiteeffectiveatdetectinglightprecipitationandisoften
wediscussthepossibilityofsuchbiasesinIMERG. used as a reference for other instruments and products
(e.g.,Behrangietal.2014;Stephensetal.2010).InNaud
b. PotentialissueswithIMERG
etal.(2018)wefoundnoevidenceoflightraindetection
issues when we compared IMERG to CloudSat pre-
1) FREQUENCYOFPRECIPITATION:IMERG
cipitationproductsinextratropicalcyclones.Therefore,
DETECTIONSKILLS
whilewecannoteliminatethepossibilitythatlightpre-
The bulk of the measurements that are fed in the cipitationisnotalwaysreportedintheIMERGproduct,
IMERG processing suite are from microwave radi- wealsocannoteliminatethepossibilitythatallmodels
ometers, which have issues with light rain detection tendtoproducelightprecipitationtoooften.
(e.g.,Stephensetal.2010).However,weensuredthat Another potential issue is with frozen precipita-
the models and IMERG all use the same minimum tion.Forexample,precipitationratesarenotretrieved
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

104 JOURNAL OF CLIMATE VOLUME33
FIG.5.Cyclone-centeredcompositesofIMERGprecipitationintensityasafunctionof(lefttoright)increasingcycloneascentstrength
and(bottomtotop)increasingcyclone-widemeanPW.Thenumberaboveeachpanelisthetotalnumberofcyclonespercategory.
for the CloudSat product if the algorithm finds a bulk As illustrated in Naud and Kahn (2015) for the
fractionofliquidinprecipitationlessthan85%.Inthe NorthernHemisphere(seetheirFig.5),drycyclones
case of IMERG the algorithm is designed to retrieve arepreferentiallysituatedonthepolewardsideofthe
precipitation rates regardless of the liquid fraction. But latitudebandexploredhere,wheretemperaturesare
inNaudetal.(2018),wehadfoundthatindrycyclones lowerandthemeltinglevelmuchclosertothesurface.
IMERGtotalprecipitationwaslessthanreportedwith Therefore we performed two separate tests: 1) using
CloudSat. However, to our knowledge, there has been MERRA-2liquid-onlyprecipitation(totalprecipitation
noindependentevaluationoveroceansofIMERG’sability rateminussnowfall),wetestthedifferenceinfrequency
andsuccessrateatdetectingfrozenprecipitation. of precipitation between MERRA-2 and IMERG in
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 105
FIG.6.Cyclone-centeredcompositesoftheIMERGfrequencyofprecipitationasafunctionof(lefttoright)increasingcycloneascent
strengthand(bottomtotop)increasingcyclone-widemeanPW.Thenumberaboveeachpanelisthetotalnumberofcyclonesper
category.
cycloneswithPW,11mm(Figs.9a–c);and2)using reducesthedifferencefromlargerthan0.5toanegative
IMERG’s report of the probability of liquid pre- bias of within 0.3 in a region where the probability of
cipitation,webuildcompositesalsoforcycloneswith liquidprecipitationismuchlessthan0.5accordingtothe
PW,11mm(Figs.9d–f).Bycontrastingthesetwose- IMERGflag.Therefore,itisquitepossiblethatIMERG
riesofcompositesandthelastrowofFig.8,weobserve doesnotdetectallofthefrozenprecipitation.However,
thefollowing:onthepolarsideofthecoldsectorwhere itisalsopossiblethatMERRA-2producesfrozenpre-
MERRA-2–IMERGdifferencesarethelargest,removing cipitationtoooften.Infact,atleastforCAM6,thecor-
all frozen precipitation from MERRA-2 frequencies respondence between the area of maximum occurrence
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

106 JOURNAL OF CLIMATE VOLUME33
FIG.7.Cyclone-centeredcompositesofthedifferenceinprecipitationintensitybetweenMERRA-2andIMERGasafunctionof(left
toright)increasingcycloneascentstrengthand(bottomtotop)increasingcyclone-widemeanPW.Thenumberaboveeachpanelisthe
totalnumberofcyclonespercategoryforMERRA-2.
offrozenprecipitationandtheareaofmaximumdiffer- etal.2018).Ourresultswouldsuggestthatthisissuemight
ence in frequency of occurrence of precipitation is less beexacerbatedinregionsoffrozenprecipitation.
clear(Fig.10).Moreover,ontheequatorwardhalfofthe
2) THEPRECIPITATIONINTENSITYDIFFERENCES:
dry cyclones, the difference in frequency of occurrence
CANIMERGOVERESTIMATERATES?
between models and IMERG cannot be explained by
either issues with IMERG or models for frozen pre- It is quite possible that models underestimate inten-
cipitation.Thisbringsbacktheissuealreadydiscussedin sity in regions of light precipitation, an issue reported
the literature that models tend to overestimate the oc- elsewhere and in tune with the differences found in
currenceoflightprecipitation(e.g.,Sunetal.2006;Terai frequency for areas where precipitation is light and
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 107
FIG.8.Cyclone-centeredcompositesofthedifferenceinfrequencyofprecipitationbetweenMERRA-2andIMERGasafunctionof
(lefttoright)increasingcycloneascentstrengthand(bottomtotop)increasingcyclone-widemeanPW.Thenumberaboveeachpanelis
thetotalnumberofcyclonespercategoryforMERRA-2.
intermittent. In contrast, in the comma region of the However, these biases were found in the tropics and
cyclones where precipitation rates are known to be mightnotholdtrue forcooleranddriermidlatitudere-
large,weneedtoenvisagethepossibilitythatIMERG gions. Also, while this observational uncertainty might
couldoverestimateprecipitationintensity.Itispossible explainthemodels’lowerratesintheregionofascent,it
if IMERG shares similar issues as the TRMM TMI doesnotexplaintheirpredictionofgreaterfrequency.
products:Hendersonetal.(2017)reportedatendency
c. ImplicationsfortestingsensitivitiesinGCMs
for precipitation rates to be overestimated in regions
of heavy stratiform precipitation, which would be the As mentioned earlier, climate models are developed
dominantprecipitationtypeincycloneascendingregions. with the aim of reproducing a realistic sensitivity of
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

108 JOURNAL OF CLIMATE VOLUME33
FIG. 9. Cyclone-centered composites of (a)–(c) the difference in frequency of precipitation between MERRA-2 liquid-only pre-
cipitationandIMERGand(d)–(f)theprobabilityofliquidprecipitationinIMERGasafunctionof(lefttoright)cycloneascentstrength
forcyclone-widemeanPW,11mm.
various parameters to environmental changes, among reanalyses (see similar tests for ERA-Interim in the
them precipitation. Therefore, we would like to test supplementalmaterial).
whether, despite possible deficiencies in the cyclone Figure 11 shows the two changes mentioned above:
precipitation characteristics, the models can still re- change in frequency of precipitation as a function of a
produce realistically how these characteristics change change in ascent strength and change in precipitation
with changing environmental conditions. Here we re- intensityasafunctionofachangeinenvironmentalPW,
strict ouranalysisto changesin cycloneenvironmental for IMERG at the three temporal averaging scales
PWandcyclonestrength.Inviewofthepotentialshort- that match the models and the three models. Note
comings in the IMERG observations discussed in the thatusingasubsetofcyclonestoremoveuncertainties
previoussection,wedonothavecompleteconfidencein caused by dry cyclones (for frequency tests) or strong
the changes in precipitation intensity with changes in cyclones(forintensity)doesnotchangeourresults(see
cyclone strength as reported with IMERG or in the FigS10intheonlinesupplementalmaterial)soherewe
changes in frequency of precipitation when cyclone usetheentirecyclonedatabase.
PWchanges.However,wecanmoreconfidentlyexam- Startingwiththechangeinfrequencyforachangein
ine changes in the frequency of precipitation between ascentstrength,IMERGreportsasignificantincrease
strong and weakcyclones as wellasthechange inpre- infrequencyofprecipitationinthecommaregion,but
cipitationintensitybetweenhighandlowPWcyclones. small or negative changes elsewhere, consistently re-
We therefore test these two changes for CAM6 and gardless of time-averaging convention (Figs. 11a–c).
devAM4,andaddMERRA-2totestwhetherthediffer- However, the difference is largest for instantaneous
enceswefindarespecifictoclimatemodelsoralsofoundin reporting (Fig. 11b) than 1- or 6-h time averaging
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 109
FIG.10.Cyclone-centeredcompositesofthedifferenceinfrequencyofprecipitationbetweenCAM6andIMERGasafunctionof(left
toright)increasingcycloneascentstrengthand(bottomtotop)increasingcyclone-widemeanPW.Thenumberaboveeachpanelisthe
totalnumberofcyclonespercategoryforCAM6.
(Figs.11a,c).Thisislikelybecausetheremightbeadis- ascending regions where precipitation occurs most of-
placement of the region of intense precipitation as cy- ten. For MERRA-2 the change in frequency of occur-
clonestravelduringthehouror6hofthetimeaveraging rence with achange in ascent strength ismuch smaller
(which is performed prior to projecting in the storm than reported with IMERG (3 times less; Fig. 11d vs
centered grid and applying the minimum precipitation Fig.11a)andthesameisfoundfordevAM4(Fig.11fvs
threshold). In this case, the frequency of precipitation Fig.11c).BothMERRA-2anddevAM4alsoindicatea
can include both ascending and descending regions relatively larger decrease in frequency in advance and
of the cyclone, which could potentially reduce the in the wake of the cold fronts (tail of the comma).
largenumberofprecipitationoccurrencethatoccursin Incontrast,ofthetwoGCMs,CAM6predictsachange
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

110 JOURNAL OF CLIMATE VOLUME33
FIG. 11. Cyclone-centered composite differences in (a)–(f) frequency of precipitation between strong- and weak-ascent-strength
cyclones for (a) IMERG 1-h, (b) IMERG instantaneous, (c) IMERG 6-h, (d) MERRA2, (e) CAM6, and (f) devAM4; and (g)–(l)
precipitationintensitybetweenhigh-andlow-PWcyclonesfor(g)IMERG1-h,(h)IMERGinstantaneous,(i)IMERG6-h,(j)MERRA2,
(k)CAM6,and(l)devAM4.
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 111
in frequency of occurrence much closer to IMERG midlatitude oceans. While all models agree quite well
(Fig. 11e vs Fig. 11b), albeit still not as strong in the withobservationsfortotalprecipitationinextratropical
areaattheheadofthecomma,whilepredictingmostly cyclones, there are systematic differences: all models
increasing frequencies elsewhere instead of a decrease slightlyunderestimateprecipitationintheascentregion
awayfromthecoldfront.EvenifIMERGisnotexact, of cyclones and overestimate precipitation in the sub-
while the impact of time averaging cannot be ignored, sidencearea.Whenwedecomposetheprecipitationinto
the quite differing magnitude and spatial distribution frequency of occurrence and precipitation rate when
oftheresponsetocyclonestrengthamongMERRA-2, precipitating,wefindthatallfourmodelsoverestimate
devAM4, and CAM6 casts doubts on the reliability of frequency(by10%inascendingbutinexcessof100%
futurepredictionofprecipitationchangeinextratropical indescendingregions)andunderestimateintensity(by
cyclones. 50%inascendingregionsandupto70%polewardofthe
While the change in precipitation intensity with a cyclone centers) when compared to IMERG. The sign
changeinPWismuch moreconsistentacross observa- of the differences is independent of cyclone strength
tionsandmodelsintermsofspatialdistribution(i.e.,the orenvironmentalmoistureamounts,butthemagnitude
change affects principally the region at the head of changes: stronger cyclones show larger differences in
thecomma),againthemagnitudesdiffer:MERRA-2 precipitationintensityintheregionofascent,whiledrier
(Fig.11f)andCAM6(Fig.11g)bothpredictasmaller cyclones show much larger differences in frequency of
change in intensity (about half) than that reported precipitation. We hypothesize that some of these dif-
withIMERG(Fig.11e),butdevAM4(Fig.11h)predictsa ferences might be caused by some limitations of the
muchstrongerchangethanthatreportedwithIMERG. IMERGproduct:theproductmightnotfullyreportvery
In contrast to changes in frequency, the change in in- lightand/orfrozenprecipitation.Itisalsopossiblethat
tensity seems less dependent on changes in time aver- theobservedintensityinstrongascentregionsmightbe
aging as instantaneous or 6-h mean IMERG are fairly overestimated(seesection4bforanexpandeddiscussion
similar(Fig.11hvsFig.11i).Presumablythisisbecause onpotentialbiasesinIMERG).
themeanprecipitationintensityiscalculatedonlywhere Nevertheless,ourresultsareconsistentwithprevious
precipitation actually occurs, suggesting that any cy- workbySunetal.(2006)orTeraietal.(2018)regarding
clone displacement during the hour or the 6-h period the overestimation of occurrence of light precipitation
only reduces the number of precipitation occurrences, and the underestimation of heavy precipitation rates
without affecting the mean intensity. Regardless of inascendingconditions.Moreover,regardlessofmodel
IMERG’s accuracy, the intermodel spread in re- or observations accuracy, there are significant disagree-
sponse of precipitation intensity to a change in cy- ments on the potential changes in precipitation charac-
clonePWagainaffectsthereliabilityoftheresponse teristicswhencontrastingenvironmentalconditions.This
ofprecipitationratestofutureincreaseinPWincurrent implies that, with the observations and models presently
models.Thissaid, theresponse of precipitationinfuture at our disposal, there is the potential for biases in the
climate simulations does not follow the same Clausius– projections of changes in precipitation in extratropical
ClapeyronrelationshipthatisobservedbetweenPWand cyclonesandpossiblyotherextremeprecipitationevents
seasurfacetemperaturechanges(e.g.,AllenandIngram that affect the midlatitudes in climate change experi-
2002; HeldandSoden 2006). This entails that PW is not ments. More specifically for the two reanalyses, the
necessarilyanidealmeasuretocharacterizeenvironmen- differenceswithIMERGthatarefoundherecouldserve
tal changes that can affect precipitation. However, Field as a reminder that precipitation is modeled in these
and Wood (2007) found that within cyclones PW and datasetsandthereforecautionshouldbeexercisedwhen
precipitationdorespondsimilarlytochangesinseasurface using these products for climatological studies or com-
temperatureandarguethatthelossofsimilarityatregional parisonswithothermodels.
orglobalscalecomesfromconcurrentchangesinthecy- While model developers might find these cyclone-
clonenumberorstrength.Sowhiletheintermodelspread centereddiagnosticsusefultotestnewversionsoftheir
fortheresponsetocyclonePWisproblematic,thespread modelsduringthedevelopmentprocess,oneadditional
inresponsetocyclonestrengthmightbeevenmoreso. testthatwouldbeinvaluableistoprovidesimilarinfor-
mationseparatelyforconvectiveandstratiformprecipi-
tation. This entails having at our disposal the means to
5. Conclusions
separate convective from stratiform precipitation in the
UsingIMERGobservationsasareference,wecom- observations.Therefore,onenextstepwillbetoassess
pare two reanalyses and two free-running GCMs thevariousdatasetsthatprovidesuchadelineation(e.g.,
cyclone-centered precipitation characteristics over the GPM,CloudSat)toprovideanadditionalconstraintfor
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

112 JOURNAL OF CLIMATE VOLUME33
modelevaluation,aswellashelpexploretheevolution ——, ——, and ——, 2011: Northern Hemisphere extratropical
ofcycloneprecipitationinachangingclimate. cyclonesinawarmingclimateintheHiGEMhigh-resolution
climate model. J. Climate, 24, 5336–5352, https://doi.org/
10.1175/2011JCLI4181.1.
Acknowledgments. The work is funded by NASA
Dee, D. P., and Coauthors, 2011: The ERA-Interim reanalysis:
PMM Grant NNX16AD82G and NOAA MAPP Configurationandperformanceofthedataassimilationsys-
GrantNA15OAR4310094.C.M.Naudisalsopartly tems.Quart.J.Roy.Meteor.Soc.,137,553–597,https://doi.org/
fundedbyNASAMAPGrant80NSSC17K0195.Work 10.1002/qj.828.
Eckhardt, S., A. Stohl, H. Wernli, P. James, C. Forster, and
byA.GettelmanattheNationalCenterforAtmospheric
N.Spichtinger,2004:A15-yearclimatologyofwarmcon-
Research is supported by the U.S. National Science
veyor belts. J. Climate, 17, 218–237, https://doi.org/10.1175/
FoundationCooperative Agreement 1852977. TheGPM 1520-0442(2004)017,0218:AYCOWC.2.0.CO;2.
IMERG products were obtained from the NASA God- Field,P.R.,andR.Wood,2007:Precipitationandcloudstruc-
dardSpaceFlightCenterPrecipitationProcessingSystem tureinmidlatitudecyclones.J.Climate,20,233–254,https://
data server. The database of cyclones with coincident doi.org/10.1175/JCLI3998.1.
——, A. Gettelman, R. Neale, R. Wood, P. J. Rasch, and
IMERG data is available at https://data.giss.nasa.gov/
H. Morrison, 2008: Midlatitude cyclone compositing to
storms/obs-etc/andhostedbytheNCCS.TheMERRA-2
constrainclimatemodelbehaviorusingsatelliteobserva-
files are available through the NASA Goddard Earth tions. J. Climate, 21, 5887–5903, https://doi.org/10.1175/
Sciences Data and Information Services Center. The 2008JCLI2235.1.
ERA-InterimfilesareobtainedfromtheEuropeanCentre ——, A. Bodas-Salcedo, and M. E. Brooks, 2011: Using model
analysisandsatellitedatatoassesscloudandprecipitationin
forMedium-RangeWeatherForecastsdataserver.The
midlatitudecyclones.Quart.J.Roy.Meteor.Soc.,137,1501–
devAM4 output were produced as part of the Model
1515,https://doi.org/10.1002/qj.858.
Diagnostics Task Force funded by the NOAA MAPP Gelaro, R., and Coauthors, 2017: The Modern-Era Retro-
program.TheCAM6outputwereproducedwithfund- spectiveAnalysisforResearchandApplications,version2
ingfromtheDept.ofEnergyOfficeofScienceGrant (MERRA-2). J. Climate, 30, 5419–5454, https://doi.org/
10.1175/JCLI-D-16-0758.1.
DE-SC0016344. The authors are grateful to the editor
Gettelman, A., P. Callaghan, V. E. Larson, C. M. Zarzycki,
andtwoanonymousreviewerswhosecommentshelped
J.T.Bacmeister,P.H.Lauritzen,P.A.Bogenschitz,and
significantlyimprovethequalityofthismanuscript. R.N.Neale,2018:Regionalclimatesimulationswiththe
CommunityEarthSystemModel.J.Adv.Model.EarthSyst.,
10,1245–1265,https://doi.org/10.1002/2017MS001227.
REFERENCES
Govekar,P.D.,C.Jakob,M.J.Reeder,andJ.Haynes,2011:The
Allen,M.R.,andW.J.Ingram,2002:Constraintsonfuturechanges three-dimensional distribution of clouds around Southern
inclimateand the hydrological cycle. Nature, 419,228–232, Hemispherecyclones.Geophys.Res.Lett.,38,L21805,https://
https://doi.org/10.1038/NATURE01092. doi.org/10.1029/2011GL049091.
Bauer,M.,andA.D.DelGenio,2006:Compositeanalysisofwinter Grecu, M., W. S. Olson, S. J. Munchak, S. Ringerud, L. Liao,
cyclones in a GCM: influence on climatological humidity. Z. Haddad, B. L. Kelley, and S. F. McLaughlin, 2016: The
J.Climate,19,1652–1672,https://doi.org/10.1175/JCLI3690.1. GPMcombinedalgorithm.J.Atmos.OceanicTechnol.,33,
——,G.Tselioudis,andW.B.Rossow,2016:Anewclimatology 2225–2245,https://doi.org/10.1175/JTECH-D-16-0019.1.
forinvestigatingstorminfluencesinandontheextratropics. Hawcroft,M.K.,L.C.Shaffrey,K.I.Hodges,andH.F.Dacre,
J. Appl. Meteor. Climatol., 55, 1287–1303, https://doi.org/ 2012:HowmuchNorthernHemisphereprecipitationisasso-
10.1175/JAMC-D-15-0245.1. ciated with extratropical cyclones? Geophys. Res. Lett., 39,
Behrangi,A.,G.Stephens,R.F.Adler,G.J.Huffman,B.Lambrigtsen, L24809,https://doi.org/10.1029/2012GL053866.
andM.Lebsock,2014:Anupdateontheoceanicprecipitation ——,——,——,and——,2016:Canclimatemodelsrepresent
rateanditszonaldistributioninlightofadvancedobservations the precipitation associated with extratropical cyclones? Cli-
fromspace.J.Climate,27,3957–3965,https://doi.org/10.1175/ mate Dyn., 47, 679–695, https://doi.org/10.1007/s00382-015-
JCLI-D-13-00679.1. 2863-z.
Bengtsson,L.,K.I.Hodges,andN.Keenlyside,2009:Willextra- ——,H.Dacre,R.Forbes,K.Hodges,L.Shaffrey,andT.Stein,
tropicalstormsintensifyinawarmerclimate?J.Climate,22, 2017:Usingsatelliteandreanalysisdatatoevaluatetherep-
2276–2301,https://doi.org/10.1175/2008JCLI2678.1. resentation of latent heating in extratropical cyclones in a
Booth,J.F.,C.M.Naud,andJ.Willison,2018a:Evaluationof climate model. Climate Dyn., 48, 2255–2278, https://doi.org/
extratropical cyclone precipitation in the North Atlantic 10.1007/s00382-016-3204-6.
basin:AnanalysisofERA-Interim,WRF,andtwoCMIP5 Haynes, J. M., T. S. L’Ecuyer, G. L. Stephens, S. D. Miller,
models.J.Climate,31,2345–2360,https://doi.org/10.1175/ C.Mitrescu,N.B.Wood,andS.Tanelli,2009:Rainfallretrieval
JCLI-D-17-0308.1. overtheoceanwithspaceborneW-bandradar.J.Geophys.Res.,
——,——,andJ.Jeyaratnam,2018b:Extratropicalcyclonepre- 114,D00A22,https://doi.org/10.1029/2008JD009973.
cipitationlifecycles:Asatellite-basedanalysis.Geophys.Res. Held, I., and B. J. Soden, 2006: Robust responses of the hy-
Lett.,45,8647–8654,https://doi.org/10.1029/2018GL078977. drologicalcycletoglobalwarming.J.Climate,19,5686–5699,
Catto,J.L.,L.C.Shaffrey,andK.I.Hodges,2010:Canclimatemodels https://doi.org/10.1175/JCLI3990.1.
capturethestructureofextratropicalcyclones?J.Climate,23, Henderson,D.S.,C.D.Kummerow,D.A.Marks,andW.Berg,2017:
1621–1635,https://doi.org/10.1175/2009JCLI3318.1. A regime-based evaluationof TRMMoceanic precipitation
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC

1JANUARY2020 NAUD ET AL. 113
biases.J.Atmos.OceanicTechnol.,34,2613–2635,https://doi.org/ data.Mon.Wea.Rev.,139,1419–1446,https://doi.org/10.1175/
10.1175/JTECH-D-16-0244.1. 2010MWR3294.1.
Hou, A. Y., and Coauthors, 2014: The Global Precipitation Skofronick-Jackson, G., and Coauthors, 2017: The Global
Measurementmission.Bull.Amer.Meteor.Soc.,95,701– PrecipitationMeasurement(GPM)missionforscienceand
722,https://doi.org/10.1175/BAMS-D-13-00164.1. society.Bull.Amer.Meteor.Soc.,98,1679–1695,https://doi.org/
Huffman, G. J., R. F. Adler, M. Morrissey, D. T. Bolvin, 10.1175/BAMS-D-15-00306.1.
S.Curtis,R.Joyce,B.McGavock,andJ.Susskind,2001: Stephens,G.L.,andCoauthors,2002:TheCloudSatmissionand
Globalprecipitationatone-degreedailyresolutionfrommulti- theA-Train:Anewdimensiontospace-basedobservationsof
satelliteobservations.J.Hydrometeor.,2,36–50,https://doi.org/ cloudsandprecipitation.Bull.Amer.Meteor.Soc.,83,1771–
10.1175/1525-7541(2001)002,0036:GPAODD.2.0.CO;2. 1790,https://doi.org/10.1175/BAMS-83-12-1771.
——,andCoauthors,2017:NASAGlobalPrecipitationMeasure- ——,andCoauthors,2010:Drearystateofprecipitationinglobal
ment (GPM) Integrated Multi-satellite Retrievals for GPM models.J.Geophys.Res.,115,D24211,https://doi.org/10.1029/
(IMERG),AlgorithmTheoreticalBasisDocument(ATBD) 2010JD014532.
version 4.6, 28 pp., https://pmm.nasa.gov/sites/default/files/ Sun,Y.,S.Solomon,A.Dai,andR.W.Portmann,2006:Howoften
document_files/IMERG_ATBD_V4.6.pdf. doesitrain?J.Climate,19,916–934,https://doi.org/10.1175/
Lau,N.-C.,andM.W.Crane,1995:Asatelliteviewofthesynoptic- JCLI3672.1.
scaleorganization of cloud properties in midlatitude and Tan, J., W. A. Petersen, P.-E. Kirstetter, and Y. Tian, 2017:
tropicalcirculationsystems.Mon.Wea.Rev.,123,1984–2006, Performance of IMERG as a function of spatiotemporal
https://doi.org/10.1175/1520-0493(1995)123,1984:ASVOTS. scale. J. Hydrometeor., 18, 307–319, https://doi.org/10.1175/
2.0.CO;2. JHM-D-16-0174.1.
Naud,C.M.,andB.H.Kahn,2015:Thermodynamicphaseandice Tapiador,F.J.,R.Roca,A.DelGenio,B.Dewitte,W.Petersen,
cloudpropertiesinNorthernHemispherewinterextratropical andF.Zhang,2019:Isprecipitationagoodmetricformodel
cyclonesobservedbyAquaAIRS.J.Appl.Meteor.Climatol., performance?Bull.Amer.Meteor.Soc.,100,223–233,https://
54,2283–2303,https://doi.org/10.1175/JAMC-D-15-0045.1. doi.org/10.1175/BAMS-D-17-0218.1.
——, D. J. Posselt, and S. C. van den Heever, 2012: Observa- Terai, C. R., P. M. Caldwell, S. A. Klein, Q. Tang, and M. L.
tional analysis of cloud and precipitation in midlatitude Branstetter, 2018: The atmospheric hydrologic cycle in the
cyclones: Northern versus Southern Hemisphere warm ACME v0.3 model. Climate Dyn., 50, 3251–3279, https://
fronts.J.Climate,25,5135–5151,https://doi.org/10.1175/JCLI- doi.org/10.1007/s00382-017-3803-x.
D-11-00569.1. Wong,S.,C.M.Naud,B.H.Kahn,L.Wu,andE.J.Fetzer,2018:
——,——,and——,2017:Observedcovariationsofaerosoloptical Couplingofprecipitationandcloudstructuresinoceanic
depthandcloudcoverinextratropicalcyclones.J.Geophys. extratropical cyclones to large-scale moisture flux conver-
Res.,122,10338–10356,https://doi.org/10.1002/2017JD027240. gence.J.Climate,31,9565–9584,https://doi.org/10.1175/JCLI-
——,J.F.Booth,M.Lebsock,andM.Grecu,2018:Observational D-18-0115.1.
constraint for precipitation in extratropical cyclones: Sensi- Yettella,V.,andJ.E.Kay,2017:Howwillprecipitationchange
tivitytodatasources.J.Appl.Meteor.Climatol.,57,991–1009, inextratropicalcyclonesastheplanetwarms?Insightsfroma
https://doi.org/10.1175/JAMC-D-17-0289.1. largeinitialconditionclimatemodelensemble.ClimateDyn.,
Pfahl,S.,andM.Sprenger,2016:Ontherelationshipbetweenex- 49,1765–1781,https://doi.org/10.1007/s00382-016-3410-2.
tratropicalcycloneprecipitationandintensity.Geophys.Res. Zhao,M.,andCoauthors,2018:TheGFDLglobalatmosphereand
Lett.,43,1752–1758,https://doi.org/10.1002/2016GL068018. land model AM4.0/LM4.0: 2. Model description, sensitivity
Rudeva, I., and S. K. Gulev, 2011: Composite analysis of North studiesandtuningstrategies.J.Adv.Model.EarthSyst.,10,
Atlantic extratropical cyclones in NCEP–NCAR reanalysis 735–769,https://doi.org/10.1002/2017MS001209.
Unauthenticated | Downloaded 03/09/26 02:43 PM UTC