import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns

servidor = r'EVANGELION\SQLEXPRESS'
nombre_bd = 'AdventureWorks2019'
nombre_usuario = 'sa'
password = '1510'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    # conexión exitosa
    print('La conexión fue exitosa ya puede usar la información de la base de datos' + nombre_bd)

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)

query = "select*from [Sales].[vPersonDemographics]"
df = pd.read_sql(query, conexion)

# print(df)

# print(df.info())

# pd.set_option('display.max_columns', None)
# print(df)

# print(df.isna().sum())

# print(df.isna())

# print(df.NumberCarsOwned.isna().sum())
# print(df.NumberCarsOwned.mean())
# print(df.NumberCarsOwned.median())
# print(df.NumberCarsOwned.describe())

valor = df.NumberCarsOwned.median()
print(valor)

df['NumberCarsOwned'] = df['NumberCarsOwned'].fillna(valor)
print(df['NumberCarsOwned'])

# print(df.isna().sum())


dfl = df.copy()
df.dropna(subset=['DateFirstPurchase'], inplace=True)
print(df.isna().sum())
