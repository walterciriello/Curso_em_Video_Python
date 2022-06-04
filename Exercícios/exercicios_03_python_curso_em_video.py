from inspect import walktree


#upper() coloca todas as letras da string em maiúsculas
# fstring utilizada para inserir as variáveis juntos com as strings

name = input("What's your name?\n").upper()
print(f"Welcome, {name}")