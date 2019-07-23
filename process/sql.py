import pyodbc, sys, time
sys.path.append('../idocmanager')
from config import relatedvm
# pyodbc.drivers()
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
## Check the DB Client ##
f = open('./bin/database_client.log', 'r')
database_client = f.read()
f.close()
## Check the DB Server ##
f = open('./bin/database_server.log', 'r')
database_server = f.read()
f.close()
## Clean the CompanyCode ##
companycode = companycode.translate({ord(i):None for i in "(),;:'!@#$'"})
## SQL Connection ##
conn_client = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV'+vmclient+';DATABASE='+database_client+';UID=tfuser;PWD=tfuser')
conn_server = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV'+vmserver+';DATABASE='+database_server+';UID=tfuser;PWD=tfuser')
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

## Check the DB Server ##
f = open('./bin/documentid.log', 'r')
documentid = f.read()
f.close()

## Get the last DocumentStatus from the StatusDescription (Got from the CompanyCode) ##
def  select_DocumentStatus_client():
        cursor = conn_client.cursor()
        cursor.execute("select top 1 StatusDescription from TFDocument where documentid ='"+documentid+"' order by CreationDate desc")
        for row in cursor:
                documentstatusclient = str(row)
                documentstatusclient = documentstatusclient.translate({ord(i):None for i in "(),;:'!@#$'\n"}).strip()
                f = open('./bin/documentstatus.log', 'w')
                f.write(documentstatusclient)
                f.close()
                return documentstatusclient

def  select_DocumentStatus_server():
        cursor = conn_server.cursor()
        cursor.execute("select top 1 StatusDescription from TFDocument where documentid ='"+documentid+"' order by CreationDate desc")
        for row in cursor:
                documentstatusserver = str(row)
                documentstatusserver = documentstatusserver.translate({ord(i):None for i in "(),;:'!@#$'\n"}).strip()
                f = open('./bin/documentstatus.log', 'w')
                f.write(documentstatusserver)
                f.close()
select_DocumentStatus_client()




## Run the method above to get the Document Status ##
while select_DocumentStatus_client() not in ('Documento enviado ao servidor', 'Erro ao enviar documento ao servidor'):
        print(select_DocumentStatus_client())
        time.sleep(7)
        select_DocumentStatus_client

if select_DocumentStatus_client() == 'Erro ao enviar documento ao servidor':
        print("There's something wrong with the document")
        print("Please, check it at the Client Portal")
        sys.exit()
if select_DocumentStatus_client() == 'Documento enviado ao servidor':
        print('Ok, the document was processed and sent to TF Server')
        print('Wait while we check for it on the server')

select_DocumentStatus_server()

while select_DocumentStatus_server not in ('Mensagem 1', 'Mensagem 2', 'Mensagem 3', 'Mensagem 4'):
        print(select_DocumentStatus_server())
        time.sleep(7)

if select_DocumentStatus_server() == 'Message 1':
        print('Return message')

