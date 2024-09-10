from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("sardar2.jpg")

title_font = ImageFont.truetype('Playfair_Display/IranNastaliq.ttf', 100)
title_font2 = ImageFont.truetype('Playfair_Display/PlayfairDisplay-Italic-VariableFont_wght.ttf' , 50)

title_text2 = 'The opportunity that exists \n in crises can not be found \n in the opportunities \n      themselves!!'

image_editable = ImageDraw.Draw(my_image)
image_editable.text((15,15), title_text2, (207,243,199), font=title_font2)

my_image.save("result.jpg")
