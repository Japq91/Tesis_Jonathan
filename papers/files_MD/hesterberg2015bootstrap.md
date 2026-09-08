The American Statistician
ISSN: 0003-1305 (Print) 1537-2731 (Online) Journal homepage: www.tandfonline.com/journals/utas20
What Teachers Should Know About the Bootstrap:
Resampling in the Undergraduate Statistics
Curriculum
Tim C. Hesterberg
To cite this article: Tim C. Hesterberg (2015) What Teachers Should Know About the Bootstrap:
Resampling in the Undergraduate Statistics Curriculum, The American Statistician, 69:4,
371-386, DOI: 10.1080/00031305.2015.1089789
To link to this article: https://doi.org/10.1080/00031305.2015.1089789
© 2015 The Author(s). Published with
license by American Fisheries Society
View supplementary material
Published online: 29 Dec 2015.
Submit your article to this journal
Article views: 36507
View related articles
View Crossmark data
Citing articles: 79 View citing articles
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=utas20

Supplementarymaterialsforthisarticleareavailableonline.Pleasegotowww.tandfonline.com/r/TAS
What Teachers Should Know About the Bootstrap: Resampling in the
|     |     |     |     |     |     |     |     | Undergraduate |     |     | Statistics |     | Curriculum |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ---------- | --- | ---------- | --- |
TimC.HESTERBERG
|     |     |     |     |     |     |     |     | computed | using | z instead | of t | quantiles | and estimating | s with |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ---- | --------- | -------------- | ------ |
Bootstrappinghasenormouspotentialinstatisticseducation a divisor of n instead of n−1. Conversely, it is more accu-
|     |     |     |     |     |     |     |     | rate than | t-intervals | for | larger | samples. | Some other | bootstrap |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------ | -------- | ---------- | --------- |
andpractice,buttherearesubtleissuesandwaystogowrong.
Forexample,thecommoncombinationofnonparametricboot- intervalshavethesamesmall-sampleissues.
Thebootstrapisusedforestimatingstandarderrorsandbias,
| strapping | and bootstrap | percentile |     | confidence |     | intervals | is less |     |     |     |     |     |     |     |
| --------- | ------------- | ---------- | --- | ---------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
accuratethanusingt-intervalsforsmallsamples,thoughmore obtaining confidence intervals, and sometimes for tests. The
accurateforlargersamples.Mygoalsinthisarticlearetoprovide focus here is on relatively simple bootstrap methods and their
pedagogicalapplication,particularlyforStat101(introductory
adeeperunderstandingofbootstrapmethods—howtheywork,
whentheyworkornot,andwhichmethodsworkbetter—andto statistics with an emphasis on data analysis) and Mathemati-
calStatistics(afirstcourseinstatisticaltheory,usingmathand
| highlightpedagogical |     | issues.Supplementarymaterialsforthis |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
articleareavailableonline. simulation),thoughthemethodsareusefulelsewhereinthecur-
|     |     |     |     |     |     |     |     | riculum. | For more | background |     | on the bootstrap |     | and a broader |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | --- | ---------------- | --- | ------------- |
KEYWORDS: Bias;Confidenceintervals;Samplingdistribu- array of applications, see Efron and Tibshirani (1993) and
tion;Standarderror;Statisticalconcepts;Teaching. DavisonandHinkley(1997).Hesterberg(2014)isalongerver-
sionofthisarticle.Hesterbergetal.(2005)isanintroductionto
thebootstrapandpermutationtestsforStat101students.
Section1introducesthebootstrapforestimatorsandtstatis-
1. INTRODUCTION
tics,anddiscussesitspedagogicalandpracticalvalue.Section2
Resampling methods, including permutation tests and the developstheideabehindthebootstrap,andimplicationsthereof.
|            |               |     |           |     |            |           |     | Section | 3 visually | explores | when | the bootstrap |     | works or not, |
| ---------- | ------------- | --- | --------- | --- | ---------- | --------- | --- | ------- | ---------- | -------- | ---- | ------------- | --- | ------------- |
| bootstrap, | have enormous |     | potential | in  | statistics | education | and |         |            |          |      |               |     |               |
andcomparestheeffectsoftwosourcesofvariation—theorig-
practice.Theyarebeginningtomakeinroadsineducation.Cobb
inalsampleandbootstrapsampling.Section4surveysselected
| (2007) was | influential | in arguing |     | for the | pedagogical |     | value of |     |     |     |     |     |     |     |
| ---------- | ----------- | ---------- | --- | ------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
confidenceintervalsandtheirpedagogicalandpracticalmerits.
| permutation | tests | in particular. | Undergraduate |     |     | textbooks | that |     |     |     |     |     |     |     |
| ----------- | ----- | -------------- | ------------- | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
consistently use resampling as tools in their own right and to Section5coverspedagogicalandpracticalissuesinregression.
Section6containsasummaryanddiscussion.
| motivate | classical | methods | are beginning |     | to appear, |     | including |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ------------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ExamplesandfiguresarecreatedinR(RCoreTeam2014),
| Lock et | al. (2013) | for Introductory |     | Statistics |     | and Chihara | and |     |     |     |     |     |     |     |
| ------- | ---------- | ---------------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Hesterberg (2011) for Mathematical Statistics. Other texts usingtheresamplepackage(Hesterberg2015).Scriptsareinan
onlinesupplement.
(Diez,Barr,andC¸etinkayaRundel2014;Tintleetal.2014a)use
permutationorotherrandomizationtexts,thoughminimalboot-
|            |              |          |     |          |      |          |       | 1.1 VerizonExample |     |     |     |     |     |     |
| ---------- | ------------ | -------- | --- | -------- | ---- | -------- | ----- | ------------------ | --- | --- | --- | --- | --- | --- |
| strapping. | Experimental | evidence |     | suggests | that | students | learn |                    |     |     |     |     |     |     |
betterusingthesemethods(Tintleetal.2014b).
Thefollowingexampleisusedthroughoutthisarticle.Verizon
Theprimaryfocusofthisarticleisthebootstrap,wherethere
wasanIncumbentLocalExchangeCarrier(ILEC),responsible
| are a variety | of competing |     | methods | and | issues | that are | subtler |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
formaintainingland-linephoneserviceincertainareas.Verizon
| and less | well-known | than | for permutation |     | tests. | I hope | to pro- |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | --------------- | --- | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
alsosoldlong-distanceservice,asdidanumberofcompetitors,
videabetterunderstandingofthekeyideasbehindthebootstrap, termed Competitive Local Exchange Carriers (CLEC). When
| and the     | merits of | different | methods.     | Without |        | this understand- |            |           |          |         |         |                 |     |              |
| ----------- | --------- | --------- | ------------ | ------- | ------ | ---------------- | ---------- | --------- | -------- | ------- | ------- | --------------- | --- | ------------ |
|             |           |           |              |         |        |                  |            | something | went     | wrong,  | Verizon | was responsible |     | for repairs, |
| ing, things | can go    | wrong.    | For example, |         | people | may              | prefer the |           |          |         |         |                 |     |              |
|             |           |           |              |         |        |                  |            | and was   | supposed | to make | repairs | as quickly      | for | CLEC long-   |
bootstrapforsmallsamples,toavoidrelyingonthecentrallimit distancecustomersasfortheirown.TheNewYorkPublicUtili-
theorem(CLT).However,thecommonbootstrappercentilecon-
tiesCommission(PUC)monitoredfairnessbycomparingrepair
fidenceintervalispoorforsmallsamples;itislikeat-interval timesforVerizonanddifferentCLECs,fordifferentclassesof
|     |     |     |     |     |     |     |     | repairs and | time   | periods.        | In each | case   | a hypothesis | test was |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --------------- | ------- | ------ | ------------ | -------- |
|     |     |     |     |     |     |     |     | performed   | at the | 1% significance |         | level, | to determine | whether  |
Tim C. Hesterberg is Senior Statistician, Google, (E-mail: timhester- repairs for CLEC’s customers were significantly slower than
| berg@gmail.com). | The | author thanks | David | Diez, | Jo Hardin, | Beth | Chance, |     |     |     |     |     |     |     |
| ---------------- | --- | ------------- | ----- | ----- | ---------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
forVerizon’scustomers.Therewerehundredsofsuchtests.If
FabianGallusser,LauraChihara,NicholasHorton,HalVarian,BradEfron,five
|     |     |     |     |     |     |     |     | substantially | more | than | 1% of | the tests | were significant, | then |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ---- | ----- | --------- | ----------------- | ---- |
referees,andtwoeditorsforhelpfulcomments.
Colorversionsofoneormoreofthefiguresinthearticlecanbefoundonline Verizonwouldpaylargepenalties.Thesetestswereperformed
atwww.tandfonline.com/r/tas. usingttests;Verizonproposedusingpermutationtestsinstead.
©2015AmericanStatisticalAssociation DOI:10.1080/00031305.2015.1089789 TheAmericanStatistician,November2015,Vol.69,No.4 371

Table1. Verizonrepairtimes θˆ =x¯ fortheILECandCLECdatasets.Weuseeachdistribu-
tiontoestimatecertainthingsaboutthecorrespondingsampling
n mean sd distribution,including:
ILEC 1664 8.41 16.5 • standard error: the bootstrap standard error is the sam-
CLEC 23 16.69 19.5 (cid:2) ple standard deviation of the bootstrap distribution, s b =
(cid:3)
1/(r−1) r
i=1
(θˆ
i
∗−θˆ∗)2.
ThedataforonecombinationofCLEC,classofservice,and • confidenceintervals:aquick-and-dirtyinterval,thebootstrap
period are shown in Table 1 and Figure 1. Both samples are percentile interval, is the range of the middle 95% of the
positivelyskewed.ThemeanCLECrepairtimeisnearlydouble bootstrapdistribution,
thatforILEC,suggestingdiscrimination,thoughthedifference • bias:thebootstrapbiasestimateisθˆ∗−θˆ.
couldbejustchance.
Theone-sidedpermutationtestp-valueis0.0171,wellabove Summarystatisticsofthebootstrapdistributionsare
the1%cutoffmandatedbythePUC.Incomparison,thepooled
Observed SE Mean Bias
t-testp-valueis0.0045,aboutfourtimestoosmall.Thepermu-
CLEC 16.50913 3.961816 16.53088 0.0217463
tation test gives the correct answer, with nearly exact Type 1
ILEC 8.41161 0.357599 8.40411 -0.0075032
error rates; this was recognized as far back as Fisher (1936),
whousedt-testsasanapproximationbecauseperturbationtests The CLEC SE is larger primarily due to the smaller sam-
were computationally infeasible then. The t-test is inaccurate ple size and secondly to the larger sample sd in the original
because it is sensitive to skewness when the sample sizes dif- data.Bootstrappercentileintervalsare(7.73√ ,9.13)forILECand
fer.Usingt-testsfor10,000Verizonfairnesstestswouldresult (10.1,25.4)forCLEC.Forcomparison,s/ n=0.36forILEC
inabout400falsepositiveresultsinsteadoftheexpected100, and4.07forCLEC,andstandardtintervalsare(7.71,9.12)and
resultinginlargemonetarypenalties.Similarly,tconfidencein- (8.1,24.9).Thedistributionappearsapproximatelynormalfor
tervalsareinaccurate.Wewillseehowinaccurate,andexplore theILECsamplebutnotforthesmallerCLECsample,suggest-
alternatives,usingthebootstrap. ingthatt intervalsmightbereasonablefortheILECmeanbut
nottheCLECmean.
1.2 One-SampleBootstrap Thebootstrapseparatestheconceptofastandarderror—the
Let θˆ be a statistic calculated from a sample of n iid obser- standard deviatio√n of a sampling distribution—from the com-
mon formula s/ n for estimating the SE of a sample mean.
vations (time series and other dependent data are beyond the
This separation should help students understand the concept.
scopeofthisarticle).Intheordinarynonparametricbootstrap,
Based on extensive experience interviewing job candidates, I
wedrawnobservationswithreplacementfromtheoriginaldata
attestthatabetterwaytoteachaboutSEsisneeded—toomany
to create a bootstrap sample or resample, and calculate the
statisticθˆ∗forthissample(weuse∗todenoteabootstrapquan- donotunderstandSEs,andevenconfuseSEsinothercontexts
tity).Werepeatthatmanytimes,sayr =10,000(weuse10,000 withtheformulafortheSEofasamplemean.
unless noted otherwise). The bootstrap statistics comprise the
1.3 Two-SampleBootstrap
bootstrapdistribution.Figure2showsbootstrapdistributionsof
Foratwo-samplebootstrap,weindependentlydrawbootstrap
samples with replacement from each sample, and compute a
statistic that compares the samples. For the Verizon data, we
drawasampleofsize1664fromtheILECdataand23fromthe
CLECdata,andcomputethedifferenceinmeansx¯ −x¯ .The
1 2
bootstrapdistribution(seeonlinesupplement)iscenteredatthe
observedstatistic;itisusedforconfidenceintervalsandstandard
errors.ItisskewedliketheCLECdistribution;tintervalswould
notbeappropriate.
Forcomparison,thepermutationtestpoolsthedataandsplits
the pooled data into two groups using sampling without re-
placement,beforetakingthedifferenceinmeans.Thesampling
isconsistentwiththenullhypothesisofnodifferencebetween
groups,andthedistributioniscenteredatzero.
1.4 Bootstrapt-Distribution
Itisnotsurprisingthattproceduresareinaccurateforskewed
data with a sample of size 23, or for the difference when one
sample is that small. More surprising is how bad t confidence
intervals are for the larger sample, size 1664. To see this, we
Figure1. NormalquantileplotofILECandCLECrepairtimes. bootstraptstatistics.
372 StatisticsandtheUndergraduateCurriculum

