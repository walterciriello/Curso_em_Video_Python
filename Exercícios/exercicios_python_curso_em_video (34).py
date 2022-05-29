from math import hypot
op_cat = float(input('What is the value of the opposite catheter: '))
ad_cat = float(input('What is the value of thr adjacent catheter: '))
print(f'The value of the hypotenuse is \033[34m{hypot(op_cat, ad_cat):.2f}')
