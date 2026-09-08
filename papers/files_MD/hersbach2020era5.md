Received:3September2019 Revised:17March2020 Accepted:30March2020 Publishedon:15June2020
DOI:10.1002/qj.3803
RESEARCH ARTICLE
The ERA5 global reanalysis
HansHersbach1 BillBell1 PaulBerrisford1 ShojiHirahara2 AndrásHorányi1 Joaquín
Muñoz-Sabater1 JulienNicolas1 CarolePeubey1 RalucaRadu1 Dinand
Schepers1 AdrianSimmons1 CornelSoci1 SalehAbdalla1 Xavier
Abellan1 GianpaoloBalsamo1 PeterBechtold1 GionataBiavati1 Jean
Bidlot1 MassimoBonavita1 GiovannaDeChiara1 PerDahlgren3 DickDee1 Michail
Diamantakis1 RossanaDragani1 JohannesFlemming1 RichardForbes1 Manuel
Fuentes1 AlanGeer1 LeoHaimberger4 SeanHealy1 RobinJ.Hogan1 Elías
Hólm1 MartaJanisková1 SarahKeeley1 PatrickLaloyaux1 PhilippeLopez1 Cristina
Lupu1 GaborRadnoti1 PatriciadeRosnay1 IrynaRozum1 Freja
Vamborg1 SebastienVillaume1 Jean-NoëlThépaut1
1EuropeanCentreforMedium-Range Abstract
WeatherForecasts,Reading,UK
Within the Copernicus Climate Change Service (C3S), ECMWF is producing
2JapanMeteorologicalAgency,Tokyo,
the ERA5 reanalysis which, once completed, will embody a detailed record of
Japan
theglobalatmosphere,landsurfaceandoceanwavesfrom1950onwards.This
3TheNorwegianMeteorologicalInstitute,
Oslo,Norway new reanalysis replaces the ERA-Interim reanalysis (spanning 1979 onwards)
4DepartmentofMeteorologyand which was started in 2006. ERA5 is based on the Integrated Forecasting Sys-
Geophysics,UniversitätWien,Vienna,
tem (IFS) Cy41r2 which was operational in 2016. ERA5 thus benefits from a
Austria
decadeofdevelopmentsinmodelphysics,coredynamicsanddataassimilation.
Correspondence Inadditiontoasignificantlyenhancedhorizontalresolutionof31km,compared
H.Hersbach,ECMWF,ShinfieldPark,
to80kmforERA-Interim,ERA5hashourlyoutputthroughout,andanuncer-
ReadingRG29AX,Reading,UK.
Email:hans.hersbach@ecmwf.int tainty estimate from an ensemble (3-hourly at half the horizontal resolution).
This paper describes the general set-up of ERA5, as well as a basic evalua-
Fundinginformation
tionofcharacteristicsandperformance,withafocusonthedatasetfrom1979
EuropeanUnionthroughtheCopernicus
onwardswhichiscurrentlypubliclyavailable.Re-forecastsfromERA5analyses
ClimateChangeService
show a gain of up to one day in skill with respect to ERA-Interim. Compari-
sonwithradiosondeandPILOTdatapriortoassimilationshowsanimproved
fit for temperature, wind and humidity in the troposphere, but not the strato-
sphere. A comparison with independent buoy data shows a much improved
fit for ocean wave height. The uncertainty estimate reflects the evolution of
the observing systems used in ERA5. The enhanced temporal and spatial res-
olution allows for a detailed evolution of weather systems. For precipitation,
global-meancorrelationwithmonthly-meanGPCPdataisincreasedfrom67%
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttributionLicense,whichpermitsuse,distributionandreproductioninanymedium,providedthe
originalworkisproperlycited.
©2020TheAuthors.QuarterlyJournaloftheRoyalMeteorologicalSocietypublishedbyJohnWiley&SonsLtdonbehalfoftheRoyalMeteorologicalSociety.
QJRMeteorolSoc.2020;146:1999–2049. wileyonlinelibrary.com/journal/qj 1999

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2000 |     |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
to77%.Ingeneral,low-frequencyvariabilityisfoundtobewellrepresentedand
from 10hPa downwards general patterns of anomalies in temperature match
thosefromtheERA-Interim,MERRA-2andJRA-55reanalyses.
KEYWORDS
climatereanalysis,CopernicusClimateChangeService,dataassimilation,ERA5,historicalobser-
vations
| 1 INTRODUCTION |     |     |     |     |     |     | Inrecentyears,ECMWFhasalsoundertakenthesys- |            |     |                  |     |             |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | ---------- | --- | ---------------- | --- | ----------- | --- |
|                |     |     |     |     |     |     | tematic                                     | production | of  | ocean reanalyses |     | culminating | in  |
Theroleofreanalysesinclimatemonitoringapplications themostrecent,ORAS5.Althoughoriginallytheseocean
isnowwidelyrecognized.ECMWF'sERA-Interimreanal- reanalyses were passive applications of the atmospheric
|           |         |       |          |           |       |          | reanalyses | in which | the | latter provided |     | the atmospheric |     |
| --------- | ------- | ----- | -------- | --------- | ----- | -------- | ---------- | -------- | --- | --------------- | --- | --------------- | --- |
| ysis (Dee | et al., | 2011) | has been | routinely | used, | together |            |          |     |                 |     |                 |     |
with other datasets, as input to the WMO annual assess- forcingfortheformer,ORAS5wentastepfurther.Forthe
mentoftheStateoftheClimateandintheassessmentscar- first time, the selection of consistent records for SST and
riedoutbytheIPCC1.ERA-InterimandtheearlierERA-40 SIC took into account the needs for atmospheric reanal-
reanalysis(Uppalaetal.,2005)havealsobeenaresource yses (Hirahara et al., 2016). Hence, the SST records are
commontobothORAS5andERA5.
fortheproductionofECVs(Bojinskietal.,2014))andCli-
mateIndicatorsrecommendedbytheGCOS.Byoptimally WithintheEuropeanCommission-fundedGEMSand
combining observations and models, reanalyses indeed MACC projects, and now the Copernicus Atmosphere
provideconsistent“mapswithoutgaps"ofECVsandstrive Monitoring Service, ECMWF has also produced reanaly-
toensureintegrityandcoherenceintherepresentationof ses of atmospheric composition in 2008, 2010 and 2018,
respectively(Table1).
themainEarthsystemcycles(e.g.,water,energy).
Reanalyses have found a wide application in atmo- Preceding and in parallel with the development
sphericsciences,notleastinoperationalweathercentres of ERA5, ECMWF has produced centennial reanaly-
where, for example, reanalyses are used to assess the ses within the EC-funded ERA-CLIM and ERA-CLIM2
impact of observing system changes, to gauge progress research projects, involving international consortia and
|              |     |              |     |               |     |           | coordinated | by  | ECMWF. | One | aspect | was the | provision |
| ------------ | --- | ------------ | --- | ------------- | --- | --------- | ----------- | --- | ------ | --- | ------ | ------- | --------- |
| in modelling | and | assimilation |     | capabilities, | and | to obtain |             |     |        |     |        |         |           |
state-of-the-art climatologies to evaluate forecast-error of boundary datasets over the oceans (SST and SIC pro-
| anomalies. |     |     |     |     |     |     | videdbytheMetOfficeHadleyCentre)andforcingterms |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
ECMWF has a long history with reanalysis, as indi- in radiation (from CMIP5) to provide a good represen-
cated in Table 1, and ERA5 is the fifth generation of tation of their evolution over the 20th century. This was
|     |     |     |     |     |     |     | successfully | implemented |     | in ERA-20CM, |     | a century-long |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ------------ | --- | -------------- | --- |
atmosphericreanalysistobeproduced.Activitiesonatmo-
sphericreanalysisstartedin1979withtheFGGEproject, ten-member ensemble model-only integration. The next
followed by the production of ERA-15 in the mid 1990s, step was the production of a century-long reanalysis,
ERA-40 from 2001 to 2003, and ERA-Interim from 2006 ERA-20C,usingsurfacepressureandmarinewindobser-
to2019.Successiveatmosphericreanalyseshavetypically vationsonly(Polietal.(2016)).Theproductionofsucha
|                |     |            |             |      |               |     | model-based | reanalysis |     | that extends | back | more | than one |
| -------------- | --- | ---------- | ----------- | ---- | ------------- | --- | ----------- | ---------- | --- | ------------ | ---- | ---- | -------- |
| offered higher |     | horizontal | resolution, | more | sophisticated |     |             |            |     |              |      |      |          |
DA schemes and have benefitted from the continuous century was first pursued in the 20CR Project (Compo
development of forecast models. All include a land com- etal.,2006)atNOAA'sEarthSystemsResearchLaboratory,
ponent and, from ERA-40 onwards, ocean surface wave where a reanalysis spanning the period 1871–2010 was
andatmosphericozoneproductshavealsobeenincluded. conducted(Compoetal.,2011).Anexperimentalreanaly-
sisfrom1939to1967usinginadditionupper-airtemper-
| Beyond | ECMWF, | several | groups | produce | global | atmo- |     |     |     |     |     |     |     |
| ------ | ------ | ------- | ------ | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
spheric reanalyses and the most recent products are the atureandwindwasalsoproduced(Hersbachetal.,2017).
MERRA-2reanalysis(Gelaroetal.,2017)fromtheNASA In the ERA-CLIM2 project, research towards coupling
GMAO, JRA-55 (Kobayashi et al., 2015) produced by the withtheoceanculminatedinacentury-longten-member
JMAandCFSR(version2)producedbyNCEP(Sahaetal., reanalysis (CERA-20C) which is based on outer-loop
|     |     |     |     |     |     |     | coupling | between | the | ocean and | atmosphere, |     | and an |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --------- | ----------- | --- | ------ |
2014).
1AllacronymsaredefinedintheGlossary(Table8).

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
HERSBACHetal. 2001
| TABLE 1 ECMWFreanalyses |     |      |              |          |     |
| ----------------------- | --- | ---- | ------------ | -------- | --- |
|                         |     | Grid | Assimilation | IFSmodel |     |
Reanalysis Periodcovered resolution scheme cycle(year) Reference
Atmosphericreanalyses
| FGGE        | 1979         | 208km | OI     | (1980)     | Bengtssonetal.(1982) |
| ----------- | ------------ | ----- | ------ | ---------- | -------------------- |
| ERA-15      | 1979–1994    | 125km | OI     | 13r4(1995) | Gibsonetal.(1999)    |
| ERA-40      | 1957–2002    | 125km | 3D-Var | 23r4(2001) | Uppalaetal.(2005)    |
| ERA-Interim | 1979–2019    | 80km  | 4D-Var | 31r2(2006) | Deeetal.(2011)       |
| ERA5        | 1950–present | 31km  | 4D-Var | 41r2(2016) | Thispaper            |
Oceanreanalyses
| ORAS3 | 1959–2012 | 1.0◦ | OI         | (2006) | Balmasedaetal.(2008) |
| ----- | --------- | ---- | ---------- | ------ | -------------------- |
| ORAS4 | 1959–2018 | 1.0◦ | 3DVar-FGAT | (2010) | Balmasedaetal.(2013) |
0.25◦
| ORAS5 | 1979–present |     | 3DVar-FGAT | (2016) | Zuoetal.(2018) |
| ----- | ------------ | --- | ---------- | ------ | -------------- |
Atmosphericcompositionreanalyses
| MACC | 2003–2012 | 80km | 4D-Var | 36r1(2010) | Innessetal.(2013) |
| ---- | --------- | ---- | ------ | ---------- | ----------------- |
CAMS-Interim 2003–2018 110km 4D-Var 40r2(2014) Flemmingetal.(2017)
| CAMS | 2003–present | 80km | 4D-Var | 42r1(2016) | Innessetal.(2019) |
| ---- | ------------ | ---- | ------ | ---------- | ----------------- |
Centennialreanalysesandmodel-onlyclimateintegrations
ERA-20CM 1899–2010 125km 4D-Var 38r1(2012) Hersbachetal.(2015)
| ERA-20C | 1900–2010 | 125km | 4D-Var | 38r1(2012) | Polietal.(2016) |
| ------- | --------- | ----- | ------ | ---------- | --------------- |
CERA-20C 1901–2010 125km 4D-Var 41r2(2016) Laloyauxetal.(2018)
CERA-SAT 2008–2016 65km 4D-Var 42r1(2016) Schepersetal.(2018)
eight-year reanalysis (CERA-SAT) for the current-day uncertainty information. This uncertainty information
full observing system with the same resolution as the is obtained from the underlying ten-member ensemble
ensemblecomponentofERA5.Collectively,thesedevelop- 4D-VarDAsystem.
ments laid the foundations for future coupled reanalyses Another innovative aspect is a timely, preliminary
atECMWF. product that is available within 5days of real time. It is
The developments outlined above also allow the replacedbyamorethoroughlyquality-checkedfinalprod-
extension of ERA5 further back in time (to 1950) than uct two months later. In practice, though, it is expected
ERA-Interim,thoughthefocusforthispaperistheperiod that both products will rarely differ, and in case they do
commontoboth,1979–2019.ERA5replacestheverypop- (due to considerable errors found in the early release),
ular ERA-Interim reanalysis, which was progressively userswillbenotified.
becomingoutdatedandwasstoppedattheendofAugust ThestepforwardwithERA5isillustratedbyFigure1,
2019. ERA5 is a highly visible activity within the Coper- whichshowsagainofuptoonedayinskillofre-forecasts
nicusClimateChangeService(C3S;Thépautetal.,2018), started from ERA5 (thick lines) analyses using the
where it provides an improved and consistent record for ERA5 model, compared to the re-forecasts run using the
a large number of ECVs for the C3S Climate Data Store ERA-Interim system (thin lines). The distinct improve-
(CDS;Raoultetal.,2017).Besidesaconsiderableincrease mentoriginatesfromabetterforecastmodel(whichisan
in resolution (both in the horizontal and vertical) and integralpartoftheassimilationsystemaswell)andinpar-
the benefit of 10 years of model and data assimilation ticulartheimprovedanalysesfromwhichtheseforecasts
| (DA)developments,ERA5providesanenhancednumber |     |     | arestarted. |     |     |
| --------------------------------------------- | --- | --- | ----------- | --- | --- |
of output parameters (such as the 100m wind product), This paper provides an overview of the configura-
hourly high-resolution output throughout and 3-hourly tionofERA5andabasicdescriptionofitscharacteristics

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2002 |     |     |     |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
Range (days) when 365-day mean 500hPa height AC (%) falls below threshold 2 ERA5 CONFIGURATION
(a) Northern hemisphere
|     |     |     |     |     | ERA5 |     | ERA-Interim |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
9
|     |     |     |     |     |     |     |     | 2.1 | Generaloverview |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
60%
8
7
Thissectionprovidesanoverviewoftheconfigurationof
| 6   |     |     |     |     |     |     | 80% |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ERA5.AsummaryisdisplayedinTable2whichincludes
5
acomparisonwithERA-Interim.
| 4   |     |     |     |     |     |     | 95% |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThestartingpointforERA5isIFSCy41r2,whichwas
3
usedintheECMWFoperationalmedium-rangeforecast-
2
1980 1985 1990 1995 2000 2005 2010 2015 ing system from 8 March to 21 November 2016. With
(b) Southern hemisphere respect to Cy31r2 on which ERA-Interim is based, this
| 9   |     |     |     |     |     |     |     | incorporates10yearsofR&Dforallitscomponents(atmo- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
60%
| 8   |     |     |     |     |     |     |     | sphere,land,oceanwaves,observationoperatorsandaddi- |     |          |     |       |        |              |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | -------- | --- | ----- | ------ | ------------ | --- |
| 7   |     |     |     |     |     |     |     | tional observations;                                |     | Sections |     | 4 and | 5) and | improvements |     |
80%
| 6   |     |     |     |     |     |     |     | in the DA   | methodology, |        | which | is now    | based   | on     | a hybrid |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------ | ----- | --------- | ------- | ------ | -------- |
|     |     |     |     |     |     |     |     | incremental | 4D-Var       | system |       | (Bonavita | et al., | 2016). | ERA5     |
5
| 4   |     |     |     |     |     |     |     | contains | an ensemble |     | component |     | (EDA; | Isaksen | et al., |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --------- | --- | ----- | ------- | ------- |
95%
| 3   |     |     |     |     |     |     |     | 2010)ofonecontrolandnineperturbedmemberswhich |                  |     |           |     |         |               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | ---------------- | --- | --------- | --- | ------- | ------------- | --- |
|     |     |     |     |     |     |     |     | provide                                       | background-error |     | estimates |     | for the | deterministic |     |
2
| 1980 | 1985 | 1990 | 1995 | 2000 | 2005 | 2010 | 2015 |     |     |     |     |     |     |     |     |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
HRESDAsystem.TheEDAsystemprovidesestimatesof
|        |     |                                      |     |     |     |     |     | analysis | and short-range |     | forecast |     | uncertainty | which | are |
| ------ | --- | ------------------------------------ | --- | --- | --- | --- | --- | -------- | --------------- | --- | -------- | --- | ----------- | ----- | --- |
| FIGURE | 1   | Range(days)atwhichrunning365-daymean |     |     |     |     |     |          |                 |     |          |     |             |       |     |
anomalycorrelationsof500hPaheightforecastsfrom0000and consideredtorepresenttheevolutionoftheerrorsinthe
1200UTCreach95%(green),80%(orange)and60%(blue),for(a) HRESsystem.Thisallowsfortheestimationofuncertain-
theextratropicalNorthernand(b)SouthernHemispheres,from tiesinthereanalysisproducts.Aconciseassessmentofthis
1979onwards.TheheaviestlinesdenoteERA5,andthethinlines innovativefeatureisprovidedinSection7.1.Detailsofthe
ERA-Interim.ShadingdenotesthedifferencebetweenERA5and EDAsystemaredeferredtoSection2.4.Beforethen,focus
ERA-Interim.TheimprovementofERA5withrespectto
isontheHRESsystem.
ERA-Interimisthoughttobedominatedbyabetteranalysisat
AlthoughozoneispartoftheEarth-systemcomponent
shortforecastranges,whiletowardslongerrangestheimproved
|     |     |     |     |     |     |     |     | atmosphere, | for | technical | reasons |     | in this | paper | the term |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ------- | --- | ------- | ----- | -------- |
forecastmodelwillalsocontribute
atmospherewillbemainlyusedtodenotethedynamical
andmoistthermodynamicalstateoftheatmosphere.The
specificsoftheozoneanalysisarediscussedseparately.
| and performance. |             | In    | general,     | results | cover           | January    | 1979 |         |              |              |     |       |        |           |         |
| ---------------- | ----------- | ----- | ------------ | ------- | --------------- | ---------- | ---- | ------- | ------------ | ------------ | --- | ----- | ------ | --------- | ------- |
|                  |             |       |              |         |                 |            |      | The     | assimilation | system       |     | makes | use of | 12-hourly | win-    |
| to August        | 2019,       | which | corresponds  |         | with            | the period | for  |         |              |              |     |       |        |           |         |
|                  |             |       |              |         |                 |            |      | dows in | which        | observations |     | are   | used   | from      | 0900 to |
| which            | ERA-Interim |       | is available |         | for comparison. |            | The  |         |              |              |     |       |        |           |         |
2100UTC(inclusive)andfrom2100to0900UTC(inclu-
structure is as follows. The general set-up is described sive) the next day. The resulting analysis fields follow
| in Section | 2.       | Details | on the  | ERA5 | production |         | and data |          |           |        |     |            |     |         |        |
| ---------- | -------- | ------- | ------- | ---- | ---------- | ------- | -------- | -------- | --------- | ------ | --- | ---------- | --- | ------- | ------ |
|            |          |         |         |      |            |         |          | the time | evolution | within |     | the window |     | and are | stored |
| access are | provided | in      | Section | 3. A | concise    | summary | of       |          |           |        |     |            |     |         |        |
hourly.Informationgatheredwithineachanalysiswindow
| the model | improvements |                | that | took    | place       | between | the |                |     |          |          |           |     |           |           |
| --------- | ------------ | -------------- | ---- | ------- | ----------- | ------- | --- | -------------- | --- | -------- | -------- | --------- | --- | --------- | --------- |
|           |              |                |      |         |             |         |     | is transported | by  | a short  | forecast | initiated |     | from      | the anal- |
| ECMWF     | IFS          | cycle releases |      | between | ERA-Interim |         | and |                |     |          |          |           |     |           |           |
|           |              |                |      |         |             |         |     | ysis fields    | 9hr | into the | window,  | that      | is, | from 1800 | and       |
ERA5 is given in Section 4. Section 5 details the obser- 0600UTC,whereitprovidesthestartingpoint(firstguess)
| vations | which | were assimilated |     | in  | ERA5, | a considerable |     |     |     |     |     |     |     |     |     |
| ------- | ----- | ---------------- | --- | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forthenextassimilation.Intheseforecasts(whicharealso
| number  | of which   | originate   |     | from | reprocessed  |     | datasets. |            |           |          |            |       |         |          |         |
| ------- | ---------- | ----------- | --- | ---- | ------------ | --- | --------- | ---------- | --------- | -------- | ---------- | ----- | ------- | -------- | ------- |
|         |            |             |     |      |              |     |           | archived   | hourly)   | all ERA5 | components |       | are     | coupled. | The     |
| Section | 6 provides | information |     | on   | the ingested |     | SST, sea  |            |           |          |            |       |         |          |         |
|         |            |             |     |      |              |     |           | atmosphere | generates |          | ocean      | waves | through | the      | surface |
ice,andexternalforcingappliedintheradiationscheme.
|     |     |     |     |     |     |     |     | wind stress, | while | the | waves | influence | the | atmospheric |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | ----- | --------- | --- | ----------- | --- |
The paper continues with some diagnostics from ensem- boundary layer via sea-state dependencies in the surface
| ble spread, | departure |     | statistics | and | analysis | increments |     |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
roughness.Atwo-wayinteractionalsoexistsbetweenthe
(Section7).Abasicassessmentofcharacteristicsismade
atmosphereandland(Section4.3).
| in Section | 8                  | (weather) | and | Section | 9          | (climate). | This |            |             |         |       |             |         |        |         |
| ---------- | ------------------ | --------- | --- | ------- | ---------- | ---------- | ---- | ---------- | ----------- | ------- | ----- | ----------- | ------- | ------ | ------- |
|            |                    |           |     |         |            |            |      | The        | interaction | between |       | ozone       | and the | (rest  | of the) |
| includes   | an intercomparison |           |     | with    | the global | reanalyses |      |            |             |         |       |             |         |        |         |
|            |                    |           |     |         |            |            |      | atmosphere | is one-way. |         | Ozone | is advected |         | by the | atmo-   |
MERRA-2 and JRA-55. Section 10 summarizes strengths spheric flow. In addition, the prognostic ozone model
| and weaknesses |     | of  | ERA5 | and ends | with | concluding |     |          |                    |     |     |        |               |     |       |
| -------------- | --- | --- | ---- | -------- | ---- | ---------- | --- | -------- | ------------------ | --- | --- | ------ | ------------- | --- | ----- |
|                |     |     |      |          |      |            |     | includes | the representation |     |     | of the | stratospheric |     | ozone |
remarks.
|     |     |     |     |     |     |     |     | chemistry | based | on the | Cariolle |     | and Teyssèdre |     | (2007) |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------ | -------- | --- | ------------- | --- | ------ |

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
HERSBACHetal. 2003
TABLE 2 OverviewofcharacteristicsofERA5
|                            | ERA-Interim     | ERA5                    |
| -------------------------- | --------------- | ----------------------- |
| Publiclyavailablenow       | 1979–August2019 | 1979onwards             |
| Expectedin2020             |                 | 1950–1978               |
| Availabilitybehindrealtime | 2–3months       | 2–3months(finalproduct) |
5days(preliminaryproduct)
| Modelcycle(year)      | Cy31r2(2006)     | Cy41r2(2016)           |
| --------------------- | ---------------- | ---------------------- |
| AtmosphericDA         | 12hr4D-Var       | 12hr4D-Varensemble     |
| Windowfor0000,1200UTC | (15 ,03],(03,15] | (21 ,09],(09,21]       |
|                       | day−1            | day−1                  |
| Modelinput            | AsinERA-40,      | Appropriateforclimate, |
(radiationandsurface) inconsistentSST e.g.,evolutiongreenhousegases,
|                   | andseaice      | aerosols,SSTandseaice |
| ----------------- | -------------- | --------------------- |
| Spatialresolution | 79kms(TL255)   | 31km(TL639),HRES      |
|                   | 60levelsto10Pa | 137levelsto1Pa        |
|                   | 1◦             | 0.36◦                 |
Oceanwaves
| Inner-loopresolution | TL95,TL159 | TL95,TL159,TL255          |
| -------------------- | ---------- | ------------------------- |
| Land-surfacemodel    | TESSEL     | HTESSEL                   |
| SoilmoistureDA       | 1D-OI      | SEKF                      |
| SnowDA               | Cressman   | 2D-OI                     |
| Uncertaintyestimate  | None       | Fromthe4D-Varensemble,EDA |
10membersat63km(TL319),
oceanwaves1◦,
TL127,TL159innerloops
| Outputfrequency | 6-hourlyforanalyses, | Hourlythroughout      |
| --------------- | -------------------- | --------------------- |
|                 | 3-hourlyforforecasts | (uncertainty3-hourly) |
Outputparameters 84(sfc),25(wave),27(ua) 205(sfc),46(wave),30(ua)
Extraobservations FollowingERA-40,GTS Inaddition,latestinstruments
| ReprocessedFCDRs       | Some                  | Manymore(Table4)          |
| ---------------------- | --------------------- | ------------------------- |
| Radiativetransfermodel | RTTOVv7               | RTTOVv11                  |
|                        | Clear-skyassimilation | Partlyall-skyassimilation |
VarBC Radiancesonly Alsoozone,ground-basedradar–gaugecomposites,
aircrafttemperature,surfacepressure
| Radiosondecorrections | RAOBCORE | RICH |
| --------------------- | -------- | ---- |
Othercorrections scatterometer,altimeter scatterometer,altimeter
Note:DA=DataAssimilation;sfc=surface;ua=upperair.
parametrization scheme in which the time evolution is atmosphereviatheradiationscheme.Diagnosticozoneis
expressedasalinearexpansionwithrespecttothephoto- usedinstead(Section6.1).
chemicalequilibriumforthelocalvalueoftheozonemass The HRES assimilation system contains two main
mixing ratio, the local overhead ozone column, the local components: incremental 4D-Var (Courtier et al., 1994)
temperatureandanadditionaltermfortherapiddepletion fortheatmosphereplusozone,andthelandDA(LDAS).
associated with the emergence of the ozone hole. How- Theinteractionbetweentheseisanexampleofweakcou-
ever, the ERA5 prognostic ozone has no feedback on the pling (Penny et al., 2017), where the influence from the

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2004 |     |      |     |      |     |     |            |       |           |     |          | HERSBACHetal. |            |
| ---- | --- | ---- | --- | ---- | --- | --- | ---------- | ----- | --------- | --- | -------- | ------------- | ---------- |
|      |     |      |     |      |     |     | complete). | Their | ingestion |     | includes | a minor       | interpola- |
|      |     | LAND |     | ATMO |     |     |            |       |           |     |          |               |            |
tionstepwhichinvolvesregriddingontotheERA5model
|     |     |     |     |      |     |     | grid, subject              | to                             | its land–sea |     | mask and | some cross-checks |     |
| --- | --- | --- | --- | ---- | --- | --- | -------------------------- | ------------------------------ | ------------ | --- | -------- | ----------------- | --- |
|     |     |     |     | WAVE |     |     | betweenthesetwoquantities. |                                |              |     |          |                   |     |
|     |     |     |     |      |     |     | 2.2                        | 4D-Varincludingvariationalbias |              |     |          |                   |     |
|     |     |     | 4D- |      |     |     | correction(VarBC)          |                                |              |     |          |                   |     |
VAR
LDAS
Theobjectiveof4D-Varistofindthebestestimateofthe
stateoftheatmospherewithinanassimilationtimewin-
|     |     |     |     |     |     |     | dow, given | a   | background | forecast | xb  | valid at the | start of |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | -------- | --- | ------------ | -------- |
yo
LAND ATMO SST the window and observations falling within that win-
|     |     |     |     |     |     |     | dow. Here, | approximately |     | following |     | the unified | notation |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --------- | --- | ----------- | -------- |
proposedbyIdeetal.(1997),anyxcontainsthemodeldata
|     |     | OI  |     | WAVE | ICE |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
atoneparticulartimeacrossalllocations,levelsandvari-
ables,andanyycontainsalltheavailableobservationsin
thewindow.Theaimistoreducethemisfitdbetweenthe
observationsandtheirmodelledequivalentsy,thatis,
Analysis
|        |     |                                          |     |     |     |     |     |     |     | d=yo−y, |     |     | (1) |
| ------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
| FIGURE | 2   | AssimilationdiagramforERA-InterimandERA5 |     |     |     |     |     |     |     |         |     |     |     |
regardingtheatmosphereincludingozone(ATMO),landsurface consistent with the estimated uncertainty of the back-
(LAND),oceanwaves(WAVE),seasurfacetemperature(SST)and ground and observations. This is done by adjusting the
seaice(ICE).Largeboxesrepresentouter-loopintegrations state of the atmosphere at the start of the assimilation
(trajectories)wheretheindicateddomainsarecoupled.Triangles windowxand,recognisingthepossibilityofbiasinobser-
representtheland-dataassimilation(LDAS)andoceanwave
vations,byadjustingavectorofparameters𝜷thatdescribe
optimalinterpolation(OI),whilecirclescorrespondto4D-Varinner
|     |     |     |     |     |     |     | such biases | b   | in observation |     | space. | Hence the | vector of |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | ------ | --------- | --------- |
loops.TheoceanwaveOIassimilationisperformedonlyinsidethe
simulatedobservationsiscomputedas
finaltrajectory.ForERA5theLDASassimilationisanexampleof
weakcoupling(Pennyetal.,2017)wheretheinfluencefromland
|     |     |     |     |     |     |     |     |     | y=H(x)+b(x,𝜷). |     |     |     | (2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
surfaceandotherobservationsisonlymixedinthenextanalysis
windowviathecoupledshortforecastfromthecurrent
| analysis |     |     |     |     |     |     | In4D-VartheobservationoperatorH()andbiasmodel |        |         |                  |      |           |           |
| -------- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | ------ | ------- | ---------------- | ---- | --------- | --------- |
|          |     |     |     |     |     |     | b() include                                   | the    | model   | integration      | from | the start | of the    |
|          |     |     |     |     |     |     | window                                        | to the | time of | the observation, |      | as well   | as inter- |
land surface and other observations is only mixed in the polationtotheobservationlocationandsimulatingofthe
nextanalysisviathecoupledshortforecastfromtheresult- observedquantity(suchasradiance)fromthemodelstate.
ingsub-analyses.Agraphicalrepresentationisprovidedin
|     |     |     |     |     |     |     | The bias | parameter | vector | consists | of  | a large | number of |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | -------- | --- | ------- | --------- |
Figure 2. The incremental formulation involves the step- small subsets (containing between 1 and 12 elements),
| wise minimization |     | of  | a linearized |     | quadratic 4D-Var | cost |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ------------ | --- | ---------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
eachofwhichdeterminesthebiasestimateforaparticu-
functionatreducedresolutionininnerloops,withnonlin- lar sub-group of observations, a ‘bias group’. Bias groups
earupdatesatfullresolutioninouterloops(trajectories). contain anything from a handful to tens of thousands of
| These latter | also | involve | the | integration | of the | coupled |     |     |     |     |     |     |     |
| ------------ | ---- | ------- | --- | ----------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
observations,collectingforexampleallthedatafromone
modeloverthelengthoftheassimilationwindow.ERA5 aircraftflightorfromonechannelofonesatelliteinstru-
| HRES uses | three | inner | loops, | and | its ensemble | compo- |     |     |     |     |     |     |     |
| --------- | ----- | ----- | ------ | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
mentononesatellite.InERA5allbiasmodelsarelinear
nent two inner loops. The ocean wave analysis, which is (Dee,2005),thatis,
| based on | optimal | interpolation |     | (OI) | is performed | in the |     |     |     |     | ∑   |     |     |
| -------- | ------- | ------------- | --- | ---- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
finaltrajectoryof4D-Var.Inordertomatchthehourlyout- b(x,𝜷)= p(x)𝛽,
|                                                 |     |     |     |     |     |     |     |     | i   |     | j   | j   | (3) |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| putofERA5,thisOIisnowperformedhourly,ratherthan |     |     |     |     |     |     |     |     |     |     | j∈S |     |     |
6-hourlyinERA-Interim.
|                                             |            |      |             |     |          |            | with p      | the linear | predictors |      | and where       | the sum | is lim- |
| ------------------------------------------- | ---------- | ---- | ----------- | --- | -------- | ---------- | ----------- | ---------- | ---------- | ---- | --------------- | ------- | ------- |
| TheLDASconsistsofanumberofsub-stepswhichare |            |      |             |     |          |            | j           |            |            |      |                 |         |         |
|                                             |            |      |             |     |          |            | ited to the | small      | subset     | S of | bias parameters | that    | relates |
| detailed                                    | in Section | 2.3. | Information |     | from SST | and SIC is |             |            |            |      |                 |         |         |
obtained from external level-4 sources (i.e., gridded and to the bias group to which one observation i belongs.

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |     |     |     |     |     |     |     |     |     |     |     |     | 2005 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
Each observation enters either exactly one bias group, quadraticcostfunctionsknownasinnerloops.Heremin-
or none at all, in which case S=∅ and no bias correc- imizations are performed where in Equation (4), d is
tion is applied. Such latter observations are also called approximatedbytheTaylorexpansion:
anchors.Thesimplestpredictorisaconstant,whileothers
d≃dn−H(x−xn)−P𝛿𝜷,
| can depend | on    | characteristics |                 | of  | the observations |     | and/or    |     |     |     |     |     | (5) |
| ---------- | ----- | --------------- | --------------- | --- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| the model  | state | at              | the observation |     | location         |     | and time. |     |     |     |     |     |     |
ERA-Interim was the first ECMWF reanalysis to include withdn =yo−H(xn)−b(xn,𝜷b),thenonlineardeparture
basedontheprevioustrajectorystartedatxn,𝜷bwherexn
variationalbiascorrections(DeeandUppala,2009).Itwas
appliedtoradiancedata.InERA5thishasbeenextended is the updated estimate from the previous minimization.
MatrixH=𝜕H∕𝜕xrepresentsalinearizationoftheobser-
| to ground-based |     | radar–gauge |     | composites, |     | total | column |     |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ----------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- |
ozone, aircraft temperature and surface pressure obser- vation operator and model equations around the most
vations.Thebiascorrectionforradiosondetemperatures, recent trajectory (indexed n) started from xn, performed
P=𝜕b∕𝜕𝜷
scatterometer backscatter and altimeter wave height is at lower inner-loop resolution (Table 2). is
prescribedindependentlyoftheDA. a matrix representation of the VarBC predictors from
4D-Varminimizesthecostfunction Equation (3). In expansion (5), the dependency of x on
|     |     |     |     |     |     |     |     | b hasbeenneglected.Note |     | that,incontrastto |     | the | model |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ----------------- | --- | --- | ----- |
J(𝜹x,𝜹𝜷)= J (𝜹x)+J (𝜹𝜷)+J (d)= state,theformulationforthebiasparametersisnotincre-
|     |     | b         | p   | o          |     |         |     |                                                  |     |     |     |     |     |
| --- | --- | --------- | --- | ---------- | --- | ------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|     | 1   |           |     | 1          |     | 1       |     | mental,thatis,theoptimizedincrementsareonlyadded |     |     |     |     |     |
|     |     | 𝜹xTB−1𝜹x+ |     | 𝜹𝜷TB𝜷−1𝜹𝜷+ |     | dTR−1d. | (4) |                                                  |     |     |     |     |     |
2 2 2 in the final trajectory which is conducted after the final
minimization.
Here 𝜹x=x−xb and 𝜹𝜷 =𝜷−𝜷b are the deviation, The first-guess departure is db from the background
or increment from the model and bias parameter back- trajectory,whiletheanalysisdeparturedaisthatfromthe
groundsxband𝜷b.Tisthetransposeoperator.Whilexbis
|     |     |     |     |     |     |     |     | final trajectory. | In some | implementations |     | of 4D-Var, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | --------------- | --- | ---------- | --- |
theresultofamodelintegrationstartingfromtheprevious termsbackgroundandfirstguesshavedifferentmeanings,
| analysis, | there | is no | bias evolution |     | model, | so  | 𝜷b are sim- |     |     |     |     |     |     |
| --------- | ----- | ----- | -------------- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- |
butheretheyareinterchangeable.Sointheremainderof
plythefinalvaluesfromthepreviousanalysis.Covariance thepaperwerefertodb asthefirst-guessdeparture.Note
matrices B, B𝜷 and R express the second-order moment thatbothdbanddaincludetheestimatedbiascorrections.
| error characteristics |     |     | in the | background |     | model | state, bias |     |     |     |     |     |     |
| --------------------- | --- | --- | ------ | ---------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
Observationsin4D-Vararesubjecttoarangeofqual-
parameter and (bias-adjusted) observations, respectively. itycontrols.Thisincludestheaprioriblacklistingofdata
ForsimplicityinEquation(4),onetermwithminoreffect,
|     |     |     |     |     |     |     |     | known to | be of poor quality, | and a | check | on the | size of |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------------- | ----- | ----- | ------ | ------- |
J ,hasbeenomitted;thisisadigitalfilterforreducinggrav- thefirst-guessdeparturedb (relativetoitsexpectedvalue,
c
itywavesintheincrements(GauthierandThépaut,2001). whichisestimatedfromtheobservationandbackground
Withtheexceptionofsomesatelliteradiances,correla-
|     |     |     |     |     |     |     |     | errors), both | of which | are applied in | the first | outer | loop |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | -------------- | --------- | ----- | ---- |
tionsbetweenobservationerrorsareneglected,thatis,R priortotheassimilation.Inaddition,observationscanbe
ismostlydiagonal.Ingeneral,ERA5usestheobservation
|     |     |     |     |     |     |     |     | downgraded | to have a | much reduced | weight | inside | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------ | ------ | ------ | --- |
errorsdescribedinPartIofECMWFR&D(2016).Correla- minimization,usingthemethodofvariationalqualitycon-
tionsbetweenbiasparametersarealsoneglected,thatis, trol (VarQC). This procedure is applied from the second
| B𝜷 is diagonal. |     | The | diagonal | elements |     | model | the rate at |               |         |             |        |      |        |
| --------------- | --- | --- | -------- | -------- | --- | ----- | ----------- | ------------- | ------- | ----------- | ------ | ---- | ------ |
|                 |     |     |          |          |     |       |             | minimization. | In ERA5 | it is based | on the | more | robust |
whichbiasparametersareallowedtochangeinoneassim- Hubernorm(TavolatoandIsaksen,2015)forconventional
ilationcycle.Formostsatellitedata,whereeachbiasgroup
data,whileforsatelliteradiancesthemethodofgrosserror
typically contains thousands of radiances, the weight is (AndersonandJärvinen,1999),asusedforallobservations
chosentobethatof5,000observations.Weightsforother inERA-Interim,isstillapplied.
biasparametersvary.Off-diagonaltermsinBdescribethe
|     |     |     |     |     |     |     |     | The blacklist | contains | rules that | vary from | the | exclu- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ---------- | --------- | --- | ------ |
correlation length-scales in the model background-error sion of certain channels on certain satellites, particular
estimate,aswellascorrelationsacrossvariables(suchas
dataoverspecificregionslikeland,seaorice,entireinstru-
between wind and temperature). At ECMWF, B is mod- ments for periods of known anomalies, and particular
elled using the wavelet formulation described by Fisher observablesfrominsituobservations(like10mwindover
| (2003), | where | background-error |     |     | correlations |     | are local- |            |              |                 |     |            |     |
| ------- | ----- | ---------------- | --- | --- | ------------ | --- | ---------- | ---------- | ------------ | --------------- | --- | ---------- | --- |
|         |       |                  |     |     |              |     |            | land). For | ERA5 this is | a blend between | the | blacklists | of  |
ized in both the spectral and the spatial domains. It is ERA-Interim(detailsinDeeetal.,2011)andtheECMWF
| evolved | dynamically |     | by the | underlying |     | ERA5 | ensemble |     |     |     |     |     |     |
| ------- | ----------- | --- | ------ | ---------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- |
operationalsystem(formorerecentperiods),augmented
(Section2.4). withrulesfornewlyingestedreprocesseddata.Inaddition,
As mentioned above, the incremental formulation of someextraexclusionswereadded,suchastheblacklisting
| 4D-Var | solves | Equation | (4) | through | a series | of  | linearised |     |     |     |     |     |     |
| ------ | ------ | -------- | --- | ------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
ofstuckpressuresensors(section3.4.2ofHersbachetal.,

2006 HERSBACHetal.
2018)and,basedonexperienceinERA-Interim,theexclu- and relative humidity, and for snow (depth and
sionoftheHIRSinstrumentonNOAA-18(asshownlater density),
inFigure5). 2. A point-wise Simplified Extended Kalman Filter
TheVarBCcoefficients𝜷 areinitializedbyeitherzero (SEKF; de Rosnay et al., 2013) for three soil moisture
or based on the most populated bin of first-guess depar- layersinthetop1mofsoil,and
turesdb.Inaddition,thereisthepossibilitytospinuptheir 3. Aone-dimensionalOIforsoil,iceandsnowtempera-
estimatesoveradesiredperiod,priortoactivelyusingthe ture.
datawithintheircorrespondingbiasgroups.Thisfacility
isusedforalargenumberofsatellitedata. Theseanalysesonlyusedatawheretheland–seamask
The 4D-Var cost function (4) is minimized for the is 50% or higher (i.e., including many islands). Over sea,
atmosphereandozonesimultaneously.However,theback- where2mtemperatureandhumidityarepurelydiagnos-
ground term B is univariate for ozone, that is, there are tic fields in the LDAS (i.e., they do not influence any
no cross-correlations with any other parts of the con- subsequentresults),incrementsaresettozero,sotheanal-
trol vector. In addition, changes in ozone advection due ysis equals the first-guess. This is an improvement on
to wind increments at the beginning of the assimilation ERA-Interim and avoids the incorrect spill-over of incre-
window or changes in ozone due to temperature pertur- mentsfromlocallandobservationsintotheoceans.Over
bations are neglected in the inner-loop minimizations. land,theseparametersarefedintothesoil-moistureanal-
The zeroing of the first dependency, which was already ysis,anddocycleinformationforwardintime.
in place for ERA-Interim, prevents anomalously large For soil moisture, the ERA5 hourly analysis products
wind increments in the stratosphere due to systematic followthetemporalevolutionoftheSEKFwithinthe12hr
model bias. Note that updates in wind and temperature window. Each OI analysis (components 1. and 3. above)
intheouterloopsdohaveaneffectonozone.Therefore, is based on 6-hr sub-windows along the 12hr assimila-
although reduced, the atmospheric analysis does influ- tion windows of 4D-Var, each only providing an analysis
encetheozoneanalysis.Ontheotherhand,ozoneinflu- at the central time of its ±3hr window, without mak-
encestheassimilationofotheratmosphericquantities,via inganycorrectionsformisfitsintiming.Toaccommodate
the observation operator for a number of satellite chan- an hourly ERA5 product, these OI analyses are now per-
nels that are sensitive to both ozone and temperature or formedhourly,thatis,12timesintheLDASanalysisstep,
humidity. Examples of these are the HIRS instrument each retaining a ±3hr observation window. Many obser-
(channel 9), and specific channels for the hyperspectral vationsarethree-hourly(at0000,0300,..,2100UTC).Asa
radiances from IASI, AIRS and CrIS. The provision of resultofthis,analysesatotherhoursofthedaymaysuffer
improved estimates for these observation operators was from systematic biases. On the other hand, observations
oneofthedriverstoimplementaprognosticozonescheme available at other times, such as some observations from
at ECMWF. Only when no such observations are avail- Australia,canintroducesystematicbiasesforanalysesat,
able (as in the pre-satellite era before the early 1970s) for example, 0000 and 1200 UTC. Note that a particular
does ozone have no effect on the rest of the atmospheric observationcanbeusedinuptosixOIanalyses.Thereis
reanalysis. noconflicthere,sinceuptoonlyoneofthem(the0600or
1800UTCanalysis)isusedforthetransportofinformation
towardsthenextanalysiswindow.
2.3 Landdataassimilation(LDAS) The SST and SIC products are stored hourly as well,
althoughtheirvaluesonlychangeoncedailyinlinewith
ERA5 includes an advanced land DA system to analyze thetemporalresolutionoftheingestedlevel-4products.
landsurfaceprognosticvariables(deRosnayetal.,2014).
It is weakly coupled with 4D-Var (Figure 2). First-guess
values are provided by the short forecasts that originate 2.4 TheEnsembleofDataAssimilation
from the previous LDAS and upper-air 4D-Var assimi- (EDA)systems
lation. However, the LDAS and 4D-Var assimilation are
producedseparatelyandtheirinfluenceisonlycombined TheensemblecomponentofERA5isanEDAof10mem-
towardsthenextassimilation.Itconsistsofthefollowing bers which provides background-error estimates for the
components: deterministicHRES4D-VarDAsystem.
TheanalysismethodisthesameforeachEDAmember
1. A two-dimensional optimal interpolation (2D-OI) andfollowsthatoftheHRESasdisplayedinFigure2.In
schemefortheanalysisofscreen-level2mtemperature particular,eachmembermakesuseoftheflow-dependent
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2007
Bmatrixasdeterminedbytheensembleasawhole.How- stateofmaturityoftheobservingsystemasawhole.There-
ever, resolution is lower (TL319, compared to TL639 for fore,itshouldfollowtheevolutionoftheobservingsystem.
the HRES), and two inner loops are performed, rather In ERA5 this is handled in a rather crude way. One sin-
thanthree.DetailsaregiveninTable2.Inaddition,each gleestimateisusedfortheperiodfrom1979totheendof
member (except the control) is run with different ran- 1999(called1979-B )whichrepresentstheearlysatellite
cli
dom perturbations added to the observations. The per- era, and one from 2000 onwards for the modern satellite
turbationsofobservationsaresampledfromazero-mean era,whichfollowswhatisusedbydefaultinCy41r2(called
Gaussiandistributionwithvarianceequaltotheexpected 41r2-B ).Theeffectoftheabrupttransitionon1January
cli
variances of the observation errors. Likewise, the model 2000 on the resulting reanalysis products is described in
physicaltendenciesareperturbed(Leutbecheretal.,2017) Section9.Thenarrowercorrelationsofthe41r2-B allow
cli
in the short forecasts that link subsequent analysis win- for more accurate, local adjustments in the model anal-
dows. Perturbations in SST and SIC are taken from the ysis around observations, while 1979-B distributes the
cli
spread within the range of available products (Hirahara informationofsparserobservationsoverlargerdistances.
et al., 2016). The perturbations applied to the observa- ThestaticB matricesweredeterminedfromthespread cli
tions,theSST,SICandthemodelimplythattheresulting inalargenumberofshort-rangeforecastsfromdedicated
background(i.e.,short-rangeforecast)ofeachmemberis hybridEDAruns,spanningseveralmonthsandcombining
implicitlyperturbed,thusavoidingtheneedforexplicitly winterandsummercasesintheperiodofinterest.
perturbing the background fields. It can be shown (Isak- TheEDAalsobenefitsfromVarBC(Dee,2005).Asfor
sen et al., 2010) that in a weakly nonlinear environment the model initial state x, bias parameters 𝜷 are not per-
thecombinationofsamplesofperturbedshort-rangefore- turbed.Analysisupdatesfor𝜷areonlyestimatedfromthe
castsprovidesagoodflow-dependenterrorestimateforB control, and are propagated as estimates for 𝜷 to all per-
whentheensemblesizeissufficientlylarge. turbedmembers.Thereasonforthisistoavoidartificially
However,theensemblesizeinERA5isquitelimited. long correlations in the background-error statistics as
Partlyforthisreason,theEDAandtheHRES4D-Varmake derivedfromtheshort-rangeensembleforecasts(Isaksen
useofahybridBformulation(Bonavitaetal.,2016).This etal.,2010).
meansthat,asfortheoperationalmedium-rangesystem,a
static,climatologicalbackground-errorcovariancematrix
(B ) is combined with a dynamic one computed using 3 PRODUCTION
cli
short-rangeforecastsfromtheEDA: AND AVAILABILITY
B=(1−𝛼)B +𝛼B . (6) ERA5isproducedontheECMWFhigh-performancecom-
cli EDA
puting facility. Typically 6 to 9 days of reanalysis can be
Thislatterbringsinflow-dependentcorrelationstruc- completed per day. To produce 70 or so years of reanal-
turestotheresultingbackground-errorcovariancematrix. ysis in a few years, ERA5 has been split into a num-
The weight 𝛼 increases with wavenumber, from 0.15 for ber of parallel streams which are later merged into one
the largest to 0.74 for the smallest scales. These weights consolidated public dataset. The original target for the
are lower than used in the Cy41r2 operational NWP sys- 40yearsdiscussedinthispaperwastohaveonestreamper
tem (0.3 to 0.93), in order to limit sampling errors from decadestartingfromERA-Interiminitialconditions,with
thesmallerensemblesize(10versus25).Theverticalpro- the exception of the stream for the 1980s and mid-2010s
filesoftheglobalaverageensemblestandarddeviationfor which were initialized from ERA-40 and ECMWF oper-
modelstatevariablesaredeterminedbytheforecasterrors ational (Cy40r1 for 30 May 2014) analyses, respectively.
ofthedayfromtheensemblemembers. A one-year overlap between streams allows for a long
For data produced prior to March 2017, 𝛼 had been spin-up period. In practice, the final consolidated prod-
keptconstant(0.15)inadvertentlyforallscalesandasim- uct from 1979 onwards was built up from more streams.
ilarweightingforstandarddeviationwasappliedaswell. Details are listed in Table 3. This deviation was driven
ThisaffectedERA5datafromJanuary2000toJune2005, bypracticalsolutionswhichwereimplementedtohandle
andfromJanuary2010toOctober2014.Aswillbeseenin issues that were discovered and resolved during produc-
Section 7.1, this change had a minor effect on the HRES tion.Themostseriousofthesewere:theinitialappearance
reanalysisproducts.Itdidhavealargereffectonthespread ofanomalouslyhighozoneduringthepolarnightbecause
in the EDA ensemble and standard deviation of analysis of issues with the assimilation of ozone; an incomplete
increments. response to the Pinatubo eruption due to the usage of a
ThestaticpartB ,thatis,thelong-termaverageerror sub-optimal B in the stratosphere; and the persistent
cli cli
characteristics of the model first-guess, depends on the appearance of anomalous sea ice over parts of the Baltic
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

2008 HERSBACHetal.
TABLE 3 StartmonthsintheconsolidatedpublicERA5datasetofthecollationofproductionstreams
fromJanuary1979toendof2019
HRES Jan1979†,Jul1981,Apr1986†,Oct1988,Aug1993†,Sep1995,Jan2000†,Oct2000†,Oct2001†,
Oct2002†,Oct2003†,Oct2004†,Oct2005†,Oct2006†,Jan2008,Jan2010,Jan2015,Mar2019
EDA Jan1979,Apr1986,Aug1993,Jan2000,Jan2010,Jan2015,Mar2019
Note:The†labelsrepairruns,whilethestreamstartingMarch2019iseffectivelyacontinuationof(i.e.,initializedby)its
predecessorandisalsousedforthetimelyupdates.
duringsummer.Byextendingcertainstreamssufficiently andalargenumberofnear-surfaceparametersandother
long into the affected subsequent stream, the final con- two-dimensional fields. The CDS data have been con-
solidated public dataset was not affected by these issues. verted from the native reduced-Gaussian grid to a regu-
Details are provided in Hersbach et al. (2018). Another lar latitude–longitude grid (0.25◦ for the high-resolution
solution,whichwasusedtocleartheseaiceissuewhich deterministic reanalysis and 0.5◦ for the ensemble prod-
was discovered quite late in the production, was to con- ucts; for ocean wave products, 0.5 and 1◦, respectively).
ductanumberofrelativelyshort‘repair’runs(11intotal) Several parameters, such as precipitation, surface fluxes
whichreplacedatafromaffectedperiods.Muchcarewas and minimum and maximum temperatures, are pro-
taken to ensure that the mean state of such re-runs only vided on the CDS as hourly timeseries which combine
deviates significantly from the original products where hourlyanalysisfieldswithshort-rangeforecastsasneeded.
required. This was accomplished by warm-starting such Thissimplifiesmanytechnicaldifficultiesthatusershave
streams from the initial production with a two-week encounteredinthepastwhenretrievingECMWFreanaly-
spin-up.Inaddition,theVarBCbiasparameterestimates sisdata.
𝛽 (Equation(3))wereimposedfromtheoriginalproduc- For convenience, ensemble spread and mean data
tion; this method is also used to avoid systematic dif- are directly available. Monthly-mean averages (both for
ferences between the EDA members (Section 2.4). Such a particular hour of the day and averaged over all hours
re-runswerenotconductedfortheensemblecomponent, in the entire month) have been pre-computed as well.
which means that the sea ice problem was not resolved Monthly-meanvaluesforensemblemeanandspreadwere
for the uncertainty estimate; the reason for this was the notpre-computed.
prohibitive cost of so doing. Some details are provided The ERA5 online data documentation (available via
inSection6.2. https://confluence.ecmwf.int/display/CKB; accessed 11
As shown later in Section 9, the mean state of the April2020)providesadetaileddescriptionofthevarious
resulting consolidated dataset exhibits very few signifi- productsandalistofallavailablegeophysicalparameters.
cantjumpsinthetroposphereorstratosphereattransition Timely updates are provided. Each day, one day of
pointsbetweenstreams.Themostseriousoneisadisconti- reanalysis products is added with a delay of 5days.
nuityinstratosphericandupper-tropospherictemperature Once a month, one month of this preliminary product
on1January2000,whichistheresultoftheswitchofthe is replaced by a more thoroughly quality-checked final
climatological part of the model background error from product with a delay of 2–3months. In practice, both
1979-B to41r2-B .Stratospherichumidityhasamarked products will rarely differ, and if they do (due to con-
cli cli
discontinuity at both this transition point and early in siderable errors found in the daily release), users will
1986, and smaller discontinuities occur at other times. benotified.
In the observation-free mesosphereand deep soil (where At the time of writing, the back extension from 1950
spin-up can take several years), at the seams discontinu- to 1978 had been completed, though was not yet pub-
itiesintimeareingeneralobserved,withtheexceptionof licly available. The stream consolidated up to Decem-
repair-runs(thestreamsdenotedbya†inTable3),since ber 1999 has been continued up to end of 2006 since,
thesewerewarm-started. as will be discussed in Section 7, its usage of the
The consolidated dataset is archived in the ECMWF 1979-B has a beneficial effect on stratospheric temper-
cli
MARS. Its volume from 1979 onwards totals about ature and the uncertainty estimate for ozone. It differs
5petabytes. To ensure fast access to ERA5 data, a very little in the troposphere. A more in-depth assess-
post-processed product (around 1petabyte), is available ment is provided in Simmons et al. (2020). This stream,
on the CDS cloud server (https://cds.climate.copernicus. which is labeled ERA5.1 in this document, was made
eu/; accessed 11 April 2020). This includes upper-air available as a supplement to the existing ERA5 dataset
parameters on 37 pressure levels from 1,000 to 1hPa, inMay2020.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |     |     |     |     |     |     |     |     | 2009 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
4 BENEFITS FROM A DECADE a modified convective available potential energy (CAPE)
| OF IFS | IMPROVEMENTS |            |     |     | closure(Bechtoldetal.,2014). |                   |                         |                  |         |
| ------ | ------------ | ---------- | --- | --- | ---------------------------- | ----------------- | ----------------------- | ---------------- | ------- |
| AND    | PREVIOUS     | REANALYSES |     |     |                              |                   |                         |                  |         |
|        |              |            |     |     | There                        | were changes      | to the parametrizations |                  | of oro- |
|        |              |            |     |     | graphic drag,                | subgrid turbulent | mixing                  | and interactions |         |
Intheten-yearperiodbetweenERA-Interim(Cy31r2)and withthesurfaceinunstableandstableconditions(Sandu
ERA5(Cy41r2),manysignificantimprovementshavebeen etal.,2011;Sanduetal.,2014).
made to the representation of model processes (and the A non-orographic gravity wave drag parametrization
treatment of their adjoint and tangent-linear approxima- was introduced to represent the effects of upward prop-
tions, where applicable) and to the DA methodology in agating gravity waves from tropospheric sources such as
theIFS.Thissectionprovidesforeachcomponent(atmo- deep convection, frontal disturbances, and shear zones.
sphere,ozone,landandoceanwaves)asummaryofsuch The parametrization uses a globally uniform wave spec-
changes,otherthanthosealreadymentionedinSection2. trum, and propagates it vertically through changing hor-
Italsoprovidesasummaryofthemajorchangesinobser- izontal winds and air density, thereby representing the
vationhandling. wave breaking effects and associated drag due to critical
levelfilteringandnonlineardissipationinthestratosphere
andmesosphere(Orretal.,2010).
4.1 Improvementsfortheatmosphere An improvement in the wind extrapolation scheme
|     |     |     |     |     | SETTLS | used for the | departure | point | calculation, |
| --- | --- | --- | --- | --- | ------ | ------------ | --------- | ----- | ------------ |
The radiation scheme used in ERA5, McRad, described described in Diamantakis (2014), reduced numerical
by Morcrette et al. (2008), is a major upgrade from the noiseintheupperstratospheretypicallyoccurringduring
schemeusedbyERA-Interim.ItincorporatestheMCICA SSW events. The practical benefits of this modification
(Pincusetal.,2003)forrepresentingsubgridcloudstruc- was a large reduction of both analysis and forecast tem-
ture and overlap, and the short-wave RRTMG (Iacono perature error and an overall enhanced medium-range
etal.,2008),consistentwiththeexistinguseofRRTMGin predictabilityofSSWevents.
thelong-wave.Theradiationschemeiscalledeveryhour Improved de-aliasing of the pressure gradient term
on a grid 2.5 times coarser in each horizontal direction. (ECMWFR&D,2016),reducednumericalnoiseintheadi-
To mitigate erroneous temperatures at coastlines caused abatic tendencies, allowing a reduction of the horizontal
by the coarser grid, approximate updates to the fluxes diffusionusedintheforecast.
are performedeverytimestepandgridpoint(Hoganand Regardingthetangent-linearandadjointphysicsthat
Bozzo,2015).Infrequentradiationcallscanleadtoawarm are used in the inner loops of the 4D-Var DA system
stratosphere bias through accumulated numerical error (JaniskováandLopez,2013),improvementsinclude:
| in sunrise | and sunset | times, but | this has | been mitigated |     |     |     |     |     |
| ---------- | ---------- | ---------- | -------- | -------------- | --- | --- | --- | --- | --- |
bytheHoganandHirahara(2016)schemeforcomputing 1. Inclusionofthefreezingofraininthemoistphysics;
effectivesolarzenithangle. 2. Substantial revision of the moist physics to match the
Thelarge-scalecloudandprecipitationscheme,based nonlinear reference large-scale cloud and convection
| onTiedtke(1993),wasupgradedwithanimprovedrepre- |     |     |     |     | schemes; |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
sentation of mixed-phase clouds (Forbes and Ahlgrimm, 3. Replacement of the old long-wave radiation
2014), and prognostic variables for precipitating rain parametrization (neural network) by the more
and snow (Forbes and Tompkins, 2011; Forbes et al., elaborateschemeofMorcrette(1991);
2011). In addition, there were numerous improvements 4. Linearized version of the new non-orographic gravity
| to the parametrization |     | of the microphysics, |     | particularly | wavedrag; |     |     |     |     |
| ---------------------- | --- | -------------------- | --- | ------------ | --------- | --- | --- | --- | --- |
forwarm-rainprocesses(AhlgrimmandForbes,2014)but 5. Added simplified linearized parametrization scheme
alsoice-phaseprocessesandicesupersaturation. for surface processes to represent the evolution of the
Changes to the parametrization of convection, origi- topsoillayer,snowandseaicetemperatures;and
nally based on Tiedtke (1989), include a thorough revi- 6. Revision of the linearized vertical diffusion to match
sion of the entrainment and the coupling with the large thechangesoftheexchangecoefficientsinthenonlin-
| scale,leadingtoalargeredistributionofrainfallfromthe |     |     |     |     | earscheme. |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
HadleyCelltotheWalkerCell,alargeimprovementinthe
| distribution | of rain | rate versus TRMM | and | an improved |     |     |     |     |     |
| ------------ | ------- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- |
representationoftropicalvariability(Bechtoldetal.,2008; 4.2 Improvementsforozone
| Hirons et | al., 2013). | Improvements | in the | diurnal cycle |     |     |     |     |     |
| --------- | ----------- | ------------ | ------ | ------------- | --- | --- | --- | --- | --- |
of convection, shifting the rainfall peak over land from Theheterogeneousozonechemistry,whichisbasedona
noon to late afternoon, have been achieved by use of modifiedversionoftheCariolleandDéqué(1986)scheme,

2010 HERSBACHetal.
was updated. A number of changes were introduced in characterisefreakwaves(JanssenandBidlot,2009),swell
theassimilationsystem,suchastheextensionofVarBCto systemsandwave-modifiedfluxestotheoceans.
observationsoftotalcolumnozone,whicharedescribedin
Sections4.5and5.10.
4.5 Improvedhandlingofobservations
4.3 Improvementsfortheland ERA5 benefits from many improvements in the observa-
component tionoperatorsandinthehandlingofobservationsimple-
mented in the IFS since the start of ERA-Interim (based
InERA5theHTESSELlandsurfaceschemeisused.Bal- onCy31r2,withRTTOV-7astheradiativetransfermodel).
samo et al. (2015) documented the revised hydrology of ERA5usesRTTOV-11(Saundersetal.,2018)astheobser-
theHTESSELschemeasusedinERA-Interim/Landcom- vation operator for radiance data (Lupu and Geer, 2015),
pared with the TESSEL scheme (van den Hurk et al., whichincorporatesimprovementsintheunderlyingspec-
2000)usedinERA-Interim.Someofthemostsignificant troscopy in both the microwave and infrared as well as
changes from ERA-Interim to ERA5 are related to (a) improvements in the optical depth predictor model rela-
the introduction of the soil texture map (Balsamo et al., tivetoRTTOV-7.
2009), and (b) an improved representation of bare soil ERA5 also benefits from the ongoing development of
evaporation (Albergel etal., 2012). The new scheme also all-skyassimilationatECMWF(Geeretal.,2017).Initially
accountsforseasonallyvaryingmonthlyvegetationmaps implementedforthemicrowaveimagers,theschemewas
specified from a MODIS-based satellite dataset (Bous- successfully extended to microwave humidity sounding
setta et al., 2013). In addition, an enhanced snowpack data. The approach exploits the capability of RTTOV to
parametrization allows a more realistic timing of runoff modelradiativetransferincloudyandprecipitatingatmo-
andterrestrialwaterstoragevariationsandabettermatch spheres, as well as a linearised moist physics scheme
ofthealbedotosatelliteproducts(Dutraetal.,2010).Bal- (Janisková and Lopez, 2013), to assimilate microwave
samo et al. (2012) introduced the capacity of forecasting observations in all-sky conditions. All-sky assimilation
of inland water bodies and evaluated the impact when improves analyses both through the improved analysis
coupled to the atmosphere, following a previous offline of moist variables, as well as through improved analyses
evaluation of sensitivity to lakes (Dutra etal., 2009). The of dynamical fields resulting from the ability of 4D-Var
chosen parametrization for lakes (FLake; Mironov et al., to extract wind information from the advection of trac-
2010), allows consideration of both subgrid and resolved ers, in this case humidity, cloud and rain. The scheme
water bodies (Manrique-Suñén et al., 2013). This series rectified a problem with the earlier 1D+4D-Var assimi-
ofchangescontributestosignificantimprovementsinthe lation of rain-affected radiances which, in ERA-Interim,
soil moisture and land surface fluxes consistency, which resulted in an underestimation of global rainfall
allowedfortheusageofsatellitedatainERA5toanalyse (Deeetal.,2011).
soilmoistureasdescribedbelow. Several other developments have enhanced the
RegardingtheLDAS,thesnowanalysisandtheSEKF exploitationofobservationssinceERA-Interim.Thediag-
forsoilmoistureareanimprovementonERA-Interimin nosis and modelling of several types of observation error
whichaCressmaninterpolationand1D-OImethodwere has advanced significantly since 2007 (Bormann et al.,
used,respectively(deRosnayetal.,2013). 2009). For example, for AMSU-A improvements were
made allowing for increased weight in the assimilation
and improved handling of observation errors in cloudy
4.4 Improvementsforoceanwaves scenesandoverorography.Situation-dependentobserva-
tionerrorsforAMVswereintroducedandtheobservation
Themodelbathymetrywasupdatedtouseamorerecent errors for GNSS-RO bending angle data were re-tuned,
version of ETOPO2 (NOAA, 2006). A new wave advec- with more weight given to bending angles in the middle
tion scheme was introduced with a revised unresolved andupperstratosphere.Advanceshavealsobeenmadein
bathymetry scheme to better account for the propaga- extendingtheuseofmicrowavedataoverlandandseaice
tion along coastlines and to better model the impact of surfaces(Bormannetal.,2017).
unresolvedislands(Bidlot,2012).Theslowattenuationof For GNSS-RO data, allowance for tangent point drift
long-period swell as well as the impact of shallow water was introduced (Poli et al., 2009) and a 2D observation
on the wind input was introduced with an overall retun- operator implemented (Healy etal., 2007). The refractive
ingofthelevelofdissipationduetowhite-capping(Bidlot, indexcoefficientsusedintheray-pathcomputationwere
2012).Extraoutputparameterswereintroducedtobetter alsorevised,includingnon-idealgaseffects(Healy,2011).
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2011
For observations of total column ozone, quality con- inSection5.1,followedbymoredetailsindedicatedsub-
trol was made stricter, rejecting all observations where sections.
first-guess departures exceed 30 Dobson units. Assim-
ilation of IR ozone-sensitive radiances was introduced
(DraganiandMcNally,2013),exploitingapartofthespec- 5.1 Theevolvingobservingsystem
trum never used before from HIRS (channel 9) and the
hyperspectralIRsoundersIASI,AIRSandCrIS. ThenumberofobservationsassimilatedinERA5increases
Regarding dedicated efforts for the ERA5 reanal- from approximately 0.75 million per day on average in
ysis, several aspects of the observation operators for 1979toaround24millionperdaybyJanuary2019.Inthe
key datasets have been improved for the early satellite 40yearsfrom1979to2019inclusive,94.6billionobserva-
era. Observations from IR sounding instruments provide tionswereactivelyassimilatedin4D-Var,65millioninthe
important information on upper-air temperatures. This OIocean-wavecomponentandaboutonebillionobserva-
information is mainly extracted from channels at wave- tionseachofsurfaceairtemperatureandrelativehumidity
lengthsaroundthe15𝜇mCO band.Forthesechannels, wereprocessedbytheLDAS. 2
theformoftheirweightingfunctions,andinparticularthe The 4D-Var component of ERA5 uses observations
heights of the peaks in the weighting functions, is deter- from over 200 satellite instruments or types of conven-
minedbytheformoftheCO concentrationprofilewhich tional data. It extracts information from insitu obser-
2
exhibits seasonal variability as well as long-term trends. vations of 10m wind over sea and 2m humidity over
Shine et al. (2008) have shown that the long-term trend land, and pressure over land and sea. Upper-air obser-
in CO , if unaccounted for, gives rise to spurious atmo- vations of wind, temperature and humidity are obtained
2
spherictemperaturetrendsfromSSUobservationswhich from PILOT, radiosonde, dropsonde and aircraft mea-
range from –0.4Kdecade−1 to +0.4Kdecade−1, depend- surements. Upper-air wind is also obtained from AMV
ing on altitude. In ERA5 the variability in CO is taken winds from a number of polar and geostationary satel-
2
into account for the early IR sensors assimilated in the lites. In addition, ERA5 uses information on rain rate
reanalysis for the duration of these missions: HIRS, SSU from ground-based radar–gauge composite observations
andVTPR.CO profilesusedinRTTOV-11areestimated from2009.ERA5usesmeasurementsfrommanysatellite 2
from zonal fields as used in the ERA5 radiation scheme platforms. These include radiances sensitive to upper-air
(Section 6.1). For the advanced IR sounders (AIRS, IASI temperature,humidityandozonefrom(clear-sky)HIRS,
and CrIS) the evolution of atmospheric CO concentra- MSU, SSU, AMSU-A, AMSU-B, ATMS, MWHS and
2
tionsisnottakenintoaccountandtheeffectontheesti- (all-sky) MWHS2, MHS, and from microwave imagers
matedbiascorrectionsisasexpectedandisillustratedin (alsoall-sky)SSMI,SSMIS,TMI,AMSR-2,AMSRE,GMI,
FiguresS1andS2. and (hyperspectral infrared radiances) from IASI, AIRS,
In a separate development, an improved observation CRIS and (mixed clear-sky and all-sky) from geostation-
operator for the assimilation of SSU observations has ary satellites. ERA5 uses level 2 ozone from a range of
been incorporated in ERA5. The SSU instruments, form- instruments.ERA5alsobenefitsfromGNSS-RObending
ing part of the TOVS suite of instruments and opera- angles (from 2001, but large quantities from 2006), pro-
tional from late-1978 until mid-2006, provide valuable vidinginformationonupper-airtemperatureandhumid-
information on mid-upper stratospheric temperatures in ity. Information on ocean vector wind (4D-Var) and land
the pre-ATOVS era (i.e., pre-1998). The SSU instrument soil moisture (LDAS) is obtained from scatterometers,
is an infrared radiometer employing a detection tech- whileinformationonocean-waveheight(OI)isobtained
nique based on pressure modulation. Leaks in the pres- from altimeters (both types of instruments from 1991).
suremodulatorcellshaveledtocomplextime-dependent In addition, the LDAS uses insitu observations of the
biases in the observations (Nash and Saunders, 2015). A global SYNOP network for temperature and humidity
parametrized correction scheme has been developed and at screen level, soil moisture and snow depth. From
tested,basedonmeasuredcellpressures,whichimproves 2004 onwards it also uses information on snow cover
thesimulationofbrightnesstemperaturesforNOAA-7and over the Northern Hemisphere from the multi-sensor
NOAA-11. IMSsystem.
Figure 3 shows daily counts of those observations
per assimilated variable, on a logarithmic scale. Radi-
5 OBSERVATIONS ances are the dominant and growing source of measure-
ments throughout the period. Major developments for
Thissectionprovidesadetailedaccountoftheobserving this class of observations have included the transition
systemasusedinERA5.Itstartswithageneraloverview from the TOVS (HIRS-2, MSU, SSU) to the ATOVS suite
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
by University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on
[11/03/2026].
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

2012 HERSBACHetal.
FIGURE 3 Numberofdailyactivelyassimilatedobservations(weakcolours)and30-daymeans(strongcolours),bothinlog10scale,
forERA-Interim(blue)andERA5(red)forthe12observablesforwhichobservationsareassimilatedin4D-Varandoceanwaveassimilation.
Numbersfor(d)upper-airwindexcludeassimilatedAMVwind.NumbersoftheselatterareshownforERA5(black),whilenostatisticsare
availableforERA-Interim.Rain(k)isassimilatedonlyinERA5.Nostatisticsareavailablefor(l)ERA-Interimsignificantwaveheight,while
informationondatausageinLDASisincompleteforbothreanalyses.Each0.3tickontheveticalaxiscorrespondstoafactorof2,andminor
ticks(0.1)toadifferenceof26%
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |     |     |     |     |     |     |     |     |     | 2013 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
(HIRS-3/-4,AMSU-A,AMSU-B)ofsoundinginstruments, 5.3 Conventionalobservations
the introduction of hyperspectral infrared radiances and andground-basedradar–gaugecomposites
| the increasing | availability | of  | observations | from | a grow- |     |     |     |     |     |
| -------------- | ------------ | --- | ------------ | ---- | ------- | --- | --- | --- | --- | --- |
ingconstellationofmicrowaveimagers.Therehasbeena Conventionalmeteorologicalmeasurementsusedasinput
markedincreaseinthenumberofothersatelliteobserva- inERA5samplethetroposphereandthelowerandmid-
tions assimilated, notably GNSS-RO, scatterometer wind dle stratosphere, and come from observations made near
observations and Level-2 ozone products. The volume of the surface on land and over oceans, upper-air sound-
conventionalobservationshasincreasedsteadilythrough- ings,andatmosphericmeasurementsfrominstrumentson
out the period. An analysis of the observation impact, board aircraft operating on air routes. Their spatial cov-
based on the Degrees of Freedom for Signal diagnostic erage and temporal resolution vary in time, from sparse
(DFS;Cardinalietal.,2004)showsthat,asexpected,satel- observations in the 1950s particularly over the South-
liteobservationsplayaprogressivelymoreimportantrole ernHemisphere,tothecurrentdenseobservingnetwork.
throughtheperiod(Horányi,2017). ERA5 uses conventional observations prepared initially
Figure 3 also shows the observation volumes assim- forERA-40,spanningSeptember1957toDecember2001,
ilated in ERA-Interim. Generally, more observations are and from the operational ECMWF data archive, received
assimilated in ERA5. Several discrepancies are apparent. through the GTS, to cover the period from 2002 to the
Thedivergenceinthevolumeofradiancemeasurements present. For the period prior to 1979, ERA5 also benefits
assimilated post-2007 (Figure 3a) is due to the assimi- from the assimilation of improved reprocessed conven-
lation of many new observations in ERA5, such as the tional datasets, including the ISPD v3.2.6 dataset (Cram
hyperspectralobservationsfromIASIandCrIS,whichare et al., 2015), the ICOADS v2.5.1 (Woodruff et al., 2011)
not assimilated in ERA-Interim, together with the grad- and data collections from the NCEP. Figure 4 provides a
ual decline in the numbers assimilated in ERA-Interim, detailedoverviewoftheobservationusageinERA5(and
as instruments and channels gradually fail. ERA5 uses comparedtoERA-Interim).
a revised cloud-detection scheme for HIRS (Krzeminski Dataselectionrulesforobservationsarepredefinedin
et al., 2009) which appears to remove more observa- blacklists that cover the entire reanalysis period, and are
tions and this is why, initially, fewer radiance measure- applied in the same way as in ERA-Interim (Dee et al.,
ments are used in ERA5. The initially smaller gain in 2011). Conventional observations are classified into five
| forecast skill | for ERA5 | in Figure | 1 seems           | to  | be unre- | types: |     |     |     |     |
| -------------- | -------- | --------- | ----------------- | --- | -------- | ------ | --- | --- | --- | --- |
| lated to this  | scheme,  | though,   | since ERA-Interim |     | type     |        |     |     |     |     |
experiments with the revised scheme performed com- • SYNOP,consistingofmeasurementsmadenearthesur-
parably to ERA-Interim itself. ERA-Interim also shows faceatlandstations(surfacepressure,relativehumid-
a sharp decline in the number of surface pressure and ity in daytime in 4D-Var and 2m temperature, rela-
upper-air winds and temperatures following the tran- tivehumidityandsnowdepthinthelandcomponent)
sition by data providers to a BUFR format from 2013 including airport weather reports (surface pressure),
onwards which the system cannot handle. In addition, and on ships (surface pressure, wind components at
| ERA5makesuseofseveralnewandimprovedreprocessed |     |     |     |     |     | 10m); |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
datasets.
|     |     |     |     |     |     | • DRIBU,comprisingdriftingandmooredbuoys(surface |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
pressure,windcomponentsat10m);
|     |     |     |     |     |     | TEMP, | which includes | radiosondes | and dropsondes |     |
| --- | --- | --- | --- | --- | --- | ----- | -------------- | ----------- | -------------- | --- |
•
| 5.2 | Reprocessedandnewdatasets |     |     |     |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(temperature,windcomponents,specifichumidity);
|              |        |                   |     |                   |     | PILOT | balloon observations | (wind | components), | and |
| ------------ | ------ | ----------------- | --- | ----------------- | --- | ----- | -------------------- | ----- | ------------ | --- |
| Improvements | in the | characterisation, |     | inter-calibration |     | •     |                      |       |              |     |
windprofilers(windcomponents),and
| and processing | of conventional |     | and | satellite measure- |     |     |     |     |     |     |
| -------------- | --------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
mentshaveenableddataproviderstoprogressivelyrefine • AIRCRAFT-based atmospheric observations (tempera-
thequalityofhistoricalobservations,intermsofcoverage ture,windcomponentsandspecifichumidity).
| and accuracy.ERA5has |     | made | use ofseveral | reprocessed |     |     |     |     |     |     |
| -------------------- | --- | ---- | ------------- | ----------- | --- | --- | --- | --- | --- | --- |
satellitedatasets,whichwereacquiredfromanumberof In addition to those observations assimilated in
ERA-Interim,ERA5assimilatestheNCEPstageIVquan-
| space agencies | and | institutes, | as listed | in Table | 4. The |     |     |     |     |     |
| -------------- | --- | ----------- | --------- | -------- | ------ | --- | --- | --- | --- | --- |
EU-fundedprecursorproject,ERA-CLIM,providedAMVs titative precipitation estimates produced over the USA
fromMeteosat-8and-9andMetop-AAVHRR.Alsoshown by combining precipitation estimates from the NEXRAD
in Table 4 are some new datasets not used in earlier with gauge measurements. An overview of the method
ECMWFreanalyses.Detailsareprovidedinthefollowing usedtoassimilatethisproductisprovidedbyLopez(2011).
|     |     |     |     |     |     | The usage | of these measurements | benefits | from | VarBC |
| --- | --- | --- | --- | --- | --- | --------- | --------------------- | -------- | ---- | ----- |
subsections.

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
2014 HERSBACHetal.
TABLE 4 Reprocessedand
| Instrument/Satellite | Periodcovered | Agency |
| -------------------- | ------------- | ------ |
new(*)satellitedataassimilatedin
ERA5 Atmosphericmotionvectors
| Meteosat1stGen.(M-2to-7) | 1982–2000      | EUMETSAT |
| ------------------------ | -------------- | -------- |
| Meteosat2ndGen.(M-8,-9)  | 2004–2012      | EUMETSAT |
| GMS(-1,-3,-4,-5)         | 1979,1987–2003 | JMA      |
| MTSAT-1R                 | 2005–2009      | JMA      |
| GOES-9                   | 2003–2009      | NOAA     |
| GOESGVAR(-8to13,-15)     | 1995–2013      | CIMSS    |
| AVHRR(NOAA-7to-18)       | 1981–2014      | CIMSS    |
| AVHRR(MetOp-A)           | 2007–2012      | EUMETSAT |
Radiances
| DMSPSSMI(F-08to-15)      | 1987–2008         | EUMETSATCMSAF |
| ------------------------ | ----------------- | ------------- |
| MeteosatSecondGen.ASRs   | 2003–2012         | EUMETAT       |
| IASI*(Metop-A,-B)        | 2006–present      | EUMETSAT      |
| CrIS*(S-NPP/NOAA-20)     | 2012–present      | NOAA          |
| MWHS*/MWHS-2*(FY-3B,-3C) | 2012/2014–present | CMA           |
TMI*/SSMIS*/AMSR-2*/GMI*
|                      | 2005/2009/2012/2015- | NASA/DMSP/      |
| -------------------- | -------------------- | --------------- |
|                      | 2015/(3)present      | JAXA/NASA       |
| Ozonechannels*(HIRS, | 1979–present         | NOAA,NASA,      |
| AIRS,IASIandCrIS)    |                      | EUMETSATandNOAA |
Radiooccultation
| Blackjack | 2001–2014 | UCAR |
| --------- | --------- | ---- |
(GRACE-A,CHAMP,SAC-C)
| IGOR | 2006–2014 | UCAR |
| ---- | --------- | ---- |
(TerraSAR-X,COSMIC-1to-6)
Scatterometerwind
| ASCAT*(MetOp-A,-B) | 2007–2014 | EUMETSAT |
| ------------------ | --------- | -------- |
Oceansat*
|     | 2012–2014 | ISRO |
| --- | --------- | ---- |
Ozoneretrievals
| GOME-2(Metop-A,-B)      | 2007–2013 | ESA/EUMETSAT |
| ----------------------- | --------- | ------------ |
| GOME(ERS-2)             | 1996–2002 | ESA          |
| MIPAS(ENVISAT)          | 2005–2012 | ESA          |
| MLS(EOS-AURA)           | 2004–2014 | NASA         |
| OMI(EOS-AURA)           | 2004–2015 | NASA         |
| BUV(Nimbus-4)*          | 1970–1977 | NASA         |
| SBUVandSBUV-2(Nimbus-7, | 1978–2013 | NOAA         |
NOAA-9,-11,-14,-16,-17,-18,-19)
| SCHIAMACHY(ENVISAT)      | 2002–2012 | ESA   |
| ------------------------ | --------- | ----- |
| TOMS(NIMBUS-7,EarthProbe | 1978–2006 | NASA  |
| ADEOS-1)                 | 1996–1997 | NASDA |

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
HERSBACHetal. 2015
TABLE 4 Continued
| Instrument/Satellite | Periodcovered | Agency |
| -------------------- | ------------- | ------ |
Scatterometersoilmoisture
| AMIonERS-1,-2   | 1991–2006 | TUWien       |
| --------------- | --------- | ------------ |
| MetOp-A,-BASCAT | 2007–2014 | EUMETSATHSAF |
Altimeterwaveheight
| RAonERS-1,-2        | 1991–2003   | ESA       |
| ------------------- | ----------- | --------- |
| AltiKaonSARAL*      | 2014onwards | CNES/ISRO |
| SIRALonCryoSat-2*   | 2014onwards | ESA       |
| Poseidon-2onJason-1 | 2001–2010   | NASA/CNES |
| RA-2onEnvisat       | 2002–2012   | ESA       |
FIGURE 4 Conventionalobservationsassimilatedperday(2100to2100UTC)inERA5duringtheperiod1979–2018.Greybars
indicatetypesofobservationusedinbothERA5andinthereferencesystem(ERA-Interim,from1500to1500UTC,until2016;ECMWF
operationsfrom2100to2100UTCthereafter;thetransitionisindicatedbytheverticaldashedline).Redbarsindicateobservations
assimilatedinthereferencesystembutnotinERA5,andgreenbarsindicateobservationsthatareusedinERA5,butnotthereference
system.Apencilsymbolprecedinganobservationtypeindicatesthataprescribedbiascorrectionisappliedtoatleastoneassimilated
variable(orand/orchannelforsatelliteobservations)providedbythatobservationtype.Similarly,ananchorsymbolindicatesthatatleast
onevariableorchannelprovidedbytheobservationtypeisusedtoanchortheanalysis,i.e.,itisassimilatedwithoutapplyingabias
correction.Detailsonanchoredvariablesandchannelsaswellasonprescribedbiascorrectionsaregiveninthesectionscoveringthe
respectiveobservations.TheNCEPstageIVquantitativeprecipitationestimatesobservationtypeisindicatedasradar/gaugecomposites
where all observations are grouped into one bias group minimum sea level pressure data contained in the ISPD
subjecttoasix-parameterbiasmodel. dataset.Thesearenotusedintheperiodfrom1979.
In order to better represent past extreme weather Atcruiselevel(around200hPa),aircraftobservations
events, the ERA5 segment prior to 1979 will benefit are on average biased warm by about 0.2K, which had
from the assimilation of the tropical cyclone best-track affectedtemperatureanalysesinERA-Interimwhentheir

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2016 |     |     |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
numbers significantly increased around 1999 (Dee and TABLE 5 Prescribedobservationerrors(K)for
radiosondetemperatureinERA5andERA-Interimasa
Uppala,2009).InERA5thishasbeenalleviatedbyextend-
functionofheight
ingVarBCtoaircrafttemperatureswithonebiasgroupper
| type of     | aircraft. | Only one | predictor |             | (a constant) | is used,      |     |               |     |             |     |     |      |     |
| ----------- | --------- | -------- | --------- | ----------- | ------------ | ------------- | --- | ------------- | --- | ----------- | --- | --- | ---- | --- |
|             |           |          |           |             |              |               |     | Pressure(hPa) |     | ERA-Interim |     |     | ERA5 |     |
| rather than | three     | (also    | ascent    | and descent |              | speed) in the |     |               |     |             |     |     |      |     |
|             |           |          |           |             |              |               |     | 10            |     | 1.47        |     |     | 1.66 |     |
ECMWFoperationalsystematthetimesince,duringthe
|              |     |       |                     |     |     |             |     | 20  |     | 1.05 |     |     | 1.34 |     |
| ------------ | --- | ----- | ------------------- | --- | --- | ----------- | --- | --- | --- | ---- | --- | --- | ---- | --- |
| preparations | for | ERA5, | that implementation |     |     | was discov- |     |     |     |      |     |     |      |     |
|              |     |       |                     |     |     |             |     | 30  |     | 0.98 |     |     | 1.28 |     |
eredtobeflawed.Thishassincebeencorrected(Ingleby
etal.,2018)inCy45r1(5June2018).
|          |         |           |      |           |         |            |     | 70  |     | 0.98 |     |     | 1.28 |     |
| -------- | ------- | --------- | ---- | --------- | ------- | ---------- | --- | --- | --- | ---- | --- | --- | ---- | --- |
| For      | surface | pressure, | bias | estimates | are     | updated by |     |     |     |      |     |     |      |     |
|          |         |           |      |           |         |            |     | 100 |     | 0.91 |     |     | 1.09 |     |
| VarBC as | it was  | developed | for  | the       | ERA-20C | reanalysis |     |     |     |      |     |     |      |     |
|          |         |           |      |           |         |            |     | 150 |     | 0.88 |     |     | 0.70 |     |
(Polietal.,2016),usingonegroupperplatformwithone
|           |              |     |       |            |     |              |     | 250 |     | 0.81 |     |     | 0.73 |     |
| --------- | ------------ | --- | ----- | ---------- | --- | ------------ | --- | --- | --- | ---- | --- | --- | ---- | --- |
| predictor | (a constant) |     | and a | background |     | B𝛽 term that |     |     |     |      |     |     |      |     |
correspondstoaresponsetimeof60days.Fortheseobser- 300 0.70 0.64
| vations, | VarBC | is performed |     | in the | screening | task, that |     |     |     |      |     |     |      |     |
| -------- | ----- | ------------ | --- | ------ | --------- | ---------- | --- | --- | --- | ---- | --- | --- | ---- | --- |
|          |       |              |     |        |           |            |     | 400 |     | 0.63 |     |     | 0.57 |     |
is,beforetheminimizationin4D-Var.Thisisachievedby
|         |          |         |         |       |     |               |     | 500 |     | 0.66 |     |     | 0.61 |     |
| ------- | -------- | ------- | ------- | ----- | --- | ------------- | --- | --- | --- | ---- | --- | --- | ---- | --- |
| solving | Equation | (4) for | 𝜹𝜷 with | 𝜹x=0, |     | which is then |     |     |     |      |     |     |      |     |
|         |          |         |         |       |     |               |     | 700 |     | 0.77 |     |     | 0.70 |     |
decoupledintoasetoflow-dimensionallinearequations,
one per bias group. For a one-parameter bias model, its 1000 0.98 0.89
solutionistrivial.Thereasonforthischoiceistoavoidan
Note:Atotherheights,observationerrorisalinear
| undesired | (and | understood) | interaction |     | with | the applied |     |     |     |     |     |     |     |     |
| --------- | ---- | ----------- | ----------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
interpolationbetweenthevaluesatthelistedpressures,while
Huber norm (Tavolato and Isaksen, 2015) which would itisconstantfrom10hPaupwards.Inthe
troposphere/stratosphereinERA5,ahigher/lowerweightthan
leadtoafartooslowresponse.
inERA-Interimisassigned,withacrossoverpointatabout
| In the | ERA5 | troposphere, |     | about | a   | 10% higher |     |     |     |     |     |     |     |     |
| ------ | ---- | ------------ | --- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
132hPa.
| weight      | is assigned | to radiosonde |              | temperatures |        | than in        |     |     |     |     |     |     |     |     |
| ----------- | ----------- | ------------- | ------------ | ------------ | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ERA-Interim |             | (Tavolato     | and Isaksen, |              | 2015). | In the strato- |     |     |     |     |     |     |     |     |
spheretheoppositeistrue,whereprescribedobservation as brightness temperatures (as is the case for all radi-
errors were inflated by 20–30%. Details are provided in ance observations), provide information on temperature
Table 5. At all heights the weight assigned to PILOT throughout the troposphere and stratosphere. ATMS
and radiosonde wind was increased by 10%, while the additionally provides humidity sounding capability. This
| weight | assigned | to radiosonde |     | humidity |     | (assimilated |           |     |        |           |        |         |           |     |
| ------ | -------- | ------------- | --- | -------- | --- | ------------ | --------- | --- | ------ | --------- | ------ | ------- | --------- | --- |
|        |          |               |     |          |     |              | component |     | of the | observing | system | evolved | consider- |     |
below 100hPa only) is unaltered. Regarding bias cor- ably throughout the 1979–2019 period (Figure 5). For
rections for radiosonde temperature, an update of the example in the mid-1990s, typically observations from
method of a pre-calculated RAOBCORE (Haimberger two microwave temperature sounding instruments were
et al., 2008) homogenization as in ERA-Interim is used, assimilated. By early 2005 this had increased to four,
| where | estimates | are now | also | based | on  | comparison |     |     |            |              |      |      |             |     |
| ----- | --------- | ------- | ---- | ----- | --- | ---------- | --- | --- | ---------- | ------------ | ---- | ---- | ----------- | --- |
|       |           |         |      |       |     |            | and | by  | early 2019 | observations | from | nine | instruments |     |
between neighbouring stations, rather than from depar- (seven AMSU-A and two ATMS) were assimilated. This
ture statistics alone (RICH; Haimberger et al., 2012). An improves the resilience of the system to discontinuities
additionalsolar-elevation-dependentcorrectionisapplied resulting from outagesof any single instrument, but also
as in ERA-Interim. From 1 January 2015 onwards, such reduces analysis errors through the effect of averaging
estimatesarenotavailableandERA5insteadfollowsthe
independenterrorsintheobservations,aswellasthrough
bias-correction scheme in the operational medium-range improvedsamplingintimethroughtheanalysiswindow.
forecastsystem. The radiances are bias corrected using VarBC (Auligné
|     |     |     |     |     |     |     | et  | al., 2007). | The | bias correction |     | model | for | channels |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | ----- | --- | -------- |
assimilatedfromthesesensorsemployaconstantterm,a
| 5.4   | Microwaveradiances    |     |     |     |     |     |                      |     |                |            |          |         |               |      |
| ----- | --------------------- | --- | --- | --- | --- | --- | -------------------- | --- | -------------- | ---------- | -------- | ------- | ------------- | ---- |
|       |                       |     |     |     |     |     | scan-angle-dependent |     |                | correction | (based   | on      | a third-order |      |
|       |                       |     |     |     |     |     | polynomial           |     | in scan-angle) |            | and four | airmass | predictors,   |      |
| 5.4.1 | Clear-skyassimilation |     |     |     |     |     |                      |     |                |            |          |         |               |      |
|       |                       |     |     |     |     |     | represented          |     | by the         | thickness  | of       | layers  | 1000–300      | hPa, |
oftemperaturesounderradiances 200–50hPa, 50–5hPa and 10–1hPa. The exception here
|              |     |          |           |     |          |      | is  | AMSU-A | channel | 14 for | which | no bias | correction | is  |
| ------------ | --- | -------- | --------- | --- | -------- | ---- | --- | ------ | ------- | ------ | ----- | ------- | ---------- | --- |
| Measurements |     | from the | microwave |     | sounders | MSU, |     |        |         |        |       |         |            |     |
applied,inordertoanchorthetemperatureanalysisinthe
AMSU-A and ATMS (Bormann et al., 2012), assimilated upperstratosphere.

HERSBACHetal. 2017
FIGURE 5 RadianceobservationsassimilatedinERA5.ThecolourschemeisasforFigure4.Additionally,bluebarsindicate
observationsthatarereprocessedrelativetothoseassimilatedinERA-Interim,orforwhichtheprocessinghaschangedsignificantlysince
ERA-Interim
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2018 |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
Similar bias models are used for the other radi- andMetOpplatforms(withtheexceptionofNOAA-16and
ance datasets described below in Sections 5.4.3, 5.5.1 NOAA-18)sincetheTIROS-Nsatellite.
| and5.5.2. |     |     |     |     |     | The SSU               | instruments |           | provide | information |          | on strato- |
| --------- | --- | --- | --- | --- | --- | --------------------- | ----------- | --------- | ------- | ----------- | -------- | ---------- |
|           |     |     |     |     |     | spheric temperatures, |             | and       | have    | three       | channels | with       |
|           |     |     |     |     |     | peak sensitivities    | in          | the range |         | 1–15hPa.    | ERA5     | assimi-    |
5.4.2 All-skyassimilationofhumidity lates SSU observations from NOAA platforms during the
sounderradiances period1979–2006,andthetreatmentofSSUincludessev-
|     |     |     |     |     |     | eral improvements |     | since | ERA-Interim | (Section |     | 4.5 and |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ----- | ----------- | -------- | --- | ------- |
Humidity information throughout the troposphere is Kobayashi et al., 2009). SSU channel 3 is used to anchor
obtained from passive microwave observations, for most the analysis. In contrast to ERA-Interim, it continued to
sensors using the all-sky approach (Geer et al., 2017). beusedasananchorwiththeadventofAMSU-Aobserva-
| Humidity | sounding | radiances | from    | MHS       | instruments | tionsin1998. |     |     |     |     |     |     |
| -------- | -------- | --------- | ------- | --------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
| on board | NOAA-18  | and       | -19 and | the MetOp | satellites  |              |     |     |     |     |     |     |
(Figure5)areassimilatedinall-skyconditionsalongwith
the FY-3C humidity sounder MWHS-2 (Lawrence et al., 5.5.2 HyperspectralIRradiances
| 2018). However |     | the MWHS-1 | sensor | on FY-3B | (Chen |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
et al. 2014) and AMSU-B sensors on NOAA-16 and -17 Radiances, assimilated as brightness temperatures, have
wereassimilatedusingclear-skyscenesonly,asanall-sky been assimilated from the hyperspectral IR instruments
configurationwasnotavailableintheCy41r2atthestart AIRS, IASI and CrIS. An overview is given in Figure 5.
| ofERA5. |     |     |     |     |     | AIRS radiances | were | assimilated |     | from | October | 2002 |
| ------- | --- | --- | --- | --- | --- | -------------- | ---- | ----------- | --- | ---- | ------- | ---- |
(McNallyetal.,2006)andbyJune2019radiancesfromtwo
|       |                                |     |     |     |     | CrIS instruments | (S-NPP |     | and NOAA-20; |     | Eresmaa | et al., |
| ----- | ------------------------------ | --- | --- | --- | --- | ---------------- | ------ | --- | ------------ | --- | ------- | ------- |
| 5.4.3 | All-skyassimilationofmicrowave |     |     |     |     |                  |        |     |              |     |         |         |
2017)andtwoIASIinstruments(Metop-Aand-B;Collard
imagerradiances andMcNally2009)werealsoassimilated.Thehyperspec-
tralIRsounders,measuringinthethermalIRregionofthe
Microwaveimagersprovideradianceobservationswhich, spectrum, provide information on temperature through-
over ice-free ocean surfaces, improve the analysis of outthetroposphereandlower-midstratosphereandtropo-
lower-tropospheric humidity, cloud liquid water and spheric humidity. Those channels that provide sufficient
ocean surface wind speed. An overview is given in informationareassimilatedusingacloud-detectiontech-
Figure 5. ERA5 assimilates EUMETSAT CM SAF SSM/I nique based on McNally and Watts (2003). Observation
FCDRs (Fennig et al., 2017) during the period August errors, including inter-channel correlations, have been
1987–December 2008. This aspect of the observing sys- estimated using observation space diagnostics (Bormann
| temhasgrownconsiderablysincethe1980sandradiances |     |     |     |     |     | etal.,2015). |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
from TMI and AMSR-E were used starting in 2005 and Variationalbiascorrectionisappliedtoallassimilated
2009(Geeretal.,2010),SSMI/SonF-17startingin2009, channelswiththeexceptionofozone-sensitivechannelsat
andAMSR2andGMIin2012and2015(Kazumorietal., 9.6𝜇m for AIRS (channel 1088), CrIS (channel 626) and
2016; Geer et al., 2017). However, to avoid possible bias IASI(channel1585).
problems,usagehasbeenlimitedthroughtheblacklistto
| a maximum | of three | imagers | at any | one time. | In addi- |     |     |     |     |     |     |     |
| --------- | -------- | ------- | ------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
tion,thehumiditysoundingchannelsofSSMI/Shavebeen 5.6 Geostationaryradiances
assimilated,includingthosefromtheF-18satellite,which
isnototherwiseused. AnoverviewisgiveninFigure5.Infraredradiancesfrom
|     |     |     |     |     |     | geostationary | satellites | are | first | assimilated | in  | ERA5 in |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ----- | ----------- | --- | ------- |
May2001(Meteosat-7).Sincethattimeradiancesfromthe
5.5 Infraredsounderradiances US GOES series of satellites (specifically GOES-8 to -16),
|     |     |     |     |     |     | covering America | and | neighbouring |     | oceanic | longitudes, |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ------- | ----------- | --- |
withsub-satellitelongitudesof135◦Wand60–75◦W,from
| 5.5.1 | MultispectralIRradiances |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theMeteosatsatellites(-5to-11)coveringmuchofEurope
The HIRS instruments are 20-channel infrared radiome- and Africa at longitudes of 0◦–10◦E, and MTSAT-1R and
ters providing information on temperature throughout -2 as well as Himawari-8 covering the Western Pacific,
the troposphere and lower-mid stratosphere and humid- East Asia and Australia at 140◦E have been assimilated.
ityinformationinthetroposphere.Anoverviewisgivenin TheIRimagerinstrumentsonboardthesesatellitesmea-
Figure5.HIRSradianceshavebeenusedfromallNOAA sure radiances in the mid-IR water vapour band, in one

HERSBACHetal. 2019
to three channels depending on instrument, and pro- delay. The physical retrieval process is well known, so
videinformationontropospherichumidity.Detailsofthe theycanbeassimilatedwithoutbiascorrection.Thelatter
operational implementation of these radiances can be meansthatGNSS-RObendinganglesareanchormeasure-
foundinKöopkenetal.(2003),Munroetal.(2004),Lupu mentsintheVarBCsystem,andthereforetheyconstrain
and McNally (2012), Letertre-Danczak (2016) and Bur- the bias corrections applied to the radiances. It has been
rows (2018). These observations have also been shown shownthattheconsistencyoflower/middlestratospheric
to improve analyses of wind fields through the abil- temperaturesamongsttheglobalreanalyseshasimproved
ity of 4D-Var to extract dynamical information from the since the assimilation of COSMIC GNSS-RO measure-
observedadvectionofwatervapourfeatures(Peubeyand mentsin2006(Longetal.,2017).
McNally,2009). ThereprocessedCOSMICGNSS-ROdataset,provided
byUCAR,incorporatesimprovedfilteringofthemeasured
phase delays. The improvement was implemented in the
5.7 Atmosphericmotionvectors near-real-timeoperationalCOSMICROdatasetinNovem-
ber 2009 and resulted in mean departure statistics more
AMVs are winds derived by tracking clouds or water consistent with those of Metop-A GRAS. An overview is
vapourfeaturesinasequenceofimagesobtainedfromgeo- presentedinFigure6.
stationarysatellites,orfrompairsofimagesobtainedfrom
polarorbitingsatellites.AMVsthereforeprovideinforma-
tiononvectorwindsthroughoutthetroposphere.Heights 5.9 Scatterometerwindandsoil
areassignedtothederivedAMVwindsusinginfraredwin- moisture
dow channel radiances. These observations are not bias
corrected. Backscatter(level1B)fromscatterometersprovidesinfor-
ERA5 assimilates winds throughout the period from mationonnear-surfacevectorwindovertheglobaloceans
1979 to the present (Figure 6). AMVs from the GOES and soil moisture over land. ERA5 is the first ECMWF
seriesofsatellites,typicallylocatedat135◦Wand60–75◦W, reanalysistoincluderemotelysensedobservationsinasoil
cover the American continent from 1979. At 140◦E the moistureanalysis.Anoverviewoftheusageofscatterom-
GMS/MTSAT/Himawariseriesofsatellites,supplemented eterdataispresentedinFigure6.
byrepositionedGOESsatellites,providenear-continuous In addition to ERS-1/-2 and QuikSCAT, ERA5 makes
coverageoftheWesternPacificandEastAsiasince1979. useofwindinformationfromthescatterometeronboard
The Meteosat series of satellites, located at 0–10◦E pro- Oceansat-2 (2013), and the ASCAT scatterometers on
vide coverage over Europe, the Middle East and Africa Metop-A/-B (2007–present), which were not used in
since 1982. The status of AMV assimilation at Cy41r2 is ERA-Interim. To improve their usage for ocean vec-
summarisedin(SalonenandBormann,2016). tor wind, the observation operator now acts on model
ERA5 assimilates a number of reprocessed AMV equivalent-neutral wind at 10m height rather than on
datasets(Table4)fromthethreemajorprovidersandsome 10m wind itself (ERA-Interim). For ASCAT and ERS-2
newdatasets(i.e.,datasetswhichdidnotexistpreviously, measurements from 22 August 2003 onwards, the rela-
e.g., recently generated polar winds from NOAA LEO tion between wind and backscatter is provided by the
satellitesoperatingintheearly1980s).Inpre-production CMOD5.n geophysical model function (Hersbach, 2010),
testing, significant benefit was obtained by assimilating whileforERS-2and(all)ERS-1observationspriortothat
reprocessed GOES observations (-8 to -13, covering the date the (bias-corrected) CMOD4 model (Stoffelen and
period 1995–2013). Model background fits to low-level Anderson, 1997) as also used in ERA-Interim, was used
winds(below400hPa)wereimprovedby10–30%relative by mistake (however, acting on neutral wind). Although
tothoseobtainedinexperimentsassimilatingtheoriginal departure statisticssuggeststhatthishadalimitedeffect
near-real-timeoperationaldatasets. on the surface-wind mean state, it likely had a negative
impact on the usage of extreme scatterometer winds for
thatperiod.
5.8 GNSS-RObendingangles Soil moisture information is only extracted from
C-band,andnotfromKu-bandscatterometers,forwhich
The GNSS-RO bending angles provide high-quality tem- theshorterwavelengthpenetrateslessdeeplyintothesur-
perature information in the upper troposphere and low- face.TheusageofareprocessedproductfromERS-1and
er/middlestratosphere.Theycomplementtheinformation -2bringstheentiretimeseriesfrom1992to2006intocon-
provided by satellite radiances, because they have good sistencywiththesoilmoistureproductsfromMetOp-A/-B
vertical resolution. GNSS-RO measures an accurate time ASCAT.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2020 |     |     |     |     |     |     | HERSBACHetal. |
| ---- | --- | --- | --- | --- | --- | --- | ------------- |
FIGURE 6 Non-radiancesatelliteobservationsassimilatedinERA5.ThecolourschemeisasforFigure5
| Reprocessed   | ASCAT      | observations | from Metop-A      | 5.10 | Ozone |     |     |
| ------------- | ---------- | ------------ | ----------------- | ---- | ----- | --- | --- |
| prior to 2014 | (both wind | and soil     | moisture) correct |      |       |     |     |
inconsistencies in backscatter and brings observations An overview is provided in Figure 7. All Level-2 ozone
into agreement with the operational data stream from productsassimilatedinERA5exceptMETOB-BGOME-2,
| 2014onwards. |     |     |     | METEOR-3 | and ADEOS-1 | TOMS have | been improved |
| ------------ | --- | --- | --- | -------- | ----------- | --------- | ------------- |

HERSBACHetal. 2021
FIGURE 7 OzoneobservationsassimilatedinERA5.ThecolourschemeisasforFigure5
through recent reprocessing efforts. Each reprocessed Ozone observations from SBUV are not assimilated
datasetisbasedonasingle,temporallyconsistentretrieval in the EDA prior to 2000. Their initial usage in this
algorithm used throughout the period of availability. component had been shown to lead to an unexplained
Reprocessed BUV/SBUV/SBUV-2 datasets (version 8.6; highensemblespreadoverthepolarnight,whichlargely
McPeters et al., 2013), from NOAA/NASA, offer an reducedtheweightassignedtothemodelfirstguess,and
increased number of levels in the vertical relative to ear- led to anomalously high values of (total column) ozone
lier data releases, as well as improved consistency over (Hersbachetal.,2018).
the period 1970–2013 while near-real-time observations
were used afterwards. Total column ozone observations
fromNimbus-7,andEarthProbeTOMS(v8.0)wereused 5.11 Altimeterwaveheight
in conjuction with an earlier version for METEOR-3
andADEOS-1TOMSobservations.Thereprocessedlimb Altimeter measurements provide information on sig-
ozone profiles from MLS (v3) were assimilated until nificant wave height over the ocean. Observations have
December2014whentheassimilationwasswitchedtothe been used since the advent of ERS-1 in 1991 (Figure 6).
near-real-timeproduct. ObservationsfromSARAL/AltiKa,CryoSat-2andJason-2
For European instruments, several algorithms and are based on the operational stream, while those from
datasets were available at the start of ERA5. Initiatives ERS-1/-2, Jason-1 and Envisat are based on repro-
such as the European Space Agency–Climate Change cessed products. Altimeter observations are subject
Initiative (ESA-CCI) were instrumental in providing to prescribed bias corrections such that wave height
long-term data records with improved inter-satellite estimates emerge unbiased with respect to the ERA5
consistency and uncertainty characterisation. Dedicated model, rather than with respect to independent insitu
round-robinassimilationexperimentswereperformedfor measurements. These wave-height-dependent tables
datasetsforwhichmultiplealgorithmswereavailable(i.e., were based on a comparison with ocean waves from
OMI, SCIAMACHY, MIPAS, GOME, and GOME-2) aim- ERA5-type test runs without using altimeter data. The
ing at identifying the best candidates for ERA5. Detailed test period (January to May 2003) focused on Envisat
assessment studies were also performed to evaluate pos- data, while results for other altimeters were determined
sible synergies from using ozone products derived from by inter-calibration of overlaps between the various
instrumentswithdifferentcharacteristics(Dragani,2016). instruments.
Additional information on ozone in ERA5 is pro-
vided by ozone-sensitive channels of the nadir-viewing
infrared sounders (HIRS, AIRS, IASI and CrIS; Dragani 6 OBSERVATION-BASED
and McNally 2013). ERA5 uses the available operational GRIDDED FORCINGS
NWPdatasetsforthesesensors. AND BOUNDARY CONDITIONS
TotalcolumnozoneobservationsaresubjecttoVarBC
(Dragani, 2009). The two-parameter bias model corrects Besidesinformationfromsub-dailyobservations,theIFS
for a global bias and temporal-spatial systematic biases reliesonclimatologicalinformation,suchasthosewhich
thatvarywithsolarelevationangle.Observationsofpartial influenceforcingfromtheradiationschemeandthepre-
ozonelayersfromnadir-andlimb-viewinginstrumentsare scription of SST and sea ice over the global oceans. For
notbiascorrectedandactasanchors. ERA5aspecialeffortwasmadetoincludestate-of-the-art
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2022 |     |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
TABLE 6 Globalmeanenergybudgets(W⋅m−2)accordingtoTrenberthetal.,(2009),ERA-Interimandtheensemble
meanofERA-20CM,averagedfromMarch2000toMay2004forTrenberthetal.,(2009),andfrom1989to2008forERA5,
ERA-Interim(bothbasedonthefirst12-hrforecasts)andERA-20CM
|     | Model                           |     |     |     | Trenberthetal.(2009) |     |     | ERA-20CM |     | ERA-Interim |     | ERA5  |
| --- | ------------------------------- | --- | --- | --- | -------------------- | --- | --- | -------- | --- | ----------- | --- | ----- |
|     | Incomingsolarradiation(TSI∕4)   |     |     |     | 341.3                |     |     | 340.4    |     | 344.2       |     | 340.4 |
|     | Netabsorbedsolarradiation(ASR)  |     |     |     | 239.4                |     |     | 240.9    |     | 244.3       |     | 242.7 |
|     | Outgoinglong-waveradiation(OLR) |     |     |     | 238.5                |     |     | 240.6    |     | 245.5       |     | 242.2 |
|     | TOAnetradiationin(R             |     | T ) |     | 0.9                  |     |     | 0.3      |     | −1.2        |     | 0.4   |
|     | Netenergyabsorbedbysurface(F    |     |     | )   | 0.9                  |     |     | 1.9      |     | 6.9         |     | 6.1   |
S
|     | Atmospherenet(TEI=R |     |     | −F ) | 0.0 |     |     | −1.6 |     | −8.1 |     | −5.6 |
| --- | ------------------- | --- | --- | ---- | --- | --- | --- | ---- | --- | ---- | --- | ---- |
T S
datasetsthatdescribewellthelow-frequencyvariabilityof systematically adds energy, which is then deposited into
theclimatesystem.Alargepartofthisworkwasprepared the surface during the connecting short forecasts, which
duringtheERA-CLIMproject. emerges as the diagnosed loss (Mayer and Haimberger,
2012).Thelossof−1.6W⋅m−2forERA-20CMresultsfrom
anunknownerrorinthecalculationofthepost-processed
6.1 CMIP5radiationforcingterms 2DfieldsforenergybudgetswithintheIFS,sinceforthese
model-onlyrunstheenergyintheatmosphereshouldrise
The provision of the total solar irradiance (TSI) is byonlyabout0.01W⋅m−2 (associatedwithglobalwarm-
very important, as well as the provision of fields of ing). Although the magnitude of this deficit varies with
aerosols,greenhousegasesandozone.Areanalysisspan- model cycle, this would suggest that the actual energy
ning several decades requires that such fields follow the imbalanceinERA5isintheorderof4W⋅m−2.
observed 20th and 21st century evolution. Within the AmoredetailedpictureispresentedinFigure8,which
ERA-CLIM project, state-of-the-art standardized sets of shows the evolution from 1979. Figure 8a shows that
such long-term forcing fields from the WCRP initiative the response from the El Chichón and Pinatubo erup-
CMIP5wereimplementedasoptionsintheIFS.Theywere tions is clearly captured by ERA5 and ERA-20CM, but
first tested in an ensemble of century-long model inte- missed by ERA-Interim. Responses from El Niño events
grations(ERA-20CM).Thesemodificationsaresharedin are captured by all. At the TOA there is no obvious and
ERA5.Detailsmaybefoundin(Hersbachetal.,2015).This significant long-term change. This is in sharp contrast
isanimprovementonERA-Interim,which,forexample, to the surface (Figure 8b), and the resulting net loss in
omitted the occurrence of stratospheric sulphate due to energy (Figure 8c) is worse when going further back in
majorvolcaniceruptions. time. This could be the result of larger systematic incre-
Theaverageeffectoftheseforcingsonglobalradiation ments.Around2010,ERA5forabrieftimealmostreaches
budgetsaveragedfrom1989to2008isdisplayedinTable6 the‘energy-neutral’stateofERA-20CM.Adetailedstudy
where,asinBerrisfordetal.(2011),valuesarecompared on the origins and evolution of sinks (and sources) is
withTrenberthetal.(2009).Fromthisitdirectlyemerges required. For ERA-20C and CERA-20C the Total Energy
that the lower value of TSI for ERA5 (based on rescaling Input(TEI)isremarkablygoodandcomparabletothatfor
| to match | the | Total Irradiance |     | Monitor | instrument | (Lean | ERA-20CM. |     |     |     |     |     |
| -------- | --- | ---------------- | --- | ------- | ---------- | ----- | --------- | --- | --- | --- | --- | --- |
etal.,2005),firstusedatECMWFintheSeasonalSystem4
| implementation |        | (Molteni    | et al.,   | 2011)) | compares   | consid- |     |                               |     |     |     |     |
| -------------- | ------ | ----------- | --------- | ------ | ---------- | ------- | --- | ----------------------------- | --- | --- | --- | --- |
| erably         | better | with the    | estimates | from   | Trenberth  | et al.  |     |                               |     |     |     |     |
|                |        |             |           |        |            |         | 6.2 | Sea-surfaceboundaryconditions |     |     |     |     |
| (2009)         | than   | ERA-Interim | does,     | which  | by mistake | used    |     |                               |     |     |     |     |
values which were too high. The net energy input at the InERA5,conditionsforSSTandSICareprovidedbyexist-
TOA,whichresultsinanetglobalwarming,agreeswithin
|        |               |             |                |            |           |         | ing level-4 | (i.e.,      | gap-less) | gridded  | datasets. | ERA-Interim      |
| ------ | ------------- | ----------- | -------------- | ---------- | --------- | ------- | ----------- | ----------- | --------- | -------- | --------- | ---------------- |
| known  | uncertainties |             | (Allan et      | al., 2014; | Trenberth | et al., |             |             |           |          |           |                  |
|        |               |             |                |            |           |         | had         | used partly | what      | was used | in        | ERA-40 (Fiorino, |
| 2014); | this is       | in contrast | to ERA-Interim |            | which     | has the |             |             |           |          |           |                  |
2004)andsubsequentlywhatwasusedintheoperational
wrongsign.However,asforERA-Interim,thenetenergy
medium-rangeforecastingsystematthetime.Detailsmay
absorbedbythesurfaceisfartoolarge.Thisleadstoanet befoundintable1ofDeeetal.(2011).ForERA5acareful
energylossoftheatmosphereofabout5.6W⋅m−2(8.1W⋅
selectionprocedurewasconducted(Hiraharaetal.,2016).
m−2forERA-Interim).Apparentlytheassimilationsystem

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |     |     |     |     |     |     | 2023 |
| ------------- | --- | --- | --- | --- | --- | --- | ---- |
(a) Anomaly of TOA Net in (Rt) Energy Flux (W/m^2), ERA-20CM, ERA-Interim, ERA5 FIGURE 8 Evolutionof
| 2   |     |     |     | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
one-yearmovingaverageof
| 1   |     |     |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
energybudgetsinERA5(red),
| 0   |     |     |     | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ERA-Interim(blue)and
| -1  |     |     |     | -1  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
ERA-20CM(gold),for(a)the
| -2  |     |     |     | -2  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
TOANet-inradiation(relativeto
| -3        |           |           |      | -3   |                           |     |     |
| --------- | --------- | --------- | ---- | ---- | ------------------------- | --- | --- |
| -4        |           |           |      | -4   | 1989–2008),(b)NetAbsorbed |     |     |
| 1980 1985 | 1990 1995 | 2000 2005 | 2010 | 2015 |                           |     |     |
Surfaceradiation(relativeto
(b) Anomaly of Net Absorbed by Surface (Fs) Energy Flux  (W/m^2), ERA-20CM, ERA-Interim, ERA5
1989-2008)andfor(c)the
| 4   |     |     |     | 4   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
AtmosphereNetflux.Thelatter
| 2   |     |     |     | 2   | includesERA-20C(black)and |     |     |
| --- | --- | --- | --- | --- | ------------------------- | --- | --- |
| 0   |     |     |     | 0   |                           |     |     |
CERA-20C(green).Thevertical
| -2  |     |     |     | -2  | ochredashedlinesindicatethe |     |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- |
eruptiondatesofElChichón
| -4        |           |           |      | -4   |             |     |     |
| --------- | --------- | --------- | ---- | ---- | ----------- | --- | --- |
| 1980 1985 | 1990 1995 | 2000 2005 | 2010 | 2015 | andPinatubo |     |     |
(c) Atmosphere Net In (TEI) Energy Flux (W/m^2), ERA-20CM, ERA-20C, CERA-20C, ERA-Interim, ERA5
| 0         |           |           |      | 0    |     |     |     |
| --------- | --------- | --------- | ---- | ---- | --- | --- | --- |
| -2        |           |           |      | -2   |     |     |     |
| -4        |           |           |      | -4   |     |     |     |
| -6        |           |           |      | -6   |     |     |     |
| -8        |           |           |      | -8   |     |     |     |
| -10       |           |           |      | -10  |     |     |     |
| -12       |           |           |      | -12  |     |     |     |
| 1980 1985 | 1990 1995 | 2000 2005 | 2010 | 2015 |     |     |     |
The goal was to compile a dataset from 1950 onwards tothestricteranalysiscut-offtime,onlytheproductfrom
thatis the previous day is available. The long-term evolution of
|     |     |     | SST and | SIC as used in | the ERA5 HRES | is displayed | in  |
| --- | --- | --- | ------- | -------------- | ------------- | ------------ | --- |
(a) asaccurateaspossibleateachmomentintime, Figure9.Theglobal-meanSSTshowstheimpactofglobal
(b) has quality suitable for climate applications, for warmingfromthemid-1970s,aswellastheinfluencefrom
exampleexhibitingnonoticeablebreaksattransitions El Niño events and major volcanic eruptions. Arctic sea
betweendatasets,and ice shows a general decline over time, especially during
| (c) isabletoprovidetimelydatafortheERA5continua- |     |     | summer. |     |     |     |     |
| ------------------------------------------------ | --- | --- | ------- | --- | --- | --- | --- |
tionclosetorealtime. ComparedtoERA-Interim,ERA5usesenhancedqual-
|     |     |     | ity control | to deal with | spurious coastal | sea ice | in the |
| --- | --- | --- | ----------- | ------------ | ---------------- | ------- | ------ |
For SST various flavours of the Met Office Hadley NorthernHemisphere.ThelimitofclearingicewhenSST
|     |     |     | 1◦C |     |     | 3◦C. |     |
| --- | --- | --- | --- | --- | --- | ---- | --- |
Centre HadISST2 product (J.J. Kennedy, 2016, personal exceeds (ERA-Interim) was raised to It is very
communication) were considered (as developed within effectiveandnotoveractive.Forthemodernperiod,where
the ERA-CLIM project and used in the ERA-20CM, OSTIA is used, this check is not required. Unfortunately
ERA-20CandCERA-20Ccentennialproducts),aswellas thisenhancedcheckwasonlyintroducedquitelateinthe
the Climate Change Initiative (ESA CCI) SST v1.1 (Mer- production,tocounteractthelackofanyqualitycontrolin
chant et al., 2014), to be combined with the Met Office theinitialpartoftheproduction,whichappearedtogive
OSTIAproduct(Donlonetal.,2012)usedintheECMWF rise to spurious ice over the Gulf of Finland and several
medium-rangeforecastingsystemsince2007.ForSICthe otherlocationsduringeachsummerpriorto2008.Forthe
EUMETSATOSISAFreanalysisproduct(v409a;Eastwood HRES final production, this was resolved through repair
etal.,2014)andvariousflavoursoftheHadISST2seaice runs as indicated in Table 3. For the EDA no repair runs
product (Titchner and Rayner, 2014) were considered, to wereconducted.AsaresulttheEDAdoescontainspurious
becombinedwiththeoperationalOSISAFproductthatis ice during summer months in the periods from January
alsopartoftheOSTIAproduct. 1979toJune1981,April1986toSeptember1988,August
Asaresultofthisstudy,thechoicesforERA5aredis- 1993 to August 1995, and from January 2000 to August
playedinTable7.AsmentionedinSection2.4,theSSTand 2007 (the end of usage of the OSI SAF sea ice product).
SIC for the ERA5 EDA follow a perturbation method as TheeffectontheERA5ensemblespreadisfoundtoberel-
describedinHiraharaetal.(2016).ERA5usestheOSTIA ativelyminor.AnexampleisprovidedinFigure10which
productattheappropriatevaliditydate.Thisisincontrast confirms(a)agood-qualityiceproductfortheHRES,(b)a
totheECMWFoperationalforecastingsystem,where,due degradedestimatefortheEDA,but(c)withamildeffecton

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2024 |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | ------------- | --- |
TABLE 7 SSTandSICproductsasusedinERA5
Timeperiod SeaSurfaceTemperature SeaIceConcentration Grid(deg)
January1949–December1960 HadISST2.1.0.0(monthly) HadISST2.0.0.0 0.25x0.25
January1961–December1978 HadISST2.1.1.0(pentad) HadISST2.0.0.0 0.25x0.25
January1979–August2007 HadISST2.1.1.0(pentad) OSISAF(409a) 0.25x0.25
| September2007onwards |     | OSTIA | OSISAFoper |     | 0.05x0.05 |     |
| -------------------- | --- | ----- | ---------- | --- | --------- | --- |
Note:Allproductsaredaily,although‘pentad’isbasedon5-dailyand‘monthly’(andallHadISST2icedatasets)onone-monthly
analysiswindows.HadISST2seaiceisgriddedon0.25◦,althoughthenativeresolutionis1◦.TheOSISAF(409a)10kmpolar
stereographicgridisregriddedin-housetofacilitateitsusage.OSTIAisusedforthecorrectdate(seetextfordetails).
(a) ERA5 Sea Surface Temperature (Celsius), GLOBE    (monthly, yearly, moving average)
|     | 18.8 |     |     |     |     | 18.8 |
| --- | ---- | --- | --- | --- | --- | ---- |
|     | 18.6 |     |     |     |     | 18.6 |
|     | 18.4 |     |     |     |     | 18.4 |
|     | 18.2 |     |     |     |     | 18.2 |
|     | 18   |     |     |     |     | 18   |
|     | 17.8 |     |     |     |     | 17.8 |
FIGURE 9 Timeseriesof
|                     | 17.6 |     |     |     |     | 17.6 |
| ------------------- | ---- | --- | --- | --- | --- | ---- |
| (a)globalseasurface | 17.4 |     |     |     |     | 17.4 |
1950 1955 1960 1965 1970 1975 1980 1985 1990 1995 2000 2005 2010 2015
temperature(◦C)and(b)Arctic
seaicecover(percent)asusedin (b) ERA5 Sea Ice Cover (percent), 60N-90N    (monthly, yearly, moving average)
|     | 80  |     |     |     |     | 80  |
| --- | --- | --- | --- | --- | --- | --- |
theERA5HRESassimilationfor
|     | 70  |     |     |     |     | 70  |
| --- | --- | --- | --- | --- | --- | --- |
datathathavebeenreleasedat
|                             | 60  |     |     |     |     | 60  |
| --------------------------- | --- | --- | --- | --- | --- | --- |
| thetimeofwriting(from1979   | 50  |     |     |     |     | 50  |
| onwards),andproducedbutnot  | 40  |     |     |     |     | 40  |
| yetreleased(1950–1978),for  | 30  |     |     |     |     | 30  |
|                             | 20  |     |     |     |     | 20  |
| monthly(blue)andyearly(red) | 10  |     |     |     |     | 10  |
running-meanaverages 1950 1955 1960 1965 1970 1975 1980 1985 1990 1995 2000 2005 2010 2015
(a) ERA5 HRES (b) ERA5 EDA control (c) Spread in 2m temperature
| 10 20 | 30 50 | 70 80 | 90 100 | 0 0.25 | 0.5 0.75 1 1.25 | 1.5 2 |
| ----- | ----- | ----- | ------ | ------ | --------------- | ----- |
FIGURE 10 Seaicecover(percent)on27July2006from(a)ERA5HRES,(b)theERA5EDAcontroland(c)thedaily-meanensemble
spreadof2mtemperature(K)

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |     |          |     |     |     |     |     |          |     |     |     |     |     | 2025 |
| ------------- | --- | -------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | ---- |
|               |     | (a) 1980 |     |     |     |     |     | (b) 2017 |     |     |     |     |     |      |
|               |     | 1        |     |     |     |     |     | 1        |     |     |     |     |     |      |
|               |     |          |     |     |     |     | 2   |          | -20 |     |     |     |     | 2    |
|               |     | 2        |     |     |     |     |     | 2        |     |     |     | -20 | -20 |      |
|               |     |          | -20 |     |     | -20 |     |          |     |     | -20 |     |     |      |
|               |     |          |     | -20 | -20 |     | 1.5 |          |     |     |     |     |     | 1.5  |
|               |     | 5        | -40 |     |     | -40 |     | 5        | -40 |     |     |     | -40 |      |
|               |     |          |     | -40 | -40 |     | 1   |          |     |     |     | -40 |     | 1    |
|               | 10  |          |     |     |     |     |     | 10       |     |     | -40 |     |     |      |
|               |     |          |     |     |     | -60 | 0.8 |          |     |     |     |     |     | 0.8  |
|               | 20  |          |     |     |     |     |     | 20       |     |     |     |     | -60 |      |
|               |     |          |     |     |     |     | 0.6 |          |     | -60 |     |     |     | 0.6  |
-60
|     | 50  |     | 0   |     |     |     |     | 50  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 6   |     |     |     | 0.4 |     |     |     |     |     |     | 0.4 |
|     | 100 |     | -   | -80 |     |     |     | 100 |     |     |     |     |     |     |
0
|     |      |     |       | -60   |       |     | 0.3 |      |     |       |       | - 6 |     | 0.3 |
| --- | ---- | --- | ----- | ----- | ----- | --- | --- | ---- | --- | ----- | ----- | --- | --- | --- |
|     | 200  |     |       |       |       |     |     | 200  |     |       |       |     |     |     |
|     |      |     |       | - 4 0 |       |     |     |      |     | 0     | - 4 0 |     |     |     |
|     |      |     | - 4 0 | - 2 0 | - 4 0 |     | 0.2 |      |     | - 4   | - 2 0 | -   | 4 0 | 0.2 |
|     |      |     | 2 0   |       |       |     |     |      |     | - 2 0 |       |     |     |     |
|     | 500  |     | -     | 00    | - 2 0 |     |     | 500  |     |       | 00    | - 2 | 0   |     |
|     |      |     | 00    |       |       |     | 0.1 |      |     | 00    |       |     |     | 0.1 |
|     | 1000 |     |       | 20    |       |     |     | 1000 |     | 20    |       |     |     |     |
90°N 60°N 30°N 0°N 30°S 60°S 90°S 90°N 60°N 30°N 0°N 30°S 60°S 90°S
FIGURE 11 Zonal-meancross-sectiononalogarithmicpressurescale(hPa)ofERA5control(contours)andensemblespread(colour
shading)oftemperature(◦C)averagedover(a)1980and(b)2017.Thetopoftheblackareasatthebottommarkthezonallyandyearly
averagedsurfacepressure(hPa)
theensemblespreadfor2mtemperature.Thelargespread Forthisreasontheensemblespreadshouldmainlybe
southofNovayaZemlyaappearsforanumberofdaysin used as a guide for the quality of representing the cor-
July2006andindicatesaparticularsensitivelocationfor rect synoptic situation at a given time, rather than for
thatmonth. long-term and/or large-scale averages, such as the global
ERA5 does not impose the 100% ice concentration mean2mtemperature.Forsuchquantitiesanysystematic
north of 82.5◦N as was applied to ERA-Interim between errorsintheERA5meanstatemaybecomesignificantand
January1989andFebruary2009(Figure10c),whichwas arenotrepresentedbytheensemble.
particularlypoorinSeptember2007whenseaiceretreated The magnitude of the ensemble spread is closely
beyond that perimeter. In addition, in ERA5 the mini- relatedtothequalityoftheobservingsystem.Anexample
mum non-zero sea ice fraction was lowered from 20% is provided by Figure 11, which shows cross-sections of
(ERA-Interim)to15%,sincethelattercoincideswiththe the one-yearly and zonally averaged (synoptic) ensemble
usualthresholdfordefiningiceedge. spreadintemperaturefor(a)1980and(b)2017.Theyear
|     |     |      |              |     |     |     |     | 1980         | falls in           | the early-satellite |     | era          | with upper-air  | sen-   |
| --- | --- | ---- | ------------ | --- | --- | --- | --- | ------------ | ------------------ | ------------------- | --- | ------------ | --------------- | ------ |
|     |     |      |              |     |     |     |     | sitive       | data predominantly |                     |     | from the     | TOVS satellites | and    |
| 7   |     | DATA | ASSIMILATION |     |     |     |     |              |                    |                     |     |              |                 |        |
|     |     |      |              |     |     |     |     | radiosondes. |                    | This explains       |     | why ensemble | spread          | is the |
DIAGNOSTICS lowest over the Northern Hemisphere troposphere and
|     |     |     |     |     |     |     |     | lower | stratosphere | where |     | radiosondes | are mostly | avail- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ----- | --- | ----------- | ---------- | ------ |
7.1 EvolutionoftheERA5uncertainty able.Thespreadinthetropicalupperstratosphereisquite
| estimate |     |     |     |     |     |     |     | large.In2017theobservingsystemismuchmorecompre- |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
hensive;about30timesmoreobservationsareassimilated.
The ERA5 EDA spread among the ten ensemble mem- Asaresultensemblespreadhastightenedupalmostevery-
| bers | can | be interpreted |     | as a measure | for the | uncertainty |     | where. |     |     |     |     |     |     |
| ---- | --- | -------------- | --- | ------------ | ------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
intheHRESestimates.Itmainlysamplesrandomerrors, The 40-year evolution of monthly and globally aver-
although perturbations in the HadISST2.2 SST dataset agedspreadisdisplayedinFigure12.Thereductionover
do contain long time correlations. The perturbed model time of temperature (Figure 12a) at 3hPa is quite large.
tendencies can also lead to small systematic differences Majorimprovementsseemtocoincidewiththeadventof
in model climate for perturbed members with respect ATOVSdatain1998,andincreasingnumbersofGNSS-RO
to the unperturbed control. However, systematic differ- datain2006.Atotherheightsimprovementoftemperature
encesbetweenperturbedmembersaresmall.Forexample, estimates is more gradual. In the troposphere, ensemble
in 2018 the mean difference (globally) between the nine spread is smallest in the mid to upper part and max-
ensemblemembersandthecontrolmember,forthevari- imal at around 850hPa. For zonal wind (Figure 12b),
ablestemperature,relativehumidityandu-componentof improvement over time is also largest for the upper part
windatthe500hPalevelwere0.006K,0.3%and0.4cm⋅s−1 ofthestratosphere,withthemostradicalchangesmarked
respectively.Valuesofasimilarmagnitudewerefoundfor around1998and2006aswell.Spreadislowestneartothe
| 1980. |     |     |     |     |     |     |     | surface. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |

2026 HERSBACHetal.
(a) (b)
(c) (d)
FIGURE 12 TimeseriesofmonthlyandgloballyaveragedERA5ensemblespreadfrom1979to2018atindicatedpressurelevelsfor
(a)temperature(K),(b)zonalwind(m⋅s−1),(c)ozone(partialpressureinmPa)and(d)specifichumidity(inpercentofthe1981to2010
meanvalueatthepressurelevelinquestion).For(c),ozoneestimatesfromERA5.1(dottedlines)havebeenincludedfor50and300hPa
Ozone (Figure 12c) shows two enhanced periods for 7.2 Fittoobservations
spread at 50hPa which start at the consolidation seams
of January 2000 and January 2010. This inflation is not TheincreasingconfidenceofERA5HRESestimatesover
relatedtodifferencesindatausage.Instead,thesearethe time,asapparentfromtheEDAensemblespread,canbe
resultofaconfigurationchangeoftheEDAconfiguration verified by a comparison with observations. An example
inMarch2017,asexplainedinSection2.4.Thesesegments is provided in Figure 13 for ERA5 analysis ocean wave
originatefromtheproductionstreamsthathadbeenpro- height versus independent buoy observations. Compared
duced prior to that date. For the extension ERA5.1 (also to ERA-Interim, the scatter index (normalized standard
displayedinFigure12c)thisincreaseisnotobserved. deviation) is in addition much lower (i.e., improved),
The spikes in spread at 3hPa in 1995 and 1997 are wherebothareverifiedagainstthesamedataset.Onecan
related to anomalously high values of ozone in the polar alsoinfersuchevolutionfromthestatisticsofdepartures
nightatthoseheightsandwerecreatedbyerroneousanal- (defined in Equations (1) and (2)) that are readily avail-
ysisincrements.Thesestemfromthesamemechanismas ablefromtheassimilationsystem.Analysisdeparturesare
described in Hersbach et al. (2018), although in a much not useful here, since these express the extent to which
milder form, and hardly affect estimates of total column the analysis has drawn to the observations, rather than
ozone.Somewhatsurprisingly,thespreadfortropospheric providing an independent assessment of performance.
ozoneincreasesovertime. As an alternative, first-guess departures are much more
For tropospheric humidity (Figure 12d) the spread informative, since these represent the comparison with
decreases over time, with a sharp drop in late 1987 at observations just prior to their assimilation. Therefore
850hPa coinciding with the start of microwave imager thesearemore(butnottotally)independent.The40-year
assimilationwiththefirstSSM/I.Relativespreadislowest evolution of the standard deviation of such first-guess
nearthesurface. departures is displayed in Figure 14 by red curves for
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2027
FIGURE 13 Scatterindex(%,
lowerisbetter)withrespectto
independentbuoywaveheight
observationsforERA-Interim(blue)
andERA5(red)analyses
FIGURE 14 30-daymean(weakcolours)ofthestandarddeviationoffirst-guessdeparturesand360-daymean(strongcolours),for
useddatainERA-Interim(blue)andERA5(red)for(a)upper-airtemperaturefromradiosondes(fromtoptobottominthepanel)within
±25hPaof50,850and400hPa;(b)upper-airzonalwindfromradiosondes,dropsondesandPILOTs;(c)upper-airhumidityfromradiosondes
anddropsondes;(d)surfacepressurefromSYNOP,buoys,shipsandMETAR;(e)10mzonalwindoverseafromvariousin-situsources;and
(f)2mrelativehumidityfromSYNOP.Thestatisticsfor(b,c)arenumber-weightedaveragesofthestandarddeviationoverpressurebandsof
50hPathroughoutthevertical,withoutmakingcorrectionsforanypressure-dependentbiases.Theverticalblacklinemarksthestartdateof
theusageofBUFRTEMPdatainERA5from1January2015(Figure4)
upper-air data from assimilated radiosonde, PILOT and statisticsforupper-airtemperatureoncedatafromBUFR
dropsonde data (a–c) and for near-surface observations radiosondes are assimilated from 1 January 2015. This is
fromSYNOP,buoys,shipsandMETARdata(d–f).Thefits partlyexplainedinInglebyetal.(2016).Wherepreviously
doimproveconsiderablyovertime.However,itshouldbe observations were more commonly used near significant
realized that these statistics measure the joint (random) levels which are typically more difficult to represent, the
error between the reanalysis short forecast and observa- BUFR radiosonde data sample the vertical more densely
tions, and the latter, generally, also improve over time. andhomogeneously(figureSB1ofthatpaper).FigureS4
Inaddition,changesinsamplingcanalsohaveaneffect. here shows the degree to which the spread (expressed as
Aclearexampleistheapparentmassiveimprovementin astandarddeviation)intheERA5first-guessdepartures,
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2028 |     |     |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
forradiosondetemperaturesat500hPa,isconsistentwith Global-mean ob-bg for 60-40hPa radiosonde temperatures (K)
| the spread | in  | the EDA | and | the assumed |     | observation | 0.6 |     |             |     | ERA5 |     |     |     |
| ---------- | --- | ------- | --- | ----------- | --- | ----------- | --- | --- | ----------- | --- | ---- | --- | --- | --- |
| errors.    |     |         |     |             |     |             |     |     | ERA-Interim |     |      |     |     |     |
0.4
| For      | ERA-Interim, |           | corresponding | fits      | are displayed | by         |     |     |     |     |     |     |     |     |
| -------- | ------------ | --------- | ------------- | --------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| the blue | curves       | in Figure | 14.           | Note that | the           | comparison | 0.2 |     |     |     |     |     |     |     |
| between  | ERA5         | and       | ERA-Interim   | is not    | pure,         | since the  |     |     |     |     |     |     |     |     |
ERA5.1
0
verificationsets(theuseddatasets)differ,aswellastheir
|     |     |     |     |     |     |     | 1980 | 1985 | 1990 | 1995 | 2000 | 2005 2010 |     | 2015 |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | --------- | --- | ---- |
biasadjustments.However,forthereporttypesconsidered
here,thedifferencesarereasonablysmallpriortoJanuary
|     |     |     |     |     |     |     | FIGURE | 15  | Monthlyaverageobservation–background |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------------------------------ | --- | --- | --- | --- | --- |
2015(whenERA5startsusingBUFRdata).ForERA5the differencesfrom1979onwardsforallassimilatedbias-adjusted
| fit to observations |     | is  | better | over the | entire troposphere, |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------ | -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
radiosondetemperaturedata(K)between40and60hPa,for
in particular for the near-surface parameters. The strato- ERA-Interim,ERA5(basedon1979-B before2000and41r2-B
|     |     |     |     |     |     |     |     |     |     |     | cli |     |     | cli |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sphereisanexception,wherethefitforERA5isactually afterwards)andERA5.1(using1979-B cli from2000–2006)
worsefortemperature(Figure14a)andwind(notshown).
Thetransitionpointisaround100hPa.Onereasonforthis
is that, despite 10 years of model development, Cy41r2 An example of a misfit that is related to the reanal-
|          |          |       |              |      |       |            | ysis product, |     | rather than | to  | the ingested | observations, |     | is  |
| -------- | -------- | ----- | ------------ | ---- | ----- | ---------- | ------------- | --- | ----------- | --- | ------------ | ------------- | --- | --- |
| exhibits | a larger | lower | stratosphere | cold | bias. | Therefore, |               |     |             |     |              |               |     |     |
displayedinFigure15.Thisshowsthemeanbias-adjusted
theanalysissystemisrequiredtoapplylargerincrements.
|              |     |         |               |     |        |       | departures  | of  | radiosonde        | data | from       | the ERA5 | (red)    | and  |
| ------------ | --- | ------- | ------------- | --- | ------ | ----- | ----------- | --- | ----------------- | ---- | ---------- | -------- | -------- | ---- |
| In addition, | in  | Cy41r2, | approximately |     | 20–30% | lower |             |     |                   |      |            |          |          |      |
|              |     |         |               |     |        |       | ERA-Interim |     | (blue) background |      | forecasts, |          | averaged | over |
weight(Table5)isgiventoradiosondestratospherictem-
peratures,sothelargermisfitisweightedless.Thirdly,and allassimilatedradiosondedatafrom40to60hPa.Depar-
turesforERA5sufferfromalargejumpatthetransition
thisappliesfrom2000,thesmallercorrelationlengthsinB
pointatJanuary2000(Table3).Asmentionedabove,this
arelessabletospreadtheinitiallysparseinformationhori-
|                                                    |     |     |     |     |     |     | is the result | of  | the usage | of                  | 41r2-B | which | is less    | able |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------------------- | ------ | ----- | ---------- | ---- |
| zontally.Thismayhavepreventedpartofthereductionfor |     |     |     |     |     |     |               |     |           |                     |        | cli   |            |      |
|                                                    |     |     |     |     |     |     | to correct    | the | model     | lower-stratospheric |        |       | cold bias. | The  |
temperatureat50hPaaround2006(whenlargeamounts
ofGNSS-ROdatabecomeavailable)tooccurearlier. resulting(cold)modelbackgroundleadstomorepositive
|     |     |     |     |     |     |     | observation | minus | background |     | departures. |     | The ERA5 | fit |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---------- | --- | ----------- | --- | -------- | --- |
Theimprovementovertimeisinlinewiththeevolu-
totheradiosondedataconsiderablyimprovesin2006once
tionoftheskillofre-forecasts,asdisplayedinFigure1.
|     |     |     |     |     |     |     | substantially |     | more GNSS-RO |     | data | are assimilated. |     | As  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ---- | ---------------- | --- | --- |
mentionedinSection3,thestreamthatwasconsolidated
7.3 Meanobservationdepartures priortoJanuary2000hasbeenextendeduptotheendof
|     |     |     |     |     |     |     | 2006(asERA5.1).Itcontinuestheusageof1979-B |     |     |     |     |     |     | and |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
cli
|            |     |                |     |              |            |      | the positive | effect | on           | departure | statistics |                | (brown | curve |
| ---------- | --- | -------------- | --- | ------------ | ---------- | ---- | ------------ | ------ | ------------ | --------- | ---------- | -------------- | ------ | ----- |
| In general | the | time evolution |     | of departure | statistics | pro- |              |        |              |           |            |                |        |       |
|            |     |                |     |              |            |      | in Figure    | 15)    | is striking, | providing |            | a more-or-less |        | seam- |
videasensitivehealthcheckfortheingestedobservations.
|           |           |          |       |                |                |         | less transition |        | when  | the GNSS-RO |             | counts | considerably |     |
| --------- | --------- | -------- | ----- | -------------- | -------------- | ------- | --------------- | ------ | ----- | ----------- | ----------- | ------ | ------------ | --- |
| Spikes in | either    | their    | mean, | standard       | deviation      | or bias |                 |        |       |             |             |        |              |     |
| estimates | typically | indicate |       | data problems. | Alternatively, |         | increase.       |        |       |             |             |        |              |     |
|           |           |          |       |                |                |         | The             | upward | spike | in the      | ERA-Interim |        | radiosonde   | fit |
thesecanalsorelatetoproblemsintheanalysisproducts
inmid-1979isduetoaslowadaptationtoachangeincal-
| themselves. | For       | this | reason   | such departure | statistics | are |          |        |               |     |      |          |      |       |
| ----------- | --------- | ---- | -------- | -------------- | ---------- | --- | -------- | ------ | ------------- | --- | ---- | -------- | ---- | ----- |
|             |           |      |          |                |            |     | ibration | of the | MSU radiances |     | from | TIROS-N. | This | is an |
| closely     | monitored | in   | the ERA5 | production     | streams.   | The |          |        |               |     |      |          |      |       |
examplewhereonetypeofobservationhashadanadverse
| amount | of statistics | is  | immense | (several | thousands): | one |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
timeseriespersatellitechannel,andarangeofheightsfor effectonthereanalysisproductwhichthenemergesinthe
departurestatisticofanothertypeofobservation.Guided
| upper-air | data, | each | stratified | with respect | to  | the globe, |     |     |     |     |     |     |     |     |
| --------- | ----- | ---- | ---------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
bythedeparture-basedmonitoring,theradiancebiascor-
andsub-areas.Acomparisonwithsimilarstatisticsfroma
rectionwasadjustedforERA5toaccountforthisspecial
reference(ERA-40priorto1979,ERA-Interim,andforthe
case.ThepositivedeparturesseenforERA-Interim,which
morerecentperiod,theECMWFoperationalNWPassim-
ilation system), is made as well. Identified problems are arerelatedtoapartialresponsetothePinatuboeruption
in1991,arenotevidentinERA5.
investigated.Whenasimplesolutionisavailable(typically
| a temporal | blacklisting, |     | or  | re-initialized | bias | estimates; |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | --- | -------------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Hersbachetal.,2018),theproductionsuiteinquestionis
|     |     |     |     |     |     |     | 7.4 | Analysisincrements |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
rewoundtoadatepriortotheevent(typicallyamonthor
two).Thisprocedurehasbeenappliedseveraltimesduring
|     |     |     |     |     |     |     | After observation |     | bias | adjustments, |     | the assimilation |     | sys- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ------------ | --- | ---------------- | --- | ---- |
theproduction,andcontributestothequalityassuranceof
temimplicitlyassumesunbiasederrorcharacteristics.As
thefinalproduct.

HERSBACHetal. 2029
(a) (b)
(c) (d)
FIGURE 16 ProfilesofmonthlyandgloballyaveragedincrementsbetweenERA5analysesandfirst-guessfieldsat0000and1200UTC
for(a)temperature(K),(b)zonalwind(m⋅s−1)(c)ozone(partialpressure)and(d)specifichumidity(percent),onalogarithmicpressure
scalefrom1,000to100hPa,and(a–c)onanadditionalscalefrom100to1hPa
such, long-term averages of analysis increments 𝜹x from observationsinSeptember1998issmallerthanitwasfor
theminimumofEquation(4)shouldbesmall.Systematic ERA-Interim.ThereasonforthisisthatERA5continues
deviations typically indicate an average conflict between to use SSU channel 3 as an anchor (from its first assimi-
observations and the forecast model that is used both lationinJuly1979onNOAA6),whileitisbias-corrected
withinthe4D-Vartrajectoriesandtheshortforecastlink- inERA-InterimonceAMSU-Aemerges.ThejumpinJan-
ingtothenextassimilationcycle.VarBCcanalleviatethis uary2000attheseheightsistheconsequenceofthechange
incompatibility,butonlyaslongasrelativebiasescanbe in B . This isinline with the time seriesfor radiosonde
cli
tracedbacktotheobservations,ratherthantothemodel. departures, as shown in Figure 15. The emerging pos-
Abruptchangesinmeananalysisincrementscanusually itive temperature increments in the lower troposphere
be related to changes in the observing system. The stan- between1988and2007 are over the oceansand adrying
dard deviation of increments indicates the work done by tendencyisseenstartingin1988forhumidityandcontin-
theassimilation,andislessinformativeaboutthehealth uingtothepresentday(Figure16d).Theseissuescoincide
ofthesystem. withtheadventofmicrowaveimagers,whichareknown
Pressure–time diagrams for monthly and globally to warm and dry the analysis at 850hPa over the ocean
averaged mean increments are displayed in Figure 16. (Geer et al., 2017). The exact mechanisms causing these
In general, these are significantly lower than for biasesremainunclear.Themid-tropospherenegativetem-
ERA-Interim(showninFigure17).Exceptionsareozone perature increments are mainly over land (Figure 16b).
and mid-tropospheric humidity where magnitudes are Analysis increments for specific humidity are in general
comparable. For temperature (Figure 16a) the positive smaller over land (not shown) than over oceans, while
meanERA5incrementinthelowerstratosphereisrelated for zonal wind the opposite applies. For upper-air wind
tothemodelcoldbiasinthisregion. (Figure 16b), the reason for the reduction of positive
Oppositeincrementsatthetopofthestratosphereindi- increments around 100hPa around 1987 is unclear. For
cateabiaswithrespecttoanchoringsatelliteobservations ozone the sharp transition in the upper stratosphere is
which peak at those heights. In this respect, the effect of related to the start of using AURA MLS and OMI data.
the introduction of the anchoring AMSU-A channel 14 Pressure–timediagramsformonthlyandgloballyaveraged
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

2030 HERSBACHetal.
(a) (b)
(c) (d)
FIGURE 17 AsFigure16,butforERA-Interim
standard deviations of analysis increments are shown in 2002). Lothar was the first of two December 1999 storms
FigureS3. and was followed by Martin 36hr later. Both of these
stormscausedconsiderabledamage.TheERA5hourlyres-
olution presents a detailed view of this rapidly evolving
8 IMPROVED RESOLUTION storm, as is apparent from Figure 18a,b,c. Although at
FOR SYNOPTIC VARIABILITY 0900 UTC the ERA5 minimum pressure is about 5hPa
higher(ensemblespread2.1hPa)thanthereportedmini-
The considerable increase in resolution of ERA5 allows mum(HewsonandNeu,2015)(whichalsohasanassoci-
much more detail to be represented both in space and ateduncertainty)andalsosomewhatmisplaced,thematch
in time (hourly output). Many examples can be pro- is within 1hPa at 1000 and 1100 UTC (spread 0.5hPa at
videdorhavealreadybeenreportedintheliterature.For 1200 UTC), and the analysed position is highly accurate
example,thepositiveeffectonthequalityofnear-surface at1100UTC.ERA5providesadetailedviewofwindgust
wind is described in Olauson (2018). Re-forecasts from (oneoftheavailableparameters,originatingfromtheshort
ERA5 reanalysis fields are more skilful than those from forecasts linking analysis windows), with maximum val-
ERA-Interim, as was demonstrated in Figure 1. ERA5 uesupto42m⋅s−1 intheBlackForestandFrenchAlpine
improves the representation of tropical cyclones. Cen- area. Maximum observed gusts in the Black Forest area
tral pressures are lower, and closer to those of the were59m⋅s−1(DWD,2000).
ECMWF operational HRES analysis than is the case for Asynopticexampleforthestratosphereisdisplayedin
ERA-Interim (F. Prates, 2018, personal communication). Figure19.Itmapstheexceptionalbreak-upofthesouth-
An illustration of this is provided in Hersbach (2019) for ernpolarvortexinlateSeptemberandearlyOctober2002.
hurricaneFlorence,whichhittheeastcoastoftheUSAon Water vapour is close to a conserved variable at the level
15September2018. shown, and no humidity observations are assimilated at
Thebenefitofhourlytemporalresolutionisillustrated this level. It thus serves as a convenient tracer to illus-
in Figure 18 which shows the evolution of storm Lothar trate the short-term dynamics of the polar stratospheric
at0900,1000and1100UTCon26December1999when vortex, despite quantitative limitations. Prior to break-
itsweptrapidlythroughWesternEuropeafteritslandfall down,thevortexischaracterisedbyarelativelyhighabun-
inBrittany,earlyinthemorningofthatday(Wernlietal., danceofwatervapour.Theperformanceoftheoperational
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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
for rules
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |     |     |     |     |     |     |     |     |        |         | 2031 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---- |
|               |     |     |     |     |     |     |     |     | FIGURE | 18 ERA5 |      |
analysisofmeansealevel
pressure(contours,instepsof
(a) 26 December 1999 09 UTC (b) 26 December 1999 10 UTC (c) 26 December 1999 11 UTC
| 980 |     |     |     |     |     |     |     |     | 2 .5 h P a ) a | n d w in d g u s t    | w it h in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------------------- | --------- |
|     |     |     | 980 |     |     |     | 0   |     |                |                       |           |
|     |     |     |     |     |     |     | 8   |     | th e p re c e  | d i ng h o ur ( c o l | ou r s,   |
9
|     |     | 0   |     |     |     |     |     |     | m⋅s−1)forstormLotharon26 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- |
9
9
|     |     |     |     | 969 |     | 990 | 970 |     | December1999at(a)0900, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
966
(b)1000,and(c)1100UTC.
990 970
| 990 |     |     |     |     |     |      |     |     | PressureminimaforERA5are |                  |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------------------------ | ---------------- | --- |
|     | 980 |     |     | 980 |     |      |     |     | 971/969/970hPaandmaximum |                  |     |
|     |     |     |     |     |     |      | 9 9 |     |                          | ⋅ s−1,for        |     |
|     |     |     |     |     |     | 1000 | 0   |     | gu st s a re             | 4 2 / 4 1 /4 2 m |     |
1000
|     |      | 990 |     | 990  |     |     |     |     | 0 90 0 /1 0 00 | / 1 1 0 0 U T C ,     |               |
| --- | ---- | --- | --- | ---- | --- | --- | --- | --- | -------------- | --------------------- | ------------- |
|     |      |     |     |      |     |     | 1   |     | r es p e ct iv | ely . E n s e m b l e | s p re a d at |
|     | 1000 |     |     | 1000 |     |     | 0 0 |     |                |                       |               |
0
|     |     |     |     |     |     |     |     | 1000 | m in i m u m | p r es s u r e lo c a | t io n i s |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --------------------- | ---------- |
2.1/0.5hPaat0900/1200UTC,
1000
respectively.Reddotsandvalues
markthepositionandpressure
(hPa)ofthereportedlow.Red
|     | 15  | 25  | 30  |     | 35  | 40  | 45  |     | plusesindicatetheERA5native |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
grid
(a) ERA-Interim (b) ERA-Interim (c) ERA-Interim (d) ERA-Interim
|     |     | 22 September |     |     | 26 September |     | 30 September |     |     | 4 October |     |
| --- | --- | ------------ | --- | --- | ------------ | --- | ------------ | --- | --- | --------- | --- |
L
L
|     | H   |     |     |     |     |     |     |     | L   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | H   | L   |     | H   | L   |     | H   |     |
L
|     |     | L   |     |     |     |     |     |     |     | L   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | L   | H   |     |     |     |     |     |     |
H
(e) ERA5 22 September (f) ERA5 26 September (g) ERA5 30 September (h) ERA5 4 October
L
L
|     | H   |     |     |     |     |     |     |     | L   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | H   | L   |     | H   | L   |     | H   |     |
L
|     |     | L   |     |     |     |     |     |     |     | L   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | L   | H   |     |     |     |     |     |     |
H
|     |     |     | 3.5 | 4   | 4.5 | 5 5.5 | 6 6.5 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- |
Water vapour (ppm)
FIGURE 19 AnalysesovertheSouthernHemisphereoftheabundanceofwatervapour(molefractioninppm;shading)and
Montgomerypotential(contourinterval4,000m2s−2)onthe850Kisentropicsurface,for(a,e)22,(b,f)26and(c,g)30Septemberand
(d,h)4October2002,from(a–d)ERA-Interimand(e–h)ERA5
ECMWFsystematthetimeisdiscussedbySimmonsetal. fromit.Remnantsofthismaterialcanbeseenwithinthe
(2005). flanking anticyclones south of Australia and over south-
On the first day shown, 22 September, the polar vor- ern South America. By 26 September the vortex has split
texisalreadyelongated,andhasbeenreducedtoasmaller completely into two similarly sized parts, and the domi-
sizethanusualbyasuccessionofeventsthatstripmaterial nant anticyclone in the Australian sector extends to the

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2032                                               |             |      |             |          |          |             |          |     |     | HERSBACHetal. |             |
| -------------------------------------------------- | ----------- | ---- | ----------- | -------- | -------- | ----------- | -------- | --- | --- | ------------- | ----------- |
| South Pole.                                        | Thereafter, |      | the vortex  | in the   | Pacific  | sector is   | (a) Mean |     |     |               |             |
|                                                    |             |      |             |          |          |             |          |     |     | ERA5          | ERA-Interim |
| stretchedaroundthenorthernflankofthisdominantanti- |             |      |             |          |          |             | 0        |     |     |               |             |
| cyclone,                                           | and breaks  | into | several     | smaller  | vortices | due to      | -4       |     |     |               |             |
| dynamical                                          | instability | of   | the ambient | easterly |          | flow. Three |          |     |     |               |             |
-8
| of these | vortices | are evident | in  | the maps | for | 4 October. |     |     |     |     |     |
| -------- | -------- | ----------- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
-12
ThecorrespondingvortexintheIndianOceansectorloses
|              |               |     |              |     |                |     | 1980 1985 | 1990 1995 | 2000 | 2005 2010 | 2015 |
| ------------ | ------------- | --- | ------------ | --- | -------------- | --- | --------- | --------- | ---- | --------- | ---- |
| lessmaterial | inthisway,and |     | iseventually |     | re-established |     |           |           |      |           |      |
(b) Standard deviation
| as the primary | polar | vortex, | albeit | a   | much | weaker one |     |     |     |     |     |
| -------------- | ----- | ------- | ------ | --- | ---- | ---------- | --- | --- | --- | --- | --- |
6
| than is | usual for | October. | This succession |     | of  | events was |     |     |     |     |     |
| ------- | --------- | -------- | --------------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
4
| also seen | in the | operational | analyses |     | at the | time. Sim- |     |     |     |     |     |
| --------- | ------ | ----------- | -------- | --- | ------ | ---------- | --- | --- | --- | --- | --- |
monsetal.(2005)notethattheoperationalanalyseswere
2
| consistent | with the | 10hPa | temperature |     | and | wind mea- |     |     |     |     |     |
| ---------- | -------- | ----- | ----------- | --- | --- | --------- | --- | --- | --- | --- | --- |
0
|     |     |     |     |     |     |     | 1980 1985 | 1990 1995 | 2000 | 2005 2010 | 2015 |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---- | --------- | ---- |
surementsfromAustralianandneighbouringradiosondes
| during | the passage | of  | the smaller | vortices |     | around the |           |                                         |     |     |     |
| ------ | ----------- | --- | ----------- | -------- | --- | ---------- | --------- | --------------------------------------- | --- | --- | --- |
|        |             |     |             |          |     |            | FIGURE 20 | (a)Monthlymeansand(b)standarddeviations |     |     |     |
anticyclone.
of4D-Var(backgroundminusobservation)departuresof2m
| ERA5 | and ERA-Interim |     | are | very similar | in  | their syn- |     |     |     |     |     |
| ---- | --------------- | --- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
temperature(K)atLongyearbyen,Svalbard,Norway(78.2◦N,
optic evolution. The filaments of air drawn from the 15.5◦E)forERA-Interim(blue)andERA5(red)
vorticesorentrainedaroundthemaresharperandricher
| in structure | in ERA5, |     | as expected | given | its | higher res- |     |     |     |     |     |
| ------------ | -------- | --- | ----------- | ----- | --- | ----------- | --- | --- | --- | --- | --- |
olution, and the small vortices in the Australian sector The agreement found previously among various
are a little stronger. ERA5 benefits from further refine- datasetsincludingERA-Interimledtotheexpectationthat
mentsoftheassimilatingmodel'ssemi-Lagrangianadvec- timeseriesofglobal-meantemperaturefromERA5would
tion scheme (Diamantakis, 2014; Diamantakis and Mag- notbesubstantiallydifferenttothosefromERA-Interim.
nusson, 2016) and is accordingly free of the noise that This is confirmed by Figure 21. The largest differences
occurs in the easterly flow on the southern flank of betweenERA5andERA-Interimoccurin2005and2006,
the Pacific sector vortex in the ERA-Interim analysis for aperiodwhenthedifferencesamongvariousdatasetsare
26September. relativelylarge.Thisisalsoaperiodinwhichdifferences
inSSTanalysisarequitelargeandinwhichthereanalyses
|     |     |     |     |     |     |     | have large anomalies | in  | polar regions | that are | not sam- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------- | -------- | -------- |
9 PERFORMANCE OF pledwellbytheconventionalanalyses.Differencesinthe
LOW-FREQUENCY VARIABILITY relationshipbetweenSSTandmarineairtemperaturealso
AND CLIMATE TRENDS play a part. Relatively large differences among datasets
havehappenedagainrecently,butinthiscaseERA5and
9.1 Surfaceairtemperature ERA-Interim (which at this time use common SST and
seaiceanalyses)giveverysimilarresults.
Since April 2019, ERA5 analyses of 2m temperature are The global fit of the analysis to observations shows
used as input to monthly summaries published by the little drift over time (not shown). The background fore-
C3S. Before that they had been based on ERA-Interim castshaveaglobalcoldbiasthatislargelyremovedbythe
foralmost4years.SuchanalysesfromERA-Interim,and optimalinterpolationscheme:themonthly-meananalysis
earlieronesfromERA-40,havebeenshowntobeofrea- fitvaries betweenzeroand –0.16K,and itsannual range
sonablequalityandcomplementarytotheproductsofcon- decreasesovertime.Thesevariationsaresmallcompared
ventionalanalysesofclimatologicalstationdata(Simmons withtheriseinmeantemperatureoverland,whichforthe
etal.,2017,andreferences). past four decades has been rather larger than the rise in
A number of regional and local improvements are global-meantemperatureshowninFigure21.
| found in | ERA5.   | An example   | is       | displayed | in  | Figure 20   |     |     |     |     |     |
| -------- | ------- | ------------ | -------- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
| which    | shows a | considerably | improved |           | fit | to observa- |     |     |     |     |     |
tions for a location in the Arctic. Annual-mean anal- 9.2 Globalbalance
| ysis increments |     | are smaller | in  | most | regions. | This is |     |     |     |     |     |
| --------------- | --- | ----------- | --- | ---- | -------- | ------- | --- | --- | --- | --- | --- |
largelyduetosmallermeanbackgrounderrors,although The extent to which the sequence of ERA analyses
some differences have been traced to differences in achieves global balance of quantities such as mass and
data quality control: ERA5 rejects fewer data as it has waterprovidesmeasuresoftheconsistencyoftheseanal-
fewer instances of large differences from background yses, and of general progress made in DA and in obser-
values. vational quality and coverage. The approach adopted for

HERSBACHetal. 2033
12-month running global mean 2m temperature anomaly (K) ERA5 ERA-Interim
0.8
ERA5 ERA-Interim Six other datasets 983.4
0.6
983.2
0.4
0.2 983
0 982.8
-0.2 1980 1985 1990 1995 2000 2005 2010 2015
-0.4
1980 1985 1990 1995 2000 2005 2010 2015 FIGURE 22 Monthlyestimatesfrom1979onwardsofthe
contributionofdryairtotheglobal-meansurfacepressure(hPa)
FIGURE 21 Twelve-monthrunningaveragesfrom1979
fromERA5(red)andERA-Interim(blue),computedbysubtracting
onwardsofglobal-meansurfaceairtemperatureanomalies(K)
thecontributionfromthetotalwatercontentoftheatmosphere
relativeto1981–2010forERA5(red)andERA-Interim(blue).Grey
fromtheglobal-meansurfacepressure
linesdenotethespreadfromsixotherdatasets:JRA-55(Kobayashi
etal.,2015);GISTEMPversion4(Hansenetal.,2010);HadCRUT4
(Moriceetal.,2012);NOAAGlobalTempversion5(Karletal.,2015);
rise and fall in dry mass centred around the year 2000.
aninfilledversionofHadCRUT4fromCowtanandWay(2014);and
In contrast, dry mass increases quite sharply in the early
adatasetfromtheBerkeleyEarthSurfaceTemperatureProject.For yearsofERA5,butisreasonablyuniformafter1990.The
ERA-Interim,valuesoverseaweretakenfromthefirstguessrather
rangeofvaluesisalittlelargerinERA5thanERA-Interim.
thantheanalysis,andpriorto2002seapointsarefurtheradjusted
The ERA5 rise in dry mass in the early and late 1980s is bysubtracting0.1K
due to rises in the global mean of the analysed surface
pressure that are not accompanied by rises in analysed
ERA5anditspredecessorscontrastswiththatadoptedby moisturecontent(notshown).Thevariationsindrymass
the producers of the MERRA-2 reanalysis (Gelaro et al., in ERA-Interim are likewise due mainly to variations in
2017), for which the assimilation method preserves, to global-meansurfacepressurethatarenotmatchedbyvari-
firstorder,thephysicalglobalconstraintofconservationof ationsinthecontributionfrommoisture.Reasonsforthe
dry-airmass(Takacsetal.,2016). different variations in surface pressure analyses have yet
Berrisford et al. (2011) examined the global atmo- to be identified. However, given that the spurious vari-
sphericbudgetsfromERA-Interimandmadecomparisons ations occur in different periods in the two reanalyses,
withERA-40.Althoughmostmeasuresindicatedimprove- theseproblemsmaywellbeduetoseparatecausesineach
mentofERA-InterimoverERA-40,thiswasnotthecase reanalysis.
fortheglobalbudgetofdrymassfortheyearscompared Aspectsoftheglobalhydrologicalbudgetarepresented
(1989–2002).Neglectingtheeffectsoffossilfuelburning, inFigure23.Variationsovertimeandimbalancearegen-
which contribute a variation of approximately 0.01hPa, erallylargerinERA-InterimthaninERA5.Thedegreeof
dryairmassisexpectedtobeapproximatelyconservedin global annual balance between precipitation and evapo-
the atmosphere (Trenberth and Smith, 2005). Given that ration in ERA5 changes over time. Balance is quite good
there are no constraints on the global dry mass in the foraperiodoftwentyorsoyearsfromthemid-1990s.The
DAsystem,theanalysedvariationsoftheglobaldrymass change that brings better balance at that time appears to
provideasimplemeasureofthequalityofthereanalysis. be in values over sea, where evaporation increases more
AsshownearlierbyTrenberthandSmith(2005),ERA-40 sharplythanprecipitation.Anearliergradualdecreasein
performed much more poorly prior to the early 1970s. marine precipitation is not matched by a corresponding
This was found by Uppala et al. (2005) to be associated decreaseinevaporation,whichalsoimprovesthebalance.
with higher analysed surface pressure, particularly over IntheperiodwhenERA5isingoodbalance,bothpre-
the data-sparse oceans of the Southern Hemisphere, and cipitationandevaporationincreaseoversea,butnotover
withloweranalysedwatervapourpriortoassimilationof land. An increase over sea has been inferred from salin-
IRsoundings,whichbeganin1973. ityobservations(DurackandWijffels,2010),butFigure23
Thedrymassoftheatmosphereisestimatedfromthe shows a much smaller increase in marine precipitation
global-meansurfacepressurebysubtractingthecontribu- fromtheGPCP(Adleretal.,2003)thanfromERA5.Inter-
tionfromthewatercontentoftheatmosphere.Figure22 annualvariationsinnetprecipitationoverlandfromERA5
shows the dry mass for ERA5 and ERA-Interim. Neither agree quite well with values from GPCP and the under-
reanalysisconservesthecontributionofdryairtosurface lying data from GPCC2 (Becker et al., 2013). Although
pressuretowithin0.3hPaoverthewholeperiod.However,
they differ in behaviour; ERA-Interim has similar values 2Datadownloadedfromhttps://www.dwd.de/EN/ourservices/gpcc/
at the beginning and end of the period, but a spurious gpcc.html;accessed13April2020
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

2034 HERSBACHetal.
12-month running global mean precipitation ( ) and evaporation ( ) (mm/day)
(a) ERA-Interim (b) ERA5
3 3
2.9 2.9
2.8 2.8
2.7 2.7
GPCP precip GPCP precip
2.6 2.6
1980 1985 1990 1995 2000 2005 2010 2015 1980 1985 1990 1995 2000 2005 2010 2015
2.6 2.6
(c) ERA-Interim contribution from sea (d) ERA5 contribution from sea
2.5 2.5
2.4 2.4
2.3 2.3
2.2 2.2
2.1 2.1
GPCP precip GPCP precip
2 2
1980 1985 1990 1995 2000 2005 2010 2015 1980 1985 1990 1995 2000 2005 2010 2015
(e) ERA-Interim contribution from land (f) ERA5 contribution from land
0.7 0.7
0.6 GPCP precip GPCP precip 0.6
GPCC precip GPCC precip
0.5 0.5
0.4 0.4
1980 1985 1990 1995 2000 2005 2010 2015 1980 1985 1990 1995 2000 2005 2010 2015
FIGURE 23 Twelve-monthrunningaveragesfrom1979onwardsofglobalmeanprecipitation(blue)andevaporation(red)rates
(mm⋅day−1)from(a)ERA-Interimand(b)ERA5.Theprecipitationestimatesfromversion2.3ofGPCParealsoshown(green).The
correspondingcontributionstotheseglobalaveragesfrom(c,d)seaand(e,f)landarealsoshown.Contributionsfromlandarealsoshownin
(e,f)forestimatesfromGPCC(brown).ThelatterarebasedonGPCC'sv.2018monthlyfull-dataproductuntiltheendof2016,version6ofits
monitoringproductformostofthefollowingperiod,anditsfirst-guessmonthlyproductforthelatest2months
animprovementoverERA-Interiminthisrespect,ERA5 3B43 dataset (Huffman et al., 2010) is used in this eval-
exhibits a larger decline in precipitation over land from uation.Thedatasetcoverstheperiodfrom1998onwards
the 1980s and 1990s to the 2000s than is the case for and the region from 50◦S to 50◦N. It utilizes data from
ERA-Interim(discussedbySimmonsetal.,2014).Sucha TRMM until April 2015 and from several other satellite
declineisnotseenintheGPCCandGPCPdata,andwas instrumentsmeasuringinthemicrowaveortheinfrared.
not expected in ERA5 as it addressed issues believed to Analysesofdirectprecipitationmeasurementsbygauges
beresponsibleforthisbehaviourinERA-Interim.Further over land from GPCC (Becker et al., 2013) are also used
effortisneededtounderstandthesefindings. in producing the TRMM/3B43 dataset. The dataset has
0.25◦ spatial resolution, and the ERA data are interpo-
latedtothisgridtomakethecomparisons.Thedatasetis
9.3 Comparisonoflong-term notentirelyindependentofERA,asERA-Interim,ERA5
andmonthlyaverageprecipitationrates and TRMM/3B43 all make use of precipitation informa-
tionfrommicrowaveimagery,albeitindifferentways,and
In addition, long-term and monthly average precipita- the estimates of rainfall rate over the USA assimilated in
tionratesfromERA-InterimandERA5havebeenevalu- ERA5frommid-2009onwardsmakeuseofUSgaugedata
atedbycomparingthemwithvaluesfromotherdatasets. thatarealsousedinformingtheGPCCdatasets.
Figure 24 presents an example. Version 7 of NASA's Figure24showsmapsofthemeandifferences(reanal-
TRMM Multi-satellite Precipitation Analysis (TMPA) ysis minus TRMM/3B43) for ERA-Interim and ERA5 for
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal.   |     |     |     |     |         |                |             |       |     |     | 2035     |
| --------------- | --- | --- | --- | --- | ------- | -------------- | ----------- | ----- | --- | --- | -------- |
|                 |     |     |     |     | -3 0 -4 | -1.5 -0.6 -0.1 | 0.1 0.6 1.5 | 4 30  |     |     |          |
| (a) ERA-Interim |     |     |     |     |         |                |             |       |     |     | (b) ERA5 |
| (c) ERA-Interim |     |     |     |     |         |                |             |       |     |     | (d) ERA5 |
|                 |     |     |     |     | -50 10  | 30 45 60       | 74 83 89    | 95 98 |     |     |          |
Correlation (%)
FIGURE 24 Meandifferencebetween(a)ERA-InterimandTMPA/3B43,andbetween(b)ERA5andTMPA/3B43precipitationrates
(mm⋅day−1)for1998–2018.(c,d)showthecorrespondingcorrelations(%)ofthesequenceofmonthlyvaluesfromthetwopairsofdatasets.
Themeanannualcycleisremovedfromeachdatasetpriortocalculatingthecorrelations
theperiod1998–2018,andthecorrespondingcorrelations thosefromERA-InterimandJRA-55.NeverthelessERA5
ofmonthlyanomaliesrelativetothe1998–2018meansfor exhibitsshiftsovertimecomparedwithGPCCandGPCP.
each month. Differences from TRMM/3B43 are in most In particular, differences between ERA5 and both GPCC
respects smaller for ERA5 than ERA-Interim, including and GPCP exhibit a distinct decline for a few years cen-
alongmountainrangesandcoastlines,offshoreofeastern tredontheyear2000overseveralregions,especiallyover
NorthAmericaandAsia,andovertheCongoBasin.Differ- theCongoBasinandsoutheasternChina.Differencesare
encesarelargerovertheITCZintheeasternPacific,and steadier thereafter. This can be seen in the net contribu-
over the extratropical Pacific, South Atlantic and Indian tions to global precipitation from all land areas that are
Oceans. Overall, the mean absolute difference over the shown for ERA5, GPCC and GPCP in Figure 23. Over-
domainfrom50◦Sto50◦Nis0.58mm⋅day−1forERA5and all, the 1979–2018 whole-globe correlations for the 2.5◦
0.65mm⋅day−1forERA-Interim.
|     |     |     |     |     |     |     | resolution | GPCP dataset | are 77% | for ERA5 | and 67% for |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ------- | -------- | ----------- |
ERA5 is also closer than ERA-Interim is to ERA-Interim. The correlations for this period with the
TRMM/3B43 in its representation of the temporal vari- 1◦ resolutionGPCCdataset,whichcoversalllandexcept
ability of monthly precipitation. The correlation maps in Antarctica,are63%forERA5and50%forERA-Interim.
| Figure 24                        | show this | to be      | widespread, |      | including       | regions |     |                                |     |     |     |
| -------------------------------- | --------- | ---------- | ----------- | ---- | --------------- | ------- | --- | ------------------------------ | --- | --- | --- |
| suchastheeasternPacificITCZwhere |           |            |             |      | meandifferences |         |     |                                |     |     |     |
|                                  |           |            |             |      |                 |         | 9.4 | IntercomparisonofERA5upper-air |     |     |     |
| are larger,                      | as well   | as regions | where       | mean | differences     | are     |     |                                |     |     |     |
fields
| smaller. | Improvement | occurs | both | over | the | extratropical |     |     |     |     |     |
| -------- | ----------- | ------ | ---- | ---- | --- | ------------- | --- | --- | --- | --- | --- |
regionsandtropicaloceaniczoneswherecorrelationsare
already quite high in ERA-Interim, and over the trop- This section examines the temporal evolution of
ical land masses where ERA-Interim has particularly upper-air temperature and ozone fields from ERA5 and
|                   |              |     |     |          |      |           | includes | some comparison | with | three | other reanalyses |
| ----------------- | ------------ | --- | --- | -------- | ---- | --------- | -------- | --------------- | ---- | ----- | ---------------- |
| low correlations. | Correlations |     |     | computed | over | the whole |          |                 |      |       |                  |
domainare70%forERA5and63%forERA-Interim. (ERA-Interim, JRA-55, and MERRA-2) for selected pres-
surelevels.Notethatacomparisonwithobservation-based
| Comparisons | (shown |     | in Figure | S5) | have | also been |     |     |     |     |     |
| ----------- | ------ | --- | --------- | --- | ---- | --------- | --- | --- | --- | --- | --- |
madewiththeGPCCandGPCPdatasetsandwithJRA-55, datasets,suchasradiosondesorsatelliteretrievals,isnot
for 12-month continental averages over the full period included here but can be found in the recent literature,
|            |                |     |         |             |     |            | in particular | Davis et | al. (2017) | and Long | et al. (2017)3. |
| ---------- | -------------- | --- | ------- | ----------- | --- | ---------- | ------------- | -------- | ---------- | -------- | --------------- |
| from 1979. | Interpretation |     | of mean | differences |     | is compli- |               |          |            |          |                 |
catedbydifferencesbetweenGPCCandGPCPdueinpart
to the adjustments for gauge undercatch made in GPCP 3NotethatthesetwopapersdonotusedatafromERA5.However,
butnotinGPCC,asalreadyfoundforERA-Interim(Sim- asofwriting,anupdatedversionofDavisetal.(2017)thatevaluates
ERA5isinpreparation(M.IHegglinandS.MDavis,2019,personal
| mons et | al., 2010). | Long-term |     | variations | from | ERA5 are |     |     |     |     |     |
| ------- | ----------- | --------- | --- | ---------- | ---- | -------- | --- | --- | --- | --- | --- |
communication)
| generally | closer to | those | from GPCC | and | GPCP | than are |     |     |     |     |     |
| --------- | --------- | ----- | --------- | --- | ---- | -------- | --- | --- | --- | --- | --- |

2036 HERSBACHetal.
(a) (b)
(c) (d)
(e)
FIGURE 25 Height–timeevolutionofmonthlyandgloballyaveragedanomaliesin(a)temperatureand(b)ozonepartialpressure
fromERA5.Theanomaliesarecalculatedbyremovingthe1981–2010monthlyclimatologyofERA5.Timeseriesof12-monthrunningmean
(c)global-averagetemperatureanomaliesat3,5,30,and500hPa;(d)global-averageozonepartialpressureanomaliesat70hPa;and(e)
Septembermeantotalcolumnozone(TCO3)averagedoverAntarctica(90◦S–60◦S).ThetimeseriesarebasedondatafromERA5(red),
ERA-Interim(blue),JRA-55(green),andMERRA-2(orange).In(c),thetimeseriesofERA5.1(Section3givesdetails)arealsoshownforthe
3and5hPalevels.(e)includesTCO3timeseriesfromaC3Smergedsatelliteproduct(Copernicus,2019)labeled‘Obs’(black)inthelegend.
Allanomaliesarecalculatedwithrespecttothe1981–2010monthlyclimatologyofeachdataset.In(a)and(b),theverticalspaceispartioned
equallybetweenpressurelevelsbelowandabove100hPa.In(c),notethedifferentintervalsusedintheverticalforeachpressurelevel
Furthermore,time seriesofseveralupper-airfieldsfrom reanalyses,althoughMERRA-2anomaliesremainslightly
ERA5wereincludedforthefirsttimeinthe2019annual lower (higher) during the 1980s (1990s). At 30hPa, the
“StateoftheClimate”report(BlundenandArndt,2019). four reanalyses exhibit very similar interannual variabil-
Figure25adisplaysthetime–heightevolutionofglob- ity but reveal some differences in the overall trend, with
allyaveragedupper-airtemperatureanomaliesfromERA5 ERA5(ERA-Interim)suggestinglarger(smaller)cooling.
whileFigure25ccomparestimeseriesoftheseanomalies The behaviour of ERA-Interim may be related to a cold
with those from ERA-Interim, JRA-55, and MERRA-2 at bias in the lower stratosphere which persists through
fourpressurelevels.Theselevelsarerepresentativeofthe the early 2000s but is then largely corrected through the
mid-troposphere (500hPa), lower stratosphere (30hPa), assimilationofGNSS-RObendingangles(Simmonsetal.,
and upper stratosphere (5 and 3hPa). Both figures high- 2014).Thisexplanationwouldthuslendmorecredenceto
light transient increases in the global mean temperature thetrendsoftheotherthreereanalyses.
related to well-known climatic events such as El Niño Spurious variations and inhomogeneities in ERA5
events (1983, 1987, 1998, 2010, 2016) in the troposphere, temperatures are more clearly apparent in the upper
and the volcanic eruptions of El Chichón (1982) and stratosphere(above10hPa)andaregenerallyconcurrent
Mount Pinatubo (1991) in the lower stratosphere. ERA5 with changes seen in the analysis increments (Figure 16
also captures the observed cooling of the latter and its andSection7.4).ThelargeinterannualvariabilityofERA5
levelling-off since the late 1990s (Randel et al., 2016; temperatures at 5 and 3hPa (Figure 25c) greatly exceeds
Maycocketal.,2018). thatseenintheotherthreereanalyses.Thedegradedskill
In Figure 25c, the temperature anomalies at 500hPa ofERA5relativetoERA-Interimmaycomeasasurprise
reveal close overall agreement between the four
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2037
giventheimprovedtreatmentofSSUobservationsimple- to ERA5 and MERRA-2 in Figure 25d can be explained
mented in ERA5 (Section 4.5). The largest anomalies in by the fact that this reanalysis did not directly assimilate
ERA5stratospherictemperaturesoccurintheearly1980s ozone observations but rather used ozone fields gener-
above 5hPa (Figure 25a) and clearly exceed the positive ated offline by a chemistry climate model (Kobayashi
anomalies seen in the other reanalyses during the same et al., 2015; Davis et al., 2017). The growing discrepancy
period (Long et al., 2017). In this instance, the pecu- between ERA5 and the other reanalyses from around
liar behaviour of ERA5 can be ascribed to a combina- 2015 onwards, which is associated with larger positive
tion of three factors: (a) the use of smaller correlation anomalies within 100–10hPa in Figure 25b, is not fully
length-scalesinthemodelbackground-errorestimatesin understoodatthisstage.
ERA5 compared to ERA-Interim, (b) the known warm Stratospheric ozone depletion during austral spring
bias of the IFS model in the upper stratosphere (Shep- over Antarctica has been an important driver of atmo-
herdetal.,2018),and(c)themoresporadicavailabilityof spheric changes in high southern latitudes in recent
SSUobservationsintheearly1980s.Thesubsequentsharp decades. Therefore, we conclude this section by compar-
drop in ERA5 temperature in early 1985 coincides with ing,inFigure25e,thetimeseriesofSeptembermeantotal
the transition between NOAA-7 SSU and NOAA-9 SSU columnozone(TCO3)averagedover90◦S–60◦Sfromthe
alreadycitedasaprobleminERA-InterimbyLongetal. fourreanalysespreviouslyused.Additionally,weinclude
(2017),albeitathigherlevels. output from a Level-4 merged satellite ECV product
Two other inhomogeneities in upper-stratospheric (Copernicus, 2019) spanning the 1979–2018 period. One
temperatures occur in 1998 and 2000 and can be linked, must keep in mind that this dataset is not independent
respectively,tothebeginningoftheanchoringofAMSU-A from the reanalyses since to a large extent both rely on
channel14observations(Section7.4)andtothechangein the same satellite observations. There is excellent agree-
B (Section2.4).Theimpactofthelatterismostvisiblein ment overall between ERA5 and the ECV product, with
cli
thevicinityof5hPa.Figure25cshowsthatthemarkeddis- the exception of September 1993 and (to a lesser extent)
continuityin2000atthispressurelevelallbutdisappears 1994. These two months fall within a period of reduced
in ERA5.1 (dashed red curve in Figure 25c), underscor- TCO3observationcoverage,betweentheendoftheNIM-
ing the significantly improved temporal consistency pro- BUS7TOMSrecordinmid-1993andthebeginningofthe
vided by this stream. At 3hPa, JRA-55 and ERA-Interim ERS-2GOMErecordinlate1995.Thelesserobservational
showremarkableagreementthroughouttheperiodwhile constraint during these two months has likely had some
the marked drop in MERRA-2 temperature in 2004 is an effectontheuncertaintyofTCO3estimatesfromthetwo
artefact known to be related to the assimilation of Aura products, making it difficult to tell which one should be
MSLtemperatureprofiles(Gelaroetal.,2017;Longetal., regardedasmorereliable.However,itisnoteworthythat
2017).Themarkedlyreducedtemperaturevariationsfrom ERA5estimatesforSeptember1993areverymuchinline
2006 onwards in all four reanalyses denote the greater with the previous and following years, which is not the
constraint on stratospheric temperatures provided by the caseoftheECVproduct.Furthermore,thelargerdiscrep-
assimilationofGNSS-ROobservations. ancies between MERRA-2 and ERA-Interim (on the one
Figure 25b shows the time–height evolution of ERA5 hand)andtheECVproductandERA5(ontheotherhand)
global mean anomalies in ozone partial pressure while in 1993–1995 can similarly be explained by the reduced
Figure 25d compares the time series of these anomalies observation availability (Davis et al., 2017). For example,
with those from the other three reanalyses at 70hPa. these authors found that MERRA-2 did not produce an
Above 100hPa, ERA5 captures the observed significant Antarcticozoneholein1994.Agreementisloweroverall
declineinstratosphericozoneduringthe1980sandearly betweenJRA-55andthefourotherdatasetsforthesame
1990s,followedbyagradualrecoveryinsubsequentyears reason already mentioned in the previous paragraph (no
(Steinbrecht et al., 2018). This recovery is exaggerated in directozoneDA).
ERA5byaspuriousincreaseinozonein2004at40–90hPa
(concurrent with a decrease at 90–150hPa), which can
be traced to the beginning of the assimilation of ozone
profilesfrom Aura MLS. Theseobservations were shown 10 CONCLUDING REMARKS
to cause inhomogeneities in the ozone field of other AND FUTURE DIRECTIONS
reanalyses as well (Davis et al., 2017), most notably in
MERRA-2 (Figure 25d). This figure also highlights large 10.1 ERA5strengths
interannualvariabilityinERA-Interimozonetimeseries,
whichDavisetal.(2017)foundtoexceedthatseeninthe As stated above, a major strength of ERA5 is the
observations. The distinct behaviour of JRA-55 relative much higher temporal and spatial resolutions than
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

2038 HERSBACHetal.
those of previous global reanalyses. The hourly out- 10.2 Knownissues
put, 31km horizontal resolution and 137 levels
spanning the surface of the Earth to 0.01hPa cap- An up-to-date list of known issues with more back-
ture much finer details of atmospheric phenomena ground information is provided in the ERA5 online data
than in previous, lower-resolution, global reanaly- documentation (https://confluence.ecmwf.int/display/
ses. The assimilation of a much larger number of CKB;accessed13April2020).
reprocessed datasets has also improved the reanaly- Although, compared to ERA-Interim, ERA5 benefits
sis products. As shown in this paper, the improvement from a decade of research and development at ECMWF,
with respect to ERA-Interim is considerable in the some aspects did not improve. The main example is the
troposphere. largercoldbiasinthelowerstratosphereandalargerwarm
The provision of the accompanying ensemble, which biasnearthestratopause.Asaresult,inthestratosphere
was not available for ERA-Interim, provides an uncer- the fit to radiosonde data is worse, and above 10hPa the
taintyestimateforthereanalysisproducts,whichismuch temporalconsistencyoftheERA5productiscompromised
soughtafterbyusersofthedata. duetothetime-evolvingcompetitionbetweenmodelbias
AnotheradvantageofERA5comparedtoERA-Interim and sparse observations. In addition, in the mesosphere,
isamuchshorterlatencyof5daysratherthan2–3months. wheretherearenoobservationstocontrolit,Cy41r2can
Based on experience of the production of ERA5 so far, it suffer from an overly strong tropical westerly jet, which
is expected that this preliminary product will only rarely particularly affects the transition seasons. The resulting
deviate from the fully quality-checked final product that volatility of this jet is one of the reasons why there can
is released 2 months later. This timely product serves be large discontinuities in the mesosphere at the transi-
importantclassesofuserneedingup-to-dateclimateinfor- tionpointsbetweendifferentproductionstreams.Another
mation in combination with a long consistent climate example of discontinuities at these transition points is
record. that of tropical stratospheric humidity, which is a slowly
In ERA-Interim, several different datasets for pre- evolvingquantity.
scribed SST and SIC were required to cover the 40-plus Although within the 12-hr assimilation windows the
yearsofthereanalysis,whichmadethesetwofieldsquite modelconstraintensuresasmoothhourlyproduct,anal-
inhomogeneous.ERA5hasonlyonesuchdatasetchange, ysis increments can introduce systematic jumps at the
in2007,soSSTandseaicearemorehomogeneousinERA5 transitionpointsbetweenthewindows.ForERA5thishas
thaninERA-Interim. beenobservedforwindintheboundarylayer.Forexample
InERA5,CMIP5specificationsprovidemorerealistic over Paris, France at 1000 UTC, ERA5 exhibits on aver-
inputtothemodelradiativeforcingthaninERA-Interim. age a jump of about 0.25m⋅s−1 in 10m wind speed. This
As a result, ERA5 has an improved response to major decreaseinwindspeedissmall,butsystematic,socanbe
volcaniceruptions. seeninclimatologies.
Following the initial release of ERA5, several inde- At specific locations, ERA5 occasionally produces
pendent studies have evaluated its performance. ERA5 amounts of precipitation that are unrealistically high.
performs well in the Arctic (Graham et al., 2019) and These“rainbombs"becameapparentintheIFSsincecycle
Antarctic(Tetzneretal.,2019)inrepresentingwinds,tem- 40r1 (which became operational in November 2013), at
peratureandhumidity.Mayeretal.(2019)foundexcellent whichtimechangestoitsconvectionschemewereintro-
closure of the Arctic energy budget using ERA5 atmo- ducedtocapturebetterthediurnalcycleofdeepconvec-
spheric data. The representation of irradiance fields has tion. Under very special conditions (moist air, low-level
beencomparedwithotherreanalyses(Trollietetal.,2018) orographic forcing with converging low-intensity winds)
andwithground-basedandsatelliteobservations(Urraca there is potential for “explicit-convection" at isolated
et al., 2018). The representation of precipitation over the grid-points (Malardel and Ricard, 2015). These features
continentalUSA,insupportofhydrologicalapplications, occur infrequently, of the order of ten episodes for an
has been evaluated relative to other modern reanalyses entireyearandmostlyconcentratedinAfrica,atisolated
(Xu et al., 2019) and observations (Tarek et al., 2019). grid-points mostly in orographic areas. This feature was
Finally,thecharacteristicsofERA5surfaceandlow-level laterresolvedintheIFSwiththeintroductionoftheocta-
winds over the ocean, relative to observations and other hedralreducedGaussiangrid.
reanalyses, has been the subject of several studies (Bel- Inmountainousregionsaboveabout1,500m,thesnow
monteRivasandStoffelen,2019;Olauson,2018;Kalverla depthisunrealisticallylarge.ThisisduetotheIFS'srep-
et al., 2019). Generally, ERA5 performs well in these resentation of the snow pack with a single layer of snow
comparisons. whichdoesnotproduceenoughmelting.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2039
In the northern winter of 1996/1997, the ozone val- In2020theperiodfrom1950to1978willbemadeavail-
ues in the upper stratosphere at high northern latitudes able.ThiswillextendthehourlyERA5recordto70years.
aremanytimeslargerthannormal.Thisproblemdoesnot Details on this extension and its characteristics will be
significantlyaffecttotalcolumnozone. reported elsewhere. The improved segment from 2000 to
Duetotheverylongspin-uptimeandnon-optimalini- 2006 (ERA5.1) was recently made available as a separate
tialization, some soil parameters, such as root-zone soil product. It provides better global-mean temperatures in
moisture, show discontinuitiesat the transition points of the stratosphere and uppermost troposphere, with very
someoftheproductionstreams. similarperformanceinthelowerandmiddletroposphere.
Besides these limitations, there were several produc- Alsoin2020accesswillbeprovidedto12-hourlyaver-
tion oversights that could have been prevented. From aged statistics of the ERA5 observation usage. This will
1979 to 2013, the SST was not used over the Great Lakes include information on first-guess and analysis depar-
to nudge the lake model, as it should have been. Con- tures, bias estimates, and applied observation errors and
sequently, the 2m temperature over these lakes has an quality control. This will, for example, allow the repro-
annual cycle that is too strong, with temperatures being ducibilityofERA5curvesinmostoftheobservation-based
toocoldinwinterandtoowarminsummer.Thisproblem Figuresofthispaper.
isparticularlypronouncedoverLakeSuperior.Overother
confinedareas,likeoverthenorthernCaspianSeaandthe
Gulf of Finland, systematic differences between the SST 10.4 Futuredirections
productsusedbefore(HadISST2)andafter2007(OSTIA)
areknowntoexist. The interaction between model bias and an evolving
The prescribed sea ice field tends to exhibit sea ice observingsystem(whichcomprisescomponentsthatgen-
in the Baltic Sea in summertime, which is not there in erally exhibit non-zero, and often significant, biases) is a
reality. Such occurrences of sea ice have been removed concerninclimatereanalysis,sinceitcanaffectthetem-
intheHRESERA5reanalysisbutitisstillpartlypresent poralconsistencyandaccuracyoftheproduct.Forfuture
intheten-memberensemble.However,itsimpactonthe reanalysisactivitiesatECMWF,researchisneededtotailor
ensemblespreadisfoundtobetempered. thelatestavailableformulationofweak-constraint4D-Var
Uptoonceortwiceperyear,theanalysednear-surface for reanalysis as well as the optimization of the use of
(e.g., 10m) winds in ERA5 suffer from a problem of anchordatainVarBC.Regardingweak-constraint4D-Var,
extremelylargewindspeeds;thelargestspeedsseensofar at ECMWF recently significant progress has been made
are of order 300m⋅s−1. Typically, these occur in the last inhandlingthemodelbiasinthestratosphere(Laloyaux
twoorthreehoursoftheassimilationwindowandonlyat et al., 2020). Potentially, large-scale model bias as esti-
oneofseveralpreferredlocationsaroundtheglobe,most mated from the recent well-observed era (i.e., including
ofwhichareneartoorographicfeatures.Amorethorough the availability of anchoring GNSS-RO data) can be used
quality check could have prevented such cases by using as a forcing term to temper the adverse effect of model
the solution that is followed when instabilities occasion- drift.Thiswouldmakethemeanstateofreanalysisprod-
ally occur in the 4D-Var tangent-linear physics. For the uctsmoreresilientwithrespecttochangesintheobserving
ERA5 timely updates, that check was implemented from system.
19February2020onwardstopreventfurtheroccurrences, The non-closure of energy budgets, and particularly
whileapracticalsolutionforexistingcasesisprovidedin itsevolutionovertime,needtobebetterunderstoodand
theonlinedocumentation. improved in future reanalysis, as well as the lack of con-
servationoftheglobaldrymassandhydrologicalbalance.
The hybrid incremental 4D-Var formulation in
10.3 Relatedproducts ERA5 allows for flow-dependent estimates of the
background-error covariance matrix. For future C3S
In conjunction with ERA5, a down-scaled land product reanalysis, a more dynamic system is to be put in place
hasbeenmadeavailable.ThisERA5-Landproduct,at9km thatallowsforanimprovedresponsetothemajorchanges
horizontal resolution (Muñoz-Sabater, 2019), was pro- in the observingsystem.For the ocean(and also land), a
ducedthroughasinglesimulationdrivenbynear-surface similar system would be required, such as to account for
atmospheric fields from ERA5, with thermodynamical the enormous change since the advent of Argo floats in
orographic adjustment of temperature. In addition to theearly2000s.Inaddition,prescribedobservationerrors
improving the quality of near-surface quantities, it pro- shouldevolveovertimetoreflectimprovementsininstru-
vides a more homogeneous dataset for soil parameters mentation, rather than to keep those constant over time
betweenERA5productionstreams. inERA5.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2040    |             |     |     |     |         |             |     |     | HERSBACHetal. |     |
| ------- | ----------- | --- | --- | --- | ------- | ----------- | --- | --- | ------------- | --- |
| TABLE   | 8 Glossary  |     |     |     | TABLE   | 8 Glossary  |     |     |               |     |
| Acronym | Description |     |     |     | Acronym | Description |     |     |               |     |
ADEOS-1 AdvancedEarthObservingSatellite1 ERA5 70-yearERAstartingfromJanuary1950onwards
withtimelyupdates
| AIRS   | AdvancedInfraredSounder |                    |            |     |        |                                           |     |     |     |     |
| ------ | ----------------------- | ------------------ | ---------- | --- | ------ | ----------------------------------------- | --- | --- | --- | --- |
|        |                         |                    |            |     | ERA-15 | 15-yearERAstartingfromJanuary1979toFebru- |     |     |     |     |
| AMSR-E | Advanced                | Microwave Scanning | Radiometer | for |        |                                           |     |     |     |     |
ary1994
EOS
|        |                                      |     |     |     | ERA-40      | 45-yearERAfromSeptember1957toAugust2002 |     |                 |          |     |
| ------ | ------------------------------------ | --- | --- | --- | ----------- | --------------------------------------- | --- | --------------- | -------- | --- |
| AMSR-2 | AdvancedMicrowaveScanningRadiometer2 |     |     |     |             |                                         |     |                 |          |     |
|        |                                      |     |     |     | ERA-20CM    | 20thCenturyECMWFModelintegration        |     |                 |          |     |
| AMSU-A | AdvancedMicrowaveSoundingUnit-A      |     |     |     |             |                                         |     |                 |          |     |
|        |                                      |     |     |     | ERA-Interim | 40-yearERAfromJanuary1979toAugust2019   |     |                 |          |     |
| AMSU-B | AdvancedMicrowaveSoundingUnit-B      |     |     |     |             |                                         |     |                 |          |     |
|        |                                      |     |     |     | ERA-CLIM    | EuropeanReanalysis                      |     | ofGlobalClimate | Observa- |     |
| AMV    | AtmosphericMotionVector              |     |     |     |             |                                         |     |                 |          |     |
tions
| ASCAT | AdvancedScatterometer                   |     |     |     |           |                    |     |                 |          |     |
| ----- | --------------------------------------- | --- | --- | --- | --------- | ------------------ | --- | --------------- | -------- | --- |
|       |                                         |     |     |     | ERA-CLIM2 | EuropeanReanalysis |     | ofGlobalClimate | Observa- |     |
| ATOVS | AdvancedTIROSOperationalVerticalSounder |     |     |     |           | tions2             |     |                 |          |     |
AVHRR AdvancedVeryHighResolutionRadiometer ERS EuropeanRemoteSensingSatellite
BUFR BinaryUniversal Form fortheRepresentation of ESA EuropeanSpaceAgency
meteorologicaldata
|      |                                       |     |     |     | ETOPO2   | 2-MinuteGriddedGlobalReliefData |     |         |              |     |
| ---- | ------------------------------------- | --- | --- | --- | -------- | ------------------------------- | --- | ------- | ------------ | --- |
| CAMS | CopernicusAtmosphereMonitoringService |     |     |     |          |                                 |     |         |              |     |
|      |                                       |     |     |     | EUMETSAT | European Organisation           |     | for the | Exploitation | of  |
| CCI  | (ESA)ClimateChangeInitiative          |     |     |     |          | MeteorologicalSatellites        |     |         |              |     |
| CDS  | C3SClimateDataStore                   |     |     |     | FCDR     | FundamentalClimateDataRecord    |     |         |              |     |
(C)ERA-20C (Coupled)ECMWFReanalysisofthe20thCentury FGGE FirstGARPGlobalExperiment
CERA-SAT CoupledECMWFReanalysisforthemodernsatel- GARP GlobalAtmosphericResearchProgram
|       | liteera                          |     |     |     | GCM  | GlobalCirculationModel       |          |              |            |     |
| ----- | -------------------------------- | --- | --- | --- | ---- | ---------------------------- | -------- | ------------ | ---------- | --- |
| CFSR  | ClimateForecastSystemReanalysis  |     |     |     |      |                              |          |              |            |     |
|       |                                  |     |     |     | GCOS | GlobalClimateObservingSystem |          |              |            |     |
| CHAMP | ChallengingMini-SatellitePayload |     |     |     |      |                              |          |              |            |     |
|       |                                  |     |     |     | GEMS | Global and                   | regional | Earth system | Monitoring |     |
CIMSS Cooperative Institute for Meteorological Satellite usingSatelliteandinsitudata
|     | Studies                 |     |     |     | GMAO | GlobalModelingandAssimilationOffice |     |            |         |     |
| --- | ----------------------- | --- | --- | --- | ---- | ----------------------------------- | --- | ---------- | ------- | --- |
| CKB | CopernicusKnowledgeBase |     |     |     |      |                                     |     |            |         |     |
|     |                         |     |     |     | GMI  | Global precipitation                |     | monitoring | mission |     |
CMIP5 CoupledModelIntercomparisonProject,Phase5 MicrowaveImager
| CMOD | C-bandmodel |     |     |     | GMS | GeostationaryMeteorologicalSatellite |     |     |     |     |
| ---- | ----------- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
CMSAF ClimateMonitoringSatelliteApplicationsFacility GNSS-RO GlobalNavigationSatelliteSystem–RadioOccul-
tation
| COSMIC | Constellation | Observing System | for Meteorology, |     |     |     |     |     |     |     |
| ------ | ------------- | ---------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
IonosphereandClimate GOES Geostationary Operational Environmental Satel-
lite
| CRIS  | Cross-TrackInfraredSounder            |     |     |     |      |                                       |           |         |          |     |
| ----- | ------------------------------------- | --- | --- | --- | ---- | ------------------------------------- | --------- | ------- | -------- | --- |
|       |                                       |     |     |     | GOME | GlobalOzoneMonitoringExperiment       |           |         |          |     |
| C3S   | CopernicusClimateChangeService        |     |     |     |      |                                       |           |         |          |     |
|       |                                       |     |     |     | GPCC | GlobalPrecipitationClimatologyCentre  |           |         |          |     |
| DMSP  | DefenseMeteorologicalSatelliteProgram |     |     |     |      |                                       |           |         |          |     |
|       |                                       |     |     |     | GPCP | GlobalPrecipitationClimatologyProject |           |         |          |     |
| DRIBU | ReportfromDriftingandmooredBuoy       |     |     |     |      |                                       |           |         |          |     |
|       |                                       |     |     |     | GRAS | Global Navigation                     | Satellite | Systems | Receiver | for |
| EC    | EuropeanCommission                    |     |     |     |      |                                       |           |         |          |     |
AtmosphericSounding
| ECMWF | European | Centre for Medium-Range | Weather |     |     |                               |     |     |     |     |
| ----- | -------- | ----------------------- | ------- | --- | --- | ----------------------------- | --- | --- | --- | --- |
|       |          |                         |         |     | GTS | GlobalTelecommunicationSystem |     |     |     |     |
Forecasts
|     |                          |     |     |     | HadISST2 | HadleyCentreSeaIceandSeaSurfaceTempera- |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | -------- | --------------------------------------- | --- | --- | --- | --- |
| ECV | EssentialClimateVariable |     |     |     |          |                                         |     |     |     |     |
turedataset
| EDA     | EnsembleofDataAssimilations |     |     |     |         |                                 |       |        |     |         |
| ------- | --------------------------- | --- | --- | --- | ------- | ------------------------------- | ----- | ------ | --- | ------- |
|         |                             |     |     |     | HRES    | HighResolutioncomponent(ofERA5) |       |        |     |         |
| ENVISAT | EnvironmentalSatellite      |     |     |     |         |                                 |       |        |     |         |
|         |                             |     |     |     | HIRS    | High-ResolutionInfraredSounder  |       |        |     |         |
| EOS     | EarthObservingSystem        |     |     |     |         |                                 |       |        |     |         |
|         |                             |     |     |     | HTESSEL | Revised Tiled                   | ECMWF | Scheme | for | Surface |
| ERA     | ECMWFReanalysis             |     |     |     |         | ExchangesoverLand               |       |        |     |         |

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
HERSBACHetal. 2041
| TABLE   | 8 Glossary  |     |     |         |             |     |     |
| ------- | ----------- | --- | --- | ------- | ----------- | --- | --- |
|         |             |     |     | TABLE 8 | Glossary    |     |     |
| Acronym | Description |     |     |         |             |     |     |
|         |             |     |     | Acronym | Description |     |     |
IASI InfraredAtmosphericSoundingInterferometer NOAA NationalOceanicandAtmosphericAdministra-
| ICOADS | International | Comprehensive | Ocean and Atmo- |     | tion(USA) |     |     |
| ------ | ------------- | ------------- | --------------- | --- | --------- | --- | --- |
sphereDataSet
|     |                          |                  |                 | OI  | Optimalinterpolation       |     |     |
| --- | ------------------------ | ---------------- | --------------- | --- | -------------------------- | --- | --- |
| IFS | IntegratedForecastSystem |                  |                 |     |                            |     |     |
|     |                          |                  |                 | OLR | OutgoingLong-waveRadiation |     |     |
| IMS | Interactive              | Multisensor Snow | and Ice Mapping |     |                            |     |     |
|     |                          |                  |                 | OMI | OzoneMonitoringInstrument  |     |     |
System
|      |                                       |     |     | ORASN  | NthECMWFOceanReanalysisSystem             |     |     |
| ---- | ------------------------------------- | --- | --- | ------ | ----------------------------------------- | --- | --- |
| IPCC | IntergovernmentalPanelonClimateChange |     |     |        |                                           |     |     |
|      |                                       |     |     | OSISAF | OceanandSeaIceSAF                         |     |     |
| IR   | InfraredRadiation                     |     |     |        |                                           |     |     |
|      |                                       |     |     | OSTIA  | OperationalSeaSurfaceTemperatureandSeaIce |     |     |
| IRAS | InfraredAtmosphericSounder            |     |     |        |                                           |     |     |
Analysis
ISPD InternationalSurfacePressureDatabank PILOT Windreportfrompilotballoon
| ITCZ   | InterTropicalConvergenceZone     |     |     |          |                                          |             |                  |
| ------ | -------------------------------- | --- | --- | -------- | ---------------------------------------- | ----------- | ---------------- |
|        |                                  |     |     | QuikSCAT | QuickScatterometer                       |             |                  |
| JAXA   | JapanAerospaceExplorationAgency  |     |     |          |                                          |             |                  |
|        |                                  |     |     | RAOBCORE | Radiosonde                               | Observation | Correction using |
| JMA    | JapanMeteorologicalAgency        |     |     |          | Reanalyses                               |             |                  |
|        |                                  |     |     | RICH     | RadiosondeInnovationCompositeHomogeniza- |             |                  |
| JRA-55 | Japanese55-yearReanalysisProject |     |     |          |                                          |             |                  |
tion
| LDAS | LandDataAssimilationSystem |     |     |      |            |             |                      |
| ---- | -------------------------- | --- | --- | ---- | ---------- | ----------- | -------------------- |
|      |                            |     |     | RISE | Radiosonde | adjustments | with solar elevation |
| LEO  | LowEarthOrbit              |     |     |      |            |             |                      |
dependence
| MACC | Monitoring | Atmospheric | Composition and Cli- |       |                                    |     |     |
| ---- | ---------- | ----------- | -------------------- | ----- | ---------------------------------- | --- | --- |
|      |            |             |                      | RRTMG | RapidRadiativeTransferModelforGCMs |     |     |
mate
|      |        |                |                        | RTTOV | RadiativeTransferforTOVS    |     |     |
| ---- | ------ | -------------- | ---------------------- | ----- | --------------------------- | --- | --- |
| MARS | ECMWF  | Meteorological | Archival and Retrieval |       |                             |     |     |
|      | System |                |                        | SARAL | SatellitewithARGOSandAltika |     |     |
McICA MonteCarloIndependentColumnApproximation SBUV SolarBackscatteredUltraViolet
MERRA-2 Modern-Era Retrospective analysis for Research SCIAMACHY ScanningImagingAbsorptionSpectrometerfor
|     | andApplications,Version2-2 |     |     |     | AtmosphericCartography |     |     |
| --- | -------------------------- | --- | --- | --- | ---------------------- | --- | --- |
METAR MeteorologicalAerodromeReports SEKF SimplifiedExtendedKalmanFilter
METEOSAT MeteorologicalSatellite SETTLS StableExtrapolationTwo-Time-LevelScheme
METOP MeteorologicalOperationalSatellite SIC SeaIceConcentration
|     |                          |     |     | SSM/I | SpecialSensorMicrowave/Imager |     |     |
| --- | ------------------------ | --- | --- | ----- | ----------------------------- | --- | --- |
| MHS | MicrowaveHumiditySounder |     |     |       |                               |     |     |
MIPAS MichelsonInterferometerforPassiveAtmospheric SSMI/S SpecialSensorMicrowaveImager/Sounder
Sounding
|     |                      |     |     | SST | SeaSurfaceTemperature     |     |     |
| --- | -------------------- | --- | --- | --- | ------------------------- | --- | --- |
| MLS | MicrowaveLimbSounder |     |     |     |                           |     |     |
|     |                      |     |     | SSU | StratosphericSoundingUnit |     |     |
MODIS ModerateResolutionImagingSpectroradiometer SSW SuddenStratosphericWarming
| MSU   | MicrowaveSoundingUnit             |     |     |        |                         |        |                       |
| ----- | --------------------------------- | --- | --- | ------ | ----------------------- | ------ | --------------------- |
|       |                                   |     |     | SYNOP  | SurfaceSynopticReport   |        |                       |
| MTSAT | MultifunctionalTransportSatellite |     |     |        |                         |        |                       |
|       |                                   |     |     | TEI    | TotalEnergyInput        |        |                       |
| MWHS  | MicrowaveHumiditySounder          |     |     |        |                         |        |                       |
|       |                                   |     |     | TEMP   | Reportfromradiosounding |        |                       |
| MWHS2 | MicrowaveHumiditySounder2         |     |     |        |                         |        |                       |
|       |                                   |     |     | TESSEL | Tiled ECMWF             | Scheme | for Surface Exchanges |
overLand
| NASA | National | Aeronautics and | Space Administration |     |     |     |     |
| ---- | -------- | --------------- | -------------------- | --- | --- | --- | --- |
(USA)
|       |                                       |                           |            | TIROS | TelevisionInfraredObservationSatellite |     |     |
| ----- | ------------------------------------- | ------------------------- | ---------- | ----- | -------------------------------------- | --- | --- |
| NASDA | NationalSpaceDevelopmentAgency(Japan) |                           |            |       |                                        |     |     |
|       |                                       |                           |            | TMI   | TRMMMicrowaveImager                    |     |     |
| NCEP  | National                              | Centers for Environmental | Prediction |       |                                        |     |     |
|       |                                       |                           |            | TOA   | TopOfAtmosphere                        |     |     |
(USA)
|        |                                               |     |     | TOMS | TotalOzoneMappingSpectrometer   |     |     |
| ------ | --------------------------------------------- | --- | --- | ---- | ------------------------------- | --- | --- |
| NESDIS | NationalEnvironmentalSatellite,Data,andInfor- |     |     |      |                                 |     |     |
|        | mationService(USA)                            |     |     | TOVS | TIROSOperationalVerticalSounder |     |     |
NEXRAD Next-GenerationRadarNetwork TRMM TropicalRainfallMeasuringMission

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2042 |     |     |     |     |     |     |     |     |     |     |     |     | HERSBACHetal. |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
TABLE 8 Glossary many people across ECMWF and from many collab-
|         |     |                      |             |     |     |             |     | orations.      | ECMWF    | implements    | the             | Copernicus |           | Climate |
| ------- | --- | -------------------- | ----------- | --- | --- | ----------- | --- | -------------- | -------- | ------------- | --------------- | ---------- | --------- | ------- |
| Acronym |     | Description          |             |     |     |             |     |                |          |               |                 |            |           |         |
|         |     |                      |             |     |     |             |     | Change Service |          | on behalf     | of the European |            | Union,    | and     |
| TSI     |     | TotalSolarIrradiance |             |     |     |             |     |                |          |               |                 |            |           |         |
|         |     |                      |             |     |     |             |     | ERA5 was       | produced | with          | funding from    | this       | Service.  | The     |
| UCAR    |     | University           | Corporation |     | for | Atmospheric |     |                |          |               |                 |            |           |         |
|         |     |                      |             |     |     |             |     | EU, through    | the      | 7th Framework | Programme,      |            | supported |         |
Research(USA) the ERA-CLIM and ERA-CLIM2 projects which served
UNFCCC UnitedNationsFrameworkConventiononCli- as precursors to the ERA5 reanalysis. The efforts of the
mateChange
|     |     |     |     |     |     |     |     | many scientists |     | involved | in these projects |     | is gratefully |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ----------------- | --- | ------------- | --- |
VarBC Variationalbiascorrection acknowledged. Preparation of ERA5 has been supported
VTPR VerticalTemperatureProfilingRadiometer by ECMWF staff, three of which were supported by the
ERA-CLIM2project,fundedbytheEuropeanUnion'sSev-
| WCRP |     | WorldClimateResearchProgramme |     |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
enthFrameworkProgramundergrantagreement607029,
| WMO |     | WorldMeteorologicalOrganisation |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
twoofwhichwerefundedbyEUMETSAT,andbystaffsec-
20CR TwentiethCenturyReanalysis ondmentsfromNCAS,aNERCCollaborativeCentre,and
4D-Var Four-DimensionalVariationaldataassimilation the JMA. ERA5 benefits from the usage of a large num-
berofreprocesseddatasetsthatwerepreparedbyCIMMS,
|     |     |     |     |     |     |     |     | ESA, EUMETSAT |     | Satellite | Application | Facilities |     | (SAF), |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ----------- | ---------- | --- | ------ |
ERA5 uncertainty estimates are based on the spread JMA, NASA, NASDA, NOAA, TU Wien and UCAR. The
Copernicus(2019)ozonedataweredownloadedfromthe
| in the | EDA component |     | which | mainly | samples |     | random |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ----- | ------ | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
C3SCDS.Inaddition,wethankthreereviewersfortheir
| error (although |     | the | perturbed | HadISST2 |     | realizations | do  |     |     |     |     |     |     |     |
| --------------- | --- | --- | --------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
valuablefeedback.
| introduce   | long-term |           | correlations |             | near the | surface). | More      |              |     |                                       |     |     |     |     |
| ----------- | --------- | --------- | ------------ | ----------- | -------- | --------- | --------- | ------------ | --- | ------------------------------------- | --- | --- | --- | --- |
| information | is        | desirable | on           | systematic  | errors   | which,    | for       |              |     |                                       |     |     |     |     |
| example,    | capture   | and       | explain      | large-scale |          | and       | long-term | ORCID        |     |                                       |     |     |     |     |
|             |           |           |              |             |          |           |           | HansHersbach |     | https://orcid.org/0000-0001-5330-7071 |     |     |     |     |
systematicdifferenceswithrespecttootherdatasets.
|                                                     |     |                          |     |     |     |               |     | JoaquínMuñoz-Sabater |     |                                       | https://orcid.org/0000-0002- |     |     |     |
| --------------------------------------------------- | --- | ------------------------ | --- | --- | --- | ------------- | --- | -------------------- | --- | ------------------------------------- | ---------------------------- | --- | --- | --- |
| Following                                           |     | user requirementanalyses |     |     |     | from communi- |     |                      |     |                                       |                              |     |     |     |
| ties,alargepartofthepreparationforfutureC3Sreanaly- |     |                          |     |     |     |               |     | 5997-290X            |     |                                       |                              |     |     |     |
|                                                     |     |                          |     |     |     |               |     | JulienNicolas        |     | https://orcid.org/0000-0003-0518-100X |                              |     |     |     |
sisarebeingaddressedatECMWF,whilepartofthework
takesplaceviaexternalC3ScontractswithotherEuropean DinandSchepers https://orcid.org/0000-0002-2611-
| organisationsandincludeswiderinternationalcollabora- |          |     |                |     |        |             |     | 487X          |     |                                       |     |     |     |     |
| ---------------------------------------------------- | -------- | --- | -------------- | --- | ------ | ----------- | --- | ------------- | --- | ------------------------------------- | --- | --- | --- | --- |
|                                                      |          |     |                |     |        |             |     | AdrianSimmons |     | https://orcid.org/0000-0002-7327-     |     |     |     |     |
| tions. This                                          | includes |     | a considerable |     | effort | by EUMETSAT |     |               |     |                                       |     |     |     |     |
| onthereprocessingofalargenumberofsatellitedatasets   |          |     |                |     |        |             |     | 6310          |     |                                       |     |     |     |     |
|                                                      |          |     |                |     |        |             |     | SalehAbdalla  |     | https://orcid.org/0000-0003-4469-7949 |     |     |     |     |
forusageinfuturereanalysis.Supportforclimatereanal-
ysis regarding satellite data rescue has been initiated, as XavierAbellan https://orcid.org/0000-0002-1999-1823
isthedevelopmentandmaintenanceofquality-controlled GianpaoloBalsamo https://orcid.org/0000-0002-1745-
|        |           |            |     |     |       |           | insitu | 3634 |     |     |     |     |     |     |
| ------ | --------- | ---------- | --- | --- | ----- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- |
| global | databases | containing |     | all | known | digitised |        |      |     |     |     |     |     |     |
upper-airweatherobservations.Thesewillcontainmeta- PeterBechtold https://orcid.org/0000-0002-1967-3382
|          |             |     |        |     |         |         |         | GionataBiavati |     | https://orcid.org/0000-0002-1675-6967 |     |     |     |     |
| -------- | ----------- | --- | ------ | --- | ------- | ------- | ------- | -------------- | --- | ------------------------------------- | --- | --- | --- | --- |
| data and | information |     | needed | for | DA such | as bias | adjust- |                |     |                                       |     |     |     |     |
ments and uncertainty estimates. In addition, a set of JeanBidlot https://orcid.org/0000-0001-7423-5118
servicestoimproveaccesstoavailableinsituinstrumental GiovannaDeChiara https://orcid.org/0000-0002-4540-
| datarecordsanddatastreamsfromobservingnetworksis |     |     |     |     |     |     |     | 0687 |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
inplace,asneededformonitoringclimatechangeandto DickDee https://orcid.org/0000-0002-8321-9125
supportclimatescience. MichailDiamantakis https://orcid.org/0000-0003-
| All | these | developments |     | and | data | will | feed into | 2279-9717 |     |     |     |     |     |     |
| --- | ----- | ------------ | --- | --- | ---- | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- |
the next generation of global reanalysis (ERA6), which JohannesFlemming https://orcid.org/0000-0003-4880-
| is to be | based | on  | a coupled |     | atmosphere–ocean |     | sys- | 5329 |     |     |     |     |     |     |
| -------- | ----- | --- | --------- | --- | ---------------- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
tem. It is foreseen that, until completion of this new RichardForbes https://orcid.org/0000-0002-3596-8287
full-observing-system reanalysis, ERA5 will be updated ManuelFuentes https://orcid.org/0000-0003-1544-9612
intothemid-2020s.
|     |     |     |     |     |     |     |     | LeoHaimberger |                                       | https://orcid.org/0000-0002-0379-6353 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------- | ------------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | SeanHealy     | https://orcid.org/0000-0003-4810-9593 |                                       |     |     |     |     |
ACKNOWLEDGMENTS RobinJ.Hogan https://orcid.org/0000-0002-3180-5157
| Reanalysis | touches |             | on a   | large | number      | of activities | at    |                |     |                                   |     |     |     |     |
| ---------- | ------- | ----------- | ------ | ----- | ----------- | ------------- | ----- | -------------- | --- | --------------------------------- | --- | --- | --- | --- |
|            |         |             |        |       |             |               |       | MartaJanisková |     | https://orcid.org/0000-0003-2644- |     |     |     |     |
| ECMWF      | and     | its success | relies | on    | the efforts | from          | many, |                |     |                                   |     |     |     |     |
8068

 1477870x, 2020, 730, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803 by University Of Sao Paulo - Brazil, Wiley Online Library on [11/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| HERSBACHetal. |                                       |     |     |     |       |                     |            |                     | 2043  |
| ------------- | ------------------------------------- | --- | --- | --- | ----- | ------------------- | ---------- | ------------------- | ----- |
| SarahKeeley   | https://orcid.org/0000-0002-8046-765X |     |     |     |       |                     |            |                     |       |
|               |                                       |     |     |     | ECMWF | model: verification | from field | site to terrestrial | water |
PatrickLaloyaux https://orcid.org/0000-0003-2808- storage and impact in the Integrated Forecast System. Jour-
|     |     |     |     |     | nal of Hydrometeorology, |     | 10, 623–643. | https://doi.org/10.1175/ |     |
| --- | --- | --- | --- | --- | ------------------------ | --- | ------------ | ------------------------ | --- |
0463
CristinaLupu https://orcid.org/0000-0003-3530-8104 2008JHM1068.1
Bechtold,P.,Köhler,M.,Jung,T.,Doblas-Reyes,F.,Leutbecher,M.,
| PatriciadeRosnay | https://orcid.org/0000-0002-7374- |     |     |     |          |                  |              |           |             |
| ---------------- | --------------------------------- | --- | --- | --- | -------- | ---------------- | ------------ | --------- | ----------- |
|                  |                                   |     |     |     | Rodwell, | M.J., Vitart, F. | and Balsamo, | G. (2008) | Advances in |
3820
simulatingatmosphericvariabilitywiththeECMWFmodel:from
| FrejaVamborg | https://orcid.org/0000-0003-3092-0775 |     |     |     |          |                         |           |         |              |
| ------------ | ------------------------------------- | --- | --- | --- | -------- | ----------------------- | --------- | ------- | ------------ |
|              |                                       |     |     |     | synoptic | to decadal time-scales. | Quarterly | Journal | of the Royal |
SebastienVillaume https://orcid.org/0000-0002-3041- MeteorologicalSociety,134,1337–1351.
Bechtold,P.,Semane,N.,Lopez,P.,Chaboureau,J.-P.,Beljaars,A.
076X
andBormann,N.(2014)Representingequilibriumandnonequi-
| Jean-NoëlThépaut | https://orcid.org/0000-0003-3214- |     |     |     |                    |                |         |                   |     |
| ---------------- | --------------------------------- | --- | --- | --- | ------------------ | -------------- | ------- | ----------------- | --- |
|                  |                                   |     |     |     | librium convection | in large-scale | models. | JournaloftheAtmo- |     |
5266
sphericSciences,71(2),734–753.
Becker,A.,Finger,P.,Meyer-Christoffer,A.,Rudolf,B.,Schamm,K.,
|     |     |     |     |     | Schneider, | U. and Ziese, | M. (2013) | A description of | the global |
| --- | --- | --- | --- | --- | ---------- | ------------- | --------- | ---------------- | ---------- |
REFERENCES land-surfaceprecipitationdataproductsoftheGlobalPrecipita-
Adler, R.F., Huffman, G.J., Chang, A., Ferraro, R., Xie, P.-P., tionClimatologyCentrewithsampleapplicationsincludingcen-
Janowiak,J.,Rudolf,B.,Schneider,U.,Curtis,S.,Bolvin,D.,Gru- tennial(trend)analysisfrom1901–present.EarthSystemScience
| ber,A.,Susskind,J.,Arkin,P.andNelkin,E.(2003)Theversion-2 |     |     |     |     | Data,5(1),71–99. |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
globalprecipitationclimatologyproject(GPCP)monthlyprecipi- Belmonte Rivas, M. and Stoffelen, A. (2019) Characterizing
ERA-InterimandERA5surfacewindbiasesusingASCAT.Ocean
tationanalysis(1979–present).JournalofHydrometeorology,4(6),
1147–1167 Science,15(3),831–852.https://doi.org/10.5194/os-15-831-2019
Ahlgrimm,M.andForbes,R.(2014)Improvingtherepresentation Bengtsson,L.,Kanamitsu,M.,Kållberg,P.W.andUppala,S.M.(1982)
oflowcloudsanddrizzleintheECMWFmodelbasedonARM FGGE4-dimensionaldataassimilationatECMWF.Bulletinofthe
observationsfromtheAzores.MonthlyWeatherReview,142(2), AmericanMeteorologicalSociety,63,29–43.
668–685. Berrisford, P., Kållberg, P., Kobayashi, S., Dee, D.P., Uppala, S.M.,
Albergel, C., Balsamo, G., de Rosnay, P., Muñoz Sabater, J. and Simmons,A.J.,Poli,P.andSato,H.(2011)Atmosphericconser-
Boussetta, S. (2012) A bare ground evaporation revision in the vationpropertiesinERA-Interim.QuarterlyJournaloftheRoyal
ECMWF land-surface scheme: evaluation of its impact using MeteorologicalSociety,137,1381–1399.
groundsoilmoistureandsatellitemicrowavedata.Hydrologyand Bidlot,J.-R. (2012). Presentstatusofwave forecastingatECMWF,
Earth System Sciences, pp.25–27inWorkshoponOceanWaves,ECMWF,Reading,UK.
16, 3607–3620. https://doi.org/10.5194/
hess-16-3607-2012 Blunden, J. and Arndt, D.S. (2019) State of the Climate in 2018.
Allan,R.P.,Liu,C.,Loeb,N.G.,Palmer,M.D.,Roberts,M.,Smith,D. BulletinoftheAmericanMeteorologicalSociety,100(9),S1–S305.
andVidale,P.-L.(2014)Changesinglobalnetradiativeimbal- https://doi.org/10.1175/2019BAMSStateoftheClimate.1
ance1985–2012.GeophysicalResearchLetters,41(15),5588–5597. Bojinski,S.,Verstraete,M.,Peterson,T.C.,Richter,C.,Simmons,A.
https://doi.org/10.1002/2014GL060962 andZemp,M.(2014)Theconceptofessentialclimatevariables
Anderson, E. and Järvinen, H. (1999) Variational quality con- insupportofclimateresearch,applications,andpolicy.Bulletin
oftheAmericanMeteorologicalSociety,95(9),1431–1443.
| trol. Quarterly | Journal of | the Royal Meteorological | Society, | 125, |     |     |     |     |     |
| --------------- | ---------- | ------------------------ | -------- | ---- | --- | --- | --- | --- | --- |
697–722. Bonavita,M.,Hólm,E.V.,Isaksen,L.andFisher,M.(2016)Theevo-
Auligné,T.,McNally,A.P.andDee,D.P.(2007)Adaptivebiascor- lutionoftheECMWFhybriddataassimilationsystem.Quarterly
rectionforsatellitedatainanumericalweatherpredictionsys- JournaloftheRoyalMeteorologicalSociety,142,287–303.
tem. QuarterlyJournaloftheRoyalMeteorologicalSociety, 133, Bormann, N., Fouilloux, A. and Bell, W. (2012). Evaluation and
631–642. assimilation of ATMS data in the ECMWF system. Technical
Balmaseda, M.A., Mogensen, K. and Weaver, A.T. (2013) Evalua- Memorandum689,ECMWF,Reading,UK.
Bormann,N.,Bonavita,M.,Dragani,R.,Eresmaa,R.,Matricardi,M.
tionoftheECMWFoceanreanalysissystemORAS4.Quarterly
JournaloftheRoyalMeteorologicalSociety,139,1132–1161. andMcNally,A.P.(2015).EnhancingtheimpactofIASIobser-
Balmaseda,M.A.,Vidard,A.andAnderson,D.(2008)TheECMWF vationsthroughanupdatedobservationerrorcovariancematrix.
OceanAnalysisSystem:ORA-S3.MonthlyWeatherReview,136, TechnicalMemorandum756,ECMWF,Reading,UK.
3018–3034. Bormann,N.,Collard,A.D.andBauer,P.(2009).Estimatesofspa-
Balsamo,G.,Albergel,C.,Beljaars,A.,Boussetta,S.,Brun,E.,Cloke, tial and interchannel observation error characteristics for cur-
H.,Dee,D.P.,Dutra,E.,MuñozSabater,J.,Pappenberger,F.,de rentsounderradiancesforNWP.TechnicalMemorandum600,
Rosnay,P.,Stockdale,T.andVitart,F.(2015)ERA-Interim/Land: ECMWF,Reading.
a global land surface reanalysis data set. Hydrology and Earth Bormann, N., Lupu, C., Geer, A.J., Lawrence, H., Weston, P.
SystemSciences,19(1),389–407. and English, S.J. (2017). Assessment of the forecast impact
|          |                         |                |                |     | of suface-sensitive | microwave | radiances | over land | and sea-ice. |
| -------- | ----------------------- | -------------- | -------------- | --- | ------------------- | --------- | --------- | --------- | ------------ |
| Balsamo, | G., Salgado, R., Dutra, | E., Boussetta, | S., Stockdale, | T.  |                     |           |           |           |              |
andPotes,M.(2012)Onthecontributionoflakesinpredicting TechnicalMemorandum804,ECMWF,Reading,UK.
near-surfacetemperatureinaglobalweatherforecastingmodel. Boussetta,S.,Balsamo,G.,Beljaars,A.,Kral,T.andJarlan,L.(2013)
TellusA,64(1).https://doi.org/10.3402/tellusa.v64i0.15829 Impactofasatellite-derivedleafareaindexmonthlyclimatology
Balsamo, G., Viterbo, P., Beljaars, A., van den Hurk, B., Hirschi, in a global numerical weather prediction model. International
M., Betts, A. and Scipal, K. (2009) A revised hydrology for the JournalofRemoteSensing,34(9–10),3520–3542.

2044 HERSBACHetal.
Burrows,C.(2018).Assimilationofradianceobservationsfromgeo- Tegtmeier,S.,Wang,T.,Wargan,K.andWright,J.S.(2017)Assess-
stationarysatellites:firstyearreport.EUMETSAT/ECMWFFel- ment of upper tropospheric and stratospheric water vapor and
lowshipProgrammeResearchReport47,ECMWF,Reading,UK. ozone in reanalyses as part of S-RIP. Atmospheric Chemistry
Cardinali,C.,Pezzulli,S.andAnderson,E.(2004)Influence-matrix and Physics, 17(20), 12743–12778. https://doi.org/10.5194/acp-
diagnosticofadataassimilationsystem.QuarterlyJournalofthe 17-12743-2017
RoyalMeteorologicalSociety,130,2767–2786. de Rosnay, P., Balsamo, G., Albergel, C., Muñoz Sabater, J. and
Cariolle, D. and Déqué, M. (1986) Southern Hemisphere Isaksen, L. (2014) Initialisation of land surface variables for
medium-scalewavesandtotalozonedisturbancesinaspectral numerical weather prediction. Surveys in Geophysics, 35(3),
generalcirculation model.JournalofGeophysicalResearch,91, 607–621.https://doi.org/10.1007/s10712-012-9207-x
10825–10846. deRosnay,P.,Drusch,M.,Vasiljevic,D.,Balsamo,G.,Albergel,C.
Cariolle,D.andTeyssèdre,H.(2007)Arevisedlinearozonephoto- andIsaksen,L.(2013)AsimplifiedExtendedKalmanFilterfor
chemistryparameterizationforuseintransportandgeneralcir- theglobaloperationalsoilmoistureanalysisatECMWF.Quar-
culationmodels:multi-annualsimulations.AtmosphericChem- terlyJournaloftheRoyalMeteorologicalSociety,139,1199–1213.
istryandPhysicsDiscussion,7,1655–1697. https://doi.org/10.1002/qj.2023
Chen,K.,English,S.J.,Bormann,N.andZhu,J.(2014).Assessment Dee,D.P.(2005)Biasanddataassimilation.QuarterlyJournalofthe
of FY-3A and FY-3B MWHS observations. ECMWF Technical RoyalMeteorologicalSociety,131,3323–3343.
Memorandum734,ECMWF,Reading. Dee, D.P. and Uppala, S.M. (2009) Variational bias correction of
Collard,A.D.andMcNally,A.P.(2009)TheassimilationofInfrared satelliteradiancedataintheERA-Interimreanalysis.Quarterly
Atmospheric Sounding Interferometer radiances at ECMWF. JournaloftheRoyalMeteorologicalSociety,135,1830–1841.
Quarterly Journal of the Royal Meteorological Society, 135, Dee, D.P., Uppala, S.M., Simmons, A.J., Berrisford, P., Poli, P.,
1044–1058.https://doi.org/10.1002/qj.410 Kobayashi,S.,Andrae,U.,Balmaseda,M.A.,Balsamo,G.,Bauer,
Compo, G.P., Whitaker, J.S. and Sardeshmukh, P.D. (2006) Fea- P., Bechtold, P., Beljaars, A.C.M., van de Berg, L., Bidlot, J.,
sibility of a 100-year reanalysis using only surface pressure Bormann, N., Delsol, C., Dragani, R., Fuentes, M., Geer, A.J.,
data. Bulletin of the American Meteorological Society, 87(2), Haimberger, L., Healy, S.B., Hersbach, H., Hólm, E.V., Isak-
175–190. sen,L.,Kållberg,P.,Köhler,M.,Matricardi,M.,McNally,A.P.,
Compo,G.P.,Whitaker,J.S.,Sardeshmukh,P.D.,Matsui,N.,Allan, Monge-Sanz, B.M., Morcrette, J.-J., Park, B.-K., Peubey, C., de
R.J.,Yin,X.,Gleason,B.E.,Vose,R.S.,Rutledge,G.,Bessemoulin, Rosnay,P.,Tavolato,C.,Thépaut,J.-N.andVitart,F.(2011)The
P., Brönnimann, S., Brunet, M., Crouthamel, R.I., Grant, A.N., ERA-Interim reanalysis: configuration and performance of the
Groisman,P.Y.,Jones,P.D.,Kruk,M.C.,Kruger,A.C.,Marshall, dataassimilationsystem.QuarterlyJournaloftheRoyalMeteoro-
G.J.,Maugeri,M.,Mok,H.Y.,Nordli,Ø.,Ross,T.F.,Trigo,R.M., logicalSociety,137,553–597.
Wang, X.L., Woodruff, S.D. and Worley, S.J. (2011) The Twen- Diamantakis, M. (2014) Improving ECMWF forecasts of sudden
tiethCenturyReanalysisProject.QuarterlyJournaloftheRoyal stratosphericwarmings.ECMWFNewsletter,141,30–36.
MeteorologicalSociety,137,1–28. Diamantakis, M. and Magnusson, L. (2016) Sensitivity of the
Copernicus (2019). Ozone monthly gridded data from 1970 to ECMWF model to semi-Lagrangian departure point iterations.
present, Level 4, version 0021. Available at https://cds.climate. MonthlyWeatherReview,144(9),3233–3250.
copernicus.eu/portfolio/dataset/satellite-ozone; accessed 11 Donlon,C.J.,Martin,M.,Stark,J.,Roberts-Jones,J.,Fiedler,E.and
April2020. Wimmer,W.(2012)Theoperationalseasurfacetemperatureand
Courtier,P.,Thépaut,J.-N.andHollingsworth,A.(1994)Astrategy seaiceanalysis(OSTIA)system.RemoteSensingofEnvironment,
foroperationalimplementationof4D-Var,usinganincremental 116,140–158.
approach.QuarterlyJournaloftheRoyalMeteorologicalSociety, Dragani,R.(2009).Variationalbiascorrectionofsatelliteozonedata.
120,1367–1388. TechnicalReportR43.8/RD/0934,ECMWF,Reading,UK.
Cowtan, K. and Way, R.G. (2014) Coverage bias in the Had- Dragani,R.(2016)AcomparativeanalysisofUVnadir-backscatter
CRUT4temperatureseriesanditsimpactonrecenttemperature andinfraredlimb-emissionozonedataassimilation.Atmospheric
trends.QuarterlyJournaloftheRoyalMeteorologicalSociety,140, ChemistryandPhysics,16(13),8539–8557.
1935–1944. Dragani, R. and McNally, A.P. (2013) Operational assimilation of
Cram,T.A.,Compo,G.P.,Yin,X.,Allan,R.J.,McColl,C.,Vose,R.S., ozone-sensitiveinfraredradiancesatECMWF.QuarterlyJournal
Whitaker, J.S., Matsui, N., Ashcroft, L., Auchmann, R., Besse- oftheRoyalMeteorologicalSociety,139,2068–2080.
moulin,P.,Brandsma,T.,Brohan,P.,Brunet,M.,Comeaux,J., Durack,P.J.andWijffels,S.E.(2010)Fifty-yeartrendsinglobalocean
Crouthamel,R.,GleasonJr,B.E.,Groisman,P.Y.,Hersbach,H., salinitiesandtheirrelationshiptobroad-scalewarming.Journal
Jones, P.D., Jónsson, T., Jourdain, S., Kelly, G.A., Knapp, K.R., ofClimate,23(16),4342–4362.
Kruger,A.,Kubota,H.,Lentini,G.,Lorrey,A.,Lott,N.,Lubker, Dutra, E., Balsamo, G., Viterbo, P., Miranda, P.M.A., Beljaars, A.,
S.J.,Luterbacher,J.,Marshall,G.J.,Maugeri,M.,Mock,C.J.,Mok, Schär,C.andElder,K.(2010)Animprovedsnowschemeforthe
H.Y.,Nordli,Ø.,Rodwell,M.J.,Ross,T.F.,Schuster,D.,Srnec,L., ECMWFlandsurfacemodel:descriptionandofflinevalidation.
Valente,M.A.,Vizi,Z.,Wang,X.L.,Westcott,N.,Woollen,J.S.and JournalofHydrometeorology,11(4),899–916.https://doi.org/10.
Worley,S.J.(2015)Theinternationalsurfacepressuredatabank 1175/2010JHM1249.1
version2.GeoscienceDataJournal,2(1),31–46.https://doi.org/ Dutra, E., Stepanenko, V., Balsamo, G., Viterbo, P., Miranda, P.,
10.1002/gdj3.25 Mironov,D.andSchär,C.(2009).ImpactoflakesontheECMWF
Davis, S.M., Hegglin, M.I., Fujiwara, M., Dragani, R., Harada, Y., surfacescheme.ECMWFTechnicalMemorandum608,ECMWF,
Kobayashi,C.,Long,C.,Manney,G.L.,Nash,E.R.,Potter,G.L., Reading,UK.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2045
DWD(2000).BewertungderOrkanwetterlageam26.12.1999auskli- Research and Applications, version 2 (MERRA-2). Journal of
matologischerSicht.Availableat:http://www.wetter-extrem.de/ Climate,30(14),5419–5454.
stuerme/lothar/orkan_lothar.pdf;accessed11April2020. Gibson, J.K., Kållberg, P., Uppala, S.M., Hernandez, A., Nomura,
Eastwood,S.,Lavergne,T.andTonboe,R.(2014).AlgorithmThe- A.andSerrano,E.(1999).ECMWFre-analysisprojectreport1,
oretical Basis Document for the OSI SAF global reprocessed ERA-15 description (version2). Technical Report, ECMWF,
seaiceconcentrationproduct,version1.1.EUMETSATSatellite Reading,UK.
ApplicationFacilities,Darmstadt,Germany. Graham,R.M.,Hudson,S.R.andMaturilli,M.(2019)ImprovedPer-
ECMWF R&D (2016). IFS documentation cy41r2. https://www. formance of ERA5 in Arctic Gateway Relative to Four Global
ecmwf.int/en/publications/ifs-documentation;accessed11April Atmospheric Reanalyses. Geophysical Research Letters, 46(11),
2020. 6138–6147.https://doi.org/10.1029/2019GL082781
Eresmaa, R., Letertre-Danczak, J., Lupu, C., Bormann, N. and Haimberger,L.,Tavolato,C.andSperka,S.(2008)Towardelimina-
McNally, A.P. (2017) The assimilation of Cross-track Infrared tionofthewarmbiasinhistoricradiosondetemperaturerecords:
Sounder radiances at ECMWF. Quarterly Journal of the Royal some new results from a comprehensive intercomparison of
MeteorologicalSociety, 143,3177–3188. https://doi.org/10.1002/ upper-airdata.JournalofClimate,21,4587–4606.
qj.3171 Haimberger,L.,Tavolato,C.andSperka,S.(2012)Homogenization
Fennig, K., Schroeder, M. and Hollmann, R. (2017). Funda- oftheglobalradiosondetemperaturedatasetthroughcombined
mental climate data record of microwave imager radiances, comparisonwithreanalysisbackgroundseriesandneighboring
edition 3. Technical Report, Satellite Application Facility on stations.JournalofClimate,25,8108–8131.
Climate Monitoring, EUMETSAT, Darmstadt, Germany, DOI Hansen, J., Ruedy, R., Sato, M. and Lo, K. (2010) Global surface
10.5676/EUM_SAF_CM/FCDR_MWI/V003,(toappearinprint). temperaturechange.ReviewsofGeophysics,48(4)
Fiorino, M. (2004). A multi-decadal daily sea surface temperature Healy,S.B.,Eyre,J.,Hamrud,M.andThépaut,J.-N.(2007)Assimilat-
and sea ice concentration data set for the ERA-40 reanalysis. ingGPSradiooccultationmeasurementswithtwo-dimensional
TechnicalReport12,ECMWF,Reading,UK. bending angle observation operators. Quarterly Journal of the
Fisher,M.(2003).Backgrounderrorcovariancemodelling.pp.45–63 RoyalMeteorologicalSociety,133,1213–1227.https://doi.org/10.
in Seminar on Recent Developments in Data Assimilation for 1002/qj.63
AtmosphereandOcean.ECMWF,Reading,UK. Healy,S.B.(2011)Refractivitycoefficientsusedintheassimilation
Flemming,J.,Benedetti,A.,Inness,A.,Engelen,R.J.,Jones,L.,Hui- ofGPSradiooccultationmeasurements.JournalofGeophysical
jnen,V.,Remy,S.,Parrington,M.,Suttie,M.,Bozzo,A.,Peuch, Research,116.https://doi.org/10.1029/2010JD014013
V.-H.,Akritidis,D.andKatragkou,E.(2017)TheCAMSinterim Hersbach,H.(2010)ComparisonofC-bandscatterometerCMOD5.N
reanalysisofcarbonmonoxide,ozoneandaerosolfor2003–2015. equivalentneutralwindswithECMWF.JournalofAtmospheric
AtmosphericChemistryandPhysics,17(3),1945–1983. andOceanicTechnology,27(4),721–736.
Forbes,R.M.andTompkins,A.M.(2011)Animprovedrepresenta- Hersbach, H. (2019) ECMWF's ERA5 reanalysis extends back to
tionofcloudandprecipitation.ECMWFNewsletter,129,13–18. 1979.ECMWFNewsletter,158,1
Forbes, R.M. and Ahlgrimm, M. (2014) On the representation of Hersbach,H.,Peubey,C.,Simmons,A.J.,Berrisford,P.,Poli,P.and
high-latitudeboundary-layermixed-phasecloudintheECMWF Dee, D.P. (2015) ERA-20CM: a twentieth-century atmospheric
globalmodel.MonthlyWeatherReview,142(9),3425–3445. model ensemble. Quarterly Journal of the Royal Meteorological
Forbes, R.M., Tompkins, A.M. and Untch, A. (2011). A new prog- Society,141,2350–2375.
nosticbulkmicrophysicsschemefortheIFS.ECMWFTechnical Hersbach,H.,Brönnimann,S.,Haimberger,L.,Mayer,M.,Villiger,
Memorandum649,ECMWF,Reading,UK. L.,Comeaux,J.,Simmons,A.J.,Dee,D.P.,Jourdain,S.,Peubey,
Gauthier, P. and Thépaut, J.-N. (2001) Impact of the digital filter C.,Poli,P.,Rayner,N.A.,Sterin,A.M.,Stickler,A.,Valente,M.A.
as a weak constraint in the preoperational 4D-VAR assimila- andWorley,S.J.(2017)Thepotentialvalueofearly(1939–1967)
tion system of Météo-France. Monthly Weather Review, 129(8), upper-airdatainatmosphericclimatereanalysis.QuarterlyJour-
2089–2102. naloftheRoyalMeteorologicalSociety,143,1197–1210.
Geer, A.J., Baordo, F., Bormann, N., English, S.J., Kazumori, M., Hersbach,H.,deRosnay,P.,Bell,B.,Schepers,D.,Simmons,A.J.,
Lawrence,H.,Lean,P.,Lonitz,K.andLupu,C.(2017)Thegrow- Soci,C.,Abdalla,S.,Balmaseda,M.A.,Balsamo,G.,Bechtold,P.,
ingimpactofsatelliteobservationssensitivetohumidity,cloud Berrisford,P.,Bidlot,J.,deBoisséson,E.,Bonavita,M.,Browne,
andprecipitation.QuarterlyJournaloftheRoyalMeteorological P.,Buizza,R.,Dahlgren,P.,Dee,D.P.,Dragani,R.,Diamantaki,
Society,143,3189–3206.https://doi.org/10.1002/qj.3172 M.,Flemming,J.,Forbes,R.,Geer,A.J.,Haiden,T.,Hólm,E.V.,
Geer, A.J., Bauer, P. and Bormann, N. (2010) Solar biases in Haimberger,L.,Hogan,R.,Horányi,A.,Janisková,M.,Laloyaux,
microwave imager observations assimilated at ECMWF. P.,Lopez,P.,MuñozSabater,J.,Peubey,C.,Radu,R.,Richard-
IEEE Transactions on Geoscience and Remote Sensing, 48(6), son,D.,Thépaut,J.-N.,Vitart,F.,Yang,X.,Zsótér,E.andZuo,H.
2660–2669.June (2018).Operationalglobalreanalysis:progress,futuredirections
Gelaro,R.,McCarty,W.,Suárez,M.J.,Todling,R.,Molod,A.,Takacs, and synergies with NWP. ERA Report Series no.27, ECMWF,
L.,Randles,C.A.,Darmenov,A.,Bosilovich,M.G.,Reichle,R., Reading,UK.
Wargan,K.,Coy,L.,Cullather,R.,Draper,C.,Akella,S.,Buchard, Hewson, T.D. and Neu, U. (2015) Cyclones, windstorms and the
V., Conaty, A., da Silva, A.M., Gu, W., Kim, G.-K., Koster, R., IMILASTproject.TellusA,67(1),27128
Lucchesi, R., Merkova, D., Nielsen, J.E., Partyka, G., Pawson, Hirahara,S.,Balmaseda,M.A.,deBoisseson,E.andHersbach,H.
S., Putman, W., Rienecker, M., Schubert, S.D., Sienkiewicz, M. (2016). Sea surface temperature and sea ice concentration for
andZhao,B.(2017)TheModern-EraRetrospectiveanalysisfor ERA5.ERAReportSeriesno.26,ECMWF,Reading,UK.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

2046 HERSBACHetal.
Hirons,L.,Inness,P.,Vitart,F.andBechtold,P.(2013)Understand- Janssen,P.A.E.M.andBidlot,J.(2009).Ontheextensionofthefreak
ingadvancesinthesimulationofintraseasonalvariabilityinthe wavewarningsystemanditsverification.TechicalMemorandum
ECMWF model. Part II: the application of process-based diag- 588,ECMWF,Reading,UK.
nostics.QuarterlyJournaloftheRoyalMeteorologicalSociety,139, Kalverla,P.C.,Duncan,J.B.J.r.,Steeneveld,G.-J.andHoltslag,A.A.M.
1427–1444. (2019) Low-level jets over the North Sea based on ERA5 and
Hogan,R.J.andBozzo,A.(2015)Mitigatingerrorsinsurfacetem- observations:togethertheydobetter.WindEnergyScience,4(2),
peratureforecastsusingapproximateradiationupdates.Journal 193–209.
ofAdvancesinModelingEarthSystems,7,836–853. Karl, T.R., Arguez, A., Huang, B., Lawrimore, J.H., McMahon,
Hogan,R.J.andHirahara,S.(2016)Effectofsolarzenithanglespec- J.R., Menne, M.J., Peterson, T.C., Vose, R.S. and Zhang, H.-M.
ificationinmodelsonmeanshortwavefluxesandstratospheric (2015)Possibleartifactsofdatabiasesintherecentglobalsur-
temperatures.GeophysicalResearchLetters,43,482–488. facewarminghiatus.Science,348,1469–1472.https://doi.org/10.
Horányi,A.(2017)Someaspectsontheuseandimpactofobserva- 1126/science.aaa5632
tionsintheERA5CopernicusClimateChangeServicereanalysis. Kazumori,M.,Geer,A.J.andEnglish,S.J.(2016)Effectsofall-sky
Idojaras,121(4),329–344. assimilation of GCOM-W/AMSR2 radiances in the ECMWF
Huffman, G.J., Adler, R.F., Bolvin, D.T. and Nelkin, E.J. (2010). numerical weather prediction system. Quarterly Journal of the
TheTRMMMulti-satellitePrecipitationAnalysis(TMPA),Chap- Royal Meteorological Society, 142, 721–737. https://doi.org/10.
ter 1 in Satellite Rainfall Applications for Surface Hydrology. 1002/qj.2669
Gebremichael,M.,Hossain,F.(eds)Springer,Berlin. Kobayashi, S., Matricardi, M., Dee, D.P. and Uppala, S.M. (2009)
Iacono,M.J.,Delamere,J.S.,Mlawer,E.J.,Shephard,M.W.,Clough, Towardaconsistentreanalysisoftheupperstratospherebasedon
S.A. and Collins, W.D. (2008) Radiative forcing by long-lived radiancemeasurementsfromSSUandAMSU-A.QuarterlyJour-
greenhousegases:calculationswiththeAERradiativetransfer naloftheRoyalMeteorologicalSociety,135,2086–2099.https://
models.JournalofGeophysicalResearch:Atmospheres,113(D13). doi.org/10.1002/qj.514
https://doi.org/10.1029/2008JD009944 Kobayashi,S.,Ota,Y.,Harada,Y.,Ebita,A.,Moriya,M.,Onoda,H.,
Ide, K., Courtier, P., Ghil, M. and Lorenc, A.C. (1997) Uni- Onogi,K.,Kamahori,H.,Kobayashi,C.,Endo,H.,Miyaoka,K.
fied notation for data assimilation: operational, sequential and andTakahashi,K.(2015)TheJRA-55reanalysis:generalspeci-
variational. Journal of the Meteorological Society of Japan, 39, ficationsandbasiccharacteristics.JournaloftheMeteorological
2038–2052. Society of Japan. Series II, 93(1), 5–48. https://doi.org/10.2151/
Ingleby,B.,Isaksen,L.,Kral,T.,Haiden,T.andDahoui,M.(2018) jmsj.2015-001
Improved use of atmospheric insitu data. ECMWF Newsletter, Köopken, C., Thépaut, J.-N. and Kelly, G.A. (2003). Assimilation
155,20–25. of Geostationary WV Radiances from GOES and Meteosat
Ingleby,B.,Pauley,P.,Kats,A.,Ator,J.,Keyser,D.,Doerenbecher, at ECMWF. EUMETSAT/ECMWF Fellowship Programme
A., Fucile, E., Hasegawa, J., Toyoda, E., Kleinert, T., Qu, W., ResearchReport14,ECMWF,Reading,UK.
St.James,J.,Tennant,W.andWeedon,R.(2016)Progresstoward Krzeminski,B.,Bormann,N.,Kelly,G.A.,McNally,A.P.andBauer,
high-resolution, real-time radiosonde reports. Bulletin of the P. (2009). Revision of the HIRS cloud detection at ECMWF.
AmericanMeteorologicalSociety,97(11),2149–2161. EUMETSAT/ECMWF Fellowship Programme Research Report
Inness,A.,Ades,M.,Agustí-Panareda,A.,Barré,J.,Benedictow,A., 19,ECMWF,Reading,UK.
Blechschmidt, A.-M., Dominguez, J.J., Engelen, R., Eskes, H., Laloyaux,P.,deBoisseson,E.,Balmaseda,M.A.,Bidlot,J.-R.,Broen-
Flemming,J.,Huijnen,V.,Jones,L.,Kipling,Z.,Massart,S.,Par- nimann, S., Buizza, R., Dalhgren, P., Dee, D.P., Haimberger,
rington, M., Peuch, V.-H., Razinger, M., Remy, S., Schulz, M. L., Hersbach, H., Kosaka, Y., Martin, M., Poli, P., Rayner, N.,
andSuttie,M.(2019)TheCAMSreanalysisofatmosphericcom- Rustemeier, E. and Schepers, D. (2018) CERA-20C: a coupled
position.AtmosphericChemistryandPhysics,19(6),3515–3556. reanalysisofthetwentiethcentury.JournalofAdvancesinMod-
https://doi.org/10.5194/acp-19-3515-2019 eling Earth Systems, 10(5), 1172–1195. https://doi.org/10.1029/
Inness,A.,Baier,F.,Benedetti,A.,Bouarar,I.,Chabrillat,S.,Clark, 2018MS001273
H.,Clerbaux,C.,Coheur,P.,Engelen,R.,Errera,Q.,Flemming, Laloyaux,P.,Bonavita,M.,Dahoui,M.,Farnan,J.,Healy,S.B.,Hölm,
J.,George,M.,Granier,C.,Hadji-Lazaro,J.,Huijnen,V.,Hurt- E.V.andLang,S.T.K.(2020)Towardsanunbiasedstratospheric
mans,D.,Jones,L.,Kaiser,J.W.,Kapsomenakis,J.,Lefever,K., analysis. Quarterly Journal of the Royal Meteorological Society.
Leitão,J.,Razinger,M.,Richter,A.,Schultz,M.G.,Simmons,A.J., https://doi.org/10.1002/qj.3798
Suttie,M.,Stein,O.,Thépaut,J.-N.,Thouret,V.,Vrekoussis,M. Lawrence,H.,Bormann,N.,Geer,A.J.,Lu,Q.andEnglish,S.J.(2018)
andZerefos,C.(2013)TheMACCreanalysis:an8-yeardataset EvaluationandassimilationoftheMicrowaveSounderMWHS-2
ofatmosphericcomposition.AtmosphericChemistryandPhysics, onboardFY-3CintheECMWFnumericalweatherpredictionsys-
13,4073–4109. tem. IEEETransactionsonGeoscience andRemoteSensing, 56,
Isaksen,L.,Bonavita,M.,Buizza,R.,Fisher,M.,Haseler,J.,Leut- 3333–3349.
becher,M.andRaynaud,L.(2010).EnsembleofDataAssimila- Lean,J.,Rottman,G.,Harder,J.andKopp,G.(2005)Sorcecontribu-
tionsatECMWF.TechnicalMemorandum636,ECMWF,Read- tionstonewunderstandingofglobalchangeandsolarvariability.
ing,UK. SolarPhysics,230,27–53.
Janisková,M.andLopez,P.(2013).Linearizedphysicsfordataassim- Letertre-Danczak, J. (2016). Monitoring and operational assim-
ilationatECMWF,pp.251–286inDataAssimilationforAtmo- ilation of Himawari-9 clear-sky geostationary radiances.
spheric,OceanicandHydrologicApplications,Vol.II.Park,S.K., Research Department Memorandum RD16-029, ECMWF,
Xu,L.(eds),Springer,Berlin. Reading,UK.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2047
Leutbecher, M., Lock, S.-J., Ollinaho, P., Lang, S.T., Balsamo, G., overview.JournalofGeophysicalResearch:Atmospheres,118(14),
Bechtold,P.,Bonavita,M.,Christensen,H.M.,Diamantakis,M., 8032–8039.https://doi.org/10.1002/jgrd.50597
Dutra, E., English, S., Fisher, M., Forbes, R.M., Goddard, J., Merchant, C.J., Embury, O., Roberts-Jones, J., Fiedler, E., Bulgin,
Haiden, T., Hogan, R.J., Juricke, S., Lawrence, H., MacLeod, C.E., Corlett, G.K., Good, S., McLaren, A., Rayner, N.A.,
D., Magnusson, L., Malardel, S., Massart, S., Sandu, I., Smo- Morak-Bozzo,S.andDonlon,C.(2014)Seasurfacetemperature
larkiewicz, P.K., Subramanian, A., Vitart, F., Wedi, N. and datasetsforclimateapplicationsfromPhase1oftheEuropean
Weisheimer,A.(2017)Stochasticrepresentationsofmodeluncer- SpaceAgencyClimateChangeInitiative(SSTCCI).Geoscience
tainties at ECMWF: state of the art and future vision. Quar- DataJournal,1(2),179–191.https://doi.org/10.1002/gdj3.20
terlyJournaloftheRoyalMeteorologicalSociety,143,2315–2339. Mironov, D., Heise, E., Kourzeneva, E., Ritter, B., Schneider,
https://doi.org/10.1002/qj.3094 N. and Terzhevik, A. (2010) Implementation of the lake
Long, C., Fujiwara, M., Davis, S.M., Mitchell, D.M. and Wright, parameterisationschemeFLakeintothenumericalweatherpre-
C.J.(2017)Climatologyandinterannualvariabilityofdynamic dictionmodelCOSMO.BorealEnvironmentResearch,15(2)
variablesinmultiplereanalysesevaluatedbytheSPARCReanal- Molteni, F., Stockdale, T., Balmaseda, M.A., Balsamo, G., Buizza,
ysisIntercomparisonProject(S-RIP).AtmosphericChemistryand R.,Ferranti,L.,Magnusson,L.,Mogensen,K.,Palmer,T.N.and
Physics,17(23) Vitart, F. (2011). The new ECMWF Seasonal Forecast System
Lopez, P. (2011) Direct 4D-Var assimilation of NCEP Stage IV (System4).TechnicalMemorandum656,ECMWF,Reading,UK.
radarandgaugeprecipitationdataatECMWF.MonthlyWeather Morcrette, J.-J. (1991) Radiation and cloud radiative properties in
Review,139,2098–2116. theEuropeanCentreforMediumRangeWeatherForecastsfore-
Lupu, C. and Geer, A.J. (2015). Operational Implementation of casting system. Journal of Geophysical Research: Atmospheres,
RTTOV-11 in the IFS. Technical Memorandum 636, ECMWF, 96(D5),9121–9132.
Reading,UK. Morcrette, J.-J., Barker, H.W., Cole, J.N.S., Iacono, M.J. and Pin-
Lupu, C. and McNally, A.P. (2012). Assimilation of cloud-affected cus, R. (2008) Impact of a new radiation package, McRad, in
radiances from Meteosat-9 at ECMWF. EUMETSAT/ECMWF the ECMWF Integrated Forecasting System. Monthly Weather
FellowshipProgrammeResearchReport25,ECMWF,Reading, Review,136,4773–4798.
UK. Morice,C.P.,Kennedy,J.J.,Rayner,N.A.andJones,P.D.(2012)Quan-
Malardel,S.andRicard,D.(2015)Analternativecell-averageddepar- tifyinguncertaintiesinglobalandregionaltemperaturechange
turepointreconstruction forpointwisesemi-Lagrangiantrans- using an ensemble of observational estimates: the HadCRUT4
portschemes.QuarterlyJournaloftheRoyalMeteorologicalSoci- dataset.JournalofGeophysicalResearch:Atmospheres,117(D8).
ety,141,2114–2126. https://doi.org/10.1029/2011JD017187
Manrique-Suñén, A., Nordbo, A., Balsamo, G., Beljaars, A. and Muñoz-Sabater,J.(2019)FirstERA5-Landdatasettobereleasedthis
Mammarella,I.(2013)Representinglandsurfaceheterogeneity: spring.ECMWFNewsletter,1598–9.
offlineanalysisofthetilingmethod.JournalofHydrometeorology, Munro,R.,Kopken,C.,Kelly,G.A.,Thépaut,J.-N.andSaunders,R.
14(3),850–867.https://doi.org/10.1175/JHM-D-12-0108.1 (2004)Characterizationoftheimpactofgeostationaryclear-sky
Maycock,A.C.,Randel,W.J.,Steiner,A.K.,Karpechko,A.Y.,Christy, radiancesonwindanalysesina4D-Varcontext.QuarterlyJournal
J., Saunders, R., Thompson, D.W.J., Zou, C.-Z., Chrysanthou, oftheRoyalMeteorologicalSociety,130,2293–2313.
A.,Abraham,N.L.,Akiyoshi,H.,Archibald,A.T.,Butchart,N., Nash,J.andSaunders,R.(2015)AreviewofStratosphericSound-
Chipperfield, M., Dameris, M., Deushi, M., Dhomse, S., Gen- ing Unit radiance observations for climate trends and reanaly-
ova, G.D., Jackel, P., Kinnison, D.E., Kirner, O., Ladstdter, F., ses. Quarterly Journal of the Royal Meteorological Society, 141,
Michou,M.,Morgenstern,O.,O'Connor,F.,Oman,L.,Pitari,G., 2103–2113.
Plummer,D.A.,Revell,L.E.,Rozanov,E.,Stenke,A.,Visioni,D., NOAA(2006).2-MinuteGriddedGlobalReliefData(ETOPO2)v2.
Yamashita,Y.andZeng,G.(2018)Revisitingthemysteryofrecent NationalGeophysicalDataCenter,NOAA,Asheville,NC.
stratospheric temperature trends. Geophysical Research Letters, Olauson, J.(2018) ERA5: thenewchampionofwindpower mod-
45(18),9919–9933.https://doi.org/10.1029/2018GL078035 elling?.RenewableEnergy,126,322–331.
Mayer,M.andHaimberger,L.(2012)Polewardatmosphericenergy Orr, A., Bechtold, P., Scinocca, J., Ern, M. and Janisková, M.
transportsandtheirvariabilityasevaluatedfromECMWFreanal- (2010) Improved middle atmosphere climate and forecasts
ysisdata.JournalofClimate,25(2),734–752. in the ECMWF model through a non-orographic gravity
Mayer,M.,Tietsche,S.,Haimberger,L.,Tsubouchi,T.,Mayer,J.and wave drag parameterization. Journal of Climate, 23(22),
Zuo,H.(2019)AnimprovedestimateofthecoupledArcticenergy 5905–5926.
budget.JournalofClimate,32,7915–7934. Penny,S.G.,Akella,S.,Buehner,M.,Chevallier,M.,Counillon,F.,
McNally,A.P.andWatts,P.D.(2003)Aclouddetectionalgorithmfor Draper,C.,Frolov,S.,Fujii,Y.,Karspeck,A.,Kumar,A.,Laloy-
high-spectral-resolutioninfraredsounders.QuarterlyJournalof aux,P.,Mahfouf,J.-F.,Martin,M.,Peña,M.,deRosnay,P.,Subra-
theRoyalMeteorologicalSociety,129,3411–3423.https://doi.org/ manian,A.,Tardif,R.,Wang,Y.andWu,X.(2017).Coupleddata
10.1256/qj.02.208 assimilationforIntegratedEarthSystemAnalysisandPrediction:
McNally, A.P., Watts, P.D., Smith, J.A., Engelen, R., Kelly, G.A., Goals,challenges,andrecommendations.WWRPreport2017-3,
Thpaut,J.-N.andMatricardi,M.(2006)TheassimilationofAIRS WMO,Geneva,Switzerland.
radiancedataatECMWF.QuarterlyJournaloftheRoyalMeteo- Peubey,C.andMcNally,A.P.(2009)Characterizationoftheimpact
rologicalSociety,132,935–957.https://doi.org/10.1256/qj.04.171 ofgeostationaryclear-skyradiancesonwindanalysesina4D-Var
McPeters, R.D., Bhartia, P., Haffner, D., Labow, G. and Flynn, context.QuarterlyJournaloftheRoyalMeteorologicalSociety,135,
L. (2013) The version 8.6 SBUV ozone data record: an 1863–1873.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

2048 HERSBACHetal.
Pincus, R., Barker, H.W. and Morcrette, J.-J. (2003) A fast, flexi- humidity,temperatureandprecipitation:inferencesfromreanal-
ble,approximatetechniqueforcomputingradiativetransferin ysesandmonthlygriddedobservationaldatasets.JournalofGeo-
inhomogeneousclouds.JournalofGeophysicalResearch:Atmo- physicalResearch,115,22987–22994.
spheres,103(4376).https://doi.org/10.1029/2002JD003322 Simmons, A.J., Poli, P., Dee, D.P., Berrisford, P., Hersbach, H.,
Poli,P.,Hersbach,H.,Dee,D.P.,Berrisford,P.,Simmons,A.J.,Vitart, Kobayashi,H.andPeubey,C.(2014)Estimatinglow-frequency
F.,Laloyaux,P.,Tan,D.G.H.,Peubey,C.,Thépaut,J.-N.,Trémo- variability and trends in atmospheric temperature from the
let,Y.,Hólm,E.V.,Bonavita,M.,Isaksen,L.andFisher,M.(2016) ERA-Interimreanalysis.QuarterlyJournaloftheRoyalMeteoro-
ERA-20C: an atmospheric reanalysis of the twentieth century. logicalSociety,140,329–353.
JournalofClimate,29(11),4083–4097. Simmons,A.J.,Berrisford,P.,Dee,D.P.,Hersbach,H.,Hirahara,S.
Poli, P., Moll, P., Puech, D., Rabier, F. and Healy, S.B. (2009) and Thépaut, J.-N. (2017) A reassessment of temperature vari-
Quality control, error analysis, and impact assessment of ations and trends from global reanalyses and monthly surface
FORMOSAT-3/COSMIC in numerical weather prediction. Ter- climatologicaldatasets.QuarterlyJournaloftheRoyalMeteoro-
restrialAtmosphericandOceanicSciences,20,101–113.https:// logicalSociety,143,101–119.
doi.org/10.3319/TAO.2008.01.21.02(F3C) Simmons,A.J.,Soci,C.,Nicolas,J.,Bell,B.,Berrisford,P.,Dragani,
Randel, W.J., Smith, A.K., Wu, F., Zou, C.-Z. and Qian, H. (2016) R., Flemming, J., Haimberger, L., Healey, S.B., Hersbach, H.,
Stratospheric temperature trends over 1979–2015 derived from Horányi,A.,Inness,A.,Muñoz-Sabater,J.,Radu,R.andSchep-
combinedSSU,MLS,andSABERsatelliteobservations.Journal ers,D.(2020).Globalstratospherictemperaturebiasandother
of Climate, 29(13), 4843–4859. https://doi.org/10.1175/JCLI-D- stratosphericaspectsofERA5andERA5.1.TechnicalMemoran-
15-0629.1 dum859,ECMWF,Reading,UK.
Raoult, B., Bergeron, C., Alós, A.L., Thépaut, J.-N. and Dee, D.P. Steinbrecht, W., Hegglin, M.I., Harris, N. and Weber, M. (2018) Is
(2017)Climateservicedevelopsuser-friendlydatastore.ECMWF global ozone recovering?. Comptes Rendus Geoscience, 350(7),
Newsletter,151,22–27. 368–375.
Saha,S.,Moorthi,S.,Wu,X.,Wang,J.,Nadiga,S.,Tripp,P.,Behringer, Stoffelen, A. and Anderson, D. (1997) Scatterometer data inter-
D.,Hou,Y.-T.,Chuang,H.-y.,Iredell,M.,Ek,M.,Meng,J.,Yang, pretation: estimation and validation of the transfer function
R.,Mendez,M.P.,vandenDool,H.,Zhang,Q.,Wang,W.,Chen, CMOD4. Journal of Geophysical Research: Oceans, 102(C3),
M. and Becker, E. (2014) The NCEP climate forecast system 5767–5780.
version2.JournalofClimate,27(6),2185–2208. Takacs,L.L.,Suárez,M.J.andTodling,R.(2016)Maintainingatmo-
Salonen, K. and Bormann, N. (2016). Atmospheric Motion Vec- sphericmassandwaterbalanceinreanalyses.QuarterlyJournal
tor observations in the ECMWF system: Fifth year report 41. oftheRoyalMeteorologicalSociety,142,1565–1573.
EUMETSAT/ECMWF Fellowship Programme Research Report Tarek,M.,Brissette,F.P.andArsenault,R.(2019)Evaluationofthe
41,ECMWF,Reading,UK. ERA5reanalysisasapotentialreferencedatasetforhydrological
Sandu,I.,Beljaars,A.,Balsamo,G.andGhelli,A.(2011)Revision modelingoverNorthAmerica.HydrologyandEarthSystemSci-
ofthesurfaceroughnesslengthtable.ECMWFNewsletter,130, encesDiscussion,2019,1–35.https://doi.org/10.5194/hess-2019-
8–10. 316
Sandu,I.,Beljaars,A.,Bechtold,P.,Mauritsen,T.andBalsamo,G. Tavolato, C. and Isaksen, L. (2015) On the use of a Huber norm
(2014)Whyisitsodifficulttorepresentstablystratifiedcondi- forobservationqualitycontrolintheECMWF4D-Var.Quarterly
tionsinnumericalweatherprediction(NWP)models?.Journalof JournaloftheRoyalMeteorologicalSociety,141,1514–1527.
AdvancesinModelingEarthSystems,5(2),117–133. Tetzner,D.,Thomas,E.andAllen,C.(2019)AvalidationofERA5
Saunders,R.,Hocking,J.,Turner,E.,Rayer,P.,Rundle,D.,Brunel,P., reanalysisdataintheSouthernAntarcticpeninsula–Ellsworth
Vidot,J.,Roquet,P.,Matricardi,M.,Geer,A.J.,Bormann,N.and Landregion,anditsimplicationsforicecorestudies.Geosciences,
Lupu,C.(2018)AnupdateontheRTTOVfastradiativetransfer 9.https://doi.org/10.3390/geosciences9070289
model(currentlyatversion12).GeoscientificModelDevelopment, Thépaut,J.-N.,Dee,D.P.,Engelen,R.andPinty,B.(2018).TheCoper-
11(7),2717–2737. nicusprogrammeanditsclimatechangeservice.pp.1591–1593
Schepers,D.,deBoisséson,E.,Eresmaa,R.,Lupu,C.anddeRosnay, inIEEEInternationalGeoscienceandRemoteSensingSympo-
P.(2018)CERA-SAT:Acoupledsatellite-erareanalysis,ECMWF sium,Valencia,Spain.
Newletter155,32–37 Tiedtke,M.(1989)Acomprehensivemassfluxschemeforcumulus
Shepherd, T.G., Polichtchouk, I., Hogan, R.J. and Simmons, A.J. parameterizationinlarge-scalemodels.MonthlyWeatherReview,
(2018).ReportonStratosphereTaskForce.TechnicalMemoran- 117(8),1779–1800.
dum824,ECMWF,Reading,UK. Tiedtke,M.(1993)Representationofcloudsinlarge-scalemodels.
Shine,K.P.,Barnett,J.J.andRandel,W.J.(2008)Temperaturetrends MonthlyWeatherReview,121(11),3040–3061.
derivedfromStratosphericSoundingUnitradiances:Theeffectof Titchner,H.A.andRayner,N.A.(2014)TheMetOfficeHadleyCen-
increasingCO ontheweightingfunction.GeophysicalResearch treseaiceandseasurfacetemperaturedataset,version2:1.Sea
2
Letters,35(L02710) iceconcentrations.JournalofGeophysicalResearch:Atmospheres,
Simmons,A.J.,Hortal,M.,Kelly,G.A.,McNally,A.P.,Untch,A.and 119(6),2864–2889.
Uppala, S.M. (2005) ECMWF analyses and forecasts of strato- Trenberth, K.E., Fasullo, J.T. and Balmaseda, M.A. (2014) Earth's
spheric winter polar vortex breakup: September 2002 in the energyimbalance.JournalofClimate,27(9),3129–3144.https://
SouthernHemisphereandrelatedevents.JournaloftheAtmo- doi.org/10.1175/JCLI-D-13-00294.1
sphericSciences,62(3),668–689. Trenberth, K.E., Fasullo, J.T. and Kiehl, J. (2009) Earth's global
Simmons, A.J., Willett, K.M., Jones, P.D., Thorne, P.W. and Dee, energybudget.BulletinoftheAmericanMeteorologicalSociety,90,
D.P. (2010) Low-frequency variations in surface atmospheric 311–323.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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

HERSBACHetal. 2049
Trenberth,K.E.andSmith,L.(2005)Themassoftheatmosphere:a Woodruff, S.D., Worley, S.J., Lubker, S.J., Ji, Z., Freeman, J.E.,
constraintonglobalanalyses.JournalofClimate,18(6),864–875. Berry, D.I., Brohan, P., Kent, E.C., Reynolds, R.W., Smith, S.R.
Trolliet,M.,Walawender,J.P.,Bourlès,B.,Boilley,A.,Trentmann,J., and Wilkinson, C. (2011) ICOADS Release 2.5: extensions and
Blanc,P.,Lefèvre,M.andWald,L.(2018)Downwellingsurface enhancements to the surface marine meteorological archive.
solarirradianceinthetropicalAtlanticOcean:acomparisonof InternationalJournalofClimatology,31(7),951–967.https://doi.
re-analysesandsatellite-deriveddatasetstoPIRATAmeasure- org/10.1002/joc.2103
ments.OceanScience,14(5),1021–1056. Xu,X.,Frey,S.K.,Boluwade,A.,Erler,A.R.,Khader,O.,Lapen,D.R.
Uppala, S.M., Kållberg, P.W., Simmons, A.J., Andrae, U., da Costa andSudicky,E.(2019)Evaluationofvariabilityamongdifferent
Bechtold, V., Fiorino, M., Gibson, J.K., Haseler, J., Hernandez, precipitationproductsintheNorthernGreatPlains.Journalof
A.,Kelly,G.A.,Li,X.,Onogi,K.,Saarinen,S.,Sokka,N.,Allan, Hydrology:RegionalStudies,24(100608).https://doi.org/10.1016/
R.P.,Andersson,E.,Arpe,K.,Balmaseda,M.A.,Beljaars,A.C.M., j.ejrh.2019.100608
vandeBerg,L.,Bidlot,J.,Bormann,N.,Caires,S.,Chevallier,F., Zuo, H., Balmaseda, M.A., Mogensen, K. and Tietsche, S. (2018).
Dethof,A.,Dragosavac,M.,Fisher,M.,Fuentes,M.,Hagemann, OCEAN5: The ECMWF Ocean Reanalysis System and its
S., Hólm, E.V., Hoskins, B.J., Isaksen, L., Janssen, P.A.E.M., real-time analysis component. Technical Report 823, ECMWF,
Jenne,R.,McNally,A.P.,Mahfouf,J.-F.,Morcrette,J.-J.,Rayner, Reading,UK.
N.A.,Saunders,R.W.,Simon,P.,Sterl,A.,Trenberth,K.E.,Untch,
A.,Vasiljevic,D.,Viterbo,P.andWoollen,J.(2005)TheERA-40
re-analysis.QuarterlyJournaloftheRoyalMeteorologicalSociety, SUPPORTING INFORMATION
131,2961–3012. Additional supporting information may be found online
Urraca,R.,Huld,T.,Gracia-Amillo,A.,Martinez-dePison,F.J.,Kas- in the Supporting Information section at the end of this
par,F.andSanz-Garcia,A.(2018)Evaluationofglobalhorizontal
article.
irradianceestimatesfromERA5andCOSMO-REA6reanalyses
usinggroundandsatellite-baseddata.SolarEnergy,164,339–354.
van den Hurk, B.J., Viterbo, P., Beljaars, A. and Betts, A. (2000). Howtocitethisarticle: HersbachH, BellB,
OfflinevalidationoftheERA40surfacescheme.TechnicalMem-
BerrisfordP,etal.TheERA5globalreanalysis.QJR
orandum295,ECMWF,Reading,UK.
MeteorolSoc.2020;146:1999–2049.
Wernli,H.,Dirren,S.,Liniger,M.A.andZillig,M.(2002)Dynamical
https://doi.org/10.1002/qj.3803
aspectsofthelifecycleofthewinterstormLothar(24–26Decem-
ber1999).QuarterlyJournaloftheRoyalMeteorologicalSociety,
128,405–429.
1477870x,
2020,
730,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803
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
[11/03/2026].
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