import pyodbc

servidor = 'EVANGELION\SQLEXPRESS'
nombre_bd = 'AdventureWorks2019'
nombre_usuario = 'sa'
password = '1510'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    # conexion exitosa
    print('La conexion fue exitosa ya puede usar la informacion de la base de datos ' + nombre_bd)

except Exception as e:
    # Atrapar error
    print('Ocurrio un error al conectar a SQL Server: ', e)


query = "select * from AdventureWorks2022.dbo.productos_venta"
registros = conexion.execute(query)

for reg in registros:
    print(reg)
