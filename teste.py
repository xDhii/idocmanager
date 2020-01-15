import json

# def testes():
with open('.\\resource\\countries.json', 'r') as f:
    countries_dict = json.load(f)
# qtt_opt = int(len(countries_dict['countries']))
# print(qtt_opt)
# i = 0
# initial_char = int(97)
# char = chr(initial_char)
# print(countries_dict['countries'])
# for x, y in countries_dict['countries'].items():
#     print(countries_dict['countries'][chr(initial_char)])
#     globals()
#     initial_char += 1
#     print(x)
#     print(y)
#     x = y
    # for k, v in y.items():
    #     print(k)
    #     print(v)
print("Test")

a = countries_dict['countries']
b = list(a)

print(a)
print(b)

for i in b:
    print(i)

print('Debug Here')
# testes()