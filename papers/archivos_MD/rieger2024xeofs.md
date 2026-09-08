|     |     | xeofs: | Comprehensive | EOF analysis | in Python | with |
| --- | --- | ------ | ------------- | ------------ | --------- | ---- |
xarray
|     |     | Niclas Rieger | 1,2,3 and | Samuel J. Levang4 |     |     |
| --- | --- | ------------- | --------- | ----------------- | --- | --- |
1 Centre de Recerca Matemàtica (CRM), Bellaterra,Spain 2 Departamentde Física, Universitat
Autònomade Barcelona,Bellaterra,Spain 3 Instituto de CienciasdelMar(ICM)-CSIC,Barcelona,
|     |     | Spain4 Salient | Predictions, | Cambridge,MA, USA |     |     |
| --- | --- | -------------- | ------------ | ----------------- | --- | --- |
DOI: 10.21105/joss.06060
Software
Summary
• Review
• Repository
xeofs is a Python package tailored for the climate science community, designed to streamline
• Archive
advanced data analysis using dimensionality reduction techniques like Empirical Orthogonal
Functions(EOF)analysis –often calledPrincipalComponentAnalysis (PCA)inotherdomains.
|     |     |     |     | xarray | xeofs |     |
| --- | --- | --- | --- | ------ | ----- | --- |
Integrating seamlessly with objects (Hoyer & Hamman, 2017), makes it easier
Editor: SamuelForbes
to analyze large, labeled, multi-dimensional datasets. By harnessing Dask’s capabilities (Dask
Reviewers:
Development Team, 2016), it scales computations efficiently across multiple cores or clusters,
• @DamienIrving
|     |     | apt for extensive | climate data | applications. |     |     |
| --- | --- | ----------------- | ------------ | ------------- | --- | --- |
• @malmans2
| Submitted: | 01 November 2023 | Statement | of Need |     |     |     |
| ---------- | ---------------- | --------- | ------- | --- | --- | --- |
| Published: | 02 January 2024  |           |         |     |     |     |
Climate science routinely deals with analyzing large, multi-dimensional datasets, whose com-
License
plexitymirrorstheintricatedynamicsoftheclimatesystemitself. Theextractionofmeaningful
| Authorsof | papers retaincopyright |     |     |     |     |     |
| --------- | ---------------------- | --- | --- | --- | --- | --- |
and release the work undera insights from such vast datasets is challenging and often requires the application of dimen-
CreativeCommons Attribution4.0 sionality reduction techniques like EOF analysis (PCA outside climate science). Packages
| International | License (CC BY 4.0). | scikit-learn |     |     |     |     |
| ------------- | -------------------- | ------------ | --- | --- | --- | --- |
such as (Pedregosa et al., 2011) offer a range of reduction techniques, yet they
often fall short of meeting the specific needs of climate scientists who work with variants of
PCA (Hannachi, 2021) including ROCK-PCA (Bueso et al., 2020) and spectral, rotated PCA
|     |     | (Guilloteau | et al., 2020). |     |     |     |
| --- | --- | ----------- | -------------- | --- | --- | --- |
Climatedatasetsareinherentlymulti-dimensional,usuallyinvolvingtime,longitudeandlatitude,
and often include missing values representing geographical features like oceans or land. These
characteristics require meticulous data transformations and tracking of missing values and
dimension coordinates, which can be cumbersome and prone to error, increasing the workload,
especiallyforsmaller-scaleprojects. Furthermore,thesizeofclimatedatasetsoftennecessitates
|     |     | out-of-memory | processing. |     |     |     |
| --- | --- | ------------- | ----------- | --- | --- | --- |
While xMCA (He, 2019) and eofs (Dawson, 2016) have addressed some of these issues by
offering analysis tools compatible with xarray and Dask, xeofs expands on these by including
a broader range of techniques such as rotated (Kaiser, 1958), complex/Hilbert (Rasmusson
et al., 1981), and extended (Weare & Nasstrom, 1982) PCA/EOF analysis. xeofs operates
natively with xarray objects, preserving data labels and structure, and handles datasets with
missingvaluesadeptly. ItalsointegratesseamlesslywithDaskandshowsimprovedperformance
in particular for larger datasets (Figure 1) due to its usage of randomized Singular Value
|     |     | Decomposition | (SVD) (Halko | et al., 2011). |     |     |
| --- | --- | ------------- | ------------ | -------------- | --- | --- |
Rieger, & Levang. (2024). xeofs: Comprehensive EOF analysis in Python with xarray. Journal of Open Source Software, 9(93), 6060. 1
https://doi.org/10.21105/joss.06060.

