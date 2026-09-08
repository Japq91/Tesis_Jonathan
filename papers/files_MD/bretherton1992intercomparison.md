--- PAGE 01 ---
VOLUME 5

JOURNAL OF CLIMATE

JUNE 1992

An Intercomparison of Methods for Finding Coupled Patterns in Climate Data

CHRISTOPHER S. BRETHERTON, CATHERINE SMITH, AND JOHN M. WALLACE
Department of Atmospheric Sciences, University of Washington, Seattle, Washington

(Manuscript received 23 July 1990, in final form 28 May 1991)

ABSTRACT

This paper introduces a conceptual framework for comparing methods that isolate important coupled modes
of variability between time series of two fields. Four specific methods are compared: principal component
analysis with the fields combined (CPCA ), canonical correlation analysis (CCA) and a variant of CCA proposed
by Barnett and Preisendorfer (BP), principal component analysis of one single field followed by correlation of
its component amplitudes with the second field (SFPCA ), and singular value decomposition of the covariance
matrix between the two fields (SVD). SVD and CPCA are easier to implement than BP, and do not involve
user-chosen parameters. All methods are applied to a simple but geophysically relevant model system and their
ability to detect a coupled signal is compared as parameters such as the number of points in each field, the
number of samples in the time domain, and the signal-to-noise ratio are varied.

In datasets involving geophysical fields, the number of sampling times may not be much larger than the
number of observing locations or grid points for each field. In a model system with these characteristics, CPCA
usually extracted the coupled pattern somewhat more accurately than SVD, BP, and SFPCA, since the patterns
it yielded exhibit smaller sampling variability; SVD and BP gave quite similar results, and CCA was uncompetitive
due to a high sampling variability unless the coupled signal was highly localized. The coupled modes derived
from CPCA and SFPCA exhibit an undesirable mean bias toward the leading EOFs of the individual fields; in
fact, for small signal-to-noise ratios these methods may identify a coupled signal that is similar to a dominant
EOF of one of the fields but is completely orthogonal to the true coupled signal within that field. For longer
time series, or in situations where the coupled signal does not resemble the EOFs of the individual fields, these

biases can make SVD and BP substantially superior to CPCA.

1. Introduction

The analysis of the relationships within and among
datasets involving large grid point (or station) arrays
and time series can be done in many different ways.
Simple methods of analysis like compositing and cor-
relation based on selected “reference grid points” or
indices are easy to perform, but they involve subjective
decisions about the choice of reference time series.
Matrix operations offer the possibility of a more ob-
jective definition of the structures in such datasets.

One such technique applicable to measurements of
a single field at many locations is called principal com-
ponent analysis (PCA). First proposed by Pearson
(1902), PCA identifies linear transformations of the
dataset that concentrate as much of the variance as
possible into a small number of variables. A related
technique, factor analysis, was introduced around the
same time as Pearson’s work by Spearman (1904a,b)
and extended by Hotelling (1935, 1936), who for-
mulated mathematical equations for defining unique
solutions. These techniques were first used extensively

Corresponding author address: John M. Wallace, University of
Washington, Department of Atmospheric Sciences, AK-40, Seattle,
WA 98195.

in the social sciences. The first applications to meteo-
rology were by Fukuoka (1951), Lorenz (1956),
Holmstrom (1963), and Obukhov (1960). The lucid
exposition of PCA by Kutzbach (1967) was instru-
mental in promoting the use of this technique in cli-
mate research.

Our focus will be on providing a unified conceptual
framework for techniques that isolate important cou-
pled modes of variability between time series of two
fields. Several approaches have been applied to geo-
physical data; we will concentrate on four of these.

Kutzbach (1967) pointed out that two or more field
variables can be combined in the same PCA to docu-
ment the relationships between the fields. We will refer
to this technique as combined PCA (CPCA). A second
method is to correlate the expansion coefficients of the
EOFs of one of the fields with the second field to obtain
correlation maps for this EOF with the second field;
this method will be called single-field—based PCA, or
SFPCA. (e.g., Wallace et al. 1990). A third widely used
technique is canonical correlation analysis (CCA),
which is designed to identify the linear combinations
of variables in one field that are most strongly correlated
with linear combinations of variables in another field.
This method was first devised by Hotelling (1935,
1936) and has been widely used in the social sciences

541

--- PAGE 02 ---
542

since the 1960s. A typical application is discussed in
the textbook of Cooley and Lohnes (1971). A group
of students answers a set of questions designed to pro-
vide information on their occupational interests and
their personality traits. There are many more student
respondents than there are items on the questionnaire.
A principal component analysis, based upon the com-
plete dataset consisting of both types of questions
[analogous to the methodology used by Kutzbach
(1967)], yields factors related to maturity, interest in
manual labor, intellectual ability, etc. Because the
questions concerning interests and personality traits
are not treated separately, this method does not nec-
essarily yield any information concerning the relation-
ship between the answers to these two groups of ques-
tions. CCA of the same dataset yields related pairs of
factors from the two groups of questions. The first fac-
tor, for example, shows that an interest in middle-class
occupations tends to be shared by those with middle-
class values; the second relates an outgoing personal-
ity with an interest in sports and outdoor occupa-
tions, etc.

The first meteorological application of CCA was by
Glahn (1968), who used it in the context of statistical
weather prediction. It has been subsequently used by
Barnett (1981, 1983) and Barnett and Preisendorfer
(1987) to relate patterns of seasonal mean SST anom-
alies over the Pacific to surface air temperature anom-
alies over the United States the following season; by
Nicholls (1987) to study teleconnections related to the
Southern Oscillation; by Déqué and Servain (1989) to
study lead/lag relationships between monthly mean
SST and 700-mb height patterns over the Atlantic sec-
tor; by Metz (1989) to study the relationship between
low-frequency fluctuations in the 500-mb height field
and the associated patterns of forcing by the high-fre-
quency fluctuations; and by Graham (1990) to identify
related simultaneous and lag-correlation patterns in
tropical Pacific SST and the Northern Hemisphere 700-
mb height field. Preisendorfer (1988) devoted a chapter
of his monograph on principal component analysis in
meteorology to a discussion of CCA. Barnett and
Preisendorfer (1987) suggested that filtering the data
for each field by projecting it onto a subset of the EOFs
of that field can make CCA less susceptible to sampling
fluctuations due to short time series. We call this variant
of CCA the BP method.

A fourth method, singular value decomposition, or
SVD, of the covariance matrix between two fields, has
not been widely used in meteorology but is the simplest
of the four methods to perform, is easily interpreted,
and (we will show in this paper) yields results similar
to the more elaborate BP method. SVD is a funda-
mental matrix operation, a generalization of the di-
agonalization procedure that is performed in PCA to
matrices that are not square or symmetric. It is available
in almost every linear algebra or statistics software
package, takes approximately the same amount of

JOURNAL OF CLIMATE

VOLUME 5

computer resources as diagonalizing a square matrix,
and has a wide variety of applications in fields such as
inverse theory. Like CCA, SVD isolates linear com-
binations of variables within two fields that tend to be
linearly related to one another. The optimality criterion
in SVD is somewhat different than that used in CCA.

SVD was first used in a meteorological context by
Prohaska (1976) to document the simultaneous rela-
tionships between monthly mean surface air temper-
ature over the United States and hemispheric sea level
pressure patterns. It has been used by Lanzante (1984)
to study the relationship between seasonal mean ex-
tratropical SST and 700-mb height anomalies and by
Dynmnikov and Filin (1985) to document the rela-
tionship between extratropical SST fluctuations and
atmospheric heating fields during the year of the GARP
Global Weather Experiment.

This paper introduces a conceptual framework in
which these methods are compared (section 2) and
summarizes their salient features (section 3). In section
4, a simple but geophysically relevant model system is
introduced. We compare the quantitative performance
of the methods in isolating a “coupled” signal as we
vary parameters such as the spatial localization of the
coupled signal, the number of sampling times, the
number of grid points in each field, and the ratio of
the coupled signal amplitude to uncoupled variability.
In a companion paper (Wallace et al. 1992), we have
compared the performance of SVD, CCA, and CPCA

‘in documenting the relationships between SST anom-

alies and anomalies in the atmospheric 500-mb geo-
potential height field over the North Pacific.

2. Nomenclature

In this section, some concepts and nomenclature that
are common to all methods of identifying correlated
patterns from observations of two time-dependent
fields. Consider a “‘left” data field s(x, t). In the com-
panion paper, this field consists of SST anomaly values
at N, grid points x; for T observation times. Consider
another “right” data field z(y, tf), consisting of 500-
mb height anomaly values z,(1) at N, (possibly differ-
ent) grid points for the same T observation times. We
will always denote time series by the notation (t) and
vectors (whose components do not depend on time or
are all observed at the same time) with boldface type.
In the companion paper, each time series is normalized
to unit standard deviation, but for this analysis we will
require only that the time series both have zero mean.
Note that any analysis of the coupling between the fields
will give meaningful results only if there are significant
correlations between some of the s;(t) and some of
the z,(f).

