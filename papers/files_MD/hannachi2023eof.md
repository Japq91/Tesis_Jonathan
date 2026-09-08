Climate Dynamics (2023) 60:1689–1703
https://doi.org/10.1007/s00382-022-06409-8
Common EOFs: a tool for multi‑model comparison and evaluation
Abdel Hannachi1,2 · Kathrin Finke1,2 · Nickolay Trendafilov3
Received: 8 October 2021 / Accepted: 27 June 2022 / Published online: 14 July 2022
© The Author(s) 2022
Abstract
With the increase in the volume of climate model simulations for past, present and future climate, from various institutions
across the globe, there is a need for efficient and robust methods for model comparison and/or evaluation. This manuscript
discusses common empirical orthogonal function analysis with a step-wise algorithm, which can be used for the above
objective. The method looks for simultaneous diagonalisation of several covariance matrices in a step-wise fashion ensuring
thus simultaneous monotonic decrease of the eigenvalues in all groups, and allowing therefore for dimension reduction. The
method is applied to a number of tropospheric and stratospheric fields from the main four reanalysis products, and also to
several historical climate model simulations from CMIP6, the Coupled Model Intercomparison Project (Phase 6). Monthly
means as well as winter daily gridded data are considered over the Northern Hemisphere. The method shows consistency
between mass fields as well as mid-tropospheric and stratospheric fields of the reanalyses, but also reveals significant differ-
ences in the 2 m surface-air temperature in terms of explained variance. CMIP6 models, on the other hand, show differences
reflected in the percentage of explained variance of the leading common EOFs with inter-group variation ranging from 5–10%
in the troposphere to about 25% in the stratosphere. Higher order statistics within the leading common modes of variability,
in addition to further merits of the method are also discussed.
Keywords Common EOF · Model comparison · CMIP6
1 Introduction
Sahara desert. Another equally important database is that
of the CMIP6, the Coupled Model Intercomparison Project
Several reanalysis products are produced by a number (Phase 6), produced by the World Climate Research Pro-
of weather centres across the globe such as the National gramme (WCRP). The objective of CMIP6 is to allow stud-
Center for Environmental Prediction (NCEP; Kalnay et al. ies that can lead to a better understanding of past, present
1996), European Centre for Medium Range Weather Fore- and future climate change resulting from natural or anthro-
casts (ECMWF) with its ERA5 (Hersbach et al. 2020) and pogenic radiative forcing within a multimodel context.1
ERA-Interim (ERAi; Dee et al. 2011), reanalyses, and Japan The existence of such rich gridded databases call for the
Meteorological Agency (JMA) with its Japanese Reanalysis need to have a robust and efficient method to compare the
(JRA55; Kobayashi et al. 2015). These reanalyses constitute reanalyses and/or CMIP6 model simulations and that helps
a valuable database used in countless investigations such as towards model evaluation. In the climate research literature
forecasting/hindcasting experiments, climate analysis, and model evaluation is commonly studied using conventional
downscaling especially in poorly observed areas, e.g. the empirical orthogonal function (EOF) method (Jolliffe 2002;
Hannachi et al. 2007) to compare, e.g. the prominent modes
of variability of different models. These EOFs and asso-
*
Abdel Hannachi ciated principal components (PCs) are model dependent
a.hannachi@misu.su.se
making comparison difficult. In other investigations, such
1 Department of Meteorology, MISU, Stockholm University, as the identification of forced response or climate change
Stockholm, Sweden experiments, the researcher computes the EOFs of the
2 Bolin Centre for Climate Research, Stockholm University, models’ ensemble mean and then proceeds by projecting
Stockholm, Sweden the individual models outputs onto these ‘mean’ EOFs,
3 Department of Human and Social Sciences, University
of Naples “L’Orientale”, Naples, Italy 1 http:// www. wcrp- clima te. org/ wgcm- cmip.
Vol.:(0112 33456789)

1 690 A. Hannachi et al.
(e.g., Venzke et al. (1999)), which do not embed variability makes common EOFs unsuitable for dimension reduction.
across the different members of the ensemble. In addition, Precisely, most available algorithms (e.g. De Lathauwer
the obtained time series resulting from the ‘mean’ EOFs are 2003; Browne and McNicholas 2014a, b) find common
not near uncorrelatedness. EOFs in an arbitrary order by focusing only on simultaneous
An alternative and robust method to address the prob- diagonalisation, and are therefore not suitable for dimension
lem described above is the common EOF method (Flury reduction, which is a major common goal in data analysis,
1984), which is a generalization of PC analysis (Jolliffe particularly for high dimensional problems as in weather
2002; Hannachi 2021) to two or more groups and attempts and climate. This is because the estimated common eigen-
to simultaneously diagonalise several covariance matrices. vectors do not have the same ranking in all groups regard-
Common EOFs provide a natural basis to compare models’ ing the accounted percentage of explained variance (e.g.
time series and their explained variance, and allow intuitive Pepler 2014). We introduce common EOF method using a
model evaluation, following various perspectives, e.g. linear stepwise algorithm that simultaneously decreases the eigen-
and/or nonlinear. Apart from its usefulness in model com- values, and thereby overcoming the above drawbacks, and
parison/evaluation, the common EOF method enjoys another apply it to several reanalysis products and model simula-
advantage, namely the benefit of combining the information tions from CMIP6. Comparison to similar existing methods
from all different groups compared to analysing individual like for example the common basis function approach (Lee
groups separately or using ensemble mean EOFs. Common et al. 2019) or a distinct EOF analysis (Bayr and Dommenget
EOFs can also be applied to one sample, in which the groups 2014; Wang et al. 2015) and using coupled CMIP6 simu-
represent different time periods (e.g., T-mode) allowing for lations goes beyond the scope of the present paper and is
investigation of the relative importance of the source of vari- left for future research. The paper is organized as follows.
ation over time. Sections 2 and 3 describe respectively the methodology
Notwithstanding its potentials, common EOF analysis and data. Application to Reanalyses and 9 models from the
was not given consideration in climate research. Basic meth- AMIP simulations are given in Sect. 4. Section 5 discusses
ods such as those based on pairwise comparison were con- the results, and a summary and conclusion are given in the
sidered in the literature (e.g. Preisendorfer 1988; Bretherton last section.
et al. 1992). Other used methods include the projection onto
the modes of variability of say observations (e.g. reanaly-
ses). To the best of our knowledge only two studies con-
2 Methodology
sidered common EOFs, which go back more than two dec-
ades (Frankignoul et al. 1995; Sengupta and Boyle 1998),
2.1 Motivation
which were based on the original Flury and Gautschi (1986)
(FG86)’s algorithm. These studies, however, were limited
in terms of size and capacity of the method. Frankignoul EOF analysis (Lorenz 1956; Jolliffe 2002; Hannachi 2007,
et al. (1995), for example, compared pairs of thermocline 2021) finds an optimal decomposition of space-time fields
depth field, over the tropical Atlantic, between a given model into orthogonal spatial patterns (EOFs) and uncorrelated
and observations. Sengupta and Boyle (1998), on the other time series or PCs, using efficient algorithms such as the
hand, compared NCEP reanalysis and five ECMWF Atmos- singular value decomposition, SVD, (Golub and van Loan
pheric Model Intercomparison Project (AMIP) simulations 1996). In this context EOF analysis deals with one sample
of 200 hPa monthly velocity potential. Due to limited com- of data, i.e. one data matrix, hence the one sample method.
putational resources, they had to truncate their field using Given a sample of n observations of p-dimensional vari-
spectral resolution of T10 in order to solve the problem. ables, 𝐱 t =(x t1 ,…,x tp )T , t=1,…n , assumed to be anoma-
This is quite similar to using the dominant PCs (instead of lies with respect to some background field, the n×p data
the whole fields) prior to applying common EOFs, and this matrix 𝐗 is given by 𝐗T = 𝐱 1 ,…,𝐱 n , where 𝐱T denotes
𝐱 𝐒
defies the objective of the common EOF method, which is to the transpose of . The sample covariance matrix is then
[ ]
explore original or higher resolution gridded data. estimated by:
The FG86 algorithm has two major drawbacks. Although 1
𝐒= 𝐗T𝐗.
the algorithm seems efficient for low dimension, it becomes n−1 (1)
extremely slow as the dimension of the problem increases.
For example, with 5 groups and 100 variables the com- The diagonalisation of
𝐒
, i.e.
𝐒=𝐄𝚲2𝐄T
, where
putational time of FG86 becomes prohibitively large (e.g. 𝚲2 =diag(𝜆2 1 ,…,𝜆2 p ) , yields the EOFs 𝐄=[𝐞 1 ,...,𝐞 p ] and
Browne and McNicholas 2014a; Pepler 2014). The other associated eigenvalues
𝜆2
1
,…,𝜆2
p .
major drawback is related to the fact that the eigenvalues With more than one covariance matrix the motivation is
in different groups are not simultaneously decreasing. This to find how much do these models share common modes
1 3

