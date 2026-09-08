Universidade de São Paulo
Instituto de Astronomia, Geofísica e Ciências Atmosféricas
Departamento de Ciências Atmosféricas
Ciclones subtropicais e ventos em superfície no sudoeste do
Oceano Atlântico Sul: Climatologia e extremos
Andressa Andrade Cardoso
São Paulo
2019

1

Andressa Andrade Cardoso
Dissertação apresentada ao Departamento de
Ciências Atmosféricas do Instituto de
Astronomia, Geofísica e Ciências Atmosféricas
da Universidade de São Paulo como requisito
parcial para a obtenção do título de Mestre em
Ciências.
Área de Concentração: Meteorologia
Orientador: Prof. Dra. Rosmeri Porfírio da
Rocha
Versão Corrigida. O original encontra-se disponível na Unidade
São Paulo
2019
2

3

“Não podemos esperar em construir um mundo
melhor sem melhorar os indivíduos” - Marie
Curie
4

AGRADECIMENTOS
Agradeço meus pais pelo incentivo e compreensão, principalmente pela minha mãe
que acreditou no meu potencial;
Agradeço a Deus por ter me guiado durante o mestrado;
Minha orientadora Profa Dra Rosmeri Porfírio da Rocha por me ajudar e me orientar
durante o período do mestrado;
A minha ex-orientadora e amiga Clara Iwabe pelas conversas, almoços, incentivos e
compreensão;
Aos membros da banca do exame de qualificação com as críticas construtivas e
sugestões que melhoraram meu trabalho;
Aos meus amigos que passaram na sala ao longo destes dois anos: Ana Helena
Maciel pelas ajudas no software R e no incentivo aos meus ataques. Yusnelis por
sempre alegrar a sala. Felipe Massarico por me fazer rir mesmo em dias difíceis,
Marcos Stoco por alegrar e me fazer sair da minha bolha social e sair mais vezes,
Franciele Barros pelos incentivos, conselhos, conversas. A Luana, mesmo não
dividindo sala, sempre estava por perto me incentivando;
Agradeço ao Eduardo Marcos por ter me ajudado na organização das trajetórias dos
ciclones e na densidade das trajetórias. E a Natália Crespo pela ajuda em algumas
dúvidas durante a minha pesquisa, também nas correções da qualificação;
Agradeço aos meus amigos do IAG pela amizade e apoio;
Aos meus amigos de Bauru por me entenderem durante este período,
principalmente quando falava que não tinha tempo em visitá-los;
Ao meu namorado Thiago Pachelli por me compreender;
A minha colega de apartamento Isabela Diniz por me animar e ouvir meus
desabafos;
Ao Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) ao
apoio financeiro;
Aos funcionários do IAG que me ajudaram de certa forma.
5

Resumo
Cardoso, A. A, 2019: Ciclones subtropicais e ventos em superfície no sudoeste do
Oceano Atlântico Sul: climatologia e extremos. 110 f. Dissertação de mestrado -
Instituto de Astronomia, Geofísica e Ciências Atmosféricas, Universidade de São
Paulo, São Paulo.
A velocidade do vento é uma das variáveis meteorológicas com grande impacto para
a economia e sociedade, principalmente quando ocorrem eventos extremos. No
Oceano Atlântico Sul, mais especificamente na costa do sudeste do Brasil,
aumentou nos últimos anos a exploração de petróleo do pré-sal, tornando-se mais
relevante conhecer os extremos de vento que afetam a região. Os sistemas
transientes impactam na velocidade do vento próximo à superfície, conduzindo
muitas vezes a eventos extremos. Desta forma, o objetivo principal desta pesquisa é
investigar a relação entre intensidade e extremos de vento com os ciclones
subtropicais no leste do sudeste do Brasil. Inicialmente, apresenta-se uma estatística
descritiva das observações da velocidade de vento médio diário para nove estações
meteorológicas automáticas e cinco boias meteoceanográficas localizadas na costa
sudeste do Brasil. Estas observações locais são também usadas para validação das
reanálises CFSR e ERA5. Os resultados mostram que as localidades com maiores
correlações para a série temporal diária em relação as observações (entre 0,5 e 0,9)
em ambas as reanálises também representam os padrões de média anual e ciclo
anual para a velocidade do vento em maior concordância com as observações
locais. Na maioria das estações meteorológicas sobre o continente as reanálises
superestimam a velocidade, enquanto sobre o oceano subestimam. Considerando
todas as localidades, as duas reanálises mostram desempenho semelhante para
representar as observações locais. A relação entre ventos e os ciclones subropicais
(tanto para a intensidade como para extremos de vento, identificados com o percentil
de 95%) é investigada considerando a forma Lagrangeana, ou seja, seguindo os
centros dos ciclones, e Euleriana que considera apenas os horários com ciclones
subtropicais. Estas análises mostram que os ventos intensos situam-se
principalmente à leste da região com maior densidade de ciclones subtropicais. Em
termos sazonais, a maior intensidade do vento é observada no verão, seguido do
outono. Para extremos de velocidade encontra-se sazonalidade similar, porém com
algumas diferenças. No verão, enquanto os maiores valores de intensidade do vento
6

estão à leste da região de maior densidade de ciclones, nos extremos localizam-se
na própria região de maior densidade de ciclones. As maiores velocidades do vento
no verão são influenciadas pelo gradiente zonal de pressão climatológico e pelos
ciclones subtropicais. Por outro lado, no outono os ciclones subtropicais
representam a principal influência na intensidade dos extremos de vento, pois nesta
estação estes sistemas são mais intensos e organizados.
Palavras-chaves: Ciclone subtropical, vento próximo à superfície, extremo de vento,
intensidade do vento, Oceano Atlântico Sul.
7

Abstract
Cardoso, A. A, 2019: Subtropical cyclones and surface winds in the southwest of the
South Atlantic Ocean: Climatology and extremes. 110 pp. Dissertação de mestrado -
Instituto de Astronomia, Geofísica e Ciências Atmosféricas, Universidade de São
Paulo, São Paulo.
Wind speed is one of the weather variables that has a major impact on the economy
and society, especially in the occurrence of extreme events. In the South Atlantic
Ocean, more specifically on the southeastern coast of Brazil, the exploration of pre-
salt oil has increased in recent years, making it more relevant to know the wind
extremes that affect the region. Transient systems impact near-surface wind speeds,
often leading to extreme events. Thus, the main objective of this research is to
investigate the relationship between wind intensity and extremes with subtropical
cyclones in eastern of southeastern Brazil. Initially, a descriptive statistic of the mean
daily wind speed observations is presented for nine automatic weather stations and
five buoys located in the southeastern coast of Brazil. These local observations are
also used to validate of CFSR and ERA5 reanalyses. The results show that the
locations with the stronger correlations for the daily time series (between 0.5 and 0.9)
in both reanalyses also represent the annual mean and annual cycle patterns for
wind speed in greater agreement with local observations. In most weather stations on
the continent reanalyses overestimate speed, while over the ocean they
underestimate it. Considering all localities, both reanalyses show similar performance
to represent local observations. The relationship between winds and subtropical
cyclones (both for intensity and wind extremes, identified with the 95% percentile) is
investigated considering the Lagrangean form, i.e., following the centers of the
cyclones, and the Eulerian one, which considers only the timesteps with subtropical
cyclones. These analyses show that strong winds are mainly to the east of the region
with the highest density of subtropical cyclones. In seasonal terms, the highest wind
intensity is observed in summer, followed by autumn. For wind extremes there is
similar seasonality, but with some differences. In summer, while the highest wind
intensity values are to the east of the highest cyclone density region, at the extremes
they are located in the region of greater cyclone density. Higher wind speeds in
summer are influenced by the climatologic zonal gradient of pressure and subtropical
cyclones. On the other hand, in autumn, subtropical cyclone represent the major
8

influence on wind extremes, since in this season these systems are more intense
and organized.
Keywords: Subtropical cyclone, wind near the surface, wind extreme, wind speed,
South Atlantic Ocean.
9

LISTA DE FIGURAS
Figura 1. Linhas de fluxo em um ciclone extratropical em movimento. Fonte:
BJERKNES (1919). ................................................................................................... 22
Figura 2. Climatologia da: (a) Distribuição anual absoluta de ciclogêneses. Fonte:
GAN e RAO (1991); (b) densidade de ciclogêneses (1990 a 1999), que se iniciaram
com vorticidade ciclônica ζ ≤ -1,5x10-5 s -1 (parte superior) e com ζ ≤ -2,5x10-5 s -1
(parte inferior) Fonte: REBOITA (2008). .................................................................... 23
Figura 3. Imagem visível de alta resolução (1 km) do instrumento Moderate
Resolution Imaging Spectroradiometer (MODIS) montado no satélite Terra para
13:55 UTC 27 de março de 2004. (b) velocidade do vento derivado da Missão
Tropical de Medição de Precipitação (TRMM). Fonte: COWAN et al., (2006)........... 27
Figura 4. (a) Distribuição sazonal de ocorrências dos ciclones subtropicais no
Atlântico Sul (preto) e Atlântico Norte (branco). Fonte: EVANS e BRAUN (2012). (b)
Média sazonal (barras) e porcentagem de ciclones subtropicais em relação ao total
de ciclones sobre a RG1. Fonte: GOZZO et al. (2014). ............................................ 29
Figura 5. Ciclogênese e ciclólise subtropical (número de ciclones por radiano
quadrado por dia) para (a), (c) NCEP1 e (b), (d) ERAInt. Fonte: GOZZO et al. (2014).
.................................................................................................................................. 30
Figura 6. (a) Modelo conceitual de Cowan et al. (2006) em que em altos níveis da
atmosfera há um bloqueio do tipo dipolo no Hemisfério Sul. (b) Modelo conceitual
adaptado de Holland et al. (1987) para o hemisfério Sul. ......................................... 31
Figura 7. Região da maior concentração dos ciclones subtropicais (RG1) (retângulo
roxo) e localização das estações meteorológicas (pontos vermelhos) e boias
meteoceanográficas (quadrados azuis). ................................................................... 35
Figura 8. Intensidade do vento correspondente ao percentil de 95% de velocidade
do vento (sombreado, ms-1) para cada ponto de grade para as duas reanálises (a)
CFSR e (b) ERA5. A RG1 é indicada pelo retângulo preto. ...................................... 43
Figura 9. Exemplo de extremos de velocidade do vento a 10 m (sombreado, em m s-
1) e o box de 20 º x 20 º (retângulo preto) utilizado em relação ao ponto central do
10

ciclone (ponto laranja) e o retângulo vermelho indica a RG1 para a data 04-03-2010
06 UTC. ..................................................................................................................... 44
Figura 10. Exemplo de vento a 10 m acumulado m s-1 para o ciclo de vida do ciclone
subtropical Anita. ....................................................................................................... 47
Figura 11. Climatologias (2008-2017, exceto em São Sebastião que engloba 2014-
2017) da rajada do vento diário (m s-1) observada em diferentes estações
meteorológicas: (a) Média anual e (b) Ciclo anual. ................................................... 49
Figura 12. Climatologias (2008-2017, exceto em São Sebastião que engloba 2014-
2017) da velocidade do vento diário (m s-1) observada em diferentes estações
meteorológicas para a média anual: (a) Observado, (b) CFSR e (c) ERA5. ............. 52
Figura 13. Climatologias (2008-2017, exceto em São Sebastião que engloba 2014-
2017) da velocidade do vento (m s-1) das reanálises interpoladas para as estações
para o ciclo anual: (a) Observado; (b) CSFR e (c) ERA5. ......................................... 53
Figura 14. Diagrama de Taylor para as séries temporais (período 2008-2017, exceto
em São Sebastião que se refere ao período 2014-2017) da velocidade do vento
média diária, onde: estão indicados valores para estação (círculo preto), ERA5
(ponto verde) e CFSR (ponto rosa): (a) Iguape, (b) Itapoá, (c) Macaé, (d) Alfredo
Chaves, (e) Parati, (f) Ilha do Mel, (g) Arraial do Cabo, (h) Florianópolis e (i) São
Sebastião. As linhas indicam: raiz do erro quadrático médio (linha contínua dourada),
desvio padrão (linha pontilhada azul) e coeficiente de correlação (linha pontilhada
preta). O desvio padrão para referência, ou seja, desvio padrão da estação (linha
contínua preta). ......................................................................................................... 56
Figura 15. Climatologias da velocidade do vento (m s-1) das boias
meteoceanográficas para o ciclo anual: (a) Observação, (b) CFSR e (c) ERA5. ...... 60
Figura 16. Climatologias da velocidade do vento (m s-1) das reanálises interpoladas
para as boias meteoceanográficas para a média anual: (a) Observação, (b) CFSR e
(c) ERA5. As séries para a média anual indicam o período disponível para obter as
climatologias nas estações........................................................................................ 61
Figura 17. Diagrama de Taylor para as séries temporais da velocidade do vento
média diária das boias meteoceanograficas, onde: estão indicados valores para
estação (círculo preto), ERA5 (ponto verde) e CFSR (ponto rosa): (a) Santos, (b)
11

Itajaí, (c) Vitória, (d) Niterói e (e) Cabo Frio. As linhas indicam: raiz do erro
quadrático médio (linha contínua dourada), desvio padrão (linha pontilhada azul) e
coeficiente de correlação (linha pontilhada preta). O desvio padrão para referência,
ou seja, desvio padrão da estação (linha contínua preta). ........................................ 62
Figura 18. Climatologia sazonal, para 1979-2015, da magnitude (sombreado, m s-1)
e direção do vento (vetores) a 10 m de altura para às reanálises CFSR (lado direito)
e ERA5 (lado esquerdo): (a) verão, (b) outono, (c) inverno, (d) primavera. Em
destaque a RG1 (retângulo em preto). ...................................................................... 68
Figura 19. Quantidade de ciclones subtropicais por estação do ano que se formaram
no SAO no período 1979-2015. ................................................................................. 69
Figura 20. Série temporal da frequência anual (absoluta) de ciclones subtropicais
que se formaram no SAO no período 1979-2015. ..................................................... 70
Figura 21. Densidade anual das trajetórias de ciclones subtropicais para o período
1979-2015. A densidade considera o número de ciclones dividido pela área. RG1 é
identificada pelo retângulo preto. .............................................................................. 71
Figura 22. Densidade sazonal das trajetórias dos ciclones subtropicais para o
período 1979-2015: (a) verão, (b) outono, (c) inverno, (d) primavera. A densidade
considera o número de ciclones dividido pela área para. RG1 é identificada pelo
retângulo preto. ......................................................................................................... 72
Figura 23. Intensidade média sazonal do vento a 10 m (sombreado, m s-1) para os
dias com ciclones tropicais no SAO no período 1979-2015 para: (a) CFSR, (b)
ERA5. RG1 está indicada pelo retângulo preto. ........................................................ 73
Figura 24. Anomalia de velocidade do vento (sombreado, m s-1) para os dias com
ciclones subtropicais (referencial Euleriano) para: (a) CFSR, (b) ERA5. A anomalia é
calculada como a diferença entre as composições para dias com ciclones e a
climatologia da intensidade do vento. RG1 indicada pelo retângulo preto. ............... 75
Figura 25. Anomalia da velocidade (sombreado, m s-1) seguindo a trajetória dos
ciclones subtropicais (referencial Lagrangeano) para: (a) CFSR, (b) ERA5. Anomalia
calculada considerando a velocidade acumulada dividida pela quantidade de vezes
que passou no mesmo lugar seguindo o centro do ciclone e climatologia. RG1
indicada pelo retângulo preto. ................................................................................... 77
12

Figura 26. Velocidade acumulada (sombreado, m s-1) seguindo o centro do ciclone
para: (a) CFSR, (b) ERA5. RG1 indicada pelo retângulo preto. ................................ 79
Figura 27. Distribuição espacial dos eventos extremos (percentil de 95%) da
magnitude do vento a 10 m (m s-1) para a reanálise CFSR: (a) média, (b) máximo.
Em destaque a RG1 (retângulo preto). ..................................................................... 81
Figura 28. Boxplot da série temporal (1979-2015) de velocidade do vento a 10 m
(m/s) máximo extraída seguindo a trajetória do ciclone para ERA5 (verde) e CFSR
(rosa) para: (a) verão, (b) outono, (c) inverno, (d) primavera. ................................... 83
Figura 29. Boxplot da série temporal de todos os pontos de grade excedendo o
percentil de 95% de velocidade do vento (m s-1) a 10m extraída seguindo as
trajetórias dos ciclones para a ERA5 (boxplot verde) e CFSR (boxplot rosa): (a)
verão, (b) outono, (c) inverno, (b) primavera. ............................................................ 85
Figura 30. Média anual para as velocidades máximas (linhas contínuas) e extremos
(acima do percentil de 95%; linhas tracejadas) do vento em 10 m a cada 6 hora no
box de 20º x 20º seguindo os centros dos ciclones subtropicais para a ERA5 (verde)
e CFSR (rosa). .......................................................................................................... 86
Figura 31. Anomalia sazonal de velocidade do vento a 10 m considerando os
extremos de velocidade nos dias de ciclones subtropicais menos a climatologia de
extremos de velocidade (sombreado, m s-1): (a) CFSR, (b) ERA5. RG1 indicada pelo
retângulo preto. ......................................................................................................... 87
Figura 32. Anomalia dos extremos de velocidade (sombreado, m s-1) ao longo das
trajetórias dos ciclones: (a) CFSR, (b) ERA5. A anomalia representa a diferença
entre velocidade dos extremos acumulados dividida pela quantidade de vezes que
os ciclones passaram no mesmo lugar seguindo as trajetórias e a climatologia dos
extremos. RG1 indicada pelo retângulo preto. .......................................................... 90
Figura 33. Extremos de velocidade acumulada (sombreado, m s-1) seguindo a
trajetória dos ciclones subtropicais para: (a) CFSR, (b) ERA5. RG1 indicada pelo
retângulo preto. ......................................................................................................... 92
Figura 34. Histograma de frequência da distância entre os extremos e o centro do
ciclone subtropical. (a) CFSR e (b) ERA5. ................................................................ 93
13

Figura 35. Boxplot da pressão central (hPa) seguindo a trajetória dos ciclones
subtropicais. .............................................................................................................. 94
Figura 36. Composições da velocidade do vento a 10 m (sombreado, m s-1) e
Pressão ao Nível Médio do Mar (PNMM, contorno, hPa) na gênese (00 h), +12 h, +
24 h e + 36h (a) para o verão e (b) outono. RG1 (retângulo preto). .......................... 96
Figura 37. Boxplot da série temporal dos valores máximos dos fluxos (soma de calor
latente e sensível em W m-2) extraídos seguindo a trajetória dos ciclones
subtropicais da reanálise CFSR (período 1979-2015). ............................................. 97
Figura 38. Composições dos fluxos de calor latente e sensível (latente + sensível)
(sombreado, W m-2) para os ciclones subtropicais, na gênese (00 h), +12 h, + 24 h e
+ 36h (a) para o verão e (b) outono. RG1 (retângulo preto) ...................................... 99
14

LISTA DE TABELAS
Tabela 1. Nomes, localizações e período de dados das estações meteorológicas
automáticas. .............................................................................................................. 33
Tabela 2. Nome, localizações e período de dados das boias meteoceanográficas. . 34
Tabela 3. Porcentagem de existência de dados observados no período considerado.
.................................................................................................................................. 36
Tabela 4. Média e correlação (entre parênteses) para o ciclo anual entre
observações (estações meteorológicas automáticas) e reanálises (ERA5 E CFSR).
.................................................................................................................................. 65
Tabela 5. Média e correlação (entre parênteses) para o ciclo anual entre
observações (boias meteoceanográficas) e reanálises (ERA5 E CFSR). ................. 66
Tabela 6. Médias sazonais das intensidades (m s-1) máximas e extremos (acima do
percentil de 95%) do vento seguindo a trajetória dos ciclones subtropicais e
correlações entre o CFSR e ERA5 para estas séries. Valores em parênteses são
para os extremos de velocidade. ............................................................................... 85
15

