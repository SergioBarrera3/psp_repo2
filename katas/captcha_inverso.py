# 1. Captcha inverso
# Sergio R. Barrera Flores

print('Introduzca la secuencia: ')
valorIntroducido = input()
digitos = list(valorIntroducido)
total = 0
x = 0
for i in digitos[:-1]:   
    try:
        if digitos[x] == digitos[x+1]:
            total += int(i)
    except:
        pass 
    x += 1   
if digitos[x] == digitos[-0]:
    total += int(digitos[-0])  
print(total)
