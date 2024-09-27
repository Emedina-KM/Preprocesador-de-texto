# Preprocesador de texto

## Descripción del reto

El objetivo del reto es implementar un preprocesador de texto en español, sin utilizar librerías externas. El preprocesador debe cumplir con los siguientes pasos de limpieza:

1. Convertir todo el texto a minúsculas.
2. Eliminar saltos de línea y caracteres que no sean letras.
3. Eliminar cualquier dígito presente en el texto.
4. Tokenizar el texto (convertirlo en una lista de palabras).
5. Remover las stopwords más comunes en español.

## Funcionalidad esperada

El programa esperará leer un archivo `raw-text.txt` que será provisto por el mentor. El programa realizará las operaciones de limpieza, escribiendo el texto procesado en otro archivo llamado `processed-text.txt`.

### Ejemplo:
* `raw-text.txt`: El curso de Python cuesta 100 soles y es excelente. ¡Lo recomiendo!
* `processed-text.txt`: ['curso', 'python', 'cuesta', 'soles', 'excelente.', 'recomiendo']

### Resultado:
* `processed-text.txt`: ['inteligencia', 'artificial', 'ia', 'campo', 'estudio', 'abarca', 'simulación', 'razonamiento', 'humano', 'creación', 'máquinas', 'aprender', 'tomar', 'decisiones', 'años', 'ia', 'avanzado', 'significativamente', 'transformando', 'industrias', 'medicina', 'transporte', 'educaciónel', 'aprendizaje', 'automático', 'rama', 'ia', 'permite', 'computadoras', 'desarrollen', 'habilidades', 'explícitamente', 'programadas', 'seguir', 'instrucciones', 'específicas', 'máquinas', 'analizar', 'cantidades', 'datos', 'detectar', 'patrones', 'mejorar', 'rendimientosin', 'avances', 'surgen', 'preocupaciones', 'ética', 'inteligencia', 'artificial', 'tema', 'discute', 'ampliamente', 'decisiones', 'automatizadas', 'afectar', 'privacidad', 'derechos', 'personas', 'medida', 'ia', 'continúa', 'desarrollándose', 'fundamental', 'establecer', 'regulaciones', 'principios', 'éticos', 'guíen', 'implementaciónpor', 'impacto', 'positivo', 'ia', 'innegable', 'diagnósticos', 'médicos', 'rápidos', 'precisos', 'vehículos', 'autónomos', 'prometen', 'reducir', 'accidentes', 'tránsito', 'aplicaciones', 'ia', 'diversas', 'constante', 'expansión', 'futuro', 'espera', 'inteligencia', 'artificial', 'siga', 'revolucionando', 'vivimos', 'brindando', 'soluciones', 'problemas', 'complejos', 'parecían', 'imposibles', 'resolver']