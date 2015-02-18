# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import cairocffi as cairo
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 300, 200)
surface = cairo.PDFSurface(f, 
context = cairo.Context(surface)
with context:
    context.set_source_rgb(1, 1, 1)  # White
    context.paint()
# Restore the default source which is black.
context.move_to(90, 140)
context.rotate(-0.5)
context.set_font_size(20)
context.show_text(u'Hi from cairo!')
surface.write_to_png('example.png')

# <codecell>

cut_lines = [
((3, 0), (9, 0)),
((9.5, -1), (15.5, -1)),
((9, -0.5), (9, 0)),
((16, -0.5), (16, 0)),
((11.5, 0), (13.5, 0)),
((16, 0), (18.5, 0)),
((18, 1), (19.5, 1)),
((18, 4), (19.5, 4)),
((19, 2), (19, 3)),
((3, 4), (8, 4)),
((8, 4), (8, 5)),
((3, 5), (8, 5)),
((17, 6), (18.5, 6)),
((17, 7), (18.5, 7)),
((11.5, 7), (11.5, 8.5)),
((13.5, 7), (13.5, 8.5)),
((9, 8), (11.5, 8)),
((13.5, 8), (16, 8)),
((3, 9), (8, 9)),
((6.5, 12), (7.5, 12)),
((6, 12.6), (6, 16)),
((6.5, 13), (7.5, 13)),
((8, 12), (11, 12)),
((8, 13), (11, 13)),
((8, 17), (18, 17)),
((8, 18), (8.5, 18)),
((3, -0.5), (3, 19.1)),
((-1, -0.5), (3, -0.5)),
((-1, 21.9), (3, 21.9)),
((3, 21.9), (3, 26)),
((6.5, 18.5), (6.5, 20)),
((7.5, 18.5), (7.5, 20)),
((8, 16), (8, 17)),
((8,17), (18, 17)),
((18, 5), (18, 6)),
((18, 6), (18, 17)),
((3, 26), (6.5, 26)),
((8, 18), (8, 20)),
((8, 21), (8, 26)),
((6.5, 26), (6.5, 26.5)),
((7.5, 26), (7.5, 26.5)),
((7.5, 26), (8, 26))
]


cut_curves =[
((9.5, -0.5), (0.5, 1), 0.5),
((15.5, -0.5), (1, 1.5), 0.5),
((18.5, 0.5), (1, 2), 0.5),
((19.5, 1.5), (1, 1.5), 0.5),
((19.5, 3.5), (1.5, 2), 0.5),
((18.5, 4.5), (1, 2), 0.5),
((18.5, 6.5), (1, 2), 0.5),
((12, 8,5), (0, 0.5), 0.5),
((13, 8.5), (1.5, 2), 0.5),
((8, 12), (1, 1.5), 3),
((8, 13), (1.5, 2), 3),
((8.5, 17.5), (1, 2), 0.5),
((8.5, 20.5), (1, 2), 0.5),
((7, 26.5), (1.5, 0.5), 0.5),
((7, 18.5), (0.5, 1.5), 0.5),
]

mountain_lines = [
((9, 0), (11.5, 0)),
((13.5, 0), (16, 0)),
((18, 0), (18, 5)),
((19, 1), (19, 4)),
((8, 4), (18, 4)),
((8, 5), (18, 5)),
((18, 6), (18, 7)),
((3, 8), (9, 8)),
((16, 8), (18, 8)),
((8, 9), (18, 9)),
((11, 12), (18, 12)),
((11, 13), (18, 13)),
((8, 16), (18, 16)),
((3, 19), (8, 19)),
((3, 23), (8, 22)),
]

# <codecell>

from PIL import Image
from PIL.ImageDraw import Draw
img = Image.new("RGBA", (100, 100))
draw = Draw(img)
draw.rectangle(((0,0), (100, 100)), fill=(255, 100, 0))
draw.rectangle((50,80,100,200), fill=0)
# img.save("foo.png")
imshow(numpy.asarray(img))

# <codecell>

given_image_size = (600, 900)
image_min_dimen = min(given_image_size)
image_center = (given_image_size[0] / 2, given_image_size[1] / 2)

from PIL import Image
from PIL.ImageDraw import Draw
from math import sin, cos, radians
import random
img = Image.new("RGBA", given_image_size)
draw = Draw(img)
span = 3600
for i in range(0, span):
    deg = float(i) / span * 360
    draw.line((image_center[0], image_center[1], image_center[0] + sin(radians(deg)) * image_min_dimen * 0.4 , image_center[1] + cos(radians(deg)) * image_min_dimen * 0.4), fill=(0, 0, 0), width=2)
imshow(numpy.asarray(img))

# <codecell>


