high = float(input('How high is the wall in meters? '))
wide = float(input('How wide is the wall in meters? '))
print(f'The total area the wall is \033[34m{high * wide:.2f}\033[m square meters.')
print(f'You will need \033[34m{high * wide / 2:.2f}\033[m cans of paint.')