BootstrapdistributionsforVerizondata.Bootstrapdistributionsforx¯,fortheILECandCLECdatasets.
Figure2.
Above we resampled univariate distributions of estimators ativemedian,soitsquantilesendup3xasasymmetricaltothe
| x¯      | x¯ −x¯      |     |         |                      |     |         |       |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------- | -------------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| like or | 1 2 . Here, | we  | look at | joint distributions, |     | for ex- | left. |     |     |     |     |     |     |     |
ample, the joint distribution of X¯ and s, and distributions of The amount of skewness apparent in the bootstrap t-
statistics that depend on both θˆ and θ. To estimate the sam- distribution matters. The bootstrap distribution is a sampling
plingdistributionofθˆ−θ,weusethebootstrapdistributionof
|     |     |     |     |     |     |     | distribution, | not | raw data; | the | CLT | has already | had | its one |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | --- | ----------- | --- | ------- |
θˆ∗−θˆ.ThebootstrapbiasestimateisE(θˆ∗−θˆ),anestimateof chance to work. At this point, any deviations indicate errors
E(θˆ−θ).Toestimatethesamplingdistributionofatstatistic
|     |     |     |     |     |     |     | in procedures                           | that | assume | normal | or  | t sampling | distributions.   |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | ---- | ------ | ------ | --- | ---------- | ---------------- | --- |
|     |     |     |     |     |     |     | 3.6%ofthebootstrapdistributionisbelow−t |      |        |        |     |            | α/2,n−1 ,and1.7% |     |
θˆ−θ
|     |     | t = |     | ,   |     |     | is above | t       | (based          | on r | =106 samples, |       | α =0.05). | Even |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | ---- | ------------- | ----- | --------- | ---- |
|     |     |     |     |     |     | (1) |          | α/2,n−1 |                 |      |               |       |           |      |
|     |     |     | SE  |     |     |     | n=1664,  |         |                 |      |               |       |           |      |
|     |     |     |     |     |     |     | with     |         | the t statistic |      | is not even   | close | to having | a t- |
whereSEisastandarderrorcalculatedfromtheoriginalsample, distribution,basedonwhatmatters—tailprobabilities.
weusethebootstrapdistributionof Inmyexperiencegivingtalksandcourses,typicallyoverhalf
oftheaudienceindicatesthereisnoproblemwiththeskewness
θˆ∗−θˆ
t∗ = . apparent in plots like Figure 3. They are used to looking at
(2)
SE∗
|        |             |       |              |     |         |            | normal quantile |      | plots of       | data, | not of   | sampling | distributions. |     |
| ------ | ----------- | ----- | ------------ | --- | ------- | ---------- | --------------- | ---- | -------------- | ----- | -------- | -------- | -------------- | --- |
|        |             |       |              |     |         | √          | A common        | flaw | in statistical |       | practice | is to    | fail to judge  | how |
| Figure | 3 shows the | joint | distribution | of  | X¯∗ and | s∗/ n, and |                 |      |                |       |          |          |                |     |
accuratestandardCLT-basedmethodsareforspecificdata;the
thedistributionoft∗,fortheILECdatawithn=1664.Standard
bootstrapt-distributionprovidesaneffectivewaytodoso.
X¯
| theory says            | that for | normal | population√s |                       | and s | are indepen- |     |     |     |     |     |     |     |     |
| ---------------------- | -------- | ------ | ------------ | --------------------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| dent,andthetstatistict |          | =(X¯   | −μ)/(s/      | n)hasat-distribution. |       |              |     |     |     |     |     |     |     |     |
1.5 PedagogicalandPracticalValue
X¯
| However, | for positively | skewed | populations |     | and | s are posi- |     |     |     |     |     |     |     |     |
| -------- | -------------- | ------ | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
tivelycorrelated,thecorrelationdoesnotgetsmallerwithlarge The bootstrap process reinforces the central role that sam-
n,andthetstatisticdoesnothaveat-distribution.WhileX¯∗ is plingfromapopulationplaysinstatistics.Samplingvariability
positivelyskewedwithmeanx¯,tistwicea√sskewedintheop- is visible, and it is natural to measure the variability of the
positedirectionbecausethedenominators/ nismoreaffected bootstrapdistributionusingmethodsstudentslearnedforsum-
bylargeobservationsthanthenumeratorX¯ marizingdata,suchasthestandarddeviation.Studentscansee
is.Andthasaneg-
ifthebootstrapdistributionisbell-shaped.Itisnaturaltousethe
middle95%ofthedistributionasa95%confidenceinterval.
Thebootstrapmakestheabstractconcrete—abstractconcepts
|     |     |     |     |     |     |     | like sampling | distributions, |     | standard  |     | errors, | bias, central | limit  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | --- | --------- | --- | ------- | ------------- | ------ |
|     |     |     |     |     |     |     | theorem,      | and confidence |     | intervals | are | visible | in plots      | of the |
bootstrapdistribution.
|     |     |     |     |     |     |     | The bootstrap |     | works | the same | way | with | a wide | variety of |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | -------- | --- | ---- | ------ | ---------- |
statistics.Thismakesiteasyforstudentstoworkwithavariety
ofstatistics,andfocusonideasratherthanformulas.Thisalso
letsusdobetterstatistics,becausewecanworkwithstatistics
|     |     |     |     |     |     |     | that are | appropriate | rather | than | just | those that | are | easy—for |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ---- | ---- | ---------- | --- | -------- |
example,amedianortrimmedmeaninsteadofamean.
Studentscanobtainconfidenceintervalsbyworkingdirectly
=
Figure 3. CLT with n 1664. Left: scatterplot of bootstrap means withthestatisticofinterest,ratherthanusingat statistic.You
andstandarderrors,ILECdata.Right:bootstrapt-distribution. couldskiptalkingabouttstatisticsandtintervals,ordeferthat
|     |     |     |     |     |     |     |     | TheAmericanStatistician,November2015,Vol.69,No.4 |     |     |     |     |     | 373 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |

Figure4. Idealworld.Samplingdistributionsareobtainedbydrawingrepeatedsamplesfromthepopulation,computingthestatisticofinterest
foreach,andcollecting(aninfinitenumberof)thosestatisticsasthesamplingdistribution.
| untillater.Atthatpointyoumayintroduceanotherquick-and- |     |     |     |     |     |     |     |     |        |                |             |              | χ2  |        |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | ----------- | ------------ | --- | ------ |
|                                                        |     |     |     |     |     |     |     |     | normal | distributions. | I recommend | not teaching | the | inter- |
dirtyconfidenceinterval,thetintervalwithbootstrapstandard vals for a variance, or F-based intervals for the ratio of vari-
error, θˆ±t s b. In mathematical statistics, students can use ances, because they are not useful in practice, with no robust-
α/2
thebootstraptohelpunderstandjointdistributionsofestimators
nessagainstnonnormality.Theircoveragedoesnotimproveas
likeX¯
| ands,andtounderstandthedistributionoftstatistics,and |     |     |     |     |     |     |     |     | n→∞. |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
computebootstraptconfidenceintervals,seeSection4.3.
Thebootstrapcanalsoreinforcetheunderstandingofformula
| methods, | and provide |     | a way | for stu√dents |     | to check | their | work. |     |     |     |     |     |     |
| -------- | ----------- | --- | ----- | ------------- | --- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
2. THEIDEABEHINDBOOTSTRAPPING
| Students | may | know the | formula | s/  | n without |     | understanding |     |     |     |     |     |     |     |
| -------- | --- | -------- | ------- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
whatitreallyis;buttheycancompareittos
|     |     |     |     |     |     | b ortoaneyeball |     |     | Inferential | statistics | is based | on sampling | distributions. | In  |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ----------- | ---------- | -------- | ----------- | -------------- | --- |
estimateofstandarddeviationfromahistogramofthebootstrap theory,togetthesewe
distribution,andseethatitmeasureshowthesamplemeanvaries
|     |     |     |     |     |     |     |     |     | • draw | (all or infinitely | many) | samples from | the population, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------ | ----- | ------------ | --------------- | --- |
duetorandomsampling.
| Resampling |     | is also | important | in  | practice. | It often | provides |     | and |     |     |     |     |     |
| ---------- | --- | ------- | --------- | --- | --------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
•
computethestatisticofinterestforeachsample(suchasthe
| the only | practical | way | to do | inference—when |     |     | it is | too dif- |     |     |     |     |     |     |
| -------- | --------- | --- | ----- | -------------- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
mean,median,etc.).
| ficult to | derive | formulas, | or  | the | data are | stored | in  | a way |     |     |     |     |     |     |
| --------- | ------ | --------- | --- | --- | -------- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
that make calculating the formulas impractical; a longer ver- Thedistributionofthestatisticsisthesamplingdistribution,
| sion of  | this article | (Hesterberg |         | 2014) | and  | (Chamandy |     | 2015) | seeFigure4. |     |     |     |     |     |
| -------- | ------------ | ----------- | ------- | ----- | ---- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- |
| contains | examples     | from        | Google, |       | from | my work   | and | oth-  |             |     |     |     |     |     |
However,inpracticewecannotdrawarbitrarilymanysamples
ers. In other cases, resampling provides better accuracy than from the population; we have only one sample. The bootstrap
formula methods. For one simple example, consider confi- ideaistodrawsamples fromanestimateofthepopulation, in
| dence intervals |     | for the | variance |     | of the | CLEC | population. |     |     |     |     |     |     |     |
| --------------- | --- | ------- | -------- | --- | ------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
lieuofthepopulation:
| s2 =380.4, |          |              |     | s2  |           |              |         |      |                               |     |     |                   |     |     |
| ---------- | -------- | ------------ | --- | --- | --------- | ------------ | ------- | ---- | ----------------------------- | --- | --- | ----------------- | --- | --- |
|            | the      | bootstrap    | SE  | for | is 267,   | and          | the 95% | per- |                               |     |     |                   |     |     |
|            |          |              |     |     |           |              |         |      | • drawsamplesfromanestimateof |     |     | thepopulation,and |     |     |
| centile    | interval | is (59,932). |     | The | classical | normal-based |         | in-  |                               |     |     |                   |     |     |
•
tervalis((n−1)s2/χ2 ,(n−1)s2/χ2 )=(228,762). computethestatisticofinterestforeachsample.
|     |     | 22,0.975 |     |     | 22,0.025 |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
It assumes that (n−1)s2/σ2 ∼χ2(n−1), but for long-tailed Thedistributionofthestatisticsisthebootstrapdistribution,
s2
| distributions | the | actual | variance | of  | is  | far greater | than | for | seeFigure5. |     |     |     |     |     |
| ------------- | --- | ------ | -------- | --- | --- | ----------- | ---- | --- | ----------- | --- | --- | --- | --- | --- |
Figure5. Bootstrapworld.Thebootstrapdistributionisobtainedbydrawingrepeatedsamplesfromanestimateofthepopulation,computing
thestatisticofinterestforeach,andcollectingthosestatistics.Thedistributioniscenteredattheobservedstatistic(x¯),nottheparameter(μ).
374 StatisticsandtheUndergraduateCurriculum

