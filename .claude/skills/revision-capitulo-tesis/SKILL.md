---
name: revision-capitulo-tesis
description: Auditoría rigurosa de un capítulo de esta tesis (introducción, fundamentos, métodos, resultados de viento/precipitación/MEOF/prototipos, conclusiones, consideraciones finales o abstract) — verifica figuras contra las cuatro preguntas, fidelidad de citas contra las fuentes reales (incluyendo re-verificar contra el código/datos cuando la cifra es propia), consistencia numérica tabla-vs-texto y entre capítulos, sobreinterpretación de mecanismos no probados, conexiones lógicas entre secciones/regiones/poblaciones, y calibración de lenguaje (hilación de ideas, palabras innecesarias, afirmaciones que exceden el sustento de los resultados). Úsala cuando el usuario pida revisar, auditar o verificar a fondo cualquier capítulo de la tesis, incluida una segunda pasada sobre uno ya revisado (ej. "revisa el capítulo 6 con la misma lógica", "revisemos el capítulo 2 una vez más", "evalúa la hilación de ideas del capítulo 4").
---

Esta skill documenta el método desarrollado y validado, capítulo por capítulo, sobre toda la tesis (introducción, fundamentos, métodos, los cuatro capítulos de resultados, conclusiones, consideraciones finales y abstract). Al aplicarla a un capítulo nuevo o a una segunda pasada de uno ya revisado, sigue este orden. Es un proceso largo y de varias rondas — no hay que hacerlo todo en un solo turno; conviene ir bloque por bloque y dejar que el usuario decida qué aplicar en cada paso. Una primera pasada limpia **no** significa que el capítulo esté terminado: varios de los hallazgos más serios de esta tesis aparecieron en segundas o terceras pasadas, con un enfoque distinto (ver Regla de oro y puntos 9-10).

## Regla de oro: profundidad real, no superficial

Este es el error más grave que cometí y el usuario corrigió varias veces a lo largo de la revisión: tras verificar varios autores a fondo (leyendo abstracts y párrafos completos), empecé a apurar el ritmo — un solo `grep` por autor, una coincidencia de palabra clave, y declaraba "confirmado" para las 4-5 citas de ese autor sin leer cada una por separado. El usuario lo notó y pidió rehacerlo, más de una vez, en capítulos distintos.

**Por cada afirmación atribuida a un autor**, lee el párrafo o abstract real de la fuente (no solo una línea aislada) antes de dar un veredicto. Si un autor tiene 5 citas distintas en el capítulo, verifica las 5 por separado — no extrapoles de una a las demás. Es lento a propósito.

**Nunca confíes en tu memoria de la conversación sobre el estado del archivo — vuelve a leerlo.** Varias veces esta revisión, correcciones que yo mismo había "propuesto y aplicado" según el resumen de la conversación en realidad **no estaban en el archivo actual** (capítulos 1 y 4: tres citas ya "corregidas" antes seguían mal atribuidas cuando volví a leer el archivo). La causa probable es que el resumen automático de una sesión larga puede describir una intención o una propuesta como si ya se hubiera aplicado. Antes de dar por bueno un capítulo, `Read` el archivo completo tal como está ahora — no asumas que coincide con lo que recuerdas haber hecho.

**Cuando el usuario dice "no parece que estés revisando a profundidad", tómalo literalmente: busca en otro lugar.** La forma más productiva de responder no es releer el mismo capítulo con más cuidado, sino **cruzarlo contra otras fuentes**: otros capítulos, las tablas, o el código/los datos reales. Los hallazgos más serios de esta sesión (ver punto 9) aparecieron así, no releyendo el capítulo en aislamiento.

## 0. Verificación de compilación (antes y después)

El capítulo suele estar comentado (`% \input{...}`) en `tese_es.tex` porque está en construcción. Antes de tocar nada:
1. Descomentar temporalmente el `\input` del capítulo a revisar (y los capítulos previos de los que depende para labels/referencias — usualmente 01-03 más los ya revisados).
2. `pdflatex -interaction=nonstopmode tese_es.tex`, luego `BSTINPUTS=".:aux:" bibtex tese_es` (el estilo `iag_es.bst` vive en `aux/`, no en la raíz), luego `pdflatex` dos veces más.
3. Revisar: sin `!` (errores fatales), sin "undefined" (referencias/citas rotas), sin archivos faltantes.
4. **Volver a comentar la línea** en `tese_es.tex` al terminar — es el estado en que el usuario lo tiene mientras trabaja capítulo por capítulo.

Repetir el mismo chequeo al final de la sesión, con todas las ediciones ya aplicadas, antes de declarar terminado.

