money = float(input('How much money do you have? R$'))
quotation = float(input('What is the quotation dollar? R$'))
print(f'You can buy \033[34m{money / quotation:.2f} dollars.')
