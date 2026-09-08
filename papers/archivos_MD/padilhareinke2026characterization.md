Wiley
Advances in Meteorology
Volume 2026, Article ID 9965323, 21 pages
https://doi.org/10.1155/adme/9965323
Research Article
Characterization and Variability of Extratropical
Cyclones in the Southwest Atlantic Ocean
Carina Klug Padilha Reinke ,1,2 Jeferson Prietsch Machado ,1 André Lopes Brum ,1
JoséLuizLimadeAzevedo ,1MauricioMagalhãesMata ,1andJaciMariaBilhalvaSaraiva 1
1OceanologyPostgraduateProgram,InstituteofOceanography,FederalUniversityofRioGrande,Av.ItaliaKm8,Carreiros,
RioGrande96203–900,RioGrandedoSul,Brazil
2CentreforMeteorologicalResearch,FederalUniversityofPelotas,CampusCapaodoLeao,CapaodoLeao96160–000,
RioGrandedoSul,Brazil
CorrespondenceshouldbeaddressedtoCarinaKlug PadilhaReinke;carina.padilha@ufpel.edu.br
Received13May2024;Revised23October2025;Accepted7November2025
AcademicEditor:PramitaMishra
Copyright©2026CarinaKlugPadilhaReinkeetal.AdvancesinMeteorologypublishedbyJohnWiley&SonsLtd.Thisisanopen
accessarticleunderthetermsoftheCreativeCommonsAttributionLicense,whichpermitsuse,distributionandreproductionin
anymedium,providedtheoriginalworkisproperlycited.
Extratropicalcyclonesarekeyfeaturesthatcontributetochangesinprecipitation,wind,andtemperatureatmidlatitudes,sometimes
causing extreme conditions. Despite the southwest Atlantic Ocean being recognized for cyclone formation and intensification,
severalaspectsofspatialandtemporalvariabilityremainunclear.Hence,inthisstudy,theoverallcharacteristicsofcyclonesthat
formwithinthesouthwestAtlanticOceanareinvestigated.Wealsoanalyzetheinterannualvariabilityinthefrequencyofcyclone
occurrencesacrosseachseason.Toaccomplishthis,weuseadatasetfromthehourlyfifthgenerationofglobalclimatereanalysis
fromtheEuropeanCentreforMediumRangeWeatherForecasts(ERA5/ECMWF)spanning41years.Theresultsrevealedincreased
interannualvariability,whichfitwithacubicregressionfortheentirestudyarea,aswellasforthenorthernandsouthernpartsofthe
area,dividedbythe35°Slatitude.Seasonally,wefoundapositivetrendof1.7perdecadeincycloneoccurrenceforthesouthernpart
oftheareaduringsummer,withastatisticalsignificanceof95%.TheFourieranalysisrevealedanenergypeakat2–3yearsinthe
northernpartduringwinter,aswellasintheentireareaduringspring,summer,andautumn.Additionally,importantpeaksatthe5-
year,6-year,and8–10-yearperiodswereobserved.Moreover,weinvestigatedextremeeventsandfoundthatthoseselectedbythe
minimumsealevelpressurearemoreconcentratedsouthofintenseeventsby10-mwinds.Thecompositesofmeteorologicalfields
during intense cyclones thatformednearthecoastal area suggest thatthe equatorialentrance oftheupper-level jetstream is a
preferentialconditionforthedevelopmentofintenseevents.Inaddition,ouranalysisrevealedtheimportanceofawide-ranging
meridionalmovingtroughintheupperandmiddleleveltroposphereandtherelevanceofmoisturetransportviathenorthwestlow-
leveljetfromthetropicstothecoastalarea,whichinducesintensecyclonesinthesouthwesternAtlanticregion.
Keywords:
extratropicalcyclones;interannualvariability;SouthwestAtlanticOcean
1. Introduction scale, extratropical cyclones are a key factor in midlatitude
atmospheric circulation because of their ability to transport
Weatherchangesatmidlatitudesareoftencontrolledbythe
heat,moisture,andmomentum(e.g., [6,7]).Severalstudies
migration of extratropical cyclones and fronts [1]. These have focused on understanding the climate characteristics,
eventsinduceheavyprecipitation,eventuallycausingfloods,
trends, and variability of cyclones from a local perspective
strong surface winds, wind gusts, storm surges, and marine (e.g., [8, 9]). Moreover, recent studies have analyzed the
storminess (e.g., [2]). In coastal areas, intense extratropical response of cyclones to a warmer environment, with
cyclones can cause large-amplitude waves and abrupt the goal of anticipating future changes in extratropical
changes in the coastal landscape (e.g., [3–5]). At the global cyclone frequency (e.g., [7, 10–12]).

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2   |     |     |     |     |     |     |     |     |     |     |     | Advances | inMeteorology |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --- |
To objectively identify extratropical cyclones in large of locations of extratropical cyclones. As outlined by Catto
datasets, many studies have developed automatic detection etal.[12],adecreaseincyclonefrequencycouldberelatedto
andtrackingschemesongriddedmapsusingreanalysisand changes in baroclinicity and a poleward shift in the upper-
intensified
global model data. Thus, many results were found from the level polar stream jet, which can contribute to
different datasets and different measures of cyclone activity precipitation patterns. Nevertheless, it is imperative to con-
[13].Raibleetal.[14]appliedthreedifferentalgorithmstothe duct more thorough regional assessments of these changes.
samedatasetandhighlightedthatatrendanalysisofcyclone Reboita et al. [30, 31], using the Regional Climate Model
significant
characteristicscanbesensitivetothechoiceofcyclonedetec- version 4 (RegCM4) [32], reported a statistically
tion and tracking schemes. To address the main results of decreaseincyclonefrequencytowardtheendofthecentury
differentmethodsinauniqueset-up,severalinstitutionscre- across thesouthwestern Atlantic Ocean.
atedtheIntercomparisonofMidLatitudeStormDiagnostics This study aims to provide a comprehensive characteri-
project(IMILAST)[15,16].Theyconcludedthatthechoiceof zationofextratropicalcycloneswithinthesouthwestAtlantic
|     |     |     |     |     |     |     |     | Ocean, | with a | specific | focus | on investigating |     | their interan- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------- | ----- | ---------------- | --- | -------------- | --- |
algorithmappliedwillsetthecount,lifetime,andintensityof
thecyclones.However,deepcyclonesandthelargestlifecycle nualvariabilityintermsoffrequencyandseasonalpatterns.
areconsistentamongthedifferentmethodologies,andthereis To understand the dynamics of intense cyclonic events, we
|     |     |     |     |     |     |     |     | analyze | annual | cyclone | counts | for four | decades | spanning |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------- | ------ | -------- | ------- | -------- | --- |
goodagreementbetweentheinterannualvariabilityandgeo-
from1982to2022.Additionally,wepresentcompositefields
graphicaldistribution.
Many authors have focused on extratropical cyclones ofvarious pressurelevelsduringthepre-andpostcyclogen-
esisphasesofintenseeventsoriginatinginacoastalarea.Our
| that formed | in  | the Southwest |     | Atlantic | Ocean, | especially | on  |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theimpactsonthesoutheastAmericanpopulationandenvi- primarycontributionisimprovingtheunderstandingofthe
ronment.SoutheasternSouthAmericaisamaincyclogenesis variability in extratropical cyclones in the southwestern
defined Atlantic Ocean and their distinct seasonal characteristics in
| area (e.g., | [17,     | 18]).    | Baroclinicity, |         |     | as the   | slope in |                 |     |          |            |     |                    |     |     |
| ----------- | -------- | -------- | -------------- | ------- | --- | -------- | -------- | --------------- | --- | -------- | ---------- | --- | ------------------ | --- | --- |
|             |          |          |                |         |     |          |          | recent decades. |     | We focus | especially | on  | the meteorological |     |     |
| constant    | pressure | surfaces | with           | respect | to  | surfaces | of con-  |                 |     |          |            |     |                    |     |     |
stantdensity[19],isthemainsourceofenergythatresultsin conditions that lead to the development of intense events
synoptic-scale disturbances at midlatitudes [20]. Vera et al. thataffectthecoastalareasofUruguayandsouthernBrazil.
|     |     |     |     |     |     |     |     | The paper | is organized |     | as  | follows: Section | 2   | describes | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | --- | ---------------- | --- | --------- | --- |
[21]analyzedsynoptic-scalewavesoverthecoldseasonand
discovered that cyclonic perturbations display significant data and methodology. Section 3 presents the results and
finally,
modifications over South America at midlatitudes, with discussion, and Section 4 presents our summary
and conclusions.
| lower-level   | perturbations |             | following     |               | the shape | of           | the Andes |         |     |         |     |     |     |     |     |
| ------------- | ------------- | ----------- | ------------- | ------------- | --------- | ------------ | --------- | ------- | --- | ------- | --- | --- | --- | --- | --- |
| Mountains     | and           | upper-level |               | perturbations |           | remaining    | mostly    |         |     |         |     |     |     |     |     |
| unaffected    | when          | moving      | eastward.     |               | Owing     | to this      | misalign- |         |     |         |     |     |     |     |     |
|               |               |             |               |               |           |              |           | 2. Data | and | Methods |     |     |     |     |     |
| ment, cyclone |               | formation   | is suppressed |               | in        | the vicinity | of the    |         |     |         |     |     |     |     |     |
orography and favored on the leeward side, where the per- fifth
|            |         |     |         |            |      |           |      | 2.1. Data. | Data       | from     | the the | hourly          | generation | of     | global |
| ---------- | ------- | --- | ------- | ---------- | ---- | --------- | ---- | ---------- | ---------- | -------- | ------- | --------------- | ---------- | ------ | ------ |
| turbations | acquire | a   | typical | baroclinic | wave | structure | [22, |            |            |          |         |                 |            |        |        |
|            |         |     |         |            |      |           |      | climate    | reanalysis | produced |         | by the European |            | Centre | for    |
23]. Mendes et al. [24] reported that the total displacement MediumRangeWeatherForecasts(ERA5/ECMWF)[33]were
frequency of winter events is better distributed than that of usedinthisstudy.Thedatasethasahorizontalresolutionof31
| other seasons. |     | Crespo | et al. | [25] analyzed |     | cyclogenesis | con- |        |              |        |      |             |     |           |     |
| -------------- | --- | ------ | ------ | ------------- | --- | ------------ | ---- | ------ | ------------ | ------ | ---- | ----------- | --- | --------- | --- |
|                |     |        |        |               |     |              |      | km and | 137 vertical | levels | from | the surface | up  | to ~80km. | In  |
ditionsincentral-easternSouthAmericaandhighlightedthe additiontotheincreasedspatialandtemporalresolutions,ERA5
importance of upper-level potential vorticity streamers and hasimprovedtheassimilationofreprocesseddatasetsandcore
cutoffsforabetterunderstandingofcyclogenesis.Dalanhese
|     |            |     |     |     |     |     |     | dynamics, | compared |           | with previous | generations |     | of ECMWF |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ------------- | ----------- | --- | -------- | --- |
|     | identified |     |     |     |     |     |     |           |          | benefited |               |             |     |          |     |
et al. [26] a low-frequency decade-to-decade see- reanalysis, which our analysis. We used hourly data
sawofleeandcoastalcyclogenesisandrelatedtheoccurrence ofmeansealevelpressure,850hParelativevorticity,and10-m
| of variations | toanomalies |     | in  | ocean | temperature. |     |     |     |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
windfrom1982to2022.Fortheconstructionofextremeevent
The impacts of extratropical cyclones over coastal areas composites,weadditionallyincorporatedzonalandmeridional
havebeenexaminedbyPariseetal.[2]andSimõesetal.[27].
|     |     |     |     |     |     |     |     | winds, geopotential |     |     | height, | air temperature, |     | and relative |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------- | ---------------- | --- | ------------ | --- |
Thesestudieshighlightthecorrelationbetweenmeteorolog- humidityfromthe300,500,700,and850hPapressurelevels.
ical tides and coastal erosion in southern Brazil with the Campos et al. [34] investigated the performance of the
proximity of extratropical cyclones to the coastline. The ERA5reanalysisforrepresentingwindpatternsintheAtlantic
strongwindsgeneratedbythesecyclonescaninducesignifi- Ocean.ThesefindingsrevealedthatERA5ishighlyreliablefor
| cantalterationstothecoastline,contributing |     |     |     |     |     | tocoastalero- |     |           |             |     |          |              |     |        |         |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- | --------- | ----------- | --- | -------- | ------------ | --- | ------ | ------- |
|                                            |     |     |     |     |     |               |     | weak wind | conditions. |     | However, | the accuracy |     | of the | dataset |
sion events and meteorologicaltides. decreases as the wind intensity increases. Despite this, they
Sinclairetal.[7]utilizedAquaplanet[28]simulationsto concludedthatextremewindsarereasonablywellrepresented
| analyze | changes | in cyclone |     | patterns | in a | warmer | environ- |     |     |     |     |     |     |     |     |
| ------- | ------- | ---------- | --- | -------- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
inERA5inextratropicalregionsoftheSouthAtlanticOcean,
ment and reported that the cyclone lifetime did not change suggestingthatreanalysisisavaluabletoolforstudyingextra-
undertheseconditionsandthatthecountofeventsperyear tropicalcyclonesinthearea.Moreover,Erlichetal.[35]com-
decreasedby~3.3%.AccordingtothelatestIntergovernmen- pared ERA5 reanalysis to WindSat polarimetric microwave
tal Panel on Climate Change (IPCC) report [29], there is a radiometer measurements for Southern Hemisphere midlati-
largeuncertaintyintheprojectedfrequenciesandlikelihood tude to high-latitude cyclones and suggested that ERA5

