## Input da data do documento ##
import os, sys
sys.path.insert(0, './config')
import messages, datareal

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Data manual ou automatica ##
# print ('Deseja inserir a data manualmente?')
# print()
# print('Digite S para inserir manualmente')
# datamanual = input('Digite N para inserir automaticamente a data de hoje:')
# datamanual = datamanual.lower()
# while datamanual not in ('s', 'n'):
#     print ('Nao entendi sua resposta')
#     print()
#     print('Digite S para inserir manualmente')
#     datamanual = input('Digite N para inserir automaticamente a data de hoje:')
#     datamanual = datamanual.lower()
# if datamanual == 's':
#     ## Input do dia do documento ##
#     dia = input('Digite o DIA do documento: ')
#     while len(dia) >= 3:
#         print()
#         print ('\033[91mOpa! O dia do documento deve ter 2 digitos')
#         dia = input('\033[0mTente novamente: ')
#         print()

#     ## Input do mês do documento ##
#     mes = input('Digite o MÊS do documento: ')
#     while len(mes) >= 3:
#         print()
#         print ('\033[91mOpa! O mês deve conter 2 dígitos!')
#         mes = input('\033[0mDigite novamente o MÊS do documento: ')
#         print()

#     ## Input do ano do documento ##
#     ano = input('Digite o ANO do documento: ')
#     while len(ano) >= 5 or len(ano) == 3 or len(ano) <= 1:
#         print()
#         print('\033[91mOpa! O ano deve conter 4 dígitos!')
#         ano = input('\033[0mDigite novamente o ANO do documento: ')
#         print()
#     if len(ano) == 2:
#         ano = "20"+ str(ano)
# if datamanual == 'n':
ano = str(datareal.ano)
mes = str(datareal.mes)
dia = str(datareal.dia)


## Ajuste de caracteres para 2 ##
mes = '{message:{fill}{align}{width}}'.format(
message = (mes) ,
fill='0',
align='>',
width=2,
)
dia = '{message:{fill}{align}{width}}'.format(
message = (dia) ,
fill='0',
align='>',
width=2,
)