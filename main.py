# This program will read the pixels one by one an separate the grey ones from the others
# Then based off a scale created by measuring the pixels between the cm scale we can convert pixels to cm
from PIL import Image

#
# SETTING UP THE IMAGE
#

filename = 'data.jpg'

# Load the original image, and get its size and color mode.
image = Image.open(filename)
width, height = image.size
mode = image.mode

# Show information about the original image.
print(f"Original image: {filename}")
print(f"Size: {width} x {height} pixels")
image = image.convert('RGB')

#
# DONE SETTING UP THE IMAGE
#


# Going through the image pixel by pixel and counting the different colors (white, grey, and other)

# Unadjusted
grey_count = 0
white_count = 0
other_count = 0

for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))

        if (r == g == b == 157):
            grey_count += 1
        elif (r == g == b == 255):
            white_count += 1
        else:
            other_count += 1

        # Adjusted
adjusted_grey_count = 0
adjusted_other_count = 0
for i in range(width):
    for j in range(height):
        r, g, b = image.getpixel((i, j))

        if (r <= g <= b <= 163):
            adjusted_grey_count += 1
        else:
            adjusted_other_count += 1

cm_area = 36  # 6*6 is the total area of the chart

# Calculating the unadgjusted results
unadjusted_percent_grey = (grey_count / (grey_count + white_count + other_count))

unadjusted_grey_cm_area = round(36 * unadjusted_percent_grey, 3)

# Calculating the adjusted results


adjusted_percent_grey = (grey_count + (.5 * other_count)) / (grey_count + white_count + other_count)

adjusted_grey_cm_area = round(36 * adjusted_percent_grey, 3)

# Printing out the unadjusted results
print("\nUnadjusted stats")
print("Total pixels:", grey_count + white_count + other_count)
print("Grey pixels:", grey_count)
print("White pixels:", white_count)
print("Other pixels:", other_count)

print(f"percent grey {round(unadjusted_percent_grey * 100, 2)} %")

print("Grey area:", unadjusted_grey_cm_area, "cm^2")

# Printing out the ajusted results
print("\nAdjusted stats")
print("Total pixels:", adjusted_grey_count + adjusted_other_count)
print("Adjusted grey pixels:", adjusted_grey_count)
print("Adjusted other pixels:", adjusted_other_count)

print(f"percent grey {round(adjusted_percent_grey * 100, 2)} %")

print("Grey area:", adjusted_grey_cm_area, "cm^2")


# Making a new image that represents the unadjusted grey area
unadjusted = Image.new('RGB', (width, height))
adjusted = Image.new('RGB', (width, height))

for a in range(width):
    for b in range(height):
        if (grey_count > 0):
            unadjusted.putpixel((a, b), (157, 157, 157))
            grey_count -= 1
        else:
            unadjusted.putpixel((a, b), (255, 255, 255))
        if (adjusted_grey_count > 0):
            adjusted.putpixel((a, b), (157, 157, 157))
            adjusted_grey_count -= 1
        else:
            adjusted.putpixel((a, b), (255, 255, 255))

unadjusted.save('unadjusted.jpg')
adjusted.save('adjusted.jpg')