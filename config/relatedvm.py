import sys
sys.path.append('../idocmanager')
# def findserver():
f = open('./bin/vmclient.log', 'r')
vmclient = f.read()
f.close()
vmclient = vmclient.translate({ord(i):None for i in "(),;:'!@#$' "})
if vmclient == "01":
    vmserverused = "02"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "03":
    vmserverused = "03"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "04":
    vmserverused = "05"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "06":
    vmserverused = "22"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "07":
    vmserverused = "21"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "14":
    vmserverused = "14"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "18":
    vmserverused = "19"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "23":
    vmserverused = "24"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "27":
    vmserverused = "28"
    database_client = "TFSAASCSDAILY"
    database_server = "TFSAASCSDAILY"
if vmclient == "NOPE":
    vmserverused = "NOPE"

f = open('./bin/vmserver.log', 'w')
f.write(vmserverused)
f.close()

f = open('./bi
database_client = "TFSAASCSDAILY"n/database_server.log', 'w')
f.writ
database_client = "TFSAASCSDAILY"e(database_server)
f.close()