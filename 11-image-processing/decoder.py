"""
Command-line tool to extract a secret message from an image.

This script reads an image file, verifies it contains a message encoded
by the companion `encoder.py` script (by checking a magic number), and then
extracts the message hidden in the pixel data using LSB steganography.
"""

import argparse
from PIL import Image

# The same magic number used by the encoder to verify the file.
MAGIC_NUMBER = (11, 22, 33)


def decode(image_path):
    """
    Extracts a secret message from an image by reading metadata and pixel data.
    """
    try:
        img = Image.open(image_path).convert('RGB')
    except FileNotFoundError:
        print(f"❌ Error: The file '{image_path}' was not found.")
        return

    # --- Read and Verify Metadata ---
    # 1. Check for the magic number to ensure it's our encoded file.
    if img.getpixel((0, 0)) != MAGIC_NUMBER:
        print("❌ Error: This image does not contain a message hidden by this tool.")
        return

    # 2. Get the message length from the metadata pixel.
    len_r, len_g, len_b = img.getpixel((1, 0))
    message_len = (len_r << 16) + (len_g << 8) + len_b

    # --- Extract Message ---
    message_bytes = bytearray()
    char_index = 0
    for y in range(1, img.height):
        for x in range(img.width):
            if char_index < message_len:
                r, _, _ = img.getpixel((x, y))
                message_bytes.append(r)
                char_index += 1
            else:
                break
        if char_index >= message_len:
            break

    try:
        # Decode the bytes and remove the null terminator.
        message = message_bytes.decode('utf-8').rstrip('\0')
        print(f"🤫 Hidden Message: {message}")
    except UnicodeDecodeError:
        print("❌ Error: Could not decode the message from the image.")


def main():
    """Parses command-line arguments and calls the decode function."""
    parser = argparse.ArgumentParser(
        description="Extract a secret message from an image.")
    parser.add_argument(
        "-i", "--image", help="Path to the encoded image", required=True)
    args = parser.parse_args()

    decode(args.image)


if __name__ == "__main__":
    main()
