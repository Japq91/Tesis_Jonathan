WeatherClim.Dynam.,4,567–589,2023
https://doi.org/10.5194/wcd-4-567-2023
©Author(s)2023.Thisworkisdistributedunder
theCreativeCommonsAttribution4.0License.
The relationship between extra-tropical cyclone intensity and
precipitation in idealised current and future climates
VictoriaA.Sinclair1andJenniferL.Catto2
1InstituteforAtmosphericandEarthSystemResearch/Physics,FacultyofScience,
UniversityofHelsinki,P.O.Box64,00014,Helsinki,Finland
2FacultyofEnvironment,ScienceandEconomy,UniversityofExeter,Exeter,UnitedKingdom
Correspondence:VictoriaA.Sinclair(victoria.sinclair@helsinki.fi)
Received:2December2022–Discussionstarted:8December2022
Revised:9May2023–Accepted:10May2023–Published:4July2023
Abstract.Extra-tropicalcyclones(ETCs)arethemaincause crease in vorticity due to diabatic heating is masked by the
of precipitation in the mid-latitudes, and there is substan- decrease in the Eady growth rate which occurs in both the
tial evidence that ETC-related precipitation will increase in uniform warming and polar amplification simulations com-
thefuture.However,littleisknownabouthowthiswillim- paredtothecontrol.
pact on the dynamical strength of ETCs, and whether the Thek-meansclusteringidentifiesfourdistinctandphysi-
impact will differ for different types of ETCs. We quantify callyrealistictypesofETCswhicharepresentinallexper-
thelinearrelationshipbetweenmaximumvorticityandETC- imentsmeaningthattheaverageprecipitationpatternsasso-
related precipitation in the current and idealised future cli- ciated with ETCs are unlikely to change in the future. The
mates and determine how this relationship depends on the strongestdependencybetweenETCmaximumvorticityand
structureandcharacteristicsoftheETC.Three10-year-long precipitation occurs for ETCs that have the most precipita-
aqua-planetsimulationsareperformedwithastate-of-the-art tionassociatedwiththewarmfront.ETCswiththeheaviest
globalmodel,OpenIFS,thatdifferintheirspecifiedseasur- precipitationalongthecoldfront,whicharethemostintense
facetemperature(SST)distributions.Acontrolsimulation,a storms in terms of maximum vorticity, also exhibit a strong
uniformwarmingsimulation,andapolaramplificationsim- dependency between precipitation and maximum vorticity,
ulationareperformed.ETCsareobjectivelyidentifiedusing butthisdependencyisweakerandhasasmallercorrelation
thefeature-trackingsoftwareTRACK,andk-meanscluster- coefficientthanthewarm-frontETCs.NotallETCtypesex-
ing is applied to the ETC precipitation field to group the hibit a strong dependency between precipitation and maxi-
ETCs into clusters with similar precipitation structures. In mumvorticity.ETCslocatedathighlatitudeswithweakpre-
allexperiments,ETCswithstrongermaximumvorticityare cipitationshowlittledependencyduetothelackofmoisture,
associatedwithmoreprecipitation. whereas ETCs with the precipitation located mainly in the
Forallcyclonesconsideredtogether,wefindthattheslope centreoftheETCshavetheweakestlinearregressionslope,
ofthelinearrelationshipbetweenmaximumcyclonevortic- whichislikelyduetothelackofupper-levelforcing.These
ity and ETC precipitation is larger in the uniform warming resultsstressthatdespitesmallchangesinthestrengthofthe
andpolaramplificationsimulationsthaninthecontrolsimu- cyclones,theprecipitationincreasesarelarge,indicatingpo-
lation.Wehypothesisethatifanincreaseinprecipitationin tentialfutureincreasesinfloodingassociatedwithcyclones.
warmerclimatesweretofeedback,viadiabaticheatingand
potentialvorticityanomalies,ontothedynamicalintensityof
theETCs,precipitationandvorticitywouldincreaseatsimi-
larrates,andhencetheslopeofthelinearregressionlinebe-
tween precipitation and vorticity would remain similar. Our
resultsindicateeitherthatthereisnofeedbackorthatthein-
PublishedbyCopernicusPublicationsonbehalfoftheEuropeanGeosciencesUnion.

