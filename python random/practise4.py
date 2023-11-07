import os

# Define a list of common image file signatures
image_signatures = [
    (b'\xFF\xD8\xFF', 'JPEG'),   # JPEG
    (b'GIF87a', 'GIF'),          # GIF 87a
    (b'GIF89a', 'GIF'),          # GIF 89a
    (b'\x89PNG\r\n\x1A\n', 'PNG')  # PNG
    # Add more image signatures here
]

# Specify the folder containing the files to be processed
folder_path = r'C:\Users\tutka\OneDrive\Desktop\New folder'

# Process the files in the specified folder
file_list = os.listdir(folder_path)

for filename in file_list:
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'rb') as file:
        header = file.read(8)  # Read the first 8 bytes

    for signature, file_type in image_signatures:
        if header.startswith(signature):
            print(f"File: {filename}, Type: {file_type}")
            break
    else:
        print(f"File: {filename}, Type: Unknown")