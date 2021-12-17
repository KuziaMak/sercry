enc1_str = 'разработка'
enc2_str = 'администрирование'
enc3_str = 'protocol'
enc4_str = 'standard'

print(enc1_str)
print(type(enc1_str))
print(enc2_str)
print(type(enc2_str))
print(enc3_str)
print(type(enc3_str))
print(enc4_str)
print(type(enc4_str))

enc1_str_bytes = enc1_str.encode('utf-8')
enc2_str_bytes = enc2_str.encode('utf-8')
enc3_str_bytes = enc3_str.encode('utf-8')
enc4_str_bytes = enc4_str.encode('utf-8')
print(enc1_str_bytes)
print(type(enc1_str_bytes))
print(enc2_str_bytes)
print(type(enc2_str_bytes))
print(enc3_str_bytes)
print(type(enc3_str_bytes))
print(enc4_str_bytes)
print(type(enc4_str_bytes))
dec1_str = enc1_str_bytes.decode('utf-8')
dec2_str = enc2_str_bytes.decode('utf-8')
dec3_str = enc3_str_bytes.decode('utf-8')
dec4_str = enc4_str_bytes.decode('utf-8')

print(dec1_str)
print(type(dec1_str))
print(dec2_str)
print(type(dec2_str))
print(dec3_str)
print(type(dec3_str))
print(dec4_str)
print(type(dec4_str))