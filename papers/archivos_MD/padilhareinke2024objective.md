atmosphere
Article
Objective Algorithm for Detection and Tracking of Extratropical
Cyclones in the Southern Hemisphere
CarinaK.PadilhaReinke1,* ,JefersonP.Machado1 ,MauricioM.Mata1 ,JoséLuizL.deAzevedo1 ,
JaciMariaBilhalvaSaraiva1andReginaRodrigues2
1 OceanologyPost-GraduateProgram,InstituteofOceanography,FederalUniversityofRioGrande,Av.Itália
Km8,Carreiros,RioGrande96203-900,RS,Brazil;jeferson.machado@furg.br(J.P.M.);
mauricio.mata@furg.br(M.M.M.);joseazevedo@furg.br(J.L.L.d.A.);jaci.saraiva@furg.br(J.M.B.S.)
2 DepartmentofOceanography,FederalUniversityofSantaCatarina,Florianópolis88040-900,SC,Brazil;
regina.rodrigues@ufsc.br
* Correspondence:carina.padilha@furg.brorcarina.padilha@gmail.com
Abstract:Inthisstudy,weproposeaneasyandrobustalgorithmtoidentifyandtrackextratropical
cycloneeventsusing850hParelativevorticitydata,gaussianfilterandconnected-componentlabeling
technique,whichrecognizethecycloneasareasunderathreshold.Beforeselectingtheevents,the
algorithm can include essential characteristics that are good metrics of intensity, like minimum
meansealevelpressureandmaximum10-mwinds.WeimplementedthealgorithmintheSouthern
Hemisphere,usinga41-yearhighresolutiondataset.Sensitivitytestswereperformedtodetermine
thebestparametersfordetectionandtracking,suchasdegreeofsmoothing,thresholdsofrelative
vorticityat850hPaandtheminimumareawithinthethreshold.Twocasestudieswereusedtoassess
thepositiveandnegativepointsofthemethodology.Theresultsshowedthatitisefficientinobtaining
thepositionofextratropicalcyclonesintheirmostintensestage,butitdoesnotalwaysperformwell
duringcyclolysis.Wecomparethemethodologyusing1-htemporalresolutiontothatusinga6-hours
temporalresolution,andtheirreproducibilityregardingtheliterature. Theextratropicalcyclone
climatologyintheSouthernHemisphereisprovidedanddiscussed.Thealgorithmdevelopedhere
canbeappliedtodatasetswithgoodspacialandtemporalresolution,providingabetterinventoryof
Citation:PadilhaReinke,C.K.;
extratropicalcyclones.
Machado,J.P.;Mata,M.M.;
deAzevedo,J.L.L.;Saraiva,J.M.B.;
Keywords: extratropical cyclones; cyclone detection and tracking algorithm; sensitivity studies;
Rodrigues,R.ObjectiveAlgorithmfor
cyclonefrequency
DetectionandTrackingof
ExtratropicalCyclonesinthe
SouthernHemisphere.Atmosphere
2024,15,230. https://doi.org/
10.3390/atmos15020230 1. Introduction
Extratropicalcyclonesareresponsiblefortransportingalargeamountofheat,moisture,
AcademicEditor:GarethMarshall
andmomentum, playingafundamentalroleinatmosphericcirculation[1,2]. Typically,
Received:19January2024 extratropical cyclones cause damages and natural hazards because they are associated
Revised:1February2024 withstrongwinds,intenseprecipitationandextremewaves. Understandinghowthese
Accepted:9February2024 meteorological systems change over the years and their climatological features over a
Published:14February2024
regioncanhelpinpredictinglocalweather,mainlywithrespecttoprecipitation,wind,and
waveintensity[3–5].
Thefirsteffortstoidentifyextratropicalcyclonesfromdigitaldatawerereportedmore
thanthreedecadesago(e.g.,[6,7]). Theincreaseintheamountofinformationobtained
Copyright: © 2024 by the authors.
by reanalysis data over a long period of time provides the challenge of organizing an
Licensee MDPI, Basel, Switzerland.
automaticmethodforidentifyingandtrackingextratropicalcyclonesonagriddedmap,
Thisarticleisanopenaccessarticle
connectingthepathofevents[3]. Methodsusedifferentinputparameterslikemeansea
distributed under the terms and
levelpressure(e.g.,[8–10]),minimumlow-pressurelevelgeopotentialheight[11],orlow-
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// pressurelevelrelativevorticity(e.g.,[4,12–14]). Ulbrichetal.[3]pointedoutthatschemes
creativecommons.org/licenses/by/ thatdetectextratropicalcyclonesusingmeansealevelpressuremayproduceunreliable
4.0/). resultsoverhighgroundduetotheeffectsofverticalextrapolationandtherealorography
Atmosphere2024,15,230.https://doi.org/10.3390/atmos15020230 https://www.mdpi.com/journal/atmosphere

Atmosphere2024,15,230 2of19
inreanalysisdatasets. Moreover,Hodgesetal.[15]explainedthatvorticitydataismore
focusedonthewindfield,givingmoreinformationonthehigh-frequencysynopticscale,
whilesealevelpressuredataislinkedtothemassfieldandrepresentsthelow-frequency
scalebetter.
In addition to choosing the best meteorological variable that identifies the posi-
tion of the cyclones, other restrictions must be considered. One of the challenges is to
track the events when several grid points can be considered the next location of a cy-
clone. There are methods that apply an across-time “nearest neighborhood” approach
to connect the identified cyclone centers of two consecutive time step with the nearest
neighbors[16,17],otherstudiesapplyalgorithmsbasedondisplacementspeed[7,10]and,
innovating,Inatsu[12]usesconnected-componentlabeltechnique(CCL)toconnectcyclone
asareasthatoverlapinconsecutivetimesteps. Anothersteptoimprovetheselectionof
centersofcyclonesisapplyingspacialfilters,usuallyameanfilter. Flauonas[18]tested
threedegreesofspacialfiltering,inordertocapturethephysicalcharacteristicsofcyclones.
Also, in order to remove spurious or very short lived systems in cyclone identification
schemes,theminimumlifetimeofeventscanbeselected,withvaluesof12h[10],18h[9]
or24h[17–21].Table1showsalistofrelevantextratropicalcyclonesdetectingandtracking
methods, allbasedonobjectivecriteria. Someofthesemethodsweredesignedupona
morecoarsespacialandtemporalresolutiondataset,comparedtothoseavailabletoday.
Furthermore,thedifferencebetweenthemethodsreflectthemultipleunderstandingsof
whatbestcharacterizesacyclone.
Table1.Relevantextratropicalciclonedetectingandtrackingmethods.
References VariableUsedtoIdentify MainCharacteristics
localminimumofthegeopotentialheightof
BlenderandScubert,2000[16];Trigo,2006[17]. nearest-neighborsearchmethod
the1000-hPasurface
CrawfordandSerreze,2016[22];Crawford
etal.,2021[23];HanleyandCaballero, Minimummeansealevelpressure nearest-neighborsearchmethod
2012[10];Lionelloetal.,2002[8]
MurrayandSimmonds,1991[7];Simmonds
andKeay,2000[24],LimandSimmonds, estimatethesubsequentdisplacementand
Minimummeansealevelpressure
2007[19];Pintoetal.,2005[21];Rudevaand pressurechange
Gulev,2007[9].
Reboitaetal.,2010[25];Reboitaetal.,2017[14] relativevorticityofthe925hPasurface nearest-neighborsearchmethod
areaunderathreshold
Inatsu,2009[12] relativevorticityofthe850hPasurface
relativevorticityofthe850hPasurface mostnaturalevolutionofrelative
Flauonas,2014[18]
vorticityfield
HewsonandTitley,2010[26] meansealevelpressureandrelativevorticity graphicalprocessing
Cyclone detection and tracking are highly complex [27], and differences in results
canoccurdependingonthemethodologyorthedataset. Thefirsteffortstointercompare
trackinganddetectionmethodsofextratropicalcyclonesandreanalysisdatasetswerefrom
Trigo et al. [17], who compared results from ERA-40 and NCEP/NCAR reanalysis and
Raible et al. [28], who compare three different cyclone detection and tracking schemes
with different reanalysis datasets. They identify differences in terms of the number of
cyclonesandcycloneintensity. However,theirinterannualvariabilityandnumberofmore
intenseeventsagreed.AprojectnamedIntercomparisonofMid-LatitudeStormDiagnostics
(IMLAST)wascreatedtoidentifyuncertaintiesrelatedtothechoiceofmethod[27]. Using
thesameinputdataset, aminimumlifecycleof24hand6-hintervals, theyconcluded
thattheconsistencyacrossthemethodsisgenerallyhigherfordeepcyclones. Theperiods
ofdevelopmentandcyclolysisdivergeoverthemethods;however,themostintensepart
ofthelifecycleissimilar. Thenumberofcyclonecentersdiffers,butoveralltheyagree
intermsofinterannualvariabilityandgeographicaldistribution,withsomeexceptions,
such as in the Mediterranean. Comparing the hemispheres, the distribution of cyclone
density is more zonally symmetric in the Southern Hemisphere than in the Northern
Hemisphere,becauseofthelargerlandmassandthetopographicfeaturesinthelatter[24].
Recently,Realeetal.[29]comparedtheidentificationofcyclonesofexplosiveactivitybya

