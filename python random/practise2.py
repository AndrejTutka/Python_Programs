
file_path = r'C:\Users\tutka\Downloads\marcel rizz.jpg'
byte_value = int(input("Enter the byte value (0-255): "))

if 0 < byte_value < 250:
    with open(file_path, 'rb') as file:
            count = file.read().count(bytes([byte_value]))
            print(f"Byte value {byte_value} occurs {count} times in the file.")
    if FileNotFoundError==True:
            print(f"File not found: {file_path}")
    else:
        pass
