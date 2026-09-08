Chapter 13
Principal Component (EOF) Analysis
13.1. BASICS OF PRINCIPAL COMPONENT ANALYSIS
Principalcomponentanalysis,oftendenotedasPCA,ispossiblythemostwidelyusedmultivariatesta-
tistical technique in the atmospheric sciences. The technique was introduced into the atmospheric
scienceliteraturebyObukhov(1947),andbecame popularforanalysisofatmospheric datafollowing
the papers byLorenz (1956),who calledthetechniqueempirical orthogonal function (EOF)analysis,
andDavis(1976).BoththenamesPCAandEOFanalysisarecommonlyused,andbothrefertothesame
setofprocedures.Sometimesthemethodisincorrectlyreferredtoasfactoranalysis,whichisarelated
but distinct multivariate statistical method. This chapter is intended to provide a basic introduction to
what has become a very large subject. Book-length treatments of PCA are given in Preisendorfer
(1988) and Navarra and Simoncini (2010), which are oriented specifically toward geophysical data;
andinJolliffe(2002),whichdescribesPCAmoregenerally.Hannachietal.(2007)provideacompre-
hensivereview.Inaddition,mosttextbooksonmultivariatestatisticalanalysiscontainchaptersonPCA.
13.1.1. Definition of PCA
PCAreducesadatasetcontainingalargenumberofvariablestoadatasetcontainingfewer(hopefully
manyfewer)newvariables.Thesenewvariablesarelinearcombinationsoftheoriginalones,andthese
linearcombinationsarechosentorepresentthemaximumpossiblefractionofthevariabilitycontainedin
the original data while being uncorrelated with each other. That is, given multiple observations of a
(K(cid:1)1)datavectorx,PCAfinds(M(cid:1)1)vectorsuwhoseelementsarelinearcombinationsoftheele-
mentsofthex0s,andwhichcontainmostoftheinformationintheoriginalcollectionofx0s.PCAismost
effectivewhenthisdatacompressioncanbeachievedwithM≪K.Thissituationoccurswhenthereare
substantialcorrelationsamongthevariableswithinx,inwhichcasexcontainsredundantinformation.
Theelements ofthesenew vectors u are calledthe principal components(PCs).
Dataforatmosphericandothergeophysicalfieldsgenerallyexhibitmanylargecorrelationsamong
thevariablesx ,andaPCAresultsinamuchmorecompactrepresentationoftheirvariations.Beyond
k
mere data compression, however, PCA can be a very useful tool for exploring large multivariate data
sets,includingthoseconsistingofgeophysicalfields.HerePCAhasthepotentialforyieldinginsights
into both the spatial and temporal variations exhibited by the field or fields being analyzed, and new
interpretations of the original data x can be suggested by the nature of the linear combinations that
are mosteffective incompressing those data.
UsuallyitisconvenienttocalculatethePCsaslinearcombinationsoftheanomaliesx0¼x–x.The
firstPC,u ,isthatlinearcombinationofx0 havingthelargestvariance.Thesubsequentprincipalcom-
1
ponentsu ,m¼2,3,…,arethelinearcombinationshavingthelargestpossiblevariances,subjecttothe
m
StatisticalMethodsintheAtmosphericSciences.https://doi.org/10.1016/B978-0-12-815823-4.00013-4
©2019ElsevierInc.Allrightsreserved. 617

618 PART III MultivariateStatistics
conditionthattheyareuncorrelatedwiththeprincipalcomponentshavinglowerindices.Theresultis
thatall the PCs are mutuallyuncorrelated.
The new variables or PCs—that is, the elements u of u that will account successively for the
m
maximumamountofthejointvariabilityofx0 (andthereforealsoofx)—areuniquelydefined(except
for sign) by the eigenvectors of the covariance matrix of x, [S]. In particular, the mth principal com-
ponent, u is obtained as the projection ofthe data vector x0 onto the mtheigenvector, e ,
m m
XK
u ¼eTx0¼ e x0, m¼1,…,M: (13.1)
m m k,m k
k¼1
Notice thateachoftheMeigenvectorscontainsoneelement pertainingtoeach oftheKvariables, x .
k
Similarly, each realization of the mth principal component in Equation 13.1 is computed from a par-
ticular set of observations of the K variables x . That is, each of the M principal components is a sort
k
of weighted average of the x values that are the elements of a particular data vector x. Although the
k
weights(thee 0s)donotsumto1,theirsquaresdobecauseofthescalingconventionjje jj¼1.(Note
k,m m
thatafixedscalingconventionfortheweightse ofthelinearcombinationsinEquation13.1allowsthe
m
maximumvarianceconstraintdefiningthePCstobemeaningful.)Ifthedatasampleconsistsofnobser-
vations(andthereforeofndatavectorsx,ornrowsinthedatamatrix[X]),therewillbenvaluesforeach
oftheprincipalcomponents,ornewvariables,u .Eachoftheseconstitutesasingle-numberindexofthe
m
resemblancebetween the eigenvector e and the corresponding individual data vectorx.
m
Geometrically,thefirsteigenvector,e ,pointsinthedirection(intheK-dimensionalspaceofx0)in
1
which the data vectors jointly exhibit the mostvariability. This first eigenvector is the one associated
withthelargesteigenvalue,l .Thesecondeigenvectore ,associatedwiththesecond-largesteigenvalue
1 2
l ,isconstrainedtobeperpendiculartoe (Equation11.50),butsubjecttothisconstraintitwillalignin
2 1
thedirectioninwhichthex0vectorsexhibittheirnextstrongestvariations.Subsequenteigenvectorse ,
m
m¼3,4,…,M,aresimilarlynumberedaccordingtodecreasingmagnitudesoftheirassociatedeigen-
values,andinturnwillbeperpendiculartoallthepreviouseigenvectors.Subjecttothisorthogonality
constrainttheseeigenvectorswillcontinuetolocatedirectionsinwhichtheoriginaldatajointlyexhibit
maximum variability.
Putanotherway,theeigenvectorsdefineanewcoordinatesysteminwhichtoviewthedata.Inpar-
ticular,theorthogonalmatrix[E]whosecolumnsaretheeigenvectors(Equation11.51)definestherigid
rotation
u¼½E(cid:3)Tx0, (13.2)
whichisthesimultaneousmatrix-notationrepresentationofM¼Klinearcombinationsoftheformof
Equation 13.1 (i.e., here the matrix [E] is square, with K eigenvector columns). This new coordinate
system is oriented such that each consecutively numbered axis is aligned along the direction of the
maximumjointvariabilityofthedata,consistentwiththataxisbeingorthogonaltotheprecedingones.
Theseaxeswillturnouttobedifferentfordifferentdatasets,becausetheyareextractedfromthesample
covariance matrix [S ] particular to a given data set. That is, they are orthogonal functions, but are
x
defined empirically according to the particular data set at hand. This observation is the basis for the
eigenvectors being known in this context as empirical orthogonal functions (EOFs). The implied dis-
tinction is with theoretical orthogonal functions, such as Fourier harmonics or Tschebyschev polyno-
mials, which alsocan beused todefine alternative coordinate systemsin which to view a data set.

| Chapter | 13 Principal | Component(EOF) |     | Analysis |     | 619 |
| ------- | ------------ | -------------- | --- | -------- | --- | --- |
Itisaremarkablepropertyoftheprincipalcomponentsthattheyareuncorrelated.Thatis,thecor-
relationmatrixforthenewvariablesu m issimply[I].Thispropertyimpliesthatthecovariancesbetween
pairs of the u 0s are all zero, so that the corresponding covariance matrix is diagonal. In fact, the
m
covariance matrix for the principal components is obtained by the diagonalization of [S ]
x
(Equation11.56)and is thus simply the diagonal matrix[L]ofthe eigenvalues of[S]:
|     |     |     | (cid:2) (cid:3) |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- |
½S (cid:3)¼Var ½E(cid:3)Tx ¼½E(cid:3)T½S (cid:3)½E(cid:3)¼½E(cid:3)(cid:4)1½S (cid:3)½E(cid:3)¼½L(cid:3): (13.3)
|     |     | u   |     | x   | x   |     |
| --- | --- | --- | --- | --- | --- | --- |
That is, the variance of the mth principal component u is the mth eigenvalue l . Equation 11.54
m m
then implies that each PC represents a share of the total variation in x that is proportional to its
eigenvalue,
|     |     |     | l                   |     | l              |        |
| --- | --- | --- | ------------------- | --- | -------------- | ------ |
|     |     |     | R2 ¼ m (cid:1)100%¼ |     | m (cid:1)100%: | (13.4) |
|     |     |     | m XK                |     | XK             |        |
|     |     |     | l k                 |     | s k,k          |        |
|     |     |     | k¼1                 |     | k¼1            |        |
HereR2isusedinthesamesensethatisfamiliarfromlinearregression(Section7.2.4).Thetotalvar-
iationexhibitedbytheoriginaldataiscompletelyrepresentedin(oraccountedforby)thefullsetofK
0s,inthesensethatthesumofthevariancesofthecentereddatax0(andthereforealsooftheuncentered
u
m
variablesx),S s ,isequaltothesumofthevariancesS l .oftheprincipalcomponentvariablesu.
|     | k k,k |     |     |     | m m |     |
| --- | ----- | --- | --- | --- | --- | --- |
x0 u
Equation 13.2 expresses the transformation of a (K(cid:1)1) data vector to a vector of PCs. If [E]
contains all K eigenvectors of [S ] (assuming [S ] is nonsingular) as its columns, the resulting vector
|     |     |     | x   | x   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
u will also have dimension (K(cid:1)1). Equation 13.2 sometimes is called the analysis formula for x0,
expressingthatthedatacanbeanalyzed,orsummarizedintermsoftheprincipalcomponents.Reversing
the transformation in Equation 13.2, the data x0 can be reconstructed from the principal components
| according | to  |     |     |           |     |        |
| --------- | --- | --- | --- | --------- | --- | ------ |
|           |     |     | x0  | ½E(cid:3) | u , | (13.5) |
¼
|     |     |     | ðK(cid:1)1Þ |     | ðK(cid:1)1Þ |     |
| --- | --- | --- | ----------- | --- | ----------- | --- |
ðK(cid:1)KÞ
whichisobtainedfromEquation13.2bymultiplyingontheleftby[E]andusingtheorthogonalitypropertyof
thismatrix(Equation11.44).Thereconstructionofx0expressedbyEquation13.5issometimescalledthe
synthesisformula.IfthefullsetofM¼KPCsisusedinthesynthesis,thereconstructioniscompleteand
exact,sinceS R2 ¼1(cf.Equation13.4).IfM<KPCs(usuallythosecorrespondingtotheMlargesteigen-
m m
values)areused,thereconstructionisapproximate,
|     |     |     | x0          | (cid:5) ½E(cid:3) | u ,         | (13.6a) |
| --- | --- | --- | ----------- | ----------------- | ----------- | ------- |
|     |     |     | ðK(cid:1)1Þ | ðK(cid:1)MÞ       | ðM(cid:1)1Þ |         |
or
XM
|     |     |     | x0 (cid:5) | e u , | k¼1,…,K, | (13.6b) |
| --- | --- | --- | ---------- | ----- | -------- | ------- |
|     |     |     | k          | k,m m |          |         |
m¼1
but the approximation improves as the number M of PCs used (or, more precisely, as the sum of the
correspondingeigenvalues,becauseofEquation13.4)increases.Because[E]inEquation13.6ahasonly
Mcolumns,andoperatesonatruncatedPCvectoruofdimension(M(cid:1)1),Equation13.6iscalledthe

620 PART III MultivariateStatistics
truncated synthesis formula. The original (in the case of Equation 13.5) or approximated (for
Equation 13.6) uncentered data x can easily be obtained by adding back the vector of sample means,
thatis, by reversingEquation 11.33.
Because each principal component u is a linear combination of the original variables x
m k
(Equation 13.1), and vice versa (Equation 13.5), pairs of principal components and original variables
will be correlated unless the eigenvector element e relating them is zero. It can sometimes be
k,m
informative tocalculate these correlations, which are given by
sffiffiffiffiffiffiffi
l
r ¼Corrðu ,x Þ¼e m: (13.7)
u,x m k k,m s
k,k
Example 13.1. PCA inTwo Dimensions
The basics of PCA are most easily appreciated in a simple example where the geometry can be visu-
alized. If K¼ 2 the space of the data is two-dimensional and can be graphed on a page. Figure13.1a
shows a scatterplot of centered (at zero) January 1987 Ithaca minimum temperatures (x 0) and
1
Canandaigua minimum temperatures (x 0) from Table A.1. This is the samescatterplot thatappears in
2
themiddleofthebottomrowofFigure3.31.ItisapparentthattheIthacatemperaturesaremorevariable
thantheCanandaiguatemperatures,withthetwostandarddeviationsbeing√s ¼13.62°Fand√s ¼
1,1 2,2
8.81°F,respectively.ThetwovariablesareclearlystronglycorrelatedandhaveaPearsoncorrelationof
+0.924(seeTable3.5).Thecovariancematrix[S]forthesetwovariablesisgivenas[A]inEquation11.59.
The two eigenvectors of this matrix are e T¼½0:848,0:530(cid:3) and e T¼½(cid:4)0:530,0:848(cid:3), so that the
1 2
eigenvector matrix [E] is that shown in Equation 11.60. The corresponding eigenvalues are l ¼
1
254.76andl ¼8.29.Thesearethesamedatausedtofitthebivariatenormalprobabilityellipsesshown
2
inFigures12.1and12.7.
TheorientationsofthetwoeigenvectorsareshowninFigure13.1a,althoughtheirlengthshavebeen
exaggeratedforclarity.Itisevidentthatthefirsteigenvectorisalignedinthedirectioninwhichthedata
jointlyexhibitmaximumvariation.Thatis,thepointcloudisinclinedatthesameangleasise ,whichis
1
32°fromthehorizontal(i.e.,fromthevector[1,0],accordingtoEquation11.15).Sincethedatainthis
simpleexampleexistinonlyK¼2dimensions,theconstraintthatthesecondeigenvectormustbeper-
pendicular to the first determines its direction up to sign (i.e., it could as easily be
(cid:4)e T¼½0:530, (cid:4)0:848(cid:3)).Thislasteigenvectorlocatesthedirectioninwhichdatajointlyexhibittheir
2
smallest variations.
Figure13.1billustratesanotherpropertyofthefirsteigenvector,whichisthatitisthedirectionthatmin-
imizes the sum of squared distances (dashed lines)perpendicular toe , connecting ittothe points. The
1
leadingeigenvectoristhusdifferentfromtheleast-squaresregressionlinesrelatingthetwovariables,which
wouldminimizeeitherthesumofsquaredverticaldistances(iftheCanandaiguatemperatureswerebeing
predicted)orthesquaredhorizontaldistances(iftheIthacatemperatureswerebeingpredicted).Inthree
dimensions,thesecondeigenvectorwouldbethedirectionperpendiculartoe ,definingthee –e planemin-
1 1 2
imizingtheperpendicularsquareddistancesfromtheplanetothepoints,andsoon,inprogressivelyhigher
dimensions.
Thetwoeigenvectorsdetermineanalternativecoordinatesysteminwhichtoviewthedata.This
fact may become more clear if you rotate this book 32° clockwise while looking at Figure 13.1a.
Within this rotated coordinate system, each point is defined by a principal component vector

| Chapter | 13 Principal Component(EOF) | Analysis |     |     | 621 |
| ------- | --------------------------- | -------- | --- | --- | --- |
F° ,′
2
x ,ylamona erutarepmet muminim augiadnanaC
e
|     | 20  | 2   |     | 6.6 |     |
| --- | --- | --- | --- | --- | --- |
e
1
10
23.0
0
–10
|     |     | –20 –10                               | 0 10 | 20    |     |
| --- | --- | ------------------------------------- | ---- | ----- | --- |
|     | (a) | Ithaca minimum temperature anomaly, x |      | ¢, °F |     |
1
F° ,′
2
x ,ylamona erutarepmet muminim augiadnanaC
e
20 2
e
1
10
0
–10
|     |     | –20 –10                               | 0 10 | 20     |     |
| --- | --- | ------------------------------------- | ---- | ------ | --- |
|     | (b) | Ithaca minimum temperature anomaly, x |      | ′, °F  |     |
1
FIGURE13.1 (a)ScatterplotofJanuary1987IthacaandCanandaiguaminimumtemperatures(convertedtoanomalies,orcen-
| tered),illustratingthegeometryofPCAintwodimensions.Theeigenvectorse |     |     | ande |                                       |     |
| ------------------------------------------------------------------- | --- | --- | ---- | ------------------------------------- | --- |
|                                                                     |     |     | 1    | 2 ofthecovariancematrix[S]forthesetwo |     |
variables,ascomputedinExample11.3,havebeenplottedwithlengthsexaggeratedforclarity.Thedatastretchoutinthedirection
ofe
1 totheextentthat96.8%ofthejointvarianceofthesetwovariablesoccursalongthisaxis.Thecoordinatesu 1 andu,corre- 2
spondingtothedatapointx0T[16.0,17.8],recordedonJanuary15andindicatedbythelargesquaresymbol,areshownbylengthsin
thedirectionsofthenewcoordinatesystemdefinedbytheeigenvectors.Thatis,thevectoruT¼[23.0,6.6]locatesthesamepointas
x0T¼[16.0,17.8].(b)Thefirsteigenvectore
1 isalsothedirectionthatminimizesthesumofsquaredlengthsofthedashedlines
| betweenthepointsande | ,thatareperpendiculartoe. |     |     |     |     |
| -------------------- | ------------------------- | --- | --- | --- | --- |
|                      | 1                         | 1   |     |     |     |

| 622 |     |     |     |     |     | PART III MultivariateStatistics |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- |
uT¼[u ,u ]ofnewtransformedvariables,whoseelementsconsistoftheprojectionsoftheoriginal
| 1   | 2   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
data onto the eigenvectors, according to the dot product in Equation 13.1. Figure 13.1a illustrates
thisprojectionforthe15Januarydatapointx0T¼[16.0,17.8],whichisindicatedbythelargesquare
symbol. For this datum, u ¼ (0.848)(16.0) + (0.530)(17.8) ¼ 23.0, and u ¼ (–0.530)(16.0) +
1 2
| (0.848)(17.8) | ¼ 6.6. |     |     |     |     |     |     |
| ------------- | ------ | --- | --- | --- | --- | --- | --- |
The sample variance of the new variable u is an expression of the degree to which it spreads out
1
along its axis (i.e., along the direction of e ). This dispersion is evidently greater than the dispersion
1
of the data along either of the original axes, and indeed it is larger than the dispersion of the data
in any other direction in this plane. This maximum sample variance of u is equal to the eigenvalue
1
254.76°F2.
l 1 ¼ The points in the data set tend to exhibit quite different values of u 1 , whereas they
havemoresimilarvaluesforu .Thatis,theyaremuchlessvariableinthee direction,andthesample
2 2
| variance | ofu is only | l ¼ 8.29°F2. |     |     |     |     |     |
| -------- | ----------- | ------------ | --- | --- | --- | --- | --- |
|          | 2           | 2            |     |     |     |     |     |
¼263.05°F2,thenewvariablesjointlyretainallthevariationexhibitedby
| Sincel | +l ¼s   | +s  |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- | --- |
|        | 1 2 1,1 | 2,2 |     |     |     |     |     |
theoriginalvariables.However,thefactthatthepointcloudseemstoexhibitnoslopeinthenewcoor-
dinateframedefinedbytheeigenvectorsindicatesthatu 1 andu 2 areuncorrelated.Theirlackofcorre-
lationcanbeverifiedbytransformingthe31pairsofminimumtemperaturesinTableA.1toprincipal
componentsandcomputingthePearsoncorrelation,whichiszero.Thevariance–covariancematrixfor
| the principal | components | is therefore | [L], | asshownin | Equation | 11.62. |     |
| ------------- | ---------- | ------------ | ---- | --------- | -------- | ------ | --- |
Thetwooriginaltemperaturevariablesaresostronglycorrelatedthataverylargefractionoftheir
jointvariance,l 1 /(l 1 +l 2 )¼0.968,isrepresentedbythefirstprincipalcomponentalone.Itwouldbesaid
thatthefirstprincipalcomponentdescribes96.8%ofthetotalvariance.Thefirstprincipalcomponent
might be interpreted as reflecting the regional minimum temperature for the area including these two
locations (they are about 50 miles, or about 80 km apart), with the second principal component
| describing | local variations | departing | from | the overallregional |     | value. |     |
| ---------- | ---------------- | --------- | ---- | ------------------- | --- | ------ | --- |
Since somuchof the joint varianceof the twotemperature series is capturedby the first principal
component,resynthesizingtheseriesusingonlythefirstprincipalcomponentwillyieldagoodapprox-
imation to the original data. Using the synthesis Equation 13.6 with only the first (M ¼ 1) principal
| component | yields |        |         |          |          |                 |        |
| --------- | ------ | ------ | ------- | -------- | -------- | --------------- | ------ |
|           |        |        | (cid:5) | (cid:6)  |          | (cid:5) (cid:6) |        |
|           |        |        | x0ðtÞ   |          |          | :848            |        |
|           |        | x0ðtÞ¼ | 1       | (cid:5)e |          | ðtÞ:            |        |
|           |        |        |         | 1        | u 1 ðtÞ¼ | :530 u 1        | (13.8) |
x0ðtÞ
2
Thetemperaturedataxaretimeseries,andthereforesoaretheprincipalcomponentsu.Thetimedepen-
denceforbothhasbeenindicatedexplicitlyinEquation13.8.Ontheotherhand,theeigenvectorsarefixed
bythecovariancestructureoftheentireseriesanddonotchangethroughtime.Figure13.2comparesthe
originalseries(black)andthereconstructionsusingthefirstprincipalcomponentu (t)only(gray)forthe
1
(a)Ithacaand(b)Canandaiguaanomalies.ThediscrepanciesaresmallbecauseR2 ¼96:8%.Theresidual
1
differenceswouldbecapturedbyu 2 .Thetwograyseriesareexactlyproportionaltoeachother,sinceeach
isascalarmultipleofthesamefirstprincipalcomponenttimeseries.SinceVar(u )¼l ¼254.76,the
1 1
variancesofthereconstructedseriesare(0.848)2254.76¼183.2and(0.530)2254.76¼71.6°F2,respec-
tively,whichareclosetobutsmallerthanthecorrespondingdiagonalelementsoftheoriginalcovariance
matrix (Equation 11.59). The larger variance for the Ithaca temperatures is also visually evident in
Figure 13.2. Using Equation 13.7, the correlations between the first principal component series u 1 (t)
and the original temperature variables are 0.848(254.76/185.47)1/2 ¼ 0.994 for Ithaca, and 0.530
| (254.76/77.58)1/2¼0.960forCanandaigua. |     |     |     |     |     |     | e   |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |

30
0
–30
1 11 21 31
30
0
–30
1 11 21 31
Date
13.1.2. PCA Based on the Covariance Matrix vs. the Correlation Matrix
APCAcanbecomputedaseasilyusingthecorrelationmatrix[R]asitcanonthecovariancematrix[S].
The correlation matrix is the variance–covariance matrix of the vector of standardized variables z
(Equation 11.32). The vector of standardized variables z is related to the vectors of original variables
xandtheircenteredcounterpartsx0accordingtothescalingtransformation(Equation11.34).Therefore
PCA on the correlation matrix amounts to analysis of the joint variance structure of the standardized
variablesz , ascomputed using either Equation 11.34or (in scalar form) Equation 3.27.
k
The difference between a PCA performed using the variance–covariance and correlation matrices
will be one of emphasis. Since PCA seeks to find variables successively maximizing the proportion of
thetotalvariance(S s )represented,analyzingthecovariancematrix[S]resultsinprincipalcomponents
k k,k
thatemphasizethex ’shavingthelargestvariances.Otherthingsequal,thetendencywillbeforthefirstfew
k
eigenvectorstoalignnearthedirectionsofthevariableshavingthebiggestvariances.InExample13.1,the
first eigenvector points more toward the Ithaca minimum temperature axis because the variance of
theIthacaminimumtemperaturesislargerthanthevarianceoftheCanandaiguaminimumtemperatures.
Conversely,PCAappliedtothecorrelationmatrix[R]weightsallthestandardizedvariablesz equally,
k
sinceallhaveequal(unit)variance.
IfthePCAiscomputedusingthecorrelationmatrix,theanalysisformula,Equations13.1and13.2,
will pertain to the standardized variables, z and z, respectively. Similarly the synthesis formulae,
k
Equations 13.5 and 13.6 will pertain toz and z rather than tox0 and x 0. In this case the original data
k k
.pmet
.nim
acahtI
.pmet
.nim
augiadnanaC
F˚
,′x
,ylamona
F˚
,′x
,ylamona
1
1
Chapter 13 Principal Component(EOF) Analysis 623
(a)
(b)
FIGURE13.2 TimeseriesofJanuary1987(a)Ithacaand(b)Canandaiguaminimumtemperatureanomalies(black),andtheir
reconstructionusingthefirstprincipalcomponentonly(gray),throughthesynthesisEquation13.8.