Atmosphere2024,15,230 3of19
groupofmethodsandfoundthattheareaofgreatestactivityoftheseexplosivecyclones
agreedwithpreviousstudies,despitethehugespreadinthenumberofexplosivecyclone
identified. Gramcianinovetal.[30]comparedtheresultsofAtlanticextratropicalcyclones
characteristicsusingtwodifferentdatasetsandshowedsmalldifferencesincyclonenumber
andcharacteristicsanddivergencesintheintensitydistributions.
Theobjectiveofthisstudyisthustoimplementaneasywaytoidentify, trackand
characterizeextratropicalcyclones,usingagaussianfilter,whichprovidesamoredelicate
filtering of the contours. Moreover, the technique identifies events with CCL, which is
recognizedasagoodmethodintheliterature. Animportantcontributionofthisworkis
togenerateacycloneidentificationandtrackdatabasetounderstandthemodificationsof
cyclonefrequencyandintensityoverthelastdecades. Thispaperprovidesandescription
ofthemethodologyaswellastestsofsensitivityandperformanceofindividualevents
to evaluate the algorithm. Also, we compare the results using 1-h resolution and 6-h
resolution,extractedfromthesamedatasetandforthesameperiod. Tounderstandthe
differenceswithothermethodologies,wepresenttheSouthernHemisphereclimatology
of extratropical cyclones using 40-yr high-resolution ERA5 reanalysis dataset from the
EuropeanCentreforMedium-RangeWeatherForecasts(ECMWF).
2. MaterialsandMethods
2.1. Data
Inthisstudy,weusemeteorologicaldatafromERA5/ECMWFreanalysis,thefifthgen-
erationECMWFreanalysisfortheglobalclimateandweather. AccordingtoHersbach[31],
amajorstrengthofthisnewreanalysisisthemuchhighertemporalandspatialresolutions
thanthoseofpreviousreanalysis. Thehorizontalresolutionis31km,andithas137vertical
levels,spanningthesurfaceoftheEarthto0.01hPa,inhourlyoutput,inaregularGaussian
grid(F128). Inadditiontothat,ithasimprovedtheassimilationofthereprocesseddataset,
withrespecttopreviousproducts.
WeusetherelativevorticitydataavailablefromERA5/ECMWFreanalysistofind
maximumvaluesofcyclonicvorticity,invorticityfieldsat850hPalevel. Theparameter
is a measure of the rotation of air in the horizontal, around a vertical axis, relative to a
fixedpointonthesurfaceoftheEarth. Intheclassicaltheory(e.g.,[32]),themicroscopic
measureofrotationinafluidisavectorfield,definedasthecurlofthevelocityofthefluid,
resultingitsrelativevorticity(ζ). Fromascaleanalysis,onlytheverticalcomponent(ζ )is
z
used,leadingtotheEquation(1).
∂v ∂u
ζ = − (1)
z
∂x ∂y
ThecorrespondingexpressioninsphericalcoordinatescanbewrittenasEquation(2)
form,whereuandvarethelocalzonalandmeridionalvelocities(m/s)respectively,ris
theearth’sradius,θisthelatitudeandλisthelongitude.
(cid:18) (cid:19)
1 ∂v ∂ucosθ
ζ = − (2)
z
rcosθ ∂λ ∂θ
ThisstudyappliestheprogramofidentificationandtrackingofcyclonesintheSouth-
ernHemisphere,thereforeclockwiserotation(negativerelativevorticity)isassociatedwith
cyclones.Meansealevelpressuredataand10-mwindsdataatgridpoints(ERA5/ECMWF)
areusedtocharacterizethemostintenseevents.
2.2. Methods
Basically,threeindependentstepscomposethealgorithm: detectionoftheposition
ofthepotentialcyclones, linkageoftheeventsandadditionofmeansealevelpressure
and10-mwinddata,toidentifytheintensityoftheevents. Thesethreestepsaredetailed
distinctlyinthefollowing.

