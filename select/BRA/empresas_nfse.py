## Selecao da Empresa NFe ##
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFSe ##
messages.empresas_nfse()

## Input e seleção da empresa ##
opt = input('Digite a letra correspondente a empresa: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'):
    print('\033[91mHmm... Não entendi sua resposta')
    opt = input('\033[0mDigite novamente a letra correspondente a empresa: ')
    opt = opt.lower()    

if opt == "a":
    cnpj = "60316817000286"
    inscxmun = "01819925"
    xnome = "Microsoft MST RJ"
    xuf = "RJ"
    cuf = "33"
    xcep = "20091007"
if opt == "b":
    cnpj = "60316817000286"
    inscxmun = "30677173"
    xnome = "Microsoft MST RJ"
    xuf = "RJ"
    cuf = "33"
    xcep = "20091007"
if opt == "c":
    cnpj = "31452113002871"
    inscxmun = "18981"
    xnome = "Clariant S.A Suzano SP"
    xuf = "SP"
    cuf = "35"
    xcep = "28890001"
if opt == "d":
    cnpj = "46323754000183"
    inscxmun = "102660"
    xnome = "Rockwell Automation SP"
    xuf = "SP"
    cuf = "35"
    xcep = "06715864"
if opt == "e":
    cnpj = "46323754000183"
    inscxmun = "6013110"
    xnome = "Rockwell Automation SP"
    xuf = "SP"
    cuf = "35"
    xcep = "06715864"
if opt == "f":
    cnpj = "24492961000129"
    inscxmun = "3505708"
    xnome = "Sovos NFSe SP"
    xuf = "SP"
    cuf = "35"
    xcep = "06454000"
if opt == "g":
    cnpj = "18628083000204"
    inscxmun = "26914"
    xnome = "Cepheid EQA"
    xuf = "SP"
    cuf = "35"
    xcep = "06696060"
if opt == "h":
    cnpj = "03715819000123"
    inscxmun = "23814"
    xnome = "Mecanotecnica PR"
    xuf = "PR"
    cuf = "41"
    xcep = "83060206"
if opt == "i":
    cnpj = "12796590000190"
    inscxmun = "1302603"
    xnome = "Kerry Ing. e Aromas AM"
    xuf = "AM"
    cuf = "13"
    xcep = "69036520"
if opt == "j":
    cnpj = "02332686001204"
    inscxmun = "3513009"
    xnome = "Kerry do Brasil SP"
    xuf = "SP"
    cuf = "35"
    xcep = "06705045"
if opt == "k":
    cnpj = "29667227000509"
    inscxmun = "3301702"
    xnome = "Lanxess RJ"
    xuf = "RJ"
    cuf = "33"
    xcep = "25221000"
if opt == "l":
    cnpj = "29667227000681"
    inscxmun = "4322004"
    xnome = "Lanxess RS"
    xuf = "RS"
    cuf = "43"
    xcep = "95853000"
if opt == "m":
    cnpj = "29667227001068"
    inscxmun = "2602902"
    xnome = "Lanxess PE"
    xuf = "PE"
    cuf = "26"
    xcep = "54515070"
if opt == "n":
    cnpj = "29667227001220"
    inscxmun = "4322004"
    xnome = "Lanxess RS"
    xuf = "RS"
    cuf = "43"
    xcep = "95853000"
if opt == "o":
    cnpj = "44837524000107"
    inscxmun = "575315"
    xnome = "Codesp SP"
    xuf = "SP"
    cuf = "35"
    xcep = "11015900"

## Checar se a empresa é de SP ##
## Caso não seja, tirar a Inscrição municipal do IDOC ##
# if xuf != "SP":
#     inscxmun = "   "

## Ajustar o tamanho da tag xnome para 115 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=115,
)

## Ajustar o tamanho da tag 'inscxmun' para 15 caracteres ## 
inscxmun = '{message:{fill}{align}{width}}'.format(
   message = (inscxmun) ,
   fill=' ',
   align='<',
   width=15,
)