624 PART III MultivariateStatistics
x can be recovered from the result of the synthesis formula by reversing the standardization given by
Equations 11.33and 11.34, thatis,
x¼½D(cid:3)z+x: (13.9)
Although z and x0 can easily be obtained from each other using Equation 11.34, the eigenvalue–
eigenvectorpairsof[R]and[S]donotbearsimplerelationshipstooneanother.Ingeneral,itisnotpos-
sibletocomputetheeigenvectorsandprincipalcomponentsofoneknowingonlytheeigenvectorsand
principal components of the other. This fact implies that these two alternatives for PCA do not yield
equivalent information and that an intelligent choice of one over the other must be made for a given
application.Ifanimportantgoaloftheanalysisistoidentifyorisolatethestrongestvariationsinadata
set, the better alternative usually will be PCA using the covariance matrix, although the choice will
dependonthejudgmentoftheanalystandthepurposeofthestudy.Forexample,inanalyzinggridded
numbers of extratropical cyclones, Overland and Preisendorfer (1982) found that PCA on their
covariancematrixbetteridentifiedregionshavingthehighestvariabilityincyclonenumbers,andthat
correlation-based PCA was more effective at locating the primarystorm tracks.
However, if the analysis is of unlike variables—variables not measured in the same units—it will
almostalwaysbepreferable tocomputethePCAusingthecorrelationmatrix.Measurementinunlike
physicalunitsyieldsarbitraryrelativescalingsofthevariables,whichresultsinarbitraryrelativemag-
nitudesofthevariancesofthesevariables.Totakeasimpleexample, thevarianceofasetoftemper-
atures measured in °F will be (1.8)2 ¼ 3.24 times as large as the variance of the same temperatures
expressed in °C. If the PCA has been done using the correlation matrix, the analysis formula,
Equation 13.2, pertains to the vector z rather than x0, and the synthesis in Equation 13.5 will yield
thestandardizedvariablesz (orapproximationstothemifEquation13.6isusedforthereconstruction).
k
ThesummationsinthedenominatorsofEquation13.4willequalthenumberofstandardizedvariables,
since each has unit variance.
Example 13.2 Correlation-Versus Covariance-BasedPCA for ArbitrarilyScaled Variables
The importance of basing a PCA on the correlation matrix when the variables being analyzed are not
measuredoncomparablescalesispresentedinTable13.1.ThistablesummarizesPCAsoftheJanuary
1987 data in Table A.1 in (a) unstandardized (covariance matrix) and (b) standardized (correlation
matrix)forms.Samplevariancesofthevariablesareshown,asarethesixeigenvectors,thesixeigen-
values,andthecumulativepercentagesofvarianceaccountedforbytheprincipalcomponents.The(6x6)
arrays in the upper-right portions of parts (a) and (b) of this table constitute the matrices [E] whose
columns are the eigenvectors.
Thesamplevariancesofeachofthevariablesareshown,asarethesixeigenvectorse arrangedin
m
decreasing orderoftheir eigenvalues l .Thecumulativepercentage ofvariancerepresented iscalcu-
m
latedaccordingtoEquation13.4.Themuchsmallervariancesoftheprecipitationvariablesin(a)arean
artifactofthemeasurementunits,butresultinprecipitationbeingunimportantinthefirstfourprincipal
components computed from the covariance matrix, which collectively account for 99.9% of the total
varianceofthedataset.Computingtheprincipalcomponentsfromthecorrelationmatrixensuresthat
variationsof the temperature and precipitationvariables are weighted equally.
Because of the different magnitudes of the variations of the data in relation to their measurement
units, the variances of the unstandardized precipitation data are tiny in comparison to the variances
ofthetemperaturevariables.Thisispurelyanartifactofthemeasurementunitforprecipitation(inches)
being relatively large in comparison to the range of variation of the data (about 1 in.), and the

| Chapter | 13 Principal Component(EOF) | Analysis |     |     | 625 |
| ------- | --------------------------- | -------- | --- | --- | --- |
TABLE13.1 ComparisonofPCAComputedUsing(a)theCovarianceMatrix,and(b)the
CorrelationMatrix,oftheDatainTableA.1
| Variable | SampleVariance | e e | e e | e e |     |
| -------- | -------------- | --- | --- | --- | --- |
|          |                | 1 2 | 3 4 | 5 6 |     |
(a)Covarianceresults:
0.059in.2
| Ithacappt. |     | .003 .017 | .002 (cid:4).028 | .818 (cid:4).575 |     |
| ---------- | --- | --------- | ---------------- | ---------------- | --- |
IthacaT 892.2°F2 .359 (cid:4).628 .182 (cid:4).665 (cid:4).014 (cid:4).003
max
| IthacaT | 185.5°F2 |     |     |     |     |
| ------- | -------- | --- | --- | --- | --- |
.717 .527 .456 .015 (cid:4).014 .000
min
0.028in.2 (cid:4).023
| Canandaiguappt. |         | .002 .010        | .005      | .574 .818 |     |
| --------------- | ------- | ---------------- | --------- | --------- | --- |
| CanandaiguaT    | 61.8°F2 | .381 (cid:4).557 | .020 .737 | .037 .000 |     |
max
| CanandaiguaT | 77.6°F2        |            |                         |                  |     |
| ------------ | -------------- | ---------- | ----------------------- | ---------------- | --- |
|              | min            | .459 .131  | (cid:4).871 (cid:4).115 | (cid:4).004 .003 |     |
|              | Eigenvalues,lk | 337.7 36.9 | 7.49 2.38               | 0.065 0.001      |     |
|              | Cum.%variance  | 87.8 97.4  | 99.3 99.9               | 100.0 100.0      |     |
(b)Correlationresults:
| Ithacappt. | 1.000 | .142 .677 | .063 (cid:4).149 | (cid:4).219 .668 |     |
| ---------- | ----- | --------- | ---------------- | ---------------- | --- |
IthacaT
| max     | 1.000 | .475 (cid:4).203 | .557 .093        | .587 .265        |     |
| ------- | ----- | ---------------- | ---------------- | ---------------- | --- |
| IthacaT | 1.000 | .495 .041        | (cid:4).526 .688 | (cid:4).020 .050 |     |
min
| Canandaiguappt. | 1.000 | .144 .670 | .245 .096 | .164 (cid:4).658 |     |
| --------------- | ----- | --------- | --------- | ---------------- | --- |
CanandaiguaT 1.000 .486 (cid:4).220 .374 (cid:4).060 (cid:4).737 (cid:4).171
max
CanandaiguaT 1.000 .502 (cid:4).021 (cid:4).458 (cid:4).695 (cid:4).192 (cid:4).135
min
Eigenvalues,lk
|     |               | 3.532 1.985 | 0.344 0.074 | 0.038 0.027 |     |
| --- | ------------- | ----------- | ----------- | ----------- | --- |
|     | Cum.%variance | 58.9 92.0   | 97.7 98.9   | 99.5 100.0  |     |
measurementunitfortemperature(°F)beingrelativelysmallincomparisontotherangeofvariationof
the data (about 40°F). If the measurement units had been millimeters and °C, respectively, the differ-
ences in variances would have been much smaller. If the precipitation had been measured in micro-
meters, the variances of the precipitation variables would dominate the variances of the temperature
variables.
Becausethevariancesofthetemperaturevariablesaresomuchlargerthanthevariancesofthepre-
cipitationvariables,thePCAcalculatedfromthecovariancematrixisdominatedbythetemperatures.
The eigenvector elements corresponding to the two precipitation variables are negligibly small in the
firstfoureigenvectors,sothesevariablesmakenegligiblecontributionstothefirstfourprincipalcom-
ponents. However, these first four principal components collectively describe 99.9% of the joint var-
iance. An application of the truncated synthesis formula (Equation 13.6) with the leading M ¼ 4
eigenvector therefore would result in reconstructed precipitation data very near their average values.
That is, essentiallynone ofthe variationinprecipitation would berepresented.
Since the correlation matrix is the covariance matrix for comparably scaled variables z , each has
k
equalvariance.Unliketheanalysisonthecovariancematrix,thisPCAdoesnotignoretheprecipitation
variables when the correlation matrix is analyzed. Here the first (and most important) principal com-
ponent represents primarily the closely intercorrelated temperature variables, as can be seen from the

| 626 |     |     |     |     | PART | III MultivariateStatistics |
| --- | --- | --- | --- | --- | ---- | -------------------------- |
relativelylargerelementsofe forthefourtemperaturevariables.However,thesecondprincipalcom-
1
ponent, which accounts for 33.1% of the total variance in the scaled data set, represents primarily
theprecipitationvariations.Theprecipitationvariationswouldnotbelostinatruncateddatarepresen-
tation including at least the first M ¼ 2 eigenvectors, but rather would be very nearly completely
e
reconstructed.
| 13.1.3. The | Varied | Terminology | of PCA |     |     |     |
| ----------- | ------ | ----------- | ------ | --- | --- | --- |
ThesubjectofPCAissometimesregardedasadifficultandconfusingone,butmuchofthisconfusion
derives froma proliferationof theassociated terminology, especially inwritingsby analystsofatmo-
sphericdata.Table13.2organizesthemorecommonoftheseinawaythatmaybehelpfulindeciphering
the PCA literature.
Lorenz(1956)introducedthetermempiricalorthogonalfunction(EOF)intotheliteratureasanother
name for the eigenvectors of a PCA. The terms modes of variation and pattern vectors also are used
primarily by analysts of geophysical data, especially in relation to analysis of fields, to be described
inSection 13.2. The remaining terms for the eigenvectors derive from the geometric interpretation of
theeigenvectorsasbasisvectors,oraxes,intheK-dimensionalspaceofthedata.Thesetermsareused
| inthe literature | ofa broader | range | ofdisciplines. |     |     |     |
| ---------------- | ----------- | ----- | -------------- | --- | --- | --- |
The most common name for individual elements of the eigenvectors in the statistical literature is
loading, connoting the weight of the kth variable x that is borne by the mth eigenvector e through
k m
the individual element e . The term “coefficient” is also a usual one in the statistical literature. The
k,m
term pattern coefficient is used mainly in relation to PCA of field data, where the spatial patterns
exhibitedbytheeigenvectorelementscanbeilluminating.Empiricalorthogonalweightsisatermthat
is sometimesused tobeconsistent with the naming of the eigenvectors asEOFs.
Thenewvariablesu definedwithrespecttotheeigenvectorsarealmostuniversallycalled"principal
m
components."However,theyaresometimesknownasempiricalorthogonalvariableswhentheeigen-
vectorsarecalledEOFs.Thereismorevariationintheterminologyfortheindividualvaluesoftheprin-
x0.
cipal componentsu i,m corresponding toparticular data vectors i Inthe statistical literature these are
TABLE13.2
APartialGuidetoSynonymousTerminologyAssociatedWithPCA
|                |     | Eigenvector |     | Principal           |     | PrincipalComponent |
| -------------- | --- | ----------- | --- | ------------------- | --- | ------------------ |
| Eigenvectors,e |     |             |     | Components,u        |     |                    |
|                | m   | elements,e  | k,m |                     | m   | Elements,u i,m     |
| EOFs           |     | Loadings    |     | EmpiricalOrthogonal |     | Scores             |
Variables
| ModesofVariation |     | Coefficients        |     |     |     | Amplitudes            |
| ---------------- | --- | ------------------- | --- | --- | --- | --------------------- |
| PatternVectors   |     | PatternCoefficients |     |     |     | ExpansionCoefficients |
| PrincipalAxes    |     | EmpiricalOrthogonal |     |     |     | Coefficients          |
Weights
PrincipalVectors
ProperFunctions
PrincipalDirections

| Chapter | 13 Principal | Component(EOF) | Analysis |     |     | 627 |
| ------- | ------------ | -------------- | -------- | --- | --- | --- |
mostcommonlycalled"scores,"whichhasahistoricalbasisintheearlyandwidespreaduseofPCAin
psychometrics.Inatmosphericapplications,theprincipalcomponentelementsareoftencalled"ampli-
tudes"byanalogytotheamplitudesofaFourierseries,whichmultiplythe(theoreticalorthogonal)sine
andcosinefunctions.Similarly,thetermexpansioncoefficientisalsousedforthismeaning.Sometimes
expansioncoefficientisshortenedsimplyto"coefficient,"althoughthiscanbethesourceofsomecon-
fusion since it is more standardfor the term coefficient todenotean eigenvector element.
| 13.1.4. | Scaling Conventions | in PCA |     |     |     |     |
| ------- | ------------------- | ------ | --- | --- | --- | --- |
AnothercontributiontoconfusionintheliteratureofPCAistheexistenceofalternativescalingconven-
tionsfortheeigenvectors.Thepresentationinthischapterassumesthattheeigenvectorsarescaledto
unitlength,thatis,jje
m jj(cid:6)1.RecallthatvectorsofanylengthwillsatisfyEquation11.48iftheypointin
theappropriatedirection,andasaconsequenceitiscommonfortheoutputofeigenvectorcomputations
| to beexpressed | with this | scaling. |     |     |     |     |
| -------------- | --------- | -------- | --- | --- | --- | --- |
However,itissometimesusefultoexpressandmanipulatePCAresultsusingalternativescalingsof
theeigenvectors.Whenthisisdone,eachelementofaneigenvectorismultipliedbythesameconstant,
sotheirrelativemagnitudesandrelationshipsremainunchanged.Thereforethequalitativeresultsofan
exploratoryanalysisbasedonPCAdonotdependonthescalingselected,butifdifferent,relatedana-
lysesare to becompared it is important tobe aware ofthe scaling conventionused ineach.
Rescalingthelengthsoftheeigenvectorschangesthemagnitudesoftheprincipalcomponentsbythe
samefactor.Thatis,multiplyingtheeigenvectore byaconstantrequiresthattheprincipalcomponent
m
scoresu m bemultipliedbythesameconstantinorderfortheanalysisformulasthatdefinetheprincipal
components(Equations13.1and13.2)toremainvalid.Theexpectedvaluesoftheprincipalcomponent
scoresforcentereddatax0arezero,andmultiplyingtheprincipalcomponentsbyaconstantwillproduce
rescaled principal components whose means are also zero. However, their variances will change by a
| factor ofthe | squareof | the scalingconstant. |     |     |     |     |
| ------------ | -------- | -------------------- | --- | --- | --- | --- |
Table13.3summarizestheeffectsofthreecommonscalingsoftheeigenvectorsonthepropertiesof
theprincipalcomponents.Thefirstrowindicatestheirpropertiesunderthescalingconventionjje
jj(cid:6)1
m
adoptedinthispresentation.Underthisscaling,theexpectedvalue(mean)ofeachoftheprincipalcom-
ponentsiszero(becauseitisthedataanomaliesx0thathavebeenprojectedontotheeigenvectors),and
thevarianceofeachisequaltotherespectiveeigenvalue,l .Thisresultissimplyanexpressionofthe
m
diagonalization of the variance–covariance matrix (Equation 11.56) produced by adopting the rigidly
rotated geometric coordinate system defined by the eigenvectors. When scaled in this way, the
TABLE13.3
ThreecommoneigenvectorscalingsusedinPCA;theirconsequencesforthe
propertiesoftheprincipalcomponents,u ;andtheirrelationshiptotheoriginalvariables,x ;and
|                                    |     |       | m       |                | k            |     |
| ---------------------------------- | --- | ----- | ------- | -------------- | ------------ | --- |
| thestandardizedoriginalvariables,z |     |       | k       |                |              |     |
| EigenvectorScaling                 |     | E(u ) | Var(u ) | Corr(u x )     | Corr(u z )   |     |
|                                    |     | m     | m       | m, k           | m, k         |     |
| ke k¼1                             |     | 0     | lm      | e k,m(lm)1/2/s | e k,m(lm)1/2 |     |
| m                                  |     |       |         | k              |              |     |
| ke mk¼(lm)1/2                      |     |       | 2       | e k,m/s        | e            |     |
|                                    |     | 0     | lm      | k              | k,m          |     |
| ke mk¼(lm)(cid:4)1/2               |     | 0     | 1       | e k,mlm/s      | e k,mlm      |     |
k

628 PART III MultivariateStatistics
correlation betweenaprincipalcomponentu andavariable x isgivenbyEquation13.7.Thecorre-
m k
lationbetweenu andthestandardizedvariablez isgivenbytheproductoftheeigenvectorelementand
m k
the square root ofthe eigenvalue, since the standarddeviation of astandardizedvariableis one.
Theeigenvectorssometimesarerescaledbymultiplyingeachelementbythesquarerootofthecor-
respondingeigenvalue.Thisrescalingproducesvectorsofdifferinglengths,jje jj(cid:6)(l )1/2,butwhich
m m
pointinexactlythesamedirectionsastheoriginaleigenvectorshavingunitlengths.Consistencyinthe
analysisformulaimpliesthattheprincipalcomponentsarealsochangedbythefactor(l )1/2,withthe
m
resultthatthevarianceofeachu increasestol 2.Amajoradvantageofthisrescaling,however,isthat
m m
theeigenvectorelementsaremoredirectlyinterpretableintermsoftherelationshipbetweentheprin-
cipal componentsand the original data.Underthisrescaling, each eigenvector elemente is numer-
k,m
ically equal to the correlation r between the mth principal component u and the kth standardized
u,z m
variable z .
k
ThelastscalingpresentedinTable13.3,resultinginjje jj(cid:6)(l ) –1/2,islesscommonlyused.This
m m
scalingisachievedbydividingeachelementoftheoriginalunit-lengtheigenvectorsbythesquarerootof
thecorrespondingeigenvalue.Theresultingexpressionforthecorrelationsbetweentheprincipalcom-
ponentsandtheoriginaldataismoreawkward,butthisscalinghastheadvantagethatalltheprincipal
componentshave equal, unit variance. This property can be usefulinthe detectionof outliers.
13.1.5. Connections to the Multivariate Normal Distribution
Thedistributionofthedatax,whosesamplecovariancematrix[S]isusedtocalculateaPCA,neednotbe
multivariate normal in order for the PCA to be valid. Regardless of the joint distribution of x, the
resultingprincipalcomponentsu willuniquelybethoseuncorrelatedlinearcombinationsthatsucces-
m
sivelymaximizetherepresentedfractionsofthevariancesonthediagonalof[S].However,ifinaddition
x(cid:7)N (m ,[S ]),thenaslinearcombinationsofthemultinormalx0s,thejointdistributionoftheprin-
K x x
cipal components willalsohave a multivariate normal distribution,
(cid:2) (cid:3)
u(cid:7)N ½E(cid:3)Tm ,½L(cid:3) : (13.10)
M x
Equation13.10isvalidbothwhenthematrix[E]containsthefullnumberM¼Kofeigenvectorsasits
columns,orsomefewernumber1(cid:8)M<K.Iftheprincipalcomponentsarecalculatedfromthecentered
data x0,then m ¼m ¼ 0.
u x0
Ifthejointdistributionofxismultivariatenormal,thenthetransformationofEquation13.2isarigid
rotationtotheprincipalaxesoftheprobabilityellipsesofthedistributionofx,yieldingtheuncorrelated
andmutuallyindependentu .WiththisbackgrounditisnotdifficulttounderstandEquations12.5and
m
12.34, which say that the distribution of Mahalanobis distances to the mean of a multivariate normal
distributionfollowsthew2 distribution.Onewaytoviewthew2 isasthedistributionofKsquaredinde-
K K
pendentstandardGaussianvariablesz2(seeSection4.4.5).CalculationoftheMahalanobisdistance(or,
k
equivalently,theMahalanobistransformation,Equation12.21)producesuncorrelatedvalueswithzero
meanandunitvariance,anda(squared)distanceinvolvingthemisthensimplythesumofthesquared
values.
ItwasnotedinSection12.3thataneffectivewaytosearchformultivariateoutlierswhenassessing
multivariatenormalityistoexaminethedistributionoflinearcombinationsformedusingeigenvectors
associated with the smallest eigenvalues of [S] (Equation 12.18). These linear combinations are, of
course,thelastprincipalcomponents.Figure13.3illustrateswhythisideaworks,intheeasilyvisualized

Chapter 13 Principal Component(EOF) Analysis 629
FIGURE13.3 Identificationofamultivariateoutlierbyexaminingthe
x
2 distributionofthelastprincipalcomponent.Theprojectionofthesingle
e
2 outlierontothefirsteigenvectoryieldsaquiteordinaryvalueforitsfirst
e principalcomponentu,butitsprojectionontothesecondeigenvector
1 1
yieldsaprominentoutlierinthedistributionoftheu values.
2
x
1
K¼2situation.ThepointscattershowsastronglycorrelatedpairofGaussianvariables,withonemul-
tivariateoutlier.Theoutlierisnotespeciallyunusualwithineitherofthetwounivariatedistributions,but
it stands out in two dimensions because it is inconsistent with the strong positive correlation of the
remaining points. Thedistributionofthe firstprincipal componentu , obtainedgeometricallybypro-
1
jectingthepointsontothefirsteigenvectore ,isatleastapproximatelyGaussian,andtheprojectionof
1
theoutlierisaveryordinarymemberofthisdistribution.Ontheotherhand,thedistributionofthesecond
principalcomponentu ,obtainedbyprojectingthepointsontothesecondeigenvectore ,isconcentrated
2 2
neartheoriginexceptforthesinglelargeoutlier.Otherthantheoutlier,thisdistributionisalsoapprox-
imatelyGaussian.Thisapproachiseffectiveinidentifyingthemultivariateoutlierbecauseitsexistence
has distorted the PCA only slightly, so that the leading eigenvector continues to be oriented in the
directionofthemaindatascatter.Becauseasmallnumberofoutlierscontributeonlyslightlytothefull
variability, it is the last (low-variance) principal components thatrepresent them.
13.2. APPLICATION OF PCA TO GEOPHYSICAL FIELDS
13.2.1. PCA for a Single Field
TheoverwhelmingmajorityofapplicationsofPCAtoatmosphericdatahaveinvolvedanalysesoffields
(i.e.,spatialarraysofvariables)suchasgeopotentialheights,temperatures,precipitation,andsoon.In
thesecasesthefulldatasetconsistsofmultipleobservationsofafieldorsetoffields.Frequentlythese
multiple observations take the form of time series, for example, a sequence of daily hemispheric 500
mbheightmaps.AnotherwaytolookatthiskindofdataisasacollectionofKmutuallycorrelatedtime
seriesthathavebeensampledateachofKgridpointsorstationlocations.ThegoalofPCAasappliedtothis
typeofdataisusuallytoexplore,ortoexpresssuccinctly,thejointspace/timevariationsofthemanyvari-
ablesinthedataset.
Eventhoughthelocationsatwhichthefieldissampledarespreadoveratwo-dimensional(orpos-
sibly three-dimensional) physical space, the data from these locations at a given observation time are
arranged in the K-dimensional vector x. That is, regardless of their geographical arrangement, each
locationisassignedanumber(asinFigure9.27)from1toK,whichreferstotheappropriateelement

