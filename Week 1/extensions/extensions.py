type = input('Enter your file and file type name: ').lower().strip()

if type.endswith('.gif'):
    print('image/gif')
elif type.endswith('.jpg'):
    print('image/jpeg')
elif type.endswith('.jpeg'):
    print('image/jpeg')
elif type.endswith('.png'):
    print('image/png')
elif type.endswith('.pdf'):
    print('application/pdf')
elif type.endswith('.txt'):
    print('text/plain')
elif type.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')


