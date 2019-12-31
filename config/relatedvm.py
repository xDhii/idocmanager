def related_vm():
    f = open('./bin/vmclient.log', 'r')
    vmclient = f.read()
    f.close()
    vmclient = vmclient.translate({ord(i):None for i in "(),;:'!@#$' "})

    if vmclient == "01":
        vmserver = "02"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "03":
        vmserver = "03"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "04":
        vmserver = "05"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "06":
        vmserver = "22"
        database_client = "TFHOUSEDAILY"
        database_server = "TFSAASCSDAILY"

    if vmclient == "07":
        vmserver = "21"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "14":
        vmserver = "14"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "18":
        vmserver = "19"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "23":
        vmserver = "24"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "27":
        vmserver = "28"
        database_client = "TFSAASRTC"
        database_server = "TFSAASCSDAILY"

    if vmclient == "NOPE":
        vmserver = "NOPE"

    f = open('./bin/vmserver.log', 'w')
    f.write(vmserver)
    f.close()

    f = open('./bin/database_client.log', 'w')
    f.write(database_client)
    f.close()

    f = open('./bin/database_server.log', 'w')
    f.write(database_server)
    f.close()