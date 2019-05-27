## Script para enviar documento para a VM ## -
import shutil, sys, os

## Encontrar a pasta inicial ##
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Seleção de enviar o IDOC para a VM ou encerrar o processo ##
print('Tudo certo ate aqui.')
enviaridoc = input('Digite S para enviar ou N para encerrar o processo e salvar o IDOC na pasta: ')
enviaridoc = enviaridoc.lower()
while enviaridoc not in ('n', 's'):
    print('\033[91mHmm... Não entendi sua resposta')
    enviaridoc = input('\033[0mVamos tentar novamente. Digite S ou N: ')
    enviaridoc = enviaridoc.lower()

## Seleção da VM e envio do IDOC via rede conforme resposta ##
if enviaridoc in ('s', 'sim', 'yes'):
    messages.limpar_tela()
    messages.mensageminicial()
    messages.tryagain()
    print('\033[0m')
# Não enviar IDOC conforme resposta ##
if enviaridoc in ("n", "nao", "não", "no", "not"):
    print()
    print('\033[92mOk! O documento gerado está dentro da pasta IDOC ;)')
print('\033[0m')