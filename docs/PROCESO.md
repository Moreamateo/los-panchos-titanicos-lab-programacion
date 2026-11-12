# Proceso de incorporación a Git

Revisión del 12/11/2026. La carpeta entregada no tenía `.git`, commits ni remotos. Se conserva el código existente y se inicia un historial real de incorporación, con fechas e identidad Git de la sesión; no se inventa una secuencia histórica de desarrollo.

Orden de incorporación:

1. Dependencias, exclusiones y carpeta de salida vacía. Incluye declarar tzdata, ya instalado y funcionando localmente.
2. Contenidos educativos existentes.
3. Generador MP4 existente.
4. Autenticación OAuth existente.
5. Subida existente, ajustando la hora de 15:00 a 21:00 conforme a la consigna.
6. Registro de errores históricos de la guía y hallazgos de la revisión.
7. Instrucciones, comparación con la guía y estado verificado de los videos.

No se creó un commit de corrección ficticia para tzdata: la guía ya registra esa solución y la instalación local resuelve la zona. La omisión en el manifiesto de esta copia se subsana al preparar dependencias.

Los archivos de credenciales se mantienen locales. Se revisan los archivos a incorporar y los objetos alcanzables del historial para detectar valores de las credenciales locales y patrones de secretos, sin imprimirlos. Si se detectaran secretos históricos, se detendría la publicación y se solicitaría corregirlos sin reescribir un remoto por cuenta propia.

No había repositorio de destino identificado al comenzar: se solicitó su URL al responsable. La publicación requiere identificar ese destino, verificar su historial y conservarlo. No se elige un repositorio ajeno ni se cambia su visibilidad.

No se ejecutó generación, OAuth ni subida a YouTube durante la organización. Los MP4 se mantienen en la computadora y fuera de Git. El PDF se consultó desde la copia local en Descargas; no se incorpora como binario al repositorio.
