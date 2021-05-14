import day8_1_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(day8_1_art.logo)


def ceasar(cypherdir, textstr, shiftamt):
    text_list = list(textstr)
    modified_list = []
    # convert text to alphabet index
    for a in range(0, len(text_list)):
        if text_list[a] in alphabet:
            index = alphabet.index(text_list[a])
            if cypherdir == "encode":
                modified_index = index + shiftamt
                if modified_index >= len(alphabet):
                    modified_index -= len(alphabet)
            if cypherdir == "decode":
                modified_index = index - shiftamt
            # new text in list
            modified_list.append(alphabet[modified_index])
        else:
            modified_list.append(text_list[a])
    print(f"The {cypherdir}d string is '{''.join(modified_list)}'")


run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(cypherdir=direction, textstr=text, shiftamt=shift)
    if input("Run again? y/n ".lower()) == "n":
        run = False

# def encrypt(textstr, shiftamt):
#     text_list = list(textstr)
#     coded_list = []
#     #convert text to alphabet index
#     for a in range(0,len(text_list)):
#         index = alphabet.index(text_list[a])
#         coded_index = index + shiftamt
#         #catch beyond z index
#         if coded_index >= len(alphabet):
#             coded_index -= len(alphabet)
#         #new text in list
#         coded_list.append(alphabet[coded_index])
#     print(''.join(coded_list))
#
#
# def decrypt(codedtext, shiftamt):
#     coded_list = list(codedtext)
#     text_list = []
#     #convert text to alphabet index
#     for a in range(0,len(coded_list)):
#         index = alphabet.index(coded_list[a])
#         decoded_index = index - shiftamt
#
#         #new text in list
#         text_list.append(alphabet[decoded_index])
#     print(''.join(text_list))

# if direction == "encode":
#     encrypt(textstr=text, shiftamt=shift)
# elif direction == "decode":
#     decrypt(codedtext=text, shiftamt=shift)
# else:
#     print("Please reconfirm if encoding or decoding.")