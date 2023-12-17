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

query = "select*from[Production].[vProductAndDescription]"

prod = pd.read_sql(query, conexion)

print(df)
print(prod)

df_r = pd.merge(df, prod, how="inner", on="ProductID")

print(df_r)
prod["CultureID"] = prod["CultureID"].astype('string')
prod["CultureID"] = prod["CultureID"].str.strip()

prod = prod[prod.CultureID == 'en']

print(prod)

df_r2 = pd.merge(df, prod, how="inner", on="ProductID")
print(df_r2)

df_r2 = pd.merge(df, prod, how="left", on="ProductID")
print(df_r2)