630 PART III MultivariateStatistics
inthedatavectorx¼[x ,x ,x ,…,x ]T.InthismostcommonapplicationofPCAtofields,thedata
1 2 3 K
matrices[X]and[X0]arethusdimensioned(n(cid:1)K),or(time(cid:1)space),sincedataatKlocationsinspace
have been sampled at n successivetimes.
ToemphasizethattheoriginaldataconsistsofKtimeseries,theanalysisequation(13.1or13.2)is
sometimes writtenwith anexplicit time index:
uðtÞ¼½E(cid:3)Tx0, (13.11a)
t
or,inscalar form,
XK
u ðtÞ¼ e x0ðtÞ,m¼1,…,M: (13.11b)
m k,m k
k¼1
Herethetimeindextrunsfrom1ton.Thesynthesisequations(13.5or13.6)canbewrittenusingthe
samenotation,aswasdoneinEquation13.8.Equation13.11emphasizesthatifthedataxconsistofaset
oftimeseries,thentheprincipalcomponentsuarealsotimeseries.Thetimeseriesofoneoftheprincipal
components,u (t),mayverywellexhibitserialcorrelation(correlationwithitselfthroughtime),andthe
m
individual principal component time series are sometimes analyzed using the tools presented in
Chapter10.However,eachofthetimeseriesofprincipalcomponentswillbeuncorrelatedwiththetime
series ofall the otherprincipal components.
WhentheKelementsofxaremeasurementsatdifferentlocationsinspace,theeigenvectorscanbe
displayedgraphicallyinaquiteinformativeway.NoticethateacheigenvectorcontainsexactlyKele-
ments,andthattheseelementshaveaone-to-onecorrespondencewitheachoftheKlocationsinthedot
product from which the corresponding principal component is calculated (Equation 13.11b). Each
eigenvectorelemente canbeplottedonamapatthesamelocationasitscorrespondingdatavalue
k,m
x 0,andthisfieldofeigenvectorelementscanitselfbesummarizedusingsmoothcontoursinthesame
k
wayasanordinarymeteorologicalfield.Suchmapsdepictclearlywhichlocationsarecontributingmost
strongly to the respectiveprincipal components. Looked at another way, such maps indicate the geo-
graphic distribution of simultaneous data anomalies represented by the corresponding principal com-
ponents. These geographic displays of eigenvectors sometimes also are interpreted as representing
uncorrelatedmodesofvariabilityofthefieldsfromwhichthePCAwasextracted.Therearecaseswhere
thiskindofinterpretationcanbereasonable(butseeSection13.2.4foracautionarycounterexample),
particularlyfortheleadingeigenvector.However,becauseofthemutualorthogonalityconstraintson
the eigenvectors, strong interpretations of this sort are often not justified for the subsequent EOFs
(North, 1984).
Figure13.4showsthefirstfoureigenvectorsofaPCAofthecorrelationmatrixforwintermonthly
mean500mbheightsatgridpointsinthenorthernhemisphere.Thepercentagesbelowandtotherightof
thepanelsshowthefractionofthetotalhemisphericvariance(Equation13.4)representedbyeachofthe
corresponding principal components. Together, the first four principal components account for nearly
half of the (normalized) hemispheric winter height variance. These patterns resemble the teleconnec-
tivity patterns for the same data shown in Figure 3.33, and apparently reflect the same underlying
physical processes in the atmosphere. For example, Figure 13.4b evidently reflects the PNA pattern
ofalternatingheightanomaliesstretchingfromthePacificOceanthroughnorthwesternNorthAmerica
tosoutheasternNorthAmerica.Apositivevalueforthesecondprincipalcomponentofthisdatasetcor-
responds to negative 500 mb height anomalies (troughs) in the northeastern Pacific and in the south-
eastern United States, and to positive height anomalies (ridges) in the western part of the continent,

| Chapter | 13 Principal | Component(EOF) |      | Analysis |     |     |     | 631 |
| ------- | ------------ | -------------- | ---- | -------- | --- | --- | --- | --- |
|         | 120°E        |                | 60°E |          |     |     |     |     |
.6 0
.4 H
61
.4 L
73
| 180° |     |       |     | 0°  | 0   |       | L       |     |
| ---- | --- | ----- | --- | --- | --- | ----- | ------- | --- |
|      |     | NP BM |     |     |     | .4 NP | BM0 6 5 | 0°  |
−.4 0
|     |     | 0   |     | H   |        |      |     |     |
| --- | --- | --- | --- | --- | ------ | ---- | --- | --- |
|     | 0   |     |     | .64 | . L    |      |     |     |
|     |     |     |     |     | −. 6 6 | H    | 0   |     |
|     |     | H   |     |     |        | .7 5 | .4  |     |
.51 |     |     |     | 0   |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
−.4
L
−.67
120°w
| (a) |     |     | 16% |     | (b) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
14%
|     |     | H   |     |     |     | L   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
.7 6 −. 58
.4 |     |     |      | L   |     |     |     | L   |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     | −.63 |     |     |     |     | −.  |     |
|     |     | 0    |     |     |     | H   | 43  |     |
6 . 7 0
|     |     | −.4   |     |     | 0   |       | 0   |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- | --- |
|     | L   | NP BM |     | 0°  |     | 0 N P | BM  | 0°  |
−. 50
|     |     |     | H   |     | H   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 0   | .72 |     |     |     |     |     |
.37 .4
.4 0
H
|     | H   |     |     |     |     |     | .6 7 −.4 |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
.47 L
0 −.67
0
| (c) |     |     | 9%  |     | (d) |     | 9%  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
FIGURE 13.4 Spatial displays of the first four eigenvectors of gridded winter monthly mean 500 mb heights for the
northernhemisphere,1962–1977.ThisPCAwascomputedusingthecorrelationmatrixoftheheightdata,andscaledsothat
jje jj¼l1/2.Percentagevaluesbelowandtotherightofeachmapareproportionoftotalvariancex100%(Equation13.4).
m m
Thepatternsresembletheteleconnectivitypatternsforthesamedata(Figure3.33).FromWallaceandGutzler(1981).©American
MeteorologicalSociety.Usedwithpermission.
and over the central tropical Pacific. A negative value of the second principal component yields the
reverse pattern of anomalies,and a morezonal 500mb flow over NorthAmerica.
Principalcomponentanalysesaremostfrequentlystructuredasjustdescribed,bycomputingtheeigen-
valuesandeigenvectorsfromthe(K(cid:1)K)covarianceorcorrelationmatrixofthe(n(cid:1)K)datamatrix[X].
However,thisusualapproach,knownasS-modePCA,isnottheonlypossibility.Analternative,known
as T-mode PCA is based on the eigenvalues and eigenvectors of the (n(cid:1)n) covariance or correlation
[X]T.
matrix of the data matrix Thus in a T-mode PCA the eigenvector elements correspond to the
u
individual data samples (which often form a time series), and the principal components relate to
theKvariables(whichmaybespatialpoints),sothatthetwoapproachesportraydifferentaspectsofa

| 632 |     |     |     | PART III | MultivariateStatistics |
| --- | --- | --- | --- | -------- | ---------------------- |
datasetincomplementaryways.CompagnucciandRichman(2008)comparethesetwoapproachesfor
representing atmospheric circulation fields. The eigenvalues and eigenvectors produced by the two
approacheswillbedifferent,becausetheS-modeanomaliesarecomputedbysubtractingtheKcolumn
meansof[X],whereastheT-modeanomaliesarecomputedbysubtractingthenrowmeans,whichwillbe
thecolumnmeansof[X]T.AccordinglythenumberofnonzeroeigenvaluesinanS-modeanalysiswillbe
thesmallerofn–1andK,andthenumberofnonzeroeigenvaluesofaT-modeanalysiswillbethesmallerof
nandK–1.
| 13.2.2. Simultaneous | PCA | for Multiple | Fields |     |     |
| -------------------- | --- | ------------ | ------ | --- | --- |
It is also possible to apply PCA to vector-valued fields, which are fields with data for more than one
variable at each location or gridpoint. This kind of analysis is equivalent to simultaneous PCA of
two or more fields. If there are L such variables at each of the K gridpoints, then the dimensionality
ofthe datavector xisgivenbytheproductKL.ThefirstKelementsofxareobservations ofthe first
variable,thesecondKelementsareobservationsofthesecondvariable,andthelastKelementsofxwill
beobservationsoftheLthvariable.SincetheLdifferentvariablesgenerallywillbemeasuredinunlike
units,itwillalmostalwaysbeappropriatetobasethePCAofsuchdataonthecorrelationmatrix.The
dimensionof[R],andofthematrixofeigenvectors[E],willthenbe(KL(cid:1)KL).ApplicationofPCAto
thiskindofcorrelationmatrixwillproduceprincipalcomponentssuccessivelymaximizingthejointvar-
ianceoftheLstandardizedvariablesinawaythatconsidersthecorrelationsbothbetweenandamong
these variables at the K locations. This joint PCA procedure is sometimes called combined PCA,
| (CPCA), or | extended EOF (EEOF)analysis. |     |     |     |     |
| ---------- | ---------------------------- | --- | --- | --- | --- |
Figure 13.5 illustrates the structure of the correlation matrix (left) and the matrix of eigenvectors
(right) for PCA of vector field data. The first K rows of [R] contain the correlations between the first
of the L variables at these locations and all of the KL variables. Rows K+1 to 2K similarly contain
the correlations between the second of the L variables and all the KL variables, and so on. Another
way to look at the correlation matrix is as a collection of L2 submatrices, each dimensioned (K(cid:1)K),
which contain the correlations between sets of the L variables jointly at the K locations. The
submatrices located on the diagonal of [R] thus contain ordinary correlation matrices for each of the
}
|     | [R ] [R ] | [R 1,L] |     |     | F i rs t |
| --- | --------- | ------- | --- | --- | -------- |
1,1 1,2
|     |     |     | e e | e e e M | va ri a b le |
| --- | --- | --- | --- | ------- | ------------ |
|     |     |     | 1 2 | 3 4     |              |
}
Second
|       | [R 2,1 ] [R 2,2 ] | [R 2,L] |       |     |          |
| ----- | ----------------- | ------- | ----- | --- | -------- |
| [R] = |                   |         | [E] = |     | variable |
}
Lth
|     | [R ] [R  | [R L,L] |     |     |          |
| --- | -------- | ------- | --- | --- | -------- |
|     | L,1 L,2] |         |     |     | variable |
FIGURE13.5 IllustrationofthestructuresofthecorrelationmatrixandofthematrixofeigenvectorsforPCAofvectorfielddata.
ThebasicdataconsistofmultipleobservationsofLvariablesateachofKlocations,sothedimensionsofboth[R]and[E]are(KL(cid:1)KL).
Thecorrelationmatrixconsistsof(K(cid:1)K)submatricescontainingthecorrelationsbetweensetsoftheLvariablesjointlyattheKloca-
tions.Thesubmatriceslocatedonthediagonalof[R]aretheordinarycorrelationmatricesforeachoftheLvariables.Theoff-diagonal
submatricescontaincorrelationcoefficients,butarenotsymmetricandwillnotcontain1’sonthediagonals.Eacheigenvectorcolumn
of[E]similarlyconsistsofLsegments,eachofwhichcontainsKelementspertainingtotheindividuallocations.

Chapter 13 Principal Component(EOF) Analysis 633
Lvariables.Theoff-diagonalsubmatricescontaincorrelationcoefficientsbutarenotsymmetricandwill
not contain 10s on their diagonals. However, the overall symmetry of [R] implies that [R ] ¼ [R ]T.
i,j j,i
Similarly,eachcolumnof[E]consistsofLsegments,andeachofthesesegmentscontainstheKelements
pertaining toeach ofthe individual locations.
TheeigenvectorelementsresultingfromaPCAofavectorfieldcanbedisplayedgraphicallyina
mannerthatissimilartothemapsdrawnforordinaryscalarfields.Here,eachoftheLgroupsofKeigen-
vectorelementsiseitheroverlaidonthesamebasemaporplottedonseparatemaps.Figure13.6,from
theclassicpaperbyKutzbach(1967),illustratesthisprocessforthecaseofL¼2datavaluesateach
location.ThetwovariablesareaverageJanuarysurfacepressureandaverageJanuarytemperature,mea-
suredatK¼23locationsinNorthAmerica.Theheavylinesareananalysisofthe(first23)elementsof
thefirsteigenvectorthatpertaintothepressuredata,andthedashedlineswithshadingshowananalysis
of the temperature (second 23) elements of the same eigenvector. The corresponding principal com-
ponent accounts for 28.6%ofthe joint varianceof the KL¼ 23(cid:1)2¼ 46 standardizedvariables.
Inadditiontoeffectivelycondensingverymuchinformation,thepatternsshowninFigure13.6are
consistentwiththeunderlyingatmosphericphysicalprocesses.Inparticular,thetemperatureanomalies
areconsistentwithpatternsofthermaladvectionimpliedbythepressureanomalies.Ifthefirstprincipal
componentu ispositiveforaparticularJanuary,thesolidcontoursimplypositivepressureanomaliesin
1
thenorthandeast,withlowerthanaveragepressuresinthesouthwest.Onthewestcoast,thispressure
e PT
1
0
–10
20 0
–20
10
–10
–10 0 10 0
10 20
20
FIGURE13.6 Spatialdisplayoftheelementsofthefirsteigenvectorofthe(46(cid:1)46)correlationmatrixofaverageJanuarysea-
levelpressuresandtemperaturesat23locationsinNorthAmerica(dots).Thefirstprincipalcomponentofthiscorrelationmatrix
accountsfor28.6%ofthejoint(standardized)varianceofthepressuresandtemperatures.Heavylinesareahandanalysisofthesea-
levelpressureelementsofthefirsteigenvector,anddashedlineswithshadingareahandanalysisofthetemperatureelementsofthe
sameeigenvector.Thejointvariationsofpressureandtemperaturedepictedarephysicallyconsistentwithtemperatureadvectionin
responsetothepressureanomalies.FromKutzbach(1967).©AmericanMeteorologicalSociety.Usedwithpermission.

634 PART III MultivariateStatistics
patternwouldresultinweakerthanaveragewesterlysurfacewindsandstrongerthanaveragenortherly
surfacewinds.Theresultingadvectionofcoldairfromthenorthwouldproducecoldertemperatures,and
this cold advection is reflected by the negative temperature anomalies in this region. Similarly, the
patternofpressureanomaliesinthesoutheastwouldenhancesoutherlyflowofwarmairfromtheGulf
ofMexico,resultinginpositivetemperatureanomaliesasshown.Conversely,ifu isnegative,reversing
1
the signs of the pressure eigenvector elements implies enhanced westerlies in the west, and northerly
windanomaliesinthesoutheast,whichareconsistentwithpositiveandnegativetemperatureanomalies,
respectively. These temperature anomalies are indicated by the dashed contours and shading in
Figure 13.6,when their signs are also reversed.
Figure13.6isasimpleexampleinvolvingfamiliarvariables.Itsinterpretationiseasyandobviousif
weareconversantwiththeclimatologicalrelationshipsofpressureandtemperaturepatternsoverNorth
America in winter. However, the physical consistency exhibited in this example (where the "right"
answerisknownaheadoftime)isindicativeofthepowerofthiskindofPCAtouncovermeaningful
joint relationships among atmospheric (and other) fields in an exploratory setting, where clues about
possiblyunknownunderlyingphysicalmechanismsmaybehiddeninthecomplexrelationshipsamong
several fields.
Example 13.3 Characterizationof the Madden–Julian Oscillation
TheMadden–Julianoscillation(MJO,MaddenandJulian,1972)isatravellingpatternofenhancedand
suppressedtropicalconvectionthatpropagateseastwardfromthewesternIndiantotheeasternPacific
ocean basins on a one- to two-month timescale. It is a prominent element of subseasonal tropical
atmospheric variability that exhibits characteristic signatures in satellite-observed outgoing longwave
radiation (OLR, which is a proxy for cold, high convective cloud tops), coupled with upper- and
lower-tropospheric zonal (east-west) windconvergence and divergence.
MonitoringoftheMJOistypicallydoneusingadiagramderivedfromextendedEOFanalysisofOLR,
850mbzonalwindsand200mbzonalwinds,averagedbetween15°Sand15°N,asafunctionoflongitude
(WheelerandHendon,2004).Figure13.7showsthetwoleadingEOFsforthethreecombinedvariables.The
tracesforeachofthethreevariablesareshownasscalarfunctionsoflongituderatherthanasmapsbecause
north–southvariationshavebeencollapsedbythemeridionalaveraging.
It is notable that these two eigenvectors in Figure 13.7 have eigenvalues of comparable magnitude,
which are well separated from the magnitudes of the third and subsequent eigenvalues (see
Section13.4),andthatthetracesforeachofthethreevariablesareinapproximatequadrature(theloadings
forEOF2lagthoseinEOF1byapproximatelyaquartercycle).Thesecharacteristics,whicharespatialcoun-
terpartstothepropertiesthatcanemergefromPCAscomputedfortimeseries(Section13.7.1),allowthe
propagating nature of the MJO to be portrayed in a two-dimensional phase space defined by the corre-
spondingprincipalcomponents(Figure13.8).InthecontextoftheMJOdiagram,theseareconventionally
denoted as RMM1 and RMM2, respectively. The diagram is divided into octants, with Phase 1 corre-
sponding to convection over the western Indian ocean, and Phase 8 corresponding to convection over
theeasternPacific.AnMJOcycleisportrayedasdailypointsinthediagramtraceoutacounterclockwise
orbitinthisphasespace,anexampleofwhichforJanuarythroughMarchof2009isshowninFigure13.8.
Figure 13.9 shows compositesofDecember throughFebruaryOLR and 850 mbzonal windanomalies,
averaged over the eight MJO phases jointly defined by the two principal components in the Wheeler–
Hendon diagram (Figure 13.8), showing that the extended EOF analysis has been very effective at
portrayingthispropagatingphenomenon. e

| Chapter | 13 Principal Component(EOF) | Analysis |     | 635 |
| ------- | --------------------------- | -------- | --- | --- |
FIGURE13.7 TheleadingtwoEOFsfromanextendedEOFanalysisofOLR,850mbzonalwind,and200mbzonalwind,
averagedwithin15°oftheequator,asfunctionsoflongitude.FromWheelerandHendon(2004).©AmericanMeteorological
Society.Usedwithpermission.
| 13.2.3. | Scaling Considerations | and Equalization | of Variance |     |
| ------- | ---------------------- | ---------------- | ----------- | --- |
A complication arises in PCA of fields in which the geographical distribution of data locations is not
uniform (Baldwin et al., 2009; Karl et al., 1982; North et al., 1982). The problem is that the PCA
hasnoinformationaboutthespatialdistributionsofthelocations,oreventhattheelementsofthedata
vectorxmaypertaintodifferentlocations,butneverthelessfindslinearcombinationsthatmaximizethe
jointvariance.Regionsthatareoverrepresentedinx,inthesensethatdatalocationsareconcentratedin
that region, willtend to dominate the analysis, whereasdata-sparse regions will beunderweighted. In
contrast,thegoalofPCAongeophysicalfieldsisusuallytoapproximatetheintrinsicEOFs(Baldwin
et al., 2009;Northet al., 1982;Stephenson, 1997), which are properties ofthe actual underlying con-
| tinuous field(s), | andare independentofany | spatialsampling | pattern. |     |
| ----------------- | ----------------------- | --------------- | -------- | --- |

Jan
Feb
Weak
MJO
Mar
Phase 2 Phase 3
Dataavailableonaregularlatitude–longitudegridisacommoncauseofthisproblem.Inthiscasethe
numberofgridpointsperunitareaincreaseswithincreasinglatitudebecausethemeridiansconvergeatthe
poles,sothataPCAforthiskindofgriddeddatawillemphasizehigh-latitudefeaturesanddeemphasize
low-latitudefeatures.Oneapproachtogeographicallyequalizingthevariancesistomultiplythedataby
√cosf, where f is the latitude (North et al., 1982). The same effect can be achieved by multiplying
eachelementofthecovarianceorcorrelationmatrixbeinganalyzedby√cosf
k
√cosf‘,wherekand
‘aretheindicesforthetwolocations(orlocation/variablecombinations)correspondingtothatelement
ofthematrix.Thesquarerootsarenecessaryeventhoughtheareasthatareproportionaltothecosines
of the latitudes, because it is the variances and covariances of the analyzed quantities that need to be
equalizedforthePCA.Baldwinetal.(2009)formulatethisprocessmoregenerallybydefiningaweighting
matrix that can concisely represent the effects of different spatial sampling arrays. Of course these
rescalings must be reversed when recovering the original data from the principal components, as in
Equations13.5and13.6.Analternativeprocedureistointerpolateirregularlyornonuniformlydistributed
dataontoanequal-areagrid(AraneoandCompagnucci,2004;Karletal.,1982).Thislatterapproachis
alsoapplicablewhenthedatapertaintoanirregularlyspacednetwork,suchasclimatologicalobserving
stations.
UseofextendedEOFanalysisisnotlimitedtosettingsinvolvingmultiplevariablesatacommonsetof
locations.Aslightlymorecomplicatedscalingproblemariseswhenmultiplefieldswithdifferentspatial
8
esahP
1
esahP
Phase 7 Phase 6
Phase
5
Phase
4
636 PART III MultivariateStatistics
FIGURE13.8 AnexampleWheeler–Hendon(2004)diagram,definedbytheprincipalcomponentsRMM1andRMM2,corre-
spondingtotheleadingeigenvectorsshowninFigure13.7.ThecounterclockwisetraceindicatesprogressionoftheMJOduring
January(dotted),February(dashed),andMarch(solid),2009.ModifiedfromPeatmanetal.(2015).

Chapter 13 Principal Component(EOF) Analysis 637
FIGURE 13.9 Composites of December–January–February MJO conditions derived from the eight sectors defined in
Figure13.8,showingregionsofenhanced(shaded)andsuppressed(hatched)convection,andcorresponding850mbzonalwind
anomalies,asthephenomenonpropagatesfromwesttoeast.FromWheelerandHendon(2004).©AmericanMeteorological
Society.Usedwithpermission.

638 PART III MultivariateStatistics
resolutionsorspatialdomainsaresimultaneouslyanalyzedwithPCA.Hereanadditionalrescalingisnec-
essarytoequalizethesumsofthevariancesineachfield.Otherwisefieldswithmoregridpointswilldom-
inatethePCA,evenifallthefieldspertaintothesamegeographicarea.
13.2.4. Domain Size Effects: Buell Patterns
In addition to providing an efficient data compression, results of a PCA are sometimes interpreted in
termsofunderlyingphysicalprocesses.Forexample,thespatialeigenvectorpatternsinFigure13.4have
been interpreted as teleconnected modes of atmospheric variability, and the eigenvector displayed in
Figure13.6reflectstheconnectionbetweenpressureandtemperaturefieldsthatisexpressedasthermal
advection. The possibility that informative or at least suggestive interpretations may result can be a
strongmotivation for computinga PCA.
OneproblemthatcanoccurwhenmakingsuchinterpretationsofaPCAforfielddataariseswhenthe
spatialscale(oroneormoreoftheimportantspatialscales)ofthedatavariationsiscomparabletoor
largerthanthespatialdomainbeinganalyzed.Insuchcasesthespace/timevariationsinthedataarestill
efficiently represented by the PCA, and PCA is still a valid approach to data compression. But the
resulting spatial eigenvector patterns take on characteristic shapes that are nearly independent of the
underlyingvariationsinthedata.ThesecharacteristicshapesarecalledBuellpatterns,aftertheauthor
ofthe paper that first pointed outtheir existence (Buell,1979).
Consider, asanartificialbutsimpleexample,a5(cid:1)5array ofK¼25pointsrepresenting asquare
spatialdomain.Definethecorrelationsamongdatavaluesobservedatthesepointstobefunctionsonly
oftheirspatialseparationd,according tor(d)¼exp(–d/2).Theseparationsofadjacent pointsinthe
horizontalandverticaldirectionsared¼1,andsowouldexhibitcorrelationr(1)¼0.61;pointsadjacent
diagonallywouldexhibitcorrelationr(√2/2)¼0.49,andsoon.Thiscorrelationfunctionisshownin
Figure 13.10a. It is unchanging across the domain, and produces no spatiallydistinct features, orpre-
ferredpatternsofvariability.Itsspatialscaleiscomparabletothedomainsize,whichis4(cid:1)4distance
unitsverticallyand horizontally,correspondingtor(4) ¼ 0.14.
Eventhoughtherearenopreferredregionsofvariabilitywithinthe5(cid:1)5domain,theeigenvectorsof
theresulting(25(cid:1)25)correlationmatrix[R]appeartoindicatethatthereare.Thefirstoftheseeigen-
vectors,whichaccountsfor34.3%ofthevariance,isshowninFigure13.10b.Itappearstoindicategen-
erally in-phase variations throughout the domain, but with larger amplitude (greater magnitudes of
variability)nearthecenter.ThisfirstcharacteristicBuellpatternisanartifactofthemathematicsbehind
theeigenvectorcalculationifallthecorrelationsarepositiveanddoesnotmeritinterpretationbeyondits
suggestion thatthe scale ofvariation ofthedata iscomparable toorlarger thanthe sizeofthespatial
domain.
ThedipolepatternsinFigures13.10cand13.10darealsocharacteristicBuellpatternsandresultfrom
theconstraintofmutualorthogonalityamongtheeigenvectors.Theydonotreflect"dipoleoscillations"
or "seesaws" in the underlying data, whose correlation structure (by virtue of the way this artificial
examplehasbeenconstructed)ishomogeneousandisotropic.Herethepatternsareorienteddiagonally,
becauseoppositecornersofthissquaredomainarefurtherapartthanoppositesides,butthecharacter-
isticdipole pairsinthesecondand third eigenvectorsmight insteadhave been orientedverticallyand
horizontallyinadifferentlyshapeddomain.Noticethatthesecondandthirdeigenvectorsaccountfor
equal proportions of the variance, and so are actually oriented arbitrarily within the two-dimensional
space that they span (see Section 13.4). Additional Buell patterns are sometimes seen in subsequent
eigenvectors,the next ofwhich typically suggest tripole patterns ofthe form – +– or+ – +.

