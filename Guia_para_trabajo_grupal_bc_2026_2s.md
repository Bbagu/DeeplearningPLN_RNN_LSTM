# Guía para el Trabajo Grupal de Investigación y Aplicación en Procesamiento de Lenguaje Natural

**ESPOCH – FIE – EIS**  
**Base de Conocimiento**

**Escuela Superior Politécnica de Chimborazo (ESPOCH)**  
**Facultad de Informática y Electrónica (FIE)**  
**Séptimo Semestre – Ingeniería en Software**  
**Asignatura: Base de Conocimiento**

**Objetivo.** Que el estudiante domine las fases críticas del Procesamiento de Lenguaje Natural (PLN), integrando la teoría con la implementación técnica en Python. Se busca generar un documento de investigación de alto impacto utilizando la plantilla LATEX oficial de la asignatura, demostrando la capacidad del estudiante para diseñar pipelines de PLN y modelos de aprendizaje automático funcionales, abordando el tema de forma integral entre los seis grupos de trabajo.

## 1. Parámetros generales y formato del informe

- **Número de grupos:** la actividad se desarrolla en **6 grupos de trabajo**, cada uno responsable de una etapa del pipeline de PLN (véase la Sección 4), de modo que entre todos se cubra el tema de forma integral.
- **Formato del informe:** LATEX, utilizando la **plantilla oficial de la asignatura**, disponible en el aula virtual. No se aceptan informes elaborados con otra plantilla ni con procesadores de texto. Contenido redactado en español.
- **Extensión del informe:** mínimo **18** y máximo **20** páginas de contenido técnico.
- **Citas bibliográficas:** entre **10 y 15** referencias de fuentes indexadas (IEEE, Springer, ScienceDirect), gestionadas en BibTeX.
- **Código fuente:** implementación en **Jupyter Notebook o script .py**, debidamente documentada y publicada en un repositorio (por ejemplo, GitHub).
- **Recursos adjuntos:** al final del informe se deben incluir los enlaces (URL) a la presentación y al repositorio de código.
- **Entrega:** el entregable final es el **PDF compilado sin errores en Overleaf**, incluyendo los enlaces a los recursos, a través del aula virtual.

## 2. Estructura obligatoria del informe

1. **Abstract** (español e inglés).
2. **Introducción** e importancia del tema.
3. **Marco teórico** (definición, utilidad y funcionalidades de las librerías de Python empleadas).
4. **Metodología y desarrollo práctico** (explicación del código).
5. **Resultados y discusión técnica** (análisis de las métricas obtenidas).
6. **Conclusiones.**
7. **Enlaces a recursos** (presentación y código).
8. **Referencias bibliográficas** (BibTeX).

**Pie de página de la página 1:** Página 1 de 4 — Isaac Torres.

## 3. Directrices para la presentación (defensa)

- **Diapositivas:** entre **10 y 12 diapositivas**, con el enlace a la presentación incluido al final del informe.
- **Tiempo de exposición:** entre **30 y 40 minutos**, e incluye una demostración práctica en vivo (*live demo*) del código desarrollado.
- **Defensa:** todos los miembros del grupo deben estar preparados para exponer y responder preguntas técnicas sobre cualquier parte del trabajo, incluyendo el funcionamiento del código.

### Resumen de entregables

| Actividad | Requisito | Observación |
|---|---|---|
| Informe técnico | 18–20 páginas | Plantilla LATEX del aula virtual |
| Presentación | 10–12 diapositivas | Enlace al final del informe |
| Código fuente | Jupyter Notebook / .py | Documentado, en repositorio |
| Defensa oral | 30–40 minutos | Incluye demostración práctica (*live demo*) |

## 4. Grupos de trabajo: el pipeline de PLN

Los seis grupos cubren, en secuencia, las etapas del procesamiento de lenguaje natural: desde los fundamentos lingüísticos hasta los modelos generativos actuales. Cada sección del informe correspondiente a un grupo debe incluir la definición teórica, su utilidad en la industria, las funcionalidades principales de las librerías de Python utilizadas y el desarrollo del ejemplo práctico sugerido.