Common EOFs: a tool for multi-model comparison and evaluation   1691
N(𝝁 ,𝚺
|     |     |     |     |     |     | assumption                        |     | k k ) , k=1,…m , of m p-variate ran- |     |         |           |      |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | ------------------------------------ | --- | ------- | --------- | ---- |
|     |     |     |     |     |     |                                   |     |                                      | 𝚺   | =𝐁𝚲2 𝐁T |           | 𝚲    |
|     |     |     |     |     |     | dom vectors, with the hypothesis  |     |                                      | k   | k       |  , where  | k ,  |
𝐁
|     |     |     |     |     |     | k=1,…m , are diagonal matrices, and  |     |     |     |  is an orthonormal  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ------------------- | --- | --- |
𝐒 ,…,𝐒
|     |     |     |     |     |     | matrix. Given the sample covariance matrices  |     |     |     |     | 1   | m ,  |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | ---- |
which follow a Wishart distribution (Chatfield and Col-
lins 1980; Anderson 2003), the likelihood function can be
shown to take the form:
m
n
|     |     |     |     |     |     | L(𝚺 ,…,𝚺 | )∝  | 𝚺 −n | ∕2exp tr | − k𝚺− | 1𝐒 , |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---- | -------- | ----- | ---- | --- |
|     |     |     |     |     |     | 1        | m   | k    | k        |       | k k  | (3) |
2
k=1
|     |     |     |     |     |     |        | ∏           |                                          | [   | (   | )]  |     |
| --- | --- | --- | --- | --- | --- | ------ | ----------- | ---------------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | 𝐀      |  and tr(𝐀)  | | |                                      |     |     |     |     |
|     |     |     |     |     |     | where  |             | stan d respectively for the determinant  |     |     |     |     |
𝐀
|     |     |     |     |     |     | and trace of the matrix  |     |  , and n | ,…n | k are positive weights  |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | -------- | --- | ----------------------- | --- | --- |
1
(taken |to |be 1 in most cases). The maximum likelihood was
then used (Flury 1984, 1988) to obtain a basic system of
|     |     |     |     |     |     |                         |        | 𝐁     | 𝚲2  , k=1,…m: |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | ------ | ----- | ------------- | --- | --- | --- |
|     |     |     |     |     |     | equations satisfied by  |        |  and  | k             |     |     |     |
|     |     |     |     |     |     | m                       | 𝜆2 −𝜆2 |       |               |     |     |     |
Fig. 1  Schematic of a simple case illustrating the common EOF  𝐛 n ki kj 𝐛 =0,1≤i<j≤p, and𝐁T𝐁=𝐈 .
|                                                                    |     |     |     |     |     | i    | k     | j   |     |     |     | p   |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- |
| method (center) that combines information of two groups (left and  |     |     |     |     |     |      | 𝜆2 𝜆2 |     |     |     |     |     |
|                                                                    |     |     |     |     |     | (k=1 | ki kj | )   |     |     |     |     |
| right)                                                             |     |     |     |     |     | ∑    |       |     |     |     |     |     |
(4)
In computational terms, Flury and Gautschi (1986, FG86)
of variability. In other words, we seek to identify common
considered the following measure, (Hadamard’s inequality):
EOFs of several groups of datasets. These “common” EOFs
diag(𝐀)
| simultaneously diagonalise the different covariance matri- |     |     |     |     |     | 𝜑(𝐀)= |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
≥1,
|     |     |     |     |     |     |     | 𝐀   |     |     |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ces, and with explained variances that depend on the indi-
| viual matrices. The algorithm presented here is based on  |     |     |     |     |     |     | |   | |   |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as deviation from diagonality, which is valid for positive
| power iteration. It is an efficient stepwise algorithm that can  |     |     |     |     |     |     | | | |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
definite symmetric matrices, see for example Noble and
find a (specified) limited number of common EOFs. The
Daniel (1977), and proposed minimizing the function
n e x t  tw o   s u b s ec t i o n s  i n t r o d u c e  t h e  a l g o r i th m ,  b u t  r e a d e r s   m 𝜑(𝐁T𝐒 𝐁) , that is:
| w h o  a re |   u n f a m il i a r  w | i t h   t e c h n ic a | l  b a c k g r o | u nd   c an   s | k i p  t o   | k=1 | k   |     |     |     |     |     |
| ----------- | ----------------------- | ---------------------- | ---------------- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
m
| the results section. |     |     |     |     |     | ∏           |           |     |        |       |     |     |
| -------------------- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ------ | ----- | --- | --- |
|                      |     |     |     |     |     | {optimal𝐁,𝚲 | ,k=1,…m}= |     | argmin | 𝜑(𝐁T𝐒 | 𝐁). |     |
|                      |     |     |     |     |     |             | k         |     |        |       | k   | (6) |
𝐁
k=1
| 2.2   Common EOF analysis and the FG86 algorithm |     |     |     |     |     |     |     |     |     | ∏   |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The FG86 algorithm is based on a sequence of Jacobi diago-
We now assume we have m groups of data matrices
nalzation and has two levels; an outer level (F-level) and
𝐗 ,…,𝐗
m , with respective sample p×p covariance matri- an inner level (G-level). The F-level constructs a converg-
1
𝐒 ,…,𝐒
ces  1 m . In application, interpolation may be used  ing sequence of orthogonal matrices by minimizing Eq. (6)
to yield same resolution of the data sets (see Sect. 3). The  whereas the G-level solves iteratively Eq. (4). Whereas the
common EOF analysis looks for simultaneous (approximate)  algorithm was shown to converge, it gets very slow with
diagonalisation of those matrices, i.e. increasing dimension. Another main criticism of FG86 is
that the method focuses on simultaneous covariance matri-
| 𝐒 ≈𝐁𝚲2𝐁T, | k=1,…m, |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k k (2) ces diagonalisation, but is not connected to dimensionality
𝐁= 𝐛 ,…,𝐛 reduction (e.g. Schott 1988; Trendafilov 2010), a main goal
| where  |     | p is the common p×p orthonormal  |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 of climate data analysis. This is because there is no guar-
|         | 𝐒 ,k=1,… | m ,  | 𝚲2 =diag(𝜆2 | ,…,𝜆2 | ) ,  |     |     |     |     |     |     |     |
| ------- | -------- | ---- | ----------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
| matrix  | of  k    | and  | k           | k1    | kp   |     |     |     |     |     |     |     |
[ ] antee the obtained eigenvalues are simultaneously ordered
k=1,…m , are p×p positive diagonal matrices. A simple
in all groups. This is important when comparing common
interpretation of common EOFs is sketched in Fig. 1. The
EOFs’ time series, or investigating, e.g. the dynamics, e.g.
two samples are shown by filled ellipses along with their
probability density functions (PDFs) or flow regimes (Han-
individual EOFs. The common EOFs provide directions that
nachi et al. 2017).
approximately diagonalise the respective covariance matri-
ces (Fig. 1).
In the original problem, Flury (1984, 1988) formulated
the problem of common PC analysis based on normality
1 3

