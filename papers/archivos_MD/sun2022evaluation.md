atmosphere
Article
Evaluation of Technology for the Analysis and Forecasting
of Precipitation Using Cyclostationary EOF and
Regression Method
MingdongSun1,2 ,GwangseobKim2,KunLei1,*andYanWang1,*
1 ChineseResearchAcademyofEnvironmentalSciences,No.8Dayangfang,AnwaiBeiyuan,
ChaoyangDistrict,Beijing100012,China;mingdongsun@hotmail.com
2 DepartmentofCivilEngineering,KyungpookNationalUniversity,Daegu702701,Korea;
kimgwsb@hotmail.com
* Correspondence:leikun@craes.org.cn(K.L.);wang.yan@craes.org.cn(Y.W.)
Abstract: Precipitationtimeseriesexhibitcomplexfluctuationsandstatisticalchanges. Existing
researchstopsshortofasimpleandfeasiblemodelforprecipitationforecasting.Inthisarticle,the
authorsinvestigateandforecastprecipitationvariationsinSouthKoreafrom1973to2021using
cyclostationaryempiricalorthogonalfunction(CSEOF)andregressionmethods. First,empirical
orthogonalfunction(EOF)andCSEOFanalysesareusedtoexaminetheperiodicchangesinthe
precipitationdata.Then,theautoregressiveintegratedmovingaverage(ARIMA)methodisapplied
totheprincipalcomponent(PC)timeseriesderivedfromtheEOFandCSEOFprecipitationanalyses.
ThefifteenleadingEOFandCSEOFmodesandtheircorrespondingPCtimeseriesclearlyreflectthe
spatialdistributionandtemporalevolutioncharacteristicsoftheprecipitationdata.BasedonthePC
(cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7) forecastsoftheEOFandCSEOFmodels,theEOF–ARIMAcompositemodelandCSEOF–ARIMA
compositemodelareusedtoobtainquantitativeprecipitationforecasts. Thecomparisonresults
Citation:Sun,M.;Kim,G.;Lei,K.;
show that both composite models have good performance and similar accuracy. However, the
Wang,Y.EvaluationofTechnology
performance of the CSEOF–ARIMA model is better than that of the EOF–ARIMA model under
fortheAnalysisandForecastingof
PrecipitationUsingCyclostationary variousmeasurements.Therefore,theCSEOF–ARIMAcompositeforecastmodelcanbeconsidered
EOFandRegressionMethod. anefficientandfeasibletechnologyrepresentingananalyticalapproachforprecipitationforecasting
Atmosphere2022,13,500. https:// inSouthKorea.
doi.org/10.3390/atmos13030500
Keywords:precipitationforecasting;EmpiricalOrthogonalFunction(EOF);CyclostationaryEmpirical
AcademicEditors:MdAbul
OrthogonalFunction(CSEOF);seasonalcycle;autoregressiveintegratedmovingaverage(ARIMA);
EhsanBhuiyan,DiegoCerraiand
climatechange
NishanKumarBiswas
Received:15January2022
Accepted:19March2022
Published:21March2022 1. Introduction
Publisher’sNote:MDPIstaysneutral Globalclimateandenvironmentalchangeshavebecomemajorworldwideissuesin
withregardtojurisdictionalclaimsin recentyears.Inparticular,interactionsbetweentheatmosphereandslowlychangingoceans
publishedmapsandinstitutionalaffil- will have profound and long-term effects on humans. Because agricultural production
iations. andhydrologicalmanagementareheavilyinfluencedbytheclimate,meteorologistsare
interestedintheeffectsofclimateandenvironmentalchanges,suchasvariationsinperiodic
meteorologicalphenomena[1].
Precipitationisanimportantvariableinclimatechangeresearchandsignificantin
Copyright: © 2022 by the authors.
hydrologicalprocesses[2,3]. Itisthemaincomponentofthewatercycleandhasagreat
Licensee MDPI, Basel, Switzerland.
influenceonsurroundingenvironmentsandhydrologicalsystems. Changesinthetiming
This article is an open access article
andamountofprecipitationinagivenareacanleadtoseriousfloodhazardsoragricultural
distributed under the terms and
failuresduetofloodsanddroughts. Becausehuman-inducedclimatechangeaccelerates
conditionsoftheCreativeCommons
thehydrologicalcycleoftheecosystem,forecastingprecipitationonthedecadalscaleisbe-
Attribution(CCBY)license(https://
creativecommons.org/licenses/by/ comingincreasinglyimportantforlong-termwaterresourcemanagement[4,5]. Advanced
4.0/). precipitationforecastingtechnologiesandtimelyprecipitationdiagnosescanhelpimprove
Atmosphere2022,13,500.https://doi.org/10.3390/atmos13030500 https://www.mdpi.com/journal/atmosphere

Atmosphere2022,13,500 2of17
theoperationofwaterstoragefacilitiesandpreventpotentialflooddisasters. Thelatest
IntergovernmentalPanelonClimateChangereportindicatedthatthereisgrowingconcern
inthescientificcommunityregardingthesignificantincreasesobservedintheamountand
intensityofprecipitationandregardingthecorrespondingvariations[6].
Muchresearchhasbeenconductedregardingforecastingprecipitation,withmany
studies highlighting that the trends observed in the annual and monthly precipitation
ofdifferentregionsdependontheregionofinterestandthetimeperiodexamined[7–9].
Severalstudieshavefocusedonseasonalpredictionsofprecipitationattheregionallevel
using different technologies, such as regional climate models [10], in conjunction with
other climate variables [11,12]. Some studies have improved the approaches used to
forecastclimateindexvalues,suchasprojectionswithteleconnectionindices[13]andthe
developmentofotherensembleforecastingmodels[14,15]. Inaddition,manystudieshave
closelyinvestigatedthevarioustrendsandspatiotemporalcharacteristicsofprecipitation
inSouthKorea[16–19].
Precipitationismeasuredbyvariousobservationsystemsonthegroundandinspace.
Therefore,understandingthenatureofmeasurementdataisthebasisforunderstanding
uncertaintyandreliability[20]. Weatherradarprovidesthespatialdistributionofprecipi-
tationestimation,butduetovariousnaturalfactors,itwillalsobelimitedinestimating
accurate precipitation [21]. The rain gauge data is considered to be real ground data
becauseofitshighquality,resolutionandavailability[22]. Fromthispointofview,the
researchofraingaugedataandprecipitationdatasethasmanyadvantages,soithasa
wideapplicationprospect.
Ingeneral,traditionalstatisticalmethodsaretypicallyusedforlong-rangeforecasting,
withtheincorporationofdynamicalmethodscontributingimprovements. Somesuccessful
approacheshaveinvolvedperformingclimateforecastingusingmultipleregressionand
correlation analysis methods. The Dynamical Climate Models have been used in SST
Forecastsfrom1997to1998withpreciselyenoughverification[23]. Seasonalpredictionof
coastaloceanconditionsintheAtlantichavebeenevaluatedbyahigherskillLinearInverse
Model(LIM)[24]. TheevolutionanddynamicpredictabilityofMadden–Julianoscillation
(MJO)havebeenexploitedandestimatedinachievingthelikelyforecastpotentialintheir
ownresearch[25,26].
Manyclimaticvariables,suchasprecipitation,surfacetemperature,andsolarflux,
areknowntoexhibitperiodic(annual,monthly,daily,etc.) variationsintheirstatistical
features. Analyses of such datasets performed using stationary approaches often yield
meaninglessstatisticalcharacteristics,representingtheweakerrorcorrectionperformance
ofthesemethodsandtheirinaccuracyinobtaininglong-termpredictions. Therefore,itis
bothappropriateandadvantageoustoadoptacyclostationarymethodologyforstatistical
analysesofclimaticphenomenathatdisplaystrongcyclicaltrends.
Precipitationhastypicalcyclicalvariationswithstatisticalfluctuationsandseasonal
tendencies. Particularlywhenaprecipitationdatasetcoversseveralweatherstationsor
spansdifferentseasons,stationarymethodscanbeusedtoobtainonlythemostobvious
statisticaltrends. Inclimatestudies,empiricalorthogonalfunction(EOF)analysesareoften
usedtostudypossiblespatialpatternsofvariabilityandhowthesepatternschangewith
time. SomestudieshaveusedEOFmodelstoanalyzeprecipitationdata. Cahalananalyzed
monthlyprecipitationdataovertheUSandCanadabasedonEOFsandtheirvariances[27].
SinghcomparedmajorrainfallpatternsusingthemainmodesofOLRdata[28]. Svensson
showedthatmostofthevarianceobservedinrainfallinfourperiodscouldbeexplainedby
anelongatedspatialrainfallpattern[29]. Assuch,EOFanalysesaresometimesclassified
asmultivariatestatisticaltechniques. However,EOFanalysesarenotbasedonphysical
principles. Thus,toadequatelyanalyzeacomprehensivedataset,weuseacyclostationary
empirical orthogonal function (CSEOF) analysis technique; this approach is useful for
extractingevolvingspatialpatterns.
Theexistingscholarshipinthisfield,however,tendstousecomplexsystemmodel
ormoreinputdataandstaysshortofgeneralizingasimpleandeasy-to-usemethodfor

