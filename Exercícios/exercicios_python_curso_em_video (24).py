price = float(input('What is the price of the product? R$'))
print(f'The new price after the discount is \033[34mR${price - (price * 5 / 100):.2f} ')
