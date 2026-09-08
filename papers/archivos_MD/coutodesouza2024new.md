Received:6February2024 Revised:16April2024 Accepted:3June2024
DOI:10.1002/joc.8539
RESEARCH ARTICLE
New perspectives on South Atlantic storm track through
an automatic method for detecting extratropical
cyclones' lifecycle
Danilo Couto de Souza1 | Pedro Leite da Silva Dias1 |
Carolina Barnez Gramcianinov2 | Matheus Bonjour Laviola da Silva1,3 |
Ricardo de Camargo1
1InstituteofAstronomy,Geophysicsand
AtmosphericSciences,Sa˜oPaulo Abstract
University,Sa˜oPaulo,Brazil ThisstudyintroducesnewinsightsintotheclimatologyofSouthAtlantic(SAt)
2InstituteforCoastalSystems–Analysis cyclones by employing a novel cyclone life cycle detection method, the Cyclo-
andModeling,Helmholtz-Zentrum
Phaser.Utilizingtheminimumrelativevorticityseriesanditsderivativeatthe
Hereon,Geesthacht,Germany
cyclonecentre,theprogrameffectivelyidentifiesdistinctphasesinthecyclone
3OceanPact,RiodeJaneiro,Brazil
lifecycle.Cyclonetracksareobtainedthroughtheanalysisofrelativevorticity
Correspondence at 850hPa, using the ERA5 dataset. The study identified six main cyclone life
DaniloCoutodeSouza,Instituteof
cycle patterns from the analysis of 28,458 systems. The predominant cyclone
Astronomy,GeophysicsandAtmospheric
Sciences,Sa˜oPauloUniversity,Ruado type, accounting for approximately 60% of the analysed systems, exhibited a
Mata˜o,226,CidadeUniversit(cid:1)aria,
four-phaseconfiguration:incipient,intensification,matureanddecay.Detailed
05508-090Sa˜oPaulo,Brazil.
statisticsforeachdevelopmentalphaseandtheoveralllifecyclearepresented,
Email:danilo.oceano@gmail.com
offering valuable comparisons and new insights while corroborating previous
Fundinginformation
research findings. Key genesis regions in the SAt are identified, along with
Coordenaça˜odeAperfeiçoamentode
track density maps that reveal distinct preferences in cyclone developmental
PessoaldeNívelSuperior-Brasil(CAPES),
Grant/AwardNumber:FinanceCode001 cycle.Themainoutcomeofthisstudyisthedemonstrationthattheautomated
classification procedure enables the analysis of cyclones' life cycles to be con-
ductedpromptlyandwithlowcomputingcosts,facilitatingthecomprehensive
studyofcyclonebehaviourwithhighefficiency.
KEYWORDS
automaticmethod,cyclone'slifetime,opensource,SouthAtlantic
1 | INTRODUCTION (Cardosoetal.,2022;deSouza&daSilva,2021),highsea
waves(Gramcianinovetal.,2023;Guimara˜esetal.,2014)
Cyclones play a crucial role in regulating global weather and storm surges (Campos et al., 2010; Leal et al., 2023),
andclimate.IntheSouthAtlantic(SAt),surfacecyclones triggering episodes ofcoastal erosion(Parise et al.,2009),
significantly influence the precipitation regimes in South resulting in economic losses in sectors such as oil explo-
America (Reboita et al., 2010b, 2018) and are associated ration, fishing and coastal infrastructure, and impacting
with extreme precipitation events (de Souza & da navigation. Therefore, enhancing our understanding of
Silva, 2021). Additionally, they pose natural hazards these systems, including their climatological aspects and
along the South American coast through intense winds the dynamical mechanisms leading to their formation
IntJClimatol.2024;1–21. wileyonlinelibrary.com/journal/joc ©2024RoyalMeteorologicalSociety 1

2 COUTODESOUZAETAL.
and evolution, is essential for improving forecasts and winds (Heinemann, 1990; Turner & Thomas, 1994).
implementing effective mitigation and adaptation Additionally, the interaction between sea ice and cyclo-
strategies. genesis at WEDDELL is significant. Recent studies high-
The SAt features various regions conducive to cyclo- light the impact of sea ice on surface albedo, thermal
genesis. Along the southeastern coast of South America, conductivity and atmospheric heat exchange processes
three genesis regions are identified: one in southeastern (Vihma, 2014). A correlation between decreased sea ice
Argentina (ARG), another near the La Plata river dis- and an enhanced number of cyclones has been observed,
charge in Uruguay (LA-PLATA) and a third near South- although these tend to be weaker (Simmonds &
eastBrazil(SE-BR)(Crespoetal.,2021;Gan&Rao,1991; Wu, 1993), while intense systems have the capacity to
Gramcianinov et al., 2019; Hoskins & Hodges, 2005; reducelocalsea-iceextent(Jenaetal.,2022).
Reboita et al., 2010a; Sinclair, 1995). Other genesis While climatologies of cyclones in the SAt, including
regions are located in the southeastern sector of the SAt genesis regions, are comprehensive, understanding the
(SE-SAO), the Weddell Sea (WEDDELL), the Antarctic specific regions where cyclones intensify, mature and
Peninsula (AT-PEN) and west of the South African and decay remains limited—a challenge not unique to the
Namibian coast (SA-NAM) (Carrasco et al., 2003; SAt but prevalent globally. The pioneering work by
Gramcianinov et al., 2019; Heinemann, 1990; Hodges Bjerknes (1922) first described extratropical cyclone life
et al., 2011; Hoskins & Hodges, 2005; Simmonds & cycles, identifying distinct phases using structural
Keay,2000). changesandlarge-scaledynamics,amethodologyfurther
Cyclogenesis alongtheSouthAmericancoastprimar- refined by Shapiro and Keyser (1990) and Neiman and
ily arises from baroclinic instability and lee cyclogenesis Shapiro (1993), who delineated phases like the incipient
(Gan & Rao, 1994; Gramcianinov et al., 2019; Vera broad baroclinic, frontal fracture, T-bone and warm-core
et al., 2002). In the ARG region, cyclogenesis is modu- seclusion.Recentresearchhasaimedtoobjectivelydefine
latedbythepositionoftheupper-leveljet,similartowin- these stages. Bengtsson et al. (2009) analysed Northern
ter genesis inLA-PLATAand SE-BR(Crespo etal., 2021; Hemisphere extratropical cyclones, while not specifying
Gramcianinov et al., 2019). During summer, LA-PLATA development stages, noted discernible phases around
benefits from warm advection driven by thermal- maximum system intensity. Schemm et al. (2018) nor-
orographic lows, while SE-BR cyclones form under baro- malized cyclone life cycles to identify front-associated
tropic conditions, enhanced by moisture advection from periods,andRudevaandGulev(2007)introduceda“non-
the Subtropical High (Crespo et al., 2021; Gozzo dimensional cyclone lifetime” to examine changes in
etal.,2017;Gramcianinovetal.,2019).Additionally,oce- cyclone radius throughout its life cycle. Other studies
anic influences such as the warm Brazil Current and the have identified the mature phase using peak vorticity or
pronounced sea-surface temperature gradients of the lowest central pressure and segmented the life cycle
the Brazil-Malvinas Confluence critically support coastal into intensification and decay stages relative to peak
cyclogenesis by providing essential moisture, heat and intensity (Azad & Sorteberg, 2014; Booth et al., 2018;
low-level baroclinicity (Gramcianinov et al., 2019; Dacre & Gray, 2009; Michaelis et al., 2017; Trigo, 2006).
Sanders&Gyakum,1980;Veraetal.,2002). For analysing intensification, Grise et al. (2013) used a
Few studies have examined the genesis mechanisms growth rate value, whereas Pinto et al. (2005) employed
for the SE-SAO, AT-PEN, WEDDELL and SA-NAM thebaroclinicEadygrowthrate.
regions. Gramcianinov et al. (2019) suggest that winter Despite these advancements, existing methods pri-
cyclogenesisinSE-SAOishighly baroclinic,oftenrelated marily focus on analysing the intensification and decay-
to secondary cyclogenesis in the cold sector of a pre- ing stages and do not provide comprehensive tools for
existing cyclone. Along the SA-NAM coast, cyclogenesis determining and analysing the mature and incipient
is likely influenced by the South African Plateau stages—periods when surface isobars are not yet fully
(Inatsu & Hoskins, 2004), potentially mirroring genesis closed,butenvironmentaldynamicsarealreadychanging
mechanisms of coastal lows west of the Andes duetothepresenceofalow-leveldisturbance.Moreover,
(e.g., Crespo et al., 2023). Less explored regions like AT- thereisalackofrobustmethodologiessuitableforclima-
PEN and WEDDELL may involve polar lows or meso- tologicalstudiesthatenabledetailedanalysisandclassifi-
scale cyclonesthat can evolve into more intense synoptic cationofdistinctstagesincyclones'lifecycles.Thisstudy
disturbances (Carrasco et al., 2003; Heinemann, 1990; proposes an objective method for determining the stages
Turner & Thomas, 1994). In these areas, lee cyclogenesis of development of cyclones using their central vorticity.
might occur due to complex topographical influences, The method is applied to study features of the life cycle
with systems in WEDDELL often developing from cold ofcyclonesintheSAtregion,providingnewinsightsinto
air pools over ice-free sea areas, influenced by offshore cyclone behaviour, such as displacement length, speed

