Received:28August2021 Revised:24June2022 Accepted:18July2022 Publishedon:17August2022
DOI:10.1002/qj.4349
RESEARCH ARTICLE
From a Shapiro–Keyser extratropical cyclone to the
subtropical cyclone Raoni: An unusual winter synoptic
situation over the South Atlantic Ocean
MichelleSimõesReboita1 LuizFelippeGozzo2 NatáliaMachadoCrespo3
MariadeSouzaCustodio2 ViníciusLucyrio1 EduardoMarcos deJesus3
RosmeriPorfírio daRocha3
1InstitutodeRecursosNaturais,
Abstract
UniversidadeFederaldeItajubá
(UNIFEI),Itajubá,Brazil The eastern coast of South America is a cyclogenetic region in terms of extra-
2SchoolofSciences,SãoPauloState tropical cyclones and, in lower number, of subtropical cyclones that are more
University(UNESP),Bauru,Brazil
frequent in austral summer and autumn. However, in June 2021, an unusual
3InstitutodeAstronomia,Geofísicae
cyclonedevelopedneartheboundaryofUruguayandsouthernBrazil,initially
CiânciasAtmosféricas,Universidadede
SãoPaulo(USP),SãoPaulo,Brazil having extratropical features and later undergoing a subtropical transition. At
1200 UTC 29 June, the Brazilian Navy named it as subtropical cyclone Raoni.
Correspondence
This study aims to describe the synoptic evolution of the cyclone and address
M.S.Reboita,UniversidadeFederalde
Itajubá(UNIFEI),InstitutodeRecursos physical drivers for the subtropical transition based on the ECMWF-ERA5
Naturais,Itajubá,MG,Brazil.
reanalysis and numerical experimentswith the WRF model. The cyclone pre-
Email:reboita@unifei.edu.br
cursor of Raoni had its genesis at 1800 UTC 26 June 2021 forced by a trough
Fundinginformation atmid–upperlevelsthatcrossedtheAndesMountainsandcausedarapidsur-
PETROBRAS;ConselhoNacionalde
facepressuredrop.Lessthan24hrlater,thecyclonepresentedafrontalT-bone
DesenvolvimentoCientíficoeTecnológico;
CoordenaçãodeAperfeiçoamentode patternandwarmseclusion,followingtheShapiro–Keyserdevelopmentmodel.
PessoaldeNívelSuperior
Strong surface heat fluxes, a deep moist troposphere, and the vertical align-
ment of the warm seclusion with an upper-level cut-off pattern provided the
adequate environment for organising convection and, consequently, for sub-
tropical transition at 0600 UTC 28 June. The fundamental role of the surface
turbulentheatfluxesforthetransitionisconfirmedthroughnumericalexper-
iments. This study is unprecedented in the sense that no subtropical cyclone
originatingfromawarmseclusionhasbeendocumentedovertheSouthAtlantic
before.Thesefindingsemphasisetheneedofmonitoringcold-seasonextratrop-
icalShapiro–Keysercyclonesintheregionsincetheycanevolvetoasubtropical
ortropicalcycloneandcancausedamagetothemaritimeactivitiesandcoastal
regionduetothestrongwinds.
KEYWORDS
cyclonephases,numericalexperiments,SouthAtlanticOcean,subtropicalcyclone,synoptic
evolution,warmseclusion
QJRMeteorolSoc.2022;148:2991–3009. wileyonlinelibrary.com/journal/qj ©2022RoyalMeteorologicalSociety 2991

2992 REBOITAetal.
1 INTRODUCTION Over the SAO, subtropical cyclones can have gene-
sis in this category or result from transitions. They are
InJune2021,anunusualsynopticdevelopmenttookstage supportedbyatroughoracut-offlowinmid–upperlev-
over the South Atlantic Ocean (SAO): an extratropical els of the atmosphere that acts to weaken the vertical
cyclone reached the status of explosive cyclone showing shear of horizontal wind and, consequently, favours the
characteristics of the Shapiro and Keyser (1990) model, organisationofthecyclone’sconvection.Furthermore,the
hereafterreferredtoasShapiro–Keyser;subsequently,the moisture transport by the northwesterly low-level winds
cycloneunderwentasubtropicaltransitionfavouredbythe from the continent to the ocean and/or by the north-
warm seclusion. This process occurred in winter, which easterlywindsfromthenorthwesternsectoroftheSASA
is a season not favourable for subtropical cyclogenesis to the cyclogenesis region are important to strengthen
in the region. Besides, the subtropical system moved to the subtropical cyclones near the east coast of Brazil
thenortheast,differingfromtheclimatology,wheremost (Gozzo et al., 2014; 2017; Reboita et al., 2019). Subtrop-
cyclones move to the southeast. Therefore, this study ical and tropical cyclones have some different features;
focuses on describing the synoptic evolution and on the for instance, in a subtropical system, the zonal deviation
processesactingfortheunusualcyclonedevelopmentand of air temperature in the system’s core is warm at low
transition. levels and cold at mid–upper levels. Moreover, at upper
Extratropicalcyclogenesisisacommonsynopticevent levels, the winds are stronger than near the surface. On
overtheSAO,mainlyneartheeastcoastofSouthAmer- the other hand, a tropical cyclone has a warm core from
ica (SA), where three preferential regions of cyclogen- the lower to the upper troposphere and the most intense
esis are identified: the south/southeast coast of Brazil windsareregisteredatlowlevels(Hart,2003;Evansand
(RG1), Uruguay and the extreme south of Brazil coasts Guishard,2009).
(RG2)andthesoutherncoastofArgentina(RG3)(Reboita As the atmosphere is a continuum, several studies
et al., 2010; 2012; 2015; 2018; Gan and Reboita, 2016; of subtropical cyclones (Quitián-Hernández et al., 2020),
Gramcianinovetal.,2019;Crespoetal.,2020a;2020b;de tropicaltransitions–TT(BentleyandMetz,2016;Mazza
Jesus et al., 2021b). Moreover, RG1 and RG2 are regions et al., 2017), “medicanes” (Mazza et al., 2017; Migli-
favourabletosubtropicalcyclogenesis(Gozzoetal.,2014; etta and Rotunno, 2019) and subtropical cyclones over
Reboitaetal.,2019;deJesusetal.,2021a).OvertheSAO, eastern Australia (Mills et al., 2010; Browning and
EvansandBraun(2012)obtainedanannualfrequencyof Goodwin, 2013) have indicated that an extratropical
∼1.3subtropicalcycloneswhileGozzoetal.(2014),using Shapiro–Keyserprecursormaybemorefavourabletotran-
a similar – but less restrictive – identification method, sition (Shapiro and Keyser, 1990; Schultz et al., 2019;
obtained ∼7.2 cyclones per year. This later study found Schultz and Keyser, 2021). In this cyclone model, there
a higher amplitude in the annual cycle of subtropical is a bent-back warm/occluded front that undergoes a
cyclonesfrequency,whichhasmoreandlessoccurrences, warm seclusion process (Davis and Bosart, 2004; Bent-
respectively, in summer and winter. Recently, de Jesus ley and Metz, 2016), which is an isolated warm air
et al. (2021a) showed that the subtropical cyclones rep- pool in the cyclone centre. The convection in the
resent ∼8.3% of the total cyclones in summer over the warm seclusion region can become organised, leading
SAO. to the transition from an extratropical to a subtrop-
ExtremelyrareintheSAOaretropicalcyclones;since ical cyclone and in some cases, even to a tropical
thebeginningofthesatelliteera,onlytwotropicalcyclones cyclone. To the author’s knowledge, there are no stud-
were registered in this ocean basin: Catarina (2004; ini- ies or documentation of subtropical transitions associ-
tial location at 26◦S, 43◦W), originated from a tropical ated with an extratropical Shapiro–Keyser cyclone over
transition, impacting states of south Brazil (Pezza and SAO. In this sense, the study of the case mentioned at
Simmonds,2005;McTaggart-Cowanetal.,2006),andIba the beginning of the Introduction will help to improve
(2019;initiallocation16.5◦S,36◦W),developedasapurely the knowledge of this kind of transition over the SAO
tropical cyclone near the south of Bahia Brazilian state basin.
(Reboitaetal.,2021).InthehurricaneCatarina,thetropi- The extratropical cyclone had its genesis near the
caltransitionwasassociatedwithanatmosphericblocking coast of southern Brazil at 1800 UTC 26 June 2021,
pattern decreasing the vertical shear of horizontal wind, and at 2330 UTC 28 June 2021, by using the DVO-
while in the case of Iba the low-level horizontal wind RAK technique (based on cloud patterns observed in
shear, between the post-frontal southwesterly winds and visible and infrared channels obtained by satellites: Dvo-
the northeasterly winds of the South Atlantic Subtropi- rak, 1984), National Oceanic and Atmospheric Admin-
cal Anticyclone (SASA), helped to generate Iba’s initial istration (NOAA) classified the system as a tropical
cyclonicvorticity. disturbancefor24hr,between2330UTC28Juneto2330
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

 1477870x, 2022, 747, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349 by Univ of Sao Paulo - Brazil, Wiley Online Library on [15/12/2024]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| REBOITAetal. |     |     |     |     |     |     |     |     |     |     |     |     | 2993 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
