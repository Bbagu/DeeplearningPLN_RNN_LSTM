# Fuentes verificables y gratuitas

Consulta y comprobación técnica: 29 de septiembre de 2026. Cada PDF de esta lista se descargó sin cuenta ni pago y se comprobó como archivo PDF. El registro `acceso_verificado.json` conserva tamaño y SHA-256. Las copias están en `investigacion/pdf/` para consulta local; no se redistribuyen automáticamente en el repositorio público.

**Cómo verificar:** abrir el enlace «texto completo», buscar el título y localizar las páginas indicadas. La página PDF cuenta desde la primera hoja del archivo; puede diferir de la paginación impresa. Las fichas son síntesis asistidas y no sustituyen la lectura crítica de los integrantes. Se revisaron los pasajes indicados, sin afirmar que el grupo haya leído íntegramente las publicaciones.

## Lectura prioritaria en español

**Doval, Yerai; Gómez-Rodríguez, Carlos; Vilares, Jesús (2016). Segmentación de palabras en español mediante modelos del lenguaje basados en redes neuronales. Procesamiento del Lenguaje Natural, 57, 75–82.**

[Texto completo gratuito en Redalyc](https://www.redalyc.org/pdf/5157/515754424008.pdf). Ubicación: sección 3.1, páginas impresas 77–78, páginas 4–5 del PDF. Explica recurrencia y el papel de compuertas y celda LSTM; la aplicación del artículo opera a nivel de caracteres y recupera espacios. **No es un experimento de autocompletado por palabras** y no se presentará como tal. Se usará como antecedente en español, conservando esa diferencia. La revista informa sus indicadores e indexación en su [página de calidad](https://www.sepln.org/index.php/la-revista/calidad); el registro también aparece en DBLP. El PDF incluye una portada de Redalyc antes del artículo.

## Fundamentos y modelos de lenguaje

| Clave | Publicación | Texto completo gratuito | Ubicación verificable y uso |
|---|---|---|---|
| bengio1994 | Bengio, Simard y Frasconi. *Learning long-term dependencies with gradient descent is difficult*. IEEE Transactions on Neural Networks, 5(2), 157–166 (1994). DOI: 10.1109/72.279181 | [Copia académica en Carnegie Mellon](https://www.cs.cmu.edu/~bhiksha/courses/deeplearning/Fall.2016/pdfs/Bengio_94.pdf) | Resumen y secciones sobre almacenamiento de información y gradientes. Manuscrito con paginación propia; no confundirla con 157–166. Explica dificultades, no garantiza fracaso de toda RNN |
| hochreiter1997 | Hochreiter y Schmidhuber. *Long Short-Term Memory*. Neural Computation, 9(8), 1735–1780 (1997). DOI: 10.1162/neco.1997.9.8.1735 | [Copia alojada en JKU](https://www.bioinf.jku.at/publications/older/2604.pdf) | Secciones 3–4 y apéndice A. Arquitectura original y flujo del error; no atribuirle automáticamente todos los componentes de las variantes modernas |
| bengio2003 | Bengio, Ducharme, Vincent y Jauvin. *A Neural Probabilistic Language Model*. JMLR, 3, 1137–1155 (2003) | [PDF editorial](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) | Sección 1.1, página PDF 3; sección 2. Representaciones distribuidas y probabilidad de palabras. Es una red de contexto fijo, no una LSTM |
| mikolov2010 | Mikolov et al. *Recurrent neural network based language model*. INTERSPEECH, 1045–1048 (2010). DOI: 10.21437/Interspeech.2010-343 | [PDF editorial ISCA](https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.pdf) | Sección 2, páginas PDF 1–2; experimentos en 3. Fundamenta el modelado recurrente y aplicaciones al reconocimiento del habla |
| sundermeyer2012 | Sundermeyer, Schlüter y Ney. *LSTM Neural Networks for Language Modeling*. INTERSPEECH, 194–197 (2012). DOI: 10.21437/Interspeech.2012-65 | [PDF editorial ISCA](https://www.isca-archive.org/interspeech_2012/sundermeyer12_interspeech.pdf) | Sección 2 y sección experimental, páginas PDF 2–4. Compara redes para modelado de lenguaje en inglés/francés; sus mejoras no predicen las de nuestro corpus |
| pascanu2013 | Pascanu, Mikolov y Bengio. *On the difficulty of training recurrent neural networks*. ICML, PMLR 28(3), 1310–1318 (2013) | [PDF editorial PMLR](https://proceedings.mlr.press/v28/pascanu13.pdf) | Sección 1.1 y ecuación 5, páginas PDF 1–2; sección 3.2 sobre gradient clipping. Distinguir explosión y desvanecimiento |
| srivastava2014 | Srivastava et al. *Dropout: A Simple Way to Prevent Neural Networks from Overfitting*. JMLR, 15, 1929–1958 (2014) | [PDF editorial](https://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf) | Resumen y descripción de dropout. Sustenta la regularización; no se usa como prueba de que cualquier dropout recurrente es adecuado |
| greff2017 | Greff et al. *LSTM: A Search Space Odyssey*. IEEE Transactions on Neural Networks and Learning Systems, 28(10), 2222–2232 (2017). DOI: 10.1109/TNNLS.2016.2582924 | [Versión de autor en arXiv](https://arxiv.org/pdf/1503.04069) | Sección II, páginas PDF 1–2; comparación de variantes. Su arquitectura incluye peepholes; nuestro `nn.LSTM` no los incorpora |
| sherstinsky2020 | Sherstinsky. *Fundamentals of Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) network*. Physica D, 404, 132306 (2020). DOI: 10.1016/j.physd.2019.132306 | [Versión de autor en arXiv](https://arxiv.org/pdf/1808.03314) | Desarrollo RNN/LSTM y ecuaciones. El PDF abierto es v10 revisado en 2023 y declara la publicación editorial de 2020; no se afirma identidad página a página con la edición editorial |

## Corpus y procedencia

| Clave | Publicación | Acceso gratuito | Qué permite verificar |
|---|---|---|---|
| taule2008 | Taulé, Martí y Recasens. *AnCora: Multilevel Annotated Corpora for Catalan and Spanish*. LREC (2008) | [PDF ACL Anthology](https://aclanthology.org/L08-1222.pdf) | Secciones 1–2, página PDF 1: origen, lenguas y naturaleza periodística. La licencia actual se verifica en el archivo de la versión usada, no en este artículo antiguo |
| nivre2020 | Nivre et al. *Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection*. LREC, 4034–4043 (2020) | [PDF ACL Anthology](https://aclanthology.org/2020.lrec-1.497.pdf) | Introducción y esquema de anotación. Es soporte sobre UD; la práctica usa el campo de texto y no entrena un analizador sintáctico |

Son **12 publicaciones académicas**, una en español. Se mantuvieron originales en inglés cuando ofrecen evidencia directa que no conviene reemplazar por resúmenes de menor calidad. Las dos publicaciones IEEE y la de Elsevier se consultan mediante copias gratuitas, conservando los datos de su publicación revisada por pares. JMLR, PMLR, ISCA, LREC y SEPLN amplían la selección con fuentes primarias pertinentes. La guía menciona IEEE, Springer y ScienceDirect como fuentes indexadas; si el docente exige exclusivamente esas plataformas, deberá confirmarse antes de cerrar la bibliografía. No se afirma haber auditado individualmente el registro de cada trabajo en Scopus o Web of Science.

## Documentación técnica abierta, separada de las 12 publicaciones

- [Repositorio y versión de AnCora utilizada](https://github.com/UniversalDependencies/UD_Spanish-AnCora/tree/r2.17).
- [Licencia del corpus](https://raw.githubusercontent.com/UniversalDependencies/UD_Spanish-AnCora/r2.17/LICENSE.txt): CC BY 4.0. El README conserva una referencia histórica a GNU y registra el cambio en v2.9; se sigue el archivo de licencia y metadatos de r2.17.
- [PyTorch LSTM](https://docs.pytorch.org/docs/2.14/generated/torch.nn.LSTM.html): ecuaciones e interfaz de la implementación usada.
- [PyTorch RNN](https://docs.pytorch.org/docs/2.14/generated/torch.nn.RNN.html): arquitectura recurrente simple.

## Enlaces descartados o sustituidos

El PDF del volumen completo en RUA devolvió HTML, por lo que no se consideró acceso verificado. La página del grupo LYS no resolvió desde este equipo. Se encontró y descargó el artículo individual en Redalyc. Los enlaces editoriales de pago de IEEE/Elsevier no son el único acceso ofrecido: se incluyen las copias abiertas comprobadas. Los libros de Springer inicialmente candidatos no se incluyeron al no contar con acceso gratuito integral verificado.