The data time series s(t) and z(t) at each of the grid
points can each be expanded in terms of a set of N
vectors, called patterns, which will depend upon the
analysis method used:

--- PAGE 03 ---
JUNE 1992
N
s(t) <= 8(t) = 2 ax(t)px, (1a)
k=1
N
z(t) <— Z(t) = 2 Alt)ax. (1b)

k=1

The time series a;,(t) and b,(t) are called expansion
coefficients and are also method dependent. With a
limited number N < T of patterns p, and q,, we may
not be able to recover the exact gridpoint time series
no matter how the expansion coefficients are chosen,
hence the notation ‘““<-”’ instead of “=.” In general, it
is required that the “synthetic” time series §(7) and
Z(t) be “as close as possible” (again, the meaning of
this varies with the method) to the actual time series.
For all methods discussed, the expansion coefficients
are calculated as weighted linear combinations of the
gridpoint data:

N,
a(t) = >) uxs;(t) = uks(2),

i=]

(2a)

Nz
Dt) = D vjez(t) = vex(t). (2b)

j=l

The vectors u, and v; will be called weight vectors.

Together, each pair of patterns, the corresponding
pair of weight vectors, and the pair of expansion coef-
ficients define a mode. Throughout the text, p, and q,
will always be used for the patterns, and u, and vy, for
the weight vectors associated with a mode, regardless
of the analysis method being discussed. The convention
is that individual grid points of the left and right fields
will always be subscripted with i and j, respectively,
and that individual modes of the two fields will always
be subscripted with k (and /if more than one mode is
referenced).

All of the methods can be discussed in terms of the
covariances between gridpoint observations of the
fields. Let (f(t) denote the time average of a time
series f(t) over the 7 observation times. It is convenient
to define the single-field covariance matrices

Cu = (s(t)s7(t)) (N,XN,), (3a)
Cre = (2(t)27(t)) (NX Nz), (3b)
the cross-covariance matrix between the fields
Cy. = (s(t)z7(t)) (N, X Nz), (3c)

and the combined covariance matrix
Core = ((8(t)|2(2)) (s(t) |2(2))7)
((N; +N.) X(N; + .N-z)). (3d)

For several of the methods PCA must be performed
on one or both of the fields or their combination. The
following notation is used:

BRETHERTON ET AL.

543

eigenvalues and eigenvectors of C,,: (Am, @m);
normalized left PCA expansion coeflicients: a,,(t)
eigenvalues and eigenvectors of C,,: (kn, fr),
normalized right PCA expansion coefficients: 8,,(¢)
— _,-1/2,T
= Ky !*z" (t) fh.

For PCA, the eigenvectors are spatially orthonormal
and the normalized expansion coefficients are uncor-
related and have unit variance. It will sometimes prove
useful to express the time series for one or both fields
in terms of its PC (principal component) basis, in which
the EOFs (eigenvectors of the variance matrix ) of this
field are used to define the spatial structures and their
associated normalized time series of expansion coef-
ficients specify the temporal evolution.

a. Correlation and covariance maps

Using the expansion coefficients a;,(t) and b,(¢) from
any method, two types of correlation maps can be gen-
erated. Let r[ f(t),g(t)] denote the correlation coefh-
cient between two time series f(t) and g(t) (if one of
the two time series is a vector, we mean the vector of
correlation coefficients between its component time
series and the other time series). The kth left homo-
geneous correlation map is defined to be the vector
r[s(t),a,(t)] of correlations between the gridpoint val-
ues of the left field and the kth left expansion coeff-
cient. Similarly, the kth left heterogeneous correlation
map is the vector of correlation coefficients between
the gridpoint values of the left field and the kth ex-
pansion coefficient of the right field. The left homo-
geneous correlation map is a useful indicator of the
geographic localization of the covarying part of the s
field, while the left heterogeneous correlation map in-
dicates how well the grid points in the left field can be
predicted from the Ath right expansion coefficient (de-
rived from the right field). All of this discussion applies
equally well if ‘‘left” and “right” are interchanged.

In a parallel manner, one may also define homo-
geneous and heterogeneous covariance maps of the co-
variance of an expansion coefficient with gridpoint
values of a field. If the gridpoint data are normalized,
the covariance map is proportional to the correlation
map. If in addition the expansion coefficient has vari-
ance one, the two maps are identical.

b. Comparative measure of explained covariance

It is useful to have a measure that indicates how
successful each method has been in explaining the ob-
served covariance matrix C,, between the fields using
a small number N of the dominant modes. In this sec-
tion, we introduce one such measure, called the cu-
mulative squared covariance fraction, or CSCF. Let Cy
be a synthetic covariance matrix constructed as ex-
plained below using just these N modes. The cumu-

--- PAGE 04 ---
544

lative squared covariance fraction explained by these
modes is defined as

ICszll
Here the Frobenius matrix norm of C (denoted by
subscript F) is defined to be the square root of the total

amount of squared covariance summed over all entries
in C:

CSCFy = 1 - (4)

N; N, z
IClz= > D Ch. (5)

t J
The CSCF will be close to unity if the synthetic co-
variance matrix is a good fit to the actual covariance
matrix and less otherwise. The squared covariance
fraction SCF, explained by a single mode k can be
defined similarly by using just mode k to construct C..

To calculate Cy, a synthetic time series §y(t) of left

field gridpoint values of the left field using just the first
N modes. The synthetic time series is the sum over the
modes of the product of the left expansion coefficient
with the left spatial pattern for that mode:

N
Sn(t) = D a(t) De. (6a)
k=

A similar synthetic time series Z,(¢) is found for the
right field:

N
En(t) = D by(t)ax.
k=1

(6b)

The synthetic covariance matrix is then defined as

Cy = (8y(1)2K(t)). (7)
3. Salient features of some analysis methods for
coupled fields

Table 1 summarizes the analysis methods that are
compared in this paper. Each method satisfies some
optimality criterion (although for PCA, the optimality
criterion is based on one field only, rather than any
measure of correlation between the fields). In this sec-
tion we will elaborate on Table 1 and will discuss for
each method how left and right patterns are deduced
and the relevance of the optimality criterion to pattern
finding. The formulas in Table 1 for the synthetic co-
variance matrix for each method can be derived using
the orthogonality relations for the given method in (6).

a. Singular value decomposition

Singular value decomposition (SVD) is a funda-
mental matrix operation that can be thought of as an
extension to rectangular matrices of the diagonalization
of a square symmetric matrix. As shown below, singular
value decomposition of the cross-covariance matrix
identifies, from two data fields, pairs of spatial patterns

JOURNAL OF CLIMATE

VOLUME 5

that explain as much as possible of the mean-squared
temporal covariance between the two fields. The ab-
breviation SVD will be used to denote both the general
matrix operation and the specific application to C,,;
the meaning should be clear from the context.

In SVD a spatially orthonormal set of patterns, which
will be specified presently, and a synthetic time series
§(t), formed as a linear combination of patterns will
be considered to be as close as possible to the true time
series s(t) of a field if at all observation times s(¢) — §(t)
is orthogonal to all N patterns. Then the expansion
coefficients are just generalized Fourier coefficients and
the weight vectors are just the patterns themselves:

Ue = Pe, Ve = Ok. (8)

Because the patterns are spatially orthonormal, the left
expansion coefficients can be thought of as the projec-
tions of the vector s(t) on the left patterns, and similarly
for the right field.

The “leading” patterns p, and q, are chosen as fol-
lows: The projection a;(f) of s on p, has the maximum
covariance with the projection 5,(f£) of z(2) on q;. Suc-
cessive pairs (p;,, q,) are chosen in exactly the same
way with the added condition that p; is orthogonal to
Pi,--- 5 Pe-1, and q, is orthogonal to q,,..., Gx-1-

The covariance of a,(t) and b,(¢) can be written
using (1c, d) and (2) as:

{ai(t), b\(t)) = pf C..q) = max. (9)

The choice of p; and q, that will maximize this co-
variance is deduced from the singular value decom-
position of C,,, whose properties are discussed by
Strang (1988, pp. 443-452). Here, some important
properties of the SVD are summarized for application
to our problem.

(Si) Any N, X N, matrix C can be decomposed
uniquely as follows:

R
C= > odaz, R<min(N,, N,),
k=l

(10)