LISTA DE ABREVIATURAS E SIGLAS
ASAS - Alta Subtropical do Atlântico Sul
CEMIG - Companhia de Energia de Minas Gerais
CFSR - Climate Forecast System Reanalysis
CISK - Conditional Instability of the Second Kind
CPS – Cyclone Phase Space
CS - Ciclone Subtropical
ECMWF - Europen Centre for Medium-Range Weather Forecasts
INMET - Instituto Nacional de Meteorologia
PNMM - Pressão ao Nível Médio do Mar
RMSE - Raiz do Erro Quadratico Médio
SAO - Oceano do Atlântico Sul
TSM – Temperatura da Superfície do Mar
WISHE - Wind Induced Surface Heat Exchange
WMO - World Meteorological Organization
ZCAS - Zona de Convergência do Atlântico Sul
16

SUMÁRIO
1. INTRODUÇÃO.............................................................................................................. 18
1.1.1. Objetivos ........................................................................................................ 20
1.1.2. Objetivos Específicos ..................................................................................... 21
1.2. Revisão Bibliográfica ............................................................................................. 21
1.2.1 Ciclones extratropicais .................................................................................... 21
1.2.2 Ciclones tropicais ........................................................................................... 24
1.2.3 Ciclones subtropicais ...................................................................................... 27
2. DADOS E METODOLOGIA .......................................................................................... 32
2.1. Dados .................................................................................................................... 32
2.2. Métodos ................................................................................................................. 37
2.2.1. Comparação reanálises e observações locais ................................................ 37
2.2.2. Rastreamento de ciclones .............................................................................. 38
2.2.3. Critério para obtenção dos extremos de ventos .............................................. 42
2.2.4. Associação entre extremos e ciclones ............................................................ 43
2.2.5. Climatologia .................................................................................................... 44
2.2.6. Série temporal seguindo o centro do ciclone .................................................. 45
2.2.7. Distância do centro do ciclone e extremos de vento ....................................... 45
2.2.8. Vento acumulado ............................................................................................ 46
3. RESULTADOS ............................................................................................................. 48
3.1. Velocidade do vento: Observações locais e reanálises ......................................... 48
3.1.1. Comparação com outros trabalhos. ................................................................ 63
3.2. Climatologia sazonal do vento a 10 m de altura ..................................................... 66
3.3. Climatologia de ciclones subtropicais .................................................................... 68
3.4. Ciclones subtropicais e vento a 10 m..................................................................... 72
3.5. Extremos da intensidade do vento ......................................................................... 79
3.6. Composições ......................................................................................................... 94
4. CONCLUSÕES........................................................................................................... 100
5. PROPOSTAS PARA TRABALHOS FUTUROS .......................................................... 103
REFERÊNCIAS BIBLIOGRÁFICAS ................................................................................... 104
17

1. INTRODUÇÃO
Os ventos são fundamentais para a manutenção do sistema climático e
estão associados ao aquecimento diferencial em diversas escalas temporais e
espaciais, desde a planetária, onde o equador é mais aquecido do que o polo, até
circulações locais de brisas (ar-mar e vale-montanha). O aproveitamento do vento
também como fonte de energia renovável tem aumentado nos últimos anos, através
da instalação de fazendas eólicas em várias partes do mundo. Além disso, os ventos
intensos podem causar impactos em setores economicamente importantes, por
exemplo, indústria portuária, pesqueira, plataforma oceânica de extração do
petróleo, por esta razão, despertam grande interesse no meio científico.
Na maioria das vezes que ocorrem ventos intensos, rajadas e extremos
são provocados por sistemas sinóticos e, tendo em vista este conhecimento prévio é
importante buscar a associação dos extremos com estes fenômenos.
Bitencourt et al. (2011) relacionaram a intensidade de ventos de estações
meteorológicas com as posições dos ciclones extratropicais na costa sudeste do
Brasil. Suas análises mostraram duas características importantes. A primeira
apresenta que os ventos são significativamente relacionados com ciclones
extratropicais apenas em regiões mais extratropicais (ao sul de 28 ºS) com exceção,
apenas uma estação mais ao norte (próximo de 27 ºS). A segunda relação condiz
com a distância mínima entre o ciclone e a costa para ele exercer alguma influência
nos ventos. Bitencount et al. (2011) constataram que as observações nas estações
próximas a 28 ºS mostram alguma associação com ciclones mais afastados da costa
(1200 km), mas não para ciclones mais próximos à costa (0 - 300 km).
Extremos da intensidade do vento sobre o oeste do Oceano Atlântico Sul
(SAO) foram estudados por Silva (2013), utilizando a técnica de análise Peaks Over
Threshold e sua relação com os sistemas sinóticos ao longo do Oceano, levando em
consideração diferentes direções do vento (quadrantes). Esta análise mostrou uma
grande variação de fenômenos com capacidade de produzir extremos para cada
quadrante do vento considerado. Na região sul do Brasil, Silva (2013) conclui que a
Alta Subtropical do Atlântico Sul (ASAS) influencia uma grande região espacial, uma
vez que possui uma maior amplitude espacial e sua persistência é constante na
região. Os extremos de ventos predominantes dos quadrantes norte e nordeste na
região costeira do sudeste do Brasil relacionaram-se com a ASAS. A aproximação
18

de um anticiclone pós-frontal pode intensificar os ventos do quadrante de nordeste e
constituir extremos para este quadrante.
Outros autores relacionaram quadrantes de ventos com sistemas
sinóticos na região de estudo. Oliveira e Quaresma (2018) caracterizaram os ventos
na costa do Espírito Santo com os cenários típicos sob atuação da ASAS, sistemas
transientes (sistemas frontais e ciclones) e Zona de Convergência do Atlântico Sul
(ZCAS). Seus resultados mostram que os eventos mais intensos ocorrem sob a ação
dos sistemas transientes, enquanto eventos menos intensos sob a ação da ASAS.
Em período de ZCAS, os ventos de sul, sudeste e sudoeste são predominantes,
enquanto ventos de norte, nordeste e leste são mais frequentes nos períodos de pré
e pós ZCAS. Dereczynski et al. (2019) estudaram os ventos em superfície com os
dados obtidos pela plataforma Floating, Production, Storage and Offloading-Brazil
operada pela Petrobrás durante o período de 2004-2013, localizada na costa do
Espírito Santo. Os resultados mostraram que os ventos são predominantes nos
quadrantes nordeste, norte e leste durante o ano. Os autores observaram que a
velocidade média do vento nesta região, depende da posição da ASAS, pois
influencia no gradiente de pressão.
Para seis casos de ciclones subtropicais no SAO, Reboita et al. (2019)
relacionaram vento e precipitação ao longo da trajetória destes sistemas. Os autores
encontraram chuvas intensas próximo da costa sul/sudeste do Brasil, na maior parte
dos eventos, a quantidade de chuva no período de vida dos ciclones superou a
climatologia. Além disso, foram observados ventos intensos ao longo do ciclo de
vida dos ciclones, com intensidade do vento em 925 hPa (ventos sustentados)
excedendo 17 m s-1 durante um longo período dos ciclos de vida.
Os ciclones subtropicais, em particular, atuam na costa sudeste do Brasil
e impactam na região costeira, implicando em ventos e chuvas intensas. Apesar
disso, é um fenômeno pouco estudado nesta região, contando até o momento com
apenas duas climatologias e poucos trabalhos que os relacionam com variáveis
meteorológicas associadas à danos na costa e continente. Os estudos sobre os
ciclones subtropicais aumentaram após o episódio do furacão Catarina. O ciclone
sofreu transição entre as fases extratropicais, subtropicais e, depois se tornando um
furacão. A partir desse episódio, alguns trabalhos visam entender melhor o furacão
e, consequentemente os processos transição na costa sudeste do Brasil
(MCTAGGART-COWAN et al., 2006) e a habilidade de simulações numéricas
19

reproduzirem este fenômeno (da SILVA, 2014 e GOZZO et al., 2017). O primeiro
ciclone subtropical estudado no Brasil foi o Anita (DUTRA, 2012, ABREU e da
ROCHA, 2015, DIAS PINTO et al., 2013, DUTRA et al., 2017 e REBOITA et al.,
2017a, b) que ocorreu em 2010 e motivou o rastreamento e identificação de ciclones
subtropicais no Atlântico Sul para obter a climatologia destes sistemas (EVANS E
BRAUN, 2012 e GOZZO et al., 2014).
Uma grande motivação para estudar ciclones subtropicais é sua estrutura
híbrida, pois há características dos ciclones extratropicais e tropicais adicionando
complexidade na sua identificação. Os processos de formação também apresentam
características diferentes em função do Hemisfério e/ou bacias oceânicos por isso,
estudá-los em cada região de ciclogênese é de extrema importância.
O grande diferencial desta pesquisa é a relação dos ventos com os
ciclones, até o momento não havia uma climatologia para entender esta relação.
Além disso, os ciclones subtropicais causam grande impacto na costa, favorecendo
ventos intensos, por esta razão, é de extrema importância entender como os ventos
se comportam na presença destes sistemas.
1.1.1. Objetivos
O principal objetivo desta pesquisa é relacionar os extremos e máximos
de velocidade do vento próximo à superfície com ciclones subtropicais no Oceano
Atlântico Sul, principalmente na costa do Brasil, região de maior densidade destes
sistemas. Esta relação será feita considerando apenas os dias com estes sistemas
(análise Euleriana) e, também seguindo a trajetória dos mesmos (análise
Lagrangeana). O segundo objetivo é entender o comportamento do vento
(velocidade média e rajada) na costa através de dados observacionais de estações
meteorológicas e boias meteoceanográficas; além de avaliar a habilidade da
reanálise de alta resolução espacial em reproduzir o dado observado.
20

1.1.2. Objetivos Específicos
• Analisar a velocidade do vento observado na região costeira do sudeste do
Brasil;
• Avaliar habilidade das reanálises ERA5 e CFSR em reproduzir a climatologia
observada da velocidade do vento;
• Aplicar um limiar para os extremos;
• Analisar os extremos de ventos considerando a série temporal a cada 6h para
as duas reanálises (CFSR e ERA5);
• Analisar os extremos da velocidade do vento associados aos ciclones
subtropicais considerando apenas as datas de ocorrência dos mesmos
(análise Euleriana);
• Analisar eventos extremos de velocidade do vento associados aos ciclones
subtropicais ao longo da trajetória dos mesmos (análise Lagrangeana).
1.2. Revisão Bibliográfica
Este capítulo apresenta uma revisão bibliográfica sobre as três principais
fases que os ciclones de escala sinótica podem sofrer transição ao redor do globo.
Descrevendo os processos de formação, estrutura vertical e climatologia. A revisão
apresenta uma ênfase maior na América do Sul e Oceano Atlântico Sul (SAO), pois
apresentam alta frequência de ciclones, com três regiões ciclogenéticas (REBOITA,
2008), (SINCLAIR, 1994 e 1996) e (HOSKINS E HODGES, 2005).
1.2.1 Ciclones extratropicais
Os primeiros estudos sobre ciclones extratropicais iniciaram-se no século
passado. Bjerknes (1919) começou estudar a estrutura dos ciclones em movimento
e os processos dinâmicos envolvidos utilizando dados de vento de estações
meteorológicas localizadas na Noruega, Suíça e Dinamarca. Nessa época ainda não
21

havia observação em níveis superiores e a distinção das diferentes categorias de
ciclones como hoje.
Figura 1. Linhas de fluxo em um ciclone extratropical em movimento. Fonte: BJERKNES
(1919).
Em seu estudo Bjerknes (1919) encontrou duas linhas de convergência,
denominadas de squall line e steering line (atualmente são chamadas de frente fria e
frente quente, respectivamente), sendo diferenciadas por suas propriedades
térmicas. A Figura 1 mostra o esquema proposto por Bjerknes com duas linhas de
convergência e a presença de setores quente e frio na região do ciclone
extratropical.
Posteriormente, Bjerknes e Solberg (1922) continuaram os estudos
mostrando avanços sobre a formação dos ciclones extratropicais. Então os autores,
apresentaram a teoria da frente polar e propuseram oito estágios para explicar o
ciclo de vida dos ciclones extratropicais. Além disso, mostraram que a fase inicial do
ciclone extratropical ocorre no encontro de duas linhas opostas com temperaturas
distintas, ou seja, uma linha fria (latitudes polares) e outra quente (latitudes
subtropicais).
O conceito teórico para ciclone extratropical elaborado por Bjerknes
(1919) e Bjerknes e Solberg (1922) foi bem aceito na época, no entanto, explicava a
formação dos ciclones apenas em superfície. Então Sutcliffe (1947) aprimorou a
descrição do processo de formação dos ciclones extratropicais não apenas em
22

superfície, mas também considerando observações em altos e médios níveis da
atmosfera.
Nas décadas seguintes, modelos conceituais de diferentes tipos de
ciclones de escala sinótica começaram a surgir com a ampliação das observações
como os de Pettersen e Smebye (1971); Radinovic (1985) e Shapiro e Keyser
(1990). Do ponto de vista dos mecanismos de desenvolvimento dinâmico dos
ciclones extratropicais, a instabilidade baroclínica surgiu em Charney (1947) e Eady
(1949). Em suma, atualmente os ciclones extratropicais são definidos como sistemas
que se formam em regiões de latitudes médias em função da presença de
instabilidade baroclínica, caracterizado pelo intenso cisalhamento vertical do vento
horizontal, diretamente associado ao gradiente horizontal de temperatura. As
circulações ciclônicas nestas regiões com contraste de temperatura formam as
frentes frias e quentes (BJERKNES e SOLBERG, 1922).
No entanto, a maioria dos trabalhos pioneiros que conceituaram ciclones
extratropicais consideraram sistemas no hemisfério Norte. No hemisfério Sul,
especificamente no Brasil, estudos sobre a climatologia e aplicação de métodos de
identificação destes sistemas começaram no final da década de 80.
a) b)
Figura 2. Climatologia da: (a) Distribuição anual absoluta de ciclogêneses. Fonte: GAN e
RAO (1991); (b) densidade de ciclogêneses (1990 a 1999), que se iniciaram com vorticidade
ciclônica ζ ≤ -1,5x10-5 s -1 (parte superior) e com ζ ≤ -2,5x10-5 s -1 (parte inferior) Fonte:
REBOITA (2008).
23

Gan e Rao (1991) elaboraram uma climatologia de ciclogêneses; os ciclones
foram identificados através da pressão ao nível médio do mar, ou seja, considerando
isóbaras fechadas. Os autores utilizaram 10 anos de cartas sinóticas (1979-1988) e,
encontraram duas regiões principais de formação de ciclones na América do Sul: na
Argentina (centrada em 42 ºS) e no Uruguai-Sul do Brasil (Figura 2a). Murray e
Simmonds (1991), também utilizaram a pressão ao nível médio do mar para
identificar as regiões ciclogenêticas próximas da Austrália.
Para o período de 1980-1986, Sinclair (1994) determinou a distribuição
espacial e temporal dos centros dos ciclones com duas análises por dia (00:00 e
12:00 UTC) em pontos de grade do ECMWF (Europen Centre for Medium-Range
Weather Forecasts). O autor utilizou a vorticidade relativa geostrófica, e encontrou
regiões ciclogenéticas nas proximidades da Antártica. Dois anos depois, Sinclair
(1996) elaborou um rastreamento automático de ciclones extratropicais
considerando vorticidade mínima relativa geostrófica em 14 anos de análises, e
encontrou regiões com formação e intensificação dos ciclones no hemisfério Sul. Em
particular, Sinclair (1996) identificou na América do Sul e SAO regiões com alta
frequência de desenvolvimento de ciclones. Reboita (2008) e Reboita et al. (2010a)
aplicaram um algoritmo para rastrear ciclones também utilizando mínimos de
vorticidade relativa, mas no vento real e não no geostrófico como em Sinclair (1996).
Aplicando o algoritmo no vento a 10 m de altura, Reboita et al. (2010a) mostraram
na climatologia entre 1990-1999 três regiões ciclogenéticas principais na costa leste
da América do Sul: sul/sudeste do Brasil, Bacia do Prata/Uruguai e sudeste da
Argentina (Figura 2b).
1.2.2 Ciclones tropicais
De acordo com Gray (1969), até meados dos anos 50 as análises de
níveis superiores eram muito escassas, devido à ausência de observações de ar
superior e de satélite. Com observações em níveis superiores, o fenômeno de
desenvolvimento de tempestade pôde ser melhor estudado, principalmente a
tempestade tropical, que se estende desde a superfície até níveis mais altos. Gray
(1969) definiu as tempestades tropicais como sistema com rotação ciclônica, baixa
pressão de núcleo quente, com ventos máximos sustentados (vento contínuo num
24

intervalo de tempo) de 35 nós (64,75 km/h) ou superior; furacões, tufões e ciclones
tropicais também estão nessa definição, utilizada pela WMO. Além disso, nestas
tempestades, o cisalhamento vertical do vento horizontal deve ser fraco para o
desenvolvimento dos sistemas.
Após uma década, Ooyama (1982) continuou os estudos sobre o
desenvolvimento dos ciclones tropicais. Ele propôs que: (a) a gênese do ciclone
tropical ocorre quando se detecta a circulação do vento de um ciclone tropical
incipiente; (b) o desenvolvimento ocorre na área de uma perturbação pré-existente
com atividade convectiva organizada. No seu estágio de desenvolvimento o sistema
tem um vórtice quase circular e núcleo quente ocupando toda a troposfera e com
centenas de quilômetros na horizontal; a região com nuvens e intensa precipitação
localiza-se na parede do “olho do furacão”, ou seja, nas bordas do centro da
tempestade. No seu estágio maduro o vórtice em rotação é simétrico em um estado
estacionário; além disso, neste estágio há uma corrente ascendente e precipitação
na borda do sistema (OOYAMA, 1982).
Charney e Eliassen (1964) propuseram que um ciclone tropical se
desenvolve de uma instabilidade secundária, denominada de Conditional Instability
of the Second Kind (CISK), na qual a convecção é maior em regiões de
convergência em baixos níveis, porém inexistente nas de divergência em baixos
níveis. De acordo com esta teoria, às nuvens são cooperantes com o ciclone,
fornecendo calor latente para seu desenvolvimento; a teoria propõe que a superfície
do oceano seria um sumidouro, e não uma fonte de calor. O spin-up para o
crescimento da perturbação dependeria da energia convectiva armazenada na
atmosfera. De acordo com Emanuel (1991) essa teoria é inconsistente, pois as
análises da atmosfera tropical marítima mostram pouca energia convectiva
armazenada, e outros locais que exibem maior quantidade de energia convectiva
armazenada não são conhecidos por produzirem ciclones incipientes. Mesmo sendo
uma teoria controversa, o CISK permaneceu popular por muito tempo, pois em sua
definição mostra que as nuvens cumulus e a circulação de grande escala cooperam
na manutenção do sistema. Porém, o CISK desconsidera inteiramente a importância
dos fluxos de calor latente vindo dos oceanos.
Então, Emanuel (1986 e 1991) propôs uma teoria alternativa que
considera a instabilidade da atmosfera tropical denominada de Wind Induced
Surface Heat Exchange (WISHE). Nesta teoria, o desenvolvimento do ciclone
25