Atmosphere2024,15,230 4of19
2.2.1. IdentifyingCyclones
The relative vorticity field is usually very noisy, mainly in low levels of the tropo-
sphere. Onewaytoimprovethenoisycharacteristicofthefieldisapplyingapreprocessing
stagebyaspatialfilter. OtherstudiesusedtheB-splinetechnique[33], timeband-pass
filtering[12,34],1-2-1filter[35]or1-1-1filter[18]. Inthepresentstudy,weuseamultidi-
mensionalGaussianfilter(G(x,y))implementedbyscipy.ndimagepythonpackage. This
filter allows a more delicate smoothing of the orographic and coastal effects and also
smoothsthemaximumlocalvorticitythatisnestedwiththenoisyfields,comparedtothe
mediumfilter[36]. Thedegreeofsmoothingisdeterminedbythestandarddeviationof
theGaussian(σ). TheGaussianfilteriscalculatedbytheEquation(3):
1 −x2+y2
G(x,y) = e 2σ2 (3)
2πσ2
wherexandyarethezonalandmeridionaldistancesfromthepointforwhichthesmoothed
iscalculated. Asthisparameterincreases,thesmoothingoperationontherelativevorticity
fieldbecomesstronger.
Afterthispreprocessingstage,theconnected-componentlabelingtechnique(CCL)is
used. CCLisexplainedbySamet[37]andusedforextratropicalcyclonesbyInatsu[12]
andInatsuandAmada[38]. Intherelativevorticityfield,thegroupofdatathatsatisfies
a pre-set threshold is selected for a single time frame. This group represents an area
big enough to attempt the recognized characteristics of extratropical cyclones. At this
point,abinarymatrixoftherelativevorticityfieldisconstructed,withareasthatsatisfy
thethreshold. Theseenclosedindependentsurfacesareconsideredpossiblepositionsof
extratropicalcyclonesatthattimeframe.Thecenterofmass(CM )ofeachareaiscalculated
a
(Equation(4))inasimplifiedform[39]toidentifythelocationoftheenclosedindependent
surfaces(a),
∑i=1
m R
CM = i=N i i (4)
a ∑m
i
where (m,R) is the mass and position, respectively, of singles grid points and N is the
numberofgridpointsoftheenclosedindependentsurfaces(a). Thecenterofmassfromthe
relativevorticityfieldindicatesthatthelatitude/longitudepositionoftheareaisinfluenced
bythepositionwithintheareacapturedbyCCLtechniquewheretherelativevorticityis
greatest. Tofurtherexplain,ifweimagineacircularareainwhichthesouthwestsectorhas
thehighestvorticity,theidentificationpositionofthisareawillnotbeatthecentralpoint
ofthecirculararea,butwillbeshiftedsouthwest.
Thecenterofmasswillbelabeledandtreatedasauniquepossiblecyclonepositionat
thattimeframe. ThehigherresolutionofERA5dataexposesthenoisycharacteristicofthe
relativevorticityfield,labelingsomeenclosedindependentsurfacesthatclearlyarenot
cyclones. Toreducethisresolutionproblem,wesimplydiscardedareasoflessthanagiven
limitofgridpoints.
Therefore, the algorithm’s performance up to this step is influenced by the choice
of the standard deviation of the Gaussian filter (during the preprocessing stage), the
thresholdofrelativevorticityat850hPaandtheminimumareaattendingthethresholdthat
characterizesanextratropicalcyclone. Inthisstudy,weshowthefollowingtests: gaussian
standard deviation of 0.5, 1.0, 1.5 and 3.0; threshold of relative vorticity of −10−5s−1,
−5×10−5s−1,−10−4 s−1 and−2×10−4 s−1 andminimumareaof9,12,15and18grid
points.ThetestsofGaussianstandarddeviationanddifferentthresholdsofrelativevorticity
at850hPaareappliedtotherelativevorticityfieldof1July2020,12UTC,whenstrong
windsassociatedwithanextratropicalcycloneat35◦ Sand46◦ Wcauseddamageonthe
coastofSouthernBrazil. AweakereventwasattheAtlanticOcean,at50◦ Sand48◦ W.For
theminimumareatest,thealgorithmisappliedto10years,from2013to2022,andsome
differencesofthechoicesarediscussed.
Fromthesetests,wechosethestandarddeviationoftheGaussianfilterof0.5,threshold
ofrelativevorticityof−10−4s−1andmaskedareaslessthan15gridpoints,attherelative

Atmosphere2024,15,230 5of19
vorticityofERA5/ECMWF.ThisstepwasappliedtotheSouthHemisphere,forthewhole
studyperiodgeneratingafileofpossiblepositionsofeachextratropicalcyclone.
2.2.2. TrackingCycloneEvents
Followingthisstep,alinkbetweenthetimeframesischained. Thefirstindependent
enclosed area is searched at the following time frame around a defined displacement
maximum, that can be adjusted. For this study, we adjust the maximum displacement
in150km/h,similartothealgorithmofCrawfordetal. (2021)[22]. Lifetimecondition
is another typical criterion of extratropical cyclone tracking algorithms. Like in many
studies(e.g.,[38]), weconsideraminimumlifetimeof12h. Itisobviousthatashorter
lifetimeconditionwouldincreasethenumberofcyclonesconsiderablyandalongerone
woulddecreaseit. However,weusea12-hminimumlifetimetobecomparabletoother
methodologiesintheliterature.
Cyclogenesisreferstothefirst-timeframeoftheemergedeventidentification. Ifthere
isnoidentificationthatcorrespondstothedisplacementandlifetimecriteriaatthenext
timeframe,thelabelidentificationisdiscarded. Ifitattendsthetwocriteria,thealgorithm
movestothenexttimeframeuntilnoidentificationcorrespondstothecriteria. Then,the
eventisselected,andthelasttimeframeindicatestheevent’sendorcyclolysis. Figure1
showsanexampleofsequenceofhourlypointscenterofmassofdetectedareasthatmatch
therelativevorticitythreshold. ThepointsofthesouthweastAtlanticcanbeselectedand
connectedasanevent,becauseitcontinuesunderthemaximumdisplacementforatleast
12h.
Figure 1. Example of points center of mass of areas that match the relative vorticity threshold-
sequenceofhourlydata.
These stages generate a list of events with the latitude/longitude of cyclogenesis,
positionduringthefollowingtimeframeandthelatitude/longitudeofcyclolysis,with
themoreintenserelativevorticityandtheareaingridpoints,capturedbytheCCL.This
database may be used to understand the frequency of cyclones over a region, areas of
cyclogenesisandcyclolisis,thegrowthrate,aswellasselectthemoreintenseeventsof
anarea.
2.2.3. QuantifyingCycloneCharacteristics
Theminimummeansealevelpressureandmaximum10-mwindassociatedwithall
timeframesoftheeventsareinvestigatedtocharacterizeeacheventintermsofintensity.
Todothis,an“effectivearea”foreachtimethecycloneisscanned,centeredatthecyclone
vorticitycenterofmassoftheareaselectedbytheconnected-componentlabelingtechnique.
Itwasstipulatedthat12gridpoints,correspondingtoapproximately3.6latitude/longitude
degreesattemperateregions,isagoodeffectiveareatocharacterizethemaximumintensity
of the events. Figure 2 shows, as an example, the effective area of an intense event of
27October2016,6UTC.Theminimumsealevelpressuredetectedwas986.5hPa,andthe
maximum10-mwindwas71.3km/h.Thus,withthisidentifyingandtrackingextratropical
cyclonemethod,theeventscanbeselectedbytheircharacteristics,inasubsequentstudy.

Atmosphere2024,15,230 6of19
Figure2.Meansealevelpressureandrelativevorticityat850hPaunder−10−4s−1,on27October
2016,06UTC.Thegreensquareisthe“effectivearea”tosearchforthemoreintensecharacteristicsof
thecyclone.Theyellowpointisthecenterofmassidentifiedbythealgorithmandthebluelineand
pointsarethefollowingtimeframesoftheevent.
Part of the area of relative vorticityabove the threshold can be out of theeffective
area. Inaddition,thecenterofmassoftheareacanhavearelativevorticitylowerthanthe
thresholdbecauseoftheshapeofthearea. Otherstudieshavedevelopeddifferentwaysto
characterizecycloneeventsintermsofminimumsealevelpressureandmaximum10-m
winds, consideringacirculardiskaroundthemaximumvorticity[18]ortheminimum
pressurecenter[19].However,afixedareaisthesimplestchoiceandaneffectivealternative
forouralgorithm.
Figure3showstheflowchartoftheprogramofidentificationofextratropicalcyclones
proposedinthisstudy.Inthenextsection,wepresentthetestsofdifferentlevelsoffiltering,
differentvaluesofthresholdandasensitivitytestofminimumareacriteria.
Figure3.Flowchartofthedetectionalgorithmofextratropicalcyclonesproposedinthisstudy.