Atmosphere2022,13,500 3of17
precipitationforecasting.Thisstudyprimarilyfocusesontheanalysisofthemostdominant
componentoftheseasonalcycleofprecipitationinSouthKorea. Empiricalorthogonal
function (EOF) and CSEOF analyses are conducted to extract individual modes in the
observed precipitation data to obtain the temporal and spatial evolution of individual
synopticfields. WeuseEOFandCSEOFanalysesastheprimarytechniquestoanalyze
the temporal evolution of the variability in precipitation and demonstrate the physical
mechanism associated with each mode of precipitation variability. The autoregressive
integratedmovingaverage(ARIMA)modelisusedtoexamineandforecasttheevolution
of the temporal modes of precipitation variability derived from the EOF and CSEOF.
Precipitationforecastsaregeneratedfromtheregressedtemporalandspatialpatterns. The
present study provides a detailed explanation of the observed changes in precipitation
variablesandexploresafeasiblestatisticalmethodologyforforecastingprecipitationina
monsoonclimate.
ThedatausedinthisstudyaredescribedinSection2. TheEOFandCSEOFanalysis
methodsusedtoanalyzeprecipitationvariabilityandtheARIMAmodelarealsoexplained
inSection2.Thecyclicalseasonalcharacteristicsofprecipitationvariabilityarepresentedin
Section3. TheforecastingperformanceandrelatedmechanismsarediscussedinSection4.
ConclusionsarepresentedinSection5.
2. DataandMethodology
2.1. Data
Theprimarydatausedinthepresentstudywereprecipitationmeasurementstaken
overSouthKoreabytheKoreaMeteorologicalAdministration(KMA).Arealtimequality
controlsystemwasdevelopedformeteorologicaldatameasuredbyintegratedmeteorolog-
icalsensorsbasedonacomparisonofqualitycontrolproceduresdevelopedformeteorolog-
icaldatabytheWorldMeteorologicalOrganizationandtheKMA.The56weatherstations
fromwhichthedataanalyzedinthisstudywerecollectedaregenerallywelldistributed
acrossthemainland,asshowninFigure1,whiledatafromJejudoandUlleungdoaswell
assomemissingdatawereexcludedfromtheanalysis. Thedatasetrepresentsthelongest
andmostconsistentprecipitationobservationsavailableinSouthKorea,spanning49years
(1973–2021). Inthisstudy,thedatafromthefirst44years(1973–2016)ofthetimeseriesare
usedtogeneratetheforecastingmodel,whilethelastfiveyears(2017–2021)ofprecipitation
recordsareusedtovalidatethemodel.
2.2. Methodology
ThestatisticaltechniquesusedinthisstudyareEOFsandCSEOFsfordecomposing
thedataandARIMAmodelsforforecasting.
2.2.1. EmpiricalOrthogonalFunction
Empiricalorthogonalfunctionanalyses[30]areamongthemostwidelyappliedtech-
niquesinoceanographyandatmosphericscienceresearch.Inthismethod,aspatiotemporal
datasetisdecomposedintoorthogonalbasisfunctionsdeterminedbythedata. Themethod
issimilartoprincipalcomponentanalysis;however,EOFscandetectbothtemporaland
spatialpatterns.
InEOFanalyses,spatiotemporaldataX(r,t)arerepresentedintermsofloadingvectors
(L)andtheirprincipalcomponent(PC)timeseries,asfollows:
∑
X(r,t) = PC (t)L (r) (1)
n n
n
whereL (r)representsaspecificspatialpatternandPC (t)representsthetemporalevolu-
n n
tionofL (r).
n

AAtmtmoospsphhereere2 2002222,,1 133,,5 x00 FOR PEER REVIEW 44 ooff 1177
FFiigguurree1 1..L Looccaattioionno off5 566p prreeccipipitiatatitoionns statatitoionnssi ninS SoouuththK Koorreeaa..
2.2. MTheitshoedqouloagtyio nsignifiesadecompositionofagivendatasetintoanumberofspatial
andteTmhep ostraatlisptaicttaelr tnesc.hTnhiqeusepsa utisaeldp iantt tehrinss saturedoyr athreo gEoOnFasl atondea CchSEoOthFesr faonrd daecreomorpdoesriendg
btyhem daagtnai atundde A;tRhIeMteAm mpoordaellpsa ftoter rfnosreocsacsitlliantge. overtime. Theloadingvectorsrepresentthe
independentpatternsofvariabilityinthedatasetandareofteninterpretedasaphysical
m2.o2d.1e.l Eomftphieriscyasl tOemrthforogmonwalh Ficuhncthtieond atawerederived[31].
Empirical orthogonal function analyses [30] are among the most widely applied tech-
2.2.2. CyclostationaryEmpiricalOrthogonalFunction
niques in oceanography and atmospheric science research. In this method, a spatiotem-
ACSEOFisthebasicfunctioninacyclostationaryprocessandisacyclostationary
poral dataset is decomposed into orthogonal basis functions determined by the data. The
analogofanEOFobtainedusingastationaryapproach[32]. TheCSEOFanalysismethod
method is similar to principal component analysis; however, EOFs can detect both tem-
isdescribedindetailbyKimandNorth[33]. InCSEOFanalyses,spatiotemporaldataare
poral and spatial patterns.
representedasfollows:
In EOF analyses, spatiotemporal data X(r,t) are represented in terms of loading vec-
d−1
tors (L) and their principal comXp(orn,te)n=t (P ∑ C) ctim(re, ts)eer2iπeiskt,/ ads follows: (2)
k
k=0
X(r,t)=PC (t)L (r)
wheredisthenestedperiodrepresentingtheinhernentpneriodicityinthedata. (1)
n
BycalculatingthecovariancefunctionandtheBlochfunction,thespace–timeCSEOFs
c w an he b r e e o L bnt ( a r) i n r e e d pr u e s s i e n n g ts t h a e sp fo e l c lo if w ic i n sp g a e ti q a u l a p t a io tt n e : rn and PCn(t) represents the temporal evolu-
tion of Ln(r).
∑
This equation signifies a Xde(rc,otm)p=ositiPoCn o(ft )aC gLiv(ern, td)ataset into a number of spat(i3a)l
n n
and temporal patterns. The spatial patternns are orthogonal to each other and are ordered
by magnitude; the temporal patterns oscillate over time. The loading vectors represent the
whereCL (r,t)isacyclostationaryloadingvector(CSLV)andPC (t)isthecorresponding
n n
independent patterns of variability in the dataset and are often interpreted as a physical
PCtimeseries.
model of the system from which the data were derived [31].
IncontrasttoEOFanalyses,theCSLVsaretime-dependent. Thetemporalevolutionof
aspatialpatternalsodependsonperiodicdatawithperiodd,calculatedasfollows:
2.2.2. Cyclostationary Empirical Orthogonal Function
A CSEOF is the basic functCioLnn (irn, ta) c=ycCloLsnt(art,iotn+ardy) process and is a cyclostationa(4r)y
analog of an EOF obtained using a stationary approach [32]. The CSEOF analysis method

Atmosphere2022,13,500 5of17
Thus,CSLVsareperiodic,time-dependenteigenfunctionsofthecovariancestatistics.
AnessentialcomponentinCSEOFanalysesisdeterminingthenestedperiod.Selecting
apropernestedperiodrequiresanadequateunderstandingofthephysicalandstatistical
characteristicsofthedatasetbeinganalyzed[34].
TheCSEOFtechniqueisconceptuallysimilartotheEOFtechniqueinthatbothextract
sequences of spatial patterns as eigenfunctions based on the spatiotemporal structure
of the covariance function. However, the major difference between EOF and CSEOF
is that in CSEOF analyses, each CSLV represents a set of spatial patterns. The critical
motivation for the temporal dependence of CSLVs is that the spatial patterns of many
knownphenomenainclimatescienceandgeophysicsevolveovertimewithrecognizable
periodswhileexhibitingslowfluctuationsoverlongertimescales. Acomparisonofstudies
thatusedEOFandCSEOFtechniquescanbefoundinKimandWu[35]. Recentstudies
havedemonstratedtheefficacyofCSEOFsinextractingrobustmodesrepresentingclimate
variabilities[36,37].
2.2.3. AutoregressiveIntegratedMovingAverage(ARIMA)
Anautoregressiveintegratedmovingaverage(ARIMA)wasintroducedbyBoxand
Jenkins [38]. It is a statistical analysis model that uses time series data to either better
understandthedatasetortoforecastfuturetendency. Thismodelisusuallyappliedto
estimaterelatedvaluesinatimeseries;itisautoregressiveifitpredictsfuturevaluesbased
onpastvalues
An ARIMA(p,d,q) model can be understood by outlining each of its components
asfollows. Autoregression(AR):referstoamodelthatshowsachangingvariablethat
regressesonitsownlagged,orprior,values. Integrated(I):representsthedifferencingof
rawobservationstoallowforthetimeseriestobecomestationary. Movingaverage(MA):
incorporatesthedependencybetweenanobservationandaresidualerrorfromamoving
averagemodelappliedtolaggedobservations. Thus,themodelcanbewrittenasfollows:
(cid:32) (cid:33) (cid:32) (cid:33)
p q
1− ∑ α Li (1−L)dX = 1+ ∑ β Lj ε (5)
i t j t
i=1 j=1
where X is the time series value, p is order of the autoregressive part, d degree of first
t
differencinginvolved,qisorderofthemovingaveragepart,αandβaretheparametersof
Atmosphere 2022, 13, x FOR PEER REVIEW 6 of 17
themodel,εiswhitenoiseandLisLagoperator.
The key difficulty in applying the ARIMA model is identifying the orders of the
model. NumerousavailabletestscanbeusedtodeterminetheordersofanARIMAmodel.
TTwwoo ccoommmmoonn pprrooppoosseedd mmeetthhooddss iinncclluuddee tthhee AAkkaaiikkee iinnffoorrmmaattiioonn ccrriitteerriioonn ((AAIICC)) aanndd tthhee
BBaayyeessiiaann iinnffoorrmmaattiioonn ccrriitteerriioonn ((BBIICC)) [[3399,,4400]]..
TThhee sscchheemmee ooff tthhee ffoorreeccaassttiinngg aapppprrooaacchheess iiss sshhoowwnn iinn FFiigguurree 22..
FFiigguurree 22.. SScchheemmee ooff tthhee aannaallyyssiiss aanndd ffoorreeccaassttiinngg..
3. ResultsandDiscussion
3. Results and Discussion
3.1. SeasonalCycleofPrecipitation
3.1. Seasonal Cycle of Precipitation
The spatial distribution of mean precipitation in South Korea from 1973 to 2021 is
The spatial distribution of mean precipitation in South Korea from 1973 to 2021 is
showninFigure3,wherethedistributionrepresentstheprecipitationinterpolationateach
shown in Figure 3, where the distribution represents the precipitation interpolation at
weatherstation. ThemeansofprecipitationinFigure3indicatetheprimaryvariabilitiesin
each weather station. The means of precipitation in Figure 3 indicate the primary varia-
bilities in precipitation. As expected, the mean is more in the north and south and less in
the middle because of seasonal fluctuations in precipitation in the summer.
Figure 3. Spatial distribution of mean monthly precipitation data totals from 1973–2021 in South
Korea.
The annual precipitation is approximately 11,250 mm (1973–2021 average), with
more than 60% of the annual rainfall occurring between June and August. Boxplots of the
monthly precipitation from 1973 to 2021 are plotted in Figure 4. The annual periodicity
involves obvious precipitation increases in the summer, with maximums occurring in July
and August corresponding to the summer monsoon in Asia; precipitation is lower at other
times of the year.