568 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
1 Introduction DaiandNie,2020).FieldandWood(2007)combinedsatel-
liteobservationswithmeansealevelpressure(MSLP)from
Extra-tropicalcyclones(ETCs)constitutealargepartofthe reanalysistounderstandhowETCprecipitationandcloudi-
Earth’scirculation,transportingenergyandmomentumpole- nessdependonETCstrengthandmoistureavailability.They
ward. These weather systems are also the dominant cause foundthatprecipitationincreaseswithbothETCstrength(as
of day-to-day weather in the mid-latitudes. Hawcroft et al. quantifiedbythemeansurfacewindspeedwithina2000km
(2012) showed that the majority of precipitation (70%– radius)andmoisturebutthatthedeepestcyclonesintermsof
80%) in the mid-latitude storm track regions is associated MSLPdonotproducethemostprecipitationdespitehaving
with ETCs, and Pfahl and Wernli (2012) found that ETCs thestrongestwinds.PfahlandSprenger(2016),usingERA-
are responsible for a high percentage of precipitation ex- Interim reanalysis data, also found a strong relationship be-
tremes. Some, but not all, ETCs can have extremely large tween ETC strength (in terms of wind speeds) and precipi-
amountsofprecipitationassociatedwiththemwhichcanlead tationbutfurthernotedthatthisrelationshipvariedstrongly
to flooding and thus to a significant societal and economic withlatitude,withaveryweakrelationshipathighlatitudes,
impact. Therefore, it is important to understand what con- duetolimitationsinmoistureavailability.Theyalsoshowed
trols the amount of precipitation related to ETCs and how thattherelationshipbetweenprecipitationandintensitywas
ETC-relatedprecipitationmaychangeinthefuture. strongestwhenlookingattheprecipitationfrom12hpriorto
ETCs have been extensively studied over the past cen- themaximumintensity.Thisresult,thatmaximumprecipita-
turystartingfromBjerknes(1919)andBjerknesandSolberg tionoccursbeforethemaximumintensityoftheETC,issup-
(1922), who developed the well-know Norwegian model, a portedbyBoothetal.(2018),whofoundthatthemaximum
conceptual model of the structure of ETCs. Already from vorticity of an ETC occurred after the precipitation maxi-
these early studies it has been known that precipitation de- muminmostETCs(>70%),whileonly20%ofETCshad
velopsinETCsinregionswhereairisascending,whichtyp- their precipitation maximum after the vorticity maximum.
icallyoccursalongthefrontalzones.Climatologicalstudies Owenetal.(2021)focusedonextremes(includingbothpre-
oftheoccurrenceoffrontshavefoundthatinthemainstorm cipitationandwindsandtheirco-occurrence)andfoundthat
trackregions,upto80%ofthetotalprecipitationcanbeas- ETCsassociatedwiththeextremestendtohavehigherinten-
sociated with fronts (Catto et al., 2012) and an even larger sitythanthosethatarenotassociatedwithextremes.
proportionofextremeprecipitationevents(CattoandPfahl, Associated with the increased moisture due to the higher
2013).Theseexactproportionsdependonthefrontidentifi- temperatures projected in the future, precipitation intensity
cationanddatasetusedbutindicatetheimportanceofthese (especially that of extremes) is expected to increase (Allen
features. andIngram,2002).Manystudieshaveshownthisisalsothe
The warm conveyor belt (WCB), a coherent ascending caseforETC-relatedprecipitation.Forexample,Zhangand
airstreamwhichoriginatesintheboundarylayerofthewarm Colle (2018) analysed ETCs in eastern North America and
sector of ETCs, was first described by Browning (1971), thewesternAtlanticin10modelsfromphase5oftheCou-
Harrold (1973), and Carlson (1980) and is also known to pledModelIntercomparisonProject(CMIP5)andfoundthat
be a source of precipitation in ETCs. Using a climatology ETC-related precipitation increases by up to 30% between
of WCBs developed based on the ERA-Interim reanalysis thehistoricalandfutureclimatesimulations.Michaelisetal.
dataset (Madonna et al., 2014), Pfahl et al. (2014) showed (2017),inregionalpseudo-global-warmingexperiments,also
that 70%–80% of precipitation extremes in some regions foundETCprecipitationincreasesinawarmerclimate,while
are associated with the WCB airstream. This feature, when Hawcroftetal.(2018)showedthatthenumberofETCsasso-
associated with fronts, also gives a higher chance of an ex- ciatedwithextremeprecipitationmaytriplebytheendofthe
treme precipitation event (Catto et al., 2015). Ascent in the century.Kodamaetal.(2019)performedtwohigh-resolution
warm conveyor belt is forced by warm air advection but is global climate model simulations – one current climate and
alsoenhancedbydiabaticheating.Thisdiabaticheatingcan onefutureclimatesimulation–andfoundthatprecipitation
also influence the cyclone dynamics via the production of associated with intense ETCs increases at 7%/1K warm-
alow-levelpositivepotentialvorticity(PV)anomaly,which ing, whereas when all ETCs are considered, precipitation
develops below the localised maximum in diabatic heating increases only at 3%/1K warming. Similar results were
(Stoelinga,1996).ThispositivePVanomalycanpotentially alsofoundbyReboitaetal.(2021)forSouthernHemisphere
feed back onto the intensity of the ETC by enhancing the ETCs when regional climate model simulations were anal-
low-level circulation. Binder et al. (2016) used a classifica- ysed.YettellaandKay(2017)analyseda30-memberinitial
tionmethodtoshowthattheWCBflowcancontributetothe condition climate model ensemble and found that most of
rapidintensificationofextra-tropicalcyclonesbutonlyinsit- the increase in the intensity of precipitation associated with
uationswherethereisstrongenoughupper-levelforcing. ETCs resulted from the thermodynamic effect of increased
ETCintensityandtheassociatedprecipitationarestrongly temperatureratherthanadynamicaleffect.Studieshavealso
linked. We expect to see more precipitation in strong ETCs suggested that, as well as an increase in ETC precipitation
wherethereisstrongforcingforascent(Milradetal.,2010; intensity in the future, the size of the cyclones and the area
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 569
of the precipitation may increase (Reboita et al., 2021; Dai andwewilltakearelatedapproachbyapplyingaclustering
andNie,2022) method to the precipitation structure to group ETCs. Using
Climatechangeisexpectedtohaveanimpactontheinten- idealisedaqua-planetsimulationsofacontrolclimate,auni-
sityofETCsthemselves.Onereasonforthisisthepredicted form global warming scenario, and an Arctic amplification
changes to the large-scale atmospheric state and in partic- scenario, we will determine potential future changes in the
ular changes to baroclinicity. Arctic amplification reduces cyclonesandassociatedprecipitationinthedifferentcyclone
| the low-level | temperature | gradient |     | and thus | baroclinicity, |     | clusters. |     |     |     |     |     |     |
| ------------- | ----------- | -------- | --- | -------- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
whereastropicalupper-tropospherewarmingactstoincrease The questions we aim to address in this research are the
| theupper-leveltemperaturegradientandbaroclinicity.Inad- |                 |     |             |     |         |             | following: |     |     |     |     |     |     |
| ------------------------------------------------------- | --------------- | --- | ----------- | --- | ------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
| dition, changes                                         | to the vertical |     | temperature |     | profile | (stability) |            |     |     |     |     |     |     |
1. Whatistherelationshipbetweenprecipitationintensity
canalsoimpactbaroclinicity.Furthermore,inawarmercli-
andcycloneintensityinthecurrentandpotentialfuture
mate,forcingfromlatentheatreleaseisprojectedtoincrease
| and potentially | may increase |     | the intensity |     | of ETCs | along- | climates? |     |     |     |     |     |     |
| --------------- | ------------ | --- | ------------- | --- | ------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
sidetheincreaseinprecipitation(Sinclairetal.,2020;Binder
|     |     |     |     |     |     |     | 2. How | does the | relationship | between |     | cyclone | precipita- |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------------ | ------- | --- | ------- | ---------- |
etal.,2023).However,thenumberofETCsofagiveninten-
|            |               |              |     |     |            |        | tion   | and cyclone | intensity | depend |     | on the type | of cy- |
| ---------- | ------------- | ------------ | --- | --- | ---------- | ------ | ------ | ----------- | --------- | ------ | --- | ----------- | ------ |
| sity (i.e. | the frequency | distribution | of  | ETC | intensity) | is not | clone? |             |           |        |     |             |        |
projectedtochangemuch(PriestleyandCatto,2022)evenin
high-emissions scenarios, indicating either that the diabatic 3. Howdoesthevariabilityinprecipitationstructuresasso-
feedback is weak or that the combination of factors listed ciatedwithextra-tropicalcycloneschangeinthefuture
above impact the number of ETCs in a different direction. climate, and are certain types of cyclones more or less
| In contrast, | the extreme            | ETCs | are projected |      | to increase | in  | common? |             |     |           |        |          |      |
| ------------ | ---------------------- | ---- | ------------- | ---- | ----------- | --- | ------- | ----------- | --- | --------- | ------ | -------- | ---- |
| intensity    | in terms of vorticity, |      | maximum       | wind | speeds,     | and |         |             |     |           |        |          |      |
|              |                        |      |               |      |             |     | Section | 2 describes | the | numerical | model, | OpenIFS, | that |
thefootprintofhighwindspeeds(Pfahletal.,2015;Sinclair
|     |     |     |     |     |     |     | we use and | the setup | of the | simulations |     | that are | performed. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | ----------- | --- | -------- | ---------- |
etal.,2020;PriestleyandCatto,2022;Dolores-Tesillosetal.,
|                   |      |         |          |      |         |        | The methods | used | to analyse | the | output | from these | simula- |
| ----------------- | ---- | ------- | -------- | ---- | ------- | ------ | ----------- | ---- | ---------- | --- | ------ | ---------- | ------- |
| 2022), suggesting | that | not all | types of | ETCs | respond | in the |             |      |            |     |        |            |         |
samemannertoclimatechange. tionsaredescribedinSect.3.InSect.4,thebasicclimatol-
ogyofthethreesimulationsisdescribedbeforetherelation-
Idealisedmodelshavebeenusedextensivelyinthepastto
shipbetweenprecipitationandcycloneintensityisdiscussed
understandcyclonedynamics(SimmonsandHoskins,1978;
inSect.5.AnanalysisofthedifferenttypesofETCsthatoc-
| Thorncroft | et al., 1993) | and, | more | recently, | to understand |     |     |     |     |     |     |     |     |
| ---------- | ------------- | ---- | ---- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
curispresentedinSect.6andhowtherelationshipbetween
ETCdynamics,precipitation,andintensityinawarmingcli-
mate. Two idealised modelling approaches have been used precipitationandETCintensitydependsonthetypeofETC
ispresentedinSect.7.ConclusionsarepresentedinSect.8.
| to study            | how the ETCs | respond     | to  | a warmer | climate: | the     |     |     |     |     |     |     |     |
| ------------------- | ------------ | ----------- | --- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| first is baroclinic | life cycle   | experiments |     | (e.g.    | Boutle   | et al., |     |     |     |     |     |     |     |
2011;Kirshbaumetal.,2018;Rantanenetal.,2019)andthe 2 Modelsimulations
secondisaqua-planetsimulations(e.g.Kodamaetal.,2014;
Pfahletal.,2015;Sinclairetal.,2020).Bothmodellingap-
2.1 OpenIFS
proachesofferadvantagesoverfullycomplexmodels,being
able to better identify physical mechanisms for changes in The numerical simulations are performed with the state-of-
ETCs.Inthisstudyweemployanaqua-planetmodelconfig- the-artglobalnumericalweatherpredictionmodel,OpenIFS
uration and include full physics, as previously used in Sin- Cy43r3v1. OpenIFS is a version of the Integrated Forecast
clairetal.(2020).ThissetupallowsforafullrangeofETCs System(IFS) usedoperationallyat theEuropean Centrefor
to develop (e.g. Catto, 2016), while removing complexities MediumRangeWeatherForecasts(ECMWF).Thedynami-
associatedwithland–seacontrastsoftemperature,moisture, cal core and the physical parameterisations in OpenIFS are
andsurfacedrag. identicaltothoseinthesamecycleofthefullIFS.However,
ItisclearthatETC-relatedprecipitationisprojectedtoin- unliketheIFS,OpenIFSdoesnotincludethedataassimila-
crease in intensity in the future. A question remains as to tionpackagenorisitcoupledtoanoceanmodel.OpenIFSis
whether this will impact the dynamical strength of the cy- availableunderlicencetoacademicandresearchinstitutions.
clones.Inotherwords,itisunclearhowtherelationshipbe- TheequivalentversionoftheIFS(Cy43r3)totheversionof
tweenprecipitationandintensitymightchangeinthefuture. OpenIFSusedinthesesimulationswasoperationalbetween
Furthermore, there are many different dynamical structures July 2017 and June 2018. The complete documentation of
of extra-tropical cyclones (e.g. Evans et al., 1994; Sinclair IFSCy43r3isavailableonlineathttps://www.ecmwf.int/en/
andRevell,2000;Catto,2016,2018;Binderetal.,2023),and publications/ifs-documentation(lastaccess:9June2023).
howthisrelationshipdependsonthetypeofETChasyetto
bequantified.Boothetal.(2018)usedasubsettingmethodto
groupsimilarcyclonesaccordingtotheirprecipitablewater,
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

570 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
2.2 OpenIFSsimulations
| The numerical |             | experiments |                   | conducted      | in            | this study | utilise  |     |     |     |     |
| ------------- | ----------- | ----------- | ----------------- | -------------- | ------------- | ---------- | -------- | --- | --- | --- | --- |
| OpenIFS       | configured  |             | as an aqua-planet |                | in which      | there      | is no    |     |     |     |     |
| land and      | the surface |             | of the            | Earth          | is completely |            | covered  |     |     |     |     |
| by ocean.     | Three       | simulations |                   | are performed, |               | and all    | are ini- |     |     |     |     |
| tialised      | from a      | real        | atmospheric       | state          | selected      | at         | random.  |     |     |     |     |
However,somemodificationsarerequiredtomaketheinitial
| conditions | suitable    | for          | an aqua-planet |         | simulation. |             | First, the |     |     |     |     |
| ---------- | ----------- | ------------ | -------------- | ------- | ----------- | ----------- | ---------- | --- | --- | --- | --- |
| land–sea   | mask        | is modified  | to             | be zero | (ocean)     | everywhere, |            |     |     |     |     |
| and the    | surface     | geopotential |                | is also | set to      | zero. The   | atmo-      |     |     |     |     |
| spheric    | states are  | then         | extrapolated   |         | to the new, | flat        | surface.   |     |     |     |     |
| Surface    | pressure    | is also      | adjusted       |         | to reflect  | the removal | of         |     |     |     |     |
| surface    | topography. | All          | simulations    |         | have a      | diurnal     | cycle in   |     |     |     |     |
| incoming   | radiation   | but          | no annual      | cycle.  | During      | the         | simula-    |     |     |     |     |
Figure1.Seasurfacetemperaturedistributionasafunctionoflat-
tionstheincomingsolarradiationisfixedattheequinoctial itudeforthethreeexperiments.Thecontrolsimulationisshownin
valueandisthussymmetricabouttheEquator.Thesimula- purplewhichhastheQObsSSTdistribution,SST4(orange)isuni-
tionsareallrunfor11years,andthefirstyearofsimulation formwarming,andAA(dashedgreen)iswarmedpoles.
| is discarded | toaccount |     | for model | spin-up.Output |     |     | fields are |     |     |     |     |
| ------------ | --------- | --- | --------- | -------------- | --- | --- | ---------- | --- | --- | --- | --- |
writtenevery6h.Thesimulationsareallrunatahorizontal
resolutionofT255(approximately80km)andhave60model those previous simulations. Firstly, the version of OpenIFS
differs(Cy43r3versusCy40r1);secondly,thehorizontalres-
levelsbetweenthesurfaceandthemodeltopat0.1hPa.
The three aqua-planet simulations performed only differ olutiondiffers(T255versusT159);andlastly,Sinclairetal.
(2020)didnotmodifythesurfacepressuretoaccountforthe
fromeachotherintermsoftheirprescribedseasurfacetem-
perature(SST)distributions(Fig.1).Ineachexperiment,the removal of topography from the randomly selected real ini-
SST distribution is analytically specified as only a function tialconditionsandthereforehavelowerclimatologicalvalues
ofsurfacepressurethaninthisstudy.
oflatitude,andtheSSTsareheldconstantthroughthesimu-
lation.Thesimulationsrepresentacontrol,acaseofuniform
warming,andacaseofpolaramplification.Thecontrolsim-
|             |          |      |          |              |          |             |          | 3 Analysismethods   |     |     |     |
| ----------- | -------- | ---- | -------- | ------------ | -------- | ----------- | -------- | ------------------- | --- | --- | --- |
| ulation     | uses the | QObs | SST      | distribution | proposed |             | by Neale |                     |     |     |     |
| and Hoskins | (2000).  |      | The QObs | SST          | profile  | is a simple | an-      |                     |     |     |     |
|             |          |      |          |              |          |             |          | 3.1 Cyclonetracking |     |     |     |
alyticalfunctionoflatitudewhichhasamaximumof27◦C
| on the Equator |     | and reaches |     | 0◦C at | 60◦N and | which | Neale |                     |                |          |                |
| -------------- | --- | ----------- | --- | ------ | -------- | ----- | ----- | ------------------- | -------------- | -------- | -------------- |
|                |     |             |     |        |          |       |       | In all experiments, | extra-tropical | cyclones | (ETCs) are ob- |
andHoskins(2000)stateresemblestheobservedzonal-mean jectively identified and tracked using TRACK (Hodges,
SSTdistributions.TheSSTdistributionintheuniformwarm- 1994,1995).ETCsareidentifiedaslocalisedmaximainthe
ingsimulation(referredtoasSST4)istheQObsdistribution
850hParelativevorticityfieldtruncatedtoT42spectralres-
butwarmedeverywhereby4K.TheSST4experimentismo- olution.Wavenumberssmallerthanwavenumber5arealso
tivated by previous aqua-planet simulations with the same settozerotoremoveplanetary-scalefeatures.The6-hourly
fixedSSTforcingthathavebeenperformedaspartofCMIP5 input data are used to identify the ETC tracks. Initially, all
(aqua4K;Tayloretal.,2012)andCMIP6(amip-p4k;Eyring ETCs in the Northern Hemisphere are identified; however,
etal.,2016).Thepolaramplificationsimulation(referredto
|     |     |     |     |     |     |     |     | to ensure | that only synoptic-scale | and mobile | ETCs are re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------------ | ---------- | ------------ |
45◦S
as AA) uses the QObs SST distribution between and tainedforanalysis,weonlyretainETCtracksthatlastforat
45◦N.PolewardsoftheselatitudestheSSTsaresetto5◦C. least 2d and travel 1000km. To remove weak ETCs, tracks
| This choice | is  | made to | test the | impact | of warming |     | the high |                |            |                    |              |
| ----------- | --- | ------- | -------- | ------ | ---------- | --- | -------- | -------------- | ---------- | ------------------ | ------------ |
|             |     |         |          |        |            |     |          | with a maximum | T42 850hPa | relative vorticity | of less than |
latitudes without altering the tropics, and hence this exper- 1×10−5s−1arealsoexcludedfromtheanalysis.Similarfil-
| iment is | not intended |     | to represent |     | reality. | Rantanen | et al. |            |                 |                    |             |
| -------- | ------------ | --- | ------------ | --- | -------- | -------- | ------ | ---------- | --------------- | ------------------ | ----------- |
|          |              |     |              |     |          |          |        | tering has | been applied in | many other studies | that employ |
(2022)show,usingreanalysisdatasets,thatlargepartsofthe TRACK (e.g. Dacre and Gray, 2009; Hodges et al., 2011;
Arcticarewarmingatarateof0.75Kperdecade(evaluated Priestley et al., 2020). In addition to these standard filters,
| between | 1979–2021), |     | and locally |     | some regions | are | warm- |     |     |     |     |
| ------- | ----------- | --- | ----------- | --- | ------------ | --- | ----- | --- | --- | --- | --- |
wealsorequirethatETCsreachtheirmaximumvorticityat
ing faster than 1K per decade. Therefore, our 5K increase a latitude north of 30◦N and exist 24h before the time of
| is consistent | with | the | amount | of warming |     | expected | over a |     |     |     |     |
| ------------- | ---- | --- | ------ | ---------- | --- | -------- | ------ | --- | --- | --- | --- |
maximumintensity.
50–60-yearperiodandthusisnotunreasonablylarge.
| Similar | aqua-planet |     | experiments |     | with OpenIFS |     | have pre- |     |     |     |     |
| ------- | ----------- | --- | ----------- | --- | ------------ | --- | --------- | --- | --- | --- | --- |
viouslybeenpresentedbySinclairetal.(2020).Afewminor
differencesexistbetweenthesimulationspresentedhereand
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 571
3.2 Cyclonecomposites ETCsinHawcroftetal.(2012).However,todeterminehow
sensitivetheresultsaretothischoiceofradius,theclustering
FollowingthesamemethodasCattoetal.(2010)andDacre wasrepeatedbutwithvariousdifferentradii(4.5,8,12,and
et al. (2012), composites of a range of meteorological vari- 18◦)oftheETCcentre,andtheseresultsarediscussedinthe
ables are computed for the ETCs at different offset times SupplementandshowninFig.S1.
relative to the time of maximum vorticity (t =0h). Nega- As we want to allocate each ETC to a cluster based on
tive offset times indicate that the composite is valid before their spatial distribution of precipitation and not on the ab-
the time of maximum intensity and hence when the ETC is soluteprecipitationvalues,weusequantilemapping(scikit-
intensifying. In contrast, positive offset times mean that the learn’s quantile transform function; Pedregosa et al., 2011)
compositeisvalidduringthedecayingpartoftheETClife- tonormalisetheprecipitationfieldofeachindividualETCto
cycle. The first step in creating the composites is to select a uniform distribution. In practice, this means that for each
which ETCs to include in the composite. Previous studies ETC,eachgridcellonthepolargridisgivenavaluebetween
have often selected the strongest 50–200ETCs (e.g. Catto 0and1,andallvalues(foreachindividualETC)representa
etal.,2010;Flaounasetal.,2015;Vesseyetal.,2022)orhave uniform distribution. Quantile mapping is robust to outliers
selectedthesubsetofETCstobecompositedbyconsidering and also performs well with sparse and semi-sparse arrays.
theirgeographiclocation.Herewecreatecompositesofdif- Althoughwedonotconsidertheabsoluteamountofprecip-
ferenttypesofETCsbasedontheirprecipitationpatternsas itationwhenclusteringtheETCs,inoursubsequentanalysis
identified by k-means clustering (more details in Sect. 3.3). wedocomputeandanalysetheETCtotalprecipitation(see
The second step in creating the composites is to regrid the Sect.3.4).
meteorologicalfieldfromtheregularlatitude–longitudegrid Adisadvantageofk-meansclusteringisthatthenumberof
thattheOpenIFSoutputisontoasphericalgridcentredon clustersisnotautomaticallyselectedbythealgorithmandin-
the cyclone centre (the location of the maximum T42 vor- steadmustbespecifiedinadvancebytheuser.Furthermore,
ticity obtained from TRACK). The spherical grid has a ra- it most situations there is no clear, ideal number of clus-
diusof18◦ andconsistsof40gridpointsintheradialdirec- ters.Usually,theoptimalnumberofclustersisdeterminedby
tion and 360 grid points in the angular direction. After the tryinganumberofdifferentoptionsandcalculatingvarious
meteorological fields have been interpolated onto this grid, measuresthatquantifyhowsimilaranelement(i.e.oneETC
these fields are then rotated so that all ETCs are travelling inourcase)istoitsownclustercomparedtootherclusters.
to the east. Finally to obtain the ETC composite, the mete- Wetested2to19clustersandforeachclusteringcomputed
orological values on the radial grid at each offset time are thesilhouettescore(Rousseeuw,1987).Thesilhouettescore
averaged. Thus, the composite extra-tropical cyclone is the ranges from −1 to +1 where large positive values indicate
simplearithmeticmeanoftheselectedETCs. that the element is very well matched to its cluster. In con-
Compared to previous studies, the composites analysed trast,lowornegativevaluesmeanthatanelementispoorly
here are produced by averaging a much larger number of matchedorpotentiallymis-classified.Thesilhouettescoreis
ETCs (e.g. >2000). This may result in a large degree of computed for each element (each ETC), and then the final
smoothing if there is large variability between the ETCs in silhouettescoreistheaverageofallelements.
theselectedpopulation.Therefore,weinvestigatedhowsen- Figure S2 shows the silhouette score for all three experi-
sitive the results of the composite mean precipitation are to mentsasafunctionofclusternumber.Basedontheseresults,
thenumberofETCsincludedineachcompositebycreating weusefourclusters.Asmallernumberofclusters(e.g.two)
clusters with sub-samples of ETCs. Overall, the main con- giveshigherscores,butlittlemeaningfulinformationcanbe
clusions are not strongly sensitive to the number of ETCs obtainedfromonlytwoclusters.Wealsoselectk=4,since,
includedincomposites(notshown). to enable us to more easily compare the three experiments,
we wanted to have the same number of clusters in each ex-
3.3 Cycloneclustering periment,andfork=4,allexperimentsstillhavemoderate
silhouettescoresandtheAAexperimentevenexhibitsalo-
K-means clustering (Lloyd, 1982) is used to separate the calisedmaximum.Fork=5,andespeciallyk=6,boththe
ETCsintodifferentgroupswithdifferentprecipitationstruc- control and AA experiments see a reduction in the silhou-
tures. As input to the k-means clustering algorithm, we use ette score, although this is not the case for the SST4 simu-
theregriddedprecipitationfield(convectivepluslarge-scale lation.Inaddition,wealsocomputedtheEuclideandistance
precipitation)withina12◦ radiusoftheETCcentre12hbe- betweeneachindividualETCandthecentroidsofallclusters
forethetimeofmaximumvorticity.Aradiusof12◦ wasse- toensurethatETCsare,onaverage,assignedtothemostap-
lectedas,basedonplottingmanyindividualETCs,thispro- propriate cluster and that the clusters are distinct from each
videdagoodbalancebetweenensuringthatallprecipitation other.AdditionaldetailsareprovidedinSect.S3intheSup-
clearly related to the ETC was included and that precipita- plement.
tion related to another nearby ETC was excluded. It is also
consistent with the radius used to attribute precipitation to
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

572 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Table1.Meantemperature(K)andmeanprecipitation(mmd −1) The zonal and time mean atmospheric state in the con-
fromallexperiments.Valuesareareaaverages,notETCaveraged trol experiment and how it changes in the SST4 and AA
values. experiments are shown in Fig. 2. In the control simula-
tion, the zonal wind has a maximum of 53ms−1 located
Diagnostic Control SST4 AA at 31.2◦N and 175hPa (Fig. 2a), and the Eady growth rate
(Eady,1949),ameasureofbaroclinicity(Fig.2c),hasamax-
Globalmean2mtemperature 286.7 290.8 287.8
Globalmeanprecipitation 3.18 3.63 3.17 imum value of 0.93d−1. Uniform warming (SST4) causes
25–70◦Nmean2mtemperature 280.1 284.2 281.7 the jet to move polewards and upwards (Fig. 2a), indicat-
25–70◦Nmeanprecipitation 2.56 2.90 2.62 ing a lifted tropopause, and causes a decrease in the Eady
growth in the mid-to-upper troposphere on the equatorward
sideofthejetandpolewardof70◦NandS.Thedecreasein
3.4 Precipitationdiagnostic theEadygrowthrateiscausedbyanincreaseintropospheric
stabilityintheseregions(Fig.S5c)ratherthanadecreasein
To enable comparison between thousands of ETCs in each the meridional temperature gradient, which barely changes
experiment, a succinct diagnostic for the ETC precipitation (Fig. S5a). Near the tropopause, there is a vertically orien-
isrequired.ForeachETC,wecomputetheaverageprecipi- tated dipole in how the Eady growth rate responds to uni-
tationrate,P ,whichisdefinedas formwarmingwhichisduetothetropopauseheightincreas-
ave
ingandthusthestabilitychanging.PolarwarmingintheAA
P = (cid:88) m P A i , (1) simulations causes the jet to move equatorwards (Fig. 2b).
ave i A TheresponseoftheEadygrowthratetopolarwarmingisa
i=1 T
decrease in the low-to-middle troposphere on the poleward
where P is the precipitation rate in each grid cell i and side of the jet and an increase in the mid-to-upper tropo-
i
m is the number of grid cells within a given radius of the sphere at high latitudes. The low-level decrease is due to
cyclone centre on the spherical grid and where P exceeds a decrease in the meridional potential temperature gradient
i
1mm(6h)−1. A is the total area covered by m grid cells, (Fig. S5b), whereas the increase at high latitudes is related
T
and A is the area of each individual grid cell i. Hence, we toadecreaseinstabilityinthepolaratmosphere(Fig.S5d).
i
averagetheprecipitationratebutonlyovergridcellswhere Thus,basedonthechangestothezonalandtimemeanEady
precipitationisactuallyoccurring. growthrate,weakerorfewerETCscouldbeexpectedinthe
SST4 simulation, whereas a more complex picture emerges
intheAAsimulation.FewerorweakerETCscouldbeantic-
4 Climatologyofthethreeexperiments ipatedinthemainstormtrackregion,butmore,orstronger,
ETCsmaybeabletodevelopathighlatitudes.
Theglobalmean2mtemperatureandprecipitation,averaged Basic statistics of the characteristics of the objectively
over the 10 years of simulation, for each simulation is pre- identified ETCs are shown in Table 2. There are 578 fewer
sentedinTable1.Thecontrolsimulationhasaglobalmean ETCsidentifiedintheSST4simulationcomparedtothecon-
2mtemperatureof286.7K(13.5◦C),whichissimilartothat trolsimulation;however,thedecreaseisnotstatisticallysig-
oftherealEarth(globalmeansurfacetemperatureof288K; nificant at the 95% confidence level when a t test is per-
Hartmann, 2015), and a global mean precipitation rate of formedontheyearlytotals(N =10)assumingunequalvari-
3.18mmd−1, which is 20% larger than the real Earth (av- ance. In contrast, 440 more ETCs are identified in the AA
erageprecipitationof2.66mmd−1;Hartmann,2015)dueto simulation than in the control, and this difference is statis-
the absence of land in these simulations. The SST4 simula- tically significant at the 95% level. Notably, there is more
tionis4.1Kwarmerthanthecontrolsimulationandalsohas year-to-year variation in the number of ETCs in the SST4
a larger global mean precipitation rate (3.63mmd−1) than simulationcomparedtoboththecontrolandAAsimulations
thecontrolsimulation.Thisprecipitationincreaseequatesto (Table2).
anincreaseof3.5%perdegreeofwarming,whichisslightly Themeanandmedianvaluesofthemaximumrelativevor-
larger than the most likely range of 2%–3% found in re- ticity of the ETCs in the control and SST4 simulations are
cent climate model simulations (Douville et al., 2021). The very similar (Table 2). The full distributions (Fig. 3a) are
AA simulation is 1.1K warmer than the control simulation, also very similar and do not differ statistically when a two-
and when global precipitation is considered, there is a very sided t test is performed, despite the reduction in the Eady
slight decrease (0.01mmd−1) compared to the control sim- growthrate.However,theSST4simulationhasabroaderdis-
ulation. However, when only the temperature and precipita- tributionwithbothmoreweakandmorestrongETCs.Inthe
tioninthemid-latitudes(25–70◦N)areconsidered,theAA SST4simulation12.1%ofETCshaveamaximumvorticity
simulationwarmsby1.6Kandtheprecipitationincreasesby exceeding10×10−5s−1,whereasonly10.3%ofETCsex-
0.06mmd−1,equivalenttoanincreaseof1.54%perdegree ceed thisthreshold in thecontrol simulation. Themean and
ofwarming. median maximum relative vorticity of all ETCs in the AA
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 573
Figure2.Zonalandtimemeanfieldsaveragedover10yearsofsimulation.(a)Potentialtemperature(greencontours,contourinterval10K)
andthezonalwindspeed(blackcontours,contourinterval10ms
−1)inthecontrolsimulation.Shadingshowsthedifferenceinthezonal
windspeedbetweenthecontrolandSST4simulations(SST4–control).Panel(b)isthesameas(a)excepttheshadingshowsthedifference
betweenthecontrolandAA.Panel(c)showsthepotentialtemperature(greencontours,contourinterval10K)andtheEadygrowthrate
(black contours, contour interval 0.25d
−1)
in the control simulation. Shading shows the difference in the Eady growth rate between the
controlandSST4simulations.Panel(d)isthesameas(c)exceptthedifferenceisbetweenthecontrolandtheAAexperiments.Notethe
non-linearcolourbars.
simulationissmallerthaninthecontrolsimulation(Table2), Lastly, as the focus of this study is on ETC-related pre-
whichisalsoevidentinthefulldistribution(Fig.3a).Aone- cipitation, we also considered the distributions of the ETC-
sided t test shows that the maximum vorticity values in the averaged precipitation in each simulation (Fig. 3c). In all
AA experiment are statistically significantly weaker than in experiments, there is a localised peak for very weak (1.25–
thecontrolsimulation.Thisisconsistentwiththefewervery 1.5mm(6h)−1)precipitationamounts.Thisispartlybecause
strongETCsintheAAsimulationcomparedtoboththecon- ofthe1mm(6h)−1 thresholdusedintheprecipitationdiag-
trolandSST4simulationsandwiththereductionintheEady nostic(Eq.1).Thislocalisedpeakismorepronouncedinthe
growth rate in the AA simulation compared to the control AA experiment as there are more ETCs with weak precip-
(Fig.2). itation compared to the other two experiments. The control
The genesis and lysis latitudes of the ETCs in each sim- simulation has more ETCs with weak to moderate precipi-
ulation are also considered and in all simulations exhibit tation(2–3mm(6h)−1)thaneithertheSST4orAAsimula-
roughly Gaussian distributions. The genesis and lysis lati- tions,whichwehypothesisemaybeduetothecontrolsim-
tudesofETCsmovepolewardsinSST4comparedtothecon- ulation being the coldest simulation. The SST4 simulation
trol,whereastheoppositebehaviouroccursintheAAsimu- hasmanymoreETCswithprecipitationamountsexceeding
lation(Table2andFig.3b,d).Thesechangesareconsistent 4mm(6h)−1 than in either the control or AA simulations,
withthelatitudinalchangesinthejetstreamposition(Fig.2). which show very similar distributions for heavier precipita-
Furthermore, the same response is found when the median tion amounts. A t test confirms that there is no significant
latitudeofmaximumvorticityisconsidered(Table2). differenceatthe95%levelbetweenthecontrolandAAsim-
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

574 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Figure3.Probabilitydensitydistributionsofthe(a)maximumrelativevorticity(T42values),(b)genesislatitude,(c)averageETCprecip-
itation12hbeforethetimeofmaximumintensity,and(d)lysislatitudeforeachexperiment.Cyclonesareonlyincludediftheyexist24h
◦
beforethetimeofmaximumvorticityandreachtheirmaximumvorticitypolewardof30 N.
ulations in terms of ETC-related precipitation. In contrast, cipitation.AftercontrollingforthedifferencesinETCmax-
t tests show that ETCs in the SST4 experiment have statis- imumvorticity,wefindthattheETCsintheAAsimulation
ticallysignificantlymoreprecipitationassociatedwiththem havestatisticallysignificantly(pvalueof2.21×10−26)more
thanETCsinthecontrolsimulationatthe95%level. precipitationassociatedwiththem:i.e.anETCintheAAex-
The distribution of the maximum vorticity of ETCs dif- periment will have more precipitation than an ETC in the
fers between the three simulations. Therefore, an analysis controlsimulationforthesamemaximumvorticity.
of covariance (ANCOVA) statistical test is applied here to
determineiftheETC-relatedprecipitationdiffersinthedif-
ferent experiments after controlling for a covariate, which 5 Therelationshipbetweenprecipitationandcyclone
in this case is the maximum vorticity of the ETC. This al- intensity
lowsustotestthenullhypothesis,whichisthatETCswith
thesameintensity(measuredintermsoftherelativevortic- Wehypothesisethatifprecipitationincreasesinwarmercli-
ity) have the same amount of precipitation associated with mates and if it were to feed back, via diabatic heating and
themineachexperiment.WhenthecontrolandSST4simu- potential vorticity anomalies, onto the dynamical intensity
lations are compared using ANCOVA, the returned p value of the ETCs, precipitation and vorticity would increase at
is 1.11×10−186, which is less than 0.05 meaning that we similar rates. Hence, if this occurs and is the dominant pro-
canrejectthenullhypothesis.Hence,theANCOVAanalysis cess acting, then the slope of the linear regression line be-
showsthatETCsintheSST4simulationhavemoreprecipi- tweenprecipitationandvorticitywouldremainsimilarinall
tationthanthoseinthecontrolsimulationevenafteraccount- experiments. To test this hypothesis the slope of the linear
ingforthedifferencesinETCmaximumvorticity.Thisisas regressionandthePearson’scorrelationcoefficientbetween
expectedgiventhatthereisnosignificantdifferencebetween themaximumvorticityandETC-relatedprecipitationatdif-
the maximum vorticity distributions yet notable differences ferent offset times relative to the maximum vorticity were
in the precipitation. Of more interest is to apply ANCOVA considered (Table 3). In all experiments, large correlations
tothecontrolandAAsimulations,astheAAsimulationhas and positive slopes occur between maximum intensity and
weaker cyclones yet the same amount of ETC-related pre- precipitation 24, 12, and 0h before the time of maximum
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 575
intensity. The smallest correlations and weakest slopes oc- and AA could result from an increase in precipitation and
cur between maximum vorticity and precipitation 24h after maystillindicateanincreaseddiabaticfeedbackonvorticity.
the time of maximum vorticity. Here we focus on the rela- However,thisdiabaticallydrivenincreaseinmaximumvor-
tionship between maximum vorticity and precipitation 12h ticitymightbemaskedbythecounteractingdecreaseinthe
before the time of maximum vorticity, as shown in Fig. 4, Eadygrowthrateinbothsimulationsrelativetothecontrol,
asthisiswhenthelargestslopesandcorrelationcoefficients similartowhatwasfoundbyBüelerandPfahl(2019).These
occur. The same as Fig. 4, but for precipitation 24 and 0h argumentswillbefurtherexploredinSect.7asitisplausi-
beforethetimeofmaximumvorticity,areshownintheSup- blethatdifferentexplanationsarevalidfordifferenttypesof
plement(Figs.S6andS7). ETC.
BoththeSST4andtheAAsimulationshavesteeperlinear The most spread and thus smallest Pearson’s correlation
regression slopes and thus a stronger dependency between coefficient(0.574)occursintheSST4simulationsuggesting
maximumvorticityandprecipitationthaninthecontrolsim- thatinthissimulation,thedynamicalintensityofthecyclone
ulation. To determine if these slopes are statistically differ- has less control on the amount of precipitation than in the
ent, bootstrapping is applied. Bootstrapping quantifies how othersimulations.Thelargestcorrelationcoefficient(0.635)
much random variation in the slope and intercept values of and hence least spread occurs in the AA simulation. How-
thefittedlinearmodelareduetosmallchangesintheinput ever, in all three simulations the correlation coefficients are
data.Foreachexperiment,were-samplethedata5000times not exceptionally large, and we hypothesise that a large de-
using a sample size equal to that of each original dataset. greeofthespreadiscausedbydifferenttypesofETCshav-
Thus, some pairs of data are represented multiple times in ing different relationships between their intensity and their
any one individual bootstrap sample, while other pairs are precipitation.
notselectedatall.Foreachre-sample,alinearregressionis
madeandtheslopeandinterceptofthismodelarecalculated.
For the control simulation the estimated slopes vary from 6 DifferenttypesofETCsaccordingtotheir
0.261–0.287mm(6h)−1/10−5s−1,fortheSST4simulation
precipitationpatterns
the values are 0.313–0.348mm(6h)−1/10−5s−1, and for
the AA simulation the estimated slopes range from 0.298– Figure5a–dshowthecompositemeantotalprecipitationfor
0.326mm(6h)−1/10−5s−1. The resulting distributions of eachofthefourclustersidentifiedbythek-meansclustering
thecomputedslopes(Fig.S8intheSupplement)foreachex- in the control simulation 12h before the time of maximum
perimentarethencomparedusingastudent’st test,andwe intensity (additional times are shown in Fig. S9). The pre-
findthattheslopesareallstatisticallysignificantlydifferent cipitationpatterndiffersbetweenallfourmeanETCsmean-
atthe99%level.Thus,wecanconcludethatthereisagreater ingthatthek-meansclusteringhassuccessfullyseparatedthe
dependencybetweenprecipitationandmaximumvorticityin ETCsintodifferentclasses.
theSST4experimentthaninboththecontrolortheAAex-
periment and that the AA experiment has a greater depen- 6.1 ETCcompositesinthecontrolsimulation
dencybetweenprecipitationandmaximumvorticitythanthe
control. This meansthat for the sameincrease in maximum ThecompositemeanETCinFig.5ahasalargeareaofvery
vorticity, precipitation increases more in the SST4 and AA heavyprecipitation,exceeding7mm(6h)−1.Thepositionof
experimentscomparedtothecontrolandhencethatourhy- thewarmandcoldfronts,aswellasthewarmsector,isev-
pothesisthatbothprecipitationandvorticitywouldincrease ident in the 850hPa potential temperature (Fig. 6a) and to-
atsimilarratesisnotsupportedbythesimulationresults. talcolumnwatervapour(TCWV;Fig.7a).Theprecipitation
SincetheSST4andAAexperimentsarebothwarmerthan is heaviest near where the warm and cold fronts meet but
thecontrolexperiment,theincreaseinprecipitationcouldbe alsoextendsalongthecoldfrontandpartsofthewarmsec-
explained by the Clausius–Clapeyron relationship between tor.Astrong(maximumvalue1.1PVU),localisedlow-level
temperature and vapour pressure. However, the same per- PVcentreisevidentclosetothecyclonecentrebutpoleward
centageincreaseinprecipitationwouldbeexpectedforETCs andslightlyupstreamoftheheaviestprecipitation(Fig.6a).
ofallintensities,whichisnotthecase.Onepotentialexpla- The convective precipitation (Fig. 7a) is moderate in inten-
nationisthattheincreaseinprecipitationislargerforETCs sityandonlylocatedonthepolewardpartsofthecoldfront.
with stronger dynamical forcing and ascent as they are bet- Hence, this composite mean is subsequently referred to as
terabletoconverttheadditionalmoistureintoprecipitation, the“cold-front”ETC.Thiscold-frontETChasaverynarrow
whichwouldalsoexplaintheincreaseinslope.However,the warm sector which is immediately equatorward of the ETC
increaseinslopecouldalsobeinterpretedastherebeingno centre.SincethisETCismeridionallyextendedyetzonally
(or weak) feedback onto the vorticity of the ETC from the confined,itexhibitssimilaritieswiththeNorwegiancyclone
enhancedprecipitationviaadiabaticallyproducedlow-level model(Bjerknes,1919).Thiscold-frontETCisalsolocated
PVanomalyas,ifthiswasthecase,similarslopeswouldbe directlyintheleft-handexitregionofastrong(>50ms−1)
foundinallexperiments.Finally,theincreasedslopeinSST4 jetstreakwherestrongforcingforascentduetopositivevor-
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

576 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Figure4.Two-dimensionalhistogramsshowingtherelationbetweenmaximumrelativevorticity(T42values)andETC-relatedprecipitation
◦
12hbeforethetimeofmaximumrelativevorticity.Precipitationistheareaaverage,averagedoverallpointswithina12 radiusoftheETC
|     |     |     | −1. |     |     |     |     |     |     |     |     |     | ◦   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
centre where the rain rate exceeds 1mm(6h) Only ETCs which exist at −24h and have their maximum vorticity north of 30 N are
| included(theslopevalueshaveunitsofmm(6h) |     |     | −1/10 | −5s −1). |     |     |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−5s −1,andlatitudesare
Table2.ETCstatisticsfromthecontrol,SST4,andAAexperiments.Relativevorticityvalueshaveunitsof×10
degreesnorth.ETCsareonlyincludediftheyexist24hbeforethetimeofmaximumvorticityandreachtheirmaximumvorticitynorthof
30 ◦ N.
|     | Diagnostic                                |     |     |     |     |           | Control |           | SST4  |           | AA    |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --------- | ------- | --------- | ----- | --------- | ----- | --- | --- |
|     | NumberofETCs                              |     |     |     |     |           | 10669   |           | 10121 |           | 11139 |     |     |
|     | MediannumberofETCsperyear±1SD             |     |     |     |     | 1133±16.4 |         | 1134±24.3 |       | 1160±14.2 |       |     |     |
|     | Meanmaximum850hPavorticity                |     |     |     |     |           | 6.66    |           | 6.66  |           | 6.14  |     |     |
|     | Medianmaximum850hPavorticity              |     |     |     |     |           | 6.53    |           | 6.50  |           | 5.97  |     |     |
|     | Standarddeviationofmaximum850hPavorticity |     |     |     |     |           | 2.56    |           | 2.71  |           | 2.45  |     |     |
−5s −1
|     | Percentageofcycloneswithmaxvorticity>10×10 |     |     |     |     |     | 10.3% |     | 12.1% |     | 6.7% |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ---- | --- | --- |
|     | Mediangenesislatitude                      |     |     |     |     |     | 43.6  |     | 45.3  |     | 42.7 |     |     |
|     | Medianlatitudeofmaximumvorticity           |     |     |     |     |     | 47.3  |     | 49.6  |     | 46.2 |     |     |
|     | Medianlysislatitude                        |     |     |     |     |     | 51.2  |     | 53.1  |     | 49.8 |     |     |
−1/10 −5s −1)andcorrela- surface, which is likely related to the strong ascent in the
Table3.Slopevalues(unitsofmm(6h)
tioncoefficientsbetweenmaximumvorticity(T42values)andETC warmconveyorbelt(Fig.8a)andthediabaticerosionofPV
precipitationatdifferentoffsettimesforeachexperiment. downstream.The315KIPVpatternalsoshowsthisETCis
wrappedupinacyclonicmanner.
Control SST4 AA Theprecipitationpatternassociatedwiththesecondiden-
|            |             |             |         |       | tified | ETC       | is of      | moderate | intensity |          | (up to | 3.5mm(6h)−1) |           |
| ---------- | ----------- | ----------- | ------- | ----- | ------ | --------- | ---------- | -------- | --------- | -------- | ------ | ------------ | --------- |
| Offsettime | Slope r     | Slope       | r Slope | r     |        |           |            |          |           |          |        |              |           |
|            |             |             |         |       | and    | is mainly | associated |          | with      | the warm | front, | a            | bent-back |
| −72h       | 0.204 0.363 | 0.241 0.352 | 0.202   | 0.352 |        |           |            |          |           |          |        |              |           |
warmfront(whichhooksaroundthepolewardandupstream
−48h
0.247 0.474 0.290 0.459 0.263 0.526 sideoftheETCcentre),andthewarmsector(Fig.5b).Thus,
−24h
|      | 0.261 0.566 | 0.319 0.561, | 0.298 | 0.615 |       |           |            |             |     |             |       |                 |      |
| ---- | ----------- | ------------ | ----- | ----- | ----- | --------- | ---------- | ----------- | --- | ----------- | ----- | --------------- | ---- |
|      |             |              |       |       | this  | composite | is         | hereinafter |     | referred    | to as | the “warm-front |      |
| −12h | 0.275 0.586 | 0.331 0.574  | 0.311 | 0.635 |       |           |            |             |     |             |       |                 |      |
|      |             |              |       |       | ETC”. | The       | warm-front |             | ETC | has a broad | warm  | sector,         | evi- |
| 0h   | 0.227 0.504 | 0.258 0.483  | 0.254 | 0.561 |       |           |            |             |     |             |       |                 |      |
+24h 0.108 0.282 0.121 0.278 0.129 0.354 dentinboththe850hPapotentialtemperature(Fig.6b)and
|     |     |     |     |     | TCWV |         | (Fig. 7b), | which     | is shifted | well    | downstream |         | of the   |
| --- | --- | --- | --- | --- | ---- | ------- | ---------- | --------- | ---------- | ------- | ---------- | ------- | -------- |
|     |     |     |     |     | ETC  | centre. | A          | low-level | PV         | maximum | is         | evident | with the |
largestvalues(0.91PVU)closetotheETCcentreandmod-
|                  |                  |          |             |     | erate | values | extending |     | downstream |     | along | the warm | front. |
| ---------------- | ---------------- | -------- | ----------- | --- | ----- | ------ | --------- | --- | ---------- | --- | ----- | -------- | ------ |
| ticity advection | can be expected. | A strong | upper-level | PV  |       |        |           |     |            |     |       |          |        |
Thestrongestascent(Fig.8b)isco-locatedwiththeheaviest
| anomaly | visible in the 315K | isentropic | potential | vorticity |     |     |     |     |     |     |     |     |     |
| ------- | ------------------- | ---------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
precipitationonthewarmfront.Verylittle(<1mm(6h)−1)
| (IPV; Fig. | 8a) is also present | immediately | upstream | of the |            |     |               |     |               |     |      |           |     |
| ---------- | ------------------- | ----------- | -------- | ------ | ---------- | --- | ------------- | --- | ------------- | --- | ---- | --------- | --- |
|            |                     |             |          |        | convective |     | precipitation |     | is associated |     | with | this mean | ETC |
ETCcentre.Consequently,thismeanETCisastrongsystem
with a minimum MSLP of 978hPa (Fig. 8a). Downstream (Fig.7b).The850hPapotentialtemperature(Fig.6b)shows
thatboththewarmandcoldfrontshavesimilartemperature
oftheETCcentre,therearelowvaluesofIPVonthe315K
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 577
Figure5.Compositemeanofthetotalprecipitation(shading,mm/6h)andthemeansealevelpressure(greycontours,every4hPa)12h
beforethetimeofthemaximumvorticity.Differentcolumnsshowdifferentclusters,anddifferentrowsshowdifferentexperiments.
gradients. The zonally broad nature of this mean ETC sug- only 10gkg−1 in the warm-front ETC. In agreement with
geststhatitresemblestheShapiro–Keyserconceptualmodel the increased moisture, this ETC has more convective pre-
(Shapiro and Keyser, 1990). Similar to the cold-front ETC, cipitation than the warm-front ETC. This ETC also differs
thewarm-frontETC isalsolocatedonthe polewardsideof fromthewarm-andcold-frontETCsinthatitdoesnothave
a jet streak. However, this ETC is not directly in the left- alargelow-pressurecentreandonlyasmall-scaleclosedcir-
handexitregionbutislocated10◦(ontherotatedpolargrid) culation.Furthermore,atupperlevelsthisETChasaweaker
poleward of the 45ms−1 jet streak (Fig. 8b), which likely IPV anomaly and is less cyclonically wrapped up than the
explainstheweakerverticalmotionandprecipitationassoci- other two ETCs, remaining more of an open wave at upper
atedwiththisETC.ThisETCalsohasastrongIPVanomaly levels.Thisweakerupper-levelforcingmayexplainwhythe
at upper levels and further shows signs of cyclonic wave MSLPisnotverylow.
breaking. The precipitation pattern of the fourth and last ETC type
The precipitation associated with the third type of ETC isshown inFig. 5d.ThisETC differsconsiderably fromall
identifiedbythek-meansclusteringisshowninFig.5c.This other ETCs. Firstly, it is much weaker in terms of vertical
ETCisalsolocatedintheleft-handexitregionofajetstreak, motion(Fig.8d)thanallotherETCs,althoughaclosedcircu-
but the jet streak is weaker than those associated with ei- lationisevidentwithaminimumMSLPof991hPa(whichis
ther the warm-front or cold-front ETC (Fig. 8c). The pre- almostthesameminimumMSLPasseeninthecentreETC).
cipitation associated with this ETC has a small spatial ex- Secondly, this weak ETC is not located in the jet exit but
tent and is mainly focused on the ETC centre. Therefore, ratherislocatedfarpolewardofthejetstreamanddoesnot
thiscompositemeanissubsequentlyreferredtoasthe“cen- haveapronouncedupper-levelIPVanomalyupstreamofthe
tre” ETC. Despite the weaker jet streak and high minimum ETCcentre.Thirdly,thereisonlyaveryweaklow-levelPV
MSLP (991hPa), the centre ETC has heavier precipitation maximum co-located with the ETC centre (Fig. 6d). Lastly,
andstrongerascentthanthewarm-frontETC,yetaslightly this ETC is located in a cold and dry air mass; the TCWV
weaker (0.85PVU) low-level PV maximum (Fig. 6c). The values near the ETC centre are around 7gkg−1 (Fig. 7d)
increasedprecipitationislikelyexplainedbythemoisterair andthe850hPatemperaturevaluesare278K(Fig.6d).The
advectedtowardsthecentreofthisETC:theTCWVvalues total and convective precipitation associated with this ETC
reach 13gkg−1 in the ETC centre in this small cyclone but are also much weaker than in all other mean ETCs. There-
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

578 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Figure 6. Composite mean of the 900–700hPa layer averaged potential vorticity (shading, PVU) and the 850hPa potential temperature
(black contours,every 2K) 12hbefore thetime of themaximum vorticity.Different columnsshow differentclusters, and differentrows
showdifferentexperiments.
fore, this composite mean issubsequently referred to as the The centre ETCs in the control simulation have statisti-
“weak”ETC. cally significantly more precipitation associated with them
So far, only the mean structure of each cluster has been than the warm-front ETCs despite the fact that the warm-
presented.Figures9,10,and11showthedistributionsofthe frontETCshavestrongermaximumvorticityvalues(thedif-
ETC-related precipitation, maximum vorticity, and the lati- ference is statistically significant). The centre ETCs reach
tude of the maximum vorticity for each cluster. The shapes their maximum vorticity at an average latitude of 45.1◦N,
whichis2.3◦fartherequatorwardthantheETCsinthewarm-
oftheprecipitation,maximumvorticity,andlatitudeofmax-
imum vorticity distributions are similar for the cold-front, front cluster which reach their maximum at an average lati-
tudeof47.4◦N(Fig.11).Thisdifferenceisfoundtobestatis-
warm-front,andcentreETCs,whereastheweakETCshave
verydifferentlyshapeddistributions,particularlyforthelat- ticallysignificantwhenthefulldistributionsareconsidered;
itudeofmaximumvorticity. thatis,thewarm-frontETCsreachtheirmaximumvorticity
The distributions for each cluster within the control sim- morepolewardthanthecentreETCsdo.TheweakETCsin
ulationcanbecomparedtoeachotherusingStudent’st test thecontrolsimulationhavethesmallestmaximumvorticities
to determine how different the clusters are and also to ex- but also occur at much higher latitudes than the other types
| plain the          | differences in | the mean | ETC structures. | When the   | ofETCs. |     |     |     |     |
| ------------------ | -------------- | -------- | --------------- | ---------- | ------- | --- | --- | --- | --- |
| full distributions | for each       | cluster  | in the control  | simulation |         |     |     |     |     |
are considered, the cold-front ETCs (Fig. 9a) have statisti- 6.2 ETCclustersintheSST4andAAsimulations
| cally significantly | more | precipitation | associated | with them |     |     |     |     |     |
| ------------------- | ---- | ------------- | ---------- | --------- | --- | --- | --- | --- | --- |
thantheETCsintheotherthreeclusters(Fig.9d,g,k),which
|     |     |     |     |     | Figure | 5e–h and i–l | show the precipitation | patterns | and |
| --- | --- | --- | --- | --- | ------ | ------------ | ---------------------- | -------- | --- |
isinagreementwiththemeanvaluespresentedinFig.5.The
|            |                   |               |               |                | MSLP for       | the four composite | mean      | ETCs in the SST4 | and    |
| ---------- | ----------------- | ------------- | ------------- | -------------- | -------------- | ------------------ | --------- | ---------------- | ------ |
| cold-front | ETCs also have    | statistically | significantly | larger         |                |                    |           |                  |        |
|            |                   |               |               |                | AA simulations | (additional        | times for | the SST and      | AA ex- |
| values of  | maximum vorticity | compared      | to all        | other clusters |                |                    |           |                  |        |
perimentsareshowninFigs.S10andS11respectively).The
| (Fig. 10a, | d, g, k) and | also reach | their maximum | vorticity |     |     |     |     |     |
| ---------- | ------------ | ---------- | ------------- | --------- | --- | --- | --- | --- | --- |
mainresultisthatinallthreeexperiments,verysimilartypes
valuesfurthersouth(meanlatitudeof44.4◦N)thanETCsin
|     |     |     |     |     | of ETCs | in terms of their | precipitation | patterns occur; | the |
| --- | --- | --- | --- | --- | ------- | ----------------- | ------------- | --------------- | --- |
theotherthreeclusters.
cold-front,warm-front,centre,andweakcyclonesidentified
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 579
Figure 7. Composite mean of the convective precipitation (shading, mm/6h) and the total column water vapour (black contours, every
2gkg
−1)
12h before the time of the maximum vorticity. Different columns show different clusters, and different rows show different
experiments.
in the control simulations also occur in the SST4 and AA front ETC. In the SST4 simulation this is associated with a
simulations.Furthermore,thedynamicalstructureandloca- weakerjetstreakcomparedtothecontrol(Fig.8b,f).
tion relative to the jet streak (Fig. 8) are very similar for Now the distributions of precipitation, maximum vortic-
all clusters in the SST4 and AA experiments compared to ity,andlatitudeofmaximumvorticityforeachclusterinthe
thecorrespondingclusterinthecontrolsimulation.However, SST4 simulation are compared to the corresponding cluster
somedifferencesdoexist,particularlyintermsoftheabso- inthecontrolsimulation.Asummaryofthestatisticallysig-
lutevaluesofthermodynamicvariables. nificant differences is presented in Fig. 12. When the dis-
The mean ETCs in the SST4 experiment all have heav- tributionsofETCprecipitationforeachclusterintheSST4
iertotalprecipitationandconvectiveprecipitationthaninthe simulationare comparedto thecorrespondingcluster inthe
controlsimulation,althoughthespatialpatternsareverysim- control simulation, one-sided t tests show that all clusters
ilar.Likewise,themeancompositeETCsintheSST4exper- intheSST4experimenthavestatisticallysignificantlymore
iment all have much higher values of TCWV and 850hPa precipitation associated with them (Figs. 9, 12). The cold-
potential temperature associated with them. This is consis- front ETCs in the SST4 simulation have statistically signif-
tent with an overall warmer and thus moister environment. icantly larger values of maximum vorticity compared to the
Related to this, the SST4 composite means have lower IPV correspondingclusterinthecontrolsimulation(Figs.10,12).
values on the 315K isentrope, caused by this isentrope be- However,whenthewarm-frontandcentreETCclustersare
ing lower in the troposphere in the warmer simulation. The considered,thereisnostatisticallysignificantdifferencebe-
minimum MSLP is 1–3hPa lower in the SST4 mean ETCs tween the distributions of maximum vorticity between the
compared to their related clusters in the control simulation. SST and control simulations. Furthermore, the weak ETC
Interestingly,theverticalmotionat700hPaisalmostidenti- cluster has statistically significantly smaller values of max-
calinthecorrespondingcompositesinthecontrolandSST4 imumvorticitycomparedtothecorrespondingclusterinthe
simulations,indicatingthatthelargeincreaseinprecipitation control.ThismeansthathowthemaximumvorticityofETCs
isnotdirectlyrelatedtochangesintheascent.Theonlydis- responds to uniform warming depends on the type of ETC.
cernibledifferenceintheETCstructureoccursforthewarm- This result is consistent with the result presented in Sect. 4
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

580 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Figure8.Compositemeanofthe300hPawindspeed(shading,ms
−1),potentialvorticityonthe315Ksurface(greycontours,every1PVU),
andthe700hPaverticalvelocity(solidpurplecontours,onlyascentshown–firstcontouris−0.2Pas −1,contourintervalof0.1Pas −1)12h
beforethetimeofthemaximumvorticity.Differentcolumnsshowdifferentclusters,anddifferentrowsshowdifferentexperiments.
–thatuniformwarmingdoesnotchangethemaximumvor- ETCs in the cold-front, warm-front, and centre ETC clus-
ticity of ETCs – but also indicates that looking at all ETCs tershavemoreprecipitationassociatedwiththemintheAA
together can mask notable changes. The cold-front, warm- simulation than in the control (summary shown in Fig. 12).
front,andcentreETCsoccurathigherlatitudesintheSST4 In contrast, the precipitation associated with the weak ETC
simulationincomparisontotheircounterpartsinthecontrol cluster has no significant difference between the AA and
simulation(Figs.11,12).However,intheSST4experiment, control simulations. The cold-front, centre, and weak ETC
the weak ETCs occur at slightly lower latitudes (mean lati- clustershavestatisticallysignificantlyweakermaximumvor-
tude of 60.8◦N) than the weak ETCs in the control simula- ticity values in the AA simulation compared to in the con-
tion. trolsimulation(Figs.10,12).Themaximumvorticityofthe
WenowcomparetheclustermeansintheAAsimulation ETCs in the warm-front cluster does not differ between the
to the corresponding clusters in the control simulation. All AAandcontrolsimulations.Allclustershavetheirlatitudeof
ETCs have significantly more precipitation associated with maximumvorticitymoreequatorwardintheAAsimulation
them in the AA simulation (Fig. 5). However, the increases comparedtothecontrol(Fig.11).Thisresultisstatistically
are relatively small except for the warm-front ETC, which significant for all clusters (Fig. 12) and consistent with the
has an increase of almost 1mm(6h)−1 in the precipitation changesingenesisandlysislatitudepresentedinFig.3.
rate on the bent-back warm front. In addition, although the
MSLP patterns are very similar between the AA and con- 6.3 FrequencyofoccurrenceofthedifferentETCs
trol composite mean ETCs, the minimum MSLP is 2–4hPa
higherintheAAsimulationthaninthecontrol.Thejetstruc- To help answer the question of whether different types of
ture,700hPaascent,andupper-levelIPVfieldsarealsovery ETCs are more or less common in the different climates,
similarbetweentheAAETCclustermeansandthoseinthe thenumberofETCsineachclusterforeachexperimentand
control. the relative occurrence of the four types of ETCs is shown
When the ETC precipitation distributions for each clus- in Fig. 13. In the controlsimulation the absolute number of
ter in the AA simulation are compared to the correspond- ETCsinthewarm-front,cold-front,andcentreETCsisvery
ingclusterinthecontrolsimulation(Fig.9),wefindthatthe similar. However, there are slightly more ETCs in the weak
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 581
Figure 9. Probability density distributions of the average ETC precipitation 12h before the time of maximum intensity for each cluster
(differentrows)andeachexperiment(differentcolumns).Cyclonesareonlyincludediftheyexist24hbeforethetimeofmaximumvorticity
| andreachtheirmaximumvorticitypolewardof30 |     |     |     |     | ◦   | N.  |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cyclone cluster. In the SST4 simulation, again the weak cy- 7 EffectofETCtypeontherelationshipbetween
cloneclusterhasthemostETCs.Thecold-frontETCcluster precipitationandcycloneintensity
isthesecondmostcommonbutcloselyfollowedbyboththe
warm-frontandcentreETCs.IntheAAsimulationthereare
|     |     |     |     |     |     |     | Figure 14 | shows | the relationship |     | between | maximum |     | vortic- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---------------- | --- | ------- | ------- | --- | ------- |
manymoreweakETCsthantheotherthreeETCtypes.Fur-
|           |            |             |      |           |           |                | ity and total | precipitation |         | 12h     | before      | the time | of maximum |         |
| --------- | ---------- | ----------- | ---- | --------- | --------- | -------------- | ------------- | ------------- | ------- | ------- | ----------- | -------- | ---------- | ------- |
| thermore, | the number | of          | weak | ETCs      | in the AA | simulation     |               |               |         |         |             |          |            |         |
|           |            |             |      |           |           |                | intensity     | for each      | cluster | in each | experiment. |          | In the     | control |
| ismuch    | largerthan | theabsolute |      | numberand |           | relativeoccur- |               |               |         |         |             |          |            |         |
simulation,thelargestcorrelationcoefficientandslopeofthe
| rence of | weak | ETCs in | the control | and | SST4 | simulations. |                   |     |         |               |     |     |           |       |
| -------- | ---- | ------- | ----------- | --- | ---- | ------------ | ----------------- | --- | ------- | ------------- | --- | --- | --------- | ----- |
|          |      |         |             |     |      |              | linear regression |     | between | precipitation |     | and | vorticity | occur |
ThisindicatesthatArcticamplificationandtheassociatedin-
|     |     |     |     |     |     |     | for the warm-front |     | ETC | (Fig. | 14d). | A moderate | correlation |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ----- | ----- | ---------- | ----------- | --- |
creaseinhigh-latitudetemperaturesanddecreaseinstability
coefficientandslopearealsopresentforthecold-frontETC
| (Fig. S5d) | lead | to many | more | weak ETCs | developing. | This |     |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | ---- | --------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
inthecontrolsimulation(Fig.14a),yetthereareverysmall
| is despite                                         | the decrease | in  | the meridional |     | temperature | gradi- |                  |     |            |     |        |               |     |      |
| -------------------------------------------------- | ------------ | --- | -------------- | --- | ----------- | ------ | ---------------- | --- | ---------- | --- | ------ | ------------- | --- | ---- |
|                                                    |              |     |                |     |             |        | correlations     | and | regression |     | slopes | in the centre | and | weak |
| entwhich,fromanenergytransportpointofview,wouldin- |              |     |                |     |             |        | ETCs(Fig.14g,j). |     |            |     |        |               |     |      |
dicatefewerETCsarerequiredtotransportheatpolewards.
Thesteeperslopeinthewarm-frontETC,comparedtothe
However,theseweakETCsaremainlyathighlatitudesand
cold-frontETCinthecontrolsimulation,meansthatvorticity
| likely contribute |     | little to | the total | poleward | heat | transport. |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | --------- | -------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
increaseslessforthesameincreaseinprecipitationinwarm-
Furthermore,theincreaseinthenumberofweakETCsdoes
|     |     |     |     |     |     |     | front ETCs | compared |     | to in cold-front |     | ETCs. | However, | de- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ---------------- | --- | ----- | -------- | --- |
notcomeattheexpenseofstrongerETCs;therearesimply spitethesteeperslopeinthewarm-frontETCs,thecold-front
| more ETCs | in  | the AA experiment, |     | but | the majority | of the |     |     |     |     |     |     |     |     |
| --------- | --- | ------------------ | --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ETCsproducemoreprecipitationthanthewarm-frontETCs
extraETCsareweak.
|     |     |     |     |     |     |     | of the same | intensity, |     | and this | is true | for all | ETC | intensi- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | -------- | ------- | ------- | --- | -------- |
ties,e.g.forweakandstrongETCs.Thismaybebecausethe
warm-frontETCsoccuratslightlyhigherlatitudes(compare
|     |     |     |     |     |     |     | Fig. 11a | and d) | where | there | is less | moisture | available | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ----- | ------- | -------- | --------- | --- |
thuslessprecipitationoccursforanETCofthesameinten-
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

582 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Figure 10. Probability density distributions of the maximum 850hPa vorticity (T42 values) for each cluster (different rows) and each
experiment(differentcolumns).Cyclonesareonlyincludediftheyexist24hbeforethetimeofmaximumvorticityandreachtheirmaximum
◦
vorticitypolewardof30 N.
sity.Alternatively,asthecold-frontETCshavealargerlow- IntheSSTexperiment,thestrongestlinearregressionand
levelPVanomaly(compareFig.6aandb),thismayindicate largest correlation coefficient is again found in the warm-
that the cold-front ETCs have a stronger diabatic feedback front ETCs (Fig. 14e). Weak correlations and linear regres-
than the warm-front ETC, and hence vorticity is enhanced sions are found in the centre and weak ETCs (Fig. 14h, k).
more for the same amount of precipitation in the cold-front Uniformwarmingcausesthelinearregressionslopesforall
ETCcomparedtothewarm-frontETC. four clusters to increase (compare the first and second col-
The small linear regression slope and correlation coeffi- umninFig.14).Hence,forallclustersprecipitationincreases
cient found for the weak ETCs in the control simulation more with uniform warming than maximum vorticity does.
(Fig. 14j) are very likely explained by the high latitude of Ourhypothesiswasthatifincreasedprecipitationinwarmer
these ETCs (Fig. 11j) and the limited amount of moisture climates feeds back, via diabatic heating and low-level PV
availableinthelocationstheydevelopinandmovethrough. anomalies, onto the dynamical intensity of the ETCs, pre-
The lack of dependency between vorticity and precipitation cipitation and vorticity would increase at similar rates, and
in the centre ETCs (Fig. 14g) is also notable as these ETCs hencetheslopeofthelinearregressionlinebetweenprecip-
occuratlowtomid-latitudes(Fig.11g)wheremoistureisnot itation and vorticity would remain similar. However, as the
limited. There are ETCs included in the centre ETC cluster slopes for all clusters increase with warming (Fig. 14), this
whichhavesmallvaluesofmaximumvorticityyetmoderate meanseitherthatthereisaweakdiabaticfeedbackorthatthe
tolargeamountsofprecipitationassociatedwiththem.These increaseinvorticitycausedbyanincreaseindiabaticheating
centreETCsarequiteconvective(Fig.7c),andhencethepre- isoffsetbyadecreaseinvorticitycausedbyareductioninthe
cipitationamountisnotheavilyinfluencedbythelarge-scale large-scale baroclinicity. The largest relative increase in the
ascent or the strength of the circulation. Furthermore, the linearregressionslopeintheSST4experimentcomparedto
centreETCshaveaweakerupper-levelPVanomaly(Fig.8c) thecontroloccursintheweakETC,aswithuniformwarm-
compared to the cold- (Fig. 8a) and warm-front (Fig. 8b) ingtheseETCsarelessmoisturelimitedthaninthecontrol
ETCsinthecontrolsimulation. simulation. The cold-front ETCs have a larger relative in-
creaseintheslopethanthewarm-frontETCswithwarming,
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 583
Figure 11. Probability density distributions of the latitude of the maximum 850hPa vorticity for each cluster (different rows) and each
experiment(differentcolumns).Cyclonesareonlyincludediftheyexist24hbeforethetimeofmaximumvorticityandreachtheirmaximum
| vorticitypolewardof30 |     | ◦ N. |     |     |     |     |     |     |     |
| --------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
indicatingthatthecold-frontETCsmaybebetteratconvert- thewarm-frontETCsisnotstatisticallydifferentbetweenthe
ingtheextramoistureintoprecipitationthanthewarm-front controlandAAsimulations.Thelackofanincreaseinvor-
| ETCs. |     |     |     |     |     | ticitysuggeststhatdiabaticprocessesdonotacttointensify |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
As was the case in the control and SST4 simulations, in warm-frontETCsorthatanyincreaseinvorticitybydiabatic
the AA experiment the largest Pearson’s correlation coeffi- processes is counteracted by a decrease in vorticity driven
cientandregressionslopeoccurforthewarm-frontcyclone byareductioninbaroclinicity.Thedecreaseinthelinearre-
cluster(Fig.14f),andweakcorrelationcoefficientsandsmall gression slope in the cold-front ETC in the AA simulation
comparedtothecontrolissmall(−2.3%),butbootstrapping
| linear | regression | slopes occur | for the | centre | (Fig. 14i) and |     |     |     |     |
| ------ | ---------- | ------------ | ------- | ------ | -------------- | --- | --- | --- | --- |
weak(Fig.14l)ETCs.Relativetothecontrolsimulation,po- showsthedifferencetobestatisticallysignificant.Thissmall
laramplificationcausestheslopeofthelinearregressionbe- decrease occurs since, although ETCs of all intensities see
tweenmaximumvorticityandprecipitationtoincreaseinthe an increase in precipitation with polar amplification, ETCs
warm-front, centre, and weak ETC clusters but to decrease withlowermaximumvorticityvaluesthatareincludedinthe
inthecold-frontETC(comparethefirstandthirdcolumnsin cold-front cluster see a slightly larger increase in precipita-
Fig.14).Thelargestrelativeincreaseintheregressionslope tionthanthestrongestETCsinthesamecluster.
comparedtothecontrolsimulationoccursforthecentreETC
(+62%);
|     | however, | the linear | regression | slope | still remains |     |     |     |     |
| --- | -------- | ---------- | ---------- | ----- | ------------- | --- | --- | --- | --- |
verysmall(0.104mm(6h)−1/10−5s−1)inthecentreETCs.
8 Conclusions
Amoderateincreaseinthelinearregressionslopeoccursfor
theweakETC(+24%),whichisduetotheincreaseinmois-
|     |     |     |     |     |     | In this study, | we investigated | the relationship | between the |
| --- | --- | --- | --- | --- | --- | -------------- | --------------- | ---------------- | ----------- |
tureinthehigh-latituderegions,wheretheseETCsoccur,in
|        |            |          |        |          |              | maximumintensityofextra-tropical |     | cyclonesandtheirpre- |     |
| ------ | ---------- | -------- | ------ | -------- | ------------ | -------------------------------- | --- | -------------------- | --- |
| the AA | experiment | compared | to the | control. | The moderate |                                  |     |                      |     |
cipitation,howthismaychangeinthefuture,andalsohowit
| increase | in the | slope for | the warm-front | ETCs | means that |     |     |     |     |
| -------- | ------ | --------- | -------------- | ---- | ---------- | --- | --- | --- | --- |
dependsonthetypeofETC.Threeaqua-planetsimulations
precipitationisincreasingmorethanvorticity.Thisisconsis-
|     |     |     |     |     |     | were performed | with the | state-of-the-art | numerical predic- |
| --- | --- | --- | --- | --- | --- | -------------- | -------- | ---------------- | ----------------- |
tentwithFig.12whichshowsthatthemaximumvorticityof
|     |     |     |     |     |     | tion model, | OpenIFS, differing | only | in terms of their pre- |
| --- | --- | --- | --- | --- | --- | ----------- | ------------------ | ---- | ---------------------- |
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

584 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
|     |     |     |     |     | ticity expected | from  | decreasing | baroclinicity, |     | especially   | for |
| --- | --- | --- | --- | --- | --------------- | ----- | ---------- | -------------- | --- | ------------ | --- |
|     |     |     |     |     | the strongest   | ETCs. | Polar      | amplification  | led | to no change | in  |
ETCprecipitation,weakerETCsintermsoftheirmaximum
|     |     |     |     |     | vorticity | being consistent |     | with the decrease |     | in Eady | growth |
| --- | --- | --- | --- | --- | --------- | ---------------- | --- | ----------------- | --- | ------- | ------ |
rate,andasmallequatorwardshiftinthestormtrack.These
resultsofhowthejetpositionandETCnumberandintensity
respondedtowarmingagreewithpreviousresultsfromboth
|     |     |     |     |     | idealised     | modelling | experiments    | and        | fully  | coupled   | realistic |
| --- | --- | --- | --- | --- | ------------- | --------- | -------------- | ---------- | ------ | --------- | --------- |
|     |     |     |     |     | climate       | models    | (e.g. Yettella | and Kay,   | 2017;  | Priestley | and       |
|     |     |     |     |     | Catto, 2022), | which     | gives          | confidence | in the | relevance | and       |
robustnessofouridealisedsimulations.
|     |     |     |     |     | In all         | three experiments, |           | there was    | a positive | correlation |         |
| --- | --- | --- | --- | --- | -------------- | ------------------ | --------- | ------------ | ---------- | ----------- | ------- |
|     |     |     |     |     | between        | the ETC            | maximum   | 850hPa       | vorticity  | and         | average |
|     |     |     |     |     | precipitation, | which              | is        | in agreement | with       | previous    | studies |
|     |     |     |     |     | (e.g. Pfahl    | and                | Sprenger, | 2016). When  | all        | ETCs were   | con-    |
sideredtogether,thelargestlinearregressionslopewasinthe
uniformwarming(SST4)experimentandwassmallestinthe
|     |     |     |     |     | control. | Thus, the | same | absolute increase |     | in ETC | strength |
| --- | --- | --- | --- | --- | -------- | --------- | ---- | ----------------- | --- | ------ | -------- |
Figure12.Summaryofstatisticallysignificantdifferencesbetween
|     |     |     |     |     | in SST4 | corresponded |     | to a larger | increase | in ETC-related |     |
| --- | --- | --- | --- | --- | ------- | ------------ | --- | ----------- | -------- | -------------- | --- |
each cluster’s precipitation, maximum vorticity, and latitudes of precipitation than in the control simulation. SST4 was the
maximumvorticityandthecorrespondingclusterinthecontrolsim- warmest and wettest simulation globally, which likely ex-
| ulation. Orange | (blue) | indicates that | thecluster as | labelled on the |     |     |     |     |     |     |     |
| --------------- | ------ | -------------- | ------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
plainsthestrongestslope,especiallywhentheresultsofYet-
| y axis has | a statistically | larger (smaller) | value than | in the corre- |           |             |     |        |         |              |     |
| ---------- | --------------- | ---------------- | ---------- | ------------- | --------- | ----------- | --- | ------ | ------- | ------------ | --- |
|            |                 |                  |            |               | tella and | Kay (2017), | who | showed | most of | the increase | in  |
spondingclusterinthecontrolsimulation.Whiteboxesmeanthere
isnostatisticaldifferencebetweentheclusterlabelledontheyaxis ETCprecipitationisduetothermodynamicaspects,arecon-
|     |     |     |     |     | sidered. | Theoretically, |     | heavy precipitation |     | causes strong | di- |
| --- | --- | --- | --- | --- | -------- | -------------- | --- | ------------------- | --- | ------------- | --- |
andthecorrespondingclusterinthecontrolsimulation.CFindicates
abaticheatingwhich,inturn,couldincreasetheintensityof
thecold-frontETCandWFthewarm-frontETC.
|     |     |     |     |     | the ETC | via the | production | of a low-level |     | positive | vorticity |
| --- | --- | --- | --- | --- | ------- | ------- | ---------- | -------------- | --- | -------- | --------- |
anomaly.However,inourwarmerexperiments,precipitation
scribed SST distributions. A control simulation, a uniform stronglyincreased,buttherewasnotanylargeincreaseinthe
warming, and a polar amplification experiment were con- intensity of ETCs; i.e. the slope was larger in SST4 than in
ducted. the control. This implies that the increased diabatic heating
First the response of the zonal-mean large-scale environ- does not feed back strongly onto the intensity of the ETCs
mentwasanalysed.Uniformwarmingresultedinapoleward in these experiments or that the diabatic feedback is coun-
shiftinthejetstream,nochangetothelow-levelmeridional teracted by a decrease in large-scale baroclinicity. The hor-
potential temperature gradient, and an increase in the Brunt izontal resolution of these simulations was relatively coarse
Väisälä frequency. Consequently, the Eady growth rate de- at 80km, and if similar experiments were performed with a
creased with uniform warming. Polar amplification resulted much higher-resolution model, the amount of diabatic heat-
in an equatorward shift in the jet stream and a narrowing ingandthestrengthofthelow-levelPVanomalywouldvery
ofthebarocliniczone.TheBruntVäisäläfrequencydidnot likelyincrease;thiswasrecentlyshowntohappenbyChoud-
changewithpolarwarminginthemid-latitudes,whichcom- haryandVoigt(2022).Potentially,thediabaticfeedbackmay
bined with a reduction in the meridional potential temper- become more visible at high resolution, in which case, we
ature gradient, led to a decrease in the Eady growth rate. wouldexpectthattheslopesofthelinearregressionlinesbe-
In the mid-to-upper troposphere at high latitudes the Brunt tweenmaximumvorticityandprecipitationwouldbesimilar
VäisäläfrequencydecreasedcausinganincreaseintheEady – albeit shifted to larger values in the warmer simulations.
growthrate.Theimpactofuniformwarmingandpolaram- However,whetherafeedbackoccursmaydependonthetype
plification on the cyclone statistics was then investigated. of cyclone. In the one case study that Choudhary and Voigt
Uniform warming resulted in an increase in ETC precipita- (2022)considered,thestrongerdiabaticheatingandpotential
tion and a small poleward shift in the storm track, consis- vorticityathigherresolutiondidnotresultinalowerMSLP
tent with the poleward shift in the jet. No statistically sig- asthecyclonewasstronglydominatedbythermaladvection
nificant change to the mean or median maximum vorticity anddiabaticheatingplayedasecondaryroleinitsintensifi-
| wasdetected,butmoreextremeETCsintermsoftheirmax- |     |     |     |     | cation. |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
imum vorticity occurred with uniform warming. Given the The variability (spread) in the relationship between pre-
decreaseintheEadygrowthratewithuniformwarming,this cipitationandETCintensityalsovariedbetweentheexperi-
response of ETC maximum vorticity indicated that diabatic ments.ThesmallestPearson’scorrelationcoefficient(r)was
processes may be acting to counteract the decrease in vor- foundintheSST4experiment,suggestingthereislargervari-
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 585
Figure13.(a)ThetotalnumberofETCsineachclusterforeachexperimentand(b)therelativefractionofETCsineachclusterforeach
experiment.
ability in ETC-related precipitation in the SST4 experiment eachsimulation.Thissuggeststhatneitheruniformwarming
than in either the control or polar amplification experiment. nor polar amplification will lead to any notable changes in
All experiments did show considerable spread (the correla- the average spatial patterns of precipitation associated with
tion coefficients ranged between 0.574 and 0.635), which ETCs.Thesecondmainresultoftheclusteringwasthatthe
suggeststhatnotallETCshaveastrongconnectionbetween absolute number and relative occurrence of the weak ETC,
ETCintensityandprecipitation.Thislargespreadmotivated whichwasfoundtodevelopincoldairmassesfarpoleward
ustoclustertheETCsintofourgroupsusingk-meansclus- ofthejetstream,increasedconsiderablywithpolaramplifi-
teringandinvestigatehowtherelationshipbetweenprecipita- cation despite the large-scale meridional temperature gradi-
tionintensityandcycloneintensitydependsoncyclonetype. ent decreasing. We hypothesise that this is because the po-
The clustering proved to be successful. Four distinct and lar amplification simulation has lower static stability in the
physically realistic mean cyclones were identified by com- mid-troposphereathighlatitudes,whichmeansforthesame
positing all ETCs allocated to each cluster together. Each forcingtherewillbemoreascentandthusitwillbeeasierfor
cluster (mean composite ETC) could be labelled based on ETCstodevelop.Secondly,asthepolarregionsarewarmer,
their precipitation patterns: a cyclone where most precipi- diabaticheatingislikelylargerinthepolaramplificationsim-
tation was associated with the cold front (cold-front ETC), ulation,whichcanincreasetheintensityoftheETCsbeyond
a cyclone where most precipitation was associated with the thethresholdvalueof1×10−1 usedtodetectanETC.This
warm front (warm-front ETC), a small-scale cyclone with indicatesthathigh-latitudecyclonesmaybecomemorecom-
most precipitation located near the cyclone centre (centre moninthefuture.
ETC), and a small-scale, high-latitude cyclone with weak The third main result from the ETC clustering was that
precipitation again focused on the cyclone centre (weak the relationship between maximum vorticity and precipita-
ETC). tion depended strongly on the type of ETC. The strongest
The first notable result from the clustering was that the relationship occurred for the warm-front ETCs, and this re-
same four mean ETCs were identified in all three experi- sultisrobustacrossallthreeexperiments.TheseETCswere
ments despite the clustering being done independently for moderatelystrong,resembledtheNorwegiancyclonemodel,
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

586 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Figure14.Two-dimensionalhistogramsshowingtherelationbetweenmaximumrelativevorticity(T42values)andETC-relatedprecipitation
12hbeforethetimeofmaximumrelativevorticityforeachsimulationandeachcluster.Precipitationistheareaaverage,averagedoverall
points with a 12 ◦ radius of the ETC centre where the rain rate exceeded 1mm(6h) −1. Only ETCs which exist at −24h and have their
◦
maximumvorticitynorthof30 Nareincluded.
and occurred more poleward than both the cold-front and tributetothelackofupper-levelforcing.ThisC2bcomposite
centre ETCs. However, the warm-front ETCs produced less cyclonealsohasprecipitationlocatedoverarelativelysmall
precipitationthanthecold-frontETCsforETCsofthesame area near the cyclone centre and thus resembles our weak
maximumvorticity. cyclonecomposite.Therefore,wehypothesisethatthepoor
A strong correlation was also found between maximum correlationwefoundbetweenETCprecipitationandvortic-
vorticity and precipitation for the cold-front ETCs, but this ityinthecyclonecentreETCswasduetothelackofstrong
was slightly weaker, and had more spread, than what was upper-level forcing for these ETCs, as suggested by Binder
foundforthewarm-frontETCs.Thecold-frontETCswere, etal.(2016).
on average, the strongest ETCs in terms of vorticity, as- The final notable result from the clustering was how the
cent,andprecipitation.TheweakETCclusterhadanotably maximumvorticityoftheETCs’responsetouniformwarm-
smaller correlation between ETC precipitation and maxi- ingdependsonthetypeofETC.Thecold-frontETCsexpe-
mum vorticity in all experiments (correlation coefficients riencedanincreaseintheirmaximumvorticitywithuniform
range from 0.241 to 0.298). These ETCs occurred at high warming, whereas both the warm-front and cyclone centre
latitudes, and therefore we concluded that the ETC precipi- ETCs showed no change in the maximum vorticity, and the
tationwaslimitedbythelackofmoistureandhencethatthe maximum vorticity of the weak ETC decreased. Hence this
dynamic intensity of the ETC had little control on the ETC isconsistentwiththeoverallpicture,whichisthatwhenall
precipitation. ETCsareconsideredtogether,therewerenochangesinETC
TheweakestofallcorrelationsbetweentheETCprecipita- intensity;however,itdoessuggestthatthedynamicalinten-
tionandvorticityoccurredforthecyclonecentreETCs(cor- sity of certain types of ETCs may respond more to climate
relationcoefficientsrangefrom0.098to0.190).Binderetal. changethanothers.Thisresultisalsoinagreementwithpre-
(2016)classifiedcyclonesbasedontheirdeepeningrateand viousstudies(e.g.PriestleyandCatto,2022)whichshowthat
warmconveyorbeltintensity,andoneoftheirsubsets,C2b, extremes respond differently to warming, as the cold-front
hasastrongwarmconveyorbeltandlow-levelPVanomaly ETCincludesthestrongestETCs.
but does not deepen rapidly, which Binder et al. (2016) at-
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 587
Ourstudyisuniqueinsomeaspects.First,previousstud- code.Wealsothankthereviewersandtheeditorfortheirconstruc-
ieshavetendedtorelateETCprecipitationtotheETCwinds, tivesuggestionstoimprovethemanuscript.
| whereas | we used | the      | maximum | vorticity |     | as identified | by      |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | ------- | --------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRACK.  | This    | approach | was     | selected  | as  | maximum       | vortic- |     |     |     |     |     |     |     |     |
ity is easily available from climate model simulations and Financialsupport. This research has been supported by the
|          |              |      |         |      |     |          |        | Academy   | of Finland | (grant  | no. | 338615)     | and          | the Natural | En- |
| -------- | ------------ | ---- | ------- | ---- | --- | -------- | ------ | --------- | ---------- | ------- | --- | ----------- | ------------ | ----------- | --- |
| is often | the variable | that | is used | when | the | question | of how |           |            |         |     |             |              |             |     |
|          |              |      |         |      |     |          |        | vironment | Research   | Council |     | (grant nos. | NE/V004166/1 |             | and |
theintensityofETCswillchangeinthefutureisaddressed.
| Our study     | also  | differs   | from   | many      | previous | studies   | in that | NE/S004645/1). |     |     |     |     |     |     |     |
| ------------- | ----- | --------- | ------ | --------- | -------- | --------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| we considered |       | ETCs      | of all | strengths | and      | not just  | the ex- |                |     |     |     |     |     |     |     |
| tremes in     | terms | of either | their  | maximum   |          | vorticity | (as was |                |     |     |     |     |     |     |     |
Reviewstatement.
ThispaperwaseditedbyStephanPfahlandre-
donebySinclairetal.,2020)orprecipitation.Thisdoesmake
viewedbytwoanonymousreferees.
| a difference | to  | how future | changes |     | are seen | (Priestley | and |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Catto,2022).However,ourstudydoeshighlightthatdespite
| small changes |     | in the strength |     | of the | cyclones, | the | precipita- |     |     |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ------ | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionincreasesarelarge,indicatingpotentialfutureincreases
| infloodingassociatedwithcyclones. |     |     |     |     |     |     |     | References |        |         |        |             |           |         |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------- | ------ | ----------- | --------- | ------- | --- |
|                                   |     |     |     |     |     |     |     | Allen, M.  | R. and | Ingram, | W. J.: | Constraints | on future | changes | in  |
Codeavailability. OpenIFS is available under license from climateandthehydrologiccycle,Nature,419,224–232,2002.
| the European | Centre | for | Medium | Range | Weather |     | Forecasting |             |            |     |       |         |         |         |         |
| ------------ | ------ | --- | ------ | ----- | ------- | --- | ----------- | ----------- | ---------- | --- | ----- | ------- | ------- | ------- | ------- |
|              |        |     |        |       |         |     |             | Binder, H., | Boettcher, | M., | Joos, | H., and | Wernli, | H.: The | role of |
(ECMWF).Seehttps://confluence.ecmwf.int/display/OIFS(lastac-
|              |       |          |          |             |     |     |              | warm | conveyor | belts for | the intensification |     | of  | extratropical | cy- |
| ------------ | ----- | -------- | -------- | ----------- | --- | --- | ------------ | ---- | -------- | --------- | ------------------- | --- | --- | ------------- | --- |
| cess: 9 June | 2023) | for more | details. | TRACK-1.5.2 |     | is  | available at |      |          |           |                     |     |     |               |     |
clonesinNorthernHemispherewinter,J.Atmos.Sci.,73,3997–
https://gitlab.act.reading.ac.uk/track/track(Hodges,2023).
4020,https://doi.org/10.1175/JAS-D-15-0302.1,2016.
|     |     |     |     |     |     |     |     | Binder, H., | Joos, | H., Sprenger, |     | M., and | Wernli, | H.: Warm | con- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------------- | --- | ------- | ------- | -------- | ---- |
veyorbeltsinpresent-dayandfutureclimatesimulations–Part2:
| Dataavailability. |     | Themaximumvorticityandcyclone-relatedpre- |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Roleofpotentialvorticityproductionforcycloneintensification,
cipitationforallcyclonesinallthreeexperimentsareavailableat Weather Clim. Dynam., 4, 19–37, https://doi.org/10.5194/wcd-
| https://doi.org/10.5281/zenodo.8027867(SinclairandCatto,2023). |     |     |     |     |     |     |     | 4-19-2023,2023. |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Thefullmodeloutputisverylargeandthereforecannotallbemade Bjerknes, J.: On the structure of moving cyclones, Mon. Weather
publiclyavailable.PleasecontactVictoriaSinclairforaccesstothe
Rev.,47,95–99,1919.
fulldataset.
Bjerknes,J.andSolberg,H.:Lifecycleofcyclonesandthepolar
|     |     |     |     |     |     |     |     | front theory | of  | atmospheric | circulation, |     | Geofys. | Publ., | 3, 1–1, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | ------------ | --- | ------- | ------ | ------- |
1922.
Supplement. Thesupplementrelatedtothisarticleisavailableon- Booth, J. F., Naud, C. M., and Jeyaratnam, J.: Extrat-
lineat:https://doi.org/10.5194/wcd-4-567-2023-supplement. ropical Cyclone Precipitation Life Cycles: A Satellite-
|     |     |     |     |     |     |     |     | Based | Analysis, | Geophys. |     | Res. Lett., | 45, | 8647–8654, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | -------- | --- | ----------- | --- | ---------- | --- |
https://doi.org/10.1029/2018GL078977,2018.
Authorcontributions. VASandJLCdesignedthestudy.VASper- Boutle, I. A., Belcher, S. E., and Plant, R. S.: Moisture transport
inmidlatitudecyclones,Q.J.Roy.Meteor.Soc.,137,360–373,
formedtheexperiments,anddidmostofthedataanalysisandwrit-
https://doi.org/10.1002/qj.783,2011.
| ing. Both | authors | contributed | equally | to  | the interpretation |     | of the |     |     |     |     |     |     |     |     |
| --------- | ------- | ----------- | ------- | --- | ------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
results. Browning, K. A.: Radar measurements of air motion near
|     |     |     |     |     |     |     |     | fronts, | Weather, | 26, | 320–340, | https://doi.org/10.1002/j.1477- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | -------- | ------------------------------- | --- | --- | --- |
8696.1971.tb04211.x,1971.
Büeler,D.andPfahl,S.:Potentialvorticitydiagnosticstoquantify
| Competinginterests. |     | The | contact | author | has declared |     | that neither |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------- | ------ | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
effectsoflatentheatinginextratropicalcyclones.PartII:appli-
oftheauthorshasanycompetinginterests.
|     |     |     |     |     |     |     |     | cation | to idealized | climate | change | simulations, |     | J. Atmos. | Sci., |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | ------- | ------ | ------------ | --- | --------- | ----- |
76,1885–1902,2019.
|             |             |     |                  |     |              |     |         | Carlson, | T.  | N.: Airflow |     | through        | midlatitude |      | cy-     |
| ----------- | ----------- | --- | ---------------- | --- | ------------ | --- | ------- | -------- | --- | ----------- | --- | -------------- | ----------- | ---- | ------- |
| Disclaimer. | Publisher’s |     | note: Copernicus |     | Publications |     | remains |          |     |             |     |                |             |      |         |
|             |             |     |                  |     |              |     |         | clones   | and | the comma   |     | cloud pattern, |             | Mon. | Weather |
neutralwithregardtojurisdictionalclaimsinpublishedmapsand
|     |     |     |     |     |     |     |     | Rev., | 108, | 1498–1509, |     | https://doi.org/10.1175/1520- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ---------- | --- | ----------------------------- | --- | --- | --- |
institutionalaffiliations.
0493(1980)108<1498:ATMCAT>2.0.CO;2,1980.
|     |     |     |     |     |     |     |     | Catto, J. | L.:     | Extratropical |     | cyclone        | classification |              | and its |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------- | --- | -------------- | -------------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | use in    | climate | studies,      |     | Rev. Geophys., |                | 54, 486–520, |         |
Acknowledgements. The authors wish to acknowledge CSC – https://doi.org/10.1002/2016RG000519,2016.
IT Center for Science, Finland, for computational resources and Catto, J. L.: A New Method to Objectively Classify Extra-
| ECMWF | for providing |     | the OpenIFS |     | model. | We thank | Kevin |          |          |     |         |          |     |         |        |
| ----- | ------------- | --- | ----------- | --- | ------ | -------- | ----- | -------- | -------- | --- | ------- | -------- | --- | ------- | ------ |
|       |               |     |             |     |        |          |       | tropical | Cyclones | for | Climate | Studies: |     | Testing | in the |
HodgesforprovidingthecyclonetrackingcodeTRACKandHe-
|     |     |     |     |     |     |     |     | Southwest | Pacific | Region, |     | J. Climate, |     | 31, 4683–4704, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | --- | ----------- | --- | -------------- | --- |
lenDacreforprovidinganinitialversionofthecyclonecomposite
https://doi.org/10.1175/JCLI-D-17-0746.1,2018.
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023

