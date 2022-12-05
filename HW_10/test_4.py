"""4* Реализовать кодирование и декодирование ключевых слов для латинского алфавита согласно указанному соответствию (маппингу). 
Шифр (используйте данное соответствие букв при решении задания)
* A B C D E F G H I  J  K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H  I  J  K L M N Q S U V W X Z
Пример:
cipher = Cipher()
cipher.encode("Hello world")
"Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
"Kojima is genius" """


encode_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
decode_letters = 'CRYPTOABDEFGHIJKLMNQSUVWXZ'
encode_letters += encode_letters.lower()
decode_letters += decode_letters.lower()
encode_str = dict(zip(encode_letters, decode_letters))
decode_str = dict(zip(decode_letters, encode_letters))


class Cipher():
    def encode(self, string):
        cipher_encode = ''
        for i in string:
            if i in encode_str:
                cipher_encode += encode_str[i]
            else:
                cipher_encode += i
        return cipher_encode

    def decode(self, string):
        cipher_decode = ''
        for i in string:
            if i in decode_str:
                cipher_decode += decode_str[i]
            else:
                cipher_decode += i
        return cipher_decode


cipher = Cipher()
print(cipher.encode('Hello world'))
print(cipher.decode('Fjedhc dn atidsn'))

