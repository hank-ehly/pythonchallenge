# First attempt
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decoded_message = list()
alph = list("abcdefghijklmnopqrstuvwxyz")

for i, char in enumerate(message):
    if char not in alph:
        decoded_message.insert(len(decoded_message), char)
        continue

    char_alph_idx = alph.index(char)
    next_alph_idx = char_alph_idx + 2

    if next_alph_idx >= len(alph):
        next_alph_idx = next_alph_idx - len(alph)

    decoded_message.insert(len(decoded_message), alph[next_alph_idx])

decoded_message = ''.join(map(str, decoded_message))
print(decoded_message)

# Second attempt
table = str.maketrans({
    'a': 'c',
    'b': 'd',
    'c': 'e',
    'd': 'f',
    'e': 'g',
    'f': 'h',
    'g': 'i',
    'h': 'j',
    'i': 'k',
    'j': 'l',
    'k': 'm',
    'l': 'n',
    'm': 'o',
    'n': 'p',
    'o': 'q',
    'p': 'r',
    'q': 's',
    'r': 't',
    's': 'u',
    't': 'v',
    'u': 'w',
    'v': 'x',
    'w': 'y',
    'x': 'z',
    'y': 'a',
    'z': 'b',
})

decoded_message = 'map'.translate(table)
print(decoded_message)

# i hope you didnt translate it by hand.
# thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended.
# now apply on the url.

# Answer: ocr