Advances in Meteorology 3
adequatelydeterminescyclonestructurethroughoutlifestages
andisvaluableforcyclonecompositinganalysis. 20°S
2.2. Methods.This study usesa recent Lagrangianapproach
techniquethatunifiesthecycloneidentificationandtracking
process by joining enclosed surface areas that satisfy a 30°S
threshold of −10 −4 s −1 at the 850hPa relative vorticity,
described by Padilha Reinke et al. [36]. Severalstudies have
employed other thresholds for this parameter. For example,
Hoskins and Hodges [37] utilized a threshold of 10
−5
s
−1, 40°S
whereasReboitaetal.[30]optedfor−1.5×10 −5s −1toiden-
tifycyclones.However,accordingtoCrawfordetal.[38],the
inputsettingsforacyclonedetectionandtrackingalgorithm 50°S
mustbereassessedwhenhigher-resolutiondataareused,as
100 km
previoussettingsforcoarserresolutionsmaynotbeoptimal.
To address this, a sensitivity test was conducted by Padilha 70°W 60°W 50°W 40°W 30°W
Reinkeetal.[36],whodemonstratedthatourthresholdwas
adequate for the present study. The identification method FIGURE1:StudyareashowingthesouthernAtlanticOceanandpart
of South America. The boundaries of the red box (gray area) are
was based on Inatsu [39], who applied the connected com-
20°–50°S and 65°–30°W. The purple box (indicating the coastal
ponentlabelingtechnique[40]tojointhesurfaceareasthat
area) has boundaries of 30°–40°S and 45°–60°W. The green line
satisfythethresholdofrelative vorticityandtreatthemasa at35°Sdividestheredboxintotwobands.
unique labeled field. The labeled fieldis identifiedby a geo-
graphicpoint(longitude,latitude)viaasimplecenterofmass
[41].Thislabeledsurfaceareawasrecordedwithitsnumber value than that of the Northern Hemisphere, because there
of grid points and its minimum 850hPa relative vorticity. are more intense cyclones in theformer hemisphere.
The advantage of this method is the easy adjustment of the Anadditionalevaluationofintenseeventsisbasedonthe
parameters and more plentiful outputs than conventional basis of 10-m winds stronger than 84km/h, which are
neighbor point tracking [42]. The cyclone tracking method approximately the 90th percentile of the maximum winds
searches the enclosed independent areas at the following
associatedwiththecyclonesinthearea.Definingathreshold
time frame around a maximum displacement of 150km/h, atwhichextremewindscausedamageinaregioniscertainly
similar to Crawford et al. [38]. We consider a minimum notstraightforward[8].Furthermore,situationsinwhichthe
lifetime of 12h, similar to Gramcianinov [43] and Padilha direction of persistent winds can be more important to
Reinkeetal.[36],toincludeshort-livedsystemswhoseinten-
coastalenvironmentalmodificationthantheirintensityexist.
sitycancausedamageincoastalareas.Atthisstage,alistof In addition, our method naturally restricts weak events
cyclones withtheirrespective positions was generated. because of the strict 850hPa relative vorticity threshold,
The minimum mean sea level pressure and 10-m wind andthe90thpercentileisacommonparameterforidentify-
speedassociatedwitheacheventwereanalyzedwithina3.6 ing extreme events.
latitude/longitude radius to characterize the cyclones and In the first stage, the identification and tracking of the
furtherseparateintenseevents.Analyzingtheintensitychar- cycloneswasperformedfortheentireSouthernHemisphere;
acteristics within this region around the cyclone center is in the second stage, events with at least one point of their
crucial because the maximum wind speed and minimum tracklocatedwithintheinterestareaofthesouthwestAtlan-
sea level pressure often occur near, but not exactly at, the tic Ocean were selected. Figure 1 shows the domain of this
central point defined by the relative vorticity threshold. study, covering latitudes of 20°–50°S and longitudes of
While Laurilla et al. [8] used a radius of 6° to identify 295°–330°E(redbox).Weseparatedtheeventsthatformed
wind gusts associated with events, Flauonas et al. [44] and
northof35°Sfromthosethatformedsouthofthislatitudeto
LimandSimmonds[45]choseavaryingdiskradiusaccord- verifythevariabilityinthenumberofcyclonesrelatedtothe
ing to the intensity and area of relative vorticity within the formationposition(thisdivisionisshowninFigure1viathe
threshold. Our radius follows the study of Padilha Reinke
greenlineat35°Slatitude).ApreviousstudybyGramciani-
et al. [36]. nov et al. [47] also identified differences in the cyclogenesis
Theintenseeventsrelatedtothemeansealevelpressure environmentwhensplittingthedomainatthissamelatitude.
were defined as those in which the mean sea level pressure Their results indicated that the dominant mechanisms vary
waslowerthanthe10thpercentileoftheeventsinthearea, not only with genesis latitude but also seasonally, with dis-
whichresultedin~966hPa.LambertandFyfe[46]ransen- tinct characteristics observed during summer and winter.
sitivitytestsofdifferentthresholdstoidentifyintenseevents Weexaminedtheinterannualvariabilityacrosstheentire
andreportedthatqualitativeresultsarenotparticularlysen- study area, as well as its northern and southern segments.
sitivetothevalueused.Furthermore,theyusedthethreshold Trends were calculated by applying linear andcubic regres-
of 960hPa for the Southern Hemisphere, which is a lower sion models to the time series. Some studies utilize solely
1306,
2026,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[27/01/2026].
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

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 4   |     |     |     |     |     |     |     | Advances | inMeteorology |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
Frequency of cyclogenesis
|      |      | Winter |           |     |      |      |      | Spring |      |     |
| ---- | ---- | ------ | --------- | --- | ---- | ---- | ---- | ------ | ---- | --- |
| 25°S |      |        |           |     | 25°S |      |      |        |      |     |
| 30°S |      |        |           |     | 30°S |      |      |        |      |     |
| 35°S |      |        |           |     | 35°S |      |      |        |      |     |
| 40°S |      |        |           |     | 40°S |      |      |        |      |     |
| 45°S |      |        |           |     | 45°S |      |      |        |      |     |
| 50°S |      |        |           |     | 50°S |      |      |        |      |     |
| 55°S |      |        |           | (A) | 55°S |      |      |        |      | (B) |
|      | 70°W | 60°W   | 50°W 40°W |     |      | 70°W | 60°W | 50°W   | 40°W |     |
|      |      | Summer |           |     |      |      |      | Autumn |      |     |
| 25°S |      |        |           |     | 25°S |      |      |        |      |     |
| 30°S |      |        |           |     | 30°S |      |      |        |      |     |
| 35°S |      |        |           |     | 35°S |      |      |        |      |     |
| 40°S |      |        |           |     | 40°S |      |      |        |      |     |
| 45°S |      |        |           |     | 45°S |      |      |        |      |     |
| 50°S |      |        |           |     | 50°S |      |      |        |      |     |
| 55°S |      |        |           | (C) | 55°S |      |      |        |      | (D) |
|      | 70°W | 60°W   | 50°W 40°W |     |      | 70°W | 60°W | 50°W   | 40°W |     |
|      | 0.5  | 1.0    | 3.0       | 6.0 | 9.0  |      | 12.0 | 15.0   | 18.0 |     |
FIGURE2:SpatialdistributionofsouthwestAtlanticcyclogenesisperseasonfor(A)winter(JJA),(B)spring(SON),(C)summer(DJF),and
(D)autumn(MAM).Thedensityunitiseventsperarea,withaunitareaofasphericalcapof106km2.
linear regression; however, the rationale for employing a technique mathematically formulated by Gilman et al. [53]
more complex model, such as cubic regression, is used to and an F-test of the significance distribution related to red
achieveamorerefinedadjustment[48,49].Cubicregression
|     |     |     |     |     | noise. | Twenty | realizations | of the power spectrum |     | were per- |
| --- | --- | --- | --- | --- | ------ | ------ | ------------ | --------------------- | --- | --------- |
providesasuperiorfitbycapturingnonlinearpatterns,thus formedto enhance the major peaks and remove noise [54].
enhancing predictive accuracy through its ability to accom- Wealsoexaminedthecharacteristicsofthestreamlines,
modatecurvatureandmultipleinflectionpoints.Thestatis-
geopotentialheight,airtemperatureandrelativehumidityat
tical significance was determined via a t-test and the 300,500,700,and850hPa,whichrepresenttheupper,mid-
Mann–Kendalltest[50]wasimplementedinboththenorth- dle,andlower-levelsofthetroposphere,respectively,bycre-
atingspatial–temporalevolutionofcompositesoftheintense
| ern and | southern | regions for | each season, to assess | the sig- |     |     |     |     |     |     |
| ------- | -------- | ----------- | ---------------------- | -------- | --- | --- | --- | --- | --- | --- |
nificance of the trends [51]. To accurately identify periodic extratropicalcyclonesthatweregeneratedinthecoastalarea,
oscillationsinthetimeseries,weconductedaFourieranaly- as indicated by the purple box in Figure 1. The maps are
significance
sis (e.g., [52]). To ascertain the of the power presented from 24h before to 12h after cyclogenesis. These
spectrum peaks, we utilized red noise analysis, with a maps contribute to a better understanding of the

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances | in Meteorology |      |           |     |      |      |      |        |      | 5   |
| -------- | -------------- | ---- | --------- | --- | ---- | ---- | ---- | ------ | ---- | --- |
|          |                |      | Winter    |     |      |      |      | Spring |      |     |
| 25°S     |                |      |           |     | 25°S |      |      |        |      |     |
| 30°S     |                |      |           |     | 30°S |      |      |        |      |     |
| 35°S     |                |      |           |     | 35°S |      |      |        |      |     |
| 40°S     |                |      |           |     | 40°S |      |      |        |      |     |
| 45°S     |                |      |           |     | 45°S |      |      |        |      |     |
| 50°S     |                |      |           |     | 50°S |      |      |        |      |     |
| 55°S     |                |      |           | (A) | 55°S |      |      |        |      | (B) |
|          | 70°W           | 60°W | 50°W 40°W |     |      | 70°W | 60°W | 50°W   | 40°W |     |
|          |                |      | Summer    |     |      |      |      | Autumn |      |     |
| 25°S     |                |      |           |     | 25°S |      |      |        |      |     |
| 30°S     |                |      |           |     | 30°S |      |      |        |      |     |
| 35°S     |                |      |           |     | 35°S |      |      |        |      |     |
| 40°S     |                |      |           |     | 40°S |      |      |        |      |     |
| 45°S     |                |      |           |     | 45°S |      |      |        |      |     |
| 50°S     |                |      |           |     | 50°S |      |      |        |      |     |
| 55°S     |                |      |           | (C) | 55°S |      |      |        |      | (D) |
|          | 70°W           | 60°W | 50°W 40°W |     |      | 70°W | 60°W | 50°W   | 40°W |     |
|          | 0.5            | 1.0  | 3.0       | 6.0 | 9.0  |      | 12.0 | 15.0   | 18.0 |     |
FIGURE3:SpatialdistributionoftheSouthwestAtlanticatthepositionwheretherelativevorticityat850hPareachesmoreintensevaluesper
seasonfor(A)winter(JJA),(B)spring(SON),(C)summer(DJF),and(D)autumn(MAM).Thedensityunitiseventsperarea,withaunit
areaofasphericalcapof106km2.
|     |     |     |     |     | 30°S | 50°S |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- |
preconditionsoftheformationofintensecoastalextratropi- and presented the greatest seasonal variation in
cal cyclones with respect to pressure and 10-m winds and cyclogenesis frequency on the coast of South America, with
their first hour evolution in thevicinityof the coastal area. more events per season in the winter than in the summer.
|     |     |     |     |     | Autumn | and | spring have | intermediate | values within | this |
| --- | --- | --- | --- | --- | ------ | --- | ----------- | ------------ | ------------- | ---- |
3. Results and Discussion area, with slightly more events occurring in spring. The
|     |     |     |     |     | near    | absence | of cyclogenesis | over the            | western part | of South |
| --- | --- | --- | --- | --- | ------- | ------- | --------------- | ------------------- | ------------ | -------- |
|     |     |     |     |     | America | can     | be explained    | by the modification | of           | the low- |
3.1.SpatialandTemporalDistribution.Thissectionprovides
anoverviewofcyclonesinthesouthwestAtlanticOcean.The level perturbations related to the Andes Mountains range
horizontaldistributionofthecyclogenesisfrequencyforeach (e.g., [21, 23]). Mendes et al. [56] studied the precondition
season is presented in Figure 2. The largest frequency of fortheformationofextratropicalcyclonesinSouthAmerica
cyclogenesisandcyclonetracksintheSouthernHemisphere andreportedthattheAndesMountainsseemtoplayadual
isbetween50°Sand70°S,becauseofthelargebaroclinicityin role: warm and moist airis channeledfrom the tropics into
that region (e.g., [6, 37, 55]). However, the region between the mid-latitudes, and interactions with upper-level

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 6   |     |              |     |     |     | Advances          | inMeteorology |
| --- | --- | ------------ | --- | --- | --- | ----------------- | ------------- |
|     |     | Duration (%) |     |     |     | Mean velocity (%) |               |
50%
25.0%
| 40%           |     |     |     | 20.0%         |     |     |     |
| ------------- | --- | --- | --- | ------------- | --- | --- | --- |
| )%( ycneuqerF |     |     |     | )%( ycneuqerF |     |     |     |
30%
15.0%
| 20% |     |     |     | 10.0% |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- |
10%
5.0%
| 0%  |     |                      |     | 0.0% |                            |                      |              |
| --- | --- | -------------------- | --- | ---- | -------------------------- | -------------------- | ------------ |
|     | 1 2 | 3 4                  | 5 6 | 7    | 20 30 40                   | 50 60                | 70 80 90 100 |
|     |     | Lifetime (days)      |     |      |                            | Mean velocity (km/h) |              |
|     |     | ðAÞ                  |     |      |                            | ðBÞ                  |              |
|     |     | Minimum pressure (%) |     |      | Maximum 10 meters wind (%) |                      |              |
35.0%
25.0%
30.0%
| 20.0%         |     |     |     | 25.0%         |     |     |     |
| ------------- | --- | --- | --- | ------------- | --- | --- | --- |
| )%( ycneuqerF |     |     |     | )%( ycneuqerF |     |     |     |
| 15.0%         |     |     |     | 20.0%         |     |     |     |
15.0%
10.0%
10.0%
| 5.0% |     |     |     | 5.0% |     |     |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- |
| 0.0% |     |     |     | 0.0% |     |     |     |
930 940 950 960 970 980 990 1000 1100 30 40 50 60 70 80 90 100 110
|     |     | Minimum pressure (hPa) |     |     | Maximum 10 meters wind (m/s) |     |     |
| --- | --- | ---------------------- | --- | --- | ---------------------------- | --- | --- |
|     |     | ðCÞ                    |     |     |                              | ðDÞ |     |
FIGURE 4: Frequency distributions of (A) duration (days), (B) mean velocity (km/h), (C) minimum sea level pressure (hPa), and (D)
maximum10-meterwinds(km/h)foreachextratropicalcycloneintheSouthwestAtlanticOcean.
TABLE1:StatisticalcharacteristicsofextratropicalcyclonesinthesouthwestAtlanticOcean(redboxinFigure1).
Statisticalcharacteristics Mean Median Standarddeviation Percentileofintensity(10%/90%)
111.0(90%)
| Countperyear                 |     |     | 97.1  | 97.0  | 9.9  |     |            |
| ---------------------------- | --- | --- | ----- | ----- | ---- | --- | ---------- |
| Meanvelocity(km/h)           |     |     | 60.1  | 59.9  | 14.0 |     | 78.3(90%)  |
| Minimumsealevelpressure(hPa) |     |     | 984.0 | 985.3 | 13.6 |     | 965.9(10%) |
84.4(90%)
| Maximum10-mwinds(km/h) |     |     | 70.0 | 69.3 | 10.9 |     |     |
| ---------------------- | --- | --- | ---- | ---- | ---- | --- | --- |
undulationsleadtointensificationofcyclogenesisbecauseof that of the more intense period by 59%, 62%, 54%, and
the downstream leeward flow from themountain range. 57% during the summer, autumn, winter, and spring sea-
Followingthemaximumrelativevorticityat850hPafor sons, respectively. These results indicate that extratropical
each extratropical cyclone, we obtained the location where cyclonesintheregiongenerallyreachtheirmaximuminten-
each cyclone is more intense. Figure 3shows thehorizontal sity farther offshore, away from the coastal area. The maxi-
distributionofthelocationwheretheeventsaremoreintense mum position in the open ocean is associated with strong
withrespecttothe850hParelativevorticity.Comparedwith baroclinicityathigherlatitudes,whichagreeswiththeresults
thepanelsofcyclogenesis,thepositionisshiftedfurtheraway of Lim and Simmonds [45]. In a recent study, Dos Santos
from the coast. To assess this, we computed the mean fre- et al. [57] provided an overview of baroclinic instability in
quency of cyclone genesis within a defined coastal region, thesouthern AtlanticOceantocharacterizethestormtrack
delineated by latitudes of 25°S and 40°S, and longitudes of regioninthesouthwesternAtlantic.Theseauthorsreported
| 50°W | 65°W. |     |     |     |     | 40°S | 50°S, |
| ---- | ----- | --- | --- | --- | --- | ---- | ----- |
and The frequency of cyclogenesis exceeded higher values mainly between and similar to our

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances | in Meteorology |     |     | 7   |
| -------- | -------------- | --- | --- | --- |
p.min. < 966 hPa Max. wind > 84 km/h
| 20°S |     |     | 20°S |     |
| ---- | --- | --- | ---- | --- |
| 30°S |     |     | 30°S |     |
| 40°S |     |     | 40°S |     |
| 50°S |     |     | 50°S |     |
| 60°S |     |     | 60°S |     |
|      |     | (A) |      | (B) |
70°W 60°W 50°W 40°W 30°W 20°W 10°W 70°W 60°W 50°W 40°W 30°W 20°W 10°W
Mean velocity > 78 km/h Two intense criteria and fast
| 20°S |     |     | 20°S |     |
| ---- | --- | --- | ---- | --- |
| 30°S |     |     | 30°S |     |
| 40°S |     |     | 40°S |     |
| 50°S |     |     | 50°S |     |
| 60°S |     | (C) | 60°S | (D) |
70°W 60°W 50°W 40°W 30°W 20°W 10°W 70°W 60°W 50°W 40°W 30°W 20°W 10°W
Two intense criteria Two intense criteria and coastal area
| 20°S |     |     | 20°S |     |
| ---- | --- | --- | ---- | --- |
| 30°S |     |     | 30°S |     |
40°S
40°S
| 50°S |     |     | 50°S |     |
| ---- | --- | --- | ---- | --- |
| 60°S |     |     | 60°S |     |
|      |     | (E) |      | (F) |
70°W 60°W 50°W 40°W 30°W 20°W 10°W 70°W 60°W 50°W 40°W 30°W 20°W 10°W
FIGURE5:TracksofintenseeventsinthesouthwestAtlanticOceanonthebasisof:(A)sealevelpressurebelow966hPa,(B)10-mwindabove
84km/h,and(C)meanvelocityabove78km/h.Panel(D)showsintenseeventsonthebasisofthethreecriteria,whilepanel(E)showsintense
eventsonthebasisofcriteria(A)and(B).Finally,panel(F)issimilartopanel(E),butforeventsgeneratedonlyinthepurplebox.Cyclones
generatednorthof35°Sareingreen,andthosegeneratedsouthof35°Sareinblue.Theredpointsrepresentthebeginningofthetrackofeach
event.
intensification
results. According to Wells [58], this preferential zone is explaining the favorable regions of of extra-
calledthebarocliniczoneandisinfluencedbylargemeridi- tropical cyclones. These baroclinic zones can be seen most
fields
onaltopographicbarriers,suchastheAndesMountains,and clearly in the mean over a great number of years, as
thedistributionsofcontinentsandoceans,whichareregions shown in Figure 3. Together, Figures 2 and 3 provide a
of heat sources or sinks, are driven by the cycle of solar comprehensive depiction of the storm-track distributions
radiation over a year. The large horizontal gradient of tem- in the southwest Atlantic Ocean, as well as their seasonal
| perature | produced by this distribution | is crucial for | differences. |     |
| -------- | ----------------------------- | -------------- | ------------ | --- |

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 8   |     |     |     |     |     |     | Advances | inMeteorology |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
Winter—p. min. < 966 hPa Spring—p. min. < 966 hPa Summer—p. min. < 966 hPa Autumn—p. min. < 966 hPa
| 25°S |     | 25°S     |     |     | 25°S |     | 25°S |     |     |
| ---- | --- | -------- | --- | --- | ---- | --- | ---- | --- | --- |
| 30°S |     | 30°S     |     |     | 30°S |     | 30°S |     |     |
| 35°S |     | 35°S     |     |     | 35°S |     | 35°S |     |     |
| 40°S |     | 40°S     |     |     | 40°S |     | 40°S |     |     |
| 45°S |     | 45°S     |     |     | 45°S |     | 45°S |     |     |
| 50°S |     | 50°S     |     |     | 50°S |     | 50°S |     |     |
| 55°S |     | (A) 55°S |     | (B) | 55°S | (C) | 55°S |     | (D) |
70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W
Winter—w. max.  > 84 km/h Spring—w. max.  > 84 km/h Summer—w. max.  > 84 km/h Autumn—w. max.  > 84 km/h
| 25°S |     | 25°S     |     |     | 25°S |     | 25°S |     |     |
| ---- | --- | -------- | --- | --- | ---- | --- | ---- | --- | --- |
| 30°S |     | 30°S     |     |     | 30°S |     | 30°S |     |     |
| 35°S |     | 35°S     |     |     | 35°S |     | 35°S |     |     |
| 40°S |     | 40°S     |     |     | 40°S |     | 40°S |     |     |
| 45°S |     | 45°S     |     |     | 45°S |     | 45°S |     |     |
| 50°S |     | 50°S     |     |     | 50°S |     | 50°S |     |     |
| 55°S |     | (E) 55°S |     | (F) | 55°S | (G) | 55°S |     | (H) |
70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W
| 0.5 |     | 3.0 | 9.0 |     | 15.0 | 21.0 |     | 27.0 |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | ---- | --- |
Frequency of intense events per season
|      | Winter |      | Spring |     | Summer |     |      | Autumn |     |
| ---- | ------ | ---- | ------ | --- | ------ | --- | ---- | ------ | --- |
| 25°S |        | 25°S |        |     | 25°S   |     | 25°S |        |     |
| 30°S |        | 30°S |        |     | 30°S   |     | 30°S |        |     |
| 35°S |        | 35°S |        |     | 35°S   |     | 35°S |        |     |
| 40°S |        | 40°S |        |     | 40°S   |     | 40°S |        |     |
| 45°S |        | 45°S |        |     | 45°S   |     | 45°S |        |     |
| 50°S |        | 50°S |        |     | 50°S   |     | 50°S |        |     |
|      |        | (I)  |        | (J) |        | (K) |      |        | (L) |
| 55°S |        | 55°S |        |     | 55°S   |     | 55°S |        |     |
70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W 70°W60°W50°W40°W30°W
| –15 |     | –9  | –3  |     | 0   | 3   | 9   |     | 15  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Frequency by min. pressure minus frequency by max. wind
(A–D)show,inthe
FIGURE6:Positions wheretheextratropical cyclonesinthesouthwestAtlanticOcean reachhigherintensities. Panels
upperline,thepositionsofintenseeventsperseasonbasedonsealevelpressurebelow966hPa.Panels(E–H)show,inthemiddleline,the
positionsofintenseeventsperseasonbasedon10-mwindsabove84km/h.Panels(I–L)present,inthelowerline,thedifferencesbetweenthe
resultsbasedonthesetwocriteria.
3.2. Storm Characteristics. To address the characteristics of 70km/h.Onaverage,theseresultswerefasterthantheveloc-
extratropical cyclones in the southwestern Atlantic Ocean, ity presented by Padilha Reinke et al. [36] for the Southern
Figure4showshistogramsofthelifetime(Figure4A),mean Hemisphere,withthesamemethodology.Theminimumsea
velocity of displacement (Figure 4B), and maximum inten- levelpressureandthemaximum10-mwindsofthecyclones
sityofextratropicalcyclonesmeasuredbytheminimumsea were effective parameters for evaluating the intensity of
level pressure (Figure 4C) and the maximum 10-m winds extratropical cyclones. They are indirectly related because
(Figure 4D). Approximately 49% of the extratropical low pressure is usually associated with an increase in the
40%
cyclones persisted for 1 day, whereas persisted for pressure gradient, which is associated with stronger winds
2 days. Our methodology employs a stringent threshold for in the low-level troposphere [8]. Both frequency distribu-
|     |     | −4s −1),potentiallyleadingto |     |     |     |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
relativevorticityat850hPa(-10 tions are skewed toward the most intense events, with
the exclusion of certain cyclolysis processes. Consequently, more weight in the right tail of the maximum 10-m winds
findings
our indicate a greater prevalence of short-lived and in theleft tailof the minimum sea level pressure.
eventsthanotherstudies,suchasGramcianinov[59].How- Table 1 shows the statistics of extratropical cyclones in
ever, we focused on events that could result in greater thestudyarea,spanningfrom1982to2022.Onaverage,97.1
impacts for coastal areas and for marine navigation; hence, cyclones were observed yearly, with a standard deviation of
this criterion restricts weak cyclones that cannot produce 9.9 and a 90th percentile of 111.0. The mean velocity of
extreme precipitation and strong winds. The lifetimes of extratropical cyclones is 60.1km/h, with a 90th percentile
cyclones in the southern hemisphere produced with the of 78.3km/h. The fastest event occurred between the 12th
same methodology have similar features, with many short- and 14th of December 2022, with a maximum 10-m wind
lifeevents[36].Withrespecttothemeanvelocity,50%ofthe
|     |     |     |     |     | speed of 82.0km/h | and | a minimum | sea level pressure | of  |
| --- | --- | --- | --- | --- | ----------------- | --- | --------- | ------------------ | --- |
extratropicalcyclonesinthestudyregionarebetween50and 977.5hPa, which is far from the continent but within the

Southwest Atlantic Ocean
1982 1986 1990 1994 1998 2002 2006 2010 2014 2018 2022
Years
raey
rep
tnuoC
120
110
100
90
80
Southwest Atlantic Ocean Linear regression
Cubic regression
ðAÞ
Northern part of the area
1982
raey
rep
tnuoC
20
18
16
14
12
10
8
6
1986 1990 1994 1998 2002 2006 2010 2014 2018 2022
Years
Northern part of SW Atlantic Ocean Linear regression
Cubic regression
ðBÞ
Southern part of the area
80
70
60
1982
raey
rep
tnuoC
Advances in Meteorology 9
100
90
1986 1990 1994 1998 2002 2006 2010 2014 2018 2022
Years
Southern part of SW Atlantic Ocean Linear regression
Cubic regression
ðCÞ
FIGURE7:Annualcountofextratropicalcyclones(blue),withlinearregression(red)andcubicpolynomialregression(purple).Theupper
panel(A)showstheresultsforthesouthwestAtlanticOcean,themiddlepanel(B)forthenorthernpartoftheregion,andthelowerpanel(C)
forthesouthernpartoftheregion.
1306,
2026,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[27/01/2026].
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

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 10  |     |     |     |     |     |     |     |     |     |     |     | Advances | inMeteorology |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
TABLE2:Slopeofthelineartrendsinthe1982–2022period,p-value
| study area. | The | minimum | sea | level | pressure | mean | is 984.0 |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | ----- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
accordingtotheMann–Kendaltestandcoefficientofdetermination
| hPa, and | the maximum |     | 10-m | wind | mean | is 70.0km/h. | The |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ---- | ---- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
(R2)ofextratropicalcyclonesintheoverall,northern,andsouthern
90thpercentileofthemaximum10-mwind(84.4km/h)and
partsofthestudyarea.
the10thpercentileoftheminimummeansealevelpressure
R2
(965.9hPa) shown in the last column of Table 1 serve as Area Mann–Kendallp-value Slope
| benchmarks | for | assessing | more | intense | events | in  | the subse- |           |     |     |      |     |     |           |
| ---------- | --- | --------- | ---- | ------- | ------ | --- | ---------- | --------- | --- | --- | ---- | --- | --- | --------- |
|            |     |           |      |         |        |     |            | Wholearea |     |     | 0.26 |     |     | 0.19 0.05 |
quent subsection. To contextualize these numbers, the Northernpart 0.35 0.04 0.02
coastalerosioneventthataffectedSouthernBrazilinOctober
|                 |            |             |            |          |          |                |          | Southernpart |     |              | 0.33 |                 |     | 0.15 0.03  |
| --------------- | ---------- | ----------- | ---------- | -------- | -------- | -------------- | -------- | ------------ | --- | ------------ | ---- | --------------- | --- | ---------- |
| 2016 was        | associated |             | with a     | cyclone, | with     | maximum        | wind     |              |     |              |      |                 |     |            |
| speeds reaching |            | 79km/h      | and        | minimum  |          | sea level      | pressure |              |     |              |      |                 |     |            |
| of 1000hPa      | in         | the coastal | area,      | as       | detailed | by Albuquerque |          |              |     |              |      |                 |     |            |
|                 |            |             |            |          |          |                |          | enhanced     | in  | the vicinity | of   | the upper-level |     | jet stream |
| et al. [4].     | Therefore, |             | the values | within   |          | the purple     | box in   |              |     |              |      |                 |     |            |
core[60].
Figure1areusedasthemostappropriatecriterionforiden- Therewasacleardecreaseinthenumberofeventsdur-
tifying events with potential coastal impacts. ing austral autumn (Figure 6D,H), and the position of
|     |     |     |     |     |     |     |     | intenseevents |     | inspringwas | slightly | further | from | theconti- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | -------- | ------- | ---- | --------- |
3.3.IntenseEvents.Theintensityofanextratropicalcyclone
|     |     |     |     |     |     |     |     | nent and | at  | latitudes | south | of 45°S. | During | winter |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | ----- | -------- | ------ | ------ |
canbedefinedbyawidevarietyofmeteorologicalvariables.
(Figure6A,E)andsummer(Figure6B,F)moreintenseevents
5A–C
Figure show the tracks of intense extratropical occurrednearthecoast.Figure6I–Lindicatethatsomeofthe
| cyclones | on the | basis | of minimum |     | sea level | pressure | (A), |     |     |     |     |     |     |     |
| -------- | ------ | ----- | ---------- | --- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
intensecasesidentifiedbythepressurecriterionexhibittheir
maximum 10-m winds (B), and faster cyclones (C), respec- most intense periods farther poleward than those identified
| tively, according |           | to  | the percentiles |         | shown        | in  | Table 1.  |             |      |              |       |            |      |               |
| ----------------- | --------- | --- | --------------- | ------- | ------------ | --- | --------- | ----------- | ---- | ------------ | ----- | ---------- | ---- | ------------- |
|                   |           |     |                 |         |              |     |           | by the 10-m | wind | criterion.   | A     | comparison | of   | these results |
| Cyclones          | generated |     | north           | of 35°S | are depicted |     | in green, |             |      |              |       |            |      |               |
|                   |           |     |                 |         |              |     |           | with those  | in   | Figure 5A,B, | where | the whole  | year | tracks are    |
andthosegeneratedtothesoutharedepictedinblue.Atotal presented,suggeststhattheintenseeventsseparatedaccord-
of407intenseeventswereidentifiedonthebasisofmeansea
ingtomaximumwindsaregenerallymoredisplacedtoward
levelpressurecriteria,425eventswereidentifiedonthebasis
theequatorthanintenseeventsseparatedaccordingtomini-
of10-mwindthresholds,and417fasteventswereidentified.
|     |     |     |     |     |     |     |     | mum pressure. |     | This difference |     | may result | from | the distinct |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------- | --- | ---------- | ---- | ------------ |
Intenseeventsonthebasisofsealevelpressureareshiftedto
natureofthevariables,withthesealevelpressurebeingmore
| the south, | and | some | extreme | events | in  | southern | South |           |     |             |         |     |      |               |
| ---------- | --- | ---- | ------- | ------ | --- | -------- | ----- | --------- | --- | ----------- | ------- | --- | ---- | ------------- |
|            |     |      |         |        |     |          |       | extensive | and | persistent, | whereas | the | 10-m | winds are, in |
America are included. Overall, faster events in the area essence, more turbulent. On the other hand, extratropical
| tended to        | form | slightly | away   | from | the continent, |        | indicating |            |          |            |                |         |           |            |
| ---------------- | ---- | -------- | ------ | ---- | -------------- | ------ | ---------- | ---------- | -------- | ---------- | -------------- | ------- | --------- | ---------- |
|                  |      |          |        |      |                |        |            | cyclones   | tend     | to exhibit | lower          | central | pressures | at higher  |
| that occurrences |      | of rapid | events | are  | less           | common | near the   |            |          |            |                |         |           |            |
|                  |      |          |        |      |                |        |            | latitudes, | possibly | due        | to atmospheric |         | dynamics  | associated |
coastline.Thephysicalexplanationforthehigheroccurrence with strong horizontal temperature gradients in the mid-
of fast cyclones over the open ocean is the reduced surface latitudes, which intensify toward the poles within a global
| friction | compared | to  | coastal | regions. | The | tracks | of events |     |     |     |     |     |     |     |
| -------- | -------- | --- | ------- | -------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
context.
| meeting | all three | criteria | display |     | notable | southward | and |     |     |     |     |     |     |     |
| ------- | --------- | -------- | ------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
away-from-the-continent shifts, totaling 56 occurrences 3.4. Interannual Variability. Figure 7 shows the annual
(Figure 5D). There were 166 intense events based simulta- count of extratropical cyclones and the respective linear
| neously | on sea | level | pressure | and | 10-m | wind | criteria |           |            |     |             |        |        |            |
| ------- | ------ | ----- | -------- | --- | ---- | ---- | -------- | --------- | ---------- | --- | ----------- | ------ | ------ | ---------- |
|         |        |       |          |     |      |      |          | and cubic | polynomial |     | regressions | of the | entire | study area |
35°S,
(Figure5E).Tounderstandthebehaviorofintensecyclones (Figure 7A), northern part of the area (north of
thatdevelopnearthecoast,weselectedeventsbetween30°S Figure 7B), and southern part of the area (south of 35°S,
| and 40°S | and | 45°W | and 60°W | longitudes |     | (purple | box in |             |          |       |      |                   |     |             |
| -------- | --- | ---- | -------- | ---------- | --- | ------- | ------ | ----------- | -------- | ----- | ---- | ----------------- | --- | ----------- |
|          |     |      |          |            |     |         |        | Figure 7C). | Overall, | there | is a | large interannual |     | variability |
Figure5F)andcreatedcompositeswithcharacteristicssimi- andaslightincreasingtrendinthethreeregions.Theresults
lar tothose of these extratropical cyclones (see Section 3.5). ofthelinearregressionshowpositiveslopesof0.19,0.04,and
Figure6showsthespatialandtemporaldistributionsof
|     |     |     |     |     |     |     |     | 0.15 for | the entire | area, | northern | part, | and southern | part, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----- | -------- | ----- | ------------ | ----- |
Mann–Kendall
cyclones at positions where they reach higher intensities, respectively. However, according to the test,
separated by season. In general, the most intense position the linear regression has no statistically significant mono-
| oftheeventsagreeswiththeresultsofhigherintensitybased |     |     |     |     |     |     |     |             |     | 90% |       |            |           |          |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ----- | ---------- | --------- | -------- |
|                                                       |     |     |     |     |     |     |     | tonic trend | at  | the | level | (Table 2). | A greater | positive |
on the 850hPa relative vorticity of all the events of the 41- trendisobservedfromthe1980stothe2010susingthecubic
yeardataset(Figure3)andwiththetheoreticaldefinitionof polynomial regression, whereas a negative trend is present
barocliniczones.Thisregion,characterizedbyastrongtem- after 2010. The coefficient of determination of the cubic
perature gradient, favors the development of surface low- polynomialregression was 0.32, 0.13, and 0.22 for thetotal,
pressure systems through the ascent of warm air and the northern, and southern parts of the area, respectively. To
descent of cold air along the boundary between two air better understand the cause of the decreasing trend in the
intensification
masses. The of extratropical cyclones is gov- annualcountofextratropicalcyclonesintheregions,further
ernedbyseveralatmosphericprocesses,includingenhanced investigation into ocean–atmosphere interactions is needed.
horizontal advection, vertical wind shear, and the conver- Changes in sea surface temperature and upper ocean heat
genceofairmassesatthesurfaceordivergenceofairmasses content (UOHC) may provide important insights into this
in the upper troposphere. The latter process is particularly variability. Additionally, large-scale climate modes such as

10.0
7.5
5.0
2.5
1980
theAtlantic multidecadal oscillation (AMO) and thesouth- observed in summer (slope of 0.03 per year) and autumn
ern annular mode (SAM) could be contributing factors. On (slope of 0.02 per year), and an even smaller trend is found
average,thereare97eventsperyearinthewholearea,13in during winter and spring. However, the p-values of the
the northern part, and 83 in the southern part. The largest Mann–Kendall test for allthe seasons are greater than 0.05,
yearly count of extratropical cyclones across the entire area whichsuggeststhatthetrendsarenotsignificantatthe95%
occurred in 2013 (122 events). In 2013, 105 events were level. Using the same test for each season in the southern
observed in the southern part, and in 1999 and 2008, 21 part, only the trend in summer (slope of 0.17 per year) is
events were observed in the northern part. According to significant(95%level).Visually,aslightnegativetrendinthe
Pearson’s correlation, the count of extratropical cyclones cyclone count is observed during the autumn, and a slight
overthetwopartsoftheareahasnosignificantcorrelation, positive trend is observed in the winter. However, these
with a coefficient of −0.14, using the statistical significance trends are not significant according to the Mann–Kendall
level of 95%. test (95%level).
Figure 8 shows the annual count of intense cyclones, Figure10showsthepowerspectrumoftheyearlycount
which is based on the minimum sea level pressure (blue of extratropical cyclones and the associated red noise, with
line), maximum 10-m winds (red line), and higher mean thelinesof99%significanceand95%significancecomputed
velocity(purpleline)criteria.Acomparisonofthevariability viatheF-test.Thereissignificantenergyduringthe2–3year
of these events revealed that the number of intense events period,thatis,duringwinter(inthenorthernpart),summer,
decreased between 1995 and 2000 and increased between spring,andautumn(inbothareas).Thisenergypeakmaybe
2005 and 2010 in the three series. This pattern suggests associated with the El Niño-Southern Oscillation (ENSO),
important interannual variability in the number of intense which is the most prominent mode of internal variability
and fast events in the region. The correlations between fast at interannual time scales and influences the precipitation
events and intense events, according to minimum pressure patterns in the region [61]. Reboita et al. [62] applied the
and 10-m winds, exhibit positive associations. Specifically, MelbourneUniversityautomaticcyclonetrackingschemeto
there is a moderate correlation between intensity as deter- investigate the relationships between extratropical cyclones
minedbyminimumpressureandthatasdeterminedby10- inthesouthAtlanticOceannearthesoutheastcoastofSouth
m winds, whereas there is a strong correlation between fast AmericaandENSOepisodesfrom1980to2012.Theirfind-
and intense events (see the left upper corner ofFigure 8). ingsindicatethatthenumberofcyclonesisgreaterduringEl
In the context of seasonal trends, Figure 9 shows the Niño years (positive phase) and lower during Niña years
annual count and the respective linear regression for each (negative phase) than during neutral periods. The 5-year
season. In the northern part, a slight positive trend is periodpresentanenergypeakduringwinterinthenorthern
raey
rep
tnuoC
Advances in Meteorology 11
Southwest Atlantic Ocean
Intense by pressure and wind p-value: 0.55
20.0 Intense by pressure and fast p-value: 0.73
Intense by wind and fast p-value: 0.81
17.5
15.0
12.5
1984 1988 1992 1996 2000 2004 2008 2012 2016 2020 2024
Years
Intense-pressure Fast
Intense-wind
FIGURE8:AnnualcountofintenseextratropicalcyclonesinthesouthwesternAtlanticOceanbasedontheminimumsealevelpressurebelow
966hPa (blue), maximum 10-m winds above 84km/h (red), and faster events (velocity greater than 78km/h, yellow) criteria. Some
correlationsarepresentedattheupperleftcornerofthefigure.
1306,
2026,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323
by
University
Of
Sao
Paulo
-
Brazil,
Wiley
Online
Library
on
[27/01/2026].
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

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 12  |     |     |     | Advances | inMeteorology |
| --- | --- | --- | --- | -------- | ------------- |
| 12  |     |     | 35  |          |               |
10
30
raey rep tnuoC
raey rep tnuoC 8
25
6
20
4
15
2
| 0         |           |           | 10        |           |           |
| --------- | --------- | --------- | --------- | --------- | --------- |
|           |           |           | 1982 1990 | 1998 2006 | 2014 2022 |
| 1982 1990 | 1998 2006 | 2014 2022 |           |           |           |
Years
Years
Winter—southern part
Winter—northern part
Linear regression
Linear regression
|     | ðAÞ |     |     | ðBÞ |     |
| --- | --- | --- | --- | --- | --- |
| 12  |     |     | 35  |     |     |
10
30
raey rep tnuoC
raey rep tnuoC 8
25
6
20
4
15
2
10
0
|           |           |           | 1982 1990 | 1998 2006 | 2014 2022 |
| --------- | --------- | --------- | --------- | --------- | --------- |
| 1982 1990 | 1998 2006 | 2014 2022 |           |           |           |
Years
Years
Spring—southern part
Spring—northern part
Linear regression
Linear regression
|     | ðCÞ |     |     | ðDÞ |     |
| --- | --- | --- | --- | --- | --- |
| 12  |     |     | 35  |     |     |
| 10  |     |     | 30  |     |     |
raey rep tnuoC
raey rep tnuoC 8
25
6
20
4
15
2
10
0
|           |           |           | 1982 1990 | 1998 2006 | 2014 2022 |
| --------- | --------- | --------- | --------- | --------- | --------- |
| 1982 1990 | 1998 2006 | 2014 2022 |           |           |           |
Years
Years
Summer—southern part
Summer—northern part
Linear regression
Linear regression
|     | ðEÞ |                     |     | ðFÞ |     |
| --- | --- | ------------------- | --- | --- | --- |
|     |     | FIGURE9: Continued. |     |     |     |

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances       | in  | Meteorology |     |     |     |     |     |                |     |     |     |     |     |     | 13  |
| -------------- | --- | ----------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
|                | 12  |             |     |     |     |     |     | 35             |     |     |     |     |     |     |     |
|                | 10  |             |     |     |     |     |     | 30             |     |     |     |     |     |     |     |
| raey rep tnuoC | 8   |             |     |     |     |     |     | raey rep tnuoC |     |     |     |     |     |     |     |
25
6
20
4
15
2
10
0
|     |      |     |      |      |      |     |           |     | 1982 | 1990 | 1998 | 2006 | 2014 | 2022 |     |
| --- | ---- | --- | ---- | ---- | ---- | --- | --------- | --- | ---- | ---- | ---- | ---- | ---- | ---- | --- |
|     | 1982 |     | 1990 | 1998 | 2006 |     | 2014 2022 |     |      |      |      |      |      |      |     |
Years
Years
Autumn—southern part
Autumn—northern part
Linear regression
Linear regression
|     |     |     |     | ðGÞ |     |     |     |     |     |     | ðHÞ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
FIGURE9:Annualcountofextratropicalcyclonesandcorrespondinglinearregressionforthenorthern(A,C,E,G)andsouthern(B,D,F,H)
partsofthestudyarea,shownforwinter(A,B),spring(C,D),summer(E,F),andautumn(G,H).
| part | and during | autumn |     | in the southern |     | part. | A significant |         |      |            |     |            |              |     |      |
| ---- | ---------- | ------ | --- | --------------- | --- | ----- | ------------- | ------- | ---- | ---------- | --- | ---------- | ------------ | --- | ---- |
|      |            |        |     |                 |     |       |               | (Figure | 11A) | at 300hPa. | The | 12h before | cyclogenesis |     | com- |
peakduringthe6-yearperiodisfoundinthewintersouthern posite shows the deepening of the trough (Figure 12B), and
andsummernorthernareas.Decadaloscillationscanbesug- the0hfieldhasamarkeddivergence(notshown)eastofthe
gestedbypeaksat8-to10-yearperiodsoverspringandwin- troughinthewindfield.Theenhancedintensityofthewind
ter. This result aligns with that of Pezzi et al. [63], who velocitysuggeststhat,onaverage,intenseeventsformatthe
identified
connections between southern hemisphere extra- equatorial entrance of the jet, and the displacement of the
tropicalcyclonesanddecadalvariabilityinthePacificOcean.
cycloneisrelatedtothemovingtroughanddisplacementof
The study revealed that during the positive phase of the thejet, which agrees with theresultsof Crespo et al. [25].
oscillation, there were fewer but more intense cyclones, Compositesofthe500hPageopotentialheightandtem-
with a weaker impact observed at lower latitudes during 11E–H)
|     |     |     |     |     |     |     |     | perature | (Figure |     |     | reveal that | the extent |     | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --- | ----------- | ---------- | --- | ------ |
the summer months. However, further analysis should be 20°S 50°S
|     |     |     |     |     |     |     |     | eastward-moving |     | trough | is  | between | and |     | in the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | --- | ------- | --- | --- | ------ |
performed to understand the underlying mechanisms middletroposphere24hbeforeand12hbeforecyclogenesis.
| responsible |     | for these | energy | peaks. |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Mendesetal.[56]studiedtheprecursorsofSouthAmerican
|               |     |                                         |     |     |     |     |     | cyclogenesis |           | and reported | that   | the transient | trough      | coming    |     |
| ------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ------------ | --------- | ------------ | ------ | ------------- | ----------- | --------- | --- |
| 3.5.Composite |     | ofIntenseEvents.Inmeteorology,composite |     |     |     |     |     |              |           |              |        |               |             |           |     |
|               |     |                                         |     |     |     |     |     | from         | the South | Pacific      | in the | middle        | troposphere | generally |     |
analysisisausefultechniquethatcanexpressthebasicstruc-
the40°S–50°Sband.
| tural | characteristics |     | of a | phenomenon. |     | Therefore, | we con- | extends | within |     |     |     |     |     |     |
| ----- | --------------- | --- | ---- | ----------- | --- | ---------- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
11I–L
|          |            |         |       |          |               |     |              |          | Figure    | present | composites |           | of geopotential |        | height, |
| -------- | ---------- | ------- | ----- | -------- | ------------- | --- | ------------ | -------- | --------- | ------- | ---------- | --------- | --------------- | ------ | ------- |
| structed | composites |         | for   | the most | intense       |     | events that  |          |           |         |            |           |                 |        |         |
|          |            |         |       |          |               |     |              | relative | humidity, |         | and wind   | at 700hPa | for             | the 20 | most    |
| impacted | the        | coastal | area, | which    | were selected |     | on the basis |          |           |         |            |           |                 |        |         |
fields
oftheirintensitycriteriaintermsofmeansealevelpressure intense events. These show the interconnection
defined between the incursion of warm, moist tropical air and the
| and                | 10-m winds. | The | coastal  | area                      | is  |     | as the region |             |     |           |         |       |              |     |         |
| ------------------ | ----------- | --- | -------- | ------------------------- | --- | --- | ------------- | ----------- | --- | --------- | ------- | ----- | ------------ | --- | ------- |
|                    |             |     |          |                           |     |     |               | midlatitude |     | transient | trough, | which | is a typical |     | feature |
| withinthepurplebox |             |     | inFigure | 1,locatedbetweenlatitudes |     |     |               |             |     |           |         |       |              |     |         |
30°–40°S and longitudes 45°–60°W. Table 3 shows the observed in intense events by Garreoud and Wallace [65]
|             |     |        |               |     |          |      |            | and | Mendes | et al. [56]. | According | to  | these authors, |     | strong |
| ----------- | --- | ------ | ------------- | --- | -------- | ---- | ---------- | --- | ------ | ------------ | --------- | --- | -------------- | --- | ------ |
| description |     | of the | extratropical |     | cyclones | that | evolved in |     |        |              |           |     |                |     |        |
andhumidnorthwesterlywindscanfavortheintensification
thisanalysis.Manyintenseeventsinthewinterareexpected,
([66–69])
since surface baroclinicity is strongest in the cold season. of cyclogenesis. Other studies emphasize the role
Figure 11 shows the spatiotemporal evolution of composite of this low-level jet asa key conduit for moisture transport,
|             |     |             |     |        |        |       |            | which | in turn | modulates |     | South American |     | precipitation. |     |
| ----------- | --- | ----------- | --- | ------ | ------ | ----- | ---------- | ----- | ------- | --------- | --- | -------------- | --- | -------------- | --- |
| atmospheric |     | circulation | 24h | before | to 12h | after | the cyclo- |       |         |           |     |                |     |                |     |
genesis of the 20 most intense winter events in the coastal Additionally, Figure 11 shows the transport of humidity
areas of southern Brazil and Uruguay (purple box in from the tropics toward the coastal area during the cyclone
formationandintensificationstages,atthe850hPafields.As
Figure1).Whileeffective,apotentialdrawbackofthecom-
positetechniqueisthatitsuppressescase-by-casevariability thecyclonemoveseastward,thisconnectionwiththeconti-
and may smooth out the individual characteristics of each nentaltransportofmoisturefromthetropicsisinterrupted,
andtheprocessesofocean–atmosphereinteractionsbecome
| event | (e.g., [64]). |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thecompositeof24hbeforecyclogenesisshowsamov- moreimportant[70].Anexpectedpatternistheinclination
ing trough aligned with the western part of South America of the cyclonic disturbance between the upper and lower
| centered | near | 70°W, |     | stretching | from | 20°S | to 50°S | troposphere. |     |     |     |     |     |     |     |
| -------- | ---- | ----- | --- | ---------- | ---- | ---- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 14   |                      |      |     | Advances             | inMeteorology |
| ---- | -------------------- | ---- | --- | -------------------- | ------------- |
|      | Winter—northern part |      |     | Winter—southern part |               |
| 0.20 |                      | 0.20 |     |                      |               |
murtceps rewop dezilamroN murtceps rewop dezilamroN
| 0.15      |                      | 0.15     |           |                      |          |
| --------- | -------------------- | -------- | --------- | -------------------- | -------- |
| 0.10      |                      | 0.10     |           |                      |          |
| 0.05      |                      | 0.05     |           |                      |          |
| 0.00      |                      | 0.00     |           |                      |          |
| 2 4 6     | 8 10 12              | 14 16 18 | 2 4 6     | 8 10 12              | 14 16 18 |
|           | Period (years)       |          |           | Period (years)       |          |
| Spectrum  | 95% confidence       |          | Spectrum  | 95% confidence       |          |
| Red-noise | 99% confidence       |          | Red-noise | 99% confidence       |          |
|           | ðAÞ                  |          |           | ðBÞ                  |          |
|           | Spring—northern part |          |           | Spring—southern part |          |
| 0.20      |                      | 0.20     |           |                      |          |
murtceps rewop dezilamroN murtceps rewop dezilamroN
| 0.15      |                      | 0.15     |           |                      |          |
| --------- | -------------------- | -------- | --------- | -------------------- | -------- |
| 0.10      |                      | 0.10     |           |                      |          |
| 0.05      |                      | 0.05     |           |                      |          |
| 0.00      |                      | 0.00     |           |                      |          |
| 2 4 6     | 8 10 12              | 14 16 18 | 2 4 6     | 8 10 12              | 14 16 18 |
|           | Period (years)       |          |           | Period (years)       |          |
| Spectrum  | 95% confidence       |          | Spectrum  | 95% confidence       |          |
| Red-noise | 99% confidence       |          | Red-noise | 99% confidence       |          |
|           | ðCÞ                  |          |           | ðDÞ                  |          |
|           | Summer—northern part |          |           | Summer—southern part |          |
| 0.20      |                      | 0.20     |           |                      |          |
murtceps rewop dezilamroN murtceps rewop dezilamroN
| 0.15      |                | 0.15     |           |                |          |
| --------- | -------------- | -------- | --------- | -------------- | -------- |
| 0.10      |                | 0.10     |           |                |          |
| 0.05      |                | 0.05     |           |                |          |
| 0.00      |                | 0.00     |           |                |          |
| 2 4 6     | 8 10 12        | 14 16 18 | 2 4 6     | 8 10 12        | 14 16 18 |
|           | Period (years) |          |           | Period (years) |          |
| Spectrum  | 95% confidence |          | Spectrum  | 95% confidence |          |
| Red-noise | 99% confidence |          | Red-noise | 99% confidence |          |
|           | ðEÞ            |          |           | ðFÞ            |          |
FIGURE10: Continued.

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances                  | in Meteorology |                      |                |     |       |                           |           |     |                      |                |     | 15    |
| ------------------------- | -------------- | -------------------- | -------------- | --- | ----- | ------------------------- | --------- | --- | -------------------- | -------------- | --- | ----- |
|                           |                | Autumn—northern part |                |     |       |                           |           |     | Autumn—southern part |                |     |       |
| 0.20                      |                |                      |                |     |       | 0.20                      |           |     |                      |                |     |       |
| murtceps rewop dezilamroN |                |                      |                |     |       | murtceps rewop dezilamroN |           |     |                      |                |     |       |
| 0.15                      |                |                      |                |     |       | 0.15                      |           |     |                      |                |     |       |
| 0.10                      |                |                      |                |     |       | 0.10                      |           |     |                      |                |     |       |
| 0.05                      |                |                      |                |     |       | 0.05                      |           |     |                      |                |     |       |
| 0.00                      |                |                      |                |     |       | 0.00                      |           |     |                      |                |     |       |
|                           | 2 4 6          | 8                    | 10 12          | 14  | 16 18 |                           | 2         | 4 6 | 8                    | 10 12          | 14  | 16 18 |
|                           |                | Period (years)       |                |     |       |                           |           |     | Period (years)       |                |     |       |
|                           | Spectrum       |                      | 95% confidence |     |       |                           | Spectrum  |     |                      | 95% confidence |     |       |
|                           | Red-noise      |                      | 99% confidence |     |       |                           | Red-noise |     |                      | 99% confidence |     |       |
|                           |                | ðGÞ                  |                |     |       |                           |           |     | ðHÞ                  |                |     |       |
FIGURE10:Normalizedpowerspectrumofextratropicalcyclonecount(blue)with20realizations,red-noisefit(red),andFtestconfidence
levelsof95%(orange)and99%(purple)forthenorthern(A,C,EandG)andsouthern(B,D,FandH)partsofthestudyarea.Theresultsare
presentedforthewinter(A,B),spring(C,D),summer(E,F),andautumn(G,H)seasonsfromtoptobottom.
TABLE3:The20mostintenseextratropicalcycloneswithcyclogenesisunderthecoastalarea(purpleboxofFigure1).
Winter Firstdate Minpressure Maxwind Summer Firstdate Minpressure Maxwind
| 1   | June4,1983   |     | 952.9  | 84.93  |     | 1   | January17,1990  |     |     | 984.27 |     | 82.88 |
| --- | ------------ | --- | ------ | ------ | --- | --- | --------------- | --- | --- | ------ | --- | ----- |
| 2   | June26,1984  |     | 965.33 | 96.79  |     | 2   | December11,1990 |     |     | 960.99 |     | 93.81 |
| 3   | June8,1990   |     | 958.35 | 88.61  |     | 3   | January17,1993  |     |     | 976.19 |     | 99.99 |
| 4   | June3,1991   |     | 957.5  | 98.51  |     | 4   | February16,1994 |     |     | 966.88 |     | 82.66 |
| 5   | June19,1991  |     | 966.16 | 90.88  |     | 5   | February10,1997 |     |     | 990.64 |     | 85.06 |
| 6   | June5,1992   |     | 953.5  | 113.21 |     | 6   | February19,1997 |     |     | 980.25 |     | 86.76 |
| 7   | July18,1992  |     | 968.68 | 95.88  |     | 7   | February2,1999  |     |     | 973.29 |     | 95.88 |
| 8   | June26,1994  |     | 960.85 | 80.6   |     | 8   | January31,2002  |     |     | 967.01 |     | 90.88 |
| 9   | June14,2001  |     | 967.69 | 87.93  |     | 9   | December9,2003  |     |     | 962.91 |     | 90.82 |
| 10  | July20,2001  |     | 969.43 | 90.07  |     | 10  | February1,2005  |     |     | 989.04 |     | 78.03 |
| 11  | June10,2002  |     | 943.68 | 102.48 |     | 11  | December26,2006 |     |     | 990.43 |     | 81.82 |
| 12  | June18,2002  |     | 963.39 | 93.3   |     | 12  | February23,2009 |     |     | 988.48 |     | 83.9  |
| 13  | June23,2007  |     | 954.77 | 82.46  |     | 13  | December12,2009 |     |     | 985.19 |     | 82.17 |
| 14  | July23,2007  |     | 965.49 | 94.08  |     | 14  | January19,2010  |     |     | 977.02 |     | 87.57 |
| 15  | July25,2010  |     | 968.64 | 91.28  |     | 15  | January14,2015  |     |     | 992.09 |     | 81.42 |
| 16  | July25,2016  |     | 959.84 | 94.76  |     | 16  | February5,2017  |     |     | 990.98 |     | 82.03 |
| 17  | June30,2020  |     | 969.59 | 97.1   |     | 17  | January7,2019   |     |     | 983.31 |     | 79.41 |
| 18  | July8,2020   |     | 969.08 | 91.53  |     | 18  | January11,2019  |     |     | 989.06 |     | 86.97 |
| 19  | August9,2021 |     | 967.13 | 80.47  |     | 19  | December15,2019 |     |     | 970.57 |     | 87.59 |
| 20  | July16,2022  |     | 959.84 | 94.76  |     | 20  | December21,2019 |     |     | 989,00 |     | 82.59 |
Figure 12 shows the same fields for the 20 most intense expected to be driven by more intense upper troposphere
| summer | events. These characteristics |     | aresimilartothose |     | of  | conditions. |     |     |     |     |     |     |
| ------ | ----------------------------- | --- | ----------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Figure11;however,theintensityofthestreamjetat300hPa Althoughindividualcasesmayexhibitdistinctcharacter-
is less pronounced. The mean atmosphere state of the sub- istics, the composite analysis of the most intense events
tropicsinthewinterexplainstheintensification,considering intensification
|     |     |     |     |     |     | reveals | common | factors | that | favor the |     | of  |
| --- | --- | --- | --- | --- | --- | ------- | ------ | ------- | ---- | --------- | --- | --- |
only intense events in the winter. The energy transport by cyclonic vorticity: (1) the positioning of the subtropical jet
Hadley is weaker during the winter hemisphere, which at upper levels of the troposphere, with mass divergence
amplified
enhances baroclinicity in the subtropics and facilitates aligned with the region of interest; (2) an trough
cyclonic formation. Thus, an intense event in the winter is atmiddlelevelsofthetropospheretotheeastoftheregion;

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 16  |     |     |     |     |     | Advances | inMeteorology |     |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
300 hPa—24 h before 300 hPa—12 h before 300 hPa—0 h before 300 hPa—12 h after
70
| 20°S | 20°S |     | 20°S |     | 20°S |     |     | 65  |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
)s/m( edutingam dniW
60
| 25°S | 25°S |     | 25°S |     | 25°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
55
| 30°S | 30°S |     | 30°S |     | 30°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
50
| 35°S | 35°S |     | 35°S |     | 35°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
45
| 40°S | 40°S |     | 40°S |     | 40°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
40
| 45°S | 45°S |     | 45°S |     | 45°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
|      | (A)  |     | (B)  |     | (C)  |     | (D) | 35  |
| 50°S | 50°S |     | 50°S |     | 50°S |     |     |     |
30
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
500 hPa—24 h before 500 hPa—12 h before 500 hPa—0 h before 500 hPa—12 h after 276
| 20°S | 20°S |     | 20°S |     | 20°S |     |     | 270 |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
| 25°S | 25°S |     | 25°S |     | 25°S |     |     | 264 |
)K( erutarepmeT
258
| 30°S | 30°S |     | 30°S |     | 30°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
252
| 35°S | 35°S |     | 35°S |     | 35°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
246
| 40°S | 40°S |     | 40°S |     | 40°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
| 45°S | 45°S |     | 45°S |     | 45°S |     |     | 240 |
|      | (E)  |     | (F)  |     | (G)  |     | (H) | 234 |
| 50°S | 50°S |     | 50°S |     | 50°S |     |     |     |
228
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
700 hPa—24 h before 700 hPa—12 h before 700 hPa—0 h before 700 hPa—12 h after
95
| 20°S | 20°S |     | 20°S |     | 20°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
90
)%( ytidimuh evitaleR
| 25°S | 25°S |     | 25°S |     | 25°S |     |     | 85  |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
| 30°S | 30°S |     | 30°S |     | 30°S |     |     | 80  |
| 35°S | 35°S |     | 35°S |     | 35°S |     |     |     |
75
| 40°S | 40°S |     | 40°S |     | 40°S |     |     | 70  |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
| 45°S | 45°S |     | 45°S |     | 45°S |     |     | 65  |
|      | (I)  |     | (J)  |     | (K)  |     | (L) |     |
| 50°S | 50°S |     | 50°S |     | 50°S |     |     |     |
60
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
850 hPa—24 h before 850 hPa—12 h before 850 hPa—0 h before 850 hPa—12 h after
95
| 20°S | 20°S |     | 20°S |     | 20°S |     |     |                          |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | ------------------------ |
|      |      |     |      |     |      |     |     | 90 )%( ytidimuh evitaleR |
| 25°S | 25°S |     | 25°S |     | 25°S |     |     |                          |
| 30°S | 30°S |     | 30°S |     | 30°S |     |     | 85                       |
| 35°S | 35°S |     | 35°S |     | 35°S |     |     |                          |
80
| 40°S | 40°S |     | 40°S |     | 40°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
75
| 45°S | 45°S |     | 45°S |     | 45°S |     |     |     |
| ---- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
|      | (M)  |     | (N)  |     | (O)  |     | (P) |     |
| 50°S | 50°S |     | 50°S |     | 50°S |     |     |     |
70
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
FIGURE11:Compositesofthe20mostintensewinterevents24hbefore(A,E,I,andM),12hbefore(B,F,J,andN),at(C,G,K,andO)and12
hafter(D,H,L,andP)cyclogenesis.(A–D)300hPastreamlines,colorshadingmagnitudeabove60m/s,(E–H)500hPageopotentialheight
(dams)andairtemperature(K),(I–L)700hPawind(barb),geopotentialheight(dams)andrelativehumidity,shadingmagnitudeabove60%
and(M–P)850hPawind(barb),geopotentialheight(dams)andrelativehumidity,shadingmagnitudeabove70%.
influenced
and (3) the advection of warm, moist air from the tropical which is by the Andes Mountains. The most
regions of South America at lower levels. These conditions favorable region for the intensification of extratropical
collectively create an environment of instability and cyclones shifted to the ocean, which is consistent with the
intensifica-
enhanced baroclinicity, which contribute to the barocliniczoneconcept.Thefrequencydistributionrevealed
tion of events. that, compared with events in the entire Southern Hemi-
|     |     |     |     | sphere, Atlantic | Ocean events | were faster, | on average. | Eval- |
| --- | --- | --- | --- | ---------------- | ------------ | ------------ | ----------- | ----- |
4. Summary and Conclusions uating the intensity of the events, the 10th percentile of the
|     |     |     |     | minimum mean | sea level | pressure was | ~966hPa, | and the |
| --- | --- | --- | --- | ------------ | --------- | ------------ | -------- | ------- |
This study investigates the characteristics of extratropical 90th percentile of the maximum 10-m wind speed was
| cyclones intheSouthwestAtlanticOcean, |     | focusingontheir |     | ~84km/h. |     |     |     |     |
| ------------------------------------- | --- | --------------- | --- | -------- | --- | --- | --- | --- |
Theintenseeventswithrespecttotheminimumsealevel
| interannual variability. | Special attention | is given | to the for- |     |     |     |     |     |
| ------------------------ | ----------------- | -------- | ----------- | --- | --- | --- | --- | --- |
35°S
mation positions related to the latitude, as well as pressure are farther south than the intense events with
cyclone intensity. respecttothemaximum 10-mwinds. Incontrast, thefaster
The spatial distribution revealed the most favorable eventsareshiftedfarfromthecontinent.Withrespecttothe
regionofcyclogenesis intheeasternpartofSouthAmerica, intenseeventsonthebasisofthetwovariablesandthefaster

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances | in Meteorology |     |     |     |     |     |     |     |     |     | 17  |
| -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
300 hPa—24 h before 300 hPa—12 h before 300 hPa—0 h before 300 hPa—12 h after
70
| 20°S |     |     | 20°S |     | 20°S |     |     |      |     |     | 65                   |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | -------------------- |
|      |     |     |      |     |      |     |     | 20°S |     |     | )s/m( edutingam dniW |
60
| 25°S |     |     | 25°S |     | 25°S |     |     | 25°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
55
| 30°S |     |     | 30°S |     | 30°S |     |     | 30°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
50
| 35°S |     |     | 35°S |     | 35°S |     |     | 35°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
45
| 40°S |     |     | 40°S |     | 40°S |     |     | 40°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
40
| 45°S |     |     | 45°S |     | 45°S |     |     | 45°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|      |     | (A) |      | (B) |      |     | (C) |      |     | (D) | 35  |
| 50°S |     |     | 50°S |     | 50°S |     |     | 50°S |     |     |     |
30
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
500 hPa—24 h before 500 hPa—12 h before 500 hPa—0 h before 500 hPa—12 h after
276
| 20°S |     |     | 20°S |     | 20°S |     |     | 20°S |     |     | 270 |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
264
| 25°S |     |     | 25°S |     | 25°S |     |     | 25°S |     |     | )K( erutarepmeT |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --------------- |
| 30°S |     |     | 30°S |     | 30°S |     |     | 30°S |     |     | 258             |
| 35°S |     |     | 35°S |     | 35°S |     |     | 35°S |     |     | 252             |
246
| 40°S |     |     | 40°S |     | 40°S |     |     | 40°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
240
| 45°S |     |     | 45°S |     | 45°S |     |     | 45°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|      |     | (E) |      | (F) |      |     | (G) |      |     | (H) | 234 |
| 50°S |     |     | 50°S |     | 50°S |     |     | 50°S |     |     |     |
228
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
700 hPa—24 h before 700 hPa—12 h before 700 hPa—0 h before 700 hPa—12 h after
95
| 20°S |     |     | 20°S |     | 20°S |     |     | 20°S |     |     | 90  |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
)%( ytidimuh evitaleR
| 25°S |     |     | 25°S |     | 25°S |     |     | 25°S |     |     | 85  |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 30°S |     |     | 30°S |     | 30°S |     |     | 30°S |     |     | 80  |
| 35°S |     |     | 35°S |     | 35°S |     |     | 35°S |     |     | 75  |
| 40°S |     |     | 40°S |     | 40°S |     |     | 40°S |     |     |     |
70
| 45°S |     |     | 45°S |     | 45°S |     |     | 45°S |     |     | 65  |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|      |     | (I) |      | (J) |      |     | (K) |      |     | (L) |     |
| 50°S |     |     | 50°S |     | 50°S |     |     | 50°S |     |     | 60  |
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
850 hPa—24 h before 850 hPa—12 h before 850 hPa—0 h before 850 hPa—12 h after
95
| 20°S |     |     | 20°S |     | 20°S |     |     | 20°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
90
)%( ytidimuh evitaleR
| 25°S |     |     | 25°S |     | 25°S |     |     | 25°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
| 30°S |     |     | 30°S |     | 30°S |     |     | 30°S |     |     | 85  |
| 35°S |     |     | 35°S |     | 35°S |     |     | 35°S |     |     |     |
80
| 40°S |     |     | 40°S |     | 40°S |     |     | 40°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
75
| 45°S |     |     | 45°S |     | 45°S |     |     | 45°S |     |     |     |
| ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | --- |
|      |     | (M) |      | (N) |      |     | (O) |      |     | (P) |     |
| 50°S |     |     | 50°S |     | 50°S |     |     | 50°S |     |     |     |
70
70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W 70°W 60°W 50°W 40°W
FIGURE12:Compositesofthe20mostintensesummerevents24hbefore(A,E,I,andM),12hbefore(B,F,J,andN),at(C,G,K,andO)and
12h after(D, H,L, and P) cyclogenesis. (A–D)300hPa streamlines, colorshading magnitudeabove 60m/s, (E–H)500hPa geopotential
height(dams)andairtemperature(K),(I–L)700hPawind(barb),geopotentialheight(dams)andrelativehumidity,shadingmagnitude
above60%and(M–P)850hPawind(barb),geopotentialheight(dams)andrelativehumidity,withshadingmagnitudeabove70%.
events,56cyclonesreachedthethree-parameterthresholdin pattern.ThePearsoncorrelationofthetwosegmentsofthe
the 41 years, with a track that shifted mainly far from the area was very weak.
continent.Ifthecyclonesthatreachedbothintensityparam- The number of intense events, measured by the mini-
eters (minimum pressure and maximum wind) are consid- mum sea level pressure and by the maximum 10-m winds,
ered, some of the 166 intense events of the 41 years are andthenumberoffasteventsshowedimportantinterannual
shifted toward the coastal region and thus have greater variability, similar to the total number of events. A greater
potential to impact the population. quantity of intense cyclones occurred between 2005 and
Acloservisualinspectionofcyclonecounttimeseriesfor 2010. The Pearson correlation is moderate between intense
the entire, northern, and southern parts of the study area, events with respect tosea levelpressure andthe10-m wind
according to the 35°Slatitude, revealed a slightly increasing criterion and strong between faster cyclones and intense
trend, although the Mann–Kendall test revealed that this events withrespect tothetwo criteria.
trendwasnotstatisticallysignificantforthethreetimeseries.
|     |     |     |     |     |     | We explored | cyclone | analysis | from | another perspective: |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | -------- | ---- | -------------------- | --- |
Thecubicpolynomialmodelbetterfitsthedataforthethree theseasonalcountofthetwopartsofthestudyarea.While
|                |              |     |             |                   |     | the trend | in the northern | part | of the | area was insignificant |     |
| -------------- | ------------ | --- | ----------- | ----------------- | --- | --------- | --------------- | ---- | ------ | ---------------------- | --- |
| areas, meaning | thatthecount |     | of cyclones | has anoscillatory |     |           |                 |      |        |                        |     |

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 18  |     |     |     |     |     |     |     |     |     |     |     | Advances | inMeteorology |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
across all seasons, a notable trend emerged in the southern provide insights into the underlying mechanisms account-
partduringsummer,withpositiveslopeof1.7perdecade,as able for theobservedpatternsof variability.
determinedbytheMann–Kendalltestatthe95%confidence Furtherinvestigationsofthelinksbetweenthevariability
significance
level. The variability analysis revealed the of in cyclone counts and key oceanic parameters, such as sea
oscillations with periods of 2–3 years in the northern part level temperature and UOHC, as well as established large-
during winter, as well as in both parts during spring, sum- scale modes of variability, such as AMO and SAM, may be
mer, and autumn. Additionally, a peak of energy in the 5- useful in understanding the factors that contribute to the
yearperiodwasobservedinthenorthernpartduringwinter oscillatory pattern observed in annual cyclone counts. The
and in the southern part during autumn. Peaks between 8 influencesofoceaniceddiesandoceanicfrontsintheatmo-
and10years,presentinwinterandspring,maybelinkedto sphere also need further investigation. Some recent studies
decadal oscillations. The origin ofthese peakswarrants fur- havefocusedonthesefeaturesandtheirroleinsea-airinter-
ther investigation in future studies. actions (e.g., [72–74]). Furthermore, exploring possible
|       |     |          |          |     |            |      |       | lagged covariances |     | between | cyclone | counts | in the | northern |
| ----- | --- | -------- | -------- | --- | ---------- | ---- | ----- | ------------------ | --- | ------- | ------- | ------ | ------ | -------- |
| Catto | et  | al. [12] | reviewed | the | mechanisms | that | could |                    |     |         |         |        |        |          |
intensification
modify the main regions of formation and and southern regions could provide interesting information
ofextratropicalcyclonesoverthenextcenturyinawarming and may reveal connections not captured by the simulta-
|     |     |     |     |     |     |     |     | neous correlation |     | analysis | provided | in this | study. | In the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | -------- | ------- | ------ | ------ |
climate.Increasedtemperaturegradientsintheuppertropo-
sphere are expected to intensify upper-level jet streams and scopeofthisstudy,specialattentionmustbegiventoclimate
enhance storm intensity during the development of extra- changeanditsimpacts.Consideringthechangesinheatand
|          |           |           |     |           |        |           |     | humidity | air-sea | fluxes under | higher | sea | surface | tempera- |
| -------- | --------- | --------- | --- | --------- | ------ | --------- | --- | -------- | ------- | ------------ | ------ | --- | ------- | -------- |
| tropical | cyclones. | Moreover, |     | increased | static | stability | and |          |         |              |        |     |         |          |
greaterlatentheatreleasemaycontributetofuturestrength- tures, it would be interesting to study the relationships
ening of events. Additionally, in response to increasing between marine heatwave events and the occurrence of
|        |             |            |     |             |                 |                  |         | cyclones, | especiallymore | intense |     | events. |     |     |
| ------ | ----------- | ---------- | --- | ----------- | --------------- | ---------------- | ------- | --------- | -------------- | ------- | --- | ------- | --- | --- |
| future | atmospheric | greenhouse |     | gas         | concentrations, |                  | climate |           |                |         |     |         |     |     |
| models | generally   | simulate   |     | a reduction |                 | in extratropical |         |           |                |         |     |         |     |     |
cyclone intensity in the North Atlantic, while projecting an Data Availability Statement
| increase | in  | extreme | winter | extratropical |     | cyclones | in the |     |     |     |     |     |     |     |
| -------- | --- | ------- | ------ | ------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Thedatathatsupportthefindingsofthisstudyareavailable
SouthernHemisphere.AccordingtoHarveyetal.[71],these
divergentresponsescanbeattributedtoprojectedchangesin inCopernicusClimateDataStoreathttps://cds.climate.cope
the low-level equator-to-pole air temperature gradient. The rnicus.eu/cdsapp#!/home.Thesedatawerederivedfromthe
|                                                     |          |              |         |             |           |             |          | following    | resources  | available | in the                          | public | domain: | ERA5/ |
| --------------------------------------------------- | -------- | ------------ | ------- | ----------- | --------- | ----------- | -------- | ------------ | ---------- | --------- | ------------------------------- | ------ | ------- | ----- |
| impact                                              | of these | factors      | remains | uncertain   |           | because     | of the   |              |            |           |                                 |        |         |       |
|                                                     |          |              |         |             |           |             |          | ECMWF        | reanalysis | dataset,  | https://cds.climate.copernicus. |        |         |       |
| nonuniform                                          |          | nature ofthe | changes | across      | different |             | regions. |              |            |           |                                 |        |         |       |
| Tounderstandthemeteorologicalcharacteristicsassoci- |          |              |         |             |           |             |          | eu/datasets. |            |           |                                 |        |         |       |
| ated with                                           | intense  | events       | in      | the coastal | areas     | of southern |          |              |            |           |                                 |        |         |       |
|                                                     |          |              |         |             |           |             |          | Conflicts    | of         | Interest  |                                 |        |         |       |
BrazilandUruguay,acompositeofthemeteorologicalvari-
| ables | of the | upper, middle, |     | and lower | levels | of the | tropo- |     |     |     |     |     |     |     |
| ----- | ------ | -------------- | --- | --------- | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
conflicts
|                                                       |                |              |            |     |                |          |         | The authors | declare | no  | of  | interest. |     |     |
| ----------------------------------------------------- | -------------- | ------------ | ---------- | --- | -------------- | -------- | ------- | ----------- | ------- | --- | --- | --------- | --- | --- |
| sphere                                                | was            | constructed. | Even       | if  | each event     | presents | a       |             |         |     |     |           |     |     |
| particular                                            | meteorological |              | condition, |     | the composites |          | help us |             |         |     |     |           |     |     |
| understandthepreferentialpatternofevolution,suchasthe |                |              |            |     |                |          |         | Funding     |         |     |     |           |     |     |
equatorialentranceofthejetstreamatupper-levels,thedeep
ThisworkwassupportedbytheNationalCouncilforScien-
| trough | at upper | and | middle | levels, | and the | importance | of  |     |     |     |     |     |     |     |
| ------ | -------- | --- | ------ | ------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
tificandTechnologicalDevelopment(CNPq),406769/2021-
moisturetransport,whichisdirectedfromthetropicstothe
|            |       |              |              |     |        |          |         | 4, 406763/2022-4. |     |     |     |     |     |     |
| ---------- | ----- | ------------ | ------------ | --- | ------ | -------- | ------- | ----------------- | --- | --- | --- | --- | --- | --- |
| coastal    | area, | in the lower | troposphere. |     | These  | patterns | are     |                   |     |     |     |     |     |     |
| consistent | with  | previous     | studies      | of  | Mendes | et al.   | [56] on |                   |     |     |     |     |     |     |
References
theprecursorsofSouthAmericancyclogenesisandMontini
etal.[68]regardingtheroleofthelow-leveljetintransport-
|     |     |     |     |     |     |     |     | [1] K.E. | Kunkel, | D.R. | Easterling, | D.A. | R.  | Kristovich, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---- | ----------- | ---- | --- | ----------- |
ingmoistureandenhancinginstabilityattheendofitspath, B.Gleason,L.Stoecker,andR.Smith,“MeteorologicalCauses
| promoting                                          | cyclone | intensification. |     |     |     |     |     |        |         |                  |             |         |               |            |
| -------------------------------------------------- | ------- | ---------------- | --- | --- | --- | --- | --- | ------ | ------- | ---------------- | ----------- | ------- | ------------- | ---------- |
|                                                    |         |                  |     |     |     |     |     | of the | Secular | Variations       | in Observed | Extreme | Precipitation |            |
| Thisstudyoffersasignificantnewperspectiveonintense |         |                  |     |     |     |     |     |        |         |                  |             |         | States,”      |            |
|                                                    |         |                  |     |     |     |     |     | Events | for     | the Conterminous |             | United  |               | Journal of |
extratropical cyclones within theSouthwest Atlantic Ocean, Hydrometeorology13,no. 3(2012):1131–1141.
contributing to the broader understanding of variability [2] C. K. Parise, L. J. Calliari, and N. Krusche, “Extreme Storm
analysis and the distinct characteristics of systems that sig- Surges in the South of Brazil: Atmospheric Conditions and
nificantly Shore Erosion,” Brazilian Journal of Oceanography 57, no.3
|     | affect | both | coastal | communities |     | and the | natural |     |     |     |     |     |     |     |
| --- | ------ | ---- | ------- | ----------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
(2009):175–188.
environment.Ourfindingsshedlightontheprevailingsyn-
|     |     |     |     |     |     |     |     |     |     | Ó.  |     |     | “Thresholds |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
optic conditions conducive to the development of intense [3] L. P. Almeida, Ferreira, and A. Pacheco, for
|     |     |     |     |     |     |     |     | Morphological |     | Changes | on an | Exposed | Sandy | Beach as a |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ----- | ------- | ----- | ---------- |
cyclones, which aligns with prior research [21, 23, 56]. Height,”
|     |     |     |     |     |     |     |     | Function | of  | Wave | Earth | Surface | Processes | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ----- | ------- | --------- | --- |
Such insights are relevant for informing and preparing for 4(2011):523–532.
Landforms36,no.
futureevents,particularlythosewiththepotentialtosignifi-
|     |     |     |     |     |     |     |     | [4] M.da | G.Albuquerque,D.C.LealAlves,J.Espinoza,U. |     |     |     |     | R.de |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------------------------------- | --- | --- | --- | --- | ---- |
cantlyimpactcoastalregions.Theprovidedresultsconcern- Oliveira,andR. S.Simões,“DeterminingShorelineResponse
ing energy peaks yield valuable insights; however, they also to Meteooceanographic Events Using Remote Sensing and

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances | in Meteorology |     |     |     |     |     |     |     |                |     | 19  |
| -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
|          |                |     |     |     |     |     |     |     | “The Influence |     |     |
Unmanned Aerial Vehicle (UAV): Case Study in Southern [23] M.A. Gan and V. B. Rao, of the Andes
Brazil,”JournalofCoastalResearch85(2018):766–770. Cordillera on Transient Disturbances,” Monthly Weather
[5] C.B. Gramcianinov, R. de Camargo, and R.M. Campos, Review122,no. 6(1994):1141–1157.
“ImpactofExtratropicalCycloneIntensityandSpeedonthe [24] D.Mendes,E. P.Souza,J. A.Marengo,andM.C.D.Mendes,
Extreme Wave Trends in the Atlantic Ocean,” Climate “Climatology of Extratropical Cyclones Over the South
Dynamics60,no.5-6(2023):1447–1466. American–SouthernOceans Sector,” Theoretical andApplied
T.P.EichlerandJ.Gottschalck,“AComparisonofSouthern Climatology100,no.3-4(2010):239–250.
[6]
P.daRocha,M.Sprenger,andH.Wernli,“A
| Hemisphere | Cyclone | Track | Climatology | and | Interannual | [25] N. M.Crespo,R. |     |     |     |     |     |
| ---------- | ------- | ----- | ----------- | --- | ----------- | ------------------- | --- | --- | --- | --- | --- |
VariabilityinCoarse-GriddedReanalysisDatasets,”Advances
PotentialVorticityPerspectiveonCyclogenesisOverCentre-
inMeteorology2013(2013):1–16:891260. EasternSouthAmerica,”InternationalJournalofClimatology
|          |           |              |               | Räisänen, |     |        | 1(2021):663–678. |     |     |     |     |
| -------- | --------- | ------------ | ------------- | --------- | --- | ------ | ---------------- | --- | --- | --- | --- |
| [7] V.A. | Sinclair, | M. Rantanen, | P. Haapanala, | J.        | and | 41,no. |                  |     |     |     |     |
H. Järvinen, “The Characteristics and Structure of Extra- [26] L.Dalanhese,J.Stuivenvolt-Allen,M.LaPlante,etal.,“ANew
Tropical Cyclones in a Warmer Climate,” Weather and Climatology of South American Extratropical Cyclogenesis
ClimateDynamicsDiscussions1,no. 1(2020):1–33. With an Inter-Comparison Among ERA5, JRA55, and the
[8] T.K. Laurila, H. Gregow, J. Cornér, and V.A. Sinclair, Brazilian Navy,” International Journal of Climatology 43,
“Characteristics of Extratropical Cyclones and Precursors to no. 15(2023):7050–7066.
Europe,”
Windstorms in Northern Weather and Climate [27] R. S. Simoes, L. J. Calliari, S. A. de Figueiredo, U.R. de
Dynamics2,no.4(2021):1111–1130. M.deAlmeida,“CoastlineDynamicsinthe
|     |     |     |     |     |     | Oliveira,andL. |     | P.  |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
J.Zhang,H.Xu,J.Ma,andJ.Deng,“InterannualVariabilityofSpring
| [9] |     |     |     |     |     | Extreme | South | of Brazil | and Their Socio-Environmental |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | ----------------------------- | --- | --- |
Impacts,”
ExtratropicalCyclonesovertheYellow,Bohai,andEastChinaSeas Ocean and Coastal Management 230 (2022):
andPossibleCauses,”Atmosphere10,no.1(2019):40.
106373.
[10] J.C. Fyfe, “Extratropical Southern Hemisphere Cyclones: [28] B.Medeiros,B.D.L.Williamson,andJ. G.Olson,“Reference
HarbingersofClimateChange?”JournalofClimate16,no. 17 Aquaplanet Climate in the Community Atmosphere Model
(2003):2802–2805. Version5,”JournalofAdvancesinModelingEarthSystems8,
[11] T.A. Shaw, M. Baldwin, E.A. Barnes, et al., “Storm Track no. 1(2016):406–424.
Processes and the Opposing Influences of Climate Change,” [29] IPCC,inClimateChange2023:SynthesisReport,Contribution
9(2016):656–664.
NatureGeoscience9,no. ofWorkingGroupsI,IIandIIItotheSixthAssessmentReport
“The
[12] J.L. Catto, D. Ackerley, J. F. Booth, et al., Future of oftheIntergovernmentalPanelonClimateChange,ed.H.Lee
|             | Cyclones,” |     |         |                |            | andJ.Romero,(2023):35–115. |     |     |     |     |     |
| ----------- | ---------- | --- | ------- | -------------- | ---------- | -------------------------- | --- | --- | --- | --- | --- |
| Midlatitude |            |     | Current | Climate Change | Reports 5, |                            |     |     |     |     |     |
no.4(2019):407–420.
[30] M.S.Reboita,R.P.daRocha,M.R.deSouza,andM.Llopart,
G.Pinto,“Extra-Tropical “ExtratropicalCyclonesOvertheSouthwesternSouthAtlantic
| [13] U.Ulbrich,G. | C.Leckebusch,andJ. |     |     |     |     |     |     |     |     |     |     |
| ----------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Cyclones in the Present and Future Climate: A Review,” Ocean: HadGEM2-ES and RegCM4 Projections,” Interna-
TheoreticalandAppliedClimatology96,no. 1-2(2009):117– tionalJournalofClimatology38,no. 6(2018):2866–2879.
131. [31] M.S. Reboita, M. Reale, R. P. da Rocha, et al., “Future
[14] C.C.Raible,P. M.Della-Marta,C.Schwierz,H.Wernli,and Changes in the Wintertime Cyclonic Activity Over the
R.Blender,“NorthernHemisphereExtratropicalCyclones:A CORDEXCORE Southern Hemisphere Domains in a Multi-
Approach,”
Comparison of Detection and Tracking Methods and model Climate Dynamics 57, no. 5-6 (2021):
|                 | Reanalyses,” |         |         |        |            | 1533–1549.      |             |            |          |     |       |
| --------------- | ------------ | ------- | ------- | ------ | ---------- | --------------- | ----------- | ---------- | -------- | --- | ----- |
| Different       |              | Monthly | Weather | Review | 136, no. 3 |                 |             |            |          |     |       |
| (2008):880–897. |              |         |         |        |            |                 |             |            | “RegCM4: |     |       |
|                 |              |         |         |        |            | [32] F. Giorgi, | E. Coppola, | F. Solmon, | et al.,  |     | Model |
U.Neu,M.G.Akperov,N.Bellenbaum,etal.,“IMILAST:A
| [15] |     |     |     |     |     | Description | and | Preliminary | Tests Over Multiple | CORDEX |     |
| ---- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ------------------- | ------ | --- |
Domains,”ClimateResearch52(2012):7–29.
| Community | Effort | to Intercompare |     | Extratropical | Cyclone |     |     |     |     |     |     |
| --------- | ------ | --------------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- |
DetectionandTrackingAlgorithms,”BulletinoftheAmerican [33] H. Hersbach, B.Bell, P. Berrisford, et al., “The ERA5 Global
MeteorologicalSociety94,no. 4(2013):529–547. Reanalysis,” Quarterly Journal of the Royal Meteorological
[16] T.D. Hewson and U. Neu, “Cyclones, Windstorms and the Society146,no.730(2020):1999–2049.
IMILAST Project,” Tellus A: Dynamic Meteorology and [34] R. M. Campos, C. B. Gramcianinov, R. de Camargo, and
Oceanography67,no.1(2015):27128. P. L. da Silva Dias, “Assessment and Calibration of ERA5
|     |     |     | “Mean |     |     |     |     |     |     |     | Data,” |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | ------ |
[17] I. Simmonds and K. Keay, Southern Hemisphere Severe Winds in the Atlantic Ocean Using Satellite
ExtratropicalCycloneBehaviorinthe40-YearNCEP–NCAR 4918(2022):1–24.
RemoteSensing14,no.
| Reanalysis,”JournalofClimate13,no. |     |     |     | 5(2000):873–885. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
[35] C.McErlich,A.McDonald,J.Renwick,andA.Schuddeboom,
“An
[18] M.S. Reboita, R. Rosmeri, T. Ambrizzi, and S. Sugahara, Assessment of Southern Hemisphere Extratropical
“SouthAtlanticOceanCyclogenesisClimatologySimulatedby WidSat,”
|     |     |     |     |     |     | Cyclones | in ERA5 | Using | Journal | of Geophysical |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ----- | ------- | -------------- | --- |
Regional Climate Model (RegCM3),” Climate Dynamics 35, Research:Atmospheres128,no. 22(2023):e2023JD038554.
no.7-8(2010):1331–1347. [36] C. K.PadilhaReinke,J. P.Machado,M.M.Mata,J. L. L.de
[19] J.P. Peixoto and A.H. Oort, Physics of Climate (American Azevedo. J. M. B. Saraiva, and R. Rodrigues, “Objective
InstituteofPhysics,1992):520. Algorithm for Detection and Tracking of Extratropical
[20] J.R. Holton and J.H. Gregory, An Introduction to Dynamic CyclonesintheSouthernHemisphere,”Atmosphere15,no.2
| Meteorology,4thed.(Elsevier,2004). |     |     |     |                       |     | (2024):230. |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --------------------- | --- | ----------- | --- | --- | --- | --- | --- |
|                                    |     |     |     | H.Berbery,“ColdSeason |     |             |     |     | “A  |     |     |
[21] C.S.Vera,P.K.Vigliarolo,andE. [37] B.J. Hoskins and K.I. Hodges, New Perspective on
|     |     |     |     |     | America,” |     |     |     | Tracks,” |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | -------- | --- | --- |
Synoptic-Scale Waves Over Subtropical South Southern Hemisphere Storm Journal of Climate 18,
|                             |     |     |     | 3(2002):684–699. |     | 20(2005):4108–4129. |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ---------------- | --- | ------------------- | --- | --- | --- | --- | --- |
| MonthlyWeatherReview130,no. |     |     |     |                  |     | no.                 |     |     |     |     |     |
M.A.GanandV.B.Rao,“SurfaceCyclogenesisOverSouth
[22] [38] A. D.Crawford,E. A.P.Schreiber,N.Sommer,M.C.Serreze,
America,”MonthlyWeatherReview119,no. 5(1991):1293– J. C. Stroeve, and D.G. Barber, “Sensitivity of Northern
| 1302. |     |     |     |     |     | HemisphereCycloneDetectionandTrackingResultstoFine |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 20  |     |     |     |     |     |     |     |     |     |     | Advances | inMeteorology |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- |
ERA5,”
Spatial and Temporal Resolution Using Monthly [56] D. Mendes, E. P. Souza, I.F. Trigo, and P. M.A. Miranda,
WeatherReview149(2021):2581–2598. “On Precursors of South American Cyclogenesis,” Tellus A:
[39] M.Inatsu,“TheNeighborEnclosedAreaTrackingAlgorithm Dynamic Meteorology and Oceanography 59, no. 1 (2007):
| for Extratropical | Wintertime |     | Cyclones,” | Atmospheric |     | Science | 114–121. |     |     |     |     |     |     |
| ----------------- | ---------- | --- | ---------- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- |
Letters10,no. 4(2009):267–272. [57] J. D.Dos Santos, J. P. Machado, and J. M.B. Saraiva, “The
[40] H. Samet, Applications of Spatial Data Structures: Computer Response of Southwest Atlantic Storm Tracks to Climate
ChangeintheBrazilianEarthSystemModel,”Atmosphere14,
| Graphics, | Image Processing |     | and Gis | (Addison-Wesley, |     | USA, |     |     |     |     |     |     |     |
| --------- | ---------------- | --- | ------- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
7(2023):1–21.
| 1989):516. |     |     |     |     |     |     | no. |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
“Calculating
[41] L. Bai and D. Breen, Center of Mass in an [58] N. C. Wells, The Atmosphere and Ocean: A Physical
Unbounded2DEnvironment,”JournalofGraphicalTools13,
|     |     |     |     |     |     |     | Introduction, |     | 3rd ed. | (John | Wiley | and Sons, University | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ----- | ----- | -------------------- | --- |
no.4(2008):53–60.
Southampton,UK,2011):432.
[42] M. Inatsu and S. Amada, “Dynamics and Geometry of [59] C. B. Gramcianinov, R. M. Campos, R. de Camargo,
Extratropical Cyclones in the Upper Troposphere by a K.I. Hodges, C. Guedes Soares, and P. L. da Silva Dias,
Neighbor Enclosed Area Tracking Algorithm,” Journal of “Analysis of Atlantic Extratropical Storm Tracks Character-
Climate26,no. 21(2013):8641–8653. isticsin41yearsofERA5andCFSR/CFSv2Databases,”Ocean
[43] C.B. Gramcianinov, R.M. Campos, C. Guedes Soares, and Engineering216(2020):1–41:108111.
“Extreme
R. de Camargo, Waves Generated by Cyclonic [60] H.B. Bluestein, Synoptic-Dynamic Meteorology at Midlati-
WindsintheWesternPortionoftheSouthAtlanticOcean,”
tudes,1sted.(OxfordUniversityPress,1992):448.
M.Barreiro,“InfluenceofENSOandtheSouthAtlanticOcean
| OceanEngineering213(2020):107745. |     |     |     |     |     |     | [61] |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
onClimatePredictabilityOverSoutheasternSouthAmerica,”
| [44] E. Flaounas, | V. Kotroni, | K.  | Lagouvardos, | and | I. Flaounas, |     |     |     |     |     |     |     |     |
| ----------------- | ----------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
“CycloTRACK(v1.0)–TrackingWiterExtratropicalCyclones 7-8(2010):1493–1508.
ClimateDynamics35,no.
Based on Relative Vorticity: Sensitivity to Data Filtering and [62] M.S. Reboita, T. Ambrizzi, and R. da Rocha, Southern
OtherRelevantParameters,”GeoscientificModelDevelopment Hemisphere Extratropical Cyclones and Their Relationship
7,no. 4(2014):1841–1853. With ENSO in Springtime (American Geophysical Union,
[45] E.-P. Lim and I. Simmonds, “Southern Hemisphere Winter SpringMeeting,2013):A31A-10.
Extratropical Cyclone Characteristics and Vertical Organiza- [63] A. B. Pezza, I. Simmonds, and J. A. Renwick, “Southern
tionObservedWiththeERA-40Datain1979–2001,”Journal
|                 |                     |     |          |     |     |     | Hemisphere |      | Cyclones | and Anticyclones: |     | Recent         | Trends and |
| --------------- | ------------------- | --- | -------- | --- | --- | --- | ---------- | ---- | -------- | ----------------- | --- | -------------- | ---------- |
|                 | 11(2007):2675–2690. |     |          |     |     |     |            |      |          |                   |     | Pacific        | Ocean,”    |
| ofClimate20,no. |                     |     |          |     |     |     | Links      | With | Decadal  | Variability       | in  | the            |            |
|                 |                     |     | “Changes |     |     |     |            |      |          |                   |     | 11(2007):1403– |            |
[46] S.J. Lambert and J.C. Fyfe, in Winter Cyclone InternationalJournalofClimatology27,no.
| Frequencies | and Strengths |     | Simulated | in Enhanced |     | Green- | 1419. |     |     |     |     |     |     |
| ----------- | ------------- | --- | --------- | ----------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
“On
house Warming Experiments: Results From the Models [64] L. Li and A.J. Dolman, the Reliability of Composite
Participating in the IPCC Diagnostic Exercise,” Climate Analysis: An Example of Wet Summers in North China,”
Dynamics26,no.7-8(2006):713–728. AtmosphericResearch292(2023):1–10:106881.
[47] C.B. Gramcianinov, K.I. Hodges, and R. Camargo, “The [65] R.D.GarreaudandJ.M.Wallace,“SummertimeIncursionsof
Properties and Genesis Environments of South Atlantic MidlatitudeAirIntoSubtropicalandTropicalSouthAmerica,”
Cyclones,”ClimateDynamics53,no. 7-8(2019):4115–4140. MonthlyWeatherReview126,no.10(1998):2713–2733.
|             |              |       |       |           |       | “On | A.Marengo,M.W.Douglas,andP.L.SilvaDias,“TheSouth |     |     |     |     |     |     |
| ----------- | ------------ | ----- | ----- | --------- | ----- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| [48] Z. Wu, | N. E. Huang, | S. R. | Long, | and C.-K. | Peng, | the | [66] J.                                          |     |     |     |     |     |     |
Trend, Detrending, and Variability of Nonlinear and AmericanLow-LevelJetEastoftheAndesDuringthe1999LBA-
|              |      | Series,” |                |     |                 |     | TRMMandLBA-WETAMCCampaign,”JournalofGeophysical |     |     |     |     |     |     |
| ------------ | ---- | -------- | -------------- | --- | --------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Nonstatioary | Time |          | in Proceedings |     | of the National |     |                                                 |     |     |     |     |     |     |
D20(2002):1–11.
Academy of Sciences (PNAS), 104, (National Academy of Research:Atmospheres107,no.
SciencesoftheUnitedStatesofAmerica(NAS),2007):14889– C.Vera,J.Baez,M.Douglas,etal.,“TheSouthAmericanLow-
[67]
14894. LevelJetExperiment,”BulletinoftheAmericanMeteorological
[49] R.J.HyndmanandG.Athanasopoulos,Forecasting:Principles Society87,no.1(2006):63–78.
andPractice,2nded.(OTexts, Melbourne,Aus,Accessedon [68] T. L. Montini, C. Jones, and L. M.V. Carvalho, “The South
27September,2024,2018). AmericanLow-LevelJet:ANewClimatology,Variability,and
[50] M.G. Kendall, Rank Correlation Methods, 4th ed. (Griffin, Changes,”JournalofGeophysicalResearch:Atmospheres124,
3(2019):1200–1218.
| London,UK,1975):202. |     |     |     |     |     |     | no. |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S.YueandP.Pilon,“AComparisonofthePowerofthet-Test, M.V.Carvalho,andQ.Ding,“TheSouth
| [51] |     |     |     |     |     |     | [69] C.Jones,Y.Mu,L. |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
Detection,”
Mann-Kendall and Bootstrap Tests for Trend America Low-Level Jet: Form, Variability and Large-Scale
| HydrologicalSciencesJournal49(2019):21–37. |     |     |     |     |     |     | Forcings,” |     |         |     |             |         |         |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | ----------- | ------- | ------- |
|                                            |     |     |     |     |     |     |            | npj | Climate | and | Atmospheric | Science | 6, no.1 |
(2023):1–11.
| [52] W.J. Emery | and R.E. | Thomson, |     | Data Analysis | Methods | in  |     |     |     |     |     |     |     |
| --------------- | -------- | -------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
PhysicalOceanography,2nded.(Elsevier,revised,2001). [70] U.A. Sutil, L. P. Pezzi, R.C. M. Alves, and A. B. Nunes,
[53] D.L. Gilman, F. J. Fuglister, and J. M. Mitchell Jr, “On the “Ocean-AtmosphereInteractionsinanExtratropicalCyclone
Power Spectrum of Red Noise,” Journal of the Atmospheric in the Southwest Atlantic,” Anuário do Instituto de
Sciences20,no. 2(1963):182–184. Geociências-UFRJ42,no.1(2019):525–535.
[54] G.A.Prieto,ImprovingEarthquakeSourceSpectrumEstima- [71] B.J.Harvey,L. C.Shaffrey,andT. J.Woollings,“Equator-to-
tion Using Multitaper TechniquesUniversity of California, Pole Temperature Differences and the Extratropical Storm
| pp.1–141,2007). |     |     |     |     |     |     |       |           |                      |           |         | Models,” |         |
| --------------- | --- | --- | --- | --- | --- | --- | ----- | --------- | -------------------- | --------- | ------- | -------- | ------- |
|                 |     |     |     |     |     |     | Track | Responses | of                   | the CMIP5 | Climate |          | Climate |
|                 |     |     | “A  |     |     |     |       |           | 5-6(2014):1171–1182. |           |         |          |         |
[55] R.J. Murray and I. Simmonds, Numerical Scheme for Dynamics43,no.
Tracking Cyclone Centres From Digital Data. Part II: [72] I.B. M. Orselli, K. Rodrigo, J. L.L. de Azevedo, F. Galdino,
E.Garcia,“TheSea-AirCO2NetFluxes
Application to January and July General Circulation Model M.Araujo,andC.A.
Simulations,” Australian Meteorological Magazine 39, no. 3 intheSouthAtlanticOceanandtheRolePlayedbyAgulhas
(1991):167–180. Eddies,”ProgressinOceanography170(2019):40–52.

 1306, 2026, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1155/adme/9965323 by University Of Sao Paulo - Brazil, Wiley Online Library on [27/01/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| Advances | in Meteorology |     |     | 21  |
| -------- | -------------- | --- | --- | --- |
A.Lorenzzetti,etal.,“Sutil“the
| [73] L.P.Pezzi,M.F. | L.Quadro,J. |     |     |     |
| ------------------- | ----------- | --- | --- | --- |
EffectofOceanicSouthAtlanticConvergenceZoneEpisodes
| on Regional | SST Anomalies:     | The Roles of Heat | Fluxes and  |     |
| ----------- | ------------------ | ----------------- | ----------- | --- |
| Upper-Ocean | Dynamics,” Climate | Dynamics          | 59, no. 7-8 |     |
(2022):2041–2065.
[74] I.Ma,I.Ginis,andS. K.Kang,“NumericalStudyofEffectsof
| Warm                               | Ocean Eddies on Tropical | Cyclones          | Intensity in |     |
| ---------------------------------- | ------------------------ | ----------------- | ------------ | --- |
| NorthwestPacific,”Atmosphere15,no. |                          | 4(2024):1–22:445. |              |     |