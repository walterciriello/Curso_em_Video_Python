# Exercise number 22

high = float(input("How high is the wall in meters?\n"))
wide = float(input("How wide is the wall in meters?\n"))

total_area = high * wide
cans_of_paint = high * wide / 2

print(f"The total area the wall is \033[34m{total_area:.2f}\033[m square meters.")

print(f"You will need \033[34m{cans_of_paint:.2f}\033[m cans of paint.")