Atmosphere2024,15,230 7of19
3. Results
3.1. SensitivitytotheSmoothingParameterfortheRelativeVorticityField
Figure4Ashowsthemeansealevel(contours)andrelativevorticityfield(shading)
obtaineddirectlyfromERA5for1July2020,12UTC,whenanintenseextratropicalcyclone
was near the coast of Uruguay and southern Brazil (35◦ S/46◦ W) and another weak
cyclonewaspositionedat50◦ Sand48◦ W.UsingstandarddeviationofGaussianfilterof
0.5tothesametimeframe(Figure4B),intensecharacteristicofcoastalcycloneandweak
characteristicofthesoutheastcyclonearepreserved. However,testsofsigmaequalto1
(Figure4C)and3(Figure4D)over-smoothedtherelativevorticityfield,totheextentof
nullifyingtheweakeventorreducingitsarea. Atestofsigmaequalto5underestimates
thenumberofcyclonesfor2020(notshown)givingunrealisticresults.
Figure4.Meansealevelpressureandrelativevorticityat850hPaunder−10−4s−1,on1July2020,
12UTC.(A)rawdataandwithdifferentstandarddeviationsoftheGaussianfilter:(B)0.5,(C)1.0
and(D)3.0.
Accordingtoanalysisoftherelativevorticityfieldofthisknownevent,itcanbeseen
thatweakeventsaredetectedjustinlowlevelofsmoothing,thenamoredetailedstudy
oftheextratropicalcyclonefeaturesisshownjustto0.5,1.0and1.5degreeofsmoothing,
appliedto10yearsinFigure5. Asexpected,thenumberofeventsdependsonthefiltering
strength,withmoreeventsusinglowerdegreeofsmoothing. Figure5Ashowsthatthere
aremoreeventsoflessthantwodaysandFigure5Bshowsthatthemeanspeedofthe
eventsarebetween40km/hand60km/husingthethreelevelsofsmoothing. Theseare
expectedfeaturesofcyclonesinSouthernHemisphere. Themeancountofextratropical
cyclonesis2430,2258and1693using0.5,1.0and1.5respectively. Thus,thesupressionof
eventswasonaverage25%,comparingsmoothinglevelfrom1.0to1.5,and7%comparing
0.5to1.0. Forthefollowingsteps,weusedasmoothingparameterof0.5.

Atmosphere2024,15,230 8of19
Figure5.Studyofthefeaturesofcyclonesforthethreesensitivitytestsoffilterdegree,computed
from2013to2022:(A)Frequencydistributionofcyclonelifetime,(B)frequencydistributionofcyclone
meanspeedand(C)timeseriesoftotalannualnumberofextratropicalcyclones.
3.2. SensitivitytoThresholdofRelativeVorticity
Thechoiceofthethresholdofrelativevorticitywillcalibratethenumberofpossible
cyclonecentersandremovesignalsthatarenotrelatedtothesesystems. Figure6shows
therelativevorticityfieldfromERA5/ECMWFon1July2020,12UTC,withthestandard
deviationofGaussianfilterof0.5,forfourdifferentthresholdsofrelativevorticity.Figure6A
showsanoisyfieldwithathresholdof−10−5s−1.Athresholdof−0.5×10−4s−1generates
a spurious signal mainly at the Andes (Figure 6B). On the other hand, the threshold of
2×10−4s−1(Figure6D)cannotidentifythecyclonecentersintheregion. Then,fromthe
visualanalysisoftherelativevorticityfield,weconcludethatagoodthresholdtoidentify
theeventsandsuppressthespurioussignalsinourtestsis10−4s−1(Figure6C).
3.3. SensitivitytotheMinimumAreaofRelativeVorticityundertheThreshold
Figure7presentsthemeanmonthlycyclonecentersdetectedbetween2013and2022
using0.5offilterparameter,thresholdofrelativevorticityof10−4s−1andwithdifferent
thresholdsofminimumareaofrelativevorticitylabels. Asexpected,thenumberofcyclone
centersperdaydependsonthechoiceoftheminimumareasize. Thiscriterionshould
beneithersostrictastoremoverealsmallcyclones,norsolenientastoincludespurious
cyclones. Furthermore, there is an expectation that more events will take place in the
winterthaninthesummerbecausethelarge-scaletemperaturegradientsarehigherinthe
winter[3]. Usingaminimumareaoflessthan9points(notshown)yieldsanunrealistic
numberofcyclones(morethan1000permonth). Itcanbeanindicationthatpersistent
signalsarecountedasdifferentcycloneevents,likethosegeneratedbyorography.However,
Figure7showsminimumareatestsof9,12,15and18pointsandtheexpectedincreasein
thenumberofcyclonesinwinterisobtained. Moreover,correlationofmonthlynumber
of cyclones between the 9 and 12 tests are 0.983, between 12 and 15 tests are 0.987 and
between15and18are0.985,suggestingthattheresultsconvergearoundtestofminimum
areaequalto15.

Atmosphere2024,15,230 9of19
Figure6.Meansealevelpressure(contours)andrelativevorticityat850hPa(shading)withthresholds
of:(A)−10−5s−1;(B)−0.5×10−4s−1;(C)−10−4s−1and(D)−2×10−4s−1,on1July2020,12UTC,
usingaGaussianfilterparameterof0.5.
Figure7.MeanCyclonecenterspermonthdetectedbetween2013and2022,usingaGaussianfilter
parameterof0.5,athresholdofrelativevorticityof−10−4s−1anddifferentsetsofminimumarea
(numberofpixels).
Figure8showsthefrequencydistributionofcyclonelifetime(A),frequencydistribu-
tionofcyclonemeanspeed(B)andthetimeseriesoftotalannualnumberofextratropical
cyclonesbetween2013and2022(C).Althoughthenumberofcyclonesdetectedusingthe
differenttestsareclearlydependentonthechoiceoftheminimumareacriterion,cyclone
lifetimeandmeanspeeddistributionaresimilarusingthefourtests. Table2showsthe
meanlifetimeandstandarddeviationinhoursandthemeanspeedmeanandstandard
deviationforthefourtestsandtheyhavenosignificantchangesontheresults. Thismeans
thatthesecharacteristicsofcyclonesarenotsensitivetotheareacriteriawithinthisrangeof
values. Fortherestofthestudy,weselectedthe15minimumareacriteriaasagoodchoice.

Atmosphere2024,15,230
10of19
Figure8.Studyofthefeaturesofcyclonesforthefoursensitivitytestsofareacriterion,computed
between2013and2022:(A)Frequencydistributionofcyclonelifecicle,(B)frequencydistributionof
cyclonemeanspeedand(C)timeseriesoftotalannualnumberofextratropicalcyclones.
Table 2.
Statistics information of lifetime and mean speed of detected cyclones using different
minimumareatests.
|                 | LifetimeStandard                                            |           | MeanSpeedStandard |           |
| --------------- | ----------------------------------------------------------- | --------- | ----------------- | --------- |
| MinimumAreaTest | LifetimeMean                                                |           | MeanSpeedMean     |           |
|                 |                                                             | Deviation |                   | Deviation |
| 9               | 24.9                                                        | 12.6      | 56.4              | 16.5      |
| 12              | 24.8                                                        | 12.2      | 56.3              | 16.4      |
| 15              | 24.6                                                        | 12.0      | 56.3              | 16.2      |
| 18              | 24.4                                                        | 11.7      | 56.3              | 16.1      |
|                 | 3.4. FirstCaseStudy: ExtratropicalCycloneof26–28October2016 |           |                   |           |
AnintenseextratropicaleventinsouthernBrazilwasdocumentedbyAlbuquerqueetal.[40]
andOliveiraetal.[41],withimpactsatHermenegildobeach(33.7◦ S,53.4◦ W,Figure9A).
Itwasaneventofhighwaveenergy,withsignificantshiftsincoastalmorphology. The
automaticstationofSantaVitoriadoPalmar(identifiedbyA899),at33.74◦ S/53.37◦
W
(Figure9A),recordedamaximumwindgustof111.2Km/hat17UTCof27October2016
andaminimummeansealevelpressureof997.4hPaat15UTCand16UTCof27October
2016. Thecyclonestartedtodevelopon26October,withlowermeansealevelpressure
over Uruguay and southern Brazil. Figure 9B shows the storm track identified by the
algorithm(blueline)andidentifiedbyavisualinspectionofthepressurefield(greenline).
Theevolutionofthecyclonetrackfromthealgorithmagreesrelativelywellwiththatfrom
thevisualdetection. Figure9C,Dshowthesimilarityofthevisualfieldinspectionandthe
algorithmresults(greenpoint)andthelocationoftheextratropicalcycloneattheinitial
frame (20 UTC 27 October) and during the more intense stage (16 UTC on 27 October)
respectively. Figure9E,Fshowtheevolutionofcycloneintensitybythemaximum10-m
winds,minimummeansealevelpressure,maximumrelativevorticitydetectionandthe