## 1. Las cuatro preguntas por figura

Para cada figura del capítulo, revisar si el texto que la rodea (caption + párrafos antes/después) responde:
- **¿Qué es?** — descripción técnica (qué muestra, cómo está organizada la matriz de paneles).
- **¿Cómo es?** — el patrón/forma observado (qué se ve, con números).
- **¿Por qué es así?** — mecanismo físico, con cita de respaldo.
- **¿Para qué?** — implicación, aplicación o qué prepara para la siguiente sección (no solo la descripción en sí).

Reportar en una tabla figura × 4 preguntas con ✓ o el hueco encontrado. El "para qué" es el que más frecuentemente falta.

## 2. Fidelidad de citas a las fuentes reales

1. Extraer todas las claves de cita únicas del capítulo (`grep -ohE "\\\\cite[tp]\{[^}]+\}"`).
2. Verificar que exista el archivo fuente en `papers/files_MD/<clave>.md`. Si el archivo existe pero con un nombre ligeramente distinto a la clave del `.bib` (ej. `rocha2016estudo.md` vs. clave `rocha2016estudio`), renombrarlo con `git mv` para que coincidan — evita "archivo no encontrado" falsos negativos en el futuro.
3. Para cada afirmación (no por autor, por afirmación — un mismo autor puede tener 10 citas distintas con distinto grado de fidelidad cada una), leer el pasaje real y dar veredicto: **CONFIRMADO** / **PARCIAL** (matiz, recorte, generalización) / **DISCREPANCIA** (no respalda o contradice).
4. Para lotes grandes (10+ afirmaciones), usar forks en paralelo (2-3 a la vez) para no saturar el contexto propio — pero luego, si el autor resulta ser de la banca evaluadora o el caso es ambiguo, repetir la verificación uno mismo leyendo el contexto completo (ver Regla de oro arriba).
5. **Autores de la banca evaluadora van primero y con máxima profundidad.** Pedir al usuario la lista de quiénes están en la banca. Para cada uno, buscar TODAS sus citas en TODA la tesis (no solo el capítulo actual) — el mismo error puede repetirse en otro capítulo (pasó con Reboita: el mismo error de cap. 4 estaba también, textualmente, en cap. 6).
6. Al proponer una corrección, separar lo que la fuente sí dice de lo que es interpretación propia del capítulo — no borrar la interpretación, solo dejar de atribuírsela a quien no la hizo.

## 3. Consistencia numérica: tablas vs. texto

Las secciones de Componentes Principales (`\input{tabelas_es/tab_stat_*.tex}`) citan en prosa cifras (asimetría, curtosis, correlación de Spearman con signo) que deben coincidir exactamente con la tabla. Leer la tabla completa y contrastar cada cifra mencionada en el texto, celda por celda, incluyendo:
- Rangos ("oscila entre X e Y") — verificar que X e Y sean realmente el mínimo y máximo del subconjunto de celdas descrito.
- Afirmaciones de "el mayor/menor salto" o "el valor más alto/bajo" — recalcular con los propios números ya dados en el texto antes de aceptar el superlativo.
- Qué valores están en negrita (significativos) — si el texto dice "X es significativo" pero la tabla no lo marca en negrita, es un error.

Este chequeo encontró errores reales en ambos capítulos ya revisados (rango de curtosis y significancia de PC2 en cap. 4; un "salto" descrito al revés en cap. 5) — es uno de los más rentables.

Si una cifra citada en el texto proviene de datos propios del usuario (ej. "este criterio retiene aproximadamente el 60% de los sistemas"), y no solo de una tabla ya generada en el LaTeX, no te conformes con que "suene razonable" — **verifica contra el código y los datos reales**, ejecutando el filtro relevante en Python si hace falta (los notebooks/scripts están en `/home/jonathan/defensa/cods`, con datos en `input_csv/`). Así se encontró que una cifra de retención (60%) no correspondía a ningún cálculo real sobre el catálogo de esta tesis — el número correcto (43-52%) solo apareció al correr el filtro real con pandas.

## 4. Sobreinterpretación de mecanismos no probados (el "problema EOF")

Buscar dónde el texto afirma que un resultado estadístico propio (patrón EOF, concentración espacial, salto de varianza) **es** o **confirma** un mecanismo físico nombrado de la literatura (WCB, CCB, sting jet, etc.) sin que la metodología del capítulo lo valide independientemente (no se analizó viento vectorial, no se analizó un campo de flujos de calor, etc.).

