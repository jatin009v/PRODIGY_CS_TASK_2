import cv2
import numpy as np
import os

# Set the path to the image file
image_path = os.path.join('PORDIGY_CS_TASK2', 'img.png')

def encrypt_image(image_path, key):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to read image file {image_path}")
            return None

        # Convert the image to RGB color space
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Perform pixel manipulation based on the key
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(3):
                    image[i, j, k] = (image[i, j, k] + key) % 256

        return image
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def decrypt_image(encrypted_image, key):
    try:
        # Reverse the pixel manipulation
        for i in range(encrypted_image.shape[0]):
            for j in range(encrypted_image.shape[1]):
                for k in range(3):
                    encrypted_image[i, j, k] = (encrypted_image[i, j, k] - key) % 256

        return encrypted_image
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Set the encryption key
key = 10

# Encrypt the image
encrypted_image = encrypt_image(image_path, key)
if encrypted_image is None:
    print("Error: Unable to encrypt image")
else:
    # Save the encrypted image
    encrypted_image_path = os.path.join('PORDIGY_CS_TASK2', 'encrypted_img.png')
    cv2.imwrite(encrypted_image_path, cv2.cvtColor(encrypted_image, cv2.COLOR_RGB2BGR))

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    if decrypted_image is None:
        print("Error: Unable to decrypt image")
    else:
        # Save the decrypted image
        decrypted_image_path = os.path.join('PORDIGY_CS_TASK2', 'decrypted_img.png')
        cv2.imwrite(decrypted_image_path, cv2.cvtColor(decrypted_image, cv2.COLOR_RGB2BGR))

        print("Image encrypted and decrypted successfully!")