Atmosphere2024,15,230 11of19
sizeofvorticityabovethethresholdateachtimeframe.Alltheparametersshowtheintense
periodbetween12UTCon27Octoberand03UTCon28October. Thelasttimeframehas
strongwinds,lowmeansealevelpressureandintenserelativevorticity,whichmaybe
associatedwithalossofthecyclolysisprocess. Theseresultssuggestthatouralgorithm
hadthebestaccuracyattheinitialstageandduringtheintenseperiodofthecyclonefor
thecasestudy.
Figure9.Extratropicalcycloneduring26to28October2016.(A)LocationofHermenegildoBeach
andautomaticstationofChui(A899).(B)Cyclonetrackfrom26October2016,20UTCto28October
2016,6UTCobtainedfromtheprogram(blueline)andvisualinspection(greenline). (C)Mean
sealevelpressureandrelativevorticityat850hPa,on26October2016,20UTC,thegreenpoint
isthepositionobtainedfromthealgorithm. (D)Sameas(C)exceptfor: 27October2016,16UTC.
(E)Minimummeansealevelpressure(greenline)andmaximum10-mwind(redline)detectedby
thealgorithmduringtheevent.(F)Minimumrelativevorticity(greenline)andtotalareaunderthe
threshold(bluehistograms)detectedbythealgorithmduringtheevent.

Atmosphere2024,15,230 12of19
3.5. SecondCaseStudy: ExtratropicalCycloneof15–17August2020
Thesecondcasestudyhastheimportantfeatureofmergingwithanotherlow-pressure
center. Whentwoormoreneighbouringcyclonesmergeorsplit,therecognitionofthecy-
clonetrajectorybecomesmoredifficult[42]. Thereisanimprovementinrecognizingmerg-
ingorsplittingextratropicalcyclonesbyusingtechniquessuchasconnected-component
label (e.g., [10,12,26,42]). Figure 10A shows the storm track identified by the algorithm
(blueline)andthatidentifiedbyavisualinspection(greenline),usingsealevelpressure
field. Bothtracksconvergeoverallstagesofthecyclonelifecycle. Theextratropicalcy-
clonedevelopedoverthesouthwestAtlanticat20UTCon15August2020(Figure10B).
Figure10Cshowstheeventinthemoreintensestage,withamaximumrelativevorticityof
−8.6−10−4s−1. Alongthesoutheastwarddisplacement,itstartedtomergeat00UTCon
17August2020. Figure10Dshowstheeventonthemergedstage.
Figure10. ExtratropicalCycloneof15to17August2020. (A)Cyclonetrackfrom15August2020,
20UTCto17August2020,06UTC,obtainedfromthealgorithm(blueline)andfromvisualinspection
(greenline).(B)Meansealevelpressureandrelativevorticityat850hPa,15August2020,20UTC,
thegreenpointisthepositionobtainedfromthealgorithm.(C)Sameas(B)exceptfor:16August
2020,06UTC.(D)Sameas(B)exceptfor: 17August2020,02UTC.(E)Minimummeansealevel
pressure(greenline)andmaximum10-mwind(redline)detectedbythealgorithmduringtheevent.
(F)Minimumrelativevorticity(greenline)andtotalareaunderthethreshold(bluebars)detectedby
thealgorithmduringtheevent.

Atmosphere2024,15,230 13of19
Figure10E,Fpresenttheevolutionofminimumsealevelpressure,maximum10-m
winds,maximumrelativevorticityat850hPaandtotalareaabovethethresholdoverthe
cyclonetimeframes. Aminimummeansealevelpressureandamaximumareaabovethe
thresholdoccurredduringthelasthoursof16August. However, themaximumwinds
andmoreintenserelativevorticitywasduringtheearlyhoursoftheevent. Thiscanbe
aconsequenceofthemergingprocessjustbeforetheweakeningthatisobservedduring
cyclolysis. In the subsequent time frame, the algorithm maximum displacement part
promotedtheendoftheevent. Possiblypartofthedecayprocessoftheeventwasnot
includedbytheprogram,duetotheincreaseinareawithinthethreshold,whichdisplaces
the calculated center of mass, making the dissolution phase shorter. These two events
highlighttheabilityofthemethodtotrackthecyclogenesisprocessandthemoreintense
stageoftheeventsandapossiblesuppressionofpartofthecyclolysisstage.
3.6. TemporalResolution
Weexpectthatthefinerthetemporalresolution,thebetterthetrackingprocessbecause
thesearchinthefollowingtimestepisdonewithinashortertimegap,andashorterradius
ofsearchingifthepropagationspeeddoesnotchange[16]. Anotherimplicationofusing
highertimeresolutiondataisthatthecyclonesareweakerontheaverage,becauseweaker
systemswithshortertracksarenotidentifiedincoarsertimeresolutiondata[21]. However,
Crawford et al. [23] examined the sensitivity of cyclone detection and tracking for the
NorthernHemisphereandshowedthatrefiningbeyond3hdoesnotnecessarilyleadto
more accurate detection and tracking, using the algorithm explained by Crawford and
Serreze[22]appliedtofinertemporalresolutiondataset.
Inadditiontothis,mostclimatologyareconstructedbasedon6-hourlyatmospheric
fields. Gramcianinov[30]comparedthe6-hourlyand1-hourlytrackingusingthesame
trackingmethodandthresholds. TheresultsshowedahighergenesisdensityinUruguay
andasmallerdensityinsouthernBrazil,using1-hourlydata. Accordingtotheauthors,
thisdifferencecanbeassociatedwiththeidentificationofthecyclonicsystemsatearlier
stagesofdevelopmentusing1-hourlydata.
Ourstudycomparesthecyclonetrackingperformanceusing6-hourlyand1-hourly
datasets. Figure 11 shows the frequency distribution of cyclone lifetime, cyclone mean
speedandthecountofextratropicalcyclonesperyearfrom1982to2022,with1-hourlyand
6-hourlytemporalresolution. Crawfordetal.[43]detachedthatchangingfrom6-hourlyto
1-hourlyresolutionshortereventsaremoreinclinedtolatedetectionorearlytermination
and explained that this leads to a grow of short-lived events. The same influence was
observedinoursresults,thatismoreeventsoflessthantwodaysusing1-hourlyresolution.
Intermsofmeanspeed,althoughthemeanvaluesaresimilar,thefrequencydistribution
ismoredispersedusing1-hourlyresolution,withastandarddeviationof21.2km/hto
1-hourlyand15.3km/hto6-hourlyresolution. Thetimeseriesoftotalannualnumberof
extratropicalcyclonesforthetworesolutions,appliedto41years(Figure11C)showan
increasingtendency. Thecoefficientofdeterminationisof0.56and0.77for6-hourlyand
1-hourlyresolution,respectively.
ViolinplotofextratropicalcyclonetrackinginSouthernHemispherefortheperiodof
1982–2022(Figure12A)highlightsthat1-hourlytemporalresolutionshasmoreeventsper
yearthan6-hourlyresolution,withanaverageof2314forthe1-hourlydatasetand1750for
the6-hourlydataset.
Consideringtheperiodof1982to2022,thedurationoftheeventsusing1-hourlyand
6-hourlydatasetshasanalogousdifferencetothefrequencydistributionoflifetime,with
anaverageof24hfromtheformerand49hforthelatter(Figure12B).Oneexplanation
tothisdifferencecouldbeaprematureterminationoftracksand/orsplitoftwotracksin
situationsthatwouldbecontinuedifanalysedmanuallybyameteorologist. Theseissues
canbeaddressedinafutureimprovementoftheprogram. HeadingofFigure12C,track
lengthinkmtendstobeshorterusingthefinertemporalresolutiondataset,becausethe
searchofthenextframehasashortertimegap,andthisimpliesmoredetailsalongthe

