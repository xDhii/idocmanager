import os, time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def restart():
    f = open('./bin/documentstatus.log', 'r+')
    status = f.read()
    f.close()
    return status

while restart() != '1':
    time.sleep(3)
    limpar_tela()
    print('Consultando Status')
    print(restart())

if restart() == '1':
    print('Teste 1 OK')