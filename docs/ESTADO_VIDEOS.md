# Estado verificado de los videos

Fecha de revisión: 12/11/2026 (Argentina).

Se encontraron 19 MP4, no solo los 18 indicados inicialmente. Todos tienen 324 segundos, H.264, 1280×720, 24 fps y 7776 fotogramas declarados, sin pista de audio. Se decodificó cada archivo completo con `ffmpeg -v error -xerror -threads 1 -i ARCHIVO -map 0:v:0 -f null -`: todos finalizaron con código 0 y sin mensajes de error. Esta es una validación técnica; no equivale a revisión visual de cada diapositiva ni verifica publicaciones en YouTube.

No se detectaron procesos Python/FFmpeg activos al comenzar. No se inició ni detuvo ninguna generación. El video 20 tiene contenido definido (18 diapositivas) y podría generarse por separado en otra sesión; no existe su MP4.

| ID | Tema | Estado | Bytes |
|---|---|---|---:|
| 01 | Qué es Python y por qué deberías aprenderlo | Completo: 5:24 | 1790255 |
| 02 | Variables y tipos de datos en Python | Completo: 5:24 | 1551179 |
| 03 | Condicionales if, elif y else en Python | Completo: 5:24 | 1534433 |
| 04 | Bucles for y while en Python | Completo: 5:24 | 1408263 |
| 05 | Funciones en Python - Guía completa para principiantes | Completo: 5:24 | 1493057 |
| 06 | Listas y diccionarios en Python | Completo: 5:24 | 1300028 |
| 07 | Introducción a la Inteligencia Artificial | Completo: 5:24 | 1710920 |
| 08 | Cómo usar ChatGPT de forma efectiva | Completo: 5:24 | 1606590 |
| 09 | Las mejores herramientas de IA en 2026 | Completo: 5:24 | 1600094 |
| 10 | Cómo crear un CV efectivo en 2026 | Completo: 5:24 | 1501143 |
| 11 | Técnica Pomodoro: cómo estudiar y trabajar mejor | Completo: 5:24 | 1464023 |
| 12 | Cómo organizar tu día para ser más productivo | Completo: 5:24 | 1547773 |
| 13 | Git y GitHub para principiantes | Completo: 5:24 | 1479961 |
| 14 | Cómo empezar a programar desde cero en 2026 | Completo: 5:24 | 1646138 |
| 15 | Errores comunes al aprender a programar | Completo: 5:24 | 1832550 |
| 16 | Qué es una API y por qué es tan importante | Completo: 5:24 | 1526637 |
| 17 | Cómo funciona Internet (explicado simple) | Completo: 5:24 | 1639277 |
| 18 | Seguridad digital básica que todos deberían saber | Completo: 5:24 | 1620305 |
| 19 | Cómo armar un portfolio de programador | Completo: 5:24 | 1573731 |
| 20 | Consejos para conseguir tu primer trabajo en tecnología | Pendiente de generar | — |

## Huellas SHA-256 de los archivos conservados

Se registraron para verificar que esta organización no alteró los videos.

```text
ac47bbf39b0ee8a8f01019cb39f77dc21d3b59f19dc1f87bd0262ef2477bf3d7  video_01.mp4
fe93bfcbcc505b741f3644826f9cbdc09ac739df92030d2b43a566faf529aa63  video_02.mp4
7bbd407132b5f018667b9e8be980fafbc04bc8e6d026fcc0e838f6246a71e442  video_03.mp4
5f08c9ca862dd29a28c58293feca08b237f335054111f2b972f9f1b4902fbd6e  video_04.mp4
1fa146636aebfeb01b680604027dd0b316bd13dd79b5c7e19e256596084357fe  video_05.mp4
47834b43d767c0686eed16110dd29c03335ae08e97d6df39e68c82b33745085c  video_06.mp4
dc618fd74048af3a38c74b38f9a4167874c2e2ca4155b9553538543d818f1cb1  video_07.mp4
fb851a307cbf804d84add020e4d9361e3d2059b36695bd975d576c90db583d3c  video_08.mp4
35a9ad0cb8db05db8066b77b6fb99d9f30d9cae5fd6c3d473c4e65a984ee94ea  video_09.mp4
4c19ef09f8c74fdcfc9a826e0d1b31f0f687df23bf149d3e74139b83eb7f973a  video_10.mp4
50843b2c585003d05fe418580e233eb93cd8ec131506f2645142bc1536cb674b  video_11.mp4
a08982c360c49ea5f68faac160ccef8f635e039cd56dba5511aba8a91e30eeac  video_12.mp4
ff665f5bd1374b1fd177e5c76c5ed387adc68ca436799a4256fa48a7f8c253e7  video_13.mp4
b27ecfd2f942573c1194f545ec869432577acca5a3a675dd133e4119279b5e3c  video_14.mp4
d88690eb9ec486e8867d4ff6ba325e5ef2f7ac5f708f4389fa2275ca4c7eff7a  video_15.mp4
b7e086e2dceed21ada1e3ef62c10d938ce21ba161e7ff7a455be60f5c8f5af89  video_16.mp4
b8aa1e311a69cce89e0cda344e3a6709b2507195443514ae5c8f9524baff07e9  video_17.mp4
73af08b0b3135753702ced391c3190582c45f6cf5959df10d1e1aecb875ee392  video_18.mp4
ff5f60b6a4f37f12a730b89106a285b1187995c58c5b1bde9efe414bb940357f  video_19.mp4
```
