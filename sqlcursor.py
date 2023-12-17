import pyodbc

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
    print("Ocurrió un error al conectar SQL Server: ", e)

query = "SELECT [BusinessEntityID],[FirstName],[LastName]," \
    + "[PostalCode],[City] FROM [Sales].[vSalesPerson]"

cursor = conexion.cursor()

registros = cursor.execute(query).fetchall()


for reg in registros:
    print(reg)
