# Prints a sentence in a box of correct width

sentence = input("Your sentence: ")

text_width = len(sentence)
box_width = text_width + 6

print()
print('+' + '-' * (box_width-2) + '+')
print('|' + ' ' * (box_width-2) + '|')
print('|' + ' ' *2 + sentence + ' ' *2 + '|')
print('|' + ' ' * (box_width-2) + '|')
print('+' + '-' * (box_width-2) + '+')
print()

input("Press <enter>")
