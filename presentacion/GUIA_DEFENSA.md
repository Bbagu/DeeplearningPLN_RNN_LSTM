# Guion de exposición del grupo 5

Duración orientativa: 35 minutos, incluidos 5 minutos de demostración. Las 12 diapositivas incluyen portada y cierre. Las notas también están dentro del PowerPoint. El PDF de diapositivas es una copia visual de consulta; para editar texto, tablas o gráficos usa el PPTX.

## Organización sugerida

Todos deben comprender el trabajo completo. Esta distribución organiza el ensayo y no certifica aportes ya realizados.

| Integrante | Diapositivas | Minutos |

|---|---|---:|

| Angel David Gadvay Cepeda | 1 y 2 | 4 |

| Walter Padilla | 3 y 4 | 7 |

| Jaime Morales | 5 y 6 | 6 |

| Jose Nieto | 7 y 8 | 5 |

| Bryan Lema | 9 y 10 | 6 |

| Max Viteri | 11 y 12 | 7 |

## Cómo ensayar

Primero explica cada figura con tus palabras. Después comprueba el dato o concepto en la guía. Cronometra el recorrido completo y cambia de expositor sin volver a explicar lo anterior. Las preguntas del docente pueden dirigirse a cualquier integrante.

## Demostración: preparación

En el equipo que se utilizará para exponer, instala las dependencias siguiendo INSTRUCCIONES_DE_USO.md en 04_PROYECTO_PYTHON. Abre una terminal en esa carpeta. La instalación requiere Internet; la predicción posterior usa los modelos locales.

```powershell
.\.venv\Scripts\python.exe codigo/demo.py
```

No hace falta entrenar antes de la defensa. Conserva el PDF de diapositivas y resultados/ejemplos_demo.json como respaldo y aclara si estás mostrando una salida guardada.

## Diapositiva 1. RNN y LSTM para autocompletado en español

Tiempo sugerido: 2 minutos.

Presentar el tema y a los seis integrantes. La pregunta central es si una LSTM predice mejor la siguiente palabra que una RNN simple bajo las mismas condiciones de datos y entrenamiento. Explicar el recorrido: mecanismo de las redes, experimento y resultados, con una demostración al final. El término PLN significa procesamiento del lenguaje natural. RNN significa red neuronal recurrente. LSTM es una clase de red recurrente con una celda de memoria y compuertas. El estudio usa texto en español y predice palabras completas.
Transición: comenzar con una entrada concreta antes de presentar fórmulas.

### Fuentes y evidencia

Informe, resúmenes e introducción. La imagen de portada es una ilustración abstracta generada para esta presentación, sin datos experimentales.

## Diapositiva 2. Predicción de la siguiente palabra

Tiempo sugerido: 2 minutos.

Leer la entrada y señalar que todavía falta una palabra. El contexto es lo escrito antes de la posición que se predice. El programa devuelve cinco sugerencias ordenadas por una probabilidad aprendida. Mostrar de, del y vasco como parte de una salida guardada, no como únicas continuaciones gramaticales. Probabilidad del modelo no significa certeza sobre la intención del usuario.
Explicar utilidad: editores y formularios pueden ofrecer continuaciones que la persona decide aceptar. Los modelos de lenguaje también ayudan a valorar hipótesis de reconocimiento de voz, aplicación estudiada por Mikolov. Nuestro programa no reconoce voz.
Objetivo: comprender la recurrencia y comparar RNN/LSTM con una referencia sencilla. La aplicación completa palabras siguientes, no letras parciales ni preguntas.

### Fuentes y evidencia

Bengio et al. 2003: https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf ; Mikolov et al. 2010: https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.html ; resultados/ejemplos_demo.json

## Diapositiva 3. RNN: actualización del estado

Tiempo sugerido: 3 minutos.

Recorrer las filas en orden. La red lee la representación numérica de una palabra, la combina con el estado anterior y obtiene un estado nuevo. En este proyecto cada estado tiene 64 valores. El estado puede contener información de varias posiciones, pero tiene capacidad limitada. Los mismos pesos se usan en todos los pasos.
Explicar la expresión en palabras antes de símbolos: x es la representación de entrada, h el estado, W los pesos y b el sesgo. tanh transforma cada componente a un valor entre menos uno y uno. Las operaciones se hacen con vectores y matrices. El estado no es una probabilidad. La capa de salida transforma el último estado válido en puntuaciones para las palabras.
Al entrenar, la señal de cambio puede hacerse pequeña o grande al recorrer posiciones. Eso dificulta conservar relaciones lejanas. El recorte de gradientes limita valores grandes, pero no recupera información ya perdida. Aquí el estado empieza de nuevo en cada ventana.

### Fuentes y evidencia

