def coding(text_string: str):
    count = 1
    resuit = ''
    for i in range(len(text_string)-1):
        if text_string[i] == text_string[i+1]:
            count += 1
        else:
            resuit = resuit + str(count) + text_string[i]
            count = 1
    if count > 1 or (text_string[len(text_string)-2] != text_string[-1]):
        resuit = resuit + str(count) + text_string[-1]
    return resuit

def decoding(text_string: str):
    number = ''
    resuit = ''
    for i in range(len(text_string)):
        if not text_string[i].isalpha():
            number += text_string[i]
        else:
            resuit = resuit + text_string[i] * int(number)
            number = ''
    return resuit



# path = 'hw5/PRE/coding.txt'
path = 'hw5/PRE/decoding.txt'

with open(path, 'r') as file:
        text = file.read()

print('Файл содержит следующий текст:\n' + text)

if text[0].isdigit():
    print(f"Текст после дешифровки: {decoding(text)}")
else:
    print(f"Текст после кодировки: {coding(text)}") 
