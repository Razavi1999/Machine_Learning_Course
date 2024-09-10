with Image.open("steganoGraphed.jpeg") as img2 :
  width , height = img2.size

  for x in range(0 , width):
    for y in range(0 , height):
        pixel2 = list(img2.getpixel((x, y)))

        for n in range(0 , 3):
            # if x < limit:
              data2 += str(pixel2[n] & 1)
              # x = x + 1
              # print(pixel[n] - pixel2[n])


for i in range(0 , len(data2) , 8):
  if tmp[-5 : ] == 'Tamam':
    print('Breaked Breaked')
    break

  letter = data2[i : i + 8]

  # print(f'word : {chr(int(str(letter), 2))}')
  tmp += chr(int(str(letter), 2))

print(f'tmp : {tmp[0 : len(tmp) - 5]}')
