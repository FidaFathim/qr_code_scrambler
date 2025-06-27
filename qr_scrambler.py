import qrcode
import random

def scramble_qr_code(data):
    # Convert data string to list of characters
    characters = list(data)

    # Shuffle the characters randomly
    random.shuffle(characters)

    # Join the characters back into a string
    scrambled_data = ''.join(characters)
    return scrambled_data

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    qr_code_img.save(f"{filename}.png")
    qr_code_img.show()

if __name__ == "__main__":
    input_data = input("Enter data to scramble: ")
    
    # Scramble the data
    scrambled = scramble_qr_code(input_data)
    
    print("Scrambled Data:", scrambled)
    
    # Generate original and scrambled QR codes
    generate_qr_code(input_data, "original_qr")
    generate_qr_code(scrambled, "scrambled_qr")
