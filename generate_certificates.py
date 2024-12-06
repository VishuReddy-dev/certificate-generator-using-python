# from PIL import Image, ImageDraw, ImageFont
# import pandas as pd

# # Load the Excel sheet
# data = pd.read_excel('cer.xlsx', engine='openpyxl')  # Replace with your Excel file name

# # Load the certificate template
# template_path = 'Cert Template 6.png'  # Replace with your template file
# font_path = 'arial.ttf'  # Replace with the font file you want to use
# output_folder = 'certificates/'  # Output folder for certificates

# # Ensure output folder exists
# import os
# os.makedirs(output_folder, exist_ok=True)

# # Configure text position and font size
# name_position = (129,115)  # Adjust as per your template
# font_size = 18

# # Load font
# font = ImageFont.truetype(font_path, font_size)

# # Iterate through each attendee and generate certificate
# for index, row in data.iterrows():
#     name = str(row['name'])  # Convert name to string
#     if not isinstance(name, str) or name.strip() == '':
#         print(f"Skipping row with invalid name: {row}")
#         continue

#     # Open the template
#     img = Image.open(template_path)
#     draw = ImageDraw.Draw(img)

#     # Add name to the certificate
#     draw.text(name_position, name, font=font, fill="black")  # Adjust fill color as needed

#     # Save the certificate
#     output_path = os.path.join(output_folder, f"{name}_certificate.png")
#     img.save(output_path)

#     print(f"Certificate generated for: {name}")

# print("All certificates have been generated!")

import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


font_path = "arial.ttf" 
template_path = "cer.png"  
output_folder = "certificates"  


os.makedirs(output_folder, exist_ok=True)


data = pd.read_excel('cer.xlsx')

def fit_text(draw, text, font_path, max_width, initial_font_size):
    font_size = initial_font_size
    font = ImageFont.truetype(font_path, font_size)
    
    while draw.textsize(text, font=font)[0] > max_width:
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
    
    return font


def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    line = ""
    
    for word in words:
        test_line = f"{line} {word}".strip()
        if draw.textsize(test_line, font=font)[0] <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)
    
    return lines

def limit_name_to_two_words(name):
    words = name.split()
    return " ".join(words[:2])


max_width = 600  
initial_font_size = 18  
name_position = (125, 115)  
line_height = 60  

for index, row in data.iterrows():
    name = str(row['name'])  
    if not name.strip():  
        print(f"Skipping row with invalid name: {row}")
        continue
    
    name = limit_name_to_two_words(name)
    
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    font = fit_text(draw, name, font_path, max_width, initial_font_size)

    lines = wrap_text(name, font, max_width)

    y_offset = name_position[1]
    for line in lines:
        draw.text((name_position[0], y_offset), line, font=font, fill="black")
        y_offset += font.getsize(line)[1]  # Move down by the line height
    
    output_path = os.path.join(output_folder, f"{name}_certificate.png")
    img.save(output_path)
    
    print(f"Certificate generated for: {name}")
