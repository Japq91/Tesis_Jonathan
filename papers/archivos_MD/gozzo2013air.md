PureAppl.Geophys.170(2013),917–934
(cid:2)2012SpringerBaselAG
Pure and Applied Geophysics
DOI10.1007/s00024-012-0584-3
Air–Sea Interaction Processes Influencing the Development of A Shapiro–Keyser
Type Cyclone over the Subtropical South Atlantic Ocean
LUIZ FELIPPE GOZZO 1 and ROSMERI PORFI´RIO DA ROCHA 1
Abstract—This study analyzes the impacts of latent and sen- cyclones especially over oceans. Model experiments
sible heat exchanges between the atmosphere and the ocean in a
carried out with and without surface fluxes reveal a
non-explosive Shapiro–Keyser type cyclogenesis event that
occurredoverthesouthwesternSouthAtlanticOcean.Thesynoptic
wide range of impacts on cyclogenesis. KUO et al.
evolutionshowsarelativelystrongwarmfrontandacoldfrontal (1991) found that the fluxes (specially the moisture
fractureduringthesystem’sdevelopmentandawarmseclusionin flux) are very important in destabilizing the environ-
its mature stage, characterizing a Shapiro–Keyser type cyclone.
ment in which the cyclones develop, favoring their
Numerical experiments with the ARW-WRF Model version 3.3
wereusedtoinvestigatetheinfluencesofsensibleandlatentfluxes intensification.LAGOUVARDOSetal.(2007),studyingan
onthetrackofthesurfacelow,intensityofthefrontsandcoupling explosive cyclogenesis over the Mediterranean Sea,
oftheloweranduppertroposphere.Thesimulationsindicatethatin
showedthatthefluxescanalsobeimportantduringthe
thepresenceofthesefluxesthecycloneunderwentgreaterinten-
sification, had a longer life time and longer trajectory, and cyclone’smaturephase.Ontheotherhand,thefluxes
presented a typical southeastward movement. In the absence of canalsosuppresscycloneintensification,bywarming
these fluxes, the cyclone developed a weaker warm front with
andcoolingthecoldandwarmsectorsofthecyclone,
consequentreductionofdiabaticheatingduetogridscaleprecip-
respectively, with consequent reduction of near-sur-
itation along it. This reduced the negative pressure tendency
southeast of the cyclone center and the surface cyclone moved facebaroclinicity(REEDandSIMMONS,1991;YINLONG
northeastward,showingadecouplingofthelower-andupper-level and MINGYU, 1999). KUO and LOW-NAM (1990) also
waves.Aconsequenceofthisanomaloustrackingisthelocationof
investigated a case in which the fluxes slightly sup-
the surface cyclone beneath the upper-level trough axis, where
there is no upper-level divergence associated with cyclonic vor- pressed the intensification of the cyclone. These
ticity advection contributing to the further system intensification. surface processes may be so important that initial
Numericalexperiments suggestthatfor thisShapiro–Keysertype
cyclogenesis can even be completely absent without
cyclone the air–sea interaction processes are crucial to obtain a
cyclonewithfeaturessimilartotheobservations. them(UCCELLINIetal.,1987).
The role of surface fluxes in the movement of
Keywords: Air–sea interaction, latent and sensible heat
extratropical cyclones presents some controversial
fluxes,cyclogenesis,Shapiro–Keysertype.
resultsaswell.Moststudiesindicatednoimpactinthe
tracking of explosive cyclones (REED and SIMMONS,
1991;LAGOUVARDOSetal.,2007;PIVAetal.,2008),but
1. Introduction
CHENetal.(1983)showedthatanintensesystemover
the Pacific Ocean moves slower in a no-flux experi-
ment, stating that the shallow developing cyclone
Surface sensible and latent turbulent heat fluxes
‘‘was less affected by the upper-level westerlies, and
(SLHF) are an important forcing mechanism for
consequentlysloweditseastwardmovement’’.Quasi-
cyclogenesis,impactingthedevelopmentofmidlatitude
geostrophic theory states that the cyclones move
because they are continuously filled up behind and
deepenedaheadoftheircentersduetochangesinthe
1 Department of Atmospheric Sciences, Institute of upper and lower-level divergence fields, caused by
Astronomy, Geophysics and Atmospheric Sciences, University
the heating of the atmospheric column via thermal
of Sao Paulo, Rua do Matao, 1226, Cidade Universitaria, Sao
Paulo, SP 05508900, Brazil. E-mail: luizfg@model.iag.usp.br; advectionand/ordiabaticprocesses(CARLSON,1998).
rosmerir@model.iag.usp.br

