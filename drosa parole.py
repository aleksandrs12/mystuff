s = input('ievadi paroli: ')
num = False
let = False
upper = False
if len(s) > 7:

    for n in s:
        try:
            int(n)
            num = True
        except:
            if str.isupper(n):
                upper = True
            else:
                let = True

if let and num and upper:
    input('parole ir droša')
else:
    input('parole nav droša')