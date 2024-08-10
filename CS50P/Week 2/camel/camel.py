
c = input('Enter camelCase: ')
n = ''
for s in c:
    if s.isupper():
        n = n + '_' + s.lower()
    else:
        n = n + s
print(n)