| Chapter | 13 Principal | Component(EOF) | Analysis |     | 639 |
| ------- | ------------ | -------------- | -------- | --- | --- |
EOF 1 (34.3%)
1.0
)d(r ,noitalerroC
0.5
0.0
|     |     | 0 2                        | 4 6 |               |     |
| --- | --- | -------------------------- | --- | ------------- | --- |
|     | (a) | Distance between points, d |     | (b)           |     |
|     |     | EOF 2 (11.7%)              |     | EOF 3 (11.7%) |     |
|     | (c) |                            |     | (d)           |     |
ArtificialexampleofBuellpatterns.Dataona5(cid:1)5squaregridwithunitverticalandhorizontalspatialsepa-
FIGURE13.10
rationexhibitcorrelationsaccordingtothefunctionoftheirspatialseparationsshownin(a).Panels(b)–(d)showthefirstthree
eigenvectorsoftheresultingcorrelationmatrix,displayedinthesame5(cid:1)5spatialarrangement.Theresultingsinglecentralhump
(b),andpairoforthogonaldipolepatterns(c)and(d),arecharacteristicartifactsofthedomainsizebeingcomparabletoorsmaller
thanthespatialscaleoftheunderlyingdatavariations.
| 13.3. TRUNCATION |              | OF THE PRINCIPAL | COMPONENTS  |     |     |
| ---------------- | ------------ | ---------------- | ----------- | --- | --- |
| 13.3.1.          | Why Truncate | the Principal    | Components? |     |     |
Mathematically,thereareasmanyeigenvectorsof[S]or[R]asthereareelementsofthedatavectorx,
providedK(cid:8)n–1.However,itistypical
|     |     |     | ofatmospheric | data thatsubstantialcovariances | (orcorrela- |
| --- | --- | --- | ------------- | ------------------------------- | ----------- |
tions)existamongtheoriginalKvariables,andasaresulttherearefewornooff-diagonalelementsof[S]
(or[R])thatarenearzero.Thissituationimpliesthatthereisredundantinformationinx,andthatthefirst
feweigenvectorsofitsdispersionmatrixwilllocatedirectionsinwhichthejointvariabilityofthedatais
greaterthanthevariabilityofanysingleelementofx.Similarly,thelastfeweigenvectorswillpointto
x
directions in the K-dimensional space of where the data jointly exhibit very little variation. This
propertywasillustratedinExample13.1fordailytemperaturevaluesmeasuredattwonearbylocations.
To the extent that there is redundancy in the original data x, it is possible to capture most of their
variance by considering only the most important directions of their joint variations. That is, most of
theinformationcontentofthedatamayberepresentedusingsomesmallernumberM<Koftheprin-
cipalcomponentsu m .Ineffect,theoriginaldatasetcontainingtheKvariablesx k isapproximatedbythe
smallersetofnewvariablesu .IfM<<K,retainingonlythefirstMoftheprincipalcomponentsresults
m
inamuchsmallerdataset.ThisdatacompressioncapabilityofPCAisoftenaprimarymotivationforits
use.IfM(cid:5)Kprincipalcomponentsarerequiredtocaptureausefullylargeproportionofthevariancein
| the original | data x there | is probablylittle | point tocomputinga | PCA. |     |
| ------------ | ------------ | ----------------- | ------------------ | ---- | --- |
The truncated representation of the original data can be expressed mathematically by a truncated
u
version of the analysis formula, Equation 13.2, in which the dimension of the truncated is (M(cid:1)1),
and [E] is the (nonsquare, K(cid:1)M) matrix whose columns consist only of the first M eigenvectors

640 PART III MultivariateStatistics
(i.e.,thoseassociatedwiththelargestMeigenvalues)of[S]or[R].Thecorrespondingsynthesisformula,
Equation13.6,isthenonlyapproximatelytruebecausetheoriginaldatacannotbeexactlyresynthesized
without using allKeigenvectors.
Whereistheappropriatebalancebetweendatacompression(choosingMtobeassmallaspossible)
andavoidingexcessiveinformationloss(truncatingonlyasmallnumber,K–M,oftheprincipalcom-
ponents)?Thereisnoclearcriterionthatcanbeusedtochoosethenumberofprincipalcomponentsthat
arebestretainedinagivencircumstance.Thechoiceofthetruncationlevelcanbeaidedbyoneormore
ofthemanyavailableprincipalcomponentselectionrules,butitisultimatelyasubjective choicethat
willdepend inpart on the data at hand andthe purpose(s)of the analysis.
13.3.2. Subjective Truncation Criteria
Someapproachestotruncatingprincipalcomponentsaresubjective,ornearlyso.Perhapsthemostbasic
criterionistoretainenoughoftheprincipalcomponentstorepresenta"sufficientfraction"ofthevariances
oftheoriginalx.Thatis,enoughprincipalcomponentsareretainedforthetotalamountofvariabilityrepre-
sentedtobelargerthansomecriticalvalue,
XM
R2 (cid:9)R2 , (13.12)
m crit
m¼1
whereR2 is defined asinEquation 13.4.Ofcourse the difficulty comes indetermininghowlargethe
m
fractionR2 mustbeinordertobeconsidered"sufficient."Ultimatelythiswillbeasubjectivechoice,
crit
informedbytheanalyst’sknowledgeofthedataathandandtheusestowhichtheywillbeput.Jolliffe
(2002) suggests that70% (cid:8)R2 (cid:8) 90%may oftenbe a reasonable range.
crit
Anotheressentiallysubjectiveapproachtoprincipalcomponenttruncationisbasedontheshapeof
thegraphoftheeigenvaluesl indecreasingorderasafunctionoftheirindexm¼1,…,K,knownas
m
theeigenvaluespectrum.Sinceeacheigenvaluemeasuresthevariancerepresentedinitscorresponding
principal component, this graph is analogous to the power spectrum (see Section 10.5.2), further
extending the parallels betweenEOF and Fourier analyses.
Plotting the eigenvalue spectrum with a linear vertical scale produces what is known as the scree
graph.Whenusingthescreegraphqualitatively,thegoalistolocateapointseparatingasteeplysloping
portiontotheleft,andamoreshallowlyslopingportiontotheright.Theprincipalcomponentnumberat
whichtheseparationoccursisthentakenasthetruncationcutoff,M.Thereisnoguaranteethattheeigen-
valuespectrumforagivenPCAwillexhibitasingleslopeseparation,orthatit(orthey)willbesuffi-
ciently abrupt to unambiguously locate a cutoff M. Sometimes this approach to principal component
truncation is called the scree "test," although this name implies more objectivityand theoretical justi-
fication than is warranted: the scree-slope criterion does not involve quantitative statistical inference.
Figure13.11ashowsthescreegraph(circles)forthePCAsummarizedinTable13.1b.Thisisarelatively
well-behaved example, in which the last three eigenvalues are quite small, leading to a fairly distinct
bendat K¼3, andso toatruncationafter the first M¼3 principal components wouldbe suggested.
Analternativebutsimilarapproachisbasedonthelog-eigenvaluespectrum,orlog-eigenvalue(LEV)
diagram.ChoosingaprincipalcomponenttruncationbasedontheLEVdiagramismotivatedbytheidea
that,ifthelastK–Mprincipalcomponentsrepresentuncorrelatednoise,thenthemagnitudesoftheireigen-
valuesshoulddecayexponentiallywithincreasingprincipalcomponentnumber.Thisbehaviorshouldbe
identifiableintheLEVdiagramasanapproximatelystraight-lineportiononitsright-handside.TheM

4 5.0
2.0
3
1.0
0.5
2
0.2
0.1
1
0.05
0 0.02
1 3 4 5 6 1 2 3 4 5 6
Principal component number Principal component number
retained principal components would then be the ones whose log-eigenvalues lie above the leftward
extrapolationofthisline.Asbefore,dependingonthedatasettheremayno,ormorethanone,quasi-linear
portions,andtheirlimitsmaynotbeclearlydefined.Figure13.11bshowstheLEVdiagramforthePCA
summarizedinTable13.1b.HereM¼3wouldprobablybechosenbymostviewersofthisLEVdiagram,
althoughthechoiceisnotunambiguous.
13.3.3. Rules Based on the Size of the Last Retained Eigenvalue
Another class of principal-component selection rules involves focusing on how small an “important”
eigenvalue can be. This set ofselection rulescan be summarized bythe criterion
T
XK
Retain l ifl > s , (13.13)
m m k,k
K
k¼1
wheres is the sample variance ofthe kth element ofx, andT is a threshold parameter.
k,k
Asimpleapplicationofthisidea,knownasKaiser’srule,involvescomparingeacheigenvalue(and
thereforethevariancedescribedbyitsprincipalcomponent)totheamountofthejointvariancereflected
by the average eigenvalue. Principal components whose eigenvalues are above this threshold are
retained. That is, Kaiser’s rule uses Equation 13.13 with the threshold parameter T ¼ 1. Jolliffe
(1972,2002)hasarguedthatKaiser’sruleistoostrict(i.e.,typicallyseemstodiscardtoomanyprincipal
components). He suggests that the alternative T ¼ 0.7 often will provide a roughly correct threshold,
which allows for the effectsof sampling variations.
eulavnegiE
Chapter 13 Principal Component(EOF) Analysis 641
2
(a) (b)
FIGURE13.11 Graphicaldisplaysofeigenvaluespectra,thatis,eigenvaluemagnitudesasafunctionoftheprincipalcomponent
number(heavierlinesconnectingcircledpoints),foraK¼6-dimensionalanalysis(seeTable13.1b):(a)Linearscaling,orscree
graph,(b)logarithmicscaling,orLEVdiagram.BoththescreeandLEVcriteriawouldleadtoretentionofthefirstthreeprincipal
componentsinthisanalysis.LighterlinesinbothpanelsshowresultsoftheresamplingtestsnecessarytoapplyRuleNofPrie-
sendorferetal.(1981).Dashedlineismedianofeigenvaluesfor1000(6(cid:1)6)dispersionmatricesofindependentGaussianvari-
ables,constructedusingthesamesamplesizeasthedatabeinganalyzed.Solidlinesindicatethe5thand95thpercentilesofthese
simulatedeigenvaluedistributions.RuleNwouldindicateretentionofonlythefirsttwoprincipalcomponents,onthegroundsthat
onlythesearesignificantlylargerthanwhatwouldbeexpectedfromdatawithnocorrelationstructure.

642 PART III MultivariateStatistics
Athirdalternativeinthisclassoftruncationrulesistousethebrokenstickmodel,socalledbecauseit
is based on the expected length of the mth longest piece of a randomly broken unit line segment.
According tothis criterion,the threshold parameterin Equation 13.13 is taken tobe
XK
1
TðmÞ¼ : (13.14)
j
j¼m
Thisruleyieldsadifferentthresholdforeachcandidatetruncationlevel,thatis,T¼T(m),sothatthe
truncationismadeatthesmallestmforwhichEquation13.13isnotsatisfied,accordingtothethreshold
inEquation 13.14.
AllofthethreecriteriadescribedinthissubsectionwouldleadtochoosingM¼2fortheeigenvalue
spectrum inFigure 13.11.
13.3.4. Rules Based on Hypothesis Testing Ideas
Facedwithasubjectivechoice among sometimesvagueandpossiblyconflicting truncationcriteria,itis
natural to hope for a more objective approach based on the sampling properties of PCA statistics.
Section13.4describessomelarge-sampleresultsforthesamplingdistributionsofeigenvalueandeigenvector
estimatesthathavebeencalculatedfrommultivariatenormalsamples.Basedontheseresults,Mardiaetal.
(1979)andJolliffe(2002)describetestsforthenullhypothesisthatthelastK–Meigenvaluesareallequal,and
socorrespondtonoisethatshouldbediscardedintheprincipalcomponenttruncation.Oneproblemwiththis
approachoccurswhenthedatabeinganalyzeddonothaveamultivariatenormaldistributionand/orarenot
independent,inwhichcaseinferencesbasedonthoseassumptionsmayproduceseriouserrors.Butamore
difficultproblemwiththisapproachisthatitusuallyinvolvesexaminingsequencesofteststhatarenotinde-
pendent:Arethelasttwoeigenvaluesplausiblyequal,andifso,arethelastthreeequal,andifso,arethelast
fourequal…?Thetruetestlevelforarandomnumberofcorrelatedtestswillbearanunknownrelationshipto
thenominallevelatwhicheachtestinthesequenceisconducted.Thisprocedurecanbeusedtochoosea
truncationlevel,butitwillbeasmucharuleofthumbastheotherpossibilitiesalreadypresentedinthissection,
andnotaquantitativechoicebasedonaknownsmallprobabilityforfalselyrejectinganullhypothesis.
Resampling counterparts to testing-based truncation rules have been used frequently with atmo-
spheric data. The most common of these is known as Rule N (Overland and Preisendorfer, 1982;
Preisendorfer et al., 1981). Rule N identifies the largest M principal components to be retained on
thebasisofasequenceofresamplingtestsinvolvingthedistributionofeigenvaluesofrandomlygen-
erateddispersionmatrices.Theprocedureinvolvesrepeatedlygeneratingsetsofvectorsofindependent
Gaussianrandomnumberswiththesamedimension(K)andsamplesize(n)asthedataxbeinganalyzed,
andthencomputingtheeigenvaluesoftheirdispersionmatrices.Theserandomlygeneratedeigenvalues
arethenscaledinawaythatmakesthemcomparabletotheeigenvaluesl tobetested,forexample,by
m
requiringthatthesumofeachsetofrandomlygeneratedeigenvalueswillequalthesumoftheeigen-
valuescomputedfromthedata.Eachl fromtherealdataisthencomparedtotheempiricaldistribution
m
ofits synthetic counterpartsand is retainedif it is larger than 95%ofthese.
Thelight lines inthepanels ofFigure13.11 illustrate the use of Rule Ntoselect aprincipal com-
ponenttruncationlevel.Thedashedlinesreflectthemediansof1000setsofeigenvaluescomputedfrom
1000(6(cid:1)6)dispersionmatricesofindependentGaussianvariables,constructedusingthesamesample
sizeasthedatabeinganalyzed.Thesolidlinesshow95thand5thpercentilesofthosedistributionsfor
eachofthesixeigenvalues.Thefirsttwoeigenvaluesl andl arelargerthanmorethan95%oftheir
1 2
synthetic counterparts, and accordingly, Rule Nwould choose M ¼2 for this data.

Chapter 13 Principal Component(EOF) Analysis 643
Atableof95%criticalvaluesforRuleN,forselectedsamplesizesnanddimensionsK,ispresented
in Overland and Preisendorfer (1982). Corresponding large-sample tables are given in Preisendorfer
et al. (1981) and Preisendorfer (1988). Preisendorfer (1988) notes that if there is substantial temporal
correlationpresentintheindividualvariablesx ,thatitmaybemoreappropriatetoconstructtheresam-
k
plingdistributionsforRuleN(ortousethetablesjustmentioned)usingthesmallesteffectivesample
size(e.g., Bretherton et al., 1999;Preisendorferet al., 1981)
1(cid:4)r2
n0(cid:5)n 1 (13.15)
1+r2
1
appropriatetoeigenvaluesandothersecondmomentquantitiesamongthex ,ratherthanusingninde-
k
pendentvectorsofGaussianvariablestoconstructeachsyntheticdispersionmatrix.Equation13.15is
analogoustoEquation5.12pertainingtoinferencesaboutmeans,butthesquaringofthelag-1autocor-
relationinEquation 13.15 rendersthe result muchlesssensitive toautocorrelation effects.
AnotherpotentialproblemwithRuleN,andothersimilarprocedures,isthatthedataxmaynotbe
approximatelyGaussian.Forexample,oneormoreofthex 0scouldbeprecipitationvariables.Tothe
k
extentthattheoriginaldataarenotGaussian,therandomnumbergenerationprocedurewillnotsimulate
accurately the underlying physical process, and the results of the test may be misleading. A possible
remedyfortheproblemofnon-GaussiandatamightbetouseabootstrapversionofRuleN,although
this approach seems nottohave been tried inthe literature todate.
TheprimaryweaknessoftheRuleNprocedurederivesfromthefactthatonlyitstestfortheleading
eigenvalueiscorrect.Thereasonisthat,havingrejectedthepropositionthatl isnotdifferentfromthe
1
others,theMonteCarlosamplingdistributionsfortheremainingeigenvaluesarenolongermeaningful
becausetheyareconditionalonallKeigenvaluesreflectingnoise.Thatis,thesesyntheticsamplingdis-
tributionswillimplytoomuchvarianceifithasbeeninferredthatl hasmorethanarandomshare,since
1
thesumoftheeigenvaluesisconstrainedtoequalthetotalvariance.Accordingly,Priesendorfer(1988)
notesthat Rule N tends toretain too fewprincipal components.
A better approach (Wilks, 2016c) is totest the sequence ofscaled eigenvalues
l
l∗¼ k , (13.16)
k
1
NX
rank
l
N (cid:4)k+1 k
rank i¼k
whereN ¼min(n–1,K)isthenumberofnonzeroeigenvalues.Equation13.16isthefractionofvar-
rank
iancerepresentedbyl whenthelargereigenvalueshavebeenomittedfromthedenominator,forwhich
k
analytic sampling distributions (Tracy and Widom, 1996) are available for sufficiently large n and K.
Good approximations to the right tails of these sampling distributions, which are different for each
l∗ , are provided by Pearson III distributions (Equation 4.55), with parameters
k
a¼46:4 (13.17a)
0:186s
b ¼ k (13.17b)
k maxðn ,K∗Þ
k
and
m (cid:4)9:85s
z ¼ k k , (13.17c)
k maxðn ,K∗Þ
k

| 644 |     |     | PART | III MultivariateStatistics |     |
| --- | --- | --- | ---- | -------------------------- | --- |
where
|     |     | (cid:2)pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi | pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi(cid:3) |     |     |
| --- | --- | ----------------------------------------------------------- | -------------------------------------------------------------- | --- | --- |
(cid:4)1=2+ K∗(cid:4)1=2 2
|     |     | m ¼ n |     |     | (13.18a) |
| --- | --- | ----- | --- | --- | -------- |
k k
and
  !
1=3
|     |     | pffiffiffiffiffi 1                                                                                                 | 1   |     |          |
| --- | --- | ------------------------------------------------------------------------------------------------------------------ | --- | --- | -------- |
|     |     | s ¼ m pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi+pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi |     |     | (13.18b) |
k k
n (cid:4)1=2 K∗(cid:4)1=2
k
| Tracy–Widom |     |     | K* K–k+1, | n–k+1. |     |
| ----------- | --- | --- | --------- | ------ | --- |
are the location and scale parameters, ¼ and n ¼ The sequence
k
of tests, k ¼ 1, 2,…,N are computed, each pertaining to the null hypothesis H :{l ¼l ¼
|     | rank |     |     | k   | k k+1 |
| --- | ---- | --- | --- | --- | ----- |
¼⋯¼l
l }thattheeigenvaluel andsmallereigenvaluesrepresentonlynoiseandsoareequal.
| k+2 Nrank |     | k   |     |     |     |
| --------- | --- | --- | --- | --- | --- |
ThetruncationpointMischosentobeonesmallerthanthefirstkforwhichH isnotrejected(i.e.,for
k
which l* is smaller than the 1–a quantile of the relevant Pearson III distribution defined by
k
| Equations 13.17and | 13.18).That      | is, |                          |     |         |
| ------------------ | ---------------- | --- | ------------------------ | --- | ------- |
|                    | M¼minðk2f1,2,…,N |     | (cid:4)1g:p >aÞ(cid:4)1, |     | (13.19) |
rank k
wherep isthepvaluepertainingtothekthtestandthenullhypothesisH .Thefirst(k¼1)ofthesetests
| k   |     |     | k   |     |     |
| --- | --- | --- | --- | --- | --- |
will be equivalent to the Rule N test for the first eigenvalue, but the subsequent tests account for the
larger-than-random fractions of variance in the lower indexed eigenvalues previously judged to be
significant.
Example 13.4 Principal Component TruncationUsingSequential Testing
Table13.1bpresentsthePCAcomputedfromthestandardizedJanuary1987datainTableA.1.Thescree
and LEV diagrams for the eigenvalues l are plotted in Figure 13.11, together with the Monte Carlo
k
distributions for Rule N. However, becausethe two leading eigenvalues clearly representmore of the
variancethanwouldtheircounterpartsderivedfrompurelyrandomdata,theRule-NMonteCarlodis-
tributionsforthetrailingeigenvaluesaretoolarge,whichmayleadtotoofeweigenvaluesbeingretained
according tothiscriterion.
Table13.4containstheinformationforthisproblemderivedfromEquations13.16–13.18,leadingtoa
sequenceofhypothesistestsallowingestimationofthetruncationpointM.Forthefirst(k¼1)ofthese
tests,l ¼l∗ becausetheaverageoverallsixeigenvalues(denominatorofEquation13.16)is1forthis
| k k                                         |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- |
| PCAbasedonacorrelationmatrix.Thequantity(l∗ |     |     | –z  |     |     |
)/b shouldbedistributedaccordingtoagamma
1 1 1
distribution with a ¼ 46.4 (Equation 13.17a) and b ¼ 1 if the null hypothesis that all the (underlying
generating-process) eigenvalues are equal, which is strongly rejected for the k ¼ 1 test. Similarly,
(l∗ –z )/b and (l∗ –z )/b are both on the far right tail of this gamma distribution, and so the null
| 2 2 2 | 3 3 3 |     |     |     |     |
| ----- | ----- | --- | --- | --- | --- |
hypothesesH andH arestronglyrejectedaswell.Thepvaluep ,forthek¼4test,isnotsmall,leading
| 2   | 3   |     | 4   |     |     |
| --- | --- | --- | --- | --- | --- |
toH beingthefirstnullhypothesisnotrejected,sothatthetruncationpointM¼3ischosenbythispro-
4
cedureaccordingtoEquation13.19.ThemoreconservativeRuleNprocedureretainsonlythefirsttwo
e
principalcomponents.
13.3.5. Rules Based on Structure in the Retained Principal Components
Thetruncationrulespresentedsofarallrelatetothemagnitudesoftheeigenvalues.Thepossibilitythat
physically important principal components need not have the largest variances (i.e., eigenvalues) has

Chapter 13 Principal Component(EOF) Analysis 645
TABLE13.4 QuantitiesfromEquations13.16–13.18AppliedtoTruncationofthePCAPresentedin
Table13.1b
k n K* m s b z l l* (l* –z )/b p Value
k k k k k k k k k k k
1 31 6 61.90 6.663 .04000 (cid:4).1203 3.532 3.532 91.31 8(cid:1)10(cid:4)8
2 30 5 57.04 6.561 .04068 (cid:4).2529 1.985 4.021 105.06 4(cid:1)10(cid:4)11
3 29 4 51.97 6.467 .04148 (cid:4).4045 0.344 2.849 78.43 3.7(cid:1)10(cid:4)5
4 28 3 46.58 6.396 .04249 (cid:4).5864 0.074 1.597 51.39 0.227
5 27 2 40.61 6.395 .04406 (cid:4).8289 0.038 1.169 45.34 0.543
motivatedaclassoftruncationrulesbasedonexpectedcharacteristicsofphysicallyimportantprincipal
componentseries(Preisendorferetal.,1981;Preisendorfer,1988).Sincemostatmosphericdatathatare
subjectedtoPCAaretimeseries(e.g.,timesequencesofspatialfieldsrecordedatKgridpoints),aplau-
sible hypothesis may be that principal components corresponding to physically meaningful processes
shouldexhibittimedependence,becausetheunderlyingphysicalprocessesareexpectedtoexhibittime
dependence.Preisendorferetal.(1981)andPreisendorfer(1988)proposedseveralsuchtruncationrules,
which test null hypotheses thatthe individual principal component time series are uncorrelated,using
eithertheirpowerspectraortheirautocorrelationfunctions.Thetruncatedprincipalcomponentsarethen
thoseforwhichthisnullhypothesisisnotrejected.Thisclassoftruncationruleseemstohavebeenused
very little inpractice.
13.4. SAMPLING PROPERTIES OF THE EIGENVALUES AND EIGENVECTORS
13.4.1. Asymptotic Sampling Results for Multivariate Normal Data
Principalcomponentanalysesarecalculatedfromfinitedatasamplesandareassubjecttosamplingvar-
iationsasanyotherstatisticalestimationprocedure.Thatis,werarelyifeverknowthetruecovariance
matrix[S]forthepopulationorunderlyinggeneratingprocess,butratherestimateitusingthesample
counterpart [S]. Accordingly the eigenvalues and eigenvectors calculated from [S] are also estimates
basedonthefinitesampleandarethussubjecttosamplingvariations.Understandingthenatureofthese
variations is quite important tocorrect interpretationof the results ofa PCA.
The equations presented in this section must be regarded as approximate, as they are asymptotic
(large-n)results,andarebasedalsoontheassumptionthattheunderlyingx’shaveamultivariatenormal
distribution.Itisalsoassumedthatnopairofthepopulationeigenvaluesareequal,implying(inthesense
tobeexplainedinSection13.4.2)thatallthepopulationeigenvectorsarewelldefined.Thevalidityof
theseresultsisthereforeapproximateinmostcircumstances,buttheyareneverthelessquiteusefulfor
understanding the nature of sampling effects on the uncertainty about estimated eigenvalues and
eigenvectors.
Eigenvalue Results
Thebasic resultforthesampling propertiesofestimated eigenvalues isthat,inthelimitofvery large
sample size, their sampling distributionis unbiased, and multivariate normal,

| 646 |     |     |      |               |               |         | PART III MultivariateStatistics |          |
| --- | --- | --- | ---- | ------------- | ------------- | ------- | ------------------------------- | -------- |
|     |     |     |      |               | (cid:2)       | (cid:3) |                                 |          |
|     |     |     | pffi | ffiffi(cid:7) | (cid:8)       |         |                                 |          |
|     |     |     |      | l^2l          | 0,2½L(cid:3)2 |         |                                 |          |
|     |     |     |      | n             | (cid:7)N      | ,       |                                 | (13.20a) |
K
or
|     |     |     |     |          | (cid:9)       | (cid:10) |     |          |
| --- | --- | --- | --- | -------- | ------------- | -------- | --- | -------- |
|     |     |     |     | l^       | 2             |          |     |          |
|     |     |     |     | (cid:7)N | l, ½L(cid:3)2 | :        |     | (13.20b) |
|     |     |     |     |          | K n           |          |     |          |
Herel^
isthe(K(cid:1)1)vectorofestimatedeigenvalues;lisitstruevalue;andthe(K(cid:1)K)matrix[L]2isthe
squareofthediagonal,populationeigenvaluematrix,havingelementsl 2.Because[L]2isdiagonalthe
k
sampling distributions for each of the K estimated eigenvalues are (approximately) independent uni-
| variate Gaussian | distributions, |     |      |                |            |         |     |          |
| ---------------- | -------------- | --- | ---- | -------------- | ---------- | ------- | --- | -------- |
|                  |                |     |      | (cid:2)        | (cid:3)    |         |     |          |
|                  |                |     | pffi | ffiffi         | (cid:7)    | (cid:8) |     |          |
|                  |                |     |      | ^              |            | 0,2l2   |     |          |
|                  |                |     |      | n l k (cid:4)l | k (cid:7)N | ,       |     | (13.21a) |
k
or
|     |     |     |     |            | (cid:9) | (cid:10) |     |          |
| --- | --- | --- | --- | ---------- | ------- | -------- | --- | -------- |
|     |     |     |     | ^          | 2       | :        |     |          |
|     |     |     |     | l (cid:7)N | l ,     | l2       |     | (13.21b) |
|     |     |     |     | k          | k n     | k        |     |          |
Equations13.20and13.21arelarge-sampleapproximations,andthereisabiasinthesampleeigen-
valuesforfinitesamplesize.Inparticular,thelargesteigenvalueswillbeoverestimated(willtendtobe
largerthantheirpopulationcounterparts)andthesmallesteigenvalueswilltendtobeunderestimated,
and these effects increase with decreasing sample size (Quadrelli et al., 2005; Von Storch and
Hannoschock, 1985). These biases can be understood as a consequence of the sorting of the sample
eigenvalues, so that the largest sample eigenvalue will be labeled as l regardless of the rank of its
1
generating-process counterpart, and similarly the smallest sample eigenvalue will be labeled as l .
K
The Monte Carlo Rule N distributions in Figure 13.11 illustrate the results of this phenomenon for a
small sample (n ¼ 31, K ¼ 6) situation where the true underlying eigenvalue spectrum is completely
| flat, with | all generating-process |     | l ¼1. |     |     |     |     |     |
| ---------- | ---------------------- | --- | ----- | --- | --- | --- | --- | --- |
k
UsingEquation13.21atoconstructastandardGaussianvariateprovidesanexpressionforthedis-
| tribution | of the relative | errorofthe | eigenvalue     |            | estimate,   |                    |     |         |
| --------- | --------------- | ---------- | -------------- | ---------- | ----------- | ------------------ | --- | ------- |
|           |                 |            | (cid:2)        | (cid:3)    |             |                    |     |         |
|           |                 | pffiffiffi |                |            | rffiffiffi  | !                  |     |         |
|           |                 |            | ^              |            |             | ^                  |     |         |
|           |                 |            | n l k (cid:4)l | k (cid:4)0 | n           | l (cid:4)l         |     |         |
|           |                 |            | pffiffiffi     |            |             | k k (cid:7)Nð0,1Þ: |     |         |
|           |                 | z¼         |                |            | ¼           |                    |     | (13.22) |
|           |                 |            |                | 2l         | 2           | l                  |     |         |
|           |                 |            |                | k          |             | k                  |     |         |
Equation 13.22implies
|     |     |     | ((cid:11)rffiffiffi  |            | !(cid:11)                       | )           |     |         |
| --- | --- | --- | -------------------- | ---------- | ------------------------------- | ----------- | --- | ------- |
|     |     |     | (cid:11)             | ^          | (cid:11)                        |             |     |         |
|     |     |     | (cid:11) n           | l (cid:4)l | (cid:11)                        |             |     |         |
|     |     |     | (cid:11)             | k          | k (cid:11)(cid:8)zð1(cid:4)a=2Þ |             |     |         |
|     |     | Pr  |                      |            |                                 | ¼1(cid:4)a, |     | (13.23) |
|     |     |     | (cid:11) 2           | l          | (cid:11)                        |             |     |         |
k
which leadstothe (1–a)(cid:10)100% confidenceinterval for the ktheigenvalue,
|             |         |                  | ^   |                                   |                        | ^   |                            |         |
| ----------- | ------- | ---------------- | --- | --------------------------------- | ---------------------- | --- | -------------------------- | ------- |
|             |         |                  | l   |                                   |                        | l   |                            |         |
|             |         |                  | k   | pffiffiffiffiffiffiffiffi(cid:8)l |                        | k   | pffiffiffiffiffiffiffiffi: |         |
|             |         |                  |     |                                   | k (cid:8)              |     |                            | (13.24) |
|             |         | 1+zð1(cid:4)a=2Þ |     | 2=n                               | 1(cid:4)zð1(cid:4)a=2Þ |     | 2=n                        |         |
| Eigenvector | Results |                  |     |                                   |                        |     |                            |         |
Theelementsofeachsampleeigenvectorareapproximatelyunbiased,andtheirsamplingdistributions
are approximately multivariate normal. But the variances of the multivariate normal sampling

| Chapter | 13 Principal | Component(EOF) |     | Analysis |     |     | 647 |
| ------- | ------------ | -------------- | --- | -------- | --- | --- | --- |
distributions for each of the eigenvectors depend on all the other eigenvalues and eigenvectors in a
somewhat complicated way. The sampling distributionfor the ktheigenvector is
|           |            |           |                    | ^e (cid:7)N | ðe  | ,½Ve (cid:3)Þ, | (13.25) |
| --------- | ---------- | --------- | ------------------ | ----------- | --- | -------------- | ------- |
|           |            |           |                    | k           | K k | k              |         |
| where the | covariance | matrixfor | thisdistributionis |             |     |                |         |
XK
|     |     |     |     | l            |      | l         |         |
| --- | --- | --- | --- | ------------ | ---- | --------- | ------- |
|     |     |     |     | ½Ve (cid:3)¼ | k    | i e eT :  | (13.26) |
|     |     |     |     | k            |      | Þ2 i i    |         |
|     |     |     |     | n            | ðl   | (cid:4) l |         |
|     |     |     |     |              | i6¼k | i k       |         |
ThesummationinEquation13.26involvesallKeigenvalue–eigenvectorpairs,indexedherebyi,except
thekthpair,forwhichthecovariancematrixisbeingcalculated.Itisasumofweightedouterproductsof
theseeigenvectors,andsoresemblesthespectraldecompositionofthetruecovariancematrix[S](cf.
Equation 11.53). But rather than being weighted only by the corresponding eigenvalues, as in
Equation11.53,theyareweightedalsobythereciprocalsofthesquaresofthedifferencesbetweenthose
eigenvalues,andtheeigenvaluebelongingtotheeigenvectorwhosecovariancematrixisbeingcalcu-
lated.Thatis,theelementsofthematricesinthesummationofEquation13.26willbequitesmall,except
forthosethatarepairedwitheigenvaluesl thatarecloseinmagnitudetotheeigenvaluel belongingto
|                 |               |            |              | i   |       | k           |     |
| --------------- | ------------- | ---------- | ------------ | --- | ----- | ----------- | --- |
| the eigenvector | whosesampling |            | distribution | is  | being | calculated. |     |
| 13.4.2.         | Effective     | Multiplets |              |     |       |             |     |
Equation 13.26, for the sampling uncertainty of the eigenvectors of a covariance matrix, has two
importantimplications.First,thepatternofuncertaintyintheestimatedeigenvectorsresemblesalinear
combination, or weighted sum, of all the other eigenvectors. Second, because the magnitudes of the
weights in this weighted sum are inversely proportional to the squares of the differences between the
correspondingeigenvalues,aneigenvectorwillberelativelypreciselyestimated(thesamplingvariances
willberelativelysmall)ifitseigenvalueiswellseparatedfromtheotherK–1eigenvalues.Conversely,
eigenvectorswhoseeigenvaluesaresimilarinmagnitudetooneormoreoftheothereigenvalueswill
exhibitlargesamplingvariations,andthosevariationswillbelargerfortheeigenvectorelementsthatare
| large inthe | eigenvectors | with | comparable | eigenvalues. |     |     |     |
| ----------- | ------------ | ---- | ---------- | ------------ | --- | --- | --- |
Thejointeffectofthesetwoconsiderationsisthatthesamplingdistributionsoftwo(ormore)eigen-
vectorshavingsimilareigenvalueswillbecloselyentangled.Theirsamplingvarianceswillbelarge,and
their patterns of sampling error will resemble the patterns of the eigenvector(s) with which they are
entangled. The net effect will be that a realization of the corresponding sample eigenvectors will be
a nearly arbitrary mixture of the true population counterparts. They will jointly represent the same
amountof variance (within the sampling boundsapproximated by Equation 13.21), butthis joint var-
iance will be arbitrarily mixed between (or among) them. Sets of such eigenvalue–eigenvector pairs
are called effectively degenerate multiplets or effective multiplets. Attempts at physical interpretation
| of such sample | eigenvectors |     | willbe frustratingif |     | nothopeless. |     |     |
| -------------- | ------------ | --- | -------------------- | --- | ------------ | --- | --- |
Thesourceofthisproblemcanbeappreciatedinthecontextofathree-dimensionalmultivariatenormal
distribution,inwhichoneoftheeigenvectorsisrelativelylarge,andthetwosmalleronesarenearlyequal.
TheresultingdistributionhasellipsoidalprobabilitycontoursresemblingthecucumbersinFigure12.3.The
eigenvectorassociatedwiththesinglelargeeigenvaluewillbealignedwiththelongaxisoftheellipsoid.But
thismultivariatenormaldistributionhas(essentially)nopreferreddirectionintheplaneperpendiculartothe
longaxis(exposedfaceontheleft-handcucumberinFigure12.3b).Anypairofperpendicularvectorsthat
arealsoperpendiculartothelongaxiscouldaseasilyjointlyrepresentvariationsinthisplane.Theleading

648 PART III MultivariateStatistics
eigenvectorcalculatedfromasamplecovariancematrixfromthisdistributionwouldbecloselyalignedwith
thetrueleadingeigenvector(longaxisofthecucumber)becauseitssamplingvariationswillbesmall.In
terms of Equation 13.26, both of the two terms in the summation would be small because l >> l (cid:5)
1 2
l .Ontheotherhand,eachoftheothertwoeigenvectorswouldbesubjecttolargesamplingvariations:
3
theterminEquation13.26correspondingtooneortheotherofthemwillbelarge,because(l –l ) –2will
2 3
belarge.Thepatternofsamplingerrorfore willresemblethetruegenerating-processe ,andviceversa.
2 3
Thatis,theorientationofthetwosampleeigenvectorsinthisplanewillbearbitrary,beyondtheconstraints
that they will be perpendicular to each other, and to e . The variationsrepresentedby each ofthese two
1
sampleeigenvectorswillaccordinglybeanarbitrarymixtureofthevariationsrepresentedbytheirtwopop-
ulationcounterparts.
13.4.3. The North et al. Rule of Thumb
Equations13.20and13.25,forthesamplingdistributionsoftheeigenvaluesandeigenvectors,dependon
thevaluesoftheirtruebutunknowncounterparts.Nevertheless,thesampleestimatesapproximatethe
truevalues,sothatlargesamplingerrorsareexpectedforthoseeigenvectorswhosesampleeigenvalues
areclosetoothersampleeigenvalues.Theideathatitispossibletodiagnoseinstanceswheresampling
variationsareexpectedtocauseproblemswitheigenvectorinterpretationinPCAwasexpressedasarule
ofthumb by North et al. (1982):
"Theruleissimplythatifthesamplingerrorofaparticulareigenvaluel[dl(cid:7)l(2/n)1/2]iscomparabletoor
largerthanthespacingbetweenlandaneighboringeigenvalue,thenthesamplingerrorsfortheEOFasso-
ciatedwithlwillbecomparabletothesizeoftheneighboringEOF.Theinterpretationisthatifagroupof
trueeigenvaluesliewithinoneortwodlofeachother,thentheyforman‘effectivelydegeneratemultiplet,’
andsampleeigenvectorsarearandommixtureofthetrueeigenvectors."
However, caution is warranted in quantitatively interpreting the degree of overlap of the confidence
intervals implied by the North et al. ruleof thumb (see Section 5.2.2).
Northetal.(1982)illustratedtheirruleofthumbwithaninstructiveexample.Theyconstructedsyn-
theticdatafromasetofknownEOFpatterns,thefirstfourofwhichareshowninFigure13.12a,together
withtheirrespectiveeigenvalues.Usingafullsetofsuchpatterns,thecovariancematrix[S]fromwhich
theycouldbeextractedwasassembledusingthespectraldecomposition(Equation11.53).Using[S]1/2
(seeSection11.3.4),realizationsofdatavectorsxfromadistributionwithcovariance[S]weregenerated
as in Section 12.4. Figure 13.12b shows the first four eigenvalue–eigenvector pairs calculated from a
sample of n¼ 300 such synthetic data vectors, and Figure 13.12c shows a realization of the leading
eigenvalue–eigenvector pairs for n¼1000.
TheleadingfourtrueeigenvectorpatternsinFigure13.12aarevisuallydistinct,buttheireigenvalues
arerelativelyclose.UsingEquation13.21bandn¼300,95%samplingintervalsforthefoureigenvalues
are 14.02 (cid:11) 2.24, 12.61 (cid:11) 2.02, 10.67 (cid:11) 1.71, and 10.43 (cid:11) 1.67 (because
F–1(0.975)
¼ 1.96), all of
which include the adjacent eigenvalues. Therefore it is expected according to the rule of thumb that
thesampleeigenvectorswillberandommixturesoftheirpopulationcounterpartsforthissamplesize,
andFigure13.12bbearsoutthisexpectation:thepatternsinthosefourpanelsappeartoberandommix-
turesofthefourpanelsinFigure13.12a.Evenifthetrueeigenvectorswereunknown,thisconclusion
would be expected from the North et al. rule of thumb, because adjacent sample eigenvectors in
Figure 13.12b are within twoestimated standarderrors, or2
d^
l ¼2
^
l(2/n)1/2 of each other.

| Chapter | 13 Principal Component(EOF) | Analysis |       |     |       | 649 |
| ------- | --------------------------- | -------- | ----- | --- | ----- | --- |
|         | 14.02                       |          | 13.76 |     | 13.75 |     |
|         | 12.61                       |          | 12.43 |     | 12.51 |     |
|         | 10.67                       |          | 11.15 |     | 11.24 |     |
|         | 10.48                       |          | 10.33 |     | 10.18 |     |
| (a)     |                             | (b)      |       | (c) |       |     |
FIGURE13.12 TheNorthetal.(1982)exampleforeffectivedegeneracy.(a)Firstfoureigenvectorsforthepopulationfrom
whichsyntheticdataweredrawn,withcorrespondingeigenvalues.(b)Thefirstfoureigenvectorscalculatedfromasampleof
n¼300,andthecorrespondingsampleeigenvalues.(c)Thefirstfoureigenvectorscalculatedfromasampleofn¼1000,and
thecorrespondingsampleeigenvalues.FromNorthetal.(1982).©AmericanMeteorologicalSociety.Usedwithpermission.
The situation is somewhat different for the larger sample size (Figure 13.12c). Again using
Equation13.21bbutwithn¼1000,the95%samplingintervalsforthefourgenerating-processeigen-
valuesare14.02(cid:11)1.22,12.61(cid:11)1.10,10.67(cid:11)0.93,and10.43(cid:11)0.91.Theseintervalsindicatethatthe
firsttwosampleEOFsshouldbereasonablydistinctfromeachotherandfromtheotherEOFs,butthat
the third and fourth eigenvectors will probably still be entangled. Applying the rule of thumb to the
sample eigenvalues in Figure 13.12c indicates that the separation between all adjacent pairs is close
to2d^ l.Theadditionalsamplingprecisionprovidedbythelargersamplesizeallowsanapproximation
to the first two true EOF patterns to emerge, although an even larger sample still would be required
beforethe sample eigenvectors wouldcorrespond well totheir population counterparts.
Thesyntheticdatarealizationsxinthisartificialexamplewerechosenindependentlyofeachother.If
the data being analyzed are serially correlated, the unadjusted rule of thumb will imply better
eigenvalue separation than is actually the case, because the variance of the sampling distribution of
2=n
the sample eigenvalues will be larger than 2 l (as given in Equation 13.21). The cause of this
k
discrepancyisthatthesampleeigenvaluesarelessconsistentfrombatchtobatchwhencalculatedfrom

650 PART III MultivariateStatistics
autocorrelateddata,sothequalitativeeffectisthesameaswasdescribedforthesamplingdistributionof
samplemeans,inSection5.2.4.However,theeffectivesamplesizeadjustmentinEquation13.15would
beappropriateinthiscase,whichimpliesamuchlessextremeeffectontheeffectivesamplesizethan
does Equation 5.12. Here r would correspond to the lag-1 autocorrelation for the corresponding
1
principal component time series when using Equation 13.21 or 13.24; and to the geometric mean of
the autocorrelation coefficients for the two corresponding principal component series, when using
Equation 13.26.
13.4.4. Bootstrap Approximations to the Sampling Distributions
TheconditionsspecifiedinSection13.4.1,oflargesamplesizeand/orunderlyingmultivariatenormal
data,maybetoounrealistictobepracticalinsomesituations.Insuchcasesitispossibletobuildgood
approximationstothesamplingdistributionsofsamplestatisticsusingthebootstrap(seeSection5.3.5).
BeranandSrivastava(1985)andEfronandTibshirani(1993)specificallydescribebootstrappingsample
covariancematricestoproducesamplingdistributionsfortheireigenvaluesandeigenvectors.Thebasic
procedure is to repeatedly resample the underlying data vectors x with replacement; to produce some
largenumber,n ,ofbootstrapsamples,eachofsizen.Eachofthen bootstrapsamplesyieldsaboot-
B B
strap realization of [S], whose eigenvalues and eigenvectors can be computed. Jointly these bootstrap
realizationsofeigenvaluesandeigenvectorsformreasonableapproximationstotherespectivesampling
distributions,whichwillreflectpropertiesoftheunderlyingdatathatmaynotconformtothoseassumed
inSection 13.4.1.
Becarefulininterpretingthesebootstrapdistributions.A(correctable)difficultyarisesfromthefact
thattheeigenvectorsaredetermineduptosignonly,sothatinsomebootstrapsamplesthecounterpartof
e mayverywellbe–e .Failuretorectifysucharbitrarysignswitcheswillleadtolargeandunwarranted
k k
inflationofthecomputedsamplingdistributionsfortheeigenvectorelements.Difficultiescanalsoarise
when resampling effective multiplets, because the random distribution of variance within a multiplet
may be different from resample to resample, so the resampled eigenvectors may not bear one-to-one
correspondences with their original sample counterparts. Finally, the bootstrap procedure destroys
any serial correlation that may be present in the underlying data, which would lead to unrealistically
narrowbootstrapsamplingdistributions.Themoving-blocksbootstrapcanbeusedforseriallycorrelated
data vectors (Wilks, 1997b) as well as scalars. Wang et al. (2014) provide an example using monthly
surface pressure data.
13.5. ROTATION OF THE EIGENVECTORS
13.5.1. Why Rotate the Eigenvectors?
There is a strong tendency to try to ascribe physical interpretations to PCA eigenvectors and the
corresponding principal components. The results shown in Figures 13.4 and 13.6 indicate that it can
bebothappropriateandinformativetodoso.However,theorthogonalityconstraintontheeigenvectors
(Equation 11.48) can lead to problems with these interpretations, especially for the second and
subsequentprincipalcomponents.Althoughtheorientationofthefirsteigenvectorisdeterminedsolely
bythedirectionofthemaximumvariationinthedata,subsequentvectorsmustbeorthogonaltoeach
higher-varianceeigenvector,regardlessofthenatureofthephysicalprocessesthatmayhavegivenrise
tothedata.Totheextentthatthoseunderlyingphysicalprocessesarenotindependent,interpretationof
thecorrespondingprincipalcomponentsasbeingindependentmodesofvariabilitywillnotbejustified
(North,1984).Thefirstprincipalcomponentmayrepresentanimportantmodeofvariabilityorphysical

Chapter 13 Principal Component(EOF) Analysis 651
process,butitmaywellalsoincludeaspectsofothercorrelatedmodesorprocesses.Thustheorthog-
onalityconstraintontheeigenvectorscanresultintheinfluencesofseveraldistinctphysicalprocesses
beingjumbled togetherina single principal component.
When physical interpretation rather than data compression is a primary goal of PCA, it is often
desirabletorotateasubsetoftheinitialeigenvectorstoasecondsetofnewcoordinatevectors.Usually
it is some number M of the leading eigenvectors (i.e., eigenvectors with largest corresponding eigen-
values) of the original PCA that are rotated, with M chosen using a truncation criterion such as those
discussedinSection13.3.Rotatedeigenvectorscanbelesspronetotheartificialfeaturesresultingfrom
theorthogonalityconstraintontheunrotatedeigenvectors,suchasBuellpatterns(Richman,1986).They
alsoappeartoexhibitbettersamplingproperties(Richman,1986;Chengetal.,1995)thantheirunrotated
counterparts. Alarge fraction ofthe review ofPCA by Hannachi et al. (2007) is devoted torotation.
Severalproceduresforrotatingtheoriginaleigenvectorsexist,butallseektoproducewhatisknownas
simplestructureintheresultinganalysis.Simplestructuregenerallyisunderstoodtohavebeenachievedifa
largefractionoftheelementsoftheresultingrotatedvectorsarenearzero,andfewoftheremainingelements
correspondtoelementsthatarenotnearzerointheotherrotatedvectors.Thedesiredresultisthateachrotated
vectorrepresentsmainlythefeworiginalvariablescorrespondingtotheelementsnotnearzero,andthatthe
representationoftheoriginalvariablesissplitbetweenasfewoftherotatedprincipalcomponentsaspos-
sible.SimplestructureaidsinterpretationofarotatedPCAtotheextentthatitallowsassociationofeach
rotatedeigenvectorwithasmallnumberoftheoriginalKvariableswhosecorrespondingeigenvectorele-
mentsarenotnearzero.
Followingrotationoftheeigenvectors,asecondsetofnewvariablesisdefined,calledrotatedprin-
cipalcomponents.Therotatedprincipalcomponentsareobtainedfromtheoriginaldataanalogouslyto
Equation 13.1 and 13.2, as the dotproducts of data vectors andthe rotated eigenvectors. They can be
interpreted as single-number summaries of the similarity between their corresponding rotated eigen-
vectorandadatavectorx.Dependingonthemethodusedtorotatetheeigenvectors,theresultingrotated
principal components may ormay not bemutuallyuncorrelated.
A price is paid for the improved interpretability and better sampling stability of the rotated eigen-
vectors.Onecostisthatthedominant-variancepropertyofPCAislost.Thefirstrotatedprincipalcom-
ponentisnolongerthatlinearcombinationoftheoriginaldatawiththelargestvariance.Thevariance
represented bythe originalunrotated eigenvectors is spread moreuniformlyamongthe rotated eigen-
vectors,sothatthecorrespondingeigenvaluespectrumisflatter.Alsolostiseithertheorthogonalityof
the eigenvectors,or the uncorrelatednessof the resulting principal components, orboth.
13.5.2. Rotation Mechanics
Rotated eigenvectors are produced as a linear transformation of a subset of M of the original K
eigenvectors,
h i
e
E ¼ ½E(cid:3) ½T(cid:3) , (13.27)
ðKxMÞ ðMxMÞ
ðKxMÞ
where[T]istherotationmatrix,andthematrixofrotatedeigenvectorsisdenotedbythetilde.If[T]is
orthogonal, that is, if [T][T]T ¼ [I], then the transformation Equation 13.27 is called an orthogonal
rotation.Otherwisetherotationiscalledoblique.
Richman (1986) lists 19 approaches to defining the rotation matrix [T] in order to achieve simple
structure, although his list is not exhaustive. However, by far the most commonly used approach is

652 PART III MultivariateStatistics
theorthogonalrotationcalledthevarimax(Kaiser,1958).Avarimaxrotationisdeterminedbychoosing
the elements of[T]to maximize
2 ! 3
XM
4
XK
e∗ 4 (cid:4) 1
XK
e∗ 2
2
5 , (13.28a)
k,m K k,m
m¼1 k¼1 k¼1
where
ee
e∗ ¼ k,m! , (13.28b)
k,m XM 1=2
ee2
k,m
m¼1
arescaledversionsoftherotatedeigenvectorelements.TogetherEquations13.28aand13.28bdefinethe
"normalvarimax,"whereasEquation13.28aalone,usingtheunscaledeigenvectorelementsee ,isknown
k,m
asthe"rawvarimax."Ineithercasethetransformationissoughtthatmaximizesthesumofthevariancesof
the(eitherscaledorraw)squaredrotatedeigenvectorelements,whichtendstomovethemtowardeither
theirmaximumorminimum(absolute)values(whichare0and1),andthustendstowardsimplestructure.
Thesolutionisiterativeandisastandardfeatureofmanystatisticalsoftwarepackages.
Theresultsofeigenvectorrotationcandependonhowmanyoftheoriginaleigenvectorsareselected
forrotation.Thatis,someoralloftheleadingrotatedeigenvectorsmaybedifferentif,say,M+1rather
thanMeigenvectorsarerotated(e.g.,O’LenicandLivezey,1988).Unfortunatelythereisoftennotaclear
answertothequestionofwhatthebestchoiceforMmightbe,andtypicallyanessentiallysubjectivechoice
ismade.SomeguidanceisavailablefromthevarioustruncationcriteriainSection13.3,althoughthese
maynotyieldauniqueanswer.Sometimesatrial-and-errorprocedureisused,whereMisincreasedslowly
untiltheleadingrotatedeigenvectorsarestable,thatis,insensitivetofurtherincreasesinM.Inanycase,
however,itmakessensetoincludeeitherall,ornone,oftheeigenvectorsmakingupaneffectivemultiplet,
sincejointlytheycarryinformationthathasbeenarbitrarilymixed.Jolliffe(1987,1989)suggeststhatit
maybehelpfultoseparatelyrotategroupsofeigenvectorswithineffectivemultipletsinordertomore
easilyinterprettheinformationthattheyjointlyrepresent.
Figure13.13comparesunrotatedandvarimax-rotatedPCAsforreconstructingspatialpatternsthat
areindependent(Figure13.13a)andoverlapping(Figure13.13b).Bothsyntheticexamplespertaintoa
30(cid:1)30-gridpointsquaredomain(K¼900),withn¼256.Theleftmostcolumnsineachpanelshowthe
threetruegenerating-processeigenvectors,thenonzerofeaturesofwhichinFigure13.13aarespatially
disjoint.Inthiscaseboththeunrotated(middlecolumn)androtated(rightmostcolumn)recoverthetrue
patterns well. Because the underlying spatial patterns of variability in the leftmost column of
Figure 13.13a already exhibit "simple structure," the unrotated and rotated solutions are equivalent
becausetherotationmatrix[T]inEquation13.27,implicitlyresultingfromEquation13.28,verynearly
equals the identity.
Thefeaturesintheunderlying"truth"eigenvectorsinFigure13.13bhaveoverlappingspatialextents,
andsocannotvaryindependently.TheunrotatedPCAinthemiddlecolumnofFigure13.13bisnotable
toseparatethethree.Herethefirstandthirdeigenvectorsincludeportionsoftheunderlyingvariabilityof
the second mode, and the second eigenvector includes influences from the first and third underlying
modes. In contrast, the varimax-rotated solution in the rightmost column of Figure 13.13b recovers
the three trueunderlying modes well.

| Chapter | 13 Principal | Component(EOF) | Analysis |       |     |      | 653 |
| ------- | ------------ | -------------- | -------- | ----- | --- | ---- | --- |
|         |              |                |          | TRUTH | EOF | REOF |     |
| TRUTH   |              | EOF            | REOF     |       |     |      |     |
| 1EDOM   |              |                |          | 1EDOM |     |      |     |
| 72%     |              | 72%            | 72%      | 44%   | 48% | 43%  |     |
| 2EDOM   |              |                |          | 2EDOM |     |      |     |
| 19%     |              | 19%            | 19%      | 33%   | 32% | 34%  |     |
| 3EDOM   |              |                |          | 3EDOM |     |      |     |
| 9%      |              | 9%             | 9%       |       |     |      |     |
|         |              |                |          | 23%   | 20% | 23%  |     |
| (a)     |              |                |          | (b)   |     |      |     |
FIGURE13.13 SyntheticexamplecomparingunrotatedandrotatedPCAswhenthreeunderlyingmodesofvariabilityare(a)
spatiallyindependent,and(b)spatiallyoverlappingandthusnonindependent.Thesquarespatialdomainconsistsof30gridpoints
ineachdirection,thecontourintervalis0.25,andareaswithnegativeeigenvectorloadingsareshaded.ModifiedfromLianand
Chen(2012).©AmericanMeteorologicalSociety.Usedwithpermission.
Figure13.14showsspatialdisplaysofthefirsttworotatedeigenvectorsofmonthlyaveragedhemi-
sphericwinter500mbheights.UsingthetruncationcriterionofEquation13.13withT¼1,thefirst19
eigenvectorsofthecorrelationmatrixforthesedatawererotated.ThetwopatternsinFigure13.14are
similartothefirsttwounrotatedeigenvectorsderivedfromthesamedata(seeFigure13.4aand13.4b),
although thesignshavebeen (arbitrarily)reversed.However,therotatedvectorsconformmoretothe
ideaofsimplestructureinthatmoreofthehemisphericfieldsarefairlyflat(nearzero)inFigure13.14,
andeachpanelemphasizes moreuniquelyaparticularfeatureofthevariabilityofthe500mbheights
correspondingtotheteleconnectionpatternsinFigure3.33.TherotatedvectorinFigure13.14afocuses
primarily on height differences in the northwestern and western tropical Pacific, called the western
Pacific teleconnection pattern. It thus represents variations in the 500 mb jet at these longitudes, with
positivevaluesofthecorrespondingrotatedprincipalcomponentindicatingweakerthanaveragewest-
erlies,and negativevalues indicatingthe reverse. Similarly,the PNA pattern stands outexceptionally
clearlyinFigure14.14b,wheretherotationhasseparateditfromtheeasternhemispherepatternevident
in Figure 13.4b.
Figure13.15showsschematicrepresentationsofeigenvectorrotationintwodimensions.Theupper
diagramsineachsectionrepresenttheeigenvectorsinthetwo-dimensionalplanedefinedbytheunder-
lying variables x and x , and the corresponding lower diagrams represent “maps” of the eigenvector
|     | 1   | 2   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
elementsplottedatthetwo“locations”x andx (thesearemeanttocorrespondtoreal-worldmapssuch
|     |     |     | 1 2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
as those shown in Figures 13.4 and13.14). Figure 13.15a illustrates the case of the originalunrotated
eigenvectors.Theleadingeigenvectore isdefinedasthedirectionontowhichaprojectionofthedata
1

| 654 |     |     |     |     |     |     |     | PART | III | MultivariateStatistics |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---------------------- | --- |
L
–90
0
0
| L   |     | H   |     |     |     |     | 60  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
–8 6
79
L
|     |     | 60  |     |     | –43 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | H   |     |     | 0   |     |
–87
| –60 |     |     |     |     |     | L   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
H
|     |     |     |     |     |     | –81 |     | –85 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
–60
0
H
–62
| (a) |     |     |     |     |     | (b) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Spatialdisplaysofthefirsttworotatedeigenvectorsofmonthlyaveragedhemisphericwinter500mbheights.
FIGURE13.14
ThedataarethesameasthoseunderlyingFigure13.4,buttherotationhasbetterisolatedthepatternsofvariability,allowinga
clearerinterpretationintermsoftheteleconnectionpatternsinFigure3.33.FromHorel(1981).©AmericanMeteorological
Society.Usedwithpermission.
|     |     | x   |     |     | ~   | x   |     |     | e~  | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 2   |     |     | e   | 2   |     |     |     | 2   |     |
|     |     | e   |     |     | 2   |     |     |     | 2   |     |     |
1
|     |     |     |     |     |     |     | e~  |     |     |     | e~  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
| 2   |     |     |     |     |     |     | 1   |     |     |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | x   |     |     |     | x   |     |     |     | x   |
|     |     |     | 1   |     |     |     | 1   |     |     |     | 1   |
|     | x   | x   |     |     | x   | x   |     |     | x   | x   |     |
|     | 1   | + 2 |     |     | 1   | 2   |     |     | + 1 | 2   |     |
+
|     | +   |     |     | ~   |     | +   |     | ~   |     | +   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e   |     |     |     | e   |     |     |     | e   |     |     |     |
| 1   |     |     |     | 1   |     |     |     | 1   |     |     |     |
|     | –   |     |     |     |     |     |     |     |     | +   |     |
+
|     |     | +   |     | ~   | –   |     |     | ~   | –   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e 2 |     |     |     | e   |     |     |     | e   |     |     |     |
|     |     |     |     | 2   |     |     |     | 2   |     |     |     |
| (a) |     |     |     | (b) |     |     |     | (c) |     |     |     |
FIGURE13.15 Schematiccomparisonof(a)unrotated,(b)orthogonallyrotated,and(c)obliquelyrotatedunit-lengtheigen-
vectorsinK¼2dimensions.Leftpanelsshoweigenvectorsinrelationtoscatterplotsofthedata,whichexhibittwogroupsor
modes.Rightpanelsshowschematictwo-pointmapsofthetwoeigenvectorsineachcase.AfterKarlandKoscielny(1982).
points(i.e.,theprincipalcomponents)hasthelargestvariance,whichlocatesacompromisebetweenthe
two clusters of points (modes). That is, it locates much of the variance of both groups, without really
characterizing either. The leading eigenvector e points in the positive direction for both x and x ,
|     |     |     |     |     | 1   |     |     |     |     |     | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
,sothecorrespondinge
butismorestronglyalignedtowardx 2 1 mapbelowshowsalargepositive“+”
forx ,andasmaller“+”forx .Thesecondeigenvectorisconstrainedtobeorthogonaltothefirst,andso
| 2   |     |     | 1   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correspondsto large negative x ,and mildly positive x ,as indicated inthe corresponding “map.”
|     |     |     | 1   |     |     | 2   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 13.15b represents orthogonally rotated eigenvectors. Within the constraint of orthogonality
they approximately locate the two point clusters, although the variance of the first rotated principal

| Chapter | 13 Principal | Component(EOF) |     | Analysis |     |     |     | 655 |
| ------- | ------------ | -------------- | --- | -------- | --- | --- | --- | --- |
componentisnolongermaximumsincetheprojectionsontoee ofthethreepointswithx <0arequite
|     |     |     |     |     |     | 1   | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
small.However,theinterpretationofthetwofeaturesisenhancedinthemapsofthetwoeigenvectors
| below,withee |     |     |     |     |     |     | ,whereasee |     |
| ------------ | --- | --- | --- | --- | --- | --- | ---------- | --- |
indicatinglargepositivex togetherwithmodestbutpositivex showslarge
|           | 1            |          |           | 1   |     |     | 2 2 |     |
| --------- | ------------ | -------- | --------- | --- | --- | --- | --- | --- |
| positivex | togetherwith | modestly | negativex |     | .   |     |     |     |
|           | 2            |          |           |     | 1   |     |     |     |
Finally,Figure13.15cillustratesanobliquerotation,wheretheresultingrotatedeigenvectorsareno
longerconstrainedtobeorthogonal.Accordinglytheyhavemoreflexibilityintheirorientationsandcan
| better accommodate |     | featuresin | the | data thatare | notorthogonal. |     |     |     |
| ------------------ | --- | ---------- | --- | ------------ | -------------- | --- | --- | --- |
13.5.3. Sensitivity of Orthogonal Rotation to Initial Eigenvector Scaling
An underappreciated aspect of orthogonal eigenvector rotation is that the orthogonality of the result
depends strongly on the scaling of the original eigenvectors before rotation (Jolliffe, 1995, 2002;
Mestas-Nun˜ez,2000).Thisdependenceisusuallysurprisingbecauseofthename"orthogonalrotation,"
whichderivesfromtheorthogonalityofthetransformationmatrix[T]inEquation13.27,thatis,[T]T[T]
¼[T][T]T¼[I].Theconfusioniscompoundedbecauseoftheincorrectassertioninanumberofpapers
that an orthogonal rotation produces both orthogonal rotated eigenvectors and uncorrelated rotated
principal components. At most one of these two results can be obtained by an orthogonal rotation,
butneitherwilloccurunlesstheeigenvectorsarescaledcorrectlybeforetherotationmatrixisapplied.
Because of the confusion about the issue, an explicit analysis of this counterintuitive phenomenon is
worthwhile.
Denote as [E] the possibly truncated (K(cid:1)M) matrix of eigenvectors of [S]. Because these eigen-
vectors are orthogonal (Equation 11.50) and are originally scaled to unit length, the matrix [E] is
orthogonal, and so satisfies Equation 11.44b. The resulting principal components can be arranged in
the matrix
|     |     |     |     | ½U(cid:3) | ¼ ½X(cid:3) | ½E(cid:3) , |     | (13.29) |
| --- | --- | --- | --- | --------- | ----------- | ----------- | --- | ------- |
|     |     |     |     | ðnxMÞ     | ðnxKÞ       | ðKxMÞ       |     |         |
eachofthenrowsofwhichcontainvaluesfortheMretainedprincipalcomponents,u
T.Asbefore,[X]
m
istheoriginaldatamatrixwhoseKcolumnscorrespondtothenobservationsoneachoftheoriginalK
variables.Theuncorrelatednessoftheunrotatedprincipalcomponentscanbediagnosedbycalculating
their covariancematrix,
ðn(cid:4)1Þ(cid:4)1½U(cid:3)T½U(cid:3)¼ðn(cid:4)1Þ(cid:4)1ð½X(cid:3)½E(cid:3)ÞT½X(cid:3)½E(cid:3)
ðMxMÞ
¼ðn(cid:4)1Þ(cid:4)1½E(cid:3)T½X(cid:3)T½X(cid:3)½E(cid:3)
|     |     |     |     |             | (cid:2) | (cid:3)                      |     | (13.30) |
| --- | --- | --- | --- | ----------- | ------- | ---------------------------- | --- | ------- |
|     |     |     |     | ¼½E(cid:3)T |         | ½E(cid:3)½L(cid:3)½E(cid:3)T |     |         |
½E(cid:3)¼½I(cid:3)½L(cid:3)½I(cid:3)
¼½L(cid:3):
Theu areuncorrelatedbecausetheircovariancematrix[L]isdiagonal,andthevarianceforeachu is
| m   |     |     |     |     |     |     |     | m   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
.ThestepsonthethirdlineofEquation13.30followfromthediagonalizationof[S]¼(n–1) –1[X]T[X]
l
m
| (Equation11.52a)and |     | the | orthogonality | ofthe | matrix | [E]. |     |     |
| ------------------- | --- | --- | ------------- | ----- | ------ | ---- | --- | --- |
Consider now the effectsofthe three eigenvector scalings listedinTable13.3on the results of an
orthogonalrotation.Inthefirstcase,theoriginaleigenvectorsarenotrescaledfromunitlength,sothe
| matrix of | rotated | eigenvectors | is simply |     |     |     |     |     |
| --------- | ------- | ------------ | --------- | --- | --- | --- | --- | --- |

656 PART III MultivariateStatistics
h i
|     |     |     |     | E e | ½E(cid:3) | ½T(cid:3) : | (13.31) |
| --- | --- | --- | --- | --- | --------- | ----------- | ------- |
¼
ðKxMÞðMxMÞ
ðKxMÞ
That these rotated eigenvectors are still orthogonal,as expected, can be shown by
h i h i
T
E e e ¼ð½E(cid:3)½T(cid:3)ÞT½E(cid:3)½T(cid:3)¼½T(cid:3)T½E(cid:3)T½E(cid:3)½T(cid:3)
E
(13.32)
¼½T(cid:3)T½I(cid:3)½T(cid:3)¼½T(cid:3)T½T(cid:3)¼½I(cid:3):
Thatis,theresultingrotatedeigenvectorsarestillmutuallyperpendicularandofunitlength.Thecor-
| respondingrotated |            | principal           | components | are          |                                                                               |                               |         |
| ----------------- | ---------- | ------------------- | ---------- | ------------ | ----------------------------------------------------------------------------- | ----------------------------- | ------- |
|                   |            |                     |            | h i          | h i                                                                           |                               |         |
|                   |            |                     |            | e            | e                                                                             |                               |         |
|                   |            |                     |            | U ¼½X(cid:3) | E                                                                             | ¼½X(cid:3)½E(cid:3)½T(cid:3), | (13.33) |
| andtheir          | covariance | matrix              | is         |              |                                                                               |                               |         |
|                   |            |                     |            | h i h i      |                                                                               |                               |         |
|                   |            | ðn(cid:4)1Þ(cid:4)1 |            | e T e        | ¼ðn(cid:4)1Þ(cid:4)1ð½X(cid:3)½E(cid:3)½T(cid:3)ÞT½X(cid:3)½E(cid:3)½T(cid:3) |                               |         |
|                   |            |                     |            | U U          |                                                                               |                               |         |
ðMxMÞ
¼ðn(cid:4)1Þ(cid:4)1½T(cid:3)T½E(cid:3)T½X(cid:3)T½X(cid:3)½E(cid:3)½T(cid:3)
(13.34)
(cid:2) (cid:3)
|     |     |     |     |     | ¼½T(cid:3)T½E(cid:3)T | ½E(cid:3)½L(cid:3)½E(cid:3)T |     |
| --- | --- | --- | --- | --- | --------------------- | ---------------------------- | --- |
½E(cid:3)½T(cid:3)
¼½T(cid:3)T½L(cid:3)½T(cid:3):
Thismatrixisnotdiagonal,reflectingthefactthattherotatedprincipalcomponentsarenolongeruncor-
related.Thisresultiseasytoappreciategeometrically,bylookingatscatterplotssuchasFigure13.1or
Figure13.3.Ineachofthesecasesthepointcloudisinclinedrelativetotheoriginal(x ,x )axes,andthe
1 2
angleofinclinationofthelongaxisofthecloudislocatedbythefirsteigenvector.Thepointcloudisnot
| inclinedinthe(e |     | ,e  |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- |
)coordinatesystemdefinedbythetwoeigenvectors,reflectingtheuncorrelatedness
1 2
of the unrotated principal components (Equation 13.30). But relative to any other pair of mutually
orthogonal axes in the plane, the points would exhibit some inclination, and therefore the projections
| ofthe data | onto | theseaxes | would | exhibit some | nonzero | correlation. |     |
| ---------- | ---- | --------- | ----- | ------------ | ------- | ------------ | --- |
ThesecondeigenvectorscalinginTable13.3,jje jj¼(l )1/2,iscommonlyemployed,andindeedis
|     |     |     |     |     |     | m m |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
thedefaultscalinginmanystatisticalsoftwarepackagesforrotatedprincipalcomponents.Inthenotation
ofthissection,employingthisscalingisequivalenttorotatingthescaledeigenvectormatrix[E][L]1/2,
| yielding | the matrix | ofrotated | eigenvectors |     |         |         |     |
| -------- | ---------- | --------- | ------------ | --- | ------- | ------- | --- |
|          |            |           |              | h i | (cid:2) | (cid:3) |     |
e ½E(cid:3)½L(cid:3)1=2
|     |     |     |     | E   | ¼   | ½T(cid:3): | (13.35) |
| --- | --- | --- | --- | --- | --- | ---------- | ------- |
Theorthogonalityofthe rotated eigenvectors inthis matrix can be checked with
|     |     |     | h i h | i (cid:2)                        |     | (cid:3)                          |     |
| --- | --- | --- | ----- | -------------------------------- | --- | -------------------------------- | --- |
|     |     |     | e T   | e ½E(cid:3)½L(cid:3)1=2½T(cid:3) |     | T ½E(cid:3)½L(cid:3)1=2½T(cid:3) |     |
E E ¼
|     |     |     |     | ¼½T(cid:3)T½L(cid:3)1=2½E(cid:3)T½E(cid:3)½L(cid:3)1=2½T(cid:3) |     |     | (13.36) |
| --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | ------- |
¼½T(cid:3)T½L(cid:3)1=2½I(cid:3)½L(cid:3)1=2½T(cid:3)¼½T(cid:3)T½L(cid:3)½T(cid:3):
Here the equality on the second line is valid because the diagonal matrix [L]1/2 is symmetric, so that
[L]1/2¼([L]1/2)T.Therotatedeigenvectorscorrespondingtothesecond,andfrequentlyused,scaling

| Chapter | 13 Principal | Component(EOF) |     | Analysis |     | 657 |
| ------- | ------------ | -------------- | --- | -------- | --- | --- |
inTable13.3arenotorthogonal,becausetheresultofEquation13.36isnotadiagonalmatrix.Neither
arethecorrespondingrotatedprincipalcomponentsindependent.Thiscanbeseenbymanipulatingtheir
| covariance | matrix, which       | is alsonot | diagonal,that          | is,                                     |                                         |     |
| ---------- | ------------------- | ---------- | ---------------------- | --------------------------------------- | --------------------------------------- | --- |
|            |                     | h          | i h i                  | (cid:2)                                 | (cid:3)                                 |     |
|            |                     | e          | T e                    |                                         | T                                       |     |
|            | ðn(cid:4)1Þ(cid:4)1 | U          | U ¼ðn(cid:4)1Þ(cid:4)1 | ½X(cid:3)½E(cid:3)½L(cid:3)1=2½T(cid:3) | ½X(cid:3)½E(cid:3)½L(cid:3)1=2½T(cid:3) |     |
ðMxMÞ
¼ðn(cid:4)1Þ(cid:4)1½T(cid:3)T½L(cid:3)1=2½E(cid:3)T½X(cid:3)T½X(cid:3)½E(cid:3)½L(cid:3)1=2½T(cid:3)
(cid:2) (cid:3)
|     |     |     | ¼½T(cid:3)T½L(cid:3)1=2½E(cid:3)T |                              | ½E(cid:3)½L(cid:3)1=2½T(cid:3) |     |
| --- | --- | --- | --------------------------------- | ---------------------------- | ------------------------------ | --- |
|     |     |     |                                   | ½E(cid:3)½L(cid:3)½E(cid:3)T | (13.37)                        |     |
¼½T(cid:3)T½L(cid:3)1=2½I(cid:3)½L(cid:3)½I(cid:3)½L(cid:3)1=2½T(cid:3)
¼½T(cid:3)T½L(cid:3)1=2½L(cid:3)½L(cid:3)1=2½T(cid:3)
¼½T(cid:3)T½L(cid:3)2½T(cid:3):
|                                           |     |     |     | jj¼(l –1/2,isusedrelativelyrarely,althoughitcan |     |     |
| ----------------------------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- |
| ThethirdeigenvectorscalinginTable13.3,jje |     |     |     | )                                               |     |     |
|                                           |     |     |     | m m                                             |     |     |
be convenientinthatit yields unit variancefor all theprincipal componentsu . Theresulting rotated
m
| eigenvectors | are not orthogonal,so |       | thatthe                                                                       | matrix product                        |         |     |
| ------------ | --------------------- | ----- | ----------------------------------------------------------------------------- | ------------------------------------- | ------- | --- |
|              |                       | h i h | i (cid:2)                                                                     | (cid:3)                               |         |     |
|              |                       | e T   | e                                                                             | T                                     |         |     |
|              |                       | E     | E ¼ ½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3)                                     | ½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3) |         |     |
|              |                       |       | ¼½T(cid:3)T½L(cid:3)(cid:4)1=2½E(cid:3)T½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3) |                                       | (13.38) |     |
¼½T(cid:3)T½L(cid:3)(cid:4)1=2½I(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3)¼½T(cid:3)T½L(cid:3)(cid:4)1½T(cid:3),
is not diagonal. However, the resulting rotated principal components are uncorrelated since their
| covariance | matrix,             |     |                          |                                                |                                                  |     |
| ---------- | ------------------- | --- | ------------------------ | ---------------------------------------------- | ------------------------------------------------ | --- |
|            |                     | h i | h i                      | (cid:2)                                        | (cid:3)                                          |     |
|            | ðn(cid:4)1Þ(cid:4)1 | e   | T e ¼ðn(cid:4)1Þ(cid:4)1 | ½X(cid:3)½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3) | T ½X(cid:3)½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3) |     |
U U
ðMxMÞ
¼ðn(cid:4)1Þ(cid:4)1½T(cid:3)T½L(cid:3)(cid:4)1=2½E(cid:3)T½X(cid:3)T½X(cid:3)½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3)
(13.39)
(cid:2) (cid:3)
|     |     |     | ¼½T(cid:3)T½L(cid:3)(cid:4)1=2½E(cid:3)T | ½E(cid:3)½L(cid:3)½E(cid:3)T | ½E(cid:3)½L(cid:3)(cid:4)1=2½T(cid:3) |     |
| --- | --- | --- | ---------------------------------------- | ---------------------------- | ------------------------------------- | --- |
¼½T(cid:3)T½I(cid:3)½I(cid:3)½T(cid:3)¼½T(cid:3)T½T(cid:3)¼½I(cid:3),
is diagonal, and also reflects unit variancesfor allthe rotated principal components.
Mostfrequentlyinmeteorologyandclimatology,theeigenvectorsinaPCAdescribespatialpatterns,
andtheprincipalcomponentsaretimeseriesreflectingtheimportanceofthecorrespondingspatialpat-
ternsintheoriginaldata.Whencalculatingorthogonallyrotatedprincipalcomponentsinthiscontext,we
canchoosetohaveeitherorthogonalrotatedspatialpatternsbutcorrelatedrotatedprincipalcomponent
time series (by using jje jj ¼ 1), or nonorthogonal rotated spatial patterns whose time sequences are
m
mutuallyuncorrelated(byusingjje jj¼(l ) –1/2),butnotboth.Itisnotclearwhattheadvantageofhaving
|     |     |     | m   | m   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
jj¼(l
neitherproperty(usingjje )1/2,asisoftendone)mightbe.Differencesintheresultsforthedif-
m m
ferentscalingswillbesmallifsetsofeffectivemultipletsarerotatedseparately,becausetheireigenvalues
willnecessarilybesimilarinmagnitude,resultinginsimilarlengthsforthescaledeigenvectors.

