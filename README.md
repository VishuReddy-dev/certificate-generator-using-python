# Automated Certificate Generator

This project automates the generation of personalized certificates using Python. It reads recipient names from an Excel file, dynamically adjusts text size and formatting, and outputs certificates as image files.

## Features

- **Dynamic Font Adjustment**: Ensures names fit perfectly within the designated area on the certificate.
- **Text Wrapping**: Handles long names by splitting them into multiple lines.
- **Customizable**: Supports the use of different templates, fonts, and configurations.
- **Batch Processing**: Generates certificates for multiple recipients at once.

## Requirements

- Python 3.x
- Libraries:
  - `Pillow`
  - `pandas`
  - `openpyxl` (for reading `.xlsx` files)

Install the dependencies using:
```bash
pip install Pillow pandas openpyxl
```
# Folder Structure
```
.
├── cer.xlsx              # Input Excel file with names
├── cer.png               # Certificate template image
├── certificates/         # Folder where certificates will be saved
├── certificate_generator.py  # Main script
```
# Usage
1.Prepare the Input Data:

- Create an Excel file named cer.xlsx with a column titled name containing the recipients' names.
2.Provide a Template:

- Use an image file named cer.png as the certificate template. Customize it to include placeholders for text positions.
3.Run the Script:

- Execute the script:
  ```
  python certificate_generator.py
  ```
  Certificates will be saved in the certificates folder.
4.Customization:
  - Font: Change the font_path variable to specify a different font file.
  - Positioning: Adjust the name_position variable to modify text placement on the certificate.
  - Maximum Width: Update the max_width variable to control text wrapping.
# Code Highlights
## Dynamic Font Sizing
Ensures names fit within the specified area:
```
def fit_text(draw, text, font_path, max_width, initial_font_size):
    font_size = initial_font_size
    font = ImageFont.truetype(font_path, font_size)
    
    while draw.textsize(text, font=font)[0] > max_width:
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
    
    return font

```
## Limiting Name to Two Words
Restricts names to two words for simplicity:
```
def limit_name_to_two_words(name):
    words = name.split()
    return " ".join(words[:2])

```
# Output
Certificates are saved in the certificates/ folder with filenames formatted as <Recipient Name>_certificate.png.

