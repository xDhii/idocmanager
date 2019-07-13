## Tipos de documento do Brasil ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
f = open('bin/country.log', 'w')
f.write('Brasil')
f.close()
f = open('bin/document.log', 'w')
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents/BRA")
## Opçoes de documentos disponiveis ##
print('Available documents: ')
print()
print('\033[1;30;47m A \033[0m - \033[4mBRA - NFe       \033[0m')
print('\033[1;30;47m B \033[0m - \033[4mBRA - NFSe      \033[0m')

print()
messages.document_select()

if opt == "a":
    document = "Brazil NFe"
    import BRA_NFE
if opt == "b":
    document = "Brazil NFSe"
    import BRA_NFSE

f.write(document)
f.close()