658 PART III MultivariateStatistics
13.5.4. Simple Structure Through Regularization
Aquitedifferentapproachtoachievingsimplestructure,sothatfewoftheeigenvectorloadingsinPCA
areappreciablydifferentfromzero,isthroughLassoregularization(Tibshirani,1996).UseoftheLasso
forregularizationofleast-squaresregression,whichimposesabudgetonthesumofabsolutevaluesfor
theregressioncoefficients,wasdiscussedinSection7.5.2.Theresultisthat,astheceilingconthesumof
absolutevaluesoftheregressioncoefficientsisdecreased,moreofthemareprogressivelydriventozero.
AsimilarapproachcanbetakeninPCA(Jolliffeetal.,2003),inwhichcasetheconstraintcanbe
expressedas
XK
je j(cid:8)c,c>1, (13.40)
k,m
k¼1
foreacheigenvectore .Jolliffeetal.(2003)namedtheapproachSimplifiedComponentTechnique—
m
LASSO,orSCoTLASS.Forc¼1themethodyieldsexactlyonenonzeroloadingine ,andsoproduces
m
regularized eigenvectors that are exactly aligned with the original coordinate axes. Unconstrained
ordinaryPCAisproducedwhenc(cid:9)√K.For1<c(cid:8)√Ktheresultingeigenvectorsareorthogonal,
andsostilldefinearigidrotationofthecoordinateaxes,butthedataprojectionsontothem(theregu-
larized principal components) are notuncorrelated.
Of course the results will depend on the regularization parameter c, the choice of which is more
ambiguous for PCA than in the regression setting because predictive cross-validation will in general
notbeavailable.Smallervaluesoftheregularizationparameterproducemoreloadingsthatareexactly
zero,butsimultaneouslythefractionofvariancerepresenteddecreasesandthecorrelationsamongthe
regularizedprincipal components increase.Jolliffe et al. (2003) suggest recomputation using multiple
values of the regularization parameter, and then choosing c subjectively, perhaps on the basis of the
problem-specificinterpretabilityoftheresultingregularizedeigenvectors.Computationofregularized
PCAismoredifficultthanitsconventionalcounterpartandmayinvolvemultiplelocalminimainthe
numerical optimization. More detailscan befound inHastie et al. (2015) and Jolliffe et al. (2003).
13.6. COMPUTATIONAL CONSIDERATIONS
13.6.1. Direct Extraction of Eigenvalues and Eigenvectors from [S]
Thesamplecovariancematrix[S]isrealandsymmetric,andsowillalwayshavereal-valuedandnonneg-
ativeeigenvalues.Standardandstablealgorithmsareavailabletoextracttheeigenvaluesandeigenvectors
fromreal,symmetricmatrices(e.g.,Pressetal.,1986),andthisapproachcanbeaverygoodoneforcom-
putingaPCA.Asnotedearlier,itissometimespreferabletocalculatethePCAusingthecorrelationmatrix
[R],whichisalsothecovariancematrixforthestandardizedvariables.Thecomputationalconsiderations
presentedinthissectionareequallyappropriatetoPCAbasedonthecorrelationmatrix.
Onepracticaldifficultythatcanariseisthattherequiredcomputationaltimeincreasesveryquickly
as the dimension of the covariance matrix increases. A typical application of PCA in meteorology or
climatologyinvolvesafieldobservedatKgrid-orotherspace-points,atasequenceofntimes,where
K>>n.Thetypicalconceptualizationisintermsofthe(K(cid:1)K)covariancematrix,whichisverylarge—
it is not unusual for K to include thousands of gridpoints. Hours of computation may be required to
extract this many eigenvalue–eigenvector pairs. Yet since K > n–1 the sample covariance matrix is