Atmosphere 2022, 13, x FOR PEER REVIEW 6 of 17
Two common proposed methods include the Akaike information criterion (AIC) and the
Bayesian information criterion (BIC) [39,40].
The scheme of the forecasting approaches is shown in Figure 2.
Figure 2. Scheme of the analysis and forecasting.
3. Results and Discussion
3.1. Seasonal Cycle of Precipitation
The spatial distribution of mean precipitation in South Korea from 1973 to 2021 is
Atmosphere2022,13,500 6of17
shown in Figure 3, where the distribution represents the precipitation interpolation at
each weather station. The means of precipitation in Figure 3 indicate the primary varia-
bilities in precipitation. As expected, the mean is more in the north and south and less in
precipitation. Asexpected,themeanismoreinthenorthandsouthandlessinthemiddle
the middle because of seasonal fluctuations in precipitation in the summer.
becauseofseasonalfluctuationsinprecipitationinthesummer.
FiguFrieg u3r.e Sp3.atiaSlp daitsitarlibduitsitornib ouft imoneaonf mmoenatnhlym pornetchilpyitaptrieocni pditaattai otontadlsa tfarotmot a1l9s73fr–o2m0211 9in7 3S–o2u0t2h1 in
KorSeoa.u thKorea.
Theannualprecipitationisapproximately11,250mm(1973–2021average),withmore
The annual precipitation is approximately 11,250 mm (1973–2021 average), with
than 60% of the annual rainfall occurring between June and August. Boxplots of the
more than 60% of the annual rainfall occurring between June and August. Boxplots of the
monthlyprecipitationfrom1973to2021areplottedinFigure4. Theannualperiodicity
monthly precipitation from 1973 to 2021 are plotted in Figure 4. The annual periodicity
Atmosphere 2022, 13, x FOR PEER REViInEvWo lvesobviousprecipitationincreasesinthesummer,withmaximumsoccurring7in oJfu 1l7y
involves obvious precipitation increases in the summer, with maximums occurring in July
andAugustcorrespondingtothesummermonsooninAsia;precipitationisloweratother
and August corresponding to the summer monsoon in Asia; precipitation is lower at other
timesoftheyear.
times of the year.
FFiigguurree 44.. BBooxxpplloottss ooff mmoonntthhlyly pprreecciippiittaattiioonn ddaattaa ttoottaallss ffrroomm 11997733 ttoo 22002211 iinn SSoouutthh KKoorreeaa.. TThhee uuppppeerr
aanndd lloowweerr bboouunnddaarriieess ooff eeaacchh bbooxx iinnddiiccaattee tthhee uuppppeerr aanndd lloowweerr qquuaarrttiilleess ooff tthhee ddiissttrriibbuuttiioonn;; tthhee
mmeeddiiaann vvaalluueess aarree sshhoowwnn bbyy tthheec crroossssa annddl ilnineew witihtihninth teheb obxo,xa,n adndth teheex etrxetmreemuep upperpdera tdaavtaa lvuaelsuaerse
are shown by dots above and below the box.
shownbydotsaboveandbelowthebox.
The precipitation data are decomposed into individual modes using EOF and CSEOF
analyses. The main motivation for using these techniques is to investigate the mechanisms
associated with changes in the variability of precipitation. A scree plot of the accumulated
percentages obtained in the EOF and CSEOF analyses is shown in Figure 5 to show how
they cumulatively rise. We present the two leading EOF and CSEOF modes to illustrate
the temporal and spatial variations in precipitation.
Figure 5. The scree plot of the accumulated percentage of EOF and CSEOF analysis, with 13 leading
modes from the EOF, 15 modes from the CSEOF can account for more than 95% of total variance.
Therefore, Figure 6 shows the first and second EOF modes, which explain 77.57% and
7.89% of the total variance, respectively. The PCs and loading patterns corresponding to
the two leading modes are described in Figure 6a,b by normalized homogeneous correla-
tion maps. The loading patterns in Figure 6c,d come from interpolation based on disper-
sion points.
The PC time series of the first and second modes of the EOF analysis (Figure 6a,b)
both represent special cycles with slight fluctuations over longer time scales than those

Atmosphere 2022, 13, x FOR PEER REVIEW 7 of 17
Figure 4. Boxplots of monthly precipitation data totals from 1973 to 2021 in South Korea. The upper
and lower boundaries of each box indicate the upper and lower quartiles of the distribution; the
Atmosphere2022,13,500 median values are shown by the cross and line within the box, and the extreme upper data va7loufe1s7
are shown by dots above and below the box.
The precipitation data are decomposed into individual modes using EOF and CSEOF
TheprecipitationdataaredecomposedintoindividualmodesusingEOFandCSEOF
aannaallyysseess.. TThhee mmaainin mmoottivivaattiioonn ffoorr uussiinngg tthheessee tetecchhnniqiquueess isis toto ininvveesstitgigaattee ththee mmeecchhaannisismmss
aassssoocciiaatteedd wwiitthh cchhaannggeess iinn tthhee vvaarriiaabbiilliittyy ooff pprreecciippiittaattiioonn.. AA ssccrreeee pplolott ooff tthhee aaccccuummuullaatteedd
ppeerrcceennttaaggeess oobbttaaiinneedd iinn tthhee EEOOFF aanndd CCSSEEOOFF aannaalylysseess isis sshhoowwnn inin FFigiguurree 55 ttoo sshhooww hhooww
tthheeyy ccuummuullaattiivveellyy rriissee.. WWee pprreesseennttt htheet wtwool elaedaidnigngE OEOFFan adndC SCESOEFOmF omdoedsetos itlolu isllturastteratthee
ttheem tpemorpaolraanld anspda stpiaaltviaalr viaatrioiantisoinnsp irne pcirpeictiaptiiotant.ion.
FFiigguurree 55. .TThhee ssccrreeee pplolot toof fththee aaccccuummuulalatetedd ppeerrcceennttaaggee ooff EEOOFF aanndd CCSSEEOOFF aannaalylyssiiss, ,wwiitthh 1133 leleaaddiinngg
mmooddeess ffrroomm tthhee EEOOFF,, 1155 mmooddeess ffrroomm tthhee CCSSEEOOFF ccaann aaccccoouunntt ffoorr mmoorree tthhaann 9955%% ooff ttoottaall vvaarriiaannccee..
TThheerreeffoorree, ,FFigiguurere 6 6shsohwows tshteh feirsfitr asntdan sdecsoencdo nEdOFE OmFodmeso,d wesh,icwhh eixcphlaeixnp 7la7i.5n77%7 .a5n7d%
7a.8n9d%7 .o8f9 %theo tfotthael vtoatraialnvcaer,i arnescpe,ecretisvpeelyct. iTvehley .PTChs eaPndC sloaanddinlgo apdaitntegrpnas tctoerrnresscpoornrdesinpgo ntod -
tihneg twtoot hleeatdwinogl emaoddinegs amreo ddeesscarriebedde sincr Fibigeudrien 6Fai,bg ubrye n6oar,bmbaylizneodr mhoamlizoegdenheoomuso gcoenrreeolau-s
tcioonrr melaatpios.n Tmhea plosa.dTihneg lpoaatdteinrngsp iant tFeirgnusrien 6Fci,dgu croem6ec ,fdrocmom inetferropmolaintitoenrp boalsaetido nonb adsiespdeorn-
sdioisnp perosiinotns. points.
TThhee PPCC ttiimmee sseerriieess oofft htheefi frisrtsat nadndse sceocnodnmd omdoedseosf tohfe thEeO FEOanFa alynsailsy(sFiisg (uFrieg6uar,eb )6bao,bt)h
broetphr erseepnrtessepnetc isapleccyiacll ecsywcleitsh wsliitghh stliflguhctt uflautcitounastioovnesr olvoenrg elorntgimere tsimcaele ssctahleasn tthhaons ethsoeseen
intheCSEOFmodes. TheamplitudeofthefirstPC(Figure6a)fluctuatesoveranannual
cycle,similartotheoriginalprecipitationdata. TheloadingpatternsofthefirstEOFmode
(Figure6c)exhibitobvioussymmetrybetweenthenorthandsouthregions,andthoseof
thesecondmode(Figure6d)exhibitanincreasefromnorthtosouth.
The advantage of the CSEOF analysis is demonstrated by the PC time series. The
nestedperioddissetto12monthsintheCSEOFanalysisbecausetheseasonalcycleisto
beextracted. ThefirstCSEOFmodeofprecipitationexplains73.86%ofthetotalvariance
(Figure7). ThePCtimeseriesofthefirstmode(Figure7a)andthecyclostationaryloading
patterns (Figure 7b) are shown for 12 months, from January to December. The loading
patternsareinterpolatedbasedonthedispersionpoints. Thismodedenotestheseasonal
cycle. The most pronounced feature of the CSLVs is the slowly varying precipitation
throughout the year: the vectors indicate low rainfall from January to May, plenty of
rainfallfromJunetoSeptember,anddecreasingrainfallfromOctobertoDecember. The
correspondingPCtimeseriesexhibitsinterannualanddecadalvariationsintheseasonal
cycle,aswellasanincreasingtrendthatissignificantbutnotconspicuous,withstronger
naturalvariability.