Figure 1: (A)Evaluation of xeofs computation times forprocessing 3D data setsof varying sizes. (B)
Performance comparison between xeofs and eofs across different data set dimensions. Dashed black
1
line indicates the contour of datasets approximately 3 MiB in size. Tests conducted on an Intel(R)
Core(TM)i7-8750H CPU @ 2.20GHz,12 threads (6 cores), with 16GB DDR4 RAM at 2667 MT/s.
Implementation
xeofs adopts the familiar scikit-learn style, delivering an intuitive interface where each
methodisaclasswithfit,andwhenapplicable, transformandinverse_transformmethods.
It also offers flexibility by allowing users to introduce custom dimensionality reduction methods
via a streamlined entry point to its internal pipeline. Additionally, the package includes a
| bootstrapping | module          | for straightforward | PCA model     | evaluation. |          |           |             |     |     |
| ------------- | --------------- | ------------------- | ------------- | ----------- | -------- | --------- | ----------- | --- | --- |
| Available     | Methods         |                     |               |             |          |           |             |     |     |
| At the time   | of publication, | xeofs provides      | the following |             | methods: |           |             |     |     |
| Method        |                 | Alternative         | name          |             |          | Reference |             |     |     |
| PCA           |                 | EOF analysis        |               |             |          |           |             |     |     |
| Rotated       | PCA             | -                   |               |             | Kaiser   | (1958),   | Hendrickson |     | &   |
|               |                 |                     |               |             |          | White     | (1964)      |     |     |
Complex PCA Hilbert EOF (HEOF) Rasmusson et al. (1981), Barnett
|          |             | analysis      |          |     |           | (1983), | Horel    | (1984)  |     |
| -------- | ----------- | ------------- | -------- | --- | --------- | ------- | -------- | ------- | --- |
| Complex  | Rotated PCA | -             |          |     |           | (Horel, | 1984)    |         |     |
| Extended | PCA         | EEOF analysis | /        |     | Weare     | &       | Nasstrom | (1982), |     |
|          |             | Multichannel  | Singular |     | Broomhead |         | & King   | (1986)  |     |
|          |             | Spectrum      | Analysis |     |           |         |          |         |     |
(M-SSA)
| Optimal | Persistence | OPA |     |     | DelSole | (2001), | DelSole |     | (2006) |
| ------- | ----------- | --- | --- | --- | ------- | ------- | ------- | --- | ------ |
Analysis
| Geographically-Weighted |     | GWPCA |     |     |     | Harris | et al. | (2011) |     |
| ----------------------- | --- | ----- | --- | --- | --- | ------ | ------ | ------ | --- |
PCA
Maximum Covariance MCA, SVD analysis Bretherton et al. (1992)
Analysis
| Rotated | MCA | -   |     |     | Cheng | &   | Dunkerton | (1995) |     |
| ------- | --- | --- | --- | --- | ----- | --- | --------- | ------ | --- |
1The
script used to generate these results is available at https://github.com/nicrie/xe-
ofs/blob/main/docs/perf/.
Rieger, & Levang. (2024). xeofs: Comprehensive EOF analysis in Python with xarray. Journal of Open Source Software, 9(93), 6060. 2
https://doi.org/10.21105/joss.06060.

