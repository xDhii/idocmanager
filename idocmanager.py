## Tipos de documento do Brasil ##
import os, sys
sys.path.append('../idocmanager')
from subprocess import Popen
from config import criar_pasta, messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

##  Opções de países disponíveis
messages.paises_disponiveis()

##  Seleção dos países
print()
print('Qual País você deseja acessar?')
opt = input('Digite a letra correspondente ao País: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c'): # Loop até a seleção de algum País disponível
    print()
    print('\033[91m Hmm... A opção digitada não existe \033[0m')
    opt = input('Tente novamente: ')

if opt == "a":
    from country import Brasil
if opt == "b":
    from country import Mexico
if opt == "c":
    from country import Uruguay
if opt == "d":
    from country import Argentina

from process import sendtovm

## Opção de reiniciar o processo
recomecar = input('Deseja criar um novo documento? Digite S ou N: ')
recomecar = recomecar.lower()
while recomecar not in ('n', 's'):
    print()
    print('\033[91m Hmm... Não entendi \033[0m')
    recomecar = input('Deseja criar um novo documento? Digite S ou N: ')
    recomecar = recomecar.lower()
## Reiniciar o processo ##
if recomecar in ("s", "sim", "yes"):
    ## Reiniciar processo no Windows ##
    if os.name == 'nt':
        os.startfile(sys.argv[0])
    ## Reiniciar processo no Linux ##
    if os.name == 'posix':
        filename = sys.argv[0]
        print("Reiniciando ")
        p = Popen("python " + filename, shell=True)
    if os.name == 'java':
        print('Foi mal, ainda nao implementei para sistemas Java')
    sys.exit("Reiniciando processo, aguarde...")
## Encerrar o processo ##
if recomecar in ("n", "nao", "não", "no"):
    sys.exit()