- Distinguir esto de comparar dos resultados **propios** del capítulo entre sí (ej. la posición del EOF1 de viento vs. la del EOF1 de precipitación) — eso sí es válido y puede afirmarse con confianza.
- Corregir con lenguaje variado, no una fórmula repetida: "compatible con", "recuerda a", "coincide con", modo condicional ("explicaría", "sería consistente con"). Evitar repetir la misma coletilla de descargo en cada ocurrencia — es mejor una sola frase de límite metodológico en el capítulo de Métodos (sección de EOF) que cubra el caso general, y dejar el resto del capítulo con hedging ligero y variado.
- Usar lenguaje simple y directo — el objetivo es que la banca lea con facilidad, no demostrar vocabulario técnico. Si una palabra sugiere una afirmación más fuerte de lo que en realidad se sostiene (ej. "variabilidad estructural" sonando a una afirmación estadística cuando solo describe la forma de un mapa compuesto), preguntar al usuario qué quiso decir antes de reescribir — no asumir.

## 5. Cuidado explícito con Población Global (PG) vs. p90

**p90 es un subconjunto extraído de PG, no una población aparte.** Antes de conectar o comparar dos hallazgos de distintas secciones, verificar explícitamente de qué población es cada uno. Es fácil mezclar sin querer un hallazgo de PG con uno de p90 al construir una "misma historia regional" — pasó una vez en esta revisión (capítulo 5, conexión entre eficiencia del PDF en p90 y persistencia de correlación de PC1 en PG). Revisar cada conexión propuesta específicamente por esto antes de mostrarla al usuario.

## 6. Conexiones lógicas entre secciones

Las secciones de PDF (magnitud) y PDFe/KDE (ubicación espacial) suelen anticipar o explicar resultados de secciones posteriores (varianza EOF, patrones EOF1, significancia Bootstrap, correlaciones PC1-3), pero el capítulo no siempre lo dice explícitamente. Buscar:
- El mismo ranking regional (SBR/LPB/ARG) apareciendo en dos secciones distintas con métricas distintas (ej. la región más concentrada en magnitud también es la más concentrada en el espacio) — si aparece, vale la pena conectarlo con una frase cruzada.
- La misma fase (Ic/It/M/D) identificada como "la más estable" o "la más marcada" en dos secciones distintas por métodos distintos (KDE y EOF) — confirmación cruzada con dos métodos, vale la pena citarse mutuamente.
- Tensiones o tensión aparente entre "concentración de magnitud" y "organización espacial" para una misma región/fase/población — puede ser un hallazgo genuino, no una contradicción (una región puede ser muy consistente en *cuánto* pero muy dispersa en *dónde*).
- Una baja densidad/magnitud en una sección explicando por qué la sección de significancia estadística (Bootstrap-t) no encuentra señal robusta ahí — señal débil es más difícil de distinguir del ruido de muestreo.

Al encontrar una posible inconsistencia (no solo una conexión), mostrarla al usuario como pregunta, no como corrección unilateral — puede ser una ambigüedad de redacción y no un error real (ver ejemplo del punto 4).

## 7. Densidad de citas (opcional, solo si el usuario lo pide)

Marcar párrafos donde se acumulan 4+ citas para un solo punto. Proponer conservar 2-3 con el detalle más específico/cuantitativo y agrupar o resumir el resto en una frase de consenso. Es una mejora de estilo, no de exactitud — no aplicar sin que el usuario lo pida explícitamente, y tratarla como "viable" (opcional) en vez de "necesaria".

## 8. Hallazgos propios no destacados

Revisar si hay contrastes o comparaciones ya presentes en los números del texto (ej. el EOF1 de una variable nunca supera el rango típico del EOF1 de otra) que no se nombran explícitamente como hallazgo — proponerlos como adiciones, no como correcciones.

## 9. Calibración de lenguaje: hilación de ideas, palabras innecesarias y afirmaciones sin sustento

Pedido explícito del usuario, como pasada **distinta y posterior** a los puntos 1-6 — se hace sobre un capítulo que ya pasó por fidelidad de citas y consistencia numérica, no en su lugar. Releer el capítulo completo buscando tres cosas a la vez:

