from PIL import Image

def encrypt_decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # XOR operation
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_image)
    print(f"Operation completed! Saved as {output_image}")

print("Image Encryption / Decryption Tool")
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = int(input("Enter your choice (1 or 2): "))
key = int(input("Enter secret key (0-255): "))

if choice == 1:
    encrypt_decrypt_image("eg.jpg", "encrypted.jpg", key)
elif choice == 2:
    encrypt_decrypt_image("encrypted.jpg", "decrypted.jpg", key)
else:
    print("Invalid choice")