| Method      |     | Alternative name       |        | Reference     |
| ----------- | --- | ---------------------- | ------ | ------------- |
| Complex MCA |     | Hilbert MCA/Analytical | Elipot | et al. (2017) |
SVD
| Complex Rotated | MCA         | -   | Rieger     | et al. (2021)         |
| --------------- | ----------- | --- | ---------- | --------------------- |
| Canonical       | Correlation | CCA | Hotelling  | (1936), Vinod (1976), |
| Analysis        |             |     | Bretherton | et al. (1992)         |
Additionally,weareactivelydevelopingfurtherenhancementstoxeofs,withplanstoincorporate
advanced methods such as ROCK-PCA (Bueso et al., 2020) and spectral, rotated PCA
| (Guilloteau | et al., 2020) | in upcoming releases. |     |     |
| ----------- | ------------- | --------------------- | --- | --- |
Acknowledgements
We express our sincere thanks to the individuals who have enhanced our software through their
| valuable issue | reports | and insightful feedback. |     |     |
| -------------- | ------- | ------------------------ | --- | --- |
This work forms part of the Climate Advanced Forecasting of sub-seasonal Extremes (CAFE)
project, undertaken within the Physics doctoral program at the Autonomous University of
Barcelona. NR acknowledges the support of the European Union’s Horizon 2020 research and
innovation program, which has funded this work under the Marie Skłodowska-Curie grant
| (agreement | No 813844). |     |     |     |
| ---------- | ----------- | --- | --- | --- |
References
Barnett, T. P. (1983). Interaction of the Monsoon and Pacific Trade Wind System at
Interannual Time Scales Part I: The Equatorial Zone. Monthly Weather Review, 111(4),
756–773. https://doi.org/10.1175/1520-0493(1983)111%3C0756:IOTMAP%3E2.0.CO;2
Bretherton, C., Smith, C., & Wallace, J. (1992). An intercomparison of methods for finding
coupled patterns in climate data. Journal of Climate, 5(6), 541–560. https://doi.org/10.
1175/1520-0442(1992)005%3C0541:AIOMFF%3E2.0.CO;2
Broomhead, D. S., & King, G. P. (1986). Extracting qualitative dynamics from experimental
data. Physica D: Nonlinear Phenomena, 20(2), 217–236. https://doi.org/10.1016/
0167-2789(86)90031-X
Bueso, D., Piles, M., & Camps-Valls, G. (2020). Nonlinear PCA for Spatio-Temporal Analysis
of Earth Observation Data. IEEE Transactions on Geoscience and Remote Sensing, 1–12.
https://doi.org/10.1109/TGRS.2020.2969813
Cheng, X., & Dunkerton, T. J. (1995). Orthogonal Rotation of Spatial Patterns Derived
from Singular Value Decomposition Analysis. Journal of Climate, 8(11), 2631–2643.
https://doi.org/10.1175/1520-0442(1995)008%3C2631:OROSPD%3E2.0.CO;2
DaskDevelopmentTeam. (2016). Dask: Libraryfordynamictaskscheduling. https://dask.org
Dawson, A. (2016). eofs: A Library for EOF Analysis of Meteorological, Oceanographic, and
| Climate | Data. 4(1), | e14. https://doi.org/10.5334/jors.122 |     |     |
| ------- | ----------- | ------------------------------------- | --- | --- |
DelSole, T. (2001). Optimally Persistent Patterns in Time-Varying Fields. Journal of the
Atmospheric Sciences, 58(11), 1341–1356. https://doi.org/10.1175/1520-0469(2001)
058%3C1341:OPPITV%3E2.0.CO;2
DelSole, T. (2006). Low-Frequency Variations of Surface Temperature in Observations and
Simulations. Journal of Climate, 19(18), 4487–4507. https://doi.org/10.1175/JCLI3879.1
Rieger, & Levang. (2024). xeofs: Comprehensive EOF analysis in Python with xarray. Journal of Open Source Software, 9(93), 6060. 3
https://doi.org/10.21105/joss.06060.