take,theyarecenteredatx¯,notμ.Insteadweusethebootstrap
2.1 Plug-InPrinciple
|     |     |     |     |     |     |     |     | to tell how | accurate | the | original estimate |     | is. In this | regard the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ----------------- | --- | ----------- | ---------- |
Thebootstrapisbasedontheplug-inprinciple—ifsomething
bootstrapislikeformulamethodsthatusethedatatwice—once
| is unknown, | we  | substitute | an  | estimate | for it. | This principle |     | is  |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | -------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tocomputeanestimate,andagaintocomputeastandarderror
veryfamilia√rtostatisticians.Forexample,thesdofthesample
fortheestimate.Thebootstrapjustusesadifferentapproachto
| mean is | σ/ n; | when | σ is unknown | we  | substitute | an  | estimate |     |     |     |     |     |     |     |
| ------- | ----- | ---- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
estimatingthestandarderror.
s,thesamplestandarddeviation.Withthebootstrapwegoone
|                      |     |     |          |       |          |     |          | If the | bootstrap | distribution | is not | centered | at  | the observed |
| -------------------- | --- | --- | -------- | ----- | -------- | --- | -------- | ------ | --------- | ------------ | ------ | -------- | --- | ------------ |
| step farther—instead |     | of  | plugging | in an | estimate | for | a single |        |           |              |        |          |     |              |
statistic—ifthereisbias—wecouldsubtracttheestimatedbias
parameter,wepluginanestimateforthewholepopulationF. θˆ−B (cid:4) ias=2θˆ−θˆ∗.
|      |            |          |     |         |            |     |           | to produce | a bias-adjusted |     | estimate, |     |     | We  |
| ---- | ---------- | -------- | --- | ------- | ---------- | --- | --------- | ---------- | --------------- | --- | --------- | --- | --- | --- |
| This | raises the | question | of  | what to | substitute | for | F. Possi- |            |                 |     |           |     |     |     |
generallydonotdothis—biasestimatescanhavehighvariabil-
| bilities | include | the nonparametric, |     | parametric, |     | and | smoothed |     |     |     |     |     |     |     |
| -------- | ------- | ------------------ | --- | ----------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ity(EfronandTibshirani1993).Biasisanotherreasonnottouse
bootstrap.Theprimaryfocusofthisarticleisthenonparamet- (cid:4)
|                |     |      |        |            |     |                |     | theaverageofbootstrapestimatesθˆ∗ |     |     |     | =θˆ+B | iastoreplacethe |     |
| -------------- | --- | ---- | ------ | ---------- | --- | -------------- | --- | --------------------------------- | --- | --- | --- | ----- | --------------- | --- |
| ric bootstrap, | the | most | common | procedure, |     | which consists | of  |                                   |     |     |     |       |                 |     |
originalestimateθˆ—thataddsthebiasestimatetotheoriginal
| drawingsamplesfromtheempiricaldistributionFˆ |     |     |     |     |     | n(withprob- |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ability1/noneachobservation),thatis,drawingsampleswith statistic,doublinganybias.
replacementfromthedata. ThesecondimplicationisthatwedonotusetheCDForquan-
tilesofthebootstrapdistributionofθˆ∗
toestimatetheCDFor
| In the | parametric | bootstrap, |     | we assume |     | a model | (e.g., | a   |     |     |     |     |     |     |
| ------ | ---------- | ---------- | --- | --------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
quantilesofthesamplingdistributionofanestimatorθˆ.Instead,
| gamma | distribution | with | unknown | shape | and | scale), | estimate |     |     |     |     |     |     |     |
| ----- | ------------ | ---- | ------- | ----- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
parameters for that model, then draw bootstrap samples from webootstraptoestimatethingslikethestandarddeviation,the
|     |     |     |     |     |     |     |     | expectedvalueofθˆ−θ,andtheCDFandquantilesofθˆ−θ |     |     |     |     |     | or  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
themodelwiththoseestimatedparameters.
(θˆ−θ)/SE.
Thesmoothedbootstrapisacompromisebetweenparametric
| and nonparametric |     | approaches; |     | if we believe |     | the population |     | is  |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
continuous, we may sample from a continuous Fˆ, say a ker- 2.4 KeyIdeaVersusImplementationDetails
| nel density | estimate | (Silverman |     | and Young |     | 1987; Hall, | DiCi- |     |     |     |     |     |     |     |
| ----------- | -------- | ---------- | --- | --------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Whatpeoplemaythinkofasthekeybootstrapidea—drawing
| ccio, and | Romano | 1989;          | Hesterberg | 2014).   |                | Smoothing | is not |         |                  |     |          |         |      |               |
| --------- | ------ | -------------- | ---------- | -------- | -------------- | --------- | ------ | ------- | ---------------- | --- | -------- | ------- | ---- | ------------- |
|           |        |                |            |          |                |           |        | samples | with replacement |     | from the | data—is | just | a pair of im- |
| common;   | it is  | rarely needed, |            | and does | not generalize |           | well   | to      |                  |     |          |         |      |               |
plementationdetails.Thefirstissubstitutingtheempiricaldis-
multivariateandfactordata.
|     |     |     |     |     |     |     |     | tribution | for the | population; | alternatives | include |     | smoothed or |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----------- | ------------ | ------- | --- | ----------- |
parametricdistributions.Thesecondisusingrandomsampling.
2.2 FundamentalBootstrapPrinciple
|     |     |     |     |     |     |     |     | Here too | there | are alternatives, | including |     | analytical | methods |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----------------- | --------- | --- | ---------- | ------- |
Thefundamentalbootstrapprincipleisthatthissubstitution (e.g., when θˆ =x¯ we may calculate the mean and variance of
| usually | works—that | we  | can plug | in  | an estimate | for | F, then |               |              |     |               |     |            |        |
| ------- | ---------- | --- | -------- | --- | ----------- | --- | ------- | ------------- | ------------ | --- | ------------- | --- | ---------- | ------ |
|         |            |     |          |     |             |     |         | the bootstrap | distribution |     | analytically) | and | exhaustive | calcu- |
nn
sample,andtheresultingbootstrapdistributionprovidesuseful lations. There are(cid:5) p(cid:6)ossible bootstrap samples from a fixed
informationaboutthesamplingdistribution. sampleofsizen, 2n−1 iforderdoesnotmatter,orevenfewer
n
The bootstrap distribution is in fact a sampling distribution. insomecases likebinarydata;ifnissmallwecould evaluate
Thebootstrapusesasamplingdistribution(fromanestimateFˆ)
allofthese.Wecallthisanexhaustivebootstraportheoretical
toestimatethingsaboutthesamplingdistribution(fromF).
bootstrap.Butmoreoftenexhaustivemethodsareinfeasible,so
There are some things to watch out for, ways the bootstrap we draw say 10,000 random samples instead; we call this the
distribution differs from the sampling distribution. We discuss MonteCarlosamplingimplementation.
| some of | these | below, but | one | is important | enough | to  | mention |     |     |     |     |     |     |     |
| ------- | ----- | ---------- | --- | ------------ | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
immediately.
|     |     |     |     |     |     |     |     | 2.5 HowtoSample |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
2.3 Inference,NotBetterEstimates Normally we should draw bootstrap samples the same way
thesamplewasdrawninreallife,forexample,simplerandom
Thebootstrapdistributioniscenteredattheobservedstatis-
tic,notthepopulationparameter,forexample,atx¯,notμ. sampling or stratified sampling. Pedagogically, this reinforces
therolethatrandomsamplingplaysinstatistics.
Thishastwoprofoundimplications.First,itmeansthatwedo
Oneexceptiontothatruleistoconditionontheobservedin-
notusethemeanofthebootstrapstatisticsasareplacementfor
formation.Forexample,whencomparingsamplesofsizen
1 and
theoriginalestimate.1Forexample,wecannotusethebootstrap
|            |     |               |     |      |           |         |     | n ,wefixthosenumbers,eveniftheoriginalsamplingprocess |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ---- | --------- | ------- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| to improve | on  | x¯; no matter | how | many | bootstrap | samples | we  | 2                                                     |     |     |     |     |     |     |
couldhaveproduceddifferentcounts.(Thisistheconditional-
|     |     |     |     |     |     |     |     | ity principle | in statistics, |     | the idea of | conditioning |           | on ancillary |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | --- | ----------- | ------------ | --------- | ------------ |
|     |     |     |     |     |     |     |     | statistics.)  | Conditioning   |     | also avoids | some         | technical | problems,    |
1Thereareexceptions,wherethebootstrapisusedtoobtainbetterestimates,
forexample,inrandomforests.Thesearetypicalwhereabootstrap-likeproce- particularlyinregression,seeSection5.
dureisusedtoworkaroundaflawinthebasicprocedure.Forexample,consider Wecanalsomodifythesamplingtoanswerwhat-if questions.
estimatingE(Y|X=x)wherethetruerelationshipissmooth,usingonlyastep Forexample,wecouldbootstrapwithandwithoutstratification
functionwithrelativelyfewsteps.Bytakingbootstrapsamplesandapplying
|     |     |     |     |     |     |     |     | and compare | the | resulting | standard | errors, | to investigate | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | -------- | ------- | -------------- | --- |
thestepfunctionestimationproceduretoeach,thestepboundariesvarybe-
valueofstratification.Wecouldalsodrawsamplesofadifferent
tweensamples;byaveragingacrosssamplesthefewlargestepsarereplaced
bymanysmallerones,givingasmootherestimate.Thisisbagging(bootstrap size; say we are planning a large study and obtain an initial
aggregating). dataset of size 100, we can draw bootstrap samples of size
|     |     |     |     |     |     |     |     |     | TheAmericanStatistician,November2015,Vol.69,No.4 |     |     |     |     | 375 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |

•
2000toestimatehowlargestandarderrorswouldbewiththat Bootstrap resamples are chosen randomly from the original
| samplesize.Conversely,thisalsoanswersacommonquestion |     |     |     |     | sample. |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
aboutbootstrapping—whywesamplewiththesamesizeasthe
originaldata—becausebydoingsothestandarderrorsreflectthe
|     |     |     |     |     | 3.1 SampleMean:LargeSampleSize |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
actualdata,ratherthanahypotheticallargerorsmallerdataset.
|     |     |     |     |     | Figure   | 6 shows    | a population, | the      | sampling | distribution for  |
| --- | --- | --- | --- | --- | -------- | ---------- | ------------- | -------- | -------- | ----------------- |
|     |     |     |     |     | the mean | with n=50, | four          | samples, | and      | the corresponding |
3. VARIATIONINBOOTSTRAPDISTRIBUTIONS
|     |     |     |     |     | bootstrap | distributions. | Each | bootstrap | distribution | is centered |
| --- | --- | --- | --- | --- | --------- | -------------- | ---- | --------- | ------------ | ----------- |
Weclaimedabovethatthebootstrapdistributionusuallypro- at the statistic x¯ from the corresponding sample rather than at
vides useful information about the sampling distribution. We thepopulationmeanμ.Thespreadsandshapesofthebootstrap
elaborate on that now with a series of visual examples, one distributionsvaryabitbutnotalot.
wherethingsgenerallyworkwellandthreewithproblems.We These observations inform what the bootstrap distributions
addresstwoquestions:
|     |     |     |     |     | may be used | for. | The bootstrap | does | not provide | a better esti- |
| --- | --- | --- | --- | --- | ----------- | ---- | ------------- | ---- | ----------- | -------------- |
mateofthepopulationparameter,becausethebootstrapmeans
• Howaccurateisthetheoretical(exhaustive)bootstrap? are centered at x¯, not μ. Similarly, quantiles of the boot-
| • How accurately | does | the Monte Carlo implementation |     | ap- |                     |     |         |        |                |              |
| ---------------- | ---- | ------------------------------ | --- | --- | ------------------- | --- | ------- | ------ | -------------- | ------------ |
|                  |      |                                |     |     | strap distributions |     | are not | useful | for estimating | quantiles of |
proximatethetheoreticalbootstrap? the sampling distribution. Instead, the bootstrap distributions
areusefulforestimatingthespreadandshapeofthesampling
| Bothreflectrandomvariation: |     |     |     |     | distribution. |        |       |            |           |               |
| --------------------------- | --- | --- | --- | --- | ------------- | ------ | ----- | ---------- | --------- | ------------- |
|                             |     |     |     |     | The right     | column | shows | additional | bootstrap | distributions |
• The original sample is chosen randomly from the forthefirstsample,withr =1000orr =104resamples.Using
population. moreresamplesreducesrandomMonteCarlovariation,butdoes
Figure6. Bootstrapdistributionforthemean,n=50.Theleftcolumnshowsthepopulationandfoursamples.Themiddlecolumnshowsthe
samplingdistributionforX¯,andbootstrapdistributionsofX¯∗foreachsample,withr =104.Therightcolumnshowsmorebootstrapdistributions
| forthefirstsample,threewithr |     | =1000andtwowithr | =104. |     |     |     |     |     |     |     |
| ---------------------------- | --- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
376 StatisticsandtheUndergraduateCurriculum

notfundamentallychangethebootstrapdistribution—itstillhas While not apparent in the pictures, bootstra√p distributions
thesameapproximatecenter,spread,andshape. tendtobetoonarrowonaverage,byafactorof (n−1)/nfor
The Monte Carlo variation is much smaller than the vari- thesamplemean,andapproximatelythatformanyotherstatis-
ation due to different original samples. For many uses, such tics.Thisgoesbacktotheplug-inprinciple;(cid:3)theempiricaldistri-
asquick-and-dirtyestimationofstandarderrorsorapproximate butionhasvarianceσˆ2 =var (X)=1/n (x −x¯)2,andthe
|                       |                                   |     |     |     | Fˆ n | i   |     |
| --------------------- | --------------------------------- | --- | --- | --- | ---- | --- | --- |
| confidenceintervals,r | =1000resamplesisadequate.However, |     |     |     |      |     |     |
theoreticalbootstrapstandarderroristhestandarddeviationof
there is noticeable variability (including important but less- a mean√of n independent observations from that distrib√ution,
noticeable variability in the tails) so when accuracy matters, s =σˆ/ n √. That is, smaller than the usual formula s/ n by
b
| r =104 |     |     |     | (n  | −1)/n. | s =3.96 |     |
| ------ | --- | --- | --- | --- | ------ | ------- | --- |
ormoresamplesshouldbeused. a factor of √ For example, the CLEC b is
|     |     |     |     | smallerthans/   | n=4.07.            |                      |     |
| --- | --- | --- | --- | --------------- | ------------------ | -------------------- | --- |
|     |     |     |     | The combination | of this narrowness | bias and variability | in  |
3.2 SampleMean:SmallSampleSize
spreadmakessomebootstrapconfidenceintervalsunder-cover,
seeSection4.Classi√caltintervalscompensateusingtwofudge
Figure7issimilartoFigure6,butforasmallersamplesize,
n/(n−1)incomputingthesamplestan-
n=9(andadifferentpopulation).Asbefore,thebootstrapdis- factors—afactorof
tributionsarecenteredatthecorrespondingsamplemeans,but darddeviations,andusingtratherthannormalquantiles.Boot-
strappercentileintervalslackthesefactors,sotendtobetoonar-
nowthespreadsandshapesofthebootstrapdistributionsvary
substantially,becausethespreadsandshapesofthesamplesvary rowandunder-coverinsmallsamples.tintervalswithbootstrap
SEincludethet/zfactor,butsuffernarrownessbias.Someother
| substantially. | As a result, | bootstrap confidence | interval widths |     |     |     |     |
| -------------- | ------------ | -------------------- | --------------- | --- | --- | --- | --- |
varysubstantially(thisisalsotrueofstandardtconfidencein- bootstrapproceduresdobetter.ForStat101Isuggestwarning
tervals).Asbefore,theMonteCarlovariationissmallandmay students about the issue; for higher courses you may discuss
remedies(Hesterberg2004,2014).
bereducedwithmoreresamples.
Figure7. Bootstrapdistributionsforthemean,n=9.Theleftcolumnshowsthepopulationandfoursamples.Themiddlecolumnshowsthe
samplingdistributionforX¯,andbootstrapdistributionsofX¯∗foreachsample,withr =104.Therightcolumnshowsmorebootstrapdistributions
| forthefirstsample,threewithr |     | =1000andtwowithr | =104. |                                                  |     |     |     |
| ---------------------------- | --- | ---------------- | ----- | ------------------------------------------------ | --- | --- | --- |
|                              |     |                  |       | TheAmericanStatistician,November2015,Vol.69,No.4 |     |     | 377 |

In two-sample or stratified sampling situations, the narrow- few observations cannot do that. The right column shows the
nessbiasdependsontheindividualsampleorstratasizes.This smoothed bootstrap; it is better, though is still poor for this
| can result | in severe bias. | For example, | the U.K. Department | smalln. |     |     |     |
| ---------- | --------------- | ------------ | ------------------- | ------- | --- | --- | --- |
of Work and Pensions wanted to bootstrap a survey of wel- In spite of the inaccurate shape and spread of the bootstrap
fare cheating. They used a stratified sampling procedure that distributions,thebootstrappercentileintervalforthemedianis
resulted in two subjects in each stratum—so an uncorrected not bad (Efron 1982). For odd n, percentile interval endpoints
b√ootstrap standar√d error would be too small by a factor of fallononeoftheobservedvalues.Exactintervalendpointsalso
(n −1)/n = 1/2. fall on one of the observed values (order statistics), and for
| i   | i   |     |     |                |                     |          |                   |
| --- | --- | --- | --- | -------------- | ------------------- | -------- | ----------------- |
|     |     |     |     | a 95% interval | those are typically | the same | or adjacent order |
statisticsasthepercentileinterval.
3.3 SampleMedian
| Now turn | to Figure | 8, where the | statistic is the sample me- |     |     |     |     |
| -------- | --------- | ------------ | --------------------------- | --- | --- | --- | --- |
3.4 Mean–VarianceRelationship
dian.Herethebootstrapdistributionsarepoorapproximations
ofthesamplingdistribution.Thesamplingdistributioniscon- In many applications, the spread or shape of the sampling
tinuous, but the bootstrap distributions are discrete—for odd distributiondependsontheparameterofinterest.Forexample,
n the bootstrap sample median is always one of the original thebinomialdistributionspreadandshapedependonp.Simi-
observations—andwithwildlyvaryingshapes. larly, for an exponential distribution, the standard deviation of
|              |           |           |                          | thesamplingdistributionofx¯ | isproportionaltoμ. |     |     |
| ------------ | --------- | --------- | ------------------------ | --------------------------- | ------------------ | --- | --- |
| The ordinary | bootstrap | tends not | to work well for statis- |                             |                    |     |     |
tics such as the median or other quantiles in small samples Thismean–variancerelationshipisreflectedinbootstrapdis-
that depend heavily on a small number of observations out of tributions. Figure 9 shows samples and bootstrap distributions
a larger sample. The bootstrap depends on the sample accu- foranexponentialpopulation.Thereisastrongdependencebe-
rately reflecting what matters about the population, and those tweenx¯ andthecorrespondingbootstrapSE.Thisrelationship
Figure8. Bootstrapdistributionsforthemedian,n=15.Theleftcolumnshowsthepopulationandfoursamples.Themiddlecolumnshows
thesamplingdist√ribution,andbootstrapdistributionsforeachsample,withr =104.Therightcolumnshowssmoothedbootstrapdistributions,
| withkernelsds/ | nandr | =104. |     |     |     |     |     |
| -------------- | ----- | ----- | --- | --- | --- | --- | --- |
378 StatisticsandtheUndergraduateCurriculum

Bootstrapdistributionsforthemean,n=50,exponentialpopulation.Theleftcolumnshowsthepopulationandfivesamples.(These
Figure9.
samplesareselectedfromalargersetofrandomsamples,tohavemeansspreadacrosstherangeofsamplemeans,andaveragestandarddeviations
conditionalonthemeans.)Themiddlecolumnshowsthesamplingdistributionandbootstrapdistributionsforeachsample.Therightcolumn
showsbootstrapt-distributions.
hasimportantimplicationsforconfidenceintervals;procedures 3.5 SummaryofVisualLessons
thatignoretherelationshipareinaccurate.Wediscussthismore
Thebootstrapdistributionreflectstheoriginalsample.Ifthe
inSection4.5.
sampleisnarrowerthanthepopulation,thebootstrapdistribu-
| There           | are other applications |     | where        | sampling distributions |      |                  |                   |               |           |     |
| --------------- | ---------------------- | --- | ------------ | ---------------------- | ---- | ---------------- | ----------------- | ------------- | --------- | --- |
|                 |                        |     |              |                        |      | tion is narrower | than the sampling | distribution. | Typically | for |
| depend strongly | on the parameter,      |     | for example, | sampling               | dis- |                  |                   |               |           |     |
largesamplesthedatarepresentthepopulationwell;forsmall
tributionsforchi-squaredstatisticsdependonthenoncentrality
|            |                  |               |     |                    |     | samples they | may not. Bootstrapping | does | not overcome | the |
| ---------- | ---------------- | ------------- | --- | ------------------ | --- | ------------ | ---------------------- | ---- | ------------ | --- |
| parameter. | Use caution when | bootstrapping |     | such applications; |     |              |                        |      |              |     |
weaknessofsmallsamplesasabasisforinference.Indeed,for
| the bootstrap | distributionmay | be  | very differentfromthe |     | sam- |                   |                 |              |                 |     |
| ------------- | --------------- | --- | --------------------- | --- | ---- | ----------------- | --------------- | ------------ | --------------- | --- |
|               |                 |     |                       |     |      | the very smallest | samples, it may | be better to | make additional |     |
plingdistribution.
assumptionssuchasaparametricfamily.
| Here there | is a bright | spot. The | right | column of | Figure | 9   |     |     |     |     |
| ---------- | ----------- | --------- | ----- | --------- | ------ | --- | --- | --- | --- | --- |
Lookingahead,twothingsmatterforaccurateinferences:
| shows the | sampling distribution |     | and bootstrap | distributions | of  |     |     |     |     |     |
| --------- | --------------------- | --- | ------------- | ------------- | --- | --- | --- | --- | --- | --- |
thetstatistic,Equations(1)and(2).Thesedistributionsaremuch
less sensitive to the original sample. We use these bootstrap t • howclosethebootstrapdistributionistothesamplingdistri-
distributionsbelowtoconstructaccurateconfidenceintervals. bution(thebootstrapthasanadvantage,seeFigure9);
|     |     |     |     |     |     |     | TheAmericanStatistician,November2015,Vol.69,No.4 |     |     | 379 |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |

• how well the procedures allow for variation in samples, for for the estimated Gˆ(q) to fall between 2.25% and 2.75% with
example,byusingfudgefactors. 95%probabilityrequiresr ≥14,982.
Forat intervalwithbootstrapSE,r shouldbelargeenough
Another visual lesson is that random sampling using that variation in s b has a similar small effect on coverage. For
only 1000 resamples causes more random variation in the large n and an approximately normal bootstrap distribution,
bootstrap distributions. Let us consider this issue more
aboutr ≥5000suffices(Hesterberg2014).
carefully. Rounding up, we need r ≥15,000 to have 95% probability
of being within 10%, for permutation tests and percentile and
bootstrap t confidence intervals, and r ≥5000 for the t with
3.6 HowManyBootstrapSamples
bootstrapSE.Whilestudentsmaynotneedthislevelofaccuracy,
Isuggestedaboveusing1000bootstrapsamplesforroughap- itisgoodtogetinthehabitofdoingaccuratesimulations.Hence,
proximations,or104 ormoreforbetteraccuracy.Thisisabout Irecommend104forroutineuse.Inpractice,iftheresultswith
MonteCarloaccuracy—howwelltheusualMonteCarloimple- r =104 are borderline, then we can increase r to reduce the
mentation of the bootstrap approximates the theoretical boot- Monte Carlo error. We want decisions to depend on the data,
strap distribution. A bootstrap distribution based on r random not random variation in the Monte Carlo implementation. We
samples corresponds to drawing r observations with replace- usedr =500,000intheVerizonproject.
mentfromthetheoreticalbootstrapdistribution. Students can do multiple runs with different r, to see how
BradEfron,inventorofthebootstrap,suggestedin1993that the results vary. They should develop some intuition into how
r =200,orevenasfewasr =25,sufficesforestimatingstan-
results vary with different r; this intuition is valuable not only
darderrorsandthatr =1000isenoughforconfidenceintervals
forresampling,butforgeneralunderstandingofhowestimates
(EfronandTibshirani1993). varyfordifferentn.
I argue that more resamples are appropriate. First, comput-
ersarefasternow.Second,thosecriteriaweredevelopedusing
arguments that combine variation due to the original random 4. CONFIDENCEINTERVALS
sample with the extra variation from the Monte Carlo imple-
mentation.Iprefertotreatthedataasgivenandlookjustatthe In this section, I describe a number of confidence intervals,
variabilityduetotheimplementation.Twopeopleanalyzingthe andcomparetheirpedagogicalvalueandaccuracy.
samedatashouldnotgetsubstantiallydifferentanswersdueto A hypothesis test or confidence interval is first-order accu-
MonteCarlovariation. rateiftheactualone-sidedrejectionprobabilitiesorone-sided
noncoverage probabilities differ from the nominal values by
Quantifyaccuracybyformulasorbootstrapping. Wecanquan- O(n−1/2). It is second-order accurate if the differences are
tifytheMonteCarlovariationintwoways—usingformulas,or O(n−1).
bybootstrapping.Forexample,letGbethecdfofatheoretical
bootstrap distribution and Gˆ the Monte Carlo approximation,
thenthevarianceofGˆ(x)isG(x)(1−G(x))/r,whichweesti- 4.1 Statistics101—Percentile,andtwithBootstrapSE
mateusingGˆ(x)(1−Gˆ(x))/r.
ForStat101,Iwouldstickwiththetwoquick-and-dirtyinter-
Similarly, a bootstrap bias estimate is a mean of r random
valsmentionedearlier:thebootstrappercentileinterval,andthe
v fo a r lu th es e m bi i a n s u i s s a s b c / o√ns r ta , n w t, h θ e ˆ∗ re − s b θˆ i ; s th th e e M sa o m nt p e le C s a t r a lo nd s a ta rd nd d a e r v d ia e t r i r o o n r w ti a n r t e er t v h a a l t w pr it o h vi b d o e o s ts i t t r , a y p o s u ta m n a d y ar a d ls e o rr u o s r e θˆ t ± he t b α/ o 2 o s t b s . tr I a f p us t in in g te s r o v f a t- l
ofthebootstrapdistribution.
describedbelow.Thepercentileintervalwillbemoreintuitive
Wecanalsobootstrapthebootstrapdistribution!Therboot-
forstudents.Thetwithbootstrapstandarderrorhelpsthemlearn
strap statistics are an iid sample from the exhaustive boot-
formulamethods.Studentscancomputebothandcompare.
strap distribution; we can bootstrap that sample. For example,
Neither interval is very accurate. They are only first-order
the 95% percentile confidence interval for the CLEC data is
accurate, and are poor in small samples—they tend to be too
(10.09,25.41);theseare2.5%and97.5%quantilesoftheboot-
n√arrow. The bootstrap standard error is too small, by a factor
strap distribution; r =104. To estimate the accuracy of those (n−1)/nsothetintervalwithbootstrapSEistoonarrowby
quantiles,wedraw resamples ofsizer fromthebootstrap dis-
thatfactor,thisis,thenarrownessbiasdiscussedinSection3.2.
tributionandcomputethequantilesforeachresample.There-
The percentile interval suffers the same narr√owness and
sultingSEsforthequantileestimatesare0.066and0.141.
more—for s√ymmetric data it is like using z α/2 σˆ/ n in place
Need r ≥ 15,000 to be within 10%. Next we determine how oft α/2,n−1 s/ n.Randomvariabilityinhowskewedthedataare
largershouldbeforaccurateresults,beginningwithtwo-sided alsoaddsvariabilitytotheendpoints,furtherreducingcoverage.
testswithsize5%.Supposethetrueone-sidedp-valueis0.025, These effects are O(n−1) (effect on coverage probability) or
and we want the estimated p-value to be within 10% of that, smaller,sotheybecomenegligiblefairlyquicklyasnincreases.
between0.0225and0.0275.T(cid:7)ohavea95%probabilityofbeing But they matter for small n, see Figure 10. The interval also
that close requires that 1.96 0.025·0.975/r <0.025/10, or hasO(n−1/2)errors—becauseitonlymakesapartialskewness
r ≥14,982. Similar results hold for a bootstrap percentile or correction,seeSection4.5.
bootstraptconfidenceinterval.Ifqisthetrue2.5%quantileof In practice, the t with bootstrap standard error offers no ad-
thetheoreticalbootstrapdistribution(forθˆ∗ort∗,respectively), vantage over a standard t procedure for the sample mean. Its
380 StatisticsandtheUndergraduateCurriculum

=P(δˆ∗
|     |     |     |     |     |     | is,α | ≤q           | α).Then |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------ | ------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |      | α/2=P(θˆ∗−θˆ |         | <q  |     |     |     |     |
α/2 )
|     |     |     |     |     |     |     | ≈P(θˆ−θ |     | <q  | )=P(θˆ−q |     | <θ). |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | -------- | --- | ---- | --- |
|     |     |     |     |     |     |     |         |     | α/2 |          | α/2 |      |     |
Similarlyfortheothertail.Theresultingconfidenceintervalis
|     |     |     |     |     |     | (θˆ−q |       | ,θˆ−q | )=(2θˆ−Q |     | ,2θˆ−Q |     | ), (3) |
| --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | -------- | --- | ------ | --- | ------ |
|     |     |     |     |     |     |       | 1−α/2 |       | α/2      |     | 1−α/2  | α/2 |        |
isthequantileofthebootstrapdistributionofθˆ∗.
|     |     |     |     |     |     | whereQ | α        |               |       |     |               |            |     |
| --- | --- | --- | --- | --- | --- | ------ | -------- | ------------- | ----- | --- | ------------- | ---------- | --- |
|     |     |     |     |     |     | This   | interval | is the mirror | image | of  | the bootstrap | percentile |     |
θˆ
|     |     |     |     |     |     | interval; | it reaches | as     | far above    | as       | the bootstrap | percentile   |     |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------ | ------------ | -------- | ------------- | ------------ | --- |
|     |     |     |     |     |     | interval  | reaches    | below. | For example, |          | for the CLEC  | mean,        | the |
|     |     |     |     |     |     |           |            | 16.5,  |              |          |               | (10.1,25.4)= |     |
|     |     |     |     |     |     | sample    | mean is    | the    | percentile   | interval | is            |              |     |
16.5+(−6.4,8.9),andthereversepercentileintervalis16.5+
(−8.9,6.4)=2·16.5−(25.4,10.1)=(7.6,22.9).
Reversingworkswellforapuretranslationfamily,butthose
arerareinpractice.MorecommonarecaseslikeFigure9,where
thespreadofthebootstrapdistributiondependsonthestatistic.
Thenagoodintervalneedstobeasymmetricinthesamedirec-
tionasthedata,seeSection4.5.Thereversepercentileinterval
isasymmetricalinthewrongdirection!Itscoverageaccuracyin
Figure10isterrible.Italsosuffersfromthesamesmall-sample
narrownessissuesasthepercentileinterval.
| Figure10. | Confidenceintervalone-sidedmissprobabilitiesfornor- |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hall(1992)calledthebootstrappercentileinterval“thewrong
| mal and exponential | populations. |     | 95% confidence | interval, | the ideal |     |     |     |     |     |     |     |     |
| ------------------- | ------------ | --- | -------------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
pivot,backward”;thereversepercentileintervalusesthatsame
noncoverageis2.5%oneachside.Theintervalsaredescribedatthe
wrongpivotinreverse.δˆisthewrongpivotbecauseitisnoteven
beginningofSection4.4.Forthenormalpopulationnoncoverageprob-
abilitiesarethesameonbothsides,andthereversepercentileinterval closetopivotal—apivotalstatisticisonewhosedistributionis
isomitted(ithasthesamecoverageasthepercentileinterval).Forthe independent of the parameter. A t statistic is closer to pivotal;
exponentialpopulation,curveswithlettersarenoncoverageprobabil- thisleadsustothenextinterval.
θ,
| ities on the | right, where the | interval | is below | and curves | without |     |     |     |     |     |     |     |     |
| ------------ | ---------------- | -------- | -------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
letterscorrespondtotheleftside.
|     |     |     |     |     |     | 4.3 BootstraptInterval |                |     |            |                 |         |               |        |
| --- | --- | --- | --- | --- | --- | ---------------------- | -------------- | --- | ---------- | --------------- | ------- | ------------- | ------ |
|     |     |     |     |     |     | We                     | saw in Section |     | 1.4 that   | the t statistic | does    | not           | have a |
|     |     |     |     |     |     | t-distribution         | when           | the | population | is              | skewed. | The bootstrap | t      |
advantagesarepedagogical,andthatitcanbeusedforstatistics
confidenceintervalisbasedonthetstatistic,butestimatesquan-
thatlackeasystandarderrorformulas. tilesoftheactualdistributionusingthedataratherthanatable.
| The percentile | interval     | is not   | a good alternative | to standard |         |       |                |        |        |      |             |           |     |
| -------------- | ------------ | -------- | ------------------ | ----------- | ------- | ----- | -------------- | ------ | ------ | ---- | ----------- | --------- | --- |
|                |              |          |                    |             |         | Efron | and Tibshirani | (1993) | called | this | “Confidence | intervals |     |
| t intervals    | for the mean | of small | samples—while      | it          | handles |       |                |        |        |      |             |           |     |
basedonbootstraptables”—usingthebootstraptogeneratethe
skewedpopulationsbetter,itislessaccurateforsmallsamples
|         |                   |                 |              |     |          | right table | for | an individual | dataset, | rather | than | using | a table |
| ------- | ----------------- | --------------- | ------------ | --- | -------- | ----------- | --- | ------------- | -------- | ------ | ---- | ----- | ------- |
| because | it is too narrow. | For exponential | populations, |     | the per- |             |     |               |          |        |      |       |         |
fromabook.Thishasthebestcoverageaccuracyofallintervals
t
| centile interval | is less accurate |     | than the standard | interval | for | inFigure10. |     |     |     |     |     |     |     |
| ---------------- | ---------------- | --- | ----------------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
n≤34.
t∗
|     |     |     |     |     |     | We  | assume | that the | distribution | of  | is approximately |     | the |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------------ | --- | ---------------- | --- | --- |
InStat101,itmaybebesttoavoidthesmall-sampleproblems
|     |     |     |     |     |     | same | as the distribution |     | of t (Equations |     | (1) and | (2)); the | right |
| --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | --------------- | --- | ------- | --------- | ----- |
byusingexampleswithlargern.Alternately,somesoftwarecor- columnofFigure9suggeststhatthisassumptionholds,thatis,
| rectsforthesmall-sampleproblems,forexample,theresample |     |     |     |     |     |               |     |          |          | q     | α      |          |        |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- | -------- | -------- | ----- | ------ | -------- | ------ |
|                                                        |     |     |     |     |     | the statistic | is  | close to | pivotal. | Let α | be the | quantile | of the |
package(Hesterberg2015)includestheexpandedpercentilein-
bootstrapt-distribution,then
terval(Hesterberg1999,2014)apercentileintervalwithfudge (cid:8) (cid:9)
| factorsmotivatedbystandardtintervals. |     |     |     |     |     |     |       | θˆ∗−θˆ |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- |
|                                       |     |     |     |     |     |     | α/2=P |        | <q  |     |     |     |     |
α/2
SE∗
|     |     |     |     |     |     |     |     | (cid:8) |     | (cid:9) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- |
4.2 ReverseBootstrapPercentileInterval
θˆ−θ
|     |     |     |     |     |     |     | ≈P  |     | <q  | =P(θˆ−q |     | SE<θ). |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- |
Thereversebootstrappercentileinterval(called“basicboot- α/2 α/2
SE
| strap confidence | interval” | in Davison | and Hinkley | 1997) | is  | a   |     |     |     |     |     |     |     |
| ---------------- | --------- | ---------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Similarlyfortheothertail.Theresultingconfidenceintervalis
| common | interval, with pedagogical |     | value in | teaching | manipu- |     |     |     |     |     |     |     |     |
| ------ | -------------------------- | --- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
lationslikethoseshownjustbelow.Butitispoorinpractice;I (θˆ−q SE,θˆ−q SE).
|     |     |     |     |     |     |     |     |     | 1−α/2 | α/2 |     |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
includeitheretohelpfacultyandstudentsunderstandwhyand
Notethatendpointsarereversed:wesubtractanupperquantile
todiscourageitsuse.
Itisbasedonthedistributionofδˆ =θˆ−θ.Weestimatethe of the bootstrap t-distribution to get the lower endpoint of the
δˆ δˆ∗ =θˆ∗−θˆ. interval,andtheconverse(thisreversaliseasytooverlookwith
| CDF of | using the bootstrap | distribution | of  |     | Let |     |     |     |     |     |     |     |     |
| ------ | ------------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
δˆ∗,
q α be the α quantile of the bootstrap distribution of that standardtintervalsduetosymmetry).
|     |     |     |     |     |     |     | TheAmericanStatistician,November2015,Vol.69,No.4 |     |     |     |     |     | 381 |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |

4.4 ConfidenceIntervalAccuracy three times as asymmetrical in the case of a 95% intervals for
amean(Hesterberg2014).Thebootstraptexplicitlyestimates
| Next | we compare | the | accuracy | of  | the different |     | confidence |          |          |     |        |          |                 |     |            |
| ---- | ---------- | --- | -------- | --- | ------------- | --- | ---------- | -------- | -------- | --- | ------ | -------- | --------------- | --- | ---------- |
|      |            |     |          |     |               |     |            | how many | standard |     | errors | to go in | each direction. |     | This table |
intervals:
|     |     |     |     |     |     |     |     | shows | how far | the endpoints |     | for the | t, percentile, | reverse | per- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------------- | --- | ------- | -------------- | ------- | ---- |
t=t:ordinarytinterval; centile,andbootstraptintervalsareaboveandbelowthesample
B=tBoot:tintervalwithbootstrapstandarderror;
meanoftheVerizonILECdata:
p=perc:bootstrappercentileinterval;
r=reverse:reversepercentileinterval;
=bootT:bootstrapt.
| T     |     |           |             |          |          |     |        |     |       |        | t Reverse | Percentile |     | bootstrapT |     |
| ----- | --- | --------- | ----------- | -------- | -------- | --- | ------ | --- | ----- | ------ | --------- | ---------- | --- | ---------- | --- |
|       |     |           |             |          |          |     |        |     | 2.5%  | −0.701 | −0.718    | −0.683     |     | −0.646     |     |
| For a | 95% | interval, | a perfectly | accurate | interval |     | misses | the |       |        |           |            |     |            |     |
|       |     |           |             |          |          |     |        |     | 97.5% | 0.701  | 0.683     | 0.718      |     | 0.762      |     |
parameter2.5%ofthetimeoneachside.Figure10showsactual
|                      |               |     |        |          |                 |     |          |     | -ratio | 1   | 0.951 | 1.050 |     | 1.180 |     |
| -------------------- | ------------- | --- | ------ | -------- | --------------- | --- | -------- | --- | ------ | --- | ----- | ----- | --- | ----- | --- |
| noncoverage          | probabilities |     | for    | normal   | and exponential |     | popula-  |     |        |     |       |       |     |       |     |
| tions, respectively. |               | The | figure | is based | on extremely    |     | accurate |     |        |     |       |       |     |       |     |
Thebootstrappercentileintervalisasymmetricalintheright
simulations,seetheappendix.
direction,butfallsshort;thereversepercentileintervalgoesthe
| Normal | population. | The | percentile |     | interval | (“p” | on the | plot) |     |     |     |     |     |     |     |
| ------ | ----------- | --- | ---------- | --- | -------- | ---- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
wrongway.
doespoorly.Itcorrespondstousingzinsteadoft,usingadivisor Forright-skeweddata,youmaybesurprisedthatgoodcon-
ofninsteadofn−1whencalculatingSE,anddoingapartial
|     |     |     |     |     |     |     |     | fidence | intervals | are | 3x as | asymmetrical | as  | the bootstrap | per- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ----- | ------------ | --- | ------------- | ---- |
correctionforskewness;sincethesampleskewnessisrandom centileinterval;Youmayevenbeinclinedto“downweightthe
| this adds | variability. | For | normal | data | the skewness |     | correction |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------ | ---- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
outliers,”anduseanintervalthatreachesfartherleft;thereverse
doesnothelp,andtheotherthreethingskillitforsmallsamples.
|     |     |     |     |     |     |     |     | percentile | interval | does | so, | with catastrophic |     | effect. | Instead, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | --- | ----------------- | --- | ------- | -------- |
Thereversepercentileintervalissimilarlypoor,withexactlythe thinkofitthisway:thedatashowthatthepopulationisskewed,
samecoveragefornormalpopulations.
takethatasgiven;wemayhaveobservedtoofewobservations
ThetintervalwithbootstrapSE(“B”)doessomewhatbetter,
fromthelongrighttail,sotheconfidenceintervalneedstoreach
| though | still under-covers. |     | The | t interval | (“t”) | and | bootstrap | t   |     |     |     |     |     |     |     |
| ------ | ------------------- | --- | --- | ---------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
fartotherighttoprotectagainstthat—many(small)SE’stothe
(“T”)intervaldoverywell.Thatisnotsurprisingforthetinter-
right.
| val, which | is optimized |     | for this | population, |     | but the | bootstrap | t   |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | -------- | ----------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
doesextremelywell,evenforverysmallsamples.
4.6 ConfidenceIntervalDetails
| Exponentialpopulation. |     |     | Thisisaharderproblem.Allintervals |     |           |     |           |       |               |     |      |            |           |        |     |
| ---------------------- | --- | --- | --------------------------------- | --- | --------- | --- | --------- | ----- | ------------- | --- | ---- | ---------- | --------- | ------ | --- |
|                        |     |     |                                   |     |           |     |           | There | are different |     | ways | to compute | quantiles | common | in  |
| badly under-cover      |     | on  | the right—the                     |     | intervals | are | too short | on    |               |     |      |            |           |        |     |
statisticalpractice.Forintervalsbasedonquantilesoftheboot-
therightside—andover-cover(bysmalleramounts)ontheleft.
|                |     |        |      |          |            |     |            | strap distribution, |     | I recommend |     | letting | the | kth largest | value in |
| -------------- | --- | ------ | ---- | -------- | ---------- | --- | ---------- | ------------------- | --- | ----------- | --- | ------- | --- | ----------- | -------- |
| (Over-covering |     | on one | side | does not | compensate |     | for under- |                     |     |             |     |         |     |             |          |
(k+1)/r
|     |     |     |     |     |     |     |     | the bootstrap |     | distribution | be  | the |     | quantile, | and inter- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | --- | --- | --------- | ---------- |
coveringontheother—instead,havingbothendpointstoolow
|          |      |             |         |       |       |     |           | polating    | for other | quantiles.                                 |     | In R (R | Core | Team 2014) | this is |
| -------- | ---- | ----------- | ------- | ----- | ----- | --- | --------- | ----------- | --------- | ------------------------------------------ | --- | ------- | ---- | ---------- | ------- |
| gives an | even | more biased | picture | about | where | the | parameter |             |           |                                            |     |         |      |            |         |
|          |      |             |         |       |       |     |           | quantile(x, |           | type=6).Otherdefinitionsgivenarrowerinter- |     |         |      |            |         |
maybethanhavingjustoneendpointtoolow.)
vals,andexacerbatetheproblemofintervalsbeingtooshort.
| The bootstrap |     | t interval |     | (“T”) does | best, | by a | substantial |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ---------- | ----- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Bootstraptintervalsrequirestandarderrors—fortheoriginal
| margin. | Itissecond-order |     | accurate, |     | and gives | coverage | within |     |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | --------- | --- | --------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
10%forn≥101.Theotherintervalsareallpoor.Thereverse sample,andeachbootstrapsample.WhenformulaSE’sarenot
available,wecanusethebootstraptoobtaintheseSE’s(Efron
| percentile | interval | (“r”) | is the | worst. | The | percentile | interval |     |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | ------ | ------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andTibshirani1993),usinganiteratedbootstrap,inwhichaset
| (“p”) is | poor for | small | samples, | but | better than | the | ordinary | t   |     |     |     |     |     |     |     |
| -------- | -------- | ----- | -------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofsecond-levelbootstrapsamplesisdrawnfromeachtop-level
(“t”)forn≥35.Toreach10%accuracyrequiresn≥2383for
bootstrapsampletoestimatetheSEforthatbootstrapsample.
percentile,4815forordinaryt,5063fortwithbootstrapstandard
|     |     |     |     |     |     |     |     |               |     | r +rr |           | r    |        |               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | --------- | ---- | ------ | ------------- | --- |
|     |     |     |     |     |     |     |     | This requires |     | 2     | resamples | if 2 | second | level samples | are |
errors,andover8000forthereversepercentilemethod.
drawnfromeachtop-levelsample.Thecomputationalcosthas
|     |     |     |     |     |     |     |     | been an | impediment, |     | but should | be  | less | so in the | future as |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ---------- | --- | ---- | --------- | --------- |
4.5 SkewnessandMean–VarianceRelationship
computersmakeuseofmultipleprocessors.
Take another look at Figure 9, for the sample mean from While the simulation results here are for the sample mean,
thebootstraptissecond-orderaccurateandtheothersarefirst-
| a skewed | population. |     | Note | how the | spread | of the | bootstrap |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ---- | ------- | ------ | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
distributionforx¯∗dependsonthestatisticx¯.Toobtainaccurate
|     |     |     |     |     |     |     |     | order accurate |     | under | quite | general | conditions, | see | Efron and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ----- | ------- | ----------- | --- | --------- |
confidence intervals, we need to allow for such a relationship Tibshirani (1993) and Davison and Hinkley (1997). Efron and
(andMathematicalStatisticsstudentsshouldbeawareofthis). Tibshirani(1993)notedthatthebootstraptisparticularlysuited
For positively skewed populations, when x¯ <μ the sample to location statistics like the sample mean, median, trimmed
standard deviation and bootstrap SE also tend to be small, so mean,orpercentiles,butperformspoorlyforacorrelationco-
a confidence interval needs to reach many (small) SE’s to the efficient;theyobtainamodifiedversionbyusingabootstrapt
righttoavoidmissingμtoooften.Conversely,whenx¯ >μ,s foratransformedversionofthestatisticψ =h(θ),wherehisa
ands variance-stabilizingtransformation(sothatvar(ψˆ)doesnotde-
| b tendtobelarge,soaconfidence |     |     |     |     | intervaldoesnotneed |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toreachmany(large)SE’stothelefttoreachμ. pendonψ)estimatedusingacreativeuseofthebootstrap.The
In fact, a good interval, like the bootstrap t interval, is even samemethodimprovesthereversepercentileinterval(Davison
moreasymmetricalthanabootstrappercentileinterval—about andHinkley1997).
382 StatisticsandtheUndergraduateCurriculum