Atmosphere 2022, 13, x FOR PEER REVIEW 8 of 17
seen in the CSEOF modes. The amplitude of the first PC (Figure 6a) fluctuates over an
annual cycle, similar to the original precipitation data. The loading patterns of the first
EOF mode (Figure 6c) exhibit obvious symmetry between the north and south regions,
Atmosphere2022,13,500 8of17
and those of the second mode (Figure 6d) exhibit an increase from north to south.
(d)
Figure 6. First anFdig usreec6o.nFdir sEtaOnFd smecoonddeEs OoFf mpordeecsipofitparteicoipni:t a(taio)n p: (rai)npcriipncaipl aclocmomppoonneennttt itmimesee rsieesroiefs1 sotf 1st
EOF mode, (b) pErOinFcmipoadle ,c(obm)pprionnciepnaltc toimmpeo nseenrtiteims eosfe 2rinesdo fE2OndF EmOFodmeo,d (ec,)(c )loloaaddiinnggv vecetcotrosrosf 1osft E1OstF EOF
mode,(d)loadingvectorsof2ndEOFmode.
mode, (d) loading vectors of 2nd EOF mode.
The advantage of the CSEOF analysis is demonstrated by the PC time series. The
nested period d is set to 12 months in the CSEOF analysis because the seasonal cycle is to
be extracted. The first CSEOF mode of precipitation explains 73.86% of the total variance
(Figure 7). The PC time series of the first mode (Figure 7a) and the cyclostationary loading
patterns (Figure 7b) are shown for 12 months, from January to December. The loading
patterns are interpolated based on the dispersion points. This mode denotes the seasonal
cycle. The most pronounced feature of the CSLVs is the slowly varying precipitation
throughout the year: the vectors indicate low rainfall from January to May, plenty of rain-

Atmosphere 2022, 13, x FOR PEER REVIEW  9 of 17

fall from June to September, and decreasing rainfall from October to December. The cor-
responding PC time series exhibits interannual and decadal variations in the seasonal cy-
Atmosphere2022,13,500 cle, as well as an increasing trend that is significant but not conspicuous, with stron9goefr1 7
natural variability.

(a)
(b)
| Jan  | !           | Feb  | !           |            | Mar  | !          | Apr  | !          |     |
| ---- | ----------- | ---- | ----------- | ---------- | ---- | ---------- | ---- | ---------- | --- |
|      | !           |      | !           |            |      | !          |      | !          |     |
|      | ! !!        |      | !           | !!         |      | ! !!       |      | ! !!       |     |
|      | ! ! !       |      | ! ! !       |            | ! !  | !          |      | ! ! !      |     |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! !         | !    | ! !         | !          |      | ! !        | !    | ! !        | !   |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! !         | !    | ! !         | !          |      | ! !        | !    | ! !        | !   |
|      | ! ! ! ! !   |      | ! ! ! !     | !          | ! !  | ! ! !      |      | ! ! ! ! !  |     |
|      | ! ! ! !     | !    | ! ! !       | ! !        | !    | ! ! !      | !    | ! ! !      | ! ! |
|      | ! !         |      | ! !         |            |      | ! !        |      | ! !        |     |
|      | ! ! ! ! !   | !    | ! ! ! ! !   | !          | ! !  | ! ! !      | !    | ! ! ! ! !  | !   |
|      | ! ! !       |      | ! !         | !          |      | ! ! !      |      | ! ! !      |     |
|      | ! ! !       |      | ! !         | !          | !    | ! !        |      | ! !        | !   |
|      | !!          |      | !!          |            |      | !!         |      | !!         |     |
|      | ! ! !!      |      | ! ! !!      |            | ! !  | !!         |      | ! ! !!     |     |
|      | ! !         |      | ! !         |            | !    | !          |      | ! !        |     |
|      | !           |      | !           |            | !    |            |      | !          |     |
| May  |             | Jun  |             |            | Jul  |            | Aug  |            |     |
|      | !           |      | !           |            |      | !          |      | !          |     |
|      | !           |      | !           |            |      | !          |      | !          |     |
|      | ! ! !!      |      | ! !         | !!         | !    | ! !!       |      | ! ! !!     |     |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! ! ! !     |      | ! ! ! !     |            | ! !  | ! !        |      | ! ! ! !    |     |
|      | !           |      | !           |            |      | !          |      | !          |     |
|      | ! !         | !    | ! !         | !          |      | ! !        | !    | ! !        | !   |
|      | ! ! ! !     |      | ! ! ! !     |            | !    | ! ! !      |      | ! ! ! !    |     |
|      | !           | !    | !           | !          |      | !          | !    | !          | !   |
|      | ! ! ! ! !   |      | ! ! ! !     | !          | ! !  | ! ! !      |      | ! ! ! ! !  |     |
|      | ! ! ! !     | !    | ! ! !       | ! !        | !    | ! ! !      | !    | ! ! !      | ! ! |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! ! ! !     | !    | ! ! ! !     | !          | !    | ! ! !      | !    | ! ! ! !    | !   |
|      | ! ! !       |      | ! !         | !          |      | ! ! !      |      | ! ! !      |     |
|      | ! ! !       |      | ! !         | !          | !    | ! !        |      | ! !        | !   |
|      | !!          |      | !!          |            |      | !!         |      | !!         |     |
|      | ! ! ! !!    |      | ! ! ! !!    |            | ! !  | ! !!       |      | ! ! ! !!   |     |
|      | !           |      | !           |            | !    |            |      | !          |     |
|      | !           |      | !           |            | !    |            |      | !          |     |
| Sep  |             | Oct  |             |            | Nov  |            | Dec  |            |     |
|      | !           |      | !           |            |      | !          |      | !          |     |
|      | ! !         |      | ! !         |            |      | ! !        |      | ! !        |     |
|      | ! ! !!      |      | ! !         | !!         | !    | ! !!       |      | ! ! !!     |     |
|      | ! ! !       |      | ! ! !       |            | ! !  | !          |      | ! ! !      |     |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | !           | !    | !           | !          |      | !          | !    | !          | !   |
|      | ! ! !       |      | ! ! !       |            |      | ! ! !      |      | ! ! !      |     |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! ! !       | !    | ! !         | ! !        |      | ! ! !      | !    | ! ! !      | !   |
|      | ! ! ! !     |      | ! ! ! !     |            | ! !  | ! !        |      | ! ! ! !    |     |
|      | ! ! !       | !    | ! !         | ! !        | !    | ! !        | !    | ! !        | ! ! |
|      | ! ! !       |      | ! ! !       |            | !    | ! !        |      | ! ! !      |     |
|      | ! ! ! ! !   | !    | ! ! ! !     | ! !        | !    | ! ! ! !    | !    | ! ! ! ! !  | !   |
|      | ! !         |      | ! !         |            |      | ! !        |      | ! !        |     |
|      | ! ! !       |      | ! !         | !          | !    | ! !        |      | ! !        | !   |
|      | ! !! !!     |      | ! !! !!     |            | !    | !! !!      |      | ! !! !!    |     |
|      | ! !         |      | ! !         |            | !    | !          |      | ! !        |     |
|      | ! !         |      | ! !         |            | ! !  |            |      | ! !        |     |
|      | −1.00~−0.75 |      | −0.50~−0.25 |  0.00~0.50 |      |  1.00~1.50 |      |  2.00~2.50 |     |

|     | −0.75~−0.50 |     | −0.25~0.00 |  0.50~1.00 |     |  1.50~2.00 |     |  2.50~3.50 |     |
| --- | ----------- | --- | ---------- | ---------- | --- | ---------- | --- | ---------- | --- |
Figure 7. First CSEOF modes of precipitation: (a) principal component time series, (b) cyclostation-
Figure7.FirstCSEOFmodesofprecipitation:(a)principalcomponenttimeseries,(b)cyclostationary
ary loading vectors (CSLV).
loadingvectors(CSLV).
TThhee sesecoconndd CCSSEEOOFF mmooddee shshoowwnn inin FFigiguurere 88 exexpplalainins s55.0.055%% oof fththe etototatla lvvarairainancec eafatfetre r
oommitittitningg thteh esesaesaosnoanla clyccylec l(eth(eth feirsfit rmstomdeo)d aen)da naddjuasdtjiunsgt ifnogr tfhoer stehaesosneaasl ocnyacllec. yTchlee. pTreh-e
cpiprietcaitpioitna tdioimnidniimshiensi sinh eAspinrilA apnrdil tahnedn tinhcerneainsecrse uansetisl uJunltyi,l dJuelcyr,edaesecsre saigsensifsiicgannitfilyc ainn tAlyui-n
gAusutg aunsdt atnhdenth ienncrienacsreesa suenstuiln DtielcDeemcebmerb. eTrh. Te hPeCP tCimtiem seersieersi eosf otfhteh seesceocnodn dmmodoed eshsohwows sa a
ppoosistiitvivee pphhaasese shshifitf tinin aapppproroxximimaatetelyly 22000066. .CCoommpparaerded wwitihth ththe eyyeaerasr sbbeefoforere 22000066, ,mmoorere
recentprecipitationtendstobemoreextensive. Thus,thesecondmodeindicatesslightly
lessprecipitationinAugustandrelativelylargeincreasesinprecipitationinJuly.

