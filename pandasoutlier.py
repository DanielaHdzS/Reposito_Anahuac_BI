import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

pd.set_option('display.max_column', None)
# print(df)

# df.TotalPurchaseYTD.describe()
# print(df)

# df = df.TotalPurchaseYTD.plot.hist()
# print(plt.show())

# df = df.TotalPurchaseYTD.plot.box()
# print(plt.show())

df = df[df['TotalPurchaseYTD'] > 0]

# print(df.TotalPurchaseYTD.describe())
# df = df.TotalPurchaseYTD.plot.box()
# print(plt.show())

# sns.displot(df['TotalPurchaseYTD'])
# print(plt.show())

# sns.distplot(df['TotalPurchaseYTD'])
# print(plt.show())

# sns.boxplot(df['TotalPurchaseYTD'])
# print(plt.show())

df.TotalPurchaseYTD.describe()
# print(df.TotalPurchaseYTD.describe())

# rango intercualtilico es la diferencia entre el cuartil 25% y el cuartil 75%
q1 = df.TotalPurchaseYTD.quantile(0.25)
q3 = df.TotalPurchaseYTD.quantile(0.75)
print(q1)
print(q3)
iqr = q3-q1
l_sup = q3 + 1.5 * iqr
l_inf = q1 - 1.5*iqr

print(iqr)
print(l_sup)
print(l_inf)

df = df[df['TotalPurchaseYTD'] > l_inf]
df = df[df['TotalPurchaseYTD'] < l_sup]

print(df.TotalPurchaseYTD.describe())

# sns.boxplot(df['TotalPurchaseYTD'])
# print(plt.show()) #aun no sale un outliner despues del 4000

# se usa el 4000 para quitar el outliner
df = df[df['TotalPurchaseYTD'] < 4000]
sns.boxplot(df['TotalPurchaseYTD'])
# print(plt.show())

plt.subplot(1, 2, 1)
sns.distplot(df['TotalPurchaseYTD'])

plt.subplot(1, 2, 2)
sns.boxplot(df['TotalPurchaseYTD'])

print(plt.show())
