def censor_text(text, key):
    strings = text.split()
    censored_count = 0
    text_len = 0

    for index, string in enumerate(strings):
        if key in string.lower():
            strings[index] = '[censored]'
            censored_count += 1
        index += 1

    text_len = len(strings)
    text = " ".join(strings)

    return text, censored_count, text_len


text_input = input("Enter your text here: ")
censor_key_input = input("Enter your key to be censored: ").lower()

text_censored, count_censored, count = censor_text(text_input, censor_key_input)

print("#of words proceeded:", count)
print("#of words censored:", count_censored)
print("---------------------------")
print("Censored text: ", text_censored)
