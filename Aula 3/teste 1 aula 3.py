print('=' * 20) # esses iguais são apenas para fins de embelezamento do codigo final 
n1 = int(input('digite um valor: '))
print('=' * 20)
n2 = int(input('digite outro valor: '))
s = n1 + n2
m = n1 * n2 
d = n1 / n2 
di = n1 // n2
e = n1 ** n2 
print('=' * 20) 
print('a soma é {} e o produto é {} e a divisão é {:.3f}' .format(s, m, d))
print('=' * 20)
print('divisão inteira {} e potencia {}' .format(di, e))