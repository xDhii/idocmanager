## Tipos de documento do Brasil ##
import os, sys
from config import messages

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
    print('\033[91mHmm... A opção digitada não existe')
    opt = input('\033[0mTente novamente: ')

if opt == "a":
    from country import Brasil
if opt == "b":
    from country import Mexico
if opt == "c":
    from country import Uruguay
if opt == "d":
    from country import Argentina

sys.path.insert(0, './process')
import sendtovm

## Opção de reiniciar o processo
recomecar = input('Deseja criar um novo documento? Digite S ou N: ')
recomecar = recomecar.lower()
while recomecar not in ('n', 's'):
    print()
    print('\033[91mHmm... Não entendi')
    recomecar = input('\033[0mDeseja criar um novo documento? Digite S ou N: ')
    recomecar = recomecar.lower()
## Reiniciar o processo ##
if recomecar in ("s", "sim", "yes"):
    os.startfile(sys.argv[0])
    sys.exit("Reiniciando processo, aguarde...")
## Encerrar o processo ##
if recomecar in ("n", "nao", "não", "no"):
    sys.exit()
    