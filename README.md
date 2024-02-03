# Final Project

La idea de este proyecto final es crear un programa que actue como buscador en una web de pisos en NYC.

En primer lugar en el datset alamcenamos todos los pisos disponibles que hayan.

Con el script de cleaning vamos a realizar una limpieza de el dataset:

    1-  Borrar las columnas donde mas del 30% de los datos sean nulos:

        1. Primero creamos una funcion que cuente los nulos en cada columnas.

        2. Creamos otra función que coja el recuento de nulos de la función anterior y lo compare con el 30% del   total del df, si es mayor, elimina la columna, sino lo es pasa.

        3. Por ultimo una función que nos permita comprobar todas las columnas del dataset.

    2- Borrar todas aquellas columnas que esten duplicadas.

    3- Almacenar el dataset limpio en la carpeta de datasets.
    
Con el script de data analysis vamos a realizar un pequeño analisis de nuestro dataframe:

    1- En primer lugar realizar una visualización general de algunas caracteristicas de las variables numericas con df.describe().

    2- Mostrar que valores unicos tiene una columna.

    3- Hacer un grafico histograma de una una columna especifica.

    4- Realizar un grafico boxplot de una columna especifica.

    5- Hacer un grafico de correlación de las columnas numericas.

    6- Mostrar un grafico de barras con los precios medios de cada barrio.

Con el script de filtering, el cliente podrá introducir sus preferencias y conseguir un resultado:

    1- Especificar cual es el barrio en el que quiere la casa.

    2- Especificar el tipo de habitación.

    3- Espicificar el precio maximo que quiere pagar.

    4- Especificar las noches minimas que quiere.

    5- Especificar la disponibilidad que quiere.

    6- Una vez se han aplicado todos estos filtros, el dataset se almacena en la carpeta outputs.

Por ultimo esta el script que muestra cuales han sido los resultados finales que se adaptan a las necesidades del cliente:

    1- Nos muestra cual es el datframe final.


# Requirements & usage

scripts --> python-1
tests --> python-1
pytest
flake8 --> flake8 folder/to/lint
Pylint --> pylint folder/to/lint

