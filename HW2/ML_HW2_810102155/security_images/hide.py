with Image.open("shahid_soleimani.jpeg") as img:
    width, height = img.size
    print(f'width , height : {width , height}')

    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0 , 3):
                if(index < limit):
                    # print(b_message[index])
                    before = bin(pixel[n])

                    # if index == 0:
                    #     print(pixel[n])

                    pixel[n] = ( (pixel[n] & ~1) | int(b_message[index]) )
                    # print(pixel[n])


                    after = bin(pixel[n])

                    index = index + 1

            img.putpixel((x,y), tuple(pixel))
    img.save("steganoGraphed.jpeg")
