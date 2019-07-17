import pyodbc
pyodbc.drivers()
## Capture generated Company Code ##
f = open('bin/companycode.log', 'r')
companycode = f.read()
f.close()

## SQL Connection ##
conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV19;DATABASE=TFSAASCSDAILY;UID=tfuser;PWD=tfuser')

## Get the last DocumentID from the CompanyCode ##
def select_DocumentID():
    cursor = conn.cursor()
    cursor.execute("select top 1 documentid from TFDocument where OwnerSearchCode ='"+companycode+"' order by CreationDate desc")
    for row in cursor:
        f = open('bin/documentid.log', 'w')
        print(row, file=f)
        f.close()
        print(row)

## Run the method above to get the DocumentID ##
select_DocumentID()

## Define DocumentID from the table as variable ##
f = open('bin/documentid.log', 'r')
documentid = f.read()
f.close()

## Clean the DocumentID ##
documentid = documentid.translate(None, "'(),")

## Get the 5 last DocumentStatus from the StatusDescription (Got from the CompanyCode) ##
def  select_DocumentStatus():
    cursor = conn.cursor()
    cursor.execute("select top 5 StatusDescription from TFDocument where documentid ='"+documentid+"' order by CreationDate desc")
    for row in cursor:
        f = open('bin/documentstatus.log', 'w')
        print(row, file=f)
        f.close()
        print(row)

## Run the method above to get the Document Status ##
select_DocumentStatus()