| 1 692                    |     |     |     |          |     |     | A. Hannachi et al. |     |
| ------------------------ | --- | --- | --- | -------- | --- | --- | ------------------ | --- |
| 2.3   Stepwise algorithm |     |     |     | 3   Data |     |     |                    |     |
To overcome the above weaknesses we propose to use here  The data considered in this paper consist of two sets. The
the stepwise algorithm (Trendafilov 2010; Hannachi et al.  first set is composed of reanalyses from four sources,
2006). The original formulation of common EOFs is based  namely the ERA5 and ERAi reanalyses, both produced by
on a matrix optimization problem, e.g. the likelihood Eq.  the ECMWF, the JRA55 reanalysis from the Japan Mete-
(3) (Flury 1984). This can be reformulated and cast into  orological Agency (JMA) and the NCEP/NCAR reanaly-
the following minimization problem: sis from the National Center for Environmental Predic-
tion (NCEP). The data have been produced at different
m
|     |     | 𝐁T𝐒 𝐁 | 𝐁T𝐁=𝐈 |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- | --- | --- |
argmin n log diag , s.t. . (7) resolutions in time and space, namely hourly at T639 with
|     | k   | k   | p   |                                                        |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
| 𝐁   | k=1 |     |     | 137 levels up to 0.01 hPa for ERA5, 6-hourly at TL255  |     |     |     |     |
∑
( )
| | resolution with 60 levels up to 0.1 hPa for ERAi, 3-hourly
If the eigenvalues are to decrease monotonically simultane-
at TL319 with 60 levels up to 0.1 hPa for JRA55, and
ously in all groups the above matrix minimization problem is
6-hourly at T62 with 28 levels up to 3 hPa for NCEP/
to be transformed into a vectorized form (Trendafilov 2010),
|                      |     |     |     | N C A R .   | M o n t h l y  m e | a n   a n d  d a i ly |   w i n t e r   (D e c | e m b e r -J a n - |
| -------------------- | --- | --- | --- | ----------- | ------------------ | --------------------- | ---------------------- | ------------------ |
| and the j’th vector  | 𝐛   |     |     |             |                    |                       |                        |                    |
j is then obtained by:
|     |     |     |     | ua ry - F e | b ru a r y ,   D JF ) |   d a t a  a re   c o | n s i d e r e d  f o r  | t he   p e ri o d   |
| --- | --- | --- | --- | ----------- | --------------------- | --------------------- | ----------------------- | ------------------- |
max m n log 𝐛T𝐒 𝐛 1979–2018. The analysed fields include 2 m surface-air
|     | k   | k   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝐛   | k=1 |     |     |     |     |     |     |     |
𝐛T𝐛=1, and𝐛TB =𝟎T (8) temperature (T2m), sea level pressure (SLP), 500 hPa
| s.t. | �   | �   |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
∑ j−1 (Z500) and 10 hPa (Z10) geopotential heights. The second
B =[𝐛 ,…𝐛 ] and  B =𝟎 set is composed of CMIP6 data. SLP, Z500 and Z10 (T2m
| where  | j−1 1 | j−1 | 0  . The procedure  |     |     |     |     |     |
| ------ | ----- | --- | ------------------- | --- | --- | --- | --- | --- |
is not provided) from 9 general circulation models (GCMs)
(Trendafilov 2010) is similar to the stepwise method applied
from different modelling centres have been selected for the
to simplified EOFs (Hannachi et al. 2006), and is based on
analysis. Table 1 provides a list of these models i’th more
projecting the gradient of the objective function, Eq. (8),
details. All simulations are taken from the historical AMIP
onto the orthogonal of the space spanned by the common
m experiment, which is an atmosphere only climate simula-
| EOFs identified in the previous step. Noting n= |     |     | n k ,  |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
k=1
tion that is initialised by historical sea surface temperature
the optimality conditions of Eq. (8) yields the following set
∑ and sea ice concentration data (Eyring et al. 2016). The
of equations:
data are first restricted to the northern hemisphere and
then bilinearily interpolated to a 1.25◦×1.25◦
| m n | 𝐒    |       |     |     |     |     |     |  latitude- |
| --- | ---- | ----- | --- | --- | --- | --- | --- | ---------- |
| k   | k −𝐈 | 𝐛 =𝟎, |     |     |     |     |     |            |
n 𝐛T𝐒 𝐛 p 1 (9) longitude grid as a requirement in addition to consistency
| ( k=1 | k 1 | )   |     |                                                         |     |     |     |     |
| ----- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
| ∑     | 1   |     |     | and easy comparison. The data are then further reduced  |     |     |     |     |
by considering every other grid point, i.e. 2.5◦×2.5◦
|     |     | 𝐛   |     |     |     |     |     |  north  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- |
f o r  t h e fi r s t le a d in g  m o de  1 , and for subsequent modes, i.e.  of 20◦N , and no area weighting was applied. Anomalies
| f o r   j = 2 | , … p  ,  w e  g | et : |     |     |     |     |     |     |
| ------------- | ---------------- | ---- | --- | --- | --- | --- | --- | --- |
with respect to the monthly and daily seasonal cycle are
|      |     | m n 𝐒 |          | obtained for monthly and DJF daily data respectively. |     |     |     |     |
| ---- | --- | ----- | -------- | ----------------------------------------------------- | --- | --- | --- | --- |
| 𝐈 −B | BT  | k k   | −𝐈 𝐛 =𝟎. |                                                       |     |     |     |     |
(10)
| p                     | j−1 j−1 | n 𝐛T𝐒 𝐛                           | p j |             |     |     |     |     |
| --------------------- | ------- | --------------------------------- | --- | ----------- | --- | --- | --- | --- |
| [                     | ( k=1   | j k j)                            | ]   |             |     |     |     |     |
| (                     | ) ∑     |                                   |     |             |     |     |     |     |
|                       |         | B =𝟎                              |     |             |     |     |     |     |
| Keeping in mind that  |         | 0  , the above two equations can  |     | 4   Results |     |     |     |     |
simply be written in one single compact form as:
|      |     | m n 𝐒 |          | 4.1   Application to reanalysis data |     |     |     |     |
| ---- | --- | ----- | -------- | ------------------------------------ | --- | --- | --- | --- |
| 𝐈 −B | BT  | k k   | −𝐈 𝐛 =𝟎, |                                      |     |     |     |     |
(11)
| p   | j−1 j−1 | n 𝐛T𝐒 𝐛 | p j |     |     |     |     |     |
| --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
| [   | ( k=1   | j k j)  | ]   |     |     |     |     |     |
( ) ∑ Common EOFs of the 4 covariance matrices of the Reanal-
for j=1,…p . These equations are then solved using a  yses are determined. Figure 2 shows the leading two com-
mon EOFs of monthly mean T2m reanalyses. The leading
standard power method (Golub and van Loan 1996).
common EOF shows mostly a monopole pattern character-
ised by large loadings over the Arctic, and small loadings
over Europe and US. The second common EOF shows
a dipole with centres located respectively over Northern
Russia, stretching to Scandinavia and eastern Canada/
Greenland. The associated percentage of explained vari-
ance shows an inter-group variation of 5 and 3% for the
1 3

Common EOFs: a tool for multi-model comparison and evaluation 1693
Fig. 2 Leading two common EOFs, EOF1 (left) and EOF2 (right), of monthly T2m anomalies from the four reanalyses ERA5, ERAi, JRA55
and NCEP
extracts the eigenvalues, which decrease simultaneously
monotonically in all groups. Interestingly, the resulted
ranking of explained variance for common EOF1 across
the reanalyses follows the models’ resolution. Low-ranked
eigenvalues of the reanalyses (Fig. 3) tend to be barely
distinguishable. High-order statistics can also be evaluated
within the low-dimensional space spanned by the leading
common EOFs. The skewness, indicating the distribu-
tions’ asymmetry around the mean value, varies between
0.2 (ERA5) to 0.6 (JRA55 and NCEP) and the excess kur-
tosis, providing information about distribution peakedness
and outliers, is of the order 1.5 (see Table 2). For a sample
size n, the variance of the sample skewness and kurto-
sis are given by 𝜎2 =6n(n−1)∕((n−2)(n+1)(n+3))
skew
and
𝜎2 =4𝜎2 (n2−1)∕((n−3)(n+5))
, which can be
kurt skew
approximated by 6/n and 24/n, respectively, for large n
(e.g. Crawley 2015). For monthly data ( n=480 ), the
skewness of common EOF1 time series of ERAi, JRA55
and NCEP T2m are significant at more than 1% level, and
at 5%w for ERA5, the excess kurtosis is positive (lepto-
kurtic) and significant, reflecting peakedness of the prob-
ability distribution.
Fig. 3 Percentage of explained variance of the first 15 common
For the DJF daily T2m data the percentage of explained
modes of variability of monthly T2m from the analysis with the four
variance of common EOF1 has an inter-group variation of
reanalysis products ERA5, ERAi, JRA55 and NCEP
5% and are all separated (Table 2). Figure 4 (top) shows
the leading two common EOFs. Common EOF1 reflects a
first and second common EOFs respectively (Table 2). This dipole with centres located over the Arctic and Siberia. The
can also be seen in the scree plot for the four reanalysis associated time series show a slight decreasing trend dur-
datasets in Fig. 3. The error bar
𝜆2±𝛿𝜆2
, estimated using ing the second half of the record. Common EOF2 shows
the standard error due to sampling 𝛿𝜆2 =𝜆2 2∕n (e.g., an elongated centre over the Arctic, Greenland and Alaska,
(North et al. 1982)), are reported in Table 2. Overall, the and two opposite centres sitting respectively over Canada
√
leading eigenvalue is well separated from the rest of the and Eurasia, plus another small centre over East Asia. These
spectrum. As the figure shows, the algorithm successfully centres of action occur mostly over northern land masses,
1 3