tropical se dá em função do feedback positivo entre os fluxos de calor (latente e
sensível) do oceano para a atmosfera e o ciclone, ou seja, a temperatura do oceano
deve estar mais quente. Algumas décadas anteriores Palmén (1948) já indicava que
a Temperatura da Superfície do Mar (TSM) precisa exceder 26º C para formação do
sistema.
Após uma década, DeMaria et al., (2001) elaborou um parâmetro de
gênese para avaliar o potencial da formação de ciclones tropicais no Atlântico Norte,
entre a África e as Ilhas do Caribe. Este parâmetro é calculado como o produto do
cisalhamento vertical médio, instabilidade vertical e umidade de nível médio em
cinco dias consecutivos.
A literatura indicava que ciclones tropicais não ocorreriam na costa leste
da América do Sul, pois nesta região os sistemas não são favorecidos pelo intenso
cisalhamento vertical do vento horizontal e a alta TSM, por não exceder 26 °C. Por
esta razão, a formação do furacão Catarina, em março de 2004, surpreendeu
pesquisadores e previsores. Por ser um evento incomum, o sistema causou
impactos socioeconômicos em cidades costeiras despreparadas. Além disso, a
existência de um sistema tropical no sul do Oceano Atlântico Sul motiva uma análise
do seu desenvolvimento em regiões de cisalhamento vertical climatologicamente
grande. A Figura 3 mostra a imagem de satélite e o vento para furacão Catarina.
A existência do bloqueio atmosférico na média troposfera mostrou-se
importante para o desenvolvimento do furacão Catarina, pois este sistema
possibilitou regiões com fraco cisalhamento vertical do vento e fraca baroclinia. Esse
processo dinâmico foi fundamental para o sistema se desenvolver, pois são
candidatos ideais para a transição tropical. As características do escoamento foram
de extrema importância para o desenvolvimento do furacão Catarina, os jatos foram
divididos e a região de baixo cisalhamento vertical do vento situou-se entre o ramo
dos jatos (MCTAGGART-COWAN et al., 2006).
26

Figura 3. Imagem visível de alta resolução (1 km) do instrumento Moderate Resolution
Imaging Spectroradiometer (MODIS) montado no satélite Terra para 13:55 UTC 27 de março
de 2004. (b) velocidade do vento derivado da Missão Tropical de Medição de Precipitação
(TRMM). Fonte: MCTAGGART-COWAN et al., (2006).
Recentemente, entre 23-28 de março de 2019, foi observado outro evento
de tempestade tropical denominado de Iba, que se desenvolveu na costa leste, entre
o sudeste e nordeste do Brasil, mas não atingiu a classificação de furacão. No
entanto, este evento ocasionou bastante precipitação na região.
1.2.3 Ciclones subtropicais
Simpson (1952) começou estudar os ciclones subtropicais com maior
detalhes. Seus estudos se concentravam no Hawai, e era denominados de kona
storms. A estrutura das tempestades kona inicia-se com núcleo frio e os ventos e
chuvas mais intensas conforme se desenvolve distante do centro do ciclone.
Os CSs são circulações ciclônicas associados com baixa pressão, mas
diferente dos ciclones extratropicais, os CSs não estão associados com a presença
de um sistema frontal. A estrutura termodinâmica do núcleo do CS tem
características de ambos os ciclones (tropicais e extratropicais), ou seja, núcleo
27

quente em baixos níveis e frio em altos níveis, por esta razão é denominado de
híbrido (GOZZO et al., 2014).
De acordo com World Meteorological Organization (WMO) a definição
para os CSs é: um sistema de baixa pressão associada com uma circulação
ciclônica, sem associação com sistema frontal, e tem características tanto dos
ciclones extratropicais e tropicais. Estes sistemas têm uma organização de
convecção moderada a profunda, e uma proporção significativa de energia para sua
formação se resultam de fontes baroclínicas. Geralmente possuem núcleo frio em
altos níveis e quente em baixos (estrutura híbrida). Outra característica dos CSs são
os ventos máximos que ocorrem longe do centro do sistema (WMO, 2005).
Holland et al., (1987) estudaram o desenvolvimento dos CSs na costa
leste da Austrália, região com grande frequência destes sistemas, entre o período de
(1970-1985). Em seu estudo encontrou dois tipos de ciclones que ocorrem na
região: o primeiro possui escala espacial pequena, com desenvolvimento sobre o
continente e uma baixa frequência de ocorrência (cinco eventos em 16 anos). O
segundo possui desenvolvimento tipicamente rápido, ao todo durante o período
analisado, foram encontrados 12 casos, sendo mais frequente no inverno.
Na América do Sul, em especial na costa do Brasil, publicações iniciais
sobre o CSs começaram em 2012. Evans e Braun (2012) fizeram a primeira
climatologia dos CSs na costa brasileira. Esse estudo encontrou 63 eventos entre
1957-2007; a estação com mais eventos foi o outono. O trabalho de Evans e Braun
(2012) compara as frequências de CSs entre o Oceano Atlântico Sul e Norte
apresentada na Figura 4. Nota-se maior quantidade de eventos por estação do ano
Atlântico Norte, também diferenças de sazonalidade.
Gozzo et al. (2014) fizeram uma climatologia, utilizando outro
rastreamento de ciclones e modificou alguns critérios para incluir sistemas rasos. No
período desta climatologia, de 1979-2011, encontrou uma média e desvio padrão de
7 ± 3 eventos por ano, com maior frequência de ciclogenese e ciclólise próximo da
costa sudeste do Brasil (Figura 5).
28

b)
a)
Figura 4. (a) Distribuição sazonal de ocorrências dos ciclones subtropicais no Atlântico Sul
(preto) e Atlântico Norte (branco). Fonte: EVANS e BRAUN (2012). (b) Média sazonal
(barras) e porcentagem de ciclones subtropicais em relação ao total de ciclones sobre a
RG1. Fonte: GOZZO et al. (2014).
Em Gozzo et al (2014), a climatologia de 1979-2011 apresenta a média
sazonal mostrada na Figura 4b, ou seja, maior frequência de CSs no verão seguido
do outono.
Os CSs formam-se na presença de um cavado ou uma baixa desprendida
(cutoff low) em médios-altos níveis da atmosfera (HOLLAND et al., 1987;
MCTAGGART-COWAN et al., 2006; GOZZO et al., 2014, REBOITA et al., 2017a e da
ROCHA et al., 2019 (Figura 6). Além disso, é necessária uma perturbação ciclônica
pré-existente em superfície para sua formação, porém seu desenvolvimento só
ocorre na presença de convecção. A convecção se mantém, enquanto o núcleo
estiver quente em baixos níveis, porém diferentemente do ciclone tropical, o núcleo
é quente apenas em baixos níveis, por isso a convecção não pode ser mantida
apenas pela circulação e fluxos de calor do oceano, precisando também de
processos dinâmicos. O padrão de bloqueio do tipo Rex é o processo dinâmico que
dá suporte para o desenvolvimento deste sistema. Gozzo (2014), através de
composições, encontrou dois tipos de formação de CSs na região do SAO. As
composições mostraram que a ciclogênese subtropical na RG1 (Região com maior
ciclogênese subtropical como mostra na Figura 5), estaria associada principalmente
com um padrão de bloqueio do tipo Rex na alta troposfera, baixa desprendida em
500 hPa e adveção quente em baixos níveis.
29

a) b)
c) d)
Figura 5. Ciclogênese e ciclólise subtropical (número de ciclones por radiano quadrado por
dia) para (a), (c) NCEP1 e (b), (d) ERAInt. Fonte: GOZZO et al. (2014).
30

a) b)
Figura 6. (a) Modelo conceitual de Mctaggart-Cowan et al. (2006) em que em altos níveis da
atmosfera há um bloqueio do tipo dipolo no Hemisfério Sul. (b) Modelo conceitual adaptado
de Holland et al. (1987) para o hemisfério Sul.
31

2. DADOS E METODOLOGIA
2.1. Dados
A análise de vento a 10 m de altura e ciclones subtropicais está dividida
em duas partes, a primeira utilizando observações locais e a segunda, reanálises.
As observações locais são compostas de estações meteorológicas
automáticas e boias meteoceanográficas. Ao todo foram utilizadas nove estações
meteorológicas e cinco boias na região da costa sul/sudeste do Brasil conforme
indicadas na Figura 7. A localização (latitude/longitude) e altitude de cada estação
estão nas Tabelas 1 e 2.
Das 9 estações meteorológicas utilizadas, oito foram fornecidas pelo
Instituto Nacional de Meteorologia (INMET) e uma pelo CEBIMar/USP
http://cebimar.usp.br/pt/o-que-oferecemos/estacoes-meteorologicas/estacao
meteorologica-do-cebimar-usp). As boias foram disponibilizadas pelo PNBOIA –
Centro de Hidrografia da Marinha https://www.marinha.mil.br/chm/dados-do-goos-
brasil/pnboia-mapa.
As datas iniciais das observações nas estações e boias estão indicadas
nas Tabelas 1 e 2, praticamente todas terminam no dia 31/12/2017, exceto Cabo
Frio antiga que termina em 2013. As observações das estações e boias
correspondem à valores diários.
Os dados de reanálise de ventos em superfície (vento a 10 m de altura)
utilizados para comparar com as trajetórias dos ciclones subtropicais e encontrar os
extremos, são do: (a) Climate Forecast System Reanalysis (CFSR) (SAHA el al.,
2010a) para o período de 1979-2010 e Climate Forecast System Reanalysis Version
2 (CFSV2) (SAHA et al., 2014b) para o período de 2011-2017. Estas duas versões
do CFSR fornecem dados a cada 6 horas em pontos de grade espaçados em 0,5 x
0,5 graus de latitude-longitude; (b) European Center for Medium-Range Weather
Forecast - Copernicus Climate Change Service (ECMWF-C3S), conhecido como
ERA5, que sucedeu ao ERA-Interim (HERSBACH e DEE, 2016). O período de
estudo corresponde à 1979-2015, com dados a cada 6 horas em pontos de grade de
0,25º x 0,25º graus de latitude-longitude. Os dados do ERA5 são fornecidos a cada
hora, no entanto para o presente trabalho foram utilizados apenas os horários das
00:00, 06:00, 12:00 e 18:00 UTC. Na reanálise CFSR os dados de vento a 10 m de
32

altura são obtidos de previsões de curto prazo (+3 horas), ou seja, 03:00, 09:00,
15:00,  21:00  +03:00  h,  foram  considerados  como  horários  sinóticos  (00:00,
06:00,12:00 e 18:00 UTC).

Tabela 1. Nomes, localizações e período de dados das estações meteorológicas
automáticas.

| Cidade  |     | Latitude  | Longitude  | Altitude (m)  | Início  | do  |
| ------- | --- | --------- | ---------- | ------------- | ------- | --- |
período
| Alfredo Chaves  |           | 20°38'S     | 40°44'W  | 35  | 01/01/2008  |     |
| --------------- | --------- | ----------- | -------- | --- | ----------- | --- |
| Arraial         | do  Cabo  | -  22°58'S  | 42°00'W  | 4   | 01/01/2008  |     |
RJ
| Florianópolis - SC  |        | 27°36'S  | 48°36'W  | 1,8  | 01/01/2008  |     |
| ------------------- | ------ | -------- | -------- | ---- | ----------- | --- |
| Iguape              | -  SP  | 24º42’S  | 47º33’W  | 1    | 01/01/2008  |     |
(INMET)
| Ilha  do  | Mel  -  PR  | 25º29’S   | 48º19’W  | 2   | 01/01/2008  |     |
| --------- | ----------- | --------- | -------- | --- | ----------- | --- |
(INMET)
| Itapoá  | -  SC  | 26º04’S  | 48º38’   | 3   | 01/01/2008  |     |
| ------- | ------ | -------- | -------- | --- | ----------- | --- |
(INMET)
| Macaé           |           | 22°23'S       | 41°49'W     | 32  | 01/01/2008  |     |
| --------------- | --------- | ------------- | ----------- | --- | ----------- | --- |
| Parati - RJ     |           | 23°13'S       | 44°43'W     | 4   | 01/01/2008  |     |
| São  Sebastião  |           | -  23º49’25S  | 45º25’18W   | 20  | 01/01/2014  |     |
| SP              | (CEBIMar- |               |             |     |             |     |
USP)

33

Tabela 2. Nome, localizações e período de dados das boias meteoceanográficas.

| Cidade  | Latitude  | Longitude  | Altitude (m)  | Início  | do  |
| ------- | --------- | ---------- | ------------- | ------- | --- |
período
| Cabo  frio  | -  RJ  22°  | 42° 06,00' W  | 4   | 24/06/2009  |     |
| ----------- | ----------- | ------------- | --- | ----------- | --- |
Antiga  58,80'S
| Itajaí - SC          | 27°24,35'S  | 47°15,93'W  | -   | 23/04/2009  |     |
| -------------------- | ----------- | ----------- | --- | ----------- | --- |
| Niterói - RJ Antiga  | 22°55,21'S  | 43°08,27'   | 1   | 05/09/2014  |     |
| Santos - SP          | 25°26,37'S  | 45°02,17'W  | 20  | 12/04/2011  |     |
| Vitória - ES         | 19°55,57'S  | 39°41,48'W  | 32  | 13/10/2015  |     |
|                      |             |             |     |             |     |

34

Figura 7. Região da maior concentração dos ciclones subtropicais (RG1) (retângulo roxo) e
localização das estações meteorológicas (pontos vermelhos) e boias meteoceanográficas
(quadrados azuis).
35

Tabela 3. Porcentagem de existência de dados observados no período considerado.
Porcentagem de dados (%)
Macaé 95,89
Florianópolis 99,92
Alfredo chaves 97,67
Arraial do Cabo 97,1
Parati 97,89
Iguape 93,87
Itapoá 95,05
Ilha do Mel 85,79
São Sebastião 94,32
Cabo Frio 25,94
Vitória 77,98
Santos 92,11
Niterói 50
Itajaí 64,92
36

2.2. Métodos
2.2.1. Comparação reanálises e observações locais
As estações meteorológicas e boias meteoceanográficas foram utilizadas
para duas finalidades. A primeira, para obter uma climatologia da velocidade do
vento na costa leste do Brasil, que é a região de estudo (Figura 7). A segunda, para
comparar os dados observados e validar com a reanálise ERA5 e CFSR. Para isso,
foram calculadas médias anuais e o ciclo anual médio, para entender a climatologia
do vento na costa e avaliar a habilidade das reanálises em reproduzir o padrão do
observado.
Na validação das reanálises extraiu-se uma série temporal considerando
uma média em uma caixa 1º x 1º centrada na latitude e longitude da estação
meteorológica. O motivo para usar este método deve-se ao fato de que a série
temporal extraída considerando o ponto mais próximo da estação fornece baixas
correlações, comparado com a série temporal resultante da média na caixa.
No caso das boias meteoceanográficas, cada uma estão em períodos
diferentes, Cabo Frio antiga (2010-2013), Itajaí (2011-2017), Niterói antiga (2015-
2017), Santos (2012-2017) e Vitória (2016-2017). Além disso, as boias estão em mar
aberto, as posições variam, o que implica na extração da série temporal
considerando o mínimo e máximo da latitude e longitude. Com esta informação
constrói-se a caixa para cada boia.
A Tabela 3 mostra a porcentagem dos dados disponíveis para todo o
período utilizado no trabalho, e permite estimar se existe muitos dados faltantes. No
caso das estações meteorológicas, na maioria delas, a porcentagem é maior que
90%, diferentemente das boias que em alguns casos (Cabo Frio antiga) possui
apenas 25% dos dados no período. Portanto, isso pode comprometer algumas
conclusões, por esta razão é necessário conhecer a informação sobre a
percentagem de dados.
O objetivo inicial na validação de modelos de fenômenos atmosféricos é
determinar se o padrão simulado se assemelha ao observado. Taylor (2001)
elaborou um diagrama que fornece um resumo estatístico conciso através da
combinação em termos de correlação, raiz do erro quadrático médio (RMSE) e
desvio padrão. Esse diagrama é denominado de diagrama de Taylor.
37

O coeficiente de correlação (R) entre as duas variáveis (f  e r ) é definido
n n
como:
|     | 1 ∑𝑁 (𝑓𝑛−𝑓)(𝑟𝑛−𝑟) |       |         |
| --- | ----------------- | ----- | ------- |
|     | 𝑅 =               |       |    (1)  |
|     | 𝑁 𝑛=1             | 𝜎 −𝜎𝑟 |         |
𝑓
onde  𝑓 e  𝑟 são os valores médios; σ e σ são os desvios padrão. O coeficiente de
|     | f r  |     |     |
| --- | ---- | --- | --- |
correlação varia de -1 a 1 (TAYLOR, 2001).
A  estatística  mais  utilizada  para  quantificar  diferenças  de  duas  séries
temporais é o RMSE. Considere duas variáveis f e r, então o RMSE é definido por:
1/2
𝑁
1
| 𝐸 = | [ ∑ (𝑓 −𝑟 | )²]   (2)  |     |
| --- | --------- | ---------- | --- |
|     | 𝑛         | 𝑛          |     |
𝑁
𝑛=1
O bias geral é definido por:
𝐸 = 𝑓 −𝑟  (3)
O RMS centralizado é definido por:
| 𝑁        |            |      | 1/2      |
| -------- | ---------- | ---- | -------- |
| 1        |            | 2    |          |
| 𝐸′ = { ∑ | [(𝑓 −𝑓)−(𝑟 | −𝑟)] | }   (4)  |
|          | 𝑛          | 𝑛    |          |
𝑁
𝑛=1

O coeficiente de correlação e a diferença do RMS fornecem informações
estatísticas complementares que quantificam a correspondência entre duas séries
temporais.  Porém  para  uma  caracterização  mais  completa,  a  variância  (desvio
padrão)  de  cada  série  também  deve  ser  fornecida.  As  quatro  estatísticas
mencionadas  (RMSE,  coeficiente  de  correlação  e  desvio  padrão  reanalise  e
observação) são úteis para a comparação, e é possível mostrá-las em um mesmo
gráfico (TAYLOR, 2001).
2.2.2.  Rastreamento de ciclones

O  rastreamento,  ou  tracking,  utilizado  neste  trabalho  foi  realizado  por
Gozzo (2014) e Gozzo et al., (2017). Primeiramente, realizou tracking para encontrar
todos os ciclones, e após isso, utilizou o diagrama proposto por Hart (2003) para
separar os eventos de CSs.
O  rastreamento  utilizado  por  Gozzo  (2014)  para  encontrar  todos  os
ciclones foi o mesmo utilizado por Reboita (2008). Sugahara (2000) desenvolveu um
algoritmo, seguindo a metodologia similar à de Sinclair (1996), utilizando vorticidade
38

relativa no rastreamento. Então, Reboita (2008) aprimorou o algoritmo de Sugahara
(2000), aperfeiçoando algumas metodologias utilizadas no rastreio, como exemplo,
na suavização dos campos.
O método de identificação define uma sequência de mínimos (no
hemisfério Sul) de vorticidade relativa (no vento em 925 hPa) utilizando o método
dos vizinhos mais próximo (Nearest-Neighbor Search). No entanto, antes de iniciar o
rastreamento, é necessário suavizar os campos, para isto se utiliza o método de
Cressmann (CRESSMAN, 1959) que depende do raio de influência para a
suavização. Reboita (2008) utilizou o raio de influência de 500 km para eliminar os
centros espúrios de vorticidade e reduzir a presença de zonas de cisalhamento
alongadas.
De acordo com Reboita (2008) o processo de identificação e tracking
(rastreamento) dos ciclones envolvem as seguintes etapas:
1) Identificação do mínimo de vorticidade;
2) Localização da posição após o primeiro deslocamento (first guess);
3) Buscar as posições seguintes.
A primeira etapa consiste na identificação dos mínimos de vorticidade
pelo método de vizinho mais próximo que compara a vorticidade em cada ponto de
grade com os pontos mais próximos. Então, considera-se o ponto em que a
vorticidade é menor do que os outros pontos e menor ou igual a um limiar pré-
estabelecido. Após esta identificação inicial, o algoritmo corrige a posição do centro
do ciclone ao fazer uma nova procura em um raio de 250 km dos mínimos de
vorticidade. Para isto, interpola o campo de vorticidade ao redor deste centro para
uma grade de alta resolução (0,28º x 0,28º) através de uma função polinomial bi-
cúbica (REBOITA, 2008 e GOZZO, 2014).
São encontradas duas posições de mínimos em tempos consecutivos, a
diferença entre estas fornece a velocidade do deslocamento do ciclone. Esta
velocidade é denominada de primeira estimativa, do inglês first guess da posição do
sistema no tempo futuro, e ao redor desta posição estima-se a nova posição no
próximo tempo. Este procedimento é repetido para identificar as futuras posições
(GOZZO, 2014).
De acordo com Reboita (2008) um ciclone deixa de existir quando a sua
vorticidade relativa exceder o limiar estabelecido (ζ = -1,5 x 10-5 s-1) ou quando
ultrapassa o tempo de vida máximo especificado (10 dias).
39