| Chapter | 13 Principal | Component(EOF) | Analysis |     |     | 659 |
| ------- | ------------ | -------------- | -------- | --- | --- | --- |
singular, implying that the last K–n+1 of its eigenvalues are exactly zero. It is pointless to calculate
numerical approximationsto these zero eigenvalues andtheir associated arbitraryeigenvectors.
Inthissituationfortunatelyitispossibletofocusthecomputationaleffortonthennonzeroeigen-
values and their associated eigenvectors, using a computational trick (Von Storch and Hannosch€ock,
1984). Recall that the (K(cid:1)K) covariance matrix [S] can be computed from the centered data matrix
[X0] using Equation 11.30. Reversing the roles of the time and space points (although it is still the
columnsoftheanomalymatrix[X0]thathavezeromean),wealsocancomputethe(n(cid:1)n)covariance
matrix
1
|     |     |     | ½S∗(cid:3) ¼ | ½X0(cid:3) ½X0(cid:3) T: |     | (13.41) |
| --- | --- | --- | ------------ | ------------------------ | --- | ------- |
n(cid:4)1
|                                                         |     |     | ðnxnÞ | ðnxKÞ ðKxnÞ |     |     |
| ------------------------------------------------------- | --- | --- | ----- | ----------- | --- | --- |
| Both[S]and[S*]havethesamemin(n–1,K)nonzeroeigenvalues,l |     |     |       |             | ¼l∗ |     |
,sotherequiredcomputa-
k k
tionaltimemaybemuchshorteriftheyareextractedfromthesmaller(n(cid:1)n)matrix[S*],andthislatter
K>>
| computation | will bemuch | faster | inthe usual | situationwhere | n.  |     |
| ----------- | ----------- | ------ | ----------- | -------------- | --- | --- |
Theeigenvectorsof[S]and[S*]aredifferent,buttheleadingn–1(i.e.,themeaningful)eigenvectors
| of [S] can | be computed | fromthe | eigenvectors | e ∗ of[S*]using |     |     |
| ---------- | ----------- | ------- | ------------ | --------------- | --- | --- |
k
½X0(cid:3)Te∗
|     |     |     | e ¼(cid:12)                    | k(cid:12) ,k¼1,…,n(cid:4)1: |     |         |
| --- | --- | --- | ------------------------------ | --------------------------- | --- | ------- |
|     |     |     | (cid:12) ½X0(cid:3)Te∗(cid:12) |                             |     | (13.42) |
k
k
Thedimensionsofthemultiplicationsinbothnumeratoranddenominatorare(K(cid:1)n)(n(cid:1)1)¼(K(cid:1)1),
e
and the role ofthe denominator is to ensure thatthe resulting k have unitlength.
| 13.6.2. | PCA via | SVD |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
TheeigenvaluesandeigenvectorsinaPCAcanalsobecomputedusingtheSVD(singularvaluedecom-
position)algorithm(Section11.3.5),intwoways.First,asillustratedinExample11.5,theeigenvalues
–1/2[X0],
andeigenvectorsofacovariancematrix[S]canbecomputedthroughSVDofthematrix(n–1)
[X0]
where the centered (n(cid:1)K) data matrix is related to the covariance matrix [S] through
(n–1) –1/
Equation 11.30. In this case, the eigenvalues of [S] are the squares of the singular values of
2[X0]—that is, l ¼o 2—and the eigenvectors of [S] are the same as the right singular vectors of
k k
| (n–1) –1/2[X0]—that |     |                 | e ¼r |     |     |     |
| ------------------- | --- | --------------- | ---- | --- | --- | --- |
|                     |     | is, [E] ¼[R],or | .    |     |     |     |
k k
An advantage of using SVD to compute a PCA in this way is that the left singular vectors (the
columns of the (n(cid:1)K) matrix [L] in Equation 11.72) are proportional to the principal components
|     |     |     |     | x0  | e   |     |
| --- | --- | --- | --- | --- | --- | --- |
(i.e., tothe projectionsof the centered data vectors onto the eigenvectors ). Inparticular,
|     |     |        |                                 | i                | k        |          |
| --- | --- | ------ | ------------------------------- | ---------------- | -------- | -------- |
|     |     |        | pffiffiffiffiffiffiffiffiffiffi | pffiffiffiffiffi |          |          |
|     |     | ¼eTx0¼ | n(cid:4)1‘                      | i¼1,…,n,         | k¼1,…,K; |          |
|     |     | u      |                                 | l ,              |          | (13.43a) |
|     |     | i,k k  | i                               | i,k k            |          |          |
or
pffiffiffiffiffiffiffiffiffiffi
1=2:
|     |     |     | ½U(cid:3) ¼ | n(cid:4)1 ½L(cid:3) ½L(cid:3) |     | (13.43b) |
| --- | --- | --- | ----------- | ----------------------------- | --- | -------- |
|     |     |     | ðnxKÞ       | ðnxKÞðKxKÞ                    |     |          |
Herethematrix[U]isusedinthesamesenseasinSection13.5.3,thatis,eachofitsKcolumnscontains
the principal component series u corresponding tothe sequence of ndata valuesx, i¼ 1,…,n.
k i
The SVD algorithm can also be used to compute a PCA by operating on the covariance matrix
directly.Comparingthespectraldecompositionofasquare,symmetricmatrix(Equation11.52a)with
itsSVD(Equation11.72),itisclearthattheseuniquedecompositionsarethesame.Inparticular,sincea

