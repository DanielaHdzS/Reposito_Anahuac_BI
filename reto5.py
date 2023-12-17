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

query = "select*from [Sales].[vStoreWithDemographics]"
df = pd.read_sql(query, conexion)


df.Name = df.Name.astype('string')
df.BankName = df.BankName.astype('string')
df.BusinessType = df.BusinessType.astype('string')
df.Specialty = df.Specialty.astype('string')
df.Brands = df.Brands.astype('string')
df.Internet = df.Internet.astype('string')

# sns.barplot(x='BusinessType', y='AnnualSales', data=df)
# print(plt.show())

# sns.barplot(x='BusinessType', y='NumberEmployees',
#             data=df, palette='dark')
# print(plt.show())

# sns.boxplot(x='BusinessType', y='NumberEmployees',
#             data=df, palette='dark')
# print(plt.show())
q1 = df.AnnualRevenue.quantile(0.25)
q3 = df.AnnualRevenue.quantile(0.75)
print(q1)
print(q3)
iqr = q3-q1
l_sup = q3 + 1.5 * iqr
l_inf = q1 - 1.5*iqr

print(iqr)
print(l_sup)
print(l_inf)

df = df[df['AnnualRevenue'] > l_inf]
df = df[df['AnnualRevenue'] < l_sup]


print(df.AnnualRevenue.describe())


ff = df[['BusinessType', 'Specialty', 'AnnualRevenue']]
ff = df.pivot_table(index='BusinessType', columns='Specialty',
                    values='AnnualRevenue', aggfunc='first')

sns.set_theme(style='whitegrid')
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(ff, annot=True, linewidths=.5, ax=ax)
plt.show()
