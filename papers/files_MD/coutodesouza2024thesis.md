|          |           | Universidade     | de             | S˜ao Paulo    |               |      |
| -------- | --------- | ---------------- | -------------- | ------------- | ------------- | ---- |
|          | Instituto | de Astronomia,   | Geof´ısica     | e Ciˆencias   | Atmosf´ericas |      |
|          |           | Departamento     | de Ciˆencias   | Atmosf´ericas |               |      |
|          |           | Danilo           | Couto          | de Souza      |               |      |
| Cyclones | in        | the Southwestern |                |               | Atlantic:     | Life |
|          |           | Cycle            | and Energetics |               |               |      |
Sa˜o Paulo
2024

|          |       | Danilo           | Couto de       | Souza         |           |                 |      |              |      |
| -------- | ----- | ---------------- | -------------- | ------------- | --------- | --------------- | ---- | ------------ | ---- |
| Cyclones | in    | the Southwestern |                |               | Atlantic: |                 |      | Life         |      |
|          | Cycle |                  | and Energetics |               |           |                 |      |              |      |
|          |       |                  | Tese           | apresentada   |           | ao Programa     |      | de Meteoro-  |      |
|          |       |                  | logia          | do Instituto  | de        | Astronomia,     |      | Geof´ısica   | e    |
|          |       |                  | Ciˆencias      | Atmosf´ericas |           | da Universidade |      | de           | Sa˜o |
|          |       |                  | Paulo          | como          | requisito | parcial         | para | a obten¸ca˜o |      |
|          |       |                  | do t´ıtulo     | de            | Doutor    | em Ciˆencias.   |      |              |      |
´
|     |     |     | Area        | de Concentra¸ca˜o: |       | Meteorologia |       |     |       |
| --- | --- | --- | ----------- | ------------------ | ----- | ------------ | ----- | --- | ----- |
|     |     |     | Orientador: |                    | Prof. | Dr. Pedro    | Leite | da  | Silva |
Dias
|     |     |     | Coorientador: |     | Prof. | Dr. Ricardo |     | de Camargo |     |
| --- | --- | --- | ------------- | --- | ----- | ----------- | --- | ---------- | --- |
Sa˜o Paulo
2024

To the boundless beauty of nature, which has been my greatest teacher and source of
inspiration.

Acknowledgements
Acknowledgments
First and foremost, I would like to express my deepest gratitude to my family for their
unwavering support and encouragement throughout this journey. To my loving girlfri-
end, Juliana, your patience and understanding have been my rock, and I could not have
| completed | this work | without | you. |
| --------- | --------- | ------- | ---- |
I am immensely grateful to my advisors, Pedro Dias and Ricardo de Camargo, for
their invaluable guidance, insightful feedback, continuous support, and friendship. Your
expertise and dedication have greatly enriched my research experience and have inspired
| me every | day. |     |     |
| -------- | ---- | --- | --- |
I would also like to acknowledge my former advisors, Renato Ramos da Silva, Roberto
Carelli Fontes, and John Beardall, for their foundational support and mentorship during
| the early | stages of | my academic | career. |
| --------- | --------- | ----------- | ------- |
A heartfelt thank you to my great friend Igor Gamella, who often acted as my pro-
gramming mentor and provided invaluable support. Your guidance and assistance have
| been indispensable |     | to my work. |     |
| ------------------ | --- | ----------- | --- |
To my colleagues, Matheus Bonjour, Renan Godoy, Maria Luiza Kovalski, Luis Andres
Rodrigues, Rodrigo Tecchio, Victor Ranieri, and the entire MASTER team, thank you for
your camaraderie and support. Your collaboration and friendship have made this journey
| enjoyable | and rewarding. |     |     |
| --------- | -------------- | --- | --- |
I am also grateful for the technical support provided by Jean Peres, Djalma, Sebasti˜ao,
and Samuca. Your help in resolving technical issues was crucial for the smooth progress
of my research.

Aspecialthanksgoestotheresearchersandprofessorswhoprovidedmewithinvaluable
assistance: Carolina Gramcianinov, Pedro Peixoto, and Felipe Bragan¸ca Alves. Your
advice and guidance have been instrumental in the completion of this work.
IwouldalsoliketoextendmyheartfeltthankstotheentireIAGcommunity: professors,
students,andstaff. YourfriendlinessandsupporthavemadetheIAGanincrediblelearning
environment. Thank you for fostering a welcoming and stimulating atmosphere that has
greatly enriched my academic journey.
I would also like to thank Karate-d¯o for teaching me discipline and hard work, as well
as perseverance and resilience. Additionally, I am grateful to the ocean for also imparting
lessons of perseverance and resilience. These lessons have been invaluable, and I will carry
them with me throughout my life.
Finally, I would like to express my appreciation to Alexandra Elbakyan, Aaron Swartz,
and the entire open-source community. Your contributions to the free and open access to
knowledge have been invaluable to my research and burgeoning academic career.
Esta tese/disserta¸c˜ao foi escrita em LATEX com a classe IAGTESE, para teses e disserta¸c˜oes do IAG.

“一、努力の精神を養うこと”
| “First,    | foster the spirit | of effort”   |
| ---------- | ----------------- | ------------ |
| “Primeiro, | criar o intuito   | do esfor¸co” |
Kanga Sakukawa

Resumo
Os ciclones sa˜o elementos cr´ıticos do sistema clima´tico da Terra, influenciando signi-
ficativamente os padr˜oes meteorolo´gicos e as condi¸c˜oes clim´aticas, enquanto representam
riscos para a vida, propriedade e ecossistemas. Compreender esses sistemas ´e vital para
aprimorar a previsa˜o do tempo, a prepara¸ca˜o para desastres e mitigar seus efeitos adver-
sos, particularmente na Am´erica do Sul, onde afetam os regimes de precipitac¸˜ao, causam
eventos clim´aticos extremos e impactam va´rios setores socioeconˆomicos. Utilizando o Ci-
clo Energ´etico de Lorenz (LEC), este estudo visa determinar os principais mecanismos
dinaˆmicos que impulsionam o desenvolvimento de ciclones ao longo das v´arias fases de
seus ciclos de vida. Os dados de trajeto´ria dos ciclones de 1979 a 2020, provenientes da
reana´lise ERA5 e gerados usando o algoritmo TRACK para identificar ciclones com base
na vorticidade relativa central a 850 hPa, foram utilizados neste estudo. O programa
CycloPhaser foi desenvolvido para categorizar as s´eries temporais de vorticidade em fases
distintas da vida, fornecendo uma climatologia detalhada dos ciclos de vida dos ciclones. O
LEC foi calculado para esses ciclones para analisar suas caracter´ısticas m´edias de energia
durante cada fase de desenvolvimento, utilizando o m´etodo semi-lagrangiano. Ana´lises de
agrupamento, fun¸co˜es ortogonais emp´ıricas e m´etodos estat´ısticos foram utilizados para
analisar e caracterizar os padr˜oes energ´eticos e os mecanismos dinˆamicos desses sistemas.
A ana´lise revela que os sistemas ciclˆonicos exibem va´rias configura¸c˜oes de fases de vida,
com algumas configura¸co˜es incluindo o desenvolvimento de ciclos de vida secunda´rios. As
distribui¸co˜es espaciais mostram que os sistemas frequentemente se intensificam e amadu-
recem perto de suas regio˜es de gˆenese e decaem em uma a´rea mais ampla, proporcionando
novas perspectivas sobre os ”rastros de tempestades”no Atlaˆntico Sul e o desenvolvimento
dos ciclones. Os resultados revelam uma variabilidade significativa nos termos do LEC

entre diferentes sistemas ciclˆonicos, destacando o papel das instabilidades barocl´ınicas e
barotro´picas no desenvolvimento dos ciclones, esse u´ltimo n˜ao completamente explorado
previamente na literatura. Esses processos atingem seu pico durante as fases de intensi-
fica¸ca˜o e madura e continuam na fase de decaimento, reforc¸ando seu papel ao longo do
ciclo de vida do ciclone. Os diagramas de Fase do Espa¸co de Lorenz (Lorenz Phase Space)
fornecem uma nova ferramenta de visualiza¸ca˜o, facilitando a compreensa˜o da energ´etica
ambiental relacionada aos sistemas ciclˆonicos. A ana´lise identificou padr˜oes energ´eticos
distintos para va´rias configura¸c˜oes de ciclos de vida, confirmando a importˆancia das con-
verso˜es barotro´picas e barocl´ınicas e da atividade convectiva. A ocorrˆencia de instabilida-
des barotro´picas e barocl´ınicas foi confirmada atrav´es do crit´erio de Rayleigh-Kuo e pela
ana´lise da Taxa M´axima de Crescimento de Eady (Eady Growth Rate). Os resultados
indicam que a instabilidade barotr´opica ´e mais pronunciada em escalas espaciais menores
e, portanto, na˜o foi totalmente notada pelos estudos cla´ssicos com a metodologia fixa do
LEC.
Palavras-chave: Fases do ciclone, Ciclo Energ´etico de Lorenz, Instabilidade Ba-
rotro´pica, Instabilidade Barocl´ınica, Ciclogˆenese.

Abstract
Cyclones are critical elements of Earth’s climate system, significantly influencing we-
ather patterns and climatic conditions, while posing risks to life, property, and ecosystems.
Understanding these systems is vital for improving weather forecasting, disaster prepared-
ness,andmitigatingtheiradverseeffects,particularlyinSouthAmerica,wheretheyimpact
precipitation regimes, cause extreme weather events, and affect various socio-economic sec-
tors. Utilizing the Lorenz Energy Cycle (LEC), this study aims to determine the main
dynamic mechanisms driving cyclone development throughout the various phases of their
life cycles. Cyclone trajectory data from 1979 to 2020, derived from the ERA5 reanalysis
and generated using the TRACK algorithm to identify cyclones based on 850 hPa relative
vorticity, were used in this study. The CycloPhaser program was developed to categorize
vorticity time series into distinct life phases, providing a detailed climatology of cyclone life
cycles. The LEC was calculated for these cyclones to analyze their average energy charac-
teristics during each development phase, employing the semi-Lagrangian method. Cluster
analysis, empirical orthogonal functions, and statistical methods were used to analyze and
characterize the energy patterns and dynamic mechanisms of these systems. The analysis
reveals that cyclonic systems exhibit various life phase configurations, with some confi-
gurations including the development of secondary life cycles. Spatial distributions show
that systems often intensify and mature near their genesis regions and decay over a broader
area,offeringnewinsightsintostormtracksintheSouthAtlanticandcyclonedevelopment.
The results reveal significant variability in LEC terms across different cyclonic systems,
highlighting the role of baroclinic and barotropic instabilities in cyclone development, the
latter of which has not been fully explored in the literature. These processes peak during
the intensification and mature phases and continue into the decay phase, highlighting their

role throughout the cyclone life cycle. Lorenz Phase Space diagrams provide a new visua-
lization tool, facilitating the understanding of environmental energetics related to cyclonic
systems. The analysis identified distinct energy patterns for various life cycle configura-
tions, confirming the importance of barotropic and baroclinic conversions and convective
activity. The occurrence of barotropic and baroclinic instabilities was confirmed through
the Rayleigh-Kuo criterion and the analysis of the Eady Growth Rate. The results indicate
that barotropic instability is more pronounced on smaller spatial scales and, therefore, was
not fully captured by classical studies using the fixed LEC methodology.
Keywords: Cyclone Phases, Lorenz Energy Cycle, Barotropic Instability, Baroclinic
Instability, Cyclogenesis.

List of Figures
2.1 Air Masses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
2.2 Phase Diagram - Hart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
2.3 Bjerknes Cyclone Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.4 Bjerknes’ and Shapiro-Keyser’s Cyclonic Models . . . . . . . . . . . . . . . 36
2.5 Tropical Cyclone - Cross Section . . . . . . . . . . . . . . . . . . . . . . . . 37
2.6 Phase Diagram - Hart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
2.7 Extratropical Cyclone - Cross Section . . . . . . . . . . . . . . . . . . . . . 41
2.8 Model of development of cyclones types A and B. . . . . . . . . . . . . . . 43
2.9 Comparison - CISK vs. WISHE . . . . . . . . . . . . . . . . . . . . . . . . 46
2.10 Conceptual Model: Instabilities and Types of Cyclones . . . . . . . . . . . 51
2.11 Global Circulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
2.12 Tropical Cyclone as a Carnot Cycle . . . . . . . . . . . . . . . . . . . . . . 54
2.13 Cyclogenesis Regions in the South Atlantic . . . . . . . . . . . . . . . . . . 58
2.14 Extratropical Cyclone Life Cycle . . . . . . . . . . . . . . . . . . . . . . . 65
2.15 Effects of Heating and Cooling on Potential Energy . . . . . . . . . . . . . 68
2.16 Available Potential Energy . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
2.17 Energy Cycle - Lorenz . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
2.18 Energy Cycle - Muench . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
2.19 Energy Cycle - Brennan . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
2.20 Energy Cycle - Michaelides . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
2.21 Eulerian LEC - Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
2.22 LEC - Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
2.23 C - Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
Z

2.24 C - Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
A
2.25 Zonal and Meridional Jets . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
2.26 Meridional Jet With Eddy . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
2.27 LEC - Chains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.1 Flowchart depicting the methodological steps used in this thesis. (A) Re-
trieval of the cyclonic system track database using central relative vorticity
at 850 hPa. (B) Identification of cyclone life phases with CycloPhaser, ca-
tegorizing the vorticity time series into distinct phases. (C) Computation
and analysis of the Lorenz Energy Cycle for the cyclones to investigate
their energetic characteristics. (D) Classification of energy patterns using
the K-means algorithm to determine distinct energy characteristics. (E)
Examination of dynamical mechanisms related to barotropic and baroclinic
instabilities influencing cyclone development. . . . . . . . . . . . . . . . . . 102
3.2 Cyclophaser - Logo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
3.3 Cyclophaser - Methodological Steps . . . . . . . . . . . . . . . . . . . . . . 106
3.4 Residual Stage - Study case . . . . . . . . . . . . . . . . . . . . . . . . . . 109
3.5 Impact of Varying Threshold Values for Intensification Phase . . . . . . . . 111
3.6 Impact of Varying Threshold Values for Decay Phase . . . . . . . . . . . . 111
3.7 Variations in Threshold Values for Mature Phase . . . . . . . . . . . . . . 112
3.8 Impact of Varying Threshold Values for Incipient Phase . . . . . . . . . . . 112
4.1 Cyclogenesis Climatology in the SESA Region . . . . . . . . . . . . . . . . 123
4.2 Life Cycle Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
4.3 Filtered Life Cycle Configurations . . . . . . . . . . . . . . . . . . . . . . . 125
4.4 Cyclone Life Cycles - Representative Examples . . . . . . . . . . . . . . . . 125
4.5 Life cycle configurations by regions and season . . . . . . . . . . . . . . . . 126
4.6 PDF - Metrics for Each Region and Season . . . . . . . . . . . . . . . . . . 127
4.7 PDF - Total Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
4.8 PDF - Total Distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
4.9 PDF - Mean Speed . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
4.10 PDF - Mean Vorticity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
4.11 PDF - Mean Growth Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

4.12 Mature Phase - Center of Mass . . . . . . . . . . . . . . . . . . . . . . . . 136
4.13 Track Density - Incipient Phase . . . . . . . . . . . . . . . . . . . . . . . . 137
4.14 Track Density - Intensification Phase . . . . . . . . . . . . . . . . . . . . . 139
4.15 Track Density - Mature Phase . . . . . . . . . . . . . . . . . . . . . . . . . 141
4.16 Track Density - Decay Phase . . . . . . . . . . . . . . . . . . . . . . . . . . 143
4.17 Track Density - Secondary Development Stages . . . . . . . . . . . . . . . 145
4.18 Track Density - Intensification 2 . . . . . . . . . . . . . . . . . . . . . . . . 147
4.19 Track Density - Mature 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
4.20 Track Density - Decay 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
4.21 Track Density - Residual Phase . . . . . . . . . . . . . . . . . . . . . . . . 151
4.22 Illustrative Representation of Cyclone Life Cycle . . . . . . . . . . . . . . . 154
5.1 Box plots - Complete Lifecycle . . . . . . . . . . . . . . . . . . . . . . . . . 158
5.2 Density Plots - Energy Terms . . . . . . . . . . . . . . . . . . . . . . . . . 159
5.3 Density Plots - Conversion Terms . . . . . . . . . . . . . . . . . . . . . . . 162
5.4 Density Plots - Boundary Terms . . . . . . . . . . . . . . . . . . . . . . . . 164
5.5 Density Plots - Generation Terms . . . . . . . . . . . . . . . . . . . . . . . 165
5.6 Density Plots - Budget Terms . . . . . . . . . . . . . . . . . . . . . . . . . 167
5.7 LEC - Mean Life Cycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
5.8 EOF - Explained Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
5.9 EOF Analysis - Total Lifecycle . . . . . . . . . . . . . . . . . . . . . . . . 171
5.10 Density Plots - Energy Terms . . . . . . . . . . . . . . . . . . . . . . . . . 175
5.11 Density Plots - Energy Terms . . . . . . . . . . . . . . . . . . . . . . . . . 177
5.12 Density Plots - Energy Terms . . . . . . . . . . . . . . . . . . . . . . . . . 180
5.13 Density Plots - Energy Terms . . . . . . . . . . . . . . . . . . . . . . . . . 182
5.14 Density Plots - Energy Terms . . . . . . . . . . . . . . . . . . . . . . . . . 184
5.15 LEC - Mean Life Cycle for Each Phase . . . . . . . . . . . . . . . . . . . . 186
5.16 LEC - Mean Life Cycle for Each Phase . . . . . . . . . . . . . . . . . . . . 190
5.17 EOF - Explained Variance for Each Phase . . . . . . . . . . . . . . . . . . 192
5.18 Reconstructed EOF1 - Phases . . . . . . . . . . . . . . . . . . . . . . . . . 194
5.19 Reconstructed EOF2 - Phases . . . . . . . . . . . . . . . . . . . . . . . . . 195
5.20 Reconstructed EOF3 - Phases . . . . . . . . . . . . . . . . . . . . . . . . . 197

5.21 Reconstructed EOF4 - Phases . . . . . . . . . . . . . . . . . . . . . . . . . 198
6.1 LPS 1 - ”Reg1”Cyclone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
6.2 LPS 2 - ”Reg1”Cyclone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
6.3 Elbow Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
6.4 LPS 1 - Clusters - All Life Cycle Configurations . . . . . . . . . . . . . . . 210
6.5 LPS 2 - Clusters - All Life Cycle Configurations . . . . . . . . . . . . . . . 212
6.6 LPS 1 - Clusters - Seasonality and Spatial Variability . . . . . . . . . . . . 213
6.7 LPS 2 - Clusters - Seasonality and Spatial Variability . . . . . . . . . . . . 214
6.8 Energy Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
6.9 Energy Patterns - Mean Intensity . . . . . . . . . . . . . . . . . . . . . . . 217
6.10 Energy Patterns - Frequency by Region . . . . . . . . . . . . . . . . . . . . 218
6.11 Energy Patterns - Seasonality . . . . . . . . . . . . . . . . . . . . . . . . . 218
6.12 Energy Patterns - Interannual Variability . . . . . . . . . . . . . . . . . . . 219
6.13 Ca and Ck - Vertical Distribution . . . . . . . . . . . . . . . . . . . . . . . 221
6.14 Rayleigh Criterion and EGR . . . . . . . . . . . . . . . . . . . . . . . . . . 222
6.15 LPS for Fixed Framework Systems . . . . . . . . . . . . . . . . . . . . . . 224
6.16 Rayleigh Criterion and EGR - Fixed Framework . . . . . . . . . . . . . . . 225
6.17 Comparative Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
6.18 LPS 1 - Dynamical Processes . . . . . . . . . . . . . . . . . . . . . . . . . 231
6.19 LPS 2 - Dynamical Processes . . . . . . . . . . . . . . . . . . . . . . . . . 232
C.1 Reconstructed EOFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
D.1 Correlation Between LEC Terms . . . . . . . . . . . . . . . . . . . . . . . . 269
E.1 Computational Domain - Reg1 System . . . . . . . . . . . . . . . . . . . . 271
E.2 Energy and Conversion Terms - Reg1 System . . . . . . . . . . . . . . . . 272
F.1 LPS 1 - All Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
F.2 LPS 1 - All Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
G.1 LPS 1 - Cluster 3 - DItMD . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
H.1 LPS 1 - Most Intense Systems . . . . . . . . . . . . . . . . . . . . . . . . . 279

I.1 Tracks - EP1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281

List of Tables
5.1 Summary Statistics of Lorenz Energetics Components . . . . . . . . . . . . 160
5.2 Statistical Analysis Results for Different Phases . . . . . . . . . . . . . . . 173

Contents
1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
1.2 Scientific goals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2. Theoretical Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.1 Cyclones: Categories and Definitions . . . . . . . . . . . . . . . . . . . . . 29
2.1.1 Material Causes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2.1.2 Formal Causes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.1.3 Efficient Causes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
2.1.4 Final Causes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
2.1.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
2.2 Cyclones in South America . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
2.2.1 Climatological aspects . . . . . . . . . . . . . . . . . . . . . . . . . 56
2.2.2 Genesis mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . 57
2.2.3 Subtropical cyclones . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.2.4 Tropical cyclones . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
2.3 Life cycle of extratropical cyclones: objective classification procedures . . . 62
2.4 Atmosphere Energetics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
2.4.1 Lorenz Energy Cycle: Historical Background . . . . . . . . . . . . . 67
2.4.2 Lorenz Energy Cycle: Mathematical expressions and physical inter-
pretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
2.4.3 Lorenz Energy Cycle applied to cyclonic systems . . . . . . . . . . . 92

3. Data & Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.1 Methodological Steps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.2 Databases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.2.1 ERA5 Reanalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.2.2 Cyclone Tracks in the South Atlantic . . . . . . . . . . . . . . . . . 103
3.3 Cyclone’s Life Cycle Detection . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.3.1 Cyclophaser Program Description . . . . . . . . . . . . . . . . . . . 104
3.3.2 Cyclophaser Settings . . . . . . . . . . . . . . . . . . . . . . . . . . 110
3.4 Lorenz Energetics Computation . . . . . . . . . . . . . . . . . . . . . . . . 113
3.5 Analysis methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.5.1 Probability Density Functions . . . . . . . . . . . . . . . . . . . . . 114
3.5.2 Cyclone Track Densities . . . . . . . . . . . . . . . . . . . . . . . . 115
3.5.3 Statistical Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
3.5.4 Empirical Orthogonal Functions . . . . . . . . . . . . . . . . . . . . 116
3.5.5 K-means Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
3.6 Investigation of Dynamical Mechanisms . . . . . . . . . . . . . . . . . . . . 118
3.6.1 Criteria Used . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
3.6.2 Composites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
4. Life Cycle of Cyclones in the Southwestern Atlantic . . . . . . . . . . . . . . . . 121
4.1 Climatology and Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
4.1.1 Climatological Aspects and Life Cycle Configurations . . . . . . . . 122
4.1.2 Mean Cyclone Statistics . . . . . . . . . . . . . . . . . . . . . . . . 124
4.1.3 Life Cycle Phase Statistics . . . . . . . . . . . . . . . . . . . . . . . 129
4.2 Spatial Distribution of Cyclone Life Cycle Phases . . . . . . . . . . . . . . 136
4.2.1 Incipient Phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
4.2.2 Intensification Phase . . . . . . . . . . . . . . . . . . . . . . . . . . 138
4.2.3 Mature Phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
4.2.4 Decay Phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
4.2.5 Secondary Development Phases . . . . . . . . . . . . . . . . . . . . 144
4.2.6 Residual Phase . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
4.3 Summary and Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . 151

5. Southwestern Atlantic Cyclones Energetics Climatology . . . . . . . . . . . . . . 157
5.1 Complete Life Cycle Climatology . . . . . . . . . . . . . . . . . . . . . . . 157
5.1.1 Descriptive Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . 157
5.1.2 Mean Energy Cycle . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
5.1.3 EOFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
5.2 Climatology Across Life Phases . . . . . . . . . . . . . . . . . . . . . . . . 172
5.2.1 Descriptive Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . 172
5.2.2 Mean Energy Cycle . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
5.2.3 EOFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
5.3 Summary and Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . 199
6. Energetic Patterns of Cyclones in the Southwestern Atlantic . . . . . . . . . . . 203
6.1 Lorenz Phase Space and Energy Patterns . . . . . . . . . . . . . . . . . . . 203
6.1.1 Introducing the Lorenz Phase Space . . . . . . . . . . . . . . . . . . 203
6.1.2 Energetic Patterns for All Life Cycle Configurations . . . . . . . . . 206
6.1.3 Energetic Patterns - Seasonality and Spatial Variability . . . . . . . 211
6.1.4 Energy Patterns - Characteristics . . . . . . . . . . . . . . . . . . . 216
6.2 Physical Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
6.2.1 Barotropic and Baroclinic Instability . . . . . . . . . . . . . . . . . 219
6.2.2 Comparing with the Fixed Framework . . . . . . . . . . . . . . . . 223
6.3 Summary and Concluding Remarks . . . . . . . . . . . . . . . . . . . . . . 228
7. Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
7.1 Summary of Main Findings . . . . . . . . . . . . . . . . . . . . . . . . . . 233
7.2 Final Remarks and Recommendations for Future Work . . . . . . . . . . . 234
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
Appendix 261
A. Lanczos Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
A.1 Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
A.2 Related Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263

B. Lorenz Energy Cycle Program Description . . . . . . . . . . . . . . . . . . . . . 265
C. Complete Life Cycle LEC EOFs Reconstructed . . . . . . . . . . . . . . . . . . 267
D. LEC - Terms Correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
E. LEC Results for Reg1 System . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
F. Lorenz Phase Space - All Systems . . . . . . . . . . . . . . . . . . . . . . . . . . 273
G. Lorenz Phase Space 1 - Early Decay . . . . . . . . . . . . . . . . . . . . . . . . 277
H. Lorenz Phase Space - Most Intense Systems . . . . . . . . . . . . . . . . . . . . 279
I. Tracks - Energy Pattern 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281

1
Chapter
Introduction
Cyclones are an important part of the Earth’s climate system. These systems are
characterized by low atmospheric pressure at their center and rotating winds. Cyclones
can be classified into different types, including tropical cyclones, extratropical cyclones,
and subtropical cyclones, each distinguished by their physical characteristics. Cyclones
play a significant role in the redistribution of heat and moisture across the Earth’s sur-
face, impacting weather patterns and climatic conditions. Additionally, cyclones can lead
to severe weather events such as heavy rainfall, strong winds, and storm surges, posing
substantial risks to life, property, and ecosystems. Understanding cyclones is vital for im-
proving weather forecasting, disaster preparedness, and mitigating the adverse effects of
these systems.
1.1 Motivation
Surface cyclones are crucial features for weather and climate in South America and
the Southwestern Atlantic sector. They significantly influence the precipitation regimes
on the continent, impacting both seasonal and annual rainfall patterns (Reboita et al.,
2010, 2018). These cyclones can potentially cause extreme precipitation events, leading
to flooding and landslides that can disrupt communities and infrastructure (de Souza and
da Silva, 2021; de Souza et al., 2024). Furthermore, the occurrence of cyclones is related
to natural hazards along the South American coast due to their extreme winds (de Souza
and da Silva, 2021; Cardoso et al., 2022), which can cause substantial damage to buildings,
power lines, and other structures. High sea waves generated by cyclones (Guimara˜es et al.,
2014; Gramcianinov et al., 2023, e.g.) pose risks to maritime activities and can affect ship-

26
Chapter1.Introduction
ping routes and port operations. The potential for cyclones to cause storm surges (Campos
et al., 2010; Albuquerque et al., 2018; Leal et al., 2023, e.g.) can lead to significant co-
astal flooding, endangering coastal communities and ecosystems, while also contributing
to coastal erosion (Parise et al., 2009, e.g.) that can undermine coastal defenses and in-
frastructure. Overall, the economic costs of cyclones in South America can be substantial,
affecting livelihoods, infrastructure, and economic stability across various sectors. This
reinforces the necessity of a detailed understanding of the mechanisms related to their ge-
nesis and intensification so that this knowledge can be incorporated into numerical models,
ultimately improving forecasts.
1.2 Scientific goals
Given the importance of cyclonic systems for weather and climate in the South Atlantic
sector, it is crucial to ensure accurate and precise forecasts of these systems. Recent
studies have investigated cyclonic systems’ projections for this region, primarily focusing
on climatological trends (Reboita et al., 2018; de Jesus et al., 2022, e.g.). How cyclone
dynamics will change under climate change scenarios, especially in the South Atlantic
region,remainsanopenquestion. However,adeepunderstandingoftheircurrentdynamics
is necessary first. Although recent investigations have advanced the understanding of
cyclone genesis and development in the South Atlantic (Dias Pinto and Rocha, 2011;
Dias Pinto et al., 2013; Gozzo et al., 2014; Reboita et al., 2018; Gramcianinov et al.,
2019, e.g.), most studies focus on case studies, and a climatological view of the dynamic
mechanisms is still lacking. Furthermore, current cyclone climatologies offer only a unified
view of the cyclone life cycle, not allowing for the geographical positioning and dynamical
mechanisms of each phase to be investigated. Given this context, the main goal of the
current thesis is to determine the main dynamical mechanisms related to cyclone
development in each of their development phases. For this, the Lorenz Energy
Cycle will be employed. Secondary scientific goals include:
• Devise a climatology for each cyclone life phase
• Investigate the mean spatial distribution for each development phase
• Create a climatology of the energetics of cyclonic systems in the Southern Atlantic

27
Section1.2.Scientificgoals
and Southeast South America regions
• Define patterns in the energy climatology
• Reveal the main energy fluxes related to cyclonic development in each life cycle phase
Chapter 2 is dedicated to the literature review, discussing cyclone characteristics, pro-
perties, development mechanisms, and their relationship with the atmospheric general cir-
culation. It also includes an overview of methods for analyzing the cyclone life cycle and
the state of the art of cyclone climatology for the South Atlantic region. It finishes with a
thorough review of the Lorenz Energy Cycle methodology, its mathematical formulation,
and a review of studies that employ this method for cyclonic systems. Chapter 3 presents
the databases used in the current research, including the programs for detecting cyclone
life cycles and computing the energy cycle, as well as the analysis procedures employed
in this study. Chapter 4 introduces a new climatology of cyclones in the South Atlantic
region, dissecting cyclones for distinct development phases. Part of the results presented
in this chapter are published in de Souza et al. (2024). Chapter 5 discusses the LEC for
all systems with genesis in the study region, examining both their mean behavior and
each development phase. Chapter 6 presents the Energy Patterns found for these systems
and explores the dynamical mechanisms related to their energy cycle. Finally, Chapter 7
summarizes all results and presents the final remarks and conclusions of this thesis.

28
Chapter1.Introduction

2
Chapter
Theoretical Background
2.1 Cyclones: Categories and Definitions
For an effective analysis and study, a phenomenon must first be accurately defined.
The Glossary of Meteorology by American Meteorological Society (2012) characterizes a
”cyclone”as ”An atmospheric cyclonic circulation, a closed circulation. A cyclone’s direc-
tion of rotation (counterclockwise in the Northern Hemisphere) is opposite to that of an
anticyclone. (...) Because cyclonic circulation and relative low atmospheric pressure usu-
ally coexist, in common practice the terms cyclone and low are used interchangeably. Also,
because cyclones are nearly always accompanied by inclement (often destructive) weather,
they are frequently referred to simply as storms”. This definition categorizes cyclones
into sub-types based on their occurrence location: tropical, extratropical, and subtropical
cyclones (Reboita et al., 2017, e.g.). This classification is based on the premise that, in
different regions of the globe, cyclones are influenced by distinct genesis environments and
dynamic maintenance processes. There are also specific cyclones in high latitudes known
as polar lows, which are characterized by a warm core structure (Emanuel and Rotunno,
1989; Harrold and Browning, 1969, e.g.). These will not be discussed in depth as the fo-
cus of the present study is on the systems generated in the adjacent regions to the South
American coast.
The aforementioned definition, while broad, lacks precise criteria. Thus, subsequent
sections will employ the Aristotelian approach to elucidate physical phenomena (Aristotle
and Aristotle, 1933). Aristotelian causes, foundational to Aristotle’s philosophy, offer a
comprehensive explanation for an object or phenomenon’s existence through four types:
material, formal, efficient, and final causes. The ensuing subsections will detail each cause,

30
Chapter2.TheoreticalBackground
enhancing the understanding of related phenomena. For each cyclone type — extratropical
and tropical — a discussion of the causes will facilitate a direct comparison between the
systems.
It is important to note that the structure and mechanisms underlying the genesis and
development of cyclones have been well-documented since the mid-twentieth century, le-
ading to the inclusion of many historical references. The aim is to highlight distinctions
between cyclone types, a comparison not commonly made in literature. Meteorologists
often specialize as ”tropical meteorologists”or ”mid-latitude meteorologists”, a division re-
flected in educational materials. Some texts focus exclusively on mid-latitude or tropical
dynamics (Chan and Kepert, 2010; Bluestein, 1992, e.g.), while others that address both,
treat them separately (Holton, 1973; Donald Ahrens and Henson, 2015, e.g.). Although
thisseparationiscustomaryandbeneficial, especiallyforeducationalpurposes, viewingcy-
clones as a continuum has become an increasingly recognized approach in the 21st century,
offering novel insights, as explored in the following sections.
2.1.1 Material Causes
Material cause, within the Aristotelian framework, denotes the substance or constitu-
ents that form an object. It encompasses the matter or physical elements constituting an
entity, serving as the foundation for its existence. For instance, wood acts as the material
cause for a table, just as water serves as the material cause for a river. Applied to cyclonic
systems, the materialcause encompasses the air masses forming these systems, particularly
emphasizing their thermal structure. This section elaborates on this concept, showcasing
its relevance in defining and categorizing cyclonic systems.
The concept of an air mass, as introduced by Swedish meteorologist Tor Bergeron
in 1928, describes a large body of air characterized by uniform temperature, moisture,
and other properties, extending over 500 to 5000 km and encompassing the troposphere’s
full height (Stull, 2015). Air masses are classified based on their temperature, moisture
content, stratification, and turbidity levels. Additionally, air masses originate from specific
source regions, areas conducive to their formation. The characteristics of an air mass are
significantly influenced by its source region’s surface conditions, necessitating a flat terrain
and mild winds for its development (Donald Ahrens and Henson, 2015). Heat transfer
between the surface and the air is gradual, requiring the air mass to remain over its source

31
Section2.1.Cyclones: CategoriesandDefinitions
´
region for an extended period to assimilate its properties (Spiridonov and Curi´c, 2021).
Therefore, mid-latitudes, characterized by variable meteorological conditions and strong
winds, are generally unsuitable for air mass formation.
Bergeron’s classification system is the most widely accepted methodology for catego-
rizing air masses. It utilizes letters to denote the moisture content and the origin of air
´
masses (Spiridonov and Curi´c, 2021). The initial letter signifies the air mass’s moisture
source—continental (dry) or maritime (moist)—while the subsequent letter indicates the
geographical origin of the air mass, whether it be tropical (T), polar (P), arctic/antarctic
(A), equatorial (E), or monsoonal (M). Figure 2.1 illustrates the spatial distribution of air
masses according to Bergeron’s scheme. Upon the encounter of two distinct air masses, im-
mediate mixing does not occur, resulting in a temporary discontinuity at their intersection,
´
known as fronts (Spiridonov and Curi´c, 2021; Donald Ahrens and Henson, 2015).
Figure 2.1: Spatial distribution of air masses according to Bergeron’s classification. Credit:
public domain (https://commons.wikimedia.org/w/index.php?curid=12526643).
Therefore, the validity of the traditional cyclone classification—tropical, extratropical,
and subtropical—relies on the premise that different types of cyclones are initiated by
distinct air masses. Specifically, tropical cyclones originate from warm, moist air masses
that span the entire troposphere and form over warm tropical waters (Gray, 1968; Frank,
1977a; Ramage, 1959; Riehl, 1948). In contrast, extratropical cyclones are associated
with frontal zones at mid-latitudes, where two different air masses meet, and are typically
linked to cold cores (Bjerknes and Holmboe, 1944; Shapiro and Keyser, 1990; Hart, 2003).
However, intense marine extratropical cyclones can experience warm seclusion, resulting
in a warm core at the system’s center (Bjerknes and Solberg, 1922; Shapiro and Keyser,
1990; Hart, 2003). Subtropical cyclones feature a hybrid structure between tropical and

| 32  |     | Chapter2.TheoreticalBackground |     |     |
| --- | --- | ------------------------------ | --- | --- |
extratropical systems, with warm, moist cores that are less pronounced and shallower than
| those in tropical | cyclones | (Hart, 2003). |     |     |
| ----------------- | -------- | ------------- | --- | --- |
Hart (2003) offers an objective methodology for identifying the thermal structure of
cyclonic systems. This analysis focuses solely on tropospheric levels (up to 300 hPa) be-
cause cyclones display an opposing thermal signal in the stratosphere. The study examines
layers between 900 and 600 hPa and between 600 and 300 hPa, which have comparable
masses. Levels below 900 hPa are excluded to prevent extrapolation below the ground or
into the boundary layer, which may not accurately represent the cyclone’s structure in the
free atmosphere. Consequently, the variable corresponding to the cyclonic perturbation in
| height is defined | as follows: |        |     |       |
| ----------------- | ----------- | ------ | --- | ----- |
|                   |             | ∆Z = Z | −Z  | (2.1) |
MAX MIN
Where Z and Z represent the maximum and minimum geopotential heights
|     | MAX | MIN |     |     |
| --- | --- | --- | --- | --- |
at a specific isobaric level, measured within a 500 km radius from the cyclone’s center.
| Following this | definition: |     |     |     |
| -------------- | ----------- | --- | --- | --- |
dg|V |
g
|     |     | ∆Z = |     | (2.2) |
| --- | --- | ---- | --- | ----- |
f
Here, d denotes the distance between the geopotential height extremes, g is the accele-
ration due to gravity, f represents the Coriolis parameter, and V is the geostrophic wind
g
speed. Consequently, the cyclone’s vertical structure (indicative of a cold or warm core) is
determined by the vertical gradient of ∆Z, which is proportional to the magnitude of the
scaled thermal wind (V ) for a constant d, applied across two tropospheric layers of equal
T
mass:
(cid:12)300hPa
∂(∆Z)(cid:12)
|     |     | (cid:12) | = −|VU| | (2.3) |
| --- | --- | -------- | ------- | ----- |
(cid:12) T
∂lnp
(cid:12)
600hPa
(cid:12)600hPa
∂(∆Z)(cid:12)
|     |     | (cid:12) | = −|VL| | (2.4) |
| --- | --- | -------- | ------- | ----- |
(cid:12)
∂lnp T
(cid:12)
900hPa
where VU and VL symbolize the thermal winds at upper and lower levels, respectively.
T T
As such, positive values of −V signify a warm core within the respective layer, whereas
T
| negative values | indicate | a cold core. |     |     |
| --------------- | -------- | ------------ | --- | --- |

33
Section2.1.Cyclones: CategoriesandDefinitions
Therelationshipbetweenthetemperatureanddepthofthecorewithincyclonicsystems
is detailed through a phase diagram by Hart (2003), depicted in Figure 2.2. This diagram
utilizes the abscissas to represent the parameter −VL, illustrating the low-level core’s
T
thermal structure. The ordinates display −VU, portraying the high-level core’s thermal
T
structure. Integrating these metrics allows for discerning whether a system possesses a
warm or cold core, and if it is shallow or deep. Figure 2.2 includes typical positions
representative of different cyclonic types within the phase space. As noted by Hart (2003),
a system may shift within this diagram throughout its lifecycle, making the depiction
general for each cyclone category. Additionally, Hart proposes a diagram for the horizontal
structure of these systems, related to their formal causes, which is addressed in Section
2.1.2.
e
r
o
C
m
r Deep warm core
a Shallowcoldcore
W Tropical cyclones
r
e
p
p
U
T
U
V
-
e
r
o
C
d
Deep cold core Shallow warm core
lo
Extratropical cyclones Subtropical cyclones
C
r e Ocluded extratropical cyclones Warm Seclusions
p
p
U
Lower Cold Core Lower Warm Core
-VL
T
Figure2.2: Phasediagramshowingtherelationshipbetweenthecoretemperatureofcyclonic
systems and their classification. Adapted from Hart (2003).
Thus, material causes, tied to the thermal structure of cyclonic systems, offer a founda-
tional method for classifying and differentiating cyclone types. This classification leverages
the phase diagram by Hart (2003) for an objective categorization. Accordingly, extratropi-
cal cyclones are characterized by cold, deep cores, whereas tropical cyclones feature warm,
deep cores. This spectrum isn’t binary; there exists a gradient of thermal structures with
systems exhibiting intermediate features classified as subtropical cyclones. Nevertheless,
relying solely on thermal attributes for classification is insufficient. For instance, extratro-
pical cyclones, through the warm seclusion process (Shapiro and Keyser, 1990, e.g.), can

34
Chapter2.TheoreticalBackground
develop warm, shallow cores (Hart, 2003), indicating the necessity for a broader analysis
incorporating additional Aristotelian causes for a comprehensive classification.
2.1.2 Formal Causes
The formal cause concerns the essence or identity that defines a thing, essentially its
design, structure, or conceptual blueprint that marks it as a particular type. To revisit the
earlier example of a table from Section 2.1.1, its formal cause is the design that qualifies
it as a table rather than a chair. In the context of cyclones, the formal cause refers to the
system’s organizational structure, such as the configuration of convection bands and/or
fronts, along with the low-pressure pattern.
Extratropical cyclones, typically associated with mid-latitudes and frontal structures,
exhibit an average diameter between 1200 and 1800 km. This size fluctuates over their
lifecycle, with the cyclone’s diameter expanding by up to 150% during its intensification
phase (Simmonds, 2000; Rudeva and Gulev, 2007). However, the spatial complexity and
variability of these systems throughout their lifecycle pose methodological challenges for
accurately estimating their dimensions and comparing findings across different studies.
The seminal model describing the formation and horizontal structure of extratropical
cyclones was introduced by Bjerknes (1919), illustrated in Figure 2.3. This model, devised
for the Northern Hemisphere, showcases the cyclone’s movement along a central horizontal
line,withthe”steerline”demarcatingtheboundarythatinfluencesthecyclone’strajectory,
characterized by warm air masses to its left. The ”squall line”indicates a zone of intense
meteorological activity, marked by strong winds and often heavy precipitation, with cold
air masses located to its left. The ”fore runner”represents a region of diverging airflow.
Bjerknes and Solberg (1922) realized that the model proposed in Bjerknes (1919) repre-
sented just one phase in the life cycle of cyclones, indicating that there are several stages
of development. Bjerknes and Solberg (1922) established the Polar Front Theory, which is
the foundation of the so-called Norwegian cyclone model. Schultz et al. (1998) synthesizes
and describes the development of extratropical cyclones according to this theory, so that
a visual representation of the horizontal structure at the surface during different stages of
cyclone evolution is found in Figure 2.4a. In the first stage, the incipient cyclone presents
a narrow and long cold front, and a wide and short warm front (Figure 2.4aI). After this,
the cyclone deepens, with a narrowing of the warm section of the cyclone through the

35
Section2.1.Cyclones: CategoriesandDefinitions
Figure 2.3: Representation of the Bjerknes model for the extratropical cyclone formation
process and its horizontal structure, for the Northern Hemisphere. Cold air regions are
illustrated with blue lines, while warm air regions with red lines. Adapted from Bjerknes
(1919).
rotation of the cold front towards the warm front (Figure 2.4aII). As cold air is denser
and, therefore, facilitates more intense horizontal pressure gradients, it moves faster than
the warm air. As the cold air at the front of the cyclone approaches the cold air at the
rear of the system (Figure 2.4aIII), the warm air is trapped in the center of the system, a
phenomenon called warm seclusion. As the cold front continues to move, the warm air at
the surface is overtaken by the cold air and is forced to ascend to upper levels. This process
is called occlusion, being responsible for trapping the cold air in the core of the system
(Figure 2.4aIV). With the continuation of occlusion, the baroclinicity along the warm front
can become so diffuse that the cyclone appears not to have a well-defined warm front.
Building on advancements enabled bythe satellite era and field campaigns, Shapiro and
Keyser (1990) introduced a revised cyclonic model, acknowledging that not all observed
cyclones conformed to the Norwegian model. Termed the Shapiro-Keyser model, it is
also summarized by Schultz et al. (1998), with its visualization in (Figure 2.4b). Initially
mirroring the development outlined by Bjerknes and Solberg (1922) (Figure 2.4bI), this
model diverges as the cold front extends perpendicularly to the warm front instead of
encircling the system (Figure 2.4bII). As the system strengthens, the polar side of the
cold front weakens, allowing the warm front to encircle the system’s western sector (Figure
2.4bIII). At peak intensity, cold air encases the warm air near the cyclone’s center, creating
a warm seclusion (Figure 2.4bIV).
Schultz et al. (1998) emphasizes that these models are complementary rather than

36
Chapter2.TheoreticalBackground
Figure 2.4: Cyclonic models by Bjerknes (1919) (a) and Shapiro and Keyser (1990) (b),
illustrating the systems’ horizontal structure across different developmental stages (I to IV).
Adapted from Schultz et al. (1998).
mutually exclusive, suggesting that the Norwegian model is more applicable to systems
forming under diffluent flow with significant amplitude, often at the terminal end of storm
tracks and on western continental edges, characterized by a meridional elongation of the
cyclone and its fronts. Conversely, the Shapiro-Keyser model is more suited to systems
emerging under confluent, low amplitude base flow, typically exhibiting east-west elonga-
tion. However,thesemodelsalonedonotfullyaccountfortheformalcausesofextratropical
cyclones, indicating a continuum where different systems may align more closely with one
model or the other (Schultz et al., 1998).
Tropical cyclones, unlike their extratropical counterparts, lack frontal structures and
exhibit organized, symmetric circulation near the surface, forming over warm tropical or
subtropical waters with intense winds below the surface (Frank, 1977a; Gray, 1968). Their
diameters vary, ranging from 100 to 1000 km at maturity, expanding up to 2000 km during
intensification. However, the area of intense convection and stronger winds typically spans
a radius of about 100 km (Holton, 1973).
Characterized by a central cyclonic circulation at lower tropospheric levels and anticy-
clonic circulation in the upper troposphere, tropical cyclones are associated with intense
precipitation and horizontal pressure gradients, leading to spiraled winds near the surface
that become increasingly circular towards the system’s center, or eye (Frank, 1977a,b;
Terry, 2007; Weatherford and Gray, 1988). These systems exhibit more intense pressure

37
Section2.1.Cyclones: CategoriesandDefinitions
gradients—and consequently stronger winds—than extratropical cyclones (Spiridonov and
´
Curi´c, 2021). Based on wind speed, they are classified into tropical depressions (maximum
winds less than 62 km/h), tropical storms (winds between 62 and 117 km/h), and tropical
´
cyclones (winds exceeding 117 km/h) (Spiridonov and Curi´c, 2021). Their nomenclature
varies by region: ”hurricanes”in the North Atlantic and North Pacific, ”typhoons”in the
Northwest Pacific, and ”cyclones”in the Indian Ocean (Donald Ahrens and Henson, 2015).
The structure of tropical cyclones comprises three main components: the eye, the eye
wall, and surrounding convection bands (Figure 2.5). The eye is the calm, warm central
region,witharadiusof5to50km,encircledbytheeyewall—acloudringabout10to20km
wide where intense upward vertical movements occur, facilitating mass transport to higher
levels (Shea and Gray, 1973; Jorgensen et al., 1985). Although these vertical movements
are typically less vigorous than those in extratropical cyclones (Jorgensen et al., 1985),
the inner core, consisting of the eye and eye wall, hosts the most intense winds and lowest
atmospheric pressures (Weatherford and Gray, 1988). The primary convection band, a
nearly stationary feature, spirals inward from the system’s outer edges towards the eye
wall, where it becomes roughly tangent (Willoughby et al., 1984).
Figure 2.5: Cross-sectional view of a mature tropical cyclone in the Southern Hemisphere,
illustrating the eye (A), eye walls (B), and convection bands (C), along with upward (red
arrows) and downward (green arrows) vertical movements, horizontal wind movement (grey
arrows), and sea-level pressure contours. Inspired from: Bluestein (1992).
Giventhedelineatedformalcauses(organizationalstructure)forbothextratropicaland
tropical cyclones, it’s evident that their structures diverge significantly. In simple terms,
extratropical cyclones, forming at the interface between distinct air masses, are associated
with frontal systems, providing them an asymmetric feature. Conversely, tropical cyclones

38
Chapter2.TheoreticalBackground
exhibit symmetry, characterized by a circular eye and spiraled convection bands extending
fromtheeyewall. Addressingthisdistinction,Hart(2003)introducesametricassessingthe
relativethicknessasymmetrybetweenthe900and600hPalevels, termedtheB parameter:
(cid:0) (cid:1)
B = h Z −Z | −Z −Z | (2.5)
600hPa 900hPa R 600hPa 900hPa L
where Z represents the isobaric height, R and L denote the right and left sides relative
to the system’s motion, the overbar signifies an average over a 500 km semicircle, as
defined in Equation 2.1, and h is a constant set to +1 or -1 for the northern and southern
hemispheres, respectively. Mature tropical cyclones exhibit a B value near zero, indicating
thermal symmetry (non-frontal), while extratropical cyclones show significant B values,
signaling thermal asymmetry (frontal). Positive B values suggest the presence of warm
air to the right of the cyclone in the southern hemisphere (and vice versa in the northern
hemisphere), aligning with the thermal wind relationship from quasi-geostrophic theory
(Sutcliffe, 1947; Trenberth, 1978).
Hart (2003) proposed a diagram correlating symmetry with VL (Equation 2.4), depic-
T
ted in Figure 2.6, offering a supplementary classification to that shown in Figure 2.2. Here,
extratropical cyclones are categorized as cold and asymmetric (frontal), whereas tropical
cyclonesarewarmandsymmetric(non-frontal). Liketheearlierdiagram, thisclassification
suggestsacontinuum, withsystemsdisplayingintermediatefeatureslabeledassubtropical.
Unlike solely thermal-based classifications, this model allows for differentiation of extra-
tropical cyclones undergoing occlusion, as these systems begin to exhibit symmetry during
this phase. Hence, the diagram involving the B parameter and VL presents an objective
T
methodology to classify cyclones’ formal causes.
While the phase diagrams by Hart (2003) facilitate objective classification criteria for
cyclonic systems, gaps remain. For instance, warm seclusions share formal and material
causes with hybrid systems, leading to potential misclassification by forecasters and cli-
mate data analysis algorithms using these diagrams exclusively. Additionally, polar lows,
characterized by both a warm core and symmetric structure, were initially likened to hur-
ricanes (Rasmussen, 1989; Emanuel and Rotunno, 1989; Nordeng and Rasmussen, 1992;
Rasmussen, 1985, 1979). However, recent studies, such as Stoll et al. (2021), suggest their
spiral bands and thermal core may result from the warm seclusion process, as per the
Shapiro-Keyser cyclone development model. These discussions underscore that material

39
Section2.1.Cyclones: CategoriesandDefinitions
and formal causes alone do not suffice for a comprehensive cyclone classification, necessi-
tating further analysis.
c
ir
t Asymmetric warm core
e Asymmetric cold core
m Subtropical cyclones
m Extratropical cyclone
y Warm seclusion
s
A
B
c
ir
t e Symmetric cold core Symmetric warm core
m
m Ocluded extratropical cyclone Tropical cyclone
y
S
Cold core Warm core
-VL
T
Figure2.6: Phasediagramillustratingtherelationshipbetweencyclonicsystems’coretempe-
rature and symmetry, offering a distinct classification procedure. Adapted from Hart (2003).
2.1.3 Efficient Causes
The efficient cause represents the agent or process that leads to the creation or transfor-
mation of something, answering the ”how”or ”why”behind an occurrence. It encompasses
the actions or processes that result in the existence of an entity. For example, in the
creation of a table, the carpenter serves as the efficient cause. In the context of cyclones,
the efficient cause includes the physical and dynamic processes responsible for their for-
mation and intensification. These processes essentially act as destabilization mechanisms,
triggering atmospheric disturbances that evolve into a cyclonic configuration.
While the polar front theory offers a descriptive perspective, it falls short of providing
a comprehensive theoretical model for the physical processes involved in system formation.
Still, it related these processes with thermal contrasts in the atmosphere, or baroclinic
zones (Bjerknes, 1919; Bjerknes and Solberg, 1922), describing cyclones as emergent phe-
nomenaarisingattheboundaryoftwodistinctaircurrents—polarandtropical—flowingin
opposite directions (east-west and west-east, respectively), differentiated by thermal con-
trasts (cold and warm, respectively). A destabilization of the flow occurs when the velocity
difference between these currents surpasses a critical threshold, generating a frontal wave

40
Chapter2.TheoreticalBackground
that intertwines the currents and reduces their velocity contrast. Some of these frontal
waves are unstable and can spontaneously amplify, representing the genesis mechanism of
cyclones according to this theory.
The Polar Front Theory provides a detailed account of the structure and formation pro-
cesses of extratropical cyclones, as shown in Figure 2.7, depicting a transverse model of a
developing cyclone (Bjerknes and Solberg, 1922). This model features horizontal isotherms
indicative of temperature variations parallel to the ground, with warm air central to the
model, characteristic of the warm front, and cold air on the edges. Initially (Figure 2.7a),
the isotherms of cold air extend horizontally until convergence forces the ascent of warm
air to higher atmospheric levels. This conversion of potential to kinetic energy continues
as the cold air from both sides of the cyclone advances to mid-atmospheric levels, further
driving the ascent of warm air. A more detailed explanation of this process is given in
Section 2.4.2. The adiabatic cooling of ascending warm air leads to temperature equaliza-
tion and depletion of the system’s potential energy reserve, while the air mass movement is
then sustained by inertia. After occlusion (Figure 2.7b and c), inertia maintains the ascent
of cold air, which cools adiabatically, utilizing the system’s kinetic energy to counteract
gravity. Initially, there is still kinetic energy production at high levels and its consumption
at low levels. However, as the elevated warm sector cools and temperatures equalize (Fi-
gure 2.7d), kinetic energy production halts. Eventually, friction outweighs kinetic energy
production, leading to its dissipation.
Since the advent of the polar front theory, our comprehension of atmospheric dynamics
has evolved significantly, incorporating new concepts into the understanding of extratro-
pical cyclones. This evolution has led to a diverse array of approaches aimed at describing
the dynamic and thermodynamic processes underlying the genesis and development of
these systems. Consequently, there is no singular, unified theory regarding extratropical
cyclogenesis. For instance, Bjerknes and Holmboe (1944) identified the formation regions
of extratropical cyclones as zones of dynamic instability associated with the westward-
flowing jet stream, employing the tendency equation to analyze atmospheric instability.
Other studies have approached cyclogenesis through various lenses, including slantwise
convection, the omega equation, potential vorticity, primitive equations, and diabatic pro-
cesses (Hoskins, 1990, e.g.). Additionally, Schultz et al. (1998)’s work categorizes cyclones
into those aligning with the Norwegian model versus the Shapiro-Keyser model, differenti-

41
Section2.1.Cyclones: CategoriesandDefinitions
A B
C D
Figure 2.7: Cross-sectional depiction of an extratropical cyclone’s development through
its various stages, adapted from Bjerknes and Solberg (1922). Stage A shows horizontal
isothermswherecoldairconverges,leadingtotheascentofwarmair. InStageB,thesystem
beginsocclusionascoldairadvancestomid-atmosphericlevels,furtherpromotingtheascent
ofwarmair. StageCcontinuestheocclusion, withsustainedascentofcoldairbyinertiaand
kineticenergyconsumption. StageDrepresentsthecessationofkineticenergyproductionas
temperatures equalize and friction begins to dominate, leading to energy dissipation. Warm
(red) and cold (blue) sectors are indicated alongside the isotherm lines.
ating them based on environmental conditions related to the base state flow (diffluent for
the former and confluent for the latter). This section will primarily focus on the develop-
ment of these systems from the perspective of dynamic destabilization mechanisms in the
atmosphere, linking these mechanisms to the energetics of transient atmospheric systems,
further explored in Section 2.4.
Baroclinic instability (I ) is identified as the principal mechanism behind the deve-
BC
lopment of typical extratropical cyclones (Charney, 1947; Bjerknes and Solberg, 1922). As
Holton (1973) explains, I involves the amplification of small disturbances in areas with
BC
strong velocity shears, such as jet streams, where the disturbances extract energy from
the jet and grow in size and intensity. In the atmosphere, I is primarily driven by the
BC
meridional temperature gradient, especially at lower levels, and is linked to vertical shear
via the thermal wind (V ) relationship, frequently occurring in the polar frontal zone.
T
Baroclinic disturbances can also intensify existing temperature gradients, leading to the
formation of frontal zones.
Charney (1947)’s seminal study on I sheds light on the intricate mechanisms behind
BC
the formation and evolution of weather patterns, including cyclones and long waves in mid-
dle and high latitudes. Employing a simplified model that allows for analytical solutions,
Charney not only corroborated previously theorized concepts about atmospheric beha-

42
Chapter2.TheoreticalBackground
vior but also deepened the understanding of how wind shear and temperature variations
vertically contribute to atmospheric instability. His analysis indicates that mid-latitude
westward-flowing currents are inherently dynamically unstable. This insight elucidates
how specific disturbances can exponentially grow within a large-scale atmospheric flow
field, explicating the process through which such disturbances can amplify and culminate
in the characteristic weather systems observed in middle and high latitudes.
Eady (1949) made significant advancements in the understanding of I in the at-
BC
mosphere, building on the work of Charney (1947). Eady’s research, which employed a
solvable simplified model, delved into the atmospheric instability arising from disturban-
ces that exponentially grow within a large-scale atmospheric motion context. His analysis
elucidated how specific conditions of stability, wind shear, and vertical temperature varia-
tions contribute to I , proposing a mechanism for the formation and evolution of weather
BC
patterns such as cyclones and long waves in middle and high latitudes. Eady highlighted
how these disturbances grow exponentially faster than others, akin to a process of natural
selection in the atmosphere, leading to the emergence of predominant weather patterns
observed in middle latitudes, including cyclonic systems.
Following the seminal works of Charney (1947) and Eady (1949), Palm´en and Newton
(1969)synthesizedthemainfindingsfromthesubsequentextensiveliteratureonI . Firs-
BC
tly, it is noted that the amplification of atmospheric disturbances is wavelength-dependent,
with disturbances below a critical length never amplifying. The optimal growth occurs
in intermediate wavelengths (between 2500 and 5000 km), with an inverse relationship
between this optimum and latitude—the closer to the Equator, the larger the critical size
below which all waves are unstable. Additionally, there exists a proportional relationship
between the intensification rate and vertical wind shear for wavelengths of maximum ins-
tability, and for longer waves, an increase in wavelength necessitates stronger shear to
maintain equivalent growth rates.
In their analysis, Petterssen and Smebye (1971) categorizes extratropical cyclones into
types based on the dynamic processes driving their development. Type A cyclones follow
the Polar Front Theory model, with the initial disturbance arising at low levels within a
maximal baroclinic zone (frontal), beneath a nearly zonal upper-level jet (Figure 2.8iA).
As these cyclones develop, a cold trough forms at high levels (Figure 2.8iB), remaining
inclined to the cyclone’s axis until occlusion occurs and surface baroclinicity diminishes

|     |     |     | Section2.1.Cyclones: | CategoriesandDefinitions |     |     | 43  |
| --- | --- | --- | -------------------- | ------------------------ | --- | --- | --- |
(Figure 2.8iC). Conversely, type B cyclones initiate from high-level forcing, as an upper-
level trough moves over an area not necessarily featuring a frontal zone (Figure 2.8iiA).
As these systems mature, the gap between the high-level trough and the surface system
narrows,withanincreaseinsurfacebaroclinicityrelativetotheinitialstage(Figure2.8iiB),
culminating in the alignment of the high-level cyclonic vortex with the surface low, leading
| to system | occlusion | (Figure | 2.8iiC). |     |     |     |     |
| --------- | --------- | ------- | -------- | --- | --- | --- | --- |
| iA        |           |         | iB       |     | iC  |     |     |
L
500 mb
| 500 mb |     |     | 500 mb |     |     |     |     |
| ------ | --- | --- | ------ | --- | --- | --- | --- |
N
| N       |     |     | N       | L   |         | L   |     |
| ------- | --- | --- | ------- | --- | ------- | --- | --- |
| Surface |     |     | Surface |     | Surface |     |     |
| iiA     |     |     | iiB     |     | iiC     |     |     |
L
| 500 mb |     |     | 500 mb |     |     |     |     |
| ------ | --- | --- | ------ | --- | --- | --- | --- |
500 mb
| N       |     |     | N       | L   |         |     |     |
| ------- | --- | --- | ------- | --- | ------- | --- | --- |
|         |     |     |         |     | N       | L   |     |
| Surface |     |     | Surface |     | Surface |     |     |
Figure2.8: IllustrationofthedevelopmentmodelforcyclonestypesA(i)andB(ii),depicting
the stages of formation (A), intensification (B), and maturity (C), as proposed by Petterssen
| and | Smebye | (1971). Inspired | by Donald | Ahrens and Henson | (2015). |     |     |
| --- | ------ | ---------------- | --------- | ----------------- | ------- | --- | --- |
Just as Hart (2003)’s classification presents a continuum, so too does Petterssen and
Smebye (1971)’s delineation of cyclone types, with A and B not being distinct categories
due to the existence of systems displaying hybrid characteristics. Petterssen and Smebye
(1971) observed that purely type A cyclones are more common, whereas purely type B
cyclones are rare, attributing this to the fact that some type of baroclinicity is often
present in the mid-latitudes. However, Petterssen noted a tendency for type A cyclones to
develop over oceans and type B cyclones over continents, though subsequent research, such

44
Chapter2.TheoreticalBackground
as by McLennan (1988) and Deveson et al. (2002), has identified type B systems forming
over oceanic regions as well.
Radinovic (1986) proposed another cyclone type, known as type C, associated with
orographic effects, commonly referred to as lee cyclones. These cyclones develop when
an upper-level cold trough passes over a mountain range, triggering baroclinic instability
and low-level cyclogenesis on the lee side of the mountain. Later, Deveson et al. (2002)
introduced a different type C classification, referring to cyclones found in high latitudes
with similarities to polar lows, characterized by stronger high-level forcing related to the
movement ofa broad troughoveroceanic regions. This studyalso highlighted thepotential
for cyclones to transition between types throughout their lifecycle.
The central role of baroclinic instability (I ) in the development of extratropical cy-
BC
clones is well-established, yet the significance of heat flows and diabatic heating cannot
be overstated. Diabatic heating involves heat exchanges between a system and its sur-
roundings through processes such as condensation, evaporation, or radiation. Convective
activities leading to upward atmospheric movements cause diabatic expansion and thus
cooling in air parcels, leading to saturation and the release of latent heat. Such mecha-
nisms provide an additional energy source for the development of extratropical cyclones,
as documented in the literature (Chang et al., 2002, e.g.). Numerical models incorporating
I alongside heat fluxes have shown that instabilities generated under these conditions
BC
yield more intense cyclones with faster development rates (Gall, 1976; Whitaker and Davis,
1994; Gutowski et al., 1992), a phenomenon referred to as moist baroclinic instability.
A pivotal study by Hoskins and Valdes (1990) underscores the importance of diabatic
fluxes in the development of extratropical cyclones, demonstrating that cyclonic develop-
mentispreferentiallylocatedinregionsofmaximalbaroclinicityovertheoceans. However,
the heat transport facilitated by these systems tends to mitigate the baroclinicity. The
study suggests that diabatic heating, through the latent heat release from individual sys-
tems, contributes to sustaining regional baroclinicity. It also highlights the role of sensible
heat exchanges between the cold air associated with these systems and the warm ocean
currents along the eastern coastlines of continents.
Tropical cyclone formation, a topic of ongoing discussion among meteorologists, ty-
pically occurs over tropical or subtropical oceans, a region where the scarcity of in situ
observations challenges the validation of theoretical models for formation and intensifica-

45
Section2.1.Cyclones: CategoriesandDefinitions
tion. During World War II, data collected from the military base in Guam facilitated Riehl
(1948) in proposing that the instability necessary for typhoon formation originates within
the trade winds, contradicting the then-prevailing belief of inter-hemispheric air mass in-
teractions being the primary cause. Subsequently, Yanai (1961)’s study on Typhoon Doris
furthered the understanding of typhoon genesis, highlighting the significant role of latent
heat released by convection. Yanai suggested a model for typhoon development, begin-
ning with a disturbance in the trade winds and culminating in the formation of a typhoon
characterized by a stabilized warm core.
Charney and Eliassen (1964) detailed the process of tropical cyclone intensification
known as conditional instability of the second kind (CISK), which was the most accepted
theory at the time (Figure 2.9i). According to CISK, the condensation of water vapor
within convective areas releases latent heat, which can amplify pre-existing atmospheric
vortices given an adequate moisture supply. This release of heat not only promotes further
convection but also lowers sea-level pressure, thereby strengthening surface winds, enhan-
cing moisture influx, and establishing a positive feedback loop. Charney underscored the
ocean’s surface role in providing the moisture necessary for sustaining convection, as well
as the importance of surface friction in dissipating kinetic energy and fostering wind con-
vergence within the moist surface boundary layer, thereby fueling the system with thermal
energy from latent heat. This mechanism emphasizes the pivotal role of latent heat release
at the cyclone’s center as a disturbance amplification factor, leading to the intensification
of the tropical depression.
While Charney and Eliassen (1964)’s work introduces a mathematical model for un-
derstanding tropical cyclone intensification through the CISK process, it doesn’t offer a
straightforward, didactic explanation of the involved mechanisms. This has left room for
various interpretations over the years, not all of which have been accurate, as noted by
Ooyama (1982). The explanation provided here aims to to simplify the main processes
proposed by Charney’s for clarity.
Challenging the CISK theory, Emanuel (1986), later refined by Yano and Emanuel
(1991), introduced the Wind-Induced Surface Heat Exchange (WISHE) theory, emphasi-
zing ocean-atmosphere interaction as the primary intensification mechanism for tropical
cyclones (Figure 2.9ii). WISHE posits that the development of these systems depends
on the thermal contrast between the atmosphere and the sea surface, mediated by latent

| 46  |     | Chapter2.TheoreticalBackground |     |     |
| --- | --- | ------------------------------ | --- | --- |
| iA  |     | iB                             |     | iC  |
| iiA |     | iiB                            |     | iiC |
Figure2.9: ComparativeillustrationoftheCISK(i)andWISHE(ii)theories. Adepictsthe
initial disturbance over warm ocean temperatures. Under CISK, the disturbance is initially
fueledbylatentheatfromconvection,whereasWISHEattributestheinitialenergysourceto
latent heat transfer from the ocean to the atmosphere. In the early development stage (B),
both theories observe an increase in convection. CISK suggests this leads to reduced central
pressure,drawinginmoremoistureandenhancingconvection,whichreleasesadditionalheat.
WISHE proposes that surface wind interaction with the sea surface at low central pressure
enhances heat release from surface water evaporation, further driving convection and subse-
quentlatentheatrelease. Bythetropicalstormphase(C),thetheoriesalignonthefeedback
| mechanisms | fueling system | intensification. |     |     |
| ---------- | -------------- | ---------------- | --- | --- |
heat transfer from the ocean to the atmosphere. This transfer is significantly amplified
by surface wind speeds, with intense winds elevating evaporation rates and thus, moisture
transfer. An initial atmospheric disturbance that promotes wind convergence toward its
center can enhance this moisture transfer and convection intensity, fostering a positive
feedback cycle. WISHE theory emphasizes the necessity of ocean temperatures exceeding
26°C
for sufficient boundary layer convergence, vital for maintaining the system. Similar
to CISK, interpretations of WISHE vary, with not all encapsulating the theory’s full scope
or accuracy (Montgomery and Smith, 2014); thus, the provided explanation concentrates
| on fundamental | aspects | for comparative | purposes with | CISK. |
| -------------- | ------- | --------------- | ------------- | ----- |

47
Section2.1.Cyclones: CategoriesandDefinitions
Despite advancements in identifying the prerequisites for tropical cyclone develop-
ment—suchasrequisiteseasurfacetemperatures, minimalverticalwindshear, andspecific
atmospheric conditions—consensus on the precise dynamic processes driving both forma-
tion and intensification remains elusive. This ongoing debate in meteorology is exemplified
by the contrasting theories of CISK and WISHE, each proposing different intensification
mechanisms for tropical cyclones (Craig and Gray, 1996; Gray, 1998; Montgomery et al.,
2015; Ooyama, 1982; Montgomery and Smith, 2014, e.g.,). Nonetheless, a common point
between them is the acknowledgment that diabatic processes, fueled by ocean-atmosphere
interactions and given an initial disturbance, are critical for providing energy and further
intensifying the system. This section’s goal is to delineate the development mechanisms of
tropical versus extratropical cyclones, for which the simplified descriptions provided herein
offer an adequate overview.
The role of diabatic heating in the intensification of tropical cyclones is underscored
by the need for an initial atmospheric disturbance. Frank (1970) conducted an analy-
sis of systems in the North Atlantic that give rise to disturbances capable of developing
into tropical cyclones. He identified several sources of these disturbances, including those
originating from the Intertropical Convergence Zone (ITCZ) and convection zones within
the Caribbean Sea. However, the majority are associated with tropical waves primarily
emanating from the African continent. Frank also highlighted the process whereby barocli-
nic systems transition into warm-core structures through the convection-driven release of
latent heat, effectively diminishing the system’s original baroclinicity. This phenomenon
is now recognized as the tropical transition of extratropical cyclones, a process further
explored and detailed in works such as those by Hart (2003).
The genesis of tropical cyclones in the North Atlantic is intricately linked to the for-
mation and development of African easterly waves, with the thermal contrast between the
Sahara Desert and cooler southern regions playing a pivotal role in creating the African
Easterly Jet (AEJ)—a key factor in generating these waves (Holton, 1973). The founda-
tionforunderstandingsuchphenomenawaslaidbyKuo(1949), whopinpointedbarotropic
instability in zonal atmospheric flows as a vital mechanism. This instability, marked by a
change in the sign of absolute vorticity, involves horizontal wind shear and allows vortexes
to extract kinetic energy from the zonal wind flow (Holton, 1973).
Burpee (1972) initially connected African easterly wave development with the insta-

48
Chapter2.TheoreticalBackground
bility of the AEJ, due to both horizontal and vertical shears, pointing to the complex
interaction between barotropic and baroclinic instabilities in the region. Following this,
Rennick (1976) applied a linear pseudo-spectral model based on primitive equations, de-
ducing that barotropic instability acts as a primary catalyst for wave development, while
downplaying the roles of vertical shear and latent heat release in the early stages. This
assertion was supported by Reed et al. (1977) through observational data, demonstrating
that medium and low-level easterly waves meet the criteria for barotropic instability.
An energetic analysis by Norquist et al. (1977) differentiated the destabilization pro-
cesses over land and ocean, with baroclinic conversion dominating over the continent and
barotropic instability gaining importance over oceanic regions—where tropical cyclones
predominantly form. More recently, Wu et al. (2012) employed reanalysis data to es-
tablish a geographical link between the AEJ’s barotropic instability and the origination
pointsofNorthAtlantictropicalcyclones,affirmingthesignificanceoftheAEJ’sbarotropic
instability in relation to tropical cyclogenesis.
The exploration of barotropic instability’s role in tropical cyclone genesis extends
beyond the North Atlantic, encompassing various global regions where similar dynamics
foster local tropical cyclogenesis. While initial studies illuminated the significance of ba-
rotropic instability in the genesis of African easterly waves and their impact on North
Atlantic tropical cyclone formation, subsequent research has broadened our understanding
to include other tropical areas. For instance, Zehr (1992) discovered that most tropi-
cal cyclogenesis events in the North Pacific are associated with a monsoon trough that
encourages local convection.
In addition to easterly waves, different types of tropical disturbances can also disrupt
the base state and instigate tropical cyclogenesis. Ferreira and Schubert (1997) used a
shallow water model to show how barotropic instability related to the ITCZ’s collapse
can initiate a series of tropical disturbances, with some progressing to become tropical
cyclones. Further, Bembenek et al. (2021) employed a global aquaplanet circulation model
to illustrate the significant roles played by the ITCZ’s latitudinal position and moisture
effects in modulating barotropic instability and, consequently, tropical cyclone genesis,
indicating the global influence of barotropic instability on tropical cyclogenesis through
theoretical studies.
Observational evidence supports these theoretical insights. Maloney and Hartmann

49
Section2.1.Cyclones: CategoriesandDefinitions
(2001) observed that the Madden-Julian Oscillation (MJO) phases conducive to westerly
winds along the Pacific enhance barotropic conversions at low levels, thereby aiding tro-
pical cyclone formation in both the Western and Eastern Pacific. Molinari et al. (1997)
noted that temporal variations in the MJO can create conditions favorable for easterly
wave growth, thereby affecting tropical cyclogenesis in the Eastern Pacific. Molinari et al.
(2000) identified a link between the barotropic instability of the base state, associated
with easterly wave occurrence, topographical effects, and the monsoon trough in foste-
ring tropical cyclogenesis in the Eastern Pacific. Lastly, Cao et al. (2012) found that
enhanced ITCZ convection during active phases of the Intraseasonal Oscillation generates
a mean flow state conducive to barotropic instability, promoting tropical cyclogenesis in
the Northwest Pacific.
While subtropical cyclones were identified in earlier works (Simpson, 1952), it wasn’t
until the study by Hart (2003) that they began receiving significant attention. The body
of literature on these systems is still developing, with the processes behind subtropical
cyclogenesis and development remaining an active area of research. Yanase et al. (2014)
advanced the understanding of cyclone genesis by developing an Environmental Parameter
Space, analyzing how cyclone genesis latitude correlates with factors like baroclinicity,
relative humidity, vertical velocity, and potential intensity. This last metric predicts a
tropical cyclone’s maximum possible strength based on environmental conditions such
as sea surface temperature and atmospheric temperature profiles. The study found a
clear correlation: extratropical cyclones are closely linked to baroclinicity, while tropical
cyclones are associated with potential intensity. Conversely, an inverse relationship was
noted—extratropical cyclones inversely relate to potential intensity and tropical cyclones
to baroclinicity. Subtropical cyclones emerged in a transitional space, influenced by both
baroclinicity and potential intensity, which supports the notion of these systems as hybrids
between tropical and extratropical cyclones (Hart, 2003, e.g). Additionally, da Rocha
et al. (2019) suggested that subtropical cyclogenesis could be linked to various synoptic
patterns, such as a shallow trough at mid-upper levels, a mid-upper level cutoff low, or
a Rex blocking pattern. However, a comprehensive discussion delineating the principal
environmental dynamics associated with subtropical cyclone development remains elusive,
indicating a need for further investigation in this area.
The discussion provided thus far can be synthesized by comparing the efficient cau-

50
Chapter2.TheoreticalBackground
ses related to the development of both extratropical and tropical cyclones. Extratropical
systems primarily develop through baroclinic instability, which may be initiated by disrup-
tions in the surface meridional temperature gradient or by the influence of an upper-level
trough, linking to baroclinic regions via the thermal wind relationship (Holton, 1973; Spi-
´
ridonov and Curi´c, 2021). In contrast, tropical cyclone genesis is largely influenced by
barotropic instability within the base state atmosphere, with subsequent disturbances in-
tensifying through processes related to latent heat release, as explained by either CISK or
WISHE theories.
This comparison illustrates that extratropical cyclone formation is closely tied to ther-
mal gradients driving baroclinic instability, whereas tropical cyclone genesis hinges on
barotropic instability, succeeded by a reinforcing latent heat release feedback mechanism.
Despite the absence of a unified diagram akin to Hart (2003)’s material and formal causes
of cyclones, Silva Dias et al. (2004) proposed a conceptual model potentially bridging this
gap (Figure 2.10). This model situates extratropical cyclones within the domain of baro-
clinic instability; tropical cyclones under barotropic instability; and subtropical cyclones
where both instabilities might coexist or compete. The model also distinguishes systems
by their reliance on diabatic processes, particularly latent heat release.
The viewpoint of Silva Dias et al. (2004) gains partial validation through Yanase et al.
(2014)’sanalysis, whichlinkeddifferentcyclonetypestospecificenvironmentalparameters.
Furthermore, Yanase et al. (2014) emphasized the critical role of relative humidity across
all cyclone categories, supporting Silva Dias et al. (2004)’s emphasis on the essential role
of latent heat release in cyclone dynamics. The current study will introduce a conceptual
model,detailedinChapter6,aimingtosynthesizetheprimarymechanismsdrivingcyclonic
development and explore their broader implications.
2.1.4 Final Causes
Final causes delve into the purpose or ultimate reason for the existence of something,
offering insights into the ”why”behind its occurrence. For instance, the final cause of a
table is to serve as a platform for activities such as writing, eating, or working. When
considering cyclones, their final cause could be viewed as the facilitation of heat and
moisture redistribution within the atmosphere, thus playing a crucial role in maintaining
global climatic equilibrium and acting as a mechanism for dissipating excess heat.

51
Section2.1.Cyclones: CategoriesandDefinitions
Latent Heat
Release
Extratropical
Tropical
Baroclinic
Instability
Subtropical
Barotropic
Instability
Figure2.10: Proposedconceptualmodelcorrelatingatmosphericdestabilizationmechanisms
with cyclone types. Each axis within the three-dimensional schema represents a different
process of atmospheric destabilization, allowing the categorization of cyclone types across
the spectrum. Adapted from Silva Dias et al. (2004).
TheEarth’sclimatesystemisfundamentallydrivenbysolarradiation, whilesimultane-
ously losing heat through infrared radiation emitted into space. The unequal distribution
of solar radiation, exacerbated by the tilt of the Earth’s axis, results in energy surpluses in
equatorial regions and deficits in polar areas. This differential heating prompts the forma-
tion of warm air masses near the equator and cold air masses in polar regions, instigating
atmospheric circulation as an effort to achieve thermal equilibrium, a state that remains
elusive due to ongoing differential heating between tropical and polar zones.
Historical and recent advancements in atmospheric science have underscored the sig-
nificance of general atmospheric circulation in climate dynamics (Lorenz, 1967; Hadley,
1735; Stull, 2015; Schneider, 2006). The Hadley Cell emerges as a critical response to the
disparity in solar radiation received at the equator compared to the poles (Figure 2.11).
Warmedairrisesneartheequator, creatinglow-pressurezonesatthesurfaceandhighpres-
sure aloft. This ascending air, replaced by cooler air from higher latitudes, moves poleward
at elevated altitudes due to mass conservation. The conservation of angular momentum

52
Chapter2.TheoreticalBackground
is crucial as this air, moving away from the equator (where surface rotational speed is
maximum), must increase its eastward velocity as it approaches the poles. This dynamic
leads to the formation of subtropical jet streams around 30° latitude. The Polar Cell, in-
tegral to high-latitude atmospheric circulation, is driven by the thermal contrast between
the poles and regions at 60° latitude. This temperature difference induces opposing north-
south pressure gradients, generating equatorward winds that, due to the Coriolis force,
become polar easterlies. At higher levels, winds flow poleward but are deflected eastward,
forming an upper-level westerly flow around the polar low, thus completing the Polar Cell
circulation.
Polar
cell
90°
30°
s
e
di
d
E 60°
y
e
a
dl ell
HC
0°
ITCZ
y
e
ld
lle
C
a
H
60°
s
e
di
d
E
30°
Polar
cell
90°
Figure 2.11: Representation of the global circulation pattern, showing the Hadley Cell
circulation prominent at low latitudes, the transport of momentum and heat by eddies at
mid-latitudes, and the polar cell circulation at high latitudes. Inspired by Stull (2015).
Together, the Hadley and Polar Cells underscore a comprehensive circulation pattern
that transports warm air and angular momentum from the equator towards the poles
and vice versa, facilitating Earth’s energy balance. Although initially conceptualized as
symmetrical circulations extending from the equator to the poles, subsequent research has
emphasized the pivotal role of large-scale eddies in heat and angular momentum transfer

53
Section2.1.Cyclones: CategoriesandDefinitions
(Schneider,2006). Theseeddies, criticaltoatmosphericdynamics, emergeduetobaroclinic
zones in mid-latitudes and are intrinsic to the structure and function of the Ferrel Cell in
mid-latitudes(Held, 1999; Schneider, 2006). Arising from mid-latitude baroclinic zones,
they are indispensable to the Ferrel Cell’s operation, influencing wind patterns across
latitudes and enhancing heat transfer between the tropics and poles (Stull, 2015; Held,
1999).
Due to their relatively small scale compared to extratropical cyclones, tropical cyclones
are not directly associated with the three-cell model of global circulation. They arise in
regions of low baroclinicity, where thermal contrasts are minimal, relying instead on the at-
mosphere’s ability to generate energy from external heat sources. These sources are largely
the warm temperatures of tropical oceans and the air above them (Palm´en and Newton,
1969). Often conceptualized as a Carnot heat engine (Figure 2.12), tropical cyclones draw
heat from the ocean surface—primarily through the latent heat of vaporization—and re-
lease it into space via longwave radiation (Emanuel, 1987; Ozawa and Shimokawa, 2015;
Wang et al., 2022, e.g.,). The cyclone’s intensity depends on the efficiency of this heat en-
gine, which is determined by the temperature difference between the heat source (ocean)
and sink (upper atmosphere). Friction, especially near the ocean surface within the boun-
dary layer, plays a crucial role by causing energy loss that can lessen wind speeds and alter
angular momentum, impacting the cyclone’s energy conversion efficiency.
We can see then that tropical cyclones serve to dissipate excess heat in the tropics,
utilizing oceanic heat to fuel the system while dissipating energy through radiation at the
upper levels or friction at the surface. Given this model’s applicability, Emanuel (1987)
predictedthatrisingatmosphericCO levelswouldleadtomoreintensetropicalcyclonesin
2
the future. Recent climate models suggest an increase in tropical cyclone intensity, though
there’s no global consensus on frequency changes (Knutson et al., 2010; Walsh, 2004;
Walsh et al., 2016, 2019). As discussed in Section 2.1.3, understanding tropical cyclone
development remains a significant scientific endeavour, complicating precise predictions of
their response to climate change and their regulatory effect on climate.
In exploring subtropical cyclones, much remains to be discovered. The global distribu-
tion of cyclonic activity exhibits a bimodal pattern, with tropical cyclones forming in tropi-
cal regions and extratropical cyclones in mid-latitudes, leaving subtropical areas relatively
calm in terms of cyclonic development (Yanase et al., 2014). It’s speculative—emphasis

54
Chapter2.TheoreticalBackground
C
Tropical cyclone
cloud band
D
Atmosphere
B A
Sea surface
Figure 2.12: Diagrammatic Representation of a Tropical Cyclone as a Carnot Heat Engine.
The process begins with isothermal inflow (A-B) at the surface, drawing energy from warm
ocean waters into the cyclone’s core. This stage is succeeded by the upward movement of air
(convection) and outward flow just below the tropopause, characterized by radiative cooling
and energy loss (B-C). Subsequently, cooled air descends away from the cyclone’s center (C-
D) and cycles back towards the cyclone, completing the circuit (D-A). Adaptation based on
the COMET Program.
on ”speculate”—to suggest that subtropical systems share the final causes of their tropical
and extratropical counterparts, acting to erase thermal gradients by redistributing heat
globally or dissipating excess heat. However, subtropical cyclones might perform these
functions under hybrid environmental conditions, possibly moderating gradients in regions
with an abundance of heat. Ongoing research into subtropical cyclones promises to pro-
vide further clarity on their impact on global circulation patterns and their role within the
broader climatic system.
2.1.5 Summary
ThissectionhasexploredtheAristoteliancausesastheypertaintocyclones, comparing
the various types—extratropical, tropical, and subtropical—while also acknowledging the
existence of other cyclonic phenomena like warm seclusions and polar lows. For succinct-

55
Section2.1.Cyclones: CategoriesandDefinitions
ness, the discussion primarily centered on the main types, suggesting that cyclonic systems
form a continuum: extratropical systems at one end, tropical cyclones at the other, and
subtropical systems exhibiting hybrid characteristics.
Initially, we discussed that cyclones’ material causes are linked to the air masses cons-
tituting them. Extratropical cyclones are associated with cold cores throughout the tro-
posphere, whereas tropical cyclones are characterized by warm cores. Subtropical cyclones,
however, display warm cores at the surface and cold cores at higher tropospheric levels.
Regardingformalcauses, thecyclonesdifferinstructure. Extratropicalcyclones, identi-
fied by their frontal features, show asymmetry. Tropical cyclones, described as symmetric,
feature convection bands spiraling the central eye. Subtropical cyclones, meanwhile, may
present a range of spatial configurations, neither fully asymmetric nor symmetric.
Efficient causes, the dynamic mechanisms behind cyclone development, vary. Extratro-
pical cyclones are primarily driven by baroclinic instability, a comprehensive mechanism
underlying their formation. Tropical cyclone genesis and intensification lack a unified
theoretical model, with current theories suggesting that barotropic instability in tropical
waves—coupled with diabatic processes like latent heat release—might describe their de-
velopment. Subtropical systems, given the incipient state of research, are speculatively
linked by the author to both baroclinic and barotropic instabilities, with diabatic heating
playing a role.
The final causes reflect cyclones’ contributions to global circulation. Extratropical
cyclones are recognized for redistributing heat, mitigating temperature gradients in mid-
latitudes. Tropical cyclones, functioning as thermal engines, dissipate excess heat in tro-
pical regions. The role of subtropical cyclones in the climate system remains speculative;
they are hypothesized to simultaneously embody the functions of the other two types.
One important feature noted is that most classifications adopted for cyclone classi-
fication are based on Hart (2003) diagrams that objectively distinguishes these systems
based on their material and formal causes. Although much knowledge exists regarding the
efficient and final causes of tropical and especially extratropical systems, such objective
criterion for these causes is still lacking. The current research proposes such objective
classification procedure in the hopes of aiding the investigation of such causes related to
cyclonic systems.

56
Chapter2.TheoreticalBackground
2.2 Cyclones in South America
This section transitions to examining cyclonic phenomena within South America, with
a particular emphasis on systems originating in or adjacent to this region. While previ-
ous sections have provided a comprehensive overview of various cyclone categories, their
structures, formation mechanisms, and roles in atmospheric circulation, here we delve into
cyclonic systems that have genesis in South America or its neighboring oceanic regions.
Although systems originating along the western coast of South America are noted (Crespo
et al., 2023, e.g.,), our primary focus is on cyclones forming in the southern and eastern
sectors of South America and the Southeastern Atlantic region. These systems significan-
tly influence the regional climate, particularly in South and Southeastern Brazil (de Souza
et al., 2022; Reboita et al., 2010, e.g.), and can cause extreme weather events (Cardoso
et al., 2022; de Souza and da Silva, 2021; Gramcianinov et al., 2020, e.g.). From this point
on, we refer to this region encompassing the Southeastern Atlantic and the adjacent South
American region as SESA.
2.2.1 Climatological aspects
The first cyclone climatologies for the SESA region were conducted by van Loon
(1965) and Taljaard (1967), using visual inspection of surface pressure maps. While Necco
(1982a,b) utilized analysis data, their study was limited to a single year (1978-1979) and
identified a cyclogenetic region south of 35ºS and west of 30ºW. More recently, Gan and
Rao (1991) utilized sea level pressure data from surface charts spanning a decade. Despite
methodological constraints, the authors identified two primary cyclogenesis regions: one
over Uruguay and another in Southeast Argentina, with the latter being more active in
austral summer and the former in winter. They hypothesized that the cyclogenesis in these
regions was driven by baroclinic instability of the westerlies and, for the Uruguay region,
lee cyclogenesis—cyclogenesis influenced by the interaction between baroclinic disturban-
ces and topography (Gan and Rao, 1994; Tibaldi et al., 1980).
Later studies, employing automated techniques to detect cyclones’ minimum central
pressure, validated the cyclogenesis regions identified by Gan and Rao (1991) (Simmonds
and Murray, 1999; Simmonds and Keay, 2000; Mendes et al., 2010). Meanwhile, analyses
based on relative vorticity fields, as opposed to minimum central pressure, found a third

57
Section2.2.CyclonesinSouthAmerica
significant cyclogenesis area near Southeast Brazil (Hoskins and Hodges, 2005; Sinclair,
1995; Reboita et al., 2010; Gramcianinov et al., 2019). The shift towards relative vorticity
for cyclone tracking, as discussed by Hoskins and Hodges (2002); Sinclair (1994), offers
several technical advantages. In mid-latitudes, the background pressure gradient’s inten-
sity can foreshadow closed isobars in developing cyclones, making it challenging to detect
cyclones until they intensify or reach higher latitudes. Thus, employing relative vorticity
enables the identification of weaker and faster-moving systems, as well as cyclones in their
nascent stages, when closed isobars might not yet be evident.
In the SESA region, previous research has successfully identified three key areas of cy-
clogenesis,andthiscurrentstudywilladoptthenomenclatureestablishedbyGramcianinov
et al. (2019) for consistency and clarity. The ARG region, situated in Southeast Argentina,
emerges as the most active, with a relatively steady cyclogenesis rate throughout the year,
though it peaks during the austral summer (Crespo et al., 2021; Gramcianinov et al., 2019;
Reboita et al., 2010). The LA-PLATA region, over the La Plata River basin, ranks second
in genesis density, displaying heightened activity in the austral winter (Crespo et al., 2021;
Gramcianinov et al., 2019; Reboita et al., 2010). It’s noteworthy that Reboita et al. (2010)
identified the LA-PLATA region along the Uruguayan coast rather than over the continent,
influenced by the application of a continental mask in cyclone tracking, which biases de-
tection towards maritime regions. The final region, SE-BR, located near the Southeastern
Brazilian coast, records the fewest genesis events, with a significant increase in activity
during the austral summer compared to winter (Reboita et al., 2010; Gramcianinov et al.,
2019; Crespo et al., 2021). Figure 2.13 summarises these findings.
2.2.2 Genesis mechanisms
The majority of systems in SESA region are extratropical (Marrafon et al., 2022),
thus baroclinic instability serves as the primary genesis mechanism across all regions, as
discussed in Section 2.1.3. However, each region is also influenced by secondary mecha-
nisms. Notably, all regions lie on the lee side of the Andes, where baroclinic development
of troughs crossing the mountain range can prompt surface cyclogenesis (Gan and Rao,
1994; Vera et al., 2002; Hoskins and Hodges, 2005; Gramcianinov et al., 2019). Addi-
tionally, downstream development, marked by system decay on the Andes’ upslope and
regeneration on the downslope facilitated by vortex stretching over the mountain barrier,

58
Chapter2.TheoreticalBackground
More active
FMAN
DJ
M
AJJ
S
O
FMAN
DJ
M
AJJ
S
O
FMAN
DJ
M
AJJ
S
O Less active
Figure 2.13: Illustrative mapping of cyclogenesis activity within the South Ameri-
can/SoutheasternAtlantic(SESA)region,categorizedintothreeprimarygenesisareas: ARG
(Southeast Argentina), LA-PLATA (La Plata River basin), and SE-BR (Southeastern Brazi-
lian coast). The diagram highlights the cyclogenesis frequency and seasonal patterns in each
region, with a visual scale indicating activity levels from more active to less active.
is observed (Hoskins and Hodges, 2005).
Gan (1992) analyzed the formation of two cyclone cases in the Plata region, one in
summer and the other in winter. In the winter case, it was observed that the cyclone
formed due to baroclinic instability, but its movement indicated interaction with the topo-
graphic wave. In the summer case, the cyclone initially formed due to topographic effects,
but during its trajectory, it intensified due to baroclinic instability. Subsequent analyses
by Gramcianinov et al. (2019) and Crespo et al. (2021) delve into the specific genesis me-
chanisms for each cyclogenesis region. Their findings, synthesized in this section, compare
summer and winter mechanisms, as transitional seasons typically exhibit intermediate cha-
racteristics (Gan and Rao, 1991; Hoskins and Hodges, 2005; Gramcianinov et al., 2019;
Crespo et al., 2021).
In both seasons, cyclones in ARG region tend to follow a traditional baroclinic de-

59
Section2.2.CyclonesinSouthAmerica
velopment pathway, heavily influenced by low level cold advection (Gramcianinov et al.,
2019). This advection is crucial in reducing static stability, due to the contrast between
the warmer surface and cold air aloft, thereby facilitating cyclogenesis. The cyclogenesis
position relative to the jet stream provides upper-level support, either at the poleward exit
during summer or the equatorward entrance during winter (Crespo et al., 2021). During
summer, a slightly more baroclinic environment and more pronounced potential vorticity
anomalies promote conditions favorable for ascending vertical movements (Crespo et al.,
2021).
Cyclone development in the LA-PLATA region is initially driven by moisture transport
from the South American low-level jet on the eastern slope of the Andes and from the
South Atlantic Subtropical High towards the southeastern coast (Gramcianinov et al.,
2019). This transport feeds cyclone development with warm, moist air, promoting low-
levelinstability. Furthermore, cyclogenesisinthisregionisinfluencedbypotentialvorticity
anomalies in both summer and winter (Crespo et al., 2021). The area is positioned beneath
the equatorial entrance of a jet streak in both seasons, with a slightly more pronounced
baroclinic environment in winter (Crespo et al., 2021).
During summer, cyclogenesis in the SE-BR region is significantly influenced by the
transportofwarmandmoistairfromthetropics, associatedwiththeSouthAmericanLow-
Level Jet (Gramcianinov et al., 2019). This process contributes to cyclogenesis through
diabatic heating and convective processes. In winter, upper-level forcing becomes more
prominent, with baroclinic conditions intensified by the presence of strong temperature
gradients and jet stream dynamics (Gramcianinov et al., 2019). Moreover, during summer,
cyclogenesis occurs in a more barotropic environment, with the jet stream significantly
displaced from the genesis region, and is highly influenced by high-level potential vorticity
anomalies (Crespo et al., 2021). Conversely, in winter, cyclogenesis occurs beneath the
equatorial entrance of a jet streak in a more baroclinic environment compared to summer,
influenced by low-level potential vorticity anomalies (Crespo et al., 2021).
2.2.3 Subtropical cyclones
It was only after Hart (2003) work that the scientific community started to take a clo-
ser look at subtropical cyclones. It wasn’t until about 20 years ago that the first detailed
climatology for subtropical cyclones in the South Atlantic was conducted by Evans and

60
Chapter2.TheoreticalBackground
Braun (2012). This study uncovered an average occurrence of roughly one subtropical cy-
clone per year in the region, with a relatively uniform distribution across seasons. Notably,
subtropical cyclogenesis was found to occur in diverse environments: genesis in the open
ocean primarily involves Rossby wave breaking, similar to systems in the North Atlan-
tic, whereas coastal genesis is often related to lee cyclogenesis, influenced by the warmer
sea surface temperatures of the Brazilian Current, which create conducive conditions for
subtropical cyclone formation.
Gozzo et al. (2014) introduced modifications to the criteria used by (Evans and Braun,
2012), aiming to capture weaker and shallower systems in their analysis. This adjustment
led to the identification of an average of 7 cyclones per year, a significant increase from the
findings of the previous study. Gozzo et al. (2014) emphasized the subtropical cyclones’
lower traveled distance and displacement speed compared to their extratropical counter-
parts, allowing them more time to interact with the unstable conditions that facilitated
their genesis and to exert greater impact on the South American coastal zone.
Moreover, Gozzoetal.(2014)noteddistinctionsinseasonalactivity, withapeakduring
summer but stronger systems occurring in autumn. The Southeastern Brazil region (SE-
BR) emerged as the predominant genesis area, with over a third of the cyclones developing
there exhibiting hybrid characteristics. These systems typically originate from upper-level
potential vorticity anomalies and divergence within a low-shear environment. At lower
levels, warm and moist air advection, primarily from the subtropical high, is crucial for
their formation. During summer, an additional moisture source from the tropics is also
significant. Also, the authors used numerical simulation for demonstrating the importance
of local latent heat fluxes for the systems develoment.
Gozzo et al. (2017) reinforced the findings of Gozzo et al. (2014), confirming the role of
moisture fluxes in the formation of subtropical cyclones in the SE-BR region. They high-
lighted that moisture transport from the subtropical high is particularly crucial during
the summer months when it shifts closer to the Brazilian southeastern coast. The redu-
ced number of genesis events observed in the winter can be attributed to the diminished
strength of this moisture transport. In contrast, during autumn, transient high-pressure
systems serve as the primary source of moisture. Moreover, through numerical simulations,
the authors demonstrated the significance of local latent heat fluxes in the development of
these systems.

61
Section2.2.CyclonesinSouthAmerica
Subtropical cyclones in the South Atlantic remain an area ripe for exploration due
to their relatively sparse coverage in scientific literature. From the limited climatologies
available, and the few study cases (Reboita et al., 2018, 2022; Dias Pinto and Rocha, 2011,
e.g.) it is evident that the formation of these systems is closely linked to Rossby wave
breaking and are fueled by both local and non-local latent heat fluxes. However, the door
remains open for more comprehensive studies to explore the their dynamics, climatological
impacts, and the potential influence of broader atmospheric and oceanic processes on their
formation.
2.2.4 Tropical cyclones
Historically, itwasbelievedthattheSouthAtlantic, specificallytheSoutheasternSouth
Atlantic (SESA), was not conducive to tropical cyclone formation due to insufficiently high
sea-surface temperatures and relatively strong vertical wind shear. This perspective, da-
ting back to Gray (1968), identified the South Atlantic as the sole oceanic basin without
such systems. However, this view was upended by Hurricane Catarina in 2004, the first re-
corded hurricane in the South Atlantic, which challenged previous assumptions. Although
there was some evidence of weak tropical cyclones in the region before the satellite era
(da Silva Dias et al., 2004), Hurricane Catarina sparked renewed investigations into the
potential for tropical cyclogenesis in South America, leading to studies such as Andre-
lina Silva and Sim˜oes Reboita (2021).
Catarina, which originated from an extratropical system near the southeastern Brazi-
lian coast, underwent a tropical transition and made landfall in Southern Brazil (Pezza
and Simmonds, 2005). The system’s trajectory and development were significantly influen-
ced by unique environmental conditions, including a dipole-blocking pattern in the upper
atmosphere, guiding the system back toward Brazil over relatively cool sea surface tem-
peratures (SSTs) of around 25°C (McTaggart-Cowan et al., 2006). This development over
cooler SSTs was facilitated by a unique combination of extreme blocking conditions, low
wind shear favored by an extreme positive phase of the Southern Annular Mode (Pezza
and Simmonds, 2005; Pezza et al., 2009), and latent heat release from air-sea interacti-
ons. Strong interactions with sub-superficial warm waters by Ekman pumping led to the
upwelling of isotherms and mixed layer waters, allowing for a significant air-sea tempera-
ture gradient and vigorous heat exchange between the ocean and atmosphere, fueling the

62
Chapter2.TheoreticalBackground
system through latent heat release (Vianna et al., 2010; Pereira Filho et al., 2010).
Hurricane Catarina, while a landmark event, did not originate from a purely tropical
process; it was a baroclinic cyclone that underwent tropical transition. This distinction
was pivotal until the emergence of a system near Brazil’s Northeast oceanic region in 2019,
reported as the first instance of pure tropical cyclogenesis in the South Atlantic. This
system, named Iba, marked a significant departure from previous understandings of cy-
clonic activity in the region (Reboita et al., 2021). Additionally, research on subtropical
cyclone Anita in March 2010 suggested its potential for tropical transition under warmer
sea surface conditions and without interference from a neighboring extratropical cyclone
(Dias Pinto and Rocha, 2011; Reboita et al., 2019). In March 2024, another system na-
med Akara´, originating near Southeastern Brazil and featuring eye-like characteristics and
a symmetric form, ignited discussions regarding its potential classification as a tropical
cyclone, although a detailed examination of its characteristics is pending.
The sporadic nature of these systems in the SESA region precludes the formation of
a comprehensive tropical cyclone climatology. While there is some conjecture about the
influence of climate change on the emergence of these systems (Pezza and Simmonds,
2005; McTaggart-Cowan et al., 2006; Pezza et al., 2009; Pereira Filho et al., 2010, e.g.,),
establishing a direct connection between recent tropical cyclone occurrences in SESA and
global climatic shifts remains elusive. The rarity of such events continues to challenge
researchers, suggesting a complex interaction between regional climatic conditions and
broader atmospheric patterns influenced by climate change.
2.3 Life cycle of extratropical cyclones: objective classification
procedures
This section explores lifecycle and classification procedures for extratropical cyclones,
building upon conceptual models and evolution patterns discussed in Sections 2.1.2 and
2.1.3. These models, derived from case studies and numerical simulations, seek to genera-
lize cyclone development phases due to the absence of standardized methods for analyzing
distinct lifecycle stages across extensive datasets. Herein, we introduce an automated ap-
proach for detecting the lifecycle of cyclones, thereby advancing the discussion on objective
classification methodologies for these atmospheric phenomena.

63
Section2.3.Lifecycleofextratropicalcyclones: objectiveclassificationprocedures
The Polar Front Theory, as detailed by Bjerknes and Solberg (1922), was among the
first to describe the lifecycle of extratropical cyclones, delineating distinct phases based
on structural transformations and large-scale dynamics. Nonetheless, Shapiro and Keyser
(1990) later argued that not all cyclones adhere strictly to the progression outlined by
Bjerknes, proposing an alternative model that complements the original theory. These
developmental models, including their respective stages, are elaborated in Section 2.1.2
and illustrated in Figure 2.4. While these descriptions offer detailed insights into the
structural changes cyclones undergo, they fall short of directly associating each phase with
specific atmospheric variables in a way that allows for algorithmic detection and statistical
and/or spatial analysis.
Whittaker and Horn (1984) conducted one of the earliest cyclone climatology studies,
identifying cyclogenesis regions based on the formation of the first closed isobar. This
definition has been widely used since (Gan and Rao, 1991; Simmonds and Keay, 2000;
Hoskins and Hodges, 2005; Trigo, 2006; Gramcianinov et al., 2019, e.g). Whittaker and
Horn(1984)alsodefinedcycloneintensificationastherateofsealevelpressuredeepening,a
definition echoed and expanded upon by later studies through metrics like relative vorticity
growth rate (Grise et al., 2013; Gramcianinov et al., 2019; Hoskins and Hodges, 2005) and
the baroclinic Eady growth rate (Pinto et al., 2005). However, Whittaker’s study lacked a
comprehensive method for classifying cyclone evolution.
A classification of the developmental phases throughout the life cycle of cyclones was
conducted by Evans and Hart (2003), with a particular focus on tropical cyclones un-
dergoing extratropical transition. This study explored the structural evolution of such
systems, employing a classification framework grounded in the environmental parameters
outlinedbyHart(2003). Theauthorspartitionedthelifecycleofthecyclonesintotwomain
phases: one preceding and the other following the peak intensity of the tropical cyclone.
This demarcation enabled a detailed analysis of the transformation these cyclones undergo
from their genesis as tropical entities to their eventual extratropical characteristics.
Gray and Dacre (2006) implemented the classification scheme originally proposed by
Deveson et al. (2002), as detailed in Section 2.1.3, to study the climatology of Northern
Atlantic extratropical cyclones. Their analysis focused on the separation between the
upper-leveltroughandthelower-levelcyclonethroughoutthecyclones’intensificationperi-
ods, whichwere identifiedwhen the cyclones’ centralrelative vorticity surpassed aspecified

64
Chapter2.TheoreticalBackground
threshold. While this approach proved beneficial for classification purposes, it overlooked
the exploration of dynamical forcing during the development of cyclones. Furthermore, the
rationale behind the selected threshold value, including its potential applicability across
various scenarios, remained unexplored.
Building upon the foundation laid by Gray and Dacre (2006), Dacre and Gray (2009)
delved into the environmental forces influencing the evolution of different types of cyclones.
To achieve a granular understanding of variations throughout the cyclones’ life cycle, they
segmented the cycle at the juncture of maximum relative vorticity. This segmentation
delineated the period leading up to this juncture as the intensification stage and the subse-
quent period as the decaying stage. Additionally, by categorizing cyclones based on their
overall lifespan, the study facilitated the identification of specific areas prone to cyclone
intensification and the environmental characteristics predominant in those regions.
Rudeva and Gulev (2007) delved into the study of changes in the radius of cyclones th-
roughouttheirlifecycle, introducingtheconceptof”nondimensionalcyclonelifetime.”This
methodology facilitates the comparison of different stages of cyclone development by nor-
malizing their lifespan to a uniform scale, achieved by dividing the current time step
within the system’s life cycle by its total duration. Similar apporaches were employed by
Booth et al. (2018) and Schemm et al. (2018). Specifically, Booth et al. (2018) focused on
analyzing precipitation rates through the cyclone life cycle, identifying the cyclones’ peak
dynamical strength with the point of maximum relative vorticity. Concurrently, Schemm
et al. (2018) applied normalization to the cyclone life cycles using the duration from gene-
sis to lysis, thereby examining the periods when the systems were associated with frontal
structures.
Trigo (2006) explored the spatial distribution of cyclogenesis (i.e., the initial detection
pointofeachlow-pressuresystem),cyclolysis(thefinaldetectedposition),andthelocations
where these systems attained their minimum central pressure. Similarly, Bengtsson et al.
(2009), albeit not explicitly defining developmental stages, observed distinguishable phases
centered around the maximum intensity of the system, characterized as the period when
maximum central relative vorticity is reached. Meanwhile, Azad and Sorteberg (2014a,b)
dissected the cyclone life cycle into distinct stages, identifying the mature phase as the
period during which geostrophic vorticity experiences its most rapid increase, with the
incipient stage occurring beforehand. Moreover, they categorized the life cycle of a cyclone

65
Section2.3.Lifecycleofextratropicalcyclones: objectiveclassificationprocedures
based on the maximum geostrophic vorticity attained; the time leading up to this peak is
labeled as the intensification stage, while the subsequent period is known as the decaying
stage.
Thediversemethodologieshighlightedintheliteratureofferarangeofobjectivecriteria
for delineating the lifecycle of extratropical cyclones, each linked to the temporal dynamics
ofspecificatmosphericvariables. Commonly, cyclonegenesisisidentifiedatthealgorithm’s
first detection, with intensification and decay phases typically defined by changes in central
pressure or, when using relative vorticity for tracking, by the increase (intensification)
or decrease (decay) of vorticity in the Northern Hemisphere. The peak of the system’s
intensityisoftenmarkedasthepointofmaturity,whilelysisisrecognizedatthealgorithm’s
final detection of the system. A schematic illustration of this lifecycle, emphasizing the use
of relative vorticity at the 850 hPa isobaric level (ζ ) for cyclone detection, is depicted
850
in Figure 2.14.
Genesis Lysis
Incipient Intensification Mature Decay
ζ850
Time
ζ850
L L L
SLP
Figure 2.14: Schematic representation of an extratropical cyclone’s life cycle, depicted th-
rough the relative vorticity field at the 850 hPa isobaric level (ζ ). The central figure
850
displays the temporal progression of central ζ at the cyclone’s core across various phases.
850
The bottom figures illustrate the evolution of the ζ field and sea level pressure (SLP) spa-
850
tial distributions during each phase.
Despite these advancements, several limitations persist in current approaches. First,
the initial phase of cyclone development, where the system is present but not yet fully
formed, is often overlooked. In such instances, a cyclone may exhibit closed central relative
vorticity without corresponding closed isobars at sea level pressure (Sinclair, 1995, e.g.).

66
Chapter2.TheoreticalBackground
Second, defining cyclone maturity as merely the point of maximum intensity overlooks
the broader period during which atmospheric dynamics illustrates the cyclone’s evolution.
Finally, characterizing all stages between genesis and maturity as intensification, and those
between maturity and lysis as decay, presupposes a singular, linear progression of these
stages. This assumption fails to account for the potential complexity of cyclone lifecycle
stages, including the possibility of multiple intensification and decay phases.
The ability to discern the distinct life cycle phases of cyclones is crucial for several
reasons. As highlighted in Section 2.2, most climatologies currently focus on either the
entirety of a cyclone’s life cycle or specific points, such as its genesis or lysis. Enhanced
techniques for dissecting a cyclone’s life cycle could unlock the potential for more granular
analyses of the processes and environmental dynamics associated with different stages of
cyclone development. For example, while the initial baroclinicity associated with extratro-
pical cyclones is well-documented, the environmental shifts that trigger their cessation of
intensification remain less understood. Case studies have shed light on these aspects, but
comprehensive testing under climatological conditions is yet to be conducted.
By identifying the environmental conditions pertinent to various stages of cyclone de-
velopment, researchers can leverage climate change projections to assess potential future
shifts in these conditions. Moreover, given the absence of a universally recognized con-
ceptual model for tropical cyclone development, detailed climatological analyses of envi-
ronmental parameters across distinct life cycle phases could offer critical insights toward
establishing such a model. Thus, the potential applications of a refined procedure for
analyzing cyclone life cycle phases are vast, limited only by the creativity and curiosity of
the research community. Such advancements would not only enhance our understanding
of cyclone dynamics but also improve our ability to predict and respond to these powerful
weather systems in the context of a changing climate.
2.4 Atmosphere Energetics
Solar radiation serves as the primary energy source within the Earth’s system. Concur-
rently, the atmosphere globally dissipates heat by emitting infrared radiation into space.
The tilt of the Earth’s axis causes a significant variation in radiative incidence between
the tropical and polar regions: tropical areas receive more solar energy than they emit,

67
Section2.4.AtmosphereEnergetics
creating an energy surplus, whereas polar regions experience an energy deficit, losing more
energy to space than they absorb. This differential heating leads to the formation of
warm air masses in tropical regions and cold air masses in polar regions. The resulting
heat imbalance drives atmospheric circulation, an ongoing process attempting to balance
these temperature disparities. However, this equilibrium is never fully achieved due to the
constant differential heating between the tropical and polar regions (Stull, 2015).
2.4.1 Lorenz Energy Cycle: Historical Background
The Lorenz Energy Cycle, introduced by Lorenz (1955), is a framework for understan-
ding how energy is distributed and transformed within the atmosphere. This framework
offers insights into the general circulation that shapes the dynamic and thermodynamic
structuresoftheatmosphere,influencingatmosphericflowsandthetransportofheat,mois-
ture, and angular momentum. In his groundbreaking work, Lorenz delineated a method
to analyze atmospheric energetics by focusing on two primary forms of energy: kinetic
energy (K) and available potential energy (APE), each further divided into zonal and eddy
(turbulent) components. This section explores these energy forms and their interactions.
Lorenz argued that the total potential energy (P) of the atmosphere does not effecti-
vely represent the energy available for conversion into K to drive global circulation. To
illustrate this concept, Lorenz proposed a thought experiment: Imagine the atmosphere is
uniformly horizontally stratified; in such a scenario, despite the presence of P, the lack of
horizontal gradients precludes air mass movement, resulting in no generation of K (Figure
2.15a). However, if part of the atmosphere is heated, it triggers vertical upward move-
ments, establishing pressure gradients and disrupting the horizontal stratification (Figure
2.15b). Conversely, cooling in a region induces similar effects but with vertical downward
movements (Figure 2.15c). Both scenarios alter the P of the system, converting it into K.
Yet, in the first case, P increases, while in the second, it decreases; that is, both increases
and decreases of P are responsible for making energy available for atmospheric circulation.
The concept of Available Potential Energy (APE) was initially proposed by Margules
(1903), who was interested in the processes that generate kinetic energy (K) in storms
(Marquet, 2017). To understand this concept, we can start from the same situation pro-
posed by Lorenz (1955), where differential heating results in ascending movements and
a heterogeneous distribution of mass in the atmosphere (Figure 2.16a). In this case, the

68
Chapter2.TheoreticalBackground
Figure 2.15: Mental experiment proposed by Lorenz (1955) to illustrate the relationship
between total P and K, depicted through a two-layer atmospheric model: (A) Initially ho-
rizontally stratified atmosphere. (B) Perturbation caused by localized heating (+Q) leading
to vertical upward movements. (C) Similar perturbation caused by cooling (-Q) resulting
in vertical downward movements. Black circles represent the atmosphere’s center of mass
post-perturbation, and white circles indicate the center of mass prior to perturbation.
resulting pressure gradients cause acceleration of the wind field (Figure 2.16b), redistri-
buting the mass in the atmosphere. Assuming this flow is adiabatic, the final result is a
horizontally stratified atmosphere (Figure 2.16c). In the first step, both forms of potential
energy (total and available) are at their maximum. With the redistribution of mass, there
is an increase in K, while the total and available potential energy decreases. In the final
stage, P is minimal, yet not zero, while the APE is zero. Thus, APE can be defined as the
amount of potential energy available for conversion into K under an adiabatic distribution
of mass.
According to Lorenz (1955), APE serves as the primary source of K in the atmosphere,
fundamentally driving the general circulation. While APE and K dominantly shape at-
mospheric dynamics, Lorenz acknowledged that diabatic processes and friction also play
critical roles, though these elements were less detailed in his work due to their complex na-
ture and the challenges associated with their quantification. In his theoretical framework,
Lorenz treated the atmosphere as a closed system, distinguishing between the zonal and
eddy (turbulent) components of APE and K to clarify the energetics involved in atmosphe-
ric processes.

|     |     |     | Section2.4.AtmosphereEnergetics |     |     | 69  |
| --- | --- | --- | ------------------------------- | --- | --- | --- |
Figure 2.16: Depiction of Available Potential Energy (APE) transformations in response to
atmospheric heating and cooling. (A) Initial state with differential heating causing heteroge-
neousmassdistribution. (B)Redistributionofmassviawindfieldsleadingtohomogenization.
(C) Final state of horizontal atmospheric stratification. Black circles indicate the center of
| mass at | each stage, with | white | circles showing | previous | positions. |     |
| ------- | ---------------- | ----- | --------------- | -------- | ---------- | --- |
This distinction is crucial as it aligns with earlier observations by Starr (1953), who
emphasized the significance of eddies in maintaining atmospheric circulation, particularly
their role in transferring K from turbulent to zonal flows. This perspective challenged
earlier assumptions and highlighted the necessity of including eddy dynamics in any com-
prehensive atmospheric circulation theory. Subsequent research by Wiin-Nielsen et al.
(1963) demonstrated the importance of eddies in global heat and momentum transport,
illustrating how different wave numbers contribute to these processes. Through these in-
sights, Lorenz’s separation of energy components facilitates a deeper understanding of
how meteorological systems, such as cyclones, develop and influence broader atmospheric
| circulation patterns. |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- |
The energy cycle can be represented by the following equations, which represent the
| energy balance | for each | component | of the | cycle: |     |     |
| -------------- | -------- | --------- | ------ | ------ | --- | --- |
∂A
Z
|     |     |     | =   | −C −C | +G  | (2.6) |
| --- | --- | --- | --- | ----- | --- | ----- |
|     |     |     | ∂t  | Z     | A Z |       |
∂A
|     |     |     | E = | −C +C | +G  | (2.7) |
| --- | --- | --- | --- | ----- | --- | ----- |
|     |     |     |     | E     | A E |       |
∂t
∂K
|     |     |     | Z = | C −C | −D  | (2.8) |
| --- | --- | --- | --- | ---- | --- | ----- |
|     |     |     |     | Z    | K Z |       |
∂t
∂K
E
|     |     |     | =   | C +C | −D  | (2.9) |
| --- | --- | --- | --- | ---- | --- | ----- |
|     |     |     | ∂t  | E    | K E |       |
Intheseequations,availablepotentialenergy(APE)isdividedintozonal(A )andeddy
Z
(A ) components, as is kinetic energy (K and K , respectively). The transformations
| E   |     |     |     | Z   | E   |     |
| --- | --- | --- | --- | --- | --- | --- |
between these forms of energy are denoted by C, with subscripts Z and E for conversions

| 70  |     | Chapter2.TheoreticalBackground |     |     |     |     |
| --- | --- | ------------------------------ | --- | --- | --- | --- |
between zonal and eddy forms, and A and K indicating conversions between APE and
kinetic energy, respectively. Thus, C represents the conversion between A and A , C
|     |     |     | A   |     | Z E | E   |
| --- | --- | --- | --- | --- | --- | --- |
denotes the conversion from A to K , C signifies the transformation from K to K ,
|     |     | E   | E K |     | E   | Z   |
| --- | --- | --- | --- | --- | --- | --- |
and C describes the conversion from A to K . Generation of APE and dissipation of
| Z   |     |     | Z Z |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
kinetic energy are indicated by G and D, with G and G marking the generation of A
|     |     |     | Z   | E   |     | Z   |
| --- | --- | --- | --- | --- | --- | --- |
and A , and D and D representing the dissipation of K and K , respectively. Full
| E   | Z   | E   |     | Z E |     |     |
| --- | --- | --- | --- | --- | --- | --- |
mathematical formulations for these processes are discussed in Section 2.4.2.
After the seminal work by Lorenz (1955) on the global energy cycle, numerous subse-
quent studies aimed to quantify this cycle, primarily focusing on the Northern Hemisphere
due to observational constraints at the time (Starr, 1959; Saltzman and Fleisher, 1961;
Holopainen, 1964; Jensen, 1961; Brown Jr, 1964; Wiin-Nielsen, 1959, e.g.). Oort (1964)
synthesized these results to depict the annual energy cycle of the Northern Hemisphere.
He innovatively categorized the energy analysis into distinct domains: the spatial domain,
where variables are analyzed based on spatial averages, aiding in the understanding of
large-scale zonal patterns such as jet streams and westerlies; the temporal domain, focu-
sing on averages and deviations over time, which facilitates insights into long-term trends
and transient disturbances; and the mixed space-time domain, which offers an integrated
perspective on how average states and disturbances, both transient and stationary, inte-
ract and are sustained. Oort noted that while there was considerable focus on spatial
domain analyses, studies addressing the mixed domain were scarce, and those considering
| the temporal | domain | were virtually | absent. |     |     |     |
| ------------ | ------ | -------------- | ------- | --- | --- | --- |
From these estimates, Oort (1964) presented a diagram that visually encapsulates the
energy cycle (Figure 2.17). This diagram illustrates the generation, conversion, and dis-
sipation of different energy forms, providing a dynamic overview in a graphical format.
Notably, the diagram allows for straightforward comparisons of diverse study results. It is
important to mention, as Oort (1964) did, that friction terms are typically calculated as
residuals due to the challenges in direct computation, balancing the zonal and turbulent
| terms of kinetic | energy. |     |     |     |     |     |
| ---------------- | ------- | --- | --- | --- | --- | --- |
As previously mentioned, the formulation proposed by Lorenz (1955) estimates the
energeticsoftheatmosphereassumingaclosedsystem,thatis,withoutenergyexchangesat
theboundaries. ThefirststudytoconsiderenergeticsforanopensystemwasbyReedetal.
(1963), which analyzed a sudden stratospheric warming event in the Northern Hemisphere.

|     |     |     | Section2.4.AtmosphereEnergetics |     |     |     |     |     | 71  |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
Figure 2.17: Representation of the energy cycle as formulated by Lorenz (1955) and sche-
matized byOort (1964). Thisdiagram displaysthe interplay amongthe fourforms ofenergy
(zonal and turbulent terms of K and APE), illustrating their conversions, generation, and
dissipation.
This study treated the stratosphere as an open system, permitting energy exchanges with
other atmospheric layers, such as the troposphere. Building on this, Muench (1965), who
was interested in stratospheric dynamics, refined Lorenz (1955)’s theory and proposed a
| new representation | of the | energy | cycle. |     |     |     |     |     |     |
| ------------------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- |
Muench’s model adds boundary flow terms (BA , BA , BK , and BK ) to the ori-
|     |     |     |     |     | Z   | E   | Z   | E   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ginal Lorenz equations, representing respectively the zonal and eddy flows of APE and K
across the system boundaries (Figure 2.18). The updated energy balance equations are:
∂A
Z
|     |     |     | = BA −C | −C  | +G  |     |     |     | (2.10) |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | ------ |
|     |     | ∂t  | Z       | Z   | A Z |     |     |     |        |
∂A
|     |     | E   | = BA −C | +C  | +G  |     |     |     | (2.11) |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | ------ |
|     |     |     | E       | E   | A E |     |     |     |        |
∂t
∂K
Z
|     |     |     | = BK +C | −C  | +BΦ | −D  |     |     | (2.12) |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | ------ |
|     |     |     | Z       | Z   | K   | Z   | Z   |     |        |
∂t
∂K
E
|     |     |     | = BK +C | +C  | +BΦ | −D  |     |     | (2.13) |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | ------ |
|     |     | ∂t  | E       | E   | K   | E   | E   |     |        |
Where BA , BA , BK , and BK represent, respectively, the flows of zonal and eddy
|     | Z E | Z   | E   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
APEandKacrosstheboundaries. ThetermsBΦ andBΦ arerepresentedtogetherwith
|     |     |     |     |     | Z   | E   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thetermsC andC , respectively, becausebotharisefromthesameprocessofderivingthe
Z E

72
Chapter2.TheoreticalBackground
balances of K and K . Muench (1965) recognizes the difficulty in interpreting the terms
Z E
BΦ and BΦ , indicating that they are related to the flow of kinetic energy towards
Z E
lower altitudes, representing the emergence of kinetic energy at the boundaries of the
computational domain.
Figure 2.18: Energy cycle as formulated by Lorenz (1955) and updated by Muench (1965).
This diagram includes additional terms representing energy flows across boundaries, illus-
trating both the local derivatives of the zonal and eddy partitions of APE and K and the
interactions at the system edges.
Although Muench’s model considers boundary flows, his domain was partially open,
extending up to the polar regions and encompassing the entire Northern Hemisphere longi-
tudinally, with the only boundary at the southern part of the domain at 30◦N. The notion
of a fully regional energy cycle was later approached by Smith (1969), who aimed to assess
the contribution of a limited region to global energetics. Smith clarified that while his work
presented a framework for regional analysis, an exact computation of local energetics was
outside its scope, and his model did not differentiate between zonal and eddy components
of APE and K.
Parallel to the work by Smith (1969), Johnson (1970), following the theoretical fra-
meworkproposedbyDuttonandJohnson(1967), introducedasemi-Lagrangianframework
for analyzing the energy cycle of limited areas. In this formulation, the delineated area
for performing energetic calculations moves with the meteorological system of interest,
spanning N fixed regions that shift in space. This analysis highlights that global Available
Potential Energy (APE) is the aggregate of all possible open atmospheric regions, plus a

73
Section2.4.AtmosphereEnergetics
term representing the thermodynamic contrast among these regions. It’s crucial to note
that Smith (1969) and Dutton and Johnson (1967) argued that the APE of a limited re-
gion should be viewed as its contribution to the global energetics rather than a standalone
quantity. This perspective stems from the interconnected nature of the atmosphere, where
local and global energetics are mutually influential.
Dutton and Johnson (1967) also critiqued Lorenz (1955)’s formulation, pointing out
its underestimation of APE, particularly during the winter months. The alternative set
of equations introduced by Johnson (1970), which utilizes isentropic coordinates, howe-
ver, included simplifications that were seen as limitations by Vincent and Chang (1973),
such as neglecting the impact of diabatic heating, rendering it impractical for diagnostic
applications. Following this rationale, Vincent and Chang (1973) developed a system of
equations in isobaric coordinates that account for the balances of APE and Kinetic Energy
(K) in an open atmospheric system from a semi-Lagrangian perspective.
This formulation partitions APE into the reference state APE of the region and two
components representing barotropic and baroclinic contributions to the APE of the deline-
ated area. The balance equations for APE now included terms for boundary movement in
the semi-Lagrangian frame and the advection of air masses with varying properties across
these boundaries. This formulation was first applied by Edmon and Vincent (1979) in an
energy cycle analysis of Hurricane Carmen (1974). Building on this, Brennan and Vincent
(1980) adapted Vincent’s approach to incorporate zonal and eddy components of APE and
K, marking the first instance of such a detailed and realistic equation set being applied
to a limited are within the troposphere. However, Brennan and Vincent (1980) utilized a
traditional Eulerian approach for their energy analysis.
Furthermore, Brennan and Vincent (1980) reinterpreted the boundary terms BΦ and
Z
BΦ as the work done by zonal and meridional wind components against atmospheric
E
pressure at the computational domain boundaries. However, they noted that these terms,
as calculated, were unrealistically large due to minor errors in the geopotential height field,
which could escalate in major errors and significantly skew the results. Consequently, these
terms were combined with the dissipation terms (D and D ) and treated as residuals in
Z E
the balance equations for K and K , resulting in new terms RK and RK . This
Z E Z E
approach and the updated energy cycle are depicted in Figure 2.19.
The modified energy balance equations are as follows:

| 74  |     |     | Chapter2.TheoreticalBackground |     |     |
| --- | --- | --- | ------------------------------ | --- | --- |
Figure 2.19: Updated energy cycle as reformulated by Brennan and Vincent (1980). This
diagram includes the integrated terms for boundary energy flows (BΦ Z and BΦ E ) merged
with dissipation processes (D Z and D E ), represented as residual terms RK Z and RK E .
∂A
Z
|     |     |     | = −C −C | +G +BA | (2.14) |
| --- | --- | --- | ------- | ------ | ------ |
|     |     | ∂t  | A       | Z Z Z  |        |
∂A
|     |     | E   | = C −C | +G +BA | (2.15) |
| --- | --- | --- | ------ | ------ | ------ |
|     |     |     | A      | E E E  |        |
∂t
∂K
|     |     | Z   | = C +C | +BK +RK | (2.16) |
| --- | --- | --- | ------ | ------- | ------ |
|     |     |     | K      | Z Z Z   |        |
∂t
∂K
E
|     |     |     | = −C | +C +BK +RK | (2.17) |
| --- | --- | --- | ---- | ---------- | ------ |
|     |     |     | K    | E E E      |        |
∂t
| And the residual | terms | are defined | as:  |       |        |
| ---------------- | ----- | ----------- | ---- | ----- | ------ |
|                  |       |             | RK = | BΦ +D | (2.18) |
|                  |       |             | Z    | Z Z   |        |
|                  |       |             | RK = | BΦ +D | (2.19) |
|                  |       |             | E    | E E   |        |
Robertson and Smith (1983) adapted the formulation presented by Brennan and Vin-
cent (1980) for limited area domains, particularly revising the term A . Building upon
E
the framework of APE for limited domains outlined by Smith et al. (1977), Robertson in-
tegrates the first law of thermodynamics into the Eulerian derivatives of the APE and A
Z
formulations. This results in a significantly different balance equation for A , introducing
E
a novel term associated with variations in the reference pressure field, which alters the

|     |     | Section2.4.AtmosphereEnergetics |     |     |     | 75  |
| --- | --- | ------------------------------- | --- | --- | --- | --- |
computation of the conversion term C . This approach was driven by the goal of evalu-
A
ating, through numerical modeling, the influence of moist processes on the energetics of
extratropical cyclones. However, the adaptation necessitated computations over isentropic
coordinates, introducing complexities in the numerical implementation.
In an effort to analyze the energetics of cyclogenesis in the Gulf of Genoa within the
Mediterranean Sea, Michaelides (1987) advanced the energy cycle formulation further.
Echoing concerns from Brennan and Vincent (1980) regarding unrealistic results for the
terms BΦ and BΦ , Michaelides introduced additional residual terms RK and RK ,
| Z   | E   |     |     |     | Z   | E   |
| --- | --- | --- | --- | --- | --- | --- |
and a correction factor (ϵ) to account for numerical errors in the estimation of these terms,
as shown in the equations and Figure 2.20. The modified set of equations is as follows:
∂A
Z
|     |     | = C | −C +BA +∆G |     |     | (2.20) |
| --- | --- | --- | ---------- | --- | --- | ------ |
|     |     |     | K A Z      | Z   |     |        |
∂t
∂A
E
|     |     | = C | −C +BA +∆G |     |     | (2.21) |
| --- | --- | --- | ---------- | --- | --- | ------ |
|     |     | ∂t  | A E E      | E   |     |        |
∂K
|     |     | Z = C | −C +BK −∆R |     |     | (2.22) |
| --- | --- | ----- | ---------- | --- | --- | ------ |
|     |     |       | K Z Z      | Z   |     |        |
∂t
∂K
|     |     | E = C | −C +BK −∆R |     |     | (2.23) |
| --- | --- | ----- | ---------- | --- | --- | ------ |
|     |     |       | E K E      | E   |     |        |
∂t
| Where the | residual terms | are defined | as:        |     |     |        |
| --------- | -------------- | ----------- | ---------- | --- | --- | ------ |
|           |                | ∆R          | = BΦ −D +ϵ |     |     | (2.24) |
|           |                | Z           | Z Z KZ     |     |     |        |
|           |                | ∆R          | = BΦ −D +ϵ |     |     | (2.25) |
|           |                | E           | E E KE     |     |     |        |
|           |                | ∆G          | = G +ϵ     |     |     | (2.26) |
|           |                | Z           | Z GZ       |     |     |        |
|           |                | ∆G          | = G +ϵ     |     |     | (2.27) |
|           |                | E           | E GE       |     |     |        |
In Michaelides et al. (1999), the author extends the energetic formulations presented in
Michaelides (1987), exploring calculations for limited areas using both Eulerian and semi-
Lagrangian reference frames. This study evaluates the energy cycle during a cyclogenesis
event in the Mediterranean from these two perspectives, providing a nuanced discussion
on the methodological implications of each. It highlights that the Eulerian approach is
commonly preferred for energy analysis in limited atmospheric areas. This method neces-
sitates defining a sufficiently large spatial domain to encapsulate all developmental stages

76
Chapter2.TheoreticalBackground
Figure2.20: RefineddepictionoftheenergycycleincorporatingmodificationsbyMichaelides
(1987). This representation includes error correction terms within the residual balances,
addressing previous challenges with the quantification of boundary terms and dissipation
factors.
of the system, including its movement and size changes. However, this approach has inter-
pretative limitations; a broad spatial domain may inadvertently include adjacent synoptic
circulations, thus diluting the specific energetics of the primary system under study.
Figure 2.21 illustrates this issue with a scenario akin to cyclogenesis in the coastal
region of Southeast Brazil (Reboita et al., 2010; Gramcianinov et al., 2019, e.g.,). Here,
the computational domain must encompass both the initial coastal genesis area and the
subsequent oceanic trajectory of the cyclone. As the cyclone progresses to the ocean in its
later stages, mesoscale circulations near the coast, such as updrafts due to surface heating
andconvectionfromseabreezeinteractionswithlocaltopography,emerge. Theseprocesses
can significantly alter the computed values of APE and K within the domain, affecting the
energy conversion, boundary, dissipation, and generation terms, thereby complicating the
interpretation of the cyclone’s energy dynamics.
Despite the inherent limitations associated with the Eulerian approach, Michaelides
et al. (1999) discusses the methodological challenges of employing a purely Lagrangian
framework to study extratropical cyclones. Such a study would require tracking the system
in a three-dimensional space, isolated from external influences, using specific conservative
variables for the encapsulated air masses. This is complicated by the diverse origins of
the air masses involved in extratropical cyclones, which include both polar and tropical

77
Section2.4.AtmosphereEnergetics
L
A
B
L
Figure 2.21: Illustration of challenges in using an Eulerian reference frame for energy cycle
analysis. A) A cyclone forming near the continent, where the newly developed cyclonic
system is the main meteorological feature inside the domain. B) The system is in its later
oceanic phase, while meso-scale circulations develop in the coastal region, such sea-breeze
and, consequently, orographic ascent over the mountain range near the coast.
sources, affecting their conservative properties. Additionally, the system must be isolated
from any spurious external circulations.
Consequently, Michaelides et al. (1999) advocates for a quasi-Lagrangian approach as
a practical solution that minimizes the impact of neighboring circulations on the system’s
energy dynamics. This approach, similar to that proposed by Vincent and Chang (1973),
utilizes multiple fixed domains at different temporal intervals to effectively track the cyclo-
nic system. However, unlike Vincent and Chang (1973), Michaelides et al. (1999)’s formu-
lation does not include terms for the displacement of computational domain boundaries.
The author conducts a comparative analysis between the Eulerian and quasi-Lagrangian
methods, revealing that they can yield significantly different results depending on the spe-
cific energetic terms analyzed. This highlights the complications in using the Eulerian
method for comparative studies, as it can incorporate the energetic contributions of adja-
cent systems. Michaelides et al. (1999) concludes that the semi-Lagrangian method offers
a more robust framework for analyzing the energetics of cyclonic systems.
Nevertheless, critiques of the quasi-Lagrangian approach exist (Dias Pinto and Rocha,

78
Chapter2.TheoreticalBackground
2011, e.g.). One major criticism is that this method does not allow for the local time
derivatives of energy terms due to the absence of a fixed computational volume, which
impedes a complete closure of the energy balance — a limitation acknowledged by Micha-
elides et al. (1999). Additionally, there is debate over whether changes in the energetics
through the cyclone lifecycle can be attributed to the system’s dynamics or to the fact that
the tracking box may capture varying environmental conditions. However, these perceived
limitations can be addressed by understanding that the distinct boxes used at each time-
step through the cyclone’s lifecycle are effectively ”snapshots”of its dynamics. Consider
the following thought experiment: we compute the LEC using both quasi-Lagrangian and
Eulerian frameworks. The quasi-Lagrangian experiment tracks the trajectory of an extra-
tropical cyclone, using a distinct 15◦ ×15◦ domain for each hourly time step. Meanwhile,
the Eulerian experiment employs a fixed 15◦×15◦ domain in a specific location, which will
coincide with the cyclone’s trajectory at a given time step, thereby exactly matching the
domain used in the quasi-Lagrangian framework. As demonstrated in Section 2.4.2, the
equations used in LEC computation do not have temporal dependencies; therefore, for this
specific time where the domains of both frameworks overlap, the results will be identical.
At this time step, the quasi-Lagrangian domain likely contains only the cyclonic system,
thus the computed energetics are indisputably linked to its development at that moment
— or, using Smith (1969)’s interpretation: the system’s contribution to global energetics.
Following this reasoning, it is logical to assume that each domain in the quasi-Lagrangian
approach represents the cyclone energetics for each specific time step, effectively providing
snapshots of the energetics.
Severalmethodologieshavebeendevelopedtorefinediagnosticequationsforatmosphe-
ric energetics, each offering unique advancements. The approach introduced by Plumb
(1983) critiques traditional energy formulations for wave propagation and employs trans-
formed Eulerian-mean equations to enhance the physical accuracy of eddy-mean flow inte-
ractions. Similarly, Marquet (1991)’s redefinition of exergy and available enthalpy provides
a more complete analysis of atmospheric dynamics, accommodating factors such as static
instabilitiesandtopographicalvariationsoftenoversimplifiedinpreviousmodels. Thelocal
APE density framework proposed by Novak and Tailleux (2018), on the other hand, intro-
duces a positive-definite local form of potential energy, akin to kinetic energy, which can
be transported, converted, and dissipated locally. Unlike the global and volume-integrated

79
Section2.4.AtmosphereEnergetics
(A) (B)
e e
d d
u u
t t
ti ti
a a
L L
Longitude Longitude
(C) (D)
Y Y
m 0 m 0
r r
e e
t t
n n
o o
si si
r r
e e
v v
n n
o o
C C
T T
0 Time 0 Time
Figure 2.22: Illustration of the quasi-Lagrangian and Eulerian frameworks employed in the LEC compu-
tation for analyzing cyclonic energetics. Panel (A) shows the Eulerian approach with a fixed 15◦ ×15◦
domain, overlapping with the cyclone’s trajectory at a specific time step (T ). Panel (B) depicts the
0
quasi-Lagrangian approach, tracking a 15◦ ×15◦ domain that moves with the cyclone, providing hourly
snapshots. The highlighted domain in Panel (B) indicates the domain at T that overlaps with the Eu-
0
lerian domain from Panel (A). Panels (C) and (D) display a hypothetical conversion term used solely for
demonstrating that both frameworks yield identical results (Y ) when the domains coincide. This align-
0
ment supports theargument thateach quasi-Lagrangiandomainsnapshot accuratelyreflects the system’s
energetics at each respective time step.
nature of Lorenz’s APE, this local APE density theory adapts potential energy calculati-
ons to specific atmospheric conditions, enhancing diagnostic precision in regional climate
studies. However, these methods significantly complicate the mathematical formulations,
requiring increased computational resources and extending computation times, which pose
substantial limitations, especially for operational purposes. Additionally, each of these
frameworks introduces new challenges in the physical interpretation of the terms.
The present work adopts the formulation presented by Michaelides et al. (1999), which
offers a balance between computational feasibility and physical accuracy. This framework
provides results that serve as a useful diagnostic tool, facilitating an understanding of

| 80  |     |     | Chapter2.TheoreticalBackground |     |     |     |     |     |
| --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
the dynamical mechanisms involved in cyclone development without requiring extensive
computational resources. While the primary goal of this thesis is scientific, there is
significant interest in developing an operational tool for diagnosing the energy cycle of
cyclones that can be made available to the scientific community. This tool is envi-
sioned to function similarly to the Hart phase diagrams, which are accessible online
(https://moe.met.fsu.edu/cyclonephase/ecmwf/fcst/index.html) and widely used for real-
time cyclone analysis. The complete mathematical formulation and physical interpretation
of each term in the Lorenz Energy Cycle (LEC) are detailed in Section 2.4.2. Additionally,
Section 3.4 describes the computational methods used to calculate the LEC.
2.4.2 Lorenz Energy Cycle: Mathematical expressions and physical interpretation
This section provides a detailed description of the symbols and expressions used for the
calculation of the Lorenz Energy Cycle (LEC), adopting the notation from Michaelides
(1987).
Firstly, we define the zonal mean of a variable X, between longitudes λ and λ :
1 2
|     |     |     |     |       | 1    | (cid:90) λ1 |     |        |
| --- | --- | --- | --- | ----- | ---- | ----------- | --- | ------ |
|     |     |     |     | [X] = |      | Xdλ         |     | (2.28) |
|     |     |     |     | λ     | λ −λ |             |     |        |
|     |     |     |     |       | 2    | 1           |     |        |
λ2
The eddy component of this variable is its deviation from the zonal mean:
|     |     |     |     | (X) | = X | −[X] |     | (2.29) |
| --- | --- | --- | --- | --- | --- | ---- | --- | ------ |
|     |     |     |     |     | λ   | λ    |     |        |
The domain mean of the variable X, defined over the computational domain bounded
| by longitudes | λ   | and λ , and | latitudes | ϕ                | and   | ϕ , is given     | by:       |        |
| ------------- | --- | ----------- | --------- | ---------------- | ----- | ---------------- | --------- | ------ |
|               | 1   | 2           |           |                  | 1     | 2                |           |        |
|               |     | (cid:18)    |           | (cid:19)(cid:18) |       | (cid:19)(cid:90) |           |        |
|               |     |             | 1         |                  | 1     |                  | λ1        |        |
|               |     | [X] =       |           |                  |       |                  | Xcosϕdλdϕ | (2.30) |
|               |     | λϕ          | λ −λ      | sinϕ             | −sinϕ |                  |           |        |
|               |     |             | 2         | 1                | 2     | 1                |           |        |
λ2
Similarly, we define the deviation of the zonal mean from the domain mean:
|     |     |     |     | ([X] ) | = [X] | −[X] |     | (2.31) |
| --- | --- | --- | --- | ------ | ----- | ---- | --- | ------ |
|     |     |     |     | λ ϕ    |       | λ    | λϕ  |        |
From the definitions above, the four energy components used in the LEC computation
| are defined | as follows: |     |     |     |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |

|     |     | Section2.4.AtmosphereEnergetics |     |     | 81  |
| --- | --- | ------------------------------- | --- | --- | --- |
(cid:90)
|     |     |     | p b ([(T) | ])2 ] |     |
| --- | --- | --- | --------- | ----- | --- |
λ ϕ λϕ
|     |     | A   | =   | dp  | (2.32) |
| --- | --- | --- | --- | --- | ------ |
Z 2[σ]
|     |     |     | pt  | λϕ  |     |
| --- | --- | --- | --- | --- | --- |
(cid:90) p
|     |     |     | b [(T)2] | ]     |        |
| --- | --- | --- | -------- | ----- | ------ |
|     |     | A   | = λ      | λϕ dp | (2.33) |
E
2[σ]
|     |     |     | pt λϕ                   |     |     |
| --- | --- | --- | ----------------------- | --- | --- |
|     |     |     | (cid:90) p [[u]2 +[v]2] |     |     |
b
|     |     | K   | = λ | λ λϕ dp | (2.34) |
| --- | --- | --- | --- | ------- | ------ |
Z
2g
pt
|     |     |     | (cid:90) p [(u)2 | +(v)2] |        |
| --- | --- | --- | ---------------- | ------ | ------ |
|     |     |     | b                | λϕ     |        |
|     |     | K   | = λ              | λ dp   | (2.35) |
E
2g
pt
where p is the atmospheric pressure, with subscripts b and t denoting the lower (base)
and upper (top) pressure boundaries of the atmosphere, respectively. T represents tempe-
rature, g is the acceleration due to gravity, and u and v are the zonal and meridional wind
components, respectively. The static stability parameter σ is defined as:
|     |     |     | (cid:20) | (cid:21) |        |
| --- | --- | --- | -------- | -------- | ------ |
|     |     |     | gT pg∂T  |          |        |
|     |     | σ   | = −      |          | (2.36) |
|     |     |     | c R      | ∂p       |        |
|     |     |     | p        | λϕ       |        |
where c is the specific heat at constant pressure, and R is the ideal gas constant for
p
dry air.
The APE terms A and A are discussed in Section 2.4 and illustrated in Figure
|     |     | Z E |     |     |     |
| --- | --- | --- | --- | --- | --- |
2.16. The term A quantifies the latitudinal temperature gradient, where higher values
Z
in the numerator indicate larger differences in mean temperature between latitudes —
characteristically, the equator being warmer than the poles. Moreover, lower values of
the denominator suggest a more unstable atmosphere, which can more readily redistribute
vertical motions and thus intensify the latitudinal temperature gradients. The term A
E
is analogous to A but referring to longitudinal temperature gradients caused by eddy
Z
motions, suggesting a higher presence of eddy available potential energy, which can be
| converted | into kinetic | energy, driving | atmospheric | motions. |     |
| --------- | ------------ | --------------- | ----------- | -------- | --- |
ThekineticenergytermsK andK quantifytheintensityofatmosphericmotions. K
|     |     | Z   | E   |     | Z   |
| --- | --- | --- | --- | --- | --- |
correlates with the zonal mean of the wind components; opposing winds cancel out, thus
higher K values occur when winds at the same latitude align directionally. The term [u]λ
Z
denotes the large-scale east-west circulations, including the trade winds, westerlies, and jet
streams, while [v]λ relates to the north-south circulations, such as those in the Hadley and
polar cells. Higher K values therefore indicate stronger mean circulations, contributing to
Z
the overall momentum and energy in the atmospheric system. In contrast, (u)λ and (v)λ

82
Chapter2.TheoreticalBackground
represent deviations from these mean values, capturing smaller-scale, turbulent motions
and deviations from the average flow, including phenomena like cyclones, anticyclones, and
othermesoscaleandsynoptic-scaledisturbances. Thus, elevatedK valuessignalincreased
E
eddy activity, enhancing turbulence and mixing within the atmosphere.
The four conversion terms are defined as follows, integrating over the atmospheric
column from the base (p ) to the top (p ) pressures:
b t
(cid:90) p b R
C = −[([T] ) ([ω] ) ] dp (2.37)
Z λ ϕ λ ϕ λϕ gp
pt
(cid:90) p b R
C = −[(T) (ω) ] dp (2.38)
E λ λ λϕ
gp
pt
(cid:32) (cid:33)
(cid:90) p b 1 (cid:20) ∂([T] ) (cid:21) 1 (cid:20) ∂([T] ) (cid:21)
λ ϕ λ ϕ
C = − (v) (T) + (ω) (T) dp (2.39)
A λ λ λ λ
2aσ ∂ϕ σ ∂p
pt λϕ λϕ
(cid:32)
(cid:90) p b 1 (cid:20) cosϕ ∂ (cid:18) [u] (cid:19)(cid:21) (cid:20) (v)2 ∂[v] (cid:21)
C = (u) (v) λ + λ λ
K λ λ
g a ∂ϕ cosϕ a ∂ϕ
pt λϕ λϕ
(2.40)
(cid:33)
(cid:20) (cid:21) (cid:20) (cid:21) (cid:20) (cid:21)
tanϕ ∂[u] ∂[v]
+ (u)2[v] + (ω) (u) λ + (ω) (v) λ dp
a λ λ λ λ ∂p λ λ ∂p
λϕ λϕ λϕ
where a is the Earth’s radius and ω is the vertical velocity in isobaric coordinates.
The term C (Equation 2.38) shares some similarities with A , as it represents the
Z Z
covariance product of temperature and vertical motion, averaged over the same latitudinal
circle. Positive values of C indicate a conversion from zonal available potential energy
Z
(A ) to kinetic energy (K ), and vice versa. This conversion is detailed in the integrand,
Z Z
which contains the covariance product of the zonal deviation from the domain mean of
−Tω. Thus, positive values of C correspond to either the vertical ascent of warm air
Z
or the descent of cold air. Conversely, negative values of C are associated with the
Z
ascent of cold air or the descent of warm air. This phenomenon is depicted in Figure 2.23,
whichillustratesaregioncharacterizedbymeridionalgradientsoftemperatureandvertical
velocity. In warmer areas where the temperature deviation is positive and the ω deviation
is negative, the product Tω is negative. With the additional negative sign in the equation
for C , this results in positive values of C , signifying a conversion from A to K . On
Z Z Z Z
the other hand, in situations where air descends in warmer regions and ascends in colder
regions, the covariance product −Tω would be positive, leading to negative C values,
Z
indicating a conversion from kinetic energy (K ) to available potential energy (A ).
Z Z

|     |     | Section2.4.AtmosphereEnergetics |     |     | 83  |
| --- | --- | ------------------------------- | --- | --- | --- |
Figure 2.23 provides a visual interpretation of C , showing a region with meridional
Z
gradients of temperature and vertical velocity. In this scenario, the combination of positive
temperature deviations and negative ω deviations in warmer regions results in a negative
product of Tω, which when combined with the equation’s negative sign, yields a positive
C , indicative of energy conversion from A to K . Conversely, in colder regions where
| Z   |     |     | Z Z |     |     |
| --- | --- | --- | --- | --- | --- |
temperature deviations are negative and ω deviations are positive, the product is also
negative, leading to a positive C . In the reverse situation, where air descends in warmer
Z
areas and rises in colder ones, the product −Tω turns positive, resulting in a negative C ,
Z
| which signifies | a reverse energy | conversion | from K | to A . |     |
| --------------- | ---------------- | ---------- | ------ | ------ | --- |
|                 |                  |            | Z      | Z      |     |
The term C analogously represents the conversion between eddy forms of energy, from
E
available potential energy (A ) to kinetic energy (K ). The interpretation of C mirrors
|     |     | E   |     | E   | E   |
| --- | --- | --- | --- | --- | --- |
that of C , but it pertains to gradients and deviations along the longitudinal axis (x-axis)
Z
rather than the latitudinal (y-axis). Swapping the axes in Figure 2.23 would illustrate a
| scenario indicative | of a positive | C . |     |     |     |
| ------------------- | ------------- | --- | --- | --- | --- |
E
φ
|     | 1   |     |     | + ([T] ) |     |
| --- | --- | --- | --- | -------- | --- |
λ φ
- ([ω] )
|     | φ   |     |     | λ φ |     |
| --- | --- | --- | --- | --- | --- |
2
|     | φ   |     |     | + ([T] ) |     |
| --- | --- | --- | --- | -------- | --- |
λ φ
|     | 3   |     |     | - ([ω] ) |     |
| --- | --- | --- | --- | -------- | --- |
λ φ
φ
4
+ ([T] )
λ φ
|     | φ   |     |     | - ([ω] ) |     |
| --- | --- | --- | --- | -------- | --- |
|     | 5   |     |     | λ φ      |     |
φ - ([T] )
|     | 6   |     |     | λ φ |     |
| --- | --- | --- | --- | --- | --- |
+ ([ω] )
λ φ
φ
7
- ([T] )
|     | φ   |     |     | λ φ |     |
| --- | --- | --- | --- | --- | --- |
+ ([ω] )
|     | 8   |     |     | λ φ |     |
| --- | --- | --- | --- | --- | --- |
φ
9 - ([T] )
λ φ
+ ([ω] )
|     | φ   |     |     | λ φ |     |
| --- | --- | --- | --- | --- | --- |
10
|     | λ   | λ λ λ | λ λ |     |     |
| --- | --- | ----- | --- | --- | --- |
|     |     | 3     | 5   | 6   |     |
|     | 1   | 2     | 4   |     |     |
cold
warm
Figure2.23: Hypotheticalsituationillustratingtheconversiontermbetweenavailablepoten-
tial energy (A Z ) and kinetic energy (K Z ), represented by C Z . The y-axis represents latitude
circles (ϕ), showing a decrease in temperature and vertical velocity ω (indicated by vertical
arrows) toward the pole in the Southern Hemisphere. The x-axis represents longitude (λ).

84
Chapter2.TheoreticalBackground
The term C (Equation 2.39) describes the energy conversion between zonal mean
A
available potential energy (A ) and eddy available potential energy (A ). Positive values
Z E
of C signify energy transfer from A to A , whereas negative values indicate the opposite.
A Z E
The equation for C can be divided into two components, each capturing how deviations
A
from the zonal mean of the meridional (north-south) and vertical winds (addressed in the
first and second components, respectively) interact with latitudinal temperature gradients.
In the first component, we have (v) (T) ∂([T] λ )φ. The negative sign within the equation
λ λ ∂φ
implies that for C to be positive, this term must be negative. To understand each term’s
A
contribution to the sign of C , consider an illustrative case: a midlatitude low-pressure
A
system in the Southern Hemisphere with a cold front propagating west to the system and a
warm front east (Figure 2.24. In the cold front region, (v) is positive (northward), (T) is
λ λ
negative(cooler),and ∂([T]λ)φ ispositive(temperatureincreasesequator-ward). Conversely,
∂φ
in the warm front region, (v) is negative (southward), (T) is positive (warmer), and
λ λ
∂([T] λ )φ remains positive. This configuration is consistent across both hemispheres when
∂φ
accounting for the appropriate directional changes in wind and temperature gradient.
The second component, (ω)λ(T)λ∂([T]λ)φ, must also be negative to contribute positively
∂p
to C . The term ∂([T]λ)φ reflects the zonal average atmospheric lapse rate, which typically
A ∂p
presents as negative over the cold air mass between ϕ and ϕ and between λ and λ ,
3 6 1 3
indicating an increase in temperature with height. Above this level, the lapse rate reverses.
In contrast, across the rest of the domain, particularly behind the warm front, this lapse
rate term is positive. Consequently, when averaged across the domain and integrated over
vertical levels, the overall contribution of this term tends to be positive. Furthermore, in
the area behind the warm front, where (ω)λ is negative (indicating ascending air) and (T)λ
is positive (indicating warmer air), the product (ω)λ(T)λ is negative. This, in turn, results
in a positive contribution to C , aligning with the term’s requirement for a negative input
A
to yield a positive output.
This analysis shows how an extratropical cyclone can influence global energetics. By
transforming meridional into zonal temperature gradients, C converts zonal APE into
A
eddy APE. The described scenarios are generalizations and do not capture all atmospheric
variations during frontal passages; however, they do reflect significant energetic contribu-
tions, especially at lower atmospheric levels. Additionally, it is important to note that the
signs of the first and second components of C do not need to match; C will be positive
A A

Section2.4.AtmosphereEnergetics 85
(A) warm
φ
1
φ 2
φ
3
φ
|     |     | 4   | L   |     |     |
| --- | --- | --- | --- | --- | --- |
φ
5
φ
6
cold
|     |     | λ   | λ λ λ | λ λ | λ λ |
| --- | --- | --- | ----- | --- | --- |
|     |     | 1   | 2 3 4 | 5 6 | 7 8 |
(B)
φ
1
φ 2
|     |     | + (v) | λ   |     | - (v) λ |
| --- | --- | ----- | --- | --- | ------- |
φ
3
|     |     | - (T) |     |     | + (T) |
| --- | --- | ----- | --- | --- | ----- |
|     |     |       | λ   |     | λ     |
φ
4
|     |     | + (ω) |     |     | - (ω) λ |
| --- | --- | ----- | --- | --- | ------- |
|     | φ   |       | λ   |     |         |
5
φ
6
|     |     | λ   | λ λ λ | λ λ | λ λ |
| --- | --- | --- | ----- | --- | --- |
|     |     | 1   | 2 3 4 | 5 6 | 7 8 |
Figure2.24: RepresentationoftheconversionprocessbetweenA andA . (A)Illustrationofanidealized
Z E
situation of a midlatitude low-pressure system in the Southern Hemisphere, with a cold front propagating
west and a warm front east. (B) Analysis of the variables involved in the formula for C (Equation
A
2.39). The y-axis represents latitude circles (ϕ), and the x-axis represents longitude (λ). In the Southern
| Hemisphere, | latitude decreases | from ϕ to | ϕ . |     |     |
| ----------- | ------------------ | --------- | --- | --- | --- |
|             |                    | 1         | 6   |     |     |
if the magnitude of the negative component exceeds that of the positive component.
The last conversion term, C (Equation 2.40), represents the conversion of kinetic
K
energy from eddies to the zonal mean state. Positive values indicate an energy transfer
from K (eddy kinetic energy) to K (zonal kinetic energy), and vice versa. This term’s
|     | E   |     | Z   |     |     |
| --- | --- | --- | --- | --- | --- |
formulation is more complex than others, comprising five distinct components: 1) meridi-
onal advection of zonal momentum, 2) meridional shear of meridional wind, 3) interaction
of eddy zonal wind with zonal meridional wind, 4) vertical advection of zonal momentum,
| and 5) | vertical advection | of meridional | momentum. |     |     |
| ------ | ------------------ | ------------- | --------- | --- | --- |
For simplicity, in analyzing the first term—meridional advection of zonal momen-
tum—we consider (u) , (v) , and ∂[u] λ, omitting variables related to the transformation
λ λ
∂ϕ
from Cartesian to spherical coordinates. Consider a purely zonal westerly jet (Figure

86 Chapter2.TheoreticalBackground
∂[u]
2.25a), where as latitude decreases from ϕ to ϕ , λ transitions from negative in the
1 10 ∂ϕ
northern part of the domain to positive in the southern part. However, both v and (u)
λ
are null in this scenario. Similarly, for a purely meridional northerly jet (Figure 2.25b),
∂[u]
(v) varies from negative to positive across the domain, but (u) and λ remain null.
| λ   |     |     | λ   | ∂ϕ  |
| --- | --- | --- | --- | --- |
Therefore, averaged over the entire domain, this term is null for both scenarios.
| (A) |     | (B) +(v)λ | -(v)λ +(v)λ |     |
| --- | --- | --------- | ----------- | --- |
higher
wind
| φ   |     | φ   |     | speeds |
| --- | --- | --- | --- | ------ |
| 1   |     | 1   |     |        |
| φ 2 |     | φ 2 |     |        |
| φ   |     | φ   |     |        |
| 3   |     | 3   |     |        |
| φ   |     | φ   |     |        |
| 4   |     | 4   |     |        |
| φ   |     | φ   |     |        |
| 5   |     | 5   |     |        |
| φ 6 |     | φ 6 |     |        |
| φ   |     | φ   |     |        |
| 7   |     | 7   |     |        |
| φ   |     | φ   |     |        |
| 8   |     | 8   |     |        |
| φ   |     | φ   |     |        |
| 9   |     | 9   |     |        |
| φ   |     | φ   |     | lower  |
| 10  |     | 10  |     |        |
wind
| λ λ | λ λ λ λ | λ λ | λ λ λ λ   | speeds |
| --- | ------- | --- | --------- | ------ |
| 1 2 | 3 4 5 6 | 1   | 2 3 4 5 6 |        |
Figure 2.25: Illustration of (A) a zonal westerly jet and (B) a meridional northerly jet in the Southern
Hemisphere. The y-axis represents the latitude circles (ϕ) and the x-axis represents longitude (λ).
In situations where small instabilities arise in the zonal or meridional flow, they may
initiate the development of larger instabilities. For example, consider a zonal jet becoming
unstable with a cyclonic (clockwise) deviation in its flow at the southern part of the
∂[u]
domain (Figure 2.26a). Similarly as in a purely zonal jet, λ exhibits negative values in
∂ϕ
the northern part of the domain and positive values in the southern part (Figure 2.26b).
With the onset of instability, (v) and (u) are no longer null across the domain: they
λ λ
are negative on the eastern flank and positive on the western flank of the perturbation.
This leads to a positive contribution to C from the first term, indicating that the eddy
K
is transferring energy to the zonal flow and thus depleting its own energy over time.
(v)2∂[v]
The second term in C - meridional shear of meridional wind - contains λ. It is
|     | K   |     |     | λ ∂ϕ |
| --- | --- | --- | --- | ---- |
evident that (v)2 is null for purely zonal jets, but otherwise is always positive, hence ∂[v] λ
λ
∂ϕ
dictates this term’s contribution to the signal of C . While ∂[v] λ is typically null for purely
K
∂ϕ
zonal and meridional jets, its contribution becomes significant for small instabilities in the
zonal flow. For the eddy development illustrated in Figure 2.26a, as |v| decreases from the
western to the eastern flank of the perturbation, [u] < 0, so ∂[v] λ > 0, making this term’s
∂ϕ
| contribution to C positive. |     |     |     |     |
| --------------------------- | --- | --- | --- | --- |
K

|        |     |     |     | Section2.4.AtmosphereEnergetics |     |     |     |     | 87  |
| ------ | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
| higher | (A) |     |     | (B)                             |     |     | (C) |     |     |
| wind   | φ   |     |     | φ                               |     |     | φ   |     |     |
| speeds | 1   |     |     | 1                               |     |     | 1   |     |     |
|        | φ 2 |     |     | φ 2                             |     |     | φ 2 |     |     |
|        | φ   |     |     | φ                               |     |     | φ   |     |     |
|        | 3   |     |     | 3                               |     |     | 3   |     |     |
|        | φ   |     |     | φ                               |     |     | φ   |     |     |
|        | 4   |     |     | 4                               |     |     | 4   |     |     |
|        | φ 5 |     |     | φ 5                             |     |     | φ 5 |     |     |
|        | φ   |     |     | φ                               |     |     | φ   |     |     |
|        | 6   |     |     | 6                               |     |     | 6   |     |     |
|        | φ   |     |     | φ                               |     |     | φ   |     |     |
|        | 7   |     |     | 7                               |     |     | 7   |     |     |
|        | φ   |     |     | φ                               |     |     | φ   |     |     |
|        | 8   |     |     | 8                               |     |     | 8   |     |     |
|        | φ 9 |     |     | φ 9                             |     |     | φ 9 |     |     |
|        | φ   |     |     | φ                               |     |     | φ   |     |     |
| lower  | 10  |     |     | 10                              |     |     | 10  |     |     |
wind
| speeds |     | λ λ λ | λ λ λ |     | λ λ λ | λ λ λ | λ λ | λ λ λ λ |     |
| ------ | --- | ----- | ----- | --- | ----- | ----- | --- | ------- | --- |
|        |     | 1 2 3 | 4 5 6 |     | 1 2 3 | 4 5 6 | 1 2 | 3 4 5 6 |     |
Figure 2.26: (A) Illustration of an eddy developing in the southern part of a purely meridional jet, (B)
signalanalysisforthefirst,(C)fourthandfifthtermsofC (Equation2.40),forthisscenario. They-axis
K
| represents | the | latitude circles | (ϕ) and | the | x-axis represents | longitude | (λ). |     |     |
| ---------- | --- | ---------------- | ------- | --- | ----------------- | --------- | ---- | --- | --- |
The third term - interaction of eddy zonal wind with zonal meridional wind - contains
| (u)2[v] |     | (u)2 |     |     |     |     |     |     |     |
| ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
. Both and [v] are null for purely zonal jets. However, similar to the previous
| λ   | λ   | λ   | λ   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
terms, their combined signal can be investigated for perturbations in the zonal flow. As
(u)2 is invariably positive, the signal of this term is influenced by [v] . In the situation
| λ   |     |     |     |     |     |     |     | λ   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
depicted in Figure 2.26a, [v] < 0 leads to a negative contribution of this term to C .
|     |     |     | λ   |     |     |     |     |     | K   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
For the fourth and fifth terms - vertical advection of zonal and meridional momentum,
respectively - the analysis is more complex due to the three-dimensional variations in
∂[u]
wind throughout the troposphere. The fourth term involves (ω) (u) λ, while the fifth
|     |     |     |     |     |     |     | λ   | λ ∂p |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
∂[v]
includes (ω) (v) λ. In scenarios of purely zonal jets, both terms are null, but they
|        | λ           | λ ∂p |               |     |        |             |     |     |     |
| ------ | ----------- | ---- | ------------- | --- | ------ | ----------- | --- | --- | --- |
| become | significant | with | perturbations |     | in the | zonal flow. |     |     |     |
∂[u]
Specifically, at mid-latitudes, we can assume that λ is generally negative ([u] incre-
∂p
ases with height) in the troposphere. However, in the scenario illustrated in Figure 2.26a,
where the flow intensifies on the eastern flank of a perturbation, [u] becomes negative
λ
∂[u]
(westward), making λ > 0 (Figure 2.26c). Additionally, if the jet is at a higher altitude
∂p
(e.g., 250 hPa), the convergence caused by the perturbation results in descending air, thus
(ω) is positive. These conditions render the contribution of this term to C negative.
| λ   |     |     |     |     |     |     |     | K   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂[v]
The analysis for the fifth term follows similarly, where λ > 0, (u) > 0, and (ω) > 0
|     |     |     |     |     |     |     | ∂p  | λ   | λ   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Figure 2.26c), resulting in a negative contribution for this term to C .
K
Collectively, the first two terms contribute positively to C while the last three terms
K
provide negative contributions. Thus, the terms that, when summed, present the highest
magnitude, will dictate the overall signal for C . It is essential to recognize that the
K

| 88  |     |     | Chapter2.TheoreticalBackground |     |     |     |     |     |
| --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
illustrative examples provided - zonal and meridional flows and a perturbation developing
in the zonal flow - are simplifications of atmospheric motion. They are not intended to
present a comprehensive picture of all conditions under which conversion between K and
Z
K might occur but serve as guiding thought experiments to aid understanding of this
E
conversion in real atmospheric motions. To the author’s knowledge, due to the complexity
of such analysis, no comprehensive attempt has been made previously in the literature.
| The | APE generation | and | K dissipation |       | terms  | are    | defined as: |        |
| --- | -------------- | --- | ------------- | ----- | ------ | ------ | ----------- | ------ |
|     |                |     | (cid:90) p    | [([q] | ) ([T] | ) ]    |             |        |
|     |                |     |               | b λ   | ϕ      | λ ϕ λϕ |             |        |
|     |                | G   | =             |       |        | dp     |             | (2.41) |
Z
c [σ]
|     |     |     | pt  |     | p λϕ |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |
(cid:90)
|     |     |     | p   | b [(q) (T) | ]    |     |     |        |
| --- | --- | --- | --- | ---------- | ---- | --- | --- | ------ |
|     |     |     |     | λ          | λ λϕ |     |     |        |
|     |     | G   | =   |            |      | dp  |     | (2.42) |
|     |     | E   |     | c [σ]      |      |     |     |        |
|     |     |     | pt  | p          | λϕ   |     |     |        |
(cid:90) p
b 1
|     |     | D   | = − | [[u] | [F  | ] +[v] | [F ] ] dp | (2.43) |
| --- | --- | --- | --- | ---- | --- | ------ | --------- | ------ |
|     |     | Z   |     |      | λ λ | λ      | λ ϕ λ λϕ  |        |
g
pt
(cid:90)
p b 1
|     |     | D   | = − | [(u) | (F  | ) +(v) | (F ) ] dp | (2.44) |
| --- | --- | --- | --- | ---- | --- | ------ | --------- | ------ |
|     |     | E   |     | g    | λ   | λ λ    | λ ϕ λ λϕ  |        |
pt
Here, F and F represent the zonal and meridional frictional components, respecti-
|     | λ ϕ |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
vely, and q is the diabatic heating term, computed as a residual from the thermodynamic
equation:
q ∂T
|     |     |     |     |     | ⃗   | ⃗    |      |        |
| --- | --- | --- | --- | --- | --- | ---- | ---- | ------ |
|     |     |     |     | =   | −V  | ·∇ T | −S ω | (2.45) |
|     |     |     | c   | ∂t  | H   | p    | p    |        |
p
⃗ ⃗
where −V ·∇ T represents the horizontal advection of temperature and S approxi-
|           | H p               |       |     |     |     |     | p   |     |
| --------- | ----------------- | ----- | --- | --- | --- | --- | --- | --- |
| mates the | static stability, | given | by: |     |     |     |     |     |
T ∂θ
|       |                    |     |              | S   | ≡ − |      |     | (2.46) |
| ----- | ------------------ | --- | ------------ | --- | --- | ---- | --- | ------ |
|       |                    |     |              |     | p   | θ ∂p |     |        |
| where | θ is the potential |     | temperature. |     |     |      |     |        |
The terms G and G functionally resemble A and A , respectively. The variable
|     | Z   | E   |     |     |     | Z   | E   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
q quantifies the heat added to or removed from an air parcel through external sources
such as radiation, latent heat release (e.g., condensation), and sensible heat exchange
(e.g., conduction from the surface). The variable σ represents the overall stratification
of the atmosphere. Generation of G or G occurs when anomalous heating aligns with
|     |     |     |     | Z   | E   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
regions of anomalously high temperature, and anomalous cooling coincides with regions of
anomalously low temperature. If the temperature/heating gradients are meridional (e.g.,

89
Section2.4.AtmosphereEnergetics
differential heating from the equator to the poles), G is generated. Conversely, if the
Z
gradients are within the same latitude belt (e.g., differential heating between ocean and
land), G is generated. Additionally, higher static stability, indicating a more stratified
E
atmosphere, reduces the efficiency of APE generation, while lower static stability enhances
it. Maximum generation of APE is analogous to the situation illustrated in Figure 2.24.
The terms D and D represent the dissipation of kinetic energy from the zonal mean
Z E
stateandtheeddies, respectively. ThevariableF denotesthefrictionalforcesactingonthe
wind, which includes elements such as surface drag and turbulent friction. These frictional
forces, notably surface drag and turbulent friction within the boundary layer, oppose the
wind direction, causing a reduction in wind speed and consequently dissipating kinetic
energy. Additionally, D and D can also represent energy exchanges between different
Z E
scales, specifically the transfer of energy from the grid scale to the subgrid scale. These
forces not only convert kinetic energy into thermal energy but also facilitate the transfer
of energy to smaller scale motions, thereby contributing to the overall energy dissipation
within the atmospheric system.
The boundary terms are given by:

90
Chapter2.TheoreticalBackground
(cid:90) p2 (cid:90) φ2 1 (cid:16)
(cid:0) (cid:1)2
(cid:17)λ2
BAZ = c 2([T] ) (T) u+ [T] u
1 2[σ] λ φ λ λφ φ
p1 φ1 λφ λ1
×dφdp+c
(cid:90) p2 1 (cid:16)
2[(v) (T) ] ([T] ) cosφ +([T] )2 [v] cosφ
(cid:17)φ2
dp
2 2[σ] λ λ λ λ φ λ φ λ
p1 λφ φ1
1
(cid:18)
(cid:104) (cid:105)
(cid:19)p2
− [2(ω) (T) ] ([T] ) + [ω] ([T] )2 (2.47)
2[σ] λ λ λ λ φ λ λ φ
λφ λφ p1
BAE = c
(cid:90) p2 (cid:90) φ2 1
(cid:2)
u(T)2
(cid:3)λ2dφdp
1
p1 φ1
2[σ]
λφ
λ λ1
+c
(cid:90) p2 1
(cid:0)(cid:2)
(T)2v
(cid:3)
cosφ
(cid:1)φ2
dp (2.48)
2
p1
2[σ]
λφ
λ λ φ1
(cid:32)
[ω(T)2]
(cid:33)p2
λ λφ
−
2[σ]
λφ
p1
BKZ = c
(cid:90) p2 (cid:90) φ2 1
(cid:0)
u
(cid:2)
u2 +v2 −(u)2 −(v)2
(cid:3)(cid:1)λ2
1 2g λ λ λ1
p1 φ1
×dφdp+c
(cid:90) p2 1
(cid:0)(cid:2)
vcosφ
(cid:2)
u2 +v2 −(u)2 −(v)2
(cid:3)(cid:3)φ2dp
(2.49)
2 2g λ λ φ1
p1
(cid:18)
1
(cid:19)p2
(cid:2) (cid:2) (cid:3)(cid:3)
− ω u2 +v2 −(u)2 −(v)2
2g λ λ λφ
p1
BKE = c
(cid:90) p2 (cid:90) φ2 1
(cid:0)
u
(cid:2)
(u)2 +(v)2
(cid:3)(cid:1)λ2dφdp
1 2g λ λ λ1
p1 φ1
+c
(cid:90) p2 1
(cid:0)(cid:2)
vcosφ
(cid:2)
(u)2 +(v)2
(cid:3)(cid:3) (cid:1)φ2dp
(2.50)
2
p1
2g λ λ λ φ1
(cid:18)
1
(cid:19)p2
(cid:2) (cid:2) (cid:3)(cid:3)
− ω (u)2 +(v)2
2g λ λ λφ
p1
where c = −[a(λ −λ )(sinφ −sinφ )]−1,c = −[a x(sinφ −sinφ )]−1.
1 2 1 2 1 2 2 1
The boundary terms BA , BA , BK , and BK represent the fluxes of A , A ,
Z E Z E Z E
K , and K , respectively, from the lateral and vertical boundaries. Each boundary term
Z E
has three components and shares a similar structure. For exemplification purposes, let’s
look into the BA term. The first component represents the contribution of the zonal
Z
temperature flux anomalies to the A term at the western and eastern boundaries. This
Z
term is computed for the westernmost and easternmost longitudes, integrated over all
latitudes and pressure levels, and averaged over the entire domain. The second component
is similar to the first one, representing the contribution of the meridional temperature
flux anomalies to the A term at the southern and northern boundaries. This term is
Z
computed for the southernmost and northernmost latitudes, integrated over all longitudes
and pressure levels, and averaged over the entire domain. The third component represents

|     |     |     | Section2.4.AtmosphereEnergetics |     |     |     |     | 91  |
| --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
the contribution of the vertical temperature flux anomalies to the A term at the top
Z
and bottom boundaries. This term is computed for the topmost and bottommost pressure
levels, integrated over all longitudes and latitudes, and averaged over the entire domain.
The same logic can be applied to all other terms, substituting A with A , K , and K ,
|     |     |     |     |     |     |     | Z E Z | E   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
respectively.
| Lastly, | the terms | BΦZ and | BΦE | are | given by: |     |     |     |
| ------- | --------- | ------- | --- | --- | --------- | --- | --- | --- |
(cid:90) (cid:90)
|     |     |     |     | p2 φ2 | 1 (cid:16) |        | (cid:17)λ2 |     |
| --- | --- | --- | --- | ----- | ---------- | ------ | ---------- | --- |
|     |     | BΦZ | =c  |       | [v]        | ([Φ] ) | dφdp       |     |
|     |     |     | 1   |       | g λ        | λ φ    |            |     |
λ1
p1 φ1
(cid:90) p2
|     |     |     |     |                      | 1 (cid:16) |                      | (cid:17)φ2 |        |
| --- | --- | --- | --- | -------------------- | ---------- | -------------------- | ---------- | ------ |
|     |     |     | +c  |                      | cosφ[v]    | ([Φ]                 | ) dp       | (2.51) |
|     |     |     |     | 2                    |            | λ                    | λ          |        |
|     |     |     |     |                      | g          |                      | φ          |        |
|     |     |     |     | p1                   |            |                      | φ1         |        |
|     |     |     |     | 1 (cid:18) (cid:104) |            | (cid:105) (cid:19)p2 |            |        |
|     |     |     | −   | ([ω]                 | ) ([Φ]     | )                    |            |        |
|     |     |     |     |                      | λ φ λ      | φ                    |            |        |
|     |     |     |     | g                    |            | λφ                   |            |        |
p1
|     |     |     | (cid:90) | p2 (cid:90) φ2 | 1   |     |     |     |
| --- | --- | --- | -------- | -------------- | --- | --- | --- | --- |
)λ2dφdp
|     |     | BΦE | =c  |     | ((u) (Φ) |      |     |     |
| --- | --- | --- | --- | --- | -------- | ---- | --- | --- |
|     |     |     | 1   |     | λ        | λ λ1 |     |     |
|     |     |     |     |     | g        | λ    |     |     |
p1 φ1
(cid:90) p2
1
|     |     |     | +c  |     | (cid:0) [(v) (Φ) | ] cosφ | (cid:1)φ2dp | (2.52) |
| --- | --- | --- | --- | --- | ---------------- | ------ | ----------- | ------ |
|     |     |     |     | 2   | λ                | λ      |             |        |
|     |     |     |     |     | g                | λ λ    | φ1          |        |
p1
|     |     |     |     | 1 (cid:16) | (cid:17)p2 |     |     |     |
| --- | --- | --- | --- | ---------- | ---------- | --- | --- | --- |
|     |     |     | −   | [(ω)       | (Φ) ]      |     |     |     |
|     |     |     |     |            | λ λ λφ     |     |     |     |
|     |     |     |     | g          |            | p1  |     |     |
The terms BΦZ and BΦE describe the dynamical mechanisms that produce or destroy
kinetic energy. As elucidated by Muench (1965), these terms, along with C and C , arise
Z E
from the derivation of the term V ⃗ · ∇Φ, where Φ is the geopotential. This expression
represents the generation of kinetic energy through cross-isobaric flow towards areas of low
pressure. Conversely, the destruction of kinetic energy occurs when there is cross-isobaric
| flow towards | areas of | high pressure. |     |     |     |     |     |     |
| ------------ | -------- | -------------- | --- | --- | --- | --- | --- | --- |
Apartfromexamining the individualcontributions ofeachtermtothe energycycle, the
Lorenz Energy Cycle (LEC) highlights specific interactions between terms that elucidate
distinctdynamicalmechanisms(Figure2.27). TheA term, involvingmeridionalgradients
Z
of temperature and atmospheric stability, interacts in such a way that C > 0 acts to
A
diminish these gradients through the meridional transport of sensible heat. This process
setsthestageforC > 0,drivenbythezonaltemperaturegradientandverticalmotions. In
E
contrast, the conversion from K to K (C ) redistributes kinetic energy without altering
|     |     |     | Z   | E   | K   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the thermal structure and is primarily influenced by the horizontal shear of the mean
flow. Therefore, the processes A → A → K are often referred to as the ”baroclinic
|     |     |     | Z   |     | E E |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
chain,”while C is known as the barotropic conversion term (Michaelides, 1992; Veiga
K

92
Chapter2.TheoreticalBackground
et al., 2013; Pezza et al., 2014; Okajima et al., 2021, e.g.). Additionally, the term ”moist
baroclinic chain”is used here to refer to the process where G supplies energy to A , acting
E E
in consonance with the baroclinic chain.
Baroclinic Barotropic
instability instability
Latent heat
release
Figure 2.27: Schematic representation of the different energy conversion chains in the Lorenz Energy
Cycle. The diagram illustrates the ”baroclinic chain”(A →A →K ), indicating the role of baroclinic
Z E E
instability, thecontributionoflatentheatreleasebytheG termandthe”barotropicchain”(K →K ).
E Z E
2.4.3 Lorenz Energy Cycle applied to cyclonic systems
During the 1960s and 1970s, extensive research was conducted on the energetics of
extratropical cyclonic systems. Smith (1980) reviewed these studies, offering a detailed
summary of their outcomes. According to the mean kinetic energy (K) budgets, cyclones
are areas of relatively higher concentrated kinetic energy compared to the rest of the
hemisphere, though the difference is not markedly substantial. Cyclones are characterized
bysignificantenergeticactivity,withsubstantialK generationthroughcross-contourflow.
E
This generation is nearly balanced by the horizontal export of energy and its dissipation.
Mature cyclones typically exhibit negative values for D ; however, in certain scenarios,
E

93
Section2.4.AtmosphereEnergetics
D can act as an energy source (D > 0), especially in regions characterized by intense
E E
convection or the presence of short upper air waves, predominantly above the planetary
boundary layer. This dynamic might be associated with energy transfer from sub-grid
scales to the grid scale. Additionally, latent heat release from convective processes plays a
critical role in the generation of APE in extratropical cyclones. The author concludes that
generally, cyclonesareinefficientthermodynamicsystems; asignificantportionofA isnot
E
converted into K , leading to an energy conversion efficiency of only 3% to 4%. Cyclones
E
account for approximately 6% of the hemispheric energy contribution. However, intense
cyclones, which are about 50% more energetically active than average, can contribute up
to 20% of the hemispheric energy.
More recently, the study by Black and Pezza (2013) provides a detailed climatology of
the energetics of cyclonic systems, specifically focusing on explosive cyclones. This rese-
arch spans four major regions—the Northwest Pacific, the North Atlantic, the Southwest
Pacific, and the South Atlantic—utilizing a 32-year climatology to analyze these pheno-
mena. The analysis reveals that anomalous energy conversions begin approximately 48
hours before the explosive cyclone development and remain strong for up to 120 hours.
The results demonstrate that the baroclinic chain is the primary mechanism driving the
energy dynamics during explosive cyclogenesis, and this holds true across different regions
and times of the year. Furthermore, the study finds that within the analyzed domains, the
energetic signatures of regular cyclones often merge with background noise, making them
indistinguishable.
ThereviewbySmith(1980)providesabroadoverviewoftheenergybudgetofextratro-
pical cyclones, focusing primarily on their contributions to general circulation rather than
on the dynamical mechanisms essential for their development, intensification, and decay.
Meanwhile, Black and Pezza (2013) offers a more detailed picture, especially of explosive
cyclones. However, the difficulty in distinguishing the energetic signatures of regular cy-
clones from background noise may be attributed to the large computational domains used,
whichareextensiveenoughtoincludemultiplecyclonicsystemssimultaneously, potentially
complicating the analysis. To overcome these challenges and gain a deeper understanding
of cyclonic energetics, specific case studies are essential. These studies provide insights into
how various energy transformations within a cyclone contribute to its lifecycle. The lite-
rature reviewed in the next paragraphs highlights the pathways that supply energy to the

94
Chapter2.TheoreticalBackground
eddy energy reservoirs, with particular emphasis on the K term, which serves as a proxy
E
for the system’s intensity. Special attention is given to the contributions of the baroclinic
(A → A → K ) and barotropic (K → K ) chains, as well as to the contributions from
Z E E Z E
latent heat release (G ) due to the eddy’s convective activity. These elements are crucial
E
for understanding the energetic dynamics that drive cyclone behavior and evolution.
There are only a few studies accessing the Lorenz Energy Cycle in the context of
tropical cyclones. For instance, Brennan and Vincent (1980) analyzes the synoptic-scale
energy budget of Hurricane Carmen (1979) as it intensified from a tropical depression to a
major hurricane. During the tropical depression stage, K serves as a source of energy for
E
both A and K , while also exporting energy (BK < 0), primarily sustained by RK .
E Z E E
Concurrently, A exports energy (BA < 0) and experiences energy destruction due to
E E
diabatic cooling and/or descending movements (G < 0). This suggests that during
E
this phase, the system predominantly relies on up-scaling of energy from subgrid scales
and/or cross-isobaric flow (BΦE > 0). However, during the hurricane stage, diabatic
heating (from G ) begins to supply energy to A , further supported by the import of
E E
energy (BA > 0) and conversion from A . Most of this energy is transformed into K .
E Z E
Additionally, the zonal circulation contributes to the eddy energy (C < 0). Consequently,
K
during the hurricane phase, moist baroclinic processes drive the system’s development,
supplemented by barotropic conversions. Despite an overall reduction in K and K , the
E Z
storm’s circulation intensifies. These authors attribute this paradox to mesoscale processes
notbeingadequatelyresolvedduetothepoorresolutionofthedataset,withnegativevalues
for both D and D indicating an energy transfer from the resolved synoptic scale to the
Z E
mesoscale. These observations imply that higher resolution datasets might reveal different
dynamics for K and K budgets.
E Z
Although the study by Brennan and Vincent (1980) provided important insights into
theenvironmentalenergeticschangesduringhurricaneformation, severalcaveatsmeritdis-
cussion. First, the dataset used features a coarse resolution with 2.5◦ grid spacing, which
is insufficient to accurately represent mesoscale phenomena associated with the hurricane.
Additionally, the data consisted primarily of point-source rawinsonde observations, surface
observations, and daily infrared satellite imagery, with gaps filled by linear interpolation.
Lastly, the computational domain was excessively large (50◦ ×50◦), raising concerns that
the system’s energetics could be confounded with background environmental influences.

|     |     | Section2.4.AtmosphereEnergetics |     |     |     | 95  |
| --- | --- | ------------------------------- | --- | --- | --- | --- |
These limitations suggest that the study’s findings should be interpreted with caution,
considering the potential blending of cyclone energetics with broader atmospheric proces-
ses.
Using data from the NCEP/NCAR reanalysis, Veiga et al. (2008) analyzed the energy
budget for Hurricane Catarina, distinguishing its development into distinct phases. Du-
ring the extra-tropical phase, the moist baroclinic chain was active, with both A and
Z
G supplying energy to A , which was predominantly converted into K . As the system
| E   | E   |     |     |     | E   |     |
| --- | --- | --- | --- | --- | --- | --- |
transitioned into the tropical phase, this chain loss intensity, notably as G decreased sig-
E
nificantly, making the conversion from K to K the primary contributor to K . However,
|     |     |     | Z E |     |     | E   |
| --- | --- | --- | --- | --- | --- | --- |
much of this energy was exported from the domain, leading to a decrease in K . Upon
E
reaching Category 1 Hurricane status, there was a reversal in the sign of the baroclinic
chain, characterized by conversions from K to A to A , with both C and RK playing
|                     |     |     | E E | Z   | K   | E   |
| ------------------- | --- | --- | --- | --- | --- | --- |
| roles in augmenting | K . |     |     |     |     |     |
E
More attention was given to the energetics of subtropical cyclones than to the tropical
systems. Michaelides (1987) analyzes the synoptic-scale energy budget of a frontal de-
pression that initially formed in the Mediterranean region, categorizing its evolution into
four distinct phases. Although the nomenclature was not established at the time, the
system might potentially have been classified as a medicane, a type of subtropical cyclone
that originates in the Mediterranean (da Rocha et al., 2019). During the precyclogene-
tic period (”incipient stage”), A is sustained by contributions from A , K , and BA .
|     |     | E   |     |     | Z   | E E |
| --- | --- | --- | --- | --- | --- | --- |
However, it experiences a net decrease due to negative generation from cooling and descen-
ding motions. Meanwhile, K sees an increase, fueled by conversions from K and energy
|     |     | E   |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- | --- |
import. As cyclogenesis begins (”intensification stage”), the signals for both C and C
A E
reverse, enabling A to feed both A and K , supported by energy import and positive
|     | E   | Z   | Z   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
G . Although K continues to enhance K , increased dissipation begins to diminish K .
| E   | Z   |     | E   |     |     | E   |
| --- | --- | --- | --- | --- | --- | --- |
In the development phase (”mature phase”), A reaches its peak, primarily due to latent
E
heat generation and significant energy import. A is actively converted to K , yet K
|     |     |     | E   |     |     | E E |
| --- | --- | --- | --- | --- | --- | --- |
continues to decline overall, affected by heightened dissipation and energy conversions to
K . In the post-cyclogenesis phase (”decay phase”), both A and K diminish as the
| Z   |     |     |     | E   | E   |     |
| --- | --- | --- | --- | --- | --- | --- |
system weakens, with marked reductions in import, conversion rates, and D reaching its
E
maximum.
In their study, Dias Pinto et al. (2013) investigate the potential for tropical transition

96
Chapter2.TheoreticalBackground
of Subtropical Cyclone Anita near the southeast Brazilian coast. During the early stages
of the system, the barotropic chain primarily fueled K . As the system evolved into a
E
hybrid stage and approached its potential for tropical transition, both moist baroclinic and
barotropic chains actively supplied energy to K , complemented by positive values of G
E E
due to convective processes. Concurrently, the system exported both A and K through
E E
its boundaries. Eventually, Anita entered a baroclinic environment and transitioned to
an extratropical system. This phase was marked by a reversal in the sign of C and a
K
dominance of the baroclinic chain in its energetics.
The study by Pezza et al. (2014) explores the energetics of the hybrid subtropical cy-
clone known as ”Duck,”which occurred over the Tasman Sea. Influenced by a persistent
mid-latitude blocking high, the genesis of Duck created a conducive environment for cy-
clogenesis, with the system undergoing a partial tropical transition. During the genesis
phase, a significant peak in C was observed, reaching a maximum near 350 hPa, faci-
K
litated by the presence of the blocking system — a similar environmental condition to
that observed during Catarina’s tropical transition. As Duck evolved, a secondary peak in
baroclinic conversion coincided with the development of an upper-level warm core for the
first time. However, the energy supply for K during this stage was insufficient for a full
E
tropical transition. The authors speculate that the baroclinic conversion prevented Duck
from achieving a complete tropical transition, hence not reaching hurricane status.
The energetics of the Duck storm were also investigated by Cavicchia et al. (2018),
with comparisons made to an extratropical cyclone, the Pasha Bulker storm. Similar to
findings by Pezza et al. (2014), the Duck storm’s lifecycle was predominantly influenced by
the barotropic chain, which was the main source of energy for K . In contrast, the Pasha
E
Bulker storm was primarily driven by the baroclinic chain, with the most significant ba-
roclinic energy conversions occurring during its intensification phase. However, Cavicchia
et al. (2018) does not present results for generation and boundary terms, which limits the
depth of the analysis.
For extratropical cyclones, a larger body of literature exploring their energy cycle can
be found, especially for the Mediterranean and South Atlantic regions. For instance, in
Michaelides (1992), an extratropical system originating in the Mediterranean region is
analyzed, providing a basis for comparison with the earlier study by Michaelides (1987).
Duringtheinitialdevelopmentphase,A increasesduetosignificantlatentheatreleaseand
E

Section2.4.AtmosphereEnergetics 97
the advection of colder air over warmer waters, which enhances G and C . Concurrently,
E A
K is sustained by conversions from both A and K . As cyclogenesis progresses, the
| E   |     |     |     | E   | Z   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
energetic profile remains similar to the previous stage; however, convective activity and
imports of A decline, leading to a decrease in this term. Simultaneously, an increase in
E
D causes a reduction in the absolute value of K . During this stage, K is primarily
| E   |     |     |     | E   |     |     | E   |
| --- | --- | --- | --- | --- | --- | --- | --- |
maintained by C . In the mature phase, there is a further decline in G and imports of
|     | K   |     |     |     |     |     | E   |
| --- | --- | --- | --- | --- | --- | --- | --- |
A , causing A to decrease further. Additionally, as D increases and conversion from
| E   | E   |     |     |     | E   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
other terms decreases, K also diminishes over time. During the decay phase, G reaches
|     |     | E   |     |     |     |     | E   |
| --- | --- | --- | --- | --- | --- | --- | --- |
its lowest level; however, A increases due to enhanced C and weakened C . Conversely,
|     |     | E   |     |     | A   |     | E   |
| --- | --- | --- | --- | --- | --- | --- | --- |
K , despite the weakened C and C , increases as dissipation becomes minimal.
| E   |     | A   | K   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Wahab et al. (2002) also analyzed the energy budget throughout the development of a
Mediterranean cyclone. The cyclogenesis phase is characterized by a significant increase
in K , primarily supported by the residual term (RK ), while A is initially sustained
| E   |     |     |     |     | E   | E   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
by K . However, as the RG term increases, A begins to feed K . The growth period
| E   |     | E   |     | E   |     | E   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
of the cyclone is marked by K being bolstered by C and imports of energy, which are
|     |     | E   |     |     | K   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
subsequently either dissipated or converted to A , with RG acting as a sink of energy.
|     |     |     |     | E   | E   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
During the dissipation period, A serves as a source of energy for both K and A .
|     |     | E   |     |     |     |     | E Z |
| --- | --- | --- | --- | --- | --- | --- | --- |
Concurrently, while K is supported by K and imports of energy, dissipation acts as a
|             |                 | E         | Z             |      |     |     |     |
| ----------- | --------------- | --------- | ------------- | ---- | --- | --- | --- |
| significant | sink of energy, | resulting | in a decrease | in K | .   |     |     |
E
The study by Bulic (2006) investigates the energy budget associated with a deep and
rapid cyclogenesis over the Mediterranean region, utilizing the ALADIN model. Before
cyclogenesis, K is converted into A , a process that reverses after the cyclone forms.
|     | E   |     | E   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Throughoutthecyclone’slifecycle,C consistentlysuppliesenergytoK . Thisconversion,
|     |     |     | K   |     |     | E   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
most intense at upper levels around 350 hPa, is identified as crucial for the system’s
development. Additionally, B is responsible for exporting eddy energy throughout the
KE
entire lifecycle, except during the time of cyclone formation. The study highlights the
cyclone’s dependency on both baroclinic and barotropic processes; however, it also notes
that the results may be limited to the dynamics captured by the model and might not
| fully reflect | observational | data. |     |     |     |     |     |
| ------------- | ------------- | ----- | --- | --- | --- | --- | --- |
Dias Pinto and Rocha (2011) analyzed the energy cycle for three extratropical cyclones,
one for each genesis region in South America, detailing each system’s development across
formation, mature, and decay phases. For the first system, with genesis in the SE-BR

98
Chapter2.TheoreticalBackground
region, the energetics were most active during the formation phase, where both baroclinic
and barotropic chains provided energy to K , with significant contributions from the C
E K
term. In the mature phase, the baroclinic chain reversed, making C the sole contributor
K
to K . During the decay phase, K transferred energy to K and A to A . The
E E Z E Z
secondsystem,originatingintheLA-PLATAregion,maintainedaconsistentenergysupply
throughout its lifecycle via the moist baroclinic chain, most prominently during the mature
phase. Throughout all phases, K consistently supplied energy to K . The third system,
E Z
with its genesis in the ARG region, was primarily sustained by the baroclinic chain, with
contributions from latent heat release (G ) only during the mature phase. Although less
E
significant, there was also an energy supply from C during the formation and mature
K
phases.
The study by Pezza et al. (2010) examines the Lorenz energetics of a high-latitude ba-
roclinic storm that caused severe flooding in Nome, Alaska. The trajectory and intensity
of the storm were significantly influenced by a blocking high-pressure system that steered
its path a week prior to its formation. From the onset of cyclogenesis to the rapid inten-
sification phase, the environment transitioned from lower to higher energy states, marked
by peaks in A and K . During these phases, both the baroclinic and barotropic energy
E E
chains supplied energy to K , with a smaller contribution from G to A . The computati-
E E E
onaldomainincludedtheblockingregion, highlightingtheroleofthishigh-pressuresystem
in facilitating the energy conversion C , which supplied K to the cyclonic system. As
K E
the storm reached its peak activity, the barotropic chain reversed, with K feeding energy
E
back to zonal kinetic energy (K ). Thus, during this stage, the maintenance of the system
Z
was predominantly sustained by the baroclinic chain. Additionally, the peak in baroclinic
energytransferoccurredapproximately18hoursbeforethestormreachedmaximuminten-
sity, indicating significant preconditioning of the environment by the baroclinic processes.
Michaelides et al. (1999) analyze the energetics of an intense Mediterranean cyclone,
employing both Eulerian and quasi-Lagrangian frameworks for comparison. The quasi-
Lagrangian framework reveals a significant increase in A during the cyclone’s develop-
E
ment, driven by diabatic heating processes such as latent heat release in the warm sector.
Concurrently, K increases from the early stages to the maturity phase and then decreases
E
as the cyclone decays. This initial rise in K is propelled by C , especially prominent at
E K
the jet level in the upper troposphere. The transformations between A and K are cha-
E E

99
Section2.4.AtmosphereEnergetics
racterized by initial conversions of A to K , fueling the cyclone’s intensification, followed
E E
by a reversal where K converts back to A as the system weakens. Notably, there are
E E
substantial imports of K during the cyclone’s intensification phase and exports during its
E
dissipation. The quasi-Lagrangian analysis indicates higher A and lower K compared
E E
to the Eulerian method, suggesting that the fixed volume method captures more ambient
kinetic energy from surrounding regions. Both methods confirm an overall conversion from
K to K , although the values are greater in the Eulerian method, and the conversions
Z E
from A to K change signs. Additionally, there are reversals in signs for the boundary
E E
terms. The semi-Lagrangian method is considered to more genuinely represent the energe-
tics characteristics of the synoptic system under study, as it isolates the cyclone as much as
possible at all times. In contrast, the Eulerian method allows for circulations other than
the cyclonic system under study to infringe into the computational region, potentially
spuriously contaminating the cyclone’s energetics.
The reviewed literature provides valuable insights into the energetics of different cy-
clonic systems. For tropical cyclones, although the limited body of literature prevents
definitive conclusions, it appears that the barotropic chain, aided by the G term and
E
subsequent conversions from A to K , is a primary driver for cyclone development. This
E E
emphasis on barotropic instability aligns well with research highlighting the role of baro-
tropic instability in tropical waves for the initial development of tropical cyclones, with
further intensification facilitated by latent heat release via CISK/WISHE mechanisms, as
discussed in Section 2.1.3. Meanwhile, studies on subtropical cyclones indicate a shared
contribution from barotropic and baroclinic processes, with the moist contributions to the
baroclinic chain being variably active. The barotropic chain seems particularly important
in the initial stages, with the baroclinic chain gaining significance in later stages. For
extratropical cyclones, contrary to expectations, the baroclinic chain is not the sole driver
of their energy cycle; most case studies indicate a role for the barotropic chain in their
development. From Black and Pezza (2013)’s results, we can infer that the primary dif-
ference in the Lorenz Energy Cycle (LEC) between regular and explosive cyclones is the
heightened importance of the baroclinic chain in the latter. Additionally, it is noteworthy
that for both subtropical and extratropical systems, barotropic conversions occur predomi-
nantly at upper tropospheric levels. Nevertheless, while these energy pathways are crucial
for system development, other terms also play important roles. For instance, D is often
E

100
Chapter2.TheoreticalBackground
indicated as a significant sink for K , with larger values as K increases. Additionally,
E E
imports of K (BK ), particularly in the early stages of development, also contribute to
E E
system development.
From the reviewed literature, it is evident that the LEC methodology is a valuable
diagnostic tool for studying cyclonic system dynamics. However, despite the methodology
dating back to the 1960s and still being in use today, the body of literature on this topic is
stillexpanding,primarilycomprisingcasestudies,withtheonlycomprehensiveclimatology
provided by Black and Pezza (2013). Furthermore, most case studies utilize the Eulerian
framework, which may underestimate contributions from certain terms, as the large-scale
environment might overshadow the systems’ energetics. There is a need for more clima-
tologies assessing the LEC for cyclonic systems—or at least analyses of a large number of
systems—to better understand the energy pathways related to their development.

3
Chapter
Data & Methods
3.1 Methodological Steps
The primary objective of this thesis was to identify the key dynamical mechanisms
influencing cyclone development in the Southwestern Atlantic and Southeast American
regions across their various development phases. This was achieved through a series of
methodological steps as detailed below and illustrated in Figure 3.1.
Acomprehensivedatabaseofcyclonicsystemtrackswasused, encompassingallsystems
with genesis in the South Atlantic region from 1979 to 2020. The cyclones were detected
based on their central relative vorticity at 850 hPa using the TRACK algorithm. This
extensive dataset served as the foundational input for subsequent analyses.
The CycloPhaser program was developed to delineate the distinct life phases of each
cyclone. CycloPhaser decomposes the relative vorticity time series into distinct phases
using its maximum, minimum, and derivative values. This tool facilitated the construction
of a climatology of cyclone life cycle phases, enabling a detailed investigation of the mean
characteristics and spatial distribution of cyclones during each phase of their development.
An application was programmed to compute the Lorenz Energy Cycle (LEC) for all
cyclones in the database. This analysis provided insights into the energetics of the systems,
allowing for a detailed examination of the mean energy characteristics across different life
cycle phases.
To further refine the analysis, the K-means clustering algorithm was employed to iden-
tify distinct energy patterns (EPs) within the cyclones. This classification enabled the
grouping of cyclones based on their energy characteristics, facilitating a more detailed
understanding of the dynamical processes at play.

102
Chapter3.Data&Methods
The final step involved a detailed investigation of the dynamical mechanisms associ-
ated with cyclonic system development. By examining absolute vorticity (η) fields, the
Rayleigh-Kuo criterion was employed for detecting the occurrence of barotropic instability
during cyclone development, while the occurrence of baroclinic instability was assessed
using maximum Eady Growth Rate fields.
(A) TRACKS (B) LIFE PHASES
ζ850
(E) BAROTROPIC AND BAROCLINIC
(C) ENERGETICS (D) ENERGY PATTERNS
INSTABILITIES
Figure 3.1: Flowchart depicting the methodological steps used in this thesis. (A) Retrieval of the cy-
clonic system track database using central relative vorticity at 850 hPa. (B) Identification of cyclone life
phases with CycloPhaser, categorizing the vorticity time series into distinct phases. (C) Computation
andanalysisoftheLorenzEnergyCycleforthecyclonestoinvestigatetheirenergeticcharacteristics. (D)
ClassificationofenergypatternsusingtheK-meansalgorithmtodeterminedistinctenergycharacteristics.
(E) Examination of dynamical mechanisms related to barotropic and baroclinic instabilities influencing
cyclone development.
3.2 Databases
3.2.1 ERA5 Reanalysis
For both the cyclone tracking procedure and for the energetics computation, the da-
tabase used was the ERA5 (Hersbach et al., 2020). The ERA5 is a comprehensive rea-
nalysis dataset developed by the European Centre for Medium-Range Weather Forecasts
(ECMWF). It represents the fifth generation of ECMWF reanalysis, providing global cli-
mate and weather data with an unprecedented level of detail and accuracy. This dataset

103
Section3.2.Databases
spans from January 1940 to the present, with ongoing updates ensuring its relevance for
current and historical climate studies.
ERA5 reanalysis data are produced using the Integrated Forecasting System (IFS)
Cy41r2, which assimilates a vast array of observations, including satellite and in-situ me-
asurements (Hersbach et al., 2020). The dataset offers hourly estimates of a multitude of
atmospheric, ocean-wave, and land-surface parameters, making it highly valuable for va-
rious meteorological and climate research applications. The spatial resolution of ERA5 is
approximately 31 km, with 137 vertical levels from the surface to 1 hPa, providing detailed
information into the vertical structure of the atmosphere.
The ERA5 reanalysis dataset has been evaluated for the Southern Hemisphere. It can
provideprecipitationpatternscomparabletoobservations, althoughthereanalysispresents
more accurate results for the extratropics, especially in winter, than for tropical regions
(Balmaceda Huarte et al., 2021; Lavers et al., 2022). The dataset also provides accurate
results for surface winds, particularly outside the tropical region, although the associated
errors increase with wind intensity (Campos et al., 2022). However, for near-surface winds,
Ramon et al. (2019) demonstrated that the ERA5 is currently the reanalysis that presents
the best results. For temperature, although the ERA5 captures accurately the spatial
distribution of temperature indices it can present warm biases near the Andes and on
southern South America (Balmaceda Huarte et al., 2021).
3.2.2 Cyclone Tracks in the South Atlantic
For this study, precise information about the positioning (track) and central vorti-
city at the 850 hPa level (ζ ) of cyclones was essential. These data were sourced from
850
the ”Atlantic Extratropical Cyclone Tracks Database”as detailed by Gramcianinov et al.
(2020). Spanning from 1979 to 2020, this database covers the entire Atlantic Ocean within
the spatial domain of 15◦S–55◦S and 75◦W–20◦E. Cyclone tracking within this database
utilizes the ERA5 reanalysis fields, employing the TRACK algorithm (Hodges, 1994, 1995)
and the method outlined by Hoskins and Hodges (2002), which computes relative vorticity
from wind components at the 850 hPa level. The TRACK algorithm has previously been
used for obtaining cyclone climatologies in the South Atlantic region (Gramcianinov et al.,
2019, 2020). The ERA5 dataset was chosen for its superior resolution, offering significant
advantages in analyzing regions with complex orography and temperature gradients, such

104
Chapter3.Data&Methods
as the SESA region, ensuring a comprehensive and consistent representation of cyclone
climatology (Gramcianinov et al., 2020).
The tracking criteria included a minimum cyclone duration of 24 hours and a displace-
ment threshold of 1000 km. These requirements align with previous climatologies of South
Atlantic cyclones (Sinclair, 1995; Gramcianinov et al., 2019). Additionally, systems that
spent over 80% of their lifecycle over continental regions were excluded to avoid counting
thermal lows and lee troughs, which are not the focus of this study (Crespo et al., 2021).
While the primary focus was on extratropical cyclones, due to the specific calibration and
sensitivity of the TRACK algorithm to features typical of these systems, the methodology
does not explicitly exclude subtropical or tropical cyclones. Despite their rarity in the
South Atlantic, subtropical systems, which occasionally exhibit characteristics similar to
extratropical cyclones (Hart, 2003), may still be detected but remain a minority in the
dataset. Further details on the methodology and database evaluation are discussed in
Gramcianinov et al. (2020).
3.3 Cyclone’s Life Cycle Detection
This section outlines the procedure for detecting the life cycle phases of cyclones. In
the current study, an automated method, the Cyclophaser program, was developed and
employed to facilitate this process. Section 3.3.1 provides an in-depth examination of
the Cyclophaser program, highlighting its functionalities and the methodologies it em-
ploys. Subsequently, Section 3.3.2 explores the specific settings and configurations of the
Cyclophaser used in this study.
3.3.1 Cyclophaser Program Description
To facilitate the detection of individual life cycle phases of cyclones, an automated
Python package named Cyclophaser (Figure 3.2) was developed (de Souza et al., 2024).
This package is open-source and freely available on the PyPI repository. It can be ins-
talled using the pip package manager with the command pip install cyclophaser.
Comprehensive documentation, including usage examples, is available on ReadTheDocs
at https://cyclophaser.readthedocs.io/en/latest/, and the complete source code,
whichisopentocontributions,canbefoundonGitHubathttps://github.com/daniloceano/

105
Section3.3.Cyclone’sLifeCycleDetection
CycloPhaser.
Figure 3.2: The logo of the Cyclophaser program.
The program is designed to detect cyclone lifecycle phases using series of relative vorti-
cityatthesystem’scentralpositionanditsfirstderivative(Figure3.3). WhileCyclophaser
wasspecificallydevelopedandtestedforthispurpose, othervariablessuchassealevelpres-
sure or geopotential data might also be effective, although tests using these variables have
not yet been conducted. Exploring how the lifecycle of cyclones might vary with diffe-
rent variables and how the geographical positioning of each stage might differ is an open
research question.
The program begins with a preprocessing stage where users have the option to apply
the Lanczos filter (Duchon, 1979) to the vorticity time series (Figure 3.3b). Based on the
sinc function, the ideal mathematical representation of a low-pass filter, the Lanczos filter
is adapted by windowing the sinc function to a finite range. Cyclophaser utilizes a band-
pass filtering technique where weights are calculated using two cutoff frequencies, creating
a differential of two sinc functions. This allows the filter to pass a specific frequency range
while attenuating frequencies outside this range, permitting customization based on the
spatio-temporal resolutions of different reanalysis datasets.
The Lanczos filter’s primary use in Cyclophaser is to remove noise unrelated to the
development of extratropical cyclones on synoptic scales, including fluctuations due to
topography-induced circulations, sea breezes, and spatial and temporal variations in sea
surfacestructures(Steeleetal.,2015;Daetal.,2017;Acevedoetal.,2010). High-resolution
datasets like ERA5 benefit from this filtering, which effectively reduces noise from struc-
tures like frontal systems (Hoskins and Hodges, 2002). However, this filtering step may
be omitted for datasets that have been preprocessed by tracking algorithms incorporating
spatial filters (Murray and Simmonds, 1991; Pinto et al., 2005; Flaounas et al., 2014; Hos-
kins and Hodges, 2002, e.g.). As the track database used in the present study employed

| 106 |     |     | Chapter3.Data&Methods |     |     |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
| (A) |     | (B) |                       | (C) |     | (D) |     |     |
y
tic
itro
V
|     | Time |     | Time |     |      |     |      |     |
| --- | ---- | --- | ---- | --- | ---- | --- | ---- | --- |
|     |      |     |      |     | Time |     | Time |     |
| (E) |      | (F) |      | (G) |      | (H) |      |     |
y
tic
itro
V
|      | Time |     | Time |     | Time |     | Time                    |        |
| ---- | ---- | --- | ---- | --- | ---- | --- | ----------------------- | ------ |
| (I)  |      | (J) |      | (K) |      |     |                         |        |
|      |      |     |      |     |      |     |  Incipient              |  ζ 850 |
| y    |      |     |      |     |      |     |   I n t e n s ification |   ζ    |
| tic  |      |     |      |     |      |     |                         | f      |
| itro |      |     |      |     |      |     |   M a t u r e           |   ζ    |
s
|     |     |     |     |     |     |     |   D e c a y |   ζ |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
| V   |     |     |     |     |     |     |             | s2  |
 Residual
|     | Time |     | Time |     | Time |     |     |     |
| --- | ---- | --- | ---- | --- | ---- | --- | --- | --- |
Figure 3.3: Illustrative representation of the methodological steps employed by Cyclophaser in analyzing
cyclone lifecycle phases using vorticity series. The detailed steps demonstrate the application of data
| processing | techniques | including | the Lanczos filter. |     |     |     |     |     |
| ---------- | ---------- | --------- | ------------------- | --- | --- | --- | --- | --- |
a filtering technique, the Lanczos filtering was not needed. Thus, a detailed formulation,
explanation, and exploration of the issues related to such a filtering technique are provided
| in Appendix | A.  |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
After the initial filtering, the CycloPhaser program employs the Savitzky-Golay filter
(Savitzky and Golay, 1964), as implemented in SciPy’s package (Virtanen et al., 2020),
to further reduce residual noise (Figure 3.3c). This step is crucial for ensuring that the
derivative curves form a sinusoidal pattern, which is essential for precise phase detection
(Figure 3.3c). The Savitzky-Golay filter operates by fitting a polynomial of degree k
to a window of 2m + 1 data points centered at each point y in the input signal. The
i
coefficientsofthispolynomialaredeterminedbyminimizingtheleastsquareserrorbetween
the polynomial and the data points within the window. The smoothed value yˆ at the point
i
| y is then | calculated | by evaluating | the | fitted polynomial | at  | x : |     |     |
| --------- | ---------- | ------------- | --- | ----------------- | --- | --- | --- | --- |
| i         |            |               |     |                   |     | i   |     |     |
m
(cid:88)
|     |     |     | yˆ  | =   | c y   |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     | i   |     | j i+j |     |     |     |
j=−m

107
Section3.3.Cyclone’sLifeCycleDetection
where c are the coefficients derived from the polynomial fit, and m represents half the
j
window size.
Usershavetheoptiontoapplythissmoothingtwice(Figure3.3d),adjustingthewindow
size 2m+1 and the polynomial order k to optimize the balance between noise reduction
and data fidelity. This flexibility allows users to fine-tune the filter settings to meet specific
requirements based on the spatio-temporal resolutions of various reanalysis datasets.
Subsequently, the first derivative of the relative vorticity is calculated predominantly
using second-order finite differences, with central differences applied to interior points and
first-order forward or backward differences used for endpoints. This derivative is then sub-
jected to double smoothing with the Savitzky-Golay filter to maintain a sinusoidal pattern
in the derivative series. This step is critical for accurately identifying cyclone lifecycle pha-
ses, making the dual smoothing process mandatory; omitting this could result in a noisy
derivative series, potentially leading to erroneous phase detections, which emphasizes its
necessity for reliable analysis.
The first phases to be detected are the intensification and decay stages. The program
achieves this by analyzing peaks and valleys in the relative vorticity time series data, as
showninFigure3.3e. Theintensificationphaseis defined astheperiod between apeakand
the subsequent valley (Figure 3.3f). Conversely, the decay phase is defined as the interval
between a valley and the following peak (Figure 3.3g). To ensure that only significant
phases are considered, each intensification and decay interval must span at least 7.5%
of the total length of the time series. This threshold helps filter out minor fluctuations
that are not indicative of true phase changes. To further refine the accuracy of phase
detection, the program checks for multiple blocks of consecutive intensification or decay
periods. If the gap between these blocks is smaller than 7.5% of the total series length, the
programmergesthemintoasingleperiod. Thismergingprocessiscrucialasitpreventsthe
fragmentation of significant phases due to short gaps, thereby providing a more accurate
and continuous representation of the intensification and decay stages.
After detecting the intensification and decay stages, the program proceeds to identify
the mature stage of the cyclone’s life cycle (Figure3.3h). This stage is determined by
analyzing not only the peaks and valleys in the relative vorticity but also the smoothed
derivative of vorticity. Between a peak and the subsequent valley (or a valley and the
subsequent peak) of the vorticity series, there is always a corresponding valley (or peak)

108
Chapter3.Data&Methods
in its derivative. These points indicate periods of maximum intensification or decay of
vorticity. The mature stage is defined as the interval between a vorticity valley and an
adjusted point calculated based on the derivative of vorticity. Specifically, the mature
stage spans from 12.5% of the time between the preceding derivative valley to 12.5% of the
time to the following derivative peak. To be recognized as a significant mature stage, each
interval must span at least 3% of the total length of the time series. This threshold ensures
that only substantial periods are classified as mature stages. Additionally, the program
verifies that all mature stages are preceded by an intensification stage and followed by a
decay stage. This verification step ensures that the mature phase is accurately identified
within the context of the entire cyclone life cycle.
Our methodology introduces the ’residual’ stage, which is not directly related to the
intrinsic development of extratropical cyclones but rather to peculiarities arising from the
tracking algorithms (Figure 3.3i). This stage is exemplified in Figure 3.4. Panel (a) illus-
trates the intensification of a cyclonic system near the southernmost part of Argentina.
The system reaches maturity, characterized by closed isobars at 850 hPa (Panel b). As the
system begins to decay, it displays open isobars and diminished relative vorticity cohesion
(Panel c). During its decay, it is influenced by a nearby system that leads to a tem-
porary increase in the magnitude of its central relative vorticity, indicating a temporary
re-intensification (Panel d). The tracking algorithm eventually discontinues its tracking,
categorizing this late period of intensification as ’residual’—a phase of late intensification
that is not associated with the primary development of the cyclone, as depicted in the
relative vorticity series (Panel e).
The CycloPhaser classifies stages as residual by analyzing the previously detected cy-
clone phases. For phases classified as mature that do not transition to a decay stage, these
instances are classified as residual. Similarly, if a full cycle of intensification, maturity,
and decay is followed by another intensification that does not lead to a mature phase, it
is also classified as residual (Figure 3.3i). This criterion accounts for scenarios where the
tracking algorithm may continue to follow a cyclone post-decay, potentially capturing a
re-intensification that does not culminate in a mature stage due to tracking limitations.
Following the residual phase classification, a post-processing step is applied to refine
cyclone phase identification. This step bridges any gaps that may appear between con-
secutive periods identified as intensification or decay phases. Specifically, the program

109
Section3.3.Cyclone’sLifeCycleDetection
Figure 3.4: Relative vorticity (shaded) and geopotential heights (contours) at 850 hPa, illustrating dis-
tinct stages of a cyclone’s lifecycle where a residual stage is present. Panel (A) shows the intensification
stage with isobars still open, indicating a strengthening system. Panel (B) depicts the mature stage, cha-
racterized by maximum organization and extent. Panel (C) illustrates the decay stage, with open isobars
and reduced relative vorticity cohesion. Panel (D) captures the residual phase, where, despite a general
trend of weakening, there is a temporary increase in vorticity influenced by external factors, not directly
associated with the primary development of the cyclone. The complete lifecycle of the system is depicted
in Panel (E), where each red dot on the vorticity series corresponds to the specific moments shown in
Panels (A) to (D).
scans for discontinuities within consecutive phase blocks and fills any identified gaps with
the adjacent phase to ensure smooth and continuous phase transitions. Additionally, this
step involves correcting isolated phases—those misclassified phases that last only one time
step—by aligning them with the subsequent phase if they occur at the start of the series,
or with the preceding phase elsewhere. This adjustment enhances the consistency of phase

110
Chapter3.Data&Methods
identification throughout the cyclone lifecycle.
Ironically, the final step of the CycloPhaser program involves identifying the incipient
stage, whichmarksthebeginningofcyclonedevelopment(Figure3.3j). Initially, allundefi-
ned periods in the time series are labeled as incipient. Subsequently, the program analyzes
the sequence of already labeled phases. If the life cycle commences with an intensification
phase, the program searches for a vorticity valley preceding the next mature stage. Should
such a valley be present, it designates the period from the start of the intensification phase
to 40% of the duration to this valley as incipient. Conversely, if the life cycle starts with
a decay phase, the program looks for a subsequent vorticity peak before the next mature
stage. Upon identifying such a peak, it marks the time from the start of the decay phase
to 40% of the duration to this peak as incipient.
The specific thresholds for phase detection, including the 7.5% duration for intensifica-
tion and decay intervals, the 3% minimum for the mature stage, and the 12.5% intervals
defining the boundaries of the mature stage, along with 40% of the series length for the in-
cipient stage, were established through rigorous testing. This testing involved an iterative
trial-and-error calibration process where various percentage thresholds were applied to a
representative sample of cyclone tracks. The objective was to determine the most accurate
parameters for delineating the phases. The chosen percentages proved effective in cap-
turing the true progression of cyclogenesis while filtering out inconsequential fluctuations
in vorticity. This meticulous calibration ensures that the CycloPhaser program reliably
identifies each phase, providing a consistent and objective methodology for analyzing the
life cycle of extratropical cyclones. This process is illustrated in Figures 3.5 and 3.6, 3.7,
3.8. For most of these thresholds, and in most cases analyzed, even altering the parameters
to 25% or 150% of their original values did not result in significant modifications to the
identified life cycle, reinforcing the method’s reliability.
3.3.2 Cyclophaser Settings
In this study, the default settings of the CycloPhaser were primarily utilized to identify
the life cycle phases of cyclones. Since the TRACK algorithm already incorporates spatial
filteringontheζ vorticityfields,applicationoftheLanczosfilterwasdeemedunnecessary
850
(Hodges, 1994, 1995). Nevertheless, the Savitzky-Golay filter was applied twice to ensure
that the ζ series exhibited a smooth sinusoidal profile. The window length of this filter
850

111
Section3.3.Cyclone’sLifeCycleDetection
Figure 3.5: Impact of varying threshold values for the minimum length of the intensification phase across
the six study cases. The original threshold value is maintained at 7.5% of the cyclone’s total life cycle
duration in panel (i). Panels (ii) to (vii) depict variations where the threshold is adjusted from 25%
to 175% of the original value, illustrating the method’s sensitivity to threshold changes. Adapted from
de Souza et al. (2024).
Figure 3.6: Same as Figure 3.5, but for the minimum length of the decay phase. Adapted from de Souza
et al. (2024).
was adjusted specifically for each system’s life cycle duration: for systems with a total life
cycle spanning 8 days, the window length was set to an odd integer approximately 25% of
the series length. For systems with shorter life cycles, the window length was adjusted to
an odd integer approximately 50% of the series length. In the second smoothing process,

| 112 |     |     | Chapter3.Data&Methods |     |
| --- | --- | --- | --------------------- | --- |
Figure 3.7: Variations in threshold values for the time intervals between the valley of vorticity and the
preceding derivative valley, as well as from the vorticity valley to the subsequent derivative peak, used
for determining the mature stage. The original threshold is set at 12.5%. Subsequent panels adjust this
threshold from 25% to 175% of the baseline value, evaluating the robustness of phase detection across six
| study cases. | Adapted from | de Souza | et al. (2024). |     |
| ------------ | ------------ | -------- | -------------- | --- |
Figure 3.8: Impact of varying the minimum length threshold for the incipient phase of cyclone develop-
ment. Theincipientphaseisidentifiedfromthebeginningofthevorticityseriestothenextpeakorvalley
in vorticity. The original threshold (shown in panel i) is set based on a percentage of the total vorticity
series length. Panels ii to vii display the results when this threshold is modified from 25% to 175% of its
| original value | across six | study cases. | Adapted from de Souza | et al. (2024). |
| -------------- | ---------- | ------------ | --------------------- | -------------- |
for life cycles exceeding 8 days, the window length was set to an odd integer close to 50%
of the series length; however, for shorter cycles, it was kept consistent with the initial

113
Section3.4.LorenzEnergeticsComputation
smoothing step.
3.4 Lorenz Energetics Computation
To compute the Lorenz Energy Cycle (LEC), an open-source Python application na-
med ”lorenz-cycle”was developed and is available on GitHub. The application is designed
for collaboration and transparency, allowing peers to freely use, modify, and review the
computation procedures. Full documentation and a user guide with illustrative examples
can be found at https://github.com/daniloceano/lorenz-cycle. The program uses
the formulation described at Section 2.4.2 and its complete description can be found at
Appendix B.
In this study, the lorenz-cycle program was configured to compute the dissipation
terms as residuals, following the methodologies of Brennan and Vincent (1980); Micha-
elides (1987); Veiga et al. (2008); Pezza et al. (2010); Dias Pinto and Rocha (2011), and to
use the Semi-Lagrangian framework (Michaelides et al., 1999). A 15◦×15◦ computational
domain centered at the cyclone’s central position, obtained from the TRACK database
(Section 3.2.2), was created for each time step. Given the impracticality of manually selec-
ting an appropriate domain size for each cyclone in the dataset, a fixed size was employed.
The focus here is on the environmental energetics directly related to cyclone develop-
ment, aiming to minimize interactions with other non-related circulations while capturing
the main structure of the cyclone. Defining cyclone size is challenging due to both metho-
dological and physical factors (Rudeva and Gulev, 2007, e.g.). The choice of a 15◦ ×15◦
computational domain is justified as it is large enough to capture the effective radius of
most cyclonic systems (Rudeva and Gulev, 2007). The effective cyclone radius is defined
as a measure of cyclone size, determined by establishing a coordinate system centered on
the cyclone and measuring the distance at which the radial pressure gradient first falls
to zero. This domain size also accounts for the cyclone’s structure (Gramcianinov et al.,
2019, e.g.).
Given the primary interest in the Southwestern Atlantic Ocean, only cyclones with
genesis near the South American coast (ARG, LA-PLATA, and SE-BR genesis regions)
were included in the LEC computation. A significant challenge in determining energe-
tic patterns across this dataset is the variable life durations of cyclones. Averaging va-

114
Chapter3.Data&Methods
lues across the entire life cycle of systems would aggregate distinct dynamical proces-
ses (e.g., intensification and decay), while technical limitations exist in dissecting the
life cycle into distinct periods. For example, Black and Pezza (2013) averaged cyclone
energetics over periods of 48 hours before explosive cyclogenesis, during explosive dee-
pening, and for 24 and 72 hours after it. However, cyclone life cycles can range from
less than 24 hours to over 10 days (Trigo, 2006; Reboita et al., 2010; Gramcianinov
et al., 2019), presenting significant physical limitations to such approaches. To address
these limitations, the Cyclophaser program was used. After computing the LEC for
each system, Cyclophaser was employed to define the life cycle phases for all analyzed
systems, and then the mean LEC values for each phase were computed. The files con-
taining the mean LEC results for each development phase are available on GitHub at
https://github.com/daniloceano/energetic_patterns_cyclones_south_atlantic.
3.5 Analysis methods
3.5.1 Probability Density Functions
In the present study, the probability density functions (PDFs) of distinct variables
analyzed were represented using the Kernel Density Estimation (KDE) from the Python
open-source library Seaborn (Waskom, 2021). KDE is a non-parametric method employed
toestimatethePDFofacontinuousrandomvariable(Parzen,1962;Rosenblatt,1956). Un-
like parametric approaches that assume a specific distribution form, KDE makes minimal
assumptions about the underlying data distribution, providing flexibility and robustness
in density estimation. The technique involves placing a kernel — a symmetric, smooth
function, typically Gaussian — on each data point and summing the contributions from
all kernels to produce a smooth, continuous estimate of the PDF. The bandwidth of the
kernel, a crucial parameter, controls the level of smoothing: a smaller bandwidth captures
more details of the data’s structure, while a larger bandwidth yields a smoother, more
generalized density function. KDE is particularly useful in visualizing the distribution of
data and identifying features such as multimodality, skewness, and the presence of outliers,
making it a valuable tool in exploratory data analysis and various scientific applications.

115
Section3.5.Analysismethods
3.5.2 Cyclone Track Densities
The spatial statistics from the TRACK program were produced using the spherical
kernel method developed by Hodges (1996). This method provides a robust framework for
estimating statistical properties from feature track data on a global scale. Unlike previous
exponential kernels, these spherical kernels — such as power, quadratic, and biweight ker-
nels—arecomputationallyefficientandlocallydefined, meaningtheirinfluenceisconfined
to a local region around each data point. The spherical kernel estimation is achieved by
calculating probability density functions directly on the sphere, thus avoiding distortions
caused by projection methods. This method includes an adaptive smoothing technique
that adjusts the smoothing parameter based on local data density, ensuring optimal ba-
lance between detail retention and noise suppression. Cross-validation is employed to
determine the optimal smoothing parameters, enhancing the reliability of the statistical
estimates. This approach is particularly valuable for analyzing climatological data.
3.5.3 Statistical Analysis
To determine if there were significant differences in LEC terms across different phases
of cyclone life cycles, we conducted a series of statistical tests. Initially, we assessed
the assumptions required for Analysis of Variance (ANOVA), which included normality
and homogeneity of variances. Normality was evaluated using the Shapiro-Wilk test, and
homogeneity of variances was assessed using Levene’s test. All statistical tests performed
here were employed using the open source Python package SciPy (Virtanen et al., 2020).
We used the Shapiro-Wilk test to assess the normality of each term’s distribution.
The p-value from this test indicates whether the data significantly deviate from a normal
distribution. A p-value greater than 0.05 implies that the data do not significantly deviate
from normality, indicating that the assumption of normality is met.
Levene’s test was used to evaluate the homogeneity of variances across different phases
for each term. The test statistic indicates the extent to which variances are equal across
groups. A high Levene’s test statistic suggests greater differences in variances. The p-value
associatedwithLevene’steststatisticindicatestheprobabilitythattheobserveddifferences
in variances could have occurred by chance. A p-value greater than 0.05 suggests that the
variances are not significantly different across the phases, implying that the assumption of

116
Chapter3.Data&Methods
homogeneity is met.
Given that many of our data sets did not meet these assumptions, we primarily em-
ployed the non-parametric Kruskal-Wallis (KW) test, which does not assume normality
or equal variances, to compare the distributions of each term across different phases. The
KW test is particularly useful when the data do not follow a normal distribution or exhibit
heterogeneous variances.
The KW test statistic measures the extent to which the medians of the groups differ.
A higher KW statistic value indicates a greater difference between group medians. The
corresponding p-value for the KW test statistic indicates the probability that the observed
differences in medians could have occurred by chance. A p-value less than 0.05 suggests
significant differences among the phases for that term.
To compare the vorticity data among different clusters, we conducted a non-parametric
statistical analysis due to the non-normal distribution of the data. Initially, we used the
KW test to assess if there were statistically significant differences in the vorticity dis-
tributions across the clusters. Following the identification of significant differences with
the KW test, we performed pairwise comparisons using the Mann-Whitney U test to de-
termine which specific clusters differed significantly. The Mann-Whitney U test is also
non-parametric and assesses whether the distributions of two independent groups are dif-
ferent. For each pairwise comparison, the test yields a U statistic and a p-value, where a
p-value less than 0.05 indicates a significant difference between the clusters. All statistical
analyses were executed using the SciPy package (Virtanen et al., 2020), and significant
differences were visually annotated on box plots to enhance interpretability.
3.5.4 Empirical Orthogonal Functions
To understand the dominant LEC variability patterns within the TRACK dataset,
an Empirical Orthogonal Function (EOF) analysis was employed using the Python open-
sourcelibrarypyEOF(Zheng,2021). EOFanalysisisastatisticaltechniqueusedtoidentify
the dominant modes of variability in spatial-temporal datasets (Fukuoka, 1951; Lorenz,
1956). It is one of the most used methods in atmospheric sciences, widely adopted for
exploratoryanalysis(Hannachietal.,2007). Themethodinvolvesdecomposingthedataset
into orthogonal patterns by performing an eigenvalue decomposition on the covariance
matrix of the data. Each EOF represents a spatial pattern, while the associated time

117
Section3.5.Analysismethods
series, or Principal Component (PC), describes the temporal evolution of that pattern.
This analysis reduces the dimensionality of the dataset, retaining the most significant
variability, and is particularly useful for uncovering underlying structures and patterns in
complex environmental data. In this context, instead of representing a spatial pattern,
each EOF presents a mode of variability of the LEC, while the PCs represent the evolution
across distinct cyclones.
3.5.5 K-means Algorithm
In the present study, the K-mean algorithm was used for determining the energetic
patterns associated with the cyclones in the SESA region. The K-Means algorithm (Mac-
Queen et al., 1967) is an iterative clustering method that partitions a dataset into K
distinct clusters, where each data point belongs to the cluster with the nearest mean (cen-
troid). The choice of K, the number of clusters, is crucial and is based on calculations to
obtain ideal values that explain the maximum variability. The initial theory of K-Means
was improved by Arthur and Vassilvitskii (2007) with the creation of K-Means++, which
is used for initializations in the K-Means implementation of the Python package ”Scikit-
Learn”(Pedregosa et al., 2011), utilized in this study. Instead of choosing all centroids
randomly, K-Means++ selects the first centroid randomly and then chooses subsequent
centroids based on a probability distribution proportional to the squared distance of data
points to the nearest already chosen centroid. This increases the likelihood that the initial
centroids are spread out across the data, reducing the probability of convergence to a local
optimum. In each iteration, the points are assigned to the cluster whose centroid is closest.
After the assignment, the centroids are recalculated as the mean of the points assigned to
each cluster. This calculation is performed until convergence, which the user can define as
the maximum number of iterations. At the end of these updates, the algorithm returns the
final clusters. The algorithm iterates between the steps of cluster assignment and centroid
updating until a stopping criterion is met. Typically, the algorithm terminates when the
centroids do not move significantly between consecutive iterations or when a maximum
number of iterations is reached.
Before applying the K-Means algorithm, we used the Elbow Method, a technique de-
signed to determine the optimal number of clusters. This method seeks a balance between
the explained variance and the number of clusters by identifying the inflection point in the

| 118 |     |     | Chapter3.Data&Methods |     |     |
| --- | --- | --- | --------------------- | --- | --- |
decrease of explained variance. Specifically, by plotting the explained variance against the
number of clusters, the inflection point on the graph indicates the optimal cluster count
| (Thorndike,       | 1953). |              |            |     |     |
| ----------------- | ------ | ------------ | ---------- | --- | --- |
| 3.6 Investigation |        | of Dynamical | Mechanisms |     |     |
| 3.6.1 Criteria    | Used   |              |            |     |     |
In this study, we utilized the Rayleigh–Kuo criterion for barotropic instability to de-
termine the presence of instability within cyclonic systems (Rayleigh, 1895; Kuo, 1949).
According to this criterion, the necessary condition for barotropic instability is the exis-
tence of a point where the gradient of absolute vorticity (η) with respect to the meridional
direction is zero and changes sign within the flow. This can be mathematically expressed
as:
∂η
|     |     |     | =   | 0   | (3.1) |
| --- | --- | --- | --- | --- | ----- |
∂y
Meanwhile,baroclinicinstabilitywasacessedusingtheEadygrowthrate,aquantitative
measure of the maximum rate of growth for baroclinic instabilities. This is a measure of
the maximum rate at which baroclinic instability can amplify disturbances in a stratified
| fluid, formulated | by Hoskins | and | Valdes (1990) | as: |     |
| ----------------- | ---------- | --- | ------------- | --- | --- |
(cid:12) (cid:12)
f (cid:12)∂u(cid:12)
|     |     |     | σ = 0.31 | (cid:12) (cid:12)    | (3.2) |
| --- | --- | --- | -------- | -------------------- | ----- |
|     |     |     | E        | N (cid:12)∂z(cid:12) |       |
where f is the Coriolis parameter, ∂u represents the vertical wind shear and N is the
∂z
Brunt-Va¨isa¨l¨a frequency, a measure of the stability of the stratification in a fluid such as
| the atmosphere | or ocean. | It is given | by the formula: |     |     |
| -------------- | --------- | ----------- | --------------- | --- | --- |
(cid:114)
gdθ
|     |     |     | N = |     | (3.3) |
| --- | --- | --- | --- | --- | ----- |
θdz
where g is the acceleration due to gravity, θ is the potential temperature and dθ is the
dz
| vertical gradient | of potential | temperature. |     |     |     |
| ----------------- | ------------ | ------------ | --- | --- | --- |
AlargervalueofN indicatesgreaterstability, meaningtheatmosphereismoreresistant
to vertical displacements. The Eady’s growth rate highlights the exponential growth of
certain atmospheric disturbances under favorable conditions of wind shear and stability.

119
Section3.6.InvestigationofDynamicalMechanisms
3.6.2 Composites
For applying the criteria described in Section 3.6.1, a composite procedure was imple-
mented. Firstly, it was necessary to determine the vertical levels at which baroclinic and
barotropic instabilities are indicated to be occurring, using the vertical profiles of C and
A
C , respectively. Then, mean values for atmospheric fields for the ERA5 reanalysis were
E
computed for the intensification phase at these vertical levels. The atmospheric fields used
were zonal, meridional, and vertical wind components, temperature, and geopotential.
ForthecompositesusingtheSemi-Lagrangianframework, firstly, themeanatmospheric
fields for the intensification phase for each system were averaged. These mean atmospheric
fields were then re-gridded to a non-dimensional spatial domain. Given that the ERA5
reanalysishasa0.25◦ horizontalspatialresolution, eachmeanfieldcontained60gridpoints
(15◦ × 15◦). As the Semi-Lagrangian domains are centered on the cyclone’s center, the
composite domain ranged from -30 to 30 grid points in both the x and y axes.
Furthermore, the differences between the Semi-Lagrangian and Fixed frameworks were
also assessed. While the methodology for the Semi-Lagrangian framework is explained in
Section 3.4, a distinct approach had to be taken for the Fixed framework. For each system
analyzed, a computational domain was automatically detected by using the minimum and
maximumlatitudeandlongitudevalues,addinga15◦×15◦ buffer. Bydoingso,itisensured
that the system’s complete development cycle is represented in the LEC computation.
For the composite procedure, firstly, the meteorological fields were averaged for each
computationaldomainduringtheintensificationphase. Then, theminimumandmaximum
latitude and longitude values across all fixed computational domains were detected. After
this, a synthetic domain was built using these coordinates, and the mean meteorological
fields were interpolated to this domain. Finally, the results interpolated to the common
grid for each case were averaged into a single composite.

120
Chapter3.Data&Methods

4
Chapter
Life Cycle of Cyclones in the Southwestern Atlantic
This chapter delves into the varied life cycle configurations, statistical characteristics,
and geographical distribution of cyclones within the Southwestern Atlantic, with a particu-
lar focus on the South American Southeastern region (SESA). Employing the Cyclophaser
program, this analysis facilitates a detailed examination of cyclone behaviors and patterns.
While some of the results discussed herein are also presented in (de Souza et al., 2024),
this chapter narrows its focus to the SESA region, unlike the cited study which includes
all cyclogenesis regions across the South Atlantic, extending to the Antarctic Peninsula
and the Weddell Sea. Section 4.1 examines statistical metrics for the selected cyclonic
systems’ whole life cycle, as well as for individual development phases, while Section 4.2
explores the spatial distribution of the distinct phases across the SESA and adjacent re-
gions. These two approaches combined not only provide a novel perspective on the South
Atlantic storm tracks and on the development of cyclonic systems but also open avenues
for future research, as will be discussed.
4.1 Climatology and Statistics
This section delves into the climatology and statistical characteristics of cyclones in the
Southwestern Atlantic, focusing on their frequency, seasonality, and developmental metrics
such as average duration and intensity. Previous analyses have explored these aspects for
systems originating in the SESA region; here, they serve both for comparative purposes
and for validating the database generated during this study. A novel aspect of this analysis
is the dissection of these metrics not just over the cyclones’ complete lifecycles but also
across distinct developmental phases. Section 4.1.1 presents the overall characteristics and

122
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
life cycle configurations of the detected cyclonic systems, Section 4.1.2 explores lifecycle
statistics for different genesis regions and seasons, and Section 4.1.3 provides detailed
statistical breakdowns by individual development phases.
4.1.1 Climatological Aspects and Life Cycle Configurations
Using the tracking methodology described in Section 3.2.2, the TRACK algorithm
identified 33,376 cyclone systems in the South Atlantic region from 1979 to 2020. The
focus here was on systems originating from the SESA region, specifically from SE-BR, LA-
PLATA, and ARG genesis regions. After filtering to include only these tracks, the number
of systems was narrowed down to 7,931 (Figure 4.1). Among these, 56% originated in the
ARG region, 23.6% in LA-PLATA, and 20.4% in SE-BR. This distribution and general
seasonality aligns with previous studies by Gramcianinov et al. (2019) and Crespo et al.
(2021). However, the SE-BR region exhibited a higher relative frequency in this analysis,
potentially attributable to the finer resolution of the ERA5 dataset used here compared
to previous studies (Gramcianinov et al., 2020). However, comparing the seasonal distri-
bution with earlier studies introduces complexities due to variations in the definitions and
boundaries of genesis regions (Reboita et al., 2010; Crespo et al., 2021, e.g.).
During the period from 1979 to 2020, cyclonic systems originating from the ARG, LA-
PLATA, and SE-BR regions demonstrated 41 distinct life cycle configurations (Figure 4.2).
Most configurations did not account for more than 1% of the total system count, typically
lacking a mature stage. This phenomenon is likely due to these systems having maturation
stages shorter than the CycloPhaser’s threshold for detecting this phase. Adjusting the
threshold to recognize shorter mature stages would risk identifying spurious cycles.
To focus on significant life cycle patterns, it was filtered the configurations to include
only those comprising at least 1% of all types (Figure 4.3). This criterion reduced the
sample size to 7,531 systems, accounting for approximately 95% of the original database.
It was also merged life cycle counts that differed solely by the inclusion of a residual stage,
as these are not indicative of the system’s actual development (as discussed in Section
3.3.1). Further, to avoid bias in phase statistics, it was excluded life cycles lacking a
mature phase. For instance, systems exhibiting only intensification and/or decay phases
might have longer durations for these phases compared to others, potentially skewing
statistics. Such configurations might represent undeveloped systems exiting the tracking

123
Section4.1.ClimatologyandStatistics
Figure4.1: NumberofsystemsandtheirrelativefrequenciesbygenesisregionintheSESAregionforthe
period 1979-2020. The inner pie chart displays the total frequency of systems by region, while the outer
ring shows the seasonal distribution of cyclogenesis within each region.
domain before maturation. With these filters applied, the number of systems analyzed was
reduced to 7,151, representing about 90% of the initial count of systems with genesis in
the SESA region (Figure 4.3b).
Figure 4.4 depicts representative cases for each life cycle configuration retained for
analysis (as shown in Figure 4.3b). The most common configuration in the SESA region
typically follows the expected development pattern of extratropical cyclones: incipient,
intensification, mature, and decay stages (Figure 4.4a), accounting for 68% of all evaluated
systems. The second most common type mirrors this sequence but omits the incipient
stage, indicating a rapid intensification process (Figure 4.4b). The third and fourth most
frequent types depict a repeated complete cycle, including a secondary intensification,
mature, and decay phases, with the third type including an incipient stage (Figure 4.4c)
and the fourth lacking one (Figure 4.4d). The fifth and sixth configurations exhibit an
early decay stage, differentiated by the presence (Figure 4.4e) or absence (Figure 4.4f) of
an incipient phase.

124
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Figure4.2: DistributionofallidentifiedcyclonelifecycleconfigurationsintheSESAregion,spanningfrom
1979to2020. Theconfigurationsaresortedbytheirtotalcount(frequency),witheachbarrepresentingthe
total number of cyclones exhibiting a specific lifecycle pattern, containing distinct stages: incipient (Ic),
intensification (It), mature (M), decay (D), and residual (R), showing their sequence within the lifecycle.
The analysis reveals minimal to negligible seasonal variability in the frequency of each
life cycle configuration across different genesis regions (Figure 4.5). The configurations ”Ic,
It, M, D”and ”Ic, It, M, D, It2, M2, D2”are consistently more frequent, jointly accounting
for 60% to 68% of all cases across all regions. However, exceptions include the ”It, M,
D”configuration emerging as the second most frequent in ARG during JJA, and in SE-BR
during MAM and JJA. Additionally, the ”Ic, D, M, D2”configuration appears significantly
more often in LA-PLATA during JJA and in SE-BR during SON.
4.1.2 Mean Cyclone Statistics
This section explores the statistical analysis of cyclones in the SESA region, comparing
the constrained data utilized in this study with extant literature. Results are presented
both for an aggregate view across all genesis regions and individually by region. To capture

Section4.1.ClimatologyandStatistics 125
Figure 4.3: (a) Lifecycle configurations of cyclones that represent at least 1% of the total identified
patterns. (b) Adjusted lifecycle configurations after merging periods classified as residual and removing
stages not contributing to a standard development pattern, focusing analysis on the core developmental
| stages of | cyclones. |     |     |     |     |     |
| --------- | --------- | --- | --- | --- | --- | --- |
Figure4.4: RepresentativeexamplesofcyclonelifecyclesforconfigurationsshowninFigure4.3b. Panels
AtoFillustratethecentralrelativevorticityζ anditsfirst(ζ )andsecond(ζ )smoothedderivatives.
|     |     |     | 850 |     | fs  | fs2 |
| --- | --- | --- | --- | --- | --- | --- |
Backgroundcolorsindicatedifferentlifecyclephases: : incipient(Ic), intensification(It), mature(M)and
decay (D). Lines represent the original vorticity series (ζ), the first (ζ ), and the second (ζ ) smoothed
fs fs2
| relative vorticity | series. |     |     |     |     |     |
| ------------------ | ------- | --- | --- | --- | --- | --- |
the seasonal variability of cyclone behavior, analysis is focused on the winter (JJA) and
summer (DJF) months. This approach is chosen because the transitional seasons (MAM
and SON) generally display characteristics that are intermediate to those observed in JJA
and DJF, aligning with findings from previous climatologies of the SESA region (Gan and
| Rao, 1991; | Reboita | et al., 2010; | Crespo | et al., 2021, | e.g.). |     |
| ---------- | ------- | ------------- | ------ | ------------- | ------ | --- |
On average, cyclones exhibit longer lifespans during DJF, with a duration of 97.6±66.2

126
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Figure 4.5: Similar to Figure 4.3, but separated by genesis region (ARG, LA-PLATA and SE-BR) and
season.
hours (Figure 4.6a) compared to 91.1±59.7 hours during JJA (Figure 4.6b). Conversely,
the average total distance traveled by cyclones is slightly greater during JJA, amounting
to 4777 ± 3182 km (Figure 4.6d), versus 4658 ± 3212 km in DJF (Figure 4.6c). This is
reflected in the mean propagation speed, which is higher in JJA at 15.3±4.8 m/s (Figure
4.6f) compared to DJF at 14.0±4.4 m/s (Figure 4.6e).
These results largely corroborate those by Gramcianinov et al. (2019, 2020); Hoskins
and Hodges (2005) and exceed the mean duration, traveled distance, and propagation
speed reported by Simmonds and Keay (2000), Mendes et al. (2010), and Reboita et al.
(2010). The disparities likely stem from differing tracking methodologies, data sets, and
theexclusionofsystemswithoutamaturephaseinouranalysis. Particularly, theexclusion
of continental systems may skew displacement statistics toward higher values during the
austral summer, as quasi-stationary lows, which tend to have minimal movement, are
prevalent over the continent (Mendes et al., 2010). Furthermore, Reboita et al. (2010)

127
Section4.1.ClimatologyandStatistics
Figure4.6: Probabilitydensityfunctions(PDF)comparingcyclonelifecyclemetricsacrossdifferentgenesis
regions (ARG, LA-PLATA, SE-BR) for DJF and JJA. Each panel displays the density distributions for a
specific metric: total time (A and B), total distance (C and D), mean speed (E and F), mean vorticity (G
and H), and mean growth rate (I and J). The lines in each graph represent the mean values for all regions
combined(black),ARG(blue),LA-PLATA(green),andSE-BR(red),whiletheannotationsrepresentthe
mean and standard deviation values.
focused on oceanic systems, which might have overlooked early development stages, and
theiruseofrelativevorticityat10m, impactedbysurfacedrag, couldaccountforvariations
in propagation speed.
The analysis reveals notable inter-regional variability in cyclone behavior, with trends
predominantly mirroring those observed in the ARG region, which accounts for the highest

128
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
frequencyofcycloneoccurrenceswithintheSESAregion(Figure4.1). Whenexaminingto-
tal cyclone duration, distinct seasonal patterns emerge: both the ARG and SE-BR regions
exhibit significantly shorter lifespans during JJA compared to DJF, with the probability
density functions (PDFs) peaking at approximately 50 hours. In contrast, the LA-PLATA
region shows slightly longer durations during JJA, with a mean difference of about 1.5
hours. Additionally, the distribution of cyclone durations in the LA-PLATA region is
more right-skewed than in ARG and SE-BR, indicating greater variability in the lifespan
of cyclones originating from LA-PLATA. Across all regions, the standard deviation decre-
ases from DJF to JJA, suggesting a higher occurrence of longer-lasting cyclones during the
summer months.
In terms of displacement, the ARG region displays shorter average distances during
DJF compared to JJA, whereas LA-PLATA and SE-BR exhibit increases, particularly
notable in SE-BR. This seasonal variation in SE-BR is likely due to the longer lifespan and
shorter displacement of cyclones during the summer, which are often associated with the
South American Convergence Zone, as well as the presence of shallow and smaller systems,
such as subtropical cyclones, that are typical in this period. In contrast, the ARG region
experiences shorter lifespans and greater displacements during the winter, likely related to
the influence of baroclinic waves.
In terms of displacement, the ARG region displays shorter average distances during
DJF compared to JJA, whereas LA-PLATA and SE-BR exhibit increases, particularly no-
table in SE-BR. Similar to the trends in duration, the displacement patterns in ARG and
SE-BR exhibit distinct peaks at approximately 2500 km, while LA-PLATA shows a more
right-skewed distribution, especially during JJA, indicating greater variability in cyclone
traveldistances. Theseregionaldifferencesindisplacementarealsomirroredintheaverage
propagation speeds of the cyclones: during DJF, cyclones in ARG generally move faster
than those in LA-PLATA and SE-BR. This changes in JJA, with SE-BR exhibiting the
highest increases in speed, making it the region with the most mobile cyclones during this
season, followed by ARG and then LA-PLATA. This variation is reflected in the PDFs for
each region: during DJF, SE-BR’s propagation speed peaks at approximately 10m s−1 and
ARG at 13m s−1, while LA-PLATA displays a bimodal distribution with peaks at appro-
ximately 10m s−1 and 15m s−1. During JJA, the peak for ARG shifts to approximately
16m s−1, and LA-PLATA’s distribution changes to peak at around 14m s−1, while SE-BR

129
Section4.1.ClimatologyandStatistics
assumes a bimodal shape, peaking at roughly 10m s−1 and 16m s−1.
The PDFs for the mean vorticity values of the examined systems display a bimodal,
right-skewed distribution with peaks near 2 × 10−5s−1 and 4 × 10−5s−1, with a higher
occurrence percentage near the first peak and an average value of 4±1.68×10−5s−1 during
DJF (Figure 4.6g). In JJA, the peaks are positioned near 2×10−5s−1 and 5×10−5s−1,
but with a higher occurrence percentage at the second peak, reflecting an overall increase
in mean vorticity, especially in the LA-PLATA region (Figure 4.6h). The ARG region
presents a PDF mirroring the mean cyclone behavior, and SE-BR peaks near 2×10−5s−1
in both seasons, being more right-skewed in JJA, which reflects the occurrence of weaker
systems in this region. Meanwhile, LA-PLATA shifts from being right-skewed in DJF
to left-skewed in JJA, reflecting a significant increase in the intensity of systems in this
region. These results highlight the previous findings that LA-PLATA presents the most
intense systems in the SESA regions, while SE-BR, the weakest (Simmonds and Keay,
2000; Reboita et al., 2010; Gramcianinov et al., 2019). Although the regional and seasonal
variability largely corroborates findings from Gramcianinov et al. (2019), the intensity of
cyclones reported here is somewhat smaller, possibly due to the ERA5 dataset be able to
detect less intense systems (Gramcianinov et al., 2020).
The mean growth rate distribution, is symmetric around zero with a low standard
deviation, indicating a dynamic equilibrium in system intensity throughout the life cycle,
marked by neither consistent intensification nor weakening, which will be later discussed
for each individual phase. It is important to note that these values were computed from
normalized relative vorticity data, where positive values suggest system intensification
(ζ increasing in magnitude), while negative values indicate a decay (ζ decreasing in
850 850
magnitude). Overall, although the differences are minimal, the results suggest slightly
more intense intensification during DJF (Figure 4.6i) compared to JJA (Figure 4.6j), with
the latter exhibiting higher mean values.
4.1.3 Life Cycle Phase Statistics
This section examines the statistical characteristics of cyclones, exploring various me-
trics describing cyclonic behavior throughout distinct lifecycle phases. This unique ap-
proach is enabled by the Cyclophaser program, offering a more granular analysis than
previously available in the literature. As shown in Section 4.1.2, the region mean results

130
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
predominantly reflect the ARG region’s behavior and hence, region-specific results are
detailed here.
Figure 4.7 displays the PDFs for the mean total time spent in each development phase.
These PDFs are right-skewed, indicating high variability across different phases but smal-
ler seasonal and regional differences. Typically, the incipient, mature, and second mature
phases show the shortest average durations, often peaking between 3 and 5 hours. The in-
tensification, second intensification, and decay phases often exhibit longer tails, suggesting
a wide variability in their durations. In the ARG region, all phases show a slight reduction
in mean duration from DJF (Figure 4.7a) to JJA (Figure 4.7b), with decay and second
decay stages exhibiting the most significant reductions, indicating that shorter average
total durations in JJA are primarily due to these phases (Figure 4.6). For LA-PLATA
and SE-BR, notable changes include particularly variations in the standard deviations of
the second intensification and decay phases, and in the decay phase for SE-BR, suggesting
that seasonal differences in total mean durations for these regions are largely attributable
to fluctuations in extreme values.
Figure 4.7: Probability density functions (PDF) comparing the mean total duration of each cyclone
phase, across all regions combined and for each genesis region (ARG, LA-PLATA, SE-BR) for DJF and
JJA. Annotations display mean and standard deviation values for each phase.

131
Section4.1.ClimatologyandStatistics
The total traveled distance for each phase is depicted in Figure 4.8, which mirrors the
overallbehaviorobservedfortotaltime(Figure4.7). AllPDFsareright-skewed, andacross
all regions and seasons, the incipient, mature, and second mature phases peak approxima-
tely between 300 and 400 km, while the other phases present long tail distributions. In
the ARG region, there is an overall reduction in traveled distance across all phases from
DJF to JJA. Conversely, for LA-PLATA and SE-BR, there is a general increase, reflecting
the seasonal behavior for the entire lifecycle’s total distance (Figure 4.6).
Figure 4.8: Similar to Figure 4.7, but for total traveled distance.
Theresults formeanspeed (Figure4.9)aggregate theresultsfor total timeandtraveled
distance. There is less variability across distinct phases for this metric when compared to
the total time and distance, with the PDFs for distinct phases, regions, and seasons often
presenting a Gaussian-like shape centered between 10 and 15 ms−1. These values align
withthosefoundinpreviousstudies(Gramcianinovetal.,2019,2020;HoskinsandHodges,
2005), although slightly higher, likely due to the constraints adopted in this analysis.
Additionally, this study’s ability to account for distinct developmental phases provides a
foundation for further research into the dynamical mechanisms that could be linked to the

132
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
systems’varyingspeedsacrossdifferentperiods. IntheARGregion, thelargestincreasesin
mean propagation speed from DJF to JJA are found in the secondary development phases,
accompanied by increases in standard deviation values, with slightly right-skewed PDFs
for these phases. LA-PLATA displays a similar behavior, especially for intensification
and mature decay, which shifts their peaks from near 10ms−1 in DJF to near 15ms−1 in
JJA. For SE-BR, the major change is in the shape of the PDFs, which change from a
Gaussian-like shape in DJF to a more right-skewed shape in JJA. Overall, although the
differences are only marginal, the cyclones tend to be faster in the incipient stage and in
the intensification stage, being slower at the mature phase, speeding up again in the decay
phase.
Also, the systems tend to be slower in the second development cycle than in the first
one, especially during the second mature phase. This slower movement in the mature
phase is likely not unique to cyclones in the SESA region but a common characteristic of
many cyclones. As they reach maturity, cyclones often become more barotropic-equivalent,
resulting in a slower movement of the entire system at both upper and lower levels. Additi-
onally, asairmassesbecomemoremixed, thereducedtemperaturegradientsatlowerlevels
contribute to the slower displacement, in line with QG theory. The slower propagation
speed of cyclones is related to extreme wave occurrence (Gramcianinov et al., 2023) and
therefore the positioning of these systems during that phase are of importance for coastal
management in the South American Southeastern coast.
ThePDFsformeancentralζ acrossvariouscyclonephasesexhibitbimodalandright-
850
skewed distributions, with a general increase in mean vorticity from DJF to JJA (Figure
4.10). ThistrendreflectstheheightenedintensityofcyclonicsystemsduringJJAcompared
to DJF (Figure 4.6). It is important to note that these vorticity values are derived from
the raw output of the TRACK program, and as such, they may include some level of noise
that can influence the statistical results. Notably, the mature phase is characteristically
the most intense during the first developmental cycle across all regions, demonstrating a
wide range of vorticity values and highlighting the variability in peak intensities of mature
cyclones. Meanwhile, the second mature phase typically records the highest vorticities
among all phases, suggesting a tendency for systems to intensify further during subsequent
cycles. In contrast, the incipient phase generally exhibits the lowest mean vorticities,
reflecting the nascent stages of cyclone development. However, in the SE-BR region, this

133
Section4.1.ClimatologyandStatistics
Figure 4.9: Similar to Figure 4.7, but for mean propagation speed.
phase shows unusually high mean vorticities during JJA, occasionally surpassing other
phases, indicating exceptionally conducive conditions for early cyclone formation. The
intensification and decay phases generally present similar mean vorticities, aligning with
their respective roles in modifying system intensity: intensification increases vorticity from
abaselinestate,whiledecayreducesitbacktowardsthisbaseline. Secondaryintensification
and decay phases often exhibit higher mean vorticities than their initial counterparts,
reflecting the dynamics of re-intensification in the lifecycle, particularly marked by the
higher mean values observed during the second mature phase.
The results found here for the incipient stage exhibit higher vorticities compared to
the initial vorticities reported by Reboita et al. (2010), Gramcianinov et al. (2019), and
Gramcianinov et al. (2020). This discrepancy may be attributed to our exclusion criteria,
which likely excluded weaker and underdeveloped systems, coupled with the observed
tendency for vorticity to increase (becoming more negative) when an incipient stage is
followed by an intensification phase (e.g., Figure 4.4a and c), potentially resulting in a bias
toward higher values for this phase. Additionally, Sinclair (1995), in their analysis focusing

134
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Figure 4.10: Similar to Figure 4.7, but for mean central relative vorticity at cyclone center (zeta ).
850
on the first time step, the time step of minimum vorticity, and the last time step, reported
highervorticityvaluescomparedtoourfindingsfortheincipient, mature, anddecaystages.
However, these authors omitted the influence of topography by using geostrophic relative
vorticity, which justifies the difference in vorticity distribution observed in their study.
There are complexities in interpreting the results for the mean growth rate due to the
use of raw vorticity data from the TRACK algorithm, which introduces additional noise
to the findings (Figure 4.11). This metric exhibits considerable variability across diffe-
rent regions, with most PDFs centered around zero yet displaying wide variations, where
standard deviations significantly exceed the mean values. The incipient stage often shows
the highest or second-highest growth rates, typically skewing more to the right. These
observations are consistent with previously reported mean growth rates for cyclogenesis
regions by Hoskins and Hodges (2005) and Gramcianinov et al. (2019). A similar pattern
is observed in the intensification phase, which alternates with the incipient stage in dis-
playing the greatest growth rates. Despite positive average values, the decay and second
decay phases predominantly peak at negative values, reflecting their role in diminishing

135
Section4.1.ClimatologyandStatistics
system vorticity.
Figure 4.11: Similar to Figure 4.7, but for mean growth rate.
While most regions and seasons show the mature phase peaking at zero — expected
due to its position near local vorticity minima — the positive mean suggests that the
increase in vorticity preceding the peak is more pronounced than the subsequent decline.
This assertion is supported by the lower mean values observed during the decay phase
compared to the intensification phase. Moreover, the detection of the mature phase often
occurs between the peaks and valleys of vorticity derivatives (Section 3.3.1), potentially
shifting its center of mass toward either the intensification or decay stages, as depicted
in Figure 4.12. During JJA in LA-PLATA, the mature phase peaks positively, whereas
in SE-BR during DJF, it peaks negatively. Determining whether these shifts are due to
greater increases in intensity, displacement of the phase’s center of mass, or residual data
noise is beyond this study’s scope.

| 136 |     | Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic |            |         |                 |     |     |
| --- | --- | ----------------------------------------------------- | ---------- | ------- | --------------- | --- | --- |
|     |     | (A)                                                   | (B)        |         | (C)             |     |     |
|     |     |                                                       | ζfs mature | ζvalley | ∂ζvalley ∂ζpeak |     |     |
Figure 4.12: Illustrative example of how the center of mass of the mature phase can be displaced: (A)
Symmetrically around the vorticity valley (∂ζ ) when distances to the first derivative valley (∂ζ )
|     |     |     | valley |     |     |     | valley |
| --- | --- | --- | ------ | --- | --- | --- | ------ |
andpeak(∂ζ )areequal. (B)Displacementtowardsthepreviousphasewhen∂ζ isclosertoζ .
|     | peak |     |     |     |     | peak | valley |
| --- | ---- | --- | --- | --- | --- | ---- | ------ |
(C) Displacement towards the subsequent phase when ∂ζ is closer to ζ .
|             |              |     |            | valley | valley       |     |     |
| ----------- | ------------ | --- | ---------- | ------ | ------------ | --- | --- |
| 4.2 Spatial | Distribution |     | of Cyclone | Life   | Cycle Phases |     |     |
The current section explores the spatial distribution across the SESA region of the
distinct phases of cyclone development: incipient (Section 4.2.1), intensification (Section
4.2.2), mature (Section 4.2.3), decay (Section 4.2.4) and the secondary development cycle,
as well the residual phase (Section 4.2.5). The analysis focuses only on systems that
presented a mature phase to avoid including underdeveloped systems, those that might
not have exhibited a mature phase before leaving the tracking domain, or cases where the
maturation stages were shorter than the CycloPhaser’s threshold for detecting this phase
(as discussed in Section 4.1.1). The track density ranges differ from one figure to the other
as does not make sense to compare track density between distinct phases, as those differ
| in duration     | and in | total displacement | (Section | 4.1.3. |     |     |     |
| --------------- | ------ | ------------------ | -------- | ------ | --- | --- | --- |
| 4.2.1 Incipient | Phase  |                    |          |        |     |     |     |
Figure 4.13 illustrates cyclone track density (cyclones per 106km2 per month) during
the incipient phase for DJF and JJA in the SESA region. Given that transitional seasons
display intermediate characteristics between these extremes (Gan and Rao, 1991; Reboita
et al., 2010; Crespo et al., 2021, e.g.,), our analysis primarily focuses on DJF and JJA,
encompassing the cyclogenesis regions of ARG, LA-PLATA, and SE-BR. As expected, the
track density for the incipient phase correlates with these genesis regions (Figure 4.13a
and b).
The ARG region consistently shows similar track densities in both DJF (Figure 4.13c)
and JJA (Figure 4.13d), exceeding 30 cyclones per 106km2 per month. In contrast, LA-
PLATAandSE-BRregionsexhibitnoticeableseasonalpatterns. LA-PLATAseesincreased

137
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
Figure 4.13: Cyclone track density during the incipient phase for all systems with genesis in the ARG,
LA-PLATA and SE-BR regions. Panels A and B show the aggregate density across all regions for DJF
and JJA, respectively. Panels C to H depict individual genesis regions: ARG (C and D), LA-PLATA (E
and F), and SE-BR (G and H) for DJF (left panels) and JJA (right panels). The unit is cyclones per
106km2 per month.

138
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
activity in JJA (Figure 4.13f) compared to DJF (Figure 4.13e), with densities rising above
20 and 10 cyclones per 106km2 per month, respectively. Conversely, SE-BR demonstrates
higher activity in DJF (Figure 4.13g) than in JJA (Figure 4.13h), with densities exceeding
10 and 8 cyclones per 106km2 per month, respectively. This seasonality is consistent with
findings from previous studies (Gan and Rao, 1991; Hoskins and Hodges, 2005; Mendes
etal.,2010;Reboitaetal.,2010;Gramcianinovetal.,2019;Crespoetal.,2021). Variations
in reported track density values by (Gramcianinov et al., 2020, 2019) may arise from
different methodologies; those studies analyzed only the initial time step of the system life
cycle, while this study considers all periods classified as the incipient stage. Additionally,
Gramcianinov et al. (2019) utilized the NCEP-CFSR reanalysis database for tracking, in
contrast to the ERA5 dataset employed here.
4.2.2 Intensification Phase
The track densities during the intensification phase (Figure 4.14) exhibit significantly
higher values compared to the incipient stage. This is expected due to the longer duration
of the intensification phase, as discussed in Section 3.3.1. Across all genesis regions, during
bothDJF(Figure4.14a)andJJA(Figure4.14b), themaximumtrackdensityextendsfrom
approximately 60◦W to 20◦W. The central concentration around 50◦S, particularly during
bothseasons, isprimarilycomposedofsystemsoriginatingintheARGregion(Figure4.14c
and d). During DJF, the maximum density region, extending eastward/southeastward
from the incipient stage, reaches up to 100 cyclones per 106km2 per month, while in JJA,
it shows a slight decrease to 80 cyclones per 106km2 per month, with a predominantly
eastward orientation. The higher track density and the cyclones reaching further east in
DJF can be attributed to the longer mean duration of the intensification phase for systems
from ARG, as shown in Figure 4.7, and the overall greater displacement distances during
this phase across all genesis regions, as indicated in Figure 4.8.
Moreover, the maximum track density at around 50◦S for the ARG region connects
with the track densities for the LA-PLATA and SE-BR regions. LA-PLATA shows higher
activity during JJA (Figure 4.14f), with track densities reaching 50 cyclones per 106km2
per month, compared to 40 during DJF (Figure 4.14e). Conversely, SE-BR exhibits higher
activity during DJF (Figure 4.14g), with densities reaching 40 cyclones per 106km2 per
month, compared to 20 during JJA (Figure 4.14h). This seasonality for both LA-PLATA

139
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
Figure 4.14: Cyclone track density during the intensification phase for all systems with genesis in the
ARG, LA-PLATA and SE-BR regions. Panels A and B show the aggregate density across all regions for
DJFandJJA,respectively. PanelsCtoHdepictindividualgenesisregions: ARG(CandD),LA-PLATA
(E and F), and SE-BR (G and H) for DJF (left panels) and JJA (right panels). The unit is cyclones per
106km2 per month.

140
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
and SE-BR regions reflects the seasonality in cyclogenesis (Figure 4.1) and consequently, of
the incipient phase (Figure 4.13). Consequently, in the aggregate densities for all regions
during DJF (Figure 4.14a), the SE-BR region’s signal is more apparent near 30◦S and
40◦W. In JJA (Figure 4.14b), the track density associated with LA-PLATA is evident as
themaximumtrackregionextendssoutheastwardfromnear35◦Sand55◦W(Figure4.14f).
Furthermore, for the LA-PLATA region, it can be seen that during JJA, the systems tend
to reach further southeast, associated with higher mean displacements (Figure 4.8).
Notably, the track densities for the intensification phase across all genesis regions show
far-reaching systems that intensify throughout the entire South Atlantic basin, extending
as far as 30◦E or even 60◦E. While the orientation of the track density for the ARG
regionispredominantlyeastward, forLA-PLATAandSE-BR,thetracksaresoutheastward
oriented. Thisresultsinaconcentrationoftrackdensitiesbetween40◦Sand60◦S,displaced
more northward during JJA than DJF, indicating a preference for systems to intensify in
this region, which corresponds to the storm track path for the South Atlantic (Hoskins
and Hodges, 2005; Gramcianinov et al., 2019).
4.2.3 Mature Phase
In the mature phase, there is a notable reduction in track densities compared to the
intensification phase, with maximum values decreasing from 100 to to 20 cyclones per
106km2 per month. During DJF, the aggregate for all genesis regions shows two principal
maximum track density areas (Figure 4.15a). The first area, centered near 35◦S and 45◦W,
exhibits a lower maximum track density reaching 14 cyclones per 106km2 per month,
predominantly associated with cyclones originating in the LA-PLATA and SE-BR regions
(Figures 4.15e and 4.15g). The second area, located near 55◦S and 30◦W, reaches up to 18
cyclones per 106km2 per month and is primarily associated with systems from the ARG
region (Figure 4.15c). During this season, maximum track densities for ARG, LA-PLATA,
and SE-BR peak at 16, 9, and 10 cyclones per 106km2 per month, respectively.
In JJA, the primary track density maximum for the aggregate is located near 45◦S
and 45◦W, slightly westward compared to the DJF maximum, with secondary maxima to
the north and northeast, each reaching 12 cyclones per 106km2 per month (Figure 4.15b).
This lower density compared to DJF reflects shorter mature phase durations and reduced
mobility of systems from the ARG region during JJA, as shown in Figures 4.7 and 4.8.

141
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
Figure 4.15: Cyclone track density during the mature phase for all systems with genesis in the ARG,
LA-PLATA and SE-BR regions. Panels A and B show the aggregate density across all regions for DJF
and JJA, respectively. Panels C to H depict individual genesis regions: ARG (C and D), LA-PLATA (E
and F), and SE-BR (G and H) for DJF (left panels) and JJA (right panels). The unit is cyclones per
106km2 per month.

142
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Notably, the track density center for the ARG region shifts from near 45◦W during DJF
to around 55◦W during JJA(Figure 4.15d), indicating a tendency for systems to mature
closer to their intensification locations, which is also indicated by the lower mobility of
these systems when compared to the other genesis regions for this period (Figure 4.8).
Secondary maxima near 35◦S and 45◦S result from overlaps in tracks from all regions, with
LA-PLATA contributing significantly (Figure 4.15f). Although this overlaps with a center
fromSE-BR,thetrackdensitymaximumforSE-BRduringJJAremainslow, notexceeding
5 cyclones per 106km2 per month(Figure 4.15h), while for LA-PLATA, it reaches up to 7
near 55◦W and 6 near 45◦W.
Overall,thedensitymaximumcentersforthematurephasearedisplacedsoutheastward
from those for the intensification phase for DJF and east/southeastward for JJA. Tracks
are typically found between 40◦S and 60◦S, aligning with the storm track path for the
South Atlantic. For DJF, most tracks are located south of 50◦S, while for JJA, they
are predominantly north of 50◦S. This pattern is more pronounced during the mature
phase than during the intensification phase, with the southward shift during DJF largely
associated with cyclones originating in the ARG region, while a maximum density region
closer to Uruguay and Southern/Southeastern Brazil is mostly linked with LA-PLATA and
SE-BR genesis regions.
4.2.4 Decay Phase
The decay phase generally exhibits increased track densities compared to the mature
phase, with maximum values reaching 40 cyclones per 106km2 per month, but still lower
than observed during the intensification phase. During DJF, two primary centers of maxi-
mum track density are observed: one near 35◦S, close to Uruguay and South/Southeastern
Brazil (Figure 4.16a), and another near 55◦S, west of the Weddell Sea (Figure 4.16a). The
latter, primarily influenced by cyclones from the ARG region, reaches up to 35 cyclones per
106km2 per month (Figure 4.16c). The former, influenced by the LA-PLATA and SE-BR
regions, records densities of up to 13 and 30 cyclones per 106km2 per month, respectively
(Figures 4.16e and 4.16g).
For JJA, two primary density maxima are identified: one centered at 45◦S, spanning
from 60◦W to 20◦W, and another near 35◦S and 40◦W, with both areas achieving track
densities up to 35 cyclones per 106km2 per month (Figure 4.16b). The former is predo-

143
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
Figure 4.16: Cyclone track density during the decay phase for all systems with genesis in the ARG,
LA-PLATA and SE-BR regions. Panels A and B show the aggregate density across all regions for DJF
and JJA, respectively. Panels C to H depict individual genesis regions: ARG (C and D), LA-PLATA (E
and F), and SE-BR (G and H) for DJF (left panels) and JJA (right panels). The unit is cyclones per
106km2 per month.

144
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
minantly linked to systems from the ARG region, where densities reach 30 cyclones per
106km2 per month (Figure 4.16d), while the latter is influenced by the SE-BR and es-
pecially the LA-PLATA regions, showing densities of 10 and 15 cyclones per 106km2 per
month, respectively (Figures 4.16h and 4.16f). Additionally, a notable center of density,
although less pronounced, emerges in the LA-PLATA region, associated with systems that
enter an early decay phase (Section 4.2.5).
For the ARG region, the decay phase densities are typically shifted southeastward from
those of the mature phase during DJF and mostly southeastward/eastward during JJA,
with some systems extending westward to the Weddell Sea. This pattern highlights a
seasonal variation in the decay behaviors of systems within the SESA region. Moreover,
for both LA-PLATA and SE-BR, decay densities are generally proximate to those of the
mature phase but extend further southeastward, reaching as far south as 70◦S and as far
east as 30◦E. This expansive spread into the southern Atlantic aligns with findings by
Hoskins and Hodges (2005), who identify the region south of 60◦S and west of the Weddell
Sea as the primary dissolution area for cyclones in the South Atlantic.
4.2.5 Secondary Development Phases
For analyzing the track densities for the phases related to the systems’ secondary de-
velopment, the results are shown as yearly values rather than by seasonal variability, as
done in previous sections. This approach is due to the lower frequency of systems under-
going secondary development compared to those that do not (Figure 4.3). Additionally,
as shown in Section 4.1.1, the number of systems presenting early intensification or decay
phases is comparable to those with secondary development stages. Therefore, the analysis
here focuses on systems that exhibited a complete secondary development cycle: incipient,
intensification, mature, decay, intensification 2, mature 2, and decay 2. Figure 4.17 illus-
trates the track density differences when other life cycle configurations are included in the
analysis. The occurrence of early intensification and decay phases impacts the overall track
density distribution, with maximum density centers between 30◦S and 40◦S, centered near
45◦W (Figures 4.17a and 4.17c). These centers disappear when the analysis focus only on
the systems with a complete secondary development (Figures 4.17b and 4.17d).
For the second intensification phase, there is a maximum track density region south
of South Africa, with 30 cyclones per 106km2 per month (Figure 4.18a). This maximum

145
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
Figure 4.17: Cyclone track density for the secondary development stages. Panels A and B display the
phase intensification 2, while panels C and D, phase decay 2. Panels A and C show the results when all
life cycle configurations are included in the analysis, while panels B and D show the results when only the
systems that exhibited a complete secondary development cycle - incipient, intensification, mature, decay,
intensification 2, mature 2, and decay 2 - are analysed. The unit is cyclones per 106km2 per month.

146
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
density region is related to the aggregate occurrence of systems from all genesis regions and
closely matches the SE-SAO cyclogenesis region reported by Gramcianinov et al. (2019).
Gramcianinov et al. (2019) highlighted a potential link between this region and secondary
cyclogenesis. It is possible that some of the detected re-intensifications might stem from
secondary cyclogenesis events or spurious links by the TRACK algorithm, which could mix
weak decaying systems with incipient secondary cyclones. While secondary cyclogenesis
generally follows a frontal wave post an extratropical cyclone’s passage (Mailier et al.,
2006; Shapiro et al., 1997; Ford et al., 1990; Rivals et al., 1998), the CycloPhaser program
classifies a phase as ”intensification 2”whenever the ζ series indicates a pattern of incre-
850
ases in its magnitude, followed by subsequent mature and decay phases. This secondary
intensification could result from a decaying wave at 850 hPa finding favorable conditions
for subsequent intensification. Alternatively, the surface cyclone might have already dis-
sipated, but there is still a signal of it in the ζ field, causing the TRACK algorithm to
850
continue tracking a weak decaying trough at 850 hPa. In these instances, the CycloPhaser
may classify this weak intensification as ’residual’ should it not progress to a mature stage
(Section 3.3.1). Conversely, if the TRACK algorithm mistakenly associates this decaying
wave with a newly forming cyclone nearby, the CycloPhaser would label this transition as
”intensification 2,”introducing potential analysis errors. However, distinguishing between
true secondary genesis and re-intensification remains beyond this study’s scope. Further-
more, notably, there is a track density maxima near Uruguay and South Brazil associated
with LA-PLATA systems.
The second mature phase, characterized by its overall low track density, presents a
diffuse spatial distribution. This low track density is primarily due to the infrequent oc-
currence of secondary development in SESA systems (Figure 4.3) and the fact that it
exhibits the lowest displacement and duration across all phases (Figures 4.8 and 4.7).
However, a notable maximum track density is centered at 60◦S and 50◦E, with 2 cyclo-
nes per 106km2 per month (Figure 4.19a). This peak is mainly associated with systems
from ARG and SE-BR (Figures 4.19b and 4.19d). A weaker density maximum is found to
the west, between 10◦E and 20◦E, predominantly linked to systems from LA-PLATA (Fi-
gure 4.19c). For all regions, the track density regions are mostly displaced southeastward
compared to the intensification 2 phase.
The second decay phase displays the systems in their southernmost and easternmost

147
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
Figure 4.18: Cyclone track density during the second intensification phase for all systems with genesis in
the ARG, LA-PLATA and SE-BR regions that display a complete secondary development cycle. Panel A
shows the aggregate density across all regions. Panels B to D depict individual genesis regions: ARG (B),
LA-PLATA (C), and SE-BR (D). The unit is cyclones per 106km2 per month.

148
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Figure 4.19: Cyclone track density during the second mature phase for all systems with genesis in the
ARG, LA-PLATA and SE-BR regions that display a complete secondary development cycle. Panel A
shows the aggregate density across all regions. Panels B to D depict individual genesis regions: ARG (B),
LA-PLATA (C), and SE-BR (D). The unit is cyclones per 106km2 per month.

149
Section4.2.SpatialDistributionofCycloneLifeCyclePhases
positions, with track densities extending up to 140◦E and bordering the Antarctic conti-
nent. All three genesis regions present a track density maximum centered between 60◦E
and 110◦E, with the resulting aggregate displaying up to 8.5 cyclones per 106km2 per
month (Figure 4.20a). Individually, each genesis region has a track maximum of approxi-
mately 2to 3 cyclones per 106km2 per month, with LA-PLATA displaying a second weaker
maximum between 20◦E and 40◦E, with up to 2 cyclones per 106km2 per month (Figure
4.20c). This region also presents the highest density values northwestwards, contributing
to the track densities near 40◦S.
Across all second development phases, a weaker albeit noticeable track density region
is present near the SE-BR genesis area. This region also shows occurrences of subtropical
cyclones Evans and Braun (2012); de Jesus et al. (2022); Cardoso et al. (2022), especially
duringDJFmonths, whereapproximately30%ofthesystemsexhibithybridcharacteristics
Gozzo et al. (2014). Previous works analyzing case studies of such systems that have
genesisintheSE-BRregionrevealthattheypresentcomplexlifecycles, oftentransitioning
betweendifferenttypesofcyclonicsystemsandpresentingmultiplestagesofintensification,
maturation, and decay (Dias Pinto et al., 2013; Veiga et al., 2008; Reboita et al., 2022;
Dutra et al., 2017; Reboita et al., 2021, e.g.,). Consequently, one can speculate that some
of the systems related to these track density regions near SE-BR might be subtropical.
However, further analysis would be needed for confirm this assertion, which is beyond the
scope of the current work.
4.2.6 Residual Phase
The residual phase, though not representing a physical stage of cyclone development,
plays an important role in identifying tracking and detection inconsistencies, highlighting
potential areas for methodological improvement. This phase typically includes systems
that experience temporary intensification due to favorable environmental factors but fail
to progress into mature cyclones. Identifying the residual phase involves detecting situa-
tions where a system’s central vorticity increases outside the standard development cycle,
often influenced by nearby systems or localized atmospheric conditions that promote brief
intensification (Section 3.3.1).
Figure 4.21 shows the track densities across all regions and seasons. A noticeable track
density maximum is present near Uruguay and South Brazil, over the Brazil-Malvinas

150
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Figure 4.20: Cyclone track density during the second decay phase for all systems with genesis in the
ARG, LA-PLATA and SE-BR regions that display a complete secondary development cycle. Panel A
shows the aggregate density across all regions. Panels B to D depict individual genesis regions: ARG (B),
LA-PLATA (C), and SE-BR (D). The unit is cyclones per 106km2 per month.

151
Section4.3.SummaryandConcludingRemarks
confluence (Gordon, 1989). The confluence region presents low-level baroclinicity, which
can be transferred upwards in the atmosphere (Sanders and Gyakum, 1980; Vera et al.,
2002, e.g.,). Systems passing over the confluence might experience brief intensification due
to favorable conditions but not achieve maturity. This could also be important for systems
with genesis in SE-BR, which are often weaker (Sinclair, 1995; Hoskins and Hodges, 2005).
Furthermore, the track density maximum near 40◦E and 55◦S indicates that upper-level jet
support(Swartetal.,2015, e.g.,) andabaroclinicenvironment(HoskinsandHodges,2005,
e.g.,) could similarly drive marginal intensification, leading to a residual classification.
Figure 4.21: Cyclone track density during the residual phase for all systems with genesis in the ARG,
LA-PLATA and SE-BR regions. The unit is cyclones per 106km2 per month.
4.3 Summary and Concluding Remarks
ThischapterintroducedCycloPhaser, anovel, open-sourcePythonpackageforautoma-
tedcyclonelifecycledetection, availableonthePyPI repository. Itslowmemoryfootprint,
flexibility, andrapiddeploymentcapabilitiesmakeitavaluableassetforclimatologicalstu-

152
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
dies or even operational forecasts. The TRACK program identified a total of 7,931 systems
from 1979 to 2020 for the cyclogenesis regions near South America. These results were
narrowed down to life cycle configurations that accounted for at least 1% of the overall life
cycle types count and presented at least one mature phase. These configurations repre-
sented approximately 95% of the total systems, amounting to 7,531 systems in total. The
most common cyclone type followed a four-phase configuration: incipient, intensification,
mature, and decay, accounting for about 60% of the analyzed systems. The results from
the CycloPhaser program align well with previous studies regarding cyclone behavior in
the South Atlantic region, confirming known cyclogenesis regions and providing statistical
insights into cyclone lifetimes and paths. The CycloPhaser program calculated an average
cyclone lifetime of approximately 97.6 and 91.1 hours (4 and 3.7 days) for austral summer
(DJF) and winter (JJA), respectively, and an average displacement of 4,658 and 4,777 km
for DJF and JJA. The mean displacement speed ranged from 14 to 15 ms−1 from DJF
to JJA, while the mean vorticity ranged from 4 to 4.5 −10−5s−1. These findings largely
corroborate those of previous studies for the regions and indicate a broad range of cyclone
behaviors (Simmonds and Murray, 1999; Hoskins and Hodges, 2005; Mendes et al., 2010;
Reboita et al., 2010; Gramcianinov et al., 2019, 2020; Crespo et al., 2023).
The analysis of spatial distributions revealed distinct patterns across various phases of
the cyclone life cycle:
• Incipient Phase: The overall pattern matches the genesis regions described in the
literature.
• Intensification Phase: The seasonal differences in track densities are mostly rela-
ted to seasonal differences in genesis. Two maxima are present in both seasons: one
mostly associated with ARG and the other with either LA-PLATA or SE-BR. Howe-
ver, other patterns include ARG systems being more eastward-oriented during JJA
than DJF and reaching further east during DJF, while LA-PLATA systems tend to
reach further southeast during JJA. Overall, the tracks are more displaced northward
during JJA than DJF.
• Mature Phase: The maximum track densities are southeast of the intensification
centers during DJF and east/southeast during JJA. During JJA, cyclones from the
ARG region mature close to the intensification. There is a higher positioning of

153
Section4.3.SummaryandConcludingRemarks
cyclones close to Uruguay and Southern/Southeastern Brazil during DJF than JJA.
• Decay Phase: The track density regions elongate southeastward compared to the
mature phase, with a maximum density east of the Weddell Sea, mainly related to
systems from ARG. Systems with an early decay phase appear as density centers
in LA-PLATA. During DJF, there are more tracks positioned near Uruguay and
South/Southeast Brazil than JJA.
• Second Intensification Phase: There is a high concentration of tracks south of
South Africa, which might be linked to secondary cyclogenesis processes (Mailier
et al., 2006; Shapiro et al., 1997; Ford et al., 1990; Rivals et al., 1998).
• Second Mature Phase: This phase generally occurs southeastward of the second
intensification phase.
• Second Decay Phase: ThisphaseoccursborderingAntarctica, predominantlyeast
of 40◦E.
Figure 4.22 provides an illustrative representation of the life cycle of systems with
genesis in the South American cyclogenesis regions. This figure highlights the systems’
path through their lifecycle, showing that after genesis, the systems follow the usual storm
tracks in the South Atlantic or, in the case of systems with genesis in ARG and LA-
PLATA, the subtropical storm path branch. Although systems from ARG and SE-BR
tend to have their genesis and intensification over the ocean, LA-PLATA systems tend to
start intensifying close to the continent, which can impact coastal communities (de Souza
and da Silva, 2021). Moreover, systems from SE-BR and LA-PLATA have their mature
phases — where they are most intense and, therefore, transfer more momentum from the
atmospheretotheocean—nearoceanicregionsclosetoSouthandSoutheastBrazil. These
regions host large urban centers and significant economic activities, such as oil drilling.
The results presented here contribute significantly to the climatology of South Atlantic
cyclones. CycloPhaser’s detailed analysis of cyclone life cycle types, particularly focusing
on configurations accounting for significant proportions of cyclone activity, enhances our
understanding of the spatial distribution of cyclone phases. This analysis reaffirms the
common four-phase configuration (incipient, intensification, mature, and decay) and sheds
light on variations in cyclone development cycles, contributing to a better understanding

154
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic
Figure4.22: Trackdensitiesnormalizedforeachregion, usingyearlyvaluesforallphases. Forcomputing
the track densities for the secondary development phases, only systems that display a complete secondary
development cycle were used. Contours representing normalized track densities above 0.8 were plotted for
each region individually.

155
Section4.3.SummaryandConcludingRemarks
of how different regions within the South Atlantic influence the formation and evolution of
distinct cyclone types. These insights are valuable for improving weather forecasting and
developing effective mitigation strategies in the region.
Despite the valuable contributions of the CycloPhaser program, it is important to
acknowledge the study’s limitations. The analysis at a single atmospheric level offers
a concentrated but partial view of the cyclone life cycle. Consequently, our conclusions
aboutcyclonecharacteristicsthroughouttheirlifecyclepredominantlyreflecttheprocesses
observable at the 850 hPa level. This methodological choice inherently limits our ability to
fully explore the cyclones’ vertical development and the complex interactions occurring at
different atmospheric altitudes. Future research could benefit from incorporating a multi-
level approach, providing a more holistic understanding of cyclone dynamics across the
troposphere.
One of the unique contributions of this research is the assessment of cyclone life cycle
stages along their storm tracks, a perspective not commonly explored in existing cyclone
track climatologies. This first application has highlighted the complexity of cyclone sys-
tems and opened several avenues for future research. The approach presented here allows
for the analysis of distinct dynamical mechanisms linked to the development of cyclonic
systems at different stages of their life cycle. Investigating cyclonic life cycles in climate
projections might be particularly relevant for coastal management in South America, po-
sing questions such as: Will future cyclones intensify and mature closer to or further away
from coastal regions? Will these phases last longer? Furthermore, using the method pre-
sented here, future studies can delve deeper into the primary processes associated with
each development stage in cyclone life cycles, including the secondary development stages
reported herein, and determine whether some of these cases represent secondary genesis.

156
Chapter4.LifeCycleofCyclonesintheSouthwesternAtlantic

5
Chapter
Southwestern Atlantic Cyclones Energetics Climatology
This chapter delves into the energetics of cyclones in the Southwestern Atlantic. The
Lorenz Energy Cycle (LEC) was computed for all 7,531 systems with genesis in the ARG,
LA-PLATA, and SE-BR regions, as described in Chapter 2.14. This extensive dataset,
the first of its kind for the South Atlantic region, provides a comprehensive view of the
energetics of cyclonic systems near South America. Section 5.1 explores the climatology
of these systems over their complete life cycle, while Section 5.2 examines the energetics
acrosseachdevelopmentphase, offeringauniqueperspectiveontheenergycycleofcyclonic
systems in the region.
5.1 Complete Life Cycle Climatology
5.1.1 Descriptive Statistics
This section provides exploratory statistics for each term of the LEC, covering the
systems’ complete life cycle. The aim is to offer a comprehensive view of the systems’
energetics while identifying the main differences among the terms. For the LEC compu-
tation, a Semi-Lagrangian limited area domain was used, which has profound impacts on
the interpretation of these results. These impacts are discussed in the following sections.
Table 5.1 contains exploratory statistical metrics for these terms. Figure 5.1 presents
the boxplots for all LEC components, where each panel depicts a distinct group of terms:
(A) energy, (B) conversion, (C) boundary, (D) generation/dissipation terms, and (E) bud-
gets. Figures 5.2, 5.3, 5.4, 5.5, and 5.6 display these groups of terms’ density distributions,
respectively.
Fortheenergyterms,thevaluesforK areanorderofmagnitudehigherthantheothers
Z

158
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
Figure 5.1: Box plots of each group of energetic terms, for the systems complete lifecycle. Each subplot
represents a different group of terms: (A) Energy Terms, (B) Conversion Terms, (C) Boundary Terms,
(D) Generation/Dissipation Terms, (E) Budgets. The box plots display the distribution of values for
each term within the specified group, with the horizontal line indicating the median, the box representing
the interquartile range (IQR), and the whiskers extending to 1.5 times the IQR. Outliers are shown as
individual points.

159
Section5.1.CompleteLifeCycleClimatology
for all metrics analyzed (Table 5.1). The high standard deviation (std) and quantile (Q)
values indicate substantial variability, primarily due to the presence of numerous outliers
(Figure 5.1a). Most values for K peak between 15 and 17 ×105J m−2 (Figure 5.2c). In
Z
contrast, A presents relatively moderate mean and median values, with a right-skewed
Z
distributionandsignificantspread(Figure5.2a). Thenotableoutliers(Figure5.1a)suggest
periods of unusually high energy values.
Overall, the eddy energy terms (A and K ) exhibit less variability and fewer outliers
E E
compared to the zonal energy terms (A and K ) (Figure 5.1a). They also have smaller
Z Z
mean and median values (Table 5.1). Although both eddy energy terms peak close to each
other, the distribution of A is more concentrated around the median (Figure 5.2b), with
E
a narrower interquartile range (IQR) and lower standard deviation, suggesting it is more
stable and consistent over time. In contrast, K presents a more right-skewed distribution
E
than A (Figure 5.2d).
E
Figure 5.2: Density plots for energy terms A (A), A (B), K (C), and K (D). The units are Jm−2.
Z E Z E
While the mean values of A and K are generally in agreement with previous studies,
E E
the values of K and A differ significantly (Michaelides et al., 1999; Veiga et al., 2008;
Z Z
Dias Pinto and Rocha, 2011; Pezza et al., 2014, e.g.,). Li et al. (2007) and Veiga et al.
(2013), analyzing global LEC values, found mean K values for the Southern Hemisphere
Z

160 Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
of approximately 10 and 15.8 × 105J m−2 and mean A values of approximately 40 and
Z
16 × 105J m−2, respectively. Analyzing the LEC of extratropical cyclones primarily in
the Northern Hemisphere, Smith (1980) found mean K and A values of 15 and 25 ×
|     |     |     |     |     |     | Z   | Z   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
105J m−2, respectively. Meanwhile, Black and Pezza (2013), for explosive cyclogenesis
in the Northwest Pacific region, found mean A and K values of approximately 30 and
|         |      |     |     |     | Z   | Z   |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| 48×105J | m−2, |     |     |     |     |     |     |     |
respectively. Here, K and A presented mean values of 28.55 and 5.55×
Z Z
| 105J m−2, | respectively. |     |     |     |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Table 5.1 - Summary Statistics of Lorenz Energetics Components: mean, median, standard deviation
(std), 20th percentile (Q20), 80th percentile (Q80), interquantile range (IQR), and range. The IQR
measures the range within which the central 50% of the values fall, while the range is computed as the
difference between the maximum and minimum values. The units for the energy terms (A , A , K , and
Z E Z
| K ) are 105Jm−2 |     | and W m−2 | for the remaining |     | terms. |     |     |     |
| --------------- | --- | --------- | ----------------- | --- | ------ | --- | --- | --- |
E
|     | Term | Mean  | Median | Std    | Q20    | Q80    | IQR    | Range   |
| --- | ---- | ----- | ------ | ------ | ------ | ------ | ------ | ------- |
|     | Az   | 5.55  | 4.68   | 3.71   | 2.41   | 8.30   | 5.89   | 36.46   |
|     | Ae   | 1.62  | 1.24   | 1.20   | 0.69   | 2.37   | 1.68   | 11.07   |
|     | Kz   | 28.55 | 26.19  | 15.10  | 15.52  | 40.16  | 24.64  | 114.55  |
|     | Ke   | 3.70  | 2.95   | 2.62   | 1.73   | 5.22   | 3.49   | 24.81   |
|     | Cz   | 0.52  | 0.38   | 4.85   | -2.69  | 3.72   | 6.41   | 86.70   |
|     | Ca   | 0.93  | 0.46   | 1.57   | -0.06  | 1.79   | 1.84   | 19.78   |
|     | Ck   | -3.56 | -1.63  | 9.51   | -7.41  | 1.11   | 8.52   | 206.43  |
|     | Ce   | 3.84  | 2.47   | 4.92   | 0.33   | 6.97   | 6.64   | 54.74   |
|     | BAz  | 3.54  | 2.03   | 7.67   | -1.35  | 8.23   | 9.57   | 175.05  |
|     | BAe  | 0.58  | 0.16   | 4.40   | -1.62  | 2.75   | 4.37   | 75.72   |
|     | BKz  | -7.93 | -5.53  | 31.75  | -29.51 | 12.06  | 41.57  | 445.63  |
|     | BKe  | 0.47  | 0.08   | 8.59   | -3.67  | 4.40   | 8.07   | 146.87  |
|     | BΦZ  | 63.87 | 49.25  | 128.05 | -24.60 | 156.65 | 181.25 | 1419.08 |
|     | BΦE  | 39.66 | 31.19  | 126.50 | -46.44 | 132.10 | 178.54 | 1353.99 |
|     | Gz   | -0.31 | -0.17  | 2.66   | -1.82  | 1.14   | 2.96   | 68.74   |
|     | Ge   | 1.17  | 0.56   | 3.14   | -0.47  | 2.79   | 3.26   | 58.39   |
|     | ∂AZ  | -0.07 | -0.14  | 4.46   | -2.66  | 2.31   | 4.97   | 106.39  |
∂t
∂AE
|     |     | -0.23 | -0.10 | 1.92 | -1.14 | 0.74 | 1.88 | 48.19 |
| --- | --- | ----- | ----- | ---- | ----- | ---- | ---- | ----- |
∂t
|     | ∂KZ | 1.59 | 0.75 | 13.38 | -7.13 | 10.40 | 17.53 | 251.24 |
| --- | --- | ---- | ---- | ----- | ----- | ----- | ----- | ------ |
∂t
∂KE
|     |     | 0.28 | 0.12 | 3.18 | -1.53 | 2.09 | 3.62 | 61.50 |
| --- | --- | ---- | ---- | ---- | ----- | ---- | ---- | ----- |
∂t
|     | RGz | -2.17 | -1.00 | 7.60  | -6.69  | 2.31  | 9.01  | 220.06 |
| --- | --- | ----- | ----- | ----- | ------ | ----- | ----- | ------ |
|     | RKz | 12.56 | 8.69  | 40.49 | -13.89 | 40.08 | 53.96 | 561.24 |
|     | RGe | 2.10  | 1.20  | 5.15  | -0.84  | 5.28  | 6.12  | 97.25  |
|     | RKe | -7.59 | -4.63 | 10.62 | -13.68 | -0.45 | 13.23 | 138.42 |

161
Section5.1.CompleteLifeCycleClimatology
The scarcity of results for a comprehensive set of systems hinders drawing decisive
conclusions about the behavior of the A and A terms in cyclonic occurrences, while
Z E
individual cases offer high variability, as indicated by case studies (Brennan and Vincent,
1980; Dias Pinto and Rocha, 2011; Pezza et al., 2014, e.g.,) and the higher variability in
the data (Table 5.1). However, several observations can be made: 1) When compared to
global energetics, cyclonic systems present higher K values. This is expected because
Z
K involves a zonal average of the wind components (Equation 2.34), and global avera-
Z
ges would yield smaller values than those for limited areas closer to the cyclonic center,
often associated with upper-level jets; 2) Limited areas provide smaller A values than
Z
hemispheric averages, due to the reduced meridional temperature and static stability gra-
dients (Equation 2.32). These effects are even more evident in the current study, as the
computational domain following the system focuses on the environmental dynamics sur-
rounding it, thus capturing overall higher wind speeds through the atmosphere and smaller
meridional temperature gradients. A similar effect is noted in Michaelides et al. (1999); 3)
Furthermore, the literature shows that the magnitude and sign of the conversion, boun-
dary, generation, and dissipation terms exhibit high variability across different systems and
development phases (Brennan and Vincent, 1980; Smith, 1980; Michaelides, 1987; Bulic,
2006; Dias Pinto and Rocha, 2011; Black and Pezza, 2013, e.g.,), complicating comparisons
of the overall values presented here with individual cases.
For the conversion terms, while C , C , and C are positive on average and in me-
Z A E
dian values, C is negative (Table 5.1). For C and C , there is a relatively narrow
K A E
spread around the median, with some significant outliers (Figure 5.1b). C , showing a
A
distribution centered around zero with both negative and positive values (Figure 5.3b),
indicates alternating periods of energy transfer in both directions, predominantly from A
Z
to A . Meanwhile, C has a left-skewed distribution (Figure 5.3d) and higher Q20 and
E E
IQR values, suggesting a more consistent positive net conversion.
The C term exhibits a wide distribution peaking at negative values (Figure 5.3c),
K
with a significant negative mean and median, indicating a dominant net conversion from
K to K . The large range and standard deviation, along with the presence of significant
Z E
outliers, suggest substantial variability in this conversion process. Lastly, C presents the
Z
most distinctive behavior, with values centered around zero but peaking at both positive
and negative values (Figure 5.3a), a consequence of the box size in relation to the scale of

162 Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
the zonal flow. However, the higher peak at positive values along with the positive mean
and median values indicate a preference for conversion from A to K .
|     |     |     | Z   | Z   |     |
| --- | --- | --- | --- | --- | --- |
The overall values presented here indicate that, throughout the systems’ complete li-
fecycle, K tends to receive energy from A and, in most cases, from K as well, although
| E   |     | E   |     | Z   |     |
| --- | --- | --- | --- | --- | --- |
there are instances where C tends to be positive. There is also a general tendency for A
|     | K   |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- |
to be converted to A , albeit with a lower magnitude. Meanwhile, although C can be
| E   |     |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- |
positive, negative, or neutral, the predominant tendency is for conversion from A to K .
Z Z
Figure 5.3: Density plots for conversion terms C (A), C (B), C (C), and C (D). The units are
|     |     | Z A | K   | E   |     |
| --- | --- | --- | --- | --- | --- |
Wm−2.
There is a notable difference between the boundary flux terms (BA , BA , BK ,
|     |     |     |     | Z   | E Z |
| --- | --- | --- | --- | --- | --- |
BK ) and the boundary pressure work terms (BΦZ and BΦE) (Table 5.1). For the
E
boundary flux terms, BA presents the highest mean and median values, while BK has
|     | Z   |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- |
the lowest. BA and BK have mean and median values closer to zero. The BA term
| E   | E   |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- |
exhibits moderate variability, with a wide distribution around the median (Figure 5.4a)
and few outliers (Figure 5.1c), a similar pattern to BK (Figure 5.4d). BA , in turn,
|     |     |     | E   | E   |     |
| --- | --- | --- | --- | --- | --- |
displays the lowest variability among the boundary terms, with most values peaking near
zero (Figure 5.4b). Meanwhile, BK presents the most distinctive behavior, exhibiting
Z
high variability, with a wide distribution (Figure 5.4c) and numerous outliers. Its values
range from the most negative to the most positive among the boundary terms, indicating

163
Section5.1.CompleteLifeCycleClimatology
an overall tendency for the exportation of zonal kinetic energy, supported by its negative
mean and median values.
On the other hand, the boundary pressure work terms present similar behavior, with
very high mean and median values, especially BΦZ, and displaying two peaks: one on
negative values (with a higher peak for the BΦE term) and another, which displays higher
densities, on positive values (Figure 5.4e and 5.4f). Both terms present low Q20 and high
Q80 values, indicating that although they generally contribute to the energy in the K and
Z
K terms, there are instances where they contribute negatively. For all metrics presented,
E
they exhibit the highest values in magnitude across all terms. As Brennan and Vincent
(1980) argued, these high values are associated with minor errors in the geopotential height
field that can escalate. Although ERA5 presents the most modern reanalysis product
offering homogeneous high-resolution data, systematic errors might be present, especially
in regions with low data coverage, such as over the oceans and high altitudes (Hersbach
et al., 2020). As most studies do not compute these terms as residuals and thus do not
present the values (for instance, none of the studies presented in Section 2.4.3 do so), direct
comparison of the values obtained here with the literature is hindered.
Althoughtheenergybudgetsarecomputedusingresiduals(whichincludetheboundary
pressure work terms), the generation terms are also analyzed as they serve both as an
overall evaluation of the generation residual terms and because, in future sections, they
will be used for understanding the systems’ dynamics. Both G and G present a similar
Z E
distribution, displayinglowvariability(Figure5.5), withmostvaluespeakingnearzeroand
with minor peaks on both positive and negative values (Figures 5.5a and 5.5b). However,
G presents a higher density of positive values, which is reflected in its higher mean and
E
median values than G and higher Q80 values (Table 5.1).
Z
For the generation residual terms, both present three peaks - at positive, neutral, and
negativevalues-butwhileRG hasthehighestdensityaroundnegativevalues, RG peaks
Z E
at positive values (Figures 5.5c and 5.5e). This results in RG presenting positive mean
E
and median values, despite a minor peak at negative values - which reflects in a negative
Q20 value - indicating that its contribution to ∂AE is mainly positive, with situations
∂t
where this term contributes negatively. For RG , the opposite is noted, with negative
Z
mean and median values, but a minor peak at positive values - reflected in a positive
Q80 - indicating it mainly contributes negatively to ∂AZ, with situations where this term
∂t

164
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
Figure 5.4: Density plots for boundary terms BA (A), BA (B), BK (C), BK (D), BΦZ (E), and
Z E Z E
BΦE (F). The units are Wm−2.

|             |             | Section5.1.CompleteLifeCycleClimatology |     |     | 165 |
| ----------- | ----------- | --------------------------------------- | --- | --- | --- |
| contributes | positively. |                                         |     |     |     |
Furthermore, whileRK presentshigherpositivemeanandmedianvalues, italsoshows
Z
high variability and numerous outliers (Figure 5.1d). It presents a distinctive density
distribution, with two marked peaks, one for positive and the other for negative values
(Figure 5.5d). This is reflected in its negative Q20 and positive Q80 values, with a high
∂KZ,
IQR. Therefore, although it mostly contributes positively to there are also significant
∂t
instances where it contributes negatively. RK , on the other hand, presents mean and
E
median values peaking at negative values (Figure 5.5f). Therefore, it mostly contributes
∂KE,
| negatively | to acting | as a sink | for K . |     |     |
| ---------- | --------- | --------- | ------- | --- | --- |
|            | ∂t        |           | E       |     |     |
Figure 5.5: Density plots for generation terms G (A) and G (B); and residual terms RG (C), RK
|         |             |                | Z         | E   | Z Z |
| ------- | ----------- | -------------- | --------- | --- | --- |
| (D), RG | (E), and RK | (F). The units | are Wm−2. |     |     |
|         | E E         |                |           |     |     |
Amongthebudgetterms, APEterms(∂AZ and ∂AE)presentnegativemeanandmedian
|     |     |     | ∂t  | ∂t  |     |
| --- | --- | --- | --- | --- | --- |
values, while the kinetic energy terms (∂KZ and ∂KE) are positive, although all of them
|     |     |     | ∂t  | ∂t  |     |
| --- | --- | --- | --- | --- | --- |

166
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
exhibit negative Q20 values and positive Q80 values, indicating variability among the
analyzed systems (Table 5.1). ∂AE has the lowest variability, with the smallest IQR and
∂t
range values, fewest outliers (Figure 5.1), and the highest peak density centered around
zero (Figure 5.6b). This indicates that while in most cases there is an overall tendency for
A to be neutral, there are also occurrences of positive and negative increments.
E
In contrast, ∂AZ and ∂KE display similar density distributions (Figure 5.6a and 5.6d),
∂t ∂t
with peaks at negative, neutral, and positive values. ∂AZ has a higher peak at negative
∂t
values, indicating a tendency for A to decrease, while ∂KE peaks at positive values,
Z ∂t
reflecting a tendency for K to increase. However, both terms also show instances of
E
neutrality and opposite trends. Lastly, ∂KZ exhibits a unique behavior with two prominent
∂t
peaks at opposite extremes (Figure 5.6c). This term has the lowest Q20 and the highest
Q80, IQR, and range values, indicating that K tends to exhibit extreme changes — either
Z
significant increases or decreases — with a smaller tendency to remain neutral.
The results for the budget terms are generally consistent with the expected outcomes
basedonthecurrentunderstandingofcyclonedynamics. Themeantendencyforbotheddy
and zonal APE to decrease over time is related to the eddy circulation acting to dissipate
horizontal temperature gradients and convert them into eddy kinetic energy through the
baroclinic instability process. However, the high variability indicates exceptions to this
rule, where distinctive behaviors are noted. These will be investigated in the next sections.
Furthermore, the extreme variability in the K budget might be related to the Semi-
Z
Lagrangian domain changing position relative to the upper-level jets, as well as an effect
related to the box size, which may not accurately represent the local zonal basic state.
Both hypotheses need further investigation.
5.1.2 Mean Energy Cycle
Figure 5.7 illustrates the LEC for the mean values of each term, providing an overview
of the mean energy fluxes in the analyzed systems. However, due to the high variability
presented for the distinct terms, as shown previously, these results should be interpreted
with caution. Additionally, G and G terms are used for a more physically based inter-
Z E
pretation, although the budgets were computed using their respective residuals. Since the
residual terms integrate these components, the presented budgets may not perfectly ba-
lance positive and negative energy fluxes due to the finite differences method used, which

Section5.1.CompleteLifeCycleClimatology 167
Figure 5.6: Density plots for budget terms ∂AZ (A) and ∂AE (B); ∂KZ (C), and ∂KE (D). The units are
|     |     | ∂t  | ∂t ∂t | ∂t  |
| --- | --- | --- | ----- | --- |
Wm−2.
| also incorporates | truncation | errors. |     |     |
| ----------------- | ---------- | ------- | --- | --- |
| (A)               |            | (B)     |     |     |
Figure 5.7: Representation of the LEC, with arrows denoting positive energy conversions (A) and mean
valuesoftheLorenzEnergyCycle(LEC)terms(B).Eachblueboxrepresentsanenergycomponent, with
arrows showing the direction of energy flow. The numbers adjacent to the arrows indicate the magnitude
and direction of the energy flux, with green indicating positive values and red indicating negative values.
The mean values indicate an overall tendency for both APE terms to decrease over

168 Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
time. The decreases in A are primarily due to conversions to A (C > 0, Figure 2.24),
|     |     | Z   | E   | A   |     |
| --- | --- | --- | --- | --- | --- |
which is an expected result. As discussed in Section 3.2.2, most cyclones in the dataset
are extratropical, which have the final cause of diminishing Equator-Pole temperature
gradients (Section 2.1.4), i.e., reducing A . Additionally, there are overall losses of A due
Z Z
to the G term, indicating either anomalous heating in cool regions or anomalous cooling
Z
inwarmregionscausedbytheeddy’smeridionalheattransportorbythediabaticradiative
heat sources/sink. Imports of A are also observed through the BA term. For the A
|     |     | Z   |     | Z   | E   |
| --- | --- | --- | --- | --- | --- |
term, there are decreases over time. Despite influxes from C , diabatic processes (G > 0)
|     |     |     | A   | E   |     |
| --- | --- | --- | --- | --- | --- |
and imports of energy (BA > 0), most of its energy is converted to K (C > 0) due to
|          |                   | E          |     | E E |     |
| -------- | ----------------- | ---------- | --- | --- | --- |
| enhanced | zonal temperature | gradients. |     |     |     |
The mean values indicate both forms of kinetic energy increasing over time. The incre-
ase in K - which is the greatest among the budget terms - primarily stems from influxes
Z
from the residual term (RK > 0). Although the inclusion of numerical errors hinders the
Z
interpretation of the residual term, Section 5.1 indicates that BΦ often presents large va-
Z
lues, suggesting that this energy influx might be related to the generation of kinetic energy
- by the zonal jets - towards the cyclone’s central low pressure. Meanwhile, a great part
of K energy is exported outside the domain (BK < 0), while a minor part is converted
| Z   |     | Z   |     |     |     |
| --- | --- | --- | --- | --- | --- |
to K through the barotropic conversion term (C < 0). Only negligible amounts are
| E   |     | K   |     |     |     |
| --- | --- | --- | --- | --- | --- |
converted from A . Finally, K displays increases over time, driven mostly by conversion
|     | Z   | E   |     |     |     |
| --- | --- | --- | --- | --- | --- |
from A , but also with significant contributions from C . Notably, RK presents high
|     | E   |     | K   | E   |     |
| --- | --- | --- | --- | --- | --- |
magnitudes, possibly indicating the dissipation of this energy. The importation of K is
E
almost negligible.
In summary, for the mechanisms related to eddy growth, it can be seen that the mean
environment energetics related to the cyclones in the SESA region indicate that both the
baroclinic and barotropic chains are active. This indicates that the eddies gain energy
from both meridional temperature gradients as well as from horizontal wind shear. More-
over, diabatic processes contribute to increasing the eddy APE, thus supporting the moist
baroclinic chain. However, the barotropic instability may trigger convection which would
also enhance the APE allowing for more conversion from A to K . Finally, the main
|     |     |     | E   | E   |     |
| --- | --- | --- | --- | --- | --- |
sink for eddy energy is the residual term, possibly associated with dissipation by frictional
forces.

169
Section5.1.CompleteLifeCycleClimatology
5.1.3 EOFs
The results presented in Section 5.1.1 demonstrate that the LEC terms exhibit high
variability. Even a view of the LEC by the mean values can be problematic, as each term
spans a wide range of possible values, often with varying signs. Therefore, delineating an
overall picture of the LEC for the analyzed systems is not a trivial task. To help address
this issue, an empirical orthogonal function (EOF) analysis is used. It is important to note
that the values represent anomalies rather than the actual magnitudes of the energy cycle
components.
Figure 5.8 illustrates the proportion of variance in the dataset that is explained by each
of the first eight Empirical Orthogonal Functions (EOFs). The first EOF accounts for the
largest share of the variance, explaining 28.3%, indicating it captures the most significant
pattern in the data. The second and third EOFs both explain around 11% of the variance,
showing that they also represent notable patterns but with less influence compared to the
first EOF. The subsequent EOFs explain progressively smaller proportions of the variance:
8.2% for the fourth, 7.4% for the fifth, 5.9% for the sixth, 5.2% for the seventh, and 4.4%
for the eighth. Together, these eight EOFs capture the primary modes of variability within
the dataset. Usually, the principal components (PCs, not shown) represent the temporal
evolutionofthesignalmagnitudeofeachEOF.However, inthiscontext, theywouldmerely
represent the signal magnitude across the distinct cyclones and therefore do not represent
any physical feature.
For the EOF1 (Figure 5.9), most terms are in general agreement with the signal for
mean values presented in Figure 5.7, indicating an enhancement of the average behavior.
The exceptions to this are the C , BA and A budget terms; however, the anomaly
Z E E
signal magnitude is lower than what is found in the mean values, indicating that for the
first variability mode, there is no reversal in the sign of the observed values. In general, this
result confirms the observation that the overall behavior of the environmental energetics
related to the cyclones in the SESA region is associated with the moist baroclinic chain,
acting together with barotropic conversions.
For the EOF2, although many terms present anomalies with a reversed sign compared
tothemeanvalues, themagnitudeofmostofthemisnothighenoughtosignalareversalin
the energy flux direction or represent significant changes in the overall behavior. However,

170
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
Figure 5.8: Proportion of variance in the dataset explained by the first eight Empirical Orthogonal
Functions (EOFs).
some significant changes can be noted in certain terms. For instance, the terms ∂AZ and
∂t
∂KE present an enhancement of the mean behavior. For ∂AZ, this is mostly linked to the
∂t ∂t
further diminishing of G in the EOF2, while for ∂KE, this is primarily associated with
Z ∂t
enhancedimportsfromBK , withminorcontributionsfromtheenhancedmoistbaroclinic
E
chain. Althoughthesignalisweak, EOF2alsopresentsasmallweakeningofthebarotropic
conversions.
For the EOF3, it is evident that the signal for ∂AE has a higher magnitude and opposite
∂t
sign compared to the mean value. The positive budget for A is mostly associated with
E
enhanced conversion from A and a reduction in the conversions to K , although there are
Z E
strong reductions in the BA , which indicate a reversal in this term’s sign. For ∂KE, there
E ∂t
is also a significant signal for the enhancement of the positive budget, primarily associated
with the enhancement of the barotropic conversion by the C term.
K
Ingeneral, whiletheEOF2presentsasubtleenhancementofthemoistbaroclinicchain,
with a diminishment of barotropic conversions, the EOF3 presents the opposite behavior.
TheEOF4, inturn, presentsareversalinsignformosttermscomparedtothemeanvalues.
However, for most of them, the signal is not high enough to represent a significant reversal
of the mean values. The most notable distinction is in the G term, which becomes even
Z
more negative.

171
Section5.1.CompleteLifeCycleClimatology
Figure 5.9: EOF Analysis of Lorenz Energy Cycle (LEC) Terms, illustrating the anomalies in energy
fluxes: EOF1 (A), EOF2 (B), EOF3 (C) and EOF4 (D). The numbers adjacent to the arrows denote the
magnitude and direction of the anomaly, with green indicating positive values and red indicating negative
values.

172
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
The following EOFs continue to exhibit such small signals, presenting only minor devi-
ations from the mean behavior of the LEC. Therefore, they will not be further discussed.
The EOF analysis presented here demonstrates that, although there is high variability in
the dataset, with individual cases presenting overall energetics deviating from the mean
values, the mean energetics or the mean state of the cyclones is much stronger than the
fluctuations or variations captured by the EOFs (Appendix C contains the reconstructed
EOFs). This might be intrinsically linked to the EOFs being calculated for the entire life
cycle of the systems, with distinct dynamical processes acting at different development
stages. Next sections will explore to what extent the results presented can be applied
to each development phase or if the distinct phases will reveal further details about the
energetics of the cyclones in SESA region.
5.2 Climatology Across Life Phases
5.2.1 Descriptive Statistics
Although Sections 5.1.1 and 5.1.3 provide an overview of the systems’ energetics, their
results apply to the complete life cycle. As distinct dynamical processes might act at
different development stages, it is expected that different phases of the cyclone’s life cycle
will present different overall energy cycles. Here, the cyclones’ lifecycle was dissected using
the Cyclophaser program to investigate the LEC for each phase individually, aiming to
understand which processes dominate in each of them.
The first step was to assess whether the different development phases exhibit statis-
tically significant differences among themselves. Table 5.2 presents the p-values for the
normality, homogeneity, and significance tests employed. Normality was assessed using
the Shapiro-Wilk test, and homogeneity was assessed using Levene’s test. For all terms,
the p-values were well below the 0.05 threshold, indicating that the data significantly
deviate from normality and that their variances differ significantly across the phases. The-
refore, to determine statistically significant differences between the phases, we employed
the non-parametric Kruskal-Wallis (KW) test. The results indicated that the differences
in the LEC terms among the phases are statistically significant. While post-hoc Dunn’s
tests could be conducted to identify which specific phases differ if the Kruskal-Wallis test
is significant, this would involve a combinatorial analysis of pairs among seven phases for

Section5.2.ClimatologyAcrossLifePhases 173
all 17 terms in the LEC. Such an analysis would be impractical. Consequently, the statis-
tically significant results from the KW test were deemed sufficient for proceeding with the
analysis.
Table5.2-StatisticalAnalysisResultsforDifferentPhases. Thetableshowsthep-valuesfortheKruskal-
Wallis (KW) test, the Shapiro-Wilk normality test, and Levene’s test for homogeneity of variances. The
Kruskal-Wallis test is used here due to non-normality or heterogeneity of variances in the data, indicating
| significant differences | among | phases if the p-value | is less than | 0.05.       |
| ----------------------- | ----- | --------------------- | ------------ | ----------- |
|                         |       | KW                    | Normality    | Homogeneity |
Term
|     |     | p-value   | p-value  | p-value   |
| --- | --- | --------- | -------- | --------- |
|     | Az  | 5.16e-273 | 2.86e-50 | 5.54e-67  |
|     | Ae  | 6.51e-283 | 1.24e-57 | 3.49e-111 |
|     | Kz  | 2.30e-22  | 3.08e-36 | 1.80e-46  |
|     | Ke  | 0.00e+00  | 3.05e-55 | 6.78e-269 |
|     | Cz  | 1.01e-48  | 1.79e-34 | 1.14e-134 |
|     | Ca  | 7.46e-192 | 5.32e-57 | 5.71e-85  |
|     | Ck  | 1.64e-92  | 5.90e-62 | 0.00e+00  |
|     | Ce  | 0.00e+00  | 6.43e-52 | 1.84e-189 |
|     | BAz | 6.58e-79  | 1.14e-54 | 8.02e-39  |
|     | BAe | 1.66e-282 | 1.92e-51 | 5.02e-137 |
|     | BKz | 7.56e-05  | 1.71e-38 | 2.54e-54  |
|     | BKe | 2.03e-118 | 6.67e-60 | 1.92e-76  |
|     | BΦZ | 2.30e-45  | 4.71e-28 | 5.33e-105 |
|     | BΦE | 6.89e-39  | 2.31e-27 | 3.23e-94  |
|     | Gz  | 1.50e-48  | 9.91e-50 | 0.00e+00  |
|     | Ge  | 0.00e+00  | 2.70e-58 | 6.95e-256 |
|     | RGz | 7.43e-164 | 5.41e-54 | 1.09e-148 |
|     | RKz | 5.09e-06  | 1.22e-35 | 2.78e-69  |
|     | RGe | 1.27e-179 | 4.83e-47 | 1.77e-122 |
|     | RKe | 1.84e-267 | 9.33e-54 | 7.03e-205 |
|     | ∂AZ | 2.58e-221 | 2.52e-50 | 0.00e+00  |
∂t
∂AE
|     |     | 3.85e-212 | 1.51e-53 | 0.00e+00 |
| --- | --- | --------- | -------- | -------- |
∂t
|     | ∂KZ | 1.33e-108 | 3.36e-44 | 3.67e-194 |
| --- | --- | --------- | -------- | --------- |
∂t
∂KE
|     |     | 0.00e+00 | 2.65e-55 | 0.00e+00 |
| --- | --- | -------- | -------- | -------- |
∂t
The next step is to investigate the overall behavior of each term across distinct deve-
lopment phases through their density distributions. Beyond energy terms, the focus will
be on the overall energy flux direction, providing a proxy for understanding the dyna-

174
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
mical forcing related to the development of cyclonic systems throughout their life cycle.
Finally, a summary of the main findings along with interpretations drawn from the results
is presented at the end of this section.
Figure 5.10 displays the density plots for the energy terms for each development phase.
It can be observed that the overall shapes of the distributions within the same term are
similar, mirroring the distribution for the complete life cycle (Section 5.1.1), with minor
differences across each specific phase. For A (Figure 5.10a), every phase presents maxi-
Z
mum densities centered between 2 and 3 155Jm−2, but displays right-skewed distributions,
indicating high variability and the occasional occurrence of extremely high values. Mature
phases (1 and 2) exhibit sharper peaks, while intensification (1 and 2) and incipient phases
presentbroaderpeaks. Anoveralltrend, indicatedbybothmeanandmedianvalues, shows
A decreasing from the incipient to the mature phase and increasing again through the
Z
decay phase. The same trend is observed during secondary development: it decreases from
intensification 2 to mature 2 and then increases again at decay 2. Notably, despite this
increase during the decay phase, the mean and median values are lower than the initial
values, and even lower during the secondary development. This overall trend displayed by
A throughout the cyclone’s life cycle aligns with the discussion at the end of Section 5.1.1
Z
andinSection2.1.4: extratropicalcyclonesaimtobalanceglobaltemperature, diminishing
temperature gradients (i.e., A ).
Z
For A (Figure 5.10b), the densities are less skewed, with sharper peaks compared to
E
A , indicating lower variability and fewer extreme values. Most values peak between 0.5
Z
and1155Jm−2,andthemeanandmedianvaluesshowanoverallincreasefromtheincipient
to the intensification phase, where A reaches its highest values, followed by a consistent
E
decrease until the decay phase. A increases again during the second intensification phase
E
and then decreases from the second mature phase to the decay phases. This pattern
suggests that after genesis, the eddies initiate the conversion from meridional to zonal
temperature gradients, which peak during intensification and diminish afterward. The
lower mean and median values at the decay phases compared to the beginning of each life
cycle indicate that the eddies not only diminish the zonal temperature gradients but also
reduce them to levels lower than their initial states.
The K term densities present narrow peaks with long tails towards low values, mir-
Z
roring the distribution for the total phase (Figure 5.10c). For all phases, the distributions

Section5.2.ClimatologyAcrossLifePhases 175
| (A) |     |     | (B) |     |     |
| --- | --- | --- | --- | --- | --- |
(D)
(C)
Figure 5.10: Density plots for energy terms A (A), A (B), K (C), and K (D), for each development
|     |     |     | Z E | Z   | E   |
| --- | --- | --- | --- | --- | --- |
phase: incipient (Ic), intensification (It), mature (M), decay (D) and the secondary development phases
(indicated by ”2”). The solid vertical lines indicate the mean values for a given phase while the dashed
Wm−2.
| lines, the median | values. The | units are |     |     |     |
| ----------------- | ----------- | --------- | --- | --- | --- |

176
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
peak at nearly 16 155Jm−2, with sharper peaks for the initial development phases and
broader peaks for the secondary development phases. Unlike the other terms, the median
values remain constant across all phases, while only the mean values vary. The mean va-
lues are higher during the intensification phases (1 and 2) and lower during the remaining
phases of the same life cycle.
The densities for K are similar to those for A , with left-skewed distributions peaking
E E
atapproximately2×155Jm−2 (Figure5.10d). However,thedensitiesforthematurephases
(1 and 2) present broader peaks. The mean and median values for this term follow the
overall trend for the relative vorticity series (Chapter 4), showing behavior opposite to that
of A : it increases from the incipient to the mature phase, decreases at the decay stage,
Z
increases again during the second intensification and mature phases, and finally decreases
during the second decay phase. As expected, this term serves as a proxy for the overall
intensity of the cyclonic systems, starting with lower energy states and gaining energy up
to their maturity, then losing energy as they decay.
Figure 5.11 displays the density plots for the conversion terms for each development
phase. All terms present density shapes with multiple peaks: C and C for neutral and
A E
positive values, while C and C also present peaks for negative values. This behavior
Z K
indicates significant variability within the terms and suggests that the energy can flow in
both directions (positive and negative peaks) or that energy fluxes can be active or inactive
(neutral peaks).
The C term exhibits high variability in its density distribution across the different de-
Z
velopment phases (Figure 5.11a). During the incipient phase, there are two distinct peaks:
one at negative values and a sharper peak at positive values, with a broad distribution
in between, resulting in positive mean and median values. In contrast, the intensification
and mature phases display symmetric peaks at both ends of the spectrum, with a broader
peak at neutral values. For the decay phase, the peak at negative values diminishes, while
the peaks at neutral and positive values become sharper, pushing the mean and median to
positive values. The second intensification phase, despite having peaks at neutral, positive,
and negative values, shows a wide distribution in the positive range, reflected in its positive
mean and median values. Lastly, the second mature and decay phases present opposite
shapes: the former has a sharper peak at negative values, while the latter has a sharper
peak at positive values. For the second mature phase, the mean and median values are

Section5.2.ClimatologyAcrossLifePhases 177
| (A) |     |     | (B) |     |     |
| --- | --- | --- | --- | --- | --- |
| (C) |     |     | (D) |     |     |
Figure5.11: DensityplotsforconversiontermsC (A),C (B),C (C),andC (D),foreachdevelopment
|     |     |     | Z A | K   | E   |
| --- | --- | --- | --- | --- | --- |
phase: incipient (Ic), intensification (It), mature (M), decay (D) and the secondary development phases
(indicated by ”2”). The solid vertical lines indicate the mean values for a given phase while the dashed
| lines, the median | values. The | units are Wm−2. |     |     |     |
| ----------------- | ----------- | --------------- | --- | --- | --- |

178
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
on opposite sides of the spectrum. Therefore, while the initial and final phases of each
development cycle tend to have overall positive values and the intermediate phases tend
toward neutrality, the high variability makes it difficult to define a definitive behavior for
the C term. This high variability (across systems and phases) is also noted in previous
Z
studies (Michaelides, 1987; Veiga et al., 2008; Dias Pinto and Rocha, 2011; Dias Pinto
et al., 2013, e.g.).
For the C term, each phase presents a peak near neutral values, right-skewed with a
A
long tail distribution extending towards positive values (Figure 5.11b). There are also a
minor peaks near 3Ws−2, which are sharper for the phases of the first development cycle.
Furthermore, the distributions become more right-skewed in the intensification phases (1
and 2) and less skewed in the later phases. Consequently, the mean and median values
increase from the beginning of each development cycle, peak during each intensification
phase, and then decrease afterward. This indicates an overall tendency for energy to be
converted from A to A during the development cycle, which aligns with the overall trend
Z E
observed for the A term (Figure 5.10b).
E
TheC term,acrossallphases,presentsapeakatnegativevalues,right-skewedtowards
K
positive values with a minor peak at positive values (Figure 5.11c). During the first
developmentcycle,theincipientstageshowsasharppeaknear−3.5Ws−2 andaminorpeak
near −1Ws−2. As the systems intensify, the minor peak becomes broader and the sharp
peak becomes more pronounced. Meanwhile, the peak at positive values, near 3.5Ws−2,
also becomes sharper. Consequently, the median values become significantly more negative
from the incipient to the mature phase and less negative during the decay phase. Although
the mean values follow a similar pattern, the sharper peak at positive values during the
mature phase results in mean values for the mature phase that are similar to — or even
less negative than — those of the intensification phase. The secondary development cycle
shows a similar behavior to the first one. These results indicate an overall tendency for
conversionfromK toK throughoutthecyclone’slifecycle,butwithasignificantnumber
Z E
of systems where the energy flows in the opposite direction. The tendency for C to be
K
negative and most intense during mature phases is consistent with the overall behavior of
the K term. However, this analysis does not clarify whether there are instances where the
E
energy flow reverses direction during the life cycle. This will be investigated in the next
sections, as previous studies have suggested that such reversals might occur, especially in

179
Section5.2.ClimatologyAcrossLifePhases
systems transitioning from one type to another (Brennan and Vincent, 1980; Michaelides,
1987; Wahab et al., 2002; Veiga et al., 2008; Pezza et al., 2010, e.g.,).
The density distributions for all phases of the C term present peaks at positive values,
E
near 3.5Ws−2, with left-skewed distributions and long tails extending into negative values,
albeit with low densities (Figure 5.11d). The peaks tend to become sharper during the
intensification phases and decrease afterward. Additionally, for the decay phases (1 and
2), a broad peak near neutral values emerges. As a result, the mean and median values
are higher during the intensification phases and closer to zero during the decay phases (1
and 2). Since the peaks in conversion from A to K coincide with the phases where A
E E E
is on average highest, it can be inferred that a significant amount of the energy content in
this term is being converted to K .
E
The density plots for the boundary terms are displayed in Figure 5.12. The BA term
Z
presents a right-skewed distribution peaking at values close to zero (Figure 5.12a). There
are also long tail distributions towards high positive values, indicating the occurrence of
unusually extreme values. This behavior is reflected in the overall positive mean and
median values. Across the phases, there is a tendency for the imports of A to decrease
Z
from the intensification to mature phases (1 and 2), increasing again for the decay phases
(1 and 2). This behavior is consistent with the values for the A term (Figure 5.10).
Z
The BA and BK terms present similar distributions, with sharp peaks near zero
E E
and long tails extending towards both negative and, especially, positive values (Figures
5.12b and 5.12d). Consequently, the mean and median values are often positive. Despite
the similarities in the density distributions, the overall behavior across the distinct phases
among these terms differs. For BA , there is a tendency for the mean and median values
E
to decrease from the beginning of each development cycle to the mature phase, becoming
negative in the latter and increasing again during decay, but with mean and median values
near zero. This behavior indicates imports of A in the systems’ early life stages but
E
exportsastheymature. Meanwhile, forBK , themeanandmedianvaluestendtoincrease
E
from the incipient to the intensification phases and then decrease from the intensification
(1 and 2) to the decay phases (1 and 2), displaying negative mean and median values at
the mature and decay phases. This indicates that after intensification, the systems overall
export K outside the computational domain.
E
The BK term presents densities peaking at positive, neutral, and negative values
Z

180
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
(A) (B)
(C) (D)
(E) (F)
Figure 5.12: Density plots for boundary terms BA (A), BA (B), BK (C), BK (D) and boundary
Z E Z E
pressure work terms BΦZ and BΦE, for each development phase: incipient (Ic), intensification (It),
mature (M), decay (D) and the secondary development phases (indicated by ”2”). The solid vertical lines
indicatethemeanvaluesforagivenphasewhilethedashedlines,themedianvalues. TheunitsareWm−2.

181
Section5.2.ClimatologyAcrossLifePhases
(Figure 5.12c). Across all phases, the peaks are often sharpest at negative values, but
the peaks at neutral values tend to become sharper throughout the systems’ life cycles.
The mean and median values are similar for the first development cycle phases, while
the differences are more marked for the second development cycle phases, with mean
and median values becoming more positive from intensification 2 to mature 2 and then
decreasing in the decay 2 phase. Overall, this pattern indicates a tendency for systems to
consistently export K through their life cycles, although there is significant variability in
Z
the data.
Lastly, BΦZ and BΦE display nearly identical distributions, presenting peaks at both
positive and negative values, but with sharper peaks at the former (Figures 5.12e and
5.12f). As a result, the median values are often aligned across all phases in the positive
range. However, during the decay phase, the peaks at negative values become sharper,
especially for BΦE, which causes the median values to decrease. As discussed in Section
2.4.2, the physical interpretation of these terms is difficult and can be hindered by small
errors in the geopotential field, which might lead to unusually high values.
Figure 5.13 displays the densities for the generation and the residuals of the dissipation
terms. Here, the generation terms will be explored instead of their residuals as they
allow for a physical interpretation, while the residuals account for numerical errors that
escalate from the other terms in the A and A budgets. For the G term, each phase
Z E Z
often displays distributions with peaks at neutral values and minor peaks at positive and
negative values (Figure 5.13a). During the incipient stage, the peak at neutral values is
broader, resulting in negative mean and median values. As the systems evolve, the peak at
neutral values becomes sharper, causing the mean and median values to approach zero by
the decay phase. Notably, for the second mature phase, the minor peak at positive values
diminishes, causing the mean and median values to become negative again.
The G term presents an identical distribution to the G term for the incipient phase,
E Z
while the other phases display peaks at both neutral and positive values, with high inter-
phase variability (Figure 5.13b). During the intensification phase, there is a broad right-
skewedpeakatneutralvalues,followedbyasharperpeakatpositivevalues. Asthesystems
transition to the mature and decay phases, the peak at positive values decreases and the
peak at neutral values becomes broader. Overall, there are negative mean and median
values during the incipient stage, reaching the largest positive values in the intensification

182
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
(A) (B)
(C) (D)
Figure 5.13: Density plots for generation and dissipation residual terms G (A), G (B), RK (C), and
Z E Z
RK (D), for each development phase: incipient (Ic), intensification (It), mature (M), decay (D) and the
E
secondary development phases (indicated by ”2”). The solid vertical lines indicate the mean values for a
given phase while the dashed lines, the median values. The units are Wm−2.

183
Section5.2.ClimatologyAcrossLifePhases
phaseanddecreasingthroughthematureanddecayphases. Theseconddevelopmentcycle,
inturn, presentsadistinctivebehavior: whilethevaluesarelargestforintensification2and
decrease during the mature 2 phase, they increase again during the decay 2 phase. Overall,
these results indicate a generation of A especially during the intensification phases, which
E
decreases afterward, consistent with the overall A behavior (Figure 5.10).
E
The RK term displays distributions with peaks at both negative and positive values,
Z
but with small inter-phase variability, similar to the BΦZ term (Figure 5.13c). This
suggests an influence of the latter on the former term, although the magnitudes are much
smaller. Due to the sharper peak at positive values compared to the one at negative
values, the mean and median values are positive across all phases, with median values
being identical. Meanwhile, RK presents right-skewed peaks at negative values, with
E
long tail distributions extending towards positive values (Figure 5.13d). The mean and
median values for this term increase from the intensification to decay phases. Although
it is tempting to associate the positive values of RK with either the upscaling of energy
Z
and generation of K through zonal jet fluxes towards the low-pressure system, and the
Z
negative values of both RK and RK with kinetic energy dissipation, the assimilation of
Z E
numerical errors and boundary pressure work terms prevents drawing such conclusions.
Finally, the budget terms result from the aggregate contributions of each energy cycle
term. The density distributions for these terms are illustrated in Figure 5.14. Due to
the high variability often present in each individual term, the budget terms also exhibit
high variability, with modest inter-phase variations in shape distribution (i.e., although
the overall behavior is preserved among the distinct phases, the magnitude of the peaks
changes).
The ∂AZ term often presents three peaks across the distinct phases: one at positive,
∂t
negative, and neutral values (Figure 5.14a). For the incipient phase, the peak at positive
values is more prominent, while for the intensification and mature phases, the peak at
negative values is more significant. The decay phase displays an increase in the peaks
at neutral and positive values. A similar behavior is seen for the secondary development
phases. As indicated by the mean and median values, A usually increases during incipient
Z
and decay phases, displaying decreases during the other phases.
Meanwhile, the ∂AE term often displays a sharp peak at neutral values, with long tail
∂t
distributions towards both positive and negative values. The exceptions are the mature

184 Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
| (A) |     |     | (B) |     |     |
| --- | --- | --- | --- | --- | --- |
| (C) |     |     | (D) |     |     |
Figure 5.14: Density plots for energy budget terms ∂AZ (A), ∂AE (B), ∂KZ (C), and ∂KE (D), for
|     |     |     | ∂t ∂t | ∂t  | ∂t  |
| --- | --- | --- | ----- | --- | --- |
each development phase: incipient (Ic), intensification (It), mature (M), decay (D) and the secondary
developmentphases(indicatedby”2”). Thesolidverticallinesindicatethemeanvaluesforagivenphase
| while the dashed | lines, the median | values. The | units are Wm−2. |     |     |
| ---------------- | ----------------- | ----------- | --------------- | --- | --- |

185
Section5.2.ClimatologyAcrossLifePhases
phases (1 and 2), which are left-skewed and present broad peaks at negative values. As
a result, while most phases tend towards neutrality for the A term, the mature phases
E
tend to decrease this term.
For the ∂KZ term, a distribution with peaks at opposite sides of the spectrum can be
∂t
seen (Figure 5.14c). The differences among each phase lie in the positioning of the sharpest
peak. Overall, for the first development cycle, there is a tendency for K to increase
Z
over the incipient and intensification phases, decrease during the mature phase, and then
increase again during the decay phase. Despite the tendency for decreases during the
second intensification, the peaks at each end of the spectrum are nearly symmetrical. The
second mature phase presents an overall tendency for decreases in K , which is reversed
Z
during the second decay. These results suggest that K is often increasing or decreasing
Z
but rarely neutral, and despite the overall trends noted here, there is high variability in
behavior among the systems.
Lastly, for ∂KE, thedistributionspresentpeaksatpositive, neutral, andnegativevalues,
∂t
with large inter-phase differences (Figure 5.14d). For the incipient and intensification
phases, the peaks are sharper at positive values, which is reversed during the mature
and decay phases. This behavior is reflected in the mean and median values. A similar
behavior can be noted for the secondary development phases. These results indicate a
tendency for K to increase during its initial development for each cycle, peaking during
E
the intensification phases (1 and 2), while the tendency in subsequent phases is a decrease.
5.2.2 Mean Energy Cycle
Figure 5.15 illustrates the LEC for the mean values of each term for the first develop-
ment cycle. As noted in Section 4.1.1, due to the high variability presented for the distinct
terms, the results should be interpreted with caution. However, they can provide an over-
view of the mean energy fluxes in the analyzed systems across the different development
phases and their respective dynamical evolution. Additionally, similarly to Figure 5.7, the
G and G terms are used instead of their respective residuals for a more physically based
Z E
interpretation, although the budgets were computed using the residuals. Since the residual
terms were integrated into the budgets, the presented budgets may not perfectly balance
positive and negative energy fluxes due to the finite differences method used, which also
incorporates numerical errors.

186
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
(A) (B)
(C) (D)
Figure 5.15: Mean values of the Lorenz Energy Cycle (LEC) terms for each life cycle phase: incipient
(A), intensification (B), mature (C), and decay (D). Each blue box represents an energy component, with
arrows showing the direction of energy flow. The numbers adjacent to the arrows indicate the magnitude
and direction of the energy flux, with green indicating positive values and red indicating negative values.
A representation of the complete cycle, with the positioning of each term can be found at Figure 5.7.

|     |     | Section5.2.ClimatologyAcrossLifePhases |     |     | 187 |
| --- | --- | -------------------------------------- | --- | --- | --- |
The incipient stage is confirmed as the development stage where the cyclone is not fully
formed and the eddy-related environmental energetics are still responding to large-scale
dynamics. This is mostly indicated by the A term, which is increasing due to heating
Z
at low latitudes and diabatic cooling at higher latitudes. However, this increase is not
driven by G , but rather from imports of A . Such behavior (both G < 0 and BA > 0)
|     | Z   |     | Z   | Z   | Z   |
| --- | --- | --- | --- | --- | --- |
∂AZ
has been observed in cases studies, but often the is negative in the initial phases
∂t
(Brennan and Vincent, 1980; Dias Pinto and Rocha, 2011; Dias Pinto et al., 2013, e.g.,).
TheexcessA isbeingconvertedintobothK andA as, inthisphase, whileameridional
|     | Z   |     | Z E |     |     |
| --- | --- | --- | --- | --- | --- |
temperature gradient is still present, there are also eddy meridional heat transports.
The K term experiences the largest increases during this phase, driven mainly by
Z
RK , although a significant portion of this energy is exported outside the domain, with
Z
some of it converted to K . In contrast, A experiences modest decreases. The negative
|     |     | E   | E   |     |     |
| --- | --- | --- | --- | --- | --- |
∂AE indicates that the initial A reservoir must be large enough to sustain the eddy
| ∂t  |     | E   |     |     |     |
| --- | --- | --- | --- | --- | --- |
development. AsFigure5.10demonstrated,thisisindeedthecase. Theexistenceofazonal
temperature gradient drives the conversion of A into K . This initial conversion chain of
E E
A → K and A → A → K is observed in the initial stages of most LECs of baroclinic
| Z   | Z Z | E E |     |     |     |
| --- | --- | --- | --- | --- | --- |
disturbances previously reported (Michaelides, 1992; Pezza et al., 2010; Dias Pinto and
| Rocha, 2011; | Black and | Pezza, 2013, | e.g.,). |     |     |
| ------------ | --------- | ------------ | ------- | --- | --- |
While A receives energy from A and there are some imports of A through the
|     | E   |     | Z   | E   |     |
| --- | --- | --- | --- | --- | --- |
boundaries, this energy is mostly converted to K . Additionally, during this stage, G is
E E
negative, possibly due to the lower convective activity at the cyclone’s initial development.
The K term then experiences increases in energy, driven by the barotropic conversion
E
term, imports of energy, and mainly conversions from A , although a significant portion
E
| of this energy | is lost | through RK | .   |     |     |
| -------------- | ------- | ---------- | --- | --- | --- |
E
During the intensification phase, although the loss of A energy from the G term and
Z Z
the conversion to K diminish, the enhancement in conversion to A causes an overall
|     | Z   |     |     | E   |     |
| --- | --- | --- | --- | --- | --- |
decrease in this term. This indicates a weakening of the meridional temperature gradient,
driven by the eddy-induced meridional heat transport. For the K term, the enhanced
Z
RK is balanced by increased export of energy and conversion to K , leading to a decrease
| Z   |     |     |     | E   |     |
| --- | --- | --- | --- | --- | --- |
∂KZ.
| in the magnitude | of  |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
∂t
In this phase, enhanced eddy-related convective processes are evident, indicated by the
positive G . This process, in conjunction with the increased meridional heat transport,
E

188
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
creates zonal temperature and ω gradients, enhancing A → K conversions. With redu-
E E
ced A imports, the magnitude of ∂AE remains consistent with the incipient phase. For
E ∂t
the K term, despite increases in all energy influxes, the increased activity of RK results
E E
in only modest increments in ∂KE.
∂t
In the mature phase, most LEC terms present an overall reduction in magnitude as the
system’s energetics become less active and begin to equalize with the environment. The
exception is the barotropic term C , which increases in magnitude. As a result, the K
K Z
term begins to experience decreases, indicating an overall weakening of the zonal jets. The
∂AE term becomes significantly more negative, primarily due to the reduction in convective
∂t
activity, asindicatedbytheG term, andbecausethistermstartstoexportenergyoutside
E
the domain.
The ∂KE term also experiences decreases, presenting a reversal in sign, despite the
∂t
enhanced barotropic conversions (C term), indicating a weakening of the eddy activity.
K
This is due to the combined effect of the reduced conversion from A — indicating an
E
overall reduction in zonal temperature gradients — and the reversal in sign of BK , as
E
the eddy begins to export energy outside the domain, alongside further increases in the
magnitude of the RK term.
E
Lastly, in the decay phase following the mature phase, most terms present a further
overall reduction in magnitude. The ∂AZ reverts to its original positive values, driven
∂t
by the enhanced imports of energy. A similar behavior is observed for ∂KZ, presenting
∂t
comparable magnitudes to their values during the incipient phase. This scenario suggests
that as the eddy decays, the atmosphere regains its original behavior, with the equator-
to-pole temperature gradients increasing and the zonal jets strengthening.
The ∂AE term also presents a magnitude comparable to the incipient stage. However,
∂t
the A boundary and generation terms present opposite signs during the decay phase
E
comparedtotheincipientphase, withG beingpositiveduetoresidualconvectiveactivity,
E
although less vigorous than in previous phases, and minimal exports of A through the
E
boundaries. DespitethedecreaseinmagnitudeofRK , thereducedcontributionsfromC
E E
— due to weakened zonal gradients — and C — due to reduced barotropic conversions
K
— along with the enhanced export of energy, result in the K term presenting its largest
E
decreases across all phases.
Notably, the energy fluxes often maintain the same direction across all development

189
Section5.2.ClimatologyAcrossLifePhases
phases, although the terms exhibit notable variations in magnitude. For instance, both
the baroclinic chain and the barotropic conversion term are active throughout the entire
life cycle. For baroclinic disturbances, this consistency in the baroclinic chain is expected
(Pezza et al., 2010; Dias Pinto and Rocha, 2011; Black and Pezza, 2013, e.g.,), although
highvariabilityispresentandthisbehaviorcanvaryfromcasetocase(Figure5.11). Regar-
ding barotropic conversions, some studies report its predominance in extratropical cyclone
development (Michaelides, 1987; Wahab et al., 2002; Bulic, 2006; Cavicchia et al., 2018,
e.g.,), while others do not (Pezza et al., 2010; Dias Pinto and Rocha, 2011, e.g.,). Here, it is
believed that the choice of computational domain as well as the use of a Semi-Lagrangian
framework might aid in making barotropic conversions more evident (Michaelides et al.,
1999). The next sections will explore this more deeply.
The contributions from G are negative during the incipient phase, peaking during
E
intensification, and diminishing afterward, which is consistent with previous studies (Mi-
chaelides, 1987; Dias Pinto and Rocha, 2011; Wahab et al., 2002, e.g.,), although those
studies analyze the RG term, making direct comparisons difficult. While the moist ba-
E
roclinic chain is most intense during the intensification phase, the barotropic conversion is
most intense during the mature phase. The RK and RK terms are also consistent across
Z E
all phases: RK provides energy to K , while RK acts as a sink of energy. Although
Z Z E
both residuals aggregate a combination of terms, making it difficult to attribute the overall
behavior to a specific term, the results presented here align with Smith (1980), which in-
dicated high generation of kinetic energy by cross-contour flow and high dissipation of K
E
throughout the system’s life cycle. Moreover, the overall paradox related to the negative
sign of the term ∂AE might be attributed to the inclusion of numerical errors in the energy
∂t
budget.
Figure 5.16 displays the Lorenz Energy Cycle (LEC) for the mean values of each term
for the second development cycle. The overall energy flux for each LEC term remains
the same as for the first development cycle: the baroclinic chain is most active during the
second intensification phase, while the barotropic conversion term is most active during the
second mature phase, along with higher RK . Notably, the ∂AE term presents positive
E ∂t
values during the second intensification, while, for the same phase, the RK shows its
Z
lowest values and C its highest values across all phases. Furthermore, the values of C
K A
and C are lower than their respective counterparts in the first development cycle. These
E

190
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
results suggest that distinct dynamical processes are related to the development during
the second cycle.
(A) (B)
(C)
Figure5.16: MeanvaluesoftheLorenzEnergyCycle(LEC)termsforeachphaseofthecyclonessecondary
development: intensification 2 (A), mature 2 (B), and decay 2 (C). Each blue box represents an energy
component,witharrowsshowingthedirectionofenergyflow. Thenumbersadjacenttothearrowsindicate
the magnitude and direction of the energy flux, with green indicating positive values and red indicating
negative values. A representation of the complete cycle, with the positioning of each term can be found
at Figure 5.7.
The analysis of the LEC across different development phases reveals significant insights
into the energy dynamics of cyclonic systems. During the incipient phase, there is a
notable increase in A , primarily due to imports rather than generation, with conversions
Z

191
Section5.2.ClimatologyAcrossLifePhases
to K and A occurring. The intensification phase sees enhanced eddy-related convective
Z E
processes and thermally direct circulation, leading to increased conversions from A to
E
K . The mature phase is characterized by a reduction in overall energy magnitudes and
E
a weakening of zonal jets. In the decay phase, the system’s energetics further diminish,
suggesting a reversion to the atmosphere’s original state.
The second development cycle exhibits similar energy flux patterns, with distinct varia-
tions in the intensity of key energy fluxes, indicating an enhanced importance of barotropic
conversions. These findings underscore the importance of both baroclinic and barotropic
processes in different phases. The baroclinic chain is especially important during the in-
tensification phase, consistent with previous studies on extratropical cyclone development,
while barotropic conversions become more evident in the mature phase and in the secon-
darydevelopmentcycle. Theobservedhighvariabilityandtheintegrationofresidualterms
into the budgets suggest that numerical errors and domain choices significantly influence
the interpretation of these energy cycles.
5.2.3 EOFs
Similar to the mean behavior presented in Section 5.1.2, the results for the mean beha-
vior across each life phase exhibit high variability. Therefore, each term can span a wide
range of possible values, possibly resulting in reversals of energy fluxes. To delineate an
overall picture of the LEC across each phase for cyclones in the SESA region, unlike the
presentation in Section 5.9, the reconstructed EOFs will be analyzed. These were compu-
ted by reversing the normalization process and adding back the mean to each EOF. Here,
the analysis is limited to the first developmental cycle for simplicity, justified by the higher
prevalence of systems that only present one developmental cycle.
Figure 5.17 illustrates the proportion of variance in the dataset that is explained by
each of the first four Empirical Orthogonal Functions (EOFs) for each life phase. As shown
for the EOFs representing the mean LEC behavior, the first four EOFs explain the main
modes of variability contained in the data. For practical reasons, only the first four EOFs
will be explored. Similar to the total life cycle, the first EOF accounts for the largest
portion of the variance for all phases, explaining approximately 26% to 30%, indicating it
captures the most significant pattern in the data. The exception is the incipient phase,
where EOF1 explains approximately 21% of the variance in the data. Meanwhile, the

192
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
subsequent EOFs explain progressively smaller proportions of the variance. Furthermore,
as discussed in Section 5.9, the PCs will not be presented as they would merely represent
the signal magnitude across the distinct cyclones rather than any physical feature.
Figure 5.17: Proportion of variance in the dataset explained by the first four Empirical Orthogonal
Functions (EOFs), for each development phase.
For EOF1 (Figure 5.18), most terms reinforce the overall behavior presented for the
mean values across each phase (Figure 5.15). An enhancement of both the baroclinic
chain and the barotropic conversion from K to K is consistent across all phases. Both
Z E
instabilities increase in activity during the life cycle, decreasing at the onset of the decay
phase: the baroclinic chain presents higher values during the incipient phase and peaks
during the intensification phase, while the barotropic conversion peaks during the mature
phase. Notably, the G term is enhanced and positive throughout all phases, peaking
E
during intensification, indicating overall enhanced convective activity for this EOF.
Furthermore, RK is highly enhanced, resulting in positive tendencies for ∂KZ. Howe-
Z ∂t
ver, this positive tendency is not significantly above the average, as most of the excess
energy is exported outside the domain via the BK term. A similar behavior is found for
Z
∂KE. Despite the increased energy influxes for K , they are accompanied by significant
∂t E
increases in RK , which sinks that extra energy. Additionally, despite the enhanced im-
E
ports of K during the incipient and intensification phases, the mature and decay phases
E

|         |          | Section5.2.ClimatologyAcrossLifePhases |     |     |     | 193 |
| ------- | -------- | -------------------------------------- | --- | --- | --- | --- |
| observe | enhanced | exports.                               |     |     |     |     |
Other distinctions from the mean behavior are found in the budgets for A and A
Z E
terms. For A , there is a negative tendency during the incipient phase, indicating a we-
Z
akening of the meridional temperature gradients during the cyclone’s initial development.
Meanwhile, for the A budget, an enhancement above the mean conditions is observed,
E
resulting in a positive budget for the incipient and intensification phases. This indicates
that the negative values found in the mean behavior might be attributed to the presence
of outliers.
In EOF2, the overall mean behavior is weakened for most terms (Figure 5.19). Notably,
during the incipient stage, there is a deviation in the energy flux from K : a reversal in
Z
the sign of the C term and a reduction in barotropic conversions are observed. The
Z
negative C , accompanied by negative G and positive C , indicates an overall weakening
|     | Z   |     | Z   | A   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
of the meridional gradient in vertical motions. During this stage, there is also a stronger
than average negative G but a strengthening of C , which is explained by imports of A
|         |                 | E   |     | E   |     | E   |
| ------- | --------------- | --- | --- | --- | --- | --- |
| through | the boundaries. |     |     |     |     |     |
For the remaining phases, the import of A reduces, the barotropic conversion pro-
E
gressively increases, and the G term is similar to the mean behavior. Despite this, ∂KE
E
∂t
presents a below-average tendency. This can be explained by the enhancement of sinks
via the RK term during the intensification and mature phases, and the progressively
E
increased exports of K . During the decay phase, although the sink from the RK term
|     |     | E   |     |     | E   |     |
| --- | --- | --- | --- | --- | --- | --- |
reduces significantly while C is strongest, this is compensated by the highest exports of
K
| energy | and the weakest | conversions | from A . |     |     |     |
| ------ | --------------- | ----------- | -------- | --- | --- | --- |
E
Furthermore, from the intensification phase onwards, an enhancement of RK can be
Z
seen, which, similar to EOF1, is followed by an enhancement of exports of K . During
Z
the decay phase, ∂AZ presents significant increases, followed by a reversal in the sign of C
|     |     | ∂t  |     |     |     | Z   |
| --- | --- | --- | --- | --- | --- | --- |
compared to previous states. These combined processes result in an enhancement of ∂KZ,
∂t
| making | it twice the | average mean. |     |     |     |     |
| ------ | ------------ | ------------- | --- | --- | --- | --- |
For EOF3, the inter-phase variability is less marked (Figure 5.20). Across all phases,
there are high values of RK , which — similarly to the previous EOFs — are almost
Z
compensated by exports of K . There is also a consistent conversion from A to K and
|     |     | Z   |     |     | Z   | Z   |
| --- | --- | --- | --- | --- | --- | --- |
imports of A . During the incipient phase, positive ∂AZ is found due to the importation
|     | Z   |     |     | ∂t  |     |     |
| --- | --- | --- | --- | --- | --- | --- |
of energy and positive generation (G ). There is then a conversion of A into A and K .
|     |     |     | Z   |     | Z E | Z   |
| --- | --- | --- | --- | --- | --- | --- |

194 Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
| (A) |     |     | (B) |
| --- | --- | --- | --- |
| (C) |     |     | (D) |
Figure 5.18: Reconstructed first EOF (EOF1) of Lorenz Energy Cycle (LEC) Terms, illustrating energy
fluxes across each phase of the first development cycle: incipient (A), intensification (B), mature (C) and
decay (D). The numbers adjacent to the arrows denote the magnitude and direction of the anomaly, with
| green indicating | positive values | and red indicating | negative values. |
| ---------------- | --------------- | ------------------ | ---------------- |

Section5.2.ClimatologyAcrossLifePhases 195
| (A) |     |     | (B) |
| --- | --- | --- | --- |
| (C) |     |     | (D) |
Figure5.19: ReconstructedsecondEOF(EOF2)ofLorenzEnergyCycle(LEC)Terms,illustratingenergy
fluxes across each phase of the first development cycle: incipient (A), intensification (B), mature (C) and
decay (D). The numbers adjacent to the arrows denote the magnitude and direction of the anomaly, with
| green indicating | positive values | and red indicating | negative values. |
| ---------------- | --------------- | ------------------ | ---------------- |

196
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
∂AZ is unusually high due to the enhanced RK and thus provides above-average energy to
∂t Z
K . This kind of situation might represent a change in the large-scale circulation outside
E
the Semi-Lagrangian domain, such as the breaking of a blocking circulation. Investigating
such occurrences is beyond the study goals and is left as a suggestion for future research.
Meanwhile, ∂AE is increasing — due to the combined effects of C , imports, and enhan-
∂t A
ced convective activity — and is providing energy to K . This term, in turn, is exporting
E
energy and losingit via RK . During the intensification and mature phases, the imports of
E
A become exports of energy, while the barotropic conversion becomes the highest contri-
E
butor to K . Meanwhile, the RK term peaks at the mature phase, decreasing afterward.
E E
Lastly, during the decay phase, most LEC terms are below average, indicating a weaker
eddy at later stages.
In EOF4, most terms generally present lower magnitudes across all phases than in
the mean behavior, indicating that this EOF corresponds to weaker systems development
(Figure 5.21). The RK presents above-mean values only during the incipient phase,
Z
where both C and C contribute equally to K . However, during this phase, G is
K E E E
negative and C is low, with the main contributor to A being the imports of energy.
A E
As the system develops, G becomes positive, peaking during the mature phase, and C
E A
increases, peaking during the intensification phase. Notably, for the first time, C is
K
positive during the decay phase.
In summary, EOF1 displays a strengthening of the mean behavior — a scenario where
themoistbaroclinicchainandbarotropicconversionssustaintheeddythroughoutitsentire
life cycle. The former is most intense during the incipient and intensification phases, while
the latter is strongest during the mature and decay phases. In EOF2, cyclogenesis and
initial development are triggered mostly by imports of A and K and the import of
E E
the former continue until the mature phase. Meanwhile, there is a consistent increase
in barotropic conversions through the life cycle. In this case it seems that instead of
intensifying the cyclone, the barotropic conversion acts as impeding it to decay earlier.
For EOF3, although the initial development is fueled by the moist baroclinic chain in
conjunctionwithimportsofA , barotropicconversionsdominateduringtheintensification
E
and mature periods. In the decay phase, all terms are weakest. For all EOFs 1, 2, and
3, during later development stages, high barotropic conversions are typically observed.
However, they are not sufficient to surpass the loss of energy from exports and the RK
E

Section5.2.ClimatologyAcrossLifePhases 197
| (A) |     |     | (B) |
| --- | --- | --- | --- |
| (C) |     |     | (D) |
Figure 5.20: Reconstructed third EOF (EOF3) of Lorenz Energy Cycle (LEC) Terms, illustrating energy
fluxes across each phase of the first development cycle: incipient (A), intensification (B), mature (C) and
decay (D). The numbers adjacent to the arrows denote the magnitude and direction of the anomaly, with
| green indicating | positive values | and red indicating | negative values. |
| ---------------- | --------------- | ------------------ | ---------------- |

198 Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
| (A) |     |     | (B) |
| --- | --- | --- | --- |
| (C) |     |     | (D) |
Figure5.21: ReconstructedfourthEOF(EOF4)ofLorenzEnergyCycle(LEC)Terms,illustratingenergy
fluxes across each phase of the first development cycle: incipient (A), intensification (B), mature (C) and
decay (D). The numbers adjacent to the arrows denote the magnitude and direction of the anomaly, with
| green indicating | positive values | and red indicating | negative values. |
| ---------------- | --------------- | ------------------ | ---------------- |

199
Section5.3.SummaryandConcludingRemarks
term, resulting in ∂AE < 0. Lastly, for EOF4, while the initial development is related
∂t
to imports of both A and K , the barotropic and especially the moist baroclinic chain
E Z
lead to eddy growth. Nonetheless, the lower than average values indicate that this EOF is
related to the development of weaker systems.
5.3 Summary and Concluding Remarks
This chapter delves into the energetics of cyclones in the Southwestern Atlantic, fo-
cusing on the Lorenz Energy Cycle (LEC) for 7,531 cyclonic systems originating in the
ARG, LA-PLATA, and SE-BR regions. It presents the first comprehensive dataset for the
South Atlantic, offering insights into the energetics of these systems over their complete
life cycles and development phases. The LEC was computed using limited-area energetics
through a Semi-Lagrangian approach, following the method proposed by Michaelides et al.
(1999). Therefore, some limitations might be recognized: the results presented represent
the limited-area contributions to the global energetics (Smith, 1969), while the formulati-
ons used do not account for the displacement related to the moving domain (Michaelides
et al., 1999). However, we advocate that by adopting the snapshot approach, where each
computational domain represents a fixed domain individually, each contribution can be
treated individually for each time-step. For small time-steps, the aggregate contribution
would represent the evolution of the eddy environment energetics.
The results presented in this chapter demonstrate that the LEC terms exhibit high
variability and many outliers, explaining the differences in results found among previous
studies. The Semi-Lagrangian framework overall results in higher mean values for K and
Z
smaller mean A than those reported by previous studies. This effect is attributed to
Z
the isolation of the jet features in the domain plus the reduced meridional temperature
gradients compared to when large domains are adopted. For the remaining terms, their
variable behavior hinders direct comparison with the literature. However, the mean LEC
behavior, presenting an overall importance of the baroclinic chain in consonance with the
barotropic conversion term, corroborates previous findings.
Here, theLECisaccessedfromcyclogenesisuntilthemomentthetrackingmethodology
stops following a given system. This moment is then considered the cyclolysis. How the
environmental energetics behave pre-cyclogenesis or post-lysis remains an open question

200
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology
and is beyond the scope of the current study. The EOF analysis demonstrates that for
both the mean behavior and across each life cycle phase, the main variability is related
to the enhancement of the moist baroclinic chain and barotropic conversions from the
zonal jets to the eddies. This reinforces the conclusion that the main contributions to the
eddy environmental energetics come from the moist baroclinic chain in consonance with
barotropic conversions. These indicate that most cyclones’ life cycles are modulated by
the meridional temperature gradients, which are converted into kinetic energy by eddy
motion. At the same time, the cyclones are also receiving momentum from the zonal jets.
This mean behavior is observed across all life phases, from cyclogenesis, often strengthened
during the intensification and mature phases, and weakened during the decay.
While these processes initiate and contribute to eddy growth, in later life stages, the
RK termandexportsofK resultintheeddy’sdecayanddissipation. AlthoughtheRK
E E E
term also aggregates numerical errors and the BΦE term, whose physical interpretation
is not obvious, the presented results suggest that most of this term’s signal is related
to the dissipation of energy, which is consistent with Smith (1980). Nevertheless, there
are also a smaller, although significant number of cases where the mechanisms leading
to eddy growth are distinct, such as imports of either or both eddy forms of energy (A
E
and K ). Michaelides et al. (1999) previously associated imports of K with downstream
E E
development (Simmons and Hoskins, 1979), a mechanism previously noted in some cases
of cyclone development in the South America region (Piva et al., 2010; Rosa et al., 2013).
Meanwhile, the A imports have not been thoroughly discussed previously and will be
E
furtherexploredinthenextchapter. Additionally, theresultsindicatedistinctmechanisms
related to the secondary development phases, but these were not fully explored as they
represent a minority of cyclones in the dataset.
Meanwhile, ubiquitous high values of RK are found across distinct phases and LEC
E
configurations. Again, this term’s interpretation is difficult. However, as the zonal circula-
tionisoftenprovidingkineticenergytotheeddycirculation(C < 0), itispossibletoinfer
K
that the positive values of RK are not related to upscaling of energy from smaller scales
Z
(D > 0). Thus, it might seem that the positive values of RK are associated with the
Z Z
BΦK term, which is further supported by the high values computed for this term. Future
research on elucidating this term’s physical interpretation and post-processing methods to
ensure its validity against small errors in the geopotential field would further reveal new

201
Section5.3.SummaryandConcludingRemarks
insights into cyclonic dynamics.
The high values of RK throughout the systems’ entire life cycle indicate that this
Z
methodology may not be ideal for studying large-scale circulation, which is understandable
given its focus on individual systems. However, the results are consistent and provide new
perspectives on cyclone energetics. Due to the high variability in the data, it was not
possibletoanalyzeseasonalityandtemporaltrends: whileanalyzingthemeanwouldreveal
little about the seasonality and/or long-term trends in the energetics of the systems in
general, using EOFs would make such an analysis impractical. The next chapter attempts
to use a different perspective, enabling such analyses to be performed.

202
Chapter5.SouthwesternAtlanticCyclonesEnergeticsClimatology

6
Chapter
Energetic Patterns of Cyclones in the Southwestern
Atlantic
Chapter 5 investigated the LEC climatology for the cyclones with genesis in the South
American sector. Although the mean behavior across all systems was discussed, the results
exhibited high variability, which hindered a deeper analysis of patterns that deviated from
thenorm. ThischapterwillemployclusteringanalysistodeterminepatternsintheLEC—
energy patterns — related to eddy development, so this variability can be further assessed.
6.1 Lorenz Phase Space and Energy Patterns
6.1.1 Introducing the Lorenz Phase Space
The first step in constructing the energy patterns (EP) involves devising a visuali-
zation that could facilitate the understanding of the environmental energetics related to
cyclonic systems. As demonstrated in Chapter 5, the usual LEC visualization (where ar-
rows representing energy fluxes connect the distinct energy terms) is a powerful tool for
understanding the atmospheric dynamics associated with atmospheric systems and their
evolution. However, it is not practical for large datasets and considering multiple phases
denoting the systems’ evolution over time, as is the case here. Therefore, the goal of this
section is to devise a new visualization tool that simplifies this process while maintaining
the focus on displaying the dynamics related to eddy development, i.e., related to their
Efficient and Final Causes (Sections 2.1.3 and 2.1.4).
Figures 6.1 and 6.2 contain Phase Diagrams, inspired by the Cyclone Phase Space
created by Hart (2003), in which distinct sets of the LEC terms are represented. These

204
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
representations are called Lorenz Phase Space (LPS) diagrams. As mentioned, these di-
agrams focus on the mechanisms related to eddy growth. Evidently, there is a trade-off
between representing as many terms as possible but keeping some degree of simplicity,
while still providing an intuitive visualization.
Figure 6.1: Lorenz Phase Space (LPS) diagram 1 for ”Reg1”cyclone (Dias Pinto and Rocha, 2011). The
x-axis represents the barotropic conversion term (C ), which indicates the conversion from zonal to eddy
K
kinetic energy, while the y-axis shows the baroclinic conversion term (C ). The color shading denotes
A
the generation of eddy potential energy (G ), with warmer colors indicating higher convective activity
E
and cooler colors representing lower activity. The size of the circles correlates with the system intensity,
measured by K . The letters ”A”and ”Z”mark the system’s initial and final positions, respectively. The
E
pointwherethesystemreachesitspeakintensityishighlightedbyathickcircleborder. Thediagonalline
in the upper left quadrant represents the 1:1 line, indicating that when the system is below this line, the
barotropic term dominates, while above it, baroclinic conversions are more significant.
Figure 6.1 displays the LPS representing the main terms related to dynamical instabi-
lities in the atmosphere. The x-axis represents the barotropic conversion term (C ), the
K
y-axis the baroclinic conversion term (C ), while the color shading represents the con-
A

205
Section6.1.LorenzPhaseSpaceandEnergyPatterns
vective activity (G ) and the circle sizes represent the system intensity (K ). There is
E E
also an ”A”and a ”Z”representing the system’s initial and final positions, and the moment
where the system is most intense is marked by a thick circle border. Meanwhile, Figure 6.2
illustrates the LPS related to imports of Eddy Energy. This diagram is similar to Figure
6.1, but here the x-axis represents importation and exportation of eddy APE across the
system boundaries (BA ), while the y-axis shows the importation and exportation of eddy
E
kinetic energy across the system boundaries (BK ).
E
The choice for using the C term in the LPS diagram (Figure 6.1) is justified by its high
A
correlation with the C term (Appendix D). Thus, when positive conversions from A to
E Z
A occur, there is a high probability that conversions from A to K are also happening,
E E E
indicating an active baroclinic chain. Additionally, since the second LPS diagram (Figure
6.2) represents the imports of A and both LPS diagrams indicate G , the C signal can
E E E
be inferred. Meanwhile, the K was chosen to represent the system’s intensity because it
E
generally increases from genesis to the mature phase and decreases during the decay phase
(Section 5.2). It also correlates well with central relative vorticity at 850 hPa (Appendix
D).
On Figures 6.1 and 6.2, the energetics of the ”Reg1”system from Dias Pinto and Rocha
(2011)areanalyzedusingtheLPSdiagrams. Here, forcomparisonwiththeoriginalresults,
the same computational procedure as from Dias Pinto and Rocha (2011) is used (Eulerian
Framework), for the same domain, as well as the same dataset (NCEP-R2 reanalysis). The
computational domain and time series for energy and conversion terms are presented in
Appendix E. The only difference is that here G is used instead of RG , in order to allow
E E
for a physical interpretation of this term’s contributions.
Using the LPS diagrams, one can easily identify the dynamical mechanisms inciting
eddy development associated to the cyclone system. For instance, Figure 6.1 indicates
that during the system’s early life stages, baroclinic and barotropic conversions provided
support for its development, as well as contributions from convective processes (evidenced
by G ). As the system’s life progresses, the importance of baroclinic conversions and
E
convective processes diminishes, with both terms becoming negative and the eddy being
sustained only by barotropic conversions. During later periods, G is negative, and the
E
eddy is feeding the zonal circulation, as well as K being converted to A .
E E
Negative G indicates APE destruction, (i.e., cooling where temperature perturbation
E

206
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
ispositiveandwarmingwheretemperatureperturbationisnegative). Coolingisassociated
to either evaporative cooling or long wave radiative energy loss. Warming is either asso-
ciated to latent/fusion heating or short wave radiative energy loss. Sensible heating near
the surface can be positive or negative, depending on the temperature difference between
the surface and the air.
Meanwhile, Figure 6.2 shows that in the initial development stages, there were exports
of both A and K outside the domain, but as the system developed, both boundary
E E
terms reverted to imports of energy, with higher magnitudes than the conversion terms
displayed in Figure 6.1. Also, in later development stages, as the combined magnitudes
of C and BA were lower than G , it can be inferred that C < 0, so the eddy-driven
A E E E
thermalcirculationhadstopped, andtheequator-to-poletemperaturegradientswerebeing
reestablished.
6.1.2 Energetic Patterns for All Life Cycle Configurations
The LPS diagrams containing all systems for the SESA region for the 1979-2020 period
can be found in Appendix F. Due to the large amount of data and the presence of outliers,
it is not possible to discern the relative importance of the LEC terms for smaller groups
of systems precisely. Therefore, the K-means algorithm is employed to group the energy
cycles into distinct representative clusters.
The first attempt at clustering all cyclones’ energetics in the dataset is performed for
all major lifecycle configurations, presented in Chapter 4 (Figure 4.3b). Thus, the LEC
termswereaveragedforeachlifecyclephase, andeachlifecycleconfigurationwasclustered
independently. For all life cycle configurations analyzed, the elbow method returned an
ideal number of clusters as 3, as represented in Figure 6.3. This figure corresponds to the
”Incipient, Intensification, Mature, Decay”life cycle configuration, but the plots for each
configuration were nearly identical.
Figures 6.4 and 6.5 present the LPS diagrams for the centroids of the three clusters
for each life cycle configuration. On these diagrams, each circle represents the energetics
correspondingtoadistinctlifecyclephase, initiatingontheincipientphase(A)andending
of either the first or second decay phases (Z). The centroids, which represent the mean
positionsofalldatapointswithinacluster,serveasrepresentativeprofilesoftheLECterms
for the respective clusters. These centroids are not actual data points from the dataset

207
Section6.1.LorenzPhaseSpaceandEnergyPatterns
Figure 6.2: Lorenz Phase Space (LPS) diagram 2 for ”Reg1”cyclone (Dias Pinto and Rocha, 2011). The
x-axis represents importation and exportation of eddy APE across the system boundaries (BA ), while
E
the y-axis shows the importation and exportation of eddy kinetic energy across the system boundaries
(BK ). The color shading denotes the generation of eddy potential energy (G ), with warmer colors
E E
indicating higher convective activity and cooler colors representing lower activity. The size of the circles
correlates with the system intensity, measured by K . The letters ”A”and ”Z”mark the system’s initial
E
and final positions, respectively. The point where the system reaches its peak intensity is highlighted by
a thick circle border.

208
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
Figure6.3: Elbowmethodplotfordeterminingtheoptimalnumberofclusters. Thex-axisrepresentsthe
numberofclusters(k), whilethey-axisindicatestheSumofSquaredErrors(SSE).Thepurplelineshows
the SSE for each k value. The red dot highlights the optimal number of clusters (k=3), where the SSE
begins to decrease at a slower rate, forming an ”elbow.”This point suggests that three clusters provide a
good balance between minimizing variance within clusters and model simplicity.

209
Section6.1.LorenzPhaseSpaceandEnergyPatterns
but synthetic constructs that encapsulate the average characteristics of the LEC terms
within each cluster. Consequently, they provide a generalized yet insightful depiction of
the typical energy dynamics observed in the cyclonic systems classified within each cluster.
This clustering approach allows us to identify and characterize distinct energetic patterns
(EPs), facilitating a deeper understanding of the underlying physical processes driving the
variability in cyclonic energetics.
The LPS 1 diagram (Figure 6.4) indicates similar patterns emerging for all life cycle
configurations, with systems often initiating in low energy states. As they intensify, both
baroclinicandbarotropicconversions, aswellasconvectiveactivity, becomemorevigorous.
Meanwhile, when the systems are decaying, they tend to revert back to lower energy states.
The EPs within the same life cycle group usually differentiate from each other by the
magnitude of the conversion and generation terms in each phase. It is notable that C
K
is usually higher than the other forms of energy, while G and C present comparable
E A
magnitudes. This reinforces the conclusion in Chapter 5 that barotropic conversions are
one of the main mechanisms driving cyclone development in the SESA region.
Therearesomeexceptionstotheoverallenergeticdevelopmentpatterndescribedabove.
For example, for the ”intensification, mature, decay”configuration (Figure 6.4b), there is
an EP which already initiates with relatively high conversion levels and convective activity,
decreasing in later stages, while another pattern starts with the highest G values for this
E
life cycle configuration EPs. Enhanced convective activity in the initial stages can also
be noted for the configuration where ”intensification, mature, decay”repeats twice (Figure
6.4d). This enhancement of energy conversion and/or generation is expected for these
configurations, as they lack an incipient stage. In the Cyclophaser program, the incipient
stage is not detected if the system’s life starts with a relatively steep increase in relative
vorticity (becoming more negative, i.e., becoming more intense) and if this process is fast
enough that the duration criteria for phase detection are not met. Therefore, the LPS
diagram 1 suggests that for these cases, the enhanced conversions/generation in earlier
life periods are responsible for an abrupt intensification phase and the lack of an incipient
phase.
Furthermore, another exception can be found in systems presenting an early decay
phase (Figure 6.4f). In this case, one EP starts with a high energy state and then reverts
to lower energy states as the system evolves. This EP, which roughly corresponds to only

210
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
(A) IcItMD (B) ItMD
(C) IcItMDIt2M2D2 (D) ItMDIt2M2D2
(E) IcDItMD2 (F) DItMD2
Figure6.4: LorenzPhaseSpace(LPS)diagram1forallmainlifecycleconfigurations(Figure4.3b). ”Ic”,
”It”, ”M,”and ”D”denote incipient, intensification, mature, and decay phases, respectively, while a ”2”is
used to denote their second occurrence within the same life cycle configuration.

211
Section6.1.LorenzPhaseSpaceandEnergyPatterns
3% of the variability for this life cycle, representing less than 3% of the cyclones in the
total dataset, is composed of only four systems. Further examination revealed that this
high energy state is linked to an outlier within this EP, while the other systems start in
lower energy states (Appendix G). Although further examination of the dynamics related
to this outlier is of interest, it is beyond the scope of the current study.
The LPS 2 diagram (Figure 6.5) presents a more heterogeneous behavior, although an
overall pattern can still be observed. Systems often initiate with imports of A , which de-
E
crease as they develop. During the intensification phase, imports of K increase, diminish
E
in the mature phase, and revert to exports of K during decay. As with LPS 1, the clusters
E
for each life cycle configuration tend to differentiate from each other by the magnitude of
the boundary and generation terms in each phase. The magnitude of the boundary terms
is often comparable to C and G , and for some EPs at specific phases, they present
A E
higher values, comparable to C values. Similarly, as noted for LPS 1, the EPs lacking an
K
incipient stage often initiate in higher energy states, reinforcing the argument that rapid
intensification in these cases is related to an enhanced energy cycle. Meanwhile, the outlier
for the life cycle configuration with an early decay can still be noted (Figure 6.5f).
Given that the behavior presented by the EPs shows low variability among distinct life
cycle configurations, the next sections will focus on the EPs for the ”incipient, intensifica-
tion, mature, decay”configuration for simplicity (Figure 6.4a). This choice is also justified
by the prevalence of this life cycle configuration within the dataset, representing nearly
60% of all systems (Figure 4.3b). This approach allows for more detailed analysis while
maintaining the potential for generalizing the results.
6.1.3 Energetic Patterns - Seasonality and Spatial Variability
While Section 6.1.2 focused on the differences of the EPs among the distinct life cycle
configurations, the present section will investigate their seasonality and spatial variability.
As previously discussed, the focus will be on the EPs for the ”incipient, intensification,
mature, decay”life cycle configuration. The spatial and seasonal variability is assessed
by employing the clustering technique for the distinct seasons and genesis regions in the
Southwestern Atlantic region: ARG, LA-PLATA, and SE-BR, as delineated in Chapter
4. For this analysis, the K-means algorithm was initialized for each region and season
separately. As in Chapter 4, only austral summer (DJF) and winter (JJA) are assessed.

212
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
(A) IcItMD (B) ItMD
(C) IcItMDIt2M2D2 (D) ItMDIt2M2D2
(E) IcDItMD2 (F) DItMD2
Figure6.5: LorenzPhaseSpace(LPS)diagram2forallmainlifecycleconfigurations(Figure4.3b). ”Ic”,
”It”, ”M,”and ”D”denote incipient, intensification, mature, and decay phases, respectively, while a ”2”is
used to denote their second occurrence within the same life cycle configuration.

213
Section6.1.LorenzPhaseSpaceandEnergyPatterns
Figure 6.6 presents the LPS 1 diagram for the EPs related to each region, for JJA
and DJF. Notably, for each season-region group, the elbow method detected an optimal
number of clusters as three, similarly to the EPs for all systems. It can be seen that the
overall behavior is preserved across the distinct seasons and regions: the systems often
initiate in lower energy states, and as they develop, the energy conversions, as well as
convective activity, become more intense. Within each group, each distinct EP represents
an overall higher energy state: one EP presents more neutrality for C , C , and G for
A K E
all life phases, while the second and third EP progressively present higher conversions and
often higher generation of A .
E
(A) (B) (C)
(D) (E) (F)
Figure6.6: LorenzPhaseSpace(LPS)diagram1forfortheEPsrelatedtothe”incipient, intensification,
mature, decay”life cycle configuration, across DJF (a, b, c) and JJA months (c, d, e) and for each genesis
region in Southwestern Atlantic Region: ARG (a, d), LA-PLATA (b, e) and SE-BR (c, f).
Despite the apparent similarity across the distinct groups, some seasonality and inter-
regional variability can be noted. The most notable distinction is in the G term: LA-
E
PLATA EPs tend to present higher G values compared to the other regions, with ARG
E
presenting relatively low values for both seasons. For both cases, there is no distinction
between each season. Meanwhile, for SE-BR, JJA systems present overall higher G than
E
DJF systems. For the conversion terms, each group consistently presents EPs that can
be interpreted as having lower, medium, and higher energy states, which are very similar
among the groups. However, for LA-PLATA and SE-BR during JJA, there are two groups

214 Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
| with higher | energy states | instead. |     |     |
| ----------- | ------------- | -------- | --- | --- |
| (A)         |               | (B)      |     | (C) |
| (D)         |               | (E)      |     | (F) |
Figure6.7: LorenzPhaseSpace(LPS)diagram2forfortheEPsrelatedtothe”incipient, intensification,
mature, decay”life cycle configuration, across DJF (a, b, c) and JJA months (c, d, e) and for each genesis
region in Southwestern Atlantic Region: ARG (a, d), LA-PLATA (b, e) and SE-BR (c, f).
Meanwhile, for the LPS 2 diagram, the seasonal and inter-regional variability is more
evident. For ARG, during both seasons, all EPs initiate with similar imports of A , with
E
the magnitude of K imports increasing in the distinct EPs. During the intensification
E
phase, K imports increase, while A imports tend to neutrality. In the mature phase,
E E
K tends to neutrality, while the systems start to export A . Lastly, in the decay stage,
| E   |     |     |     | E   |
| --- | --- | --- | --- | --- |
the boundary terms tend to neutrality, except for one cluster, where there are relatively
| high exports | of K , accompanied | by lesser exports | of A . |     |
| ------------ | ------------------ | ----------------- | ------ | --- |
|              | E                  |                   | E      |     |
For LA-PLATA during DJF, two clusters initiate importing A , with K imports in-
E E
creasing during the intensification phase. These imports are higher for one of the EPs.
For the remaining phases and the other EP, the boundary terms tend to neutrality. For
JJA, one cluster begins with A imports, tending to neutrality in later phases. Meanwhile,
E
another cluster starts with high imports of A , with K imports increasing but still mo-
E E
derate in the intensification phase, and both terms tending to neutrality later. For the
remaining EP, there are initial imports of A , high K imports in the mature phase, and
E E
| then finishing | near neutrality. |     |     |     |
| -------------- | ---------------- | --- | --- | --- |
Lastly, for SE-BR, the imports, especially of A , seem to be of lesser importance. For
E

215
Section6.1.LorenzPhaseSpaceandEnergyPatterns
DJF, all but one EP present neutrality for the import of both forms of energy, with the
exception related to imports of K in the initial phases and exports in the mature and
E
decay phases. For JJA, one of the EPs presents neutrality for the boundary terms, except
during the intensification phase, which shows modest contributions of A imports. The
E
remaining EPs start with neutral A imports, with increasing K imports during the
E E
intensification phase. While for one of the EPs, both terms tend to neutrality after the
intensification, for the other, BA becomes negative during the mature phase, though it
E
remains small, and BK becomes negative during decay.
E
In conclusion, utilizing K-means clustering, the analysis for different regions — ARG,
LA-PLATA, and SE-BR — during austral summer (DJF) and winter (JJA) demonstrates
that while overall cyclonic systems generally follow a progression from lower to higher
energystatesthroughgenesisandintensification, thereareregionalandseasonalvariations.
The G term showed distinct regional characteristics, with LA-PLATA exhibiting higher
E
values and ARG showing lower values irrespective of the season, whereas SE-BR systems
displayed higher G during winter. For LA-PLATA, the high G values for both seasons
E E
align with enhanced moisture transport from the South American Low-Level Jet to this
region (Marengo et al., 2004; Drumond et al., 2008), which is an important heat and
moisturesourceforcyclonesforminginthisregion(Gramcianinovetal.,2019). Meanwhile,
during winter, the sea-air temperature gradient, due to the colder atmosphere over the
warm Brazil Current, enhances sensible and latent heat transfer (Everson et al., 2011,
e.g.), which reduces atmospheric static stability and supports convective activity.
Additionally, each region-season group had EPs representing low, medium, and high
energy states, with specific variations observed in LA-PLATA and SE-BR during win-
ter. The LPS 2 diagram further highlighted regional differences in energy import/export
behaviors, with ARG displaying varied import/export dynamics across life cycle phases,
LA-PLATAshowingdifferingpatternsbetweenDJFandJJA,andSE-BRgenerallypresen-
ting neutral energy imports/exports with some phase-specific deviations. These findings
emphasize the importance of baroclinic and especially barotropic conversions for cyclone
development on the SESA region, while imports of both eddy energy forms presents a more
pronounced seasonal and inter-regional variability.

216
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
6.1.4 Energy Patterns - Characteristics
In this section, the main characteristics of the EPs for the ”incipient, intensification,
mature, decay”life cycle configuration will be analyzed (Figure 6.8). As in Section 6.1.2,
these EPs were devised by initializing the K-means algorithm for the LEC results for
systems in the dataset. EP1 presented the highest occurrence probability, relating to 52%
of all systems, while EP2 and EP3 present progressively lesser probabilities of 36% and
11%, respectively. Even when the K-means algorithm was initialized for only the systems
where the minimum relative vorticity is lower than the 0.9 quantile, the detected EPs were
very similar to EP1. This indicates a consistency in the energy cycle for the systems within
the dataset (Appendix H).
(A) (B) (C)
(D) (E) (F)
Figure 6.8: Lorenz Phase Space (LPS) diagrams 1 (a, b, c) and 2 (d, e, f) for EPs 1 (a, d), 2 (b, e), and
3 (c, f), related to the ”incipient, intensification, mature, decay”life cycle configuration.
As indicated in Sections 6.1.2 and 6.1.3, the differences found in the EPs are related to
their energy states. For the three EPs detected, EP1 has a low energy state, with EPs 2
and 3 presenting progressively higher energy states. Figure 6.9 compares the vorticity dis-
tributions across each EP to confirm whether the higher/lower energy states correlate with
higher/lower system intensity. The Kruskal-Wallis test was used to assess overall differen-
ces in vorticity among the clusters, revealing significant disparities. Subsequently, pairwise
comparisons using the Mann-Whitney U test identified specific clusters with significantly

217
Section6.1.LorenzPhaseSpaceandEnergyPatterns
different vorticity values. The plot illustrates that the EPs exhibit significantly different
vorticity values, as indicated by the stars, which represent p-values from the pairwise com-
parisons. Therefore, the hypothesis that each EP represents a distinct intensity cyclone
category is confirmed.
Figure 6.9: Box plot comparing the vorticity distributions among different energy patterns (EPs). The
Kruskal-Wallis test was used to determine if there were statistically significant differences in the vorticity
distributions across the clusters. Significant differences identified by pairwise Mann-Whitney U tests are
annotated on the plot.
In Figure 6.10, the relative frequency of each EP for each genesis region is represented.
For ARG and SE-BR, the regional behavior is similar to the overall frequencies, with the
mostintensesystems(EP3)presentinglowerfrequenciesandrelativefrequenciesincreasing
progressively for EP2 and EP1. However, for LA-PLATA, EP2 presents a higher relative
frequency than EP1. Additionally, this region shows the highest relative frequencies for
EP2 and EP3, indicating that it often generates more intense systems than the others.
Figure 6.11 displays the seasonality of each EP, represented as the counts of the cyclo-
genesis events associated with each EP. These events were defined as the first time step
of the track for each system in the dataset. The results presented here differ from those
presented in Section 6.1.3, as there the EPs for each region-season group were determined
independently, while here, the seasonal behavior of the mean EPs is observed.

218
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
Figure 6.10: Relative regional variability of each energy pattern (EP) for each genesis region in the
Southwestern Atlantic. The annotations alongside each bar represent the total count for each EP for the
given region.
Overall, there is a higher occurrence of EP1 in DJF, followed by SON. EP2 presents a
more homogeneous distribution across seasons, while EP3 is especially active during JJA,
with low activity in DJF. This indicates a higher occurrence of stronger cyclonic systems,
withmoreactiveenergyconversionandconvectiveactivityduringJJA,andweakersystems
during DJF. This result is corroborated by Chapter 4 (Figure 4.10), which indicates the
occurrence of stronger systems during JJA than DJF.
Figure 6.11: Box plot comparing the Seasonality of energy petterns (EPs) in the Southwestern Atlantic
region, with the y-axis representing the percentage of cyclones occurring in each season within the respec-
tive EP.
Figure 6.12 illustrates the interannual variability of each EP from 1979 to 2020. While
the results do not indicate clear trends in EP occurrence over the years, they do reflect
significant interannual differences. Notably, EP3 exhibits higher variability, with relative
yearly frequencies ranging from 1% to 5%, whereas EPs 1 and 2 demonstrate more homo-

219
Section6.2.PhysicalMechanisms
geneous behavior, typically with relative frequencies between 2% and 3%. Exceptionally
high frequencies of EP1 were observed in 1996 and 2013, with particularly low frequencies
in 2016. The relative importance of EP3 is noteworthy due to the impacts caused by
strong cyclonic systems in coastal regions (de Souza and da Silva, 2021; Cardoso et al.,
2022; Leal et al., 2023). This variability could suggest low-frequency climate influences
on cyclone genesis and development in the South Atlantic region, such as those from the
El Nin˜o-Southern Oscillation and the Southern Annular Mode, which will be explored in
future studies.
Figure 6.12: Interannual variability of energy patterns (EPs) from 1979 to 2020. The y-axis represents
the percentage of cyclones each year for different EPs, normalized to total cyclones numbers for each EP.
6.2 Physical Mechanisms
6.2.1 Barotropic and Baroclinic Instability
Through Chapter 5 and Section 6.1 the results for the LEC for all systems forming
on the cyclogenesis regions located near South America, for the period ranging from 1979
and 2020 were explored and discussed. The results indicates an ominous importance of
baroclinicandbarotropicconversionsforthedevelopmentofthecyclonicsystemsanalysed.
The role of baroclinic instability on mid-latitude cyclogenesis, and the further development
of these systems, is deeply established on the literature (Bjerknes and Solberg, 1922; Eady,
1949; Charney, 1947; Petterssen and Smebye, 1971; Hoskins and Valdes, 1990). However,

220
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
the relationship of barotropic instability and extratropical cyclogenesis and development
is not often explored.
Given that the relationship between extratropical cyclones and barotropic instability
might challenge the common notions in the scientific literature, the current section aims
to demonstrate the validity of the presented results. An analysis of the Rayleigh-Kuo
criterion will be performed to determine if barotropic instability is indeed occurring in the
systems analyzed (Section 3.6). For this, only the systems associated with EP1 will be
used, as they present the highest energy states (Figure 6.8). These systems tracks are
represented on Appendix I. Also, only data for the intensification phase will be used, as
these conversions are often strong during this phase and for ensuring the dynamics related
to the system intensification is captured.
Firstly, the vertical levels where the baroclinic and barotropic conversions are most
intense are assessed. Figure 6.13 displays the vertical distribution of C and C terms for
A K
EP1 systems. It can be seen that for C , the most positive values (indicating baroclinic
A
conversions) are found near the surface, at 1000 hPa. This agrees with the Polar Front
Theory, which suggests that low-level baroclinicity initiates cyclogenesis and maintains
cyclone development (Bjerknes and Solberg, 1922), as well as with Petterssen type A
cyclones (Petterssen and Smebye, 1971). Positive mean values can also be seen for C on
A
the upper troposphere, but with smaller overall magnitudes. For barotropic conversions,
however, the lowest values (K → K conversions) are found in the upper troposphere,
Z E
with the lowest mean values at 300 hPa. This vertical distribution of C is consistent with
K
the mean jet vertical positioning, indicating the importance of upper-level jet streams in
providing kinetic energy to the eddy motions.
Given such vertical distributions for C and C terms, composites of meteorological
A K
fields were prepared to assess the occurrence of baroclinic and classical barotropic instabi-
lities at these distinct levels. For this purpose, the maximum Eady Growth Rate (EGR)
fields were evaluated and the Rayleigh-Kuo (RK) criterion was applied. These metrics are
shown in Figure 6.14, for the composites of all systems related to EP1, across the mean
fields during the intensification phase.
Figure6.14ademonstratestheRKcriterion, showingthederivativeofabsolutevorticity
(η) at 250 hPa with respect to latitude. A strong meridional gradient of η is evident, with
a sign reversal near the cyclone center, satisfying the RK criterion and indicating that

221
Section6.2.PhysicalMechanisms
(A) (B)
Figure 6.13: Boxplots for each vertical level, for (A) C and (B) C terms, for energy pattern (EP) 1
A K
systems.
barotropic instability might indeed be occurring. Figure 6.14b shows the zonally averaged
meridional derivative of η, providing a clearer illustration of the RK criterion.
Meanwhile, Figure 6.14c shows the potential vorticity composites. Here, the 900 hPa
level was used instead of 1000 hPa due to artifacts related to the vertical coordinate
interpolation from height to isobaric levels when computing the EGR fields. This figure
reveals an area of intense cyclonic activity in the middle of the Semi-Lagrangian domain,
associatedwithlow-pressuresystemsandsignificantvorticity. Figure6.14dshowstheEGR
composites, demonstrating a strong baroclinic region east/southeast of the cyclone centers,
indicating regions susceptible to baroclinic instability, which is on agreement with mean
cyclone displacement on SESA region (Hoskins and Hodges, 2005; Gramcianinov et al.,
2019). These areas coincide with sharp PV gradients observed in Figure 6.14c, reinforcing
these areas as susceptible to cyclonic development.
These results reinforce the conclusions from Chapter 5 and Section 6.1 that both ba-
roclinic and barotropic instabilities act in consonance for cyclone genesis and develop-
ment in the SESA region. While barotropic instability acts in the upper troposphere,
extracting energy from the jets for cyclonic development, baroclinic instability in the lower
troposphere transforms the meridional temperature gradients into eddy potential energy,
ultimately feeding eddy kinetic energy.
Hoskinsetal.(1985)describedthegeneralsituationwhereanupper-levelPVannomaly

222
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
(A) (B)
(C) (D)
Figure6.14: CompositeAnalysisofBarotropicandBaroclinicInstabilities. (a)Thederivativeofabsolute
vorticity(η)at250hPawithrespecttolatitude,illustratingtheRayleigh-Kuo(RK)criterion. (b)Zonally
averaged meridional derivative of η. (c) Potential vorticity (PV) composites at 900 hPa. (d) Maximum
Eady Growth Rate (EGR) composites at 900 hPa.

223
Section6.2.PhysicalMechanisms
acting over a low-level baroclinic region triggers surface cyclogenesis. The results shown
here indicate that the baroclinic chain is initially stronger, with barotropic conversions
increasing afterward and peaking at the cyclone’s mature phase (Section 5.2.3). If these
baroclinic conversions occur at lower levels, while barotropic conversions occur at upper
levels, this suggests a distinct mechanism as proposed by Hoskins et al. (1985), although
this requires further exploration.
It is important to recognize, however, that the approach adopted has its limitations.
Firstly, the Rayleigh–Kuo criterion is derived from a linear stability analysis, which assu-
mes small perturbations to the basic flow and does not account for the nonlinear processes
that can become significant as instabilities grow and evolve. It is also based on idealized
conditions, such as an inviscid (non-viscous) and incompressible flow, whereas real at-
mospheric and oceanic flows are neither purely inviscid nor incompressible. Furthermore,
it is a necessary but insufficient criterion for instability (see Read et al. (2020)). However,
the overall K → K conversions, in consonance with satisfying the RK criterion, pro-
Z E
vide strong evidence for barotropic instability being related to cyclone development in the
SESA region.
6.2.2 Comparing with the Fixed Framework
The results shown so far indicate that barotropic instability plays an important role in
extratropical cyclone development. While some studies have detected this phenomenon,
it has not been fully explored in the literature. Why has this important aspect received
limited attention? As the use of the Semi-Lagrangian Framework is rarely seen in the
literature, the answer might lie in the intrinsic differences between the Semi-Lagrangian
and the more commonly used Fixed Framework.
Thissectionaimstoexplorethisdichotomy. Here,thesamesystemsanalyzedinSection
6.2.1 (the systems related to EP1) are analyzed, but now using the Fixed Framework. In
Figure 6.15 it is shown the LPS diagram 1 for EP1 systems mean values. In this case,
the LEC of EP1 systems were computed using the Fixed Framework and then, for each
development phase (incipient, intensification, mature and decay), the mean values were
computed, excluding outliers. The LPS indicates a mean behaviour where the cyclones
have genesis and intensify with shared contributions from moist baroclinic and barotropic
conversions, with the barotropic conversions becoming more important on the mature

224
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
and decay phases. These results indicate that the Fixed Framework also evidences the
importance of barotropic conversions on cyclonic systems in SESA region, but with lower
mean magnitude than the Semi-Lagrangian method. Also, caution should be taken into
examining the results from the Fixed Framework, as, for EP1 cases there were systems
with large horizontal displacement (Appendix I), therefore their computational domain
encompassed almost entirely the Southern Atlantic region and most certainly more than
one cyclonic system was acting on that domain during the analysis.
Figure 6.15: Lorenz Phase Space (LPS) diagram 1 for energy pattern (EP) 1 systems mean values for
each phase (incipient, intensification, mature and decay), computed using a fixed framework.
The following step was to defined to investigate the role of the LEC methodology in
affecting the magnitude of the barotropic and baroclinic conversions. Figure 6.16 displays
the same analysis as Figure 6.14, but for the composites using the Fixed Framework.
Although there are sign reversals in the meridional η derivative zonally averaged values,

225
Section6.2.PhysicalMechanisms
the spatial field displays a less cohesive spatial field compared to the Semi-Lagrangian
results. For the PV field, an increase in its magnitude can be seen poleward, which is
the expected behavior. Additionally, for EGR, a modest baroclinic region can be seen
from the central to eastern parts of the domain. This is again the expected behavior for
this region, with magnitudes comparable to the climatological values (de Souza and Piva,
2023). There is also a spot of high baroclinicity to the west, near the interpolated domain
area equivalent to the ARG cyclogenesis region. Although this high baroclinic region in
the west might be related to cyclogenesis in the Southwestern region, the composites do
not show a clear signature of cyclonic development as in Figure 6.14.
(B)
(A)
(C) (D)
Figure6.16: CompositeAnalysisofBarotropicandBaroclinicInstabilitiesusingtheFixedFramework. (a)
The derivative of absolute vorticity (η) at 250 hPa with respect to latitude, illustrating the Rayleigh-Kuo
(RK) criterion. (b) Zonally averaged meridional derivative of η. (c) Potential vorticity (PV) composites
at 900 hPa. (d) Maximum Eady Growth Rate (EGR) composites at 900 hPa.
To better illustrate the effect of the methodology on the results, let us examine a case

226
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
study comparing the results for both methodologies. Figure 6.17 shows the results for a
system with genesis on March 1, 1982, during the period when the barotropic conversions
were most intense. Figure 6.17a illustrates the computational domain used for running
the Fixed Framework, while its track is displayed in Figure 6.17b, along with the Semi-
Lagrangian domain defined for that given time step.
The EGR fields for the Fixed domain display a maximum in the southern parts of
South America, near 70◦W (Figure 6.17c), while the cyclonic center is at 36◦W (Figure
6.17d). Here, the EGR fields for 875 hPa are displayed due to the occurrence of artifacts
related to the vertical interpolation in the 900 hPa fields. Thus, despite the mean EGR
values for the Fixed domain being higher (0.55 day−1) than those for the Semi-Lagrangian
domain (0.45 day−1), these values are related to the maximum away from the cyclone
center, therefore reinforcing the reasoning that the use of the Fixed Framework captures
dynamics unrelated to cyclonic system development. For the meridional derivative of η,
regions inside the Fixed Framework satisfying the RK criterion can be seen, such as in
Southern Argentina (Figure 6.17e). However, inside the Semi-Lagrangian domain, near
the cyclone center, this effect is more pronounced (Figure 6.17f).
The results presented here suggest that the Semi-Lagrangian Framework better repre-
sents the process of barotropic instability compared to the Fixed Framework. When Fixed
domains are used for computing the LEC of cyclonic systems, they have to be large enough
to capture the system’s total displacement, which is on average approximately 5,000 km for
the South Atlantic but can reach up to 10,000 km (Figure 4.8). Therefore, such domains
would definitely capture the baroclinic regions in the mid-latitudes. However, barotropic
conversions occur more localized in specific areas and thus can be overshadowed when
analyzing larger domains using the Fixed Framework. The more localized aspect of the
barotropic instability process is highlighted in Grimm and Dias (1995), which explores the
role of the zonal variability of the upper tropospheric level jet in setting up barotropic
instabilities responsible for the generation of teleconnection patterns not forced by loca-
lized vorticity sources. For the Semi-Lagrangian Framework, however, the computational
domain is centered on the cyclonic system, where the barotropic conversions are well repre-
sented. Nevertheless, it was shown that the use of Fixed domains captures the energetics of
regions not associated with eddy development, which could potentially lead to misleading
results.

227
Section6.2.PhysicalMechanisms
(A) (B)
(C) (D)
(E)
(F)
Figure 6.17: Comparison of barotropic and baroclinic instability analysis between the Fixed and Semi-
LagrangianFrameworksforsystem19820099,duringthetimestepofmostintenseK →K conversions.
Z E
(a) Computational domain for the Fixed Framework, indicated by the larger rectangle. (b) Track of the
system with the Semi-Lagrangian domain, indicated by the smaller rectangle. (c) EGR fields for the
Fixed domain, with the averaged EGR value in the domain shown in parentheses (0.55 day−1). (d) EGR
fields for the Semi-Lagrangian domain, with the averaged EGR value in the domain shown in parentheses
(0.45 day−1). (e) Meridional derivative of η for the Fixed domain. (f) Meridional derivative of η for the
Semi-Lagrangian domain.

228
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
Furthermore, the use of the Fixed Framework for computing the LEC for EP1 systems
demonstrated that even with this Framework, the importance of barotropic conversions is
still evident. Thus, the apparent underestimation of the role of barotropic instability in
extratropical cyclone development is not a methodological issue. It can be argued that
either the role of barotropic conversions is more pronounced in this methodology only for
the most intense systems, whose energetics might not have been analyzed previously, or
that this issue might arise from the lack of studies investigating the energetics of such a
large number of systems.
6.3 Summary and Concluding Remarks
This chapter presented the Lorenz Phase Space (LPS) diagrams, a visualization tool
aimed at providing a diagnostic of the eddy-related energetics inspired by the Hart (2003)
CyclonePhaseSpace. Thistoolallowsforaquickassessmentofthedynamicalmechanisms
related to cyclone development, such as baroclinic and barotropic energy conversions, im-
ports of both eddy kinetic and available potential energy, as well as the generation of eddy
available potential energy due to diabatic processes (convective activity).
TheenergycycleofallsystemswithgenesisintheSouthwesternAtlanticandSoutheast
America (SESA) region was dissected for each life cycle phase and then clustered using
the K-means algorithm to determine their energy patterns (EP). Three EPs were found,
and the differences among them were defined by their energy states. EP1 represents the
most common cyclones in the SESA region, presenting low energy states and the lowest
maximum relative vorticity values. Meanwhile, EPs 2 and 3 display progressively increased
energy states and higher maximum vorticity values.
The identified EPs indicate the following behavior for the energy cycle of cyclones in
the SESA region:
• During cyclogenesis and incipient development, the systems present low baroclinic
and barotropic conversions, but with imports of eddy APE. The imports of eddy
kinetic energy are initially neutral, but more intense systems present progressively
higher levels of imports of such energy.
• In the intensification phase, the baroclinic conversions and imports of eddy kinetic

229
Section6.3.SummaryandConcludingRemarks
energy are often at their maximum, with their relative magnitude increasing from
EP1 to 3. During this phase, imports of eddy APE become neutral.
• Both baroclinic conversions and imports of eddy kinetic energy tend to diminish in
the mature phase. Meanwhile, barotropic conversions become more intense and the
systems begin to export eddy APE, with progressively higher values for both terms
from EPs 1 to 3.
• The baroclinic and barotropic conversion terms, as well as boundary fluxes of eddy
APE, tend to become more neutral during the decay phase, while the export of eddy
kinetic energy tends to intensify.
Significant variability in this mean behavior across different life cycle configurations or
genesis regions and seasons was not found, although the overall magnitude of the terms
tends to vary, with some exceptions noted.
The importance of barotropic conversions for cyclone development was not evidenced
by previous studies. To determine whether barotropic instability was occurring near the
cyclonesystems, itwasinvestigatediftheRayleigh-Kuocriterionwasbeingsatisfied, which
was confirmed by the analysis for EP1 systems. These results were replicated using the
FixedFramework,revealingthatevenwithadifferentmethodology,thesignalofbarotropic
conversions was still noted, although weakened.
Besides directly providing kinetic energy to the cyclone systems, barotropic instability
might also contribute to cyclonic development via the Ekman pumping mechanism. Once
the initial perturbation is established, Ekman pumping in the boundary layer can enhance
vertical movements (Hamouda and Kucharski, 2019, e.g.), leading to cloud formation and
latent heat release. Another mechanism that might be at play is Wave-CISK (Lindzen,
1974; Raymond, 1976). Convergence induced by Wave-CISK can contribute to reducing
low pressure, drawing in moist air, and enhancing upward motion. This process leads to
increased cloud formation and latent heat release, further fueling cyclonic development.
Nevertheless, the barotropic conversion term C is composed of five distinct terms:
K
meridional advection of zonal momentum, meridional shear of meridional wind, interaction
of eddy zonal wind with meridional wind, and vertical advection of zonal momentum.
Only the first three terms are strictly related to the classical view of barotropic instability
(Rayleigh, 1895; Kuo, 1949; Holton, 1973). Meanwhile, the last two terms involve vertical

230
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
transports of momentum, which are intimately related to the presence of vertical wind
shear and, therefore, due to the thermal-wind relationship, i.e., baroclinicity. A future
study will be conducted to assess which terms dominate in the barotropic conversions.
The author believes this can help to better understand the dynamical processes presented
here and will open avenues for further research.
In conclusion, the results shown here indicate barotropic instability as an important
dynamical mechanism for cyclone development in the SESA region. The lack of previous
indication of such behavior is due to either a lack of analysis of such a large dataset or due
to methodological limitations, or both.
It is proposed here to use the LPS diagrams as the visual representation of the dynamic
processes related to cyclone development, similarly to how Hart (2003) is a representation
of the cyclones’ thermal structure and symmetry. In Figure 6.18, LPS diagram 1 is repre-
sented along with the dynamical processes related to each of its quadrants. Cyclones in the
top-right quadrant are said to be related to baroclinic instability, while in the bottom-left,
barotropic instability, and in the top-left, both instabilities are occurring. Lastly, in the
bottom-right, the eddy is feeding the zonal circulation.
While this research contributed to understanding the mechanisms related to each qua-
drant in LPS diagram 1, this is not the case for LPS diagram 2 (Figure 6.19). While the
imports of eddy kinetic energy have been suggested to be related to downstream develop-
ment (Michaelides et al., 1999), this relationship was not further investigated. Also, for
imports of eddy APE, from the mathematical expression for such term, it is tentative to
relate it to thermal advection or heat fluxes, previously related as important mechanisms
for cyclone development on SESA region (Gozzo et al., 2014; Dutra et al., 2017; Gram-
cianinov et al., 2019). It is then suggested here for future research to investigate such
relationships.
Nevertheless, the LPS diagrams are not yet ready to be used as a diagnostic tool for
cyclone classification. For this, future research should be conducted on examining the
EPs for distinct cyclonic systems, such as tropical and subtropical cyclones. It is the
author’s best wish to continue with this research, providing an integrated Framework for
cycloneclassification, alongsidewithHart(2003)diagrams, whichwillaccountforcyclones’
Material, Formal, Efficient, and Final Causes.

231
Section6.3.SummaryandConcludingRemarks
Figure 6.18: Lorenz Phase Space (LPS) diagram 1 representation with each dynamical process related to
each quadrant represented.

232
Chapter6.EnergeticPatternsofCyclonesintheSouthwesternAtlantic
Figure 6.19: Lorenz Phase Space (LPS) diagram 2 representation with each dynamical process related to
each quadrant represented.

7
Chapter
Conclusions
The main goal of this thesis was to determine the primary dynamical mechanisms
related to cyclone development in the Southwestern Atlantic and Southeast American
regions during each of their development phases. For this, a database of cyclonic system
tracks with genesis in this region was utilized. This database was constructed by detecting
cyclones from their central relative vorticity at 850 hPa and includes all systems in the
South Atlantic region from 1979 to 2020. Subsequently, a program called CycloPhaser
was created to dissect the relative vorticity series into distinct life phases, based on its
maximum, minimum, and derivative values. The CycloPhaser was then used to construct
a climatology of cyclone life cycle phases from the original track database, which also
allowed for investigating the mean characteristics of cyclones across each phase.
The next step involved programming an application to compute the Lorenz Energy
Cycle and using it to analyze the energetics of all cyclones in the database. The mean
characteristics of the systems’ energy cycles were investigated and dissected for each life
cycle phase. Afterward, the K-means algorithm was employed to determine the energy
patterns. Finally, the dynamical mechanisms related to cyclonic system development, as
indicated by the energy cycle analysis, were further investigated.
7.1 Summary of Main Findings
This thesis provides significant insights into the detection, analysis, and energetics of
7,531 cyclonic systems in the Southwestern Atlantic region through the development and
application of new methodologies.
First, the CycloPhaser’s ability to detect and analyze cyclone life cycles was demons-

234
Chapter7.Conclusions
trated, highlighting key patterns in cyclone behavior. The analysis confirmed known cy-
clogenesis regions, cyclone paths, and statistical properties such as average lifetime and
displacement, providing new insights related to each development phase. It was revealed
that cyclonic systems exhibit multiple life phase configurations, with some configurations
including secondary life cycle development. The analysis of spatial distributions across
various phases of the cyclone life cycle reveals that systems often intensify and mature
near their genesis regions, decaying over a broader area.
Second, the thesis delved into the Lorenz Energy Cycle (LEC) to assess the energetics
of the selected cyclonic systems in the Southwestern Atlantic. Using a Semi-Lagrangian
approach, the study revealed high variability in LEC terms, highlighting the importance
of the baroclinic chain, convective activity, and barotropic conversions in cyclone deve-
lopment. The main mode of variability emphasized the significance of these processes
throughout the cyclone life cycle, from cyclogenesis to decay, with the moist baroclinic
chain peaking during the intensification phase and the barotropic conversions peaking du-
ring the mature phase. Nevertheless, these conversions continue even during the decay
phase, where exports and especially dissipation of eddy kinetic energy lead to the eventual
dissipation of the eddy. Furthermore, there is a relevant group of systems for which the
imports of eddy APE are important during the cyclones’ initial life stages.
Third, the Lorenz Phase Space (LPS) diagrams were introduced as a diagnostic tool for
eddy-related energetics. These diagrams provided a visual representation of the dynamic
mechanisms in cyclone development, including baroclinic and barotropic conversions and
imports of eddy kinetic and available potential energy. The analysis identified three energy
patterns (EPs) with distinct energy states and vorticity values, providing new perspectives
on cyclone energetics. Furthermore, the occurrence of barotropic and baroclinic instabili-
ties was further indicated through the application of the Rayleigh-Kuo criterion and the
analysis of the maximum Eady Growth Rate for composites and case studies.
7.2 Final Remarks and Recommendations for Future Work
The Lorenz Energy Cycle of cyclonic systems in the Southwestern Atlantic and Southe-
ast America region indicates that barotropic instability plays a pivotal role in extratropical
cyclone development, which is commonly associated with baroclinic instability. Although

235
Section7.2.FinalRemarksandRecommendationsforFutureWork
the occurrence of such instabilities was not directly assessed, the indications from the
energy cycle and the Rayleigh-Kuo criterion provide strong evidence for this argument. It
is also demonstrated that the use of the Fixed framework for computing the Lorenz Energy
Cycle underestimates the role of barotropic conversions while capturing baroclinic effects
unrelated to cyclone development, which might produce misleading results.
The findings presented here lead to the following research questions, left as suggestions
for future work:
• Why do cyclones have distinct life cycle configurations? For example, why do some
systems not present an incipient stage, and why do others present a secondary life
cycle? To answer these questions, the energy cycle (as done in the current study) as
well as vorticity and heat budgets (Dutra et al., 2017, e.g.) can be employed, and
the different life cycle configurations can be assessed.
• HowdoesclimatechangeaffectthespatialdistributionofcyclonephasesintheSouth
Atlantic region? Will cyclones mature closer to the coast? Will phase characteristics
(duration,displacement,etc.) change? Thiscouldbeevaluatedusingclimatemodels,
as has already been done in the literature (Reboita et al., 2018; de Jesus et al., 2022,
e.g.), but using the CycloPhaser program to diagnose differences in life cycle phases.
• Which terms of the barotropic conversion term C present the dominant magnitude
K
for the cyclones in the current dataset? Do their behaviors change across distinct life
cycles? This could be evaluated by modifying the Lorenz-cycle program to export
the results for each distinct term and comparing the results.
• What are the actual physical mechanisms related to the imports of eddy APE and
kineticenergy? Toinvestigatetheformer,vorticityandheatbudgetscanbeemployed
(Dutra et al., 2017, e.g.), while for the latter, an initial point could be investigating
whether it can be attributed to downstream development (Piva et al., 2010, e.g.).

236
Chapter7.Conclusions

Bibliography
AcevedoO.C.,PezziL.P.,SouzaR.B.,AnaborV.,DegraziaG.A.,Atmosphericboundary
layeradjustmenttothesynopticcycleattheBrazil-MalvinasConfluence, SouthAtlantic
Ocean, Journal of Geophysical Research: Atmospheres, 2010, vol. 115
Albuquerque M. d. G., Leal Alves D. C., Espinoza J. M. d. A., Oliveira U. R., Simo˜es R. S.,
Determining shoreline response to meteo-oceanographic events using remote sensing and
unmanned aerial vehicle (UAV): case study in southern Brazil, Journal of Coastal Re-
| search, 2018, | pp 766–770 |     |
| ------------- | ---------- | --- |
American Meteorological Society, 2012 Cyclone https://glossary.ametsoc.org/wiki/
Cyclone
´
Andrelina Silva B., Simo˜es Reboita M., Climatologia do Indice do Potencial de Gˆenese de
Ciclones Tropicais nos Oceanos Adjacentes a` Am´erica do Sul., Anu´ario do Instituto de
| Geociˆencias, | 2021, vol. | 44  |
| ------------- | ---------- | --- |
Aristotle A., Aristotle Metaphysics. vol. 1, Harvard University Press Cambridge, MA, 1933
Arthur D., Vassilvitskii S., K-Means++: The Advantages of Careful Seeding. In Soda ,
| vol. 8, 2007, | p. 1027 |     |
| ------------- | ------- | --- |
AzadR., SortebergA., ThevorticitybudgetsofNorthAtlanticwinterextratropicalcyclone
life cycles in MERRA reanalysis. Part I: Development phase, Journal of the Atmospheric
| Sciences, | 2014a, vol. | 71, p. 3109 |
| --------- | ----------- | ----------- |
AzadR., SortebergA., ThevorticitybudgetsofNorthAtlanticwinterextratropicalcyclone
life cycles in MERRA reanalysis. Part II: Decaying phase, Journal of the Atmospheric
| Sciences, | 2014b, vol. | 71, p. 3129 |
| --------- | ----------- | ----------- |

| 238 |     |     |     |     | Bibliography |
| --- | --- | --- | --- | --- | ------------ |
Balmaceda Huarte R., Olmo M. E., Bettolli M. L., Poggi M. M., Evaluation of multiple re-
analyses in reproducing the spatio-temporal variability of temperature and precipitation
indices over southern South America, International Journal of Climatology, 2021
Bembenek E., Merlis T. M., Straub D. N., Influence of latitude and moisture effects on the
barotropic instability of an idealized ITCZ, Journal of the Atmospheric Sciences, 2021,
| vol. 78, | p. 2677 |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
Bengtsson L., Hodges K. I., Keenlyside N., Will extratropical storms intensify in a warmer
| climate?, | Journal | of Climate, | 2009, | vol. | 22, p. 2276 |
| --------- | ------- | ----------- | ----- | ---- | ----------- |
Bjerknes J., On the structure of moving cyclones, Monthly Weather Review, 1919, vol. 47,
p. 95
Bjerknes J., Holmboe J., On the theory of cyclones, Journal of Atmospheric Sciences, 1944,
| vol. 1, p. | 1   |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- |
Bjerknes J., Solberg H., Life cycle of cyclones and the polar front theory of atmospheric
| circulation. | Grondahl, |     | 1922 |     |     |
| ------------ | --------- | --- | ---- | --- | --- |
Black M. T., Pezza A. B., A universal, broad-environment energy conversion signature of
explosive cyclones, Geophysical Research Letters, 2013, vol. 40, p. 452
Bluestein H. B., Synoptic-dynamic Meteorology in Midlatitudes: Observations and theory
| of weather | systems. | vol. | 2, Taylor | &   | Francis, 1992 |
| ---------- | -------- | ---- | --------- | --- | ------------- |
Booth J. F., Naud C. M., Jeyaratnam J., Extratropical cyclone precipitation life cycles: A
satellite-based analysis, Geophysical Research Letters, 2018, vol. 45, p. 8647
Brennan F. E., Vincent D. G., Zonal and eddy components of the synoptic-scale energy
budget during intensification of hurricane Carmen (1974), Monthly Weather Review,
| 1980, vol. | 108, | p. 954 |     |     |     |
| ---------- | ---- | ------ | --- | --- | --- |
Brown Jr J. A., A diagnostic study of tropospheric diabatic heating and the generation of
| available | potential | energy, | Tellus, | 1964, | vol. 16, p. 371 |
| --------- | --------- | ------- | ------- | ----- | --------------- |
Bulic I., Limited area energy budget during a life cycle of Genoa cyclone (18-21 Novem-
ber 1999), NUOVO CIMENTO-SOCIETA ITALIANA DI FISICA SEZIONE C, 2006,
| vol. 29, | p. 167 |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |

Bibliography 239
Burpee R. W., The origin and structure of easterly waves in the lower troposphere of North
Africa, Journal of the Atmospheric Sciences, 1972, vol. 29, p. 77
Campos R. M., Camargo R. D., Harari J., Characterization of extreme sea level events in
Santos and their correspondence with the NCEP model reanalysis in the southwest of
the South Atlantic, Revista Brasileira de Meteorologia, 2010, vol. 25, p. 175
Campos R. M., Gramcianinov C. B., de Camargo R., da Silva Dias P. L., Assessment and
calibration of ERA5 severe winds in the Atlantic Ocean using satellite data, Remote
| Sensing, 2022, | vol. 14, | p. 4918 |     |     |
| -------------- | -------- | ------- | --- | --- |
CaoX., HuangP., ChenG., ChenW., ModulationofwesternNorthPacifictropicalcyclone
genesis by intraseasonal oscillation of the ITCZ: A statistical analysis, Advances in
| Atmospheric | Sciences, | 2012, vol. 29, | p. 744 |     |
| ----------- | --------- | -------------- | ------ | --- |
CardosoA.A., daRochaR.P.,CrespoN.M., SynopticClimatologyofSubtropicalCyclone
ImpactsonNear-SurfaceWindsOvertheSouthAtlanticBasin,EarthandSpaceScience,
| 2022, vol. | 9, p. e2022EA002482 |     |     |     |
| ---------- | ------------------- | --- | --- | --- |
Cavicchia L., Dowdy A., Walsh K., Energetics and dynamics of subtropical australian east
coast cyclones: Two contrasting cases, Monthly Weather Review, 2018, vol. 146, p. 1511
Chan J. C. L., Kepert J. D., eds, Global Perspectives on Tropical Cyclones: From Science
to Mitigation. vol. 4 of World Scientific Series on Asia-Pacific Weather and Climate,
| World Scientific | Singapore, | 2010 |     |     |
| ---------------- | ---------- | ---- | --- | --- |
Chang E. K., Lee S., Swanson K. L., Storm track dynamics, Journal of climate, 2002,
| vol. 15, p. | 2163 |     |     |     |
| ----------- | ---- | --- | --- | --- |
Charney J. G., The dynamics of long waves in a baroclinic westerly current, Journal of the
| Atmospheric | Sciences, | 1947, vol. 4, | p. 136 |     |
| ----------- | --------- | ------------- | ------ | --- |
Charney J. G., Eliassen A., On the growth of the hurricane depression, Journal of the
| Atmospheric | Sciences, | 1964, vol. 21, | p. 68 |     |
| ----------- | --------- | -------------- | ----- | --- |
Craig G. C., Gray S. L., CISK or WISHE as the mechanism for tropical cyclone intensifi-
| cation, Journal | of Atmospheric | Sciences, | 1996, vol. 53, | p. 3528 |
| --------------- | -------------- | --------- | -------------- | ------- |

| 240 |     |     |     | Bibliography |     |
| --- | --- | --- | --- | ------------ | --- |
Crespo N. M., da RochaR. P., Sprenger M., WernliH., A potential vorticity perspective on
cyclogenesis over centre-eastern South America, International Journal of Climatology,
| 2021, vol. | 41, p. | 663 |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
Crespo N. M., Reboita M. S., Gozzo L. F., de Jesus E. M., Torres-Alavez J. A., Lagos-
Zu´n˜iga M. A., ´ Torrez-Rodriguez L., Reale M., da Rocha R. P., Assessment of the
RegCM4-CORDEX-CORE performance in simulating cyclones affecting the western co-
| ast of South | America, | Climate | Dynamics, | 2023, | vol. 60, p. 2041 |
| ------------ | -------- | ------- | --------- | ----- | ---------------- |
Da C., Shen B., Yan P., Ma D., Song J., The shallow water equation and the vorticity
equation for a change in height of the topography, Plos one, 2017, vol. 12, p. e0178184
da Rocha R. P., Reboita M. S., Gozzo L. F., Dutra L. M. M., de Jesus E. M., Subtropical
cyclonesovertheoceanicbasins: areview, AnnalsoftheNewYorkAcademyofSciences,
| 2019, vol. | 1436, | p. 138 |     |     |     |
| ---------- | ----- | ------ | --- | --- | --- |
da Silva Dias P. L., da Silva Dias M. A. F., Seluchi M., de Assis Diniz F., O ciclone
Catarina: Ana´lise preliminar da estrutura, dinˆamica e previsibilidade. In CONGRESSO
| BRASILEIRO |     | DE METEOROLOGIA |     | , 2004 |     |
| ---------- | --- | --------------- | --- | ------ | --- |
Dacre H. F., Gray S. L., The spatial distribution and evolution characteristics of North
Atlantic cyclones, Monthly Weather Review, 2009, vol. 137, p. 99
Daniel J., Data science with Python and Dask. Simon and Schuster, 2019
de Jesus E. M., da Rocha R. P., Crespo N. M., Reboita M. S., Gozzo L. F., Future climate
trends of subtropical cyclones in the South Atlantic basin in an ensemble of global and
| regional | projections, | Climate | Dynamics, | 2022, | vol. 58, p. 1221 |
| -------- | ------------ | ------- | --------- | ----- | ---------------- |
de Souza D., da Silva R. R., Ocean-Land Atmosphere Model (OLAM) performance for
major extreme meteorological events near the coastal region of southern Brazil, Climate
| Research, | 2021, | vol. 84, p. 1 |     |     |     |
| --------- | ----- | ------------- | --- | --- | --- |
deSouzaD.C., CrespoN.M., daSilvaD.V., HaradaL.M., deGodoyR.M.P., Domingues
L. M., Luiz R., Bortolozo C. A., Metodiev D., de Andrade M. R. M., et al., Extreme
rainfall and landslides as a response to human-induced climate change: a case study at
| Baixada | Santista, | Brazil, 2020, | Natural | Hazards, | 2024, pp 1–26 |
| ------- | --------- | ------------- | ------- | -------- | ------------- |

Bibliography 241
de Souza D. C., da Silva Dias P. L., Gramcianinov C. B., da Silva M. B. L., de Camargo
R., New perspectives on South Atlantic storm track through an automatic method for
detecting extratropical cyclones’ lifecycle, International Journal of Climatology, 2024,
| vol. 1, | p. 1 |     |     |     |
| ------- | ---- | --- | --- | --- |
de Souza D. C., Ramos da Silva R., Gomes da Silva P., Fetter Filho A. F. H., Mendez
F. J., Werth D., A hybrid regional climate downscaling for the southern Brazil coastal
region, International Journal of Climatology, 2022, vol. 42, p. 6753
de Souza M. R., Piva E. D., Storm tracks and cyclogenesis over the Southern Ocean: An
overview with the HadGEM3-GC3. 1 model, International Journal of Climatology, 2023,
| vol. 43, | p. 7565 |     |     |     |
| -------- | ------- | --- | --- | --- |
Deveson A., Browning K., Hewson T., A classification of FASTEX cyclones using a height-
attributablequasi-geostrophicvertical-motiondiagnostic,QuarterlyJournaloftheRoyal
Meteorological Society: A journal of the atmospheric sciences, applied meteorology and
| physical | oceanography, |     | 2002, vol. | 128, p. 93 |
| -------- | ------------- | --- | ---------- | ---------- |
Dias Pinto J. R., Reboita M. S., da Rocha R. P., Synoptic and dynamical analysis of
subtropical cyclone Anita (2010) and its potential for tropical transition over the South
Atlantic Ocean, Journal of Geophysical Research: Atmospheres, 2013, vol. 118, p. 10
Dias Pinto J. R., Rocha R. P., The energy cycle and structural evolution of cyclones over
southeastern South America in three case studies, Journal of Geophysical Research:
| Atmospheres, |     | 2011, | vol. 116 |     |
| ------------ | --- | ----- | -------- | --- |
Donald Ahrens C., Henson R., Meteorology Today: An introduction to weather, climate
| and the | environment. |     | Brooks/Cole, | 2015 |
| ------- | ------------ | --- | ------------ | ---- |
Drumond A., Nieto R., Gimeno L., Ambrizzi T., A Lagrangian identification of major
sources of moisture over Central Brazil and La Plata Basin, Journal of Geophysical
| Research: | Atmospheres, |     | 2008, | vol. 113 |
| --------- | ------------ | --- | ----- | -------- |
DuchonC.E., Lanczosfilteringinoneandtwodimensions, JournalofAppliedMeteorology
| and Climatology, |     | 1979, | vol. 18, | p. 1016 |
| ---------------- | --- | ----- | -------- | ------- |

| 242 |     |     |     | Bibliography |     |
| --- | --- | --- | --- | ------------ | --- |
Dutra L. M. M., da Rocha R. P., Lee R. W., Peres J. R. R., de Camargo R., Structure
and evolution of subtropical cyclone Anita as evaluated by heat and vorticity budgets,
Quarterly Journal of the Royal Meteorological Society, 2017, vol. 143, p. 1539
Dutton J. A., Johnson D. R., The theory of available potential energy and a variational
approach to atmospheric energetics, Advances in geophysics, 1967, vol. 12, p. 333
Eady E. T., Long waves and cyclone waves, Tellus, 1949, vol. 1, p. 33
Edmon H. J., Vincent D. G., Large-scale atmospheric conditions during the intensification
of Hurricane Carmen (1974) II. Diabatic heating rates and energy budgets, Monthly
| Weather | Review, | 1979, | vol. 107, | p. 295 |     |
| ------- | ------- | ----- | --------- | ------ | --- |
Emanuel K. A., An air-sea interaction theory for tropical cyclones. Part I: Steady-state
maintenance, Journal of Atmospheric Sciences, 1986, vol. 43, p. 585
Emanuel K. A., The dependence of hurricane intensity on climate, Nature, 1987, vol. 326,
p. 483
Emanuel K. A., Rotunno R., Polar lows as arctic hurricanes, Tellus A: Dynamic Meteoro-
| logy and | Oceanography, |     | 1989, vol. | 41, p. 1 |     |
| -------- | ------------- | --- | ---------- | -------- | --- |
Evans J. L., Braun A., A climatology of subtropical cyclones in the South Atlantic, Journal
| of Climate, | 2012, | vol. | 25, p. 7328 |     |     |
| ----------- | ----- | ---- | ----------- | --- | --- |
Evans J. L., Hart R. E., Objective indicators of the life cycle evolution of extratropical
transition for Atlantic tropical cyclones, Monthly Weather Review, 2003, vol. 131, p.
909
Everson D., Gan M. A., de Lima MOSCATI M. C., The role of latent and sensible heat
fluxes in an explosive cyclogenesis over the South American East Coast, Journal of the
| Meteorological |     | Society | of Japan, | 2011, vol. 89, | p. 637 |
| -------------- | --- | ------- | --------- | -------------- | ------ |
Ferreira R. N., Schubert W. H., Barotropic aspects of ITCZ breakdown, Journal of the
| Atmospheric | Sciences, |     | 1997, vol. | 54, p. 261 |     |
| ----------- | --------- | --- | ---------- | ---------- | --- |
Flaounas E., Kotroni V., Lagouvardos K., Flaounas I., CycloTRACK (v1. 0)–tracking
winter extratropical cyclones based on relative vorticity: sensitivity to data filtering and
other relevant parameters, Geoscientific Model Development, 2014, vol. 7, p. 1841

Bibliography 243
Ford R., Ford R. P., Moore G. W. K., Moore G. W. K., Moore G. W. K., Secondary
Cyclogenesis—Comparison of Observations and Theory, Monthly Weather Review, 1990
Frank N. L., Atlantic tropical systems of 1969, Monthly Weather Review, 1970, vol. 98, p.
307
Frank W. M., The structure and energetics of the tropical cyclone I. Storm structure,
| Monthly | Weather | Review, | 1977a, | vol. | 105, | p. 1119 |     |
| ------- | ------- | ------- | ------ | ---- | ---- | ------- | --- |
Frank W. M., The structure and energetics of the tropical cyclone II. Dynamics and ener-
| getics, | Monthly | Weather | Review, | 1977b, |     | vol. 105, | p. 1136 |
| ------- | ------- | ------- | ------- | ------ | --- | --------- | ------- |
Fukuoka A., A Study of 10-day Forecast (A Synthetic Report), The Geophysical Magazine,
| 1951, vol. | XXII, | p. 177 |     |     |     |     |     |
| ---------- | ----- | ------ | --- | --- | --- | --- | --- |
Gall R., The effects of released latent heat in growing baroclinic waves, Journal of the
| Atmospheric |     | Sciences, | 1976, vol. | 33, | p. 1686 |     |     |
| ----------- | --- | --------- | ---------- | --- | ------- | --- | --- |
Gan M. A., Ciclogˆeneses e ciclones sobre a Am´erica do Sul, Instituto Nacional de Pesquisas
| Espaciais | (INPE), | 1992, | Tese |     |     |     |     |
| --------- | ------- | ----- | ---- | --- | --- | --- | --- |
Gan M. A., Rao V. B., Surface cyclogenesis over south America, Monthly Weather Review,
| 1991, vol. | 119, | p. 1293 |     |     |     |     |     |
| ---------- | ---- | ------- | --- | --- | --- | --- | --- |
Gan M. A., Rao V. B., The influence of the Andes Cordillera on transient disturbances,
| Monthly  | Weather       | Review, | 1994,   | vol. | 122,  | p. 1141  |        |
| -------- | ------------- | ------- | ------- | ---- | ----- | -------- | ------ |
| Gibbs J. | W., Fourier’s | series, | Nature, |      | 1898, | vol. 59, | p. 200 |
Gordon A.L., Brazil-malvinas confluence–1984, Deep SeaResearch Part A. Oceanographic
| Research | Papers, | 1989, | vol. 36, | p. 359 |     |     |     |
| -------- | ------- | ----- | -------- | ------ | --- | --- | --- |
Gozzo L., Da Rocha R., Gimeno L., Drumond A., Climatology and numerical case study of
moisture sources associated with subtropical cyclogenesis over the southwestern Atlantic
Ocean, Journal of Geophysical Research: Atmospheres, 2017, vol. 122, p. 5636
Gozzo L. F., da Rocha R. P., Reboita M. S., Sugahara S., Subtropical cyclones over the
southwestern South Atlantic: Climatological aspects and case study, Journal of Climate,
| 2014, vol. | 27, | p. 8543 |     |     |     |     |     |
| ---------- | --- | ------- | --- | --- | --- | --- | --- |

| 244 |     |     | Bibliography |     |
| --- | --- | --- | ------------ | --- |
Gramcianinov C., Campos R., De Camargo R., Hodges K., Soares C. G., da Silva Dias P.,
Analysis of Atlantic extratropical storm tracks characteristics in 41 years of ERA5 and
CFSR/CFSv2 databases, Ocean Engineering, 2020, vol. 216, p. 108
Gramcianinov C., Campos R., Soares C. G., de Camargo R., Extreme waves generated by
cyclonic winds in the western portion of the South Atlantic Ocean, Ocean Engineering,
| 2020, vol. 213, | p. 107745 |     |     |     |
| --------------- | --------- | --- | --- | --- |
Gramcianinov C., Hodges K., Camargo R. d., The properties and genesis environments of
South Atlantic cyclones, Climate Dynamics, 2019, vol. 53, p. 4115
Gramcianinov C. B., Campos R. M., de Camargo R., Hodges K. I., Guedes Soares C.,
da Silva Dias P. L., Atlantic extratropical cyclone tracks in 41 years of ERA5 and
| CFSR/CFSv2 | databases, | Mendeley | Data, 2020, | vol. V4 |
| ---------- | ---------- | -------- | ----------- | ------- |
Gramcianinov C. B., de Camargo R., Campos R. M., Guedes Soares C., da Silva Dias
P. L., Impact of extratropical cyclone intensity and speed on the extreme wave trends
| in the Atlantic | Ocean, | Climate dynamics, | 2023, | vol. 60, p. 1447 |
| --------------- | ------ | ----------------- | ----- | ---------------- |
Gray S. L., Dacre H. F., Classifying dynamical forcing mechanisms using a climatology
of extratropical cyclones, Quarterly Journal of the Royal Meteorological Society: A
journal of the atmospheric sciences, applied meteorology and physical oceanography,
| 2006, vol. 132, | p. 1119 |     |     |     |
| --------------- | ------- | --- | --- | --- |
Gray W. M., Global view of the origin of tropical disturbances and storms, Monthly
| Weather Review, | 1968, | vol. 96, p. | 669 |     |
| --------------- | ----- | ----------- | --- | --- |
Gray W. M., The formation of tropical cyclones, Meteorology and atmospheric physics,
| 1998, vol. 67, | p. 37 |     |     |     |
| -------------- | ----- | --- | --- | --- |
Grimm A. M., Dias P. L. S., Analysis of tropical-extratropical interactions with influence
functions of a barotropic model., Journal of the Atmospheric Sciences, 1995, vol. 52
Grise K. M., Son S.-W., Gyakum J. R., Intraseasonal and interannual variability in North
American storm tracks and its relationship to equatorial Pacific variability, Monthly
| Weather Review, | 2013, | vol. 141, | p. 3610 |     |
| --------------- | ----- | --------- | ------- | --- |

Bibliography 245
Guimara˜es P., Farina L., Toldo Jr E., Analysis of extreme wave events on the southern
coast of Brazil, Natural Hazards and Earth System Sciences, 2014, vol. 14, p. 3195
Gutowski W. J., Branscome L. E., Stewart D. A., Life cycles of moist baroclinic eddies,
| Journal | of the | atmospheric |     | sciences, | 1992, | vol. | 49, | p. 306 |
| ------- | ------ | ----------- | --- | --------- | ----- | ---- | --- | ------ |
HadleyG., VI.Concerningthecauseofthegeneraltrade-winds, PhilosophicalTransactions
| of the  | Royal Society |         | of London, | 1735,    | vol. | 39,   | p. 58 |     |
| ------- | ------------- | ------- | ---------- | -------- | ---- | ----- | ----- | --- |
| Hamming | R. W.,        | Digital | Filters.   | Prentice |      | Hall, | 1989  |     |
Hamouda M. E., Kucharski F., Ekman pumping mechanism driving precipitation anoma-
lies in response to equatorial heating, Climate Dynamics, 2019, vol. 52, p. 697
Hannachi A., Jolliffe I. T., Stephenson D. B., et al., Empirical orthogonal functions and
relatedtechniquesinatmosphericscience: Areview, Internationaljournalofclimatology,
| 2007, | vol. 27, | p. 1119 |     |     |     |     |     |     |
| ----- | -------- | ------- | --- | --- | --- | --- | --- | --- |
Harris F. J., On the use of windows for harmonic analysis with the discrete Fourier trans-
| form, | Proceedings | of  | the | IEEE, 1978, | vol. | 66, | p. 51 |     |
| ----- | ----------- | --- | --- | ----------- | ---- | --- | ----- | --- |
Harrold T., Browning K., The polar low as a baroclinic disturbance, Quarterly Journal of
| the Royal | Meteorological |     |     | Society, 1969, |     | vol. 95, | p.  | 710 |
| --------- | -------------- | --- | --- | -------------- | --- | -------- | --- | --- |
Hart R. E., A cyclone phase space derived from thermal wind and thermal asymmetry,
| Monthly | weather | review, |     | 2003, vol. | 131, | p. 585 |     |     |
| ------- | ------- | ------- | --- | ---------- | ---- | ------ | --- | --- |
Held I. M., The macroturbulence of the troposphere, Tellus A, 1999, vol. 51, p. 59
Hersbach H., Bell B., Berrisford P., Hirahara S., Hor´anyi A., Mun˜oz-Sabater J., Nicolas J.,
Peubey C., Radu R., Schepers D., et al., The ERA5 global reanalysis, Quarterly Journal
| of the | Royal Meteorological |     |     | Society, | 2020, | vol. | 146, | p. 1999 |
| ------ | -------------------- | --- | --- | -------- | ----- | ---- | ---- | ------- |
Hodges K., Feature tracking on the unit sphere, Monthly Weather Review, 1995, vol. 123,
p. 3458
Hodges K., Spherical nonparametric estimators applied to the UGAMP model integration
| for AMIP, | Monthly |     | Weather | Review, | 1996, | vol. | 124, | p. 2914 |
| --------- | ------- | --- | ------- | ------- | ----- | ---- | ---- | ------- |

| 246 |     |     | Bibliography |     |     |
| --- | --- | --- | ------------ | --- | --- |
Hodges K. I., A general method for tracking analysis and its application to meteorological
| data, Monthly | Weather | Review, | 1994, vol. | 122, | p. 2573 |
| ------------- | ------- | ------- | ---------- | ---- | ------- |
HolopainenE.O.,Investigationoffrictionanddiabaticprocessesintheatmosphere.vol.29,
na, 1964
Holton J. R., An introduction to dynamic meteorology. vol. 41, American Association of
| Physics | Teachers, | 1973, 752 |     |     |     |
| ------- | --------- | --------- | --- | --- | --- |
Hoskins B. J., Theory of extratropical cyclones. Springer, 1990, 63
Hoskins B. J., Hodges K. I., New perspectives on the Northern Hemisphere winter storm
tracks, Journal of the Atmospheric Sciences, 2002, vol. 59, p. 1041
Hoskins B. J., Hodges K. I., A new perspective on Southern Hemisphere storm tracks,
| Journal | of Climate, | 2005, vol. | 18, p. 4108 |     |     |
| ------- | ----------- | ---------- | ----------- | --- | --- |
Hoskins B. J., McIntyre M. E., Robertson A. W., On the use and significance of isentropic
potential vorticity maps, Quarterly Journal of the Royal Meteorological Society, 1985,
| vol. 111, | p. 877 |     |     |     |     |
| --------- | ------ | --- | --- | --- | --- |
Hoskins B. J., Valdes P. J., On the existence of storm-tracks, Journal of Atmospheric
| Sciences, | 1990, vol. | 47, p. 1854 |     |     |     |
| --------- | ---------- | ----------- | --- | --- | --- |
Jensen C. E., Energy transformation and vertical flux processes over the northern he-
misphere, Journal of Geophysical Research, 1961, vol. 66, p. 1145
Johnson D. R., The available potential energy of storms, Journal of Atmospheric Sciences,
| 1970, vol. | 27, p. 727 |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
Jorgensen D. P., Zipser E. J., LeMone M. A., Vertical motions in intense hurricanes,
| Journal | of the atmospheric | sciences, | 1985, | vol. | 42, p. 839 |
| ------- | ------------------ | --------- | ----- | ---- | ---------- |
Knutson T. R., McBride J. L., Chan J., Emanuel K., Holland G., Landsea C., Held I.,
Kossin J. P., Srivastava A., Sugi M., Tropical cyclones and climate change, Nature
| geoscience, | 2010, vol. | 3, p. 157 |     |     |     |
| ----------- | ---------- | --------- | --- | --- | --- |
Kuo H.-l., Dynamic instability of two-dimensional nondivergent flow in a barotropic at-
| mosphere, | Journal | of Atmospheric | sciences, | 1949, | vol. 6, p. 105 |
| --------- | ------- | -------------- | --------- | ----- | -------------- |

247
Bibliography
Lavers D. A., Simmons A., Vamborg F., Rodwell M. J., An evaluation of ERA5 precipi-
tation for climate monitoring, Quarterly Journal of the Royal Meteorological Society,
2022, vol. 148, p. 3152
Leal K. B., Robaina L. E. d. S., K¨orting T. S., Nicolodi J. L., da Costa J. D., Souza V. G.,
Identification of coastal natural disasters using official databases to provide support for
the coastal management: the case of Santa Catarina, Brazil, Natural Hazards, 2023, pp
1–18
Li L., Ingersoll A. P., Jiang X., Feldman D., Yung Y. L., Lorenz energy cycle of the global
atmosphere based on reanalysis datasets, Geophysical Research Letters, 2007, vol. 34
Lindzen R. S., Wave-CISK in the tropics, Journal of Atmospheric Sciences, 1974, vol. 31,
p. 156
Lorenz E., The nature and theory of the general circulation of the atmosphere, World
meteorological organization, 1967, vol. 161
Lorenz E. N., Available Potential Energy and the Maintenance of the General Circulation,
Tellus, 1955, vol. 7, p. 157
Lorenz E. N., Empirical orthogonal functions and statistical weather prediction. vol. 1,
Massachusetts Institute of Technology, Department of Meteorology Cambridge, 1956
McLennan N., , 1988 Technical report Marine Bombs Program: Phase II. Pacific Weather
Centre
MacQueen J., et al., Some methods for classification and analysis of multivariate obser-
vations. In Proceedings of the fifth Berkeley symposium on mathematical statistics and
probability , 1967, p. 281
McTaggart-Cowan R., Bosart L. F., Davis C. A., Atallah E. H., Gyakum J. R., Emanuel
K. A., Analysis of hurricane Catarina (2004), Monthly Weather Review, 2006, vol. 134,
p. 3029
Mailier P., Mailier P. J., Stephenson D. B., Stephenson D. B., Ferro C. A. T., Ferro C.
A. T., Hodges K. I., Hodges K. I., Serial Clustering of Extratropical Cyclones, Monthly
Weather Review, 2006

| 248 |     |     | Bibliography |     |
| --- | --- | --- | ------------ | --- |
Maloney E. D., Hartmann D. L., The Madden–Julian oscillation, barotropic dynamics,
and North Pacific tropical cyclone formation. Part I: Observations, Journal of the at-
| mospheric | sciences, | 2001, vol. 58, | p. 2545 |     |
| --------- | --------- | -------------- | ------- | --- |
Marengo J. A., Soares W. R., Saulo C., Nicolini M., Climatology of the low-level jet east of
the Andes as derived from the NCEP–NCAR reanalyses: Characteristics and temporal
| variability, | Journal | of climate, 2004, | vol. 17, | p. 2261 |
| ------------ | ------- | ----------------- | -------- | ------- |
Margules M., Uber die Energie der Sturnie, Jahrb. kair-kon Zent, 1903
Marquet P., On the concept of exergy and available enthalpy: Application to atmospheric
energetics, Quarterly Journal of the Royal Meteorological Society, 1991, vol. 117, p. 449
Marquet P., The last paper”On the theory of storm”(Zur Sturmtheorie) published by Max
| Margules | in 1906, | arXiv preprint | arXiv:1704.06128, | 2017 |
| -------- | -------- | -------------- | ----------------- | ---- |
Marrafon V. H., Reboita M. S., da Rocha R. P., de Jesus E. M., Classifica¸ca˜o dos tipos de
ciclones sobre o Oceano Atlaˆntico Sul em proje¸co˜es com o RegCM4 E MCGs, Revista
| Brasileira | de Climatologia, | 2022, | vol. 30, p. | 1   |
| ---------- | ---------------- | ----- | ----------- | --- |
May R. M., Goebbert K. H., Thielen J. E., Leeman J. R., Camron M. D., Bruick Z., Bru-
ning E. C., Manser R. P., Arms S. C., Marsh P. T., MetPy: A meteorological Python
library for data analysis and visualization, Bulletin of the American Meteorological So-
| ciety, 2022, | vol. 103, | p. E2273 |     |     |
| ------------ | --------- | -------- | --- | --- |
Mendes D., Souza E. P., Marengo J. A., Mendes M. C., Climatology of extratropical
cyclones over the South American–southern oceans sector, Theoretical and applied cli-
| matology, | 2010, vol. | 100, p. 239 |     |     |
| --------- | ---------- | ----------- | --- | --- |
MichaelidesS.C.,LimitedareaenergeticsofGenoacyclogenesis,MonthlyWeatherReview,
| 1987, | vol. 115, p. | 13  |     |     |
| ----- | ------------ | --- | --- | --- |
Michaelides S. C., A spatial and temporal energetics analysis of a baroclinic disturbance
in the Mediterranen, Monthly weather review, 1992, vol. 120, p. 1224
Michaelides S. C., Prezerakos N. G., Flocas H. A., Quasi-Lagrangian energetics of an
intense Mediterranean cyclone, Quarterly Journal of the Royal Meteorological Society,
| 1999, | vol. 125, p. | 139 |     |     |
| ----- | ------------ | --- | --- | --- |

Bibliography 249
Mitra S. K., Digital Signal Processing: A Computer-Based Approach. McGraw-Hill, 2001
Molinari J., Knight D., Dickinson M., Vollaro D., Skubis S., Potential vorticity, easterly
waves, and eastern Pacific tropical cyclogenesis, Monthly weather review, 1997, vol. 125,
p. 2699
Molinari J., Vollaro D., Skubis S., Dickinson M., Origins and mechanisms of eastern Pacific
tropical cyclogenesis: A case study, Monthly Weather Review, 2000, vol. 128, p. 125
Montgomery M. T., Persing J., Smith R. K., Putting to rest WISHE-ful misconceptions for
tropical cyclone intensification, Journal of Advances in Modeling Earth Systems, 2015,
| vol. 7, p. | 92  |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- |
Montgomery M. T., Smith R. K., Paradigms for tropical cyclone intensification, Australian
| Meteorological | and | Oceanographic |     | Journal, | 2014, vol. 64, | p. 37 |
| -------------- | --- | ------------- | --- | -------- | -------------- | ----- |
Muench H. S., On the dynamics of the wintertime stratosphere circulation, Journal of
| Atmospheric | Sciences, |     | 1965, vol. | 22, p. 349 |     |     |
| ----------- | --------- | --- | ---------- | ---------- | --- | --- |
Murray R. J., Simmonds I., A numerical scheme for tracking cyclone centres from digital
data. Part II: Application to January and July general circulation model simulations,
| Australian | Meteorological |     | Magazine, | 1991, | vol. 39, p. 167 |     |
| ---------- | -------------- | --- | --------- | ----- | --------------- | --- |
Necco G., Comportamiento de vortices ciclonicos en el area Sudamericana durante el
| FGGE: | Ciclogenesis, | Meteorologica, |     | 1982a, | vol. 13, p. 7 |     |
| ----- | ------------- | -------------- | --- | ------ | ------------- | --- |
Necco G., Comportamiento de v´ortices cicl´onicos en el a´rea sudamericana durante el
FGGE: trayectorias y desarrollos, Meteorologica, 1982b, vol. 13, p. 21
Nordeng T. E., Rasmussen E. A., A most beautiful polar low. A case study of a polar low
development in the Bear Island region, Tellus A, 1992, vol. 44, p. 81
Norquist D. C., Recker E. E., Reed R. J., The energetics of African wave disturbances as
observed during phase III of GATE, Monthly Weather Review, 1977, vol. 105, p. 334
Novak L., Tailleux R., On the local view of atmospheric available potential energy, Journal
| of the Atmospheric |     | Sciences, | 2018, | vol. 75, | p. 1891 |     |
| ------------------ | --- | --------- | ----- | -------- | ------- | --- |

| 250 |     |     |     | Bibliography |     |
| --- | --- | --- | --- | ------------ | --- |
Okajima S., Nakamura H., Kaspi Y., Cyclonic and anticyclonic contributions to atmosphe-
| ric energetics, |     | Scientific reports, | 2021, | vol. 11, | p. 13202 |
| --------------- | --- | ------------------- | ----- | -------- | -------- |
Oort A. H., On estimates of the atmospheric energy cycle, Monthly Weather Review, 1964,
vol. 92
Ooyama K. V., Conceptual evolution of the theory and modeling of the tropical cyclone,
Journal of the Meteorological Society of Japan. Ser. II, 1982, vol. 60, p. 369
Oppenheim A. V., Discrete-time signal processing. Pearson Education India, 1999
Oppenheim A. V., Schafer R. W., Discrete-Time Signal Processing. Prentice Hall, 2009
Ozawa H., Shimokawa S., Thermodynamics of a tropical cyclone: Generation and dis-
sipation of mechanical energy in a self-driven convection system, Tellus A: Dynamic
| Meteorology | and | Oceanography, | 2015, | vol. 67, | p. 24216 |
| ----------- | --- | ------------- | ----- | -------- | -------- |
Palm´en E. H., Newton C. W., Atmospheric circulation systems: their structure and phy-
| sical interpretation. |     | vol. | 13, Academic | press, 1969 |     |
| --------------------- | --- | ---- | ------------ | ----------- | --- |
Parise C. K., Calliari L. J., Krusche N., Extreme storm surges in the south of Brazil:
atmospheric conditions and shore erosion, Brazilian Journal of Oceanography, 2009,
| vol. 57, | p. 175 |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- |
Parzen E., On estimation of a probability density function and mode, The annals of mathe-
| matical | statistics, | 1962, vol. | 33, p. | 1065 |     |
| ------- | ----------- | ---------- | ------ | ---- | --- |
Pedregosa F., Varoquaux G., Gramfort A., Michel V., Thirion B., Grisel O., Blondel
M., Prettenhofer P., Weiss R., Dubourg V., Vanderplas J., Passos A., Cournapeau D.,
´
Brucher M., Perrot M., Edouard Duchesnay Scikit-learn: Machine Learning in Python,
| Journal | of Machine | Learning | Research, | 2011, vol. | 12, p. 2825 |
| ------- | ---------- | -------- | --------- | ---------- | ----------- |
Pereira Filho A. J., Pezza A. B., Simmonds I., Lima R. S., Vianna M., New perspectives
on the synoptic and mesoscale structure of Hurricane Catarina, Atmospheric Research,
| 2010, vol. | 95, p. | 157 |     |     |     |
| ---------- | ------ | --- | --- | --- | --- |
Petterssen S., Smebye S., On the development of extratropical cyclones, Quarterly Journal
| of the Royal | Meteorological |     | Society, | 1971, vol. | 97, p. 457 |
| ------------ | -------------- | --- | -------- | ---------- | ---------- |

Bibliography 251
PezzaA.B.,GardeL.A.,VeigaJ.A.P.,SimmondsI.,Largescalefeaturesandenergeticsof
the hybrid subtropical low ‘Duck’over the Tasman Sea, Climate dynamics, 2014, vol. 42,
p. 453
Pezza A. B., Simmonds I., The first South Atlantic hurricane: Unprecedented blocking,
low shear and climate change, Geophysical Research Letters, 2005, vol. 32
Pezza A. B., Simmonds I., Pereira Filho A. J., Climate perspective on the large-scale circu-
lation associated with the transition of the first South Atlantic hurricane, International
Journal of Climatology: A Journal of the Royal Meteorological Society, 2009, vol. 29, p.
1116
Pezza A. B., Veiga J. A. P., Simmonds I., Keay K., Mesquita M. d. S., Environmental
energetics of an exceptional high-latitude storm, Atmospheric Science Letters, 2010,
| vol. 11, p. | 39  |     |     |
| ----------- | --- | --- | --- |
Pinto J. G., Spangehl T., Ulbrich U., Speth P., Sensitivities of a cyclone detection and
tracking algorithm: individual tracks and climatology, Meteorologische Zeitschrift, 2005,
| vol. 14, p. | 823 |     |     |
| ----------- | --- | --- | --- |
Piva E. D., Gan M. A., Rao V. B., Energetics of winter troughs entering South America,
| Monthly Weather | Review, | 2010, vol. 138, | p. 1084 |
| --------------- | ------- | --------------- | ------- |
Plumb R. A., A new look at the energy cycle, Journal of Atmospheric Sciences, 1983,
| vol. 40, p. | 1669 |     |     |
| ----------- | ---- | --- | --- |
Proakis J. G., Manolakis D. G., Digital Signal Processing: Principles, Algorithms, and
| Applications. | Prentice Hall, | 2006 |     |
| ------------- | -------------- | ---- | --- |
Radinovic D., On the development of orographic cyclones, Quarterly Journal of the Royal
| Meteorological | Society, 1986, | vol. 112, | p. 927 |
| -------------- | -------------- | --------- | ------ |
Ramage C. S., Hurricane development, Journal of Atmospheric Sciences, 1959, vol. 16, p.
227
Ramon J., Lled´o L., Torralba V., Soret A., Doblas-Reyes F. J., What global reanalysis best
represents near-surface winds?, Quarterly Journal of the Royal Meteorological Society,
| 2019, vol. | 145, p. 3236 |     |     |
| ---------- | ------------ | --- | --- |

| 252 |     |     | Bibliography |     |
| --- | --- | --- | ------------ | --- |
Rasmussen E., The polar low as an extratropical CISK disturbance, Quarterly Journal of
| the Royal | Meteorological | Society, | 1979, vol. 105, | p. 531 |
| --------- | -------------- | -------- | --------------- | ------ |
Rasmussen E., A case study of a polar low development over the Barents Sea, Tellus A,
| 1985, vol. | 37, p. 407 |     |     |     |
| ---------- | ---------- | --- | --- | --- |
Rasmussen E. A., A comparative study of tropical cyclones and polar lows. vol. 47, A.
| Deepak | Publishing, | 1989, 80 |     |     |
| ------ | ----------- | -------- | --- | --- |
Rayleigh On the stability or instability of certain fluid motions (iii.), Proceedings of the
| London | Mathematical | Society, | 1895, vol. 1, p. 5 |     |
| ------ | ------------ | -------- | ------------------ | --- |
Raymond D. J., Wave-CISK and convective mesosystems, J. Atmos. Sci, 1976, vol. 33, p.
2392
Read P., Kennedy D., Lewis N., Scolan H., Tabataba-Vakili F., Wang Y., Wright S.,
Young R., Baroclinic and barotropic instabilities in planetary atmospheres: energetics,
equilibration and adjustment, Nonlinear Processes in Geophysics, 2020, vol. 27, p. 147
Reboita M., Crespo N., Dutra L., Silva B., Capucin B., da Rocha R., Iba: the first pure
tropical cyclogenesis over the western South Atlantic Ocean, Journal of Geophysical
| Research: | Atmospheres, | 2021, vol. | 126, p. e2020JD033431 |     |
| --------- | ------------ | ---------- | --------------------- | --- |
Reboita M. S., Da Rocha R. P., Ambrizzi T., Sugahara S., South Atlantic Ocean cyclo-
genesis climatology simulated by regional climate model (RegCM3), Climate Dynamics,
| 2010, vol. | 35, p. 1331 |     |     |     |
| ---------- | ----------- | --- | --- | --- |
Reboita M. S., da Rocha R. P., de Souza M. R., Llopart M., et al., Extratropical cyclones
over the southwestern South Atlantic Ocean: HadGEM2-ES and RegCM4 projections,
| Int. J. | Climatol, 2018, | vol. 38, p. | 2866 |     |
| ------- | --------------- | ----------- | ---- | --- |
Reboita M. S., Da Rocha R. P., Oliveira D. M. d., Key features and adverse weather of the
named subtropical cyclones over the Southwestern South Atlantic Ocean, Atmosphere,
| 2018, vol. | 10, p. 6 |     |     |     |
| ---------- | -------- | --- | --- | --- |
Reboita M. S., Gan M. A., Rocha R. P. d., Ambrizzi T., Regimes de precipita¸ca˜o na
Am´erica do Sul: uma revisa˜o bibliogra´fica, Revista brasileira de meteorologia, 2010,
| vol. 25, | p. 185 |     |     |     |
| -------- | ------ | --- | --- | --- |

Bibliography 253
Reboita M. S., Gan M. A., Rocha R. P. d., Cust´odio I. S., Ciclones em superf´ıcie nas
latitudesaustrais: ParteI-revis˜aobibliogr´afica, RevistaBrasileiradeMeteorologia, 2017,
| vol. 32, | p. 171 |     |     |     |
| -------- | ------ | --- | --- | --- |
Reboita M. S., Gozzo L. F., Crespo N. M., Custodio M. d. S., Lucyrio V., de Jesus E. M.,
da Rocha R. P., From a Shapiro–Keyser extratropical cyclone to the subtropical cyclone
Raoni: An unusual winter synoptic situation over the South Atlantic Ocean, Quarterly
Journal of the Royal Meteorological Society, 2022, vol. 148, p. 2991
Reboita M. S., Oliveira D., Da Rocha R., Dutra L., Subtropical cyclone Anita’s poten-
tial to tropical transition under warmer sea surface temperature scenarios, Geophysical
| Research | Letters, | 2019, vol. | 46, p. 8484 |     |
| -------- | -------- | ---------- | ----------- | --- |
Reed R. J., Norquist D. C., Recker E. E., The structure and properties of African wave
disturbances as observed during phase III of GATE, Monthly Weather Review, 1977,
| vol. 105, | p. 317 |     |     |     |
| --------- | ------ | --- | --- | --- |
Reed R. J., Wolfe J. L., Nishimoto H., A spectral analysis of the energetics of the stra-
tospheric sudden warming of early 1957, Journal of the Atmospheric Sciences, 1963,
| vol. 20, | p. 256 |     |     |     |
| -------- | ------ | --- | --- | --- |
Rennick M. A., The generation of African waves, Journal of Atmospheric Sciences, 1976,
| vol. 33, | p. 1955 |     |     |     |
| -------- | ------- | --- | --- | --- |
Riehl H., On the formation of typhoons, Journal of the Atmospheric Sciences, 1948, vol. 5,
p. 247
Rivals H., Rivals H., Cammas J., Cammas J.-P., Renfrew I. A., Renfrew I. A., Secondary
cyclogenesis: The initiation phase of a frontal wave observed over the eastern Atlantic,
| Quarterly | Journal | of the Royal | Meteorological | Society, 1998 |
| --------- | ------- | ------------ | -------------- | ------------- |
Robertson F., Smith P., The impact of model moist processes on the energetics of extra-
tropical cyclones, Monthly Weather Review, 1983, vol. 111, p. 723
Rosa M. B., Ferreira N. J., Gan M. A., Machado L. H. R., Energetics of cyclogenesis events
over the southern coast of Brazil, Revista Brasileira de Meteorologia, 2013, vol. 28, p.
231

| 254 |     |     |     | Bibliography |     |
| --- | --- | --- | --- | ------------ | --- |
Rosenblatt M., Estimation of a probability density-function and mode, Ann Math Statist,
| 1956, vol. | 27, p. 832 |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
RudevaI., GulevS.K., Climatologyofcyclonesizecharacteristicsandtheirchangesduring
the cyclone life cycle, Monthly Weather Review, 2007, vol. 135, p. 2568
Saltzman B., Fleisher A., Further statistics on the modes of release of available potential
| energy, Journal | of Geophysical |     | Research, | 1961, vol. | 66, p. 2271 |
| --------------- | -------------- | --- | --------- | ---------- | ----------- |
SandersF.,GyakumJ.R.,Synoptic-dynamicclimatologyofthe“bomb”,MonthlyWeather
| Review, 1980, | vol. 108, | p. 1589 |     |     |     |
| ------------- | --------- | ------- | --- | --- | --- |
Savitzky A., Golay M. J., Smoothing and differentiation of data by simplified least squares
| procedures., | Analytical | chemistry, | 1964, | vol. 36, | p. 1627 |
| ------------ | ---------- | ---------- | ----- | -------- | ------- |
Schemm S., Sprenger M., Wernli H., When during their life cycle are extratropical cyclones
attended by fronts?, Bulletin of the American Meteorological Society, 2018, vol. 99, p.
149
Schneider T., The general circulation of the atmosphere, Annu. Rev. Earth Planet. Sci.,
| 2006, vol. | 34, p. 655 |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --- |
Schultz D. M., Keyser D., Bosart L. F., The effect of large-scale flow on low-level frontal
structure and evolution in midlatitude cyclones, Monthly weather review, 1998, vol. 126,
p. 1767
Shapiro M. A., Doyle J., Zou X., Jorgensen D. P., Jorgensen D. P., Jorgensen D. P.,
Extratropical Secondary Cyclones: Simulations and Observations,, null, 1997
Shapiro M. A., Keyser D., Fronts, jet streams and the tropopause. Springer, 1990
Shea D. J., Gray W. M., The hurricane’s inner core region. I. Symmetric and asymmetric
structure, Journal of the Atmospheric Sciences, 1973, vol. 30, p. 1544
Silva Dias P. L., Gan M., Beven J. L., Pezza A., Holland G., Pereira A., McTaggart-Cowan
R., Diniz F. d. A., Seluchi M., Braga H. J., The Catarina Phenomenon. In Proceedings
of the Sixth International Workshop on Tropical Cyclones , Sa˜o Paulo, Brazil, 2004

Bibliography 255
Simmonds I., Size changes over the life of sea level cyclones in the NCEP reanalysis,
| Monthly | Weather | Review, | 2000, | vol. 128, | p. 4118 |
| ------- | ------- | ------- | ----- | --------- | ------- |
Simmonds I., Keay K., Mean Southern Hemisphere extratropical cyclone behavior in the
40-year NCEP–NCAR reanalysis, Journal of Climate, 2000, vol. 13, p. 873
Simmonds I., Murray R. J., Southern extratropical cyclone behavior in ECMWF analyses
during the FROST special observing periods, Weather and forecasting, 1999, vol. 14, p.
878
Simmons A. J., Hoskins B. J., The downstream and upstream development of unstable
baroclinic waves, Journal of the Atmospheric Sciences, 1979, vol. 36, p. 1239
Simpson R. H., Evolution of the Kona storm a subtropical cyclone, Journal of Atmospheric
| Sciences, | 1952, | vol. 9, | p. 24 |     |     |
| --------- | ----- | ------- | ----- | --- | --- |
Sinclair M. R., An objective cyclone climatology for the Southern Hemisphere, Monthly
| Weather | Review, | 1994, | vol. 122, | p. 2239 |     |
| ------- | ------- | ----- | --------- | ------- | --- |
Sinclair M. R., A climatology of cyclogenesis for the Southern Hemisphere, Monthly We-
| ather Review, |     | 1995, vol. | 123, | p. 1601 |     |
| ------------- | --- | ---------- | ---- | ------- | --- |
Smith P. J., On the contribution of a limited region to the global energy budget, Tellus,
| 1969, vol. | 21, | p. 202 |     |     |     |
| ---------- | --- | ------ | --- | --- | --- |
Smith P. J., The energetics of extratropical cyclones, Reviews of Geophysics, 1980, vol. 18,
p. 378
Smith P. J., Vincent D. G., Edmond Jr H. J., The time dependence of reference pressure
in limited region available potential energy budget equations, Tellus, 1977, vol. 29, p.
476
Smith S. W., The Scientist and Engineer’s Guide to Digital Signal Processing. California
| Technical | Publishing, |     | 1997 |     |     |
| --------- | ----------- | --- | ---- | --- | --- |
Spiridonov V., Curi´c ´ M., Fundamentals of meteorology. Springer, 2021
Starr V. P., Note concerning the nature of the large-scale eddies in the atmosphere, Tellus,
| 1953, vol. | 5, p. | 494 |     |     |     |
| ---------- | ----- | --- | --- | --- | --- |

| 256 |     |     |     | Bibliography |
| --- | --- | --- | --- | ------------ |
Starr V. P., Further statistics concerning the general circulation, Tellus, 1959, vol. 11, p.
481
Steele C., Dorling S., von Glasow R., Bacon J., Modelling sea-breeze climatologies and
interactions on coasts in the southern North Sea: implications for offshore wind energy,
Quarterly Journal of the Royal Meteorological Society, 2015, vol. 141, p. 1821
Stoll P. J., Spengler T., Terpstra A., Graversen R. G., Polar lows–moist-baroclinic cyclones
developing in four different vertical wind shear environments, Weather and Climate
| Dynamics, | 2021, vol. | 2,  | p. 19 |     |
| --------- | ---------- | --- | ----- | --- |
Stull R. B., Practical meteorology: an algebra-based survey of atmospheric science. Uni-
| versity | of British Columbia, |     | 2015 |     |
| ------- | -------------------- | --- | ---- | --- |
Sutcliffe R., A contribution to the problem of development, Quarterly Journal of the Royal
| Meteorological | Society, |     | 1947, vol. | 73, p. 370 |
| -------------- | -------- | --- | ---------- | ---------- |
Swart N. C., Fyfe J. C., Gillett N., Marshall G. J., Comparing trends in the southern
annular mode and surface westerly jet, Journal of Climate, 2015, vol. 28, p. 8840
Taljaard J., Development, distribution and movement of cyclones and anticyclones in the
Southern Hemisphere during the IGY, Journal of Applied Meteorology and Climatology,
| 1967, vol. | 6, p. 973 |     |     |     |
| ---------- | --------- | --- | --- | --- |
Terry J. P., Tropical cyclones: climatology and impacts in the South Pacific. Springer
| Science | & Business | Media, | 2007 |     |
| ------- | ---------- | ------ | ---- | --- |
Thorndike R. L., Who belongs in the family?, Psychometrika, 1953, vol. 18, p. 267
Tibaldi S., Buzzi A., Malguzzi P., Orographically induced cyclogenesis: Analysis of nume-
rical experiments, Monthly Weather Review, 1980, vol. 108, p. 1302
TrenberthK.E., Ontheinterpretationofthediagnosticquasi-geostrophicomegaequation,
| Mon. Wea. | Rev, 1978, | vol. | 106, | p. 131 |
| --------- | ---------- | ---- | ---- | ------ |
Trigo I. F., Climatology and interannual variability of storm-tracks in the Euro-Atlantic
sector: acomparisonbetweenERA-40andNCEP/NCARreanalyses,ClimateDynamics,
| 2006, vol. | 26, p. 127 |     |     |     |
| ---------- | ---------- | --- | --- | --- |

257
Bibliography
van Loon H., A climatological study of the atmospheric circulation in the Southern He-
misphere during the IGY, Part I: 1 July 1957–31 March 1958, Journal of Applied Mete-
orology and Climatology, 1965, vol. 4, p. 479
Veiga J. A. P., Ambrizzi T., et al., A global and hemispherical analysis of the Lorenz
energeticsbasedontherepresentativeconcentrationpathwaysusedinCMIP5, Advances
in Meteorology, 2013, vol. 2013
Veiga J. A. P., Pezza A. B., Simmonds I., Silva Dias P. L., An analysis of the environ-
mental energetics associated with the transition of the first South Atlantic hurricane,
Geophysical Research Letters, 2008, vol. 35
Vera C. S., Vigliarolo P. K., Berbery E. H., Cold season synoptic-scale waves over subtro-
pical South America, Monthly Weather Review, 2002, vol. 130, p. 684
Vianna M., Menezes V., Pezza A., Simmonds I., Interactions between Hurricane Cata-
rina (2004) and warm core rings in the South Atlantic Ocean, Journal of Geophysical
Research: Oceans, 2010, vol. 115
Vincent D., Chang L., Some further considerations concerning energy budgets of moving
systems, Tellus, 1973, vol. 25, p. 224
Virtanen P., Gommers R., Oliphant T. E., Haberland M., Reddy T., Cournapeau D., Bu-
rovskiE.,PetersonP.,WeckesserW.,BrightJ.,etal.,SciPy1.0: fundamentalalgorithms
for scientific computing in Python, Nature methods, 2020, vol. 17, p. 261
Virtanen P., Gommers R., Oliphant T. E., Haberland M., Reddy T., Cournapeau D.,
Burovski E., Peterson P., Weckesser W., Bright J., van der Walt S. J., Brett M., Wilson
J.,MillmanK.J.,MayorovN.,NelsonA.R.J.,JonesE.,KernR.,LarsonE.,CareyC.J.,
˙
Polat I., Feng Y., Moore E. W., VanderPlas J., Laxalde D., Perktold J., Cimrman R.,
Henriksen I., Quintero E. A., Harris C. R., Archibald A. M., Ribeiro A. H., Pedregosa
F., van Mulbregt P., SciPy 1.0 Contributors SciPy 1.0: Fundamental Algorithms for
Scientific Computing in Python, Nature Methods, 2020, vol. 17, p. 261
Wahab M. A., Basset H. A., Lasheen A., On the mechanism of winter cyclogenesis in
relation to vertical axis tilt, Meteorology and Atmospheric Physics, 2002, vol. 81, p. 103

| 258 |     |     | Bibliography |     |
| --- | --- | --- | ------------ | --- |
Walsh K., Tropical cyclones and climate change: unresolved issues, Climate Research,
| 2004, vol. | 27, p. 77 |     |     |     |
| ---------- | --------- | --- | --- | --- |
Walsh K. J., Camargo S. J., Knutson T. R., Kossin J., Lee T.-C., Murakami H., Patricola
C., Tropical cyclones and climate change, Tropical Cyclone Research and Review, 2019,
| vol. 8, | p. 240 |     |     |     |
| ------- | ------ | --- | --- | --- |
Walsh K. J., McBride J. L., Klotzbach P. J., Balachandran S., Camargo S. J., Holland G.,
Knutson T. R., Kossin J. P., Lee T.-c., Sobel A., et al., Tropical cyclones and climate
change, Wiley Interdisciplinary Reviews: Climate Change, 2016, vol. 7, p. 65
WangD., LinY., ChavasD.R., Tropicalcyclonepotentialsize, JournaloftheAtmospheric
| Sciences, | 2022, vol. 79, | p. 3001 |     |     |
| --------- | -------------- | ------- | --- | --- |
Waskom M. L., Seaborn: statistical data visualization, Journal of Open Source Software,
| 2021, vol. | 6, p. 3021 |     |     |     |
| ---------- | ---------- | --- | --- | --- |
Weatherford C. L., Gray W. M., Typhoon structure as revealed by aircraft reconnaissance.
Part I: Data analysis and climatology, Monthly Weather Review, 1988, vol. 116, p. 1032
Whitaker J. S., Davis C. A., Cyclogenesis in a saturated environment, Journal of the
| atmospheric | sciences, 1994, | vol. 51, | p. 889 |     |
| ----------- | --------------- | -------- | ------ | --- |
Whittaker L., Horn L., Northern Hemisphere extratropical cyclone activity for four mid-
| season | months, Journal | of Climatology, | 1984, vol. | 4, p. 297 |
| ------ | --------------- | --------------- | ---------- | --------- |
Wiin-NielsenA., Astudyofenergyconversionandmeridionalcirculationforthelarge-scale
motion in the atmosphere, Monthly Weather Review, 1959, vol. 87, p. 319
Wiin-Nielsen A., Brown J. A., Drake M., On atmospheric energy conversions between the
| zonal flow | and the eddies, | Tellus, 1963, | vol. 15, | p. 261 |
| ---------- | --------------- | ------------- | -------- | ------ |
Willoughby H. E., Marks F. D., Feinberg R. J., Stationary and moving convective bands
in hurricanes, Journal of the Atmospheric Sciences, 1984, vol. 41, p. 3189
Wu M.-L. C., Reale O., Schubert S. D., Suarez M. J., Thorncroft C. D., African easterly
jet: Barotropic instability, waves, and cyclogenesis, Journal of Climate, 2012, vol. 25, p.
1489

Bibliography 259
Yanai M., A detailed analysis of typhoon formation, Journal of the Meteorological Society
| of Japan. | Ser. II, 1961, | vol. 39, | p. 187 |     |
| --------- | -------------- | -------- | ------ | --- |
Yanase W., Niino H., Hodges K., Kitabatake N., Parameter spaces of environmental fields
responsible for cyclone development from tropics to extratropics, Journal of Climate,
| 2014, | vol. 27, p. 652 |     |     |     |
| ----- | --------------- | --- | --- | --- |
Yano J.-I., Emanuel K., An improved model of the equatorial troposphere and its coupling
with the stratosphere, Journal of Atmospheric Sciences, 1991, vol. 48, p. 377
Zehr R. M., , 1992 Technical Report 61 Tropical cyclogenesis in the western North Pacific.
NationalEnvironmentalSatellite,Data,andInformationService(NESDIS),NOAAUSA
| Zheng | Z., , 2021 zzheng93/pyEOF: |     | First release | (v0.0.0) |
| ----- | -------------------------- | --- | ------------- | -------- |

260
Bibliography

Appendix

A
Appendix
|     |     | Lanczos | Filter |     |     |
| --- | --- | ------- | ------ | --- | --- |
A.1 Formulation
The Lanczos band-pass filter is mathematically formulated as follows:

|      |  2·(cutoff    | −cutoff           | )   |           | if n = 0          |
| ---- | --------------- | ----------------- | --- | --------- | ----------------- |
|      |                 | high              | low |           |                   |
| w(n) | =               |                   |     |           | (A.1)             |
|      |                |                   |     |           | (cid:0) n (cid:1) |
|      | (sinc(2·cutoff | ·n)−sinc(2·cutoff |     | ·n))·sinc | if n ̸= 0         |
|      |                 | high              |     | low       | N                 |
where n is the index of the weight in the filter window, w(n) is the weight at index n,
cutoff and cutoff are the specified lower and upper cutoff frequencies, respectively,
| low | high |     |     |     |     |
| --- | ---- | --- | --- | --- | --- |
and N is half the length of the filter window. The sinc function is defined as:
sin(πx)
sinc(x) = (A.2)
πx
| A.2 Related | Issues |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
The Lanczos filter, like other finite impulse response filters (FIR), can exhibit issues at
discontinuities in the data. For the vorticity data series, this would be at its endpoints.
These issues arise primarily due to the Gibbs phenomenon and edge effects:
1. Gibbs Phenomenon: The Gibbs phenomenon refers to the overshoot and ringing
that occurs near discontinuities when approximating a function with a finite series of basis
functions(Gibbs,1898;Hamming,1989). InthecontextoftheLanczosfilter, whichutilizes
a sinc function, abrupt changes at the edges of the filter window can cause ringing effects
| at the points | of discontinuity | in the | data. |     |     |
| ------------- | ---------------- | ------ | ----- | --- | --- |

264
Appendix A. LanczosFilter
2. Edge Effects: FIR filters, including the Lanczos filter, can produce artifacts at the
boundaries of the data series due to the reliance on data points that may not be available
at the edges (Oppenheim and Schafer, 2009; Proakis and Manolakis, 2006). Techniques
such as zero-padding or reflection are often used to mitigate these effects, but they can
still result in artifacts or less accurate filtering near the boundaries.
3. Finite Window Length: The window length of the Lanczos filter determines the
number of data points used in the convolution. A finite window length means the filter
may not fully capture long-term trends or low-frequency components, especially at the
edges, leading to discontinuities or spurious oscillations (Smith, 1997; Oppenheim, 1999).
4. Windowing Effect: The Lanczos filter uses a windowed sinc function to perform
the convolution. While windowing reduces spectral leakage by smoothing the transition at
the edges of the filter, it also introduces artifacts, particularly near discontinuities where
the transition from one region to another is abrupt (Harris, 1978; Mitra, 2001).
To mitigate this, a weaker low-pass Lanczos filter is applied to the initial and final 5%
of the data series, ensuring smoother transitions at the endpoints (Figure 3.3b).

B
Appendix
Lorenz Energy Cycle Program Description
To compute the Lorenz Energy Cycle (LEC), an open-source Python application na-
med ”lorenz-cycle”was developed and is available on GitHub. The application is designed
for collaboration and transparency, allowing peers to freely use, modify, and review the
computation procedures. Full documentation and a user guide with illustrative examples
can be found at https://github.com/daniloceano/lorenz-cycle.
The lorenz-cycle application utilizes the mathematical expressions detailed in Section
2.4.2 and supports both Eulerian and Semi-Lagrangian frameworks. Additionally, it can
computethegenerationanddissipationtermsdirectlyorestimatethemasresiduals. When
using the residual approach, the budget equations are estimated using finite differences:
a first-order forward/backward method is applied to the endpoints, while second-order
centered differences are employed for the remaining data points. Regardless of whether
residuals are estimated or not, the generation terms are always computed.
In the Semi-Lagrangian framework, users can either run the program using a predefined
track file or iteratively choose the computation domain step-by-step. For the Eulerian
framework, users must provide a ”box limits”file containing the minimum and maximum
latitudes and longitudes for the desired computational domain. When using a predefined
trackfile, thetrackmayonlycontainthesystem’scentralposition(latitudeandlongitude),
in which case the program defaults to a 15◦ ×15◦ domain for each time step. The track
file can also be adjusted to include the length and width of the computational domain for
each time step.
Additionally, in the Semi-Lagrangian approach, users can provide an input file con-
taining the required meteorological data or, by using an appropriate program flag, auto-
matically download the matching ERA5 dataset using ECMWF’s Python plugin ”CDS

266
Appendix B. LorenzEnergyCycleProgramDescription
API”(https://pypi.org/project/cdsapi/). To use this option, the user must ins-
tall and configure the library as instructed at https://cds.climate.copernicus.eu/
api-how-to.
The program is not limited to the ERA5 dataset and can run with any meteorological
dataset, whether it is reanalysis data or model output. It reads a namelist file specifying
the variable naming conventions used in the input file. The requirements for the input
file are: 1) it must be a NetCDF file, 2) the horizontal grid must be structured, and 3)
it must use an isobaric vertical coordinate system. The file should also contain data for
temperature,uandvwindcomponents,ω verticalwindcomponent,andeithergeopotential
or geopotential height data.
For handling meteorological constants and variable units, the lorenz-cycle program uses
the MetPy package (May et al., 2022). This open-source package, initially developed and
maintainedbytheNationalScienceFoundation(NSF)Unidata,amemberoftheUniversity
Corporation for Atmospheric Research (UCAR) Community Programs, ensures correct
variable assignment and unit conversion, preventing errors such as summing variables with
different units.
To ensure efficient and fast computations, the program is fully parallelized using Dask,
a parallel computing library that handles large datasets efficiently (Daniel, 2019). Dask
allows large data arrays to be split into smaller chunks for independent processing by
multiple computing cores, preventing memory overload and optimizing performance. In
the lorenz-cycle program, Dask’s configuration is optimized to handle large matrices by
dividing them into smaller chunks for efficient processing.
The program outputs the results for each term in comma-separated values (CSV) fi-
les. It generates one CSV file for each term, and for energy, conversion, and generation
terms, it also provides results for each vertical level, enabling a two-dimensional analysis.
Additionally, the program can be configured by the user to automatically generate plots.
These plots include spatial representations of the computational domain defined for the
analysis, time series of the system’s central minimum pressure and relative vorticity at 850
hPa, time series of each LEC term, Hovm¨oller diagrams, and complete energy flux boxes
for the LEC.

C
Appendix
Complete Life Cycle LEC EOFs Reconstructed
Figures C.1 illustrate the reconstructed EOFs for the complete life cycle. These EOFs
were reconstructed by reversing the normalization process and adding the mean values to
each EOF.

| 268 |                   | Appendix | C. CompleteLifeCycleLECEOFsReconstructed |                   |      |
| --- | ----------------- | -------- | ---------------------------------------- | ----------------- | ---- |
|     | (a) Reconstructed |          | EOF1                                     | (b) Reconstructed | EOF2 |
|     | (c) Reconstructed |          | EOF3                                     | (d) Reconstructed | EOF4 |
FigureC.1: LorenzEnergyCycle(LEC)TermsEOFsreconstructed. Thenumbersadjacenttothearrows
denotethemagnitudeanddirectionoftheanomaly,withgreenindicatingpositivevaluesandredindicating
negative values.

D
Appendix
|     |     | LEC | - Terms | Correlation |
| --- | --- | --- | ------- | ----------- |
Figure D.1 presents correlation plots between the conversion terms C and C (Figure
A E
D.1a) and between eddy kinetic energy K and relative vorticity at 850 hPa in the cyclone
E
| center (Figure | D.1b). |     |     |     |
| -------------- | ------ | --- | --- | --- |
(a) (b)
Figure D.1: Correlation between C and C (a), as well as between K and relative vorticity at 850
A E E
hPa in the cyclone center (b). The red line represents the linear regression, with the Pearson’s correlation
| coefficient | (r) indicated | in each plot. |     |     |
| ----------- | ------------- | ------------- | --- | --- |

| 270 | Appendix | D. LEC-TermsCorrelation |
| --- | -------- | ----------------------- |

E
Appendix
|     |     | LEC Results | for Reg1 | System |
| --- | --- | ----------- | -------- | ------ |
Here, the same analysis conducted by Dias Pinto and Rocha (2011) is performed for the
”Reg1”system. The aim is to validate the results obtained by the ”lorenz-cycle”program
and provide support for the analysis performed using the Lorenz Phase Space Diagrams.
Figure E.1 illustrates the computational domain used for computing the LEC for this
system, while Figure E.2 displays the energy and conversion terms, matching Figure 5
| from Dias | Pinto | and Rocha (2011). |     |     |
| --------- | ----- | ----------------- | --- | --- |
Figure E.1: Computational domain used for analyzing the ”Reg1”system (Dias Pinto and Rocha, 2011).

| 272 |     | Appendix | E. LECResultsforReg1System |
| --- | --- | -------- | -------------------------- |
Figure E.2: Energy and conversion terms computed for the ”Reg1”system (Dias Pinto and Rocha, 2011),
| using an Eulerian | framework | (Figure E.1). |     |
| ----------------- | --------- | ------------- | --- |

F
Appendix
|     | Lorenz | Phase | Space | - All Systems |
| --- | ------ | ----- | ----- | ------------- |
Figures F.1 and F.2 illustrate the LPS diagrams for all systems with genesis in ARG,
LA-PLATA, and SE-BR between 1979 and 2020. Due to the large amount of data and the
presence of outliers, it is not possible to discern the relative importance of the LEC terms
for smaller groups of systems precisely. However, the LPS visualization still provides an
overview of the main mechanisms related to cyclone development in the SESA region.
For LPS diagram type 1, a cloud of data spreads primarily over the top-left quadrant.
Moreover, there is a high density below the 1:1 diagonal line. This indicates that for
most systems, there is a shared importance of baroclinic and barotropic conversions for
eddy development, as indicated in previous chapters. For diagram type 2, a clear distinct
tendency cannot be found from this analysis, indicating a high quantity of systems that
| either import | or export | both A and | K . |     |
| ------------- | --------- | ---------- | --- | --- |
|               |           | E          | E   |     |

| 274 | Appendix | F. LorenzPhaseSpace-AllSystems |
| --- | -------- | ------------------------------ |
Figure F.1: Lorenz Phase Space (LPS) diagram 1 for all systems with genesis near South America.

| AppendixF. | LorenzPhaseSpace-AllSystems | 275 |
| ---------- | --------------------------- | --- |
Figure F.2: Lorenz Phase Space (LPS) diagram 2 for all systems with genesis near South America.

| 276 | Appendix | F. LorenzPhaseSpace-AllSystems |
| --- | -------- | ------------------------------ |

G
Appendix
|     | Lorenz | Phase | Space | 1 - Early | Decay |
| --- | ------ | ----- | ----- | --------- | ----- |
Figure G.1: Lorenz Phase Space (LPS) diagram 1 for all systems represented in cluster 3 of the ”decay,
| intensification, | matude, decay | 2”life cycle. |     |     |     |
| ---------------- | ------------- | ------------- | --- | --- | --- |

| 278 | Appendix | G. LorenzPhaseSpace1-EarlyDecay |
| --- | -------- | ------------------------------- |

H
Appendix
| Lorenz |     | Phase Space | - Most | Intense | Systems |
| ------ | --- | ----------- | ------ | ------- | ------- |
FigureH.1: LorenzPhaseSpace(LPS)diagram1fortheenergypatternsofthesystemspresentingcentral
| relative vorticity | higher than | the 0.9 quantile. |     |     |     |
| ------------------ | ----------- | ----------------- | --- | --- | --- |

| 280 | Appendix | H. LorenzPhaseSpace-MostIntenseSystems |
| --- | -------- | -------------------------------------- |

I
Appendix
| Tracks              | - Energy          | Pattern     | 1            |     |
| ------------------- | ----------------- | ----------- | ------------ | --- |
| Figure I.1: Cyclone | tracks associated | with energy | pattern (EP) | 1.  |