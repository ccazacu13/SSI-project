
import hashlib

letter_list = ['C','R','I','S','T','I','A','N']

def calculate_sha256(data):
# Convert data to bytes if it’s not already
    if isinstance(data, str):
        data = data.encode()

# Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(data).hexdigest()

    return sha256_hash

hex_list = []
for letter in letter_list:
    hex_list.append(calculate_sha256(letter))

print(hex_list)

baseline_width = 3
baseline_height = 3
counter = 1

g = open("headers.txt",'a')
for hex_letter in hex_list:
    ppm_header = f'P6 {baseline_width} {baseline_height} 255\n'
    g.write(calculate_sha256(ppm_header[:-1]) + "\n")

    with open(f'Letter_{counter}.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        f.write(bytes.fromhex(hex_letter))
    counter += 1

#un caracter in sha 256 este cryptat in 64 de caractere hexa => 32 de bytes
#pt formatul ppm P6 3 bytes sunt folositi sa reprezinte un pixel, deci pot reprezenta aprox. 9 pixeli, de accea imaginile sunt de 3 pe 3