- **Palabras que afirman más de lo que el resultado estadístico sostiene**: "demuestra"/"confirma"/"valida"/"prueba" para hallazgos de covarianza o correlación moderada casi siempre deberían ser "muestra"/"indica"/"respalda"/"es consistente con". Una correlación de Spearman moderada (ej. r entre -0.3 y -0.45) descrita como "sistemáticamente" o una geometría llamada "predecible" sobreafirma. Revisar también generalizaciones de más alcance que la muestra real (ej. "Hemisferio Sur" cuando el estudio cubre solo 3 regiones del Atlántico Sudoccidental; "universal" para un patrón visto en 3 regiones).
- **Imprecisión técnica repetida**: "linealmente"/"lineal" usado para describir una correlación de Spearman (que mide relación monótona, no lineal) aparece muchas veces a lo largo de la tesis — revisar cada instancia por separado, no asumir que ya quedó resuelta porque se corrigió en otro capítulo.
- **Palabras complicadas, términos inventados o de registro informal**: "previsibilidad geométrica", "reducción dimensional efectiva" (redundante — un EOF que concentra varianza ya es por definición una reducción dimensional), "devela", "dramático", "se empaquetan", "esta historia" (metáfora narrativa fuera de lugar en un capítulo de conclusiones). Reemplazar por la palabra simple y directa equivalente; si el reemplazo obvio usa un concepto que el usuario no ha trabajado en su tesis (ej. "capa límite"), preguntar antes de introducirlo.
- **Hilación de ideas**: párrafos que acumulan 3-4 citas de fuentes distintas sin un hilo explícito que conecte cada una con el resultado que debería sustentar, o una sola oración que mezcla dos mecanismos físicos distintos sin separarlos. Dividir en oraciones o párrafos más cortos sin cambiar el contenido ni usar guiones largos si el usuario ya pidió evitarlos.

Aplica también al Abstract, Conclusiones y Consideraciones Finales — de hecho ahí es donde más rinde, porque son los capítulos que la banca lee primero y con más atención.

## 10. Capítulos de síntesis (Abstract, Conclusiones, Consideraciones Finales): verificación cruzada, no solo interna

Estos capítulos repiten cifras y comparaciones que ya aparecieron en los capítulos de resultados — por eso el error más grave no se encuentra releyendo el capítulo de síntesis solo, sino **cruzando cada cifra y cada comparación regional contra el capítulo de resultados de donde proviene**. Los dos hallazgos más serios de toda esta revisión aparecieron así, no releyendo un capítulo en aislamiento:
- Un rango de viento (20--25~m/s) en Conclusiones y Abstract que no aparece en ninguna parte del capítulo de viento — la fuente real decía 20--23~m/s, y ni siquiera coincidía consigo misma entre el cuerpo del capítulo y su propia síntesis (20--22 vs. 20--23).
- El orden regional de una comparación (SBR/LPB/ARG) invertido: Conclusiones y Abstract describían a ARG como "más atenuado" en una separación geométrica, cuando el capítulo de prototipos —la fuente del dato— dice explícitamente y dos veces que ARG tiene la mayor magnitud de las tres regiones.

Ninguno de los dos se habría encontrado leyendo el capítulo de síntesis en aislamiento — ambos números "sonaban" razonables por sí solos. Por cada cifra o comparación regional en un capítulo de síntesis, ubicar la sección del capítulo de resultados de donde proviene y confirmar coincidencia exacta, no solo plausibilidad.

Evaluar además el **Abstract específicamente por extensión y propósito**, no solo por exactitud: no debe repetir cada cifra de cada síntesis de capítulo (esta tesis tenía uno de ~1,166 palabras haciendo eso, comprimido después a ~450). Un abstract debe comunicar el problema, el vacío, el enfoque, 2-3 hallazgos centrales con pocas cifras ancla, y la implicación — el detalle granular (coordenadas exactas, cada percentil secundario) pertenece a los capítulos de resultados. Preguntar al usuario si el abstract cumple ese propósito antes de asumir que solo necesita corrección de cifras puntuales.

## Proceso de trabajo con el usuario

- Mostrar siempre **original vs. propuesta** con una justificación breve antes de aplicar — nunca aplicar directamente sin mostrar primero, salvo que el usuario ya haya dicho "aplica todas" para un lote ya mostrado.
- Clasificar hallazgos en **necesario** (afecta veracidad o es un error real) vs. **viable** (mejora de estilo/claridad, opcional) cuando el volumen es grande, para que el usuario priorice.
- Con lotes largos (autores, secciones), ir contando y reportando progreso ("van 5 de 10"), y hacer pausas naturales para que el usuario decida si continuar.
- Idioma: responder siempre en español, con lenguaje simple y moderado — esta tesis la va a leer una banca evaluadora, no busca terminología difícil.
- Git: los cambios se comprometen (`git add` + `commit`) solo cuando el usuario lo pide explícitamente ("sube a GitHub", "commit"), agrupando en un commit todo lo aplicado desde el último push, con mensaje descriptivo y la línea `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`. Nunca hacer `push` sin que el usuario lo pida. Antes de compilar para verificar, revisar `git status`/`git diff` para saber exactamente qué cambió; después de compilar, revertir `tese_es.tex` a su estado base (capítulos comentados) con `git checkout -- tese_es.tex`, nunca a mano.
