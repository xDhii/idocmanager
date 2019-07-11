import datetime, sys
sys.path.append('../idocmanager')
from idocmanager import country, document


f = open('idocmanager.py', 'r')
date_time = datetime.datetime.now()

date = date_time.date()  # Retorna a data
time = date_time.time()  # Retorna a hora
horacomex = time.hour - 5# Retorna a horas atrasada
horas = time.hour        # Retorna a hora
minutos = time.minute    # Retorna os minutos
segundos = time.second   # Retorna os segundos
ano = date.year          # Retorna o ano
mes = date.month         # Retorna o mes
dia = date.day           # Retorna o dia

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

datacompleta = str(ano)+str(mes)+str(dia)
datacompletabarra = str(ano)+'/'+str(mes)+'/'+str(dia)
horacompleta = str(horas)+str(minutos)+str(segundos)
horacompletaseparada = str(horas)+':'+str(minutos)+':'+str(segundos)

f = open('./logs/log_'+ str(datacompleta) +'.txt', 'a+')

f.write('Some document was generated at '+ str(horacompletaseparada) +' on '+ str(datacompletabarra) +'\n')
f.write('It was generated '+ str(variaveis.document) + ' for '+ str(variaveis.country) +'\n')
f.write('\n')
f.close()