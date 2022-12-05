
s = b'r\xc3\xa9sum\xc3\xa9'
s_decode = str(s.decode('latin-1'))
print(f'Закодированное значение: {s} в декодированном виде: {s_decode}')
s_encode = s_decode.encode('utf8')
print(f'Декодированное значение: {s_decode} в закодированном формате utf-8: {s_encode}')
s_decode2 = s_encode.decode('utf16')
print(f'Закодированное значение: {s_encode} в декодированном формате utf-16: {s_decode2}')