Atmosphere 2022, 13, x FOR PEER REVIEW 10 of 17
Atmosphere2022,13,500 recent precipitation tends to be more extensive. Thus, the second mode indicates sli1g0hotfly17
less precipitation in August and relatively large increases in precipitation in July.
(a)
(b)
Jan ! Feb ! Mar ! Apr !
! ! ! !
! ! ! !
! ! ! ! ! !! ! ! ! ! ! !! ! ! ! ! ! !! ! ! ! ! ! !!
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! !
!
! ! !
!! !! !
! ! !
!! !! !
! ! !
!! !! !
! ! !
!! !!
! ! ! !
May ! Jun ! Jul ! Aug !
! ! ! !
! ! ! !
! ! ! ! ! !! ! ! ! ! ! !! ! ! ! ! ! !! ! ! ! ! ! !!
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! !
!
! ! !
!! !! !
! ! !
!! !! !
! ! !
!! !! !
! ! !
!! !!
! ! ! !
Sep ! Oct ! Nov ! Dec !
! ! ! !
! ! ! !
! ! ! ! ! !! ! ! ! ! ! !! ! ! ! ! ! !! ! ! ! ! ! !!
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
! ! ! ! ! ! ! ! ! ! ! !
!
! ! !
!! !! !
! ! !
!! !! !
! ! !
!! !! !
! ! !
!! !!
! ! ! !
−4.00~−2.00 −1.50~−1.00 −0.50~0.00 0.50~1.00 1.50~2.00
−2.00~−1.50 −1.00~−0.50 0.00~0.50 1.00~1.50 2.00~4.00
Figure 8. Second CSEOF modes of precipitation: (a) principal component time series, (b) cyclosta-
Figure8.SecondCSEOFmodesofprecipitation:(a)principalcomponenttimeseries,(b)cyclosta-
tionary loading vectors (CSLV).
tionaryloadingvectors(CSLV).
In the EOF and CSEOF analyses, the thirteen leading EOF modes and fifteen leading
IntheEOFandCSEOFanalyses,thethirteenleadingEOFmodesandfifteenleading
CSEOF modes account for 95.15% and 95.22% of the total variance, respectively; these
CSEOF modes account for 95.15% and 95.22% of the total variance, respectively; these
modes are statistically significant and distinct from the other modes; thus, they are se-
modesarestatisticallysignificantanddistinctfromtheothermodes;thus,theyareselected
lected for forecasting according to the rule of thumb [41]. The 13 leading temporal modes
forforecastingaccordingtotheruleofthumb[41].The13leadingtemporalmodesfromthe
fEroOmF tahned E1O5Fm aondde s1f5o mrmodthees CfoSrEmO tFhcea CnSaEcOcoFu cnatna baocvcoeu9n5t% aboofvtoet a9l5v%a roiaf ntocteaal rveairniatenrcper eatreed
inastetrhpereptreidm aasr ythceo pnrdimitiaornys cfoonrdtihteiofnosr mfoar ttihoen foofrmpraetcioipni toaft iporne,ciwpiitthatitohne, rwemitha itnhien gremmoadine-s
incogn msioddereesd coanssniodiesreeodf adsa ntao.ise of data.

Atmosphere 2022, 13, x FOR PEERREVIEW 11 of 17
Atmosphere2022,13,500 11of17
3.2. Forecasting of Precipitation
3.2. FoOrencacsetitnhge opfrPerceipciiptiattaitoionn dataaredecomposed intoEOF and CSEOF modes, anARIMA
model is applied in the EOF and CSEOF spaceto derive precipitation variations in the PC
OncetheprecipitationdataaredecomposedintoEOFandCSEOFmodes,anARIMA
time series. This composition of analysis and regression method results in twocombined
modelisappliedintheEOFandCSEOFspacetoderiveprecipitationvariationsinthePC
forecasting models: a combined EOF–ARIMA model and a combined CSEOF–ARIMA
timeseries.Thiscompositionofanalysisandregressionmethodresultsintwocombinedfore-
model.
castingmodels: acombinedEOF–ARIMAmodelandacombinedCSEOF–ARIMAmodel.
Forecasts of the temporalpatterns andtimescales of the PCs can be estimatedusing
ForecastsofthetemporalpatternsandtimescalesofthePCscanbeestimatedusing
thesecombinedmodels. Figure9 shows the forecasts for the four leading PCs of the pre-
these combined models. Figure 9 shows the forecasts for the four leading PCs of the
prceipciiptaittiaotnio dnadtaa.t aT.hTe hfoerfeocraesctass ftosrf othret hfiersfit rPsCtP oCbtoabintaeidneudsinugsi nthge tEhOeFE–OAFR–IAMRAIM mAodmeol dadele-
adqeuqautealtye lcyacpatputruerethteh eanannunualalflfluuctcutuaatitoionnss, ,aanndd tthhee ffoorreeccaassttss ffoorr tthhee ootthheerrPPCCssa alslosoe xehxhibiibtit
cyccylcilciaclalflfuluctcutuaatitoionnss( (FFiigguurree 99aa))wwiitthh ssmmaalllleerr aammpplliittuuddeess. .TTheh efofroerceacsatsst osbotbaitnaiendeudsuinsgin tghe
thCeSCESOEFO–AF–RAIMRIAM Amomdoedl eclocnotnintiuneu ethteh eininteterarannnnuualalaanndd ddeeccaaddaallttrreennddss oobbsseerrvveedd inint htehe
CCSESEOOFFa nanalaylysissis( F(iFgiguurere9 b9)b.).T Thheea mamppliltiutuddeesso offt htheefl fuluctcutuataitoionnssa raerecocnontitninuuataitoionnsso offt hthee
papsatsPtCPCs;st;h tihsisis isth teheg ogaolaolfotfh teheC CSESOEOF–FA–ARIRMIMAAm modoedle.l.
b
FiFgiugruere9 .9F. Foroerceacsatsstso offp prirninccipipaallc coommppoonneennttt tiimmee sseerriieess bbaasseedd oonn EEOOFF aanndd CCSSEEOOFF aannaallyyssiiss.. ((aa)) PPCC
fofroerceacsatsstos foEf OEOF–FA–ARIRMIMAA,(,b()bP) CPCfo froerceacsatsstos foCf SCESOEOF–FA–RAIRMIMA.A.
Based on the PC forecasts, precipitation forecasts can be easily extrapolated using
theloadingvectors(spatialpatterns)oftheEOFandCSEOF.Quantitativeprecipitation

Atmosphere 2022, 13, x FOR PEER REVIEW  12 of 17

Atmosphere 2022, 13, x FOR PEER REVIEW  12 of 17