660 PART III MultivariateStatistics
covariancematrix[S]issquareandsymmetric,boththeleftandrightmatricesofitsSVDareequal,and
containtheeigenvectors,thatis,[E]¼[L]¼[R].Inaddition,thediagonalmatrixofsingularvaluesis
| exactly the | diagonal matrix | ofeigenvalues, | [L]¼[O]. |     |
| ----------- | --------------- | -------------- | -------- | --- |
ComputationofPCAusingtheSVDalgorithmiscomparativelyfast. However,beaware thatpar-
ticularsoftwareimplementationsoftheSVDmaynotsorttheeigenvaluesindescendingorder,although
| each eigenvector | will stillbe | associated | with the correct | eigenvalue. |
| ---------------- | ------------ | ---------- | ---------------- | ----------- |
| 13.6.3. The      | Power Method |            |                  |             |
Insomeapplications(e.g.,Wilks,2016c)onlytheleadingeigenvalueandeigenvectorareneeded,sothat
computationofafullPCAisunnecessarilyslowandwastefulofcomputingresources.Insuchcasesit
can be advantageous to find the leading eigenvalue–eigenvector pair using the power method (e.g.,
| Goluband | van Loan, 1996). |     |     |     |
| -------- | ---------------- | --- | --- | --- |
Beginningwithanarbitraryinitialguessfortheleadingeigenvector,e ,withjje jj¼1,thepower
1 1
| method algorithm | proceeds | by iterating |     |     |
| ---------------- | -------- | ------------ | --- | --- |
v¼½S(cid:3)e (13.44a)
¼kvk
l (13.44b)
1
e ¼v=l (13.44c)
|     |     |     | 1   | 1        |
| --- | --- | --- | --- | -------- |
|     |     | vis |     | andjjvjj |
until convergence. Here an intermediate storage vector, denotes itsEuclidean length.
| 13.6.4. PCA | and Missing | Data |     |     |
| ----------- | ----------- | ---- | --- | --- |
ComputationofasamplecovarianceorcorrelationmatrixusingEquation11.30asinputtoaPCA,oralter-
nativelycomputationofaPCAthroughSVDonthedatamatrixasinExample11.5,bothrequirethatthe
inputdataanomalymatrix[X0]containsnomissingvalues.Ofcoursethereareoftenmissingvalueinreal
datasets,requiringthatsomeaccommodationbemadebeforecomputationofaPCA.Ontheotherhand,
oncethePCAhasbeencomputed,itcanbeusedtoestimatethemissingvalues.
Ifthereareveryfewmissingvaluesinadatasetitmaybereasonabletosimplydeleteanyincomplete
datavectors before proceeding,butusuallythisapproach willleadtoanexcessiveportionofthe data
beinglost.Alternatively,therearetwoapproachestodealingwiththemissingdatabeforecomputation
ofa PCA. The first is to substitute the appropriate sample mean for any missing data, yielding a zero
anomaly for the corresponding missing value x0 , which is equally applicable when computing a
i,k
covarianceorcorrelationmatrix,andwhencomputingtheSVDofadatamatrix.Thesecondapproach
istoestimatetheelementsofthecovarianceorcorrelationmatrixusingthenumeratorofEquation3.28,
| including only | terms for | which both | elements are nonmissing. |     |
| -------------- | --------- | ---------- | ------------------------ | --- |
The two methods will differ only with respect to the divisor in the covariance calculation in the
numerator of Equation 3.28, because the first approach will yield zero contribution to the sum when
eitherofthetwoanomaliesarezero,eventhoughthedivisorisn–1.Accordinglyimputingzeroanomaly
for any missing values leads to negative bias in the absolute values of the resulting variance and
covariance estimates. On the other hand, using the second approach yields different sample sizes for
theestimatedcovariancesorcorrelations,inconsistenciesamongwhichmayresultinasingularmatrix.
Inthatcasesomeofthetrailingeigenvaluesmaybenegativewhich,asaconsequenceofEquation11.54,
| willleadto | anupwardbias | inthe leading | estimated | eigenvalues. |
| ---------- | ------------ | ------------- | --------- | ------------ |

Chapter 13 Principal Component(EOF) Analysis 661
Once a PCA involving missing data values has been computed, its eigenvectors can be used to
estimatethosemissingdata.First,theprincipalcomponentsinthematrix[U](Equation13.29)areesti-
mated using
XK
x0 e
i,k k,m
k¼1
x valid
i,k
u ¼ , (13.45)
i,m XK
e2
k,m
k¼1
x valid
i,k
wherethesummationsincludeonlytermsforwhichdatavaluesx arenonmissing.Whenadatavector
i,k
x containsnomissingelements,thedenominatorofEquation13.45is1(Equation11.49),inwhichcase
i
Equation 13.45 is equivalent to Equation 13.1. The missing anomaly values can then be estimated
throughapplication ofa synthesis,
XM
x0 ¼ u e : (13.46)
i,k i,m m,k
m¼1
Equation13.45istheresultofaleast-squaresapproachthatminimizestheerror([X]–[U][ET])T([X]–[U]
[ET]),whichisderivedfromEquation13.29.Ityieldsreasonableresultswhentheproportionofmissing
data is notexcessive. Forlarger (thanperhaps10%to 20%) fractions of missing data, moreelaborate
iterativeapproaches have been found tobe more accurate (Taylor et al., 2013).
13.7. SOME ADDITIONAL USES OF PCA
13.7.1. Singular Spectrum Analysis (SSA): Time-Series PCA
Principalcomponentanalysiscanalsobeappliedtoscalarormultivariatetimeseries.Thisapproachto
time-seriesanalysisisknownbothassingularspectrumanalysisandsingularsystemsanalysis(SSA,in
eithercase).FullerdevelopmentsofSSAthanispresentedherecanbefoundinElsnerandTsonis(1996),
Ghil et al. (2002), and Vautard et al. (1992).
SSAiseasiesttounderstandintermsofascalartimeseriesx,t¼1,…,n;althoughthegeneralization
t
tomultivariatetimeseriesofavectorx isreasonablystraightforward.AsavariantofPCA,SSAinvolves
t
extractionofeigenvaluesandeigenvectorsfromacovariancematrix.Thiscovariancematrixiscalculated
fromascalartimeseriesbypassingadelaywindow,orimposinganembeddingdimension,oflengthKon
thetimeseries.TheprocessisillustratedinFigure13.16.ForK¼3,thefirstK-dimensionaldatavector,
x iscomposedofthefirstthreemembersofthescalartimeseries,x iscomposedofthesecondthree
(1) (2)
membersofthescalartimeseries,andsoon,yieldingatotalofn–K+1overlappinglaggeddatavectors.
Ifthetimeseriesx iscovariancestationary,thatis,ifitsmean,variance,andlaggedcorrelationsdo
t
notchangethroughtime,the(K(cid:1)K)populationcovariancematrixofthelaggedtime-seriesvectorsx
()
takesonaspecialbandedstructureknownasToeplitz,inwhichtheelementss i,j ¼g ji–jj ¼E[x t 0 x0 t+|i–j|]
arearrangedindiagonalparallelbands.Thatis,theelementsoftheresultingcovariancematrixaretaken
fromtheautocovariancefunction(Equation3.39),withlagsarrangedinincreasingorderawayfromthe
maindiagonal.Alltheelementsofthemaindiagonalares ¼g ,thatis,thevariance.Theelementson
i,i 0

| 662 |         |                       |         | PART    | III MultivariateStatistics |
| --- | ------- | --------------------- | ------- | ------- | -------------------------- |
|     | x , x , | x , x , x , .  .  .,  | x , x   | , x , x | , x                        |
|     | 1 2     | 3 4 5                 | n–4 n–3 | n–2 n–1 | n                          |
x
|     | x      |     |            | n – 4 |     |
| --- | ------ | --- | ---------- | ----- | --- |
|     | 1      |     | x (n–4)= x |       |     |
|     | x =  x |     |            | n – 3 |     |
(1) 2
|     | x   |     |     | x n–2 |     |
| --- | --- | --- | --- | ----- | --- |
3
|     |     | x   |     | x n–3 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | 2   |     | x     |     |
(n–3)= x
|     | x   | =  x  |     | n – 2      |     |
| --- | --- | ----- | --- | ---------- | --- |
|     | (2) | 3     |     | x          |     |
|     |     | x     |     | n – 1      |     |
|     |     | 4     |     |            | x   |
|     |     | x     |     |            | n–2 |
|     |     | 3     |     | x (n–2)= x |     |
|     |     | x = x |     |            | n–1 |
(3) 4
|     |     | x   |     |     | x   |
| --- | --- | --- | --- | --- | --- |
|     |     | 5   |     |     | n   |
FIGURE13.16 Illustrationoftheconstructionofthevectortimeseriesx ,t¼1,…,n–M+1,bypassingadelaywindowof
(t)
embeddingdimensionM¼3overconsecutivemembersofthescalartimeseriesx.
t
thediagonalbandsadjacenttothemaindiagonalareallequaltog ,reflectingthefactthat,forexample,
1
thecovariancebetweenthefirstandsecondelementsofthevectorsx
inFigure13.16isthesameasthe
(t)
covariancebetweenthesecondandthirdelements.Theelementsseparatedfromthemaindiagonalby
onepositionareallequaltog 2 ,andsoon.Becauseofedgeeffectsatthebeginningsandendsofsample
timeseries,thesamplecovariancematrixmaybeonlyapproximatelyToeplitz,althoughthediagonally
bandedToeplitzstructureissometimesenforcedbeforecalculationoftheSSA(AllenandSmith,1996;
| Elsner and Tsonis,1996; | Groth and | Ghil, 2015). |     |     |     |
| ----------------------- | --------- | ------------ | --- | --- | --- |
SinceSSAisaPCA,thesamemathematicalconsiderationsapply.Inparticular,theprincipalcom-
ponentsarelinearcombinationsofthedataaccordingtotheeigenvectors(Equations13.1and13.2).The
analysisoperationcanbereversedtosynthesize,orapproximate,thedatafromall(Equation13.20)or
some (Equation 13.21) of the principal components. What makes SSA different follows from the dif-
ferent nature of the underlying data, and the implications of that different nature on interpretation of
theeigenvectorsandprincipalcomponents.Inparticular,thedatavectorsarefragmentsoftimeseries
ratherthanthemoreusualspatialdistributionofvaluesatasingletime,sothattheeigenvectorsinSSA
represent characteristic time patterns exhibited by the data, rather than characteristic spatial patterns.
Accordingly,theeigenvectorsinSSAaresometimescalledT-EOFs.Sincetheoverlappingtimeseries
fragmentsx
t themselvesoccurinatimesequence,theprincipalcomponentsalsohaveatimeordering,as
in Equation 13.11. These temporal principal components u , or T-PCs, index the degree to which the
k
correspondingtime-seriesfragmentx resemblesthecorrespondingT-EOF,e .Becausethedataarecon-
|     |     | t   |     |     | k   |
| --- | --- | --- | --- | --- | --- |
secutivefragmentsoftheoriginaltimeseries,theprincipalcomponentsarelinearcombinationsofthese
time-seriessegments,withtheweightsgivenbytheT-EOFelements.TheT-PCsaremutuallyuncorre-
lated, butin general an individual T-PC will exhibit temporal autocorrelations.
TheanalogybetweenSSAandFourieranalysisoftimeseriesisespeciallystrong,withtheT-EOFs
corresponding to the sine and cosine functions, and the T-PCs corresponding to the amplitudes.
However,therearetwomajordifferences.First,theorthogonalbasisfunctionsinaFourierdecompo-
sition are the fixed harmonic functions, whereas the basis functions in SSA are the data-adaptive T-
EOFs.ThereforeanSSAmaybemoreefficientthanaFourieranalysis,inthesenseofrequiringfewer
basisfunctionstorepresentagivenfractionofthevarianceofatimeseries.Similarly,theFourierampli-
tudes are time-independent constants, but their counterparts, the T-PCs, are themselves functions of

