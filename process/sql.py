import pyodbc
pyodbc.drivers()
## Capture generated Company Code ##
f = open('bin/companycode.log', 'r')
companycode = f.read()
f.close()

conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV19;DATABASE=TFSAASCSDAILY;UID=tfuser;PWD=tfuser')

def select_DocumentID():
    cursor = conn.cursor()
    cursor.execute("select TOP 1 * from TFDocument where OwnerSearchCode='"+str(companycode)+"'")
    for row in cursor:
        print(row)

select_DocumentID()