O método que descreve a estrutura tridimensional dos ciclones é
chamado Cyclone Phase Space - CPS (HART, 2003), que foi utilizado para
separação dos ciclones subtropicais no trabalho de Gozzo (2014).
De acordo com Hart (2003) muitos parâmetros foram examinados para
entender melhor a estrutura térmica e dinâmica dos ciclones. Após uma avaliação
cuidadosa dos parâmetros (vorticidade potencial, perfil vertical, vetor Q, temperatura
potencial, inclinação ciclônica e entre outros). Hart (2003) verificou que duas
medidas mais simples, no entanto, fundamentais, denominadas de assimetria
térmica e vento térmico. Os três parâmetros utilizados para descrever a estrutura
geral dos ciclones são assimetria térmica (parâmetro B), vento térmico na troposfera
inferior (núcleo frio versus quente, parâmetro −𝑉𝐿) e vento térmico na troposfera
𝑇
superior (núcleo frio versus quente, parâmetro −𝑉𝑈).
𝑇
I) Parâmetro B: simetria térmica do ciclone
A classificação dos ciclones ao redor do globo dividiu-se inicialmente em
dois tipos principais: extratropicais (resultantes do gradiente horizontal de
temperatura - assimétricos ou frontais) e tropicais (simétricos e não frontais). A
natureza frontal do ciclone (ou a falta) indica o tipo de ciclone e seu estágio de
evolução. Esta característica é definida como a assimetria na baixa-média troposfera
(B), na camada 900-600 hPa de espessura, relativa ao movimento dos sistemas
considerando um raio de 500 km. Então B é definido como:
𝐵 = ℎ(𝑍 − 𝑍 | −𝑍 − 𝑍 | ) (5)
600 ℎ𝑃𝑎 900 ℎ𝑃𝑎 𝑅 600 ℎ𝑃𝑎 900 ℎ𝑃𝑎 𝐿
onde Z é a altura geopotencial, R indica a posição à direita do movimento dos
sistemas, L indica à esquerda e a barra superior indica a média da área sobre o
semicírculo de raio de 500 km. O h assume valores -1 no HN e +1 no HS.
Um ciclone tropical no seu estágio maduro tem B ~ 0 enquanto um ciclone
extratropical em desenvolvimento tem um grande valor positivo de B. Um valor
positivo de B indica ar frio (quente) à esquerda (direita) do ciclone no HN (HS),
consistente com a relação do vento térmico entre o gradiente horizontal de
temperatura e o cisalhamento vertical do vento horizontal. Um limiar para distinguir
os dois ciclones é B=10 m. Este limiar também é utilizado para diferenciar sistemas
não frontais quando o centro não está exatamente em B ~ 0. Então, o parâmetro B
40

para o ciclone tropical assume valores -10 m < B < +10 m. Para sistemas
extratropicais em formação e desenvolvimento B >> 0. A classificação dos ciclones
subtropicais assumiu valor de B superior a 10 m, mas não muito elevado (até 25 m)
(GOZZO, 2014; GOZZO et al., 2014 e GOZZO et al, 2017).
II) Parâmetro −𝑉𝐿 e −𝑉𝑈: Vento térmico - núcleo frio versus quente.
𝑇 𝑇
Os parâmetros do vento térmico mostram a distinção do núcleo frio-
quente, que é feita considerando a mudança de espessura entre camadas de 900-
600 hPa e 600-300 hPa. A perturbação da altura do ciclone (𝚫Z) é definida como:
𝛥𝑍 = 𝑍 −𝑍 (6)
𝑚á𝑥 𝑚í𝑛
Considerando d como a distância entre os extremos geopotencial na
equação (6) e sendo f o parâmetro de Coriolis, então 𝚫Z é proporcional a magnitude
do vento geostrófico (V )
g
𝛥𝑍 = 𝜕𝑔|𝑉 |𝑓 (7)
𝑔
A estrutura vertical do ciclone (núcleo frio vs quente) é definida como a
derivada vertical 𝚫Z,
𝜕(𝛥𝑍) |600 ℎ𝑃𝑎 = |−𝑉𝐿 (8𝑎)
900 ℎ𝑃𝑎 𝑇
𝜕𝑙𝑛𝑃
𝜕(𝛥𝑍)
|300 ℎ𝑃𝑎 = |−𝑉𝑈(8𝑏)
𝜕𝑙𝑛𝑃 600 ℎ𝑃𝑎 𝑇
A estrutura de núcleo frio versus quente se relaciona diretamente com a
estrutura vertical da perturbação do sistema.
Para cada tipo de ciclone existe um valor do parâmetro do vento térmico
(assim como para B) nas diferentes fases de ciclones. No ciclone extratropical, os
valores são negativos, ou seja, −|𝑉𝐿|< 0 e −|𝑉𝑈|< 0 (Hart e Evans, 2001). Pelo
𝑇 𝑇
balanço do vento térmico deve existir um gradiente horizontal de temperatura
positiva no centro do ciclone, ou seja, núcleo frio (GOZZO, 2014). Nos ciclones
tropicais (HART e EVANS, 2001) os valores são positivos, pois a perturbação é mais
intensa em baixos níveis (GOZZO, 2014), e então −|𝑉𝐿|> 0 e −|𝑉𝑈|> 0, isto ocorre
𝑇 𝑇
por causa do núcleo quente em toda troposfera. Evans e Hart (2003), Evans e
Guishard (2009) e Guishard, Evans e Hart (2008) mostraram para o ciclone
41

subtropical valores de−|𝑉𝐿| > 0 e −|𝑉𝑈| < 0 definindo a estrutura híbrida do núcleo
𝑇 𝑇
deste tipo de sistema.
2.2.3. Critério para obtenção dos extremos de ventos
Foi desenvolvido um critério para encontrar os extremos da velocidade do
vento na região de estudo (Figura 7) para as reanálises CFSR e ERA5.
Primeiramente, calcula-se a magnitude do vento, e a partir desta, encontra-se o
percentil extremo para cada ponto de grade da Figura 8. No presente trabalho, foi
utilizado o percentil de 95%, pois a finalidade é encontrar extremos de vento, e como
indica a literatura, este é o percentil mais utilizado (da SILVA, 2013). Este percentil
permitiu encontrar os extremos, ou seja, se a velocidade do vento em um
determinado tempo e posição superar o percentil, considera-se a ocorrência de um
extremo. Em síntese, fez-se uma varredura no tempo, comparando cada ponto de
grade com os percentis de 95% e, se a magnitude do vento exceder este limiar no
ponto de grade, é considerado um extremo, por outro lado, se não houver um
extremo, os valores serão “não válidos (NA ou NULL)”. A Figura 9 mostra um
exemplo para um dia com extremos de velocidade do vento ao mesmo tempo que se
registrou a ocorrência de um ciclone subtropical. Em outras palavras, neste trabalho
foi considerado um extremo, se a intensidade do vento exceder o limiar pré-
estabelecido, ou seja, para cada horarío sinótico e ponto de grade pode conter um
extremo de vento.
42

a) b)
Figura 8. Intensidade do vento correspondente ao percentil de 95% de velocidade do vento
(sombreado, m s-1) para cada ponto de grade para as duas reanálises (a) CFSR e (b) ERA5.
A RG1 é indicada pelo retângulo preto.
2.2.4. Associação entre extremos e ciclones
Um dos objetivos do trabalho é associar extremos de vento no leste do
sudeste do Brasil com os ciclones subtropicais. Alguns métodos são utilizados para
relacionar os extremos de vento com a região dos ciclones. Primeiramente emprega-
se uma caixa, com um tamanho aproximado semelhante ao do ciclone (20º X 20º);
para seis ciclones subtropicais estudados por Reboita et al. (2019) apresentaram
este tamanho, por isto, Reboita et al. (2019) e no presente trabalho utilizam essa
caixa. Posteriormente, faz-se uma varredura se na hora e dentro dessa área são
registrados pelo menos um extremo de vento, foi considerado associado ao ciclone.
Como as saídas do tracking são a cada 6h, esta varredura é realizada para cada
posição da trajetória do ciclone, desde o início até o fim do ciclo de vida. A Figura 9
mostra um exemplo do ciclone subtropical Anita e a velocidade do vento superando
o percentil de 95% ao longo da trajetória do ciclone. Observa-se que na região com
a maior parte dos extremos do vento estão dentro da caixa desenhada em relação
ao centro do ciclone.
43

Figura 9. Exemplo de extremos de velocidade do vento a 10 m (sombreado, em m s-1) e o
box de 20 º x 20 º (retângulo preto) utilizado em relação ao ponto central do ciclone (ponto
laranja) e o retângulo vermelho indica a RG1 para a data 04-03-2010 06 UTC.
2.2.5. Climatologia
Duas climatologias sazonais são calculadas para o vento a 10 m de
altura. A primeira calcula a média sazonal das componentes zonal e meridional do
vento horizontal (u e v) e, então obtém a intensidade média do vento. Esta primeira
climatologia permite discutir o padrão espacial da velocidade e direção dos ventos
em cada estação do ano, bem como a sua intensidade. A segunda climatologia
considera apenas a intensidade do vento. Neste caso, calcula-se a magnitude do
vento para cada horário e após, a média sazonal. Esta climatologia serve para
entender a intensidade do vento independente da direção média e é utilizada
também para as outros cálculos que serão descritos posteriormente.
A climatologia da intensidade do vento (segunda) dos dias com ciclone
subtropical considera apenas os horários do ciclone. As localizações dos ciclones
estão disponíveis a cada 6 horas, então foram utilizados apenas as datas com
ciclones para obter uma média sazonal. Após isso, calculam-se anomalias
44

(subtraindo a média sazonal dos dias com ciclone com a média sazonal de todo o
período em relação a climatologia).
A climatologia sazonal considera os meses de junho, julho e agosto (JJA -
Inverno), Março, Maio e Abril (MMA - Outono), Dezembro, Janeiro e Fevereiro (DJF -
Verão) e Setembro, Outubro e Novembro (SON - Primavera).
2.2.6. Série temporal seguindo o centro do ciclone
Como mencionado anteriormente, o trajeto do ciclone mostra a posição
central a cada 6 horas. Esta trajetória permite extrair uma série temporal dos
máximos da velocidade do vento e extremos do vento seguindo a trajetória do
ciclone. Para isto, considera-se uma caixa de 20º x 20º em relação ao centro do
ciclone como referência, então seguindo o trajeto do ciclone extrai-se o máximo da
velocidade e extremos da velocidade nesta caixa.
Com a série temporal, são calculadas algumas estatísticas (boxplot
sazonal e média anual) para entender o comportamento da velocidade do vento nos
dias com ciclone.
2.2.7. Distância do centro do ciclone e extremos de vento
Os extremos de vento podem acontecer em várias regiões do SAO.
Para encontrar a distância de cada extremo de vento em relação ao centro do
ciclone consideram-se apenas os extremos contidos na caixa de 20º x 20º em
relação ao centro do ciclone. A partir disso, calcula-se a distância de cada
extremo de vento interceptado com a caixa e o centro do ciclone a cada 6
horas. Em linhas gerais, cada ponto de grande que excedeu o limiar é um
extremo, e então calculou-se a distância para cada grade que contém
extremos.
Há várias formas para calcular a distância entre dois pontos, sendo:
Haversine, VicentySphere,VicentyEllisoid e lei dos cossenos do círculo máximo
(do inglês law of cossine “great circle”). Neste trabalho se utiliza a lei do
cosseno e a distância é determinada por:
45

𝑑 = 𝑟 𝑐𝑜𝑠−1(𝑠𝑒𝑛𝜙 𝑠𝑒𝑛𝜙 + 𝑐𝑜𝑠𝜙 𝑐𝑜𝑠𝜙 𝑐𝑜𝑠(𝜆 − 𝜆 )) (9)
1 2 1 2 1 2
onde Φ é a Latitude, λ a Longitude, r o raio da terra (r=6371000 m)
2.2.8. Vento acumulado
Para associar os ventos com os ciclones subtropicais desenvolveu-se um
método que acumula o vento seguindo a trajetória do ciclone. O tracking do ciclone
fornece a posição a cada 6 horas, ou seja, o centro do CS naquele momento. Para
cada posição é considerado uma caixa de 20 º x 20º em relação ao centro do
ciclone. Após isso, é realizada a somatória nos pontos de grade que coincidem com
outro ponto de grade, ou seja, se a grade dentro da box, coincidir com outra,
acumula-se a velocidade. A Figura 10 mostra um exemplo da velocidade acumulada
ao longo da trajetória do Ciclone Subtropical Anita. Este procedimento é similar ao
utilizado para identificar a chuva associada aos ciclones extratropicais como, por
exemplo, utilizado em Reboita et al., (2018) e Reboita et al., (2019).
Após calcular o vento acumulado, faz-se uma contagem de quantas vezes
cada posição coincide, em seguida, divide-se o acumulado de vento por esta
quantidade, obtendo-se a velocidade média associada com a trajetória de ciclone.
Com isso, no vento acumulado está associado às posições de maior ocorrência de
ventos intensos e ciclones e o vento médio à intensidade dos ventos nos dias que
ocorrem ciclones.
46

Figura 10. Exemplo de vento a 10 m acumulado m s-1 para o ciclo de vida do ciclone
subtropical Anita.
47

3. RESULTADOS
Este capítulo descreve os resultados da pesquisa em duas partes. A
primeira parte é focada no entendimento da climatologia do vento 10 m de altura
utilizando dados de observações locais e comparações entre estes e as reanálises
(ERA5 e CFSR) utilizando o diagrama de Taylor. A segunda parte tem como
propósito em relacionar os ciclones subtropicais com os ventos em superfície (vento
em 10 m).
3.1. Velocidade do vento: Observações locais e reanálises
A climatologia de rajadas de vento (Figura 11), ou seja, as maiores
velocidades registradas em um dia, apresentam padrão semelhante ao da
velocidade média (Figura 12). Em termos médios anuais, a estação de Arraial do
Cabo registra maiores rajadas de vento e as de Itapoá e Parati as menores. Para o
ciclo anual, as maiores rajadas de vento ocorrem entre agosto-outubro, e as
menores entre março-junho (Figura 11), padrão semelhante ao do ciclo anual para a
velocidade média diária (Figura 12).
48

a)
b)
Figura 11. Climatologias (2008-2017, exceto em São Sebastião que engloba 2014-2017) da
rajada do vento diário (m s-1) observada em diferentes estações meteorológicas: (a) Média
anual e (b) Ciclo anual.
A climatologia mostra que na estação localizada em Arraial do Cabo a
intensidade do vento é maior comparada com as outras localidades, seguida de São
Sebastião (Figura 12a e 13a). As menores velocidades são registradas em Itapoá,
Iguape e Parati. Na série temporal para a média anual (Figura 12a), as localidades
de Macaé e Arraial do Cabo apresentam padrão bastante similar de variabilidade
interanual, concordando com anos de aumento e diminuição da velocidade do vento.
Em alguns anos a maioria das localidades apresentou picos semelhantes, como
exemplo 2013 e 2016. O ciclo anual de todas as localidades indica padrão
semelhante (Figura 13a). O inverno com as menores velocidades de vento,
enquanto primavera e verão são observadas velocidades maiores.
As Figuras 12 e 13 mostram o ciclo e média anual da velocidade do
vento para as observações e reanálises. As observações de Iguape e Itapoá
possuem valores próximos de velocidade do vento ao longo do período. Nas
reanálises em Itapoá o vento é mais intenso do que Iguape, diferente do que indicam
49

as observações locais. O padrão do ciclo anual entre a observação (Itapoá e Iguape)
e reanálise é semelhante. Na média anual (Figura 12) há picos que a intensidade do
vento é maior nas reanálises do que nas observações das estações. Existe uma
maior similaridade entre as fases nas diferentes localidades em termos de
variabilidade interanual (aumentos e decréscimos) da velocidade do vento nas
reanálises do que nas observações locais (Figura 12).
A observação em Ilha do Mel apresenta intensidade do vento maior
comparada com as reanálises ERA5 e CFSR, ou seja, as reanálises subestimam a
intensidade do vento nessa estação. O padrão do ciclo anual nas reanálises, em
comparação ao observado, o padrão é diferente como ocorre também para a
velocidade média anual.
Na estação de Arraial do Cabo a oscilação do ciclo anual para as
reanálises ERA5 e CFSR é similar à observada (Figuras 13), mas as reanálises
superestimam a intensidade do vento, sendo que a ERA5 (Figura 13c) apresenta
maior superestimativa. Na série temporal da velocidade média anual (Figura 12), o
padrão de variabilidade interanual entre a observação e a reanálise é similar. Há
picos que nas reanálises a intensidade é maior comparado com observação, como
nos anos de 2010/2011, 2013/2014 e 2016/2017. No caso de 2014/2015 as duas
reanálises têm um decréscimo, enquanto as observações indicam um aumento.
Em Alfredo Chaves a série temporal da velocidade média anual das
reanálises ERA5 e CFSR apresentam padrão similar ao observado (Figura 12), com
o CFSR mais próximo da observação. A intensidade do vento nas duas reanálises é
maior do que no observado, comparativamente a ERA5 é mais próxima da
observação. O padrão do ciclo anual da velocidade do vento (Figura 13) nas
reanálises é semelhante ao observado, exceto entre julho-setembro quando o
aumento de velocidade é mais pronunciado nas reanálises.
O padrão do ciclo anual da velocidade do vento (Figura 13) nas
reanálises está fora de fase em relação à observação em Florianópolis. Por
exemplo, entre junho/julho as velocidades diminuem na observação (Figura 13a).
No entanto, na reanálise nota-se um aumento (Figura 13 b e c). Como já
encontrado para outras estações, na ERA5 a intensidade do vento é maior do que
no CFSR e observação. A média anual de intensidade do vento (Figura 12) diminui
na observação nos anos 2010, 2012 e aumenta em 2014, enquanto o oposto ocorre
nas reanálises.
50

Em Macaé os padrões do ciclo (Figura 13) e evolução temporal média
anual (Figura 12) da velocidade do vento são similares entre as reanálises e
observação, no entanto, nas reanálises a intensidade é maior.
No caso de São Sebastião, o ciclo anual de velocidade (Figura 13) é
semelhante à das reanálises. Para a variabilidade interanual (Figura 12), a média
anual em 2014 e 2015 aumenta na reanálise CFSR o que não ocorre no observado.
A série temporal de velocidade do vento na ERA5 se assemelha mais à observada
do que o CFSR.
51

a)
b)
c)
Figura 12. Climatologias (2008-2017, exceto em São Sebastião que engloba 2014-2017) da
velocidade do vento diário (m s-1) observada em diferentes estações meteorológicas para a
média anual: (a) Observado, (b) CFSR e (c) ERA5.
52

a)
b)
c)
Figura 13. Climatologias (2008-2017, exceto em São Sebastião que engloba 2014-2017) da
velocidade do vento (m s-1) das reanálises interpoladas para as estações para o ciclo anual:
(a) Observado; (b) CSFR e (c) ERA5.
Os diagramas de Taylor na Figura 14 auxiliam nas comparações entre
observações e reanálises. Estes diagramas foram obtidos considerando valores
diários de velocidade do vento para todo período de disponibilidade de observações,
ou seja, de 2008-2017 (exceto em São Sebastião com período 2014-2017).
De uma forma geral, os resultados das séries temporais e os diagramas
de Taylor apresentam padrões semelhantes, isto é, quando a série está fora de fase,
observa-se uma baixa correlação. Por outro lado, quando os mínimos e máximos
estão distantes entre as reanalises e observações o RMSE é alto, ou seja, os
53

