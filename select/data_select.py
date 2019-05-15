## Input da data do documento ##
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Input do dia do documento ##
dia = input('Digite o DIA do documento: ')
while len(dia) >= 3:
    print()
    print ('\033[91mOpa! O dia do documento deve ter 2 digitos')
    dia = input('\033[0mTente novamente: ')
    print()
dia = '{message:{fill}{align}{width}}'.format(
   message = (dia) ,
   fill='0',
   align='>',
   width=2,
)

## Input do mês do documento ##
mes = input('Digite o MÊS do documento: ')
while len(mes) >= 3:
    print()
    print ('\033[91mOpa! O mês deve conter 2 dígitos!')
    mes = input('\033[0mDigite novamente o MÊS do documento: ')
    print()
mes = '{message:{fill}{align}{width}}'.format(
   message = (mes) ,
   fill='0',
   align='>',
   width=2,
)

## Input do ano do documento ##
ano = input('Digite o ANO do documento: ')
while len(ano) >= 5 or len(ano) == 3 or len(ano) <= 1:
    print()
    print('\033[91mOpa! O ano deve conter 4 dígitos!')
    ano = input('\033[0mDigite novamente o ANO do documento: ')
    print()
if len(ano) == 2:
    ano = "20"+ str(ano)
