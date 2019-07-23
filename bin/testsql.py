import os, time, pyodbc
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

conn_client = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV18;DATABASE=TFSAASRTC;UID=tfuser;PWD=tfuser')
# conn_server = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=INVQASRV'+vmserver+';DATABASE='+database+';UID=tfuser;PWD=tfuser')
## Get the last DocumentID from the CompanyCode ##

cursor = conn_client.cursor()
cursor.execute("select top 1 documentid from TFDocument where OwnerSearchCode = '24492961000129' order by CreationDate desc")
for row in cursor:
    f = open('./bin/documentid.log', 'w')
    documentid = str(row)
    ## Clean the DocumentID removing the unwanted characters ##
    documentid = documentid.translate({ord(i):None for i in "(),;:'!@#$' \n"})
    f.write(documentid)
    f.close()
    print(documentid)


# def restart():
#     f = open('./bin/documentstatus.log', 'r+')
#     status = f.read()
#     f.close()
#     return status

# while restart() != '1':
#     time.sleep(3)
#     limpar_tela()
#     print('Consultando Status')
#     print(restart())

# if restart() == '1':
#     print('Teste 1 OK')