extremos não são muito bem representados. No desvio padrão mostra a amplitude
da variabilidade temporal entre as reanálises e observações. As próximas análises
serão direcionadas nessas comparações.
A Figura 14f mostra que na estação da Ilha do Mel as correlações são
baixas (0,35 e 0,21, respectivamente ERA5 e CFSR). As Figuras 12 e 13 mostram
que o padrão do ciclo anual e a série temporal da média anual da velocidade na Ilha
do Mel diferem entre reanálises e observações explicando as baixas correlações. A
raiz quadrada do erro quadrático médio (RMSE) para ambas as reanálises são de
1,2 m s-1 aproximadamente. O vento observado (Figuras 12a e 13a) é mais intenso
do que a reanálise CFSR, por isso o desvio padrão é diferente da observação. Por
outro lado, na ERA5 o desvio padrão está mais próximo do valor da estação.
Como mostram as Figuras 12 e 13 as observações de Florianópolis
apresentam um padrão para a média e ciclo anual de velocidade bem diferente entre
as reanálises. Além disso, é a estação com a menor correlação temporal entre as 9
estações (Figura 14h), os valores das correlações temporais para a velocidade do
vento são próximas de 0 em ambas as reanálises. No entanto, o desvio padrão das
reanálises é próximo ao da observação, principalmente para o CFSR.
A cidade de Arraial do Cabo apresenta a maior correlação (Figura 14g)
(0,8 para as duas reanálises), ou seja, os padrões de variabilidade temporal da
velocidade diárias das reanálises são similares ao observado. O desvio padrão da
ERA5 é um pouco mais próximo ao observado do que no CFSR. O RMSE para as
duas tem valor próximo entre si (~ 1,25 m s-1).
A localidade de São Sebastião (Figura 14i) apresenta correlações
relativamente altas entre as nove estações analisadas, ou seja, 0,64 (ERA5) e 0,66
(CFSR). Como indicam as comparações anteriores (Figuras 12 e 13) a intensidade
do vento na ERA5 é mais próxima do observado e o desvio padrão do ERA5 é
ligeiramente mais próximo da observação. No entanto, o RMSE do CFSR é um
pouco menor.
Em Parati as correlações entre as séries diárias de velocidade são baixas
(0, 12 e 0,10, respectivamente, para a CFSR e ERA5), além disso, o desvio padrão
das reanálises está distante do observado (Figura 14e). As observações não
apresentam forte variabilidade diária da velocidade do vento presente nas
reanálises. Isto também ocorre para a velocidade média anual e ciclo anual (Figuras
12 e 13) onde as variações no tempo são mais acentuadas nas reanálises do que na
54

estação, com alguns decréscimos e aumentos diferentes entre observado e
reanálise.
Em linhas gerais, os diagramas de Taylor (Figura 14) sintetizam a maior
habilidade das reanálises em reproduzir a velocidade do vento observado nas
estações de Iguape, Macaé, Arraial do Cabo, São Sebastião e Itapoá. Enquanto nas
estações de Florianópolis, Parati, Alfredo Chaves e Ilha do Mel as correlações
temporais são baixas e os RMSEs são altos e indicam dificuldades de representação
das observações locais.
55

a) b)
c)
d)
Figura 14. Diagrama de Taylor para as séries temporais (período 2008-2017, exceto em
São Sebastião que se refere ao período 2014-2017) da velocidade do vento média diária,
onde: estão indicados valores para estação (círculo preto), ERA5 (ponto verde) e CFSR
(ponto rosa): (a) Iguape, (b) Itapoá, (c) Macaé, (d) Alfredo Chaves, (e) Parati, (f) Ilha do Mel,
(g) Arraial do Cabo, (h) Florianópolis e (i) São Sebastião. As linhas indicam: raiz do erro
quadrático médio (linha contínua dourada), desvio padrão (linha pontilhada azul) e
coeficiente de correlação (linha pontilhada preta). O desvio padrão para referência, ou seja,
desvio padrão da estação (linha contínua preta).
56

e) f)
g) h)
i)
Figura 14. Continuação
Além de utilizar dados de estações meteorológicas automáticas, também
foram analisados dados de boias meteoceanográficas, mesmo com a dificuldade
adicional de utilizar estes dados em função de contar com muitos dados faltantes.
Nas boias (Figura 15), o ciclo anual não é tão suavizado como nas
estações, isso pode ter acontecido por dois motivos. O primeiro é que a quantidade
57

de dados é menor, como indicado na Tabela 3. As boias com maior período em
anos e menos dados faltantes são de Santos e Itajaí (Tabela 2) e, mesmo assim há
um grande contraste na variação do ciclo anual. O segundo motivo, é que os
sistemas meteorológicos que ocasionam ressacas e ondas, fazem com que as
boias, instaladas em mar aberto, registrem mais livremente grandes variações de
velocidade do vento, evidenciando esse maior contraste.
No entanto, de uma forma geral, as boias (Figura 15a) mostram que no
inverno a intensidade do vento é menor, e maior no final da primavera e no verão.
Em Itajaí o ciclo anual é praticamente oposto, com o vento mais intenso no final do
inverno e começo da primavera e menos intenso no verão, esta localidade é a única
na região sul do país, localizada em Santa Catarina, isso pode afetar na diferença do
ciclo anual, pois na região Sul do pais as frentes passam com mais frequência no
inverno e começo da primavera (ANDRADE, 2005) .
Em geral, nas estações meteorológicas (continente), as reanálises
superestimam a intensidade do vento na maioria das cidades, enquanto nas boias
(oceano) nota-se comportamento contrário, ou seja, as reanálises subestimam a
intensidade do vento.
As estações de Niterói e Cabo Frio têm padrões de média e ciclo anual
diferentes do observado (Figuras 15 e 16), refletindo em baixos valores de
correlação temporal da série diária de velocidade indicadas no diagrama de Taylor
(Figura 17 d e e). Em Cabo Frio a correlação é muita pequena para CFSR (0,05) e
ligeiramente maior (0,3) na ERA5. Em Niterói a correlação também é pequena para
as duas reanálises, sendo menor que 0,1. No entanto, as estatísticas em Cabo Frio
devem ser analisadas com cuidados desde que possui uma série temporal muito
curta de observações como mostra a Figura 15, além disso, existem muito dados
faltantes nesses anos (Tabela 3).
Em Vitória os padrões na média anual e ciclo anual das reanálises
(Figura 15bc e 16bc) se assemelham aos observados (Figuras 15a e 16a),
resultando na alta correlação para as séries diárias de velocidade que chega a 0,9
na CFSR e 0,91 na ERA5 como mostra o diagrama de Taylor (Figura 17c). O desvio
padrão das reanálises é próximo do observado e a raiz do EQM é o menor entre as
5 boias, sendo 1,0 m/s (CFSR) e 0,8 m/s (ERA5).
A média anual e ciclo anual de velocidade para Itajaí mostram que as
observações são bem representadas pelas reanálises na maior parte do período. As
58

correlações (Figura 17b) para a CFSR (0.8), como para a ERA5 (0.79). A
intensidade do vento observado é subestimada pelas as reanálises. Nota-se ainda
menor desvio padrão nas reanálises indicando menor variabilidade da série diária de
velocidade do que indica a observação.
Em Santos as reanálises possuem um desempenho razoável para
representar valores diários observados de velocidade, dado que a correlação entre
ambas as reanálises é de 0.6 (Figura 17a). Por outro lado, o alto valor de EQM nas
reanálises indica problemas na representação de extremos; e o desvio padrão
menor do que o observado estaria associado à dificuldade em representar a
variabilidade diária na velocidade. Isto se reflete na média anual da intensidade que
varia entre 5,5 - 6 m/s nas reanálises, enquanto nas observações varia 6,5 – 9 m/s.
Essa grande variação de intensidade do vento também é vista no ciclo anual
observado.
59

a)
b)
c)
Figura 15. Climatologias da velocidade do vento (m s-1) das boias meteoceanográficas para
o ciclo anual: (a) Observação, (b) CFSR e (c) ERA5.
60

a)
b)
c)
Figura 16. Climatologias da velocidade do vento (m s-1) das reanálises interpoladas para as
boias meteoceanográficas para a média anual: (a) Observação, (b) CFSR e (c) ERA5. As
séries para a média anual indicam o período disponível para obter as climatologias nas
estações.
61

a) b)
c) d)
e)
Figura 17. Diagrama de Taylor para as séries temporais da velocidade do vento média
diária das boias meteoceanograficas, onde: estão indicados valores para estação (círculo
preto), ERA5 (ponto verde) e CFSR (ponto rosa): (a) Santos, (b) Itajaí, (c) Vitória, (d) Niterói
e (e) Cabo Frio. As linhas indicam: raiz do erro quadrático médio (linha contínua dourada),
desvio padrão (linha pontilhada azul) e coeficiente de correlação (linha pontilhada preta). O
desvio padrão para referência, ou seja, desvio padrão da estação (linha contínua preta).
62

3.1.1. Comparação com outros trabalhos.
De uma forma geral, as localidades com maiores correlações para as
séries diárias em ambas as reanálises também representam o padrão de média
anual e ciclo anual para a velocidade do vento em maior concordância com as
observações. No caso das estações meteorológicas (continente) as reanálises
superestimam a velocidade do vento, exceto em Ilha do Mel que subestima. Nas
boias (oceano) as reanálises subestimam a intensidade do vento.
Nas boias, a diferença da intensidade e variabilidade diária do vento é
grande entre observações e reanálises. Na maioria delas os desvios padrões para
as séries diárias de velocidade das reanálises são sempre menores do que os
observados, indicando menor variabilidade diária. Além disso, a raiz do EQM de três
boias (Santos, Itajaí e Cabo Frio) são elevados, passando de 2 m s-1, ou seja, as
reanálises têm dificuldade em representar valores extremos (máximos e mínimos) da
série diária de velocidade com as observações.
As Tabelas 4 e 5 mostram uma síntese das correlações e médias do ciclo
anual da velocidade do vento para as observações locais e reanálises. Deste modo,
as correlações são altas para o ciclo anual em praticamente todas as estações e
boias. A reanálise ERA5 representa melhor o padrão do ciclo anual da velocidade do
vento, ou seja, das nove estações, seis destas a correlação da ERA5 foi mais alta
comparada com a reanálise CFSR. No caso das boias a reanálise CFSR é melhor
apenas em duas localidades. Portanto, para estas localidades, tanto para a
correlação de ciclo anual (Tabelas 4 e 5) e para variabilidade diária (Figuras 14 e
17), a ERA5 tem uma maior habilidade em reproduzir a velocidade do vento
observado.
Nas boias e estações meteorológicas, as correlações das séries diárias
de velocidade são similares para ERA5 e CFSR. A reanálise do ERA5 é
relativamente nova, por esta razão, não existem muitos trabalhos que a compare
com dados observacionais. Bets et al. (2019), compararam o vento a 10m da ERA5
com observações no Canadá e, mostraram que a mesma subestima a velocidade do
vento observado. Existem estudos mais abrangentes comparando ERA-Interim,
antecessora da ERA5, com observações locais (PENG et al., 2013, STÜCKER et al.,
2016, MICALICHEN e DIAS, 2018, CARVALHO et al., 2014 e KIM, KIM e KANG,
2013).
63

Alguns autores fizeram comparações em diferentes localidades utilizando
a reanálise CFSR e outras reanálises e/ou modelos. Por exemplo, Stücker et al.
(2016) compararam velocidade e direção do vento para 33 estações meteorológicas
automáticas do INMET no Rio Grande do Sul com as reanálises CFSR e Era-Interim.
Encontraram basicamente melhores correlações para a magnitude do vento entre as
estações e a reanálise CFSR e para a direção do vento entre as estações a ERA-
Interim.
Peng et al. (2013) correlacionou dados de 12 boias nas regiões do
Oceano Atlântico, Índico e Pacífico com cinco análises de vento. Compararam as
reanálises do ECMWF e CFSR, modelo DWD (que assimila dados de vento de boias
com ventos do satélite scatterometer), o blended sea surface winds (baseados em
observações e múltiplos instrumentos em satélites, incluindo radiômetro passivo de
microondas e active scatterometer) e os ventos NWP (são ventos de previsão de
curto alcance de análises que são construídos por dados observados). Seus
resultados mostraram melhor desempenho do CFSR, que apresenta alta correlação
e baixo EQM. Em contraste, o DWD apresenta correlações mais baixas,
especialmente para componente meridional do vento (v).
Kim, Kim e Kang (2013) compararam dados de vento de 10 torres
meteorológicas em diferentes altitudes na Coreia do Sul com quatro reanálises
(MERRA, MERRA-2, CFSR, ERA-Interim) de terceira geração de reanálise. A
MERRA-2 representa melhor as observações locais na maioria das torres, com
correlação de 0,67, ligeiramente superior às do CFSR. Carvalho et al. (2014) com o
intuito de comparar dados observacionais e diversas análises e outros produtos
(modelo, satélite, reanálise e análise) para os ventos em superfície na Península
Ibérica (costa da Espanha e Portugal) calcularam vários índices estatísticos (RMSE,
desvio padrão, coeficiente de correlação e bias.) De uma forma geral, a reanálise
CFSR mostrou maior habilidade em representar o vento em superfície do que a
reanálise ERA-Interim (antecessora da ERA5), com altos coeficientes de correlação
e baixo bias.
Micalichen e Dias (2018) utilizaram 17 estações meteorológicas no estado
de Minas Gerais obtidas da Companhia de Energia de Minas Gerais (CEMIG) e
correlacionaram a velocidade do vento em superfície (vento 10 m) com a reanálise
CFSR. Estes autores obtiveram que para as localidades analisadas as correlações
não excedem 0,5. A raiz do erro quadrático os valores não ultrapassam a 2 m/s. O
64

viés  gira  em  torno  de  ±  0,8  m/s,  exceto  por  duas  estações  que  os  valores
ultrapassam ± 1 m/s.  Como conclusão geral, os autores consideram que para tais
localidades a reanálise CFSR não representa adequadamente o vento observado.
Comparativamente, para algumas estações analisadas no presente estudo (Macaé,
Iguape, Arraial do Cabo, São Sebastião e Itapoá) as reanálises fornecem índices
estatísticos superiores indicando maior representativa pelas reanálises do vento em
regiões costeiras.

Tabela 4. Média e correlação (entre parênteses) para o ciclo anual entre observações
(estações meteorológicas automáticas) e reanálises (ERA5 E CFSR).

| Estações  |         | Observações   | ERA5         | CFSR         |
| --------- | ------- | ------------- | ------------ | ------------ |
| Alfredo   | Chaves  | –  1,93       | 3,59 (0,63)  | 3,21 (0,57)  |
ES
| Arraial do Cabo –  |     | 4,47  | 5,03 (0,97)  | 4,64 (0,93)  |
| ------------------ | --- | ----- | ------------ | ------------ |
RJ
| Florianópolis - SC  |             | 1,71  | 3,49 (- 0,077)  | 3,13 (-0.42)  |
| ------------------- | ----------- | ----- | --------------- | ------------- |
| Iguape              | -  SP       | 1,30  | 2,62 (0,93)     | 2,24 (0,92)   |
| (INMET)             |             |       |                 |               |
| Ilha  do            | Mel  -  PR  | 2,50  | 2,59 (0,86)     | 2,22 (0,88)   |
(INMET)

| Itapoá          | -  SC  | 1,16     | 2,87 (0,89)    | 2,57 (0,73)    |
| --------------- | ------ | -------- | -------------- | -------------- |
| (INMET)         |        |          |                |                |
| Macaé – RJ      |        | 2,66     | 3,46 (0,93)    | 3,27 (0,75)    |
| Parati – RJ     |        | 1,48     | 2,45 (- 0.41)  | 3,01 (- 0.38)  |
| São  Sebastião  |        | –  3,58  | 3,82 (0,88)    | 3,74 (0,89)    |
SP

65

Tabela 5. Média e correlação (entre parênteses) para o ciclo anual entre observações (boias
meteoceanográficas) e reanálises (ERA5 E CFSR).

| Boias        | Observações  | ERA5         | CFSR         |
| ------------ | ------------ | ------------ | ------------ |
| Cabo  frio   | -  RJ  4,25  | 5,06 (0,56)  | 4,12 (0,32)  |
| Antiga       |              |              |              |
| Itajaí – SC  | 7,66         | 5,45 (0,82)  | 5.45 (0,80)  |

| Niterói - RJ Antiga  | 3,21  | 2,87 (- 0,29)  | 2,49  (- 0,35)  |
| -------------------- | ----- | -------------- | --------------- |

| Santos – SP   | 7,60  | 5,73 (0,46)  | 5,83 (0,53)  |
| ------------- | ----- | ------------ | ------------ |
| Vitória – ES  | 7,05  | 5,90 (0,96)  | 5,09 (0,94)  |

Estes  trabalhos  mencionados  anteriormente  apresentam  validação  de
dados observados em relação com diversos produtos (reanálises, modelos, satélites
e entre outros) em várias regiões do globo. Na grande parte destes, a reanálise
CFSR mostra uma melhor representação dos dados observados. Todavia, como a
ERA5 é um produto mais recente, não existe muitos trabalhos  que utilizam seu
conjunto de dado. Por esta razão, existe uma dificuldade em comparar os resultados
discutidos nesta seção com a reanalise ERA5.

3.2.  Climatologia sazonal do vento a 10 m de altura

A Figura 18 mostra a climatologia sazonal, para o período de 1979-2015,
do vento a 10 m de altura para as reanálises CFSR e ERA5. Os padrões espaciais
de  direção  e  velocidade  do  vento  das  duas  reanálises  são  bem  similares,  com
diferenças de intensidade do vento em algumas localidades. No inverno e outono,
observam-se ventos menos intensos na RG1, o que condiz com a climatologia dos
dados  observados  nas  estações.  No  verão  e  primavera,  a  magnitude  do  vento
aumenta na área do estudo, mas alcança maior intensidade no verão.
O sistema mais evidente na Figura 18 é a ASAS que persiste nas quatro
estações do ano. O que muda de uma estação a outra é a sua posição e intensidade
66

(REBOITA et al., 2019). No verão, o centro da ASAS está em ~33º S, ou seja, situa-
se mais ao sul e a atuação simultânea da baixa térmica sobre a parte central da
América do Sul (REBOITA et al, 2010b e REBOITA et al, 2019) nesta estação
intensificam o vento a 10 m na costa do sudeste brasileiro. Isso pode favorecer a
intensificação dos ventos associados com os ciclones subtropicais, como será
discutido posteriormente. No outono a ASAS também está mais ao sul, mas como a
baixa térmica não está atuando nesta época, implicando em ventos são mais fracos,
pois não há o favorecimento do intenso gradiente horizontal de pressão. No inverno
a ASAS desloca-se para norte (27º S), a baixa térmica não está atuando, ou seja,
não há favorecimento do gradiente zonal de pressão, resultando em ventos mais
fracos na RG1. Na primavera, os padrões da ASAS são semelhantes ao verão, no
entanto como a baixa térmica ainda não está bem estabelecida como no verão, os
ventos se intensificam na região da costa sudeste, porém são ligeiramente mais
fracos se comparado com o verão.
Reboita et al. (2010b) e Reboita (2008) analisaram a sazonalidade dos
ventos em superfície (vento 10 m) entre o período 1990-1999 na reanálise do NCEP
que possui resolução horizontal mais grosseira. Estes estudos encontraram
sazonalidade dos ventos em superfície semelhantes ao do presente estudo na
região da costa do Brasil, ou seja, em latitudes subtropicais os ventos se
intensificam entre os meses de outubro até março e os ventos são mais intensos
próximo da costa sudeste do Brasil, principalmente na região RG1 onde atuam tanto
ciclones subtropicais como extratropicais (GOZZO et al., 2014). Outros trabalhos
como, Satyamurty e Mattos (1989), Reboita (2008) e Reboita et al., (2010b) mostram
ainda que durante o verão e primavera a esta região é também frontogenética,
favorecendo ventos mais fortes, principalmente na primavera.
67

