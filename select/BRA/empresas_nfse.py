## Selecao da Empresa NFe ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
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
    xcep = "20091007"
if opt == "b":
    cnpj = "60316817000286"
    inscxmun = "30677173"
    xnome = "Microsoft MST RJ"
    xuf = "RJ"
    xcep = "20091007"
if opt == "c":
    cnpj = "31452113002871"
    inscxmun = "18981"
    xnome = "Clariant S.A Suzano rj"
    xuf = "RJ"
    xcep = "28890001"
if opt == "d":
    cnpj = "46323754000183"
    inscxmun = "102660"
    xnome = "Rockwell Automation SP"
    xuf = "SP"
    xcep = "06715864"
if opt == "e":
    cnpj = "46323754000183"
    inscxmun = "6013110"
    xnome = "Rockwell Automation SP"
    xuf = "SP"
    xcep = "06715864"
if opt == "f":
    cnpj = "24492961000129"
    inscxmun = "3505708"
    xnome = "Sovos NFSe SP"
    xuf = "SP"
    xcep = "06454000"
if opt == "g":
    cnpj = "18628083000204"
    inscxmun = "26914"
    xnome = "Cepheid EQA"
    xuf = "SP"
    xcep = "06696060"
if opt == "h":
    cnpj = "03715819000123"
    inscxmun = "23814"
    xnome = "Mecanotecnica PR"
    xuf = "PR"
    xcep = "83060206"
if opt == "i":
    cnpj = "12796590000190"
    inscxmun = "1302603"
    xnome = "Kerry Ing. e Aromas AM"
    xuf = "AM"
    xcep = "69036520"
if opt == "j":
    cnpj = "02332686001204"
    inscxmun = "3513009"
    xnome = "Kerry do Brasil SP"
    xuf = "SP"
    xcep = "06705045"
if opt == "k":
    cnpj = "29667227000509"
    inscxmun = "3301702"
    xnome = "Lanxess RJ"
    xuf = "RJ"
    xcep = "25221000"
if opt == "l":
    cnpj = "29667227000681"
    inscxmun = "4322004"
    xnome = "Lanxess RS"
    xuf = "RS"
    xcep = "95853000"
if opt == "m":
    cnpj = "29667227001068"
    inscxmun = "2602902"
    xnome = "Lanxess PE"
    xuf = "PE"
    xcep = "54515070"
if opt == "n":
    cnpj = "29667227001220"
    inscxmun = "4322004"
    xnome = "Lanxess RS"
    xuf = "RS"
    xcep = "95853000"
if opt == "o":
    cnpj = "44837524000107"
    inscxmun = "575315"
    xnome = "Codesp SP"
    xuf = "SP"
    xcep = "11015900"

## Definir estado e municipio ##
import estados, municipios

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
