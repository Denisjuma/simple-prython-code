petName = ['Samia', 'Oram', 'Helip']
name = input('Enter petty name: ')
if name not in petName:
    print('Sorry the name not available')
else:
    print('Pet ' + name + ' is available')
