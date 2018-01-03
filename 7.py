import urllib.request
import os
import math
from PIL import Image


def download_image():
    if not os.path.exists('tmp/7'):
        os.makedirs('tmp/7')
    img_path = 'tmp/7/oxygen.png'
    if not os.path.exists(img_path):
        urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png', img_path)
    return Image.open(img_path)


image = download_image()
center_y = math.floor(image.height / 2)

uniq_vals = []
for i in range(image.width)[::7]:
    pixel = image.getpixel((i, center_y))
    if pixel[0] == pixel[1] == pixel[2]:
        uniq_vals.append(pixel[0])

ascii_map = ''.join(map(chr, uniq_vals))
print(ascii_map)  # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

answer = ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
print(answer)

# Answer: integrity
