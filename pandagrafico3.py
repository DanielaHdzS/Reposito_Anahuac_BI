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

query = "select year(a.ModifiedDate) año, a.ProductID ,[Name], avg(UnitPrice) as AVGUnitprice, sum(LineTotal) sumLineTotal" \
    " from [Sales].[SalesOrderDetail] a inner join [Production].[Product] b" \
    " on a.ProductID = b.ProductID" \
    " group by year(a.ModifiedDate),a.ProductID,[Name]"

df = pd.read_sql(query, conexion)

total_año = df.año.value_counts()
print(total_año)

barras = total_año.plot.barh()  # bar para vertical y barh para horizontal
barras1 = plt.show()
print(barras1)

barras = total_año.plot.pie()  # bar para vertical y barh para horizontal
barras1 = plt.show()
print(barras1)
