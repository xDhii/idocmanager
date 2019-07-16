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


## Ajuste de caracteres para 2 ##
# mes = '{message:{fill}{align}{width}}'.format(
# message = (mes) ,
# fill='0',
# align='>',
# width=2,
# )
# dia = '{message:{fill}{align}{width}}'.format(
# message = (dia) ,
# fill='0',
# align='>',
# width=2,
# )