| COUTODESOUZAETAL. |     |     |     |     |     | 3   |
| ----------------- | --- | --- | --- | --- | --- | --- |
|                   |     | (c) |     | (d) |     |     |
| (a)               | (b) |     |     |     |     |     |
(e)
|     | (f) | (g) |     | (h) |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| (i) | (j) | (k) |     |     |     |     |
FIGURE 1 SequentialmethodologyoftheCycloPhaserprogramforcyclonelifecycleanalysis.(a)Originalvorticityseriesinput.
(b)NoisereductionusingtheLanczosfilter,supplementedbyalow-passfilterontheinitialandfinal5%toremovespuriousoscillations.(c,
d)SeriessmoothingthroughfirstandsecondapplicationsoftheSavitzky–Golayfilter.(e)Peaksandvalleysidentificationintheprepared
series.(f–j)Detectionandlabellingofthecyclonedevelopmentstages:intensification,decay,mature,residualandincipient,respectively.
(k)Comprehensiveoverviewcombiningalldetectedstageswiththeoriginalandprocessedvorticityseries.[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
and duration, as well as the preferred regions of occur- repository (https://pypi.org/project/cyclophaser) and can
rence for each phase. The main outcome of this study is beinstalledviathepippackagemanager.Comprehensive
that the automated classification procedure enables large documentation for the package, along with illustrative
quantities of data to be processed promptly, opening examples of its usage, is accessible on the PyPI project
doors for future studies, such as analysing cyclone life website. It identifies the phases by analysing the relative
cycle behaviour in climate projections, including those vorticity at the cyclone centre and its first derivative
fromCMIP6models,andcomparingthemtothepresent- (Figure1).Primarilydesignedforcentralrelativevorticity
dayclimatology. analysis, as utilized in our study, CycloPhaser also
|     |     | accommodates | sea-level | pressure | or geopotential |     |
| --- | --- | ------------ | --------- | -------- | --------------- | --- |
heightdata.
| 2 | METHODS |     | Theprogramstartswithapre-processing |                 |          | stage.Onit, |        |
| ----------- | --- | ----------------------------------- | --------------- | -------- | ----------- | ------ |
|             |     | the users                           | have the option | to apply | the Lanczos | filter |
2.1 | The CycloPhaser program (Duchon, 1979) to the vorticity time series to remove
|     |     | noise in | the data (Figure | 1b), mostly | unrelated | to the |
| --- | --- | -------- | ---------------- | ----------- | --------- | ------ |
We developed CycloPhaser, an automated Python pack- development of extratropical cyclones on synoptic scales,
age for detecting cyclone life cycle phases. This open- including fluctuations in wind components induced by
source Python package is freely available in the PyPI featuresliketopography-inducedcirculations,seabreezes

4 COUTODESOUZAETAL.
and spatial and temporal variations in sea surface struc- corresponds to the periods of maximum intensification
tures (e.g., Acevedo et al., 2010; Da et al., 2017; Steele (decay) of vorticity. Therefore, the mature stage was
etal.,2015).High-resolutiondatasets,suchasERA5,ben- defined as the intervals between the valley of vorticity
efit from this filtering due to their sensitivity to noise and 12.5% of the time between the preceding derivative
from structures like frontal systems (Hoskins & valley,aswellas12.5%ofthetimetothefollowingderiv-
Hodges, 2002). However, this step can be skipped for ative peak. To be recognized as a significant mature
datasets already processed by tracking algorithms that stage, each interval must span at least 3% of the total
include spatial filtering (Flaounas et al., 2014; Hoskins & series length. Additionally, the program verifies that all
Hodges, 2002; Murray & Simmonds, 1991; Pinto mature stages are preceded by an intensification stage
et al., 2005). The Lanczos filter, functioning as a and followed by a decay stage, ensuring the accurate
band-pass, permits customization of cutoff frequencies identification of the mature phase within the cyclone's
for precise filtering. To counteract potential spurious lifecycle.
oscillations at data series endpoints introduced by spec- The specific thresholds for phase detection, including
tral filtering, a weaker low-pass Lanczos filter can be the 7.5% span for intensification/decay intervals and the
applied to the initial and final 5% of the data series, 3% minimum for the mature stage, along with the 12.5%
ensuringsmootherendpoints(Figure1b). intervals defining the bounds of the mature stage, were
After filtering, the CycloPhaser program uses a established through rigorous testing. This testing
Savitzky–Golay filter (Savitzky & Golay, 1964) to further involved an iterative calibration process, where various
reduce residual noise, crucial for ensuring the derivative percentage thresholds were applied to a representative
curves form a sinusoidal pattern for precise phase detec- sample of cyclone tracks to determine the most accurate
tion (Figure 1c). Users can apply this smoothing twice parameters for phase delineation. The final percentages
(Figure1d),adjustingitsintensitytobalancenoisereduc- were selected based on their effectiveness in capturing
tion and data integrity, tailoring the process to specific the genuine progression of cyclogenesis while filtering
requirements. Following this, the first derivative of rela- out inconsequential fluctuations in vorticity. This careful
tive vorticity is calculated primarily using second-order calibrationensuresthattheCycloPhaserprogramreliably
finite differences, employing central differences for inte- identifies each phase, providing a consistent and objec-
riorpointsandforward/backward(first-order)differences tivemethodologyforanalysingthelifecycleofextratropi-
for the endpoints. This derivative is then subjected to cal cyclones. For a understanding of how variations in
doublesmoothingwiththeSavitzky–Golayfiltertomain- these thresholds affect phase detection, please refer to
tainasinusoidalpatterninthederivativeseries,acritical Figures S1–S4, Supporting Information which offer a
step for accurately identifying cyclone life cycle phases. comparativeanalysisusingasetofcyclonecasestudies.
Skipping this dual smoothing could lead to false phase Next, our methodology introduces the “residual”
detections,emphasizingitsnecessityforreliableanalysis. stage to address peculiarities of tracking algorithms
The first phases to be detected are the intensification rather than signifying a distinct phase in extratropical
and decay stages. In those stages, the program employs a cyclone evolution (Figure 1i). The CycloPhaser program
method based on detecting peaks and valleys in the rela- tags stages as “residual” by analysing detected cyclone
tive vorticity time series (Figure 1e). The intensification phases; if a mature stage does not transition to a decay
phase is defined by the intervals from one peak to the stageorifanintensificationstagepostafullcycle(inten-
subsequent valley (Figure 1f), while the decay stage is sification, mature, decay) does not lead to another
determinedbythespansfromonevalleytothefollowing mature phase, these instances are classified as “residual”
peak (Figure 1g). Each intensification/decay interval (Figure 1e). This criterion accounts for scenarios where
must span at least 7.5% of the total series length to be the tracking algorithm may continue to follow a cyclone
considered significant. To ensure accuracy, the program post-decay, potentially capturing a re-intensification that
checks for multiple blocks of consecutive intensification/ doesnotculminateinamaturestageduetotrackinglim-
decay periods and merges them if the gap between them itations. For instance, Figure 1e depicts a system re-
issmallerthan7.5%oftheserieslength. intensifying post-decay without progressing to a mature
Theprogramthenproceedstodetectthematurestage phase,interpretedasatrackinganomaly.
ofthecyclone'slifecycle(Figure1h).Similartotheprevi- Following, a post-processing is applied, where the
ousstep,itidentifiespeaksandvalleysintherelativevor- program refines cyclone phase identification by bridging
ticity, however in this case, it also considers the gapsbetweensuccessiveintensificationanddecayphases.
derivative of vorticity (already smoothed). Between a It checks for discontinuities within consecutive phase
peak (valley) and a valley (peak) of vorticity series, there blocks, filling any found with the adjacent phase to
is always a valley (peak) of its derivative, which ensure continuous phase transitions. Moreover, it

COUTODESOUZAETAL. 5
corrects isolated phases lasting only one time step by extratropical cyclones. It is important to note that sub-
aligningthemwitheitherthesubsequentphase(atseries tropical systems, which share characteristics with both
start) or the preceding phase (elsewhere), enhancing tropicaland extratropical cyclones (e.g.,Hart,2003),may
phaseconsistencythroughoutthecyclonelifecycle. occasionally be detected, but they constitute a minority
In the cyclone phase identification's final step, the withinthedataset.Inthehistoricalrecordfortheregion,
program discerns the“incipient”stage(Figure 1j)byfirst there have only been two notable cases of tropical
labelling any unassigned phases as “incipient.” It then cyclones: Hurricane Catarina (Pezza & Simmonds, 2005)
analyses the phase sequence for an incipient- andTropicalStormIba(Reboitaetal.,2021).
to-intensification or incipient-to-decay transition. For In this study, the CycloPhaser's default settings were
incipient-to-intensification, “incipient” labels cover the primarily used to identify cyclone life cycle phases. The
initial 40% towards the next vorticity derivative valley. TRACK program's spatial filtering (Hodges, 1994, 1995)
For incipient-to-decay, they extend 40% towards the next negated the need for applying the Lanczos filter on rela-
peak(Figure1f).This40%threshold,establishedthrough tive vorticity series. The Savitzky–Golay filter's window
testing,ensurestheprecisedelineationofcyclonephases, length was tailored to each system's life cycle duration;
accommodating cyclones that initiate with ambiguous or for those exceeding 8days, it was set to an odd integer
rapidphasetransitions. near25%oftheserieslength,whileforshorterlifecycles,
it was adjusted to an odd integer near 50% of the series
length. During the second smoothing, for life cycles over
2.2 | Southern Atlantic cyclone detection 8days, the window length was an odd integer close to
and life cycle determination 50%oftheserieslength,butforshortercycles,itwaskept
consistentwiththefirstsmoothingstep.
The cyclone track information used in the current study
was obtained from the “Atlantic extratropical cyclone
tracksdatabase”availableatGramcianinovetal.(2020b), 3 | RESULTS AND DISCUSSION
which covers the entire Atlantic Ocean from 1979 to
2020. The spatial domain chosen for the analysis lies 3.1 | Life cycle types
between15(cid:1)S–55(cid:1)Sand75(cid:1)W–20(cid:1)E.Cyclonesaretracked
based on ERA5 fields (winds at 850hPa) using the The TRACK algorithm identified 33,376 cyclone systems
TRACKalgorithm(Hodges,1994,1995)andHoskinsand from 1979 to 2020, using criteria described in section 2.2.
Hodges (2002) method, following the minimum duration Initially, 39 cyclone life cycle types were detected, but to
and displacement requirements of 24h and 1000km, focusouranalysis,weconcentratedonconfigurationscom-
respectively. ERA5 was selected for its finer resolution prisingatleast1%ofalltypes,asshowninFigure2a.This
compared to alternatives like CFSR/CFSv2, offering sig- refinementledtoafocusontypesrepresenting95%ofsys-
nificant advantages in analysing regions characterized by tems (31,719), justifying the removal of the less significant
complex orography and temperature gradients, thereby types. Notably, several identified types included a “resid-
ensuring a comprehensive and consistent representation ual” stage, not indicative of an actual development phase.
of cyclones (Gramcianinov et al., 2020a). This approach To adjust, we merged counts of life cycle types differing
aligns with the characteristics and counts observed in only by this stage. Also, systems without a mature stage
previous South Atlantic cyclogenesis studies. Systems were excluded to prevent skewing phase statistics, recog-
spending over 80% of their life cycle over the continent nizing that such systems might have unique processes or
were excluded to omit thermal lows and lee troughs could be undeveloped troughs, requiring further investiga-
(e.g., Crespo et al., 2021), employing mobility criteria tion.Thisrefinedapproachledtoanalysing28,458systems,
consistent with earlier South Atlantic cyclone climatol- about 85% of total SAt-origin systems, ensuring a more
ogies(e.g.,Gramcianinovetal.,2019;Sinclair,1995).Fur- accuraterepresentationofcyclonelifecycles(Figure2b).
ther details on the methodology and database evaluation The life cycle of representative systems of the six life
arediscussedinGramcianinovetal.(2020a). cycletypespresentingmorethan1%ofoccurrenceinthe
The primary focus on extratropical cyclones in this SAt and that presents at least one mature stage is dis-
study stems from the specific calibration and design of playedatFigure3.Byfar,themostcommoncyclonetype
the TRACK algorithm used for cyclone tracking. While follow a four-phase configuration: incipient, intensifica-
the methodology does not explicitly exclude subtropical tion, mature and decay, collectively accounting for
or tropical cyclones, the detection of such systems is less approximately 60% of the analysed systems (Figure 3a).
likely due to their rarity in the South Atlantic and the This configuration represents a complete extratropical
algorithm's sensitivity to the features typical of cyclone development cycle. The second most prevalent

6 COUTODESOUZAETAL.
FIGURE 2 Distributionofidentifiedcyclonelifecycletypesasapercentageofthetotalnumberofcasesstudied(33,376),witheach
typerepresentingatleast1%ofthetotalcases.(a)Initialcountdistributionoflifecycletypes,includingthosewitha“residual”phase;bars
ofthesamecolourindicatestructurallysimilarlifecycleconfigurationsthatdifferonlybythepresenceorabsenceoftheresidualphase.
(b)Distributionafteraggregatingsimilarlifecycletypesbyremovingthe“residual”phaseandexcludingconfigurationswithouta“mature”
phase.Thephasesarelabelled:“incipient”(Ic),“intensification”(It),“mature”(M),“decay”(D),“residual”(R),withasecondoccurrence
denotedby(2).[Colourfigurecanbeviewedatwileyonlinelibrary.com]
FIGURE 3 IllustrativeexamplesofcyclonelifecyclescorrespondingtothecategoriesdefinedinFigure2b.Eachpanel(a–f)displaysthe
temporalevolutionofvorticityanditssmoothedderivatives,withcolouredbackgroundsindicatingthedifferentstagesofacyclone'slife
cycle.Thelinesrepresenttheoriginalvorticityseries(ζ)andthefirst(ζ
fs
)andsecond(ζ fs2)smoothedrelativevorticity.[Colourfigurecanbe
viewedatwileyonlinelibrary.com]
type, representing 7.3% of occurrences, follows the full cyclone development cycle twice, presenting a secondary
developmental cycle but lacks the incipient stage intensification, mature and decay phases. The former
(Figure 3b). The third and fifth most frequent types, presents an incipient stage (Figure 3d) and the latter,
accounting for 5.8% and 4.0%, respectively, feature an does not (Figure 3f). Remarkably, the frequency of these
early decay. The former includes an incipient stage types exhibits minimal to no seasonal (Figure S5) or spa-
(Figure 3c), while the latter does not (Figure 3e). Lastly, tial (Figure S6) variability for their respective genesis
the fourth and sixth configurations entail the complete regions(asdefinedinsection3.3.1).

COUTODESOUZAETAL. 7
FIGURE 4 Statisticsforthe
totalsystem'slifecycleandeach
individualphase:(a)total
duration(h),(b)maximum
travelleddistance(km),
(c)meanspeed(inm(cid:3)s−1),
(d)meanvorticity(scaledby
−1×10−5s−1,(e)meangrowth
rate(10−5s−1(cid:3)day −1).[Colour
figurecanbeviewedat
wileyonlinelibrary.com]
3.2 | Cyclone life cycle statistics et al. (2019, 2020a), but slightly higher than Simmonds
and Keay (2000), Mendes et al. (2010) and Reboita et al.
The average lifetime of SAt cyclones with at least one (2010a). Furthermore, Mendes et al. (2010) documented
mature stage is 90.72±58.12h (3.78±2.42days), peak- longer lifetimes but shorter displacements than our
ing in duration between 30 and 60h (1.25 and 2.5days), results. The observed differences are likely attributed to
and an average displacement of 3269±2290km, mostly varying tracking methodologies, datasets and our exclu-
ranging from 1000 to 1500km (Figure 4a,b). These find- sion of systems without a mature phase. Especially, the
ings are generally in line with those by Gramcianinov exclusion of continental systems might have contributed

8 COUTODESOUZAETAL.
to higher displacements, as on austral summer and Sinclair (1995) reported higher vorticity values compared
autumn, there are quasi-stationary lows over the South toourfindingsfortheincipient,matureanddecaystages.
American continent (Mendes et al., 2010). Additionally, However,theseauthorsomittedtheinfluenceoftopogra-
Reboita et al.'s (2010a) study focus on oceanic-only sys- phybyusinggeostrophicrelativevorticity,whichjustifies
temsovershadows theinitial developmentstagesofsome thedifferenceinvorticitydistribution.
systems,asshownbyGramcianinovetal.(2019). Theanalysisrevealedthatthesystemsaremostintense
In detail, the PDFs for both duration and displace- during the mature phase, as expected, exhibiting a broad
mentareleft-skewed(Figure4a,b),indicatingthatlonger range of vorticity values, highlighting the variability in
orfarther-reachingphasesarelesscommon.Theshortest mature cyclones' peak intensities. The intensification and
average durations and displacements are seen in the decay phases, by contrast, display more similar mean vor-
incipient, mature and second mature phases, which pre- ticities,reflectingtheirlifecycleroles:intensificationlowers
sent the highest frequencies at approximately 3h and system vorticity from the base state, whereas decay phase
3000km, highlighting that these stages of development bringsitcloserto thebasestateagain.Secondaryintensifi-
in SAt cyclones may often go undetected in standard cation and maturation phases typically show lower mean
6-hourly analyses. Conversely, the first intensification vorticitiesthantheirprimarycounterparts,occurringwhen
anddecayphasesshowthelongestdurationsandgreatest a cyclone re-intensifies without returning to its original
displacements, with notably shorter subsequent occur- genesis vorticity. Thus, these phases experience similar
rences. Given that the third most frequent cyclone life intensification and decay levels but do not achieve the
cycle type undergoes early decay (Figure 2), it is impor- higher vorticities of initial phases, illustrating the nuanced
tant to bear in mind that the mean values observed for relationship between cyclogenesis dynamics and the envi-
the first decay phase encompass both early decay stages ronmentalconditionsinfluencingthecyclonelifecycle.
aswellasdecaystagesoccurringafteramaturephase. The mean growth rate distribution is symmetric
The mean translational speed of approximately around zero (Figure 4e) and has low standard deviation,
13.9±5.5m(cid:3)s −1 is on agreement with previous studies indicatingadynamicequilibriuminsystemintensityover
(e.g., Gramcianinov et al., 2019, 2020a; Hoskins & the life cycle, with neither consistent intensification nor
Hodges, 2005) but higher than mean values found by weakening. Despite this symmetry, individual stages
Reboitaetal.(2010a).However,inthatstudy,theauthors show significant variability due to inherent noise in vor-
usedrelativevorticityat10mforthetrackingprocedure, ticitydata,evenafterspatialfilteringbytheTRACKalgo-
which is affected by the surface drag. Surprisingly, the rithm. The second mature stage distribution is slightly
meanspeed issimilar amongallphases,withthe highest left skewed, potentially influenced by the Lanczos filter,
difference in 0.4m(cid:3)s −1 but decreasing mean values from suggests some instances of second intensification might
the incipient to mature stage. This pattern still holds for be classified as part of the second mature phase
the second life cycle. Therefore, the cyclones in the SAt (Figure 3c). Despite these nuances, the CycloPhaser
are slower at their mature phases, which are related to adeptlyoutlinesSouthernAtlantictransientsystems'life-
extremewaveoccurrence(Gramcianinovetal.,2023). cycles,markingthehighestmeangrowthratesinintensi-
The PDF for the lifecycle of examined systems shows ficationstagesandthelowestindecaystages.
abimodal,left-skeweddistributionwithpeaksnear2and Unexpectedly, the incipient stage displays relatively
between 4 and 5−1×10−5s −1, with an average value of high positive mean growth rate values. This finding
4:1±1:8−1×10−5s −1 (Figure 4d). However, unlike tradi- alignswiththemeangrowthrateforcyclogenesisregions
tional studies focusing on vorticity at specific points, the as reported by Hoskins and Hodges (2005) and Gramcia-
CycloPhaser approach offers a detailed analysis through- ninovetal.(2019).Althoughthemeanvaluesforthesec-
out various developmental stages of cyclonic systems, ondintensificationanddecaystagesarelowerthanthose
providingadeeperinsightintothecyclonelifecycle.Our of the initial stages, they show higher standard devia-
results for the incipient stage exhibit higher vorticities tions, correlating with their mean intensity. This varia-
comparedtotheinitialvorticitiesreportedbyGramciani- tion could stem from the smaller sample size of these
novetal.(2019),Gramcianinovetal.(2020a)andReboita stages and the increased variability in the secondary life
et al. (2010a). This discrepancy may be attributed to our cycleofsystemsundergoingthisdevelopment.
exclusion criteria and the observed tendency for vorticity
to decrease when an incipient stage is followed by an
intensificationphase(e.g.,Figure3a,d),possiblyresulting 3.3 | Track density maps
in a bias towards lower values for this phase. Further-
more,intheiranalysisfocusingonthefirsttimestep,the In this section, we present a detailed analysis of the spa-
time step of minimum vorticity and the last time step, tial distribution of cyclone density across different

COUTODESOUZAETAL. 9
FIGURE 5 Cyclonetrackdensityforincipientphase,forallsystemswithgenesisintheSouthAtlantic,for(a)australsummer(DJF)
and(b)australwinter(JJA),andeachrespectivegenesisregion.Thetrackdensityunitiscycloneper106 km2permonth.[Colourfigurecan
beviewedatwileyonlinelibrary.com]
developmental phases, highlighting the key storm track regionsthat,whileidentifiedinpreviousstudies,havenot
regions in the Southern Atlantic. This analysis enhances beenasextensivelydiscussedandunderstoodasARG,LA-
our understanding of the extratropical cyclone develop- PLATA and SE-BR. These regions are situated along the
ment cycle within the study area, revealing patterns and SoutheastAtlantic(SE-SAO),SouthAfricanandNamibian
trends that may have implications for regional weather coast(SA-NAM),AntarcticPeninsula(AT-PEN)andWed-
and climateforecasting.Thecyclone densityiscomputed dell Sea (WEDDELL). Figure 5 illustrates cyclone track
using the kernel density estimation (KDE) method density (cyclones per 106 km2 per month) for the austral
(Hodges, 1996). We calculate the track density for each summer (DJF) and winter (JJA) in the SAt. As transi-
phase using the central point of the cyclones during all tional seasons demonstrate characteristics that lie
time steps in which the system is identified in a given between these two extremes, consistent with findings
phase. Note that this method differs from the traditional from earlier research (e.g., Crespo et al., 2021; Gan &
track density obtained by the TRACK program Rao, 1991; Reboita et al., 2010a), our analysis will pre-
(e.g., Gramcianinov et al., 2020a; Hoskins & dominantly concentrate on DJF and JJA, along with the
Hodges, 2002), which considers a specific or unique time previouslymentionedcyclogenesisregions.
step along the track to compute the track density. The The ARG region consistently maintains similar track
raw density statistics are then scaled to represent densities throughout both DJF (Figure 5a) and JJA
thenumberofcyclonespermonthperunitarea,allowing (Figure 5a), exceeding 30 cyclones per 106 km2 per
foranormalized comparison acrossdifferentregions and month, respectively. In contrast, the LA-PLATA and SE-
phases.Thisscalingiscrucialforaccuratelyassessingthe BR regions display a noticeable seasonality pattern. The
relative frequencyand intensity of cyclone activity indif- LA-PLATA region experiences increased activity during
ferent parts of the Southern Atlantic. The area unit used JJA compared to DJF, with densities surpassing 20 and
forthisanalysisisequivalenttoa5(cid:1) sphericalcap,which 10 cyclones per 106 km2 per month, respectively. Mean-
approximates to 106 km2. This unit size was chosen to while,theSE-BRregionpresentsheightenedactivitydur-
provide a balance between spatial resolution and statisti- ing DJF compared to JJA, with densities exceeding
cal robustness, ensuring that the density maps effectively 10 cyclones per 106 km2 per month during DJF, whereas
capture regional variations in cyclone activity while it exhibits negligible activity during JJA. It is important
maintainingsufficientdatapointsforreliableanalysis. tonotethatthevariationsintrackdensity,incomparison
to the genesis densities reported by Gramcianinov
et al. (2020a, 2019), stem from their focus solely on the
3.3.1 | Incipient phase initial time step of the system life cycle for analysis,
whereas this study considers all periods classified as the
Duringtheincipientstage,itwasobservedthethreecyclo- incipient stage. Also, on Gramcianinov et al. (2019),
genesis regions along the South American coast: SE-BR, the tracks steamed from the NCEP-CFSR reanalysis,
LA-PLATA and ARG (Figure 5). Nevertheless, this analy- whereas here, those were identified using the ERA5. For
sis reveals the existence of several other cyclogenesis the genesis regions on the South American coast, the

| 10  |     |     |     |     |     |        | COUTODESOUZAETAL. |     |
| --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- |
|     |     |     |     |     |     | FIGURE | 6 Cyclonetrack    |     |
densityforintensificationphase
foraustralsummer(DJF)(a)for
allsystemswithgenesisinthe
SouthAtlantic,(b)forARG,
(c)forLA-PLATA,(d)forSE-
BR,(e)forSE-SAO,(f)forAT-
PEN,(g)forWEDDELL,(h)for
SA-NAM.Thetrackdensityunit
|     |     |     |     |     |     | iscycloneper106 | km2per |     |
| --- | --- | --- | --- | --- | --- | --------------- | ------ | --- |
month.[Colourfigurecanbe
viewedat
wileyonlinelibrary.com]
seasonality observed here aligns with previous studies incipient stage, as expected due to the longer duration of
(Crespo et al., 2021; Gan & Rao, 1991; Gramcianinov the intensification phase (refer to Figure 1). During DJF
etal.,2019;Hoskins&Hodges,2005;Mendesetal.,2010; and JJA, the track densities range from approximately
|                      |     |     | 60(cid:1)E 60(cid:1)W, |      |           |               |        | 50(cid:1)S. |
| -------------------- | --- | --- | ---------------------- | ---- | --------- | ------------- | ------ | ----------- |
| Reboitaetal.,2010a). |     |     | to                     | with | a central | concentration | around |             |
The SE-SAO region exhibits increased activity during Notably, there is an area of maximum density east of
JJA(Figure5b)comparedtoDJF(Figure5a),withdensi- ARG during both seasons. During DJF (Figure 6d), this
ties for the incipient stage exceeding 10 and 5 cyclones maximumdensityregiondisplayshigherdensities(reach-
per106 km2 permonth,respectively.Notably,thisregion ing 70 cyclones per 106 km2 per month) and is oriented
demonstrates a wider spatial distribution of density than southeastwardinrelationtothemaximumdensityregion
theothers,withDJFtracksresemblingacontinuousarea observed during the incipient stage. Furthermore, during
of incipient systems extending from the ARG region to DJF, there is a separate maximum track density region
the western boundary of the SAt. Track densities related associatedwithSE-BR,asshowninFigure6.ThisSE-BR
toWEDDELLandSA-NAMregionsarealsomorepromi- regionalso displayssoutheastward orientation,with den-
106 km2
nent during JJA than DJF, exceeding 15 cyclones per sities reaching up to 40 cyclones per per month,
106 km2 permonth.DuringDJF,WEDDELLexperiences and it is centred in a region close to the incipient maxi-
km2
genesis at a rate of up to 10 cyclones per 106 per mum. This implies that the systems generated in the SE-
month,whiletheSA-NAMregion'sgenesisisnearlynegli- BR region tend to intensify near their genesis area and
gible, merging with the SE-SAO region. In contrast, SAT- exhibit relatively low mobility during the intensification
PENpresentssimilardensitiesandspatialpatternsforboth phase. However, it is important to note that, for this sea-
seasons,withmaximumdensitiescloseto10and8cyclones son, while LA-PLATA presents maximum track densities
km2
per106 permonthforJJAandDJF,respectively. comparable to SE-BR, the LA-PLATA region does not
|       |                   |       | appear as       | distinctly    | in the densities    | map                  | when     | consider- |
| ----- | ----------------- | ----- | --------------- | ------------- | ------------------- | -------------------- | -------- | --------- |
|       |                   |       | ing all systems | (Figure       | 6). This            | is because           | LA-PLATA | is        |
| 3.3.2 | | Intensification | phase |                 |               |                     |                      |          |           |
|       |                   |       | oriented        | southeastward | and                 | is thus overshadowed |          | by the    |
|       |                   |       | ARG tracks.     | In JJA,       | the intensification |                      | stage    | reveals a |
In the intensification phase (Figures 6 and 7), the track maximumtrackdensityextendingfromLA-PLATAtoits
densities exhibit significantly higher values than the southeast (Figure 7c) and another region that stretches

COUTODESOUZAETAL. 11
FIGURE 7 Sameas
Figure6,butforaustralwinter
(JJA).[Colourfigurecanbe
viewedat
wileyonlinelibrary.com]
from ARG to the east (Figure 7d), with both regions region, most likely resulting from the superposition of
exceeding50cyclonesper106 km2 permonth.Thesetwo systemsfromvariousregionsintensifyinginthisarea.
regions are interconnected (Figure 7a). This pattern indi- Furthermore, a maximum track density region
cates that while ARG cyclones exhibit distinct displace- exceeding 30 cyclones per 106 km2 per month appears
ments for DJF and JJA during the intensification stage, southeast of the AT-PEN, connected to the maximum
the systems originating at LA-PLATA tend to present density region originating from the WEDDELL genesis
similardisplacementsacrossseasons. area (with densities above 40 cyclones per 106 km2) per
SE-SAO displays a comparable behaviour for both DJF month and extending to the northeast. In contrast to the
andJJA(Figures6eand7e),withthelatterexhibitinghigher incipient stage, maximum densities for AT-PEN are
track density, in line with increased genesis activity during higher during DJF than JJA (35 and 30 cyclones per
thisperiod(Gramcianinovetal.,2019).InDJF,amaximum 106 km2 permonth,respectively),suggestingthatsystems
densityregionexceeding50cyclonesper106 km2 permonth in DJF exhibit smaller displacements compared to those
issituatedsoutheastward oftheregionofmaximumden- in JJA. During JJA, the maximum density region indi-
sity for the incipient stage, centred near 30(cid:1)E and 50(cid:1)S. cates an eastward displacement, while DJF suggests a
For JJA, this region shifts eastwardof the genesis region, northeastwardshift.TheWEDDELLregionpresentssim-
centred near 20(cid:1)E and 45(cid:1)S. This positioning relative to ilar density patterns for both DJF and JJA, with higher
the genesis region implies that these systems undergo densities during JJA, consistent with the pattern indi-
either high mobility during the intensification stage or cated by the incipient stage. Lastly, albeit more active
experience prolonged intensification periods. Similar to during JJA, densities near SA-NAM remain concentrated
the ARG region, there is a seasonality in the displace- aroundthedensityregionobservedintheincipientstage,
mentofthesesystems during theintensification stage.In indicatingthatthesesystemsexhibitlowermobility.
DJF,whenlookingforallsystemsgeneratedintheSouth
Atlantic (Figure 6), close to 15(cid:1)E, two centres of maxi-
mum density exceeding 50 cyclones per 106 km2 per 3.3.3 | Mature phase
month are observed, one at 50(cid:1)S and the other at 70(cid:1)S.
WhiletheformercanbeattributedtotheSE-SAOregion, For the mature stage, the track density representing all
the latter cannot be associated with any specific genesis the systems generated in the South Atlantic exhibits a

12 COUTODESOUZAETAL.
FIGURE 8 Sameas
Figure6,butformaturephase.
[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
FIGURE 9 Sameas
Figure6,butformaturephase
andforaustralwinter(JJA).
[Colourfigurecanbeviewedat
wileyonlinelibrary.com]

COUTODESOUZAETAL. 13
spatial pattern shifted southeastward from the intensifi- DJFand 50(cid:1)Eduring JJA (Figure 9e). Cyclonesfrom this
cation stage's densities (Figures 8a and 9a), with a maxi- region mature from the area close to the genesis maxi-
mum density region centred at 20(cid:1)E and 65(cid:1)S. This mum, extending up to the southeastern boundary of the
pattern closely resembles the spatial structure of South- Indian Ocean. The AT-PEN region demonstrates consis-
ern Atlantic storm tracks, albeit with the maximum den- tent spatial patterns for both seasons, with a maximum
sity region positioned further south (Gramcianinov track density exceeding 8 cyclones per 106 km2 per
et al., 2019; Hoskins & Hodges, 2005). During DJF, three monthcentredat40(cid:1)Wand65(cid:1)S(Figures8fand9f).Sys-
spots of maximum track densities become apparent. The tems originating in this region mature from 70(cid:1)W to the
first,situatedaround30(cid:1)Wand55(cid:1)S,canbeattributedto southeastern Indian Ocean. WEDDELL region exhibits
the convergence of mature systems from the genesis maximum track densities exceeding 10 cyclones per
regions along the South American coast, SE-BR, LA- 106 km2 per month for both seasons (Figures 8g and 9g).
PLATA and ARG (Figure 8a–c, respectively). The second During DJF, this maximum density region closely aligns
spot, located approximately at 0(cid:1) and 55(cid:1)S, likely results with that of the incipient phase. However, during JJA,
from the overlapping of systems originating from the the region expands northeastward, similar to the intensi-
South American coast, less mobile systems from SE-SAO fication stage. In the SA-NAM region, during DJF, the
(Figure 8e) and highly mobile systems from WEDDELL densities are almost negligible, not exceeding 5 cyclones
(Figure 8g). The last maximum, centred at 30(cid:1)E and per 106 km2 per month. In contrast, during JJA, systems
60(cid:1)S, is situated southeast of the region with the highest display a maximum track density exceeding 10 cyclones
density during the intensification period, including sys- per 106 km2 per month concentrated over the same area
tems with genesis across all regions within the study as the incipient and intensification stages (Figure 9g).
area, especially SE-SAO. Meanwhile, during JJA, two Thisreaffirmsthestationarynatureofthesesystems.
regions of maximum densities emerge. The first, located
between 30(cid:1)S and 70(cid:1)S, is associated with AT-PEN and
WEDDELL regions (Figure 9f,g). The second region, 3.3.4 | Decay phase
spanning from 10(cid:1)W to 50(cid:1)E and centred at approxi-
mately 65(cid:1)S, represents the maturation of systems from The decay stage exhibits the highest track densities
all the genesis regions within the study area. Notably, among all phases of the cyclone life cycle for both DJF
there is a secondary maximum in the SA-NAM region, and JJA when considering all cyclones with genesis in
confirmingthelowmobilityofthesesystems. theSouthAtlantic(Figures10aand11a).Inbothseasons,
The ARG region exhibits a distinct seasonality in the the maximum track density surpasses 100 cyclones per
spatial pattern of maximum density associated with 106 km2 per month and is centred at 65(cid:1)S and 30(cid:1)W.
thematurestage.DuringDJF,amaximumdensityregion Cyclones in the decay stage disperse throughout the
exceeding 10 cyclones per 106 km2 per month emerges entire South Atlantic, extending as far as the southeast-
southeastward of the region related to the intensification ern boundary of the Indian Ocean. These results are
stage (Figure 8b). In contrast, during JJA (Figure 9b), alignedwithSinclair(1995).Aswithpreviousphases,the
there is a region with a maximum track density exceed- systems with genesis in the ARG region exhibits a dis-
ing 8 cyclones per 106 km2 per month, positioned east- tinct seasonal pattern, with maximum track densities
ward the areas of maximum track densities for the exceeding 20 cyclones per 106 km2 per month in both
intensification and incipient stages. On the other hand, seasons (Figures 10b and 11b). In DJF, this maximum
the LA-PLATA and SE-BR regions present a maximum densityregionspansfrom50(cid:1)Wto20(cid:1)E,suggestingeither
trackdensitythatdoesnotexceed8cyclonesper106 km2 highermobilityorlongerdecayperiodsduringthisseason.
per month (Figures 8c,d and 9c,d). For DJF, cyclones Incontrast,inJJA,itiscentredsoutheastofthepeakden-
originating from both regions commence their matura- sity observed during theintensification stage.The systems
tion southeastward from the maximum track density withgenesisatLA-PLATAexhibitsmaximumtrackdensi-
associated with the intensification stage, extending up to ties for both seasons that exceed 15 cyclones per 106 km2
50(cid:1)E. During JJA, LA-PLATA systems mature up per month (Figures 10c and 11c). The track density
to70(cid:1)E,whileSE-BRexhibitslowermaximumtrackden- regions are centred in the same area observed in the
sities, not exceeding 5 cyclones per 106 km2 per month, mature stage but extend further southeastward and
which alignswith theloweractivityofthisregion during northwestward. The density to the northwest aligns with
thisseason. the maximum density related to the incipient stage,
For the systems with genesis in the SE-SAO region, a representingsystemsthatundergoearlydecay(Figure2).
maximum track density exceeding 8 cyclones per During JJA, the maximum track density region extends
106 km2 per month is centred at 60(cid:1)S and 40(cid:1)E during over a larger area, in alignment with the increased

14 COUTODESOUZAETAL.
FIGURE 10 Sameas
Figure6,butfordecayphase.
[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
FIGURE 11 Sameas
Figure6,butformaturephase
andforaustralwinter(JJA).
[Colourfigurecanbeviewedat
wileyonlinelibrary.com]

COUTODESOUZAETAL. 15
FIGURE 12 Cyclonetrack
densityforsecondary
developmentphases(a–c)for
australsummer(DJF)and
residual(d).(a)Second
intensificationstage,(b)second
maturestage,(c)seconddecay
stage.Thetrackdensityunitis
cycloneper106 km2permonth.
[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
genesis activity during this season. SE-BR also displays a decay phases) during DJF and JJA, respectively, for
maximumtrackdensityneartheregionsobservedinpre- Southern Atlantic-originating systems. Track density
vious phases, underscoring the limited mobility of these for these stages is lower, indicating that only a subset of
systems (Figures 10d and 11d). The maximum trackden- systemsexperiencesecondary development,asillustrated
sityexceeds20and8cyclonesper106 km2 permonthfor inFigure2.
JJA and DJF, respectively, highlighting the increased The second intensification stage shows two distinct
activityofthisregionduringDJF. density maxima. The first, near 50(cid:1)S and 30(cid:1)E during
Despiteitsseasonalactivityforgenesis,SE-SAOpre- DJF (Figure 12a), is close to the SE-SAO cyclogenesis
sents similar patterns for both DJF and JJA for the region and shows a higher track density, surpassing
decay stage, presenting a maximum track density east 8 cyclones per 106 km2 per month. In JJA (Figure 13a),
of the one for the mature stage, exceeding 20 cyclones this maximum does not have a cohesive spatial structure
per 106 km2 per month (Figures 8e and 9e). Notably, and is spread from approximately 40(cid:1)S to 70(cid:1)S and from
some systems with genesis in this region decay farther 0(cid:1) to 60(cid:1)E, with densities ranging from 4 to 6 cyclones
east, on the southwestern Pacific Ocean. SAT-PEN sys- per 106 km2 per month. The second density maximum,
tems decay close to their maturation, with maximum near the decay maxima for the WEDDELL region for
track densities centred at 40(cid:1)E and 65(cid:1)S (Figures 8f and both seasons, shows higher densities in DJF than JJA
9f). However, during DJF, the maximum track density is (exceeding 12 and 8 cyclones per 106 km2 per month,
notablyhigherthanforJJA(exceeding30and10cyclones respectively). This is a notable contrast to the mature
per 106 km2 per month, respectively). This indicates that stage,whereJJAtypicallypresentshighertrackdensities.
SAT-PEN systems present longer decay during DJF. This pattern suggests a non-negligible proportion of sys-
Meanwhile,WEDDELLpresentsthesamespatialpattern tems originating from the WEDDELL region undergo
asforpreviousstages(Figures8gand9g).Forthisregion, secondarydevelopment,particularlyinDJF.
the maximum track density is closer to the maximum Gramcianinov et al. (2019) highlighted a potential
density of incipient, intensification and mature phases linkbetweentheSE-SAOregionandsecondarycyclogen-
during DJF, while JJA maximum density is oriented esis. We do not exclude the possibility of some of the
northeastward (exceeding 20 and 30 cyclones per detected re-intensification might stem from secondary
106 km2 per month, respectively). Lastly, SA-NAM pre- cyclogenesiseventsorspuriouslinksbytheTRACKalgo-
sents the same pattern present for previous stages, with rithm, mixing weak decaying systems with incipient sec-
systemsclosetothegenesisregionanddecreasedactivity ondary cyclones. This necessitates further investigation,
for DJF when compared to JJA, with systems exceeding especially since re-intensification near the WEDDELL
10 and 15 cyclones per 106 km2 per month, respectively region aligns with growth regions identified by Hoskins
(Figures8hand9h). and Hodges (2005), suggesting these instances are more
likely re-intensifications than new cyclogenesis events,
underscoring the need for additional climatological
3.3.5 | Secondary development stages researchonWEDDELL-originsystems.
While secondary cyclogenesis generally follows a
Figures 12 and 13 show the secondary development frontalwavepostanextratropicalcyclone'spassage(Ford
stages (including a second intensification, mature and/or et al., 1990; Mailier et al., 2006; Rivals et al., 1998;

16 COUTODESOUZAETAL.
FIGURE 13 Sameas
Figure12butforaustralwinter
(JJA).[Colourfigurecanbe
viewedat
wileyonlinelibrary.com]
Shapiro et al., 1997), the CycloPhaser identifies a unique South American coast. The second centre, located near
pattern of secondary development involving re- the WEDDELL genesis region, exhibits higher densities
intensification and subsequent mature and decay phases. in DJF than in JJA (exceeding 12 and 8 cyclones per
This secondary intensification could result from a decay- 106 km2 per month, respectively). This pattern suggests
ing wave at 850hPa finding favourable conditions or, if limited mobility for WEDDELL systems undergoing sec-
the surface cyclone has dissipated and the TRACK algo- ondarydevelopment.
rithm is tracking a weak through at 850hPa, the Cyclo- A notable observation in both the second intensifica-
Phaser may classify this weak intensification as tionanddecayphasesistheregionneartheSE-BRgene-
“residual” should it not progress to a mature stage. Con- sis area during DJF, where relatively high track densities
versely, if the TRACK algorithm mistakenly associates extend southwestward. While a significant proportion of
thisdecayingwavewithanewlyformingcyclonenearby, systems decaying in this region may be associated with
the CycloPhaser labels the transition as “re- early decay in their life cycle 2, other processes should
intensification,” introducing potential analysis errors. also be considered. This region is known for the occur-
However, distinguishing between true secondary genesis rence of subtropical cyclones during DJF (Cardoso
andre-intensificationremainsbeyondthisstudy'sscope. et al., 2022; de Jesus et al., 2022; Evans & Braun, 2012),
The second mature stage exhibits the lowest maxi- with approximately 30% of the systems exhibiting hybrid
mum density among the secondary development stages, characteristics (Gozzo et al., 2014). Case studies of such
aligning with its shortest mean duration in theentire life systems originating in the SE-BR region reveal complex
cycle (Figure 4b). During DJF (Figure 12b), the maxi- life cycles, often transitioning between different system
mum density is higher than in JJA (Figure 13b), exceed- types and presenting multiple stages of intensification,
ing1and2cyclonesper106 km2 permonth,respectively. maturation and decay (e.g., Dias Pinto et al., 2013; Dutra
This maximum density region contours the Antarctic et al., 2017; Reboita et al., 2021; Reboita et al., 2022;
coastline, extending from the WEDDELL genesis area at Veigaetal.,2008).Consequently,itisplausiblethatsome
approximately90(cid:1)Eandpositionedsoutheastofthemax- of the systems represented in these high-density areas
imaobservedforthesecondintensificationstage. mightbesubtropical.However,furtheranalysisisneeded
For the second decay stage, two distinct density max- toconfirmthishypothesis.
imaareobserved.Thefirst,exhibitinghigherdensities,is
located eastward of the mature stage maxima during
DJF, near 60(cid:1)E and 60(cid:1)S, with densities surpassing 3.3.6 | Residual
16 cyclones per 106 km2 per month (Figure 12c). During
JJA, this centre shifts southward of the SE-SAO genesis The residual phase, although not indicative of a physical
region, near 30(cid:1)E and 60(cid:1)S (Figure 13c). Notably, this cyclone development stage per se, is crucial for under-
centre of maximum second decay is positioned westward standingtrackinganddetectiondiscrepancies,anditsug-
ofthefirstdecaystage'smaxima.Itisassociatedwithsys- gests areas for methodological refinement. This phase
tems originating in SE-SAO that followed distinct trajec- primarily captures systems that undergo temporary
tories compared to those undergoing only a single intensification due to favourable environmental condi-
developmental stage, systems from WEDDELL, and tions but do not evolve into mature cyclones. Detection
highlymobilesystemsfromthegenesisregionsalongthe of the residual phase involves recognizing instances

COUTODESOUZAETAL. 17
FIGURE 14 Relative
vorticity(shaded)and
geopotentialheights(contours)
at850hPaillustratethemature
(a)anddecaying(b)stagesofa
representativesystemthat
exhibitsaresidualphaseinits
lifecycle(c).Thecompletelife
cycleofthesystemisdepictedin
(d).[Colourfigurecanbeviewed
atwileyonlinelibrary.com]
where a system's central vorticity increases outside the relative vorticity (Figure 14c), indicating temporary re-
typical development cycle, often influenced by proximity intensification.Eventually,theTRACKalgorithmdiscon-
toothersystemsorlocalizedatmosphericconditionscon- tinues the tracking, signifying the end of observation
ducivetointensification. (Figure14d).Thisprocessoftransitoryintensificationfol-
During DJF, significant track densities for residuals lowing the decay stage is not related to the original sys-
are noted in SE-BR, SA-NAM and SE-SAO regions. tem'slifecycleandthusisclassifiedasresidual.
Cyclones from SE-BR, often weaker and lacking closed
isobars (Hoskins & Hodges, 2005; Sinclair, 1995), might
experience residual intensification near the Brazil- 4 | SUMMARY AND CONCLUDING
Malvinas confluence, an area fostering low-level barocli- REMARKS
nicity (Gordon, 1989; Sanders & Gyakum, 1980). This
suggests that residuals may represent weak systems This study introduces CycloPhaser, a novel, open-source
briefly intensifying due to favourable conditions but not Python package for automated cyclone life cycle detec-
achieving maturity. For SA-NAM and SE-SAO, despite tion, available on PyPI repository. Its low memory foot-
limitedresearch,theSE-SAO'smaxima'spositioningindi- print, flexibility and rapid deployment capabilities make
cates that upper-level jet support (e.g., Swart et al., 2015) itavaluableassetforclimatologicalstudiesorevenoper-
and baroclinic environments (e.g., Hoskins & ational forecasts. The research identified a total of 33,376
Hodges, 2005) could similarly drive marginal intensifica- systems from 1979 to 2020, focusing on configurations
tion,leadingtoaresidualclassification. that accounted for at least 1% of the overall life cycle
Conclusive statements for dynamics associated with types count and presented at least one mature phase.
the residual from regions like SA-NAM is hindered by These represented approximately 95% of the total sys-
scarce research. Yet, SE-SAO's maxima during DJF and tems, amounting to 31,719 systems in total. The most
JJA (Figure 13d),positionedsouth ofthe upper-leveljet's common cyclone type followed a four-phase configura-
mean location (e.g., Swart et al., 2015), imply upper-level tion: incipient, intensification, mature and decay,
jet support might spur marginal intensification, catego- accounting for about 60% of the analysed systems. The
rizing as residual. Notably, SA-NAM's maximum track results from the CycloPhaser program align well with
densityexhibitsseasonalshifts,movingnorthwestinDJF previous studies regarding cyclone behaviour in the
and south in JJA (Figures 12d and 13d), reflecting sea- South Atlantic region, confirming known cyclogenesis
sonal dynamic variations influencing residual classifica- regionsandprovidingstatisticalinsightsintocyclonelife-
tionsinSA-NAM-origincyclones. times and paths. The CycloPhaser program calculated an
Figure 14 illustrates the emergence of a residual average cyclone lifetime of approximately 90.72h
phase. Initially, Figure 14a presents a mature cyclone (3.78days) and an average displacement of 3269km,
with closed isobars at 850hPa. However, Figure 14b findingsthatlargelycorroboratethoseofpreviousstudies
reveals the system entering decay, with open isobars and andindicateabroadrangeofcyclonebehaviours.
diminished relative vorticity cohesion. A nearby system The research presents a detailed analysis of South
influences the decaying system, intensifying its central Atlantic cyclone development stages, including incipient,

18 COUTODESOUZAETAL.
intensification, mature, decay and secondary develop- offers a concentrated but partial view of cyclone life
ment.Theincipientphaseprimarilyoccursinestablished cycle.Consequently,ourconclusions about cyclonechar-
cyclogenesisregionsalongtheSouthAmericancoast(SE- acteristics through their life cycle predominantly reflect
BR, LA-PLATA and ARG), with additional regions iden- the processes observable at the 850hPa level. This meth-
tified in the Southeast Atlantic, near South Africa and odological choice inherently limits our ability to fully
Namibia (SA-NAM), the Antarctic Peninsula (AT-PEN), explore the cyclones' vertical development and the com-
and the Weddell Sea (WEDDELL). These regions show plex interactions occurring at different atmospheric alti-
seasonal variations, being most active during JJA, except tudes.Futureresearchcouldbenefitfromincorporatinga
SE-BR,whichpeaksinDJF,andARG,showinglittlesea- multi-level approach, providing a more holistic under-
sonal change. The intensification phase reveals high standingofcyclonedynamicsacrossthetroposphere.
track densities near 50(cid:1)S, primarily east or southeast of One of the uniquecontributions ofthisresearchisthe
genesis regions, except for WEDDELL, where tracks are assessment of cyclone life cycle stages along their storm
densernorthwestofthegenesis,andSA-NAM,whichdis- tracks, a perspective not commonly explored in existing
plays stationary behaviour. This displacement pattern is cyclone track climatologies. This approach may open ave-
consistent in the remaining phases. The mature phase nuesforfutureresearch,particularlyinunderstandingthe
tracks converge near Antarctica's coast at approximately nuances of cyclone development mechanisms and behav-
70(cid:1)S, 30(cid:1)E, while the decay phase shows a broader iour. From this first application, several open questions
spread, reflecting the high mobility and early decay of popped-up, highlighting the complexity and dynamic
some systems. Both mature and decay phases exhibit nature of cyclone systems. Using the method presented
noticeable seasonality, shifting south/southeastward dur- here, future studies can investigate further the primary
ingJJA.Secondarydevelopmentstagesarelessdensebut processes associated with each development stage in the
show significant seasonal variability. Also, the impor- life cycles of cyclones, including the secondary develop-
tance of the WEDDELL region for secondary life cycle ment stages reported herein—and if some of these cases
occurrence is highlighted, while acknowledging the limi- configureasecondarygenesisinstead.
tations infully understandingthisaspect dueto thescar-
cityofexistingresearch. AUTHOR CONTRIBUTIONS
The results presented here contribute significantly to Danilo Couto de Souza: Conceptualization; methodol-
the climatology of South Atlantic cyclones by enabling a ogy; software; validation; investigation; formal analysis;
more comprehensive exploration of neglected or less- data curation; visualization; writing – original draft.
studied regions. By identifying and including additional Pedro Leite da Silva Dias: Validation; resources;
cyclogenesisregionslikeSE-SAO,SA-NAM,AT-PENand writing – review and editing; supervision; funding acqui-
the WEDDELL, the climatology presented here opens up sition. Carolina Barnez Gramcianinov: Investigation;
new avenues for understanding cyclone formation and data curation; writing – review and editing. Matheus
behaviour in these areas. This expanded focus is crucial Bonjour Laviola da Silva: Resources; writing – review
for a more complete understanding of the climatological and editing. Ricardo de Camargo: Resources; supervi-
patterns and variations in cyclone activity across SAt. sion;fundingacquisition.
Furthermore, the CycloPhaser's detailed analysis of
cyclonelifecycletypes,particularlythefocusonconfigu- ACKNOWLEDGEMENTS
rations accounting for significant proportions of cyclone This study was partly financed by the Coordenaça˜o de
activity, enhances ourunderstanding ofthespatialdistri- Aperfeiçoamento de Pessoal de Nível Superior-Brasil
butionofcyclonephases.Thisanalysisnotonlyreaffirms (CAPES) under Finance Code 001. CBG is funded by the
the common four-phase configuration (incipient, intensi- Helmholtz European Partnership “Research Capacity
fication, mature and decay) but also shedslight on varia- Building for Healthy, Productive and Resilient Seas”
tionsincyclonedevelopmentcycles,therebycontributing (SEA-ReCap,GrantNo.PIE-0025).Thefirstauthortothe
toabetterunderstandingofhowdifferent regionswithin LaboratoryofAppliedMeteorologyforRegionalMeteoro-
SAt influence the formation and evolution of distinct logical Systems (MASTER) for the data processing infra-
cyclone types. These insights are valuable for improving structure, special thanks are extended to Jean Peres and
weather forecasting and developing effective mitigation Djalma Vieira for their invaluable technical assistance
strategiesintheregion. and support in the laboratory, contributing significantly
While the CycloPhaser program provides a novel and tothesuccessofthisresearch.
effectivetoolforanalysingcyclonelifecyclesintheSouth
Atlantic, it is important to acknowledge this study's limi- CONFLICT OF INTEREST STATEMENT
tations. The analysis at this single atmospheric level, Theauthorsdeclarenoconflictsofinterest.

| COUTODESOUZAETAL. |     |     |     |     |     |     |     |     |     |     |     |     |     | 19  |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DATA AVAILABILITY STATEMENT affectingthewesterncoastofSouthAmerica.ClimateDynam-
ics,60,2041–2059.
| The cyclone | tracks | used | in  | this study | were | obtained |     |     |     |     |     |     |     |     |
| ----------- | ------ | ---- | --- | ---------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
from the "Atlantic extratropical cyclone tracks database" Da, C., Shen, B., Yan, P., Ma, D. & Song, J. (2017) The shallow
|                                          |     |     |     |     |     |        | water | equation | and | the vorticity | equation | for | a change | in  |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------ | ----- | -------- | --- | ------------- | -------- | --- | -------- | --- |
| (https://doi.org/10.17632/kwcvfr52hp.4). |     |     |     |     | The | Cyclo- |       |          |     |               |          |     |          |     |
heightofthetopography.PLoSOne,12,e0178184.
| Phaser code | is  | available | at  | https://pypi.org/project/ |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dacre,H.F.&Gray,S.L.(2009)Thespatialdistributionandevolu-
cyclophaser.
|     |     |     |     |     |     |     | tion | characteristics |     | of North | Atlantic | cyclones. | Monthly |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | -------- | -------- | --------- | ------- | --- |
WeatherReview,137,99–115.
ORCID
|     |     |     |     |     |     |     | de Jesus, | E.M., | da Rocha, | R.P., | Crespo, | N.M., | Reboita, M.S. | &   |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --------- | ----- | ------- | ----- | ------------- | --- |
DaniloCoutodeSouza https://orcid.org/0000-0003- Gozzo,L.F.(2022)Futureclimatetrendsofsubtropicalcyclones
|     |     |     |     |     |     |     | in the | South | Atlantic | basin | in an ensemble |     | of global | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | -------- | ----- | -------------- | --- | --------- | --- |
4121-7583
regionalprojections.ClimateDynamics,58,1221–1236.
| PedroLeitedaSilvaDias |     |     | https://orcid.org/0000-0002- |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deSouza,D.&daSilva,R.R.(2021)Ocean-landatmospheremodel
4051-2962
(OLAM)performanceformajorextrememeteorologicalevents
| CarolinaBarnezGramcianinov |     |     |     | https://orcid.org/0000- |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nearthecoastalregionofsouthernBrazil.ClimateResearch,84,
| 0002-3919-5226 |     |     |     |     |     |     | 1–21. |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
MatheusBonjourLavioladaSilva https://orcid.org/ DiasPinto,J.R.,Reboita,M.S.&daRocha,R.P.(2013)Synopticand
0000-0002-8629-8762 dynamical analysis of subtropical cyclone Anita (2010) and its
RicardodeCamargo https://orcid.org/0000-0002-9425- potentialfortropicaltransitionovertheSouthAtlanticOcean.
| 5391 |     |     |     |     |     |     | JournalofGeophysicalResearch:Atmospheres,118,10–870. |               |     |           |        |        |             |     |
| ---- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | ------------- | --- | --------- | ------ | ------ | ----------- | --- |
|      |     |     |     |     |     |     | Duchon,C.E.                                          | (1979)Lanczos |     | filtering | in one | andtwo | dimensions. |     |
JournalofAppliedMeteorologyandClimatology,18,1016–1022.
REFERENCES
|     |     |     |     |     |     |     | Dutra, L.M.M., |     | da Rocha, | R.P., | Lee, R.W., | Peres, | J.R.R. | & de |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ----- | ---------- | ------ | ------ | ---- |
Acevedo, O.C., Pezzi, L.P., Souza, R.B., Anabor, V. & Camargo, R. (2017) Structure and evolution of subtropical
Degrazia,G.A.(2010)Atmosphericboundarylayeradjustment cycloneAnitaasevaluatedbyheatandvorticitybudgets.Quar-
to the synoptic cycle at the Brazil-Malvinas confluence, South terlyJournaloftheRoyalMeteorologicalSociety,143,1539–1553.
Atlantic Ocean. Journal of Geophysical Research: Atmospheres, Evans,J.L.&Braun,A.(2012)Aclimatologyofsubtropicalcyclones
115,D22107. intheSouthAtlantic.JournalofClimate,25,7328–7340.
| Azad, R. & | Sorteberg, | A.  | (2014) | The vorticity | budgets | of North |           |              |     |              |     |             |     |        |
| ---------- | ---------- | --- | ------ | ------------- | ------- | -------- | --------- | ------------ | --- | ------------ | --- | ----------- | --- | ------ |
|            |            |     |        |               |         |          | Flaounas, | E., Kotroni, | V., | Lagouvardos, | K.  | & Flaounas, | I.  | (2014) |
AtlanticwinterextratropicalcyclonelifecyclesinMERRArea-
|     |     |     |     |     |     |     | Cyclotrack | (v1.0)–tracking |     | winter | extratropical |     | cyclones | based |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------ | ------------- | --- | -------- | ----- |
nalysis. Part I: development phase. Journal of the Atmospheric on relative vorticity: sensitivity to data filtering and other rele-
Sciences,71,3109–3128. vantparameters.GeoscientificModelDevelopment,7,1841–1853.
Bengtsson,L.,Hodges,K.I.&Keenlyside,N.(2009)Willextratropi-
|     |     |     |     |     |     |     | Ford, R., | Ford, | R.P., | Moore, | G.W.K., | Moore, | G.W.K. | &   |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----- | ------ | ------- | ------ | ------ | --- |
cal storms intensify in a warmer climate? Journal of Climate, Moore, G.W.K. (1990) Secondary cyclogenesis—comparison of
22,2276–2301. observations and theory. Monthly Weather Review, 118,
| Bjerknes,J.(1922)Lifecycleofcyclonesandthepolarfronttheory |     |     |     |     |     |     | 427–446. |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ofatmosphericcirculation.Geofys.Publ.,3,1–18.
|     |     |     |     |     |     |     | Gan, M.A. | & Rao, | V.B. | (1991) Surface | cyclogenesis |     | over | South |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | -------------- | ------------ | --- | ---- | ----- |
Booth, J.F., Naud, C.M. & Jeyaratnam, J. (2018) Extratropical America.MonthlyWeatherReview,119,1293–1302.
cycloneprecipitationlifecycles:asatellite-basedanalysis.Geo-
Gan,M.A.&Rao,V.B.(1994)TheinfluenceoftheAndesCordillera
physicalResearchLetters,45,8647–8654.
ontransientdisturbances.MonthlyWeatherReview,122,1141–
| Campos,R.M.,Camargo,R.D.&Harari,J.(2010)Characterization |     |     |     |     |     |     | 1157. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ofextremesealeveleventsinSantosandtheircorrespondence Gordon, A.L. (1989) Brazil-Malvinas confluence–1984. Deep Sea
withtheNCEPmodelreanalysisinthesouthwestoftheSouth ResearchPartA:OceanographicResearchPapers,36,359–384.
Atlantic.RevistaBrasileiradeMeteorologia,25,175–184.
Gozzo,L.,DaRocha,R.,Gimeno,L.&Drumond,A.(2017)Clima-
Cardoso, A.A.,da Rocha,R.P.& Crespo, N.M.(2022)Synoptic cli- tologyandnumericalcasestudyofmoisturesourcesassociated
matologyofsubtropicalcycloneimpactsonnear-surfacewinds
|     |     |     |     |     |     |     | with | subtropical | cyclogenesis |     | over the | southwestern | Atlantic |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ------------ | --- | -------- | ------------ | -------- | --- |
over the South Atlantic basin. Earth and Space Science, 9, Ocean. Journal of Geophysical Research: Atmospheres, 122,
| e2022EA002482. |     |     |     |     |     |     | 5636–5653. |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Carrasco,J.F.,Bromwich, D.H.&Monaghan,A.J. (2003)Distribu- Gozzo, L.F., da Rocha, R.P., Reboita, M.S. & Sugahara, S. (2014)
tionandcharacteristicsofmesoscalecyclonesintheAntarctic:
SubtropicalcyclonesoverthesouthwesternSouthAtlantic:cli-
RossSeaeastwardtotheWeddellSea.MonthlyWeatherReview, matological aspects and case study. Journal of Climate, 27,
| 131,289–301. |     |     |     |     |     |     | 8543–8562. |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Crespo,N.M.,daRocha,R.P.,Sprenger,M.&Wernli,H.(2021)A Gramcianinov, C., Campos, R., De Camargo, R., Hodges, K.,
potential vorticity perspective on cyclogenesis over centre- Soares, C.G. & da Silva Dias, P. (2020a) Analysis of Atlantic
eastern South America. International Journal of Climatology, extratropical storm tracks characteristics in 41years of ERA5
41,663–678. andCFSR/CFSV2databases.OceanEngineering,216,108–111.
Crespo, N.M., Reboita, M.S., Gozzo, L.F., de Jesus, E.M., Torres- Gramcianinov,C.,Hodges,K.&Camargo,R.D.(2019)Theproper-
´
Alavez,J.A.,Lagos-Zúñiga,M.A.etal.(2023)Assessmentofthe ties and genesis environments of South Atlantic cyclones. Cli-
RegCM4-CORDEX-CORE performance in simulating cyclones mateDynamics,53,4115–4140.

20 COUTODESOUZAETAL.
Gramcianinov, C.B., Campos, R.M., de Camargo, R., Hodges, K.I., Michaelis, A.C., Willison, J., Lackmann, G.M. & Robinson, W.A.
GuedesSoares,C.&daSilvaDias,P.L.(2020b)Atlanticextra- (2017)ChangesinwinterNorthAtlanticextratropicalcyclones
tropical cyclone tracks in 41years of ERA5 and CFSR/CFSv2 in high-resolution regional pseudo–global warming simula-
databases.MendeleyData,4,108111. tions.JournalofClimate,30,6905–6925.
Gramcianinov, C.B., de Camargo, R., Campos, R.M., Guedes Murray,R.J.&Simmonds,I.(1991)Anumericalschemefortrack-
Soares, C. & da Silva Dias, P.L. (2023) Impact of extratropical ing cyclone centres from digital data. Part II: application to
cycloneintensityandspeedontheextremewavetrendsinthe January and July general circulation model simulations.
AtlanticOcean.ClimateDynamics,60,1447–1466. AustralianMeteorologicalMagazine,39,167–180.
Grise, K.M., Son, S.-W. & Gyakum, J.R. (2013) Intraseasonal and Neiman,P.J.&Shapiro,M.(1993)Thelifecycleofanextratropical
interannualvariabilityinNorthAmericanstormtracksandits marinecyclone.PartI:frontal-cycloneevolutionandthermody-
relationship to equatorial Pacific variability. Monthly Weather namicair-seainteraction.Monthly WeatherReview,121,2153–
Review,141,3610–3625. 2176.
Guimara˜es,P.,Farina,L.&Toldo,E.,Jr.(2014)Analysisofextreme Parise, C.K., Calliari, L.J. & Krusche, N. (2009) Extreme storm
wave events on the southern coast of Brazil. Natural Hazards surgesinthesouthofBrazil:atmosphericconditionsandshore
andEarthSystemSciences,14,3195–3205. erosion.BrazilianJournalofOceanography,57,175–188.
Hart,R.E.(2003)Acyclonephasespacederivedfromthermalwind Pezza, A.B. & Simmonds, I. (2005) The first South Atlantic hurri-
and thermal asymmetry. Monthly Weather Review, 131, cane: unprecedented blocking, low shear and climate change.
585–616. GeophysicalResearchLetters,32,L15712.
Heinemann,G.(1990)MesoscalevorticesintheWeddellSearegion Pinto,J.G.,Spangehl,T.,Ulbrich,U.&Speth,P.(2005)Sensitivities
(Antarctica).MonthlyWeatherReview,118,779–793. ofacyclonedetectionandtrackingalgorithm:individualtracks
Hodges, K. (1995) Feature tracking on the unit sphere. Monthly andclimatology.MeteorologischeZeitschrift,14,823–838.
WeatherReview,123,3458–3465. Reboita, M., Crespo, N., Dutra, L., Silva, B., Capucin, B. & da
Hodges, K. (1996) Spherical nonparametric estimators applied to Rocha, R. (2021) Iba: the first pure tropical cyclogenesis over
the UGAMP model integration for AMIP. Monthly Weather the western South Atlantic Ocean. Journal of Geophysical
Review,124,2914–2932. Research:Atmospheres,126,e2020JD033431.
Hodges,K.I.(1994)Ageneralmethodfortrackinganalysisandits Reboita,M.S.,DaRocha,R.P.,Ambrizzi,T.&Sugahara,S.(2010a)
application to meteorological data. Monthly Weather Review, South atlantic ocean cyclogenesis climatology simulated by
122,2573–2586. regionalclimatemodel(RegCM3).ClimateDynamics,35,1331–
Hodges, K.I., Lee, R.W. & Bengtsson, L. (2011) A comparison of 1347.
extratropicalcyclonesinrecentreanalysesERA-Interim,NASA Reboita,M.S.,daRocha,R.P.,deSouza,M.R.&Llopart,M.(2018)
MERRA, NCEP CFSR, and JRA-25. Journal of Climate, 24, Extratropical cyclones over the southwestern South Atlantic
4888–4906. Ocean: HadGEM2-ES and RegCM4 projections. International
Hoskins,B.J.&Hodges,K.I.(2002)NewperspectivesontheNorth- JournalofClimatology,38,2866–2879.
ernHemispherewinterstormtracks.JournaloftheAtmospheric Reboita,M.S.,Gan,M.A.,DaRocha,R.&Ambrizzi,T.(2010b)Pre-
Sciences,59,1041–1061. cipitation regimes in south america: a bibliography review.
Hoskins,B.J.&Hodges,K.I.(2005)AnewperspectiveonSouthern RevistaBrasileiradeMeteorologia,25,185–204.
Hemispherestormtracks.JournalofClimate,18,4108–4129. Reboita, M.S., Gozzo, L.F., Crespo, N.M., Custodio, M.d.S.,
Inatsu, M. & Hoskins, B.J. (2004) The zonal asymmetry of the Lucyrio,V.,deJesus,E.M.etal.(2022)FromaShapiro–Keyser
Southern Hemisphere winter storm track. Journal of Climate, extratropical cyclone to the subtropical cyclone raoni: an
17,4882–4892. unusual winter synoptic situation over the South Atlantic
Jena,B.,Bajish,C.,Turner,J.,Ravichandran,M.,Anilkumar,N.& ocean. Quarterly Journal of the Royal Meteorological Society,
Kshitija,S.(2022)Recordlowseaiceextentintheweddellsea, 148,2991–3009.
Antarctica in April/May 2019 driven by intense and explosive Rivals,H., Rivals, H., Cammas, J., Cammas, J.-P., Renfrew, I.A. &
polarcyclones.npjClimateandAtmosphericScience,5,19. Renfrew, I.A. (1998) Secondary cyclogenesis: the initiation
Leal, K.B., Robaina, L.E.d.S., Körting, T.S., Nicolodi, J.L., da phase of a frontal wave observed over the eastern Atlantic.
Costa,J.D.&Souza,V.G.(2023)Identificationofcoastalnatu- Quarterly Journal of the Royal Meteorological Society., 124,
raldisasters usingofficial databases toprovidesupportfor the 243–267.
coastalmanagement:thecaseofsantacatarina,Brazil.Natural Rudeva,I.&Gulev,S.K.(2007)Climatologyofcyclonesizecharac-
Hazards, 1–18. https://link.springer.com/article/10.1007/ teristics and their changes during the cyclone life cycle.
s11069-023-06150-3 MonthlyWeatherReview,135,2568–2587.
Mailier, P., Mailier, P.J., Stephenson, D.B., Stephenson, D.B., Sanders,F.&Gyakum,J.R.(1980)Synoptic-dynamicclimatologyof
Ferro, C.A.T., Ferro, C.A.T. et al. (2006) Serial clustering of the“bomb”.MonthlyWeatherReview,108,1589–1606.
extratropical cyclones. Monthly Weather Review, 134, 2224– Savitzky,A.&Golay,M.J.(1964)Smoothinganddifferentiationof
2240. databysimplifiedleastsquaresprocedures.AnalyticalChemis-
Mendes,D.,Souza,E.P.,Marengo,J.A.&Mendes,M.C.(2010)Cli- try,36,1627–1639.
matology of extratropical cyclones over the South American– Schemm, S., Sprenger, M. & Wernli, H. (2018) When during their
southern oceans sector. Theoretical and Applied Climatology, lifecycleareextratropicalcyclonesattendedbyfronts?Bulletin
100,239–250. oftheAmericanMeteorologicalSociety,99,149–165.

| COUTODESOUZAETAL. |     |     |     |     |     |     |     | 21  |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Shapiro,M.A.,Doyle,J.,Zou,X.,Jorgensen,D.P.,Jorgensen,D.P.& and links with the synoptic-scale environment. International
JournalofClimatology,14,871–894.
Jorgensen,D.P.(1997)Extratropicalsecondarycyclones:simu-
lationsandobservations. Veiga,J.A.P.,Pezza,A.B.,Simmonds,I.&SilvaDias,P.L.(2008)An
Shapiro,M.A.&Keyser,D.(1990)Fronts,jetstreamsandthetropo- analysis of the environmental energetics associated with the
pause.Boston,MA:Springer. transition of the first South Atlantic hurricane. Geophysical
Simmonds,I.&Keay,K.(2000)MeanSouthernHemisphereextra- ResearchLetters,35,L15806.
tropicalcyclonebehaviorinthe40-yearNCEP–NCARreanaly- Vera, C.S., Vigliarolo, P.K. & Berbery, E.H. (2002) Cold season
sis.JournalofClimate,13,873–885. synoptic-scale waves over subtropical South America. Monthly
WeatherReview,130,684–699.
| Simmonds, | I. & Wu, X. | (1993) Cyclone | behaviour | response | to  |     |     |     |
| --------- | ----------- | -------------- | --------- | -------- | --- | --- | --- | --- |
changesinwinterSouthernHemispheresea-iceconcentration. Vihma, T. (2014) Effects of Arctic Sea ice decline on weather and
QuarterlyJournaloftheRoyalMeteorologicalSociety,119,1121– climate:areview.SurveysinGeophysics,35,1175–1214.
1148.
Sinclair,M.R.(1995)AclimatologyofcyclogenesisfortheSouthern
|     |     |     |     |     | SUPPORTING | INFORMATION |     |     |
| --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- |
Hemisphere.MonthlyWeatherReview,123,1601–1619.
|     |     |     |     |     | Additional supporting | information | can be | found online |
| --- | --- | --- | --- | --- | --------------------- | ----------- | ------ | ------------ |
Steele,C.,Dorling,S.,vonGlasow,R.&Bacon,J.(2015)Modelling
|            |               |              |              |           | in the Supporting | Information | section at | the end of this |
| ---------- | ------------- | ------------ | ------------ | --------- | ----------------- | ----------- | ---------- | --------------- |
| sea-breeze | climatologies | and          | interactions | on coasts | in the            |             |            |                 |
| southern   | North Sea:    | implications | for offshore | wind      | energy. article.  |             |            |                 |
QuarterlyJournaloftheRoyalMeteorologicalSociety,141,1821–
1835.
Howtocitethisarticle:CoutodeSouza,D.,
Swart,N.C.,Fyfe,J.C.,Gillett,N.&Marshall,G.J.(2015)Compar-
ingtrendsin thesouthernannular modeandsurfacewesterly daSilvaDias,P.L.,Gramcianinov,C.B.,daSilva,
jet.JournalofClimate,28,8840–8859. M.B.L.,&deCamargo,R.(2024).New
Trigo,I.F.(2006)Climatologyandinterannualvariabilityofstorm- perspectivesonSouthAtlanticstormtrackthrough
| tracks | in the EURO-Atlantic |     | sector: a comparison |     | between |     |     |     |
| ------ | -------------------- | --- | -------------------- | --- | ------- | --- | --- | --- |
anautomaticmethodfordetectingextratropical
| ERA-40 | and NCEP/NCAR | reanalyses. | Climate | Dynamics, | 26, |     |     |     |
| ------ | ------------- | ----------- | ------- | --------- | --- | --- | --- | --- |
cyclones'lifecycle.InternationalJournalof
127–143.
Climatology,1–21.https://doi.org/10.1002/joc.8539
| Turner, J. | & Thomas, | J.P. (1994) | Summer-season | mesoscale |     |     |     |     |
| ---------- | --------- | ----------- | ------------- | --------- | --- | --- | --- | --- |
cyclonesintheBellingshausen-Weddellregionoftheantarctic