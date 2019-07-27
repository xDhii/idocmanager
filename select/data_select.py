## Input da data do documento ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages, datareal

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

ano = str(datareal.ano)
mes = str(datareal.mes)
dia = str(datareal.dia)

