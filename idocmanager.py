## Tipos de documento do Brasil ##
import os, sys, time
sys.path.append('../idocmanager')
from subprocess import Popen
from config import criar_pasta, messages, autofoliocheck, updater_creator
from country import countries

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

##  Opções de países disponíveis
messages.paises_disponiveis()

##  Seleção dos países
print('Which Country do you want to access?')
opt = input('Enter the letter corresponding to the Country: ')
opt = opt.lower()

while opt not in ('a', 'b', 'c', 'd', 'e','f', 'x', 'z'): # Loop até a seleção de algum País disponível
    print()
    print('\033[91m Hmm... The option you entered does not exist \033[0m')
    opt = input("Let's try again: ")

if opt == "a":
    countries.Argentina()
if opt == "b":
    countries.Brasil()
if opt == "c":
    countries.Chile()
if opt == "d":
    countries.Mexico()
if opt == "e":
    countries.Peru()
if opt == "f":
    countries.Uruguay()
if opt == "x":
    updater_creator.create_updater()
    os.system("start /B start cmd.exe @cmd /k Updater.bat")
    sys.exit()
if opt == "z":
    from process import resetfolio
    sys.exit()

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
        os.system("start /B start cmd.exe @cmd /k python idocmanager.py")
    ## Reiniciar processo no Linux ##
    if os.name == 'posix':
        filename = sys.argv[0]
        print("Restarting... ")
        p = Popen("python " + filename, shell=True)
    if os.name == 'java':
        print('My bad, not yet implemented for Java systems')
    sys.exit()
## Encerrar o processo ##
if restart == "n":
    print("Ok, exiting...")
    time.sleep(3)
    sys.exit()