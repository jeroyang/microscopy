# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

dpcm = 37.8
zero_x = -2.3
zero_y = -1.4

# <codecell>

def col(locs):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm))

# <codecell>

point = (24.2, 5.9)
print col(point)

# <codecell>

point = (9.5, 6.5)
print col(point)

# <codecell>

2.0* dpcm

# <codecell>

locs = [(17.1, 4.1),
        (17.9, 4.1),
        (17.1, 4.9),
        (17.9, 4.9),
        (17.5, 4.5),
        (24.5, 7.5),
        (14.1, 4.5)]
for loc in locs:
    print col(loc)

# <codecell>

def col2(locs2):
    return col([locs2[0], locs2[1]]), col([locs2[2], locs2[3]])

pattern = '<path d = "M{} {} L{} {}" />'

lines = [(10.9, 0.5, 11.7, 0.5), 
 (10.9, 0.5, 10.9, 1.9), 
 (10.9, 1.9, 11.7, 1.9), 
 (11.7, 0.5, 11.7, 1.9),
 (24.1, 6.0, 24.1, 8.2),
 (24.1, 6.5, 24.1, 8.7),
 (23.1, 8.0, 23.1, 9.0),
 (23.0, 8.0, 23.0, 9.0),
 (23.1, 9.0, 25.9, 9.0),
 (23.1, 8.0, 23.6, 8.0),
 (23.0, 8.5, 25.9, 8.5),
 (24.4, 7.5, 24.6, 7.5),
 (13.7, 4.1, 14.5, 4.1),
 (24.3, 5.3, 24.7, 5.3),
 (24.3, 5.7, 24.7, 5.7),
 (24.3, 5.9, 24.3, 6.3),
 (24.7, 5.9, 24.7, 6.3)]

for line in lines:
    locs = col2(line)
    print pattern.format(locs[0][0], locs[0][1], locs[1][0], locs[1][1])

# <codecell>

base = """
<!DOCTYPE html>
<html>
<body>

<svg height="794" width="1123">

<g fill="none" stroke="black" stroke-width="2">
{}
</g>
  Sorry, your browser does not support inline SVG.
</svg>

</body>
</html>
"""

# <codecell>

from itertools import product
rec_pattern =  '<rect x="{}" y="{}" width="150" height="150" />'
rec_svg = []
for i in product(range(0, 1050, 150), range(0, 750, 200)):
    rec_svg.append(rec_pattern.format(i[0], i[1]))
print base.format("\n".join(rec_svg))

# <codecell>

print 1123/150 * 150

# <codecell>


