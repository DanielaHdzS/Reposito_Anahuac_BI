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
pd.set_option('display.max_column', None)

df = df[df['DateFirstPurchase'].notna()]
# df = df[df.TotalPurchaseYTD > 0]
# df = df[df.TotalPurchaseYTD < 4000]

print(df)

# Asignacion de tipos de datos correctos, cambiar los datos object por strings
df.MaritalStatus = df.MaritalStatus.astype('string')
df.YearlyIncome = df.YearlyIncome .astype('string')
df.Gender = df.Gender.astype('string')
df.Education = df.Education.astype('string')
df.Occupation = df.Occupation.astype('string')
df.HomeOwnerFlag = df.HomeOwnerFlag.astype('string')
df.NumberCarsOwned = df.NumberCarsOwned.astype('string')
# print(df.info())

df = df.drop('BusinessEntityID', axis=1)
print(df.info())

# sns.pairplot(df)
# print(plt.show())

# sns.pairplot(df, hue='Gender')
# print(plt.show())

# Boxplot1
# sns.boxplot(x='TotalPurchaseYTD', y='Education', data=df)
# # print(plt.show())

# # Boxplot2
# sns.boxplot(x='TotalPurchaseYTD', y='Education', data=df,
#             whis=[0, 100], width=.6, palette='vlag')
# print(plt.show())

# catplot
# sns.set_theme(style='whitegrid')
# g = sns.catplot(data=df, kind='violin', x='Education', y='TotalPurchaseYTD', hue='Gender',
#                 palette='dark', alpha=.6, height=6)

# g.despine(left=True)
# g.set_axis_labels('', 'TotalPurchaseYTD')
# g.legend.set_title('')


# sns.barplot(x='Education', y='TotalPurchaseYTD', hue='Gender', data=df)
# print(plt.show())

ff = df[['Education', 'Occupation', 'NumberCarsOwned']]
ff = df.pivot_table(index='Education', columns='Occupation',
                    values='NumberCarsOwned', aggfunc='first')

# Draw a heatmap with the numeric values in each cell

sns.set_theme(style='whitegrid')
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(ff, annot=True, linewidths=.5, ax=ax)
plt.show()
