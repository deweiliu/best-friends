class Bot(object):
    bot_secret='qzV4V-KS1BQ.cwA.6pg.iVbb0ZlWXuFVhhNdkEu29cFhEoClfp0lvAPV1prCcKw'
class Database():
    server = 'tcp:deweiliu.database.windows.net'
    database = 'deweiliu'
    username = 'deweiliu'
    password = 'Azure1234'
    odbc = 'Driver={ODBC Driver 13 for SQL Server};Server='+server+',1433;Database=deweiliu;Uid='+username+'@'+database+';Pwd={%s};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;' % (
    password)
