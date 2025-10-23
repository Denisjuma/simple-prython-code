spam = ['Bananas', 'Apple', 'Tofu', 'Cats', 12,32]

def conv(x):
    return ','.join(str(x) for x in x)
    

print(conv(spam))