where the 1, are an orthonormal set of R vectors of
length N, called the /eft singular vectors, the r, are an
orthonormal set of R vectors of length N, called the
right singular vectors, and the o;, are nonnegative num-
bers called the singular values, ordered such that o;
2o,2 +++ 2o,and Ris the rank of C.

(82) Ch, = OLF ks Cri, = Oxy.

(S3) The o? are the R nonzero eigenvalues of C7C
and CC’. The remaining eigenvalues of these two ma-
trices are zero, For a covariance matrix taken from T
observations, there are at most 7 — 1 nonzero singular
values (the rank of C is no larger than T ~ 1). The
rank is J — 1 rather than T because one degree of
freedom is lost when the sample mean is subtracted
from each observation to calculate covariances.

--- PAGE 05 ---
545

BRETHERTON ET AL.

JUNE 1992

“Pley 1811 ay UO puadap jou sop (7)%7 1UaTIYJa09 UOTsURdxa ATUO 9Y} ‘WOdT 104 “spiay Y10q BuNYSIaM 103994 1YyBIam aU ST MIYI VWOdD 104 (og)

(19) = gO-D Jo yues oyp st (2 ’
*PIPY Jeu) Jo aouvLeA ati Jo uOMOBY (%O/ “8'9) pjoysary) & UTe[dxa ye Play YoRa Jo s.jOY Jo Jaquinu WMUIIUTUL ay} d3ey 0} St 2910)

Nr 0

0 tn

ew xe = ) = win xn “(ele |) =a TW x (

‘Ny 0
o

=V['W x ‘N] ('Na]- + |'8) = Teg

“TET S Y OST “(*D) VOd UI syuaIsyja0o uorsuedxa !ay SuIpesy ay) JO Joyoaa-"Ay ue “('N0 «2. . 10) = (7)0 ay en)
YS sUQ “Ussoyo Jasn are “Ay pue "A (5)

‘T— CN “n)xeul <7 yey} sormbar sry. ‘ajqnueaut aq isnut “9 pue *D (es)
“DO Jo yues st (7 “NUM S Y cg)
“SUOISUSUNIP 9}OUP SJayxOeIq aIENDS (og)

sapoul Af JO} xuyeU

Ib%d t= = =
yord "4 Pwd ' 2c pbrd*d tt pbid7g '=37 ybd%0 1-47 JOUBLBAOD oNNayIUAS
yo = iF tale) Wo — i oe ,
Pe + 'b.b ‘id id Pig =li.ta Aig = a
1g e878 MG = BB = yoy +9079 "td Kq paoejdar "0 "9% = ('q tn) "9 % (14 Iq) <'q ty
@ = (40%) PQ = (10%) YIM WOOD [ROISSE]O se auIES Fe = (iq 1g) = Civ tp) Aero = ¢'q tn) suonejal AypeuosoyC
%» 7) Cg ‘s) sdew
*b “d *b *d ‘bd "dd ‘bd dtd *b49 Adt0 RAR Essie
» ‘a , Cg °Z) ‘Clo ‘s) sdew
» ‘d 1b 1d » 4d W794 il ie) SUBUIRAOD SnosuasOWOL]
2%q (a)
vas (y'e (2) (2)%2 (7% (Nga (2)0 + (Za (Stn (YZ 74 Qs-% swuamyjooe voneedieg
BED y IN 7a, ty yt 49,1 LWA 1], VI se) in 4 1 "4% Od suoneg
(98) 4X (0984-74 y-Wa te) J ote) 4 q Ya “in s101994 ISI,
weary yeT way YeT wary Yel wary yeT qwsry yeT
(YZ G)S)- 78,4 = (1)
(Sta, 2X = (7) SJUdTOYJI0O
uOIsUBdXd PazeULION [@n]*2

s}US1OJa09
uolsurdxa poziyeulion,
‘[EEN]}* sioyoauastq
“ty sanpeauasio ‘Ay
(®0) WOd

*IO}9A IYBIOM YO] IYI
Aq pourejdxe ppey Ye]
SY} Ul SOURLIBA SOZIWIXE]

7N + ‘NC§|?9) = 78
SIOJOOAUISIT
“th sonpeauadia 747 + SAT
(7*°D) Wod

“SPIPg

YJOq UI SJUSUITO JO UNS

poiysiom eB Aq poureldxo
SOURLIRA SOZIUNIXEI

SIOJDOA IENBUIS IYsTY
UN $20199A re[nsuls yoT
"4d sanqea JepNsuts y
wal'N X 'N](9?D) GAS

(es) SHOU
yysu %ay Burpeay oo
psafoid oie eep 1Yysu
pue sjOd yet A’ urpesy
010 pajysofoid ore eyep
42] Jaye suns poyysion
TYSU pue Ye, usemjoq
UOTEPILIOD SOZIWIXeY]

END srowon sepndurs 1y8ry
[NT 4 sxo1ea sepndurs yor]
ag" sonea sendus Y
yO" Dy2D) GAS

‘suns payysziom
1YyZU pue yor UsomIeq
UONP[ALIOD SOZIUITXe

[7N]%4 store semndurs 1WsTy
[ATT s10190a sejnBurs yo]
ag’) Sanyea Jepnsuis y

(79) GAS

“sapoul
jo Joquinu UdAId & JOJ
5) 0} 1Y JIQISsod ysaq 9U3 ST
XUJEUI SOUBLIRAOD STOYIUAS
‘SUNS poyysiom poziTeuiou
Ajfeneds yysur pue yoy
U39M19qQ DOULLIVAOD SOZIUITXE|A

s}nso1/suonesadO

Ayadoid Ayewundo

VOdT

VOd2

dd

VOD «[ROISSETD,,

GAS

polo

“SP[9Y OM] UI SUJONIed Po}DsUUOD SUIUTUIA}SP JO} spoyJoU Jo UOsUedUIOD Y ‘| ATAYL

--- PAGE 06 ---
546

(S3) The 1, are the eigenvectors of CC’ with non-
zero eigenvalues, and the r; are the eigenvectors of C7C
with nonzero eigenvalues.

(S5) For a square symmetric matrix, the left and
right singular vectors are both equal to the eigenvectors
and the singular values are the absolute values of the
eigenvalues.

(S6) The square of the Frobenius matrix norm of
C is the sum of the squares of its singular values:

R
ICllz= > of. (11)
k=1

The SVD can be computed with an efficient, nu-
merically stable algorithm available in most linear al-
gebra software packages (such as LINPACK and
MatLab). For a full rank matrix C with R = N, < N,,
the method takes O(.N,N2) floating point calculations
(flops) (Golub and Van Loan 1983, p. 175). A
straightforward but numerically less attractive method
of obtaining the singular values used by Prohaska
(1976) and Lanzante (1984) is to use (S3) and com-
pute the singular values and right singular vectors as
the eigenvalues and eigenvectors of the matrix CC’;
one can then find the left singular vectors from (S2).
The advantages of the former method, as discussed by
Golub and Reinsch (1970), are that it is more nu-
merically stable and requires only a fraction of the
number of flops.

With these properties in mind, the spatial patterns
p; and q, we now expand in the bases of left and right
singular vectors, respectively:

Ng

| 2 Mmm, (12a)
m=!
Nz

a = > mtn. (12b)

n=l

Taking the inner product of (12a) with itself, using the
orthonormality of the 1, and noting that |p,| = 1, we
deduced that || = 1. Similarly || = 1. Substituting
(6) and (7) into (5), we find that

Ns Nz r
<ay(t), by(t)> = 2 D Umtn & Oplmlpl p¥n
m=) n=1 p=

r r
= > MpNp Op S o| > HpNp|
p=1 p=1

< oi |ulln| = 0. (13)
This relationship becomes an equality only when
=m = 1 and all other coefficients y,, 7, are zero; that
is, when p,; = },, q; = r1. Hence, the maximum co-
variance is equal to the largest singular value o, and is
obtained by projecting the left field s(t) onto the first

JOURNAL OF CLIMATE

VOLUME 5

left singular vector and the right field z(¢) onto the first
right singular vector.

Similarly, the subsequent pairs of patterns that ex-
plain the maximum amount of covariance of the two
fields, subject to the constraint that they be orthogonal
to the previous patterns, are the pairs of left and right
singular vectors:

Pe=h, ak = ¥x. (14)

The total (squared) covariance explained by a single
pair of patterns is o%, so that the squared covariance
fraction, or the percentage of the (squared ) covariance
explained by a pair of patterns, is [ from (S6)}:

SCF, = SMht)> bel)” _ _ oh
2 of
i=1