1 694 A. Hannachi et al.
Fig. 4 Leading two common
modes of variability, EOF1 (top
leftl) and EOF2 (top right) and
a quantile-quantile plot of com-
mon EOF1 time series (bottom
panel) of winter daily T2m from
the four reanalyses
which control the T2m. The skewness becomes more promi- eigenvalues and associated time series are quite comparable.
nent compared to monthly data, particularly for the leading The leading common EOF of SLP anomalies, for example,
mode for all reanalyses (see Table 2). The excess kurtosis reflects the standard Arctic Oscillation, AO (Thompson and
associated with common EOF1 is positive and significant, Wallace 1998). The AO pattern becomes more prominent
but non-significant (i.e. mesokurtic) for common EOF2. The with Z500 anomalies, and with Z10 anomalies one gets the
leptokurtic distributions have fatter tails than the Gaussian conventional AO with one single (nearly) zonally symmet-
and yield greater probability of extremes. These results are ric centre over the polar region representing the variability
summarized by a quantile-quantile (QQ) plot shown in Fig. 4 of the stratospheric polar vortex. The second mode of Z10
(bottom) for the 4 reanalysis products. The negative skew- shows a dipole sitting over Scandinavia and Western Can-
ness is reflected by the deviation of the left side of the curves ada/Alaska (e.g. Iqbal et al. 2019). The two leading patterns
below the diagonal line. Note that the deviation below the of Z10 explain respectively around 68 and 13% of monthly
diagonal line of the right side of the curves indicates thinner variability, and are significantly skewed and strongly lep-
(right) tail than the normal distribution (see, e.g. Hannachi tokurtic, favouring thus a weaker polar vortex and vortex
et al. 2003). displacement over western Canada/Alaska relating to sudden
For the SLP, Z500 and Z10 anomalies, the difference stratospheric warming (SSW). On winter daily time scales
between the four reanalysis products is minimal for both the two leading patterns explain about 56 and 17% respec-
monthly and winter daily time scales (not shown). The tively. They are also significantly skewed, and the four time
1 3

Common EOFs: a tool for multi-model comparison and evaluation 1695
represents the AO, and common EOF2 has a main centre
located over the North Pacific, with an inter-group variation
of percentage of explained variance of 10%. Only MPI and
Had show significant skewness of the time series of common
EOF1. All models, however, show positive excess kurtosis.
The results from the common EOF analysis based on ensem-
ble members are similar to those of the ensemble mean in
various aspects. Only two models (ACCESS and MPI) show
significant skewness of common EOF1 time series.
For Z500 the largest difference in the percentage of
explained variance is also obtained with common EOF1
(Fig. 5), with an inter-group variation of 7%. Except for few
exceptions it is interesting that there is a tendency for higher
resolved models to explain more variance in the first mode.
Figure 6 shows the leading two common EOFs of monthly
Z500 anomalies. Common EOF1 describes also the AO pat-
tern with a weakened North Atlantic centre, which is shifted
over western Europe whereas common EOF2 projects onto
Fig. 5 Percentage of explained variance of the leading 15 common the Pacific North America (PNA) pattern (Wallace and Gut-
EOFs of monthly Z500 anomalies from the CMIP6 models zler 1981). The two leading modes show significant skew-
ness only with ESM and MIR. The excess kurtosis of the
series associated with the leading pattern are mesokurtic, leading common mode is largely positive for all models.
and significant negative excess kurtosis is observed with the For stratospheric monthly time scales, the inter-group var-
second pattern. iation of the percentage of explained variance of Z10 com-
mon EOF1 has increased significantly reaching 15%. Com-
4.2 Application to CMIP6 data
mon EOF1 shows a anomaly center over the polar region
whereas common EOF2 displays a dipole over Eurasia and
All but two models (GFDL, INM) have more than one Canada (not shown). For the ensemble members the inter-
ensemble member. We have investigated both the ensemble group variation of explained variance for common EOF1
mean and ensemble members by (randomly) choosing one varies within a range of about 20%, with the largest value
ensemble member from each of the 7 models. Note that the (about 71%) obtained with ESM, and the smallest (around
Z500 of Had and ACCESS are not defined in many locations 52%) with GFDL. The skewness is not uniform across the
as the pressure surface crosses high mountains. models. For the ensemble mean all models show significant
For monthly SLP anomalies of the ensemble mean, the positive skewness of common EOF1, and the models’ dis-
percentage of explained variance associated with the lead- tributions are again significantly leptokurtic. Note also that
ing common EOF, has an inter-group variation of about for the leading common pattern of the ensemble members,
10%, with the largest value obtained with MPI (44%) and skewness is significantly positive for all models except MPI,
the smallest with MIR (35%). Common EOF1 (not shown)
Table 1 CMIP6 models that have been used in this study including their origin, horizontal (lon × lat) and vertical [number of levels (nlev) reso-
lution and their top level (top)], the time period of the historical AMIP simulation and corresponding ensemble members (EM)
Model Institution Resolution lon × lat/nlev/top Period EM
ACCESS-CM2 (ACCESS) (Dix et al. 2019) CSIRO-ARCCSS 192 × 144/85/85 km 1979–2014 3
CanESM5 (ESM) (Swart et al. 2019) CCCma 128 × 64/49/1 hPa 1950–2014 5
CESM2-WACCM (CES) (Danabasoglu 2019) NCAR 288 × 192/70/ 4.5×10−6 hPa 1950–2015 3
EC-Earth3 (ECE) ((EC-Earth) 2019) EC-Earth-Consortium 512 × 256/91/0.01 hPa 1979–2017 3
GFDL-CM4 (GFDL) (Huan et al. 2018) NOAA-GFDL 360 × 180/33/1 hPa 1979–2014 1
HadGEM3_GC31_LL (Had) (Ridley et al. 2019) MOHC 192 × 144/85/85 km 1979–2014 5
INM-CM5-0 (INM) (Volodin et al. 2019) INM 180 × 120/73/𝜎 = 0.0002 1979–2014 1
MIROC6 (MIR) (Tatebe and Watanabe 2018) MIROC 256 × 128/81/0.004 hPa 1979–2014 5
MPI-ESM1-2-HR (MPI) (Jungclaus et al. 2019) MPI-M 384 × 192/95/0.01 hPa 1979–2014 3
1 3

1 696 A. Hannachi et al.
Fig. 6 Leading two common EOFs, EOF1 (left) and EOF2 (right), of monthly Z500 anomalies of the CMIP6 models
which yields a stronger polar vortex compared to the other particular, the positive skewness, as seen in the ensemble
models. mean, reflects excursions towards a weaker polar vortex
For tropospheric DJF daily data, SLP and Z500 common exemplified by SSW also reflected by the negative excess
EOF1 project onto the AO. Z500 common EOF2 projects kurtosis (e.g. Christiansen 2009). Note also that the signifi-
onto the PNA, and for SLP it shows a tripole with centres cant skewness of common EOF2 (Fig. 8) in some models
located respectively over western Canada/Aleutian, Scan- (e.g. ACCESS, ESM, Had) means preference for vortex
dinavia/Russia and the Mediterranean (not shown). Table 3 displacement over Canada (e.g Hannachi et al. 2011). Fig-
shows the percentage of explained variance of the leading ure 9 shows scatter plots of the time series of the leading
two common EOFs along with their skewness and kurtosis two common modes of variability of Z10 anomalies. These
based on an ensemble member of each model for SLP and scatter plots largely show the strong non-Gaussian character
Z500 anomalies. For example, whereas monthly fields show
largely leptokurtic structure (peaked distribution), the daily
data shifts to more platykurtic structure. Notice the signifi-
cant skewness of Z500, and the negative excess kurtosis for
most models. Negative excess kurtosis, in particular, may
provide support for nonlinear regime behaviour (Sura and
Hannachi 2015; Hannachi 2010).
In the winter stratosphere, the difference across daily
data is more prominent in terms of both the percentage of
explained variance and the significance of high order statis-
tics. Table 4 is like Table 3, but for Z10 anomalies, for both
ensemble mean and ensemble members. Figure 7 shows a
scree plot of Z10 anomalies based on ensemble members.
The range of inter-group variation of explained variance of
common EOF1 is about 20% for the ensemble mean and
25% for the ensemble member analysis. Figure 8 shows
the obtained leading two common EOFs of Z10 anomalies
showing respectively a positive AO and a dipole located
over Eurasia and North America. Notice, in particular, that
most models show highly significant skewness and nega-
tive excess kurtosis (Table 4). CES, Had, and MPI show
Fig. 7 Scree plot showing the percentage of explained variance of the
particularly large negative excess kurtosis for both the lead-
leading 15 common EOFs of winter daily Z10 anomalies from the
ing two common EOFs, in addition to their skewness. In CMIP6 models
1 3

