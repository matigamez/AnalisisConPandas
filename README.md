Este Proyecto desarrolle en el marco del Curso de Analisis de Datos con Pandas en codigndojolatam.la
Las Instrucciones de la practica fueron:

Preparación del Entorno
Asegúrate de tener instalado Pandas en tu entorno de trabajo.
Descarga el archivo vgsales.csv desde Kaggle y colócalo en tu directorio de trabajo.
Cargar los Datos
Carga el archivo vgsales.csv en un DataFrame de Pandas.
Muestra las primeras 10 filas del DataFrame para confirmar que los datos se han cargado correctamente.
Exploración Inicial de los Datos
Muestra las últimas 5 filas del DataFrame.
Utiliza el método info() para obtener información general sobre el DataFrame, incluyendo el número de entradas, nombres de las columnas, tipos de datos y memoria utilizada.
Genera estadísticas descriptivas del DataFrame utilizando el método describe().
Inspección de los Datos
Inspecciona los tipos de datos de cada columna utilizando el atributo dtypes.
Cuenta los valores únicos en la columna Genre utilizando el método value_counts().
Muestra todos los valores únicos en la columna Platform utilizando el método unique().
Filtrado de Datos
Filtra el DataFrame para mostrar solo las filas donde las ventas en América del Norte (NA_Sales) sean mayores a 1 millón.
Filtra el DataFrame para mostrar solo las filas donde las ventas en Japón (JP_Sales) sean menores a 0.1 millón.
Utilizando el método query(), filtra el DataFrame para mostrar las filas donde el género sea Action y las ventas globales (Global_Sales) sean mayores a 2 millones.
Slicing de Datos
Selecciona y muestra solo las columnas Name y Global_Sales del DataFrame.
Utilizando loc[], selecciona y muestra las filas de la 5 a la 10 (inclusive) y las columnas Name y Genre.
Utilizando iloc[], selecciona y muestra las primeras 5 filas y las primeras 3 columnas del DataFrame.