15a
[Cal (15a)

Similarly, one can show that the cumulative squared
covariance fraction of C,, explained by the leading N
modes is
N
ok
k=l

CSCFy = r
Dy ok
k=1

(15b)

Stewart (1973, Theorem 6.7, p. 322) showed that
for a given matrix C,,, the matrix C of rank N that
minimizes ||C,, — Cll-, and hence the SCSF, is given
by the first NV terms in the SVD of C,,. For any of the
methods discussed, the synthetic covariance matrix
derived using N modes has rank N. Hence, SVD is an
“optimal” method in that it explains the maximum
possible CSCF with N modes.

The CSCF is an analog for a covariance matrix of
the “cumulative variance fraction” explained by the
leading modes in PCA analysis. If the left and right
fields s and z are identical, (S5) implies that PCA and
SVD will yield equivalent results with the singular val-
ues o; equal to the mode variances ), (the eigenvalues
of the variance matrix). Note that in this case, CSCF,
as obtained from (15b), approaches unity more rapidly
with the incorporation of additional modes than the
cumulative variance fraction CVFy = > #1 Ag/ Des
d,, because the variances are sguared in the CSCF,
emphasizing the leading modes with larger mode
variances. Thus, large CSCF is less significant than
large CVF.

Once a;(t) and b,(t) are obtained from SVD, we
can generate heterogeneous and homogeneous corre-
lation maps, as defined in section 2. If the time series
have been normalized, the left heterogeneous corre-
lation map is proportional to the left singular vector.
From (1d) and (S1):

r[s(t), Di{t)] = (s(t) bx(t))/Cbe(2))',
if (s(t?) = 1 Vi

--- PAGE 07 ---
JUNE 1992

= s2Ox/(bz(t))"””,

= (on/(b3(t))”) px. (16a)

Note that the kth left homogeneous correlation map
is not proportional to p,;; in fact, from (1c) one can
deduce that for a normalized time series

r[s(t), ax(t)] = Coe/(ak(t)>. — (16b)

The schematic flow chart in Fig. 1 illustrates the
steps involved in SVD. In this figure, a vector is rep-
resented by a typical component of that vector with
subscript i for the left field and subscript j for the right
field. First we compute the SVD of the covariance ma-
trix between the two fields (triangle). The gridpoint
data are projected onto its singular vectors to obtain
the expansion coefficients a,(t) and b,(t). Last, the
expansion coefficients can be correlated with the grid-
point data to find the correlation maps.

b. Canonical correlation analysis

Canonical correlation analysis is a technique that
isolates the linear combination of data from the left
field and the linear combination of data from the right
field that have the maximum correlation coefficient.
This pair of time series is more strongly correlated than
the expansion coefficients of the leading pair of patterns
deduced from SVD, but explains a smaller fraction of
the covariance between the two fields.

To identify the linear combinations a(t) and b(t)
that are maximally correlated, we express them in terms
of unknown weight vectors multiplying time series of
the left and right fields:

a(t) = u's(2), (17a)
b(t) = v"z(t). (17b)

Without changing the spatial structure of the left and
right weight vectors (and hence the correlation between
the left and right expansion coefficients), we can require
that a(t) and b(t) be normalized to have variance 1

Ca z;(t)
Cyz
1 [a] r[by,2)]
| | /
ay (t) <— Dix jk —> 6, (0)
Ok

Fic. 1. A schematic outline of the computational procedures used
in direct SVD. The SVD operation itself is represented by the triangle.
All vectors are written in component form.

BRETHERTON ET AL.

547

(because the correlation coefficient is unchanged when
the expansion coefficients are multiplied by constants).
To retain the terminology introduced in section 2, a(t)
and b(t) will be called the left and right expansion
coefficients, respectively (rather than the predictor /
predictand terminology used in many papers on this
subject), and u and v the left and right weight vectors
(rather than the commonly used term “‘canonical vec-
tors’).

In SVD, the weight vectors are constrained to be
mutually spatially orthogonal, so generalized Fourier
analysis guarantees that the gridpoint data can be re-
covered as the sum of the expansion coefficients mul-
tiplied by their respective weight vectors; that is, the
patterns are the same as the weight vectors. In CCA
the expansion coefficients are constrained to be tem-
porally uncorrelated, but in general the weight vectors
are not spatially orthogonal. Hence, the patterns are
not the same as the weight vectors. The weight vectors
indicate which gridpoint values are dominant in form-
ing the expansion coefficient. As will be shown in sec-
tion 3b.(2), for CCA the patterns are the homogeneous
correlation maps, which show how individual gridpoint
values are correlated with the expansion coefficient. As
with SVD, the left and right weight vectors and ho-
mogeneous correlation maps are important pairs of
fields to examine when using CCA.

There are two mathematical approaches to CCA—
a “classical” treatment found in many texts on mul-
tivariate analysis (e.g., Anderson 1958, among others)
and an approach due to Barnett and Preisendorfer
(1987) in which the time series of each field is filtered
by projection onto a leading subset of its EOFs and
then the maximum correlation between linear com-
binations of the filtered time series of the two fields is
sought.

1) THE CLASSICAL APPROACH TO CCA

In the classical approach, the weight vectors are
found by solving the following constrained maximi-
zation problem using Lagrange multipliers:

rla(t), b(t)] = (a(t) b(t)
= u?(s(t)z"(t))v = max,

with

It

(a?(t)) = u7(s(t)s7(t))u = 1 and
(b?(t)) = v7(z(t)z7(t))v = 1. (18)

We can simplify the appearance of the constraints by
defining “normalized” weight vectors a, and %; such
that

— -1/2A
ue = Ce) i,

(19a)

Substituting (19) into the maximization problem (18)

--- PAGE 08 ---
548

transforms it into the equivalent maximization prob-

lem:

(a(t)b(t)) = a74¥ = max, 4 = C3)/?C,,Cz}/
(20a)

with

{a’(t)) = a= 1

and (b7(t)) =97¥ = 1,

(20b)

which has a form identical to the maximization prob-
lem (5). Therefore, the solution is given by the SVD
of A, as pointed out by Nicholls (1987) and as indicated
in Table 1. The normalized weight vectors are the
singular vectors of A; the weight vectors are found
from (19).

The singular values p; are usually referred to as the
canonical correlations. They are the correlation coef-
ficients between the left and right expansion coefh-
cients. The left and right expansion coefficients a;(t)
and b,(t) are obtained by substituting the left and right
weight vectors u; and v; into (17). They obey the tem-
poral orthogonality relations shown in Table 1. Each
expansion coefficient pair has the maximum possible
correlation coefficient subject to the restriction that the
left expansion coefficient is uncorrelated with all the
previous left expansion coefficients, and similarly for
the right expansion coefficient.

The patterns are chosen such that the rms difference
between the real and the synthetic time series for both
left and right fields at each grid point is minimum.
Note that this is a different and perhaps more natural
fitting criterion than used for the SVD method. Math-
ematically, we choose px to minimize <[s;(t)
— §;(t)]?); similarly for the q;, using z. The temporal
orthonormality of the expansion coefficients makes this
easy; the minimum error is obtained by choosing the
patterns to be the temporal projection of the time series
onto the expansion coefficients:

Die = (Si(thax(t)) or px = (s(t)ax(t)), (21a)

Ge = (Z(t)bAt)> or gx = Cz(t)b(t)>.  (21b)

Since the expansion coefficients have unit variance,
the homogeneous correlation maps are the same as the
patterns for normalized data, as indicated in Table 1.
Expressing the expansion coefficients as inner products
of the fields and the weight vectors using (2) in (21)
implies that

(22a)
(22b)

In geophysical applications, the number of observation
times may be less than the number of grid points in
the spatial fields. In this case, the matrices C,, and C,,
are not of full rank and are not invertible. A solution
can still be obtained using a generalized inverse or
““pseudoinverse” (see Muller 1982; or Kharti 1976),

Pr = Cyst,

a = Cr :

JOURNAL OF CLIMATE

VOLUME 5

but this solution is more difficult to calculate and in-
terpret. In fact, unless the number of observation times
is much larger than the number of grid points, the same
problem shows up in another form (Preisendorfer
1988): the random sampling fluctuations in the co-
variance matrices create pairs of weight vectors with
serendipitous extremely high correlations. An example
of this small sample size sensitivity is presented in sec-
tion 4.

2) CCA IN THE BASIS OF PRINCIPAL COMPONENTS

An alternative approach to CCA (Barnett and
Preisendorfer 1987) is preferable because it circum-
vents the aforementioned problem. The two fields are
prefiltered by retaining only the projection of each field
on a subset of its EOFs then applying CCA. If all the
EOFs of both fields are retained, the results of this
method are identical to those of the classical approach
to CCA; prefiltering by retaining only a few leading
EOFs decreases the number of degrees of freedom in
each field and renders the resulting modes more stable
with respect to sampling variability. This filtering may
introduce systematic biases into the predicted weight
vectors; these will be addressed in section 4.