Informe, sección 3. Bengio et al. 1994: https://www.cs.cmu.edu/~bhiksha/courses/deeplearning/Fall.2016/pdfs/Bengio_94.pdf ; Pascanu et al. 2013: https://proceedings.mlr.press/v28/pascanu13.pdf

## Diapositiva 4. LSTM: memoria regulada por compuertas

Tiempo sugerido: 4 minutos.

Seguir la línea superior: la celda anterior se multiplica por la compuerta de olvido. El contenido candidato se multiplica por la compuerta de entrada. La suma forma la celda nueva. Después tanh transforma esa celda y la compuerta de salida regula el estado oculto. La ilustración simplifica la actualización y omite el cálculo de las compuertas.
Cada compuerta usa entrada y estado anterior, pesos aprendidos y sigmoide, con valores entre cero y uno. No son interruptores obligatoriamente binarios. El candidato usa tanh y puede ser positivo o negativo. Multiplicar ocurre componente por componente.
Ejemplo didáctico de una componente: celda anterior 0,8, olvido 0,75, entrada 0,2 y candidato 0,5. Queda 0,75 por 0,8 más 0,2 por 0,5, igual a 0,7. Con salida 0,6, el estado es 0,6 por tanh(0,7), aproximadamente 0,363. Estas cantidades enseñan la operación y no proceden del entrenamiento.
La celda y el estado son diferentes. La memoria no garantiza conservar todo. El programa reinicia ambos por consulta y la ventana limita qué palabras puede recibir. La implementación moderna no reproduce literalmente todas las variantes históricas.

### Fuentes y evidencia

Hochreiter y Schmidhuber 1997: https://www.bioinf.jku.at/publications/older/2604.pdf ; Sherstinsky: https://arxiv.org/pdf/1808.03314 ; Greff et al.: https://arxiv.org/pdf/1503.04069 . Ilustración explicativa generada para esta presentación, basada en las operaciones descritas.

## Diapositiva 5. Datos en español y separación por documento

Tiempo sugerido: 3 minutos.

AnCora aporta textos periodísticos. Se usa la distribución UD Spanish-AnCora r2.17, bajo CC BY 4.0 según LICENSE.txt. Se unen los archivos originales y se crea una partición propia por identificador documental, no el benchmark oficial. La misma regla fija asigna documentos completos a entrenamiento, validación o prueba.
El programa conserva el texto original de la oración, convierte a minúsculas, conserva tildes, normaliza números y omite puntuación. Mantiene palabras como de y el. Elimina 62 oraciones exactamente repetidas después de normalizar.
Distinguir palabras disponibles y objetivos usados: entrenamiento tiene 372317 posiciones, pero solo usa 100000 seleccionadas. Validación usa 52695 y prueba 56796. El vocabulario contiene 3000 entradas: 2997 frecuentes de entrenamiento y tres señales PAD, UNK, BOS. UNK agrupa palabras fuera de vocabulario. Nunca se construye el vocabulario mirando prueba.

### Fuentes y evidencia

datos/procesados/resumen.json y documentos.json. Taulé et al. 2008: https://aclanthology.org/L08-1222.pdf ; Nivre et al. 2020: https://aclanthology.org/2020.lrec-1.497.pdf ; corpus y licencia: https://github.com/UniversalDependencies/UD_Spanish-AnCora/tree/r2.17

## Diapositiva 6. Código: recorrido de una entrada

Tiempo sugerido: 3 minutos.

Explicar qué hace cada biblioteca y conectar con código/pln.py. PyTorch define embeddings, RNN/LSTM, salida y entrenamiento. NumPy organiza las matrices y el muestreo. Matplotlib dibuja los resultados ya medidos. Ninguna gráfica entrena el modelo.
Para el contexto real el presidente del gobierno, tokens produce cuatro palabras. Se antepone BOS y se obtienen identificadores [2,5,46,11,42]. Son índices, no puntuaciones. Embedding asigna 48 valores a cada uno. La red recurrente produce estados de 64 valores. forward toma el último estado real mediante lengths menos uno, porque Python cuenta desde cero. Así el relleno posterior no altera la salida elegida. Una capa lineal produce 3000 puntuaciones y softmax las convierte en probabilidades. PAD y BOS quedan restringidos.
Durante entrenamiento se calcula pérdida, se obtienen gradientes y Adam actualiza los pesos. Durante la demo solo se cargan pesos y se calcula una salida, sin aprender de la consulta. Mostrar dónde están tokens, LanguageModel.forward y predict.

### Fuentes y evidencia

codigo/pln.py: tokens, LanguageModel.forward, train y predict. Documentación técnica: https://docs.pytorch.org/docs/2.14/generated/torch.nn.LSTM.html ; informe, sección 5.

