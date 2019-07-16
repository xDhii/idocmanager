import pyodbc
pyodbc.drivers()
## Capture generated Company Code ##
f = open('bin/companycode.log', 'r')
companycode = f.read()
f.close()

conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV19;DATABASE=TFSAASCSDAILY;UID=tfuser;PWD=tfuser')

def select_DocumentID():
    cursor = conn.cursor()
    cursor.execute("select top 5 statusdescription from TFDocumentHistoryFlow where documentid = (select top 1 documentid from TFDocument where OwnerSearchCode ='"+companycode+"' order by CreationDate desc)")
    for row in cursor:
        print(row)

select_DocumentID()