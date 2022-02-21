layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
                           'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'),
                  "йцукенгшщзхъфывапролджэячсмитьбю."
                  'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'
                  ))

print("Dctv ghbdtn".translate(layout))