Elipot, S., Frajka-Williams, E., Hughes, C. W., Olhede, S., & Lankhorst, M. (2017). Ob-
served Basin-Scale Response of the North Atlantic Meridional Overturning Circulation to
Wind Stress Forcing. Journal of Climate, 30(6), 2029–2054. https://doi.org/10.1175/
JCLI-D-16-0664.1
Guilloteau, C., Mamalakis, A., Vulis, L., Georgiou, T. T., & Foufoula-Georgiou, E. (2020).
Rotated spectral principal component analysis (rsPCA) for identifying dynamical modes
of variability in climate systems. arXiv:2004.11411 [Physics]. https://doi.org/10.1175/
JCLI-D-20-0266.1
Halko, N., Martinsson, P. G., & Tropp, J. A. (2011). Finding Structure with Randomness:
Probabilistic Algorithms for Constructing Approximate Matrix Decompositions. SIAM
Review, 53(2), 217–288. https://doi.org/10.1137/090771806
Hannachi, A. (2021). Patterns Identification and Data Mining in Weather and Climate.
Springer International Publishing. https://doi.org/10.1007/978-3-030-67073-3
Harris,P.,Brunsdon,C.,&Charlton,M.(2011). Geographicallyweightedprincipalcomponents
analysis. International Journal of Geographical Information Science, 25(10), 1717–1736.
https://doi.org/10.1080/13658816.2011.554838
He, C. (2019). xMCA: Maximum Covariance Analysis in xarray for Climate Science. In GitHub
repository. GitHub. https://github.com/Yefee/xMCA
Hendrickson, A. E., & White, P. O. (1964). Promax: A Quick Method for Rotation to
Oblique Simple Structure. British Journal of Statistical Psychology, 17(1), 65–70. https:
//doi.org/10.1111/j.2044-8317.1964.tb00244.x
Horel, J. (1984). Complex Principal Component Analysis: Theory and Examples. Jour-
nal of Climate and Applied Meteorology, 23(12), 1660–1673. https://doi.org/10.1175/
1520-0450(1984)023%3C1660:CPCATA%3E2.0.CO;2
Hotelling, H. (1936). Relations Between Two Sets of Variates. Biometrika, 28(3), 321–377.
https://doi.org/10.2307/2333955
Hoyer, S., & Hamman, J. (2017). Xarray: N-D labeled arrays and datasets in Python. Journal
of Open Research Software, 5(1). https://doi.org/10.5334/jors.148
Kaiser, H. F. (1958). The varimax criterion for analytic rotation in factor analysis. Psychome-
trika, 23(3), 187–200. https://doi.org/10.1007/BF02289233
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel,
M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau,
D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine Learning in
Python. Journal of Machine Learning Research, 12, 2825–2830.
Rasmusson, E. M., Arkin, P. A., Chen, W.-Y., & Jalickee, J. B. (1981). Biennial variations
in surface temperature over the United States as revealed by singular decomposition.
Monthly Weather Review, 109(3), 587–598. https://doi.org/10.1175/1520-0493(1981)
109%3C0587:BVISTO%3E2.0.CO;2
Rieger, N., Corral, Á., Olmedo, E., & Turiel, A. (2021). Lagged Teleconnections of Climate
VariablesIdentifiedviaComplexRotatedMaximumCovarianceAnalysis. JournalofClimate,
34(24), 9861–9878. https://doi.org/10.1175/JCLI-D-21-0244.1
Vinod, H. D. (1976). Canonical ridge and econometrics of joint production. Journal of
Econometrics, 4(2), 147–166. https://doi.org/10.1016/0304-4076(76)90010-5
Weare, B. C., & Nasstrom, J. S. (1982). Examples of Extended Empirical Orthogonal
Function Analyses. Monthly Weather Review, 110(6), 481–485. https://doi.org/10.1175/
1520-0493(1982)110%3C0481:EOEEOF%3E2.0.CO;2
Rieger, & Levang. (2024). xeofs: Comprehensive EOF analysis in Python with xarray. Journal of Open Source Software, 9(93), 6060. 4
https://doi.org/10.21105/joss.06060.