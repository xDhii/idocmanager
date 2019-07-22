import os, sys, shutil, time
from config import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

zerar = 0
## ARG ##
f = open('./select/ARG/folio.txt', 'w')
print(zerar, file=f)
f.close()
## BRA NFE ##
f = open('./select/BRA/folio.txt', 'w')
print(zerar, file=f)
f.close()
## BRA NFSE ##
f = open('./select/BRA/rps.txt', 'w')
print(zerar, file=f)
f.close()
## MEX ##
f = open('./select/MEX/folio.txt', 'w')
print(zerar, file=f)
f.close()
## URY ##
f = open('./select/URY/folio.txt', 'w')
print(zerar, file=f)
f.close()

print('Okay, all the folios was reseted.')
print()
print('Do you want to clean all the log files?')
cleanlog = input('Y to clean or N to leave: ')
cleanlog = cleanlog.lower()
print()
if cleanlog == 'y':
    print('Roger that!')
    f = open('./bin/companycode.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/companyname.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/database.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/country.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/documentid.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/documentstatus.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/folio.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/vmclient.log', 'w')
    f.write('\n')
    f.close()
    f = open('./bin/vmserver.log', 'w')
    f.write('\n')
    f.close()
    shutil.rmtree('logs/')
    shutil.rmtree('idoc/')
    print('Everything is clear!')
elif cleanlog == 'n':
    print('Okay, bye bye.')
else:
    print('I did not understand your answer...')
    print('I will not touch your logs.')
time.sleep(5)