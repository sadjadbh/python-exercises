# Python Steganography Tool 🖼️

This project provides a pair of command-line tools to hide a secret text message within an image (`encoder.py`) and to extract that hidden message (`decoder.py`).

It uses a simple Least Significant Bit (LSB) steganography technique on the red channel of pixels.

---

### Features

* **Command-Line Interface:** Easy to use with arguments for input/output files and messages.
* **Metadata Embedding:** The encoded image is self-contained. It includes:
    * A **Magic Number**: A unique signature to identify files encoded by this program.
    * **Message Length**: The decoder knows exactly how many characters to read.
* **Error Handling:** Provides clear error messages for missing files or messages that are too long.
* **Portable:** No hardcoded paths—run it on any system with your own files.

---

### File Structure

* `encoder.py`: The script to hide a message in an image.
* `decoder.py`: The script to extract a message from an encoded image.
* `README.md`: This file.

---

### How to Use

You'll need the `Pillow` library, which you can install if you haven't already:
```bash
pip install Pillow
```

**1. To Hide a Message**
Use the `encoder.py` script. You must provide the original image, the message, and a name for the output file.

Syntax:
```bash
python encoder.py --image <input_image_path> --message "<your_secret_message>" --output <output_image_path>
```
Example:
```bash
python encoder.py --image landscape.jpg --message "Meet at midnight" --output secret_image.png
```
|   ✅ Message successfully hidden in 'secret_image.png'


**2. To Extract a Message**
Use the `decoder.py` script. You only need to provide the image that contains the secret.

Syntax:
```bash
python decoder.py --image <encoded_image_path>
```

Example:
```bash
python decoder.py --image secret_image.png
```
|   🤫 Hidden Message: Meet at midnight