Atmosphere2024,15,230 14of19
cyclonetrack,withmoreeventsofshortlifetimeandshortdistancetraveledincludedin
thegroupofevents. Thetrackdistanceaveragesfrom1355kmusingthe1-hourlydataset
to2224kmusing6-hourlydataset. Thethirdquartilealsoshowsadifference,with1628km
and2917kmusing1-hourlyand6-hourlydatasetresolution,respectively.
Figure11.StudyofthefeaturesofcyclonesintheSouthernHemisphereusing1-hourly(blue)and
6-hourly(orange)temporalresolutions,fortheperiodof1982–2021:(A)Frequencydistributionof
cyclonelifecicle,(B)frequencydistributionofcyclonemeanspeedand(C)timeseriesoftotalannual
numberofextratropicalcyclones.
The evaluation of cyclone speed (Figure 12D) shows similar average values using
the6-hourlydatasetcomparingtothoseobtainedbyIMILASTintercomparisonproject.
However,theaveragespeed56km/husingthe1-hourlydatasetisslightlyhigherthan
thatfromthe6-hourlydataset(46km/h)andIMILASTintercomparisonproject. Thiscan
beexplainedbytheinclusionoffastercases,withfinertemporalresolutionandthemore
dispersedistributionshowninFigure11B.
Focusingontheintensityoftheevents,Figure12Eshowstherelativevorticityminimum
at850hPa,identifiedusingthetwotemporalresolutions.Theaveragesare−4.4×10−4s−1
and −4.3 × 10−4 s−1 for the 1-hourly and 6-hourly datasets, respectively. As expected,
usingthe1-hourlyresolution,thealgorithmismoreefficientinfindingthemostintense
events,indicatedbytheelongatedrangeofvaluesintheviolinplot. Intermsoftheaverage
of the area with relative vorticity above the threshold (Figure 12F), the two temporal
resolutionsaresimilar,106and95forthe1-hourlyand6-hourlydataset,respectively. When
usingthefinerresolution,thealgorithmcapturesslightlylargerareas.
3.7. ExtratropicalCycloneClimatology
Generally,studiesusingdifferentmethodologiesofdetectingandtrackingofextra-
tropicalcyclonespresentthenumberofcyclonecenters,eitherbymonthorseason,and
perunitareaoverahemisphere. ThisiscalledsystemdensitybySimmondsandKeay[24].
When these results are presented as a percentage of the total time, it is usually called
cyclone frequency or cyclone density [27]. Most of the previous studies use different
6-hourlyreanalysisdatasets. Todeterminetherobustfeaturesamongthedifferentmethod-
ologies,theIMILASTprojectcompiledclimatologiesofcyclonefrequencyoverthesame
period(20-yrperiod),withthesametimeresolution(6hourly),andthesamedataset(ERA-
Interim/ECMWFdataset,with1.5◦ spatialresolution),withthesameminimumlifetimeof
24h[27],forbothhemispheres. Here,wecomparetheresultsobtainedfromouralgorithm
withthosefromtheIMILASTprojectandotherstudies,takingintoconsiderationthatour

Atmosphere2024,15,230 15of19
studyusesadifferentdataset,withhighertemporalandspatialresolution,foralonger
period. So,weintendtopresentthesimilaritiesanddifferenceswiththeseassumptions
inmind.
Figure12.ViolinplotofextratropicalcyclonestrackingintheSouthernHemisphereusing1-hourly
(blue)and6-hourly(orange)temporalresolutions,fortheperiodof1982–2022.(A)Eventsperyear.
(B)Durationinhours.(C)Tracklengthinkm.(D)Averagespeedinkm/h.(E)Minimumrelative
vorticityofeventsins−1.(F)Maximumareawithrelativevorticityunderthethreshold.
Figure 13 shows the mean number of cyclogenesis per month, with a cap area of
106 km2 intheSouthernHemisphereforthefourseasons. Itisevidentthatthegreatest
numberofcyclogenesisoccursalongthe70◦ S–50◦ Slatitudeband,whichagreeswithSim-
mondsandKeay[24]. Consistentwithpreviousstudiesandasexpected,thefrequencyand
spatialextentofcyclogenesisarehigherduringwinter. Ourmethodologyalsoreproduces
theabsenceofcyclogenesiswestoftheAndesandanintensificationofcyclogenesisalong
thesoutheasterncoastofSouthAmerica[44,45]. AstheperturbationcrossestheAndes
atmiddlelatitudes,thelower-levelperturbationadvancesfollowingtheorographyand
propagatesontheleesideoftheAndes,detachedfromtheupper-levelperturbationand
suppressing the instability. Approaching the southeastern coast of South America, the
perturbationencountersamorefavorablebaroclinicstructure,promotingcyclogenesis. The
strongregionofcyclogenesisobservedinthecoastalareaofAntarcticawasalsoobserved

Atmosphere2024,15,230 16of19
byTreutandKalnay[46],MurrayandSimmonds[7],Hodges[33],SimmondsandKeay[24],
HoskingsandHodges[47]andValsangkaretal.[48].
Figure13.TheaveragenumberofcyclogenesispermonthintheSouthernHemisphere,withacap
areaof106km2.(A)Winter:June,JulyandAugust,(B)Summer:December,JanuaryandFebruary,
(C)Spring:September,OctoberandNovember,(D)Autumn:March,AprilandMay.
4. DiscussionandConclusions
Inthisarticle,wepresentedanalgorithmtodetectandtrackextratropicalcyclones,
studyingthechoiceofparametersfortheERA5reanalysis,intheSouthernHemisphere. To
identifycycloniccenters,weuserelativevorticityat850hPaandconnected-component
labeling,whichtrackscyclonesasareasratherthanlocalminimums. Wetestedtheuse
of three degrees of filtering smoothing of gaussian filter to determine the ideal level of
filteringforthebestdetectionofcyclones. Also,weshowedanexampleofrelativevorticity
fieldat850hPa,usingdifferentthresholdsforrelativevorticityandtestedfourdifferent
valuesofminimumareacriteria. Withtheseanalyses,weadjustedwithinthealgorithmto
improveitsperformance. Weusestandarddeviationofthegaussianfilterof0.5gridpoints,
thresholdofrelativevorticityof−10−4s−1,andareacriteriaof15pixels. Themaximum
displacementinonehourwasfixedto150km.
The two case studies presented here highlighted the good performance to detect
cyclogenesis and the more intense periods of the cyclones and identify cyclones that
merge/splitalongtheirlifetime. However,thepositionofthecyclonecenterduringthe
cyclolysis can be inaccurate, because of the increase in the area within the threshold,
possiblesuppressingpartofthedissipationprocess,asshownbythesecondcasestudy.
Despitethesefindings,webelievethatthealgorithmisusefulforstudyingextratropical
cyclonesandexploringthedifferentcharacteristicsoftheevents.
Comparingtheresultsusing1-hourlyand6-hourlytemporalresolution,wefinda
greateraveragenumberofeventsperyearusing1-hourlytemporalresolution. Thiscan

