'''
from PIL import Image
import coolcolours

image_green = Image.open("kid-green.jpg").load
image_beach = Image.open("beach.jpg").load

image_output = Image.open("kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        r = image_green[i,j][0]
        g = image_green[i,j][1]
        b = image_green[i,j][2]

        if coolcolours.is_green(r,g,b):
            beach_colour = image_beach[i,j] # get beach color at same spot
            image_output.putpixel((i,j), beach_colour)  # set the output pixel

# save the resulting image in C
image_output.save("output.png", "png")
'''
'''
from PIL import Image

file = Image.open("jelly_beans.jpg")
jbimg = file.load()

width = file.width
height = file.height

yellow_pixels = 0

for i in range(width):
    for j in range(height):

        #if the pixel is yellow ~(255,255,0), add it to a list or counter
        r = jbimg[i,j][0]
        g = jbimg[i,j][1]
        b = jbimg[i,j][2]

        if r > 150 and g > 150 and b < 100:
            yellow_pixels += 1

# calculate the percentage of yellow pixels 
# over the total number of pixels in the image
print(yellow_pixels)
print(width*height)

# output the report
percent_yellow = 100*yellow_pixels/(width*height)

report = "There are {:.2f} percent yellow jellybeans."
'''

from PIL import Image 
file = Image.open("5.1/jelly_beans.jpg")
jbimg = file.load()

width = file.width
height = file.height

for x in range(width):
    for y in range(height):

        #if the pixel is yellow ~(255,255,0), add it to a list or counter
        r = jbimg[x,y][0]
        g = jbimg[x,y][1]
        b = jbimg[x,y][2]

        if r > 150 and g > 150 and b < 100:
            file.putpixel((x, y), (255,255,255))

file.save("ouput.png", "png")