To prefilter the fields, each is expressed in its PC
(principal component) basis as defined in section 2.
In the PC basis, the projection of the left field onto its
N, leading EOFs can be written as the N,-vector a(7)
with components a;(¢),..., @y,(4), and the projection
of the right field onto its Ny leading EOFs is the N>-
vector 6(t) with components §)(1),..., 8n,(t). Note
that any linear combination of filtered gridpoint time
series can just as well be written in the PC basis as an
equivalent linear combination of the expansion coef-
ficients retained. Therefore, CCA can be done in the
PC basis using the fields a(t) and 8(t). The temporal
orthonormality of PCA expansion coefficients guar-
antees that

Con = Co(thaT(t)) =1 (23a)
Cog = B(1)B7(t)> = I. (23b)

Hence, in the PC basis, CCA reduces to finding the
SVD of Cy, and the left and right weight vectors are
just the left and right singular vectors 1, and f;, of this
matrix. The expansion coefficients are then found as
inner products of these weight vectors with the fields
(in the PC basis) as indicated in Table 1.

Using (8) the inner product for the left expansion
coefficient can be written in the form ufs(t), where
u; can be interpreted as the left weight vector in the
gridpoint basis, and is given in Table 1. The expansion
coefficients obey the same temporal orthonormality as
in classical CCA, since we have just applied to an un-
conventional pair of fields. Hence, formulas (21) and
(22) for the patterns still apply. When applied to the
BP left weight vector, (22) yields the left pattern given

--- PAGE 09 ---
JUNE 1992

in Table 1. Similar formulas are given for the right
expansion coefficient, weight vectors, and patterns.

The computational scheme for CCA is outlined in
Fig, 2. First a PCA of each field is performed (squares),
and then the normalized expansion coefficients a,,(7)
and 8,,(t) of the leading modes are computed. To high-
light the fact that only a subset of the PCA modes is
retained the squares are darkened. Then the SVD of
the covariance matrix between the expansion coeffi-
cients is found (triangle), the outputs of which are the
canonical correlations p, and the weight vectors uj, and
vj, in the PC basis. From these weight vectors, the CCA
expansion coefficients a,(¢) and b,(t) are obtained and
correlated with the gridpoint time series to generate
the homogeneous correlation maps. Last, the weight
vectors u, and v; in the gridpoint basis can be found
from (22).

Had we not normalized the expansion coefficients
and truncated the linear combinations before calcu-
lating the SVD, we would have recovered precisely the
same result as found in SVD. The normalization, which
magnifies the role of EOFs that account for little of the
variance in their individual fields and are subject to
large sampling fluctuations (North et al. 1982), is one
way of understanding the poor small-sample stability
of CCA. Prefiltering using BP circumvents this diffi-
culty by entirely neglecting the EOFs with small vari-
ances. SVD, by maximizing the covariance (rather than
the correlation ) between the paired linear combinations
[a,(t), b,(t)] of the two fields, also selects linear com-
binations of the field variables that not only are well
correlated but also each have a large variance and,

S;(t) Zz; jC)
A — — normalize - — -f
a i a (t)

Am Kn
Cim fin
a;,(t) we

Lr [ay s} Ny u’ v'
sa | a nk
eet a

ve
Px

Fic. 2. As in Fig. | except for CCA. The squares represent PCA
operations. PCA and SVD symbols are darkened for steps in which
only a leading subset of the modes in the expansion is retained.

BRETHERTON ET AL.

549

hence, tend to be dominated by the leading EOFs of
the fields. Therefore, it should come as no surprise that
the performance of BP-prefiltered CCA and of SVD
on the example presented in section 4 are quite similar.

The parameters N, and N2 must be chosen so as to
retain only the “important” EOFs. Both N; and N2
must be less than the number T of observation times,
or else modes explaining no variance will be retained.
In fact, artificially high correlations will likely be ob-
tained unless N, and N> are both only a small fraction
(10% or less) of N,, the number of temporal degrees
of freedom in the dataset (Davis 1976; also see section
4). Here N, is T divided by an integral autocorrelation
length that measures how many successive observations
tend to be temporally correlated. If successive obser-
vations are independent, then the integral autocorre-
lation length is 1 and N, is 7, Otherwise, N, will be
less than J. If too few modes are chosen, correlated
parts of the two fields may be discarded (see Joliffe
1982).

In the remainder of this paper, we will choose N;
and N; to be the minimum number of EOFs to account
for at least 70% of the variance of their respective fields.
This method is referred to as BP70. As discussed in
section 4, this leads to weight vectors whose expansion
coefficients are both highly correlated and “small-sam-
ple stable” (and hence presumably physically mean-
ingful). Tests are performed using the model of section
4, with explained variance thresholds of 70%, 80%, and
90% to determine which threshold gave the optimal
trade-off between random errors due to sampling fluc-
tuations (which dominate when the threshold becomes
too close to 100% and a large fraction of the EOFs are
kept) and systematic errors (which are large when the
variance threshold is low and too few EOFs are kept
to adequately represent the dominant coupled pat-
terns). It was found for our model problem that the
80% threshold usually led to slightly larger errors than
the 70% threshold, while the 90% threshold led to sub-
stantially larger errors.

3) AN SVD PREFILTER FOR CCA

In the companion paper ( Wallace et al. 1992), SVD
is compared with a variation of CCA that uses a
straightforward variation of Barnett and Preisendorfer’s
prefiltering scheme of using only the first few expansion
coefficients. In place of the gridpoint data, CCA is
applied to time series d,(¢) and 5,(t) of the expansion
coefficients of the NV leading SVD modes, but then no
further filtering is done. The number N should be cho-
sen to be as small as possible, consistent with the first
N modes accounting for most of the covariance be-
tween the fields; in the companion paper the sensitivity
of CCA to N. Our Mth CCA solution represents the
linear combination of the first N modes of the original
SVD solution that maximizes the correlation coeffi-

--- PAGE 10 ---
550

cients between the respective SST and 500-mb height
time series. To recover the weight vectors in the grid-
point basis requires two steps. First, we proceed as for
classical CCA to find the weight vectors a, and %, of
length N in the basis of the SVD modes. Second, the
N, X N matrix P whose columns are the N leading left
singular vectors from the SVD analysis and the N,
x N matrix Q whose columns are the N leading right
singular vectors are formed. It follows from (1c, d) and
(17) that the weight vectors in the gridpoint basis are

y= Pi, (24a)

Vi = OV>~. (24b)
Figure 3 diagrams this computational scheme for CCA.
In this diagram, the subscript h is the index of a mode
retained after SVD prefiltering, and m and n are indices
of the s and z EOFs and expansion coefficients derived
from the subsequent PCA. Figure 3 is the same as Fig.
2 except that it is encased by an outer shell in which
the SVD operation is performed on the gridpoint fields

Coz
a a, (t) 6y(t) i
J | IN
“| ey PS
iw 4 B,(t)
Aum Cog Ky
Pih hm fhn jh
. t b(t
Pa rv 4
ar Umk | Vink t [by,2)]
v

Uhk hk
Px

Fic. 3. As in Fig. 2 except for CCA using SVD
in place of PCA as a prefilter.

JOURNAL OF CLIMATE

VOLUME 5

to get prefiltered time series for the first NSVD modes,
which are used as input to the CCA. The PCAs are not

used to further filter the data, so the squares are not
darkened.

c. CPCA and PCA

The PCA separates a field into modes using its own
covariance matrix. The terminology of expansion coef-
ficients, weight vectors, and patterns is still applicable
to this situation and leads transparently to all of the
formulas given in Table 1 for CPCA. In LPCA (one-
field PCA based on the EOFs of the left field), the
modes of the left field are deduced from PCA, and then
patterns in the right field that best correlate with each
of these modes are found. Hence, the method is asym-
metric. The expansion coefficient used for both fields
is the normalized PCA expansion coefficient for the
left field. The left weight vector and pattern follow di-
rectly from PCA of the left field. Since the expansion
coefficient does not depend on the right field, the right
weight vector is zero. The right pattern is again found
from (21) and (8) since the expansion coefficients are
temporally orthonormal:

Vi = Cag(t)2(t)) = Az? Chip. (25)
The left homogeneous correlation map will be the EOF,
while from (25) the right heterogeneous correlation
map is the right pattern. Similar results hold for RPCA
in which PCA is done on the right field and the ex-
pansion coefficients of the resulting EOFs are correlated
with the left field.

4. A comparative example of SVD, CCA, BP,
CPCA, and OFPCA

The example in this sections illustrates some of the
trade-offs intrinsic to each method. No one example
is universally applicable, so the conclusions are only a
loose guide to the performance of the methods on geo-
physical datasets.

a. Description of a model coupled system

