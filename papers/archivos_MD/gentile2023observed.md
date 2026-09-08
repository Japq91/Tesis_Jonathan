Received:3August2022 Revised:28December2022 Accepted:2January2023 Publishedon:18January2023
DOI:10.1002/joc.7999
RESEARCH ARTICLE
Attribution of observed extreme marine wind speeds
and associated hazards to midlatitude cyclone
conveyor belt jets near the British Isles
Emanuele S. Gentile | Suzanne L. Gray
DepartmentofMeteorology,Universityof
Abstract
Reading,Reading,UK
Extreme windspeeds,gusts,andwind wave heights associatedwith midlatitude
Correspondence cyclonesposeahazardtoshippinglanesandoffshoreinfrastructureoperatingin
EmanueleS.Gentile,Departmentof
theNorthAtlanticOceanseassurroundingtheBritishIsles.Severalstudieshave
Meteorology,UniversityofReading,
ReadingRG66ET,UK. assessed the variability of wind and waves in this region using reanalyses, but
Email:e.gentile@pgr.reading.ac.uk
few have used surface observations of extreme wind speeds and wave heights.
Here,weuseanetworkofmarinesurfacestationstoderivethe2012–2020clima-
Fundinginformation
NaturalEnvironmentResearchCouncil, tology of daily maximum wind speed events. An algorithm is used to attribute
Grant/AwardNumber:NE/R007640/1 theextremewindevents,characterizedasexceedingthe20and25m(cid:1)s −1thresh-
olds,tothecyclonewarmconveyorbelt(WCB),andearly(CCBa)andreturning
(CCBb)coldconveyorbeltjets;cyclonesarematchedwithupto90%ofextreme
wind events. The CCBb is most frequently associated with the strong wind
speeds, accounting for 46 and 59% of the events exceeding the two thresholds,
respectively.TheCCBbalso leads to thelargest numberofcompoundwind and
wavehazardevents(37outof87).AlthoughtheWCBisassociatedwiththesec-
ond largest number of extreme wind events, the CCBa accounts for the second
largestnumberofcompoundextremewindandwaveevents(24).TheERA5rea-
nalysis underestimates the observed extreme wind speeds, and associated gusts
andwind-waveheights,duringextremewindeventsforalltheconveyorbeltjets.
The wind speeds and associated gusts are most underestimated, by median
values of 4.5 and 5.5m(cid:1)s −1, respectively, and similar percentage error (≈25%),
when associated with the CCBb; however, the wind-wave heights are most
underestimated,byamedianof3.4m,whenassociatedwiththeCCBa.Hence,
while the marine CCBb jet,found in mature cyclones, is both most hazardous
and underestimated in the ERA5 near the British Isles, the CCBa jet can be
nearlyashazardouswhenconsideringcompoundwind-waveevents.
KEYWORDS
compoundwind-wavehazard,conveyorbeltjets,ERA5bias,extremegust,extremewind
speed,midlatitudecyclones,reanalysis,surfaceobservations
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttributionLicense,whichpermitsuse,distributionandreproductioninanymedium,provided
theoriginalworkisproperlycited.
©2023TheAuthors.InternationalJournalofClimatologypublishedbyJohnWiley&SonsLtdonbehalfofRoyalMeteorologicalSociety.
IntJClimatol.2023;43:2735–2753. wileyonlinelibrary.com/journal/joc 2735

