#show and crop image
'''
from PIL import Image

img = Image.open("my_bros.jpg")

print(img.size)
print(img.format)

area = ( 100, 400, 1650, 3250)
cropped_image = img.crop(area)

#img.show()
cropped_image.show()
'''

# overlay an image with a cropped/uncropped version of another image(with a specific area)
'''
from PIL import Image

bros = Image.open("my_bros.jpg")
girl = Image.open("portGirl.png")
# i have to do some quick maths here to get the value of where i am to paste my image
area = (20, 20, 2000, 3000)

bros.paste(girl, area)

bros.show()

'''

# to spilt the red, green and blue mode of a pics(R,G,B)
# to print out the r,g,b of an image in different order
'''
from PIL import Image

bros = Image.open("my_bros.jpg")

#print(bros.mode)
r, g , b = bros.split()

#r.show()
#g.show()
#b.show()
new_image = Image.merge("RGB", (r, b, g))

new_image.show()
'''

#to combine the r,g,b of one image with another
'''

from PIL import Image

anime = Image.open("anime.png")
portGirl = Image.open("portGirl.png")
r1, g1 , b1 = anime.split()
r2, g2 , b2 = portGirl.split()
new_image = Image.merge("RGB", (r1, b2, g1))

new_image.show()
'''
#print(anime.mode)
#print(portGirl.mode)


#to resize an image
#to flip an image(side or up-down)
#to spin am image


from PIL import Image

anime = Image.open("anime.png")
square_hackSwag = anime.resize((250,250))
flip_hackSwag = anime.transpose(Image.FLIP_LEFT_RIGHT)
spin_hackSwag = anime.transpose(Image.ROTATE_90)
upside_hackSwag = anime.transpose(Image.FLIP_TOP_BOTTOM)

anime.show()
square_hackSwag.show()
flip_hackSwag.show()
spin_hackSwag.show()
upside_hackSwag.show()



# converting image mode i.e(from RGB to CMYK or others like black and white)
"""
from PIL import Image

meten = Image.open("meten.jpg")
black_me = meten.convert("L")

black_me.show()


# image filtters
from PIL import Image
from PIL import ImageFilter

anime = Image.open("anime.png")
blur = anime.filter(ImageFilter.BLUR)
detail = anime.filter(ImageFilter.DETAIL)
edges = anime.filter(ImageFilter.FIND_EDGES)


anime.show()
blur.show()
detail.show()
edges.show()


"""






 

