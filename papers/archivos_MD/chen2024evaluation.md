| Received:15May2023 |     | Revised:7November2023 |     |     | Accepted:4December2023 |     |     |     |     |     |     |
| ------------------ | --- | --------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
DOI:10.1002/joc.8339
| RESEARCH   | ARTICLE |       |               |               |           |          |             |       |         |       |     |
| ---------- | ------- | ----- | ------------- | ------------- | --------- | -------- | ----------- | ----- | ------- | ----- | --- |
| Evaluation |         | of    | ERA5          | precipitation |           |          | and         | 10-m  | wind    | speed |     |
| associated |         | with  | extratropical |               |           | cyclones |             | using | station |       |     |
| data over  |         | North | America       |               |           |          |             |       |         |       |     |
| Ting-Chen  | Chen1,2 |       | | François    |               | Collet1,3 |          | | Alejandro | Di    | Luca1   |       |     |
1DépartementdesSciencesdelaTerreet
|     |     | (cid:1) |     | Abstract |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
del'atmosphère,CentreEtudeet
simulationduclimatàl'échellerégionale While the ERA5 reanalysis is commonly utilized in climate studies on
(ESCER),UniversitéduQuébecà
extratropical cyclones (ETCs), only a few studies have quantified its ability in
Montréal,Montréal,Quebec,Canada
therepresentationofETCsoverland.Toaddressthisgap,thisstudyevaluates
2InstituteforMeteorologyandClimate
Research—DepartmentTroposphere ERA5'sskill inrepresenting the ETC-associated 10-mwind speed and thepre-
2005–2019.
(IMK-TRO),KarlsruheInstituteof cipitation in central and eastern North America during Hourly
| Technology,Karlsruhe,Germany |     |     |     |     |     | (cid:1)3000 |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
data collected from stations, amounting to around 420 million reports
3CECIUniversitédeToulouse,
storedintheIntegratedSurfaceDatabase,isusedasreference.Forthespatial-
CERFACS/CNRS,Toulouse,France
averaged ETC properties, ERA5 shows a good skill for wind speed with
| Correspondence |     |     |     |     |     |     |     | −0.7% |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
normalized mean bias (NMB) of and normalized root-mean-square
FrançoisCollet,CECIUniversitéde
error (NRMSE) of 14.3%, despite a tendency to overestimate low winds and
Toulouse,CERFACS/CNRS,Toulouse,
France. underestimate high winds. The ERA5 skill is worse for precipitation than for
| Email:collet@cerfacs.fr |     |     |     |     |     |     | −10.4% |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
wind speed with NMB of and NRMSE of 56.5% and a strong tendency
to underestimate high values. For both variables, the best and worst perfor-
Fundinginformation
NaturalSciencesandEngineering mance is found in DJF and JJA, respectively. Negative biases are often identi-
ResearchCouncilofCanada(NSERC),
fied over regions with stronger precipitation/wind speeds, and a systematic
Grant/AwardNumber:RGPIN-2020-
05631;GovernmentofQuébec underestimation of wind speed isfound over the Rockies with complex topog-
raphy. Compared to the averaged ETCs, ERA5's performance deteriorates for
thetop5%extremeETCswithastrongertendencytounderestimatebothwind
|     |     |     |     |       |                   |     |         | −10.2% | −22.6%, |                |          |
| --- | --- | --- | --- | ----- | ----------------- | --- | ------- | ------ | ------- | -------------- | -------- |
|     |     |     |     | speed | and precipitation |     | (NMB of |        | and     | respectively). | Further- |
more,ERA5'sskillisworseforlocalextremevalueswithinETCsthanforspa-
tial averages. Our results highlight some important limitations of the ERA5
reanalysisproductsforstudieslookingatthepossibleimpactsofETCs.
KEYWORDS
ERA5evaluation,extratropicalcyclone,localextremes,near-surfacewinds,precipitation
|     |     |     |     |     |     | 1             | | INTRODUCTION |          |        |          |             |
| --- | --- | --- | --- | --- | --- | ------------- | -------------- | -------- | ------ | -------- | ----------- |
|     |     |     |     |     |     | Extratropical |                | cyclones | (ETCs) | modulate | the weather |
Ting-ChenChenandFrançoisColletshouldbeconsideredjointfirst
authors. variability in mid-to-high latitudes and constitute an
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttribution-NonCommercialLicense,whichpermitsuse,distributionandreproductioninany
medium,providedtheoriginalworkisproperlycitedandisnotusedforcommercialpurposes.
©2024TheAuthors.InternationalJournalofClimatologypublishedbyJohnWiley&SonsLtdonbehalfofRoyalMeteorologicalSociety.
IntJClimatol.2024;44:729–747.
|     |     |     |     |     |     |     |     |     | wileyonlinelibrary.com/journal/joc |     | 729 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |

730 CHENETAL.
essential component of the atmospheric general circula- assimilation techniques (e.g., Naud et al., 2018; Wang
tion (e.g., Catto et al., 2019). ETCs are favoured over etal.,2016).Whileintercomparisonstudiesindicatethat
regions with strong low-level temperature gradients recent reanalysis products show converging results in
(baroclinic instability), but orographic effects (e.g., lee terms of the number and location of ETCs (e.g., Catto
cyclogenesis) and diabatic effects (e.g., surface fluxes, et al., 2010; Di Luca et al., 2015; Hodges et al., 2011),
latent heating) are also important contributing factors large uncertainties are still found in the instantaneous
for cyclone development (Hoskins, 1990; Petterssen & fields at small spatial scales (Hodges et al., 2011),
Smebye, 1971; Uccellini, 1990). In regions dominated by particularly for weak cyclones (Neu et al., 2013).
their occurrence, ETCs are often the main contributor to Furthermore,ithasbeenshownthatreanalysiscontains
local extreme precipitation and near-surface wind, shaping more significant biases in extreme than non-extreme
the regional climatology and causing severe damages weather conditions (e.g., Campos et al., 2022; Lei
(Booth et al., 2015; Hawcroft et al., 2012; Kunkel et al., 2022). For example, Campos et al. (2022) evalu-
et al., 2012). For example, the Halloween storm in 2019 ated the quality of near-surface winds in the ERA5 rea-
swept through eastern Canada with heavy precipitation nalysis using higher spatiotemporal resolution satellite
and damaging wind gusts, resulting in over 250 million in data over the Atlantic Ocean. They found greater dis-
insureddamagesandthemostseverepoweroutageinQue- crepancies (with ERA5 underestimating winds by
bec province in 20years (Government of Canada, 2020; approximately 10%–15%) with the presence of tropical
Insurance Bureau of Canada, 2019). Therefore, improving or ETCs than no-cyclone conditions. They also showed
ourabilitytocaptureandunderstandETCs'space–timefea- that the relative underestimation of ERA5 increases as
tures and impacts is of great social-economic and climatic thewindsbecomemoreextreme.
importance. While many studies have assessed the quality of
To characterize the lifecycle of ETCs, including their reanalysis products for different variables with various
frequency and intensity, reanalysis data are generally reference data, most of them either considered a fixed
used due to their homogeneous availability in time and geographical region without differentiating ETC events
space, especially over oceans where ETCs are active but (e.g., Jiao et al., 2021; Minola et al., 2020; Molina
in-situ observations are sparse (e.g., Di Luca et al., 2015; et al., 2021; Peña-Arancibia et al., 2013) or focused on
Hodges et al., 2011; Rudeva & Gulev, 2011; Simmonds & oceanic cyclones only (e.g., Naud et al., 2018, 2020;
Keay, 2000; Wang et al., 2006). To obtain a climatology Pepler et al., 2018). Although reanalysis assimilate rela-
of ETCs, Lagrangian approaches employ objective identi- tively more observational data over land than ocean, the
fication and tracking algorithms, usually using mean complex terrain and heterogeneous land types may pose
sea level pressure or relative vorticity fields (e.g., Neu greater challenges for models and reanalysis products to
et al., 2013). Statistical cyclone properties can then be represent the near-surface atmospheric variables that are
constructed, and the storm structure can be obtained via strongly dependent on local characteristics (e.g., Brune
cyclone-centered composites of temperature, low-level et al., 2021; Gualtieri, 2022; Jiménez et al., 2008; Lavers
windspeed, precipitation, andso forth(e.g.,Bauer&Del et al., 2022; Minola et al., 2020). It is therefore impor-
Genio, 2006; Booth et al., 2018; Field & Wood, 2007; tant to investigate the reliability of reanalysis for ETCs
Pepler et al., 2018; Sinclair et al., 2020). Some climate- over the continent, where human activities are directly
model-based studies assess the response of ETCs to cli- affected.
mate change by comparing the cyclone statistics over a Therefore, this study aims to address this gap by
historical period with those simulated under projected evaluating the skill of the most up-to-date and widely-
future climate scenarios. In such studies, reanalysis data used global reanalysis product from the European Cen-
arestillimportantastheyareoftentakenasabaselineto tre for Medium-Range Weather Forecasts (ECMWF),
evaluate the performance of climate models via hindcast the ERA5 reanalysis (Hersbach et al., 2020), at repre-
simulations (e.g., Catto et al., 2010; Feser et al., 2015; senting 10-m wind speed and precipitation associated
Zappa et al., 2013). Additionally, reanalysis products are with ETCs over North America during 2005–2019. We
also frequently used to assess the precipitation, wind, utilize the in-situ station data from the Integrated Sur-
and/orcompoundextremesbroughtbyETCs(e.g.,Hénin face Database (ISD) as the reference, considering that
etal.,2021;Owenetal.,2021). thenear-surfacewindandsurfaceprecipitationobserva-
However, a reanalysis is only a proxy of the actual tionsfromISDarenot directlyassimilatedinERA5.We
atmospheric conditions, and different reanalysis data- identify and track ETCs with an objective algorithm
sets do not necessarily agree with each other in and, using the centre of each cyclone and a constant
the representation of ETCs due to the varying model radius, we perform the evaluation of ERA5 using two
physics, resolution, observations being ingested, and quantities: a spatial average and a spatial extreme over
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

 10970088, 2024, 3, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| CHENETAL. |     |     |     |     |     |     | 731 |