a) a)
b)
c)
d)
Figura 18. Climatologia sazonal, para 1979-2015, da magnitude (sombreado, m s-1) e
direção do vento (vetores) a 10 m de altura para às reanálises CFSR (lado direito) e ERA5
(lado esquerdo): (a) verão, (b) outono, (c) inverno, (d) primavera. Em destaque a RG1
(retângulo em preto).
3.3. Climatologia de ciclones subtropicais
O rastreamento e classificação de ciclones subtropicais utilizados neste
estudo foram fornecidos por Gozzo. (2014) e Gozzo et al. (2017). Essas informações
permitem identificar várias características dos ciclones subtropicais como será
apresentado a seguir.
68

A quantidade de ciclones subtropicais que se formaram no sudoeste do
Oceano Atlântico Sul (SAO) no período 1979-2015, de acordo com as estações do
ano é apresentada na Figura 19. O verão tem a maior parte dos eventos, com
praticamente metade (46%). Em contrapartida, poucos casos ocorreram no inverno,
representando apenas 5,8% o que dificulta nas análises estatísticas por representar
uma amostra pequena de eventos, como será discutido adiante em seções
subsequentes. O outono é a segunda estação com grande ocorrência de ciclones
subtropicais, 72 eventos, que representam 28% do total.
Figura 19. Quantidade de ciclones subtropicais por estação do ano que se formaram no
SAO no período 1979-2015.
A variabilidade interanual dos ciclones subtropicais mostrada na Figura
20, não apresenta um padrão claramente definido. A frequência anual não apresenta
tendência de aumento ou diminuição de ciclones subtropicais. Nota-se, no entanto
alguns períodos distintos (com médias diferentes), com maior e menor frequência de
ciclones caracterizando alguma variabilidade de mais baixa frequência. Nos
períodos mais ativos de 1979-1984 e 2004-2010 têm-se uma média de,
respectivamente, ~ 8 e 10 (excluindo o ano de 2007 quando não se registrou
69

nenhum evento), enquanto nos períodos menos ativos a frequência anual cai para 6
(1986-2000) e 7 (2010-2015). Considerando a variabilidade interanual, alguns anos
apresentam maior e outra menor ocorrência de ciclones subtropicais. Por exemplo,
em 1983, 2001, 2004 e 2008 ocorreram mais de 10 eventos. E 2001 se destacou
como recorde desde que registrou o maior número de ciclones subtropicais em 37
anos, totalizando 15. Os anos com apenas 4 casos foram 1979, 1986, 2003 e 2014.
Figura 20. Série temporal da frequência anual (absoluta) de ciclones subtropicais que se
formaram no SAO no período 1979-2015.
Como mostra a Figura 21, a maior concentração das trajetórias dos
ciclones subtropicais para todo o período ocorre na RG1. Observa-se que a
densidade de trajetória de ciclone subtropical ocupa um grande faixa longitudinal,
entre 45-13oS do SAO. Considerando só a densidade ciclogenética (no momento de
formação do evento), Gozzo et al. (2014) mostraram maior frequência na RG1. Os
altos valores de densidade de trajetórias nesta região indicam o caráter semi-
estacionário dos ciclones subtropicais, como já discutido em Gozzo et al. (2014). No
entanto, ao longo do ciclo de vida, alguns ciclones subtropicais começam a se
70

dissipar ou ainda podem sofrer transição para ciclone extratropical (algumas raras
vezes também fazem transição para ciclone tropical no Atlântico Sul) ou até mesmo
dissipar por completo. A dissipação ocorre quando os sistemas estão se
movimentando para leste/sudeste. Por esta razão, a densidade de trajetória também
mostra baixos valores de densidade em grande parte a leste do SAO.
Figura 21. Densidade anual das trajetórias de ciclones subtropicais para o período 1979-
2015. A densidade considera o número de ciclones dividido pela área. RG1 é identificada
pelo retângulo preto.
A Figura 19 mostra que no verão ocorrem mais ciclones subtropicais, o
que se reflete na densidade das trajetórias mostrada na Figura 22. No verão,
primavera e outono a maior concentração de trajetórias situa-se dentro da RG1, no
seu setor norte e nordeste. Todavia, no inverno a maior ocorrência de trajetórias
encontra-se ao sul. Na primavera as trajetórias se estendem mais ao norte de SAO
em até 13º S próximo da costa da Bahia (Figura 22). Em consequência da baixa
frequência de ciclones subtropicais no inverno a densidade de trajetórias é menos
organizada e indica distâncias menores comparando com as outras estações do ano
(Figura 22).
De acordo com Gozzo et al. (2014) os ciclones subtropicais no verão são
mais estacionários, próximos da costa do que nas outras estações do ano, e isso
pode ser observado também na Figura 22.
71

a) b)
c) d)
Figura 22. Densidade sazonal das trajetórias dos ciclones subtropicais para o período 1979-
2015: (a) verão, (b) outono, (c) inverno, (d) primavera. A densidade considera o número de
ciclones dividido pela área para. RG1 é identificada pelo retângulo preto.
3.4. Ciclones subtropicais e vento a 10 m
As médias sazonais da velocidade do vento para os dias com ciclones
subtropicais são mostradas na Figura 23. Nota-se que no inverno a velocidade é
maior na costa do sul do Brasil, no centro-leste da região RG1. Como o tamanho da
amostra é menor, estes valores de velocidade seriam menos representativos. Já no
verão a amostra é maior e os ventos são também intensos na costa sudeste do
Brasil em dias de ciclones subtropicais. Então, considerando a maior
representatividade pode-se concluir que os ventos mais intensos na região próxima
da costa e RG1 ocorrem nesta estação. Por esta razão, nas próximas análises
muitos dos resultados para o inverno levarão à mesma conclusão. Como visto na
Figura 18 no verão o gradiente zonal de pressão é mais intenso, favorecendo
ventos intensos na RG1 e proximidades. Portanto, a presença climatológica de
ventos mais intensos no verão pode se somar aos dos ciclones subtropicais,
72

resultando assim nos campos da Figura 23 que mostram ventos mais intensos nesta
estação.
a)
b)
Figura 23. Intensidade média sazonal do vento a 10 m (sombreado, m s-1) para os dias com
ciclones tropicais no SAO no período 1979-2015 para: (a) CFSR, (b) ERA5. RG1 está
indicada pelo retângulo preto.
Para entender melhor o comportamento dos ventos nos dias com ciclones
subtropicais e comparar com a climatologia, a Figura 24 apresenta a anomalia
73

sazonal em relação aos dias com ciclones subtropicais e a média climatológica
(período 1979 - 2015).
O inverno apresenta anomalias positivas de velocidade principalmente a
leste da RG1, entre 40-10º W e 20-35ºS, e negativas ao sul e distante da RG1
(Figura 24). As anomalias positivas podem ser interpretadas como a intensidade
dos ventos são maiores em dias com ciclones subtropicais (análise Euleriana). De
uma forma geral, nas quatro estações do ano, as anomalias positivas de velocidade
ocorrem a leste da RG1, sendo que no verão e outono tais valores foram mais
expressivos. No verão e primavera as anomalias positivas de velocidade chegam
próximo da costa nordeste do Brasil, diferente do outono e inverno. Essas anomalias
positivas a leste da RG1 condizem com Gozzo (2014) que encontrou os ventos
máximos situados entre 350-450 km longe do centro do ciclone. Estudos de casos
de Reboita et al. (2019) mostraram também ventos mais intensos ocorrendo a leste
e sudeste de seis eventos de ciclone subtropical. O verão e outono apresentam
intensidade do vento mais intensa comparando os dias com ciclones subtropicais e a
climatologia (referencial Euleriano).
Como mostra a Figura 24, os padrões espaciais de anomalias positivas e
negativas de intensidade vento nas reanálises CFSR e ERA5 são bem similares,
com algumas diferenças em relação a intensidade da anomalia.
74

a)
b)
Figura 24. Anomalia de velocidade do vento (sombreado, m s-1) para os dias com ciclones
subtropicais (referencial Euleriano) para: (a) CFSR, (b) ERA5. A anomalia é calculada como
a diferença entre as composições para dias com ciclones e a climatologia da intensidade do
vento. RG1 indicada pelo retângulo preto.
75

A Figura 25 mostra a anomalia calculada através da velocidade
acumulada dividida pela quantidade de vezes, que a caixa encontrou o mesmo
ponto de grade. A anomalia positiva é compreendida como intensidade dos ventos
nos dias que os ciclones subtropicais foram superiores a climatologia. Com isso,
observa-se que no verão, as anomalias positivas abrangem grande parte da SAO.
No outono e primavera os padrões espaciais com anomalias positivas são
semelhantes aos apresentados na análise Euleriana da Figura 24.
De uma forma geral, os padrões das Figuras 24 e 25 são similares. No
entanto, a Figura 25 fornece a relação entre a intensidade do vento e a trajetória
dos sistemas, resultando nas regiões com anomalias positivas de algumas estações
do ano, mais abrangentes no SAO.
76

a)
b)
Figura 25. Anomalia da velocidade (sombreado, m s-1) seguindo a trajetória dos ciclones
subtropicais (referencial Lagrangeano) para: (a) CFSR, (b) ERA5. Anomalia calculada
considerando a velocidade acumulada dividida pela quantidade de vezes que passou no
mesmo lugar seguindo o centro do ciclone e climatologia. RG1 indicada pelo retângulo
preto.
Além da anomalia dos dias com ciclones, o acumulado da velocidade
seguindo as trajetórias dos ciclones em uma caixa de 20 º x 20 º é apresentado na
Figura 26. A região com maior intensidade seguindo a trajetória do sistema mostra
padrão espacial similar ao da Figura 24, com os ventos acumulados mais intensos à
leste e sudeste da RG1. Como o acumulado de velocidade segue as trajetórias dos
ciclones nota-se uma similaridade dos maiores valores com o de maior densidade de
77

trajetórias. No entanto, no caso do acumulado de vento a região de maiores
intensidades sempre se situam um pouco a leste/sudeste daquelas com maiores
densidades de trajetórias. Este resultado condiz com o que foi encontrado para a
anomalia de velocidade do vento em vários estudos de caso por Reboita et al.
(2019)
A diferença entre os campos de velocidade acumulada entre as
reanálises CFSR e ERA5 são pequenas (Figura 26). No caso do verão observa-se
que a região com maior intensidade do vento acumulado na CFSR é ligeiramente
maior do que no ERA5.
78

a)
b)
Figura 26. Velocidade acumulada (sombreado, m s-1) seguindo o centro do ciclone para: (a)
CFSR, (b) ERA5. RG1 indicada pelo retângulo preto.
3.5. Extremos da intensidade do vento
Para os extremos identificou-se o percentil de 95% da velocidade do
vento a 10 m de altura em cada ponto de grade das reanálises ERA5 e CFSR. A
Figura 27 mostra a média e o máximo destes eventos extremos calculados para
todo o período de análise (1979-2015) apenas para a CFSR, desde que o padrão
79

espacial da ERA5 é similar. Observa-se no campo da média dos eventos extremos
na RG1 valores superiores a 12 m s-1. Na região extratropical (entre 30-45ºS) a
média atinge magnitudes maiores, chegando a 19 m s-1. No campo do máximo, os
valores estão acima de 22 m s-1 na RG1, enquanto nos extratrópicos (30-45ºS)
esses máximos excedem 26 m s-1, chegando em algumas localidades a 41 m s-1. A
explicação mais provável para a intensidade dos extremos nas regiões extratropicais
são os ciclones extratropicais e os sistemas frontais que acontecem com grande
frequência nesse cinturão de latitudes. No entanto, na RG1, com maior
concentração dos ciclones subtropicais, tanto a média como o máximo atingem
valores consideravelmente altos. No leste do Rio Grande do Sul observa-se valores
altos para a magnitude média do vento (12-17 m s-1), possivelmente resultante dos
sistemas frontais e ciclones (extratropicais) que atuam praticamente o ano todo
nessa área.
80

a)
b)
Figura 27. Distribuição espacial dos eventos extremos (percentil de 95%) da magnitude do
vento a 10 m (m s-1) para a reanálise CFSR: (a) média, (b) máximo. Em destaque a RG1
(retângulo preto).
Os boxplots da série temporal de máximos de velocidade do vento a 10 m
seguindo a trajetória dos ciclones mostram que as maiores velocidades são
observadas no inverno para ambas as reanálises (Figura 28). No entanto, como
visto na Figura 19 o inverno tem apenas 15 eventos para todo o período de
climatologia (1979-2015), afetando as estatísticas apresentadas na Figura 28.
Todavia, o verão tem mais casos e a velocidade é a segunda maior, sendo assim
81

nesta estação o máximo de velocidade do vento seguindo a trajetória do sistema é
mais estatisticamente representativo e mais intenso, como também observado nas
climatologias campos espaciais (Figura 18).
De acordo com Guishard et al. (2009), Evans e Braun (2012) e Reboita et
al. (2017 a,b e 2019) os ciclones subtropicais exibem ventos sustentados maiores
que 17 m s-1 em 925 hPa durante o ciclo de vida. Na Figura 27 observa-se que a
média chega à 16 m s-1 no outono e no verão em 17 m s-1, o percentil de 75% em
todas as estações do ano ultrapassa 18 m s-1 para a reanálise CFSR. As
intensidades dos ventos na ERA5 são ligeiramente menores comparadas com a
reanálise CFSR. Na maioria das estações na ERA5, o percentil de 75 % e a média
são menores que 17 m s-1, exceto no inverno.
Ao todo foram utilizadas 4131 posições das trajetórias, que percorrem
todo ciclo de vida para cada ciclones subtropicais. Destas, na reanálise ERA5
existem 774 e 1376 para CFSR com velocidades maiores que 17 m s-1, ou seja, na
reanálise ERA5 os ventos máximos dentro da box seguindo a trajetória dos ciclones
são mais fracos, com menor número de ventos que são superiores ao limiar. Este
mesmo comportamento ocorre nas outras análises do vento a 10 m, principalmente
nos extremos.
Os boxplots da ERA5 e CFSR são similares, ambos mostram o mesmo
padrão de verão e inverno com ventos mais intensos, enquanto na primavera as
velocidades são menores. Entretanto, na reanálise ERA5 a intensidade do vento é
sempre menor em comparação a CFSR.
82

a) b)
b) d)
Figura 28. Boxplot da série temporal (1979-2015) de velocidade do vento a 10 m (m/s)
máximo extraída seguindo a trajetória do ciclone para ERA5 (verde) e CFSR (rosa) para: (a)
verão, (b) outono, (c) inverno, (d) primavera.
A Figura 29 mostra os boxplots dos extremos de intensidade do vento
que inclui todos os pontos de grade excedendo o percentil de 95% de velocidade do
vento (m s-1) a 10m seguindo as trajetórias dos ciclones. Os padrões de distribuições
para os eventos excedendo o percentil de 95% são semelhantes aos de máxima
intensidade do vento (Figura 28) discutidos anteriormente. No verão e outono maior
ocorrência de extremos de velocidades e no outono há um maior espalhamento
entre os percentis de 25% e 75%. Esta característica também é observada no
inverno, mas é importante notar a menor representatividade destas estatísticas em
função do pequeno número de eventos (apenas 15). Para a reanálise CFSR a
velocidade média dos eventos excedendo 95% chega a 16,29 e 15,82 m s-1,
respectivamente, no verão e outono (Tabela 6).
83

Além disso, encontrou a associação dos ciclones subtropicais com os
extremos de vento. Ao todo são 4131 trajetórias dos ciclones subtropicais ao longo
do período analisado (1979-2015). Para considerar que o extremo está associado
com cada trajetória, é preciso de pelo menos um extremo de vento dentro da caixa
20º X 20º, como foi visto no exemplo para o Ciclone Anita (Figura 9). Na reanálise
CFSR foi encontrado 3654 posições com pelo menos um extremo de vento, e na
ERA5 foram obtidos 3633 trajetórias com extremos. Com este resultado, percebe-se
que os ventos na ERA5 são menores que a reanálise CFSR.
A comparação entre as reanálises mostra distribuições similares para os
eventos extremos, onde o inverno registra maiores medianas e percentis de 75% e
25%, seguido do verão e outono (Figura 29). No entanto, nessas duas estações do
ano, tanto no CFSR e ERA5, os extremos são mais frequentes e intensos.
Comparativamente, as velocidades também para os extremos são menores na
reanálise ERA5 comparada com a CFSR. A comparação entre as médias sazonais
para os máximos e extremo de velocidade para cada reanálise é melhor visualizada
na Tabela 6. As diferenças de velocidade entre as reanálises são maiores no verão,
com extremos em média 1,56 m s-1 mais fracos na ERA5 do que na CFSR, e
menores no outono, onde a ERA5 apresenta extremos de velocidade apenas 0,71 m
s-1 mais fracos do que na CFSR. De forma geral, em todas as estações do ano as
correlações são ligeiramente maiores (entre 0,72 e 0,87) para os máximos do que
para os extremos (entre 0,64 e 0,81) de velocidade (Tabela 6). Considerando a
variação sazonal destes destas variáveis, as correlações entre as reanálises são
relativamente altas, com o menor valor (0,64) ocorrendo para os extremos de verão
e o maior (0,87) para os máximos de inverno.
84

a)
b)
d)
c)

Figura 29. Boxplot da série temporal de todos os pontos de grade excedendo o percentil de
95% de velocidade do vento (m s-1) a 10m extraída seguindo as trajetórias dos ciclones para
a ERA5 (boxplot verde) e CFSR (boxplot rosa): (a) verão, (b) outono, (c) inverno, (b)
primavera.

Tabela 6. Médias sazonais das intensidades (m s-1) máximas e extremos (acima do percentil
de 95%) do vento seguindo a trajetória dos ciclones subtropicais e correlações entre o
CFSR e ERA5 para estas séries. Valores em parênteses são para os extremos de
velocidade.

| Estações do ano  | CFSR           | ERA5           | Correlação   |
| ---------------- | -------------- | -------------- | ------------ |
| Verão            | 16,11 (16,26)  | 14,76 (14,69)  | 0,72 (0,64)  |
| Outono           | 15,68 (15,82)  | 14,97 (15,09)  | 0,77 (0,70)  |
| Inverno          | 17,03 (17,44)  | 15,78 (16,31)  | 0,87 (0,81)  |
| Primavera        | 15,75 (15,71)  | 14,61(14,44)   | 0,77 (0,69)  |

85

Figura 30. Média anual para as velocidades máximas (linhas contínuas) e extremos (acima
do percentil de 95%; linhas tracejadas) do vento em 10 m a cada 6 hora no box de 20º x 20º
seguindo os centros dos ciclones subtropicais para a ERA5 (verde) e CFSR (rosa).
A série temporal para o valor médio anual das velocidades dos ventos
máximas e extremos seguindo as trajetórias dos sistemas é apresentada na Figura
30. A Figura 20 apresenta a quantidade de ciclones por ano que pode ser
comparada com a Figura 30. Em alguns anos a quantidade de eventos é menor
coincidindo com menor velocidade média anual (máxima e extrema), como nos anos
de 1986, 1988 e 2003. No entanto, o que mais se destaca é quando ocorre o oposto,
ou seja, um menor número de sistemas resultando em maiores velocidades, pois
mostra que mesmo com poucos ciclones subtropicais a velocidade é intensa. Isto
ocorre em 1979, que com apenas 4 casos de ciclones a velocidade média chega à
17,50 m s-1 no CFSR (extremo e máximo) e 14,25 m s-1 (extremo) e 14,80 m s-1
(máximo) na ERA5.
Embora as duas reanálises apresentem variabilidade interanual
semelhante (máximos e mínimos coincidindo no tempo) a diferença de intensidade
(que em alguns anos ultrapassa 2 m s-1, como em 2013) é discrepante em todo o
período da série temporal da média anual. Esta discrepância ocorre tanto para a
intensidade máxima como a intensidade dos extremos do vento a 10 m (Figura 30).
86

