## Tipos de documento do Brasil ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
f = open('bin/country.log', 'w')
f.write('Argentina')
f.close()
f = open('bin/document.log', 'w')
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents")
import documents
## Opçoes de documentos disponiveis ##
print('Available documents: ')
print()
print('\033[1;30;47m A \033[0m - \033[4mARG - Exportation Invoice (With CUIT Destino)\033[0m')
print('\033[1;30;47m B \033[0m - \033[4mARG - Exportation Invoice (Without CUIT Destino)\033[0m')
print('\033[1;30;47m C \033[0m - \033[4mARG - Local Invoice MTX CAEA\033[0m')
print('\033[1;30;47m D \033[0m - \033[4mARG - Local Invoice MTX\033[0m')
print('\033[1;30;47m E \033[0m - \033[4mARG - Local Invoice MTX CAE & CAEA\033[0m')
print('\033[1;30;47m F \033[0m - \033[4mARG - Local Invoice\033[0m')

print()
print("Got it. What kind of document do you want to create?")
opt = input('Enter the letter corresponding to the document type: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'e', 'f'):
    print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
    opt = input("Let's try again. Enter the corresponding letter: ")
    opt = opt.lower()

if opt == "a":
    document = "Argentina Exportation Invoice"
    documents.ARG_Exportation_Invoice_WithCUITDestino()
    # from documents import ARG_Exportation_Invoice_WithCUITDestino
if opt == "b":
    document = "Argentina Exportation Invoice"
    documents.ARG_Exportation_Invoice_WithoutCUITDestino
if opt == "c":
    document = "Argentina Local Invoice MTX CAEA"
    documents.ARG_Local_Invoice_MTX_CAEA
if opt == "d":
    document = "Argentina Local Invoice MTX"
    documents.ARG_Local_Invoice_MTX
if opt == "e":
    document = "Argentina Local Invoice MTX CAE & CAEA"
    documents.ARG_Local_Invoice_MTXCAECAEA
if opt == "f":
    document = "Argentina Local Invoice"
    documents.ARG_Local_Invoice

f.write(document)
f.close()