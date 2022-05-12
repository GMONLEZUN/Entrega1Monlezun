# Entrega1Monlezun
Este proyecto es la entrega intermedia del proyecto final del curso de Python+Django de CoderHouse


Este proyecto se trata de una página web de contenido sobre el ajedrez, donde tiene una pantalla de inicio con links a diferentes sectores de la página:

Jugadores: donde contiene información de los jugadores cargados, nombre, apellido, nacionalidad y ranking. 
      Además tiene una sección de carga de nuevos jugadores y la posibilidad de realizar búsquedas por nombre, por apellido y por nacionalidad

Humanos vs Máquina: contiene información de los diferentes matches entre jugadores humanos contra software especializado en el juego. 
      Tal como en la sección de jugadores, tiene una sección de carga de nuevos matches y la posibilidad de realizar búsquedas por palabras claves en el título,
      por jugador humano y por año.

Campeones: detalla los diferentes campeones del mundo del ajedrez a lo largo de los diferentes períodos. Posee un espacio de carga de nuevos datos.

*Posee herencia de HTML de un archivo padre.html.
*3 clases de models funcionando: Jugadores, torneos y campeones + un extra que no le agregué funcionalidad aún.
*Todos los models poseen un formulario para la carga de datos.
*En dos models que tenían más sentido incluí el formulario de búsqueda.

---------------------------------------------------------------------------------------------------

Test:
 - Probé en cargar nuevos datos en las tres secciones. 
 - Probé las diferentes búsquedas comprobando que funcionen correctamente.
 - Las búsquedas se basan en el atributo icontains por lo que trae datos aún con búsquedas inexactas.
 - Se probaron los diferentes links, corroborando el correcto funcionamiento.