588 V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation
Catto, J. L. and Pfahl, S.: The importance of fronts for ex- taldesignandorganization,Geosci.ModelDev.,9,1937–1958,
treme precipitation, J. Geophys. Res., 118, 10791–10801, https://doi.org/10.5194/gmd-9-1937-2016,2016.
https://doi.org/10.1002/jgrd.50852,2013. Field, P. R. and Wood, R.: Precipitation and cloud struc-
Catto,J.L.,Shaffrey,L.C.,andHodges,K.I.:Canclimatemodels ture in midlatitude cyclones, J. Climate, 20, 233–254,
capture the structure of extratropical cyclones?, J. Climate, 23, https://doi.org/10.1175/JCLI3998.1,2007.
1621–1635,https://doi.org/10.1175/2009JCLI3318.1,2010. Flaounas, E., Raveh-Rubin, S., Wernli, H., Drobinski, P., and
Catto,J.L.,Jakob,C.,Berry,G.,andNicholls,N.:Relatingglobal Bastin,S.:ThedynamicalstructureofintenseMediterraneancy-
precipitation to atmospheric fronts, Geophys. Res. Lett., 39, clones,Clim.Dynam.,44,2411–2427,2015.
L10805,https://doi.org/10.1029/2012GL051736,2012. Harrold,T.W.:Mechanismsinfluencingthedistributionofprecipi-
Catto,J.L.,Madonna,E.,Joos,H.,Rudeva,I.,andSimmonds,I.: tationwithinbaroclinicdisturbances,Q.J.Roy.Meteor.Soc.,99,
GlobalRelationshipbetweenFrontsandWarmConveyorBelts 232–251,https://doi.org/10.1002/qj.49709942003,1973.
andtheImpactonExtremePrecipitation,J.Climate,28,8411– Hartmann,D.L.:GlobalPhysicalClimatology,vol.103,Elsevier,
8429,https://doi.org/10.1175/JCLI-D-15-0171.1,2015. https://doi.org/10.1016/C2009-0-00030-0,2015.
Choudhary, A. and Voigt, A.: Impact of grid spacing, convective Hawcroft,M.,Walsh,E.,Hodges,K.,andZappa,G.:Significantly
parameterization and cloud microphysics in ICON simulations increased extreme precipitation expected in Europe and North
ofawarmconveyorbelt,WeatherClim.Dynam.,3,1199–1214, America from extratropical cyclones, Environ. Res. Lett., 13,
https://doi.org/10.5194/wcd-3-1199-2022,2022. 124006,https://doi.org/10.1088/1748-9326/aaed59,2018.
Dacre,H.F.andGray,S.L.:Thespatialdistributionandevolution Hawcroft,M.K.,Shaffrey,L.C.,Hodges,K.I.,andDacre,H.F.:
characteristics of North Atlantic cyclones, Mon. Weather Rev., How much Northern Hemisphere precipitation is associated
137,99–115,https://doi.org/10.1175/2008MWR2491.1,2009. with extratropical cyclones?, Geophys. Res. Lett., 39, L24809,
Dacre, H. F., Hawcroft, M. K., Stringer, M. A., and Hodges, https://doi.org/10.1029/2012GL053866,2012.
K. I.: An extratropical cyclone atlas: A tool for illustrating cy- Hodges,K.:TRACK,UniversityofReading[code],https://gitlab.
clone structure and evolution characteristics, B. Am. Meteo- act.reading.ac.uk/track/track,lastaccess:9June2023.
rol Soc., 93, 1497–1502, https://doi.org/10.1175/BAMS-D-11- Hodges, K. I.: A general method for tracking analysis and
00164.1,2012. its application to meteorological data, Mon. Weather
Dai, P. and Nie, J.: A global quasigeostrophic diagnosis of ex- Rev., 122, 2573–2586, https://doi.org/10.1175/1520-
tratropical extreme precipitation, J. Climate, 33, 9629–9642, 0493(1994)122<2573:AGMFTA>2.0.CO;2,1994.
https://doi.org/10.1175/JCLI-D-20-0146.1,2020. Hodges, K. I.: Feature tracking on the unit sphere, Mon.
Dai, P. and Nie, J.: Robust expansion of extreme midlati- Weather Rev., 123, 3458–3465, https://doi.org/10.1175/1520-
tude storms under global warming, Geophys. Res. Lett., 49, 0493(1995)123<3458:FTOTUS>2.0.CO;2,1995.
e2022GL099007,https://doi.org/10.1029/2022GL099007,2022. Hodges, K. I., Lee, R. W., and Bengtsson, L.: A comparison of
Dolores-Tesillos, E., Teubler, F., and Pfahl, S.: Future changes extratropicalcyclonesinrecentreanalysesERA-Interim,NASA
in North Atlantic winter cyclones in CESM-LE – Part 1: MERRA,NCEPCFSR,andJRA-25,J.Climate,24,4888–4906,
Cyclone intensity, potential vorticity anomalies, and hori- https://doi.org/10.1175/2011JCLI4097.1,2011.
zontal wind speed, Weather Clim. Dynam., 3, 429–448, Kirshbaum,D.,Merlis,T.,Gyakum,J.,andMcTaggart-Cowan,R.:
https://doi.org/10.5194/wcd-3-429-2022,2022. Sensitivityofidealizedmoistbaroclinicwavestoenvironmental
Douville,H.,Raghavan,K.,Renwick,J.,Allan,R.P.,Arias,P.A., temperatureandmoisturecontent,J.Atmos.Sci.,75,337–360,
Barlow,M.,Cerezo-Mota,R.,Cherchi,A.,Gan,T.Y.,Gergis,J., https://doi.org/10.1175/JAS-D-17-0188.1,2018.
Jiang,D.,Khan,A.,PokamMba,W.,Rosenfeld,D.,Tierney,J., Kodama, C., Iga, S., and Satoh, M.: Impact of the sea surface
andZolina,O.:WaterCycleChanges,in:ClimateChange2021: temperatureriseonstorm-trackcloudsinglobalnonhydrostatic
ThePhysicalScienceBasis.ContributionofWorkingGroupIto aqua planet simulations, Geophys. Res. Lett., 41, 3545–3552,
theSixthAssessmentReportoftheIntergovernmentalPanelon https://doi.org/10.1002/2014GL059972,2014.
Climate Change, edited by: Masson-Delmotte, V., Zhai, P., Pi- Kodama, C., Stevens, B., Mauritsen, T., Seiki, T., and Satoh, M.:
rani, A., Connors, S. L., Péan, C., Berger, S., Caud, N., Chen, Anewperspectiveforfutureprecipitationchangefromintense
Y.,Goldfarb,L.,Gomis,M.I.,Huang,M.,Leitzell,K.,Lonnoy, extratropical cyclones, Geophys. Res. Lett., 46, 12435–12444,
E.,Matthews,J.B.R.,Maycock,T.K.,Waterfield,T.,Yelekçi, https://doi.org/10.1029/2019GL084001,2019.
O., Yu, R., and Zhou, B., Cambridge University Press, Cam- Lloyd,S.:LeastsquaresquantizationinPCM,IEEET.Inform.The-
bridge,UnitedKingdomandNewYork,NY,USA,1055–1210, ory, 28, 129–137, https://doi.org/10.1109/TIT.1982.1056489,
https://doi.org/10.1017/9781009157896.010,2021. 1982.
Eady,E.T.:Longwavesandcyclonewaves,Tellus,1,33–52,1949. Madonna, E., Wernli, H., Joos, H., and Martius, O.: Warm Con-
Evans, M. S., Keyser, D., Bosart, L. F., and Lack- veyorBeltsintheERA-InterimDataset(1979–2010).PartI:Cli-
mann, G. M.: A Satellite-Derived Classification Scheme matologyandPotentialVorticityEvolution,J.Climate,27,3–26,
for Rapid Maritime Cyclogenesis, Mon. Weather https://doi.org/10.1175/JCLI-D-12-00720.1,2014.
Rev., 122, 1381–1416, https://doi.org/10.1175/1520- Michaelis, A. C., Willison, J., Lackmann, G. M., and Robinson,
0493(1994)122<1381:ASDCSF>2.0.CO;2,1994. W.A.:ChangesinWinterNorthAtlanticExtratropicalCyclones
Eyring, V., Bony, S., Meehl, G. A., Senior, C. A., Stevens, B., inHigh-ResolutionRegionalPseudo–GlobalWarmingSimula-
Stouffer, R. J., and Taylor, K. E.: Overview of the Coupled tions, J. Climate, 30, 6905–6925, https://doi.org/10.1175/JCLI-
Model Intercomparison Project Phase 6 (CMIP6) experimen- D-16-0697.1,2017.
WeatherClim.Dynam.,4,567–589,2023 https://doi.org/10.5194/wcd-4-567-2023

