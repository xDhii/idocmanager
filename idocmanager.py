## Tipos de documento do Brasil ##
import os, sys, time
sys.path.append('../idocmanager')
from subprocess import Popen
from config import criar_pasta, messages, autofoliocheck

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

##  Opções de países disponíveis
messages.paises_disponiveis()

##  Seleção dos países
print('Which Country do you want to access?')
opt = input('Enter the letter corresponding to the Country: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'z'): # Loop até a seleção de algum País disponível
    print()
    print('\033[91m Hmm... The option you entered does not exist \033[0m')
    opt = input("Let's try again: ")

if opt == "a":
    from country import Argentina
if opt == "b":
    from country import Brasil
if opt == "c":
    from country import Mexico
if opt == "d":
    from country import Uruguay
if opt == "z":
    from process import resetfolio
    goto

from process import sendtovm
from config import log_generate
## Opção de reiniciar o processo
restart = input('Do you want to create a new document? Enter Y or N: ')
restart = restart.lower()
while restart not in ('y', 'n'):
    print()
    print('\033[91m Hmm... I did not understand \033[0m')
    restart = input('Do you want to create a new document? Enter Y or N: ')
    restart = restart.lower()
## Reiniciar o processo ##
if restart == "y":
    ## Reiniciar processo no Windows ##
    if os.name == 'nt':
        p = Popen("python " + filename, shell=True)
        # os.startfile(sys.argv[0])
    ## Reiniciar processo no Linux ##
    if os.name == 'posix':
        filename = sys.argv[0]
        print("Restarting... ")
        p = Popen("python " + filename, shell=True)
    if os.name == 'java':
        print('My bad, not yet implemented for Java systems')
#    sys.exit("Reiniciando processo, aguarde...")
## Encerrar o processo ##
if restart in ("n", "nao", "não", "no"):
    print("Ok, exiting...")
    time.sleep(3)