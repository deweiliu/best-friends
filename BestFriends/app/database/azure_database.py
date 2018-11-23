import pyodbc
from app.variables import Database
class AzureDatabase(object):
    @staticmethod
    def get_connection():
        connection = pyodbc.connect(Database.odbc)
        return connection

    @staticmethod
    def close(cursor):
        try:
            cursor.close()
            del cursor
        except:
            pass

    @staticmethod
    def execute(command):

        connection = AzureDatabase.get_connection()
        csr = connection.cursor()
        print('Executing command %s'%(command))
        csr.execute(command)
        try:
            rows = csr.fetchall()
        except:
            rows = None
        finally:
            connection.commit()
            AzureDatabase.close(csr)
        return rows
    @staticmethod
    def create(table_name,*attributes):
        args_str = ", ".join(attributes)
        command = "IF NOT EXISTS (SELECT * from sysobjects where name='%s') CREATE TABLE %s (%s);" % (table_name,table_name,args_str)
        return AzureDatabase.execute(command)



    @staticmethod
    def drop(table_name):
        command = "IF EXISTS (SELECT * from sysobjects where name='%s') DROP TABLE dbo.%s;" % (table_name,table_name)
        return AzureDatabase.execute(command)


        