Common EOFs: a tool for multi-model comparison and evaluation 1697
Fig. 8 Leading two common EOFs, EOF1 (left) and EOF2 (right) of winter daily Z10 anomalies from the CMIP6 models
Fig. 9 Scatter plot of the trajectory of winter daily Z10 anomalies for CES (a), Had (b), and MPI (c) models within the leading two common
EOFs of the CMIP6 models
with particular flatness of the PDF, also associated with the variation of the percentage of explained variance is about 8
nonlinear behaviour of the winter stratospheric polar vortex. and 5% for common EOF1 and EOF2, respectively. These
are larger than those obtained with the CMIP6 models only.
4.3 Case of reanalysis‑CMIP6 data
Only two models show significant skewness (ESM, MIR)
of the leading common mode of variability, and all models
Lastly, we have also compared the reanalysis and CMIP6 are highly and coherently leptokurtic. On winter daily time
data, and we only discuss the case with ERA5 for concise- scales, the range of inter-group variation of the percentage of
ness. On monthly time scales, for example, the application of explained variance of the leading common EOFs goes from
common EOFs to ERA5 and CMIP6 Z500 anomalies yields 10% in the troposphere to about 25% in the stratosphere. In
the AO as the leading common mode of variability, and PNA terms of hogh-order statistics of Z10 anomalies some mod-
as the common EOF2 (not shown). The range of inter-group els show stronger skewness (e.g. Had, ESM, GFDL) and
1 3

| 1 698 |     |     |     |     | A. Hannachi et al. |     |
| ----- | --- | --- | --- | --- | ------------------ | --- |
about 5%, a significant amount, particularly for winter daily
time scales. Differences across the Reanalyses are suggested
to result from the data assimilation scheme and the para-
metrization of the land-surface processes. The leading mode
of DJF daily T2m has a dipole structure over the Arctic and
Siberia. The associated time series exhibit a slight decreas-
ing trend for all four reanalysis fields during the second half
of the record reflecting a slight warming over the Arctic and
cooling over Siberia. Panagiatopoulos et al. (2005) found,
using station-based observations over Siberia, a decreasing
trend of the Siberian high index between late 1970’s and
2000. However, the Siberian high has witnessed fast recov-
ery starting around mid 1990s (Jeong et al. 2011). Also, Li
et al. (2020) showed that Eurasian temperatures in the fall
Fig. 10  Quantile–quantile plot of common EOF1 time series of win-
witnessed significant cooling over the period 2004–2018,
ter daily Z10 anomalies of CMIP6 ensemble means and ERA5
associated with strengthening of the Pacific Decadal Oscil-
lation and Siberian high.
excess kurtosis (e.g., ACCESS, MIR, MPI) than ERA5. A  The CMIP6 models show varying degrees of differences.
quantile-quantile plot of common EOF1 time series of win- In the troposphere the inter-group percentage of explained
ter daily Z10 anomalies from the ensemble mean CMIP6  variance varies within a range of 5% mostly with the few
models and ERA5 is shown in Fig. 10. The positive skew- leading common modes of variability based on SLP and
ness is now reflected by the deviation of the right side of  Z500 anomalies. The common leading mode reflects the AO
the curves above the diagonal line. Note, in particular, the  whereas the second mode reflects in general a PNA (with
strong skewness of Had and ESM models with large posi- Z500) or a Pacific mode (with SLP). The largest difference
tive extremes. ERA5 has also large skewness but with less  in the percentage of explained variance takes place in the
outliers. stratosphere, with a inter-group variation going from 15%
for monthly time series to about 25% for winter daily data.
The leading common mode of variability shows a clear polar
5   Discussion
center reflecting the variability of the polar vortex whereas
the second mode has a dipole with centres of action located
The application of common EOFs to Reanalyses show great  respectively over Russia/Scandinavia and North America.
degree of coherence of large-scale flow over the period  High-order statistics of the obtained time series have also
1979-2018 as shown from the common EOFs and associated  been analysed. The winter daily T2m from reanalysis shows
PCs of the mass field, mid-tropospheric and stratospheric  large negative skewness, indicating a tendency towards
geopotential heights. The largest (smallest) explained vari- warmer Arctic and colder Siberia (e.g. Li et al. 2020). For
ance of common EOF1 are obtained with NCEP (ERA5).  the CMIP6 models, on monthly time scales, the simulations
Differences, however, are observed in the explained variance  have varying degrees of skewness, with tendency for large
between the Reanalyses in the T2m, for which the inter- amplitude of −AO (MPI, Had), and most models show large
group variation of the percentage of explained variance is  positive excess kurtosis. For Z10 this tends to favour weaker
Table 2  Percentage and error interval of explained variance (%) of the leading two common EOFs of monthly and DJF daily T2m from the rea-
nalyses products along with skewness and kurtosis of the associated time series
| Reanalysis | Monthly data              |            |          | DJF daily data          |             |           |
| ---------- | ------------------------- | ---------- | -------- | ----------------------- | ----------- | --------- |
|            | % variance                | Skew       | Kurtosis | % variance              | Skew        | Kurtosis  |
|            |                           | 0.2/−0.24  |          |                         | −0.6∕−0.17  | 0.5/−0.14 |
| ERA5       | 23/12                     |            | 1.3/1.5  | 14/8                    |             |           |
|            | [21.5, 24.5]/[11.5, 12.5] |            |          | [13.6, 14.3]/[7.8, 8.2] |             |           |
|            |                           | 0.35/−0.27 |          |                         | −0.5∕−0.14  | 0.2/−0.15 |
| ERAi       | 28/11                     |            | 1.3/1.6  | 17/8                    |             |           |
|            | [26.5, 29.5]/[10.5, 11.5] |            |          | [16.6, 17.4]/[7.8, 8.2] |             |           |
|            |                           | 0.6/−0.24  |          |                         | −0.75∕−0.22 | 0.8/−0.12 |
| JRA55      | 26/11                     |            | 1.4/1.4  | 18/8                    |             |           |
|            | [24.5, 27.5]/[10.5, 11.5] |            |          | [17.6, 18.4]/[7.8, 8.2] |             |           |
|            |                           | 0.6/−0.25  |          |                         | −0.35∕−0.14 | 0.3/−0.15 |
| NCEP       | 28/9                      |            | 1.6/1.6  | 19/6                    |             |           |
|            | [26.5, 29.5]/[8.5, 9.5]   |            |          | [18.6, 19.4]/[5.9, 6.1] |             |           |
1 3

Common EOFs: a tool for multi-model comparison and evaluation 1699
combined with skewness is contingent with high probability
of extremes. Negative excess kurtosis may provide support
for nonlinear regimes. This is also the case for daily win-
ter Z10 anomalies. The CES, Had and MPI models stand
out with a particularly robust negative excess kurtosis. A
preliminary investigation of clustering within the leading
two common EOFs using gap statistics (Tibshirani et al.
2001; Hannachi et al. 2011), reveals clustering with a num-
ber of clusters between 2 and 3. Further results, however,
go beyond the scope of this paper and are left for future
research.
Lastly, further merits of the method are worth mention-
ing. For example, an interesting feature of the method is the
structure of the obtained spectra. Figure 11 shows examples
of scree plots of SLP anomalies from the reanalyses obtained
using both common and conventional EOFs. The common
EOF spectra show a clear jump/break or ‘elbow’, where the
values change abruptly from around 40% to about 10%, then
a different rate of decrease afterwards. An elbow in the spec-
tra is quite useful in the analysis. It helps towards physical
Fig. 11 Percentage of explained variance of the leading 15 common
interpretation, and also suggests a guideline for truncation or
EOFs of the reanalyses monthly SLP anomalies, along with the same
percentages obtained using conventional EOF analysis of individual dimension reduction (Hannachi 2007). For example, here the
(reanalyses) SLP anomalies. Notice the large change obtained with analysis suggests that the leading one or two commom EOFs
common EOF analysis compared to those obtained from EOF analy- are the most sensible common modes of variability. Note,
sis
however, that this is less prominent in the conventional EOF
analysis (Fig. 11). This feature carries over to the CMIP6
polar vortex, except for MIR and MPI models, which have models (Fig. 12). Moreover, as the formulation involves a
positive but weak skewness. logarithm (Eq. 8), the method can be applied to fields with
On daily time scales, the outstanding feature is the change different scalings, which are absorbed by the diagonal matri-
of kurtosis for several models. The excess kurtosis of SLP ces (Eq. 2). Common EOFs can also be used in the T-mode,
and Z500 anomalies, are negative for the leading two com- rather like canonical covariance analysis (Bretherton et al.
mon EOFs for several models. Few models show positive 1992; Wallace et al. 1992). This is demonstrated by Fig. 13,
excess kurtosis (CES, GFDL). Positive excess kurtosis showing the leading common PC and associated patterns of
Fig. 12 As in Fig. 11, but for CMIP6 monthly SLP anomalies derived using EOF (a) and common EOF (b) analyses
1 3

