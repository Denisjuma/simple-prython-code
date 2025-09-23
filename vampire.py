name = input('Enter your name: ')
age = int(input('Enter your age: '))
name=lower().name
print(name)
if name == 'alice':
    print('Hi',  name)
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