Atmosphere2024,15,230 17of19
beexplainedbythegreaterprecisioninidentifyingthetimeframeofcyclogenesisand
cyclolysiswithafinerresolution,andbytheinclusionofsomeshortereventsthatwould
havebeenremovedbytheminimumlifetimethreshold. Using41yearsofdata,theannual
count of extratropical cyclones of Southern Hemisphere displayed a slowly increasing
trendinbothtemporalresolution. Thedurationofthecyclonesofaround2daysisslightly
largerusing6-hourlytemporalresolutions,butitisinagreementwithNeu[16],which
comparesvariousmethodologiesusing6-hourlyresolutiondataset. Thedistancetraveled
bythecycloneswasalittlelongerusingthe6-htemporalresolutionduetotheremoval
ofshortercases. Thecyclonescapturedby1-htemporalresolutionareinaveragefaster
thanthosebythe6-htemporalresolution. Our6-htemporalresolutionresultsagreedwith
IMILASTintermofaveragespeed,mainlyrangingfrom20km/hto60km/h.
Thespatialdistributionofcyclogenesisfrequencyfromouralgorithmisverysimilar
tothosefromotherstudies, inparticularwithregardtothemostfavorableareasofde-
velopmentofextratropicalcyclones. Ingeneral,thenumberofeventsisconsistentwith
previousstudies,althoughthereisnoconsensusonthisamongthevariousmethods,as
shown by the IMILAST project. In terms of areas of suppression and intensification of
cyclogenesisintheSouthernHemisphere,ourresultsareconsistentwithpreviousstudies.
Furtherimprovementstothealgorithmcanbemade,suchasincludingdifferentparameter
thresholdsatdifferentaltitudelevels. ThealgorithmwasimplementedinPython,andits
sourcecodeisfreelyavailablefromtheauthorsuponrequest.
Futureresearchusingthemethodologydevelopedinthisstudyincludesunderstand-
ing the interannual variability of the characteristics of extratropical cyclones along the
southeasterncoastofSouthAmericaandpotentiallinkstoextremeeventsofoceantemper-
ature,knownasmarineheatwaves.
AuthorContributions:Conceptualization,C.K.P.R.;methodology,C.K.P.R.;software,C.K.P.R.;vali-
dation,C.K.P.R.;formalanalysis,C.K.P.R.andJ.P.M.;investigation,C.K.P.R.;writing—originaldraft
preparation,C.K.P.R.andJ.P.M.;writing—reviewandediting,J.P.M.,M.M.M.,R.R.andJ.L.L.d.A.;su-
pervision,J.M.B.S.;projectadministration,C.K.P.R.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding: National Council for Scientific and Technological Development (CNPq), projects
n◦ 406769/2021-4and406763/2022-4.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
Data Availability Statement: The ERA5/ECMWF reanalysis data is accessible at https://cds.
climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-level?tab=overview accessed on
23 May 2023 and the identification and tracking program is freely available upon request (ca-
rina.padilha@gmail.com).
Acknowledgments: WearealsogratefultotheNationalCouncilforScientificandTechnological
Development(CNPq)forprojectsfunding(n◦ 406769/2021-4and406763/2022-4). Wethankthe
resourcesprovidedbyCAPEStosupporttheGraduatePrograminOceanology.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
1. Wallace,J.M.;Hobbs,P.V.TheGeneralCirculation.InAnIntroductorySurvey,2nded.;Elsevier:Amsterdam,TheNetherlands;
AcademicPress:Boston,MA,USA,2006;pp.412–450.
2. Peixoto,J.P.;Oort,A.H.PhisicsofClimate;AmericanInstituteofPhisics:CollegePark,ML,USA,1992;520p.
3. Ulbrich,U.;Leckebusch,G.C.;Pinto,J.G.Extra-tropicalcyclonesinthepresentandfutureclimate:Areview.Theor.Appl.Climatol.
2009,96,117–131.[CrossRef]
4. Catto,J.L.; Ackerley,D.; Booth,J.F.; Champion,A.J.; Colle,B.A.; Pfahl,S.; Pinto,J.G.; Quinting,J.F.; Seiler,S.TheFutureof
MidlatitudeCyclones.Curr.Clim.Chang.Rep.2019,5,407–420.[CrossRef]
5. Sinclair,V.A.;Rantanen,M.;Haapanala,P.;Räisänen,J.;Järvinen,H.Thecharacteristicsandstructureofextra-tropicalcyclonesin
awarmerclimate.WeatherClim.Dyn.2020,1,1–25.[CrossRef]

