from PIL import Image, ImageDraw, ImageFont

font_size = 8
text = "情人节快乐呀"
img_path = "E:\Pictures\Eric_Wangyz\wym4.jpg"

img_raw = Image.open(img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('C:/Windows/fonts/STHUPO.TTF', font_size)

def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

# img_new.convert('RGB').save("F://save3.jpeg",quality=200)
img_new.convert('RGB').show()
# img_new.show()
img_new.save("F://save4.jpeg",quality=200)