Atmosphere2022,13,500 Based on the PC forecasts, precipitation forecasts can be easily extrapolate1d2 oufs1i7ng the
loading vectors (spatial patterns) of the EOF and CSEOF. Quantitative precipitation fore-
Based on the PC forecasts, precipitation forecasts can be easily extrapolated using the
casts are calculated for 56 weather stations over five years using the EOF–ARIMA and
loading vectors (spatial patterns) of the EOF and CSEOF. Quantitative precipitation fore-
CSfoErOecFa–sAtsRarIeMcAalc muloatdeedlsfo, ran56dw theaet hreesruslttasti aornes tohveenr ficvheecykeaerds uagsianignstht ethEeO oFb–AseRrIvMedA panredcipita-
casts are calculated for 56 weather stations over five years using the EOF–ARIMA and
CSEOF–ARIMAmodels,andtheresultsarethencheckedagainsttheobservedprecipitation
tion data. Figure 10 shows scatter plots of the observations and the forecasts resulting  CSEOF–ARIMA models, and the results are then checked against the observed precipita-
data. Figure10showsscatterplotsoftheobservationsandtheforecastsresultingfromthe
frotmio nt hdea ttaw. oFi gmuored e1l0s .s hTohwe sp sociantttesr c polrortess pofo nthdei nogbs teorv faotrioencas satns df rtohme  fEorOecFa–sAtsR rIeMsuAlti nagn d ob-
twomodels. ThepointscorrespondingtoforecastsfromEOF–ARIMAandobservation
serfvroamtio tnh ep tawrtol ym doodtetlesd. T ahreo uponidn tasb coovrree sapnodn dbienlgo wto  tfhoere yca =st xs  flrionme  dEiOviFd–eAdR bIMy Aob asnedrv oabt-ion as
partlydottedaroundaboveandbelowthey=xlinedividedbyobservationas400mm
400se mrvmat i(oFni gpuarrtel y1 0dao)t.t eItd m areoaunnsd t habaot vthe ea nfodr beeclaoswts  tahree y s l=i gxh ltinlye  odviveirdeesdti mbya otebdse wrvhateinon l easss  than
(Figure10a). Itmeansthattheforecastsareslightlyoverestimatedwhenlessthan400mm
40b04 u 0mt 0  mmn m d be  (ur F eti s g tuu imnreda  1 tee 0rd ae)sw .t Iih tm  m naetg aer nde s a  wt h eha tet   tnh a e ng fr4 oe0 rae 0tcem ars m ttsh  aaI r nne  c s4o li0n g0t h r t aml y tm  o v.h e eIrne p s octi iom nnt a sttrc eao dsr  tw r,e h sthp eneo   lpe soi s ni nt htt aso nc orre-
|     | u   | e   | t r h | .   | s , t | n d g |
| --- | --- | --- | ----- | --- | ----- | ----- |
400 mm but underestimated when greater than 400 mm. In contrast, the points corre-
spfoonredciansgts tforo mforCeScEaOstFs– fAroRmIM ACSaEndOoFb–sAerRvIaMtioAn calnudst eorebdsearrvouatnidonth celyus=texrleinde a(Frioguunred1 0thbe). y = x
sponding to forecasts from CSEOF–ARIMA and observation clustered around the y = x
linIet l(oFoikgsumreo 1re0bev).e Intl ylodoikstsr imbuotreed eavnedntloy hdaivsetrhibiguhteerdd aisnpde rtsoio hna.ve higher dispersion.
line (Figure 10b). It looks more evenly distributed and to have higher dispersion.
| (a) |     |     | (b) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| (a) |     |     | (b) |     |     |     |
| 800 |     |     | 800 |     |     |     |
| 800 |     |     | 800 |     |     |     |
y=x y=x
|        |     | y=x |            |     | y=x |     |
| ------ | --- | --- | ---------- | --- | --- | --- |
| m)60 0 |     |     | m)m)660000 |     |     |     |
m) 600
| m m       |     |     | mm        |     |     |     |
| --------- | --- | --- | --------- | --- | --- | --- |
| ( t  ( t  |     |     | ( t  ( t  |     |     |     |
| s s       |     |     | s s       |     |     |     |
| a40a0 400 |     |     | aa440000  |     |     |     |
| c         |     |     | c         |     |     |     |
| e c e     |     |     | e re c    |     |     |     |
r
| o r o |         |         | Fo o r |         |         |     |
| ----- | ------- | ------- | ------ | ------- | ------- | --- |
| F F   |         |         | F      |         |         |     |
| 200   |         |         | 200    |         |         |     |
| 200   |         |         | 200    |         |         |     |
| 0     |         |         | 0      |         |         |     |
| 0 0   | 200 400 | 600 800 | 00     | 200 400 | 600 800 |     |
0 200 Obs4e0rv0ation (m60m0) 800 0 2O00bservat4io0n0 (mm) 600 800

|     | Observation (mm) |     |     | Observation (mm) |     |     |
| --- | ---------------- | --- | --- | ---------------- | --- | --- |

Figure 10. Scatter plots on observation and forecasts of EOF–ARIMA and CSEOF–ARIMA: (a) EOF–
FigFAuigRrueIMr 1e0A1.0  Sf.ocSracetactatetsret rsp,p l(olbot)ts s CooSnnE ooObbFss–eeArrvvRaaItMtiiooAnn a fanonrdedfco afrsoetrsce.a csatsstosf oEfO EFO–AFR–AIMRAIManAd aCnSdE OCFS–EAORFIM–AAR:I(Ma)AEO: (Fa–) EOF–
ARAIRMIMAA fofroerceacasststs, ,((bb)) CCSSEEOOFF––AARRIMIMAAfo froerceacstass.ts.
The mean monthly values of the precipitation forecasts obtained from the two com-
binTehdT e hm  e momdea eealnsn   mamreo o ncnot t hmh l ypy  av vraea ldl u u we s oho f ftt  hh thee eop resr cee irc pvi iap tta iit toi ont nsio, fan os  r f esohc aoe swc ts o it bns t   a oFiib ngt eua drien f r e1o d1m.  fBr teo hcm eaut w tsheo eoc o wtmhoe-
|     |     | l e sit  |  bp | a   | r ans |    ft   com- |
| --- | --- | -------- | --- | --- | ----- | ------------ |
beifnfeecdt mof otdheel sAasiraenc momonpsaoroedn, wraiitnhfathlle iso ubsneervveant,i ownist,ha msoshsto rwaninfianllF oigcucurerr1in1g. iBne tchaeu sseumof-
bined models are compared with the observations, as shown in Figure 11. Because of the
tmheere.f fTehcte oEfOthFe–AARsiIaMnAm foonrseocaosnt,s raarien fnalolt ispaurntiecvuelnar,lwy igthoomdo, setspraeicniafalllyl ofcocru trhrien gsuimnmtheer
effect of the Asian monsoon, rainfall is uneven, with most rainfall occurring in the sum-
smumonmthesr.. HThoewEeOveFr–, AthReI MCSAEOfoFr–eAcaRstIsMaAre fnooretcpaasrttsi cnuolta orlnylyg ocoapdt,uersep ethciea slleyasfoorntahl evasurimatmioenrs
mer. The EOF–ARIMA forecasts are not particularly good, especially for the summer
mino nptrhesc.iHpiotawtieovne r,btuhte aClSsoE OgFiv–eA RcIoMnfAidfeonrte cqaustasnntoittaotinvley cparpetduircetitohness eoafs othnea lpvraerciaiptiiotnatsioinn
months. However, the CSEOF–ARIMA forecasts not only capture the seasonal variations
parmecoiupnittast.i onbutalsogiveconfidentquantitativepredictionsoftheprecipitationamounts.
in precipitation but also give confident quantitative predictions of the precipitation
amounts.

FFiigguurree1 111.. TTeemmppoorraallm meeaanno offo obbsseerrvvaatitoionnw witihthE EOOFF––AARRIMIMAAa annddC CSSEEOOFF––AARRIMIMAAf oforereccaastsst.s.
Themeandeviationsoftheforecastsobtainedforthesummermonsoonseason(June,

July,AugustandSeptember)ateachweatherstationareshowninFigure12. TheEOF–
Figure 11. Temporal mean of observation with EOF–ARIMA and CSEOF–ARIMA forecasts.
ARIMAmodelgiveshigherforecastsinJuneandSeptemberbutrelativelylowforecasts

Atmosphere 2022, 13, x FOR PEER REVIEW 13 of 17
The mean deviations of the forecasts obtained for the summer monsoon season (June,
July, August and September) at each weather station are shown in Figure 12. The EOF–
ARIMA model gives higher forecasts in June and September but relatively low forecasts
in July and August (Figure 12a). In contrast, the mean deviation of the forecasts obtained
from the CSEOF–ARIMA model are much smaller, with small overestimations in June
and July and small underestimations in August and September (Figure 12b).
When the EOF method is used to analyze precipitation time series data, it cannot
provide temporal variation responses in the spatial domain when decomposing the time
components; thus, some errors result in the distribution analysis. The use of the CSEOF
method can make up for this deficiency.
In the spatial distribution of the mean deviation (Figure 12a,b), the errors spread over
Atmosphere2022,13,500 13of17
in June are higher than those in July of the study area. We considered that the reason for
this result is that precipitation increases obviously and the distribution changes greatly in
July, leading to increased errors and causing the June and July deviation characteristics in
inJulyandAugust(Figure12a). Incontrast,themeandeviationoftheforecastsobtained
botfhro mmeththeoCdSsE.O F–ARIMAmodelaremuchsmaller,withsmalloverestimationsinJuneand
JulyandsmallunderestimationsinAugustandSeptember(Figure12b).
(a) (b)
Figure12.MeandeviationdistributionofforecastsofEOF–ARIMAandCSEOF–ARIMAinJune,July,
Figure 12. Mean deviation distribution of forecasts of EOF–ARIMA and CSEOF–ARIMA in June,
AugustandSeptember,(a)EOF–ARIMAforecastsmeandeviationdistribution,(b)CSEOF–ARIMA
July, August and September, (a) EOF–ARIMA forecasts mean deviation distribution, (b) CSEOF–
forecastsmeandeviationdistribution.
ARIMA forecasts mean deviation distribution.
When the EOF method is used to analyze precipitation time series data, it cannot
providetemporalvariationresponsesinthespatialdomainwhendecomposingthetime
Several statistical measures are used to evaluate the performance of the forecasting
components;thus,someerrorsresultinthedistributionanalysis. TheuseoftheCSEOF
methods: the mean absolute error (MAE), the root mean squared error (RMSE) and the
methodcanmakeupforthisdeficiency.
coeffici I e n n t t h o e f s p d a e t t ia e l r d m is i t n ri a b t u i t o io n n ( o R f2t ) h . e W m e e a u n s d e e t v h ia e t s io e n s ( t F a i n gu d r a e r 1 d 2 s a , t b o ), m the ea e s rr u o r rs e s t p h r e e a e d rr o o v r e r between the
obsienrJvuende avraelhuiegh aenrdth asnimthuolsaetiendJ uvlayloufet hoefs otuudry maroead.eWl esoco anss itdoe rmedetahsautrthee trheea saopnpfolircability and
pratchtiiscraebsuillittiys tohfa topurre cmipoitadteioln aisn car ewashesooleb.v Tioaubsllye a1n dprthoevdidisetrsi bau tcioonmcphaanrgiseosngr eoaft ltyhiense measures
July,leadingtoincreasederrorsandcausingtheJuneandJulydeviationcharacteristicsin
applied for the two combined models. The results show that both models achieve good
bothmethods.
performance and that their accuracies are similar. However, the performance of the
Severalstatisticalmeasuresareusedtoevaluatetheperformanceoftheforecasting
CSEmOetFh–oAdsR: IthMeAm emanoadbeslo lius tbeeetrtreorr (tMhaAnE )t,hthaet orofo tthmee EanOsFq–uAarRedIMerrAor m(RoMdSeEl )uannddethr eevery meas-
urec. oTefhfiec ioenvteorfadlle treersmuilntast iionnd(iRca 2)t.eW theauts eththee CseSsEtaOndFa–rAdsRtIoMmAea smuroedtehle iesr raonr beeftfweceteinve approach
theobservedvalueandsimulatedvalueofourmodelsoastomeasuretheapplicability
for precipitation forecasting.
andpracticabilityofourmodelasawhole. Table1providesacomparisonofthesemea-
suresappliedforthetwocombinedmodels. Theresultsshowthatbothmodelsachieve
goodperformanceandthattheiraccuraciesaresimilar. However,theperformanceofthe
CSEOF–ARIMAmodelisbetterthanthatoftheEOF–ARIMAmodelundereverymeasure.
TheoverallresultsindicatethattheCSEOF–ARIMAmodelisaneffectiveapproachfor
precipitationforecasting.

| Atmosphere2022,13,500 |     |     |     |     |     |     | 14of17 |
| --------------------- | --- | --- | --- | --- | --- | --- | ------ |
Table1.Quantitativestatisticalverificationmeasuresofforecasts.
R2
|     |     | Index       | MAE(mm) | RMSE(mm) |     |      | CC   |
| --- | --- | ----------- | ------- | -------- | --- | ---- | ---- |
|     |     | EOF–ARIMA   | 57.86   | 74.44    |     | 0.79 | 0.68 |
|     |     | CSEOF–ARIMA | 49.41   | 67.71    |     | 0.87 | 0.76 |
4. Discussion
Manyscholarshaveadoptedawiderangeofmethodsforstudyingtheprecipitation
predictionworkinSouthKorea,suchasusingtheWeatherResearchandForecasting(WRF)
andVery-Short-RangeForecastofPrecipitation(VSRF)systemmodelsforprecipitationfore-
castinginindividualbasinsofSouthKorea[42–44].Inaddition,someacademicsfocusedon
monthlyprecipitationforecastingoversouthKoreabycombiningthesuperensemblepro-
cedurewitheigenvectoranalysisandcorrelationanalysis[45,46]. Basedonthreedifferent
BayesianRegressionModels,otherresearchersinvestigatedtheprecipitationforecastingof
summerseasoninaregionaroundKorea[47].
Inordertobetterdescribetheperformanceofourmodel,wecompareourmodelto
thepublishedresearchaboutprecipitationforecastinginKorea. Theresultsareshownin
Table2.
Table2.ComparisonofseveralprecipitationforecastingmodelsinKorea.
|               |           | PrecipitationSource |           |           |            | PerformanceEvaluation |       |
| ------------- | --------- | ------------------- | --------- | --------- | ---------- | --------------------- | ----- |
| ModelorSystem | StudyArea |                     | Predictor | TimeScale | TimePeriod |                       |       |
|               |           | Type                |           |           |            | RMSE                  | CC R2 |
BayesianRegression
OverSouthKorea StationsandGrids GDAPS Monthly 1979–2007 1.09 - -
| Models[47]     |                  |                  |     | (AverageJJA) |           |              |     |
| -------------- | ---------------- | ---------------- | --- | ------------ | --------- | ------------ | --- |
| Meteorological | ImjinRiverBasin  |                  |     |              |           |              |     |
|                |                  | StationsandGrids | -   | 6h           | 2007–2011 | 59.67–212.80 | - - |
| ModelofWRF[42] | ofKoreapeninsula |                  |     |              |           |              |     |
Seoul&suburban
WRFModel[43] inSouthKorea Grids SSTData 3h 26–29July2011 2.54–13.18 0.2–0.59 -
|               | KyounganRiver | StationsandRadar |     |        |     |           |           |
| ------------- | ------------- | ---------------- | --- | ------ | --- | --------- | --------- |
| VSRFmodel[44] | basinof       |                  | -   | Hourly |     | 5.77–7.67 | - 0.7–0.8 |
|               | SouthKorea    | Reflectivity     |     |        |     |           |           |
SVDAandCCA[45] OverSouthKorea Stations SLPData Monthly 1954–2003 - 0.11–0.87 -
CyclostationaryEOF
OverSouthKorea Stations SST Monthly 1973–2013 54.17–63.85 0.69–0.73 0.55–0.67
andCCA[46]
CyclostationaryEOF
andARIMA OverSouthKorea Stations Precipitation Monthly 1973–2021 67.71–74.44 0.79–0.87 0.68–0.76
Table2showsthecomparisonbetweenourmodelandseveralpublishedcharacteristic
modelsontheirstudyareainput,datasets,timescaleperiodandperformanceevaluation.
From the table, we can see that the study areas of these models are all or part of
SouthKorea, whichprovidescomparabilityinthispaper. Intermsofdatasources, the
precipitationdatausedineachmodelwerebasicallystation,satelliteandradarobservation
data. Dataselectionmainlydependsonthecharacteristicsandrequirementsofeachmodel
TheSVDAandCSEOFmodelsallusedstationdata,andothersusedsatelliteandradar
data. Inthecomparisonofpredictors,allmodelsusedsomeoceanvariablesaspredictors
exceptours;ourmodeluseditsownstationdataasapredictor. Therefore,ourmodelis
relativelysimpleinthecompositionarchitecture. Fromtheanalysisoftimescale,theWRF
modelsystemcouldforecastprecipitationonmultiplehourscale,whichistheadvantage
ofthesemodels. Whileotherstatisticalmodels(includeours)couldonlydoprecipitation
forecasting on monthly scale. In terms of time period, some models are only aimed at
theforecastofconcentratedrainfallinsummer,whilestatisticalmodelsareaimedatthe
precipitationforecastoflong-timeseriesthroughouttheyear. Fromtheanalysisofmodel
performance, although there are differences in time scale, these models had obtained
accurateandreliableresults.
Wecanseethatourmodelonlyusesitsowndataasinputdataanddoesnothaveas
muchdataasothermodels. Thisisthecharacteristicofourmodelthatisdifferentfrom
othermodels.

Atmosphere2022,13,500 15of17
Inourwork,weprovidearelativelysimplemethodbasedonstatisticsforprecipitation
forecasting in South Korea. The required data are only the rainfall observation data of
eachstationwithoutcomplexdatarequirements. Intermsofaccuracy,itmaynotbemore
accuratethanothercomplicatedmethods,butithasstrongapplicabilityandcanbeapplied
tostationrainfallpredictioninvariousorspecificareas.
5. Conclusions
Thisstudyextendsresearchandprovidesasimpleandfeasiblemethodforprecip-
itation forecasting that only relies on stations’ precipitation data. We investigated the
spatiotemporal variability in precipitation data in South Korea using EOF and CSEOF
analysesandproposedaneffectivemethodologyforprecipitationforecasting. Ofthetotal
variance in the spatial distribution and temporal evolution of the studied precipitation
data,the13leadingEOFmodesaccountedfor95.15%,andthe15leadingCSEOFmodes
accountedfor95.22%. TheEOFmodesrepresentedcycleswithlongertimescalesthanthe
CSEOFmodes;theCSEOFmodesrepresentedinterannualanddecadalvariationsinthe
seasonalcyclewithstrongernaturalvariabilitiesthanthoseseenintheEOFmodes.
We estimated precipitation forecasts using a regression method. The PC forecasts
obtained from the EOF–ARIMA model exhibited clear cyclical fluctuations, and those
obtainedfromtheCSEOF–ARIMAmodelrepresentedextensionsoftheinterannualand
decadalvariationsobservedintheCSEOFanalysis. BasedonthePCforecasts,quantitative
precipitationforecastswerecalculatedfor56stationsoverfiveyearsusingtheEOF–ARIMA
and CSEOF–ARIMA models; these forecasts were then checked against the observed
precipitationdata.
In this article, we combined the EOF and CSEOF models with the ARIMA model,
respectively,forprecipitationforecasting. Basedonthecomparisonbetweenthesimulated
valuesofthetwomodelsandtheobservedvalues,throughthestatisticalmeasuredvalues
(MAE, RMSE, R2), we preliminarily draw this conclusion: For these two models, the
CSEOF–ARIMAcombinedmodelperformedbetterthantheEOF–ARIMAcombinedmodel.
BecauseintheCSEOFanalysispart,theprecipitationdataaredecomposedintomonthly
spatialdistribution. ThatmeanstheCSEOFmodelcanfullytakeintoaccounttheseasonal
variationcharacteristicsofrainfalldatawithintheyear,whichshowstheadvantagesover
theEOFmodel.
ThefindingsuggeststhatthecombinedCSEOF–ARIMAforecastingmodelgavethe
betterapproximationperformanceandthatitcapturedthevariationaltrends,temporal
evolutionandrecurrentseasonalcyclesintheprecipitationdata. Theseresultsindicatethat
theuseoftheCSEOF–ARIMAmodelisanaccurateandefficientapproachforprecipitation
forecastinginKorea.
AuthorContributions: Conceptualization, M.S.; methodology, G.K.andY.W.; validationandre-
sources,M.S.andK.L.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbyKeyTechniquesforthePollutantSourceApportionmentand
WaterQualityManagementandtheirapplicationinthetypicalcontaminatedzoneofBohaiSea,grant
number2018YFC140707604.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
Acknowledgments:Wearethankfultoallthosewhocontributedtothisstudy.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.

Atmosphere2022,13,500 16of17
References
1. Trenberth,K.E.RecentObservedInterdecadalClimateChangesintheNorthernHemisphere.Bull.Am.Meteorol.Soc.1990,71,
377–390.[CrossRef]
2. Alijanian,M.;Rakhshandehroo,G.R.;Mishra,A.K.;Dehghani,M.EvaluationofsatelliterainfallclimatologyusingCMORPH,
PERSIANN-CDR,PERSIANN,TRMM,MSWEPoverIran.Int.J.Climatol.2017,37,4896–4914.[CrossRef]
3. Yao,J.;Chen,Y.;Yu,X.;Zhao,Y.;Yang,L.Evaluationofmultiplegriddedprecipitationdatasetsforthearidregionofnorthwestern
China.Atmos.Res.2020,236,104818.[CrossRef]
4. Huntington, T.G. Evidence for intensification of the global water cycle: Review and synthesis. J. Hydrol. 2006, 319, 83–95.
[CrossRef]
5. Oki,T.;Kanae,S.Globalhydrologicalcyclesandworldwaterresources.Science2006,313,1068–1072.[CrossRef]
6. Nicholls,N.;Alexander,L.Hastheclimatebecomemorevariableorextreme?Progress1992–2006.Prog.Phys.Geogr.2007,31,
77–87.[CrossRef]
7. Becker,S.;Gemmer,M.;Jiang,T.SpatiotemporalanalysisofprecipitationtrendsintheYangtzeRivercatchment.Stoch.Environ.
Res.RiskAssess.2006,20,435–444.[CrossRef]
8. Lim,Y.K.;Kim,K.Y.ANewPerspectiveontheClimatePredictionofAsianSummerMonsoonPrecipitation.J.Clim.2006,19,
4840–4853.[CrossRef]
9. Zhou,B.T.;Wang,H.RelationshipbetweentheborealspringHadleycirculationandthesummerprecipitationintheYangtze
Rivervalley.J.Geophys.Res.Atmos.2006,111,275.[CrossRef]
10. Kim,J.;Miller,N.L.;Farrara,J.D.;Hong,S.Y.ASeasonalPrecipitationandStreamFlowHindcastandPredictionStudyinthe
WesternUnitedStatesduringthe1997/98WinterSeasonUsingaDynamicDownscalingSystem. J.Hydrometeorol. 2000, 1,
311–329.[CrossRef]
11. Higgins,R.W.;Kim,H.K.;Unger,D.Long-LeadSeasonalTemperatureandPrecipitationPredictionUsingTropicalPacificSST
ConsolidationForecasts.J.Clim.2004,17,3398–3414.[CrossRef]
12. Wang,H.;Ting,M.;Ji,M.PredictionofseasonalmeanUnitedStatesprecipitationbasedonElNiñoseasurfacetemperatures.
Geophys.Res.Lett.1999,26,1341–1344.[CrossRef]
13. Silverman,D.;Dracup,J.A.ArtificialNeuralNetworksandLong-RangePrecipitationPredictioninCalifornia.J.Appl.Meteor
2010,39,57–66.[CrossRef]
14. Block,P.;Rajagopalan,B.InterannualVariabilityandEnsembleForecastofUpperBlueNileBasinKiremtSeasonPrecipitation.
J.Hydrometeorol.2007,8,327.[CrossRef]
15. Peel,S.;Wilson,L.J.ADiagnosticVerificationofthePrecipitationForecastsProducedbytheCanadianEnsemblePrediction
System.Weather.Forecast.2008,23,1.[CrossRef]
16. Chang,H.;Kwon,W.T.SpatialvariationsofsummerprecipitationtrendsinSouthKorea,1973–2005.Environ.Res.Lett.2007,2,
45012–45019.[CrossRef]
17. Jin,Y.H.;Kawamura,A.;Jinno,K.;Berndtsson,R.DetectionofENSO-influenceonthemonthlyprecipitationinSouthKorea.
Hydrol.Processes2005,19,4081–4092.[CrossRef]
18. Kim,K.Y.;Kim,Y.Y.InvestigationoftropicalPacificupper-oceanvariabilityusingcyclostationaryEOFsofassimilateddata.Ocean
Dyn.2004,54,489–505.[CrossRef]
19. Wang,B.;Ding,Q.;Jhun,J.G.TrendsinSeoul(1778–2004)summerprecipitation.Geophys.Res.Lett.2006,33,292–306.[CrossRef]
20. Aghakouchak,A.Evaluationofsatellite-retrievedextremeprecipitationratesacrossthecentralUnitedStates.J.Geophys.Res.
Atmos.2011,116,1–11.[CrossRef]
21. Stampoulis,D.;Anagnostou,E.N.EvaluationofGlobalSatelliteRainfallProductsoverContinentalEurope. J.Hydrometeorol.
2012,13,588–603.[CrossRef]
22. Gaona,M.;Overeem,A.;Brasjen,A.M.;Meirink,J.F.;Leijnse,H.;Uijlenhoet,R.EvaluationofRainfallProductsDerivedFrom
SatellitesandMicrowaveLinksforTheNetherlands.IEEETrans.Geosci.RemoteSens.2017,55,6849–6859.[CrossRef]
23. Barnston,A.G.;He,Y.;Glantz,M.H.PredictiveSkillofStatisticalandDynamicalClimateModelsinSSTForecastsduringthe
1997–98ElNiñoEpisodeandthe1998LaNiñaOnset.Bull.Am.Meteorol.Soc.1999,80,217–243.[CrossRef]
24. Vautard,R.;Plaut,G.;Wang,R.;Brunet,G.SeasonalPredictionofNorthAmericanSurfaceAirTemperaturesUsingSpace-Time
PrincipalComponents.J.Clim.1999,12,380–394.[CrossRef]
25. Waliser,D.E.;Jones,C.;Schemm,J.K.E.;Graham,N.E.AStatisticalExtended-RangeTropicalForecastModelBasedontheSlow
EvolutionoftheMadden-JulianOscillation.J.Clim.1999,12,1918–1939.[CrossRef]
26. Waliser,D.E.;Lau,K.M.;Stern,W.;Jones,C.PotentialPredictabilityoftheMadden-JulianOscillation.Bull.Am.Meteorol.Soc.
2003,84,33–50.[CrossRef]
27. Cahalan,R.F.;Wharton,L.E.;Wu,M.L.EmpiricalorthogonalfunctionsofmonthlyprecipitationandtemperatureovertheUnited
Statesandhomogeneousstochasticmodels.J.Geophys.Res.Atmos.1996,101,26309–26318.[CrossRef]
28. Singh, C.V. Empirical Orthogonal Function (EOF) analysis of monsoon rainfall and satellite-observed outgoing long-wave
radiationforIndianmonsoon:Acomparativestudy.Meteorol.Atmos.Phys.2004,85,227–234.[CrossRef]
29. Svensson,C.EmpiricalOrthogonalFunctionAnalysisofDailyRainfallintheUpperReachesoftheHuaiRiverBasin,China.
Theor.Appl.Climatol.1999,62,147–161.[CrossRef]

Atmosphere2022,13,500 17of17
30. Lorenz,E.N.EmpiricalOrthogonalFunctionsandStatisticalWeatherPrediction;ScientificReportNo.1;MIT:Cambridge,MA,USA,
1956;pp.1–49.
31. Hannachi,A.;Jolliffe,I.T.;Stephenson,D.B.Empiricalorthogonalfunctionsandrelatedtechniquesinatmosphericscience:A
review.Int.J.Climatol.2007,27,1119–1152.[CrossRef]
32. Kim,K.;North,G.R.;Huang,J.EOFsofOne-DimensionalCyclostationaryTimeSeries:Computations,Examples,andStochastic
Modeling.J.Atmos.Sci.1996,53,1007–1017.[CrossRef]
33. Kim,K.;North,G.R.EOFsofHarmonizableCyclostationaryProcesses.J.Atmos.Sci.1997,54,2416–2427.[CrossRef]
34. Kim,K.;Chung,C.OntheEvolutionoftheAnnualCycleintheTropicalPacific.J.Clim.2001,14,991–994.[CrossRef]
35. Kim,K.;Wu,Q.AComparisonStudyofEOFTechniques:AnalysisofNonstationaryDatawithPeriodicStatistics.J.Clim.1999,
12,185–199.[CrossRef]
36. Kim,K.;Roh,J.PhysicalMechanismsoftheWintertimeSurfaceAirTemperatureVariabilityinSouthKoreaandthenear-7Day
Oscillations.J.Clim.2010,23,2197–2212.[CrossRef]
37. Kim,Y.;Kim,K.-Y.;Kim,B.-M.PhysicalmechanismsofEuropeanwintersnowcovervariabilityanditsrelationshiptotheNAO.
Clim.Dyn.2013,40,1657–1669.[CrossRef]
38. Box,G.E.P.;Jenkins,G.M.TimeSeriesAnalysis:ForecastingandControl;Holden-Day:SanFrancisco,CA,USA,1971.
39. Akaike,H.ANewLookattheStatisticalModelIdentification.IEEETrans.Autom.Control1974,19,716–723.[CrossRef]
40. Schwarz,G.EstimatingtheDimensionofaModel.Ann.Stat.1978,6,461–464.[CrossRef]
41. North,G.R.;Bell,T.L.;Cahalan,R.F.;Moeng,F.J.SamplingErrorsintheEstimationofEmpiricalOrthogonalFunctions. Mon.
WeatherRev.1982,110,699.[CrossRef]
42. Jabbari,A.;So,J.-M.;Bae,D.-H.PrecipitationForecastContributionAssessmentintheCoupledMeteo-HydrologicalModels.
Atmosphere2020,11,34.[CrossRef]
43. Jee,J.B.;Ki,S.SensitivityStudyonHigh-ResolutionWRFPrecipitationForecastforaHeavyRainfallEvent.Atmosphere2017,8,96.
[CrossRef]
44. Kim,H.;Choi,J.;Nam,K.-Y.;Chang,K.;Oh,S.TheOperationalVeryShortRangeForecastofPrecipitationanditsHydrological
ApplicationsinSouthKorea.InProceedingsofthe33rdConferenceonRadarMeteorology,Cairns,Australia,5–10August2007.
45. Kim,M.K.;Kang,I.S.;Park,C.K.;Kim,K.M.SuperensemblepredictionofregionalprecipitationoverKorea.Int.J.Climatol.2004,
24,777–790.[CrossRef]
46. Sun,M.;Kim,G.QuantitativeMonthlyPrecipitationForecastingUsingCyclostationaryEmpiricalOrthogonalFunctionand
CanonicalCorrelationAnalysis.J.Hydrol.Eng.2016,21,123–145.[CrossRef]
47. Jo,S.;Lim,Y.;Lee,J.;Kang,H.S.;Oh,H.S.BayesianregressionmodelforseasonalforecastofprecipitationoverKorea.Asia-Pac.J.
Atmos.Sci.2012,48,205–212.[CrossRef]