| 918 |     |     |     | L.F.Gozzo,R.P.daRocha |     |     |     |     | PureAppl.Geophys. |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | ----------------- | --- |
Some numerical and observational studies to convection the cyclone structure remains similar,
addressing the influence of SLHF suggested that butthefronts(andnotablythebent-backwarmfront)
these fluxes are likely to play a fundamental role in were weaker. The strong coupling between convec-
cyclogenesisintheSouthAtlanticOcean(SAO),near tive activity and surface fluxes (LESLIE et al., 1987)
the eastern coast of South America. For anexplosive suggests that the latter process could have similar
| cyclogenesis | in this | region, | simulations |     | of PIVA et al. | impact. |     |     |     |     |
| ------------ | ------- | ------- | ----------- | --- | -------------- | ------- | --- | --- | --- | --- |
(2008) showed a weaker cyclone in the absence of The impacts of SLHF in the development of the
latent heat fluxes, while the middle tropospheric SAO Shapiro–Keyser cyclone are analyzed using
features remained unchanged. Considering a long numerical experimentswith the WRF model. We are
period and various cyclone intensities, climatic sim- particularly addressing changes in cyclone tracking,
ulationsofREBOITAetal.(2011)indicatedthat,inthe fronts andvertical structure (coupling between lower
absence of SLHF, the cyclones are weaker and have and upper troposphere) in the absence of SLHF, and
shorter lifetime; the larger impacts were noted over howthesechangesimpactthepressuredecrease.The
systemsinthesubtropicalsector(around20–25(cid:3)S)of work is organized as follows: Sect. 2 describes the
the SAO. A case study by IWABE and DA ROCHA WRFmodel,dataandmethodology;Sect.3presentsa
(2009), using reanalysis and observed data, indicated synoptic description of the studied cyclone; in Sect. 4
that the interactions between SLHF and upper-level the model is validated and the results are discussed;
potential vorticity anomalies were main controlling and Sect. 5 states the conclusions.
factorsofsecondarycyclogenesisinthesouthwestern
SAO.
| In this     | paper     | we analyze | the           | impact | of air–sea |     |                  |     |             |     |
| ----------- | --------- | ---------- | ------------- | ------ | ---------- | --- | ---------------- | --- | ----------- | --- |
|             |           |            |               |        |            | 2.  | Data Description | and | Methodology |     |
| interaction | processes | in the     | non-explosive |        | develop-   |     |                  |     |             |     |
mentofacyclonethatoccurredoverthesouthwestern
|     |     |     |     |     |     | 2.1. Model | Description |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | --- |
SAO,from28May1997to07June1997.Itwasalong-
livedcyclonethatinitsfirstdaysgeneratedstrongnear- Numerical experiments were performed using the
surface winds and high sea waves, shipwrecks and Weather Research and Forecast (WRF) model ver-
sinking ofboats(CAMPOS, 1999;DA ROCHAand CAET- sion 3.3 (SKAMAROCK et al., 2008). The WRF is a
|             |          |     |          |     |             | limited | area, non-hydrostatic | numerical | model | that |
| ----------- | -------- | --- | -------- | --- | ----------- | ------- | --------------------- | --------- | ----- | ---- |
| ANO, 2010). | As shown | in  | DA ROCHA |     | and CAETANO |         |                       |           |       |      |
(2010), the Brazilian Center for Weather Prediction solves the Euler equations in a totally compressible
and Climate Studies (CPTEC) global model 24-h atmosphere, with a terrain-following vertical
| forecastwasunabletopredictthedevelopmentofthis |     |     |     |     |     | coordinate.    |                       |                  |        |         |
| ---------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --------------------- | ---------------- | ------ | ------- |
| system.                                        |     |     |     |     |     | The            | surface layer         | parameterization | used   | follows |
|                                                |     |     |     |     |     | the similarity | theoryofMonin–Obukhov |                  | (MONIN | and     |
Moreover,thiscycloneunderwentalifecyclethat
resembled the Shapiro–Keyser model (SHAPIRO and OBUKHOV, 1954), including the corrections proposed
KEYSER,1990),anupdatedversionofthewell-known by PAULSON (1970) for unstable and by WEBB (1970)
Norwegian model (BJERKNES and SOLBERG, 1922) for stable atmospheric conditions. The moisture
resulting fromthe inclusion ofnewandbetter upper- scaling presents a different formulation to account
foreffectsofverticalmoleculardiffusion(ZHANGand
levelobservations.SCHULTZetal.(1998)showedthat
cyclones moving into a diffluent upper-level flow ANTHES, 1982). The Yonsei University PBL (YSU-
becomes meridionally elongated, developing a PBL) scheme is used to parameterize turbulent
structure similar to the Norwegian model, while vertical diffusion in the planetary boundary layer
cyclones that move into a confluent and more zonal (PBL).Thisschemerepresentsthenextgenerationof
flow tend to develop a structure resembling the MRF-PBL (HONG and PAN, 1996), adding to the
Shapiro–Keyserdescription.Regardingthenumerical counter-gradient flux representation an explicit treat-
|     |     |     |     |     |     | ment of | the entrainment | layer | at the PBL top. | The |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | ----- | --------------- | --- |
simulationsofthistypeofcyclone,NIELSENandSASS
(2003) and KUWANO-YOSHIDA and ASUMA (2008) 5-layer thermal diffusion land-surface model based
showed that in the absence of latent heat release due ontheMM55-layersoiltemperaturemodelisusedto

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 919
provide heat and moisture fluxes over land and sea The ERA-Interim reanalysis dataset developed by
ice grid points (SKAMAROCK et al., 2008). the European Centre for Medium-Range Weather
The longwave radiative processes are parameter- Forecasts(ECMWF;BERRISFORDetal.,2009)wasused
ized using the Rapid Radiation Transfer Model inthesynopticanalysisandforvalidationoftheWRF
(RRTM)scheme based onthe MM5model(MLAWER control simulation. This data is available every 6 h
etal.,1997),whiletheshortwaveradiativeprocesses (0000, 0600, 1200 and 1800 UTC) with a horizontal
are treated in a scheme based in DUDHIA (1989). The resolutionof1.5(cid:3) 9 1.5(cid:3)and37verticallevels.
cumulus parameterization used is the Betts–Miller– Daily means of SLHF over the oceans, with
Janjic scheme, derived from the Betts–Miller adjust- globalcoverageandhorizontalresolutionof1(cid:3) 9 1(cid:3),
mentscheme(BETTS,1986;BETTSandMILLER,1986), fromWoodsHoleOceanographicInstitution(WHOI;
with variabledeep convection profiles andrelaxation Yu et al., 2008) were used to validate the simulated
times that are a function of cloud efficiency (JANJIC, fluxes.
1994). The microphysics processes are resolved by
theGoddardmicrophysicsscheme(TAOandSIMPSON,
2.3. Experimental Design and Methodology
1993).
Two simulations are analyzed. The first one uses
the complete physics available in the WRF (exper-
2.2. Data
iment FLX), and the second is without the surface
The initial and boundary conditions for the WRF heat and moisture fluxes (experiment NOFLX). Both
simulations were provided by FNL-NCEP analyses simulationsuseda30 kmhorizontalresolutioninthe
with a horizontal resolution of 2.5(cid:3) 9 2.5(cid:3), 16 domain shown in Fig. 1, using a Lambert conformal
verticallevelsandtemporalresolutionof12 h.These projection. The horizontal resolution was chosen
data are from the Research Data Archive (RDA), based on the fact that it is fine enough to accurately
which is maintained by the Computational and simulate both synoptic scale and mesoscale (frontal)
Information Systems Laboratory (CISL) at the processesassociated with thesystem.The simulation
National Center for Atmospheric Research (NCAR). startedat0000UTC27May1997andendedat0000
Figure1
Thesimulationsdomainandtopography(inm,shadedwithscaleinthebottom)

