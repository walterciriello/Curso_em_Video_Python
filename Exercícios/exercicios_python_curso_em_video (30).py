day = int(input('How many days did the car lease last? '))
km = float(input('How many km did the vehicle travel? '))
print(f'The total amount to be paid is \033[34mR${day*60+km*0.15:.2f}')
