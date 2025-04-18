# Import the library to handle the images
from PIL import Image

# Open both images
flag_image = Image.open("flag.png").convert("RGB")
lemur_image = Image.open("lemur.png").convert("RGB")

# Temp new image to hold the result
result = Image.new("RGB", flag_image.size)

# XOR each pixel
for x in range(flag_image.width):
    for y in range(flag_image.height):
        r1, g1, b1 = flag_image.getpixel((x, y))
        r2, g2, b2 = lemur_image.getpixel((x, y))
        xor_pixel = (r1 ^ r2, g1 ^ g2, b1 ^ b2)
        result.putpixel((x, y), xor_pixel)

# Save the new XOR'ed image
result.save("xored_file.png")