| 920 |     |     |     | L.F.Gozzo,R.P.daRocha |     |     |     |     |     | PureAppl.Geophys. |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
UTC 03 June 1997. As previously said, the cyclone where h is the potential temperature (K), q is the
lasted until 07 June, but the focus of this study is on specific humidity (kg kg-1), h is the equivalent
e
impacts ofoceanicsurfacefluxesinthe development potential temperature (K), c is the specific heat at
p
and mature stages of the system. Therefore 0000 constantpressure(1,004 J kg-1 K-1),Sisthesurface
UTC 29 May is used as a representative time for the sensible heat, L is the latent heat of condensation
c
|     |     |     |     |     |     |     | 106 kg-1), |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
development stage, because at this time the entire (2.5 9 J T is the air temperature, and p is
cyclonic circulation moved from the continent to the pressure and p is the mean sea level pressure. These
s
ocean, and 1200 UTC 31 May represents the mature equations assume that the fluxes decrease linearly
stage when the cyclone attained strongest intensity. from their maximum value at the surface to zero at
In order to validate the simulations, the surface the first inversion level, so the derivatives are
temperatureandSLHF,geopotentialheight,windand calculated from the surface up to this level.
sea level pressure fields are interpolated from the The role of SLHF in the development of the
simulationresolutiontothatofanalyses(1.0(cid:3) 9 1.0(cid:3) cycloneisanalyzedthroughvisualcomparisonofthe
forSLHFand1.5(cid:3) 9 1.5(cid:3)foratmosphericvariables). two simulations. Figures showing their differences
The cyclone’s development is investigated using are not shown because the locations of the cyclone
|     |     |     |     |     |     | are very | different | in each | simulation, |     | so the | simple |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ------- | ----------- | --- | ------ | ------ |
theSutcliffedevelopmentequation(SUTCLIFFE,1947),
written according to PETTERSSEN (1956) as: subtraction of one field from another would lead to
|     |     |     |     |     |     | useless | information. |     | The approximate |     | position | of  |
| --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | --------------- | --- | -------- | --- |
Z p0
o Q 0¼(cid:2) ! ! R (cid:2) g (cid:3) ð1Þ warm and cold fronts were drawn according to the
|     | V (cid:3) rQ | 500(cid:2) r2 | A TþHþE |       | dlnp; |          |              |           |           |            |      |           |
| --- | ------------ | ------------- | ------- | ----- | ----- | -------- | ------------ | --------- | --------- | ---------- | ---- | --------- |
| o t |              | f             | R       |       |       |          |              |           |           |            |      |           |
|     |              |               | p       |       |       | position | of strongest | low-level |           | horizontal | wind | con-      |
| ðIÞ | ðIIÞ         |               |         | ðIIIÞ |       | vergence | and          | cyclonic  | vorticity |            | and  | strongest |
where Q = (f ? f) is the absolute vorticity at horizontal temperature gradient.
|                                     | 0 0                             |     |     |     |              |     |     |     |     |     |     |     |
| ----------------------------------- | ------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| 1,000 hPa,Q                         | 500 istheabsolutevorticityat500 |     |     |     | hPa,Ris      |     |     |     |     |     |     |     |
| thespecificgasconstantfordryair(287 |                                 |     |     |     | J kg-1 K-1), |     |     |     |     |     |     |     |
s-2),f
| gisaccelerationofgravity(9.8 |     |                                 | m   |     | istherelative |     |     |             |          |     |     |     |
| ---------------------------- | --- | ------------------------------- | --- | --- | ------------- | --- | --- | ----------- | -------- | --- | --- | --- |
|                              |     |                                 |     | 0   |               |     |     | 3. Synoptic | Overview |     |     |     |
| vorticityat1,000             |     | hPa,fistheCoriolisparameter.The |     |     |               |     |     |             |          |     |     |     |
termsin(1)describe:
|     |     |     |     |     |     | The | system | under | study formed |     | on the | southern |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------------ | --- | ------ | -------- |
(I) absolute vorticity tendency at the surface Brazilian coast, at 1200 UTC 28 May 1997, as a
(1,000 hPa); 1,015 hPa closed isobar, located east of a 500 hPa
(II) 500 hPa absolute vorticity advection; trough and under cyclonic vorticity advection
|                                       |     |     |     |     |              | (Fig. 2a). | In this | figure | it can | also be | seen | that the |
| ------------------------------------- | --- | --- | --- | --- | ------------ | ---------- | ------- | ------ | ------ | ------- | ---- | -------- |
| (III) vorticitytendencydueto1,000–500 |     |     |     |     | hPathickness |            |         |        |        |         |      |          |
change processes: A (temperature advection), large- scale flow east of the surface cyclone is con-
T
H(diabaticheating)andE(stability). fluent and zonally oriented, as is the flow at 300 hPa
|                |            |                |             |            |              | (figure                           | not shown). | This    | is   | an indication  |               | that the |
| -------------- | ---------- | -------------- | ----------- | ---------- | ------------ | --------------------------------- | ----------- | ------- | ---- | -------------- | ------------- | -------- |
| The            | heating    | and moistening |             | of the     | lower tropo- |                                   |             |         |      |                |               |          |
|                |            |                |             |            |              | cyclone                           | will        | develop | as a | Shapiro–Keyser |               | type     |
| sphere due     | to surface |                | fluxes were | calculated | using        |                                   |             |         |      |                |               |          |
|                |            |                |             |            |              | (SCHULTZ                          | et al.,     | 1998).  | The  | meridional     | equivalent    |          |
| the Lagrangian |            | equations      | of NEIMAN   |            | and SHAPIRO  |                                   |             |         |      |                |               |          |
|                |            |                |             |            |              | potentialtemperaturegradientat925 |             |         |      |                | hPaisstrongin |          |
(1993):
|     |     |     |         |          |     | the area      | of cyclonic    |                | circulation | (Fig.      | 2b),              | and this    |
| --- | --- | --- | ------- | -------- | --- | ------------- | -------------- | -------------- | ----------- | ---------- | ----------------- | ----------- |
|     |     |     |         |          |     | configuration |                | of temperature |             | and wind   | fields            | con-        |
|     |     | dh  | g oS    |          |     |               |                |                |             |            |                   |             |
|     |     |     | ¼       |          | ð2Þ |               |                |                |             |            |                   |             |
|     |     |     |         |          |     | tributes      | to the         | strong         | 850 hPa     | warm       | air advection     |             |
|     |     | dt  | c p op  |          |     |               |                |                |             |            |                   |             |
|     |     |     |         |          |     | ahead of      | the surface    | cyclone        |             | (Fig. 2c). | The               | relative    |
|     |     | dq  | g oL    |          |     | vorticity     | and divergence |                | fields      | at 925     | hPa show          | two         |
|     |     |     | ¼       |          | ð3Þ |               |                |                |             |            |                   |             |
|     |     | dt  | L op    |          |     |               |                |                |             |            |                   |             |
|     |     |     | c       |          |     | small frontal | regions        | associated     |             | with       | this circulation: |             |
|     |     |     |         |          |     | a weak        | cold           | front over     | the         | continent  | (near             | 27(cid:3)S, |
|     | "   |     | (cid:4) | (cid:5)R | #   |               |                |                |             |            |                   |             |
| dh  | g   | oS  | 1000    | cpoL     |     |               |                |                |             |            |                   |             |
e ¼ ð1(cid:2)jÞ þ ej; ð4Þ 53(cid:3)W) and a strong warm front over the SAO (near
| dt  | c p | op  | p   | s op |     | 28(cid:3)S, 47(cid:3)W). |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 921
Figure2
1200UTC28May1997ERA-Interimanalysisofameansealevelpressure(dottedlines,inhPa),500hPageopotentialheight(contours,in
m)and500hPacyclonicrelativevorticityadvection(shaded,in10-9s-2);b925hPapotentialequivalenttemperature(shaded,inK)and
horizontalwindvector(ms-1,withscaleinthebottom);c850hPatemperatureadvection(shaded,inKday-1)andd925hPacyclonic
relativevorticity(shaded, in 10-5s-1) andconvergenceofthe horizontal wind (dashedlines, in 10-5s-1). In band d,the approximate
positionsofsurfacefrontsareindicated
At0000UTC29May1997,thecyclone’scentral 25(cid:3)S–42(cid:3)W, and a strong, zonally elongated warm
pressure is 1,010 hPa and its inner isobars are com- front near 28(cid:3)S–40(cid:3)W (Fig. 3d). The convergence
pletelyovertheSAO(Fig. 3a).At500 hPathetrough along the warm frontis inexcessof-5 9 10-5 s-1,
intensified and moved eastward, accompanied by whileitdoesnotexceed-3 9 10-5 s-1inthewarm
cyclonic vorticity advection near the trough axis. At sector of the cold front.
this time, the horizontal gradient of equivalent At 0000 UTC 30 May 1997, the geopotential at
potential temperature is stronger than before in the 500 hPa shows the merging of the two waves men-
region of cyclonic circulation (Fig. 3b) and the tioned in Fig. 3a in a single pronounced trough, and
intensification of the cold and warm temperature the surface cyclone is still beneath the relative
advection at 850 hPa level (Fig. 3c) should be noted cyclonicvorticityadvectionat500 hPa(Fig. 4a).The
as well. The 925 hPa convergence and cyclonic 925 hPa wind field shows strong winds in the
vorticity fields indicate an intensified cold front near southwest sector of the surface cyclone associated

922 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
Figure3
AsinFig.2,for0000UTC29May1997
withastrongerpressuregradientbetweenthecyclone alongthewarmfront,whiletheyweakenedalongand
and the polar anticyclone, centered at 42(cid:3)S–49(cid:3)W in the warm sector of the cold front.
(Fig. 4b). The colder air moved northward and the Thecycloneattainsthematurestageat1200UTC
even stronger gradients of equivalent potential tem- 31 May 1997. The surface cyclone reaches its mini-
perature are evident around the surface cyclone mumcentralpressure(999 hPa)anditisjustbeneath
(Fig. 4b). At 850 hPa, there is widespread cold air a closed low in the geopotential field at 500 hPa,
advectionwestwardofthesurface cyclone, whilethe indicating the equivalent barotropic structure of the
warm advection in its eastern sector weakened system(Fig. 5a).At925 hPa,theequivalentpotential
(Fig. 4c). The vorticity and divergence fields show temperature field shows the presence of a warm
the meridionally-oriented cold front extending to the seclusion with the 302 K isotherm centered near
coast of Northeast Brazil and its position perpendic- 33(cid:3)W–31(cid:3)S (Fig. 5b), in the same area where the
ular to the strengthened warm front (Fig. 4d). cyclonic vorticity is strongest (Fig. 5d). The warm
Compared with 12 h before (Fig. 3d), both cyclonic advectionat850 hPaintensifiedinthevicinityofthe
vorticity and convergence continue to be intense warm front mainly due to intensification of the

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 923
Figure4
AsinFig.2,for0000UTC30May1997
northerly winds (Fig. 5c). At this time, there is weak 4. Results
| cold air | advection in a | broad | area behind | the cold |     |     |     |     |     |     |
| -------- | -------------- | ----- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
front. The frontal T-bone pattern (with a stronger 4.1. Validation and Distribution of SLHF
| warm front)            | and the        | cold front   | fracture | (around          |                                           |                                      |       |                          |         |      |
| ---------------------- | -------------- | ------------ | -------- | ---------------- | ----------------------------------------- | ------------------------------------ | ----- | ------------------------ | ------- | ---- |
|                        |                |              |          |                  | Figure                                    | 6presentsthemeandailysurfacefluxeson |       |                          |         |      |
| 25(cid:3)W–33(cid:3)S) | are also       | clearly      | seen in  | the 925 hPa      |                                           |                                      |       |                          |         |      |
|                        |                |              |          |                  | 29 May.                                   | According                            | tothe | WHOI analysis,           | the     | SLHF |
| convergence            | and relative   | cyclonic     |          | vorticity fields |                                           |                                      |       |                          |         |      |
|                        |                |              |          |                  | fromtheseatotheatmosphere(positivevalues) |                                      |       |                          |         | near |
| (Fig. 5d).             | These features | characterize |          | the Shapiro–     |                                           |                                      |       |                          |         |      |
|                        |                |              |          |                  | the cyclone                               | center                               | are   | closer to                | ?40 and | ?200 |
| Keyser cyclone         | life cycle     | (NEIMAN      |          | and SHAPIRO,     |                                           |                                      |       |                          |         |      |
|                        |                |              |          |                  | W m-2,respectively(Fig.                   |                                      |       | 6a,c).Thestrongestfluxes |         |      |
1993).
|     |     |     |     |     | are in the | southern | sector | of the cyclone, | i.e., | in the |
| --- | --- | --- | --- | --- | ---------- | -------- | ------ | --------------- | ----- | ------ |
AfterJune1st,thecyclonecentralpressurebegins
|                              |     |     |      |              | cold air | mass. | The spatial | pattern | and intensity | of  |
| ---------------------------- | --- | --- | ---- | ------------ | -------- | ----- | ----------- | ------- | ------------- | --- |
| toriseanditsmovementisslower |     |     | than | before. From |          |       |             |         |               |     |
sensibleheatfluxessimulatedbytheFLXexperiment
| June1sttoJune3rd,itsmeanvelocityisjust2 |                    |       |          | m s-1,           |            |             |           |                     |      |          |
| --------------------------------------- | ------------------ | ----- | -------- | ---------------- | ---------- | ----------- | --------- | ------------------- | ---- | -------- |
|                                         |                    |       |          |                  | (Fig. 6a)  | are similar | to        | that of the         | WHOI | analysis |
| which is                                | slow in comparison | to    | the mean | velocity of      |            |             |           |                     |      |          |
|                                         |                    |       |          |                  | (Fig. 6b). | The         | simulated | 2-m air temperature |      | field    |
| systems in                              | this area of       | 10–15 | m s-1    | (REBOITA et al., |            |             |           |                     |      |          |
indicatesthatthebarocliniczoneisovertheseawith
2010b).

924 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
Figure5
AsinFig.2,for1200UTC31May1997
similar intensity to that shown by ERA-Interim cyclone in 40(cid:3)S–44(cid:3)W (Fig. 7c, d). Figures 6 and 7
reanalysis (Fig. 6a, b). Figure 6c, d show that the show that FLX simulates a sensible heat flux
WRF simulates more intense latent heat fluxes in intensity similar to that of the WHOI analysis, while
the southern sector of the surface cyclone than does the latent heat flux is overestimated. Figure 7 also
the WHOI analysis. A second core of strong latent indicates that the simulated baroclinic zone and
heat flux is simulated by FLX northwest of the cyclone center locations, as well as the associated
cyclone center. cold and warm fronts, are in agreement with ERA-
On 31 May, both FLX and WHOI present large Interim reanalysis.
SLHFbehindthecoldfrontandinabroadareaahead Figure 8 presents the time series of daily surface
of warm front, i.e., in the cyclone’s cold sector fluxes averaged over an area of 20(cid:3) 9 20(cid:3) (latitude
(Fig. 7). At this time, two main mechanisms are by longitude) centered on the cyclone center at 1200
actingtomaintainthesefluxes:(a)southeasterlyflow UTCofthegivenday.On28May,bothsensibleand
is transporting colder and drier air from higher latent fluxes in FLX are weaker than in WHOI. This
latitudes to the warm waters of subtropical SAO; difference can be attributed to the cyclone location.
(b) intensification of southeasterly winds due to a On this day, the simulated cyclone is still over the
polar anticyclone centered southwestward of the continent, while in ERA-Interim it is partially over

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 925
Figure6
29Maydailymeansensibleheatflux(Wm-2)and1200UTC2-mheightairtemperature(K)inaFLXandbWHOI(fluxes)andERA-
Interim(2-mairtemperature);29Maydailymeanlatentheatflux(Wm-2)and1200UTCsealevelpressure(hPa)incFLXanddWHOI
(fluxes)andERA-Interim(sealevelpressure).Theapproximatepositionsofsurfacefrontsareindicated
|          |            |         |                |             | 4.2. SLHF | Effects | on Cyclone | Track, | Intensification |     |
| -------- | ---------- | ------- | -------------- | ----------- | --------- | ------- | ---------- | ------ | --------------- | --- |
| the sea, | increasing | surface | fluxes, mainly | latent heat |           |         |            |        |                 |     |
flux, under it (figure not show). From 29 May and Vertical Structure
| onward,     | the FLX  | experiment | overestimates | both    |        |               |     |      |           |          |
| ----------- | -------- | ---------- | ------------- | ------- | ------ | ------------- | --- | ---- | --------- | -------- |
|             |          |            |               |         | Figure | 9 illustrates | the | mean | sea level | pressure |
| fluxes. For | sensible | (latent)   | heat flux the | maximum |        |               |     |      |           |          |
andaccumulatedprecipitationintwodifferentphases
| values attained |     | are *47 (240)      | and 60 (320) | W m-2       |              |              |        |                 |        |           |
| --------------- | --- | ------------------ | ------------ | ----------- | ------------ | ------------ | ------ | --------------- | ------ | --------- |
|                 |     |                    |              |             | (development | and          | mature | stage)          | in the | FLX and   |
| in WHOI         | and | FLX, respectively. | Despite      | intensity   |              |              |        |                 |        |           |
|                 |     |                    |              |             | NOFLX        | experiments. | In     | the development |        | phase, at |
| differences,    | the | time evolution     | and          | location of |              |              |        |                 |        |           |
0000UTC29May,thecycloneinNOFLXislocated
| simulated      | SLHF | in relation   | to the cyclone | center     |                                       |           |         |           |           |        |
| -------------- | ---- | ------------- | -------------- | ---------- | ------------------------------------- | --------- | ------- | --------- | --------- | ------ |
|                |      |               |                |            | *500 kmwestofthatinFLXexperiment(Fig. |           |         |           |           | 9a,b). |
| are consistent |      | with the WHOI | analysis,      | making the |                                       |           |         |           |           |        |
|                |      |               |                |            | At this                               | time, the | central | pressures | are 1,012 | and    |
FLXexperimentreliableenoughtousefordiscussion
1,004 hPainNOFLXandFLX,respectively.InFLX,
| of air–sea | interaction | processes | during | cyclone |     |     |     |     |     |     |
| ---------- | ----------- | --------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
day-1)
|     |     |     |     |     | precipitation | is intense | (over | 100 | mm  | along |
| --- | --- | --- | --- | --- | ------------- | ---------- | ----- | --- | --- | ----- |
development.

926 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
Figure7
31Maydailymeansensibleheatflux(Wm-2)and1200UTC2-mheightairtemperature(K)inaFLXandbWHOI(fluxes)andERA-
Interim(2-mairtemperature);31Maydailymeanlatentheatflux(Wm-2)and1200UTCsealevelpressure(hPa)incFLXanddWHOI
(fluxes)andERA-Interim(sealevelpressure).Theapproximatepositionsofsurfacefrontsareindicated
thenearlyeast–westorientedwarmfront(centeredat 996 hPa (Fig. 9c). In this simulation, the accumu-
*32(cid:3)S) and behind it, while in NOFLX weaker latedrainfallduringMay31isdistributedaroundthe
precipitation (up to 60 mm day-1) occurs in a small cyclonecenter,alongthewarmfrontandaheadofthe
area in the southeastern sector of the cyclone. At cold front. For the NOFLX experiment, the precip-
0000 UTC 31 May, when the cyclone is attaining its itation is much weaker and occupies a small area
mature phase, the differences are larger between the southeastward of the cyclone (Fig. 9d), along the
experiments (Fig. 9c, d). In NOFLX the polar warm front and to the east of it. Comparing the
anticyclone to the rear (4 hPa stronger than in FLX) simulations shown here with those in DA ROCHA and
iselongatedeastward,whilethecycloneisveryweak CAETANO (2010), this cyclone development shows
(1,020 hPa central pressure) and remains near the stronger sensitivity to the absence of SLHF than to
southeastern coast of Brazil (Fig. 9d). The FLX the use of different convective parameterizations. As
experimentshowsthecycloneoccupyingalargearea a Shapiro–Keyser cyclone, its warm front (whose
over the subtropical SAO, with central pressure of precipitation is mostly controlled by synoptic scale

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 927
Figure8
Timeseriesofarealaverage(ina20(cid:3)920(cid:3)squarecenteredinthecyclonecenter)dailymeansurfaceasensibleandblatentturbulentheat
fluxes(Wm-2)assimulatedbyFLXandfromWHOIanalysis
upwardmotions)isstrongerthanitscoldfront(where by the absence of fluxes, and how can this change in
convective precipitation is more important). There- track impact the cyclone intensification?
fore, the suppression of SLHF weakens the synoptic As previously discussed, the Sutcliffe develop-
scale upward motion and the vertical transport of menttheoryshowsthatextratropicalcyclonestendto
moisture mainly along the warm front, reducing movetowardregionsofstrongestwarmairadvection
drastically the grid-scale precipitation. The cumulus and/or greatest latent heat release, represented by
parameterization changes affect only the convective term (II) in Eq. (1). Then we might expect that
part of precipitation that was predominant in the changesintheseprocessesmayinfluencethecyclone
development stage (64 % of total precipitation accu- track.At0000UTCMay29,FLXsimulationshowsa
mulated on 29 May) but reduced during the cyclone broad area of warm air advection at 850 hPa to the
life cycle and represented 39 % of the total precip- east-northeast of the cyclone center and strong cold
itation in the mature phase (31 May). airadvectionbehindit(Fig. 11a),similartotheERA-
The absence of SLHF strongly influenced the Interim reanalysis (Fig. 3c). For the NOFLX exper-
cyclone track and intensification. Figure 10 presents iment both warm and cold air advections occur in a
the central pressure and position during the period similarpatternnearthecoast(Fig. 11b),withgreatest
0000UTC28Mayto0000UTC03June1997.Inthe differences occurring over the ocean. At this time
FLX experiment, the cyclone pressure is similar to bothexperimentspresentstrongerwarmairadvection
that in the ERA-Interim reanalysis (Fig. 10a) mainly with similar magnitude northeastward of the cyclone
until 01 June. After that, FLX simulated a more center, indicating weak impact of the thermal advec-
intense cyclone than the reanalysis. In NOFLX, tion in changing the cyclone track.
initially the pressure decreases only 3 hPa, and after Numerical experiments FLX and NOFLX show
0000UTC29Mayitstartstorise.Thecyclonetrack very different diabatic heating values in the vertical
in FLX follows the ERA-Interim reanalysis, while in column.InFLX,theintegrated900–500 hPadiabatic
NOFLX it moves first eastward and then northeast- heating is stronger (up to 30 K day-1) and occurs
ward, becoming unidentifiable in the sea level over a large area eastward of the cyclone center
pressurefieldat0000UTC31May(Fig. 10b).These (Fig. 11c). Larger heating occurs near the warm
results raise two questions: why is the track affected front,wheretheupwardmotionandprecipitation(see

928 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
Figure9
Sea level pressure (hPa, solid lines) and 24-h accumulated precipitation (shaded, mm 24h-1) at 0000 UTC 29 May 1997 for a FLX,
bNOFLXexperiments,andat0000UTC31May1997forcFLX,dNOFLXexperiments.Theapproximatepositionsofsurfacefrontsare
indicated
Fig. 7a) are intense, and with smaller intensity along cyclonic vorticity advection at mid-troposphere
the north–south (*35(cid:3)W) oriented cold front. The strengthens cyclonic vorticity at the surface, as
low pressure center tends to move southeastward of depicted by the Sutcliffe Eq. (1). This process is
its position, where the pressure in the column is happeningat0000UTC29MayinFLX,whencyclonic
decreasing due to latent heat release within it. vorticityadvectionisintenseat500 hPaeastoftrough
Diabatic heating in NOFLX is weaker (up to anddirectlyoverthesurfacelow,favoringitsfurther
10 K day-1) and occurs along the weaker warm intensification. The 500 hPageopotential height field
front, to the east and northeast of the cyclone center is similar in both the FLX and NOFLX experiments.
(Fig. 11d). In this case the contribution to eastward However, the vertical structure of the cyclone is
movement is smaller, and the strong anticyclone considerably modified by a decoupling of low and
positioned to the east and south of the low helps to upper levels. In FLX, the surface cyclone is under a
maintain the cyclone near the coast. regionofcyclonicvorticityadvectionaloft(Fig. 12a).
Achangeincyclonetrackcanalsoimpactcyclone InNOFLXthesurfacecyclonedoesnotmovesouth-
intensification.Accordingtoquasi-geostrophictheory, eastwardandliesbeneaththetroughaxis,wherethere

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 929
Figure10
Timeevolutionofsealevelpressureinthecenterofthecyclone,atevery6hforERA-Interimreanalysis(linewithcircles),andsimulatedby
FLX(dashedlinewithsquares)andNOFLX(dotlinewithdiamond)andbtrackingofthecycloneaccordingtoEra-Interimreanalysis(open
circles),FLX(blacktriangles)andNOFLX(opentriangles).Thetrajectoriesstarton0000UTC28May1997oversouthernBrazilandthe
pointsaremarkedatevery12h
is no cyclonic vorticity advection (Fig. 12b). This likely warmed by large sensible heat fluxes (around
vertical structure inhibits further cyclone intensifica- 300 W m-2) from the underlying warm Gulf Stream
tioninNOFLX. waters. In order to analyze this in the present study,
Due to the distinct development without SLHF, the near-surface Lagrangian potential temperature
differences in the low-level structure of the cyclone tendencies in the well-mixed maritime boundary
are also expected. Figure 13a shows that FLX layer, due to surface sensible heat fluxes, were
simulatesthelow-levelwindandequivalentpotential estimatedusingEqs.(2),(3)and(4).Thecalculations
temperature fields in the mature phase of the system are for 1200 UTC 30 May 1997 (24 h before the
at1200UTC31MayinaccordwiththeERA-Interim closed warm seclusion, following CORDEIRA and
(Fig. 5b). The warm seclusion with 302 K is well BOSART, 2011), at 30(cid:3)S–39(cid:3)W (eastern sector of the
positioned at 30(cid:3)S–31(cid:3)W, but slightly colder than in bent-back front). This point is identified in Fig. 13c,
ERA-Interim. In NOFLX, a warm seclusion with andthesensibleheatfluxthereisaround250 W m-2.
295 K is formed around 25(cid:3)S–43(cid:3)W (Fig. 13b), the The height of the inversion layer is 650 hPa, as
warmfrontisweakerthaninFLX,andthebent-back indicated by the simulated FLX tropospheric sound-
front is almost absent. However, in NOFLX a strong ing at that point.
cold front developed, differing from FLX and ERA- Equation (2) shows a heating rate of
Interim. These results are in agreement with simula- ?6.1 K day-1 due to the sensible heat flux. This
tionsofaShapiro–Keysercyclonewithnolatentheat heating would be more than compensated for by the
release due to precipitation processes (NIELSEN and horizontal cold air advection at 850 hPa, around
SAAS, 2003). -12 K day-1 (Fig. 13d). This indicates that the
Thecomparisonbetweensimulationsindicatesthe sensible heat flux alone cannot account for the
importance of SLHF in the formation of the warm heating of air parcels near the bent-back front in this
seclusion. CORDEIRA and BOSART (2011) studied an case. Therefore, the latent heat flux seems to play a
oceanic cyclogenesis and showed that the warm fundamental role in the process of warming the
seclusion process in that case resulted from isolation atmospheric column in that region. Indeed, the
by the bent-back warm front of parcels that were moisture tendency of the lower atmosphere (Eq. 3)

930 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
Figure11
0000UTC29May1997temperatureadvection(inKday-1;shaded)at850hPaforaFLXandbNOFLXexperiments.Theblackdotmarks
thelocationofthecyclonecenteratthattime.0000UTC29May1997integrated(900–500hPa)diabaticheating(Kday-1)incFLXand
dNOFLXexperiments.Theapproximatepositionsofsurfacefrontsareindicated
was8 g kg-1 day-1,andtheverticalcross-sectionof where sensible heat flux alone is likely to warm air
specific humidity and pseudo-vertical velocity at parcels,andisinagreementwithIWABEandDAROCHA
30(cid:3)S shows strong upward motion and transport of (2009) who indicated the importance of total surface
water vapor near the calculation point (Fig. 13e), heatfluxestotheheatinganddestabilizationofnear-
indicating considerable latent heat release. The surface air in a cyclogenesis over the SAO.
combined effect of SLHF in the Lagrangian equiv-
alent potential temperature tendency (Eq. 4) is
?29.4 K day-1, more than twice the cooling due to 5. Summary and Conclusions
coldairadvection.Therefore,bothsensibleandlatent
heat fluxes are contributing to warm the lower WRF simulations were utilized on assessing the
troposphere and to develop the warm seclusion. This influence of air–sea interaction processes on the
result differs from CORDEIRA and BOSART (2011), development of a Shapiro–Keyser cyclone that

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 931
Figure12
0000UTC29May1997geopotentialheight(contour,inm)andcyclonicrelativevorticityadvection(shaded,in10-9s-2)at500hPa,and
meansealevelpressure(dottedlines,inhPa)inaFLXandbNOFLXexperiments
developedon28May1997oversubtropicallatitudes simulation, the area of convective heating on the
of the SAO. After being initiated, the cyclone moves eastern side of the cyclone is weaker, and, hence,
slowly eastward–southeastward attaining minimum there is no thermodynamic support for the cyclone
central pressure on May 31. WRF numerical experi- motion. The magnitudes of low-level cold and warm
ments were carried out both with included and with temperature advection are similar in the experiments
excluded surface sensible and latent heat fluxes withandwithoutSLHF,buttheycoverasmallerarea
(SLHF). in the latter case. In the absence of SLHF, there is a
The synoptic evolution shows both the stronger decoupling ofthe low- and upper-level waves during
warmfrontandthecoldfrontalfractureduringthesys- the cyclone development: while the upper-level
temdevelopmentandthewarmseclusioninitsmature trough moves eastward, the surface cyclone moves
stagethatcharacterizesaShapiro–Keysertypecyclone. northeastward. Therefore, the surface cyclone lies
In the WRF experiment that includes SLHF, the over the trough axis, where upper-level cyclonic
simulated cyclone presents an eastward–southeast- vorticity advection is no longer effective in inducing
ward trajectory very similar to that of the ERA- upper-level mass divergence and further surface
Interim reanalysis. Similarities of cyclone intensity cyclone intensification.
arealsoobtainedinthefirstdaysofsimulation.After Thematurecycloneproducesawarmseclusionin
that, the simulated cyclone is more intense than that both experiments. Surface sensible heat flux alone is
of the ERA-Interim reanalysis, which may be asso- notenoughtowarmthesecludedairparcels,solatent
ciated with stronger SLHF in the simulation. When heat released by moist air ascent near the region of
the SLHF are turned off, the simulation develops a the bent-back front is essential to the heating of the
weaker cyclone that disappears from the sea level lower troposphere in this case. The warm front and
pressure field after 5 days of simulation. especially the bent-back front are much less intense
The cyclone has greatest intensification, and intheexperimentwithoutfluxes,whilethecoldfront
longer track and lifetime in the presence of SLHF, is sharper than in the control experiment.
presenting a typical southeastward trajectory and The numerical experiments with the WRF indi-
located beneath the eastern side of a low amplitude catethatthisShapiro–Keysercyclonedevelopmentis
upper-level trough. In the absence of SLHF, the more sensitive to the suppression of SLHF than to
cyclone moves northeastward and the trailing polar the cumulus parameterization schemes discussed in
anticyclonesplits,advancingaheadofthelow.Inthis DAROCHAandCAETANO(2010).Theintenselarge-scale

932 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
Figure13
1200 UTC 30 May 1997 925hPa potential equivalent temperature (shaded, in K) and horizontal wind vector (ms-1, with scale in the
bottom),inaFLXandbNOFLX,csurfacesensibleheatfluxes(Wm-2),dtemperatureadvection(inKday-1;shaded)at850hPa,evertical
sectionofspecifichumidity(shaded,inkgkg-1)andpseudo-verticalvelocity(Pas-1)at30(cid:3)S.Theapproximatepositionsofsurfacefrontsare
indicated,andanhorizontalbarincdesignatetheareaofverticalsection(e)

Vol.170,(2013) Air–SeaInteractionProcessesInfluencingtheDevelopment 933
precipitation associated with the warm front during DA ROCHA, R. P. and CAETANO, E. (2010), The role of convective
the whole cyclone lifetime is greatly affected in the parameterizationin the simulation of a cyclone overthe South
Atlantic.Atmo´sfera.23,1–23.
| absence | of SLHF, | while | the | region | of convective |     |     |     |     |     |     |     |     |
| ------- | -------- | ----- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
DUDHIA,J.(1989)Numericalstudyofconvectionobservedduring
precipitationinthevicinityofthecoldfrontweakens
|     |     |     |     |     |     |     | the winter | monsoon | experiment | using | a mesoscale | two-dimen- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---------- | ----- | ----------- | ---------- | --- |
as the cyclone develops. sionalmodel,JournalofAtmosphericSciences.46,3077–3107.
HONG,S.-Y.andPANH.-L.(1996),Nonlocalboundarylayerver-
| The               | WRF | experiments  | suggest |        | that air–sea | inter- |                 |     |                |     |          |             |      |
| ----------------- | --- | ------------ | ------- | ------ | ------------ | ------ | --------------- | --- | -------------- | --- | -------- | ----------- | ---- |
|                   |     |              |         |        |              |        | tical diffusion | in  | a medium-range |     | forecast | model, Mon. | Wea. |
| action processes, |     | particularly |         | latent | heat fluxes, | are    |                 |     |                |     |          |             |      |
Rev.124,2322–2339.
very important to this Shapiro–Keyser cyclone IWABE,C.M.N.andDAROCHA,R.P.(2009),Aneventofstrato-
development. Future research is planned to address spheric air intrusion and its associated secondary surface
|                |     |              |     |           |     |          | cyclogenesis | over | the South | Atlantic | Ocean, | Journal | of Geo- |
| -------------- | --- | ------------ | --- | --------- | --- | -------- | ------------ | ---- | --------- | -------- | ------ | ------- | ------- |
| the individual |     | contribution |     | of latent | and | sensible |              |      |           |          |        |         |         |
physicalResearch.114,1–15.
fluxes,withamoredetaileddescriptionofchangesin JANJIC,Z.I.(1994),Thestep-mountainetacoordinatemodel:fur-
lowtropospherestabilityandboundarylayerprocesses. ther developments of the convection, viscous sublayer and
turbulenceclosureschemes.Mon.Wea.Rev.122,927–945.
| Also, a | deeper | study | of frontogenetical |     | processes | is  |     |     |     |     |     |     |     |
| ------- | ------ | ----- | ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
KUO,Y.H.andLOW-NAM,S.(1990),PredictionofNineExplosive
anticipated.
|     |     |     |     |     |     |     | Cyclones | over | the Western | Atlantic | Ocean | with a | Regional |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ----------- | -------- | ----- | ------ | -------- |
Model,MonthlyWeatherReview.118,3–25.
|     |     |     |     |     |     |     | KUO, Y. H.,           | REED, | R. J.; LOW-NAM,                    |     | S. (1991), | Effects | of surface |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ----- | ---------------------------------- | --- | ---------- | ------- | ---------- |
|     |     |     |     |     |     |     | energyfluxesduringthe |       | earlydevelopmentandrapidintensifi- |     |            |         |            |
Acknowledgments
cationstagesofsevenexplosivecycloneinthewesternAtlantic,
Mon.Wea.Rev.119,457–476.
|     |     |     |     |     |     |     |     |     |     |     |     | Numerical | Study of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- |
TheauthorswishtothankNCARformakingavailable KUWANO-YOSHIDA, A. and ASUMA, Y. (2008),
|     |     |     |     |     |     |     | Explosively | Developing | Extratropical |     | Cyclones | in  | the North- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------- | --- | -------- | --- | ---------- |
theWRFmodel;toECMWFandWHOIforproviding westernPacificRegion,Mon.Wea.Rev.136,712–740.
accesstothemeteorologicalanalysis.CNPq(307519/ LAGOUVARDOS, K., KOTRONI, V. and Defer, E. (2007), The 21-22
|              |               |                                |     |                |     |     | January        | 2004 explosive |                 | cyclogenesis | over      | the Aegean   | Sea: |
| ------------ | ------------- | ------------------------------ | --- | -------------- | --- | --- | -------------- | -------------- | --------------- | ------------ | --------- | ------------ | ---- |
| 2008-2,      | 558121/2009-8 |                                | and | 307202/2011-9) |     | and |                |                |                 |              |           |              |      |
|              |               |                                |     |                |     |     | Observations   | and            | model analysis, |              | Quart. J. | Roy. Meteor. | Soc. |
| CAPES-PROCAD |               | 179/2007forthefinancialsupport |     |                |     |     | 133,1519–1531. |                |                 |              |           |              |      |
provided. LESLIE,L.M.;HOLLAND,G.J.andLYNCH,A.H.(1987),Australian
East-CoastCyclones.PartII:NumericalModelingStudy,Mon.
Wea.Rev.115,3037–3054.
REFERENCES MLAWER, E. J., TAUBMAN, S. J., BROWN, P. D., IACONO, M. J. and
|     |     |     |     |     |     |     | CLOUGH,     | S. A. | (1997), Radiative |     | transfer     | for inhomogeneous |         |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----------------- | --- | ------------ | ----------------- | ------- |
|     |     |     |     |     |     |     | atmosphere: | RRTM, | a validated       |     | correlated-k | model             | for the |
BERRISFORD,P.,DEE,D.,FIELDING,K.,FUENTES,M.,KALLBERG,P.,
longwave.J.Geophys.Res.102,16663–16682.
KOBAYASHI,S.andUPPALA,S.(2009),TheERA-Interimarchive,
|     |     |     |     |     |     |     | MONIN, A.S. | and OBUKHOV, |     | A.M. (1954), | Basic | laws of | turbulent |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------------ | ----- | ------- | --------- |
ERAReportSeries,ECMWFPublisher,ShinfieldPark,Read-
mixinginthesurfacelayeroftheatmosphere,Contrib.Geophys.
ing,UK.
Inst.Acad.Sci.,USSR.151,163–187.
BETTS,A.K.(1986),Anewconvectiveadjustmentscheme.PartI:
|     |     |     |     |     |     |     | NEIMAN, P. | J. and | SHAPIRO, | M. A. | (1993), The | life cycle | of an |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------- | ----- | ----------- | ---------- | ----- |
Observationalandtheoreticalbasis,Quart.J.Roy.Meteor.Soc.
extratropicalmarinecyclone.PartI:Frontal-cycloneevolution
112,677–691.
|     |     |     |     |     |     |     | and thermodynamic |     | air–sea | interaction. | Mon. | Wea. | Rev. 121, |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ------------ | ---- | ---- | --------- |
BETTS,A.K.andMILLER,M.J.(1986),Anewconvectiveadjust-
2153–2176.
| ment scheme. | Part | II: Single | column | tests | using GATE | wave, |     |     |     |     |     |     |     |
| ------------ | ---- | ---------- | ------ | ----- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
NIELSEN,N.W.andSASS,B.H.(2003),Anumerical,high-resolu-
| BOMEX,and | arctic | air-mass | data | sets, Quart. | J. Roy. | Meteor. |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ---- | ------------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tionstudyofthelifecycleoftheseverestormoverDenmarkon3
Soc.112,693–709.
December1999,TellusA.55,338–351.
| BJERKNES,J. | andSOLBERG,H.(1922),Life |     |     | Cycleof | Cyclonesand |     |             |            |     |              |                |     |         |
| ----------- | ------------------------ | --- | --- | ------- | ----------- | --- | ----------- | ---------- | --- | ------------ | -------------- | --- | ------- |
|             |                          |     |     |         |             |     | PAULSON, C. | A. (1970), | The | mathematical | representation |     | of wind |
thePolarFrontTheoryofAtmosphericCirculation.Geof.Publ.
|     |     |     |     |     |     |     | speed and | temperature | profiles |     | in the unstable | atmospheric |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | -------- | --- | --------------- | ----------- | --- |
3,3–18.
surfacelayer,JournalofAppliedMeteorology.9,857–861.
CAMPOS,C.N.(1999),Estudodafrontogeˆneseemumciclonedo
|     |     |     |     |     |     |     | PETTERSSEN, | S. Weather | Analysis | and | Forecasting | (McGRAW- |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | --- | ----------- | -------- | --- |
tipoShapiro-Keyser.Master’sthesis,InstitutoNacionaldePes-
HILL,1956).
quisasEspaciais,SP,Brazil.
PIVA,E.Dal,MOSCATI,M.C.L.andGAN,M.A.(2008),Papeldos
CARLSON,T.,Mid-LatitudeWeatherSystems(HARPERCOLLINS,
fluxosdecalorlatenteesensı´velemsuperfı´cieassociadosaum
1998).
|          |            |       |             |     |            |           | caso de | ciclogeˆnese | na costa | leste | da Ame´rica | do Sul, | Revista |
| -------- | ---------- | ----- | ----------- | --- | ---------- | --------- | ------- | ------------ | -------- | ----- | ----------- | ------- | ------- |
| CHEN, T. | C.; CHANG, | C. B. | and PERKEY, | D.  | J. (1983), | Numerical |         |              |          |       |             |         |         |
BrasileiradeMeteorologia.23,450–476.
StudyofanAMTEX’75OceanicCyclone,Mon.Wea.Rev.111,
REBOITA,M.S.,DAROCHA,R.P.andAMBRIZZI,T.(2011)Dynamic
1818–1829.
|     |     |     |     |     |     |     | and Climatological |     | Features | of  | Cyclonic | Developments | over |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | -------- | ------------ | ---- |
CORDEIRA,J.M.andBOSART,L.F.(2011),Cycloneinteractionsand
SouthwesternSouthAtlanticOcean.HorizontsinEarthScience.
evolutionsduringthe‘‘PerfectStorms’’oflateOctoberandearly
6,215–241.
November1991.Mon.Wea.Rev.139,1683–1707.

934 L.F.Gozzo,R.P.daRocha PureAppl.Geophys.
REBOITA, M. S., DA ROCHA, R. P., AMBRIZZI, T. and SUGAHARA, S. UCCELLINI,L.W.,PETERSEN,R.A.,BRILL,F.K.,KOCINP.J.E.and
(2010b), South Atlantic Ocean cyclogenesis climatology simu- TUCCILLO,J.J.(1987),Synergisticinteractionsbetweenanupper-
latedbyregionalclimatemodel(RegCM3),ClimateDynamics. leveljetstreakanddiabaticprocessesthatinfluencethedevel-
35,1331–1347. opmentofalow-leveljetandasecondarycoastalcyclone,Mon.
REED,R.J.andSIMMONS,A.J.(1991),Numericalsimulationofan Wea.Rev.115,2227–2261.
explosivelydeepening cyclone overthe northAtlantic that was WEBB, E. K. (1970), Profile relationships: The log-linear range,
unaffected by concurrent surface energy fluxes, Weather and andextensiontostrongstability,Quart.J.Roy.Meteor.Soc.96,
Forecasting.6,117–122. 67–90.
SCHULTZ,D.M.,KEYSERD.andBOSART,L.F.(1998),Theeffectof YINLONG,X.andMINGYU,Z.(1999),Numericalsimulationsonthe
large-scale flowonlow-levelfrontalstructure andevolutionin explosivecyclogenesisovertheKuroshioCurrent,Advancesin
midlatitudecyclones,MonthlyWeatherReview.126,1767–1791. AtmosphericSciences.16,64–76.
SKAMAROCK,W.C.,KLEMP,J.B.,DUDHIA,J.,GILL,D.O.,BARKER, YU, L., JIN, X. and WELLER, R. A. (2008), Multidecade Global
D. M., DUDA, M. G., HUANG, X. Y., WANG, W., POWERS, J. G. Flux Datasets from the Objectively Analyzed Air–sea Fluxes
(2008),AdescriptionoftheAdvancedResearchWRFVersion3, (OAFlux)Project:Latentandsensibleheatfluxes,oceanevap-
NCAR Technical Note NCAR/TN–475?STR, Boulder, CO, oration, and related surface meteorological variables. Woods
USA. Hole Oceanographic Institution, OAFlux Project Technical
SHAPIRO,M.AandKEYSER,D.(1990),Fronts,jetstreamsandthe Report.OA-2008-01.WoodsHole,Massachusetts,USA.
tropopause,InExtratropicalCyclones,theErikPalme´nMemo- ZHANG,D.L.andANTHES,R.A.(1982),Ahigh-resolutionmodelof
rialVolume(Amer.Met.Soc.)pp.167–191. the planetary boundary layer-sensitivity tests and comparisons
SUTCLIFFE, R. C. (1947), A contribution to the problem of devel- with SESAME-79 data, Journal of Applied Meteorology. 21,
opment,Quart.J.Roy.Meteor.Soc.73,370–383. 1594–1609.
TAO, W.-K., and SIMPSON, J. (1993), The Goddard cumulus
ensemble model. Part I: Model description. Terr. Atmos. Oce-
anicSci.4,35–72.
(Received January13,2012,revised August21,2012,accepted August23,2012,Publishedonline September15,2012)