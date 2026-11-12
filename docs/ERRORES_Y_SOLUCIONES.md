# Errores y soluciones

## Antecedentes de la guía

Fuente: `Guia_Video_Python_YouTube 2.pdf`, guía de agosto de 2026, páginas 6 y 7. Son incidencias relatadas por ese documento, no errores reproducidos durante esta revisión del 12/11/2026.

- **403 access_denied en OAuth:** la cuenta del canal no estaba incluida entre los usuarios de prueba de la aplicación. La guía registra que se agregó en Test users y se repitió la autorización.
- **ModuleNotFoundError: tzdata / ZoneInfoNotFoundError en Windows:** faltaba la base IANA para `ZoneInfo("America/Argentina/Buenos_Aires")`. La solución registrada fue instalar `tzdata` en el entorno virtual.

## Hallazgos de esta revisión

- `tzdata` ya estaba instalado (versión 2026.3) y la zona horaria se resolvió correctamente, pero no figuraba en el `requirements.txt` de esta copia. Se incorporó a las dependencias para reproducir el entorno. No se creó un commit que simule la reparación del error histórico.
- La subida estaba configurada a las 15:00 aunque la consigna pide 21:00. Se ajustaron la constante y los textos a las 21:00; se mantiene el comienzo desde mañana.
- El generador recorre toda la lista y puede sobrescribir archivos existentes. Se conserva su implementación; el README explica cómo generar únicamente el pendiente, comprobando antes que el destino no exista.
- El script de subida comprueba existencia, no integridad, de los MP4. Tampoco guarda un registro persistente de subidas ni evita duplicados. No se ejecutó durante esta revisión.

## Validaciones realizadas

Se verificaron sintaxis e importaciones, 20 identificadores únicos con 18 diapositivas cada uno, fuentes locales, zona horaria y programación de días consecutivos atravesando el cambio de año. La solicitud de subida se probó con un cliente simulado, sin red, credenciales ni subida real. Los 19 MP4 se comprobaron con ffprobe y decodificación completa de FFmpeg sin errores.

No se ejecutó OAuth, no se renovaron tokens y no se verificó el canal en YouTube Studio. Los archivos locales de credenciales se conservan excluidos de Git.
