
def findserver():
    f = open('bin/vm.log', 'r')
    vmclient = f.read()
    f.close()
    if vmclient == "01":
        vmserver = "02"
        database = "TFSAASCSDAILY"
    if vmclient == "03":
        vmserver = "03"
        database = "TFSAASCSDAILY"
    if vmclient == "04":
        vmserver = "05"
        database = "TFSAASCSDAILY"
    if vmclient == "06":
        vmserver = "22"
        database = "TFSAASCSDAILY"
    if vmclient == "07":
        vmserver = "21":
        database = "TFSAASCSDAILY"
    if vmclient == "14":
        vmserver = "14"
        database = "TFSAASCSDAILY"
    if vmclient == "18":
        vmserver = "19"
        database = "TFSAASCSDAILY"
    if vmclient == "23":
        vmserver = "24"
        database = "TFSAASCSDAILY"
    if vmclient == "27":
        vmserver = "28":
        database = "TFSAASCSDAILY"
    if vmclient = "NOPE":
        vmserver = "NOPE"
    f = open('vmserver.log', 'w')
    f.write(vmserver)
    f.close()
    f = open('database.log', 'w')
    f.write(database)
    f.close()