## Diapositiva 7. Comparación bajo un mismo protocolo

Tiempo sugerido: 3 minutos.

La comparación principal usa dos arquitecturas, tres semillas por arquitectura y contexto máximo doce. Las semillas 17, 29 y 43 cambian inicialización y orden de entrenamiento, no el conjunto de prueba. Son seis ejecuciones principales. Se añaden cuatro de sensibilidad, con contextos cuatro y veinticuatro y semilla 17, para diez finales. El piloto se excluye.
Una época recorre los objetivos elegidos. El lote contiene hasta 512 ejemplos. Adam usa tasa 0,003, dropout 0,15 después de recurrencia y recorte de gradientes a norma 1. La representación y el estado tienen tamaños 48 y 64. RNN tiene 346296 parámetros y LSTM 368184. No se igualó el número de parámetros ni el tiempo.
El bigrama estima la siguiente palabra con la palabra inmediatamente anterior y los mismos objetivos. El suavizado asigna probabilidad a continuaciones no observadas. Alfa 1, 10 y 100 se comparan en validación y se elige 100 por menor pérdida. Se guarda el checkpoint con menor NLL de validación. Solo después se evalúa prueba. El archivo final conserva esa evaluación.

### Fuentes y evidencia

investigacion/PROTOCOLO_EXPERIMENTAL.md, resultados/bigrama_validacion.json, resultados/*_entrenamiento.json, codigo/experimentos.py y codigo/pln.py. Srivastava et al. 2014: https://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf

## Diapositiva 8. Qué mide cada resultado

Tiempo sugerido: 2 minutos.

Explicar dos preguntas distintas: cuánto valor de probabilidad se asigna a la respuesta real y dónde queda esa respuesta en el orden de candidatas. NLL es el promedio del logaritmo negativo de su probabilidad. Menor es mejor. Perplejidad es exp(NLL), también menor es mejor bajo los mismos datos y vocabulario. No es porcentaje de error.
Top-1 verifica el primer lugar y top-5 los primeros cinco. Ejemplo didáctico: si la respuesta es anunció y ocupa el cuarto puesto, top-1 falla y top-5 acierta.
En nuestra evaluación UNK nunca cuenta como palabra acertada y todas las posiciones permanecen en el denominador. NLL y perplejidad sí usan UNK como objetivo interno. Además, UNK puede ocupar un puesto entre los cinco antes del filtrado. La demo lo oculta, por eso las cinco palabras visibles no son exactamente la métrica top-5. No interpretar una probabilidad como confianza calibrada en la intención del usuario.

### Fuentes y evidencia

codigo/pln.py: metrics_from_logits, evaluate_model y predict. Informe, secciones 5.13 a 5.16.

## Diapositiva 9. La RNN obtuvo mejores medias en esta prueba

Tiempo sugerido: 3 minutos.

Leer ambos gráficos: a la izquierda una barra más baja es mejor, a la derecha una más alta es mejor. Todos usan 56796 objetivos. RNN y LSTM son medias de tres semillas, contexto doce. Bigrama es una configuración seleccionada.
Perplejidad: bigrama 85,93, RNN 75,60 y LSTM 78,15. Desviación muestral: RNN 0,36 y LSTM 1,05. Top-5: 25,62 %, 26,58 % y 26,14 %. Desviación en puntos porcentuales: 0,08 y 0,09. Estos gráficos muestran medias, sin barras de dispersión, para facilitar lectura. Las cifras completas están en la tabla del informe. Top-1 fue 2,82 %, 7,23 % y 6,72 %.
La ganancia top-5 respecto al bigrama es 0,96 puntos porcentuales para RNN y 0,52 para LSTM. La reducción relativa de perplejidad fue aproximadamente 12,02 % y 9,05 %, pero no es acierto adicional. Tres semillas y una partición no prueban superioridad general ni significación estadística.

### Fuentes y evidencia

resultados/evaluacion_test.json y resumen_comparacion.json. Informe, cuadro de comparación principal.

## Diapositiva 10. El aprendizaje mejora, pero la cobertura limita

Tiempo sugerido: 3 minutos.

La curva corresponde únicamente a LSTM, contexto doce, semilla 29, la seleccionada para la demo. El eje horizontal indica época y el vertical NLL de validación. Los cinco valores son 4,735, 4,561, 4,456, 4,384 y 4,339. Cada punto resume toda la validación, no una palabra. La quinta época es la de menor pérdida registrada y queda guardada.
La tendencia indica mejora en estas cinco épocas, no que el modelo haya alcanzado su máximo posible ni que entrenar sin límite mejoraría. No se eligió la época usando prueba. El informe incluye también las otras cinco curvas.
La limitación principal es cobertura: 12033 de 56796 objetivos, el 21,19 %, están fuera del vocabulario. UNK agrupa esos casos. Riobamba, ESPOCH y Chimborazo resultan desconocidas en el modelo conservado. No se puede concluir capacidad de escritura sobre cualquier tema a partir de prensa.
Los contextos cuatro y veinticuatro no producen una mejora continua para semilla 17. Esa comparación exploratoria no mide causalmente memoria a larga distancia. No se evaluó ahorro de tiempo de usuarios ni uso productivo.

### Fuentes y evidencia

resultados/lstm_c12_s29_historial.json, datos/procesados/resumen.json y resultados/ejemplos_demo.json. Informe, resultados y limitaciones.

## Diapositiva 11. Demostración del autocompletado

Tiempo sugerido: 5 minutos.

Antes de exponer, abrir PowerShell en la carpeta del proyecto y comprobar el entorno. Ejecutar .\.venv\Scripts\python.exe codigo/demo.py. En el paquete compartido el proyecto está dentro de 04_PROYECTO_PYTHON.
Minuto 1: introducir el presidente del gobierno. Identificar modelo lstm_c12_s29.pt, tokens y sugerencias. Minuto 2: explicar que se eligió esa LSTM por validación para mostrar el mecanismo LSTM, aunque RNN obtuvo mejor media. La tabla de la diapositiva es una salida guardada, no sustituye la ejecución. Minuto 3: probar Riobamba ESPOCH Chimborazo y leer desconocidas. El modelo aún produce propuestas porque usa UNK, pero eso no significa que conozca los lugares. Minuto 4: mostrar LanguageModel.forward y la selección de última posición válida. Si el tiempo permite, ejecutar las ocho pruebas. Minuto 5: cerrar con /salir y explicar probabilidades.
Las cinco probabilidades suman 28,06 %, porque el resto corresponde a otras entradas y a UNK. No se renormalizan después de ocultar símbolos. Cambiar la entrada no entrena. La consulta no tiene una respuesta única con la que calcular acierto automáticamente.
Contingencia: si falla la ejecución, mostrar resultados/ejemplos_demo.json y declarar que son salidas guardadas. No presentarlas como una demo ejecutada. La demo no necesita Internet después de instalar dependencias y disponer del modelo.

### Fuentes y evidencia

codigo/demo.py, codigo/pln.py: predict y load_model. resultados/ejemplos_demo.json.

## Diapositiva 12. Conclusiones del estudio

Tiempo sugerido: 2 minutos.

Responder la pregunta inicial: bajo este protocolo, LSTM no superó a RNN. RNN obtuvo menor perplejidad y mayor acierto medio. Esto no invalida el mecanismo de memoria de LSTM ni demuestra una ley general.
Recapitular mecanismo: RNN actualiza un estado y LSTM añade una celda y compuertas aprendidas. Su resultado también depende del vocabulario, de los datos y del entrenamiento. La mejora top-5 fue pequeña y la cobertura desconocida fue alta. Por eso se presenta como prototipo educativo.
Posibles extensiones: vocabulario de mayor cobertura, otro presupuesto de entrenamiento y más semillas en la comparación de contextos. Son propuestas y no resultados ya obtenidos.
Indicar dónde contrastar: el informe incluye doce referencias y la guía localiza los pasajes abiertos. Los resultados experimentales están en JSON, no en los artículos. No dar una URL de repositorio o presentación que todavía no existe. Abrir el turno de preguntas. Todos deben poder explicar cualquier bloque.

### Fuentes y evidencia

Informe, conclusiones. Catálogo completo: investigacion/FUENTES_ABIERTAS.md. Fuentes principales: Bengio 1994 y 2003; Hochreiter y Schmidhuber 1997; Mikolov 2010; Sundermeyer 2012; Pascanu 2013; Srivastava 2014; Greff 2017; Sherstinsky 2020; Doval et al. 2016; Taulé et al. 2008; Nivre et al. 2020. Los enlaces abiertos y pasajes están en la guía y el catálogo compartidos.

## Preguntas para comprobar el dominio

1. ¿Qué diferencia existe entre el estado de RNN y la celda de LSTM?
2. ¿Qué limita el contexto a doce posiciones?
3. ¿Por qué se separan documentos y no solo filas aleatorias?
4. ¿Por qué 75,60 de perplejidad no significa 75,60 % de acierto?
5. ¿Por qué la demo usa LSTM si RNN obtuvo mejores medias?
6. ¿Qué significa UNK y por qué cambia la interpretación de las métricas?
7. ¿Qué archivo permite comprobar una cifra concreta?
8. ¿Qué se puede concluir y qué requeriría otro experimento?

Las respuestas desarrolladas están en las notas anteriores y en los capítulos 10 a 16 y 18 de la guía.