1 700 A. Hannachi et al.
Fig. 13 Common EOF analysis
in T-mode applied to ERA5
T2m, SLP, Z500 and Z10
anomalies showing the leading
common PC (top) and the asso-
ciated patterns of T2m (middle
left), SLP (middle right), Z500
(bottom left) and Z10 (bottom
right) anomalies
monthly ERA5 T2m, SLP, Z500 and Z10 anomalies. It is with negative NAO and a weakening of the polar vortex
interesting that the pattern of T2m (Fig. 13) associates, not (associated with SSW), which is concomitant with warm-
with common T2m EOF1 but with common EOF2 (Fig. 2). ing over Canadian Arctic Archipelago and Greenland, and
The T2m pattern is associated more with the North Atlan- cooling over northern Eurasia (Fig. 13).
tic Oscillation, NAO, (Stendel et al. 2016) (Fig. 13, middle
right and bottom left), and with the AO (polar vortex slightly
6 Summary and conclusion
shifted towards Siberia) with a slight dipolar structure with
the weaker centre located over western Canada/North Pacific
(Fig. 13, bottom right). The common PC (Fig. 13, top) has The volume of climate data including Reanalyses and
positive skewness (significant at 15% level) and is highly model simulations is witnessing an unprecedented increase
leptokurtic, i.e. extreme events are associated favourably begging for efficient tools of analyses and evaluation.
1 3

Common EOFs: a tool for multi-model comparison and evaluation   1701
Table 3  As in Table 2, but for
| Reanalysis | DJF SLP anomalies |     |     | DJF Z500 anomalies |     |
| ---------- | ----------------- | --- | --- | ------------------ | --- |
the winter daily CMIP6 SLP
and Z500 anomalies % variance Skew Kurtosis % variance Skew Kurtosis
|        |      | 0.07/−0.02 | 0.15/−0.28 |     |     |
| ------ | ---- | ---------- | ---------- | --- | --- |
| ACCESS | 23/9 |            |            | –   | – – |
0.12/−0.2
| CES | 24/9 | 0.1/0      |             | 21/8 | 0.27/0.19 0.24/0.01 |
| --- | ---- | ---------- | ----------- | ---- | ------------------- |
|     |      | 0.2/−0.01  | 0.03/−0.07  |      | −0.03∕−0.03         |
| ECE | 24/9 |            |             | 21/8 | 0.14/0.26           |
|     |      | 0.04/−0.06 | −0.12∕−0.13 |      | −0.09∕−0.01         |
| ESM | 23/9 |            |             | 20/7 | 0.2/0.2             |
0.51/−0.01 −0.08∕0.17
| GFDL | 25/9 | 0.09/0.05  |            | 21/8 | 0.24/0.16 |
| ---- | ---- | ---------- | ---------- | ---- | --------- |
|      |      | −0.04∕0.13 | −0.16∕0.11 |      |           |
| Had  | 25/9 |            |            | –    | – –       |
0.29/−0.23 0.27/−0.17
| INM | 25/9  | 0.19/0.03  |             | 21/8 | 0.42/0.27   |
| --- | ----- | ---------- | ----------- | ---- | ----------- |
|     |       | 0.17/−0.1  | 0/−0.3      |      | −0.18∕−0.04 |
| MIR | 24/9  |            |             | 23/7 | 0.18/0.06   |
|     |       | 0.25/−0.02 | −0.18∕−0.32 |      | −0.18∕−0.06 |
| MPI | 28/10 |            |             | 24/8 | 0.35/0.17   |
Table 4  As in Table 2, but
| Reanalysis | DJF Z10 (ens. member) |     |     | DJF Z10 (ens. mean) |     |
| ---------- | --------------------- | --- | --- | ------------------- | --- |
for CMIP6 winter daily
Z10 anomalies of ensemble  % variance Skew Kurtosis % variance Skew Kurtosis
members and ensemble mean
ACCESS 55/16 − 0.64/− 0.24 0.15/− 0.18 53/16 0.32/0.29 0.26/0.1
CES 58/15 − 0.56/− 0.12 − 0.46/− 0.31 57/16 0.4/− 0.02 − 0.16/− 0.26
ECE 58/15 − 0.41/− 0.04 − 0.04/− 0.1 59/15 0.43/0.05 0.16/− 0.24
| ESM  | 56/19 | − 0.77/− 0.4 | 0.26/− 0.33 | 60/18 | 0.56/0.43 1.23/0.02 |
| ---- | ----- | ------------ | ----------- | ----- | ------------------- |
| GFDL | 35/22 | − 1.0/0.02   | 2.6/− 0.09  | –     | – –                 |
Had 53/17 − 0.54/− 0.24 − 0.16/− 0.29 59/13 0.78/0.25 1.16/− 0.01
| INM | 59/16 | − 0.73/0.1  | 0/− 0.25    | –     | – –               |
| --- | ----- | ----------- | ----------- | ----- | ----------------- |
| MIR | 47/19 | − 0.63/0.02 | 0.32/− 0.06 | 49/16 | 0.1/0.08 0.5/0.21 |
MPI 56/17 − 0.25/0.04 − 0.26/− 0.53 56/17 0.13/− 0.15 0.3/− 0.26
We presented here common EOF method and applied it  the differences in resolving the upper atmosphere. Large
to Reanalyses and CMIP6 simulations. The approach is  variation is also observed in the high-order statistics also
based on a step-wise algorithm seeking simultaneous diag- mainly in the Z10 field. The T-mode application suggests a
onalisation of multiple covariance matrices. Unlike the  link between a dipolar structure of T2m (opposite polarity
Jacobi diagonalization of FG86, our method uses a fast/ between Greenland/Canadian Archipellago and northern
economic power iteration, which can find a limited number  Eurasia/Siberia), the NAO and the polar vortex.
of eigenelements helping thus towards dimension reduc-
tion. Beside its usefullness in the T-mode application, the  Acknowledgements We acknowledge the modeling groups, the Pro-
gram for Climate Model Diagnosis and Intercomparison (PCMDI)
method can also be applied to fields with different scaling.
and the WCRP’s Working Group on Coupled Modelling (WGCM) for
The application to the data reveals differences in vari-
their roles in making available the WCRP CMIP6 multi-model dataset.
ous aspects, but also agreement in others. Whereas the  Thanks are also due to the European Centre for Medium Weather Fore-
large scale mass field and upper air geopotential height  casting, ECMWF, for providing the ERA5 and ERA interim reanalyses,
the Japan Meteorological Agency for providing JRA55 reanalyses, and
fields are quite consistent between the reanalysis prod-
the National Center for Environmental Prediction for providing NCEP
ucts, the T2m fields do differ following the leading com-
reanalyses. Two anonymous reviewers provided constructive comments
mon EOF pattern. The leading (DJF daily) T2m common  that helped improve the manuscript. The computations were performed
mode of variability shows highly significant skewness  on resources provided by the Swedish National Infrastructure for Com-
for all Reanalyses varying between about −0.8 (JRA55)  puting (SNIC) at the National Supercomputer Centre (NSC). This
research is supported by a faculty-funded PhD program. We declare
and −0.4 (NCEP) concurrent with extreme warm and cold
no conflict of interest.
temperatures over the polar region and Siberia respec-
tively. The CMIP6 models commonly identify the AO as  Funding Open access funding provided by Stockholm University.
the leading mode of variability for the mass and height
fields and the PNA as the second common EOF of Z500.  Data availability Enquiries about data availability should be directed
to the authors.
Unlike the Reanalyses, the AMIP models show large inter-
group variation of the percentage of explained variance
(up to 25%) in the stratosphere. This may be explained by
1 3

