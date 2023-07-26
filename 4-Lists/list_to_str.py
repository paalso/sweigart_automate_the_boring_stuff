def add_and(L):
    if len(L) < 2:
        return ''.join(L)
    return ', '.join(L[:-1]) + ', and ' + L[-1]


spam = ['apples', 'bananas', 'tofu', 'cats']
print(add_and(spam))

spam = ['apples', 'bananas']
print(add_and(spam))

spam = ['apples']
print(add_and(spam))

spam = []
print(add_and(spam))
