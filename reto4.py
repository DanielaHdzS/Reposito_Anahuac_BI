import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

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

query = "SELECT [BusinessEntityID],[SalesLastYear]," \
    + "[CountryRegionName],[City] FROM [Sales].[vSalesPerson]"\


df = pd.read_sql(query, conexion)
print(df)

print(df.describe())

grafico = df.plot.barh(y='SalesLastYear', x='City')
grafico2 = plt.show()

print(grafico2)
