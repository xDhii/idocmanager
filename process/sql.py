import pyodbc
from config import relatedvm
pyodbc.drivers()
## Capture generated Company Code ##
f = open('bin/companycode.log', 'r')
companycode = f.read()
f.close()
## Run the method to check VM and DB used ##
relatedvm.findserver
## Check the VM Used ##
f = open('bin/vmserver.log', 'r')
vmserver = f.read()
f.close()
## Check the DB Used ##
f = open('bin/database.log', 'r')
database = f.read()
f.close()
## Clean the CompanyCode ##
companycode = companycode.translate({ord(i):None for i in "(),;:'!@#$'"})
## SQL Connection ##
conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV'+vmserver+';DATABASE='+database+';UID=tfuser;PWD=tfuser')

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
documentid = documentid.translate({ord(i):None for i in "(),;:'!@#$'"})

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