### Grupo 1: Fundamentos lingüísticos y niveles del lenguaje

- **Qué investigar:** niveles fonológico, morfológico, sintáctico y semántico del lenguaje. Problemática de la ambigüedad en la IA.
- **Ejemplo práctico:** análisis de etiquetas POS y de dependencias sintácticas con spaCy.

### Grupo 2: Preprocesamiento y normalización de texto

- **Qué investigar:** tokenización, lematización, stemming y remoción de ruido.
- **Ejemplo práctico:** pipeline de limpieza de texto para datasets de redes sociales.

### Grupo 3: Representación del texto – de lo estadístico a lo semántico

- **Qué investigar:** representación estadística mediante vectores de frecuencia y ponderación (Bag of Words y TF-IDF), y representación semántica mediante espacios vectoriales densos (word embeddings como Word2Vec o GloVe). Ventajas y limitaciones de cada enfoque.
- **Ejemplo práctico:** construir un buscador de documentos por similitud utilizando TF-IDF (Scikit-learn) y comparar sus resultados frente a la similitud obtenida con embeddings preentrenados (Word2Vec/GloVe con Gensim).

**Pie de página de la página 2:** Página 2 de 4 — Isaac Torres.

### Grupo 4: Clasificación de texto y análisis de sentimientos

- **Qué investigar:** algoritmos supervisados de clasificación de texto y métricas de evaluación (Accuracy, F1-Score, entre otras).
- **Ejemplo práctico:** clasificador de sentimientos para reseñas de comercio electrónico.

### Grupo 5: Deep learning en PLN – RNN y LSTM

- **Qué investigar:** arquitectura de redes neuronales recurrentes y manejo de memoria en secuencias mediante LSTM.
- **Ejemplo práctico:** generador de autocompletado de texto (predicción de la siguiente palabra).

### Grupo 6: Arquitectura Transformer y modelos generativos

- **Qué investigar:** mecanismo de atención y evolución hacia modelos como BERT y GPT.
- **Ejemplo práctico:** traducción automática o generación de resúmenes utilizando modelos Transformer.

## 5. Rúbrica de evaluación (total: 3 puntos)

La calificación total es de 3.0 puntos, distribuidos de la siguiente manera:

| Criterio | Indicadores de calidad | Puntaje |
|---|---|---:|
| Fondo | Profundidad técnica de la investigación y correcto funcionamiento del código Python. | 1.0 pt |
| Forma | Cumplimiento de la plantilla LATEX oficial, extensión (18–20 páginas) y gestión de citas en BibTeX. | 1.0 pt |
| Defensa | Claridad en la exposición (30–40 minutos), dominio del tema y calidad del *live demo*. | 1.0 pt |
| **Total** |  | **3.0 pts** |

## 6. Política de integridad académica y uso de inteligencia artificial

El uso de modelos de inteligencia artificial debe limitarse a la consulta, la estructuración de ideas o la revisión gramatical. Su objetivo como futuros ingenieros es investigar, diseñar y validar sus propios modelos, no tercerizar su aprendizaje a un modelo de lenguaje.

> **Regla de integridad académica**  
> Se acepta únicamente hasta un máximo del **10 % de contenido generado por inteligencia artificial** en el informe. Todos los trabajos serán analizados con **Compilatio** para garantizar el uso responsable de la IA. **Si el porcentaje supera el 10 %, el trabajo será anulado en su totalidad (calificación: 0).**

Además, tengan en cuenta lo siguiente:

- Todo contenido apoyado en IA debe pasar por parafraseo, análisis crítico y aporte propio del grupo.
- El código publicado en el repositorio debe ser funcional y reproducible; el grupo debe poder explicarlo y ejecutarlo en vivo durante la defensa.
- Las referencias bibliográficas deben ser reales y verificables. Un trabajo con citas inexistentes o que no respalden lo afirmado será penalizado en la rúbrica.
- Todos los integrantes deben poder explicar y defender cualquier parte del informe y del código durante la exposición.

**Pie de página de la página 3:** Página 3 de 4 — Isaac Torres.

**Pie de página de la página 4:** Página 4 de 4 — Isaac Torres.
