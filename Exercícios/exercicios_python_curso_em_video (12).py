#

number = int(input('Enter the number: '))
double = number * 2
triple = number * 3
square_root = number ** (1/2)

print('The double is \033[34m{}\033[m'.format(double))
print('The triple is \033[34m{}\033[m'.format(triple))
print('The square root is \033[34m{:.2f}\033[m'.format(square_root))