Chapter 13 Principal Component(EOF) Analysis 663
time.Thereforesimilarlytowaveletanalysis(Section10.6),SSAcanrepresenttimevariationsthatmay
be localized intime, and sonot necessarilyrecurring throughout the time series.
AlsoincommonwithFourieranalysis,SSAcandetectandrepresentoscillatoryorquasi-oscillatory
featuresintheunderlyingtimeseries.Aperiodicorquasi-periodicfeatureinatimeseriesisrepresented
inSSAbypairsofT-PCsandtheircorrespondingeigenvectors.Thesepairshaveeigenvaluesthatare
equalornearlyequal.Thecharacteristictimepatternsrepresentedbythesepairsofeigenvectorshavethe
same(orverysimilar)shape,butareoffsetintimebyaquartercycle(asareapairofsineandcosine
functions).UnlikethesineandcosinefunctionsthesepairsofT-EOFstakeonshapesthataredetermined
by the time patterns in the underlying data. A common motivation for using SSA is to search, on an
exploratory basis, for possible periodicities in time series, which periodicities may be intermittent
and/ornonsinusoidalinform.FeaturesofthiskindareindeedidentifiedbyaSSA,butfalseperiodicities
arisingonlyfromsamplingvariationsmayalsoeasilyoccurintheanalysis(AllenandRobertson,1996;
Allenand Smith, 1996).
AnimportantconsiderationinSSAischoiceofthewindowlengthorembeddingdimension,K.Obvi-
ouslytheanalysiscannotrepresentvariationslongerthanthislength,althoughchoosingtoolargeavalue
resultsinasmallsamplesize,n–K+1,fromwhichtoestimatethecovariancematrix.Also,thecompu-
tationaleffortincreasesquicklyasKincreases.Usualrulesofthumbarethatanadequatesamplesize
maybeachievedforK<n/3,andthattheanalysiswillbesuccessfulinrepresentingtimevariationswith
periods betweenK/5and K.
Example 13.5 SSAfor an AR(2) Series
Figure13.17showsann¼100-pointrealizationfromtheAR(2)process(Equation10.27)withparameters
f ¼0.9,f ¼–0.6,m¼0,ands ¼1.Thisisapurelyrandomseries,buttheparametersf andf havebeen
1 2 e 1 2
choseninawaythatallowstheprocesstoexhibitpseudoperiodicities.Thatis,thereisatendencyforthe
seriestooscillate,although the oscillations are irregular withrespect totheir frequency and phase. The
spectraldensityfunctionforthisAR(2)process,includedinFigure10.21,showsamaximumcenterednear
f¼0.15,correspondingtoatypicalperiodnearτ¼1/f(cid:5)6.7timesteps.
Analyzing the series using SSA requires choosing a delay window length, K, that should be long
enough to capture the feature of interest yet short enough for reasonably stable covariance estimates
tobecalculated.Combiningtherulesofthumbforthewindowlength,K/5<τ<K<n/3,aplausible
choiceisK¼10.Thischoiceyieldsn–K+1¼91overlappingtimeseriesfragmentsx oflengthK¼10.
(t)
Calculatingthecovariancesforthissampleof91datavectorsx intheconventionalwayyieldsthe
(t)
(10(cid:1)10)matrix
2
x
t 0
–2
0 20 40 60 80 100
Time, t
FIGURE13.17 Ann¼100-pointrealizationfromanAR(2)processwithf ¼0.9andf ¼–0.6.
1 2

664 PART III MultivariateStatistics
2 3
1:792
6
6
:955 1:813 7
7
6 6(cid:4):184 :958 1:795 7
7
6 6(cid:4):819 (cid:4):207 :935 1:800 7
7
½S(cid:3)¼ 6 6 6 6 (cid:4) (cid:4) : : 7 1 1 4 6 9 (cid:4) (cid:4) : : 8 6 5 5 1 7 (cid:4) (cid:4) : : 2 7 2 8 2 0 (cid:4) : : 9 2 5 2 9 2 1: : 8 9 4 0 3 3 1:805 7 7 7 7 : (13.47)
6
6
:079 (cid:4):079 (cid:4):575 (cid:4):783 (cid:4):291 :867 1:773 7
7
6
6
:008 :146 (cid:4):011 (cid:4):588 (cid:4):854 (cid:4):293 :873 1:809 7
7
4 (cid:4):199 :010 :146 (cid:4):013 (cid:4):590 (cid:4):850 (cid:4):289 :877 1:809 5
(cid:4):149 (cid:4):245 (cid:4):044 :148 :033 (cid:4):566 (cid:4):828 (cid:4):292 :874 1:794
Forclarity,onlytheelementsinthelowertriangleofthissymmetricmatrixhavebeenprinted.Because
ofedgeeffectsinthefinitesample,thiscovariancematrixisapproximately,butnotexactly,Toeplitz.
The10elementsonthemaindiagonalareonlyapproximatelyequal,andeachisestimatingthetruelag-0
autocovarianceg ¼s2 (cid:5)2:29.Similarly,thenineelementsontheseconddiagonalareapproximately
0 x
equal,witheachestimatingthelag-1autocovarianceg (cid:5)1.29,theeightelementsonthethirddiagonal
1
estimatethelag-2autocovarianceg (cid:5)–0.21,andsoon.Thepseudoperiodicityinthedataisreflectedin
2
thelargenegativeautocovarianceatthreelags,andthesubsequentdampedoscillationintheautocovar-
iancefunction,whichcanbeseeneasilybyreadingdownthefirstcolumn,orreadingthebottomrow
fromrighttoleft.
Figure 13.18 shows the leading four eigenvectors of the covariance matrix in Equation 13.47 and
theirassociatedeigenvalues.Thefirsttwooftheseeigenvectors(Figure13.18a),whichareassociated
withnearlyequaleigenvalues,areverysimilarinshapeandareseparatedbyapproximatelyaquarterof
theperiodτcorrespondingtothemiddleofthespectralpeakinFigure10.21.Jointlytheyrepresentthe
dominantfeatureofthedataseriesinFigure13.17,namelythepseudoperiodicbehavior,withsuccessive
peaks and crests tending tobe separated by six orseven time units.
ThethirdandfourthT-EOFsinFigure13.18brepresentother,nonperiodicaspectsofthetimeseries
inFigure12.17.UnliketheleadingT-EOFsinFigure13.18a,theyarenotoffsetimagesofeachotherand
0.5 0.5
0.0 0.0
t = 6.7
–0.5 –0.5
T-EOF 1,l1= 4.95 T-EOF 3,l3 = 3.10
T-EOF 2,l2= 4.34 T-EOF 4,l4 = 2.37
1 3 5 7 9 1 3 5 7 9
(a) Time separation (b) Time separation
FIGURE13.18 (a)FirsttwoeigenvectorsofthecovariancematrixinEquation12.38,and(b)thethirdandfourtheigenvectors.

Chapter 13 Principal Component(EOF) Analysis 665
donothave nearlyequaleigenvalues. Jointlythefourpatterns inFigure13.18represent83.5% ofthe
variancewithinthe10-elementtimeseriesfragments(butnotincludingvarianceassociatedwithlonger
timescales).
Ghil et al. (2002) present a similar extended example of SSA, using a time series of the Southern
Oscillation Index (Figure 3.16). e
It is conceptually straightforward toextend SSAto simultaneous analysis ofmultiple (i.e., vector)
time series, which is called multichannel SSA, or MSSA (Ghil et al., 2002; Plaut and Vautard, 1994).
The relationship between SSA and MSSA parallels that between an ordinary PCA for a single field
and simultaneous PCA for multiple fields as described in Section 13.2.2. The multiple channels in a
MSSAmightbetheLgridpointsrepresentingaspatialfieldattimet,inwhichcasethetimeseriesfrag-
mentscorrespondingtothedelaywindowlengthKwouldbecodedintoa(LK(cid:1)1)vectorx ,yieldinga
(t)
(LK(cid:1)LK)covariancematrixfromwhichtoextractspace-timeeigenvaluesandeigenvectors(ST-EOFs).
Thedimensionofsuchamatrixmaybecomeunmanageable,andonesolution(PlautandVautard,1994)
can betofirstcalculateanordinaryPCAforthespatial fields,andthensubjectthefirstfewprincipal
componentstotheMSSA.Inthiscaseeachchannelcorrespondstooneofthespatialprincipalcompo-
nentscalculatedintheinitialdatacompressionstep.Vautardetal.(1996,1999)describeMSSA-based
forecasts of fields constructed by forecasting the space-time principal components, and then reconsti-
tuting the forecastfields through a truncated synthesis.
13.7.2. Principal-Component Regression
A pathology that may occur in multiple linear regression (see Section 7.3.1) is that a set of predictor
variableshavingstrongmutualcorrelationscanresultinthecalculationofanunstableregressionrela-
tionship,inthe sense that the sampling distributionsofthe estimated regression parameters may have
veryhighvariances.TheproblemcanbeappreciatedinthecontextofEquation11.40,forthecovariance
matrixofthejointsamplingdistributionoftheestimatedregressionparameters.Thisequationdepends
ontheinverseofthematrix[X]T[X],whichisproportionaltothecovariancematrix[S ]ofthepredictors.
x
Verystrongintercorrelationsamongthepredictorsleadstotheircovariancematrix(andthusalso[X]T
[X])beingnearlysingular,orsmallinthesensethatitsdeterminantisnearzero.Theinverse,([X]T[X]) –1
isthenlarge,andinflatesthecovariancematrix[S ]inEquation11.40.Theresultisthatanyspecificset
b
ofestimatedregressionparametersmaybeveryfarfromtheircorrectvaluesasaconsequenceofsam-
plingvariations,leadingthefittedregressionequationtoperformpoorlyonindependentdata.Thepre-
diction intervals (basedupon Equation11.42) are also inflated.
Anapproachtoremedyingthisproblemistofirsttransformthepredictorstotheirprincipalcompo-
nents,thecorrelationsamongwhicharezero.Theresultingprincipal-componentregressionisconve-
nient to work with, because the uncorrelated predictors can be added to or taken out of a tentative
regression equation at will without affecting the contributions and parameter estimates of the other
principal-component predictors.If all the principal componentsare retained in aprincipal-component
regression, then nothing is gained over the conventional least-squares fit to the full predictor set.
However,Jolliffe(2002)showsthatmulticollinearities,ifpresent,areassociatedwiththeprincipalcom-
ponentshavingthesmallesteigenvalues.Asaconsequence,theeffectsofthemulticollinearities,andin
particulartheinflatedcovariancematrixfortheestimatedparameters,caninprincipleberemovedby
truncating the trailing principal components associated with the very small eigenvalues.

| 666 |     |     |     | PART | III MultivariateStatistics |     |
| --- | --- | --- | --- | ---- | -------------------------- | --- |
Thereareproblemsthatmaybeassociatedwithprincipal-componentregression.Unlesstheprin-
cipalcomponentsthatareretainedaspredictorsareinterpretableinthecontextoftheproblembeing
analyzed,theinsightto be gainedfromtheregressionmaybelimited.Itispossibletoreexpressthe
principal-component regression in terms of the original predictors using the synthesis equation
(Equation13.6),buttheresultwillingeneralinvolvealltheoriginalpredictorvariablesevenifonly
one or a few principal component predictors have been used. This reconstituted regression will be
biased, although often the variance is much smaller than for the least-squares alternative, resulting
| in a smaller | MSE overall. |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- |
| 13.7.3.      | The Biplot   |     |     |     |     |     |
ItwasnotedinSection3.6thatgraphicalEDAforhigh-dimensionaldataisespeciallydifficult.Since
principalcomponentanalysisexcelsatdatacompressionusingtheminimumnumberofdimensions,itis
naturaltothinkaboutapplyingPCAtoEDA.Thebiplot,originatedbyGabriel(1971),issuchatool.The
"bi-" in biplot refers to the simultaneous representation of the n rows (the observations) and the K
| columns | (the variables) | ofa data matrix | [X]. |     |     |     |
| ------- | --------------- | --------------- | ---- | --- | --- | --- |
Thebiplotisatwo-dimensionalgraph,whoseaxesarethefirsttwoeigenvectorsof[S ].Thebiplot
x
representsthenobservationsastheirprojectionsontotheplanedefinedbythesetwoeigenvectors,that
)/S
is,asthescatterplotofthefirsttwoprincipalcomponents.Totheextentthat(l +l l (cid:5)1,thisscat-
1 2 k k
terplot will be a close approximation to their higher-dimensional relationships, in a graphable two-
dimensional space. Exploratory inspection of the data plotted in this way may reveal such aspects of
thedataasthepointsclusteringintonaturalgroups,ortimesequencesofpointsthatareorganizedinto
| coherent | trajectories inthe | planeof the | plot. |     |     |     |
| -------- | ------------------ | ----------- | ----- | --- | --- | --- |
The other element of the biplot is the simultaneous representation of the K variables. Each of the
coordinate axes of the K-dimensional data space defined by the variables can be thought of as a unit
basis vector indicating the direction of the corresponding variable, that is,
| b T¼½1,0,0,…,0(cid:3),b | T¼½0,1,0,…,0(cid:3),…,b |     | T¼½0,0,0,…,1(cid:3). |             |         |                  |
| ----------------------- | ----------------------- | --- | -------------------- | ----------- | ------- | ---------------- |
|                         |                         |     |                      | These basis | vectors | can also be pro- |
| 1                       | 2                       |     | K                    |             |         |                  |
jected onto the two leadingeigenvectors defining the planeof the biplot,that is,
XK
eTb
|     |     |     | ¼   | e b   |     | (13.48a) |
| --- | --- | --- | --- | ----- | --- | -------- |
|     |     |     | 1 k | 1,k k |     |          |
k¼1
and
XK
|     |     |     | eTb   | :       |     |          |
| --- | --- | --- | ----- | ------- | --- | -------- |
|     |     |     | k ¼ e | 2,k b k |     | (13.48b) |
2
k¼1
Sinceeachoftheelementsofeachofthebasisvectorsb iszeroexceptforthekth,thesedotproductsare
k
simplythekthelementsofthetwoeigenvectors.ThereforeeachoftheKbasisvectorsb
k islocatedonthe
biplotbycoordinatesgivenbythecorrespondingeigenvectorelements.Becausethedatavaluesandtheir
originalcoordinateaxesarebothprojectedinthesameway,thebiplotamountstoaprojectionofthefull
K-dimensionalscatterplotofthedata,includingthecoordinateaxes,ontotheplanedefinedbythetwo
leading eigenvectors.
Figure13.19showsabiplotfortheK¼6-dimensionalJanuary1987datainTableA.1,afterstan-
dardizationtozeromeanandunitvariance,sothatthePCApertainstotheircorrelationmatrix,[R].The
PCAforthesedataisgiveninTable13.1b.Thenumbersindicatethecalendardateforeachplotteddata
point. The projections of the six original basis vectors (plotted longer than the actual projections in

| Chapter | 13 Principal | Component(EOF) | Analysis |     |     | 667 |
| ------- | ------------ | -------------- | -------- | --- | --- | --- |
e
|     |     | 2   |     | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
5
PIPC
23
20
11
|     |     | 25  |             | NI                   |     |     |
| --- | --- | --- | ----------- | -------------------- | --- | --- |
|     |     | 0   | 27 26 24 17 | 1 0 113 N            |     |     |
|     |     |     | 28 29541    | 2 23 2 1 9 1 2 3 2 C |     |     |
|     |     |     |             | 8 0 6 1 8            |     |     |
|     |     |     |             | 1 4 1 9 X            |     |     |
|     |     |     |             | 716 I                |     |     |
X C 15
e
1
–5
|     |     | –5  |     | 0   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- |
FIGURE13.19 BiplotoftheJanuary1987datainTableA.1,afterstandardization.P¼precipitation,X¼maximumtemper-
ature,andN¼minimumtemperature.Numberedpointsrefertothecorrespondingcalendardates.Theplotisaprojectionofthefull
six-dimensionalscatterplotontotheplanedefinedbythefirsttwoprincipalcomponents.
Equation13.48forclarity,butwiththecorrectrelativemagnitudes)areindicatedbythelinesegments
diverging from the origin. "P," "N," and "X" indicate precipitation, minimum temperature, and
maximum temperature, respectively, and the subscripts "I" and "C" indicate Ithaca and Canandaigua.
It is immediately evident that the pairs of lines corresponding to like variables at the two locations
areorientednearlyinthesamedirections,andthatthetemperaturevariablesareorientednearlyperpen-
dicularlytotheprecipitationvariables.Approximately(becausethevariancedescribedbythefirsttwo
principalcomponentsis92%ratherthan100%),thecorrelationsamongthesesixvariablesareequalto
thecosinesoftheanglesbetweenthecorrespondinglinesinthebiplot(compareTable3.5),sothevari-
| ablesorientedin | very | similar directions | form | natural groupings. |     |     |
| --------------- | ---- | ------------------ | ---- | ------------------ | --- | --- |
ThescatterofthendatapointsnotonlyportraystheirK-dimensionalbehaviorinapotentiallyunder-
standableway,buttheirinterpretationisinformedfurtherbytheirrelationshiptotheorientationsofthe
variables.InFigure13.19mostofthepointsareorientednearlyhorizontally,withaslightinclinationthat
isaboutmidwaybetweentheanglesoftheminimumandmaximumtemperaturevariables,andperpen-
dicular to the precipitation variables. These are the days corresponding to small or zero precipitation,
whose primary variability characteristics relate to temperature differences. They are mainly located
below the origin, because the mean precipitation is a bit above zero, and the precipitation variables
areorientednearlyvertically(i.e.,correspondcloselytothesecondprincipalcomponent).Pointstoward
the right of the diagram, that are oriented similarly to the temperature variables, represent relatively
warm days (with little or no precipitation), whereas points to the left are the cold days. Focusing on
thedatesforthecoldestdays,wecanseethattheseoccurredinasinglerun,towardtheendofthemonth.
Finally,thescatterofdatapointsindicatesthatthefewvaluesintheupperportionofthebiplotaredif-
ferentfromtheremainingobservations,butitisthesimultaneousdisplayofthevariablesthatallowsus
| to see thattheseresult |     | fromlarge | positive values | for precipitation. |     |     |
| ---------------------- | --- | --------- | --------------- | ------------------ | --- | --- |

| 668 |     |     |     |     |     |     |     | PART III MultivariateStatistics |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- |
13.8. EXERCISES
| 13.1. | Using | informationfrom |     | Exercise | 11.8, |     |     |     |     |
| ----- | ----- | --------------- | --- | -------- | ----- | --- | --- | --- | --- |
a. Calculate the valuesof the first principal componentsfor 1 Januaryand for 2 January.
b. Estimate the varianceofall 31valuesof the first principal component.
c. Whatproportionofthetotalvariabilityofthemaximumtemperaturedataisrepresentedbythe
|     |     | first principal | component? |     |     |     |     |     |     |
| --- | --- | --------------- | ---------- | --- | --- | --- | --- | --- | --- |
13.2. a. Compute the first two principal components for 1 Januaryinthe PCA inTable 13.1b.
b. Reconstruct the six (standardized) weather variable values for 1 January, using the first 2
PCs only.
13.3. A principal component analysis of the data in Table A.3 yields the three eigenvectors
e T¼ ½:593,:552, (cid:4):587(cid:3),e T¼½:332, (cid:4):831, (cid:4):446(cid:3),ande T¼½:734, (cid:4):069,:676(cid:3),where
|     | 1   |     |     |     | 2   |     |     | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the three elements in each vector pertain to the temperature, precipitation, and pressure data,
respectively.Thecorresponding three eigenvalues arel ¼2.476,l ¼0.356,andl ¼0.169.
|     |     |     |     |     |     |     | 1   | 2   | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a. Wasthisanalysisdoneusingthecovariancematrixorthecorrelationmatrix?Howcanyoutell?
b. HowmanyprincipalcomponentsshouldberetainedaccordingtoKaiser’srule,Jolliffe’smod-
|     |     | ification, | andthe | broken stick | model? |     |     |     |     |
| --- | --- | ---------- | ------ | ------------ | ------ | --- | --- | --- | --- |
c. Estimate the missing precipitation value for 1956 using the first PC only.
| 13.4. | Use | the information |     | in Exercise | 13.3 to |     |     |     |     |
| ----- | --- | --------------- | --- | ----------- | ------- | --- | --- | --- | --- |
a. Compute 95% confidence intervals for the eigenvalues, assuming large samples and
|     |     | multinormal | data. |     |     |     |     |     |     |
| --- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
b. Examine the eigenvalue separation using the North et al. ruleofthumb.
13.5. Using theinformationinExercise13.3,calculatetheeigenvectormatrix[E]tobeorthogonally
|     | rotated | if            |           |               |     |                    |     |     |     |
| --- | ------- | ------------- | --------- | ------------- | --- | ------------------ | --- | --- | --- |
|     | a.      | The resulting | rotated   | eigenvectors  | are | tobe orthogonal.   |     |     |     |
|     | b.      | Theresulting  | principal | componentsare |     | to beuncorrelated. |     |     |     |
13.6. UsetheSVDinEquation11.74tofindthefirstthreevaluesofthefirstprincipalcomponentofthe
|     | minimum | temperature |     | data inTable | A.1. |     |     |     |     |
| --- | ------- | ----------- | --- | ------------ | ---- | --- | --- | --- | --- |
13.7. Table13.1bisthesummaryofaPCAon(thestandardized)dailyweatherdataatIthacaandCan-
andaiguaforJanuary1987.Usingtheseresults,theprincipal-componentregressionequationpre-
dicting the corresponding daily maximum temperatures at Central Park, NYcity is:
|     |     |     |     |         |             |              | (cid:7)  | (cid:8) |     |
| --- | --- | --- | --- | ------- | ----------- | ------------ | -------- | ------- | --- |
|     |     |     |     |         | ¼37:5+7:15u | (cid:4)2:81u | R2¼75:9% |         |     |
|     |     |     |     | Max NYC |             | 1            | 3        |         |     |
whereu andu arethefirstandthirdprincipalcomponents,respectively.Determinethecorre-
|     |     | 1   | 3   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sponding regression equationinterms ofthe six original(standardized) predictorvariables.
13.8. Construct abiplot for the data inTable A.3, using the informationinExercise 13.3.