Let us imagine that time series of SST are measured
at two “rakes” of observing stations (Fig. 4). Each rake
consists of a series of N stations, all at the same lon-
gitude but at different, fairly closely spaced latitudes.
Such a rake might be set up to detect equatorially
trapped wave modes in the atmosphere or ocean. The
two rakes are assumed to be relatively far apart in lat-
itude—one might be in the west Pacific, one in the east
Pacific. Suppose that the SST anomaly at each station

--- PAGE 11 ---
JUNE 1992

R,(t) +nof(s) R,(t) -nof(t)

x S$], x 23
x $2 x 22
x x
x x
x Sn x Zn

Fic. 4. The model coupled system (explained in the text).

consists of spatially red noise (which is correlated with
neighboring stations but not with stations in the other
rake) plus a sinusoidal oscillation (the “signal” ) in time
whose amplitude depends on latitude and whose phase
is anticorrelated between the rakes. For instance,
imagine that when the west Pacific is warmer, the east
Pacific is colder, with maximum temperature anom-
alies occurring on the equator with a Gaussian decline
of the anomalies with latitude. Now compare how well
the various methods can isolate the spatial pattern of
SST anomalies in the two rakes associated with the
signal.

We generate synthetic time series for the two rakes,
assuming that each time the red noise is completely
uncorrelated with the previous observation time. The
time series have the form

S(t) = R.(t) + nof(t),
2(t) = R.(t) — nof(t).

(26a)
(26b)

Here R,(z) and R_(f) are vectors of temporally uncor-
related but spatially red noise of unit variance. The
latitudinal variation of the signal on each rake is given
by the vector ¢, which is normalized so that its rms
component amplitude is one. The signal-to-noise ratio
is n. It is assumed that f(t) is a periodic function of ¢
with mean zero and rms value | and that the total
length of time for which observations have been taken
is an integral multiple (or at least much longer than)
of the signal period so that ¢ f(t) = 1. For definite-
ness,

S(t) = 2)” sin(wt); (27)
any other similarly normalized periodic signal would
give essentially identical results.

We will compare the methods applied to three dif-
ferent signal shapes. In all of these cases, a rake with
more stations is assumed to sample the same signal

BRETHERTON ET AL.

551

(and the same red noise) at an increased spatial reso-
lution. The bell signal is an off-center Gaussian:

$; = Cp exp(—y7 /2)
yi =S5G-1)/(N-1)-1, 7=1, +++, N, (28a)

where c is a normalization constant. The half-wave
signal is a half-wavelength cosine wave over the span
of the rake,

ob; = Ch cos(ay;/2). (28b)

The spike signal is an off-center spike at a single station,

N72
A

To generate the red noise vector R(t) for either field,
at each time t, an independent pseudorandom Gauss-
ian white noise vector W(t, is generated. Then we use
the Markov process:

Ri(t,) = W(t)
Ri(t,) = @Rj-1(tn) + (1 — a?)'? With). (29)

The red noise generated has mean zero, variance one,
and

yi=l

(28c)
otherwise.

oj =

(R(t)R™(1)) = V(a), Vila) = al. (30)

If the number of stations is varied (corresponding to
a shorter distance between stations) we vary a so as to
maintain a fixed noise redness length L (the separation
at which the red noise correlation drops to e7'). If
length is measured in signal half-widths, the rake is 5
units long and the interstation spacing is 5/(N — 1),
so

a = exp{—5/[(N— 1)]L}. (31)

b. Method comparison for an infinite time record

In this subsection we investigate how the methods
perform if the number T of observation times is infinite,
so that the covariance matrices estimated from the data
are the true covariance matrices. In the next subsection,
we look at the geophysically relevant case in which T
is finite, so that the covariance matrices estimated from
the-data differ from the true covariance matrices as a
result of sampling fluctuations.

It is not entirely obvious how to interpret the output
of some of these methods in terms of correlated signals
in the two fields. Probably the most appropriate output
to look at is the left and right patterns. By construction,
the first left pattern when multiplied by the first left
expansion coefficient gives an estimate of the left field
that is optimal (in a sense that depends on the method
but generally maximizes some measure of coupling be-
tween the fields over all estimates based on a single
pattern ); it is similar for the right pattern. The coupling

Unauthenticated | Downloaded 02/03/26

2:44 PM UTC

--- PAGE 12 ---
552

between the fields is entirely in the signal, so the pat-
terns should reflect the signal. For the PCA-based
methods, the patterns also incorporate aspects of the
red noise within each rake as well as the signal. Since
the noise characteristics are unknown, we still interpret
the correlated signals in the left and right fields to be
proportional to the left and right patterns. For com-
parison, all of the patterns are normalized to have
mean-square component amplitude one. The different
types of normalization used for different methods pre-
clude a direct comparison of the signal amplitude pre-
dicted by the different methods. For an infinite time
record, SVD and CCA can detect the signal exactly in
both fields, while the other methods have systematic
prediction biases because they incorporate red noise
characteristics into the patterns. This can be demon-

First left pattern

—— Tne
—-— BP70
—— CPCA

° —-- LPCA
—-- RPCA

n

2

w

oO

2

Oo

wo

9

0 10 20 30

i

JOURNAL OF CLIMATE

VOLUME 5

strated by calculating the exact covariance matrices
from

Cos = Cz, = V(a) + 0°poT (32a)

Cy = — 77697. (32b)
All of the methods can be carried out knowing these
covariance matrices use the algorithms in Table 1. In
Fig. 5, results are shown for rakes with N = 36 points
each, 7 = 1, and a noise redness length L = 1. The
normalized patterns for SVD and CCA are identical
to the signal. BP70 exhibits slight biases due to the
prefiltering of the two fields. For CPCA both patterns
are biased, for LPCA the left pattern is biased but the

First right pattern

n= 36

a eta= 0.4
L=1

nt infinite

a

2

ve)

oOo

4 4

Oo

wn

°

r r

0 10 20 30
j

Fic. 5. The true (exact) bell signal in the left and right fields and the normalized patterns for N = 36, = | for BP70, CPCA, LPCA,
and RPCA given an infinite length time series. The SVD and CCA patterns are identical to the exact signal.

--- PAGE 13 ---
JUNE 1992

Leading Noise EOFs

2

n

oS

2

oa

my

id

2 |

7 \ / ——_1 (32%)
\ can ers 2 (21%)
\ / —-— 3(13%)

Seccaee" \ J
0 10 20 30

Fic. 6. The leading three EOFs of the noise covariance matrix.

right pattern is correct, and for RPCA the right pattern
is biased but the left pattern is correct. These biases
can be understood as follows. The CPCA patterns
maximize the explained variance over both fields com-
bined. If the noise is highly spatially red, most of the
noise variance can be explained by a few modes (so
that the patterns are biased toward these modes). Fig-
ure 6 shows the first, second, and third EOF of the pure
noise variance matrix V(a) for each rake. These three
EOFs explain 32%, 21%, and 13% of the variance, re-
spectively. One can see that the CPCA patterns are
biased toward the first noise EOF. Similarly, the left
patterns in LPCA are just the EOFs of the left field,
which reflect the leading modes of the left noise vari-
ance matrix V(a) in addition to the signal. The right
patterns in LPCA are exact, because the only infor-

BRETHERTON ET AL.

553

mation used about the right field is its cross correlation
matrix with the left field. Since the only correlation
between the fields is through the signal, and the left
pattern, though biased, is correlated with the signal,
the right pattern will just be the signal. Analogous re-
sults apply to RPCA.

A corollary of the above discussion is that the leading
patterns for CPCA, LPCA, and RPCA may in fact have
almost no relation to the signal, especially if the signal
is weak. For instance, suppose that LPCA is performed
when the signal is orthogonal to the leading EOF of
the noise variance and it is projected principally onto
the second noise EOF. Now consider the full left co-
variance matrix C,, of signal plus noise. For a small
signal-to-noise ratio, the leading EOF will be approx-

First left pattern

y
°
79)
Oo
o
° —— Tre
srrcosees ela = 0.2
eta = 0.25)
wo
>
4
ed
0 10 20 30

i
Fic. 7. The half-wave signal and the “exact” patterns
for CPCA as functions of the signal-to-noise ratio.

--- PAGE 14 ---
554

imately the leading EOF of the noise alone, which can
still explain a plurality of the variance. Hence, the left
pattern will have no resemblance (and in fact will be
orthogonal to) the signal. For a larger signal-to-noise
ratio, the combination of the signal and the second
noise EOF will have larger variance and the pattern
will better resemble the signal. CPCA also can be
“fooled” in this way, but only at a lower signal-to-
noise ratio, because CPCA also uses the cross covari-
ances between the fields, which are entirely due to the
signal.

