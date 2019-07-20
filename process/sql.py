import pyodbc, sys, time
sys.path.append('../idocmanager')
from config import relatedvm
pyodbc.drivers()
## Capture generated Company Code ##
f = open('./bin/companycode.log', 'r')
companycode = f.read()
f.close()
## Check the VM Used and Get the server ##
f = open('./bin/vmclient.log', 'r')
vmclient = f.read()
f.close()
## Check the VM Used and Get the server ##
f = open('./bin/vmserver.log', 'r')
vmserver = f.read()
f.close()
## Check the DB Used ##
f = open('./bin/database.log', 'r')
database = f.read()
f.close()
## Clean the CompanyCode ##
companycode = companycode.translate({ord(i):None for i in "(),;:'!@#$'"})
## SQL Connection ##
conn_client = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV'+vmclient+';DATABASE='+database+';UID=tfuser;PWD=tfuser')
conn_server = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV'+vmserver+';DATABASE='+database+';UID=tfuser;PWD=tfuser')
## Get the last DocumentID from the CompanyCode ##
def select_DocumentID():
    cursor = conn_client.cursor()
    cursor.execute("select top 1 documentid from TFDocument where OwnerSearchCode ='"+companycode+"' order by CreationDate desc")
    for row in cursor:
        f = open('./bin/documentid.log', 'w')
        documentid = str(row)
        ## Clean the DocumentID removing the unwanted characters ##
        documentid = documentid.translate({ord(i):None for i in "(),;:'!@#$' \n"})
        f.write(documentid)
        f.close()

## Run the method above to get the DocumentID ##
select_DocumentID()

## Get the 5 last DocumentStatus from the StatusDescription (Got from the CompanyCode) ##
def  select_DocumentStatus_client():
        cursor = conn_client.cursor()
        cursor.execute("select top 1 StatusDescription from TFDocument where documentid ='"+documentid+"' order by CreationDate desc")
        for row in cursor:
                f = open('./bin/documentstatus.log', 'w')
                documentstatus = str(row)
                f.write(documentstatus)
                documentstatus = documentstatus.translate({ord(i):None for i in "(),;:'!@#$'\n"})
                f.close()
        return documentstatus

def  select_DocumentStatus_server():
        cursor = conn_server.cursor()
        cursor.execute("select top 1 StatusDescription from TFDocument where documentid ='"+documentid+"' order by CreationDate desc")
        for row in cursor:
                f = open('./bin/documentstatus.log', 'w')
                documentstatus = str(row)
                f.write(documentstatus)
                documentstatus = documentstatus.translate({ord(i):None for i in "(),;:'!@#$'\n"})
                f.close()
        return documentstatus


## Run the method above to get the Document Status ##
while select_DocumentStatus_client != 'Documento enviado ao servidor':
        print(select_DocumentStatus_client())
        time.sleep(7)

while select_DocumentStatus_server not in select_DocumentStatus_server():
        print(select_DocumentStatus_server())
        time.sleep(7)