1 702 A. Hannachi et al.
Declarations Trenham C, Vohralik P, Watterson I, Williams G, Woodhouse
M, Bodman R, Dias FB, Domingues C, Hannah N, Heerdegen
Conflict of interest The authors declare no conflict of interest. A, Savita A, Wales S, Allen C, Druken K, Evans B, Richards C,
Ridzwan SM, Roberts D, Smillie J, Snow K, Ward M, Yang R
(2019) CSIRO-ARCCSS ACCESS-CM2 model output prepared
Open Access This article is licensed under a Creative Commons Attri-
for CMIP6 CMIP amip. https://d oi.o rg/1 0.2 2033/E SGF/C MIP6.
bution 4.0 International License, which permits use, sharing, adapta-
4239. version = 20191108
tion, distribution and reproduction in any medium or format, as long
(EC-Earth) EEC (2019) EC-Earth-Consortium EC-Earth3 model out-
as you give appropriate credit to the original author(s) and the source,
put prepared for CMIP6 CMIP amip. https://d oi.o rg/1 0.2 2033/
provide a link to the Creative Commons licence, and indicate if changes
ESGF/C MIP6.4 529. version = 20200203
were made. The images or other third party material in this article are
Eyring V, Bony S, Meehl GA, Senior CA, Stevens B, Stouffer RJ,
included in the article's Creative Commons licence, unless indicated
Taylor KE (2016) Overview of the Coupled Model Intercompari-
otherwise in a credit line to the material. If material is not included in
son Project Phase 6 (CMIP6) experimental design and organiza-
the article's Creative Commons licence and your intended use is not
tion. Geosci Model Dev 9(5):1937–1958. https://d oi.o rg/1 0.5 194/
permitted by statutory regulation or exceeds the permitted use, you will
gmd-9-1 937-2 016
need to obtain permission directly from the copyright holder. To view a
Flury BN (1984) Common principal components in k groups. J Am Stat
copy of this licence, visit http://c reati vecom mons.o rg/l icens es/b y/4.0 /.
Assoc 79:892–898. https://d oi.o rg/1 0.2 307/2 28872 1
Flury BN (1988) Common Principal Components and Related Muti-
variate Models. Wiley, New York
Flury BN, Gautschi W (1986) An algorithm for simultaneous orthogo-
References nal transformation of several positive definite symmetric matrices
to nearly diagonal form. SIAM J Sci Stat Comput 7:169–184.
https://d oi.o rg/1 0.1 137/0 90701 3
Anderson TW (2003) An introduction to multivariate statistical analy- Frankignoul C, Février S, Sennéchael N, Verbeek J, Braconnot P
sis, 3rd edn. Whiley Interscience, New York, p 747 (1995) An intercomparison between four tropical ocean models.
Bayr T, Dommenget D (2014) Comparing the spatial structure of Tellus A Dyn Meteorol Oceanogr 47(3):351–364. https://d oi.o rg/
variability in two datasets against each other on the basis of 10.3 402/t ellus a.v 47i3.1 1522
EOF-modes. Clim Dyn 42:1631–1648. https://d oi.o rg/1 0.1 007/ Golub GH, van Loan CF (1996) Matrix computation, 3d edn. The John
s00382-0 13-1 708-x Hopkins University Press, Baltimore
Bretherton CS, Smith C, Wallace JM (1992) An intercomparison of Hannachi A (2007) Pattern hunting in climate: a new method for find-
methods for finding coupled patterns in climate data. J Clim ing trends in gridded climate data. Int J Climatol 27(1):1–15.
5:541–560. https://d oi.o rg/1 0.1 175/1 520-0 442(1992)0 05<0 541: https://d oi.o rg/1 0.1 002/j oc.1 375
AIOMFF >2.0 .C O;2 Hannachi A (2010) On the origin of planetary-scale extra-tropical win-
Browne RP, McNicholas PD (2014a) Estimating common principal ter circulation regimes. J Atmos Sci 67(5):1382–1401. https://d oi.
components in high dimensions. Adv Data Anal Classif 8:217– org/1 0.1 175/2 009JA S3296.1
226. https://d oi.o rg/1 0.1 007/s 11634-0 13-0 139-1 Hannachi A (2021) Pattern identification and data mining in weather
Browne RP, McNicholas PD (2014b) Orthogonal Stiefel manifold opti- and climate. Springer, Berlin, p 600
mization for eigen-decomposed covariance parameter estimation Hannachi A, Stephenson DB, Sperber KR (2003) Probability-based
in mixture models. Stat Comput 24:203–210. https://d oi.o rg/1 0. methods for quantifying nonlinearity in the ENSO. Clim Dyn
1007/s 11222-0 12-9 364-2 20:241–256. https://d oi.o rg/1 0.1 007/s 00382-0 02-0 263-7
Chatfield C, Collins AJ (1980) Introduction to multivariate analysis. Hannachi A, Jolliffe IT, Stephenson DB, Trendafilov N (2006) In
Springer, Berlin, p 249 search of simple structures in climate: simplifying EOFs. Int J
Christiansen B (2009) Is the atmosphere interesting? A projection pur- Climatol 26(1):7–28. https://d oi.o rg/1 0.1 002/j oc.1 243
suit study of the circulation in the northern hemisphere winter. Hannachi A, Jolliffe IT, Stephenson DB (2007) Empirical orthogonal
J Clim 22:1239–1254. https://d oi.o rg/1 0.1 175/2 008JC LI263 3.1 functions and related techniques in atmospheric science: a review.
Crawley MJ (2015) Statistics: an introduction using R, 2nd edn. Wiley, Int J Climatol 27(9):1119–1152. https://d oi.o rg/1 0.1 002/j oc.1 499
New York, p 357 Hannachi A, Mitchell LGD, Charlton-Perez A (2011) On the use of
Danabasoglu G (2019) NCAR CESM2-WACCM model output pre- geometric moments to examine the continuum of sudden strato-
pared for CMIP6 CMIP amip. https://d oi.o rg/1 0.2 2033/E SGF/ spheric warmings. J Atmos Sci 68(3):657–674. https://d oi.o rg/1 0.
CMIP6.1 0041. version = 20190220 1175/2 010JA S3585.1
De Lathauwer L (2003) Simultaneous matrix diagonalization: the Hannachi A, Straus DM, Franzke CLE, Corti S, Woollings T (2017)
overcomplete case. ICA 03. In: Fourth international symposium Low-frequency nonlinearity and regime behavior in the Northern
on independent component analysis and blind signal separation, Hemisphere extratropical atmosphere. Rev Geophys 55(1):199–
Nara, Japan, pp 821–825 234. https://d oi.o rg/1 0.1 002/2 015RG 00050 9
Dee DP, Uppala SM, Simmons AJ, Berrisford P, Poli P, Kobayashi Hersbach H, Bell B, Berrisford P, Hirahara S, Horányi A, Muñoz-
S, Andrae U, Balmaseda MA, Balsamo G, Bauer P, Bechtold P, Sabater J, Nicolas J, Peubey C, Radu R, Schepers D, Simmons A,
Beljaars ACM, van de Berg L, Bidlot J, Bormann N, Delsol C, Soci C, Abdalla S, Abellan X, Balsamo G, Bechtold P, Biavati G,
Dragani R, Fuentes M, Geer AJ, Haimberger L, Healy SB, Hers- Bidlot J, Bonavita M, De Chiara G, Dahlgren P, Dee D, Diaman-
bach H, Hólm EV, Isaksen L, Kållberg P, Köhler M, Matricardi takis M, Dragani R, Flemming J, Forbes R, Fuentes M, Geer A,
M, McNally AP, Monge-Sanz BM, Morcrette JJ, Park BK, Peubey Haimberger L, Healy S, Hogan RJ, Hólm E, Janisková M, Keeley
C, de Rosnay P, Tavolato C, Thépaut JN, Vitart F (2011) The S, Laloyaux P, Lopez P, Lupu C, Radnoti G, de Rosnay P, Rozum
ERA-Interim reanalysis: configuration and performance of the I, Vamborg F, Villaume S, Thépaut JN (2020) The ERA5 global
data assimilation system. Q J R Meteorol Soc 137(656):553–597. reanalysis. Q J Roy Meteorol Soc 146(730):1999–2049. https://
https://d oi.o rg/1 0.1 002/q j.8 28 doi.o rg/1 0.1 002/q j.3 803
Dix M, Bi D, Dobrohotoff P, Fiedler R, Harman I, Law R, Mackallah Huan G, John JG, Blanton C, McHugh C, Nikonov S, Radhakrishnan
C, Marsland S, O’Farrell S, Rashid H, Srbinovsky J, Sullivan A, A, Rand K, Zadeh NT, Balaji V, Durachta J, Dupuis C, Menzel
1 3