Atmosphere2024,15,230 18of19
6. Lambert,S.J.AcycloneclimatologyoftheCanadianclimatecentregeneralcirculation.J.Clim.1988,1,109–115.[CrossRef]
7. Murray,R.J.;Simmonds,I.Anumericalschemefortrackingcyclonecentresfromdigitaldata.PartI:Developmentandoperation
ofthescheme.Aust.Meteorol.Mag.1991,39,155–166.
8. Lionello,P.;Dalan,F.;Elvini,E.CyclonesintheMediterraneanregion:ThepresentandthedoubledCO climatescenarios.Clim.
2
Res.2002,22,147–159.[CrossRef]
9. Rudeva,I.;Gulev,S.K.Climatologyofcyclonesizecharacteristicsandtheirchangesduringthecyclonelifecycle.Mon.Weather
Rev.2007,135,2568–2587.[CrossRef]
10. Hanley,J.;Caballero,R.ObjectiveidentificationandtrackingofmulticentrecyclonesintheERA-Interimreanalysisdataset.Q.J.
R.Meteorol.Soc.2012,138,612–625.[CrossRef]
11. Sinclair,M.R.AnobjectivecycloneclimatologyfortheSouthernHemisphere.Mon.WeatherRev.1994,122,2239–2256.[CrossRef]
12. Inatsu,M.Theneighborenclosedareatrackingalgorithmforextratropicalwintertimecyclones.Atmos.Sci.Lett.2009,10,267–272.
[CrossRef]
13. Hodges,K.I.Ageneralmethodfortrackinganalysisanditsapplicationtometeorologicaldata. Mon. WeatherRev. 1994,12,
2573–2586.[CrossRef]
14. Reboita,M.S.;daRocha,R.P.;deSouza,M.R.;Llopart,M.ExtratropicalcyclonesoverthesouthwesternSouthAtlanticOcean:
HadGEM2-ESandRegCM4projections.Int.J.Climatol.2018,38,2866–2879.[CrossRef]
15. Hodges,K.I.;Hoskins,B.J.;Boyle,J.AComparisonofRecentReanalysisDatasetsUsingObjectiveFeatureTracking:StormTracks
andTropicalEasterlyWaves.Mon.WeatherRev.2003,131,2012–2037.[CrossRef]
16. Blender,R.;Shubert,M.CycloneTrackinginDifferentSpatialandTemporalResolutions.Mon.WeatherRev.2000,128,377–384.
[CrossRef]
17. Trigo,I.F.Climatologyandinterannualvariabilityofstorm-tracksintheEuro-Atlanticsector:AcomparisonbetweenERA-40and
NCEP/NCARreanalyses.Clim.Dyn.2006,26,127–143.[CrossRef]
18. Flaounas,E.;Kotroni,V.;Lagouvardos,K.;Flaounas,I.CycloTRACK(v1.0)-trackingwinterextratropicalcyclonesbasedon
relativevorticity:Sensitivitytodatafilteringandotherrelevantparameters.Geosci.ModelDev.2014,7,1841–1853.[CrossRef]
19. Lim,E.P.;Simmonds,I.Southernhemispherewinterextratropicalcyclonecharacteristicsandverticalorganizationob-served
withtheERA-40datain1979–2001.J.Clim.2007,20,2675–2690.[CrossRef]
20. Wang,X.L.;Swail,V.R.;Zwiers,F.W.ClimatologyandChangesofExtratropicalCycloneActivity:ComparisonofERA-40with
NCEP-NCARReanalysisfor1958–2001.J.Clim.2006,19,3145–3166.[CrossRef]
21. Pinto,J.G.;Spangehl,T.;Ulbrich,U.;Speth,P.Sensitivitiesofacyclonedetectionandtrackingalgorithm:Individualtracksand
climatology.Meteorol.Z.2005,14,823–838.[CrossRef]
22. Crawford,A.D.;Serreze,M.C.DoestheSummerArcticFrontalZoneInfluenceArcticOceanCycloneActivity?J.Clim.2016,29,
4977–4993.[CrossRef]
23. Crawford,A.D.;Schreiber,E.A.P.;Sommer,N.;Serreze,M.C.;Stroeve,J.C.;Barber,D.G.SensitivityofNorthernHemisphere
CycloneDetectionandTrackingResultstoFineSpatialandTemporalResolutionUsingERA5. Mon. WeatherRev. 2021,149,
2581–2598.[CrossRef]
24. Simmonds,I.;Keay,K.VariabilityofSouthernHemisphereExtratropicalCycloneBehavior,1958-97.J.Clim.2000,13,550–561.
[CrossRef]
25. Reboita,M.S.;daRocha,R.P.;Ambrizzi,T.;Sugahara,S.SouthAtlanticOceancyclogenesisclimatologysimulatedbyregional
climatemodel(RegCM3).Clim.Dyn.2010,35,1331–1347.[CrossRef]
26. Hewson,T.D.;Titley,H.A.Objectiveidentification,typingandtrackingofthecompletelife-cyclesofcyclonicfeaturesathigh
spatialresolution.Meteorol.Appl.2009,17,355–381.[CrossRef]
27. Neu,U.;Akperov,M.G.;Bellenbaum,N.;Benestad,R.;Blender,R.;Caballero,R.;Cocozza,A.;Dacre,H.F.;Feng,Y.;Fraedrich,K.;
etal.Imilast:Acommunityefforttointer-compareextratropicalcyclonedetectionandtrackingalgorithms.Bull.Am.Meteorol.
Soc.2013,94,529–547.[CrossRef]
28. Raible,C.C.;Della-Marta,P.M.;Schwierz,C.;Wernli,H.;Blender,R.NorthernHemisphereextratropicalcyclones:Acomparison
ofdetectionandtrackingmethodsanddifferentreanalyses.Mon.WeatherRev.2009,136,880–897.[CrossRef]
29. Reale, M.; Margarida, L.R.; Liberato, L.R.; Lionello, P.; Pinto, J.G.; Salon, S.; Ulbrich, S.AGlobalClimatologyofExplosive
CyclonesusingaMulti-TrackingApproach.TellusDyn.Meteorol.Oceanogr.2019,71,1611340.[CrossRef]
30. Gramcianinov,C.B.;Campos,R.M.;Camargo,R.;Hodges,K.I.;Soares,C.G.;daSilvaDias,P.L.AnalysisofAtlanticextratropical
stormtrackscharacteristicsin41yearsofERA5andCFSR/CFSv2databases.Ocean.Eng.2020,216,108111.[CrossRef]
31. Hersbach,H.;Bell,B.;Berrisford,P.;Hirahara,S.;Horányi,A.;Muñoz-Sabater,J.;Nicolas,J.;Peubey,C.;Radu,R.;Schepers,D.;
etal.TheERA5globalreanalysis.Q.J.R.Meteorol.Soc.2020,146,1999–2049.[CrossRef]
32. Holton,J.R.IntroductiontoDynamicMeteorology,4thed.;Elsevier:Amsterdam,TheNetherlands,2004;p.535.
33. Hodges,K.I.Featuretrackingontheunitsphere.Mon.WeatherRev.1995,123,3458–3465.[CrossRef]
34. Hoskins,B.J.;Hodges,K.I.NewPerspectivesontheNorthernHemispherewinterstormtracks.J.Atmos.Sci.2002,59,1041–1061.
[CrossRef]
35. Satake,Y.;Inatsu,M.;Mori,M.;Hasegawa,A.Tropicalcyclonetrackingusinganeighborenclosedareatrackingalgorithm.Mon.
WeatherRev.2013,141,3539–3555.[CrossRef]

Atmosphere2024,15,230 19of19
36. Gonzales,R.C.;Woods,R.E.;PrenticeHall,P.DigitalImageProcessing,3rded.;PearsonInternationalEdition;PearsonEducation:
London,UK,1992.
37. Samet,H.ApplicationsofSpecialDataStructures:ComputerGraphics,ImageProcessingandGIS;Addison-Wesley:Boston,MA,USA,
1989;507p.
38. Inatsu,M.;Amada,S.Dynamicsandgeometryofextratropicalcyclonesintheuppertropospherebyaneighborenclosedarea
trackingalgorithm.J.Clim.2013,26,8641–8653.[CrossRef]
39. Bai,L.;Breen,D.CalculatingCenterofMassinanUnbounded2DEnvironment.J.Graph.Tools2008,13,53–60.[CrossRef]
40. Albuquerque,M.D.G.;LealAlves,D.C.;Espinoza,J.M.D.A.;Oliveira,U.R.;Simões,R.S.DeterminingShorelineRes-ponseto
Meteo-oceanographicEventsUsingRemoteSensingandUnmannedAerialVehicle(UAV):CaseStudyinSouthernBrazil.J.Coast.
Res.2018,85,766–770.[CrossRef]
41. Oliveira,U.R.;Simões,R.S.;Calliari,L.J.Duneserosionunderanextremehighwaveenergyeventonthecentralandsouthern
coastofRioGrandedoSulstate,Brazil.Rev.Bras.Geomorfol.2019,20,137–158.[CrossRef]
42. Lu,C.Amodifiedalgorithmforidentifyingandtrackingextratropicalcyclones.Adv.Atmos.Sci.2017,34,909–924.[CrossRef]
43. Crawford,A.D.;Alley,E.E.;Cooke,A.M.;Serreze,M.C.Synopticclimatologyofrain-on-snoweventsinAlaska.Mon.WeatherRev.
2020,148,1275–1295.[CrossRef]
44. Gan,M.A.;Rao,V.B.TheinfluenceoftheAndesCordilleraontransientdisturbances.Mon.WeatherRev.1994,122,1141–1157.
[CrossRef]
45. Vera,C.S.;Vigliarolo,P.K.;Berbry,E.H.Coldseasonsynoptic-scalewavesoversubtropicalSouthAmerica.Mon.WeatherRev.
2002,130,684–699.[CrossRef]
46. Treut,H.L.;Kalnay,E.Comparisonofobservedandsimulatedcyclonefrequencydistributionasdeterminedbyanobjective
method.Atmósfera1990,3,57–71.
47. Hoskins,B.J.;Hodges,K.I.AnewperspectiveonSouthernHemispherestormtracks.J.Clim.2005,18,4108–4129.[CrossRef]
48. Valsangkar,A.;Monteiro,J.M.;Narayanan,V.;Hotz,I.;Natarajan,V.AnExploratoryFrameworkforCycloneIdentificationand
Tracking.IEEETrans.Vis.Comput.Graph.2019,10,1–14.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.