To illustrate this point, the left pattern for CPCA
and LPCA is shown in Fig. 7 for the “half-wave” signal
at 7 = 0.2 and 0.25 with N = 36 and noise redness
length ZL = 1 as above. For 7 = 0.25, the pattern is
quite close to the true signal, but for 7 = 0.2, the pattern
is entirely different—in fact, it is the leading EOF of

First left pattern

——="True
oe SVD
—-- BP70

oO —_——

° CPCA

n

od

wo

3

Oo

°

”

9

0 10 20 30

JOURNAL OF CLIMATE

VOLUME 5

the noise as seen in Fig. 6. The bias in CPCA, LPCA,
and RPCA decreases rapidly as 7 is increased (see the
lower curves on Fig. 9). For the “spike” signal, which
has projections of approximately equal magnitude on
all of the noise EOFs, no method was fooled but there
was a strong bias in the leading patterns toward the
nearly uniform leading noise EOF at small signal-to-
noise ratios.

c. Method comparison for a finite time record

In geophysical applications, the number T of obser-
vation times may not greatly exceed the number of
locations N at which each field is measured. The sam-
pling fluctuations in the covariance matrices can greatly
reduce the skill of all of these methods at isolating the
signal. Using synthetically generated red noise, each of

First right pattern

2.0

1.5

1.0

0.5

0.0

-0.5

v T

0 10 20 30

Fic. 8. The left SVD, BP70, and CPCA patterns for an pseudorandom time series of 100 independent observations: N = 36, 7 = 0.4.

--- PAGE 15 ---
JUNE 1992

these methods is applied to time series of finite length.
An ensemble of 20 such realizations was used to de-
termine the “error” « for each method, defined as the
square root of the average over the 20 realizations of
the mean-square difference of the components of the
normalized left and right patterns from the signal. It
was found (at least when the signal-to-noise ratio was
not too small) that the average over all of the realiza-
tions of the patterns was very close to the infinite time
record patterns. Consequently, it is useful to decompose
the finite time record errors for each method into a
“random” component e, (the rms difference of the pat-
tern from the T = oo pattern) and a systematic com-
ponent e, due to the method bias. The sum of the square
of these errors would be exactly equal to e? if the average
patterns were the JT = oo patterns; it is slightly larger
when this is not exactly the case.

BRETHERTON ET AL.

555

Figure 8 shows the SVD, CCA, BP70, and CPCA
left patterns derived for one typical realization with the
bell signal, N = 36, 7 = 1, and T = 100. The right
patterns show the same behavior. The random error
in all the methods is noticeable. Figure 9 shows the
rms and systematic errors for 25 realizations of the bell
signal with the same rake as the signal-to-noise ratio is
varied. As is decreased, both the total and the sys-
tematic errors increase quite rapidly. If instead the
number of observations T is varied (Fig. 10) with 7
= 0.4, the systematic component of the error begins to
dominate the CPCA, LPCA, and RPCA errors for T
on the order of 10N or larger, and SVD and BP70 give
superior results. For T = 800, CCA also gives good
results. Of all methods, CPCA consistently has the
smallest random errors (as little as half that of other
methods) because it blends together all of the data and

Error vs. eta (bell)

| WA A ae

° (40 oO oe
4 (4400 4 Vy
3 Ve ee el
ae ae A

| VAR D8 A PVA

0.1 0.2 0.3 0.4

SB

NI

0.5

CCA-tot
CCA-sys
LPCA-tot
LPCA-sys
BP70-tot
BP70-sys
SVD-tot
SVD-sys
CPCA-tot
CPCA-sys

RES ess
Swaw
TANS As
S
NNN
Qe.
ae
KS)
se
NJ

an
Ra

0.6 0.7 0.8 0.9 1

ela

Fic. 9. Rms error e in detecting the bell signal using ensembles of 25 realizations as a function of n, with T = 100, N = 36.

Unauthenticated | Downloaded 02/03/26 12:44 PM UTC

--- PAGE 16 ---
556

JOURNAL OF CLIMATE

VOLUME 5

Error vs. T (bell)

error
0.6 0.8

0.4

0.2
4.

0.0

50 100

CCA-tot
CCA-sys
LPCA-tot
LPCA-sys
BP70-tot
BP70-sys
SVD-tot
SVD-sys
CPCA-tot
CPCA-sys

CZ)

400 800

FiG. 10. As in Fig. 9 except as a function of JT with n = 0.4, N = 36.

hence has four times as many covariances in which to
find a signal. Classical CCA, on the other hand, is ex-
tremely prone to random errors with T/N on the order
of 10 or less, as it is here. BP70 and SVD have com-
parable total errors, which are slightly less than those
of LPCA in this example. Essentially this is because all
of them weight modes that dominate the covariance,
which is comparatively small-sample stable. LPCA and
RPCA use just the leading EOF of one of the fields,
which is the most small-sample stable of all EOFs, but
then are vulnerable to the full sampling fluctuations of
C,,. SVD finds the coupled modes that best explain
the cross covariance between the fields. These modes
must explain enough of the variance in both fields in-
dividually to also be relatively small-sample stable. The
BP method just truncates the EOFs to the few domi-
nant (hence, most small-sample stable) EOFs in both

fields before any CCA analysis is done, so it is also a
small-sample stable method. The LPCA, RPCA, and
(to a somewhat lesser extent) CPCA may have signif-
icant systematic biases, while SVD and CCA have no
systematic bias (Fig. 9). The systematic bias of BP70
is generally much smaller than the random errors. In
general, BP70 and SVD give quite similar patterns in
the individual realizations.

With the normalizations used here, the errors are
very insensitive to rake size N. With fixed T = 100 and
n = 0.4, we compared the rms errors over 25 realiza-
tions for N = 11, 21, 36, 56, and 81. The results (Fig.
11) show essentially no dependence of the total or sys-
tematic errors on N, except for CCA, which had an
rms error of 0.5 (somewhat worse than other methods)
for N = 11 (7/N = 9) but had an error of one, cor-
responding to no skill in finding the coupled signal

Unauthenticated | Downloaded 02/03/26

12:44 PM UTC

--- PAGE 17 ---
JUNE 1992

BRETHERTON ET AL.

557

Error vs. N (bell)

1.0

error

0.5

0.0
be

CCA-tot
CCA-sys
LPCA-tot
LPCA-sys
BP70-tot
BP70-sys
SVD-tot
SVD-sys
CPCA-tot
CPCA-sys

Fic. 11. As in Fig. 9 except as a function of N with » = 0.4, T = 100.

for N = 36 (T/N = 3) or more, in accordance with
Fig. 10.

The half-wave signal produces generally similar re-
sults to the bell signal for 7 > 0.3 (Fig. 12). For smaller
signal-to-noise ratios, SFPCA and CPCA frequently err
because they do not choose the signal-containing mode.
However, the random sampling fluctuations cause
comparable errors in SVD and BP70. CCA is again
uncompetitive.

For the spike signal (Fig. 13), CCA does the best at
all signal-to-noise ratios. This is not surprising. The
spike projects significantly onto all of the EOFs of the
noise field, so methods that favor the dominant modes
filter out much of the correlation between the fields
along with the noise. However, for 7 = 0.4, SVD and
BP70 do not have significantly larger errors than CCA,
and for 7 = 0.6 CPCA also is competitive. Note that
the CPCA and LPCA errors are largely due to the sys-

tematic error, so they would not improve much with
further sampling.

5. Concluding remarks

We have reviewed several methods for finding cor-
related patterns between two fields. Table 1 indicates
how all of these methods can be brought into a unified
theoretical framework in which it is easy to compare
their performance. Each of the methods optimizes a
different measure of goodness of fit to the data. The
methods were applied to an example in which two rakes
of observing stations experience a single spatially vary-
ing signal that is perfectly anticorrelated between the
rakes, superposed on spatially red noise, which is un-
correlated between the rakes. Results from this example
suggest that if the coupled signals are similar to the
dominant EOFs of the individual fields, so that the

Unauthenticated | Downloaded 02/03/26 12:44 PM UTC

--- PAGE 18 ---
error

