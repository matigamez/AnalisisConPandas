import pandas as pd

# Carga el archivo vgsales.csv en un DataFrame de Pandas
df = pd.read_csv('./data/vgsales.csv')

# Muestra las primeras 10 filas del DataFrame
print("Primeras 10 filas del DataFrame:")
print(df.head(10))

# Exploración Inicial de los Datos
print("\nÚltimas 5 filas del DataFrame:")
print(df.tail())

print("\nInformación general del DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())

# Inspección de los Datos
print("\nTipos de datos de cada columna:")
print(df.dtypes)

print("\nConteo de valores únicos en la columna 'Genre':")
print(df['Genre'].value_counts())

print("\nValores únicos en la columna 'Platform':")
print(df['Platform'].unique())

# Filtrado de Datos
print("\nFilas donde NA_Sales > 1 millón:")
print(df[df['NA_Sales'] > 1])

print("\nFilas donde JP_Sales < 0.1 millón:")
print(df[df['JP_Sales'] < 0.1])

print("\nFilas donde Genre es 'Action' y Global_Sales > 2 millones:")
print(df.query("Genre == 'Action' and Global_Sales > 2"))

# Slicing de Datos
print("\nSeleccionando columnas 'Name' y 'Global_Sales':")
print(df[['Name', 'Global_Sales']])

print("\nFilas de la 5 a la 10 (inclusive) y columnas 'Name' y 'Genre':")
print(df.loc[4:9, ['Name', 'Genre']])  # Recuerda que loc incluye el límite superior

print("\nPrimeras 5 filas y primeras 3 columnas del DataFrame:")
print(df.iloc[:5, :3])  # iloc excluye el límite superior