Common EOFs: a tool for multi-model comparison and evaluation 1703
R, Robinson T, Underwood S, Vahlenkamp H, Bushuk M, Dunne Ridley J, Menary M, Kuhlbrodt T, Andrews M, Andrews T (2019)
KA, Dussin R, Gauthier PP, Ginoux P, Griffies SM, Hallberg MOHC HadGEM3-GC31-LL model output prepared for CMIP6
R, Harrison M, Hurlin W, Lin P, Malyshev S, Naik V, Paulot F, CMIP amip. https://d oi.o rg/1 0.2 2033/E SGF/C MIP6.5 853. version
Paynter DJ, Ploshay J, Reichl BG, Schwarzkopf DM, Seman CJ, = 20190617
Shao A, Silvers L, Wyman B, Yan X, Zeng Y, Adcroft A, Dunne Schott JR (1988) Common principal component subspaces in two
JP, Held IM, Krasting JP, Horowitz LW, Milly P, Shevliakova E, groups. Biometrika 75(2):229–236
Winton M, Zhao M, Zhang R (2018) NOAA-GFDL GFDL-CM4 Sengupta S, Boyle JS (1998) Using common principal components
model output amip. https://d oi.o rg/1 0.2 2033/E SGF/C MIP6.8 494. for comparing GCM simulations. J Clim 11(5):816–830. https://
version=20180701 doi.o rg/1 0.1 175/1 520-0 442(1998)0 11<0 816:U CPCFC >2.0 .C O;2
Iqbal W, Hannachi A, Hirooka T, Chafik L, Harada Y (2019) Tropo- Sura P, Hannachi A (2015) Perspectives of non-Gaussianity in
sphere–stratosphere dynamical coupling in regard to the North atmospheric synoptic and low-frequency variability. J Clim
Atlantic eddy-driven jet variability. J Meteorol Soc Jpn 97(3):657– 28(13):5091–5114. https://d oi.o rg/1 0.1 175/J CLI-D-1 4-0 0572.1
671. https://d oi.o rg/1 0.2 151/j msj.2 019-0 37 Swart NC, Cole JN, Kharin VV, Lazare M, Scinocca JF, Gillett NP,
Jeong JH, Ou T, Linderholm HW, Kim BM, Kim SJ, Kug JS, Chen D Anstey J, Arora V, Christian JR, Jiao Y, Lee WG, Majaess F, Sae-
(2011) Recent recovery of the Siberian High intensity. J Geophys nko OA, Seiler C, Seinen C, Shao A, Solheim L, von Salzen K,
Res Atmos 116(D23):102. https://d oi.o rg/1 0.1 029/2 011JD 01590 4 Yang D, Winter B, Sigmond M (2019) CCCma CanESM5 model
Jolliffe IT (2002) Principal component analysis, 2nd edn. Springer, output prepared for CMIP6 CMIP amip. https://d oi.o rg/1 0.2 2033/
New York ESGF/C MIP6.3 535. version = 20190429
Jungclaus J, Bittner M, Wieners KH, Wachsmann F, Schupfner M, Stendel M, van den Besselaar E, Hannachi A, Kent E, Lefebvre C,
Legutke S, Giorgetta M, Reick C, Gayler V, Haak H, de Vrese Rosenhagen G, Schenk F, van der Schrier, Woollings T (2016)
P, Raddatz T, Esch M, Mauritsen T, von Storch JS, Behrens J, Recent change—atmosphere. In: Quante Colijn (ed) North Sea
Brovkin V, Claussen M, Crueger T, Fast I, Fiedler S, Hagemann S, Region climate change assessment. Springer, Berlin–Heidelberg,
Hohenegger C, Jahns T, Kloster S, Kinne S, Lasslop G, Kornblueh pp 55–84
L, Marotzke J, Matei D, Meraner K, Mikolajewicz U, Modali K, Tatebe H, Watanabe M (2018) MIROC MIROC6 model output pre-
Müller W, Nabel J, Notz D, Peters K, Pincus R, Pohlmann H, pared for CMIP6 CMIP amip. https://d oi.o rg/1 0.2 2033/E SGF/
Pongratz J, Rast S, Schmidt H, Schnur R, Schulzweida U, Six K, CMIP6.5 422. version = 20191016
Stevens B, Voigt A, Roeckner E (2019) MPI-M MPI-ESM1.2-HR Thompson DWJ, Wallace JM (1998) The Arctic oscillation signature
model output prepared for CMIP6 CMIP amip. https://d oi.o rg/1 0. in the wintertime geopotential height and temperature fields. Geo-
22033/E SGF/C MIP6.6 463. version = 20190710 phys Res Lett 25(9):1297–1300. https://d oi.o rg/1 0.1 029/9 8GL0
Kalnay E, Kanamitsu M, Kistler R, Collins W, Deaven D, Gandin 0950
L, Iredell M, Saha S, White G, Woollen J, Zhu Y, Chelliah M, Tibshirani R, Walther G, Hastie T (2001) Estimating the number of
Ebisuzaki W, Higgins W, Janowiak J, Mo KC, Ropelewski C, clusters in a data set via the gap statistic. J Roy Stat Soc Ser B
Wang J, Leetmaa A, Reynolds R, Jenne R, Joseph D (1996) The (Stat Methodol) 63(2):411–423. https://d oi.o rg/1 0.1 111/1 467-
NCEP/NCAR 40-year reanalysis project. Bull Am Meteorol Soc 9868.0 0293
77(3):437–472. https://d oi.o rg/1 0.1 175/1 520-0 477(1996)0 77< Trendafilov N (2010) Stepwise estimation of common principal com-
0437:T NYRP> 2.0 .C O;2 ponents. Comput Stat Data Anal 54(12):3446–3457. http://o ro.
Kobayashi S, Ota Y, Harada Y, Ebita A, Moriya M, Onada H, Kama- open.a c.u k/4 9279/
hori KOH, Kobayashi C, Endo H, Miyakoi K, Takahashi K (2015) Venzke S, Allen MR, Sutton RT, Rowell DP (1999) The atmospheric
The JRA-55 reanalysis: general specifications and basic charac- response over the North Atlantic to decadal changes in sea surface
teristics. J Meteorol Soc Jpn Ser II 93(1):5–48. https://d oi.o rg/1 0. temperature. J Clim 12:2562–2584
2151/j msj.2 015-0 01 Volodin E, Mortikov E, Gritsun A, Lykossov V, Galin V, Diansky
Lee J, Sperber K, Gleckler P, W BCJ, E TK, (2019) Quantifying the N, Gusev A, Kostrykin S, Iakovlev N, Shestakova A, Emelina
agreement between observed and simulated extratropical modes S (2019) INM INM-CM5-0 model output prepared for CMIP6
of interannual variability. Clim Dyn 52:4057–4089. https://d oi. CMIP amip. https://d oi. org/1 0.2 2033/ ESGF/C MIP6.4 935. ver-
org/1 0.1 007/s 00382-0 18-4 355-4 sion = 20190610
Li B, Li Y, Chen Y, Zhang B, Shi X (2020) Recent fall Eurasian cooling Wallace JM, Gutzler DS (1981) Teleconnections in the geopotential
linked to North Pacific sea surface temperatures and a strengthen- height field during the Northern Hemisphere winter. Mon Weather
ing Siberian high. Nat Commun 11:5202. https://d oi.o rg/1 0.1 038/ Rev 109(4):784–812. https://d oi.o rg/1 0.1 175/1 520-0 493(1981)
s41467-0 20-1 9014-2 109<0 784:T ITGHF >2.0 .C O;2
Lorenz EN (1956) Empirical orthogonal functions and statistical Wallace JM, Smith C, Bretherton CS (1992) Singular value decompo-
weather prediction. Science Report 1, Statistical Forecasting sition of wintertime sea surface temperature and 500-mb height
Project, Department of Meteorology, MIT, p 49 anomalies. J Clim 5(6):561–576. https://d oi.o rg/1 0.1 175/1 520-
Noble B, Daniel JW (1977) Applied linear algebra. Prentice Hall, 0442(1992)0 05<0 561:S VDOWS >2.0 .C O;2
Hoboken, p 477 Wang G, Dommenget D, Frauen C (2015) An evaluation of the CMIP3
North GR, Bell T, Cahalan R, Moeng F (1982) Sampling errors in the and CMIP5 simulations in their skill of simulating the spatial
estimation of empirical orthogonal functions. Mon Weather Rev structure of SST variability. Clim Dyn 44:95–114. https://d oi.o rg/
110(7):699–706. https://d oi.o rg/1 0.1 038/s 41467-0 20-1 9014-2 10.1 007/s 00382-0 14-2 154-0
Panagiatopoulos F, Shahgedanova M, Hannachi A, Stepenson DB
(2005) Observed trends and teleconnections of the Siberian high: Publisher's Note Springer Nature remains neutral with regard to
a recently declining center of action. J Clim 18(9):1411–1422. jurisdictional claims in published maps and institutional affiliations.
https://d oi.o rg/1 0.1 175/J CLI33 52.1
Pepler PT (2014) The identification and application of common princi-
pal components. Stellenbosch University, Stellenbosch
Preisendorfer RW (1988) Principal component analysis in meteorology
and oceanography. Elsevier, Amsterdam
1 3