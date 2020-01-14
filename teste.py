import json

def testes():
    with open('.\\resource\\countries.json', 'r') as f:
        countries_dict = json.load(f)
    qtt_opt = int(len(countries_dict))
    # print(qtt_opt)
    i = 0

    for x in range (qtt_opt):
        print(i)
        i += 1


testes()