558 JOURNAL OF CLIMATE VOLUME 5
Error vs. eta (wave)
CCA-tot
< = _ oy CCA-sys
LPCA-tot
LPCA-sys
BP70-tot
BP70-sys
n = SVD-tot
~ Z SVD-sys
Z CPCA-tot
V (73 CPCA-sys
= 4
3 Gig
A aa el
Aa a ae
0.1 0.2 03 0.4 0.5 0.6 0.7 0.8 0.9 1

eta

Fic. 12. As in Fig. 9 except using wave signal.

systematic biases in the PCA-based methods are small,
then CPCA most accurately isolates the signal since it
has the smallest random errors. If the coupled signals
are rather dissimilar from the EOFs but are still smooth
in the sense that they project principally onto only the
leading few eigenmodes of the individual fields, SVD
and BP may be superior to CPCA. In fact, in this sit-
uation, CPCA may be “fooled” into an entirely mis-
leading first pattern if the signal is almost orthogonal
to the leading eigenmodes of the individual fields.
SFPCA may also be subject to problems with system-
atic errors and may exhibit random errors no smaller
than found with SVD, therefore SFPCA is uncompe-
titive. Classical CCA is subject to large random errors,
except for spike-like signals that excite all the EOFs of
the individual fields equally, in which case it works
best of all.

In general, SVD and BP have rather similar error
characteristics. SVD is very simple to perform and in-
terpret and requires no user-supplied parameters. The
BP method was usually slightly more accurate on our
example with a 70% variance threshold but is substan-
tially more complex to implement and requires a cri-
terion (such as the cumulative variance threshold used
in this paper) for deciding the number of modes to be
kept for each field. It has nonzero but generally insig-
nificant systematic errors. Because of their lack of sys-
tematic bias and good general performance, SVD and
BP are perhaps the most preferable for general use. A
conceptual advantage of both SVD and BP is that, un-
like CPCA, they directly produce explicit measures of
relatedness between the derived coupled patterns, An
important future area of research should be to extend
SVD or BP to cases in which one would like to find

Unauthenticated | Downloaded 02/03/26 12:44 PM UTC

--- PAGE 19 ---
BRETHERTON ET AL.

559

Error vs. eta (spike)

JUNE 1992
‘7. Ae 7
iy ,
° uy 4
Vy) Y “AV
; 4 nn a
ro) g Y y4V
t | WA a
Vy) Y Yy 4
YY) { Ya yy 4
Vy) W 4 YY
Wy) 4 WY
ol Wy y IY
2 g YY
Ve ay Y
Y Y
Bs of
a} (ay y
Y a
VAY
2 J W 9g

0.1 0.2

03 0.4 0.5

CCA-tot
CCA-sys
LPCA-tot
LPCA-sys
BP70-tot
BP70-sys
SVD-tot
SVD-sys
CPCA-tot
CPCA-sys

0.6 0.7 0.8 0.9 1
ela

FIG. 13. As in Fig. 9 except using spike signal.

coupled patterns in three or more fields; this type of
analysis is straightforward with CPCA.

The companion paper (Wallace et al. 1992) illus-
trates SVD applied to a geophysical problem, the in-
terannual coupling between wintertime Pacific sea sur-
face temperature anomalies and atmospheric 500-mb
height. It compares SVD to CCA and CPCA and PCA,
and it shows that SVD clearly isolates the two most
important extratropical modes of variability in this
case.

Acknowledgments. We would like to thank Dr. Val-
entin Dymnikov of the Center for Numerical Mathe-
matics of the USSR Academy of Sciences for bringing
SVD to our attention. Ms. Yuan Zhang’s careful read-
ing helped improve the manuscript. This work was
supported by the National Science Foundation through
the Climate Dynamics Program under Grant ATM

8822872 and the Meteorology Program under Grant
ATM 8858846.

REFERENCES

Anderson, T. W., 1958: An Introduction to Multivariate Statistical
Analysis. John Wiley & Sons, 374 pp.

Barnett, T. P., 1981: Statistical prediction of Northern American air
temperatures from Pacific predictors. Mon. Wea. Rev., 109,

1021-1041.

, 1983: Interaction of the monsoon and Pacific trade wind sys-

tems at interannual time scales. Part I: The equatorial zone.

Mon. Wea. Rev., 111, 756-773.

, and R. W. Preisendorfer, 1987: Origins and levels of monthly
and seasonal forecast skill for United States surface air temper-
atures determined by canonical correlation analysis. Mon. Wea.
Rev., 115, 1825-1850.

Cooley, W., and P. Lohnes, 1971: Multivariate Data Analysis. John
Wiley & Sons, 364 pp.

Davis, R., 1976: Predictability of sea surface temperature and sea-

Unauthenticated | Downloaded 02/03/26 12:44 PM UTC

--- PAGE 20 ---
560

level pressure anomalies over the Northern Hemisphere. J. Phys.
Oceanogr., 6, 249-266.

Déqué, M., and J. Servain, 1989: Teleconnections between tropical
Atlantic sea-surface temperatures and midlatitude 50-kPa heights
during the period 1964-86. J. Climate, 2, 929-944.

Dymnikov, V. P., and S. K. Filin, 1985: A study of the correlations
between sea-surface temperature anomalies in mid-latitudes and
anomalies in heating, based on data from the First GARP Global
Experiment. Reprint of the Department of Numerical Mathe-
matics of the U.S.S.R. Academy of Sciences. [Available from
Leninskij Prosp., 14; 117901 Moscow B-71.}

Fukuoka, 1951: A study on 10-day forecast (a synthetic report).
Geophys. Mag., 22, 117-208.

Glahn, H. R., 1968: Canonical correlation and its relationship to
discriminant analysis and multiple regression. J. Atmos. Sci.,
25, 23-31.

Golub, G. H., and C. Reinsch, 1970: Singular value decomposition
and least squares solutions. Numerical Math., 14, 403-420.

———, and C. F. Van Loan, 1983: Matrix Computations. Johns Hop-
kins University Press, 476 pp. .

Graham, N. E., 1990: Seasonal relations between tropical Pacific
SSTs and Northern Hemisphere 700-mb heights. Proc. of Four-
teenth Annual Climate Diagnostics Workshop. NOAA Climate
Analysis Center, 184-191.

Holmstrom, I., 1963: On a method for parametric representation of
the atmosphere. Tellus, 15, 127-149.

Hotelling, H., 1935: The most predictable criterion. J. Ed. Psych.,
26, 139-142.

——, 1936: Relations between two sets of variates. Biometrika, 28,
321-377.

Joliffe, 1. T., 1982: A note on the use of principal components in
regression. Appl. Statist. 31, 300-303.

Kharti C. G., 1976: A note on multiple and canonical correlation
for a singular covariance matrix. Pschychometrika, 41, 465-470.

Kutzbach, J., 1967: Empirical eigenvectors of sea-level pressure, sur-
face temperature, and precipitation complexes over North
America. J. Appl. Meteor., 6, 791-802.

Lanzante, J. R., 1984: A rotated eigenanalysis of the correlation be-
tween 700-mb heights and sea surface temperatures in the Pacific
and Atlantic. Mon. Wea. Rev., 112, 2270-2280.

JOURNAL OF CLIMATE

VOLUME 5

Lorenz, E. N., 1956: Empirical orthogonal functions and statistical
weather prediction. Sci. Rep. No. 1, Statistical Forecasting Proj-
ect, Department of Meteorology, Massachusetts Institute of
Technology.

Metz, W., 1989: Low-frequency anomalies of atmospheric flow and
the effects of cyclone-scale eddies: a canonical correlation anal-
ysis. J. Atmos. Sci., 46, 1026-1041.

Muller, K. E., 1982: Understanding canonical correlation through
the general linear model and principal components. Amer. Stat.,
36, 342-354.

Nicholls, N., 1987: The use of canonical correlation to study tele-
connections. Mon. Wea. Rev., 115, 393-399.

North, G., T. Bell, R. Cahalan, and F. Moeng, 1982: Sampling errors
in the estimation of empirical orthogonal functions. Mon. Wea.
Rey., 110, 699-706.

Obukhov, A. M., 1960: On statistical orthogonal expansions in em-
pirical functions. Izvest. Geophys. Ser. (Eng. Trans), 288-291.

Pearson, K., 1902: On lines and planes of closest fit to system of
points in space. Philos. Mag., 6, 559-572.

Preisendorfer, R. W., 1988: Principal Component Analysis in Me-
teorology and Oceanography, C. Mobley, Ed., Elsevier, 418 pp.

Prohaska, J., 1976: A technique for analyzing the linear relationships
between two meteorological fields. Mon. Wea. Rev., 104, 1345-
1353.

Spearman, C., 1904a: The proof and measurement of the association
between two things. Am. J. Psych., 15, 72-101.

~-—, 1904b: General intelligence, objectively determined and mea-
sured. Am. J. Psych., 15, 201-293.

Stewart, G. W., 1973: Introduction to Matrix Computations. Aca-
demic Press, 441 pp.

Strang, G., 1988: Linear Algebra and its Applications. Harcourt, Brace,
and Jovanovitch, 505 pp.

Wallace, J. M., C. Smith and C. S. Bretherton, 1990: Singular value
decomposition of sea-surface temperature and 500-mb height
anomalies. J. Climate.

+ ——, and Q. Jiang, 1990: Spatial patterns of atmosphere-

Ocean interaction in the Northern winter. J. Climate, 3, 990-

998.


