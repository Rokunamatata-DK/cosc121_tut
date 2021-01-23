# def first_half(s):
#     """asd"""
#     if len(s) % 2 == 0:
#         return s[0:int(len(s) / 2)]
#     else:
#         return s[0:int((len(s) - 1) / 2)]

# print(first_half('WooHoo'))


def make_out_word(out, word):
    """asd"""
    return out[:int(len(out) / 2)] + word + out[int(len(out) / 2):]

print(make_out_word('<<>>', 'Yay'))


