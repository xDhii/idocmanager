## Script para enviar documento para a VM ## -
import shutil, sys, os
import os, sys
sys.path.append('../idocmanager')
from config import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Seleção de enviar o IDOC para a VM ou encerrar o processo ##
print('Ok, everything is fine.')
print('Do you want to send the document to TF or just save the IDOC?')
enviaridoc = input('Enter Y to send or N to save it: ')
enviaridoc = enviaridoc.lower()
while enviaridoc not in ('y', 'n'):
    print('\033[91m Hmm... I did not understand \033[0m')
    enviaridoc = input("Let's try again. Enter Y or N: ")
    enviaridoc = enviaridoc.lower()

## Seleção da VM e envio do IDOC via rede conforme resposta ##
if enviaridoc == 'y':
    messages.limpar_tela()
    messages.mensageminicial()
    messages.tryagain()
    print('\033[0m')
# Não enviar IDOC conforme resposta ##
if enviaridoc == 'n':
    print()
    print('\033[92m Ok! The document is in the IDOC Folder ;) \033[0m')
print('\033[0m')