2736 GENTILEANDGRAY
1 | INTRODUCTION the boundary layer in the warm and cold sectors of
cyclones). Sometimes afiner mesoscaleairstream, theSJ,
Midlatitude cyclones pose a major threat to shipping is present in midlatitude cyclones. The SJ exits from the
lanes and offshore installations located in the seas sur- tip of the hook-shaped cloud head and descends to the
rounding the British Isles (Bell et al., 2017). Associated surface over several hours, producing an additional
strong winds and waves batter wind farms and oil pro- region of strong winds and exceptionally strong gusts
ductionplatforms,leadingtostructuraldamage(Cardone (Clark and Gray, 2018). Besides sting jets, there are also
et al.,2014).Offshore energy industries and weather cen- other fine-scale features associated with midlatitude
tres could benefit from an improved understanding of cyclonesresponsiblefordamagingsurfacewinds,suchas
cyclone features associated with observed extreme sur- the lines of organized convection that occur along cold
face wind speeds and wind-wave heights: offshore indus- frontal boundaries, and (less so) near occluded fronts
tries could better assess the compound wind-wave risk (Clark, 2013; Earl et al., 2017). The strong wind regions
posed by midlatitude cyclones, while weather centres associated with the cyclone conveyor belts are illustrated
could better diagnose and attribute biases in model ana- inFigure1bforareal-worldexamplecyclone,windstorm
lyses and reanalyses to specific cyclone features. In this Friedhelm (2011), using 10-m wind speeds derived from
paper we present a climatology of observed offshore European Centre for Medium-range Weather Forecasts
extreme wind speeds and objectively partition events (ECMWF) fifth generation hourly reanalysis (ERA5). As
accordingtotheassociatedcyclonefeatures. discussed in Vaughan et al. (2015), cyclone Friedhelm
Many studies have linked the extreme wind speeds deepened spectacularly by 44hPa between 1200UTC on
observed by land weather stations and by soundings in December 7 and 1200UTC on December 8 (while cross-
the mid-troposphere to three different airflows within ing the North Atlantic). Structurally, cyclone Friedhelm
midlatitude cyclones (Parton et al., 2010; Martínez- resembled a Shapiro–Keyser cyclone (for the diagram of
Alvarado et al., 2012; Neu et al., 2013; Hewson and a Shapiro–Keyser cyclone, see Figure 1a). The strongest
Neu, 2015): the warm and cold conveyor belt wind jets winds, exceeding 20m(cid:1)s −1, are associated with the CCB,
(WCBandCCB,respectively)andthestingjet(SJ).These while the slightly weaker winds, of up to 18–20m(cid:1)s −1
airflowscanberepresentedbytheconveyorbeltconcep- andlocatedinthewarmsectorofthecyclone,areassoci-
tual model (Browning and Roberts, 1994), illustrated in ated with the WCB. The CCB flow is initially southeast-
Figure 1a. The WCB originates as a near-surface jet, erly (CCBa), but as the CCB wraps around the cyclone
whichcanhaveintensewinds,andthenascendsoverthe centre (located off the east coast of northern Scotland) it
warm front above the cold air below (Martínez-Alvarado changes from northerly to southwesterly (CCBb). Since
et al., 2014). However, some of the strongest and most the WCB is also characterized by a southwesterly flow,
damaging surface winds form on the rear, equatorward knowledge of the boundary between the cold and the
flank of midlatitude cyclones, when the CCB jet wraps warmsectorairmassesisrequiredtodistinguishbetween
around the low-pressure centre and the winds are mixed the two features. Previous studies have shown that the
through the boundary layer producing extreme gusts at CCB and WCB can be easily detected from reanalysis
the surface, as described in Hewson and Neu (2015). In data alone by combining information on location of
earth-relativewinds,theCCBoftenappearssplitintotwo fronts (e.g., diagnosed from the location of the sharpest
components due to the jet, which has a easterly system- equivalent potential temperature gradient) with wind
relative component, opposing the typically northeast- direction (Catto et al., 2015; Hart et al., 2017; Catto and
wards direction of travel of the cyclone (as shown in Raveh-Rubin, 2019; Eisenstein et al., 2022; Volonté
Figure 1a). The part of the CCB leading to strong winds et al., 2022). The CCB and WCB can also be identified
on the rear equatorward flank of the cyclone, termed objectivelyusingcriteriaappliedtoairparceltrajectories.
CCBb, is distinct from the early part of the CCB, termed For example, Madonna et al. (2014) used this method to
CCBa.Therelationshipbetweenthewindspeedandgust produceaclimatologyofWCBsusingreanalysisdata.
speed associated with strong wind jets is dependent on Reanalyses are among the most popular datasets for
the stability, and related height, of the boundary layer. the assessment of both land and marine wind variability.
The WCB jet occurs in the warm sector of the cyclone Besides to being easy to use, reanalyses also provide a
which generally has a shallow stable boundary layer. In physically coherent wind field. However, reanalyses'
contrast, the CCB jet (and particularly the CCBb part of coarse resolution (the highest being ≈30 km in the mid-
it) occurs in the cold sector which typically has a more latitudes) and boundary-layer parametrization issues
unstable and deeper boundary layer (see table 2 in Hew- (Smart and Browning, 2014) make reanalyses less suit-
son and Neu (2015) for the stability characteristics of the able for detecting wind speed extremes and associated
jets and fig. 14 of Sinclair et al. (2010) for the height of weather hazards, such as high waves (Hewson and
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on [10/03/2026].
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

GENTILEANDGRAY 2737
FIGURE 1 (a)ConceptualmodelofaShapiro-KeysercyclonewiththeWCB,CCBa,andCCBbindicated.Frontsaremarked
conventionally,“L”indicatesthecyclonecentreandstipplingindicatescloud.(b)IllustrationoftheconveyorbeltjetsofcycloneFriedhelm
(December8,2011,1700UTC)usingERA5data.Thejetregions(subjectivelyidentified)areenclosedbywhitedashedlinesand10-mwinds
areshownbyarrowswithspeedsshaded.Thebluecrossindicatesthemeansealevelpressureminimumofthecyclone,whilethethickred
lineindicatestheboundarybetweenthewarmandcoldsectors(computedbythealgorithmdevelopedinthispaperdetailedinsection2.4)
[Colourfigurecanbeviewedatwileyonlinelibrary.com]
Neu, 2015; Molina et al., 2021). This shortcoming can be Incontrasttotheseobservation-basedwindandgustcli-
overcome by the use of surface observation data, which, matologies focusing on the UK land, only a few studies
despitetheirinhomogeneity,haveprovedusefultoinves- have focused on the North Sea and other North Atlantic
tigate extreme wind and wave events (Earl and Ocean seas that surround the British Isles. Because of the
Dorling, 2013; Bell et al., 2017). Besides surface observa- dearth of historical time series of wind, gust, and wave
tions, satellite-derived datasets have also been used to heightobservations,thesestudieshavehadtorelyonmodel
detect weather extremes, such as North Atlantic extreme hindcasts, reanalysis data, and just a few surface observa-
wave heights (Rulent et al., 2020; Ponce de Leo(cid:2)n and tions.Acommontraitofthesestudiesisthefocusonwind
Bettencourt, 2021) though, compared to surface observa- energyapplicationsratherthanonthephysicalunderstand-
tions, they present the disadvantages of rain contamina- ing of circulation patterns and wind on gust and wave
tion, a lack of data near land (usually within ≈15 km heights extremes. For example, Geyer et al. (2015) investi-
from the coast), and intermittent temporal sampling gated the 1958–2012 North Sea surface wind climatology
(Bourassaetal.,2019). from a model hindcast in order to derive an assessment of
There are many studies that have investigated the vari- the wind power potential, finding a decadal variation in
abilityoftheextremewindspeedsandgustsassociatedwith wind power as high as 10%. The earlier study of Coelingh
mesoscale cyclone features by utilizing surface observations et al. (1998) compared coastal observations to those from
over the UK land (Hewston and Dorling, 2011; Earl and surfacestationslocatedonthreedifferentoffshoreplatforms
Dorling, 2013; Earl et al., 2017). In summary, these studies in the North Sea, finding a daytime peak in surface wind
find that the prevailing direction of strongest winds and speeds between 1200 and 1400UTC at the coastal stations,
daily maximum gusts (DMGS) is westerly (ranging from but hardly any diurnal variation at the offshore platforms.
northwesterlytosouthwesterly),that ≈80%oftheextreme Furtherresults from Coelingh et al.(1998) highlightedthat
observed wind speeds occur in cyclone-dense seasons, windswithfetchovertheseapresentedsimilardistributions
and that boundary-layer convective-scale processes and ofwindspeedwithwinddirection(aggregatedby12differ-
land surface characteristics can control the intensity of ent sectors) at coastal stations and offshore platforms, as
observed DMGS. Combining the DMGS observed by a expected given that in both cases the wind fetch stretches
land surface station network for the period 2008–2014 overhundredsofkmofseasurface(excludingthesoutherly
with radar imagery and UK surface pressure charts, Earl windswhichwereshieldedatthecoastalstations).Thelink
et al. (2017) manually attributed the recorded DMGS to betweensynoptic-scaleflowinintensemidlatitudecyclones
subsynoptic cyclone features, deriving a statistics of the and associated extreme ocean wave heights has been
frequency with which each cyclone feature (WCB, CCB, exploredeitherbylookingatindividualcasestudyhindcasts
SJ,convectivelines)associatedwithextremeDMGS. (Cardone et al., 2014; Pinto et al., 2014) or by analysing
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

2738 GENTILEANDGRAY
historical series of extreme wind speeds and ocean wave winds that created them, rather than free waves such as
heightsforaselectedsurfaceobservationstation,theForties swells),andhourlyor6-hourlymaximum10-mwindgusts
oil platform in the North Sea (Bell et al., 2017). The latter (depending on availability), observed by ship, buoy (for
studydemonstratedthatthelargestmeasuredwaveheights mostofthe sites),and fixedplatform surfacestations.The
were associated with northwesterly cyclone wind events observations from these stations are reported in the SHIP
aided in growth by the large fetch over the central North synopcodeandarchivedbytheMetOfficeMetDBSystem
Sea,butsoutherlycyclonewindeventswerefoundtocreate at CEDA (Met Office, 2008). The station buoy identifica-
largewaveheightsdespitethelimitedfetch. tion numbers, or call signs for ships and fixed offshore
In this study, we explore the systematic link between platforms, are provided as Supporting Information. The
theconveyorbeltjetsinmidlatitudecyclonesandobserved analysed time period was the 9-year period 2012–2020
extreme wind speeds,gusts,and waveheights for theseas (inclusive), selected because it was the longest period for
surroundingtheBritishIsles.Towardsthisaim,aclimato- which surface observation data were available in all the
logical analysis has been performed using the 2012–2020 North Atlantic Ocean seas surrounding the British Isles
timeseriesofextremewindspeeds,gusts,andwaveheights consideredinthisstudy:theCelticSea,theEnglishChan-
observedat26stationsspreadacrosstheseassurrounding nel, and the southern, central, and northern North Sea.
the British Isles and then the observed extremes objec- The 10-m wind speeds are reported hourly to the nearest
tivelyattributedusinganalgorithmtomidlatitudecyclone 0.1m(cid:1)s −1 and 10(cid:3) by all observation stations, while maxi-
conveyor belt wind jets. The attribution algorithm detects mum gusts are reportedhourly or6-hourly,dependingon
the frontal boundary between the cyclone cold and warm the specific station. The hourly 10-m wind speed is mea-
sectors and then uses the observed surface wind direction sured by averaging the wind fluctuations (sampled every
to distinguish between the WCB, CCBa, and CCBb jets. 0.25s due to their turbulent nature) over the 10-min
Using this partitioning we have quantified the absolute period leading up to the hourly reporting time. The maxi-
and relative 2012–2020 compound wind-wave risk and mum 10-m gust is the maximum 3-s average wind speed
ranked the jets accordingly. Finally, we have determined recordedoverthefulltimeperiodleadinguptothereport-
the relationship between the boundary-layer height diag- ing time (i.e., 1 or 6 hr). Finally, the wind-wave heights
nosed in ERA5 and the jet type, and analysed the ERA5 aremeasuredhourlyandtothenearest0.1m.
biases in wind speeds, gusts, and wave heights associated All the observations considered in this study have
witheachjet.Weexpectthattheresultsofthisstudycould passed the rigorous quality control by the Met Office via
contribute to more accurate estimation of wind power checksontheequipmentandrawdata(MetOffice,2008;
resourcesandcompoundwind-wavehazards,andsobene- Hewston and Dorling, 2011). The dataset was further fil-
fitoffshoreeconomicactors. teredtoguaranteeagoodtemporalcoverageofthe2012–
The remainder of the paper is structured as follows. 2020 period. First, we discarded the stations for which
Section 2 describes the marine observations, reanalysis more than 10% of the 10-m wind speed measurements
data,andjetattributionalgorithmused.Resultsaregiven were missing (discarding 25, though mostly located in
in section 3, where we show the prevailing wind direc- the central and northern North Sea where a dense net-
tion of the extreme wind speeds across the selected work of stations was available), obtaining a network of
marine observation stations along with an analysis of 26 stations which were labelled from A to Z (see map in
their inter- and intra-annual variability. We also deter- Figure2a).Then,foreachstationwediscardedthemaxi-
mine at each station whether the WCB, CCBa, or CCBb mumgustsandwind-waveheighttimeserieswithreports
jetismorelikelytoleadtoanextremewindspeedevent, for fewer than 50 and 10%, respectively, of the times
and then discuss the associated flow characteristics and available. A less strict threshold was used for the gusts
compound wind-wave hazards. Finally, we present the becauseofthedearthofgustmeasurementsovertheseas.
partitioning of ERA5 bias according to the jets. Further At the end of the filtering process, of the 26 stations
discussionandconclusionsaregiveninsection4. reporting 10-m wind, 22 also report wind-wave heights,
and 10 also report maximum gusts (7-hourly and three
6-hourly),asshowninFigure2a.
2 | DATA AND METHODS
2.1 | Observations of wind, maximum 2.2 | Characterization of the extreme tail
gust, and wind-wave heights of the observed wind speeds
Weanalysedhourlyreported10-mwindspeeds,direction, Intheliterature,extremewindspeedsaretypicallydefined
wind-wave height (waves still under the action of the as exceeding an upper percentile of wind speed and so
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on [10/03/2026].
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

GENTILEANDGRAY 2739
FIGURE 2 Legendonnextpage.
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

2740 GENTILEANDGRAY
characterize the upper (or extreme) tail of the wind speed threshold. Moreover, wind directions, gusts, and wind-
distribution at a given observation station or over a given wave heights associated with the DMWS events (i.e., at
geographicalregion(e.g.,HewstonandDorling,2011;Earl thesametimeastheDMWS)areusedtobettercharacter-
and Dorling, 2013; Earl et al., 2017). Here, we define ize the atmospheric flow and sea state. For the three sta-
extreme daily maximum wind speeds as those exceeding tions for which the maximum gust is reported 6-hourly,
the 20 or 25m(cid:1)s −1 threshold. The 20m(cid:1)s −1 threshold cor- the gust associated with the event is that at the nearest
respondstoaBeaufortscaleof8(stronggale),which,over reportingtimeaheadoftheDMWStime.
the sea, is associated with moderately high waves with
theircrests beginning to topple, tumble and rollover,and
probable maximum wave heights of up to 7m 2.3 | ERA5 data
(WMO, 1970). Note, however, that 7m can be considered
quite an extreme wind-wave height. For example, as ERA5 is the fifth generation hourly reanalysis of the
shown by Valiente et al. (2021), the wind-wave heights ECMWF (Hersbach et al., 2020). It provides values for
associated with midlatitude cyclone Xaver (December atmosphere,ocean,wave,andlandsurfacevariableswith
2013), one of the storms that crossed the UK during the a horizontal grid resolution of 0.25(cid:3), corresponding to
2013–2014winter(oneofthestormiestwintersovernorth- ’31 km. The atmospheric component is interpolated to
westEuropeinthepastfewdecades),barelyexceededthe 37 pressure levels from the surface up to 1Pa. Observa-
7m threshold in the North Sea regions where the in-situ tions are assimilated in ERA5 from many satellite and
observation stations used in this paper are located. The conventional surface stations instruments. As detailed in
25m(cid:1)s −1 threshold corresponds to the important opera- Hersbach et al. (2020), because the 10-m wind speed
tional value of power cut-out because wind turbines can observations we consider are encoded in SHIP SYNOP
be forced to shut down for wind speeds exceeding this messages they ought to have been assimilated in ERA5,
threshold to avoid damage from further operation while wind-wave heights and maximum gusts are not
(Dupont et al., 2018; IMAREST, 2018). However, surface (more details in Hersbach et al., 2020). Although wind-
stations report wind speeds at, or corrected to, 10-m wave heights measured by conventional in situ observa-
height,butthehubheightofoffshorewindturbinesistyp- tions are not assimilated in ERA5, significant wave
ically 100–200m and other offshore installations are also heightsremotelysensedbysatellitealtimetersareassimi-
typically taller than 10m. Hence, in section 3.1 the rela- lated(Hersbachetal.,2020).
tionship between 10- and 100-m wind speeds is explored WeextractedfromERA5thefollowingfields:thehor-
by exploiting the availability of both fields in ERA5. izontal components of 10-m wind, 10-m wind direction,
Finally, we define a compound wind-wave hazard, rele- and 10-m maximum gust since previous postprocessing,
vant forpower cut-out, asthe simultaneous occurrence of along with wind-wave height, boundary-layer depth, and
a 10-m wind speed exceeding 25m(cid:1)s −1 and significant 850-hPa relative vorticity, ξ , temperature, and relative
850
wind-wave height exceeding 7m, since, as discussed, humidity.ToselecttheERA5datacorrespondingtoeach
extreme wind and waves exceeding these thresholds can observationstation,weextractedthetemporaltimeseries
damage the offshore infrastructure (PAFA Consulting of the nearest-neighbour ERA5 grid point. Although it
Engineers,2001;IMAREST,2018). could occur that this method attributes the same ERA5
To select only independent extreme wind speed grid points to different stations, this did not happen in
events at each network station, we consider daily maxi- ourstudy.
mum wind speed (DMWS), that is, the strongest wind Itisimportanttonotethatwecomparedtheobserved
speed reported between 0000–2359UTC each day, and maximum gust and wind-wave height observations with
define a DMWS event if this exceeds the 20 or 25m(cid:1)s −1 the corresponding ERA5 fields defined in the same way
FIGURE 2 (a)Mapof10-mwindspeed,wind-waveheight,andmaximumgustobservationstationsforthe2012–2020timeperiod,
surroundedbywindrosesforasetof12representativestationsshowingwindspeeddistributionperwinddirectionsector(of20(cid:3)width
each).The26stationsarelabelledwithlettersfromAtoZ,followinganorderofincreasinglatitude.Stationsaremarkedwithablackstar,
bluestar,orredstaraccordingtowhethertheyreport10-mwindspeed,10-mwindspeedandwind-waveheight,and10-mwindspeed,
wind-waveheights,andgustspeeds,respectively.Thethreedashedcirclesillustratetheclusterofstationsinthenorthern,central,and
southernNorthSea.(b)Boxandwhiskerplotofobserved(blue)andcorrespondingERA5(red)10-mwindspeedateachstation.The
minimumandmaximumvalues(within3σfromthemean)areindicatedbytheendsofthewhiskers,withthemedian,25thand75th
percentilevaluesmarkedbythemiddle,lowerandupperpartsofthebox,respectively[Colourfigurecanbeviewedat
wileyonlinelibrary.com]
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

 10970088, 2023, 6, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| GENTILEANDGRAY |     |     |     |     |     |     |     |     |     |     |     |     | 2741 |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
asforthenetworkstations.Thus,theobservedmaximum large scale background, while the spectral filtering to
gust was compared with ERA5 10-m maximum gust, T63isneededto reducethe noiseinwhatisanother-
F , which is computed based on the argument that the wisenoisyfieldforthepurposeoftracking.
gust
difference between F and the mean 10-m wind speed, 2. ForeveryDMWSevent,determine,withina1,000-km
gust
F 10 , is proportional to the standard deviation of the hori- radius, the nearest midlatitude cyclone track point
zontal wind, σ . The value of σ is computed following defined by the mean sea level pressure minimum and
|     |     | u   |     | u   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesimilarityrelationofPanofskyetal.(1977), matching the same time (to the hour) of the observed
|     |     |     |     |     |     |     | DMWS | event. | If a cyclone | track | point | like | this exists, |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ------------ | ----- | ----- | ---- | ------------ |
(
|     |     |     | (cid:1) | (cid:3) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2:29u(cid:4) 1−0: 5 z 1 L<0 t he e v e n t is c la ss if ie d a s “c y c lon e -a s s o c i ate d ” ( fou n d
|     | σ   | =   |     | blh 3 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | 1 2 L | ,   |     |     |     | ≈ % |     |     |     |     |
u 2:29u(cid:4) L>0 t o b e t r u e fo r 8 5 a n d 9 0 % o f e v e n t s fo r 2 0 a n d
25m(cid:1)s −1thresholds,respectively).
“cyclone-associated”
|     |     |     |     |     |     |     | 3. For each |     |     |     | DMWS | event, | compute |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ---- | ------ | ------- |
where u(cid:4) is the friction velocity, z the boundary-layer the 850-hPa equivalent potential temperature, θ ,
|     |     |     |     | blh |     |     |     |     |     |     |     |     | e850 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
height, L the Monin–Obukhov length, and L<0 indicates representative of the cyclone frontal boundary,
|     |     |     |     | L>0 |     |     |     | eθ  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
an unstable boundary layer, while indicates a stable defined as e850 . Following the methodology of Hart
eθ
boundarylayer.Then,F iscomputedas etal.(2017), isthemeanθ ,obtainedfrom the
|     |     |     | gust |     |     |     |      |             | e850      |     | e850     |            |        |
| --- | --- | --- | ---- | --- | --- | --- | ---- | ----------- | --------- | --- | -------- | ---------- | ------ |
|     |     |     |      |     |     |     | ERA5 | grid points | exceeding |     | the 99th | percentile | of the |
F =F +c u(cid:4)fðz =LÞ, ð1Þ gradient of θ , rθ , within 750km of the cyclone
|     |     | gust | 10 ugn | i   |     |     |         | e850  | e850    |        |         |      |                |
| --- | --- | ---- | ------ | --- | --- | --- | ------- | ----- | ------- | ------ | ------- | ---- | -------------- |
|     |     |      |        |     |     |     | centre. | As in | Manning | et al. | (2022), | grid | points at ele- |
where z i is a scale height of the boundary-layer depth vationsabove500maremaskedbeforecalculatingthe
and c =7:71 is a dimensionless number determined 99th percentile of rθ to remove noise introduced
| ugn |     |     |     |     |     |     |     |     |     | e850 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
fromtheuniversalturbulencespectrafora50%exceeding byorography.
probabilityofthethree-secondwindgust(Beljaars,1987). 4. Attribute the “cyclone-associated” DMWS events to
The value of F every time step, and its maximum the cyclone cold or warm sector by comparing the
gust
|     |     |     |     |     |     |     |     |     | θ   |     | eθ  |     | “cyclone- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
value since previous post-processing is output. To nearest grid point e850 with e850 . Thus, a
account for the effect of deep convection on F , in associated” DMWS is attributed to the cold sector if
gust
|                   |     |        |              |     |              |      | θ <eθ | andtothewarmsectorifθ |     |     |     |      | >eθ  |
| ----------------- | --- | ------ | ------------ | --- | ------------ | ---- | ----- | --------------------- | --- | --- | --- | ---- | ---- |
| strong convective |     | events | a convective |     | contribution | as a |       |                       |     |     |     |      | .    |
|                   |     |        |              |     |              |      | e850  | e850                  |     |     |     | e850 | e850 |
function of the vertical wind shear is added to 5. Further partition the cold and warm sector DMWS
Equation(1),whichbecomes events according to the DMWS wind direction α, in
thefollowingway:
| F =F | +c  | u(cid:4)fðz | =LÞ+C | maxð0,U | −U  | Þ,  |     |     |     |     |     |     |     |
| ---- | --- | ----------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gust | 10  | ugn         | i     | conv    | 850 | 950 |     |     |     |     |     |     |     |
(cid:129)
|     |     |     |     |     |     | ð2Þ | A cold | sector | DMWS  | event         | is attributed |      | to the CCBa |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ----- | ------------- | ------------- | ---- | ----------- |
|     |     |     |     |     |     |     | jet    | if it  | has a | southeasterly |               | wind | direc-      |
(cid:3)≤α≤210(cid:3)).
| where C | is  | the convective |     | mixing | parameter, | set to | tion(90 |     |     |     |     |     |     |
| ------- | --- | -------------- | --- | ------ | ---------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
conv
| =0:6, |     |     |     |     |     |     | (cid:129) |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
C conv and U 850 and U 950 are the wind speeds at 850 A cold sector DMWS event is attributed to the CCBb
and950hPa,respectively. jet if it has a northwesterly wind direc-
|     |     |     |     |     |     |     | tion(240(cid:3)≤α≤360 |     | (cid:3) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------- | --- | --- | --- | --- |
).
|     |     |     |     |     |     |     | (cid:129) A warm | sector | DMWS | event | is attributed |     | to the WCB |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------ | ---- | ----- | ------------- | --- | ---------- |
2.4 | Attribution of DMWS events to jetifithasawinddirectionrangingfromsoutheasterly
| conveyor | belt | jets |     |     |     |     |                     |          | (cid:3)≤α≤250 |        | (cid:3) |        |           |
| -------- | ---- | ---- | --- | --- | --- | --- | ------------------- | -------- | ------------- | ------ | ------- | ------ | --------- |
|          |      |      |     |     |     |     | tosouthwesterly(130 |          |               |        | ).      |        |           |
|          |      |      |     |     |     |     | (cid:129) All the   | cold and | warm          | sector | DMWS    | events | that have |
To determine which conveyor belt jet (WCB, CCBa, and not been attributed to any of the conveyor belt jets are
CCBb) each DMWS event (with winds exceeding 20 or labelledas“other.”
−1)
| 25m(cid:1)s  | is attributed |     | to, the | algorithm | outlined | below |                                                |         |       |      |         |           |      |
| ------------ | ------------- | --- | ------- | --------- | -------- | ----- | ---------------------------------------------- | ------- | ----- | ---- | ------- | --------- | ---- |
| wasfollowed. |               |     |         |           |          |       | ThisclassificationmethodattributesDMWSeventsto |         |       |      |         |           |      |
|              |               |     |         |           |          |       | midlatitude                                    | cyclone | early | CCBs | (CCBa), | returning | CCBs |
1. Calculate the cyclone tracks in the Northern Hemi- (CCBb),orWCBs.AscanbeseeninFigure1b,thestrong
sphere using the TRACK algorithm (Hodges, 1995; winds associated with the WCB jet lie almost entirely
Hodgesetal.,2011)appliedtohourlyrelativevorticity within the warm sector delimited by calculated frontal
ξ
at 850hPa, , smoothed to spectral T63 resolution. boundary.ItislikelythatsomeoftheDMWSeventsclas-
850
Relativevorticityat850hPaisamoreusefulfieldthan sified as “other” correspond to other causes of strong
meansealevelpressureasitallowscyclonesystemsto 10-m winds in cyclones such as convective lines, quasi-
be identified earlier and is also less sensitive to the convective lines, and embedded frontal convection. Also,

2742 GENTILEANDGRAY
some ofthe events attributed to the CCBb jet could actu- England's southwest peninsula) and E (Celtic Sea, south
ally be associated with a SJ as this feature occurs in the of Ireland), followed by station M (central North Sea,
same part of the cyclone as the CCBb (when it occurs). 35.1m(cid:1)s −1). Station B (English Channel) and stations S,
However, all these features are too fine scale to be repre- U,andZ(centralandnorthernNorthSea)alsooccasion-
sented by the (relatively) coarse ’31 km resolution of ally report 10-m wind speeds exceeding 30m(cid:1)s −1, but
themodelusedtogenerateERA5. below 35m(cid:1)s −1. The median of the observed 10-m wind
speeddistributionateachstationvariesbetween ≈6and
≈9 m(cid:1)s−1. Stations B, D, and F located in the English
3 | RESULTS Channel are characterized by median and upper/lower
quartiles ≈1:5m(cid:1)s−1 higher than those of the southern
3.1 | Wind speed variability over the North Sea stations (G–I), but in line with the median of
British Isles surrounding seas the distribution reported by the central North Sea
stations.
The geographic variability of the observed 10-m wind Figure 3 shows the number of exceedences in the
speeds and directions for the period 2012–2020 is shown observations and ERA5 data for both thresholds and for
in Figure 2a,b, along with the map of the location of the each station per year. The northern North Sea and west-
26 network stations. In Figure 2a, a sample of 12 wind ern English Channel stations experience more wind
roses illustrates the prevailing wind direction across the speed events exceeding the 20 and 25m(cid:1)s −1 thresholds
networkstations,whichisoveralldominatedbythewest- per year than those in the southern/central North Sea,
erly sector of the compass. However, some variations in besides presenting higher median and quartile values.
the wind speed direction occur with latitude, longitude, For example, station E, in the Celtic Sea immediately
and distance from the British Isles coasts. The winds for south of Ireland, experiences ≈210 wind speed events
the more southerly stations (A–G) are mainly dominated exceeding 20m(cid:1)s −1 and ≈33 events exceeding 25m(cid:1)s −1,
by the southwestern quadrant, and less so by the north- the largest number of exceedances per year of the two
western quadrant. In comparison, the central (K–T) and wind speed thresholds across all the network stations.
northern North Sea stations (U–Z) generally show less TheotherstationsintheAtlanticOcean,Englishchannel
dominance of the southwestern quadrant. For the three andnorthernNorthSeaexceedthethresholds ≈50%less
northern North Sea stations (V, Y, and Z), the contribu- often than station E, and even fewer exceedances are
tions of the northwestern and southeastern quadrants of observed at the stations in the central North Sea and off
the compass strongly exceed that of the southwestern the coast of East Anglia (in the southern North Sea). In
quadrant. When considering only 10-m wind speeds particular, the stations H–J off East Anglia report
exceeding 25m(cid:1)s −1, a similar pattern is revealed (not between20 and50 exceedances ofthe 20m(cid:1)s −1 threshold
shown). The predominant southeasterly and northwest- and between 0 and 3 exceedances of the 25m(cid:1)s −1 thresh-
erly wind directions in the northern (and less so central) oldperyear,thefewestamongthestations.
North Sea stations suggest a more important role of the ThevariabilityoftheERA510-mwindspeeddistribu-
CCBa and CCBb in producing strong surface winds here tion across the stations mirrors that of the observed
than for the rest of the network stations. Indeed, due to distributions, as shown in Figure 2b. However, non-
theirgeographiclocation,thecentralandnorthernNorth negligible differences can be noted in the median, quar-
Sea stations are exposed to more mature midlatitude tiles and also extremes of the ERA5 and observed
cyclones in which the CCB has had time to develop distributions for several stations. The largest negative
(erodingthewarmsector).However,thelargenumberof biasesbetweenthemedianandtheupper/lowerquartiles
westerly/southwesterly wind events exceeding 20m(cid:1)s −1 ofthe ERA5 and observed 10-mwind speed distributions
atthemoresoutherlystationscouldalsoindicatethatthe can be seen in the Celtic Sea and English Channel sta-
CCBb plays an important role in generating gale-force tions B–F, for which ERA5 underestimates the observed
surface winds in this region. In section 3.3 the method medianandquartilesbyupto ≈2m(cid:1)s−1.Instead,ERA5
presented in section 2 is used to distinguish the different overestimates median and quartiles by up to ≈2 m(cid:1)s−1
conveyorbeltjets. for some of the stations off East Anglia in the southern
Tobettercharacterizethe10-mwindspeedvariability North Sea (for instance, see stations H and I), and for
ateachnetworkstation,weplottedthemedian,quartiles, some of the stations in the central and northern North
and extremes of the 10-m wind speed distribution Sea (for instance, see stations M, N, P, R, and V), with
observed at each station along with the corresponding negligibledifferences≤0:5m(cid:1)s−1 foundfortheothersta-
ERA5 values (see Figure 2b). The strongest wind speeds tions.ThedifferencesbetweenERA5andobservedwinds
are 37.5m(cid:1)s −1 at stations C (off Cornwall, at the tip of have a symmetrical distribution for the low to moderate
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on [10/03/2026].
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

 10970088, 2023, 6, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| GENTILEANDGRAY |     |     |     |     |     |     |     | 2743 |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ---- |
Barchartshowing,ateachnetworkstation,thenumberofobserved(grey)andERA5(orange)(a)20m(cid:1)s−1and(b)25m(cid:1)s−1
| FIGURE | 3   |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- |
thresholdexceedancesof10-mwindspeedeventsperyear[Colourfigurecanbeviewedatwileyonlinelibrary.com]
|     | (2–20m(cid:1)s | −1  |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
wind speed values range), but consistently height of offshore wind turbine hubs), a scatterplot con-
smaller ERA5 values for wind speeds exceeding the sideringallthe10-and100-mERA5windspeeddatacor-
20m(cid:1)s −1threshold,andevenmoresoforthoseexceeding
|     |     |     |     | responding | to the observed | 10-m wind | speed events | by  |
| --- | --- | --- | --- | ---------- | --------------- | --------- | ------------ | --- |
the25m(cid:1)s −1threshold. the network stations is shown in Figure 4. This figure
Further comparison of observed and ERA5 10-m shows a roughly linear dependence of the ERA5 100-m
wind speeds considering the number of exceedances per wind speeds on the ERA5 10-m wind speeds, modelled
year of the 20m(cid:1)s −1 threshold shows that the ERA5 by the linear relationship y=1:23x, with an excellent R2
R2=0:97.
exceedances drop to between half and one third of those fit of As can be seen from Figure 4, for 10-m
observedformostofthestations(Figure3a).Thereduced wind speeds above 20m(cid:1)s −1, the dependence of 100-m
magnitude of the ERA5 wind speeds compared to wind speeds on the 10-m wind speeds becomes slightly
≈25%
observed values is even more accentuated for station E, steeper, giving 100-m wind speeds which are
justsouthofIreland,whichistheonlystationtoreporta largerinvaluethanthecorresponding10-mwindspeeds.
|     |     | 20m(cid:1)s −1 |     |     |     |     | 20m(cid:1)s −1 |     |
| --- | --- | -------------- | --- | --- | --- | --- | -------------- | --- |
10-fold reduction in threshold exceedances. As a result, an ERA5 10-m wind speed of corre-
Consideringthehigherthresholdof25m(cid:1)s −1,only10out sponds to an ERA5 100-m wind speed close to or above
−1,
of the 26 network stations report ERA5 wind speed the power cut-out threshold of 25m(cid:1)s highlighting the
|     |     |     |     |     |     |     | 25m(cid:1)s | −1  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
exceedances (Figure 3b). Station E reports the largest importance of considering both the 20 and
number of ERA5 exceedances (six), followed by X and Z thresholds for 10-m wind speeds in this study. A similar
with five each. In general, the number of observed relationship between ERA5 wind speeds at 10 and 100m
25m(cid:1)s −1 exceedances per year is disproportionately heightwasalsofoundbySunetal.(2021)forsiteslocated
higher than for the ERA5 (up to 20 times as higher). in the Po valley, Italy (though associated with a slightly
steeperslopeof1:3).
| However,       | for station | T and X the        | ERA5 and observed |        |     |     |     |     |
| -------------- | ----------- | ------------------ | ----------------- | ------ | --- | --- | --- | --- |
| wind speeds    | exceedances | of the 25m(cid:1)s | −1 threshold      | are    |     |     |     |     |
| similar. Apart | from these  | two stations,      | the ERA5          | under- |     |     |     |     |
estimatestheexceedencesovertheCelticSea,theEnglish 3.2 | Interannual and monthly
Channel, and the North Sea. In summary, the higher the variability of wind speeds over the British
|               |                  |          |                      | Isles seas |     |     |     |     |
| ------------- | ---------------- | -------- | -------------------- | ---------- | --- | --- | --- | --- |
| observed      | 10-m wind speed, | the more | likely it is that    | the        |     |     |     |     |
| corresponding | speed from       | the ERA5 | will have a negative |            |     |     |     |     |
bias. These results confirm and extend previous findings To characterize the interannual and monthly variability
of Molina et al. (2021) that indicated that European land of extreme wind speed events over the British Isles sur-
stations reporting more frequent exceedances of the rounding seas the number of 10-m wind speed excee-
| 25m(cid:1)s −1 |     |     |     |     |     |     | 25m(cid:1)s −1, |     |
| -------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |
threshold (the only threshold used) were gener- dances of the two thresholds, 20 and are
allyassociatedwithlargernegativebiasintheERA5. aggregated over each station by year in Figure 5a and by
To investigate how the wind speeds at 10m height month in Figure 5b. Overlain on the intra-annual vari-
compare to those at 100m height (approximately the ability plot is the correspondingly averaged monthly

2744 GENTILEANDGRAY
FIGURE 4 Scatterplotof100-m
against10-mERA5windspeedsforall
networkstations(greenscatterpoints).
Theblacklineisthelinearfitofthe
10-mand100-mwindswhileredlineis
thelineofequality.Thegoodnessofthe
linearfitisgivenbytheR2value[Colour
figurecanbeviewedat
wileyonlinelibrary.com]
FIGURE 5 (a)Interannual2012–
2020variabilityofnumberof10-mwind
speedeventsexceedingthe20and
25m(cid:1)s−1threshold,aggregatedoverall
networkstations(b)Monthly,intra-
annualvariabilityof10-mwindspeeds
exceedingthe20and25m(cid:1)s−1thresholds,
aggregatedoverallnetworkstations,and
overlaidbytheaveragesforeachmonth
ofthe2012–2020NAOindexcalculated
fromthemonthlyaveragesproducedby
theClimatePredictionCenteratthe
NationalOceanicAtmospheric
Administration(NOAA,2020)[Colour
figurecanbeviewedat
wileyonlinelibrary.com]
North Atlantic Oscillation (NAO) index. The NAO is a that associated with the 25m(cid:1)s −1 threshold. Some inter-
major mode of wind variability in the Northern Hemi- annual variability can be observed for the 20m(cid:1)s −1
sphere and exhibits strong decadal and seasonal variabil- threshold exceedances, with the years 2013, 2014, and
ity (Hurrell et al., 2003), the latter evident from 2020presentingthethreehighestnumberofexceedances
Figure5b. (381, 402, and 477 events, respectively). Indeed, the two
Figure 5a reveals that the number of exceedances of midlatitude cyclones that are found to affect all the sta-
the 20m(cid:1)s −1 threshold is typically about 300 events per tions, leading to one of the top five DMWS events (all
year for the station network, about 10 times larger than exceeding 25m(cid:1)s −1) recorded by each station, are from
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

GENTILEANDGRAY 2745
the 2013/2014 and the 2019/2020 cyclone season, respec- Considering separately the two CCB jets, the returning
tively, storm Tini, and storm Ciara. However, the inter- CCBb is approximately three times more likely to gener-
annualvariabilityofthenumberof25m(cid:1)s −1exceedances ate an event exceeding the 20m(cid:1)s −1 threshold than the
does not correlate strongly with that of the 20m(cid:1)s −1 earlyCCBa(16%CCBavs.46%CCBbevents),andnearly
exceedances. Figure 5b shows that the winter months, fourtimesmorelikelytogenerateaneventexceedingthe
December–February, account for ≈80% of the 20m(cid:1)s −1 25m(cid:1)s −1 threshold (15% of CCBa vs. 59% CCBb events).
threshold exceedances and ≈90% of the 25m(cid:1)s −1 thresh- The CCBb also accounts for the increase in cold sector
old exceedances. Apart from the NAO index value for eventsbetweenthetwothresholds, beingassociatedwith
September, the monthly NAO index averaged over the 3/5 of the strongest events recorded across the network.
2012–2020 period correlates well with the monthly In comparison, the WCB accounts only for 25% of the
threshold exceedances, being both highest in the late- events exceeding the 20m(cid:1)s −1 threshold and 20% of the
autumn and winter months and lowest over spring and events exceeding the 25m(cid:1)s −1 threshold. Consequently,
summermonths.Thiscorrelationwasexpectedasaposi- theCCBbisthemostlikelyconveyorbelttocausestrong
tiveNAOindexisassociatedwithastrongerNorthAtlan- surfacewindsacrossthestationnetwork,followedbythe
tic jet stream and a northward shift of the storm track WCB and then CCBa. Note that warm or cold sector
leading to northern Europe (including the British Isles) DMWS events that did not exhibit the wind directions
experiencing more cyclones (Hoskins and Hodges, 2019). typically associated with conveyor belts in those sectors
The relationship between the NAO and midlatitude (S/SW for WCB, W/NW for CCBb, and S/SE for CCBa)
cyclone characteristics has also been quantified by were classified as “other” (grey segment in Figure 6a)
Rudeva and Simmonds (2015), who found positive corre- and represent ≈14% and ≈6% of the total number of
lations between frequency of frontal activity and the events exceeding the 20 and 25m(cid:1)s −1 thresholds, respec-
NAO in a belt stretching across the North Atlantic to tively. An examination of Met Office surface analysis
Europe (north of 40(cid:3)N), with maximum correlation coef- charts for some randomly-picked events labelled as
ficient (exceeding 0.7) east of Newfoundland and over “other,”suggestedtheycouldplausiblybeassociatedwith
theUK. convectivelines,quasi-convectivelines,orconvectivesys-
In contrast to the obvious relationship between the temsinthesectors,butthelackofradardataoverthesea
monthly-averaged NAO index and monthly threshold and the relatively coarse resolution of ERA5 prohibited
exceedances shown in Figure 5b, there is no meaningful their objective classification. Note that, compared to the
relationship between the winter-season (or yearly) aver- 20m(cid:1)s −1threshold,thecontributionoftheseunidentified
aged NAO index for each year and the yearly threshold conveyor belt wind jet events halved when considering
exceedances plotted in Figure 5a (not shown). This lack the25m(cid:1)s −1threshold.
of a relationship is consistent with results from recent The CCBb jet is the dominant conveyor belt jet for
papers(e.g.,Laurilaetal.,2021)thatshowthatthecorre- DMWS events exceeding both wind thresholds for each
lation between NAO and 10-m wind speeds is not obvi- cluster of neighbouring stations considered (see
ous,evenonthemuchlongerinterdecadaltimescales. Figure 6c) as well as when aggregating over all stations.
In contrast, the contribution of the WCB and CCBa jets
toeventsisnothomogeneousacrossthestationnetwork.
3.3 | Climatology of conveyor belt jets TheCelticSea,EnglishChannel,andsouthernNorthSea
contributing to extreme observed 10-m stations are more affected by WCB jets than CCBa jets
wind speeds (with the exception of station C) for both wind speed
thresholds. As the latitude and the longitude of the sta-
To investigate the attribution of independent extreme tionsincrease,thecontributionoftheCCBajetsbecomes
wind speed events exceeding the 20 and 25m(cid:1)s −1 thresh- larger than WCB jets, with central North Sea and north-
oldstocycloneWCB,CCBa,andCCBbjets,DMWSevents ern North Sea stations exhibiting CCBa events up to
(computed as the strongest wind speeds observed in the twice as often as WCB events (for instance, see northern
period0000–2359UTCeachday;formoredetails;seesec- NorthSea25m(cid:1)s −1exceedancesinFigure6c).
tion2)areconsidered.PiechartsinFigure6a,bsummarize
the resulting partitioning. Over the 2012–2020 period, the
coldsector(whichincludesCCBaandCCBbjets)accounts 3.4 | Flow characteristics of conveyor
for most of the DMWS events with ≈60% of the events belt wind jets
exceeding the 20m(cid:1)s −1 threshold (across all network sta-
tions; Figure 6a). This percentage rises to ≈75% of the Thecharacteristicsoftheflowassociatedwitheachofthe
total events for those exceeding the 25m(cid:1)s −1 threshold. conveyor belt jets are depicted in Figure 7a–c for the
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on [10/03/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on Wiley
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

2746 GENTILEANDGRAY
FIGURE 6 Legendonnextpage.
DMWS events exceeding the 20 and 25m(cid:1)s −1. The cold WCB) (Figure 7a): the median and the upper quartile of
sector winds (associated with CCBa and CCBb) are more the CCBa and CCBb events exceeding the 20 and
intense than the warm sector winds (associated with the 25m(cid:1)s −1 thresholds are up to 0.5 and 1m(cid:1)s −1 higher,
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

GENTILEANDGRAY 2747
FIGURE 7 Boxplotof(a)observed10-mwindspeed,(b)observedgust,and(c)ERA5boundary-layerheightdistributionsfortheWCB,
CCBa,andCCBbjetsassociatedwiththeDMWSeventsexceeding20m(cid:1)s−1(blue)and25m(cid:1)s−1(red).BoxplotsaredefinedasforFigure2.
(d)HistogramofnumberofDMWSeventsexceeding25m(cid:1)s−1co-occurringwithobservedsignificantwind-waveheighteventsexceeding
7mheight,associatedwithWCB,CCBa,andCCBbjets.Thebluehistogrambarsshowthenumberofthewind-wavecompoundevents
aggregatedoverallthenetworkstationsintheBritishIslessurroundingseas,whiletheredhistogrambarsareforthenorthernandcentral
NorthSeastationclustersonly[Colourfigurecanbeviewedatwileyonlinelibrary.com]
respectively, than the corresponding WCB values. A median and upper quartile values are smaller than the
closer look at the wind speeds exceeding the higher CCBbones:27.8and30.2fortheWCBmedianandupper
threshold shows that, excluding the outliers of each dis- quartile and 27.3 and 29.3 for the corresponding CCBa
tribution, the upper tail (whisker) of the CCBb events is values. Both the median and upper quartile of the gusts
the most intense, ranging between 28.2 and 30.8m(cid:1)s −1, observed for CCBb, CCBa, and WCB events exceeding
but no appreciable difference can be seen between the the 25m(cid:1)s −1 threshold are ≈5, ≈4, and ≈3m(cid:1)s −1 larger,
upper tails for the CCBa and WCB events (both ranging respectively,thanthecorresponding20m(cid:1)s −1values.
between 27.1 and 29.6m(cid:1)s −1). The gustiness of the con- Figure 7c shows that the CCBb events are associated
veyor belt wind jet events, shown in Figure 7b, has been with deeper boundary layers (diagnosed from ERA5)
derived from the observed gusts associated with the than WCB and CCBa events. The median and upper
DMWS events (i.e., taking the gust value closest to the quartile of the boundary-layer height of the CCBb events
time of each DMWS event, as described in section 2.2). exceeding 20m(cid:1)s −1 are ≈200 m higher than those of the
Themedianandupperquartilevaluesofthegustsforthe WCBevents and ≈250 mhigher than thoseoftheCCBa
CCBb events (exceeding 20m(cid:1)s −1) are 28.1 and events. For the higher 25m(cid:1)s −1 threshold, the CCBb
31.8m(cid:1)s −1, respectively, with extreme values reaching boundary-layer height distribution median and upper
39.1m(cid:1)s −1 (excluding outliers). The WCB and CCBa quartile are ≈400 m higher than those for the WCB and
FIGURE 6 Piechartsshowingthepercentageofconveyorbeltjetsassociatedwith(a)>20m(cid:1)s−1and(b)>25m(cid:1)s−1DMWSs,aggregated
overallobservationstations.(c)DistributionofconveyorbeltjetsassociatedwithDMWSsaggregatedoverdistinctgeographicalregionsof
theBritishIslessurroundingseas:CelticSeaandEnglishChannel,southernNorthSea,centralNorthSea,northernNorthSea,illustrating
howtherelativepercentageoffeaturesvarywithlatitudeandlongitudeacrossthenetwork.OrangesectorcorrespondstoWCBevents,grey
sectortoCCBaevents,pinktoCCBbevents,andlightbluetoDMWSswhichcouldnotbeassociatedwithanyofthecyclonefeaturesWCB,
CCBa,andCCBb.Intotalthereare2,267DMWSeventsexceedingthe20m(cid:1)s−1threshold,and267DMWSeventsexceedingthe25m(cid:1)s−1
thresholdassociatedwithamidlatitudecyclonetrackpoint[Colourfigurecanbeviewedatwileyonlinelibrary.com]
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

2748 GENTILEANDGRAY
CCBa, almost twice as large as those observed for the its intense northwesterly/westerly winds favours the for-
lower 20m(cid:1)s −1 threshold. When considering only the mation of extreme wind-wave heights, as noted by Ponce
CCBb boundary-layer height values lying above the dis- de Leo(cid:2)n and Guedes Soares (2014), Bell et al. (2017), and
tribution upperquartile,these canreach ≈2750 m, com- PoncedeLeo(cid:2)n andBettencourt(2021).Notethat,because
paredtomaximumWCBandCCBavaluesof ≈2200and the 100-m wind speeds typically exceed those at 10-m
≈1800 m, respectively (excluding outliers). The deeper (Figure 4 showed that they are ≈25% stronger in ERA5
boundary layers associated with the CCBb jet compared data) wind turbines are likely to cut-out at 10-m wind
to the WCB and CCBa jets are consistent with expecta- speed thresholds weaker than 25m(cid:1)s −1. Also significant
tions for a jet in the cold sector of cyclones (e.g., Sinclair wave heights of around 2m can be sufficient to inhibit
etal.,2010). the safe working of associated vessels, far less than the
Overall, these results indicate that the CCBb is associ- 7m threshold used here. Hence, this definition of com-
ated with the strongest observed winds, the highest gusti- poundwind-wavehazardscanbeconsideredextreme.
ness, and the deepest boundary layers. The WCB and
CCBacanalsoproduceverystrongwinds,butnotasstrong
as those attributed to the CCBb. This is likely influenced 3.5 | ERA5 bias of the conveyor belt jet
somewhat by the instability in the surface layer generated winds and waves
when the cool air of the CCBb hooks around the cyclone
pressurelowanddescendsoverwarmeroceanwatersfacil- ThedistributionofthebiasoftheERA510-mwinds,gusts,
itating the downward mixing of fast flowing air from the and wind-wave heights associated with the observed WCB,
topoftheboundarylayerandthusproducingstrongerand CCBa, CCBb jet events is shown in the box plots in
gustier winds, compared to the other cyclone features. Figure 8. On average the ERA5 underestimates all three
Despite slightly stronger winds in the CCBa events, the fieldsfortheevents.TheCCBbeventshavethehighestneg-
medianoftheCCBagustsis≈1m(cid:1)s −1lessintensethanfor ative bias with a median at −4.6m(cid:1)s −1, roughly 0.5m(cid:1)s −1
WCB events. A possible explanation is that the typically larger in magnitude than for WCB events and 1.2m(cid:1)s −1
deeper boundary layer associated with the WCB is more larger than for CCBa events (Figure 8a). The same pattern
turbulent, leading to enhanced momentum transport occursforthelowertails(largernegativebiases)ofthedistri-
towardsthesurfaceandconsequentlystrongergusts. butions, as defined by the lower whiskers of the box plots,
Figure 7d shows the compound wind-wave hazard with values reaching −12m(cid:1)s −1 for CCBb events (though
reported by the network stations (wind speed exceeding theloweroutliersextendtosimilarvaluesfortheWCBand
25m(cid:1)s −1 co-occurring with wind-wave height exceeding CCBb). The differences between the ERA5 gust bias distri-
7m atthe sametimeasa DMWS event). The CCBb jet is butions for each jet event follow a similar pattern to those
themosthazardousfollowedbytheCCBajetandthenthe forthe10-mwindspeedbiases(Figure8b):thelowertailof
WCB jet. The network stations reported 37 compound theCCBbeventsgustbiasextendsto−20.2m(cid:1)s −1(without-
wind-wavehazardsassociatedwiththeCCBbjet,24associ- liers extending to −23.3m(cid:1)s −1). As discussed in section 2.2,
ated with the CCBa jet, and 10 associated with the WCB threestationsonlyreportgusts6-hourly.However,virtually
jet. Considering the North Sea stations only, the gap identicalmedianandquartileswereobtainedifobservations
between the number of compound wind-wave hazards from these stations were excluded (although there were
producedbytheCCBbandCCBajetsisevensmaller,with slight changes to the extreme values of gust bias distribu-
the CCBb jet producing only 2 more compound wind- tion). This similarity implies that the results are robust to
wave hazards, 26, than the CCBa jet, 24. Moreover, thedifferentreportingfrequencies.
Figure 7d shows that the CCBa is more than twice as The distribution of the biases for the WCB events,
likely as the WCB jet to produce a compound wind-wave and more so for the CCBa events, are narrower than the
hazard for the full set of network stations and more than CCBb events for all fields considered, even when consid-
three times more likely when considering only the North ering the outliers. However, while the gust and 10-m
Sea stations,despite the WCB jet being responsible for5% wind speed bias distributions of the CCBa and WCB
morecyclone-associatedDMWSeventsexceeding25m(cid:1)s −1 eventsarecharacterizedbyasmallermagnitudemedians
thantheCCBa(Figure6b).Overall,thesefindingsindicate than for the CCBb events, the CCBa and WCB events
that the most likely wind speed directions for compound wind-wave height bias distributions are characterized by
wind-wave hazards are westerly/northwesterly flow (asso- a larger magnitude median than for the CCBb events
ciatedwiththeCCBb)followedbythesouth/southeasterly (−3:4, −2:7, and −2:0 m for CCBa, WCB, and CCBb
flow (associated with the CCBa). A plausible explanation events,respectively).
for the highest number of compound wind-wave hazards To investigate whether the larger absolute errors (rel-
beingattributedtotheCCBbbeingisthatthelongfetchof ative to observed values) of ERA5 maximum gusts
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
by
University
Of
Sao
Paulo
- Brazil,
Wiley
Online
Library
on [10/03/2026].
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

GENTILEANDGRAY 2749
FIGURE 8 (a–c)BoxplotsshowingthebiasofERA5for(a)10-mwindspeed,(b)gust,and(c)wind-waveheightsvaluesofthe
DMWSs,computedasthedifferencebetweenERA5andobservedvaluesandpartitionedbytheconveyorbeltjets(WCB,CCBa,andCCBb).
(d)BoxplotsofthepercentageERA5error,computedfrom100×(ERA5value-observation)/observation,foreach10-mwindspeed(black
boxplots)andmaximumgust(redboxplots).BoxplotsaredefinedasforFigure2.[Colourfigurecanbeviewedatwileyonlinelibrary.com]
comparedtoERA510-mwindspeedsweresimplydueto has been produced for a 9-year time period (2012–2020)
the generally larger wind gust values or instead also cor- based on a network of 26 stations, and extreme events
respondedtoaproportionallylargererror,thepercentage havebeenattributedtomidlatitudecycloneconveyorbelt
error was computed and partitioned per conveyor belt as jets.ExtremeDMWSeventsweredefinedasoccurringfor
shown in Figure 8d. For each conveyor belt jet, the 10-m wind speeds exceeding the 20 and 25m(cid:1)s −1 thresh-
median of the ERA5 10-m wind speed percentage error olds;thesetwothresholdscharacterizetheextremetailof
roughlycorrespondstothatofthemaximumgust(within the wind speed distribution. The extreme DMWS events
≈±2%), indicating that the larger absolute errors of the were objectively attributed to a cyclone conveyor belt jet
ERA5 maximum gusts do not translate into proportion- (WCB, CCBa, or CCBb) by a two-step algorithm. First,
ally higher errors (once normalized by the field value). these events are attributed to a cyclone if they occurred
However, the relative differences between the conveyor within a 1,000-km radius from a midlatitude cyclone
beltjetsshowninFigure8a,barepreservedwhenconsid- track point defined by the mean sea level pressure mini-
ering the percentage error. The CCBb jet has the highest mumatacoincident time.Theneachevent isobjectively
negative percentage error in 10-m wind speeds and gusts attributed to a jet based on whether the event is in the
(medians, respectively, of −25% and −25:5%), followed cold or warm sector of the cyclone (diagnosed from
by the WCB jet (medians, respectively, of −22:5% and ERA5 data) and the observed wind direction. We also
−22:6%), and then the CCBa jet (medians, respectively, analysed the distributions of observed gusts and wind-
of −16:3%and −14:4%),mirroringthepatternfoundfor wave heights, and ERA5 boundary-layer heights, associ-
theabsoluteerrors. ated with each jet event. The climatological compound
hazard of each jet was determined by computing the
number of DMWS events with wind speeds exceeding
4 | DISCUSSION AND 25m(cid:1)s −1 and co-occurring wind-wave heights exceeding
CONCLUSION 7m. Lastly, we calculated the ERA5 bias in the DMWS
events associated with the jets to demonstrate the limita-
In this study, a climatology of observed marine extreme tions of ERA5 for evaluation of marine wind speeds and
wind speeds over the seas surrounding the British Isles theassociatedgustsandwind-waveheights.
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

2750 GENTILEANDGRAY
The climatology showed that the winds recorded by explained by the British Isles being at the end of the
thenetworkstationslocatedintheCelticseaandEnglish North Atlantic storm track (Dacre and Gray, 2009).
Channel were predominantly westerly and southwest- Because the WCB develops earlier than the CCB in the
erly, consistent with previous extreme wind and gust cli- midlatitude cyclone lifecycle (see fig. 1 in Hewson and
matologies over the UK land (Hewston and Neu, 2015), by the time the cyclones reach the British
Dorling, 2011), but stations located in the central North Isles the warm sector has already been eroded. In fact,
Sea and northern North Sea also recorded pronounced thecentralNorthSeastationsreportedthesmallestnum-
northwesterly and southeasterly wind direction compo- berofDMWSeventsassociatedwiththeWCB,withthese
nents. The stations in the English Channel and northern stationsbeingthefarthestfromthestormtracksreaching
North Sea recorded up to 1m(cid:1)s −1 higher median wind theBritishIsles.
speeds than those inthe central and southern NorthSea, The CCBb jet led to stronger winds at the surface
thelatterreportingvirtuallynoexceedancesofthehigher and, during DMWS events, is associated with higher
25m(cid:1)s −1 threshold due to sheltering from the nearby gusts than CCBa and WCB, probably because the CCBb
land. Comparable differences in magnitude between boundary layer is buoyancy driven, as suggested by the
meanwindspeedsinthenorthern NorthSeaandcentral deeper CCBb ERA5 boundary-layer heights than the
and southern North Sea were also found by Laurila et al. CCBa and WCB jets. The cool air of the CCB, while
(2021) for a longer time period climatology (1979–2018) hooking around the cyclone low-pressure centre and
of wind speeds from the ERA5 over the North Atlantic flowing over warmer ocean water, forces large and posi-
andEuropeandomain. tive heat fluxes, in addition to the large momentum
The DMWS events did not show a clear interannual fluxes associated with wind shear (Sinclair et al., 2010).
trend. However, the 2years that exhibited the most The resulting unstable and turbulent surface layer facili-
events exceeding the 20m(cid:1)s −1 threshold (2014 and 2020 tates the downward mixing of high momentum air from
with approximately 400 and 500 exceedances, respec- theboundary-layertopandproducesstrongerandgustier
tively)werealsocharacterizedbythemostdensemidlati- winds compared to the other jets (Coronel et al., 2016).
tude cyclone seasons, as reported by (Kendon, 2020). Instead,thewarmairoftheWCB,whileflowingoverthe
When considering the seasonal trend, the winter months cooler ocean water, forces negative heat fluxes which
(December–February) were the dominant contributors, enhancethestaticstabilityoftheboundarylayer,leading
accounting for 70% and 80% of the extreme wind speeds to a more shallow, shear-driven boundary layer, as sug-
exceeding the 20 and 25m(cid:1)s −1 thresholds, respectively; gested by the shallower boundary-layer heights than the
this is consistent with Earl et al. (2017) results based on CCBb events. Lastly, that the CCBa events are character-
extrememaximumgusts(top2and0.1%)observedbythe ized by smaller gusts than WCB events despite being
UKlandstations. associated with larger surface wind speeds can be plausi-
Objective attribution, by means of an algorithm, of bly explained by the magnitude of the (positive) surface
the extreme DMWS events exceeding the 20m(cid:1)s −1 heat fluxes being smaller than on the equatorward flank
threshold (over the period 2012–2020) to the conveyor ofthecyclone(wheretheCCBboccurs),giventhatinthe
beltjetsdemonstrated thattheCCBb jet,occurring when CCBa (the early part of the CCB) the CCB cool air has
the direction of the CCB jet is aligned with the cyclone notalreadymixeddowntothesurfacelayer.
direction of travel, accounts for most DMWS events In addition to being associated with the largest num-
(46%), followed by the WCB (25%), and then the early ber of extreme DMWSs events, the CCBb jet was also
part of the CCB, the CCBa (15%). The CCBb is found to found to be responsible for the largest number of com-
playaneven larger roleininfluencing theDMWSevents pound wind-wave hazards, followed by the CCBa and
exceeding the higher 25m(cid:1)s −1 threshold (59%). In con- then WCB jets. Although the CCBa accounted for fewer
trast, the role of the WCB is reduced, accounting just for eventsexceedingthe25m(cid:1)s −1thresholdthantheWCB,it
20% of these events, consistent with results found for led to more than twice the number of compound wind-
cyclone feature association over land (Earl et al., 2017). wave hazards than the WCB, only ≈30% less than for
When considering separately the different regions of the theCCBb.WhenrestrictingtheanalysistotheNorthSea
North Atlantic Ocean seas surrounding the British Isles, stations only, the southerly/southeasterly CCBa events
the CCBb is confirmed as the most dominant feature in were found to cause 24 compound wind-wave hazards,
all regions, but for the central and northern North Sea just 2 fewer than those caused by westerly/northwesterly
regions the CCBa replaces the WCB as the second most CCBbevents.ThisresultextendspreviousfindingsofBell
dominant jet. Cold sector (CCBa and CCBb) events are et al. (2017) who also found that cyclone-associated
three to four times more likely than warm sector (WCB) southerly winds can create nearly as many large wave
events for both thresholds considered, and this can be heightsasnorthwesterlywindsdespitetheirlimitedfetch
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

 10970088, 2023, 6, Downloaded from https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999 by University Of Sao Paulo - Brazil, Wiley Online Library on [10/03/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| GENTILEANDGRAY |     |     |     |     |     |     |     |     |     |     |     | 2751 |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
over the North Sea. However, unlike in this paper they marine hazards in both weather forecasts and climate
| did not | perform | an objective |     | attribution | to  | the conveyor |     | integrations. |     |     |     |     |
| ------- | ------- | ------------ | --- | ----------- | --- | ------------ | --- | ------------- | --- | --- | --- | --- |
beltjets.
The partitioning of the ERA5 biases showed that the AUTHOR CONTRIBUTIONS
ERA5 typically underestimated the observed extreme Emanuele S. Gentile: Conceptualization; investigation;
wind speeds, gusts and wave heights for all jet events. writing – original draft; methodology; validation;
–
The extreme winds and gusts were most underestimated visualization; writing review and editing; software;
fortheCCBbevents,withmedianabsolutebiasesof−4.5 formal analysis; data curation. Suzanne L. Gray: Con-
−1,
and −5.5m(cid:1)s respectively, but approximately equal ceptualization;fundingacquisition;methodology;writing
|     |     |     |     |     | −25%) |     |     | –reviewand |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ---------- | --- | --- | --- | --- |
percentage errors (approximately due to the editing; formalanalysis;project administra-
larger values of the maximum gusts relative to the 10-m tion;resources;supervision.
| wind speeds. | However, |     | the | largest | underestimate |     | of the |     |     |     |     |     |
| ------------ | -------- | --- | --- | ------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
wind-wave heights was associated with the CCBa events, ACKNOWLEDGEMENTS
with a median absolute bias of −2:88 m. A possible WearegratefultoDr.KevinHodges(UniversityofRead-
explanation could be that the generation of large wind- ing) for provision of the cyclone tracking algorithm and
waves occurring when the wind has a short fetch (as for support for its use in the algorithm developed and used
the CCBa jet events in the North Sea) is less well repre- in this paper. Emanuele S. Gentile's contribution was
sented in ERA5 than when the fetch is longer (as for the funded through a Natural Environment Research Coun-
CCBb jet events, associated with the smallest bias). As cil (NERC) Industrial CASE studentship in collaboration
the resolution of ERA5 is insufficient to represent meso- withtheMetOffice(NE/R007640/1).
| scale extratropical |     |     | cyclone | processes | associated |     | with |     |     |     |     |     |
| ------------------- | --- | --- | ------- | --------- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
strong winds and gusts at the surface such as SJs and CONFLICT OF INTEREST
convective lines, it was not possible to attribute extreme Theauthorsdeclarenopotentialconflictofinterest.
DMWSeventstotheseandothermesoscalefeatures.The
SJ precursor tool developed by Martínez-Alvarado et al. DATA AVAILABILITY STATEMENT
(2012) could be used to determine the likelihood that The ERA5 dataset is publicly available and Global
some of the events attributed to the CCBb by the ad hoc Marine Meteorological Observations data is available
algorithmdevelopedhereareinsteadassociatedwithSJs. uponrequesttoCEDA(MetOffice,2008).
| By combining |     | the attribution |             | algorithm | with   | the  | SJ pre-  |     |     |     |     |     |
| ------------ | --- | --------------- | ----------- | --------- | ------ | ---- | -------- | --- | --- | --- | --- | --- |
| cursor tool, | it  | would           | be possible | to        | obtain | both | an esti- |     |     |     |     |     |
REFERENCES
mateoftheERA5biasassociatedwiththeSJandamore
Beljaars,A.(1987)Theinfluenceofsamplingandfilteringonmea-
| accurate | estimate | of  | the ERA5 | bias | associated | with | the |     |     |     |     |     |
| -------- | -------- | --- | -------- | ---- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
CCBb.Inaddition,therecentavailabilityofnewhighres- suredwindgusts.JournalofAtmosphericandOceanicTechnol-
ogy,4,613–626.
| olution | re-analysis | and | other | products | providing |     | wind |     |     |     |     |     |
| ------- | ----------- | --- | ----- | -------- | --------- | --- | ---- | --- | --- | --- | --- | --- |
Bell,R.,Gray,S.andJones,O.(2017)NorthAtlanticstormdriving
| speeds | over decadal |     | periods | with | hourly | or subhourly |     |     |     |     |     |     |
| ------ | ------------ | --- | ------- | ---- | ------ | ------------ | --- | --- | --- | --- | --- | --- |
ofextremewaveheightsintheNorthSea.GeophysicalResearch
temporalfrequencycouldformthebasisoffurtherfuture
Letters,122,3253–3268.
research on attribution of extreme wind speeds to meso- Bourassa, M.A., Meissner, T., Cerovecki, I., Chang, P.S., Dong, X.,
| scale extratropical |     | cyclone |     | features. | Examples | of  | these |     |     |     |     |     |
| ------------------- | --- | ------- | --- | --------- | -------- | --- | ----- | --- | --- | --- | --- | --- |
DeChiara,G.,Donlon,C.,Dukhovskoy,D.S.,Elya,J.,Fore,A.,
products are the recently developed Copernicus Fewings, M.R., Foster, R.C., Gille, S.T., Haus, B.K., Hristova-
Veleva,S.,Holbach,H.M.,Jelenak,Z.,Knaff,J.A.,Kranz,S.A.,
| European | Regional |       | Reanalysis | (CERRA) |          | and the | New   |             |                  |               |                |             |
| -------- | -------- | ----- | ---------- | ------- | -------- | ------- | ----- | ----------- | ---------------- | ------------- | -------------- | ----------- |
|          |          |       |            |         |          |         |       | Manaster,   | A., Mazloff, M., | Mears,        | C.,            | Mouche, A., |
| European | Wind     | Atlas | (mesoscale |         | dataset) | with    | 5.5km |             |                  |               |                |             |
|          |          |       |            |         |          |         |       | Portabella, | M., Reul, N.,    | Ricciardulli, | L., Rodriguez, | E.,         |
and3kmgridspacing,respectively.
|          |     |         |        |      |           |     |        | Sampson, | C., Solis, D., Stoffelen, | A., | Stukel, M.R., | Stiles, B., |
| -------- | --- | ------- | ------ | ---- | --------- | --- | ------ | -------- | ------------------------- | --- | ------------- | ----------- |
| Overall, | our | results | reveal | that | hazardous |     | marine |          |                           |     |               |             |
Weissman,D.andWentz,F.(2019)Remotelysensedwindsand
| wind (both | 10-m | wind | and | gust) and | compound |     | wind- |     |     |     |     |     |
| ---------- | ---- | ---- | --- | --------- | -------- | --- | ----- | --- | --- | --- | --- | --- |
windstressesformarineforecastingandoceanmodeling.Fron-
wave events near the British Isles are most commonly tiersinMarineScience,6,1–28.
associated with the CCBb jet that occurs when the CCB Browning, K.A. and Roberts, N.M. (1994) Structure of a frontal
hooks around the low-pressure cyclone centre into the cyclone. Quarterly Journal of the Royal Meteorological Society,
120,1535–1557.
| southwest | quadrant |           | of a mature | cyclone.  |      | However,    | the |              |                       |          |                |      |
| --------- | -------- | --------- | ----------- | --------- | ---- | ----------- | --- | ------------ | --------------------- | -------- | -------------- | ---- |
|           |          |           |             |           |      |             |     | Cardone, V., | Callahan, B.T., Chen, | H., Cox, | A.T., Morrone, | M.A. |
| CCBa jet  | can      | be nearly | as          | hazardous | when | considering |     |              |                       |          |                |      |
andSwail,V.R.(2014)Globaldistributionandrisktoshipping
compoundwind-waveevents,especiallyintheNorthSea
ofveryextremeseastates(VESS).InternationalJournalofCli-
| with24CCBaevents |     |     | overthe9yearsanalysedcompared |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
matology,35,69–84.
to 26 CCBb events. Hence, accurate simulation of these Catto,J.,Madonna,E.,Joos,H.,Rudeva,I.andSimmonds,I.(2015)
| cyclone | conveyor | belt | jets | is critical | for | assessment | of  |                     |         |            |      |                |
| ------- | -------- | ---- | ---- | ----------- | --- | ---------- | --- | ------------------- | ------- | ---------- | ---- | -------------- |
|         |          |      |      |             |     |            |     | Global relationship | between | fronts and | warm | conveyor belts |

2752 GENTILEANDGRAY
and the impact on extreme precipitation. Journal of Climate, Hodges,K.I., Lee,R.W. and Bengtsson, L. (2011) Acomparison of
28,8411–8429. extratropical cyclones in recent reanalyses ERA-Interim,
Catto,J. andRaveh-Rubin,S.(2019)Climatologyanddynamicsof NASA,MERRA,NCEP,CFSR,andJRA-25.JournalofClimate,
thelinkbetweendryintrusionsandcoldfrontsduringwinter. 24,4888–4906.
PartI:globalclimatology.ClimateDynamics,53,1873–1892. Hoskins,B.J.andHodges,K.I.(2019)Theannualcycleofnorthern
Clark, M. (2013) A provisional climatology of cool-season convec- hemisphere storm tracks. Part I: seasons. Journal of Climate,
tivelinesintheUK.AtmosphericResearch,123,180–196. 32,1743–1760.
Clark,P.A.andGray,S.L.(2018)Stingjetsinextratropicalcyclones: Hurrell, J.W.,Kushnir,Y.,Ottersen,G.andVisbeck,M.(2003) The
areview.Quarterly Journalofthe RoyalMeteorological Society, NorthAtlanticOscillation:ClimateSignificanceandEnvironmen-
144,943–969. talImpact.WashingtonD.C.:AmericanGeophysicalUnion.
Coelingh,J.,vanWijk,A.andHoltslag,A.(1998)Analysisofwind IMAREST. (2018) Metocean procedures guide for offshore renew-
speed observations over the North Sea coast. Journal of Wind ables. Available at: https://www.imarest.org/reports/650-
EngineeringandIndustrialAerodynamics,73,125–144. metocean-procedures-guide/file.
Coronel, B., Ricard, D., Rivière, G. and Arbogast, P. (2016) Cold- Kendon, M. (2020) Met Office report of storm Ciara. Available at:
conveyor-belt jet, sting jet and slantwise circulations in ideal- https://www.metoffice.gov.uk/binaries/content/assets/metoffice
izedsimulationsofextratropicalcyclones.QuarterlyJournalof govuk/pdf/weather/learn-about/uk-past-events/interesting/
theRoyalMeteorologicalSociety,142,1781–1796. 2020/2020_02_storm_ciara.pdf.
Dacre,H.andGray,S.(2009)Thespatialdistributionandevolution Laurila, T.K., Sinclair, V.A. and Gregow, H. (2021) Climatology,
characteristics of North Atlantic cyclones. Monthly Weather variability, and trends in near-surface wind speeds over the
Review,137,99–115. North Atlantic and Europe during 1979–2018 based on ERA5.
Dupont,E.,Koppelaar,R.andJeanmart,H.(2018)Globalavailable InternationalJournalofClimatology,41,2253–2278.
wind energy with physical and energy return on investment Madonna, E., Wernli, H., Joos, H. and Martius, O. (2014) Warm
constraints.AppliedEnergy,209,322–338. conveyorbeltsintheERA-Interimdataset(1979–2010).PartI:
Earl,N.andDorling,S.(2013)1980–2010variabilityinU.K.surface climatology and potential vorticity evolution. Journal of Cli-
windclimate.JournalofClimate,26,1172–1191. mate,27,3–26.
Earl,N.,Dorling,S.,Starks,M.andFinch,R.(2017)Subsynoptic-scale Manning, C., Kendon, E., Fowler, H., Roberts, N.M., Berthou, S.,
featuresassociatedwithextremesurfacegustsinUKextratropical Suri,D.andRoberts,M.(2022)Extremewindstormsandsting
cycloneevents.GeophysicalResearchLetters,44,3932–3940. jetsinconvection-permitting climatesimulationsoverEurope.
Eisenstein,L.,Schulz,B.,Qadir,G.A.,Pinto,J.G.andKnippertz,P. ClimateDynamics,58,2387–2404.
(2022) Objective identification of high-wind features within Martínez-Alvarado, O., Baker, L.H., Gray, S.L., Methven, J. and
extratropical cyclones using a probabilistic random forest Plant, R.S. (2014) Distinguishing the cold conveyor belt and
(RAMEFI).PartI:methodandillustrativecasestudies.Weather stingjetairstreamsinanintenseextratropicalcyclone.Monthly
andClimateDynamicsDiscussions,3,1157–1182. WeatherReview,142,2571–2595.
Geyer, B., Bisling, P. and Winterfeldt, J. (2015) Climatology of Martínez-Alvarado, O.S., Gray, S., Catto, J. and Clark, P. (2012)
North Sea wind energy derived from a model hindcast for Sting jets in intense winter North-Atlantic windstorms. Envi-
1958–2012.JournalofWindEngineeringandIndustrialAerody- ronmentalResearchLetters,7,1–8.
namics,147,18–29. MetOffice.(2008)ShipSYNOPreportsfromship,buoyandfixedplat-
Hart,N.C.G.,Gray,S.L.andClark,P.A.(2017)Sting-jetwindstorms form stations collected by the Met Office MetDB System. NCAS
over the North Atlantic: climatology and contribution to BritishAtmosphericDataCentre.Availableat:https://catalogue.
extremewindrisk.JournalofClimate,30,5455–5471. ceda.ac.uk/uuid/65ca7898647cc3686492bcb8bb483a1cl[Accessed
Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., Hor(cid:2)anyi, A., on10thDecember2021].
Muñoz-Sabater, J., Nicolas, J., Peubey, C., Radu, R., Molina,M.O.,Gutiérrez,C.andS(cid:2)anchez,E.(2021)Comparisonof
Schepers, D., Simmons, A., Soci, C., Abdalla, S., Abellan, X., ERA5 surface wind speed climatologies over Europe with
Balsamo, G., Bechtold, P., Biavati, G., Bidlot, J., Bonavita, M., observationsfromtheHadISDdataset.QuarterlyJournalofthe
De Chiara, G., Dahlgren, P., Dee, D., Diamantakis, M., RoyalMeteorologicalSociety,144,943–969.
Dragani, R., Flemming, J., Forbes, R., Fuentes, M., Geer, A., Neu, U., Akperov, M.G., Bellenbaum, N., Benestad, R., Blender, R.,
Haimberger,L.,Healy,S.,Hogan,R.,Ho(cid:2)lm,E.,Janiskov(cid:2)a,M., Caballero,R.,Cocozza,A.,Dacre,H.F., Feng,Y., Fraedrich,K.,
Keeley, S., Laloyaux, P., Lopez, P., Lupu, C., Radnoti, G., de Grieger, J., Gulev, S., Hanley, J., Hewson, T., Inatsu, M.,
Rosnay, P., Rozum, I., Vamborg, F., Villaume, S. and Keay,K.,Kew,S.F.,Kindem,I.,Leckebusch,G.C.,Liberato,M.L.
Thépaut, J.-N. (2020) The ERA5 global reanalysis. Quarterly R.,Lionello,P.,Mokhov,I.I.,Pinto,J.G.,Raible,C.C.,Reale,M.,
JournaloftheRoyalMeteorologicalSociety,146,1999–2049. Rudeva,I.,Schuster,M.,Simmonds,I.,Sinclair,M.,Sprenger,M.,
Hewson, T.D. and Neu, U. (2015) Cyclones, windstorms and the Tilinina, N.D., Trigo, I.F., Ulbrich, S., Ulbrich, U., Wang, X.L.
IMILASTproject.TellusA,67,27–128. andWernli,H.(2013)IMILAST:acommunityefforttointercom-
Hewston, R. and Dorling, S. (2011) An analysis of observed daily pareextratropicalcyclonedetectionandtrackingalgorithms.Bul-
maximum wind gusts in the UK. Journal of Wind Engineering letinoftheAmericanMeteorologicalSociety,94,529–547.
andIndustrialAerodynamics,91,845–856. NOAA.(2020)NorthAtlanticOscillation(NAO).Availableat:www.
Hodges, K.I. (1995) Feature tracking on the unit sphere. Monthly cpc.ncep.noaa.gov/products/precip/CWlink/pna/nao.shtml
WeatherReview,123,3458–3465. [Accessedon30thMarch2022].
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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

GENTILEANDGRAY 2753
PAFAConsultingEngineers.(2001)Weather-sensitiveoffshoreoper- (2021) The impact of wave model source terms and coupling
ations and Metocean data. Available at: https://www.hse.gov. strategies to rapidly developing waves across the north-west
uk/research/otopdf/2001/oto01022.pdf. European shelf during extreme events. Journal of Marine Sci-
Panofsky,H.,Tennekes,H.,Lenschow,D.andWyngaard,J.(1977) enceandEngineering,9,403.
Thecharacteristicsofturbulentvelocitycomponentsinthesur- Vaughan,G.,Methven, J., Anderson,D., Antonescu, B.,Baker,L.,
facelayerunderconvectiveconditions.Boundary-LayerMeteo- Baker, T.P., Ballard, S.P., Bower, K.N., Brown, P.R.A.,
rology,11,355–361. Chagnon, J., Choularton, T.W., Chylik, J., Connolly, P.J.,
Parton, G.A., Dore, A. and Vaughan, G. (2010) A climatology of Cook, P.A., Cotton, R.J., Crosier, J., Dearden, C., Dorsey, J.R.,
mid-troposphericmesoscalestrongwindeventsasobservedby Frame, T.H.A., Gallagher, M.W., Goodliff, M., Gray, S.L.,
the MST radar, Aberystwyth. Meteorological Applications, 17, Harvey, B.J., Knippertz, P., Lean, H.W., Li, D., Lloyd, G.,
340–354. Martínez–Alvarado, O., Nicol, J., Norris, J., Öström, E.,
Pinto, J., Go(cid:2)mara, I., Masato, G., Dacre, H.F., Woollings, T. and Owen,J.,Parker,D.J.,Plant,R.S.,Renfrew,I.A.,Roberts,N.M.,
Caballero,R.(2014)Large-scaledynamicsassociatedwithclus- Rosenberg, P., Rudd, A.C., Schultz, D.M., Taylor, J.P.,
teringofextratropicalcyclonesaffectingWesternEurope.Jour- Trzeciak, T., Tubbs, R., Vance, A.K., van Leeuwen, P.J.,
nalofGeophysicalResearch:Atmospheres,119,704–713. Wellpott,A.andWoolley,A.(2015)Cloudbandingandwinds
PoncedeLeo(cid:2)n,S.andBettencourt,J.(2021)Compositeanalysisof in intense European cyclones: results from the DIAMET pro-
NorthAtlanticextra-tropicalcyclonewavesfromsatellitealtim- ject. Bulletin of the American Meteorological Society, 96,
etryobservations.AdvancesinSpaceResearch,68,762–772. 249–265.
Ponce de Leo(cid:2)n, S. and Guedes Soares, C. (2014) Extreme wave Volonté, A., Turner, A.G., Schiemann, R., Vidale, P.L. and
parametersunderNorthAtlanticextratropicalcyclones.Ocean Klingaman,N.P.(2022)Characterisingtheinteractionoftropi-
Modelling,81,78–88. calandextratropicalairmassescontrollingEastAsiansummer
Rudeva,I.andSimmonds,I.(2015)Variabilityandtrendsofglobal monsoonprogressionusinganovelfrontaldetectionapproach.
atmosphericfrontalactivityandlinkswithlarge-scalemodesof WeatherandClimateDynamics,3,575–599.
variability.JournalofClimate,28,3311–3330. WMO. (1970) Commission for maritime meteorology. The Beaufort
Rulent, J., Calafat, F.M., Banks, C.J., Bricheno, L.M., scaleofwindforce(technicalandoperationalaspects).
Gommenginger, C., Green, J.A.M., Haigh, I.D., Lewis, H. and
Martin, A.C.H. (2020) Comparing water level estimation in
SUPPORTING INFORMATION
coastal and shelf seas from satellite altimetry and numerical
models.FrontiersinMarineScience,7,1–14. Additional supporting information can be found online
Sinclair, V., Belcher, S. and Gray, S. (2010) Synoptic controls on in the Supporting Information section at the end of this
boundary-layer characteristics. Boundary-Layer Meteorology, article.
134,387–409.
Smart,D.J.andBrowning,K.A.(2014)Attributionofstrongwinds
to a cold conveyor belt and sting jet. Quarterly Journal of the Howtocitethisarticle:Gentile,E.S.,&Gray,
RoyalMeteorologicalSociety,140,595–610.
S.L.(2023).Attributionofobservedextreme
Sun, K., Li, L., Jagini, S. and Li, D. (2021) A satellite-data-driven
marinewindspeedsandassociatedhazardsto
framework to rapidly quantify air-basin-scale no emissions
x midlatitudecycloneconveyorbeltjetsnearthe
and its application to the po valley during the covid-19 pan-
BritishIsles.InternationalJournalofClimatology,
demic.AtmosphericChemistryandPhysics,21,13311–13332.
43(6),2735–2753.https://doi.org/10.1002/joc.7999
Valiente, N.G., Saulter, A., Edwards, J.M., Lewis, H.W., Castillo
Sanchez, J.M., Bruciaferri, D., Bunney, C. and Siddorn, J.
10970088,
2023,
6,
Downloaded
from
https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.7999
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