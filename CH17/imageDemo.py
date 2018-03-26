from PIL import Image

img = Image.open('demo.jpg')
width, height = img.size
name = img.filename

startX = 256
startY = 256
cropImg = img.crop((startX, startY, width/4 + startX, height/4 + startY))

newImg = Image.new('RGBA', (512, 512), 'white')
newImg.paste(cropImg, (0, 0))
newImg.paste(cropImg, (256, 256))
newImg.save('output.png')

newWidth, newHeight = newImg.size
for x in range(newWidth):
    for y in range(newHeight):
        color = newImg.getpixel((x, y))
        newImg.putpixel((x, y), (color[0], color[1], color[2], int(color[3]/3)))
newImg.save('output.png')
