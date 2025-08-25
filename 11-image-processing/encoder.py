"""
Command-line tool to hide a secret message within an image file.

This script uses a Least Significant Bit (LSB) steganography technique to
embed a user-provided message into the pixels of an image. It also embeds
metadata (a magic number and the message length) to allow the companion
`decoder.py` script to easily extract the message.
"""

import argparse
from PIL import Image

# A unique pixel value to identify our encoded images.
MAGIC_NUMBER = (11, 22, 33)


def encode(image_path, message, output_path):
    """
    Hides a secret message within an image by modifying the red channel of pixels.
    It embeds metadata (magic number, message length) in the first few pixels.
    """
    try:
        img = Image.open(image_path).convert('RGB')
    except FileNotFoundError:
        print(f"❌ Error: The file '{image_path}' was not found.")
        return

    # Add a null character as an end-of-message marker for extra robustness.
    message += "\0"
    message_bytes = message.encode('utf-8')
    message_len = len(message_bytes)

    # Check if the image is large enough to hold the metadata and message.
    # Reserve first row for metadata
    if message_len > img.width * (img.height - 1):
        print("❌ Error: Message is too long for this image.")
        return

    # --- Embed Metadata ---
    # 1. Place the magic number to identify our file
    img.putpixel((0, 0), MAGIC_NUMBER)

    # 2. Store the message length in the next pixels.
    # We can store 255*255*255 = 16,581,375, which is more than enough.
    len_r = (message_len >> 16) & 0xFF
    len_g = (message_len >> 8) & 0xFF
    len_b = message_len & 0xFF
    img.putpixel((1, 0), (len_r, len_g, len_b))

    # --- Embed Message ---
    char_index = 0
    for y in range(1, img.height):
        for x in range(img.width):
            if char_index < message_len:
                r, g, b = img.getpixel((x, y))
                r = message_bytes[char_index]
                new_pixel = (r, g, b)
                img.putpixel((x, y), new_pixel)
                char_index += 1
            else:
                break
        if char_index >= message_len:
            break

    img.save(output_path)
    print(f"✅ Message successfully hidden in '{output_path}'")


def main():
    """Parses command-line arguments and calls the encode function."""
    parser = argparse.ArgumentParser(
        description="Hide a secret message in an image.")
    parser.add_argument(
        "-i", "--image", help="Input image path", required=True)
    parser.add_argument("-m", "--message",
                        help="The secret message to hide", required=True)
    parser.add_argument(
        "-o", "--output", help="Output path for the encoded image", required=True)
    args = parser.parse_args()

    encode(args.image, args.message, args.output)


if __name__ == '__main__':
    main()