a)
b)
Figura 31. Anomalia sazonal de velocidade do vento a 10 m considerando os extremos de
velocidade nos dias de ciclones subtropicais menos a climatologia de extremos de
velocidade (sombreado, m s-1): (a) CFSR, (b) ERA5. RG1 indicada pelo retângulo preto.
A Figura 31 apresenta a anomalia de velocidade do vento a 10 m para de
extremos de vento nos dias de ciclones subtropicais (calculada como a diferença
entre a média de extremos em dias de ciclone e a climatologia de extremos). Como
87

regra geral, na RG1 ou nas imediações a ocorrência de ciclones subtropicais está
associada à extremos de velocidades do vento a 10 m superiores aos extremos
climatológicos desde que a anomalia é majoritariamente positiva (Figura 31). Ao
mesmo tempo, períodos de ciclones subtropicais estão associados a ventos
extremos mais fracos, principalmente ao sul da RG1.
No outono as anomalias positivas situam-se fora da RG1, pois a maioria
dos sistemas nesta época localizam-se mais a leste em grande parte do seu ciclo de
vida, como mostrado na densidade das trajetórias (Figura 22). No centro-sudeste da
RG1 há uma região de maiores anomalias positivas. A localidade de maior
intensidade de vento (anomalia positiva) localiza-se a leste do segundo maior núcleo
de densidade de trajetórias, desde que o primeiro se encontra dentro da RG1. A
extensão de anomalia positiva no outono é mais abrangente comparado com as
demais estações do ano.
A maior densidade das trajetórias no inverno é observada mais próxima
do sul do Brasil e a leste do SAO (20-25oS e 30-20oW), regiões onde se observam
núcleos de anomalias de intensidade de extremos positivas (Figura 31).
Diferentemente das outras estações do ano a anomalia positiva não ocorre a leste
da região de maior concentração de trajetórias dos ciclones. O núcleo com maior
intensidade de extremo de velocidade situa-se na costa de Santa Catarina e Paraná.
As anomalias positivas dos extremos (Figura 31) no verão ocorrem dentro
da RG1 e se estendem até a costa da Bahia, o que condiz com a climatologia de
velocidade do vento (Figura 24). Porém, a anomalia positiva dentro da RG1 é mais
próxima da costa do que mostra na climatologia (Figura 24). O núcleo de anomalia
positiva dentro da RG1 está na mesma região de maior densidade das trajetórias de
ciclones da Figura 22. O segundo núcleo, que chega até a costa da Bahia, também
coincide a com região de maior densidade de trajetórias de ciclones. A anomalia
positiva de velocidade não ultrapassa 1 m s-1 no verão. Nesta estação, o padrão de
anomalia de extremos difere daquele que considera a velocidade do vento em dias
de ciclones subtropicais apresentado na Figura 24. Neste caso, anomalias positivas
de velocidade situam-se à leste da RG1, enquanto nos extremos a maior
concentração das anomalias positiva coincidem dentro d RG1, ou seja, com a
densidade das trajetórias.
Na primavera os extremos de velocidade são intensos na região à
nordeste da RG1 e também no meio do SAO, em aproximadamente 20º-30ºW e 30º-
88

40ºS. Na anomalia de velocidade total apresentada na Figura 24 os núcleos com
valores positivos também se situam à nordeste da RG1, condizentes com a
anomalias de extremos.
Na reanálise ERA5 o padrão de anomalias de velocidade é similar ao da
CFSR, no entanto em algumas localidades mais específicas, a região com extremos
é maior e estes são mais intensos, principalmente nas anomalias positivas (Figura
31). Existe maior concentração de anomalias negativas na reanálise CFSR do que
na ERA5, como por exemplo, na costa sul do Rio Grande do Sul e Uruguai no
inverno e outono.
A Figura 32 apresenta a anomalia os extremos de ventos seguindo os
ciclones subtropicais em relação a climatologia dos extremos de vento, ou seja, a
construção é a mesma da Figura 25, porém, utilizando os extremos de vento. Nesta
análise (Lagrangeana) observa-se resultados similares com a anomalia
considerando apenas os dias com ciclones subtropicais (Euleriana) (Figura 31). O
inverno apresentou anomalias positivas em regiões com densidade de trajetórias
dos ciclones. No verão os valores positivos se encontram dentro da RG1,
diferentemente do que foi encontrado nos resultados da intensidade do vento.
89

a)
b)
Figura 32. Anomalia dos extremos de velocidade (sombreado, m s-1) ao longo das
trajetórias dos ciclones: (a) CFSR, (b) ERA5. A anomalia representa a diferença entre
velocidade dos extremos acumulados dividida pela quantidade de vezes que os ciclones
passaram no mesmo lugar seguindo as trajetórias e a climatologia dos extremos. RG1
indicada pelo retângulo preto.
O acumulado de extremos de vento é visualizado na Figura 33. Os
padrões com os valores maiores da intensidade do vento acumulado são parecidos
com outros campos, como nas Figuras 26 e 32. O inverno apresenta regiões de
90

maiores acumulados (30º-40ºS e 20º-30ºW). Na primavera, as regiões com maiores
acumulados coincidem com a densidade das trajetórias (Figura 22). A densidade de
trajetórias mostra que os ciclones se estendem em regiões mais ao norte do Brasil,
favorecendo diretamente no acumulado dos extremos de vento. No verão e outono,
os maiores acumulados de extremos da intensidade do vento estão localizados a
leste da RG1, como é visto nas outras análises (Figuras 24, 25, 31 e 32).
91

a)
b)
Figura 33. Extremos de velocidade acumulada (sombreado, m s-1) seguindo a trajetória dos
ciclones subtropicais para: (a) CFSR, (b) ERA5. RG1 indicada pelo retângulo preto.
A Figura 34 mostra a distância em quilômetros do centro do sistema e
que o extremo foi encontrado, e com isso observa-se uma maior parte dos ventos
extremos está em um raio de 400-500 km aproximadamente. Gozzo (2014) mostra
que a maior parte dos ciclones de transição (de extratropical para subtropical ou
vice-versa), sendo 75% EraInterim e 67% no NCEP1 atinge a intensidade máxima
92

na fase subtropical com ventos máximos entre 18 e 20 m s-1 em um raio de 350-450
km. Ou seja, os ventos extremos corroboram com o que foi encontrado em Gozzo et
al. (2014). Em Reboita et al. (2019) também mostram que os ventos máximos
ocorrem na borda do sistema.
a)
b)
Figura 34. Histograma de frequência da distância entre os extremos e o centro do ciclone
subtropical. (a) CFSR e (b) ERA5.
93

3.6. Composições
Como visto para os máximos de velocidade (Figura 28) seguindo a
trajetória, e na velocidade acumulada e anomalia (Figuras 24 e 25), no inverno as
velocidades associadas aos ciclones são maiores. No entanto, como a amostra é
menor optou-se por analisar as composições no verão desde que apresenta uma
maior amostra, também ventos intensos, o que pode estar relacionado com a
intensidade dos ciclones. A Figura 35 mostra que, no verão os ciclones subtropicais
atingem menores valores de pressão central, indicando sistemas mais intensos.
Tanto a mediana como os intervalos interquartis, também o grande número de
extremos inferiores, indicam menores valores de pressão central nos ciclones
subtropicais durante o verão. A mediana de pressão central é superior a 1010 hPa
em todas as estações do ano indicando que os ciclones subtropicais são
relativamente fracos. No entanto, alguns eventos podem se intensificar ao longo do
ciclo de vida e atingir pressão central inferior a 990 hPa, principalmente no verão.
Por esta razão, para entender melhor o padrão espacial associado aos ciclones
subtropicais é analisada as composições no verão e outono.
Figura 35. Boxplot da pressão central (hPa) seguindo a trajetória dos ciclones subtropicais.
94

As composições para o verão mostram uma baixa pressão dentro da RG1
desde a formação (00h) até 36 horas (+36h) após formado. (Figura 36a). A pressão
dentro da RG1 praticamente não muda de valor, em torno de 1011 hPa, no decorrer
do tempo. Além disso, no setor sudoeste da RG1, próximo da costa do Paraná e
Santa Catarina, há uma baixa pressão alongada que conforme passa o tempo se
intensifica, e apresenta também uma isóbara fechada de 1011 hPa em +24h.
O núcleo de maior intensidade do vento se movimenta ligeiramente para
leste e atinge valores máximos em +12h, chegando ao valor médio de 9 m s-1. A
região de vento mais intenso é observada na região leste e sudeste do centro da
baixa pressão (Figura 36a). Este centro se mantém ancorado próximo da costa
sudeste do Brasil até +36h indicando o caráter semi-estacionário dos ciclones
subtropicais que se formam nesta região no verão. No outono (Figura 36b) a baixa
pressão dentro da RG1 é mais alongada do que no verão. A velocidade do vento,
como no verão, é mais intensa em +12h, porém a região da intensidade máxima
está mais ao sul da RG1 do que no verão.
95

a)
b)
Figura 36. Composições da velocidade do vento a 10 m (sombreado, m s-1) e Pressão ao
Nível Médio do Mar (PNMM, contorno, hPa) na gênese (00 h), +12 h, + 24 h e + 36h (a) para
o verão e (b) outono. RG1 (retângulo preto).
Reboita et al. (2010b) estudaram a climatologia dos fluxos de calor latente
e sensível sobre o SAO e, encontraram que estes são maiores durante o outono e
inverno próximo da região analisada neste trabalho. Isso ocorre, principalmente, pela
contribuição do gradiente vertical de umidade na interface ar-mar uma vez que os
ventos estão fracos nestas estações do ano. Além disso, ocorrem incursões de
96

massas de ar mais frias e secas do interior do continente sobre o oceano que
encontram a superfície do mar mais quente (na região a TSM atinge maiores valores
em abril).
Dada a importância da transferência de energia na interface ar-mar para
ciclones subtropicais, a Figura 37 mostra a somatória dos máximos valores dos
fluxos (calor latente e sensível) seguindo o centro do ciclone para cada estação do
ano. Nota-se que no outono os fluxos de calor latente e sensível são mais intensos,
seguido do verão (Figura 37). Estes fluxos máximos no outono apresentam
mediana próxima de 360 W m e exceto no inverno nota-se a presença de um
-2
grande número de valores extremos.
Figura 37. Boxplot da série temporal dos valores máximos dos fluxos (soma de calor latente
e sensível em W m-2) extraídos seguindo a trajetória dos ciclones subtropicais da reanálise
CFSR (período 1979-2015).
As composições para a somatória dos fluxos de calor latente e sensível
mostram fluxos mais intensos na costa do Brasil (Figura 38b) e na região oeste da
ASAS (Figura 38a). No verão, durante a formação dos ciclones, os fluxos estão em
torno de 140 W m-2 na maior parte da RG1. Entre o horário de formação (00h) até 12
97

horas (+12h) após nota-se que estes fluxos de calor aumentam (acima de 160 W m-
2) na RG1 o que pode estar associado à fase inicial de intensificação da circulação
associada ao ciclone (Figura 38a). Este mesmo processo de intensificação da
circulação atua para reduzir os fluxos de calor à medida que o ciclone evolui no
tempo. Isto ocorre devido ao caráter semi-estacionário destes sistemas (Figura 36),
isto é, os ventos intensos permanecem atuando em uma mesma área por um longo
tempo. Com isto promovem mistura na superfície do oceano, com consequente
afloramento de água mais fria para a superfície agindo tanto para diminuir a TSM
como os fluxos turbulentos de calor na interface ar-mar. No outono (Figura 38b), os
fluxos de calor latente e sensível são mais intensos próximo da costa comparado
com o verão, porém perto da ASAS os fluxos são menos intensos. No horário da
gênese (00 h) os fluxos são mais intensos no outono próximo da costa do Brasil
(Figura 38b), entre 24 e 36 h os fluxos na região vão diminuindo.
De acordo com Gozzo et al. (2017) o transporte de umidade de fontes
remotas, como a ASAS, somado com os fluxos de calor latente e sensível no local
de formação são fatores importantes para o desenvolvimento dos ciclones
subtropicais na RG1. No verão, como já visto na climatologia (Figura 18), a ASAS
influencia no intenso gradiente zonal de pressão conjuntamente com a baixa
térmica, proporcionando ventos mais intensos. Além disso, de acordo com Gozzo et
al. (2014) os fatores associados aos desenvolvimentos dos ciclones subtropicais
mudam entre o outono e o verão. No verão Gozzo et al. (2014) observaram a
presença de uma região (a nordeste da RG1) com fluxos de calor latente e sensível
mais intensos, o que também é capturado nas composições da Figura 38a. A
umidade do oceano nesta região é transferida para atmosfera pelos ventos mais
intensos e transportada para a RG1 pelo giro anticiclônico da ASAS. Quando a TSM
é menor na RG1, esse transporte de umidade é o principal fator para o
desenvolvimento dos ciclones subtropicais, pois os fluxos de calor latente e sensível
não são tão intensos na própria RG1 (Figura 38a).
No outono os ciclones se formam em águas mais quentes. Os fluxos
locais são mais intensos na RG1, fornecendo energia adicional para o
desenvolvimento dos ciclones subtropicais (GOZZO et al., 2014), este resultado
também foi visto na Figura 38b das composições dos fluxos de calor latente e
sensível para os ciclones subtropicais. Os fluxos mais intensos no outono estão
associados às massas de ar frio e seco do interior do continente e sobre o oceano
98

com a TSM mais quente na região, favorecendo os fluxos de calor latente e sensível.
Os ventos climatologicamente são mais fracos, pois no outono o gradiente zonal de
pressão entre o continente e o oceano é enfraquecido. Isto ocorre porque a baixa
térmica não está atuando e a ASAS se encontra mais ao norte. Desta forma, o
principal fator influenciando os ventos mais intensos próximo à superfície em dias
com ciclones subtropicais no outono seriam os próprios ciclones, diferentemente do
verão.
a)
b)
Figura 38. Composições dos fluxos de calor latente e sensível (latente + sensível)
(sombreado, W m-2) para os ciclones subtropicais, na gênese (00 h), +12 h, + 24 h e + 36h
(a) para o verão e (b) outono. RG1 (retângulo preto).
99

4. CONCLUSÕES
Este trabalho analisou a relação entre os ventos e extremos de
velocidade próximo à superfície (a 10 m de altura) com ciclones subtropicais no
sudoeste do Oceano Atlântico Sul no período de 1979-2015. Além disso, também
comparou as observações do vento próximo à superfície de estações
meteorológicas e boias meteoceanográficas com as reanálises ERA5 E CFSR, que
são mais recentes e possuem grade horizontal mais refinada. Por esta razão, o
trabalho foi subdividido em duas etapas. Na primeira, investigou-se qual reanálise
tem maior habilidade em reproduzir as observações locais. A segunda etapa
consistiu em relacionar os ventos e extremos de vento com os ciclones subtropicais,
utilizando as reanálises CFSR e ERA5.
Para comparação dos dados observados e reanálises na região do estudo
(costa sudeste do Brasil) foram utilizadas nove estações meteorológicas e cinco
boias meteoceanográficas com observações do vento em superfície. As análises
utilizaram o diagrama de Taylor, média anual e ciclo anual. Ao longo do período, a
velocidade do vento é superestimada nas reanálises em comparação com estações
meteorológicas, em contrapartida as mesmas subestimam a velocidade observada
nas boias. Entre as nove estações, em cinco delas as correlações para valores de
velocidade média diária foram maiores que 0,5 e RMSE menor que 1,0 m/s. No caso
das boias, três destas as correlações foram superiores a 0,5, mas os RMSEs
superam 1,0 m/s. Isso se deve ao fato de que as velocidades nas boias, que estão
em mar aberto, são maiores do que sobre o continente.
Na comparação com as observações locais as duas reanálises
apresentam estatísticas similares e com número de observações pequeno (9
estações e cinco boias) se conclui que ambas representam satisfatoriamente as
observações locais. Além disso, não há outros trabalhos que comparem as mesmas
reanálises, pois a ERA5 é um produto mais recente. Porém, estes trabalhos ao
compararem com a antecessora da ERA5 (ERA-Interim) mostram melhor
desempenho da reanálise CFSR.
Além de comparar os ventos das estações com as reanálises, analisou-se
o comportamento do vento na observação (costa e oceano) e com as reanálises
(espacialmente). As observações indicaram que no inverno os ventos são mais
100

fracos e mais intensos na primavera e verão, exceto em Itajaí (final do inverno e
começo da primavera). Nas reanálises (espacialmente) a climatologia mostra que as
estações quentes (primavera e verão) os ventos são mais intensos no leste do
sudeste do Brasil, região denominada de RG1, favorecido pelo forte gradiente zonal
de pressão entre o anticiclone subtropical do Atlântico Sul, que está posicionado
mais ao sul e a baixa térmica na parte central do continente. No inverno e outono, os
ventos na RG1 enfraquecem, pois não há o favorecimento do intenso gradiente
zonal de pressão mencionado para primavera-verão.
A relação da intensidade e extremos de vento próximo à superfície com
os ciclones subtropicais considerou dois procedimentos: seguindo a trajetória do
sistema (Lagrangeana); também considerando apenas os dias com ciclones
(Euleriana). De uma forma geral, a intensidade do vento em dias com ciclone
subtropical mostra que, no inverno, as velocidades são maiores, mas a quantidade
de eventos é menor (apenas 15 ciclones), a estimativa estatística pode estar
comprometendo a média. Por outro lado, em seguida identificou-se o verão com
velocidades intensas e com mais casos, ou seja, fornece maior confiança de que na
estação de verão (118 eventos) a intensidade do vento é maior em dias com
ciclones subtropicais. Estes sistemas ocorrem com maior frequência durante essa
estação do ano. Em contrapartida, o outono é a segunda maior velocidade nas
reanálises e, a segunda em ocorrência (72 eventos) de ciclones subtropicais.
O método Euleriano (considerando apenas as datas com ciclones
subtropicais) mostra que a intensidade do vento no verão e o outono são maiores.
Além disso, os ventos intensos são observados no setor leste da RG1 para as
estações de outono, verão e primavera. A análise Lagrangeana (a intensidade do
vento seguindo o centro do ciclone) indica que no verão e outono as velocidades dos
ventos são maiores. A série temporal seguindo os centros dos ciclones subtropicais
mostra maiores velocidades no inverno, porém como já mencionado há problemas
com o tamanho da amostra, então considerou o verão como mais representativo da
estação com velocidade maior.
Em termos de extremos de vento notou-se algumas diferenças em
relação à intensidade considerando todos os eventos e horários. As anomalias
(Euleriano) nos extremos de vento apresentam valores positivos na região de maior
densidade de trajetórias de ciclones no verão, diferente da anomalia da intensidade
do vento que mostra valores positivos a leste da RG1. Todavia, no outono as
101

