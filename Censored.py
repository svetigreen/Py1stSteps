text = input("Enter your text here: ")
censor_key = input("Enter your key to be censored: ")

strings = text.split()

for index, string in enumerate(strings):
    if censor_key in string:
        strings[index] = '[censored]'
    index += 1

text = " ".join(strings)
print(text)

