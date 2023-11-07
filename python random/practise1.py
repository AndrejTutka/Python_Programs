file_path = r'C:\Users\tutka\Downloads\marcel rizz.jpg'


with open(f'{file_path}', 'rb') as file:
    while True:
        data = file.read(16)
        if not data:
            break

        hex_data = ' '.join(f'{byte:02X}' for byte in data)
        text_data = ''.join(chr(byte) if 32 <= byte < 127 else '.' for byte in data)

        print(f'{hex_data}  {text_data}')