UTC29June(https://www.ssd.noaa.gov/PS/TROP/2021/ 2.2 Synopticanalysisandcyclone
| bulletins/archive.html).However,theBrazilianNavyclas- |      |        |     |               |     |         |     | structure |     |     |     |     |     |
| ----------------------------------------------------- | ---- | ------ | --- | ------------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- |
| sified the                                            | same | system | as  | a subtropical |     | cyclone | and |           |     |     |     |     |     |
named it Raoni (an indigenous name meaning “war- The region of study comprises the SAO near south
rior”) at 1200 UTC 29 June 2021, when it was over Brazil (Figure 1). The cyclone track, from the genesis
the south Brazilian coast. The unusual nature of this at 1800 UTC 26 June to cyclolysis at 1800 UTC 1 July
cyclone and its controversial classification by the mete- 2021, was obtained by identifying the minimum MSLP
orological centres justifies a deeper study. Therefore, grid point at the cyclone region (representing its cen-
the goal of this study is to address four questions: tre position) every 6 hr. Cyclogenesis was defined at
(a) What were the extratropical cyclogenesis drivers? the time when the first closed surface isobar occurs
(b) Which mechanisms contributed to the extratropi- in the cyclone centre. To describe the whole life cycle
cal cyclone acquiring features from the Shapiro–Keyser of the cyclone, we selected the ERA5 reanalysis syn-
cyclone model? (c) Did the cyclone reach a tropical optic charts (from 0000 UTC 26 June to 1800 UTC 1
phase, as stated in NOAA bulletins, or only a subtrop- July 2021) and satellite images more representative of its
| ical phase, | as  | classified | by  | the Brazilian |     | Navy? | and (d) | evolution. |     |     |     |     |     |
| ----------- | --- | ---------- | --- | ------------- | --- | ----- | ------- | ---------- | --- | --- | --- | --- | --- |
Whichprocessesledtothesubtropicaltransition?Thearti- Cyclone Phase-Space methodology (CPS: Hart, 2003)
cle is organised as follows: Section 2 presents data and was applied to classify the cyclone phases during its life
methodology, Section 3 starts with an overview of the cycle. Briefly, the CPS describes the thermal structure of
cyclonelifecycle(Section3.1),followedbyansweringthe the cyclones using three parameters computed from the
question (a) in Section 3.2, question (b) in Section 3.3; geopotential height at the atmospheric levels of 300, 600
question(c)isinitiallyansweredinSection3.1andcom- and 900hPa: thermal symmetry (B), which measures the
plemented in Section 3.4, and question (d) is answered strength of the frontal nature of the cyclone, and ther-
|     |     |     |     |     |     |     |     |     |     | L)andupper(−V |     | U)levels,which |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- |
in Section 3.5. Finally, Section 4 presents the main malwindatlow(−V T T
conclusions. allowsidentifyingthelevelwherethecyclonehashigher
|     |     |     |     |     |     |     |     | wind speed | (subtropical | and | extratropical | cyclones | have |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ------------- | -------- | ---- |
moreintensewindsatupperlevelsandtropicalcyclonesat
2 DATA AND METHODOLOGY lowerlevels).ForacompletedescriptionoftheCPSparam-
|     |     |     |     |     |     |     |     | eters, see | Hart (2003) | and da | Rocha | et al. (2019). | Here, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------ | ----- | -------------- | ----- |
2.1 Data we consider a cyclone to be subtropical when B <25m,
|     |     |     |     |     |     |     |     | <−10 |        | >−50. |       |           |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ----- | ----- | --------- | ------ |
|     |     |     |     |     |     |     |     | −V U | and −V | L     | These | threshold | values |
|     |     |     |     |     |     |     |     | T    |        | T     |       |           |        |
ThisstudyisdevelopedusingtheECMWFERA5reanal- are slightly different from the original values proposed
ysis (Hersbach et al., 2020), available at https://cds. byHart(2003),butwerefoundtobemorerepresentative
climate.copernicus.eu/, with a horizontal grid spacing of of subtropical cyclones that occur over the SAO by
| 0.25◦×0.25       | ◦            | of longitude |                | by latitude.   |             | The atmospheric |          |     |     |     |     |     |     |
| ---------------- | ------------ | ------------ | -------------- | -------------- | ----------- | --------------- | -------- | --- | --- | --- | --- | --- | --- |
| variables        | used         | are air      | temperature,   |                | zonal       | and meridional  |          |     |     |     |     |     |     |
| wind components, |              | geopotential |                | and            | relative    | humidity        | at       |     |     |     |     |     |     |
| pressure         | levels       | (from        | 1,000hPa       | up             | to 100hPa), |                 | and the  |     |     |     |     |     |     |
| near-surface     |              | variables:   | mean-sea-level |                | pressure    |                 | (MSLP),  |     |     |     |     |     |     |
| 2 m air          | temperature, |              | total          | precipitation, |             | latent          | and sen- |     |     |     |     |     |     |
| sible heat       | fluxes       | and          | 10 m           | horizontal     | wind        | components.     |          |     |     |     |     |     |     |
Besides,sea-surfacetemperature(SST)fromERA5isalso
used.
Fortheconvectiveactivityanalysisassociatedwiththe
| cyclone,     | brightness | temperature        |              | from | the      | Geostationary |            |     |     |     |     |     |     |
| ------------ | ---------- | ------------------ | ------------ | ---- | -------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- |
| IR Channel   | Brightness |                    | Temperature  |      | (BT)     | – GridSat-B1  |            |     |     |     |     |     |     |
| Climate      | Data       | Record             | (CDR)        | is   | used.    | Global        | BT data    |     |     |     |     |     |     |
| are obtained |            | from geostationary |              |      | infrared | (IR)          | satellites |     |     |     |     |     |     |
| (Knapp       | and NOAA   |                    | CDR Program) |      | and      | are available | at         |     |     |     |     |     |     |
https://www.ncei.noaa.gov/products/climate-data-records
| /geostationary-IR-channel-brightness-temperature. |     |     |     |     |     |     | This |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
datasethasatime-frequencyof3hrandhorizontalreso-
|     |     |     |     |     |     |     |     | FIGURE | 1 Domainofsimulationandstudyarea |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------------------------- | --- | --- | --- | --- |
0.07◦×0.07◦
| lution of |     |     | of longitude |     | by latitude | from | 1980 |     |     |     |     |     |     |
| --------- | --- | --- | ------------ | --- | ----------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
(southwesternSouthAtlanticOcean)[Colourfigurecanbeviewed
| tothepresent. |     |     |     |     |     |     |     | atwileyonlinelibrary.com] |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |

2994 REBOITAetal.
Gozzoetal.(2014)anddeJesusetal.(2021a).Thus,these 2.3 Frontogenesis
values were chosen to be applied here to determine the
subtropicalphaseofRaoni. Frontogenesisandfrontsaredefinedbyhorizontalgradi-
Besides CPS, an efficient way to evaluate the time ents in density (expressed through temperature changes,
evolution of the thermal structure and other features e.g.HoskinsandBretherton,1972).Inthissense,Thomas
of cyclones is through vertical cross-sections of mean and Schultz (2019) highlight that it is more adequate to
windintensityandzonaldeviationoftemperaturefocused identify fronts using air temperature or potential tem-
on the cyclone centre. These vertical cross-sections are perature than 𝜃 since it is influenced by the moisture
e
obtainedasfollows:(a)thelatitudeofthesurfacecyclone content of the air (see the advantages and disadvantages
centre is identified; (b) the coordinate obtained in (a) is of using these variables in table 2 from Thomas and
usedasthecentreofaboxof2◦ latitudeby10◦ longitude Schultz (2019)). Although there are different methodolo-
(i.e.1◦ northandsouthand5◦ westandeast)toperform giestotheobjectiveidentificationoffronts(Hewson,1998;
theaverageoftheairtemperature(foreachtimestepand Ribeiroetal.,2016;ThomasandSchultz,2019),wefollow
vertical level), which characterises the cyclone environ- Schultzetal.(1998),whorecommendusingthefrontoge-
ment just in its centre; (c) the same coordinate obtained neticfunction(F)derivedoriginallybyPetterssen(1936).
in (a) is used to define a box of 2◦ latitude by 30◦ longi- F is the Lagrangian rate of change of the magnitude of
tudeinordertocomputetheairtemperature(foreachtime
thehorizontaltemperaturegradient(𝛁⃗
T)duetothehor-
stepandverticallevel)representativeofthezonalenviron- izontalwind,whichidentifiestheregionswherethehor-
ment in which the cyclone is embedded; finally, (d) the izontalflowcreatesfrontogenesisand/orfrontolysis.F is
timeevolutionoftheverticalcross-sectionconsideringthe computedas:
subtraction (b) – (c) is obtained. For wind, we only
computed the mean wind intensity considering a box of F = 1 |𝛁⃗ T|(Ecos2𝛽−D), (3)
2◦ latitude by 10◦ longitude in relation to the cyclone 2
centre. where𝛽isthelocalanglebetweenthetemperatureandthe
Verticalcross-sectionsofequivalentpotentialtemper-
a(xis of dilatat)ion, D is the divergence of horizontal wind
ature (𝜃 e ) and potential vorticity (PV) are also analysed D= 𝜕u + 𝜕v andEisthedeformationgivenby:
inthecyclonecentre.Forthisreason,𝜃 (Bolton,1980)is 𝜕x 𝜕y
e
calculatedas:
( )
1
E= E2 +E2 2 , (4)
st sh
( )
𝜃 e =𝜃 exp L c c q T , (1) where E st = 𝜕 𝜕 u x − 𝜕 𝜕 y v is the stretching deformation, and
p
E =
𝜕v
+
𝜕u
is the shearing deformation. F was com-
sh 𝜕x 𝜕y
where 𝜃 is the potential temperature in K, T the air puted at 850 and 700hPa and then averaged. F has been
temperature in K, q the specific humidity in kg⋅kg−1, L commonly applied in studies related to fronts and extra-
c
the latent heat of condensation at 0 ◦C (2.5×106J⋅kg−1), tropical cyclones, such as Reboita et al. (2009), Brâncus¸
and c the specific heat of dry air at constant pressure etal.(2019),Zhaoetal.(2020),andReederetal.(2021).
p
(1,004J⋅K−1⋅kg−1).
PV in isobaric coordinates (Reed, 1955) is calculated
as: 2.4 Numericalexperiments
[ ]
( )𝜕𝜃 𝜕𝜃 𝜕v 𝜕𝜃𝜕u Two idealised experiments are performed with the
PV=−g 𝜁 +f − + , (2)
p 𝜕p 𝜕x𝜕p 𝜕y𝜕p Weather Research and Forecasting (WRF) model version
3.8.1, a non-hydrostatic and incompressible atmospheric
wheregisthegravityacceleration,𝜁 p istheverticalcom- model with terrain-following vertical coordinate (Ska-
ponent of the relative vorticity at constant pressure sur- marock et al., 2008). The control experiment (CTRL)
face, f is the Coriolis parameter, and u and v are the includes all physical parametrizations, while a sensitiv-
zonalandmeridionalwindcomponents.Byconservation, ity experiment excludes the sensible and latent surface
where one term changes, the other must compensate for heat fluxes (NOFLUX). Both experiments have the
the difference. The unit of PV is normally expressed as same configurations (41 vertical levels and horizontal
1PVU=1×10−6 m2⋅K⋅s−1⋅kg−1.Byconvention,cyclonic grid spacing of 12km in a domain covering most of SA
vorticity results in negative values of PV in the Southern (Figure 1) and physical parametrizations (Kain–Fritsch
Hemisphere. convective scheme, Thompson microphysics, CLM4
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
See
the Terms
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
use; OA
articles
are
governed
by
the
applicable
Creative
Commons
License

REBOITAetal. 2995
land-surface interactions, Mellor-Yamada Nakanishi and isobar,neartheboundaryofBrazilandUruguay(at30◦S,
Niino–MYNN–surfacelayer,MYNNlevel2.5boundary 55◦W; Figure 3b) is formed embedded in the elongated
layer as described in Skamarock et al. (2008)), except by isobar pattern between Paraguay (where there is a ther-
theturn-offoftheturbulentfluxesintheNOFLUXexper- mal low) and the coast of southern Brazil. At this time,
iment.WRFisdrivenbyERA5atmosphericvariablesand CPS shows that the cyclogenesis (indicated with a letter
SST. The simulations start at 0000 UTC 26 June (18hr A)hasextratropicalfeaturessinceB≫10m,−V L∼−200
T
beforethecyclogenesis)andfinishat0000UTC1July. and−V U ∼−400(Figure2b,c).Theverticaldistribution
T
of air temperature zonal deviations and of wind speed at
thecyclonecentreonthecyclogenesisdayalsoshowsthe
3 RESULTS extratropicalnature:colderairoccupiesallverticaldepth
(Figure4a)andthemostintensewindsarelocatedatupper
3.1 Overviewofthesynopticevolution levels(Figure4b).
From 0000 to 1200 UTC 27 June (Figure 3c–e), the
Thecyclonetrackalongitslifecycle,accordingtoERA5, upstream mid-level ridge amplifies southward of the
is shown in Figure 2a. Cyclogenesis occurs near the trough;withthispattern,thecoldairtendstobetrapped
boundary of Uruguay and Brazil. The cyclone moves inthecentreofthetrough,originatingacut-offlow,which
southward over the SAO, reaching its most austral posi- canbeidentifiedbytheclosedthicknesslines(Figure3e).
tion (39◦S) at 0000 UTC 28 June (being semi-stationary Onthesurface,thereisanupstreammigratoryanticyclone
duringthatday),thenitacquiresananomaloustracktothe thatfollowstheridgepatternatmid-levels.Moreover,the
northeastanddecaysnear26◦Sat1800UTC1July2021. surfacecyclonedeepensandinteractswiththemigratory
To discuss the synoptic evolution of the cyclone, we anticyclone(alreadyeastoftheAndes);thentheyadvect
show in Figure 3 the most representative time steps coldairfromhigherlatitudestocontinentalSA(Figure3e).
of this system from 26 June to 1 July 2021. At 0600 At0000UTC28June(Figure3f),thereisapatternresem-
UTC 26 June, there is a trough at mid-levels with its blingadipoleblockingat250hPa(cut-offlownorthward
axis(northwest–southeastorientated)extendingfromthe ofananticyclone).Thecut-offlowisnotyetinphasewith
SouthPacifictotheSAO,crossingArgentina(Figure3a). the surface cyclone, but it helps to decrease the vertical
From 0600 to 1800 UTC 26 June, the trough remains wind shear since there is a bifurcation of the upper-level
semi-stationarywhileanupstreamridge(shownthrough westerlies around the blocking pattern, contributing to
the zigzag yellow line) amplifies reaching the southern- organising convection in the vertical column. These pro-
most tip of SA and the SAO (Figure 3a,b). Cyclogene- cessesareimportanttothesurfacecyclonestrengthening,
sis occurs at 1800 UTC 26 June, when a small closed anditacquiresfeaturesoftheShapiro–Keysermodel(see
FIGURE 2 (a)ERA5cyclonetrack
(linesanddots)atevery6hrfromgenesis
(1800UTC26June)tolysis(1800UTC1
July).Cyclonephasespace(CPS)parameters
ateach6hr:(b)Bversus−V Land(c)–V L
T T
versus–V U.AandZindicate,respectively,
T
cyclogenesisandcyclolysis.Thelegend
below(a)indicatesthemeanradiusof
gale-forcewindsat925hPa(thresholdis
17m⋅s−1)incircleswithdifferentsizesand
MSLP(hPa)incolours[Colourfigurecanbe
viewedatwileyonlinelibrary.com]
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

2996 REBOITAetal.
FIGURE 3 (a–h)Evolutionofthe
synopticenvironmentofthecyclonebased
onERA5from26to29June2021.The
chartsshowMSLP(blacklines,hPa),
1,000–500hPathickness(m;reddashed
lines),andwindintensityat250hPa
(shaded)higherthan30m⋅s−1(indicative
ofupper-leveljets).Thecut-offlow,
thermallow(TL),andthenear-shore
(Raoni)anddetachedextratropicallows
(L)aremarkedinsidethepanels.The
middle-leveltrough(ridge)isidentifiedby
ayellowdashed(zigzag)line.In(f,h)
satelliteimagesdepictthedifferentcloud
bandsfeaturesofthesystem.In(f)is
shownTerraMODIStruecolourcorrected
reflectanceimage(https://wvs.earthdata.
nasa.gov/)andin(h)GOES16visible
channelimage(availableathttps://cimss.
ssec.wisc.edu/satellite-blog/archives/
41296)on28June2021[Colourfigurecan
beviewedatwileyonlinelibrary.com]
discussioninsection3.3).At0000UTC28June(Figure3f), (−V U ≈−20),attainingtheCPSconditionsofasubtrop-
T
the surface near-shore cyclone remains semi-stationary icalcyclone.Thisverticalthermalstructureisalsoshown
and detached from the cold front. The semi-stationarity inFigure4a,whileFigure4bindicatestheintensification
in part is due to the influence of the anticyclone that and weakening of the winds, respectively, at lower and
hampers the southeastward displacement of this low. upperlevels.
Then, the cyclone centre stays in an area with weaker At 0000 UTC 29 June (figure not shown), the block-
verticalshearunderthemid-levelcut-offlow(duetothe ing pattern is slightly shifted to the east, and the cut-off
mid–upper-levelblockingpattern). lowandthesurfacecyclonearealmostinphase.Thecom-
From0000to0600UTC28June,theatmosphericpat- plete coupling occurs at 1200 UTC at the same time that
terns practically do not show any important difference the cyclone moves to the west and reaches the Brazil-
(Figure3f,g),buttheCPSindicatestheoccurrenceofthe iancoast(Figure3h),receivingthenameRaonifromthe
subtropicaltransition(Figure2a,b).At0600UTC28June Brazilian Navy as highlighted in Figure 4. At this time,
(Figure 3g), the CPS diagram (Figure 2b,c) shows that thenear-shorecyclonecirculationiscompletelydetached
thecyclonehasthermalsymmetry(B≈23m),warm-core fromthecoldfront,whichisbeingpushedsoutheastward
at low levels (−V L ≈110) and cold-core at upper levels byaweakersecondarylow-pressurecentreof1,010hPaat
T
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

REBOITAetal. 2997
FIGURE 4 Timeevolutionofverticalcross-sectionsofthe(a)zonaldeviationofairtemperature(◦C)and(b)meanwindintensity
(m⋅s−1)calculatedinaboxcentredinthecyclonecore(videtextfordetails).Thephasesofthecycloneareindicatedinverticallines:
cyclogenesis,subtropicaltransition,andsynoptictimewhenthecycloneisnamedRaonibytheBrazilianNavy.TheShapiro–Keyser
extratropicalcyclonephaseisindicatedwithablackhorizontalline[Colourfigurecanbeviewedatwileyonlinelibrary.com]
approximately43◦S,38◦W(Figure3h).Atthistime,deep of the surface cyclone does not show relevant changes,
convection is organised around the near-shore cyclone exceptbyitsnortheastwardmovement.At0000UTC1July
centreresemblingatropicalcycloneasshownbythesatel- (figurenotshown),theblockingpatternisweakenedand
liteimageatthetopofFigure3h.AccordingtoHart(2003), the subtropical system weakens as well. From this time,
acyclonewithpuretropicalstructurepresentsCPSparam- theintensemigratorypost-frontalanticyclonetothewest-
eters’ values of −10m< B <10m, −V L >0 and, in at /southpushesthecyclonetothenortheast(Figure2a),as
T
least one time step, −V U >0. The latter condition is amesoscalesystem,stillembeddedintheanticyclonecir- T
equivalent to winds at upper levels being weaker than at culation.Raonidecaysat1800UTC1July,and,according
lower levels. During Raoni evolution, these tropical sig- toCPS(Figure2b,c),itoccurswithsubtropicalfeatures.
natures are not verified either in CPS (in which Raoni
shows −V U closer to −50 in only one time step and
T
never reaches positive values; Figure 2c) or in the verti- 3.2 Physicalprocessesofcyclogenesis
cal profiles of wind speed (where the upper-level winds
are always stronger than at low levels; Figure 4b). More- Itisknownfrompreviousstudies(e.g.Seluchi,1995;Vera
over, Figure 4a does not show a positive zonal deviation et al., 2002; Gan and Reboita, 2016; Crespo et al., 2020b)
of temperature throughout the whole tropospheric col- that troughs at mid–upper levels crossing the Andes dis-
umn, which is a basic characteristic of tropical cyclones turbtheMSLPoverthecontinentandthetypicalconfig-
(e.g. Hart, 2003; Chang et al., 2019). Instead, there is a uration is an isobar showing a connection between the
colderlayerbetween500and300hPa,whichisacommon thermallow(TL)locatedoverBolivia/Paraguay/Argentina
pattern observed in subtropical cyclones. Thus, despite (near 20oS) and the low-pressure area in southern Brazil
its appearance (Figure 3h, top), Raoni did not reach the and Uruguay, as shown in Figure 3a,b. Cyclogenesis will
tropicalphase(thisaffirmationissupportedbythenumer- occur near the east coast of SA only when other “ingre-
ical simulations in Section 3.5). It can be also illustrated dients” feed into the surface pressure deepening, such
by comparing Raoni’s features to hurricane Iba (Reboita as intensification of the surface horizontal temperature
et al., 2021). Subtropical and tropical cyclones classifica- gradientsoramoisturefluxconvergence.
tionbasedonreanalysisshouldbetakencarefullysinceits Indeed, the cyclogenesis at 1800 UTC 26 June 2021
relativelycoarseresolutionmayimplyshallowwarmcores over the boundary between Uruguay and extreme south
as well as it may affect CPS parameters (in other words, Brazil (Figure 3b) may be explained by the classical
reanalysiscanbeasourceofuncertainty).However,inthis mechanismofcyclogenesisinRG2(Figure5a):massdiver-
study, as ERA5 and simulations (Section 3.5) have great gence eastward of a pronounced trough at mid–upper
similarities,wedidnotfacethedescribedissues. levels travelling from the Pacific to the Atlantic Ocean
From 1800 UTC 29 June to 1800 UTC 30 June (Seluchi,1995;Reboitaetal.,2012;GanandReboita,2016).
(figures not shown), the mid-level ridge acquires a more Inaddition,asthecyclogenesisoccursundertheequato-
meridionalconfiguration.However,thesynopticsituation rialsideoftheentranceoftheupper-leveljetstreaknear
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

 1477870x, 2022, 747, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349 by Univ of Sao Paulo - Brazil, Wiley Online Library on [15/12/2024]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 2998 |     |     |     |     |     |     |     |     |     |     |     |     | REBOITAetal. |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |
37◦S,50◦W(Figure3b),theupper-leveldivergencefavours warm front (red line in Figure 5f–h), a common feature
the column upward motion and, consequently, surface of the Shapiro–Keyser extratropical cyclone model.
pressure drop, characterising the cyclogenesis (Crespo The position of the axis of dilatations that are con-
et al., 2020b). The cyclogenesis also occurred in a baro- tributing to the warm frontogenesis is indicated by
clinicregionatthesurface,asshownbythe1,000–500hPa light blue lines in Figure 5f,g. Intense warm advec-
thickness (Figure 3a,b), and with moisture convergence tion (by the northerly winds over continental South
flux(figurenotshown). America) towards the warm front also helps to increase
Another important feature of the studied cyclone is frontogenesis in the warm sector, as illustrated in
its fast-deepening rate. During 24hr, from 0000 UTC Figure 5e–g. Frontolysis is separating the cold and
27 to 0000 UTC 28 June, the cyclone deepening rate warm fronts in Figure 5f,g, which indicates the frontal
| reached | 22hPa. | Using | the Sanders | and | Gyakum | (1980) | fracture. |     |     |     |     |     |     |
| ------- | ------ | ----- | ----------- | --- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- |
formulation of the Normalised Central Pressure Deepen- Amoredetailedexplanationofhowthecyclonebears
ingRate(NDR),thecyclonereached1.33NDR,whichis resemblance to stages I, II, III and IV of the Shapiro
enough to classify it as a moderate (1.3≤NDR<1.8; see –Keyser conceptual model is presented in Figure 6,
through𝜃
Sanders(1986))explosiveextratropicalcyclone.Recently, andairtemperaturefieldsat850hPa.
e
Avilaetal.(2021)documentedsixexplosivecyclonesfrom
| 2012 to 2014 | over | the SAO | that | developed | following | the |     |     |     |     |     |     |     |
| ------------ | ---- | ------- | ---- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
• StageI:thelow-pressurecentreandthewarmandcold
Shapiro–Keysermodel,reinforcingthatthisisacommon frontsdevelopinabarocliniczone(Figures5eand6a).
developmentpathforexplosivecyclones.
|     |     |     |     |     |     |     | • Stage | II: a | weakening        | occurs | in     | the baroclinic | zone      |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------------- | ------ | ------ | -------------- | --------- |
|     |     |     |     |     |     |     | (marked | by    | the frontolysis, |        | Figure | 5f) along      | the pole- |
wardportionofthecoldfrontnearthelowcentreand
| 3.3 | FromShapiro–Keyser |     |     |     |     |     |              |     |          |         |          |        |            |
| --- | ------------------ | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------- | -------- | ------ | ---------- |
|     |                    |     |     |     |     |     | this feature |     | is named | frontal | fracture | (thick | green line |
tosubtropicalcyclone
inFigure6b).Thebaroclinicityweakeningisassociated
|         |      |            |     |             |         |     | with | axes of | dilatation | (also | represented |     | by the green |
| ------- | ---- | ---------- | --- | ----------- | ------- | --- | ---- | ------- | ---------- | ----- | ----------- | --- | ------------ |
| Studies | such | as Schultz | et  | al. (1998), | Schultz | and |      |         |            |       |             |     |              |
lineinFigure6b)lyingalmostperpendiculartotheisen-
| Wernli (2001) |     | and Schultz |     | and Zhang | (2007) | show |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
35◦S,
|                 |     |               |     |          |      |           | tropes, | near | which | leads | to  | the spreading | of the |
| --------------- | --- | ------------- | --- | -------- | ---- | --------- | ------- | ---- | ----- | ----- | --- | ------------- | ------ |
| that baroclinic |     | perturbations |     | embedded | in a | confluent |         |      |       |       |     |               |        |
isentropes(frontalfracture).Slightlysouthwardof35◦S,
backgroundflowhavealower-troposphericfrontalstruc-
thereisanotheraxisofdilatation(thicklightbluelines
| ture and | evolution | following |     | the Shapiro–Keyser |     | model |     |     |     |     |     |     |     |
| -------- | --------- | --------- | --- | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
inFigures5fand6b)associatedwiththelarge-scaleflow
(azonallyorientedcyclone,strongwarmfront,bent-back
|            |     |      |             |     |           |           | and responsible |     | for | the zonal | orientation |     | of the warm |
| ---------- | --- | ---- | ----------- | --- | --------- | --------- | --------------- | --- | --- | --------- | ----------- | --- | ----------- |
| warm front | and | warm | seclusion), |     | since the | confluent |                 |     |     |           |             |     |             |
front.
| flow stretches | the | cyclones | and | fronts | in the zonal | direc- |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --- | ------ | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
• StageIII:thewarmfrontdevelopszonallysouthwardof
| tion. On | the other | hand, | baroclinic | perturbations |     | within |     |     |     |     |     |     |     |
| -------- | --------- | ----- | ---------- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
a diffluent background have frontal structure and evo- theamplifiedfracture(Figures5gand6c);theportionof
thewarmfrontsouthwesttothecyclonecentreconfig-
| lution of | the Norwegian |     | cyclone | model | (a meridionally |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ------- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
oriented cyclone, strong cold front, and occlusion) since urestheso-calledbent-backwarmfront(Figure6c),and
alongwiththecoldfrontdisplaysaT-bonepattern.The
thediffluentflowstretchesthecycloneinthemeridional
warmfrontalsointensifieseastwardasaconsequence
direction.Despitetheformationofwarmseclusionsinthe
later stages of all Shapiro–Keyser cyclones, they are not of strong frontogenesis associated with the large-scale
confluentflow.
constrainedtoacquiresubtropicalcharacteristics.Rather,
subtropical cyclogenesis following seclusion is the less • StageIV:thewarm-coreseclusionformsatthelowcen-
frequent case in the later stages of the Shapiro–Keyser tre(Figure6d).Theverticaltemperatureaverageprofile
model since cyclones acquire Norwegian model charac- (Figure 4a) evidences the presence of this warm core
teristics (Schultz and Zhang, 2007). Indeed, case-studies fromthesurfaceupto∼600hPaon27June(priortothe
for the SAO show that many Shapiro–Keyser cyclones subtropicaltransition).At0000UTC28June,avertical
did not undergo subtropical transition (Dias Pinto and cross-section highlights this warmer air with 𝜃 rang-
e
39◦S
da Rocha, 2011; Gozzo and da Rocha, 2013; Reboita ing from 280 to 309K near (Figure 7) separating
| etal.,2017). |     |     |     |     |     |     | thecoldairmassintwobranches:onetothesouthand |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
Raoni’s precursor extratropical cyclone developed theothertothenorth.Intensecyclonicvorticityandthe
under a downstream confluent flow at upper (figures largeregionofstabilityatlowerlevelsareduetolatent
not shown) and lower (Figure 5e–h) levels. Large-scale heat release. The strengthened circulation and closer
confluence acts to orient the axes of dilatation zonally isentropes caused by the latent heat release increased
over the cyclone region, resulting in a zonally oriented PV in the mid–lower troposphere (Figure 7). The cold

REBOITAetal. 2999
FIGURE 5 (a–d)850–250hPavertical
windshear(m⋅s−1;shaded),geopotential
height(m;blacklines)at250hPa,andmass
divergenceat250hPahigherthan2×10−5s−1
(whitelines)fromERA5.In(a)isalsoshown
theconceptualmodelofRossbywavebreaking
intheSouthernHemispherebasedonPostel
andHitchman(1999).The250hPatrough
(ridge)isindicatedinblackdashed(zigzag)
line,blackarrowshighlightthelarge-scale
confluentflowandthewhiteLindicatesthe
lowpositionbasedonMSLP.(e–h)
Frontogeneticfunction(×10−10K⋅m−1⋅s−1;
shaded)averagedbetween850–700hPaand
streamlinesat850hPa.Thelowpositionbased
onMSLPisindicatedbyL,thecolouredlines
indicatethecold(darkblue)andwarm(red)
fronts,thefrontalfracture(green)andthe
dilationaxisofthehorizontalwind(lightblue),
andblackarrowshighlightthelarge-scale
confluentflow[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
front(characterisedbyanintensehorizontalgradientof (Figure6),whichagreeswiththeShapiro–Keysermodel.
𝜃 atlowlevels)islocatedtothenorth,inthesubtropics Inthewarmseclusionstage,thesurfacecycloneislocated e
(∼25◦S),awayfromthewarmseclusion. onthepolewardsideofthe250hPajetstream(Figure3g).
Thisisacommonpositioningofallextratropicalcyclones
The warm-core seclusion air has lower temperatures in their occlusion (Norwegian model) or warm seclusion
thanthoseinitiallywithinthewarmsectorofthecyclone (Shapiro–Keysermodel)stages.Fromthispoint,cyclolysis
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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
the applicable
Creative
Commons
License

3000 REBOITAetal.
usuallybegins.However,inthisunusualcase,thecyclone
strengthenedandunderwentsubtropicaltransitionandin
winter, a season that is less preferential for subtropical
cyclonedevelopment.
Based on ERA5, the warm seclusion (Figure 6d) is
formed in a weak vertical wind shear environment pro-
pitiatedbytheverticalalignmentwiththemiddle–upper
tropospheric cut-off low (Figure 5d). Weak vertical shear
allows the convection to be organised, and, indeed,
from 1200 UTC 27 to 0000 UTC 28 June, visually the
cloudsbecomemoreorganisedaroundthecyclonecentre
(Figure8d–k),differingfromitsinitialphase(Figure8a–c).
Cloudiness in its turn is evidence of diabatic heat-
ing (latent heat release from condensation), which is
a feedback mechanism since this heating can be used
to strengthen the convection itself, contributing, conse-
quently, to decreasing the surface pressure. More evi-
dence of the diabatic heating is the presence of strong
PV at low levels in the region of the warm seclusion
(Figure 7). These features show some similarities with
Shapiro–Keysercyclonesthatundergosubtropicaltransi-
tion over the North Atlantic Ocean (Quitián-Hernández
etal.,2020).
Here we summarize remarkable differences between
warm seclusion on Shapiro–Keyser cyclones that did not
undergo subtropical transition over the SAO (Dias Pinto
and da Rocha, 2011; Gozzo and da Rocha, 2013) and
a transitioning cyclone over the North Atlantic Ocean
(Quitián-Hernández et al., 2020). In the former case, the
FIGURE 6 Leftside:Snapshotsoftheextratropicalcyclone
cyclones move faster, while in the latter case it remains
stagesfollowingtheShapiro–Keyser(1990)modelshowingthe
semi-stationary. At upper levels, the cyclone environ-
MSLPandfronts(top),andthepotentialtemperatureat850K
ment also differs, with the first case linked to a broad (bottom);rightside:𝜃 (K;shaded)andairtemperature(◦C;white
e
trough connected to the midlatitude flow, while the lat- lines)at850hPahighlightingtheShapiro–Keyserstructureofthe
ter one was coupled to a mid-tropospheric cut-off low. cyclone.(a)Initialphase,(b)frontalfracture,(c)bent-backfront
Bythiscomparison,andnotingthatRaoniseemedtofol- andT-bone,and(d)warmseclusion.In(b,c)thelinesindicatethe
low a development path similar to the second case, we frontalfracture(green)andthedilationaxisofthehorizontalwind
suggest that the subtropical transition was supported by (lightblue)[Colourfigurecanbeviewedatwileyonlinelibrary.com]
the cut-off low acting to the semi-stationarity of the sur-
face low (warm seclusion). In this scenario, strong con-
describedinthissection,arediscussedthroughnumerical vection is fuelled by the turbulent surface fluxes from
experimentsinsection3.5.
theoceantotheatmosphere(seesection3.5);latentheat
fluxincreasesthewatervapouramountintheatmosphere
and, then, the convection and its associated condensa-
tional latent heat release (diabatic heating) are strength- 3.4 NOAAclassificationofRaoni,
ened. This process helps to deepen the cyclone and andDvorakTechnique
favoursitsfurthertransition.Indeed,duringnearlyallthe
cyclonelifecycle,itwasoverpositiveSSTanomalies(0.5 Somestudies(e.g.Cohen,2011)highlightthatwarm-core
◦C above the 1979–2021 climatological mean of ERA5) seclusions may resemble the eye of a tropical cyclone.
that were warmer than the overlying air, with total heat At 0000 UTC 28 June, the studied cyclone presents an
fluxes thus acting to warm the atmosphere (figures not area with concentric cloudiness in the centre of the
shown). warm seclusion (Figure 8e), and the persistence of this
The environmental conditions that can have led to feature in the following satellite images led NOAA to
the warm seclusion undergoing a subtropical cyclone, classify the system as a tropical disturbance at 2330
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

 1477870x, 2022, 747, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349 by Univ of Sao Paulo - Brazil, Wiley Online Library on [15/12/2024]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| REBOITAetal. |     |     |     |     |            |           |              |          |        |             |       | 3001   |
| ------------ | --- | --- | --- | --- | ---------- | --------- | ------------ | -------- | ------ | ----------- | ----- | ------ |
|              |     |     |     |     | (which     | can be    | more diverse |          | in the | subtropical | case) | and    |
|              |     |     |     |     | cloudiness | (central  | dense        | overcast | is     | not present | in    | sub-   |
|              |     |     |     |     | tropical   | cyclones, | and          | cloud    | bands  | may not     | be as | well). |
Thus,thecycloneclassificationbasedonlyonDTmustbe
consideredasasourceofuncertainty,suchasinthecase
studiedhere.
|     |     |     |     |     | In a         | nutshell, | Raoni | resembled |          | a tropical     | cyclone   |     |
| --- | --- | --- | --- | --- | ------------ | --------- | ----- | --------- | -------- | -------------- | --------- | --- |
|     |     |     |     |     | on satellite | images,   | but   | the       | vertical | cross-sections |           | of  |
|     |     |     |     |     | temperature  | and       | wind  | (Figure   | 4)       | and of         | 𝜃 (Figure | 7)  |
e
|        |                                                 |     |     |     | together           | with       | the CPS | (Figure     | 2b,c)      | show        | that it evolved |     |
| ------ | ----------------------------------------------- | --- | --- | --- | ------------------ | ---------- | ------- | ----------- | ---------- | ----------- | --------------- | --- |
|        |                                                 |     |     |     | from extratropical |            | to      | subtropical |            | only. These | findings        |     |
|        |                                                 |     |     |     | are supported      |            | by the  | WRF         | simulation |             | presented       | in  |
| FIGURE | 7 Verticalcross-sectionofPV(onlynegativevalues; |     |     |     |                    |            |         |             |            |             |                 |     |
|        |                                                 |     |     |     | section            | 3.5 (where | we      | compared    | vertical   |             | cross-sections  |     |
shaded)and𝜃
e (K;solidlines)at0000UTC28Junecentredonthe and the CPS from ERA5 and WRF) and by the Met
longitudeofthewarmseclusion(52◦W)[Colourfigurecanbe
|     |     |     |     |     | Office | reports, | which | classify | Raoni | as  | a subtropi- |     |
| --- | --- | --- | --- | --- | ------ | -------- | ----- | -------- | ----- | --- | ----------- | --- |
viewedatwileyonlinelibrary.com]
|     |     |     |     |     | cal system |     | (https://www.metoffice.gov.uk/research/ |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
weather/tropical-cyclones/verification/seasons/shem2020
-21; https://twitter.com/metofficestorms/status/14097777
| UTC 28 June | 2021 (https://www.ssd.noaa.gov/PS/TROP/ |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
22692452352).
DATA/2021/bulletins/satl/202106282330IN1.html).
NOAAclassifiesthesystemsbasicallybytheirappear-
anceinsatelliteimagesusingtheDvoraktechnique–DT 3.5 Mechanismstosubtropical
| (Dvorak,   | 1984; Velden    | et al., 2006). Additional |     | details  | transition |     |     |     |     |     |     |     |
| ---------- | --------------- | ------------------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| related to | the methodology | of the bulletins          | can | be found |            |     |     |     |     |     |     |     |
in the document https://severeweather.wmo.int/TCFW/ Figure 8e showed that the clouds around the cyclone
RAIV_Workshop2016/08_DvorakTechnique_JackBeven. centre were detached from the fronts, and the features
pdf.Featuressuchascurvedcloudbands,acentraldense presented in Figures 2b,c and 4 indicated that the extrat-
overcast,awell-definedeyeandstrongconvectionaround ropicalcycloneunderwentsubtropicaltransitionearlyon
the eye are associated with wind speed thresholds and 28June.Thissectionaddressesthequestion“Whichwere
withaspecificnumberintheDvorakscale,rangingfrom0 thephysicalmechanismsassociatedwithwarmseclusion
(pre-storm)to8(hurricane).Thecurvedcloudbandingin detachment from the frontal wave and its transition to a
thelatehoursof28Juneandthestrengtheningofconvec- subtropicalcyclone?”
tionaroundan“eye”ledNOAAtoassignRaoniwiththe As the surface turbulent heat fluxes are supposed
number3.5intheDvorakscale,correspondingtoatropi- to have great importance to the cyclone strengthening
calstorm(Figure8h).Inthefirsthoursof30June,NOAA (section3.3),wecomparetwosensitivitynumericalexper-
degraded Raoni to subtropical disturbance. We show in iments: one with the complete physics (CTRL) and the
section 3.1 that Raoni actually did not achieve tropical other with turbulent heat fluxes turned off (NOFLUX).
phase, but NOAA bulletins’ classification misconception ThetrackandCPSofthesimulatedcycloneineachexper-
is understandable because they do not analyse thermal iment are shown in Figure 9. CTRL (Figure 9b,c) simu-
andkinematicfeaturesofthecyclone(Figures2b,cand4) lates the cyclone with a very similar movement, central
andtheclouddistributionwithinitwasreallysimilartoa pressure and CPS diagrams to ERA5 (Figure 2), while
tropical disturbance. Also, the cloud patterns in Figure 8 NOFLUX (Figure 9d,e) simulates a weaker system with
wereverysimilartoCatarina,thefirstdocumentedtrop- shorter life cycle, without northeastward movement and
ical cyclone over SAO (McTaggart-Cowan et al., 2006), without subtropical transition in the CPS since −V L
T
whichtransitionedfromsubtropicaltotropicalstructure; and −V U are negative during the whole cyclone life
T
thismayalsoexplainthemisguidedclassification. cycle. These findings are clear evidence that the tur-
It is noteworthy that as far back as the 1970s, bulent heat fluxes have a decisive contribution to the
researchers and operational meteorologists were already subtropical transition. Figure 10a,b shows that accu-
facing problems when trying to classify subtropical mulated precipitation along the cyclone track (which
cyclonesusingtheDT.HebertandPoteat(1975)alsohigh- is a proxy of the latent heating in the atmosphere) is
lightedthattheclassicalDTwasleadingtoerrorsinsub- strongerinCTRLthaninNOFLUX.Ithighlightsthatthe
tropicalclassification,duetoenvironmentalandstructural most important physical difference between the experi-
differences such as different vertical wind shear regimes ments occurs exactly when the cyclone was performing

3002 REBOITAetal.
FIGURE 8 (a–l)Evolutionofthebrightnesstemperature(K;greyscale)from26Juneto1July2021.In(h)isshownasnapshotofthe
Dvorakmodel(1984)[Colourfigurecanbeviewedatwileyonlinelibrary.com]
a backward movement, at the time of the subtropical inNOFLUX),andthethermodynamicfactorsacquirerel-
transition. evantrolesforthelow-levelwarmseclusionandsubtrop-
By the 250hPa jet stream configuration in ERA5 ical transition. From the CTRL experiment, the physical
(Figure3)andinthetwoexperiments(Figure11a–d),we explanation is the following: the cut-off low contributes
notethepresenceofaRossbywavebreakingevent(RWB: to supporting the convection with its cold core acting to
PostelandHitchman,1999).RWB,ingeneral,isanenvi- destabilisetheunderlyingatmosphere(McTaggart-Cowan
ronment conducive to cut-off lows formation (Ndarana et al., 2006; Porcù et al., 2007; Singleton and Rea-
and Waugh, 2010; Portmann et al., 2020) since the ridge son, 2007). Cut-off lows, being a kind of atmospheric
amplificationsouthwardofthetroughactstosegregatethe blocking (COMET, 2021), also provide a weakened zonal
coldairequatorward(Figure5a,top).Althoughitisapos- flow, which can be seen by weak vertical wind shear in
sibleexplanation,othermechanismsinducingthecut-off Figures5dand11c,d.Lowwindshearenvironmenthelps
of the trough, such as negative anomalies of PV in the tobuildthecyclone’swarmcoresincetheconvectiveactiv-
upper troposphere (Posselt and Martin, 2004), deserve to ity is taking place (Figure 10) concentrating the latent
beinvestigatedinafuturework. heatreleasedand,consequently,thereisamoreefficient
IntheNOFLUXexperiment,thecut-offlowisstronger heatingoftheatmosphericcolumn.Inbothexperiments,
thaninCTRL(whichisobservedbycomparingthegeopo- thecut-offlowsupportsconvection,butinNOFLUXcon-
tential height isoline of 10,200 gpm in both experiments vection is weaker as shown by the smaller precipitation
inFigure11c,dandfollowingtimesteps,notshown)since rate(Figure10a,b).Consequently,theatmosphericwarm-
inNOFLUX,weakerconvection,withconsequentsmaller ing by convection is smaller (as the atmosphere is not
diabatic heating, does not weaken the mid–upper-level gaining surface latent heat), hindering the warm seclu-
coldcore.Theweakercut-offlowintheCTRLexperiment sion as shown in the 𝜃 field (Figure 11f). Moreover, e
is in agreement with studies that found diabatic heat- Figure12ashowshighervolumesofprecipitationaround
ing as a destructive mechanism of cut-off lows (Hoskins 28 June in CTRL than in NOFLUX. At the same time,
et al., 1985; Garreaud and Fuenzalida, 2007; Pinheiro CTRL simulates an increase of 300W⋅m−2 in the total
etal.,2017;Portmannetal.,2020). heat fluxes from 27 to 28 June (Figure 12b), which can
Asinbothexperiments,themid–upper-levelsdynamic besupportedbythestrongerlow-levelwinds(Figure12c).
issimilar(exceptforthecut-offlowtobeslightlystronger It is a feedback mechanism since more intense low-level
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

REBOITAetal. 3003
FIGURE 9 (a)Cyclonetracks(WRFCTRLisshowningreyandNOFLUXinorange)atevery6hrfromgenesis(1800UTC26June)to
lysis.Cyclonephasespace(CPS)parametersateach6hrfor(b,c)WRFCTRLand(d,e)WRFNOFLUX.AandZindicate,respectively,
cyclogenesisandcyclolysis.Thelegendbelow(a)indicatesthemeanradiusofgale-forcewindsat925hPa(thresholdis17m⋅s−1)incircles
withdifferentsizesandMSLP(hPa)incolours[Colourfigurecanbeviewedatwileyonlinelibrary.com]
windsintensifytheturbulentheatfluxesandithelpsthe heating, which contributes to reducing the vertical wind
deepening of pressure and, consequently, the intensifica- shear. This decrease of the wind shear has an additional
tion of the low-level winds. This process is described by contributionofthebarotropicverticalstructureprovided
thewind-inducedsurfaceheatexchangetheory(WISHE: bythepresenceoftheupper-levelcut-offlow.Therefore,
Emanuel, 1986; Craig and Gray, 1996). On 28 June, the both processes (cut-off low environment with low shear
mean 10 m winds are stronger than 16m⋅s−1 in ERA5, and the low shear associated with diabatic heating) are
14m⋅s−1inCTRLanddonotexceed12m⋅s−1inNOFLUX importanttostrengthenthewarmseclusion,leadingtothe
(Figure12c). surface pressure deepening and increasing the low-level
In the CTRL experiment, the surface cyclone evolves windintensity.
followingtheShapiro–Keysermodel:thereisalower-level Aspreviouslymentioned,thetransitiondrivenbythe
warm core as shown by the CPS (Figure 9b,c)and a pro- surface fluxes seems to be especially favoured when the
nounced warm tongue toward the cyclone centre in the cyclone remains semi-stationary for a period of time.
𝜃 field(Figure11e).Ontheotherhand,NOFLUXdepicts In the case of Raoni, the cut-off low is the structure
e
a lower-level cold core (Figure 9d,e) and no features of that halted it, allowing the surface fluxes to feed and
anisolatedwarmcore(warmseclusion)inFigure11f.At strengthenconvection(Figure10a,b).Themid-levelsteer-
0000UTC28June,thehigher𝜃 valuesinthewarm-core ingmayalsohavebeenthecauseofanotherveryunusual
e
seclusion of the CTRL indicate warmer and moister air behaviour of Raoni: its northeastward movement. Cli-
compared with the NOFLUX (Figure 11e,f). The almost matologically, cyclones move to the southeast over the
uniform warming of the region leads to a weakening of SAO (e.g. de Jesus et al., 2021b), but Raoni moved
the low-level baroclinicity favouring the warm seclusion northeastward both in ERA5 (Figure 2a) and in CTRL
in the CTRL and not in NOFLUX (Figure 11e–h). Dur- (Figure 9a). It occurred mainly between 29 June and
ingRaonidevelopment,thesurfacefluxesacttopromote 1 July, when the semi-stationary cut-off low dissipated
stronger convection with consequent vertical redistribu- and the trough then moved northeastward, steering the
tion/production of PV at low–mid levels due to diabatic surface low in this same direction (figures not shown).
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

3004 REBOITAetal.
FIGURE 10
Accumulatedprecipitation
(mm)every6hfollowingthe
cyclonecentre(boxof
10◦×10o)andtrackfor(a)WRF
CTRLand(b)WRFNOFLUX
experiments;(c)averagedtotal
heatfluxes(W⋅m−2)from26to
30Juneandthecyclonetrack
(blackline)simulatedbyWRF
CTRL,and(d)totalheatfluxes
(W⋅m−2;greenlines)andMSLP
(hPa;blacklines)at1800UTC
29Juneandaccumulated
precipitation(mm;shaded)
between1500and1800UTC29
June2021[Colourfigurecanbe
viewedat
wileyonlinelibrary.com]
The process is similar to the displacement of subtropical lifecyclehadanunusualdevelopment.Initially,itevolved
cyclones steered by the mid-level flow over the north- followingtheShapiro–Keysercyclonemodelandreached
eastern North Atlantic (González-Alemán et al., 2015; the status of explosive cyclone; subsequently, the warm
Quitián-Hernándezetal.,2020).FromFigure10a,wenote seclusionunderwentsubtropicaltransition.Althoughnot
that the cyclone moved towards the region with warmer veryfrequent,anextratropicalcyclonethatreachesexplo-
low-levelconditions,i.e.strongertotalsurfaceheatfluxes. sive status and follows the Shapiro–Keyser model is not
Besides, a surface high-pressure established to the south unusual. But an explosive Shapiro–Keyser cyclone that
ofthecyclone(Figures3g,hand11a,b)inhibiteditssouth- undergoes subtropical transition and moves northeast-
eastwardmovement. ward is, indeed, unusual. And all the more unusual by
While moving northeastward, Raoni did not reach originating a subtropical cyclone during winter, a season
the tropical category, decaying as a subtropical cyclone. wheretheyarerareoverthesouthwesternSouthAtlantic
Although in some synoptic times the apparent eye-like (Gozzoetal.,2014;deJesusetal.,2021a).
featureinthesatelliteimages(Figure8)wouldbeanindi- The main features of the cyclone evolution, which
cationofdeepconvectionsurroundingthecyclonecentre, answerthequestionsposedintheIntroduction,aresum-
itseemstobeincontradictiontoweakobservedandsim- marisedbelow:
ulated precipitation encircling Raoni along its life cycle
(Figure10).Moreover,moreintensevolumesofprecipita- 1. Drivers of cyclogenesis: the classical process in the
tionoccurdisplacedfromthecyclonecentre(tothenorth region, i.e. a trough at mid–upper levels, crossing the
and south, respectively, as exemplified in Figures 10d). AndesMountainsfromtheSouthPacifictotheSouth
Hence, these facts may be a reason why Raoni’s deepen- AtlanticOcean,andthepresenceofhorizontaltemper-
ing stalled. When Raoni approaches the polar side of the aturegradientsinthelowertropospherecontributedto
upper-level jet entrance, it weakens and dissipates by 2 thesurfacelow-pressuredevelopmentnearthebound-
JulyinERA5(figurenotshown). aryofUruguayandsouthernBrazil.
2. Drivers of the Shapiro–Keyser cyclone model: the
extratropical cyclone developed embedded in a
4 CONCLUSIONS low–mid-level confluent large-scale flow. This conflu-
ent flow stretches the warm front zonally, leading to
At1800UTC26June2021,overtheboundaryofUruguay a cyclone with characteristics of the Shapiro–Keyser
andsouthernBrazil,acyclogenesisoccurredthatalongits model: near right-angle between the cold and warm
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

REBOITAetal. 3005
FIGURE 11 Synoptic
environmentin(a,c,e,g)WRFCTRL
and(b,d,f,h)WRFNOFLUXat0000
UTC28June2021.(a,b)Similarto
Figure3;(c,d)similartoFigure5;(e,f)
similartoFigure6and(g,h)similarto
Figure7,butcentredat50◦WinWRF
CTRLand48◦WinWRFNOFLUX
[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
fronts (resembling a T-bone appearance), a frontal Phase Space and inspection of key variables in verti-
fracture(weakeningofthecoldfrontonitspolarside), cal structure) revealed that the thermal structure of
an extension of the warm or occluded front to the the cyclone evolved from extratropical to subtropical,
rearofthecyclone(bent-backfront),andawarm-core without reaching the tropical phase. Therefore, our
seclusion. classificationagreeswiththeBrazilianNavy.
3. Classificationofthesystembythemeteorologicalcen- 4. Drivers of subtropical transition: a mid–upper-level
tres: the satellite images showed a cloudiness pattern cut-off low was important to provide an environment
similar to that of a tropical cyclone, leading NOAA with weak vertical wind shear allowing the organisa-
to classify the system as a tropical cyclone follow- tionoftheconvectionfuelledbythesea–airturbulent
ing the Dvorak technique. However, this classifica- heatfluxesand,consequently,strengtheningthewarm
tion contrasted with the Brazilian Navy which clas- seclusion (similar to Miglietta and Rotunno, 2019;
sified the system as the subtropical cyclone Raoni. Quitián-Hernández et al., 2020; and other studies).
Ourevaluationusingamodernmethodology(Cyclone Weakeningoftheverticalwindshearalsoresultsfrom
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

 1477870x, 2022, 747, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349 by Univ of Sao Paulo - Brazil, Wiley Online Library on [15/12/2024]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 3006 |     |          |            |     |      |            |     |          | REBOITAetal. |     |
| ---- | --- | -------- | ---------- | --- | ---- | ---------- | --- | -------- | ------------ | --- |
|      |     | stronger | convection |     | with | consequent |     | vertical | redistri-    |     |
bution/productionofPVatlow–midlevelsduetodia-
baticheating.Bothprocessesreinforceeachotherand,
|     |     | therefore, | the | warm | seclusion |     | intensifies |     | evolving | to  |
| --- | --- | ---------- | --- | ---- | --------- | --- | ----------- | --- | -------- | --- |
asubtropicalsystem.Throughnumericalexperiments,
|     |     | we confirmed |           | that        | the  | warm     | seclusion    | intensification |             |     |
| --- | --- | ------------ | --------- | ----------- | ---- | -------- | ------------ | --------------- | ----------- | --- |
|     |     | was          | supported | by          | the  | intense  | near-surface |                 | turbulent   |     |
|     |     | heat         | fluxes    | feeding     | more | vigorous |              | convective      | activity.   |     |
|     |     | Numerical    |           | experiments |      | also     | suggest      | that            | the cyclone |     |
didnotevolvetoatropicalsystemduetotheinsufficient
precipitationvolumesandtheiroccurrencefarfromthe
cyclonecentreduringitsnortheastwardmovement.
|     |     | This      | study    | adds | knowledge |     | on cyclone  |     | physics | over  |
| --- | --- | --------- | -------- | ---- | --------- | --- | ----------- | --- | ------- | ----- |
|     |     | the South | Atlantic |      | Ocean     | and | contributes |     | as an   | alert |
tooperationalweatherforecasters.Additionally,itshows
|     |     | the importance    |             | of paying     |              | attention | to         | the development |      |        |
| --- | --- | ----------------- | ----------- | ------------- | ------------ | --------- | ---------- | --------------- | ---- | ------ |
|     |     | of Shapiro–Keyser |             | extratropical |              |           | cyclones,  | since           | they | can    |
|     |     | undergo           | subtropical |               | and tropical |           | transition |                 | even | in the |
coldseason,asoccurredinRaoniandisalsoregisteredin
|     |     | other ocean | basins. |     | The resulting |     | systems | are | difficult | to  |
| --- | --- | ----------- | ------- | --- | ------------- | --- | ------- | --- | --------- | --- |
forecast,andmayhavestrongwindsleadingtodamagein
coastalregions.Consideringourresults,futureclimatolog-
icalstudieswouldbeimportant,tounderstandifthistype
ofeventmaybecomemorefrequentintheregion.
|     |     | AUTHOR    | CONTRIBUTIONS |     |           |                    |              |     |            |        |
| --- | --- | --------- | ------------- | --- | --------- | ------------------ | ------------ | --- | ---------- | ------ |
|     |     | Michelle  | Simões        |     | Reboita:  | Conceptualization; |              |     |            | formal |
|     |     | analysis; | methodology;  |     | software; |                    | supervision; |     | visualiza- |        |
tion;writing–originaldraft;writing–reviewandediting.
LuizFelippeGozzo:Conceptualization;formalanalysis;
|     |     | methodology;       |           | validation;  |              | writing        | – original         |                | draft;      | writ- |
| --- | --- | ------------------ | --------- | ------------ | ------------ | -------------- | ------------------ | -------------- | ----------- | ----- |
|     |     | ing – review       |           | and editing. |              | Natália        | Machado            |                | Crespo:     |       |
|     |     | Conceptualization; |           |              | formal       | analysis;      | methodology;       |                |             | soft- |
|     |     | ware; writing      |           | – original   | draft;       | writing        |                    | – review       | and         | edit- |
|     |     | ing. Maria         | de        | Souza        | Custódio:    |                | Conceptualization; |                |             | val-  |
|     |     | idation.           | Vinícius  | Lucyrio:     |              | Investigation; |                    | software;      |             | visu- |
|     |     | alization.         | Eduardo   |              | Marcos       | de             | Jesus:             | Data           | curation;   |       |
|     |     | resources.         | Rosmeri   |              | Porfírio     | da             | Rocha:             | Conceptualiza- |             |       |
|     |     | tion; formal       | analysis; |              | methodology; |                | software;          |                | validation; |       |
writing–originaldraft;writing–reviewandediting.
| FIGURE 12 | Timeevolutionofthe(a)accumulated | ACKNOWLEDGEMENTS |     |     |     |     |     |     |     |     |
| --------- | -------------------------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
precipitation(mm/6hr−1),(b)totalheatfluxes(latentplus
|     |     | The | authors |     | acknowledge |     | Coordenação |     |     | de  |
| --- | --- | --- | ------- | --- | ----------- | --- | ----------- | --- | --- | --- |
sensible)(W⋅m−2),and(c)10mwindintensity(m⋅s−1)inERA5 Aperfeiçoamento de Pessoal de Nível Superior (CAPES)
(blackline)andWRFsimulations(CTRLingreyandNOFLUXin
|     |     | Finance | Code | 001, | Conselho | Nacional |     | de  | Desenvolvi- |     |
| --- | --- | ------- | ---- | ---- | -------- | -------- | --- | --- | ----------- | --- |
orange)ateach6hrfrom1800UTC26Juneto0000UTC1July. mento Científico e Tecnológico (CNPq Grants Nos.
Notethatin(b)thereisnoinformationforNOFLUXbecauseitis0
|     |     | 430314/2018-3, |     | 304949/2018-3, |     |     | 420262/2018-0, |     | 305304/ |     |
| --- | --- | -------------- | --- | -------------- | --- | --- | -------------- | --- | ------- | --- |
atalltimesteps.Allvariableswerecomputedinaboxof8◦×8◦
2017-8,306488/2020-5)andPETROBRAS(2017/00671-3)
withthecycloneinitscentre[Colourfigurecanbeviewedat
|     |     | for financial |     | support. | We  | also | thank | the | centres | that |
| --- | --- | ------------- | --- | -------- | --- | ---- | ----- | --- | ------- | ---- |
wileyonlinelibrary.com]
providedthedatasetsandfiguresusedinthisstudy.

 1477870x, 2022, 747, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349 by Univ of Sao Paulo - Brazil, Wiley Online Library on [15/12/2024]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| REBOITAetal. |             |     |     |             |           |      |             |     |       |        | 3007   |
| ------------ | ----------- | --- | --- | ----------- | --------- | ---- | ----------- | --- | ----- | ------ | ------ |
| CONFLICT     | OF INTEREST |     |     |             |           |      |             |     |       |        |        |
|              |             |     |     | Craig, G.C. | and Gray, | S.L. | (1996) CISK | or  | WISHE | as the | mecha- |
Theauthorsdeclaretheydonothaveanyconflictofinter- nismfortropicalcycloneintensification.JournalofAtmospheric
Sciences,53(23),3528–3540.
| est; all datasets | used in | the article are | public and the |     |     |     |     |     |     |     |     |
| ----------------- | ------- | --------------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
study was funded by Coordenação de Aperfeiçoamento CrespoN.M.,daRochaR.P.anddeJesusE.M.(2020a)Cyclonesden-
sityandcharacteristicsindifferentreanalysesdatasetoverSouth
dePessoaldeNívelSuperior(CAPES),ConselhoNacional
America.In:EGUGeneralAssembly2020.10.5194/egusphere-
deDesenvolvimentoCientíficoeTecnológico(CNPq)and
egu2020-11316.Online4–8May2020,EGU2020-11316.
PETROBRAS.
|     |     |     |     | Crespo, N.M., | da          | Rocha,    | R.P., Sprenger, |     | M. and          | Wernli, | H.   |
| --- | --- | --- | --- | ------------- | ----------- | --------- | --------------- | --- | --------------- | ------- | ---- |
|     |     |     |     | (2020b)       | A potential | vorticity | perspective     |     | on cyclogenesis |         | over |
centre-easternSouthAmerica.InternationalJournalofClimatol-
ORCID
ogy,41,663–678.https://doi.org/10.1002/joc.6644.
| MichelleSimõesReboita |     | https://orcid.org/0000-0002- |     |           |                |       |        |       |        |        |        |
| --------------------- | --- | ---------------------------- | --- | --------- | -------------- | ----- | ------ | ----- | ------ | ------ | ------ |
|                       |     |                              |     | da Rocha, | R.P., Reboita, | M.S., | Gozzo, | L.F., | Dutra, | L.M.M. | and de |
1734-2395
Jesus,E.M.(2019)Subtropicalcyclonesovertheoceanicbasins:
LuizFelippeGozzo https://orcid.org/0000-0002-7476- areview.AnnalsoftheNewYorkAcademyofSciences,1436(1),
| 6776 |     |     |     | 138–156.https://doi.org/10.1111/nyas.13927. |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
NatáliaMachadoCrespo https://orcid.org/0000-0002- Davis,C.A.andBosart,L.F.(2004)TheTTproblem:forecastingthe
3585-5100 tropicaltransitionofcyclones.BulletinoftheAmericanMeteoro-
MariadeSouzaCustodio https://orcid.org/0000-0001- logicalSociety,85,1657–1662.
|     |     |     |     | de Jesus, E.M., | da  | Rocha, | R.P., Crespo, | N.M., | Reboita, |     | M.S. and |
| --- | --- | --- | --- | --------------- | --- | ------ | ------------- | ----- | -------- | --- | -------- |
5680-4479
Gozzo,L.F.(2021a)Futureclimatetrendsofsubtropicalcyclones
| ViníciusLucyrio | https://orcid.org/0000-0002-9338-8504 |     |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
intheSouthAtlanticbasininanensembleofglobalandregional
| EduardoMarcos | deJesus | https://orcid.org/0000-0002- |     |     |     |     |     |     |     |     |     |
| ------------- | ------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
projections.ClimateDynamics,58(3),1221–1236.https://doi.org/
| 1568-7883 |     |     |     | 10.1007/s00382-021-05958-8. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
RosmeriPorfírio daRocha https://orcid.org/0000- de Jesus, E.M., da Rocha, R.P., Crespo, N.M., Reboita, M.S. and
0003-3378-393X Gozzo,L.F.(2021b)Multi-modelclimateprojectionsofthemain
|     |     |     |     | cyclogenesis | hot-spots |     | and associated |     | winds over | the | eastern |
| --- | --- | --- | --- | ------------ | --------- | --- | -------------- | --- | ---------- | --- | ------- |
coastofSouthAmerica.ClimateDynamics,56,537–557.https://
REFERENCES
doi.org/10.1007/s00382-020-05490-1.
Avila, V.D., Nunes, A.B. and Alves, R.D.C.M. (2021) Comparing DiasPinto,J.R.anddaRocha,R.P.(2011)Theenergycycleandstruc-
explosivecyclogenesiscasesofdifferentintensitiesoccurredin turalevolutionofcyclonesoversoutheasternSouthAmericain
southernAtlantic.AnaisdaAcademiaBrasileiradeCiências,93, threecasestudies.JournalofGeophysicalResearch,116,D14112.
e20190157.https://doi.org/10.1590/0001-3765202120190157. https://doi.org/10.1029/2011JD016217.
Bentley, A.M. and Metz, N.D. (2016) Tropical transition of an Dvorak,V.F.(1984)Tropicalcycloneintensityanalysisusingsatellite
unnamed,high-latitude,tropicalcycloneovertheeasternNorth data, Vol. 11. US Department of Commerce, National Oceanic
| Pacific. MonthlyWeatherReview, |     | 144, 713–736. | https://doi.org/ |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | ------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
andAtmosphericAdministration,NationalEnvironmentalSatel-
10.1175/MWR-D-15-0213.1. lite, Data, and Information Service. https://repository.library.
Bolton, D. (1980) The computation of equivalent potential noaa.gov/view/noaa/19322
temperature. Monthly Weather Review, 108, 1046–1053. Emanuel, K.A. (1986) An air–sea interaction theory for trop-
https://doi.org/10.1175/1520-0493(1980)108<1046:TCOEPT>2.0.
|     |     |     |     | ical cyclones. |     | Part I: | Steady-state | maintenance. |     | Journal | of  |
| --- | --- | --- | --- | -------------- | --- | ------- | ------------ | ------------ | --- | ------- | --- |
CO;2. Atmospheric Sciences, 43(6), 585–605. https://doi.org/10.1175/
Brâncus¸,M.,Schultz,D.M.,Antonescu,B.,Dearden,C.andS¸tefan, 1520-0469(1986)043<0585:AASITF>2.0.CO;2.
S. (2019) Origin of strong winds in an explosive Mediter- Evans, J.L. and Braun, A. (2012) A climatology of subtropical
raneanextratropicalcyclone.MonthlyWeatherReview,147(10), cyclones in the South Atlantic. Journal of Climate, 25(21),
| 3649–3671. |     |     |     | 7328–7340. |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Browning,S.A.andGoodwin,I.D.(2013)Large-scaleinfluenceson Evans, J.L. and Guishard, M.P. (2009) Atlantic subtropical storms.
theevolutionofwintersubtropicalmaritimecyclonesaffecting Part I: Diagnostic criteria and composite analysis. Monthly
Australia’seastcoast.MonthlyWeatherReview,141,2416–2431. WeatherReview,137(7),2065–2080.
https://doi.org/10.1175/MWR-D-12-00312.1. Gan,M.A.andReboita,M.S.(2016)Cyclogenesisandextra-tropical
Chang, M.H., Ho, C.-H., Chan, J.C.L., Park, M.-S., Son, S.-W. and cyclonesoversoutheasternSouthAmerica. Available at: https://
Kim, J.W. (2019) The tropical transition in the western North sites.google.com/site/cmsforsh.[Accessed27August2021].
Pacific:thecaseoftropicalcyclonePeipah(2007).JournalofGeo- Garreaud, R.D. and Fuenzalida, H.A. (2007) The influence of the
physicalResearch:Atmospheres,124,5151–5165.https://doi.org/
|                       |     |     |     | Andes                 | on cutoff | lows: | a modelling | study. | Monthly |     | Weather |
| --------------------- | --- | --- | --- | --------------------- | --------- | ----- | ----------- | ------ | ------- | --- | ------- |
| 10.1029/2018JD029446. |     |     |     | Review,135,1596–1613. |           |       |             |        |         |     |         |
Cohen, J. (2011) Explosive cyclones. In: Schneider, S.H., Root, González-Alemán, J.J., Valero, F., Martín-León, F. and Evans,
T.L.andMastrandrea,M.D.(Eds.)EncyclopediaofClimateand J.L. (2015) Classification and synoptic analysis of subtropical
Weather,Vol.1.Oxford:OxfordUniversityPress,pp.339–344. cycloneswithinthenortheasternAtlanticOcean.JournalofCli-
COMET. (2021) Satellite feature identification: blocking patterns. mate,28(8),3331–3352.
Available at: https://www.meted.ucar.edu/norlat/sat_features/ Gozzo,L.F.anddaRocha,R.P.(2013)Air–seainteractionprocesses
blocking_patterns/navmenu.php?tab=1&page=2-0-0&type=
|     |     |     |     | influencingthedevelopment |     |     | ofaShapiro–Keysertypecyclone |     |     |     |     |
| --- | --- | --- | --- | ------------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- |
flash.[Accessed27August2021]. over the subtropical South Atlantic Ocean. Pure and Applied

3008 REBOITAetal.
Geophysics, 170, 917–934. https://doi.org/10.1007/s00024-012- Mills,G.A.,Webb,R.,Davidson,N.E.,Kepert,J.,Seed,A.andAbbs,
0584-3. D.(2010)ThePashaBulkereastcoastlowof8June2007.CAWCR
Gozzo, L.F., da Rocha, R.P., Gimeno, L. and Drumond, A. TechnicalReport,023,62pp.CentreforAustralianWeatherand
(2017) Climatology and numerical case study of moisture ClimateResearch,Melbourne,Australia.
sources associated with subtropical cyclogenesis over the Ndarana, T. and Waugh, D.W. (2010) The link between cut-off
southwestern Atlantic Ocean. Journal of Geophysical Research: lows and Rossby wave breaking in the Southern Hemisphere.
Atmospheres, 122, 5636–5653. https://doi.org/10.1002/ QuarterlyJournaloftheRoyalMeteorological Society, 136(649),
2016JD025764. 869–885.https://doi.org/10.1002/qj.627.
Gozzo,L.F.,daRocha,R.P.,Reboita,M.S.andSugahara,S.(2014) Petterssen, S. (1936) Contribution to the theory of frontogenesis.
SubtropicalcyclonesoverthesouthwesternSouthAtlantic:cli- Geophysics,11(6),1–27.
matological aspects and case study. JournalofClimate, 27(22), Pezza,A.B.andSimmonds,I.(2005)ThefirstSouthAtlantichur-
8543–8562. ricane:unprecedentedblocking,lowshearandclimatechange.
Gramcianinov, C.B., Hodges, K.I. and de Camargo, R. (2019) The GeophysicalResearchLetters,32,L15712.https://doi.org/10.1029/
propertiesandgenesisenvironmentsofSouthAtlanticcyclones. 2005GL023390.
Climate Dynamics, 53(7), 4115–4140. https://doi.org/10.1007/ Pinheiro, H.R., Hodges, K.I., Gan, M.A. and Ferreira, N.J. (2017)
s00382-019-04778-1. Anewperspectiveoftheclimatologicalfeaturesofupper-level
Hart, R.E. (2003) A cyclone phase space derived from thermal cut-off lows in the Southern Hemisphere. Climate Dynamics,
windandthermalasymmetry.MonthlyWeatherReview,131(4), 48(1),541–559.https://doi.org/10.1007/s00382-016-3093-8.
585–616. doi:10.1175/1520-0493(2003)131<0585:ACPSDF>2.0. Porcù,F.,Carrassi,A.,Medaglia,C.,Prodi,F.andMugnai,A.(2007)
CO;2. Astudyoncut-offlowverticalstructureandprecipitationinthe
Hewson,T.D.(1998)Objectivefronts.MeteorologicalApplications,5, Mediterraneanregion.MeteorologyandAtmosphericPhysics,96,
37–65. 121–140.https://doi.org/10.1007/s00703-006-0224-5.
Hersbach,H.,Bell,B.,Berrisford,P.,Horányi,A.,Muñoz-Sabater,J., Portmann, R., Sprenger, M. and Wernli, H. (2020) The
Nicolas,J.,Peubey,C.,Radu,R.,Schepers,D.,Simmons,A.,Soci, three-dimensionallifecycleofpotentialvorticitycutoffs:aglobal
C., Abdalla, S., Abellan, X., Balsamo, G., Bechtold, P., Biavati, ERA-Interim climatology (1979–2017). Weather and Climate
G.,Bidlot,J.,Bonavita,M.,DeChiara,G.,Dahlgren,P.,Dee,D., DynamicsDiscussions,2020,1–52.https://doi.org/10.5194/wcd-
Diamantakis,M.,Dragani,R.,Flemming,J.,Forbes,R.,Fuentes, 2020-30.
M., Geer, A., Haimberger, L., Healy, S., Hogan, R.J., Hólm, Posselt, D.J. and Martin, J.E. (2004) The effect of latent heat
E., Janisková, M., Keeley, S., Laloyaux, P., Lopez, P., Lupu, C., release on the evolution of a warm occluded thermal
Radnoti,G.,deRosnay,P.,Rozum,I.,Vamborg,F.,Villaume,S. structure. Monthly Weather Review, 132(2), 578–599.
andThépaut,J.-N.(2020)TheERA5globalreanalysis.Quarterly doi:10.1175/1520-0493(2004)132<0578:TEOLHR>2.0.CO;2.
JournaloftheRoyalMeteorologicalSociety,146(730),1999–2049. Postel, G.A. and Hitchman, M.H. (1999) A climatology of
Hebert, P.J. and Poteat, K.O. (1975) A satellite classification tech- Rossby wave breaking along the subtropical tropopause.
nique for subtropical cyclones. NOAA Technical Memorandum Journal of the Atmospheric Sciences, 56(3), 359–373.
NWSSR-83.SouthernRegion,NationalWeatherService:Scien- doi:10.1175/1520-0469(1999)056<0359:ACORWB>2.0.CO;2.
tificServicesDivision. Quitián-Hernández, L., González-Alemán, J.J., Santos-Muñoz, D.,
Hoskins,B.J.andBretherton,F.P.(1972)Atmosphericfrontogenesis Fernández-González, S., Valero, F. and Martín, M.L. (2020)
models:mathematicalformulationandsolution.Journalofthe Subtropical cyclone formation via warm seclusion develop-
AtmosphericSciences,29(1),1–37. ment: the importance of surface fluxes. JournalofGeophysical
Hoskins,B.J.,McIntyre,M.E.andRobertson,A.W.(1985)Ontheuse Research:Atmospheres,125,e2019JD031526.https://doi.org/10.
andsignificanceofisentropicpotentialvorticitymaps.Quarterly 1029/2019JD031526.
Journal of the Royal Meteorological Society, 111(470), 877–946. Reboita,M.S.,Ambrizzi,T.anddaRocha,R.P.(2009)Relationship
https://doi.org/10.1002/qj.49711147002. betweenthesouthernannularmodeandSouthernHemisphere
Knapp, K.R., NOAA CDR Program. (2014) NOAA Climate atmospheric systems. Revista Brasileira de Meteorologia, 24(1),
Data Record (CDR) of Gridded Satellite Data from ISCCP B1 48–55.
(GridSat-B1) Infrared Channel Brightness Temperature, Version Reboita,M.S.,Crespo,N.M.,Dutra,L.M.M.,Silva,B.A.,Capucin,B.C.
2. [subset: brightness temperature]. NOAA National Centers anddaRocha,R.P.(2021)Iba:thefirstpuretropicalcyclogene-
for Environmental Information. doi:https://doi.org/10.7289/ sisoverthewesternSouthAtlanticOcean.JournalofGeophysical
V59P2ZKR[Accessed15January2022]. Research:Atmospheres,126,e2020JD033431.
Mazza,E.,Ulbrich,U.andKlein,R.(2017)Thetropicaltransition Reboita,M.S.,daRocha,R.P.,Ambrizzi,T.,Caetano,E.andSuga-
of the October 1996 medicane in the western Mediterranean hara,S.(2012)Dynamicandclimatologicalfeaturesofcyclonic
Sea: a warm seclusion event. Monthly Weather Review, 145, developmentsoversouthwesternSouthAtlanticOcean.Horizons
2575–2595. inEarthScienceResearch,6,135–160.
McTaggart-Cowan, R., Bosart, L.F., Davis, C.A., Atallah, E.H., Reboita, M.S., da Rocha, R.P., Ambrizzi, T. and Gouveia, C.D.
Gyakum, J.R. and Emanuel, K.A. (2006) Analysis of hurricane (2015) Trend and teleconnection patterns in the climatology
Catarina(2004).MonthlyWeatherReview,134,3029–3053. of extratropical cyclones over the Southern Hemisphere. Cli-
Miglietta,M.M.andRotunno,R.(2019)Developmentmechanisms mateDynamics,45,1929–1944.https://doi.org/10.1007/s00382-
forMediterraneantropical-likecyclones(medicanes).Quarterly 014-2447-3.
JournaloftheRoyalMeteorologicalSociety,145(721),1444–1460. Reboita,M.S.,daRocha,R.P.,Ambrizzi,T.andSugahara,S.(2010)
https://doi.org/10.1002/qj.3503. South Atlantic Ocean cyclogenesis climatology simulated by
1477870x,
2022,
747,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349
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
[15/12/2024].
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

 1477870x, 2022, 747, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4349 by Univ of Sao Paulo - Brazil, Wiley Online Library on [15/12/2024]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| REBOITAetal. |     |     |     |     |     |     |     | 3009 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ---- |
regional climate model (RegCM3). Climate Dynamics, 35(7), Seluchi,M.E.(1995)Diagnósticoyprognósticodesituacionessinóp-
1331–1347.https://doi.org/10.1007/s00382-009-0668-7. ticas conducentes a ciclogénesis sobre el este de Sudamérica.
Reboita,M.S.,daRocha,R.P.,deSouza,M.R.andLlopart,M.(2018) GeofísicaInternacional,34(2),171–186.
Extratropical cyclones over the southwestern South Atlantic Shapiro, M.A. and Keyser, D. (1990) Fronts, jet streams, and the
Ocean: HadGEM2-ES and RegCM4 projections. International tropopause.In:Newton,C.W.andHolopainen,E.(Eds.)Extrat-
Journal of Climatology, 38(6), 2866–2879. https://doi.org/10. ropicalCyclones:TheErikPalménMemorialVolume.Boston,MA:
| 1002/joc.5468. |     |     |     |     | AmericanMeteorologicalSociety,pp.167–191. |     |     |     |
| -------------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
Reboita,M.S.,daRocha,R.P.anddeOliveira,D.M.(2019)Keyfea- Singleton,A.T.andReason,C.J.C.(2007)Anumericalmodelstudy
turesandadverseweatherofthenamedsubtropicalcyclonesover of an intense cutoff low pressure system over South Africa.
thesouthwesternSouthAtlanticOcean.Atmosphere,10(1),6. MonthlyWeatherReview,135(3),1128–1150.https://doi.org/10.
Reboita,M.S.,Gan,M.A.,daRocha,R.P.andCustódio,I.S.(2017) 1175/MWR3311.1.
Surface cyclones over austral latitudes: Part II Cases study. Skamarock,W.C.,Klemp,J.B.,Dudhia,J.,Gill,D.O.,Barker,D.,
RevistaBrasileiradeMeteorologia,32(4),509–542. Duda, M.G., X.-Y. Huang, W. Wang, and J.G. Powers, (2008)
Reed, R.J. (1955) A study of a characteristic type of upper-level A description of the Advanced Research WRF version 3 (No.
frontogenesis.JournalofAtmosphericSciences,12(3),226–237. NCAR/TN-475+STR). University Corporation for Atmospheric
Reeder,M.J.,Spengler,T.andSpensberger,C.(2021)Theeffectofsea Research.doi:https://doi.org/10.5065/D68S4MVH
surfacetemperaturefrontsonatmosphericfrontogenesis.Journal Thomas,C.M.andSchultz,D.M.(2019)Whatarethebestthermody-
oftheAtmosphericSciences,78(6),1753–1771. namicquantityandfunctiontodefineafrontingriddedmodel
Ribeiro,B.Z.,Seluchi,M.E.andChou,S.C.(2016)Synopticclimatol- output? BulletinoftheAmericanMeteorologicalSociety, 100(5),
| ogyofwarmfrontsinsoutheasternSouthAmerica.International |     |     |     |     | 873–895. |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- |
JournalofClimatology,36(2),644–655. Vera, C.S., Vigliarolo, P.K. and Berbery, E.H. (2002) Cold season
Sanders, F. (1986) Explosive cyclogenesis in the west-central synoptic-scale waves over subtropical South America. Monthly
North Atlantic Ocean, 1981–84. Part I: Composite structure WeatherReview,130,684–699.
and mean behavior. Monthly Weather Review, 114, 1781–1794. Velden,C.,Harper,B.,Wells,F.,Beven,J.L.,II,Zehr,R.,Olander,
doi:10.1175/1520-0493(1986)114<1781:ECITWC>2.0.CO;2.
|     |     |     |     |     | T., Mayfield, | M., Guard, | C., Lander, M., Edson, | R., Avila, L., |
| --- | --- | --- | --- | --- | ------------- | ---------- | ---------------------- | -------------- |
Sanders,F.andGyakum,J.R.(1980)Synoptic-dynamicclimatology Burton,A.,Turk,M.,Kikuchi,A.,Christian,A.,Caroff,P.and
ofthe“bomb”.MonthlyWeatherReview,108,1589–1606.doi:10. McCrone,P.(2006)TheDvoraktropicalcycloneintensityestima-
1175/1520-0493(1980)108%3C1589:SDCOT%3E2.0.CO;2. tiontechnique:asatellite-basedmethodthathasenduredforover
Schultz, D.M. and Keyser, D. (2021) Antecedents for the 30years. Bulletin of the American Meteorological Society, 87(9),
| Shapiro–KeysercyclonemodelintheBergenSchoolliterature. |     |     |     |     | 1195–1210. |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | ---------- | --- | --- | --- |
Bulletin of the American Meteorological Society, 102(2), Zhao, Y., Fu, L., Yang, C.-F. and Chen, X.-F. (2020) Case study of
E383–E398.https://doi.org/10.1175/BAMS-D-20-0078.1. aheavysnowstormassociatedwithanextratropicalcyclonefea-
Schultz, D. M. and Wernli, H. (2001) Determining midlatitude turing a back-bent warm front structure. Atmosphere, 11(12),
| cyclonestructureandevolutionfromtheupper-levelflow. |                                                       |     |     | Avail- | 1272. |     |     |     |
| --------------------------------------------------- | ----------------------------------------------------- | --- | --- | ------ | ----- | --- | --- | --- |
| able at:                                            | https://ocean.weather.gov/articles/Schultz-Wernli.pdf |     |     |        |       |     |     |     |
[Accessed15August2021].
Schultz,D.M.andZhang,F.Q.(2007)Baroclinicdevelopmentwithin
zonally-varyingflows.QuarterlyJournaloftheRoyalMeteorolog-
|     |     |     |     |     | Howtocitethisarticle: |     | Reboita,M.S.,Gozzo, |     |
| --- | --- | --- | --- | --- | --------------------- | --- | ------------------- | --- |
icalSociety,133(626),1101–1112.https://doi.org/10.1002/qj.87.
L.F.,Crespo,N.M.,Custodio,M.S.,Lucyrio,V.,
| Schultz, D.M., | Keyser, D. | and Bosart, L.F. | (1998) The | effect of |     |     |     |     |
| -------------- | ---------- | ---------------- | ---------- | --------- | --- | --- | --- | --- |
large-scaleflowonlow-levelfrontalstructureandevolutionin deJesus,E.M.etal.(2022)FromaShapiro–Keyser
extratropicalcyclonetothesubtropicalcyclone
midlatitudecyclones.MonthlyWeatherReview,126,1767–1791.
Schultz, D.M., Bosart, L.F., Colle, B.A., Davies, H.C., Dearden, Raoni:Anunusualwintersynopticsituationover
C., Keyser, D., Martius, O., Roebber, P.J., Steenburgh, W.J., theSouthAtlanticOcean.QuarterlyJournalofthe
| Volkert, | H. and Winters, | A.C. (2019) | Extratropical | cyclones: |     |     |     |     |
| -------- | --------------- | ----------- | ------------- | --------- | --- | --- | --- | --- |
RoyalMeteorologicalSociety,148(747),2991–3009.
| a century | of research | on meteorology’s | centerpiece. | Meteo- |     |     |     |     |
| --------- | ----------- | ---------------- | ------------ | ------ | --- | --- | --- | --- |
Availablefrom:https://doi.org/10.1002/qj.4349
| rological | Monographs, 59, | 16.1–16.56. | https://doi.org/10.1175/ |     |     |     |     |     |
| --------- | --------------- | ----------- | ------------------------ | --- | --- | --- | --- | --- |
AMSMONOGRAPHS-D-18-0015.1.