V.A.SinclairandJ.L.Catto:Cycloneintensityandprecipitation 589
Milrad, S. M., Atallah, E. H., and Gyakum, J. R.: Synoptic typ- Rousseeuw, P. J.: Silhouettes: a graphical aid to the interpretation
ing of extreme cool-season precipitation events at St. John’s, and validation of cluster analysis, J. Comput. Appl. Math., 20,
Newfoundland, 1979–2005, Weather Forecast., 25, 562–586, 53–65,https://doi.org/10.1016/0377-0427(87)90125-7,1987.
https://doi.org/10.1175/2009WAF2222301.1,2010. Shapiro, M. A. and Keyser, D.: Fronts, Jet Streams and
Neale,R.B.andHoskins,B.J.:AstandardtestforAGCMsinclud- the Tropopause, in: Extratropical Cyclones, edited
ingtheirphysicalparametrizations:I:Theproposal,Atmos.Sci. by: American Meteorological Society, Boston, MA,
Lett.,1,101–107,https://doi.org/10.1006/asle.2000.0022,2000. https://doi.org/10.1007/978-1-944970-33-8_10,1990.
Owen, L. E., Catto, J. L., Stephenson, D. B., and Dun- Simmons, A. J. and Hoskins, B. J.: The life cy-
stone, N. J.: Compound precipitation and wind extremes cles of some nonlinear baroclinic waves, J. At-
over Europe and their relationship to extratropical cy- mos. Sci., 35, 414–432, https://doi.org/10.1175/1520-
clones, Weather and Climate Extremes, 33, 100342, 0469(1978)035<0414:TLCOSN>2.0.CO;2,1978.
https://doi.org/10.1016/j.wace.2021.100342,2021. Sinclair, M. R. and Revell, M. J.: Classification and
Pedregosa,F.,Varoquaux,G.,Gramfort,A.,Michel,V.,Thirion,B., Composite Diagnosis of Extratropical Cyclogene-
Grisel,O.,Blondel,M.,Prettenhofer,P.,Weiss,R.,Dubourg,V., sis Events in the Southwest Pacific, Mon. Weather
Vanderplas,J.,Passos,A.,Cournapeau,D.,Brucher,M.,Perrot, Rev., 128, 1089–1105, https://doi.org/10.1175/1520-
M.,andDuchesnay,E.:Scikit-learn:MachinelearninginPython, 0493(2000)128<1089:CACDOE>2.0.CO;2,2000.
J.Mach.Learn.Res.,12,2825–2830,2011. Sinclair, V. and Catto, J.: Extra-tropical cyclone statistics
Pfahl,S.andSprenger,M.:Ontherelationshipbetweenextratrop- from OpenIFS aquaplanet simulations, Zenodo [data set],
icalcycloneprecipitationandintensity,Geophys.Res.Lett.,43, https://doi.org/10.5281/zenodo.8027867,2023.
1752–1758,https://doi.org/10.1002/2016GL068018,2016. Sinclair,V.A.,Rantanen,M.,Haapanala,P.,Räisänen,J.,andJärvi-
Pfahl, S. and Wernli, H.: Quantifying the Relevance of Cy- nen, H.: The characteristics and structure of extra-tropical cy-
clones for Precipitation Extremes, J. Climate, 25, 6770–6780, clones in a warmer climate, Weather Clim. Dynam., 1, 1–25,
https://doi.org/10.1175/JCLI-D-11-00705.1,2012. https://doi.org/10.5194/wcd-1-1-2020,2020.
Pfahl, S., Madonna, E., Boettcher, M., Joos, H., and Wernli, H.: Stoelinga,M.T.:Apotentialvorticity-basedstudyoftheroleofdi-
WarmConveyorBeltsintheERA-InterimDataset(1979–2010). abaticheatingandfrictioninanumericallysimulatedbaroclinic
Part II: Moisture Origin and Relevance for Precipitation, J. cyclone,Mon.WeatherRev.,124,849–874,1996.
Climate,27,27–40,https://doi.org/10.1175/JCLI-D-13-00223.1, Taylor, K. E., Stouffer, R. J., and Meehl, G. A.: An overview of
2014. CMIP5andtheexperimentdesign,B.Am.Meteorol.Soc.,93,
Pfahl,S.,O’Gorman,P.A.,andSingh,M.S.:Extratropicalcyclones 485–498,2012.
in idealized simulations of changed climates, J. Climate, 28, Thorncroft,C.,Hoskins,B.,andMcIntyre,M.:Twoparadigmsof
9373–9392,https://doi.org/10.1175/JCLI-D-14-00816.1,2015. baroclinic-wave life-cycle behaviour, Q. J. Roy. Meteor. Soc.,
Priestley, M. D. K. and Catto, J. L.: Future changes in 119,17–55,https://doi.org/10.1002/qj.49711950903,1993.
the extratropical storm tracks and cyclone intensity, wind Vessey, A. F., Hodges, K. I., Shaffrey, L. C., and Day, J. J.:
speed, and structure, Weather Clim. Dynam., 3, 337–360, The composite development and structure of intense synoptic-
https://doi.org/10.5194/wcd-3-337-2022,2022. scale Arctic cyclones, Weather Clim. Dynam., 3, 1097–1112,
Priestley,M.D.,Ackerley,D.,Catto,J.L.,Hodges,K.I.,McDon- https://doi.org/10.5194/wcd-3-1097-2022,2022.
ald,R.E.,andLee,R.W.:Anoverviewoftheextratropicalstorm Yettella,V.andKay,J.E.:Howwillprecipitationchangeinextra-
tracks in CMIP6 historical simulations, J. Climate, 33, 6315– tropicalcyclonesastheplanetwarms?Insightsfromalargeini-
6343,https://doi.org/10.1175/JCLI-D-19-0928.1,2020. tialconditionclimatemodelensemble,Clim.Dynam.,49,1765–
Rantanen,M.,Räisänen,J.,Sinclair,V.A.,andJärvinen,H.:Sensi- 1781,https://doi.org/10.1007/s00382-016-3410-2,2017.
tivityofidealisedbaroclinicwavestomeanatmospherictemper- Zhang, Z. and Colle, B. A.: Impact of Dynamically Down-
ature and meridional temperature gradient changes, Clim. Dy- scaling Two CMIP5 Models on the Historical and Fu-
nam.,52,2703–2719,https://doi.org/10.1007/s00382-018-4283- ture Changes in Winter Extratropical Cyclones along the
3,2019. East Coast of North America, J. Climate, 31, 8499–8525,
Rantanen, M., Karpechko, A. Y., Lipponen, A., Nordling, K., https://doi.org/10.1175/JCLI-D-18-0178.1,2018.
Hyvärinen, O., Ruosteenoja, K., Vihma, T., and Laaksonen,
A.: The Arctic has warmed nearly four times faster than the
globesince1979,CommunicationsEarth&Environment,3,168,
https://doi.org/10.1038/s43247-022-00498-3,2022.
Reboita, M. S., Reale, M., da Rocha, R. P., Giorgi, F., Giuliani,
G., Coppola, E., Nino, R. B. L., Llopart, M., Torres, J. A.,
andCavazos,T.:Futurechangesinthewintertimecyclonicac-
tivity over the CORDEX-CORE southern hemisphere domains
in a multi-model approach, Clim. Dynam., 57, 1533–1549,
https://doi.org/10.1007/s00382-020-05317-z,2021.
https://doi.org/10.5194/wcd-4-567-2023 WeatherClim.Dynam.,4,567–589,2023