anomalias positivas de velocidade extremas são maiores do que no verão,
diferentemente do que ocorre na anomalia da intensidade do vento. Isso ocorre pois,
os ciclones subtropicais no outono, são mais intensos e organizados, contribuindo
para maiores extremos de vento. No inverno, como a densidade das trajetórias são
mais a sul do que as outras estações do ano os extremos de velocidade situam-se
na costa do sul do Brasil.
No verão e outono as intensidades do vento e de extremos do vento são
maiores. No verão a climatologia mostra que os ventos já são mais intensos na
região de estudo, podendo favorecer uma maior intensidade, além dos ciclones
subtropicais. Por outro lado, no outono a climatologia mostra ventos mais fracos na
região de estudo, ou seja, a maior intensidade é favorecida apenas pelos ciclones
subtropicais. No outono os ciclones subtropicais são mais intensos e organizados,
pois ocorrem sobre temperatura da superfície do mar (TSM) mais alta com
consequente intensificação dos fluxos de calor (latente e sensível) na RG1, que
favorece o transporte do gradiente vertical de umidade entre oceano-atmosfera na
própria região de maior concentração destes sistemas. No verão, os ciclones
subtropicais se desenvolvem quando a TSM ainda está aumentando e o transporte
de umidade é realizado pelo giro anticiclônico no setor nordeste do anticiclone
subtropical do Atlântico Sul. Contudo, estas diferenças sazonais indicam que os
ciclones subtropicais são mais organizados e mais intensos no outono.
102

5. PROPOSTAS PARA TRABALHOS FUTUROS
O estudo apresentado nesta dissertação mostra a relação da intensidade
e extremos de vento com os ciclones subtropicais para cada estação do ano. Além
disso, valida as duas reanálises mais recentes com dados observados na região do
estudo. Esta pesquisa é importante e tem o diferencial de entender os ventos com
os ciclones subtropicais, tais sistemas afetam a sociedade e economia, por se
desenvolveram próximo da costa, trazendo ventos intensos. Seguindo o mesmo
raciocínio, os próximos passos desta pesquisa são:
• Correlacionar os ciclones subtropicais e oscilações de baixa frequência e
entender sua dinâmica.
• Aplicar a mesma metodologia de extremos para outras variáveis que são
influenciadas pelos ciclones subtropicais, como a precipitação;
• Correlacionar os possíveis padrões encontrados com os casos de extremos
para os ventos e precipitação, para entender melhor como essas oscilações
afetam os ciclones e as variáveis.
• Aplicar análises similares para experimentos numéricos no mesmo período e
para projeções de um futuro próximo e distante nos cenários de mudanças
climáticas para ventos, extremos de ventos, precipitação e extremos de
precipitação.
103

REFERÊNCIAS BIBLIOGRÁFICAS
ANDRADE, K. M. Climatologia e Comportamento dos Sistemas Frontais Sobre a
América do Sul. 187. P. Dissertação (Mestrado em Meteorologia) - Instituto Nacional
de Pesquisas Espaciais (INPE), 2005.
BETTS, A. K.; CHAN, D. Z; DESJARDINS, R. L. Near-Surface Biases in ERA5 Over
the Canadian Prairies. Frontiers in Environmental Science, v. 7, n. 129, 2019.
BITENCOURT, D. P.; GAN, M.; ACEVEDO, O. C.; FUENTES, M. V.; MUZA, M. N.;
RODRIGUES, M. L.; QUADRO, M. L. F. Relating Winds along the Southern Brazilian
Coast to Extratropical Cyclones. Meteorological Applications, v. 18.2, p. 223-29,
2010.
BJERKNES, J. On the structure of moving cyclones. Geofysiske Publikasjoner, v.
1, n. 2, p. 1-8, 1919
BJERKNESS, J; SOLBERG, H. Life Cycles of Cyclones and Polar Front Theory of
Atmospheric Circulation. Geofys. Publ, v. 3, n. 1, p. 3-18, 1922.
CARVALHO, D.; ROCHA, A.; GÓMEZ, G. M.; SANTOS, C. S. Offshore Wind Energy
Resource Simulation Forced by Different Reanalyses: Comparison with Observed
Data in the Iberian Peninsula. Applied Energy, vol. 134, 2014, p. 57–64, 2014
doi:10.1016/j.apenergy.2014.08.018.
CARUSO, S. J.; BUSINGER, S. Subtropical Cyclogenesis over the Central North
Pacific*. Weather and Forecasting, v. 21(2), p. 193-205. doi:10.1175/waf914.1,
2006.
CHARNEY, J. G. The Dynamics of Long Waves in a Baroclinic Westerly Currents.
Journal of Meteorology, p. 135-162, 1947.
CHARNEY, J. G.; ELIASSEN, A. On the Growth of the Hurricane Depression.
Journal of the Atmospheric Sciences, v. 21, n. 1, p. 68–75, 1964.
CRESSMAN, G. P.: An Operational Objective Analysis System. Mon. Wea. Rev., v.
7 (10), p. 367-374, 1959.
da SILVA, M. C. L. Simulações Numéricas do Ciclone Catarina: Impacto dos Efeitos
Subgrade, Resolução e Assimilação de Dados. 55f. Tese (Doutorado em Ciências
Atmosféricas) – Instituto de Astronomia, Geofísica e Ciências Atmosféricas da
Universidade de São Paulo, 2014.
da SILVA, N. P. Extremos de Vento Sobre o Oeste do Oceano Atlântico Sul: Análise
Direcional das Ocorrências, 35f. Dissertação (Mestrado em Ciências Atmosféricas) -
104

Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São
Paulo, 2013.
da ROCHA, R. P.; REBOITA, M. S.; GOZZO, L. F.; DUTRA, L. M. M.; DE JESUS, E.
M. Subtropical cyclones over the oceanic basins: a review. Annals of the New York
Academy of Sciences, p. 138-156, 2018.
de ABREU, R, C., da ROCHA, R. P. Experimentos numéricos para o ciclone
subtropical “Anita” com o modelo WRF. Ciência e Natura, Santa Maria, v. 37 Ed.
Especial SIC, p. 69 – 74, 2015.
DEMARIA, M.; KNAFF, J. A.; CONNELL, B. H. tropical cyclone genesis parameter
for the tropical Atlantic. Weather Forecasting, v. 16, p. 219-233, 2001.
DERECZYNSKI, C. P.; LOPESS, Í. R.; CARVALHO, N. O.; SILVA, M. G. A. J.;
GROSSMAN, K. S.; MARTINS, R. P. Climatology of Espírito Santo and the Northern
Campos Basin, Offshore Southeast Brazil. Anuário Do Instituto De Geociências -
UFRJ, v. 42, n. 1, p. 386–401., doi:10.11137/2019_1_386_401, 2019.
DIAS PINTO, J. R.; REBOITA, M, S.; da ROCHA, R. P. Synoptic and Dynamical
Analysis of Subtropical Cyclone Anita (2010) and Its Potential for Tropical Transition
over the South Atlantic Ocean. Journal of Geophysical Research: Atmospheres,
v. 118, n. 19, 2013, doi:10.1002/jgrd.50830.
DUTRA, L. M. M, 2012: Ciclones Subtropicais sobre o Atlântico Sul: análise da
estrutura dinâmica de eventos. Dissertação (Mestrado em Meteorologia). Instituto de
Astronomia, Geofísica e Ciências Atmosféricas (IAG), Universidade de São Paulo,
São Paulo, 136f.
DUTRA, L. M., da ROCHA, R. P., LEE, R. W., PERES, J. R.; de CAMARGO, R.
Structure and evolution of subtropical cyclone Anita as evaluated by heat and
vorticity budgets. Q.J.R. Meteorol. Soc., v. 143, p. 1539-1553, 2017,
doi:10.1002/qj.3024
EADY, E.T. Long Waves and Cyclones Waves. Tellus, v. 1, n. 3, p. 35-52, 1949.
EMANUEL, K. A. An air-sea interaction theory for tropical cyclones. Part I. J. Atmos.
Sci, 1986, 43:585q50.
Emanuel, K. A. The Theory Of Hurricanes. Annual Review of Fluid Mechanics, v.
23. p. 179-196, 1991.
EVANS, J. L.; BRAUN, A. A Climatology of Subtropical Cyclones in the South
Atlantic. Journal of Climate, v.25, p. 7328-7340, 2012.
105

EVANS, J. L; GUISHARD, M. P. GUISHARD. Atlantic subtropical storms. Part I:
Diagnostic criteria and composite analysis. Monthly Weather Review, v. 137(7), p.
2065-2080, 2009.
Evans, J. L.; HART, R.Objective indicators of the life cycle evolution of extratropical
transition for Atlantic tropical cyclones. Mon. Wea. Rev., v. 131, p. 909–925, 2003.
GAN, M. A.; RAO, V. B. Surface Cyclogenesis over South America. Monthly
Weather Review, v. 119, p. 1293-1302, 1991.
GOZZO, Luiz. F. Ciclones Subtropicais Sobre o Sudoeste do Atlântico Sul:
Climatologia e Fontes de Umidade, 77 f. Tese (Doutorado em Ciências Atmosféricas)
- Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São
Paulo, 2014.
GOZZO, L. F.; da ROCHA, R. P.; REBOITA, M. S; SUGAHARA, S. Subtropical
Cyclones over the Southwestern South Atlantic: Climatological Aspects and Case
Study. J. Climate, v. 27, p. 8543–8562, 2014.
GOZZO, L. F., da ROCHA, R. P; GIMENO, L.; DRUMOND, A. Climatology and
numerical case study of moisture sources associated with subtropical cyclogenesis
over the southwestern Atlantic Ocean. Journal of Geophysical Research:
Atmospheres, v. 122, p. 5636–5653, 2017
GUISHARD, M. P., 2006: Atlantic subtropical storms: Climatology and
characteristics. Tese (Doutorado em Meteorologia), Dept. of Meteorology, The
Pennsylvania State University, University Park, PA, 158 pp.
GUISHARD, M. P.; EVANS, J. L; HART, R. E. Atlantic Subtropical Storms. Part II:
Climatology. Journal of Climate, v. 22, p. 3574-3594, 2009.
GRAY, W. M. Global view of the origin of tropical disturbances and storms. Monthly
Weather Review, v. 96, p. 669-700, 1968.
HART, R. E. A cyclone phase space derived from thermal wind and thermal
asymmetry. Monthly Weather Review, v. 131, p. 585–616, 2003.
HART, R. E.; EVANS, J. L. A Climatology of the Extratropical Transition of Atlantic
Tropical Cyclones. Journal of Climate, v. 14, p. 546–564, 2001,
https://doi.org/10.1175/1520-0442(2001)014<0546:ACOTET>2.0.CO;2
HERSBACH, H.; DEE, D. ERA5 reanalysis is in production. ECMWF Newsl, n. 147,
v. 7, 2016
HOLLAND, G. J.; LYNCH, A. H.; LESLIE, L. M. Australian East-Coast Cyclones. Part
I: Synoptic Overview and Case Study. Monthly Weather Review, v. 115, p. 3024-
3036, 1987.
106

HOSKINS, B. J.; HODGES, K. I. A New Perspective on Southern Hemisphere Storm
Tracks. Journal of Climate, v.18.20, p. 4108-129, 2005.
KIM, H. G.; KIM, J. Y.; KANG, Y, H. Comparative Evaluation of the Third-Generation
Reanalysis Data for Wind Resource Assessment of the Southwestern Offshore in
South Korea. Atmosphere, v. 9, n. 2, p. 73, 2018.
MCTAGGART-COWAN, R.; BOSART, L. F.; DAVIS, C. A.; ATALLAH, E. H.;
GYAKUM, J. R.; EMANUEL, K. A. Analysis of Hurricane Catarina (2004). Monthly
Weather Review, v. 134, p. 3029-3053, 2006.
MICALICHEN, M, L. M. de M.; DIAS, N. L. D. C. Análise comparativa da velocidade
do vento e da temperatura do ar, entre dados gerados por reanálises meteorológicas
e dados observacionais na região de Minas Gerais. Ciência e Natura, v. 40, p. 20,
2018.
MURRAY, R. J.; SIMMONDS, I. A numerical scheme for tracking cyclone centers
from digital data. Part I: Development and operation of the scheme. Aust. Meteor.
Mag., v, 39, p. 155-166, 1991.
PALMEN, E., 1948: On the formation and structure of tropical cyclones. Geophysics,
v. 3, p. 26–38, 1948
PEREIRA, N. Impactos dos Ciclones Extratropicais em Eventos Extremos de
Precipitação na Bacia do Rio Prata, 45f. Dissertação (Mestrado em Ciências
Atmosféricas) – Instituto de Astronomia, Geofísica e Ciências Atmosféricas da
Universidade de São Paulo, 2014.
PENG, G., ZHANG, H. M.; FRANK, H.P.; BIDLOT, J.R.; HIGAKI, M; STEVENS, S;
HANKINS, W. R. Hankins. Evaluation of various surface wind products with
OceanSITES buoy measurements. Weather and Forecasting, v. 28, p. 1281–1303.
2013.
PETTERSSEN, S.; SMEBYE, S. J. On the development of extratropical cyclones.
Quart. J. Roy. Meteorol. Soc., v. 97 (414), p. 457-482, 1971.
OLIVEIRA, K. S. S., QUARESMA, V. da S. Condições típicas de vento sobre a
região marinha adjacente à costa do Espírito Santo. Revista Brasileira de
Climatologia, v. 22, p. 501-523, 2018.
OOYAMA, K. Conceptual evolution of the theory and modeling of the tropical
cyclone. J. Meteor. Soc. Japan, v. 60, p. 369-379, 1982.
RADINOVIC, D. On the development of orographic cyclones. Tech. Rep., n.50,
1985.
107

REBOITA, M. S. Ciclones Extratropicais sobre o Atlântico Sul: Simulação Climática e
Experimentos de Sensibilidade, f. 158. Tese (Doutorado em Meteorologia). Instituto
de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo,
2008.
REBOITA, M. S.; AMBRIZZI, T.; SILVA, B. A.; PINHEIRO, R. F.; da ROCHA, R. P.
The South Atlantic Subtropical Anticyclone: Present and Future Climate. Frontiers in
Earth Science, v. 7. doi:10.3389/feart.2019.00008, 2019
REBOITA, M. S.; da ROCHA, R. P.; AMBRIZZI, T.; SUGAHARA, S. South Atlantic
Ocean cyclogenesis climatology simulated by regional climate model (RegCM3).
Climatic Dynamics. Available in:
<http://www.springerlink.com/content/a1hk527684043206/fulltext.pdf>. Acesso in:
11/8/2010. DOI:10.1007/s00382-009-0668-7, 2010a.
REBOITA, M. S.; da ROCHA, R. P.; AMBRIZZI, T.; CAETANO, E. An assessment of
the latent and sensible heat flux on the simulated regional climate over Southwestern
South Atlantic Ocean. Climate Dynamics, v. 34, p. 873-889., 2010b.
REBOITA, M. S, da Rocha, R. P, OLIVEIRA, D. M. Key Features and Adverse
Weather of the Named Subtropical Cyclones Over the Southwestern South Atlantic
Ocean. Atmosphere, v. 6, n. 10, p. 1-21, 2019.
REBOITA, M. S.; da ROCHA, R. P.; de SOUZA, M. R.; LLOPART, M. Extratropical
Cyclones over the Southwestern South Atlantic Ocean: HadGEM2-ES and RegCM4
Projections. International Journal of Climatology, v. 38.6, p. 2866-879, 2018.
REBOITA, M. S, GAN, M. A, da ROCHA, R. P, CUSTÓDIO, I. S. Ciclones em
Superfície nas Latitudes Austrais: Parte I - Revisão Bibliográfica. Revista
Brasileira de Meteorologia, v. 32, n. 2, p. 171-186, 2017b.
REBOITA, M. S, GAN, M. A, da ROCHA, R, P, CUSTÓDIO, I, S, 2017b: Ciclones em
Superfície nas Latitudes Austrais: Parte II - Estudo de Casos. Revista Brasileira de
Meteorologia, v. 32, n. 4, p. 504-542, 2017b.
SAHA, S., S. MOORTHI, H. PAN, X. WU, J. WANG, S. NADIGA, P. TRIPP, R.
KISTLER, J. WOOLLEN, D. BEHRINGER, H. LIU, D. STOKES, R. GRUMBINE, G.
GAYNO, J. WANG, Y. HOU, H. CHUANG, H.H. JUANG, J. SELA, M. IREDELL, R.
TREADON, D. KLEIST, P. VAN DELST, D. KEYSER, J. DERBER, M. EK, J. MENG,
H. WEI, R. YANG, S. LORD, H. VAN DEN DOOL, A. KUMAR, W. WANG, C. LONG,
M. CHELLIAH, Y. XUE, B. HUANG, J. SCHEMM, W. EBISUZAKI, R. LIN, P. XIE, M.
CHEN, S. ZHOU, W. HIGGINS, C. ZOU, Q. LIU, Y. CHEN, Y. HAN, L. CUCURULL,
R.W. REYNOLDS, G. RUTLEDGE, AND M. GOLDBERG: The NCEP Climate
Forecast System Reanalysis. Bull. Amer. Meteor. Soc., v. 91, p. 1015–1058,
https://doi.org/10.1175/2010BAMS3001.1, 2010.
108

SAHA, SURANJANA, SHRINIVAS MOORTHI, XINGREN WU, JIANDE WANG,
SUDHIR NADIGA, PATRICK TRIPP, DAVID BEHRINGER, YU-TAI HOU, HUI-YA
CHUANG, MARK IREDELL, MICHAEL EK, JESSE MENG, RONGQIAN YANG,
MALAQUÍAS PEÑA MENDEZ, HUUG VAN DEN DOOL, QIN ZHANG, WANQIU
WANG, MINGYUE CHEN, AND EMILY BECKER. The NCEP Climate Forecast
System Version 2. Journal of Climate, v. 27.6, p. 2185-208, 2014.
SATYAMURTY, P.; MATTOS, L. F. Climatological lower tropospheric frontogenesis
in the midlatitudes due to horizontal deformation and divergence. Mon. Wea. Rev., v.
17 (6), p. 1355-1364, 1989.
SHAPIRO, M.A.; KEYSER, D. Fronts, jet streams and the tropopause. Extratropical
Cyclones, The Erik Palmén Memorial Volume, C. W. Newton and E. O. Holopainen,
Eds., American Meteorological Society, p. 167-191, 1990
SIMPSON, R. H. Evolution of the Kona Storm, a Subtropical Storm. J. Meteor., v. 9,
p. 24–35.121, 1952.
SINCLAIR, M. R.An objective cyclone climatology for the Southern Hemisphere.
Monthly Weather Review, v. 122, p. 2239-2256, 1994.
SINCLAIR, M. R. A climatology of cyclogenesis for the Southern Hemisphere.
Monthly Weather Review, v. 123, p. 1601-1619, 1996.
SUGAHARA, S., 2000: Variação anual da frequência de ciclones no Atlântico Sul. In:
XI Congresso Brasileiro de Meteorologia – II Encontro Brasileiro de Interação
Oceano-Atmosfera, outubro de 2000. Rio de Janeiro, Brasil, p. 2607-2611.
SUTCLIFFE, R. C.A Contribution to the Problem of Development. Quart. J. Roy.
Meteor. Soc., v. 73, p. 370-383, 1947.
STÜKER, Eduardo et al. COMPARAÇÃO ENTRE OS DADOS DE VENTO DAS
REANÁLISES METEOROLÓGICAS ERA-INTERIM E CFSR COM OS DADOS DAS
ESTAÇÕES AUTOMÁTICAS DO INMET NO RIO GRANDE DO SUL. Ciência e
Natura, [S.l.], v. 38, p. 284-290, jul. 2016. ISSN 2179-460X. Disponível em:
<https://periodicos.ufsm.br/cienciaenatura/article/view/20233>. Acesso em: 24 jul.
2018. doi:http://dx.doi.org/10.5902/2179460X20233.
TAYLOR, K. E. Summarizing multiple aspects of model performance in a single
diagram. Journal of Geophysical Research, v. 106, n. 7, p. 7183-7192, 2001.
WORLD METEOROLOGICAL ORGANIZATION. Technical Document #94 Tropical
Cyclone Programme Report No. TCP-30 Regional Association IV (North America,
Central America and the Caribbean) Hurricane Operational Plan 2005 Edition, 2005.
109