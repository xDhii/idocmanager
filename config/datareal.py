import datetime
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

horacomex = '{message:{fill}{align}{width}}'.format(
   message = (horacomex) ,
   fill='0',
   align='>',
   width=2,
)
horas = '{message:{fill}{align}{width}}'.format(
   message = (horas) ,
   fill='0',
   align='>',
   width=2,
)
minutos = '{message:{fill}{align}{width}}'.format(
   message = (minutos) ,
   fill='0',
   align='>',
   width=2,
)
segundos = '{message:{fill}{align}{width}}'.format(
   message = (segundos) ,
   fill='0',
   align='>',
   width=2,
)

datacompleta = str(ano)+str(mes)+str(dia)
datacompletaseparada = str(ano)+'-'+str(mes)+'-'+str(dia)
datacompletabarra = str(ano)+'/'+str(mes)+'/'+str(dia)
horacompleta = str(horas)+':'+str(minutos)+':'+str(segundos)
horacompletacomex = str(horacomex)+':'+str(minutos)+':'+str(segundos)
# print (str(horacompleta))
# print (str(horacomex) +":"+ str(time.minute) +":"+ str(time.second))
# print (str(horacomex) +":"+ str(time.minute) +":"+ str(segundos))
# print (str(date.year) +"-"+ str(date.month) + "-"+ str(date.day))
# print (str(time.hour) +":"+ str(time.minute) +":"+ str(time.second) +":"+ str(time.microsecond))