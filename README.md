# recopilacionNetflix

- En este proyecto se extraen registros de una api que se alimenta de los datos de Netflix, con el objetivo de conformar archivos csv para su posterior utilización.
- La api que se utiliza fue obtenida en el sitio RapidApi y su creador es uNoGS, cabe mencionar que todos los registros que entrega la api se encuentran en ingles
- Para poder consumir esta api, se necesita de una api-key, la cual esta disponibilizada en el proyecto, tambien se puede utilizar sin parametros ya que esta dispone de parametros por defecto
- Dentro de los parametros que se le pueden entregar, estan:
*   limit: es el limite de objetos que entrega la consulta, siendo el defecto de 100 objetos
*  person: es el reparto de actores o directores que conforman la pelicula
*   audio: es el idioma hablado en la pelicula
- Los registros que conforman el objeto de la respuesta de la api son los siguientes:
*   title: nombre de la pelicula
*   img: caratula de la pelicula,
*   title_type: tipo de contenido, en este caso pelicula,
*   netflix_id: identificador unico de Netflix,
*   synopsis: resumen o descripcion de la pelicula,
*   rating: clasificacion dentro de Netflix,
*   year: año de estreno,
*   runtime: duracion de la pelicula,
*   imdb_id: identificador unico en imdb,
*   poster: poster promocional pelicula,
*   top250: se desconoce,
*   op250tv: se desconoce,
*   title_date : fecha de estreno 

  