| 4.7 BootstrapHypothesisTesting |     |     |     |     |     |     |     |     | 5.  | REGRESSION |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
Therearetwobroadapproachestobootstraphypothesistest-
|     |     |     |     |     |     |     | There | are | two ways | that bootstrapping | in  | regression | is par- |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | ------------------ | --- | ---------- | ------- |
ing.Oneapproachistoinvertaconfidenceinterval—rejectH
|     |     |     |     |     |     | 0 if | ticularly | useful | pedagogically. | The | first is to | help students | un- |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ------ | -------------- | --- | ----------- | ------------- | --- |
thecorrespondingintervalexcludesθ . derstandthevariabilityofregressionpredictionsbyagraphical
0
Anotherapproachistosampleinawaythatisconsistentwith
|     |     |     |     |     |     |     | bootstrap. |     | For example, | in Figure | 11 we bootstrap |     | regression |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --------- | --------------- | --- | ---------- |
H
,thencalculateap-valueasatailprobability.Forexample, lines; those lines help students understand the variability of
0
| we could | perform | a two-sample | bootstrap | test | by pooling | the |     |     |     |     |     |     |     |
| -------- | ------- | ------------ | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
slopeandinterceptcoefficients,andofpredictionsateachvalue
|     |     |     |     |     | n   | n   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
data and drawing bootstrap samples of size 1 and 2 with ofx.Themoreweextrapolateineitherdirection,themorevari-
replacementfromthepooleddata.However,thisbootstraptest ablethepredictionsbecome.Abootstrappercentileconfidence
isnotasaccurateasthepermutationtest.Suppose,forexample, E(Y|x)
|     |     |     |     |     |     |     | interval | for | is  | the range of | the middle | 95% | of the y |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------------ | ---------- | --- | -------- |
that the data contain three outliers. The permutation test tells valuesforregressionlinesatanyx;theseintervalsarewiderfor
| howcommontheobservedstatisticis,giventhethreeoutliers. |           |     |            |             |       |       | moreextremex. |     |     |     |     |     |     |
| ------------------------------------------------------ | --------- | --- | ---------- | ----------- | ----- | ----- | ------------- | --- | --- | --- | --- | --- | --- |
| With a pooled                                          | bootstrap |     | the number | of outliers | would | vary. |               |     |     |     |     |     |     |
Thesecondistohelpstudentsunderstandthedifferencebe-
Thepermutationtestconditionsonthedata,treatingonlygroup tweenconfidenceandpredictionintervals.Intheleftpanel,we
assignmentasrandom.
seethatthevariabilityofindividualobservationsismuchlarger
Anotherexample,foraone-samplemean,istotranslatethe thanthevariabilityoftheregressionlines;confidenceintervals
data, subtracting x¯ −μ from each x so the translated mean based on the lines would capture only a small fraction of ob-
|             |          | 0    |                | i     |         |         |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | -------------- | ----- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| is μ , then | resample | from | the translated | data. | This is | equiva- |     |     |     |     |     |     |     |
0 servations. To capture observations, prediction intervals must
lent to inverting a reverse percentile confidence interval, with be much wider, and should approximate the quantiles of the
| corresponding | inaccuracy |     | for skewed | data. It | can also | yield |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | ---------- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
residualdistribution,becausetheyareprimarilyintervalsforin-
impossible data, like negative values for data that must be dividualobservations—noCLTappliesforpredictionintervals.
positive. The bootstrap estimates the performance of the model that
Translationmodifiesadistributionbymodifyingthevalues.
wasactuallyfittothedata,regardlessofwhetherthatisapoor
Abetterwaytomodifyadistributionistokeepthesamevalues, model. In the right panel of Figure 11, a linear approximation
| but change | the probabilities |     | on those | values, | using bootstrap |     |     |           |        |                  |               |     |           |
| ---------- | ----------------- | --- | -------- | ------- | --------------- | --- | --- | --------- | ------ | ---------------- | ------------- | --- | --------- |
|            |                   |     |          |         |                 |     | was | used even | though | the relationship | is quadratic; |     | the boot- |
tilting(Efron1981;DavisonandHinkley1997);empiricallike- strapmeasuresthevariabilityofthelinearapproximation,and
lihood(Owen2001)isrelated.Tiltingpreservesmean–variance estimatesthebiasof(alinearapproximationtothedata)asan
| relationships. | I believe | tilting | has great | pedagogical | potential |     |     |     |     |     |     |     |     |
| -------------- | --------- | ------- | --------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
estimateof(alinearapproximationtothepopulation).Theboot-
for mathematical statistics; it nicely connects parametric and strapfindsnobias—foranyx,thebootstraplinesarecentered
| nonparametric | statistics, |     | can help students | understand |     | the re- |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | ----------------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
verticallyaroundtheoriginalfit.
lationshipbetweenparametersandsamplingdistributions,and
better understand confidence intervals. See the online supple- 5.1 ResampleObservationsorConditionalDistributions
mentforanexample.Butsuitablesoftwareforeducationaluse
Twocommonprocedureswhenbootstrappingregressionare
isnotcurrentlyavailable.
| Neitherapproachisasaccurateaspermutationtests,insitua- |     |     |     |     |     |     | •   |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bootstrapobservations,and
tionswherepermutationtestscanbeused.Theactualone-sided
• bootstrapresiduals.
rejectionprobabilitieswheninvertingconfidenceintervalscor-
respond to Figure 10. In contrast, permutation tests are nearly Thelatterisaspecialcaseofamoregeneralrule:
| exact. |     |     |     |     |     |     | •   |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resampleyfromitsestimatedconditionaldistributiongivenx.
Figure 11. Bootstrapping linear regression. Left: Linear regression linear model fits. At any x, the y values from the bootstrap lines form
a bootstrap distribution that may be used for standard errors or confidence intervals. Prediction intervals are wider, to capture individual
observations.Right:Fittingalinearrelationshiptodatathatarenotlinear;thebootstrapdoesnotdiagnosethepoorfit.
|     |     |     |     |     |     |     |     |     | TheAmericanStatistician,November2015,Vol.69,No.4 |     |     |     | 383 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |

In bootstrapping observations, we sample with replacement playsinstatistics.Studentscanusefamiliartoolslikehistograms
fromtheobservations,keepingyandcorrespondingx’stogether. to visualize sampling distributions and standard errors. They
In any bootstrap sample some observations may be repeated mayunderstandthatanSEisthestandarddeviationofasam-
multipletimes,andothersnotincluded. plingdistribution.Studentscanworkdirectlywithestimatesof
Inbootstrappingresiduals,wefitaregressionmodel,compute interest, like sample means, instead of t statistics, and use the
predicted values yˆi and residuals e i =y i −yˆi, then create a samebasicprocedureformanydifferentstatisticswithoutnew
bootstrap sample using the same x values as in the original formulas. Robust statistics like medians and trimmed means
data,butwithyobtainedbyaddingthepredictionsandrandom can be used throughout the course. Students can focus on the
residuals, y
i
∗ =yˆi +e
i
∗, where e
i
∗ are sampled randomly with ideas,notformulas.Whenlearningformulas,theycancompare
replacementfromtheoriginalresiduals. formulaandbootstrapanswers.Graphicalbootstrappingforre-
Bootstrappingresidualscorrespondtoadesignedexperiment gression demonstrates the variation in regression predictions,
wherethex’sarefixedandonlyyisrandom,andbootstrapping andthedifferencebetweenconfidenceandpredictionintervals.
observationstorandomlysampleddatawherebothxandyare Understandingthekeyideabehindthebootstrap—sampling
sampledfromajointdistribution.Bytheprincipleofsampling from an estimate of the population—is important to use the
thewaythedataweredrawn,wewouldbootstrapobservations bootstrap appropriately, and helps to understand when it may
if the x’s were random. Alternately, we can follow the prece- notworkwell,orwhichmethodsmayworkbetter.Whenusing
dentsetbythecommonformulaapproach,whereformulasare MonteCarlosampling,enoughsamplesshouldbeusedtoobtain
derivedassumingthex’sarefixed,andinpracticeweusethese accurateanswers—10,000isgoodforroutineuse.Studentscan
even when the x’s are random. In doing so we condition on gaininsightintosamplingvariationbytryingdifferentnumbers.
theobservedx’s,andhenceontheobservedinformation(inre- Bootstrap distributions and percentile confidence intervals
gressiontheinformationdependsonthespreadofthex’s—the tendtobetoonarrow,particularlyforsmallsamples.Asaresult,
widerthespread,thelessβˆvaries).Similarly,inbootstrapping, percentile intervals are less accurate than common t intervals
we may resample the residuals, conditioning on the observed for small samples, though more accurate for larger samples.
x’s. Mostaccuratearebootstraptintervals.Thereasonrelatestothe
Fixing the x’s can make a big difference in practice; boot- fundamentalideaofthebootstrap—toreplacethepopulationby
strappingobservationscanbedangerous.Forexample,suppose an estimate of the population, then use the resulting bootstrap
oneofthex’sisafactorvariablewithararelevel,sayonlyfive distribution as an estimate of the sampling distribution. This
observations. When resampling observations, about 67 out of substitution is more accurate for a pivotal statistic—and the
10,000 samples omit those five observations entirely; then the tstatisticisclosetopivotal.
regressionsoftwarecannotestimateacoefficientforthatlevel. Forskeweddata,confidenceintervalsshouldreachlongerin
Worse,manysampleswillincludejustoneortwoobservations thedirectionoftheskewness;thebootstraptdoesthiswell,the
fromthatlevel;thenthesoftwareproducesestimateswithhigh percentilemakesabout1/3ofthatcorrection,tintervalsignore
variance, with no error message to flag the problem. Similar skewness,andreversepercentileintervalsgothewrongway.
problemsoccurinmodelswithinteractions(cid:3),orwithcontinuous We generally sample the way the data were produced (e.g.,
variables when some linear combination c j x j has most of simple random or stratified sampling), except to condition on
itsvariationinasmallnumberofobservations.Weavoidthese observed information. For regression, that means to fix the x
problemsbybootstrappingresiduals. values, that is, to resample residuals rather than observations.
Bootstrapping residuals is a special case of a more general Thisavoidsproblemsinpractice.
rule, to sample Y from its estimated conditional distribution To reach the full potential of bootstrapping in practice and
given X. For example, when bootstrapping logistic regression, education,weneedbettersoftwareandinstructionalmaterials.
wefitthemodel,andcalculatepredictedvaluesyˆi =Eˆ(Y|X = Software such as https://www.stat.auckland.ac.nz/wild/VIT or
x i)=Pˆ(Y =1|X =x i). To generate a bootstrap sample, we http://lock5stat.com/statkey has a place in education, to help
keepthesamex’s,andlety
i
∗ =1withprobabilityyˆi,otherwise studentsvisualizethesamplingprocess,butisnotsuitablewhen
y∗ =0. This is an example of a parametric bootstrap. We use studentsgointorealjobs.InR(RCoreTeam2014),studentscan
i
this at Google in a complicated multi-stage logistic regression writebootstraploopsfromscratch,butthisisdifficultforStat
procedure. 101students.Forthatmatteritmaybedifficultforhigherlevel
Theconditionaldistributionideaalsohelpsinlinearregres- students,butitisworthputtinginthateffort.Modernstatistics
sionwherethereisheteroscedasticityorlackoffit;wesample requires extensive computing skills including resampling and
residualsfromobservationswithsimilarresidualdistributions, simulation(ASA2014),anddevelopingthoseskillsshouldstart
for example, from observations with similar predictions (for early. The Mosaic package (Pruim, Kaplan, and Horton 2015)
heteroscedasticity)orx’s(forlackoffit). canmakethiseasier,andthepackagecontainsonevignettefor
resampling and another with resources including supplements
using Mosaic for (Lock et al. 2013; Tintle et al. 2014a). In
6. DISCUSSION
practice, implementing some of the more accurate bootstrap
We first summarize some points from above, then discuss methods is difficult (especially those not described here), and
booksandsoftware. peopleshoulduseapackageratherthanattemptthisthemselves.
Bootstrapping offers a number of pedagogical benefits. The ForR,thebootpackage(CantyandRipley2014)ispowerful
processofbootstrappingmimicsthecentralrolethatsampling butdifficulttouse.Theresamplepackage(Hesterberg2015)is
384 StatisticsandtheUndergraduateCurriculum

