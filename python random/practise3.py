
file_path = r'C:\Users\tutka\Downloads\marcel rizz.jpg'  

with open(file_path, 'rb') as file:
    data = file.read()

    if len(data) < 10:
        print("File does not contain enough bytes.")
    else:
        first_10_bytes = data[0:10]
        last_10_bytes = data[-10:]
        middle_10_bytes = data[max(0, len(data) // 2 - 5):len(data) // 2 + 5]

        print(f"First 10 bytes: {first_10_bytes}")
        print(f"Last 10 bytes: {last_10_bytes}")
        print(f"10 bytes around the middle: {middle_10_bytes}")


