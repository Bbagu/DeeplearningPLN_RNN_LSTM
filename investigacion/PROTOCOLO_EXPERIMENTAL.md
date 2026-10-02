# Protocolo fijado antes de evaluar prueba

Fecha: 29 de septiembre de 2026. Seis integrantes registrados en `proyecto.json`; entrega: 6 de octubre de 2026.

Se utilizará UD Spanish-AnCora r2.17. Se unen los archivos originales y se redistribuyen documentos completos mediante SHA-256 (`grupo5-v1:` + identificador), con umbrales 80/10/10. Las proporciones por palabra no son exactamente esos porcentajes. Se eliminan oraciones idénticas normalizadas globalmente. Las ventanas nunca cruzan oraciones ni documentos. Estas particiones son propias y no corresponden al benchmark oficial de dependencias.

La representación usa palabras superficiales del campo `text`, minúsculas NFC y tildes; los números se sustituyen por `<num>`. Se omiten los signos de puntuación. Se conservan palabras funcionales y flexión. Vocabulario de 3000 entradas, incluidas PAD, UNK y BOS, ajustado solo sobre entrenamiento. Se seleccionan 100000 objetivos de entrenamiento sin reemplazo, con semilla 20260929, para hacer viable la ejecución en CPU. Bigrama y redes usan los mismos objetivos seleccionados.

Estudio principal: RNN y LSTM, contexto 12 palabras, semillas 17, 29 y 43. Sensibilidad: contextos 4 y 24, semilla 17, exploratoria. Todas las redes: embedding 48, estado oculto 64, una capa unidireccional, dropout 0.15 después del estado recurrente, Adam 0.003, lote 512, 5 épocas, recorte de norma 1. Se guarda la época de menor pérdida de validación. No se ajustará la arquitectura a la vista de prueba.

El piloto utilizó 2048 ejemplos, una época y se excluye de las comparaciones. No consultó las etiquetas de prueba. El tamaño del vocabulario limita la cobertura: se reportará la tasa de desconocidas, sin ocultarla ni aumentarlo después de mirar las métricas finales.

Bigrama con prior unigrama y pseudoconteo: elegir alfa entre 1, 10 y 100 según pérdida de validación. Reportar NLL media y perplejidad en el vocabulario reducido, además de top-1 y top-5 léxicos. Predecir UNK no contará como acertar la palabra original; todas las palabras objetivo permanecen en el denominador.

Una vez terminados los entrenamientos, evaluar prueba. Presentar media y desviación estándar muestral de las tres semillas principales, sin afirmar significación estadística. Las variaciones de contexto solo tienen una semilla. Latencia: lote 1, 10 calentamientos y 100 consultas, mediana y percentil 95; no incluye carga del modelo ni tokenización.

Los resultados corresponden a modelos pequeños sobre prensa y con vocabulario cerrado. No se generalizan automáticamente a chat, español ecuatoriano ni sistemas comerciales. La demo predice la siguiente palabra y presenta cinco sugerencias con sus probabilidades originales, sin renormalizarlas al ocultar símbolos.