easierbutlimitedinscope.Thebootandresamplepackages REFERENCES
aredesignedforpractice,notforpedagogy,theyhidedetailsand
donotprovidedynamicsimulationsdemonstratingresampling. ASA(2014),CurriculumGuidelinesforUndergraduateProgramsinStatistical
boot offers tilting. resample offers the expanded percentile Science,Alexandria,VA:AmericanStatisticalAssociation.[384]
interval,withimprovedsmall-samplecoverage. Canty, A., and Ripley, B. (2014), boot: Bootstrap R (S-
Plus) Functions, R package version 1.3-16. Available at
Books need improvement. Too few textbooks use the boot-
https://cran.r-project.org/web/packages/boot/index.html.[384]
strap, and those that do could stand improvement. Chihara
Chamandy,N.,Muralidharan,O.,andWager,S.(2015),“TeachingStatisticsat
and Hesterberg (2011) and Lock et al. (2013) used permuta-
GoogleScale,”TheAmericanStatistician,69,thisissue.[374]
tion/randomization tests and bootstrapping to introduce infer-
Chihara,L.,andHesterberg,T.(2011),MathematicalStatisticsWithResampling
ence,andlatertointroduceformulamethods.Thetreatmentsare
andR,Hoboken,NJ:Wiley.[371,385]
largely pedagogically appropriate and valuable. However, nei-
Cobb, G. (2007), “The Introductory Statistics Course: A Ptolemaic Cur-
therrecognizesthatbootstrappercentileintervalsaretoonarrow
riculum,”TechnologyInnovationsinStatisticsEducation,1.Availableat
forsmallsamplesandinappropriatelyrecommendthatmethod
http://escholarship.org/uc/item/6hb3k0nz[371]
forsmallsamples.Locketal.(2013)alsorecommendedtesting
Davison,A.,andHinkley,D.(1997),BootstrapMethodsandTheirApplications,
asinglemeanusingthetranslationtechniquediscussedinSec-
Cambridge,UK:CambridgeUniversityPress.[371,381,382,383]
tion4.7;whilethatisusefulpedagogicallytodemonstratesome
Diez, D. M., Barr, C. D., and C¸etinkaya Rundel, M. (2014),
manipulations,itshouldbereplacedwithbetteralternativeslike
Introductory Statistics With Randomization and Simulation (1st
thebootstrapt.Diez,Barr,and C¸etinkaya Rundel (2014) used ed.), CreateSpace Independent Publishing Platform. Available at
thebootstrapforonlyoneapplication,atintervalwithbootstrap https://www.openintro.org/stat/textbook.php?stat_book=isrs[371,385]
SEforconfidenceintervalsforastandarddeviation.Otherwise Efron,B.(1981),“NonparametricStandardErrorsandConfidenceIntervals,”
theyavoidthebootstrap,duetopoorsmall-samplecoverageof CanadianJournalofStatistics,9,139–172.[383]
percentileintervals. ——— (1982), The Jackknife, the Bootstrap and Other Resampling Plans,
Theseimperfectionsshouldnotstopteachersfromusingthe NationalScienceFoundation–ConferenceBoardoftheMathematicalSci-
bootstrap now. The techniques can help students understand encesMonograph38,Philadelphia,PA:SocietyforIndustrialandApplied
Mathematics.[378]
statisticalconceptsrelatedtosamplingvariability.
I hope that this article spurs progress—that teachers better Efron,B.,andTibshirani,R.J.(1993),AnIntroductiontotheBootstrap,London:
ChapmanandHall.[371,375,380,381,382]
understandwhatthebootstrapcandoanduseittohelpstudents
understand statistical concepts, that people make more effec- Fisher, R. A. (1936), “Coefficient of Racial Likeness and the Future of
Craniometry,”JournaloftheRoyalAnthropologicalInstitute,66,57–63.
tive use of bootstrap techniques appropriate to the application
[372]
(not the percentile interval for small samples!), that textbook
Hall,P.(1992),TheBootstrapandEdgeworthExpansion,NewYork:Springer.
authorsrecommendbettertechniques,andthatbettersoftware
[381]
forpracticeandpedagogyresults.
Hall,P.,DiCiccio,T.,andRomano,J.(1989),“OnSmoothingandtheBoot-
strap,”TheAnnalsofStatistics,17,692–704.[375]
APPENDIX:SIMULATIONDETAILS
Hesterberg,T.C.(1999),“BootstrapTiltingConfidenceIntervals,”Computer
Figure 10 is based on 104 samples (except 5·103 for n≥6000), ScienceandStatistics:Proceedingsofthe31stSymposiumontheInterface,
FairfaxStation,VA:InterfaceFoundationofNorthAmerica,pp.389–393.
with r =104 resamples for bootstrap intervals, using a variance re-
[381]
duction technique based on conditioning. For normal data, X¯ and
V =(X 1 −X¯,...,X n −X¯) are independent, and each interval is ———(2004),“UnbiasingtheBootstrap—BootknifeSamplingvs.Smooth-
translation-invariant (the intervals for V and V +x¯ differ by x¯). ing,”inProceedingsoftheSectiononStatistics&theEnvironment,Alexan-
dria,VA:AmericanStatisticalAssociation,pp.2924–2930.[377]
Let U be the upper endpoint of an interval, and P(U <μ)=
E V(E(U <μ|V)).Theinnerexpectedvalueisanormalprobability: ——— (2014), “What Teachers Should Know About the Bootstrap: Re-
E(U <μ|V)=P(X¯ +U(V)<μ|V)=P(X¯ <μ−U(V)|V).This sampling in the Undergraduate Statistics Curriculum,” available at
techniquereducesthevariancebyfactorsrangingfrom9.6(forn=5) http://arxiv.org/abs/1411.5279.[371,374,375,377,380,381,382]
toover500(forn=160). ———(2015),Resample:ResamplingFunctions,Rpackageversion0.4.Avail-
Similarly, for the exponential distribution, X¯ and V = ableathttps://cran.r-project.org/web/packages/resample/.[371,381,384]
(X 1 /X¯,...,X n /X¯)areindependent,andweusethesameconditioning Hesterberg,T.,Moore,D.S.,Monaghan,S.,Clipson,A.,andEpstein,R.(2005),
technique.ThisreducestheMonteCarlovariancebyfactorsranging “BootstrapMethodsandPermutationTests,”inIntroductiontothePractice
from8.9(forn=5)toover5000(forn=8000).Theresultingaccu- ofStatistics(2nded.),eds.D.S.MooreandG.McCabe,NewYork:W.H.
racyisasgoodasusing89,000ormoresampleswithoutconditioning. Freeman.[371]
Forexample,standarderrorsforone-sidedcoverageforn=8000are Lock, R. H., Lock, R. H., Morgan, K. L., Lock, E. F., and Lock, D. F.
0.000030orsmaller. (2013), Statistics: Unlocking the Power of Data, Hoboken, NJ: Wiley.
[371,384,385]
SUPPLEMENTARYMATERIALS Owen,A.(2001),EmpiricalLikelihood,London:Chapman&Hall/CRCPress.
[383]
The online supplement contains R scripts for all examples,
Pruim, R., Kaplan, D., and Horton, N. (2015), Mosaic: The Project MO-
and a document with additional figures and more information SAIC Package, R package version 0.10.0. Available at https://cran.r-
aboutbiasestimatesandconfidenceintervals. project.org/web/packages/mosaic/.[384]
R Core Team (2014), R: A Language and Environment for Statistical
[ReceivedDecember2014.RevisedAugust2015] Computing, Vienna, Austria: R Foundation for Statistical Computing.
[371,382,384]
TheAmericanStatistician,November2015,Vol.69,No.4 385

Silverman, B., and Young, G. (1987), “The Bootstrap: to Smooth or Not to Tintle, N. L., Rogers, A., Chance, B., Cobb, G., Rossman, A., Roy,
Smooth,”Biometrika,74,469–479.[375] S., Swanson, T., and VanderStoep, J. (2014b), “Quantitative Ev-
idence for the Use Simulation and Randomization in the Intro-
Tintle,N.,Chance,B.,Cobb,G.,Rossman,A.,Roy,S.,Swanson,T.,andVan-
ductory Statistics Course,” in Proceedings of the Ninth Interna-
derStoep,J.(2014a),IntroductiontoStatisticalInvestigations(preliminary
tional Conference on Teaching Statistics, volume ICOTS-9. Available
edition),Hoboken,NJ:Wiley.[371,384]
at http://iase-web.org/icots/9/proceedings/pdfs/ICOTS9_8A3_TINTLE.pdf
[371]
386 StatisticsandtheUndergraduateCurriculum