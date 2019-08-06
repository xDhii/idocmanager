zerar = 0
## Check Folio Argentina
try:
    f = open('./select/ARG/folio.txt')
    check = f.read()
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/ARG/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/ARG/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio Brazil
try:
    f = open('./select/BRA/folio.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/BRA/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/BRA/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check RPS Brazil
try:
    f = open('./select/BRA/rps.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/BRA/rps.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/BRA/rps.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio Chile
try:
    f = open('./select/CHL/folio.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/CHL/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/CHL/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio Ecuador
try:
    f = open('./select/ECU/folio.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/ECU/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/ECU/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio MEX ##
try:
    f = open('./select/MEX/folio.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/MEX/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/MEX/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio PER ##
try:
    f = open('./select/PER/folio.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/PER/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/PER/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
## Check Folio URY ##
try:
    f = open('./select/URY/folio.txt')
    f.close()
    print('File found!')
    if check == '':
        f = open('.select/URY/folio.txt')
        f.write(zerar)
        f.close()
    else:
        print('Ok, Next one...')
except FileNotFoundError:
    f = open('./select/URY/folio.txt', 'w')
    f.write('0')
    f.close()
    print("File not found!")
    print("A new file was created")
