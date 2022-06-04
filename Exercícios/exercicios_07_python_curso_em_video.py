#verificando características da entrada

x = input('Type something: ')
print('The primitive type of this value is: \033[34m{}\033[m'.format(type(x)))
print('Only have spaces? \033[34m{}\033[m'.format(x.isspace()))
print('Is it a number? \033[34m{}\033[m'.format(x.isnumeric()))
print('Is it alphabetical? \033[34m{}\033[m'.format(x.isalpha()))
print('Is it alphanumeric? \033[34m{}\033[m'.format(x.isalnum()))
print('Is it capitalized? \033[34m{}\033[m'.format(x.istitle()))
print('Is it lower case? \033[34m{}\033[m'.format(x.islower()))
print('Is it capital latter? \033[34m{}\033[m'.format(x.isupper()))