| --------- | --- | --- | --- | --- | --- | --- | --- |
each cyclone. The first quantity provides an assessment et al., 2020). NCEP stage IV is only available in the
oftheactual qualityoftheERA5reanalysis.Thesecond United States. The 10-m wind speed is derived from
measure evaluates not only the ERA5 quality but also the instantaneous zonal (u) and meridional (v) wind
pffiffiffiffiffiffiffiffiffiffiffiffiffi
the distinct spatial representativity of station and ERA5 speed components at 10m height (ws= u2+v2). The
data (Lavers et al., 2022). All analyses are made at the ERA5 10-m wind speed is a diagnosed product to be
| seasonal | and annual | scale. Section | 2 describes the data- |     |     |     |     |
| -------- | ---------- | -------------- | --------------------- | --- | --- | --- | --- |
compatiblewiththewindobservationsfromSYNOP(sur-
sets,themethodologyforcyclonetrackinganddatapro- faceSYNOPticobservations)stations.Becausethestation
cessing,andtheevaluationmetrics.Resultsareshownin
|     |     |     |     | requires | wind measurement | to be in open | terrain, an |
| --- | --- | --- | --- | -------- | ---------------- | ------------- | ----------- |
Section 3. Section 4 discusses the sensitivity of our results exposure adjustment is included in ERA5 10-m winds
to various methodological choices, and a comparison (ECMWF,2016).
| between | our mainfindingswithpreviousstudies. |     | Conclu- |     |     |     |     |
| ------- | ------------------------------------ | --- | ------- | --- | --- | --- | --- |
sionsarepresentedinSection5. Because ground-based observation instruments have
|     |     |     |     | a finite detectable | precision | but ERA5 does | not, ERA5 |
| --- | --- | --- | --- | ------------------- | --------- | ------------- | --------- |
likelyhasapositivebiasagainstISDatthelowendofthe
| 2 | DATA | AND | METHODS |     |                    |                    |                     |                |
| -------- | --- | ------- | --- | ------------------ | ------------------ | ------------------- | -------------- |
|          |     |         |     | wind/precipitation | distributions.     | To take             | this precision |
|          |     |         |     | issue into         | account, we adjust | the ERA5 grid-point | value          |
2.1 | The ERA5 reanalysis to 0 if the wind speed is smaller than 0.5m/s and if the
|     |     |     |     | precipitation | rate is smaller | than 0.2mm/h, | based on |
| --- | --- | --- | --- | ------------- | --------------- | ------------- | -------- |
ERA5 is the latest reanalysis produced by the ECMWF some up-to-date instruments manuals for rain gauges
and provides a range of atmospheric, land-surface and and wind sensors (Vaisala, 2020, 2021). Note that these
sea-state variables over the globe (Hersbach et al., 2020). thresholds also seem reasonable based on our examina-
ERA5 is based on the Integral Forecasting System (IFS) tion on the station data utilized in this study: For wind
Cycle 41r2 model, which has a horizontal resolution of speed, most stations have a minimum non-zero values of
31km and uses a total of 137 levels in the vertical (the either (cid:1)0.1, 0.5 or 1.5m/s, while for precipitation, the
majorityshowavalueof(cid:1)0.2mm/h(FigureS1).
| model's    | top is at 0.01hPa). | The model       | also uses a state-   |     |     |     |     |
| ---------- | ------------------- | --------------- | -------------------- | --- | --- | --- | --- |
| of-the-art | representation      | of sub-grid     | scale processes,     |     |     |     |     |
| including  | a scheme            | for large-scale | cloud and precipita- |     |     |     |     |
tion with prognostic variables for precipitating rain and 2.2 | The ISD
| snow and | a revised | deep-convection | scheme (see |     |     |     |     |
| -------- | --------- | --------------- | ----------- | --- | --- | --- | --- |
Hersbach et al., 2020 and references therein). In the sur- The ISD developed by the National Centers for Environ-
face layer (up to the lowest model level at about 10m), mental Information (NCEI) at the National Oceanic and
themodelusesMonin–Obukhovsimilaritytheorytorep-
|     |     |     |     | Atmospheric | Administration | (NOAA) archives | sub-daily |
| --- | --- | --- | --- | ----------- | -------------- | --------------- | --------- |
resentturbulentfluxesbetweenthesurfaceandtheatmo- observationsfrommorethan20,000automatedandman-
sphere. The model also uses a parametrization of ual surface weather stations across the globe (NOAA-
orographic drag that will affect near-surface wind speeds NCEI, 2018; Smith et al., 2011). It includes multiple
(ECMWF,2016). sources of meteorological reports and comprises several
In this study, the ERA5 reanalysis data, available atmospheric variables, including surface precipitation,
hourly on a regular latitude–longitude grid with a grid 10-m wind speed and direction, 2-m air and dew point
0.25(cid:3),
spacing of are used with a double objective. First, temperature, atmospheric sea level pressure and more.
we use its mean sea level pressure and 850-hPa relative This study uses 10-m wind speed and precipitation vari-
vorticity fields to identify and track ETCs over North ablesrecordedinNorthAmerica(10N–75Nand120W–
2005–2019.
America(seeSection2.3).Second,totalsurfaceprecipita- 40W region) during The precipitation vari-
tionand10-mwindspeedareusedtoassesstheabilityof able (“AA1 in the ISD dataset”) includes rain, snow and
the reanalysis to reproduce high-impact variables associ- anyotherfrozenprecipitation,melteddownintoawater-
ated with ETCs. Total precipitation represents the accu- equivalent value by Automated Surface Observing Sys-
mulatedliquidandfrozenwaterthatfallsoveragridbox tem stations with heated bucket rain gauges (NOAA,
during each hour and corresponds to the sum of convec- 1998). In order to merge multiple types of reports into
tiveprecipitationcalculatedbytheconvectionparametri- one dataset, ISD included a series of quality checks,
zation and the large-scale precipitation. Although surface assessingthedatavalidity,consistencybetweenvariables,
precipitation observations are not directly assimilated, the temporalcontinuity,andsoforth.Basedonthesechecks,
ERA5 assimilates the NCEP stage IV precipitation esti- each observed variable is flagged with a quality code and
mates (Lin & Mitchell, 2005) that combine NEXRADpre- expressed in a uniform format (NOAA-NCEI, 2018).
cipitation estimates with gauge measurements (Hersbach ReadersarereferredtoLott(2004)formoreinformation.

732 CHENETAL.
In this study, we employ additional ISD data selec- observations that do not pass all ISD quality checks
tions and post-processing techniques to compare with (i.e., quality code different than 1 or 5, which indicates
ERA5. The first selection is based on the type of data ‘passed all quality control checks’ and ‘passed all qual-
report. Several weather stations that transmit hourly ity control checks, data originate from an NCEI data
METAR(METeorologicalAerodromeReports)alsotrans- source’, respectively; NOAA-NCEI, 2018) are discarded.
mit intermediate METAR/SPECIs (METAR SPECIal For precipitation, only the 1-h accumulated records are
reports) every 20min. Even though intermediate reports considered (i.e., accumulation period code of 1). For
were recorded as 1-h accumulations, our manual checks wind speed, the type codes that indicate 5-, 60- and
suggest that the precipitation in these reports was accu- 180-min averaged wind speed are removed. To our
mulated for less than 1h, likely due to the constraints of knowledge, the remaining wind speed observations rep-
theISDdataformat.Therefore,weleaveouttheMETAR/ resentthe2-minaveragesat10mabovethegroundsur-
SPECIEs and AUTO (METAR reported without human face (Environnement et Changement Climatique
supervision) reports for precipitation data. For wind Canada,2021;NOAA-NCEI,2018).
speed observations, we exclude the NOAA's Climate Because not allobservations arerecordedatthe exact
Reference Network data because they are primarily hour, to compare them with the hourly ERA5 data, we
hourly averages and thus not compatible with the select the nearest-to-the-hour ISD observations within a
instantaneous winds we use from ERA5. To sum up, specifiedtimewindow.Thenearest1-haccumulatedpre-
we consider METAR and the NOAA's Climate Refer- cipitationreportthatpassesallISDqualitycheckswithin
ence Network data for precipitation and METAR, 15min prior to each hour is utilized, no matter whether
METAR/SPECIs, AUTO, SAO (Surface Airways Obser- the accumulated value is zero or not, while the wind
vation)andSYNOPforwindspeed. observation within a 30-min window centred on each
Next, we filter data based on their quality code and hour is selected. If several weather reports are recorded
observational type. Precipitation and wind speed at the same time for the same station, only the first
FIGURE 1 (a)Thelocationofintegratedsurfacedatabase(ISD)stationsforwindspeedobservationsusedinthisstudy.Thecolours
indicatetheproportionofsuchdataavailablefortheentire2005–2019period.Thegreenframerepresentstheregionusedtoselectcyclones,
asdescribedinSection2.3.(b)Sameas(a)butforprecipitation.(c)Totalnumberofreportsperdayforwindspeed,precipitationandboth
(simultaneously)asafunctionoftime.(d)Theproportionofwindspeed(red)andprecipitation(blue)observationasafunctionoftheUTC
houroftheday.(e)Sameas(d)butofthemonthoftheyear,withproportionstandardizedtoamonthof30days.[Colourfigurecanbe
viewedatwileyonlinelibrary.com]
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

CHENETAL. 733
report is utilized. We note that the cumulative distribu- 2.3 | ETC tracks
tions of these two observational variables are not contin-
uous as many records have a discrete unit/increment of ETC tracks are obtained by applying a cyclone tracking
one knot (i.e., 0.51m/s) for wind speed and 0.01 inch algorithm developed at the University of Quebec at Mon-
(i.e.,0.254mm/h)forprecipitation. tréal with the hourly ERA5 data (Chartrand &
The above ISD data processing leads to a total of Pausata,2020;Chenetal.,2022).Thisalgorithmidentifies
3831and2809stationsusedatleastonceforwindspeed cyclone centres based on the mean sea level pressure and
and precipitation, respectively (Figure 1a,b). These sta- the 850-hParelativevorticity.Forthisstudy,we onlycon-
tions are not homogeneously distributed over North sider ETCs whose centres remain in central and eastern
America, with a higher density in the central and east- North America (continental regions within 110–50W and
ern United States and a lower (zero) density in Canada 20–65N;namedCENAhereafter)formorethan24h.The
(Mexico). There are almost doubled amounts of wind westernpartofNorthAmericaisnotincludedbecausethe
speed reports compared to precipitation reports, but tracking algorithm is unreliable over regions with high
none of them show sharp changes during our study topography. It should be noted that some of the cyclones
period (Figure 1c), nor do they show large variation identified might be tropical cyclones and tropical transi-
across the hour of the day or the month of the year tions as no additional filter is applied to only select ETCs.
(Figure 1d,e). The temporal availability of stations dif- A total of 3643 cyclone tracks/cases are identified, result-
fers with variables. For all 3831 stations reporting wind inginatotalof310,000hourlyrecordsof‘cyclonecentre’.
speed, about 47% of them have hourly data for more
than 50% of the 2005–2019 period, while 32% of the sta-
tions have data for more than 90% of the period. For 2.4 | ETC-associated 10-m wind speed
precipitation, around 31% and 24% of the 2809 stations and precipitation
have hourly observations covering more than 50% and
90% of the period of interest, respectively. While these To evaluate ERA5 for ETC events, we compare the wind
values may seem low, they are somewhat underesti- speed and precipitation variables against observations,
mated measures of the station data's actual complete- whenandwhere applicable withina1000-km radiusofa
ness for multiple reasons. First, they only account for cyclone centre. This horizontal length is assumed to be
the selected data after the above filtering. Second, more suitable to capture the bulk impacts and the embedded
than 300 stations only provide SYNOP reports that are local extremes associated with ETCs (e.g., Catto
not provided hourly, and about 1400 stations provide at etal.,2010;Field&Wood,2007;Jeyaratnametal.,2020).
least one SYNOP report. Finally, about 50% of the sta- Resultsbasedonasmallerradiusof500kmarediscussed
tionsusedinthisstudyhaveanoperatinglengthshorter inSection4.1.
than the study period. Since this work does not involve To ensure a fair comparison, three additional criteria
anytrendanalysis,wedonotputanadditionalselection are imposed. First, while there can be as many as 7500
criterion based on the stations' temporal coverage. Nev- ERA5 grid cells within a 1000-km-radius circular region,
ertheless,wehaveconductedanexaminationbasedona only a few hundred ISD observations are available in
longer study period from 2000 to 2019 with an even most cases. To account for the spatial heterogeneity of
lower percentage of temporal coverage and found con- ISD stations, ERA5 grid points are masked out where
sistentresults(notshown). and when no interpolated ISD observation is available.
Finally, the selected ISD data are spatially interpo- Second, because ISD stations are mostly over land but
lated to the ERA5 0.25 ×0.25(cid:3) latitude–longitude regu- can be on the shore, we discard all ERA5 grid points for
lar grid over North America. For each ERA5 grid cell, which the land-sea mask is lower than 0.5, a suggested
we consider the available ISD observation that is minimum value indicating a mixture of land and inland
locatedwithinandnearesttothecentreofthegridcell. water but not ocean (Copernicus Climate Change Ser-
If ISD data are not available, a missing value is vice, Climate Data Store, 2023). The second criterion is
recorded.Wehavealsotestedanaveragingmethod,for requiredbecausesomecoastalorlakesideISDstationscan
which the average of all ISD observations within one be interpolated to an almost pure-water ERA5 grid point.
grid cell is taken, but the results do not change signifi- Note that we have also tested a lower land-sea mask
cantly from the nearest-station method due to the threshold of 0.2, including grid points with a higher
sparse ISD station density with respect to the ERA5 ocean/lakefraction,andfoundalargerdifferencebetween
grid resolution. As shown in Figure S2, only a small ERA5 and ISD, a natural bias due to the different surface
number of ERA5 grid cells contain multiple ISD roughnesslengthsbetweenlandandwater/ice.Third,only
observations. the cyclone centres with at least 100 interpolated ISD
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

 10970088, 2024, 3, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 734 |     |     |     |     |     | CHENETAL. |
| --- | --- | --- | --- | --- | --- | --------- |
FIGURE 2 (a)AnexampleshowingtheidentificationofWSavgandWS95foragivencyclonecentreat48.5(cid:3)N,93.25(cid:3)W,at2100UTC
on26October2010,overlaidwiththeERA5meansealevelpressure(greendashedcontours;hPa).Thegreysolidcirclerepresentsthe
cyclone's1000-kmdomain,whichincludes313ISDstationsinthiscase(smalldots;windspeedshownincolours),fromwhichtheWSavg
andWS95arederived(upper-leftbox).(b)TheERA510-mwindspeedforthesamecyclonecentre,withthecompletenativefieldshownin
translucentshadingsandtheunmaskedERA5gridvalues(tobecomparedwithISD)showninsmalldotsasin(a).Thewholetrackofthis
cycloneisshownintheupper-rightcorner.ISD,IntegratedSurfaceDatabase.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
observations within the 1000-km radius were considered. 2.5 | Evaluation metrics
| This threshold | was arbitrarily | set by a trade-off | between |     |     |     |
| -------------- | --------------- | ------------------ | ------- | --- | --- | --- |
having sufficiently large observational samples for each To assess the ERA5 performance, we use several quanti-
cyclone and having enough cyclones to systematically tative metrics, including the bias, root mean squared
examine the potential bias for ETCs. Our results do not error (RMSE), Pearson correlation coefficient and ordi-
change substantially when different thresholds of 50, 100 nary least squares regression analysis. To investigate the
and200stationsareused(FigureS3). seasonal skill, these metrics are also calculated for
To evaluate ERA5's skill in representing ETCs' overall cyclonesindifferentseasons.
impacts,thespatialaveragesofallunmaskedERA5andISD First, the normalized mean bias (NMB) is calculated
grid-pointwindspeedandprecipitation,namedWSavgand as the averaged difference (bias) for a target variable
PRavg, respectively, are computed for each cyclone centre. CbetweenERA5andISDacrossallcyclones,normalized
AnillustrationexampleisgiveninFigure2.Sinceonlythe bythemeanvalueoftheobservation:
| unmasked | data are considered,it | should be | borne in mind |     |            |         |
| -------- | ---------------------- | --------- | ------------- | --- | ---------- | ------- |
|          |                        |           |               |     | Pn (cid:3) | (cid:4) |
thatWSavgandPRavgdonotpresentrealisticcyclonestatis-
1 CERA5−CISD
|     |     |     |     |     | n i | i   |
| --- | --- | --- | --- | --- | --- | --- |
t i cs a n d a re b i as e d to w a r d s r e g io n s w i t h h ig h d e n s ity o f NMB= bi a s = i=1 ð1Þ
o b se rv a tio n s( C h e n et a l., 2 0 2 2) . I n a d di ti o n ,t o a sse s s E R A5 's I SD P n
|     |     |     |     |     | C 1 | CISD |
| --- | --- | --- | --- | --- | --- | ---- |
i
| performanceincapturingtheextremes,wefurtherexamine |         |                  |               |     | n i=1 |     |
| -------------------------------------------------- | ------- | ---------------- | ------------- | --- | ----- | --- |
| the most extreme                                   | cyclone | centres based on | the top 5% of |     |       |     |
WSavg/PRavg and the local extremes within the cyclones whereC denotesWSavg,PRavg,WS95 orPR95 forthe
|     |     |     |     | i   | i i | i i |
| --- | --- | --- | --- | --- | --- | --- |
basedonthespatial95th,98thand99thpercentilesineach cyclone centre i, and the overbar denotes the averages
1000-km cyclone domain. For the latter, we will focus on over n cyclone centres. Defined this way, NMB gives
results based on the 95th percentiles (noted as WS95 and moreweighttoETCtracksthatlastlongerandfacilitates
PR95forwindspeedandprecipitation,respectively)andthe the comparison of errors across different variables, sea-
sensitivitytodifferentpercentileswillbeshowninSection4. sons and regions, taking into account the varying back-
Note that in the evaluation for spatial extremes, we do not groundintensity.
require ERA5 and ISD to capture them at the same grid Similarly, the normalized root-mean-square error
points.Instead,weareinterestedinwhetherERA5canpro- (NRMSE) measures the RMSE between ERA5 and ISD
ducesimilarlystrongmagnitudeswithinETCs. scaledbytheaveragedISDobservationalvalue:

 10970088, 2024, 3, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
CHENETAL. 735
|     |     | qffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi (cid:3) | (cid:4) |     |     |     |     |
| --- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | --- | --- | --- | --- |
P b et w e e n t h e t w o v a r i a b le s a r e c a u s e d b y t h e a v a i l a b i l i t y
|     |         | 1 n CE R A | 5−CI SD 2 |     |     |     |     |
| --- | ------- | ---------- | --------- | --- | --- | --- | --- |
|     | R M S E | n i= i     | i         |     |     |     |     |
NRMSE= = 1 : ð2Þ o f o b s e r v a t io n r e c o r d s ( Se c t io n 2 . 4 ) , a n d w i n d s p e e d
Pn
C IS D I SD o b s er v a t i o n s a re g l o b a l ly m o r e n u m e r o u s t h a n p r e c i p i t a -
1 C
n i
|     |     | i=1 |     | tion observations  | (Figure 1a,b). | Out of          | the total number |
| --- | --- | --- | --- | ------------------ | -------------- | --------------- | ---------------- |
|     |     |     |     | of cyclone centres | identified     | by the tracking | algorithm,       |
Finally, the Pearson correlation coefficient (CC) is about 30% and 21% are retained for wind speed and pre-
used to measure the linear association between the vari- cipitation variables, respectively. The number of cyclone
ablesderivedfromERA5andISD: centres varies with seasons, with the smallest number in
JJA(with21,258and12,198cyclonecentresforwindand
|     | P (cid:5) | (cid:6)(cid:5) | (cid:6) |     |     |     |     |
| --- | --------- | -------------- | ------- | --- | --- | --- | --- |
n CERA5−CERA5 CISD−CISD precipitation, respectively) and the largest number in
|     | i = ffiffiffi1ffiffiffiffiffiffiffiffiiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi | ffiffiffiffirffiffiffiffiffiffiffiffiiffiffiffiffi |     |     |     |     |     |
| --- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- | --- | --- | --- | --- | --- |
CC=rffiffiffiffiffiffiffiffiffiffiffiffi ffiffi ffi ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffiffiffiffi: MAM (with 27,586 and 20,314 cyclone centres for wind
|     | P (cid:5) | (cid:6) P (cid:5) | (cid:6) |     |     |     |     |
| --- | --------- | ----------------- | ------- | --- | --- | --- | --- |
|     |           | 2                 | 2       |     |     |     |     |
n CERA5−CERA5 n CISD−CISD and precipitation, respectively). Yet, the distribution of
|     | i=1 i | i=1 | i   |                |              |            |               |
| --- | ----- | --- | --- | -------------- | ------------ | ---------- | ------------- |
|     |       |     |     | cyclone centre | density does | not change | substantially |
ð3Þ
betweenseasonsforbothvariables(notshown).
| 3 | | RESULTS |     |     | 3.2 | Evaluation | of  | ETC averages |     |
| --- | ------- | --- | --- | ---------------- | --- | ------------ | --- |
3.1 | Cyclone distribution for WS and PR 3.2.1 | Domain averages of WSavg and
| evaluation |     |     |     | PRavg |     |     |     |
| ---------- | --- | --- | --- | ----- | --- | --- | --- |
Figure 3 shows the total number of cyclone centres that We first assess the ability of ERA5 in representing the
occurred in each ERA5 grid cell over the CENA region ETCs' spatial-mean wind speed. Figure 4a–d show the
during2005–2019.Notethatthisisnottheclimatologyof scatter plots of WSavg between ERA5 and ISD in DJF,
all cyclones but only those qualified for our evaluation. MAM,JJAandSON.Itisclearthatmostofthedatapoints
That said, large densities of cyclone centres still agree are distributed along the 1:1 line, indicating an overall
with the well-identified cyclone-active regions: the lee goodagreementbetweenISDandERA5.Theannualaver-
side of the Rockies where frequent cyclogenesis occurs, aged WSavg estimated from ISD and ERA5 are very close
theGreatLakesregionwhereenhancedheatfluxesfoster withthesameroundedvaluesof4.3m/s(Figure4e).How-
cyclone development/steepening and where cyclone ever, the lower slope of the linear fit compared with the
tracks of Alberta Clippers and Colorado Lows converge, 1:1linesuggeststhatERA5tendstobepositivelybiasedat
and the eastern coastline upstream to the Gulf Stream low wind speed values and negatively biased at high
where storm track prevails (e.g., Plante et al., 2015; Poan values in all seasons. Consistently, the quantile–quantile
et al., 2018; Reitan, 1974). The different sample sizes plots (red diamonds in Figure 4a–d) show that ERA5 and
FIGURE 3 (a)Numberofcyclonecentresateachgridpointwithmorethan10010-m-wind-speedobservationsavailablewithintheir
1000-kmradiusduring2005–2019period.Thetotalnumberofcyclonecentres(n)isshownonthetoprightcornerofeachmap.(b)Sameas
(a)butforprecipitationobservations.[Colourfigurecanbeviewedatwileyonlinelibrary.com]

736 CHENETAL.
FIGURE 4 (a–d)SeasonalscatterplotofISDagainstERA5WSavgwithGaussiandensityinblueshades.Quantile–quantileplotsare
showninreddiamondmarkersfor25th,50thand75thquantilesandstarmarkersfor1st,2nd,5th,10th,90th,95th,98thand99thquantiles
foreachseason.Theordinaryleastsquaresregressionisshownwithabluelineineachplot.(e)AveragedWSavgintensityforbothISDand
ERA5,(f)NMB,(g)NRMSEand(h)Pearsoncorrelationcoefficient(CC),allcalculatedseasonallyandannuallyoverthe2005–2019period.
[Colourfigurecanbeviewedatwileyonlinelibrary.com]
ISDagreequitewellinthemiddlerange,whereasthelow peaks magnitudes with opposite signs, −5.5% and 3.8%
quantiles of ERA5 (the 1st, 2nd, 5th and 10th) tend to be for MAM and SON, respectively. A closer examination
higherthanISDandthehighquantilesofERA5(the90th, of the quantile–quantile plots shows that the upper
95th, 98th, and 99th) tend to be lower than ISD. The tail of WSavg distribution is the most underestimated
annual normalized mean bias (NMB) is low (−0.7%) by ERA5 in MAM while the lower quantiles are the
although the NRMSE is a bit higher (14.3%). The annual most overestimated in SON (Figure 4b,d). For JJA,
correlation (CC) is 0.92, demonstrating a good linear rela- despite the large NRMSE, the notable positive and
tionship between ERA5 and ISD. In general, ERA5 well negative biases in both tails partially cancel out and
represents the WSavg despite slightly larger deviations for thus lead to a NMB closer to zero than during MAM
lowerandhighervalues. andSON.
On the seasonal scale, most error metrics show the To evaluate ERA5's performance in capturing the
worstperformancesofERA5inJJAwhentheaveraged ETCs' spatial-mean precipitation intensity, Figures 5a–d
WSavg reaches the annual minimum at 3.7 m/s showscatterplotsofPRavgbetweenERA5andISDofall
(Figure 4e). JJA has the highest NRMSE with a value cyclone centres in each season. Contrary to that for
of 17.5% and the lowest CC of 0.88, indicating a larger WSavg,ERA5doesnotexhibitanotableunderestimation
spread of ERA5 values (larger uncertainty) corre- at low values and the degree of underestimation at high
sponding to the same value of ISD. In contrast, ERA5 values varies notably with season. ERA5 represents the
exhibits the best performance in DJF with NMB close annually-averagedPRavgfairlywell,withaslightlylower
to0%,NRMSEof11.4%andCCof0.94.ForbothMAM value of 0.25mm/h than the ISD of 0.28mm/h. How-
and SON, ERA5 shows intermediate performances ever, the larger dispersion in scatter plots in Figure 5a–d
with NRMSE values of 14.6% and 14.2%, and correla- than in Figure 4a–d indicates a greater variability and
tion coefficients of 0.93. However, it is interesting to uncertainty in the precipitation field than in 10-m wind
note that the NMB in these transition seasons exhibit speed. Both the annual NMB (−10.4%) and NRMSE
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

CHENETAL. 737
FIGURE 5 SameasFigure4butforPRavg.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
(56.5%) for precipitation are at least four times larger indicating a general overestimation of ERA5 in winter-
than those for wind speed. Consistently, the CC is nota- timeETCs'averagedprecipitation.
bly lower (0.87) than for wind speed. Therefore, the
quantile–quantile plots (orange markers in Figure 5a–d)
can better describe the data than the linear fitted line, 3.2.2 | Spatial variability of WSavg and
showing that the right-skewed precipitation distribution PRavg
is nevertheless captured reasonably by ERA5 in all sea-
sonsexceptforJJA. It is of interest to examine whether the above results
Across seasons, it is clear that the largest disagree- exhibit some dependency on the geographical feature.
ment between ISD and ERA5 for ETC precipitation also We record the observed WSavg value and the associated
happens in JJA when the observed value reaches the ERA5-ISDbiasatthelocationofeachcyclonecentre(see
annual maximum (Figure 5e–h). Such a seasonal PRavg the big central dot in Figure 2) and take the local-
peak in JJA is not captured by ERA5, which shows an grid-cell average of all coinciding centres during 2005–
annual maximum inSONinstead.InJJA,ERA5severely 2019 to obtain a spatial distribution (Figure 6). Overall,
underestimates the mid and the upper quantiles, leading theintensityofwindspeedishigher over/near theRock-
to the largest magnitudes of NMB (−25.7%), NRMSE ies and central United States and lower in the southeast-
(63.0%) and the lowest CC (0.78). This is likely related to ern United States. High wind speeds are also observed in
the fact that ETCs are more convective in summertime the northeastern CENA, that is, near the entrance to the
(Jeyaratnametal.,2020)andthatthemodelresolutionis mid-latitude maritime storm track. The spatial variability
insufficient to resolve the embedded convective pro- of the WSavg bias shows some dependency on the wind
cesses, which are often accompanied by high-intensity intensity: negative biases are observed in regions with
precipitation.Incontrast,ERA5performsrelativelybetter strongerWSavg,thatis,overthewesternandnortheastern
for SON and DJF as the associated quantile distributions CENA, and positive biases are found mostly over where
are more aligned with the 1:1 line, and their seasonal WSavgarerelativelyweaker.Inaddition,Figure6suggests
averaged NRMSE are the lowest (yet still high) at about a strong tie between bias and the orography. The signifi-
45%. Interestingly, NMB is positive only for DJF, cant negative bias highlighted over the Rockies in all
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on Wiley
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

738 CHENETAL.
FIGURE 6 SpatialdistributionoftheISDWSavgmagnitude(leftcolumn)andthebias(ERA5-ISD;rightcolumn)averagedforall
cyclonecentersineachseason.NotethatwhileWSavgrepresentstheaverageovera1000-kmdomain,thevalueisrecordedonlyatthegrid
pointofthecyclonecentre(thebigdotinFigure2).Toimprovereadability,therawresultshavebeenspatiallysmoothedviathelinear
radialbasisfunctioninterpolation.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
seasons agrees with previous studies that ERA5 tends to United States towards the Great Plains (e.g., Arsenault
underestimate 10-m wind speed in regions with complex etal.,2020;Nelsonetal.,2016).Seasonalvariationsexistin
topography (e.g., Minola et al., 2020). The underlying rea- that the relatively wet region extends farther towards the
sons include the insufficiently-resolved topographic fea- northwestern CENA in MAM, JJA and SON, while it is
tures and the parametrization of orographic drag in the restrictedinthesoutheasternUnitedStatesinDJF.Further-
model (Irina Sandu et al., n.d.). The most negative NMB more,in addition to theoverall high PRavgnearthecoast,
in MAM (Figure 4f) is associated with the strong winds another peak is observed in the Midwestern United States
and thus large negative biases over the Rocky Mountains. in JJA (Figure 7c). It has been shown that summertime
On the other hand, the most positive NMB in SON cyclonesexhibitapolewardshiftofcyclogenesisandoccur-
(Figure4f)correspondstoseveralpatchesofpositivebiases rencecomparedtootherseasons(e.g.,Reitan,1974).While
alongtheeastcoast,Florida,andnearinlandlakes,where summertime ETCs do not produce as strong winds as in
WSavgseemmoderate(Figure6h). other seasons, their contribution to the precipitation is still
Figure 7 shows the maps of observed PRavg and bias pronounced. Additionally, Arctic cyclones are active in
associated with ETCs. In all, the distribution of PRavg is summer and those track southeastward into the Canadian
qualitativelyconsistent withthe climatologyofannualpre- Arctic Archipelago can transport moisture equatorward to
cipitation overNorth America,showinga gradualdecrease mid-latitude North America (Serreze et al., 2001;
of precipitation from the Gulf and Atlantic States of the Sorteberg & Walsh, 2008). Contrary to the WSavg, the
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

CHENETAL. 739
FIGURE 7 SameasFigure6butforPRavg.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
PRavgbiasdoesnot showacleardependencyontheorog- between the top 5% of WSavg and PRavg as represented
raphy, nor on the distribution of precipitation intensity inERA5andISD.
(Figure 7e–h). DJF exhibits mainly weak positive biases For hourly wind speed, the minimum threshold for
overtheentireCENAregion,whileJJAshowsmostlynega- selectingthetop5%(95thquantile)is7.0m/sinISDand
tive biases.Both SONand MAM present weakmagnitudes 6.5m/s in ERA5. Comparing two sets of the top 5%, we
with both signs over CENA. The most negative seasonal find a match of 73%, that is, 3452 out of a total of 4732
bias in JJA (Figure 5f) corresponds to the bias minima of observed extreme ETC instances are successfully cap-
below−0.125mm/hinMidwesternUnitedStates,collocat- tured as the top 5% by ERA5. To quantify the intensity
ingwiththelocalmaximaofPRavg. difference, we further perform comparisons using two
methods. Method 1 compares the intensity of extreme
centres by first identifying the top 5% extreme ETC cen-
3.3 | Evaluation of ETC extremes tres in ISD as ‘truth’ and retrieving these centres from
the ERA5 dataset. The derived mean intensity is 7.8m/s
3.3.1 | Extreme cases based on WSavg/ inISDand7.0m/sinERA5,withanNMBof−10.2%,an
PRavg NRMSEof12.5%,andaCCof0.71.Alternatively,method
II compares only the ‘matched’ ETC instances identified
As severe damages are often caused by the rare but inbothISDandERA5.TheaverageWSavgisalsoweaker
extremely strong ETCs, we compare the consistency inERA5(7.3m/s)thaninISD(7.9m/s),withanNMBof
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

 10970088, 2024, 3, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 740 |     |     |     |     |     |     |     | CHENETAL. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- |
TABLE 1 Summaryofthe
Averagedintensity
evaluationofERA5againstISDfor
|            | ISD      | ERA5     | NMB    | NRMSE | CC   | differentquantities. |     |     |
| ---------- | -------- | -------- | ------ | ----- | ---- | -------------------- | --- | --- |
| WSavg      | 4.3m/s   | 4.3m/s   | −0.7%  | 14.3% | 0.92 |                      |     |     |
| WSavgtop5% | 7.8m/s   | 7.0m/s   | −10.2% | 12.5% | 0.71 |                      |     |     |
| WS95       | 8.5m/s   | 7.1m/s   | −17.0% | 21.0% | 0.92 |                      |     |     |
| PRavg      | 0.28mm/h | 0.25mm/h | −10.4% | 56.5% | 0.87 |                      |     |     |
| PRavgtop5% | 1.18mm/h | 0.92mm/h | −22.6% | 42.6% | 0.30 |                      |     |     |
| PR95       | 1.40mm/h | 1.29mm/h | −7.2%  | 59.6% | 0.87 |                      |     |     |
Note:Forthetop5%evaluation,wecomparethevaluesofETCcentresidentifiedinISD(seemethodIin
thetext).
Abbreviations:CC,correlationcoefficient;ISD,IntegratedSurfaceDatabase;NMB,normalizedmeanbias;
NRMSE,normalizedroot-mean-squareerror.
−7.8%, an NRMSE of 10.0% and a CC of 0.73. In both percentile of hourly wind speed/precipitation (WS95/
comparisons, all error metrics except for the NRMSE PR95) within each cyclone centre. For this comparison,
indicate a worse performance, a systematic underestima- some discrepancy is expected given the inherent scale
tion, of ERA5 in capturing the wind speed for extreme disparity between ERA5 and ISD, because ERA5 vari-
cases than for the entire sample (Table 1). The ability of ables represent the areal-mean values over a grid cells of
ERA5 in capturing the extreme ETCs decreases with about 31×31km (Chen & Knutson, 2008; Di Luca
higher quantiles, as the percentage of cyclone matches et al., 2020), while station-based observations are point
withISDisloweredto63%forthetop1%WSavgcases. estimates that account for an area of only a few square
For hourly precipitation, the 95th-quantile thresholds km(Chuetal.,2021).Ourgoalisnottoisolatetherepre-
ofthePRavgare0.9mm/hinISDand0.8mm/hinERA5. sentativeness of ERA5 but to assess its overall (in)ade-
Only64%ofthetop5%PRavginISDaresuccessfullycap- quacy in applications of extreme analysis and risk
tured as the top 5% in ERA5 (i.e., 2068 out of a total of assessmentatlocalscales.
3242extreme ETCinstances),a lowermatchratethanfor For WS95, the annual-mean magnitude is 7.1 and
wind speed.Comparison usingmethod I shows aremark- 8.5m/s for ERA5 and ISD, respectively, that is, almost
able contrast between ISD and ERA5, with an averaged twotimeslargerthantheirintensityofWSavg(Figure8).
intensity of 1.18mm/h in ISD and 0.92mm/h in ERA5, Compared to the WSavg analysis for the entire and the
andtheNMB,NRMSEandCCof−22.6%,42.6%and0.30,
|     |     |     |     | top 5% | samples, ERA5 | exhibits a more | severe | tendency |
| --- | --- | --- | --- | ------ | ------------- | --------------- | ------ | -------- |
respectively. Comparing only those matched cyclone cen- to underestimate WS95 that persists across seasons.
tres(methodII),theaveragedintensityis1.2mm/hinISD Both NMB and NRMSE for WS95 indicate greater errors
−17.0%
and 1.1mm/h in ERA5, and the NMB, NRMSE and CC with annual values of and 21.0%, respectively
are −8.6%, 21.0% and 0.66, respectively. Again, except for (Table 1). The annual CC of 0.92 is similar to that for
NRMSE, all error metrics in both comparisons suggest a WSavg, indicating that the variability across cyclone cen-
worse, systematic underestimation of ERA5 in capturing tres is still well reproduced despite a systematic underes-
the precipitation intensity for the top 5% than for the timation. Different from that for WSavg, ERA5 shows its
entire sample (Table 1). The percentage of matches best performance in SON and its worst in MAM for
between ISD and ERA5 is also lowered, from 64% to 54% WS95 in terms of NMB and NRMSE, but the lowest sea-
whenweconsiderthetop1%PRavginsteadofthetop5%. sonal CC is still found in JJA. The spatial variability of
TheaboveresultsshowthatERA5hasalowerskillin the WS95 bias is similar to that of WSavg but is mostly
capturing the upper tails of wind speed and precipitation negative with a larger magnitude (Figure S4). In all, the
averages of all ETC centres, and this is not simply an results indicate that ERA5 performs worse in capturing
issue of spatial resolution as the comparisons are all thelocalextremevaluesthantheoverallimpactsofaver-
| basedonthe1000-km-radiusaverages. |                  |             |     | aged/extremecyclones. |                       |            |               |             |
| --------------------------------- | ---------------- | ----------- | --- | --------------------- | --------------------- | ---------- | ------------- | ----------- |
|                                   |                  |             |     | For                   | PR95, the annual-mean | magnitude  |               | is 1.29m/s  |
|                                   |                  |             |     | and 1.40m/s           | for ERA5              | and ISD,   | respectively, | approxi-    |
| 3.3.2                             | | Local extremes | (WS95/PR95) |     |                       |                       |            |               |             |
|                                   |                  |             |     | mately                | five times as large   | as the     | PRavg values  | on the      |
|                                   |                  |             |     | annual                | scale (Figure         | 9). Unlike | for the       | wind speed, |
Finally, we evaluate the performance of ERA5 in captur- the performance of ERA5 is not particularly worse for
ing the local extreme values, that is, the spatial 95th PR95 than for PRavg with a smaller magnitude of NMB

CHENETAL. 741
FIGURE 8 SameasFigure4butforWS95.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
FIGURE 9 SameasFigure5butforPR95.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

742 CHENETAL.
(−7.2%),asimilarCC(0.87)andaslightlyhigherNRMSE near cyclone-core region where precipitation and winds
of 59.6% annually (Table 1). The seasonal variation for are overall stronger, the averaged magnitudes of WSavg
PR95remainssimilartothatforPRavginthatERA5still and PRavg both increase, with a more notable change in
presents the best performance in DJF and the worst per- the latter than in the former. While the increase is seen
formances in JJA. However, two changes are observed. inbothERA5andISD,somechangesintheerrormetrics
First, the tendency of ERA5 underestimating the upper are observed. For wind speed, all error metrics indicate
quantiles becomes notable in all seasons, including DJF thatERA5performs slightly worse forthe moreconfined
(Figure9a–d).Second,thesevereunderestimationinJJAin (500-km radius) region than for the larger (1000-km
PRavg is improved notably for PR95 in relative terms radius) domain surrounding a cyclone, but the seasonal
(Figures 5e,f vs. 9e,f), thus leading to an overall reduced variation remains similar. Such performancedegradation
magnitude of NMB. As will be seen in Section 4.2, these is not surprising, as one would expect that as the radius
resultsaresomewhatsensitivetothechosenspatialpercen- increases, the compensation among local errors will also
tile for the definition of local extremes. Interestingly, while increase. Furthermore, a larger radius also allows some
thereisnoclearspatialcorrelationbetweenbiasandprecipi- room for potential shift/dislocation of moderate/strong
tation magnitude for PRavg, such correspondence emerges winds in ERA5. For precipitation, the skill degradation
for extreme values; larger negative bias tends to occur in for a smaller calculation radius still holds true in general
regionswithhigherPR95andviceversa(FigureS5). (except for NMB), but the most severe degradation is
observedinMAM,leadingtoashiftintheworstseasonal
performanceforPRavgfromJJAtoMAM.
4 | DISCUSSION
4.1 | Sensitivity of results to the cyclone 4.2 | Sensitivity of errors to the
radius definition of local extremes
In this study, we examine the sensitivity of our evalua- In this study, we examine the sensitivity of error metrics
tiontothechoiceofa500-kmradiusaroundETCcentres to the definition of local wind speed and precipitation
(Figure S6). Since a smaller radius concentrates on the extremes by considering different spatial percentiles
FIGURE 10 SensitivityoftheNRB(left),theNRMSE(middle)andtheCC(right)tothedefinitionofextremewindspeeds(toppanels)
andprecipitation(bottompanels)withinETCs.Threequantilevaluesareusedtoassessthesensitivity:95th,98thand99th.[Colourfigure
canbeviewedatwileyonlinelibrary.com]
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

CHENETAL. 743
(98th and 99th) within ETC centres (Figure 10). Regard- speed over mountainous regions but overestimation in
less of the variable, the higher the spatial percentile, the coastalsites(e.g.,Gualtieri,2022;Minolaetal.,2020).
larger the error magnitudes (NMB and NRMSE) and Regarding the ETC-associated precipitation, our
the lower the linear correlation (CC) between ERA5 and results showing an overall underestimation tendency in
ISD for all seasons. This indicates a monotonic decrease their intensity are in quantitative agreement with previ-
in the performance of ERA5 at representing rarer local ous studies, although these studies were not condi-
wind and precipitation extremes within ETCs. The sea- tioned to cyclone events and were focused on different
sonal variation of error metrics mostly remains continentalregions(e.g.,Bandhaueretal.,2022;Lavers
unchanged when different percentiles are used (except etal.,2022;Leietal.,2022;Singhetal.,2021).Leietal.
for NMSE for PR98 and PR99). The error is more sensi- (2022) showed that the applicability of ERA5 increases
tive to different percentiles for precipitation extremes with the precipitation amount and hence ERA5 exhi-
than for wind speed extremes. For example, the change bits a better ability to estimate extreme precipitation in
ofannualNMBfrom95thto99thpercentilesisabout6% rainythannon-rainyseasonsinChina.Suchresultsare
(from −16.4% to −21.9%) for wind and 30% (from −6.5% contrary to our findings as we find the best seasonal
to −37.7%) for precipitation. This is partially related to performance in DJF when ETCs over North America
thestructuraldisparityinthetailsofthedistributionsfor are characterized by relatively low precipitation due to
both variables, as extreme precipitation values increase low moisture content. Interestingly, our PRavg bias
more sharply than wind speed values given the same map prevailed by relatively strong negative values in
incrementinpercentiles. JJAbearssomeresemblancetoLaversetal.(2022,their
fig. 2) even though their evaluation was not exclusive
to cyclones. Based on the gauged-based precipitation,
4.3 | Comparison with previous studies theynotedthatwhilewetbiasesforthemeandailypre-
cipitationaremorecommonoverNorthAmerica,there
Our findings regarding ERA5's good performance in the is a notable dry bias over the central United States in
spatially-averaged 10-m wind speeds but a systematic July, which they suggested to be related to the model's
underestimation at moderate and strong intensities are in uncertainty in irrigation and soil moisture content.
general agreement with previous studies evaluating ERA5 Overall, our results are consistent with Lavers et al.
against the buoy and satellite data over the ocean (2022) that the capability of ERA5 precipitation in the
(e.g.,Çalıs¸ıretal.,2023;Camposetal.,2022).Camposetal. Northern Hemisphere extratropics reduces from winter
(2022)reportedanunderestimationofthelong-termmean tosummer.
wind speed by 10%–15% conditioned on the presence of
cyclones over the central and western North Atlantic. The
valueiscomparabletoourestimationof17%underestima- 5 | CONCLUSION
tion based on the annual-mean, ETC-associated WSavg
over the continental North America, although slightly This study provides a novel and comprehensive evalua-
smaller. Our results are somewhat contrary to those of tion of the ability of ERA5 reanalysis at representing the
Molina et al. (2021), who examined the monthly 10-m 10-m wind speed and hourly precipitation associated
wind speed betweenERA5 and station data acrossEurope with ETCs over North America. Hourly data collected
without pre-conditioning on ETCs. They showed that from approximately 3000 stations, amounting to around
ERA5 tends to overestimate higher wind speeds in cold 420 million reports stored in the ISD, serve as the refer-
months and that ERA5 exhibits a better performance in ence dataset. To ensure a fair comparison, ERA5 grid
summer months. The differences from our results may be points are masked out where and when ISD data were
relatedto that the reanalysis performance varies for differ- not available, and additional quality control and time
enttimescales(e.g.,Tanetal.,2017),geographicalregions resampling are also employed on ISD to be consistent
and meteorological conditions (e.g., Campos et al., 2022). with the regularly-gridded hourly ERA5 data. Such post-
Nevertheless, Molina et al.'s (2021) examination using the processed ISD data has been made publicly available to
hourly ERA5 data at the worst-performing stations agrees facilitate future studies (Collet et al., 2022). We use an
thatERA5tendstooverestimatelightwindsandunderesti- objective algorithm to identify and track ETCs, and two
mate strong winds, a well-known feature in reanalysis quantities are computed for each identified cyclone cen-
datasets (e.g., Cannon et al., 2015). Ourbias mapsare also tre: a spatial average and a spatial extreme (the spatial
in line with previous works, showing that reanalysis 95th, 98th and 99th percentiles) within a radius of
products tend to severely underestimate near-surface wind 1000km.
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

 10970088, 2024, 3, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 744 |     |     |     |     |     |     |     |     |     |     |     |     | CHENETAL. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
In terms of the spatial means around cyclones cen- ETCs suggests that such applications should be per-
tres, it is shown that ERA5 is able to represent the 10-m formedwithcaution.
windspeedswell,withanannualnormalizedbias(NMB;
ERA5-ISD) and root-mean-square error (NRMSE) of AUTHOR CONTRIBUTIONS
|     | −0.7% |     |     |     |     |     |     |     |     | –   |     |     | –   |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
about and 14%, and a correlation coefficient Ting-Chen Chen: Writing original draft; writing
(CC) of 0.92. Despite good overall performance, ERA5 reviewand editing; investigation;supervision; validation;
–
consistently overestimates low wind speeds and under- methodology. François Collet: Writing original draft;
estimates high wind speeds. For precipitation, an overall writing–reviewandediting;datacuration;investigation;
underestimation tendency is observed (except for DJF). formal analysis; methodology; visualization; validation.
TheperformanceofERA5ispoorerforprecipitationthan Alejandro Di Luca: Conceptualization; funding acquisi-
for wind speed in all seasons, with NMB and NRMSE tion;writing–reviewandediting;projectadministration;
−10%
increasing their magnitudes to and 57%, respec- resources; supervision; investigation; methodology;
| tively,  | and | the CC dropping |     | to 0.87.    | Such      | a result is | validation. |     |     |     |     |     |     |
| -------- | --- | --------------- | --- | ----------- | --------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- |
| expected | as  | precipitation   | is  | notoriously | difficult | to prop-    |             |     |     |     |     |     |     |
erly represent in models and reanalysis products, owing ACKNOWLEDGEMENTS
to its nonlinear multiscale nature and its dependency on This research has been conducted as part of the project
|     |     |     |     |     |     |     | “Simulation |     |     |     |     | résolution” |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | ----------- | --- |
parameterized processes (Tapiador et al., 2019). For both et analyse du climate à haute
variables, ERA5 usually exhibits the best and the worst funded by the Government of Québec. A. Di Luca was
performance during DJF and JJA, respectively, likely also funded by the Natural Sciences and Engineering
related to the inadequacy of coarse-resolution models to Research Council of Canada (NSERC) grant (RGPIN-
simulate convective processes,which are more dominant 2020-05631). The authors would like to thank Katja
during summer and less active in winter months. As Winger,FrançoisRobergeandFrédérikToupinformain-
for the spatial distribution, negative biases are often taining a user-friendly local computing facility and for
observed over regions with stronger ETC-associated pre- downloading and preparing some of the precipitation
| cipitation/wind |             | speeds,     | which | are           | generally | distributed    | datasets. |     |     |     |     |     |     |
| --------------- | ----------- | ----------- | ----- | ------------- | --------- | -------------- | --------- | --- | --- | --- | --- | --- | --- |
| on              | the central | and eastern |       | North America |           | for precipita- |           |     |     |     |     |     |     |
tion, and near Rockies and northeastern North America DATA AVAILABILITY STATEMENT
(entrance of maritime storm tracks) for wind speed. In The data we post-process in this study have been
addition, systematic underestimation in wind speed also archived as North America ISD to ERA5 (NA-ISD2ERA)
prevailsovercomplextopography. Catalogue and made available on the Borealis data
Theevaluationforthetop5%extremecyclonecentres repository (Collet et al., 2022). The observational station
based on the spatial means of wind speed/precipitation data, NOAA Integrated Surface Database (ISD) was
show a clear skill degradation of ERA5 compared to its accessed from https://registry.opendata.aws/noaa-isd.
performance for the entire sample of ETCs. For wind TheERA5reanalysisisfreelyavailableontheCopernicus
−0.7%
speed, the magnitude of NMB increases from to Data Store (CDS) at https://cds.climate.copernicus.eu/
−10% and the CC reduces from 0.9 to 0.7. For precipita- cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview
tion, ERA5's skill deteriorates even more with the NMB (Hersbachetal.,2020).
| changes                                        | from | −10% to | −23% | and CC | drops | from 0.9 to |       |     |     |     |     |     |     |
| ---------------------------------------------- | ---- | ------- | ---- | ------ | ----- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
| 0.3.ForthespatialextremeswithinanETC,ERA5shows |      |         |      |        |       |             | ORCID |     |     |     |     |     |     |
anevenstrongertendencytounderestimatethelocalized Ting-ChenChen https://orcid.org/0000-0001-9254-2314
extreme values than presenting the spatial means of FrançoisCollet https://orcid.org/0009-0000-9110-817X
| extreme             | ETCs, | and all | error | metrics | increases | at higher |            |     |     |     |     |     |     |
| ------------------- | ----- | ------- | ----- | ------- | --------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
| spatialpercentiles. |       |         |       |         |           |           | REFERENCES |     |     |     |     |     |     |
Our results highlight some important limitations of Arsenault, R., Brissette, F., Martel, J.L., Martel, J.L., Troin, M.,
theERA5reanalysisproductsforstudieslookingatpossi- Lévesque, G. et al. (2020) A comprehensive, multisource
ble impacts of ETCs. ERA5 is in general more reliable in database for hydrometeorological modeling of 14,425 North
|     |     |     |     |     |     |     | American | watersheds. | Scientific | Data, | 7,  | 243. Available | from: |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---------- | ----- | --- | -------------- | ----- |
presentingETC-associated10-mwindspeedthanprecipi-
tation. An overall higher skill in DJFlends confidencein https://doi.org/10.1038/s41597-020-00583-2
|     |       |             |              |     |              |         | Bandhauer, | M., Isotta, | F., Lakatos, | M., | Lussana, | C., Båserud, | L., |
| --- | ----- | ----------- | ------------ | --- | ------------ | ------- | ---------- | ----------- | ------------ | --- | -------- | ------------ | --- |
| the | usage | of ERA5 for | representing |     | the averaged | impacts |            |             |              |     |          |              |     |
Izs(cid:1)ak,B.etal.(2022)Evaluationofdailyprecipitationanalyses
| ofwintertime |             | ETCs,while |     | thelower      | skill | inJJA suggests |            |          |             |               |     |               |         |
| ------------ | ----------- | ---------- | --- | ------------- | ----- | -------------- | ---------- | -------- | ----------- | ------------- | --- | ------------- | ------- |
|              |             |            |     |               |       |                | in E-OBS   | (v19.0e) | and ERA5    | by comparison |     | to regional   | high-   |
| that         | uncertainty | should     | not | be overlooked |       | when investi-  |            |          |             |               |     |               |         |
|              |             |            |     |               |       |                | resolution | datasets | in European | regions.      |     | International | Journal |
gating summer events with ERA5. The deteriorated per- ofClimatology,42(2),727–747.Availablefrom:https://doi.org/
formance of ERA5 in representing local extremes within 10.1002/joc.7269

CHENETAL. 745
Bauer, M. & Del Genio, A.D. (2006) Composite analysis of winter Forest Meteorology, 301–302, 108350. Available from: https://
cyclonesinaGCM:influenceonclimatologicalhumidity.Jour- doi.org/10.1016/j.agrformet.2021.108350
nal of Climate, 19, 1652–1672. Available from: https://doi.org/ Collet,F.,DiLuca,A.&Chen,T.-C.(2022)NorthAmericaISDto
10.1175/JCLI3690.1 ERA5 (NA-ISD2ERA) Catalogue. https://doi.org/10.5683/SP3/
Booth,J.F.,Naud,C.M.&Willison,J.(2018)Evaluationofextratro- LWMGRM
picalcycloneprecipitationintheNorthAtlanticbasin:ananal- Copernicus Climate Change Service, Climate Data Store. (2023)
ysisofERA-interim,WRF,andtwoCMIP5models.Journalof ERA5hourlydataonsinglelevelsfrom1940topresent.Coperni-
Climate, 31(6), 2345–2360. Available from: https://doi.org/10. cus Climate Change Service (C3S) Climate Data Store (CDS).
1175/JCLI-D-17-0308.1 https://doi.org/10.24381/cds.adbb2d47
Booth,J.F.,Rieder,H.E.,Lee,D.E.&Kushnir,Y.(2015)Thepaths DiLuca,A.,deElia,R.,Bador,M.&Argüeso,D.(2020)Contribu-
ofextratropicalcyclonesassociatedwithwintertimehigh-wind tion of mean climate to hot temperature extremes for present
events in the Northeastern United States. Journal of Applied and future climates. Weather and Climate Extremes, 28, 1–13.
Meteorology and Climatology, 54, 1871–1885. Available from: Availablefrom:https://doi.org/10.1016/j.wace.2020.100255
https://doi.org/10.1175/JAMC-D-14-0320.1 Di Luca, A., Evans, J.P., Pepler, A., Alexander, L. & Argüeso, D.
Brune,S.,Keller,J.D.&Wahl, S.(2021)Evaluationofwindspeed (2015) Resolution sensitivity of cyclone climatology over East-
estimatesinreanalysesforwindenergyapplications.Advances ernAustraliausingsixreanalysisproducts.JournalofClimate,
in Science and Research, 18, 115–126. Available from: https:// 28,9530–9549.Availablefrom:https://doi.org/10.1175/JCLI-D-
doi.org/10.5194/asr-18-115-2021 14-00645.1
Çalıs¸ır, E., Soran, M.B. & Akpınar, A. (2023) Quality of the ERA5 Environnement et Changement Climatique Canada. (2021) Manuel
andCFSRwindsandtheircontributiontowavemodellingper- desnormesd'observationsmétéorologiquesdesurface(MANOBS).
formanceinasemi-closedsea.JournalofOperationalOceanog- Available from https://www.canada.ca/fr/environnement-
raphy, 16(2), 106–130. Available from: https://doi.org/10.1080/ changement-climatique/services/manuels-documents-conditions-
1755876X.2021.1911126 meteorologiques/manobs-observations-surface.html#toc0
Campos, R.M., Gramcianinov, C.B., de Camargo, R. & da Silva European Centre for Medium-Range Weather Forecasts. (2016)
Dias,P.L.(2022)AssessmentandcalibrationofERA5severe IFS documentation CY41R2—part IV: physical processes.
winds in the Atlantic Ocean using satellite data. Remote In: IFS documentation CY41R2. Reading, UK: ECMWF. Avail-
Sensing, 14, 4918. Available from: https://doi.org/10.3390/ ablefrom:https://doi.org/10.21957/tr5rv27xu
rs14194918 Feser, F., Barcikowska, M., Krueger, O., Schenk, F., Weisse, R. &
Cannon, D.,Brayshaw,D., Methven,J., Coker,P.&Lenaghan,D. Xia, L. (2015) Storminess over the North Atlantic and north-
(2015) Using reanalysis data to quantify extreme wind power westernEurope—areview.QuarterlyJournaloftheRoyalMete-
generation statistics: a 33 year case study in Great Britain. orologicalSociety,141,350–382.Availablefrom:https://doi.org/
RenewableEnergy,75,767–778.Availablefrom:https://doi.org/ 10.1002/qj.2364
10.1016/j.renene.2014.10.024 Field,P.R. & Wood, R. (2007)Precipitation andcloud structure in
Catto, J.L., Ackerley, D., Booth, J.F., Champion, A.J., Colle, B.A., midlatitudecyclones.JournalofClimate,20(2),233–254.Avail-
Pfahl, S. et al. (2019) The future of midlatitude cyclones. Cur- ablefrom:https://doi.org/10.1175/JCLI3998.1
rent Climate Change Reports, 5, 407–420. Available from: Government of Canada. (2020) Canada's top 10 weather stories of
https://doi.org/10.1007/s40641-019-00149-4 2019.Available from:https://www.canada.ca/en/environment-
Catto,J.L.,Shaffrey,L.C.&Hodges,K.I.(2010)Canclimatemodels climate-change/services/top-ten-weather-stories/2019.html#toc8
capture the structure of extratropical cyclones? Journal of Cli- [Accessed7thOctober2023].
mate, 23(7), 1621–1635. Available from: https://doi.org/10. Gualtieri, G. (2022) Analysing the uncertainties of reanalysis data
1175/2009JCLI3318.1 usedforwindresourceassessment:acriticalreview.Renewable
Chartrand,J.&Pausata,F.S.R.(2020)ImpactsoftheNorthAtlantic and Sustainable Energy Reviews, 167, 112741. Available from:
oscillation on winter precipitations and storm track variability https://doi.org/10.1016/j.rser.2022.112741
inSoutheastCanadaandtheNortheastUnitedStates.Weather Hawcroft, M.K., Shaffrey, L.C., Hodges, K.I. & Dacre, H.F. (2012)
and Climate Dynamics, 1(2), 731–744. Available from: https:// How much northern hemisphere precipitation is associated
doi.org/10.5194/wcd-1-731-2020 with extratropical cyclones? Geophysical Research Letters,
Chen,C.&Knutson,T.(2008)Ontheverificationandcomparison 39(24),L24809.Availablefrom:10.1029/2012GL053866
ofextremerainfallindicesfromclimatemodels.JournalofCli- Hénin, R., Ramos, A.M., Pinto, J.G. & Liberato, M.L.R. (2021) A
mate, 21, 1605–1621. Available from: https://doi.org/10.1175/ ranking of concurrent precipitation and wind events for the
2007JCLI1494.1 Iberian Peninsula. International Journal of Climatology, 41,
Chen,T.-C.,DiLuca,A.,Winger,K.,Laprise,R.&Thériault,J.M. 1421–1437.Availablefrom:https://doi.org/10.1002/joc.6829
(2022) Seasonality of continental extratropical-cyclone wind Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Hor(cid:1)anyi, A.,
speedsovernortheasternNorthAmerica.GeophysicalResearch Muñoz-Sabater, J. et al. (2020) The ERA5 global reanalysis.
Letters,49(15),e2022GL098776.Availablefrom:https://doi.org/ Quarterly Journalof theRoyal Meteorological Society,146(730),
10.1029/2022GL098776 1999–2049.Availablefrom:https://doi.org/10.1002/qj.3803
Chu, H., Luo, X., Ouyang,Z., Chan, W.S., Dengel, S., Biraud, S.C. Hodges, K.I., Lee, R.W. & Bengtsson, L. (2011) A comparison
et al. (2021) Representativeness of Eddy-covariance flux foot- of extratropical cyclones in recent reanalyses ERA-interim,
prints for areas surrounding AmeriFlux sites. Agricultural and NASA MERRA, NCEP CFSR, and JRA-25. Journal of Climate,
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
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

746 CHENETAL.
24(18), 4888–4906. Available from: https://doi.org/10.1175/2011JC Climatology, 57, 991–1009. Available from: https://doi.org/10.
LI4097.1 1175/JAMC-D-17-0289.1
Hoskins, B.J. (1990) Theory of extratropical cyclones. In: Naud,C.M.,Jeyaratnam,J.,Booth,J.F.,Zhao,M.&Gettelman,A.
Newton,C.W.&Holopainen,E.O.(Eds.)Extratropicalcyclones. (2020)Evaluationofmodeledprecipitationinoceanicextratro-
Boston,MA:AmericanMeteorologicalSociety.Availablefrom: pical cyclones using IMERG. Journal of Climate, 33, 95–113.
https://doi.org/10.1007/978-1-944970-33-8_5 Availablefrom:https://doi.org/10.1175/JCLI-D-19-0369.1
Insurance Bureau of Canada. (2019) Halloween storm across Eastern Nelson, B.R., Prat, O.P., Seo, D. & Habib, E. (2016) Assessment
Canada caused over $250 million in insured damage. Available andimplicationsofNCEPstageIVquantitativeprecipitation
from: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/ estimates for product intercomparisons. Weather and Fore-
https://bac-quebec.qc.ca/media/5487/20191210_press-release_ casting, 31, 371–394. Available from: 10.1175/WAF-D-14-
nr-eastern-canada-fall-storms.pdf[Accessed7thOctober2023]. 00112.1
Jeyaratnam,J.,Booth,J.F.,Naud,C.M.,Luo,Z.J.&Homeyer,C.R. Neu,U.,Akperov,M.G.,Bellenbaum,N.,Benestad,R.,Blender,R.,
(2020) Upright convection in extratropical cyclones: a survey Caballero,R.etal.(2013)Imilast:acommunityefforttointer-
usingground-basedradardataovertheUnitedStates.Geophys- compare extratropical cyclone detection and tracking algo-
ical Research Letters, 47, e2019GL086620. Available from: rithms. Bulletin of the American Meteorological Society, 94(4),
https://doi.org/10.1029/2019GL086620 529–547. Available from: https://doi.org/10.1175/BAMS-D-11-
Jiao, D., Xu, N., Yang, F. & Xu, K. (2021) Evaluation of spatial- 00154.1
temporal variation performance of ERA5 precipitation data in NOAA(1998)Automated Surface ObservingSystem: User’s guide.
China. Scientific Reports, 11(1), 17956. Available from: https:// National Oceanic andAtmospheric Administration Doc.,61 pp.
doi.org/10.1038/s41598-021-97432-y Available at: https://www.weather.gov/media/asos/aum-toc.
Jiménez, P.A., García-Bustamante, E., Gonz(cid:1)alez-Rouco, J.F., pdf[Accessed:7thDecember2023].
Valero, F., Mont(cid:1)avez, J.P. & Navarro, J. (2008) Surface wind NOAA-National Centers for Environmental Information. (2018)
regionalizationincomplexterrain.JournalofAppliedMeteorol- Federalclimatecomplexdatadocumentationforintegratedsur-
ogy and Climatology, 47, 308–325. Available from: https://doi. face data (ISD). Available from: https://www.ncei.noaa.gov/
org/10.1175/2007JAMC1483.1 data/global-hourly/doc/isd-format-document.pdf
Kunkel, K.E., Easterling, D.R., Kristovich, D.A.R., Gleason, B., Owen, L.E., Catto, J.L., Stephenson, D.B. & Dunstone, N.J. (2021)
Stoecker, L. & Smith, R. (2012) Meteorological causes of the Compound precipitation and wind extremes over Europe and
secular variations in observed extreme precipitation events for their relationship to extratropical cyclones. Weather and Cli-
the conterminous United States. Journal of Hydrometeorology, mate Extremes, 33, 100342. Available from: https://doi.org/10.
13,1131–1141.Availablefrom:10.1175/JHM-D-11-0108.1 1016/j.wace.2021.100342
Lavers,D.A.,Simmons,A.,Vamborg,F.&Rodwell,M.J.(2022)An Peña-Arancibia, J.L., van Dijk, A.I.J.M., Renzullo, L.J. &
evaluationofERA5precipitationforclimatemonitoring.Quar- Mulligan, M. (2013) Evaluation of precipitation estimation
terlyJournaloftheRoyalMeteorologicalSociety,148(748),3124– accuracy in reanalyses, satellite products, and an ensemble
3137.Availablefrom:https://doi.org/10.1002/qj.4351 methodforregionsinAustraliaandsouthandEastAsia.Jour-
Lei, X., Xu, W., Chen, S., Yu, T., Hu, Z., Zhang, M. et al. (2022) nal of Hydrometeorology, 14(4), 1323–1333 https://journals.
How well does the ERA5 reanalysis capture the extreme cli- ametsoc.org/view/journals/hydr/14/4/jhm-d-12-0132_1.xml
mateeventsoverChina?PartI:extremeprecipitation.Frontiers Pepler,A.,DiLuca,A.&Evans,J.P.(2018)Independentlyassessing
in Environmental Science, 10, 921658. Available from: https:// the representation of midlatitude cyclones in high-resolution
doi.org/10.3389/fenvs.2022.921658 reanalysesusingsatelliteobservedwinds.InternationalJournal
Lin,Y.&Mitchell,K.E.(2005)TheNCEPstageII/IVhourlyprecip- of Climatology, 38, 1314–1327. Available from: https://doi.org/
itation analyses: development and applications. In: Preprints. 10.1002/joc.5245
19thconferenceonhydrology.SanDiego,CA:AmericanMeteo- Petterssen,S.&Smebye,S.J.(1971)Onthedevelopmentofextratro-
rologicalSociety.Availablefrom:https://ams.confex.com/ams/ pical cyclones. Quarterly Journal of the Royal Meteorological
pdfpapers/83847.pdf Society,97,457–482.
Lott,J.N.(2004)Thequalitycontroloftheintegratedsurfacehourly Plante, M., Son, S.W., Atallah, E., Gyakum, J. & Grise, K. (2015)
database.Seattle,WA:AmericanMeteorologicalSociety. ExtratropicalcycloneclimatologyacrosseasternCanada.Inter-
Minola, L., Zhang, F., Azorin-Molina, C., Pirooz, A.A.S., national Journal of Climatology, 35(10), 2759–2776. Available
Flay,R.G.J.,Hersbach,H.etal.(2020)Near-surfacemeanand from:https://doi.org/10.1002/joc.4170
gustwindspeedsinERA5acrossSweden:towardsanimproved Poan,E.D.,Gachon,P.,Laprise,R.,Aider,R.&Dueymes,G.(2018)
gust parametrization. Climate Dynamics, 55(3–4), 887–907. Investigatingaddedvalueofregionalclimatemodelinginnorth
Availablefrom:https://doi.org/10.1007/s00382-020-05302-6 American winter storm track simulations. Climate Dynamics,
Molina, M.O., Gutiérrez, C. & S(cid:1)anchez, E. (2021) Comparison of 50(5–6), 1799–1818. Available from: https://doi.org/10.1007/
ERA5 surface wind speed climatologies over Europe with s00382-017-3723-9
observationsfromtheHadISDdataset.InternationalJournalof Reitan, C.H. (1974) Frequencies of Cyclones and Cyclogenesis for
Climatology,41(10),4864–4878.Availablefrom:https://doi.org/ NorthAmerica,1951–1970.MonthlyWeatherReview,102,861–
10.1002/joc.7103 868. Available from: https://doi.org/10.1175/1520-0493(1974)
Naud,C.M.,Booth,J.F.,Lebsock,M.&Grecu,M.(2018)Observa- 102<0861:FOCACF>2.0.CO;2
tionalconstraintforprecipitationinextratropicalcyclones:sen- Rudeva,I.&Gulev,S.K.(2011)CompositeanalysisofNorthAtlan-
sitivity to data sources. Journal of Applied Meteorology and tic extratropical cyclones in NCEP–NCAR reanalysis data.
10970088,
2024,
3,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339
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
[10/03/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on Wiley
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

 10970088, 2024, 3, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.8339 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| CHENETAL. |     |     |     |     |     |     |     |     | 747 |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Monthly Weather Review, 139, 1419–1446. Available from: Uccellini,L.W. (1990)Processes contributing totherapiddevelop-
https://doi.org/10.1175/2010MWR3294.1 ment of extratropical cyclones. In: Newton, C.W. &
Sandu,I.,Zadra,A.&Wedi,N.(n.d.)Impactoforographicdragon Holopainen, E.O. (Eds.) Extratropical Cyclones. Boston, MA:
forecast skill. Available from: https://www.ecmwf.int/en/ American Meteorological Society. Available from: https://doi.
newsletter/150/meteorology/impact-orographic-drag-forecast- org/10.1007/978-1-944970-33-8_6
skill[Accessed29thAugust2022]. Vaisala. (2020) Wind sensor WM30 for mobile applications.
Serreze,M.C.,Lynch,A.H.&Clark,M.P.(2001)TheArcticfrontal Available from: https://www.vaisala.com/sites/default/files/
zone as seen in the NCEP–NCAR reanalysis. Journal of Cli- documents/WM30-datasheet-B210384EN.pdf [Accessed: 3rd
1550–1567.
| mate, | 14(7), |     | Available | from: https://doi.org/10. |     | November2023]. |     |     |     |
| ----- | ------ | --- | --------- | ------------------------- | --- | -------------- | --- | --- | --- |
1175/1520-0442(2001)014<1550:TAFZAS>2.0.CO;2 Vaisala.(2021)RaingaugeQMR101andQMR101.Availablefrom:
Simmonds,I.&Keay,K.(2000)Meansouthernhemisphereextra- https://www.vaisala.com/sites/default/files/documents/QMR101-
tropicalcyclonebehaviorinthe40-yearNCEP–NCARreanaly-
|     |     |     |     |     |     | QMR101M-Datasheet-B211713EN.pdf[Accessed: |     | 3rd | November |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | -------- |
sis.JournalofClimate,13,873–885.Availablefrom:https://doi.
2023].
org/10.1175/1520-0442(2000)013<0873:MSHECB>2.0.CO;2 Wang,X.L.,Feng,Y.,Chan,R.&Isaac,V.(2016)Inter-comparison
Sinclair, V.A., Rantanen, M., Haapanala, P., Räisänen, J. & of extra-tropical cyclone activity in nine reanalysis datasets.
133–153.
Järvinen, H. (2020) The characteristics and structure of extra- Atmospheric Research, 181, Available from: https://
tropical cyclones in a warmer climate. Weather and Climate doi.org/10.1016/j.atmosres.2016.06.010
Dynamics, 1(1), 1–25. Available from: https://doi.org/10.5194/ Wang, X.L., Swail, V.R. & Zwiers, F.W. (2006) Climatology and
wcd-1-1-2020 changes of extratropical cyclone activity: comparison of
Singh,T.,Saha,U.,Prasad,V.S.&Gupta,M.D.(2021)Assessment ERA-40 with NCEP–NCAR reanalysis for 1958–2001. Journal
ofnewly-developedhighresolutionreanalyses(IMDAA,NGFS of Climate, 19, 3145–3166. Available from: https://doi.org/10.
| and | ERA5) against | rainfall | observations | for Indian | region. | 1175/JCLI3781.1 |     |     |     |
| --- | ------------- | -------- | ------------ | ---------- | ------- | --------------- | --- | --- | --- |
AtmosphericResearch,259,105679.Availablefrom:https://doi. Zappa,G.,Shaffrey,L.C.&Hodges,K.I.(2013)TheabilityofCMIP5
org/10.1016/j.atmosres.2021.105679 modelstosimulateNorthAtlanticextratropicalcyclones.Journal
Smith, A., Lott, N. & Vose, R. (2011) The integrated surface data- ofClimate,26,5379–5396.
| base:    | recent developments |     | and partnerships. | Bulletin           | of the |     |     |     |     |
| -------- | ------------------- | --- | ----------------- | ------------------ | ------ | --- | --- | --- | --- |
| American | Meteorological      |     | Society, 92(6),   | 704–708. Available |        |     |     |     |     |
from:https://doi.org/10.1175/2011BAMS3015.1 SUPPORTING INFORMATION
|            |             |             |          |                     |     | Additional supporting | information | can be found | online |
| ---------- | ----------- | ----------- | -------- | ------------------- | --- | --------------------- | ----------- | ------------ | ------ |
| Sorteberg, | A. & Walsh, | J.E. (2008) | Seasonal | cyclone variability | at  |                       |             |              |        |
70(cid:3)N
and its impact on moisture transport into the Arctic. in the Supporting Information section at the end of this
TellusA,60,570–586.Availablefrom:https://doi.org/10.1111/j.
article.
1600-0870.2008.00314.x
| Tan, J., Petersen, | W.A., | Kirstetter, | P.-E. | & Tian, Y. (2017) | Perfor- |     |     |     |     |
| ------------------ | ----- | ----------- | ----- | ----------------- | ------- | --- | --- | --- | --- |
manceofIMERGasafunctionofspatiotemporalscale.Journal Howtocitethisarticle:Chen,T.-C.,Collet,F.,&
| of Hydrometeorology, |     | 18, 307–319. | Available | from: https://doi. |     |     |     |     |     |
| -------------------- | --- | ------------ | --------- | ------------------ | --- | --- | --- | --- | --- |
DiLuca,A.(2024).EvaluationofERA5precipitation
org/10.1175/JHM-D-16-0174.1 and10-mwindspeedassociatedwithextratropical
Tapiador,F.J.,Roca,R.,DelGenio,A.,Dewitte,B.,Petersen,W.&
cyclonesusingstationdataoverNorthAmerica.
| Zhang, | F. (2019) | Is precipitation | a good | metric for model | per- |     |     |     |     |
| ------ | --------- | ---------------- | ------ | ---------------- | ---- | --- | --- | --- | --- |
InternationalJournalofClimatology,44(3),729–747.
formance?BulletinoftheAmericanMeteorologicalSociety,100,
https://doi.org/10.1002/joc.8339
| 223–233. | Available | from: | https://doi.org/10.1175/BAMS-D-17- |     |     |     |     |     |     |
| -------- | --------- | ----- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
0218.1