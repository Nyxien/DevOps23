# Lista som innehåll bilar
bilar = []

# Interaktiv user experience interface
ui_width = 30
print(ui_width * '*')
print(' | STACKMASTER |'.center(ui_width))
print(ui_width * '-')

print(bilar)


print('-' * ui_width)
print('::| MENU |::'.center(ui_width))
print('Push | Push element to stack'.center(ui_width))
print('Pull | Pull element from stack'.center(ui_width))
print('Exit | Exit program'.center(ui_width))
print('-' * ui_width)

user_input = input("Menu>")

if user_input.lower() == 'push':
    bilar.append(input("Ange en bil: "))
