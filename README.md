# Deep learning en PLN - RNN y LSTM

Proyecto del **grupo 5**, Base de Conocimiento, Ingeniería en Software, ESPOCH. Predicción de la siguiente palabra en español mediante RNN y LSTM, comparadas con un bigrama suavizado.

**Integrantes:** Angel David Gadvay Cepeda, Walter Padilla, Jaime Morales, Jose Nieto, Bryan Lema y Max Viteri. **Entrega prevista:** 6 de octubre de 2026.

## Documentos y presentación

| Recurso | Contenido |
|---|---|
| [Informe ampliado](informe/main.pdf) | Investigación, método, resultados y referencias BibTeX |
| [Guía de evaluación y aprendizaje](guia/Guia_para_entender_el_proyecto.pdf) | Requisitos, fuentes, fundamentos, fórmulas, resultados y uso paso a paso |
| [Presentación](presentacion/README.md) | 12 diapositivas en PDF, PowerPoint editable y guion de 35 minutos con demo |
| [Proyecto para Overleaf](grupo5_overleaf.zip) | ZIP de fuentes del informe; importar como proyecto existente y seleccionar main.tex |
| [Fuentes abiertas](investigacion/FUENTES_ABIERTAS.md) | Doce publicaciones con enlaces gratuitos y pasajes utilizados |
| [Protocolo experimental](investigacion/PROTOCOLO_EXPERIMENTAL.md) | Datos, particiones, parámetros, selección y métricas |
| [Estado académico](CIERRE_ACADEMICO.md) | Requisitos verificados y condiciones pendientes de entrega |

La guía empieza evaluando las seis secciones de la actividad. El capítulo 7 presenta las fuentes; los capítulos 8–16 desarrollan el aprendizaje y los resultados; el 18 explica la ejecución y el 19, Overleaf. Los documentos son material asistido de estudio y revisión: no certifican autoría estudiantil ni cumplimiento del límite institucional de IA.

## Descargar el proyecto

Usa **Code → Download ZIP** y extrae el ZIP, o clona con Git:

```powershell
git clone https://github.com/chvya/DeeplearningPLN_RNN_LSTM.git
cd DeeplearningPLN_RNN_LSTM
```

Abre PowerShell dentro de la carpeta descargada. El repositorio incluye datos procesados y diez modelos finales: no necesitas entrenar ni descargar artículos para probar la demo. La instalación inicial sí requiere Internet.

## Instalar y ejecutar en Windows

Entorno de referencia: Python 3.12.14 de 64 bits, PyTorch 2.14.0+cpu, NumPy 2.5.3 y Matplotlib 3.11.2. Instala Python 3.12 si `py -3.12 --version` no lo encuentra. Después ejecuta:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install torch==2.14.0+cpu --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt --extra-index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m unittest discover -s codigo -p test_*.py -v
.\.venv\Scripts\python.exe codigo/demo.py
```

Escribe `el presidente del gobierno` y pulsa Enter. El modelo LSTM seleccionado por validación propone, entre otras, `de`, `del` y `vasco`. Usa `/salir` para terminar. No completa letras parciales: predice una palabra después del contexto. Sus sugerencias pueden ser inadecuadas; es un prototipo académico con vocabulario limitado.

Consulta individual:

```powershell
.\.venv\Scripts\python.exe codigo/pln.py predecir --texto "el presidente del gobierno"
```

La demo funciona sin Internet después de instalar dependencias. Las ocho pruebas y la consulta se verificaron en la copia preparada para publicación, con el entorno local existente. No se afirma que se haya probado una instalación nueva en cada sistema operativo.

## Evidencia de resultados

| Modelo | Perplejidad de prueba | Top-5 léxico |
|---|---:|---:|
| Bigrama | 85,93 | 25,62 % |
| RNN, media de tres semillas | 75,60 | 26,58 % |
| LSTM, media de tres semillas | 78,15 | 26,14 % |

Se evaluaron 56 796 objetivos, con contexto 12 y vocabulario de 3 000 entradas. Menor perplejidad significa mejor probabilidad asignada a los objetivos; no representa porcentaje de acierto. UNK interviene en la pérdida, pero no cuenta como acierto léxico. La tasa de desconocidas de prueba es 21,19 %. No se demuestra superioridad general de RNN sobre LSTM.

`resultados/evaluacion_test.json` y `resultados/resumen_comparacion.json` permiten contrastar cifras. Los historiales conservan la evolución por época. La demo elige LSTM por validación dentro de esa arquitectura; no se elige por sus resultados de prueba.

## Reproducir el experimento

```powershell
.\.venv\Scripts\python.exe herramientas/reproducir.py --destino replicas/replica_01
```

El destino debe ser nuevo. Se preparan datos, se ejecutan pruebas y se entrenan diez configuraciones; requiere más tiempo que la demo. Conserva los resultados originales. La réplica usa el corpus incluido. Para reconstruir únicamente figuras y tablas desde los registros:

```powershell
.\.venv\Scripts\python.exe codigo/analizar.py
```

Esta última orden actualiza archivos derivados. El modelo piloto no se publica como parte del conjunto final y no se incluye en sus medias. Los diez modelos finales y sus registros sí se conservan.

## Organización

| Carpeta | Función |
|---|---|
| `codigo/` | Preparación, modelos, entrenamiento, evaluación, demo y ocho pruebas |
| `datos/originales/` | UD Spanish-AnCora r2.17, atribución y licencia |
| `datos/procesados/` | Vocabulario, documentos, oraciones y matrices utilizadas |
| `modelos/` | Pesos finales y configuración de cada entrenamiento |
| `resultados/` | Métricas, historiales, comparación y ejemplos |
| `informe/` | Fuentes LaTeX, BibTeX, plantilla oficial, figuras y PDF |
| `presentacion/` | Diapositivas y guion |
| `guia/` | Guía en PDF y Markdown |
| `investigacion/` | Fuentes, protocolo y registros de acceso |
| `herramientas/` | Descarga, réplica, compilación local y ZIP para Overleaf |

## Atribución y alcance

Consulta [ATRIBUCION_Y_ALCANCE.md](ATRIBUCION_Y_ALCANCE.md). AnCora conserva CC BY 4.0 y sus autores; las transformaciones propias están documentadas. Los artículos completos de terceros no se redistribuyen. Se declara la asistencia de IA y se conservan las condiciones de la plantilla ACM. La publicación del repositorio no sustituye la compilación en Overleaf, la revisión académica, el ensayo de defensa ni la entrega en el aula virtual.
