# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

base = """
<!DOCTYPE html>
<html>
<body>

<svg height="794" width="1123">
<g fill="none" stroke="#91C5EB" stroke-width="1">
{}
</g>
<g fill="none" stroke="#91C5EB" stroke-width="2">
{}
</g>
<g fill="none" stroke="black" stroke-width="2">
{}
{}
{}
{}
{}
{}
</g>
<g fill="none" stroke="black" stroke-width="1" stroke-dasharray="5,5">
{}
</g>
<g fill="none" stroke="black" stroke-width="1" stroke-dasharray="10, 5, 3, 5">
{}
</g>
<g fill="none" stroke="red" stroke-width="1">
<circle cx="86" cy="52" r="1"/>
</g>

  Sorry, your browser does not support inline SVG.
</svg>

</body>
</html>
"""

# <codecell>

v_lines = [
    (15.6, 3.0, 15.6, 5.0),
    (4.3, -1.0, 4.3, 3.0),
    (9.9, -1.0, 9.9, 3.0),
    (12.0, 8.0, 13.0, 8.0),
    (16.0, 3.0, 16.0, 8.0),
    (16.0, 8.0, 18.0, 8.0),
    (12.7, 3.0, 15.5, 3.0),
    ]

cut_lines = [
    (-0.6, 3.0, -0.6, 6.0),
    (-1.6, 6.5, -1.6, 15.5),
    (-1.1, 6.0, -0.6, 6.0),
    (-1.1, 16.0, -0.6, 16.0),
    (-0.6, 11.5, -0.6, 13.5),
    (-0.6, 16.0, -0.6, 17.0),
    (-0.6, 17.0, -0.5, 17.0),
    (-0.5, 17.0, -0.5, 17.5),
    (0.5, 17.0, 0.5, 18.0),
    (0.5, 18.0, 0.6, 18.0),
    (0.6, 18.0, 0.6, 18.5),
    (3.7, 17.0, 3.7, 18.0),
    (3.6, 18.0, 3.6, 18.5),
    (3.6, 18.0, 3.7, 18.0),
    (1.6, 18.0, 2.6, 18.0),
    (3.7, 8.0, 4.8, 8.0),
    (4.8, 3.0, 4.8, 8.0),
    (5.9, 16.0, 5.9, 17.5),
    (6.9, 16.0, 6.9, 17.5),
    (7.0, 11.5, 8.5, 11.5),
    (7.0, 13.5, 8.5, 13.5),
    (8.0, 6.0, 8.0, 11.5),
    (8.0, 13.5, 8.0, 16.0),
    (8.7, 4.0, 9.0, 4.0),
    (8.7, 5.0, 9.0, 5.0),
    (9.0, 3.0, 9.0, 8.0),
    (12.6, 5.0, 16.0, 5.0),
    (13.0, 6.5, 13.0, 7.5),
    (12.0, 8.0, 12.0, 11.0),
    (17.0, 8.8, 17.0, 17.0),
    (-1.3, 3.0, 12.7, 3.0),
    (-1.3, -1.0, 15.5, -1.0),
    (18.5, 6.5, 19.0, 6.5),
    (18.5, 7.5, 19.0, 7.5),
    (20.3, 0.0, 25.9, 0.0),
    (20.3, 0.0, 20.3, 0.7),
    (20.3, 0.7, 20.6, 0.5),
    (20.6, 0.5, 20.6, 1.7),
    (20.3, 1.5, 20.6, 1.7), 
    (20.3, 1.5, 20.3, 2.5),
    (20.3, 2.5, 23.1, 2.5),
    (15.5, -1.0, 15.5, 3.0),
    (-1.3, -1.0, -1.3, 3.0),
    (25.9, -1.0, 25.9, 3.0),
    (25.9, 3.0, 26.0, 3.0),
    (15.5, 3.0, 23.1, 3.0),
    
    (19.0, 8.0, 19.0, 11.0),

    (17.0, 8.8, 17.0, 17.0),
    (4.7, 17.0, 5.9, 17.0),
    (6.9, 17.0, 17.0, 17.0),
    (26.0, 3.0, 26.0, 11.0),
    (23.0, 4.0, 23.0, 5.0),
    (23.1, 2.5, 23.1, 3.0),
    (22.0, 8.0, 23.0, 8.0),
    (1.1, 19.0, 3.1, 19.0),
    (4.7, 17.0, 4.7, 17.5),
    (9.0, 12.0, 9.0, 13.0),
    (13.0, 8.0, 16.0, 8.0),
    (23.6, 2.4, 25.4, 2.4),
    (25.6, 0.7, 25.9, 0.5),
    (25.6, 1.5, 25.9, 1.7),

    (23.6, 2.4, 23.6, 2.6),
    (25.4, 2.4, 25.4, 2.6),

    (21.7, 1.1, 21.7, 1.5), (21.7, 1.1, 21.9, 1.4464101615137757), (21.7, 1.1, 22.046410161513776, 1.3000000000000003), (21.7, 1.1, 22.099999999999998, 1.1), (21.7, 1.1, 22.046410161513776, 0.9000000000000001), (21.7, 1.1, 21.9, 0.7535898384862245), (21.7, 1.1, 21.7, 0.7000000000000001), (21.7, 1.1, 21.5, 0.7535898384862246), (21.7, 1.1, 21.353589838486222, 0.8999999999999999), (21.7, 1.1, 21.3, 1.1), (21.7, 1.1, 21.353589838486222, 1.3), (21.7, 1.1, 21.5, 1.4464101615137754),
    (24.5, 1.1, 24.5, 1.5), (24.5, 1.1, 24.7, 1.4464101615137757), (24.5, 1.1, 24.846410161513777, 1.3000000000000003), (24.5, 1.1, 24.9, 1.1), (24.5, 1.1, 24.846410161513777, 0.9000000000000001), (24.5, 1.1, 24.7, 0.7535898384862245), (24.5, 1.1, 24.5, 0.7000000000000001), (24.5, 1.1, 24.3, 0.7535898384862246), (24.5, 1.1, 24.153589838486226, 0.8999999999999999), (24.5, 1.1, 24.1, 1.1), (24.5, 1.1, 24.153589838486223, 1.3), (24.5, 1.1, 24.3, 1.4464101615137754),
    
    (24.1, 4.1, 24.1, 4.9), (24.1, 4.1, 24.9, 4.1), (24.1, 4.9, 24.9, 4.9), (24.9, 4.1, 24.9, 4.9),
    (13.7, 4.1, 13.7, 5.0), (13.7, 4.1, 14.5, 4.1), (13.7, 5.0, 14.5, 5.0), (14.5, 4.1, 14.5, 5.0),
    (13.7, 0.5, 13.7, 1.9), (13.7, 0.5, 14.5, 0.5), (13.7, 1.9, 14.5, 1.9), (14.5, 0.5, 14.5, 1.9),
    (13.7, 0.5, 14.5, 0.5), (13.7, 0.5, 13.7, 1.9), (13.7, 1.9, 14.5, 1.9), (14.5, 0.5, 14.5, 1.9),
    (-0.3, 0.5, 0.5, 0.5), (-0.3, 0.5, -0.3, 1.9), (-0.3, 1.9, 0.5, 1.9), (0.5, 0.5, 0.5, 1.9),
    (2.5, 0.5, 3.3, 0.5), (2.5, 0.5, 2.5, 1.9), (2.5, 1.9, 3.3, 1.9), (3.3, 0.5, 3.3, 1.9),
    (5.3, 0.5, 6.1000000000000005, 0.5), (5.3, 0.5, 5.3, 1.9), (5.3, 1.9, 6.1000000000000005, 1.9), (6.1000000000000005, 0.5, 6.1000000000000005, 1.9),
    (8.1, 0.5, 8.9, 0.5), (8.1, 0.5, 8.1, 1.9), (8.1, 1.9, 8.9, 1.9), (8.9, 0.5, 8.9, 1.9),
    
    ]

m_lines = [
    (0.5, 3.0, 0.5, 17.0),
    (-0.6, 6.0, -0.6, 16.0),
    (-0.5, 17.0, 4.8, 17.0),
    (0.7, 18.0, 3.7, 18.0),
    (3.7, 3.0, 3.7, 17.0),
    (4.8, 8.0, 4.8, 17.0),
    (5.9, 17.0, 6.9, 17.0),
    (8.0, 3.0, 8.0, 9.0),
    (8.0, 16.0, 8.0, 17.0),
    (9.0, 8.0, 9.0, 17.0),
    (9.0, 4.0, 9.0, 5.0),
    (12.0, 11.0, 12.0, 17.0),
    (13.0, 8.0, 13.0, 17.0),
    (16.0, 8.0, 16.0, 17.0),
    (19.0, 3.0, 19.0, 8.0),
    (22.0, 3.0, 22.0, 8.0),
    (23.0, 3.0, 23.0, 8.0),
    (5.9, 17.0, 6.9, 17.0),
    (12.6, 3.0, 12.6, 5.0),
    (12.0, 3.0, 12.0, 8.0),
    (13.0, 5.0, 13.0, 8.0),
    (8.0, 11.5, 8.0, 13.5),
    (23.1, -1.0, 23.1, 3.0),
    (23.1, 2.6, 23.6, 2.6),
    (25.4, 2.6, 25.9, 2.6),
    (23.1, 3.0, 25.9, 3.0),
    (1.5, -1.0, 1.5, 3.0),
    (7.1, -1.0, 7.1, 3.0),
    (12.7, -1.0, 12.7, 3.0),
    (13.5, 8.0, 14.0, 8.0),
    (26.0, 5.5, 26.0, 6.5),
    ]

# <codecell>

d = {'cut_lines': cut_lines, 'm_lines': m_lines, 'v_lines': v_lines}
for n, lines in d.items():
    print "%s = [" % n
    for line in lines:
        if line[0] >=19.0 and line[1] <=3.0 and line[2] <=23.0 and line[3] <= 3.0:
            pass
        else:
            pass
#            print "    (%.1f, %.1f, %.1f, %.1f)," % line
#    print "    ]"
#    print

# <codecell>

cc30_n = [
    (9.0, 8.0, 12.0, 11.0),
    (19.0, 11.0, 22.0, 8.0)]
    
cc25 = []

cc05_n = [
    (-1.1, 6.0, -1.6, 6.5),
    (-1.6, 15.5, -1.1, 16.0),
    (-0.5, 17.5, 0.5, 17.5),
    (3.7, 17.5, 4.7, 17.5),
    (0.6, 18.5, 1.1, 19.0),
    (3.1, 19.0, 3.6, 18.5),
    (5.9, 17.5, 6.9, 17.5),
    (9.0, 12.0, 8.5, 11.5),
    (8.5, 13.5, 9.0, 13.0),
    (8.7, 4.0, 8.7, 5.0),
    (18.5, 6.5, 18.5, 7.5),
    ]

circles03 = [
             (11.3, 1.5),
             (11.3, 1.1),
           (10.5, 4.5),
           (17.5, 4.5),
           (20.5, 4.5),
           (21.7, 1.1),
           (24.5, 1.1),
           ]

circles10 = []

# <codecell>

cut_pattern = '<path d = "M%i %i L%i %i" />'
dpcm = 37.8
zero_x = -1.8
zero_y = -1.4
def cor(d):
    return int(float(d + 1.6) * dpcm)

def col(locs):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm), int((locs[2] - zero_x) * dpcm), int((locs[3] - zero_y) * dpcm))
cut_svg = [cut_pattern % col(loc) for loc in cut_lines]
m_svg = [cut_pattern %  col(loc) for loc in m_lines]
v_svg = [cut_pattern % col(loc) for loc in v_lines]

# <codecell>

curve_pattern = '<path d = "M{2} {3} A{4} {4} 0 0 1 {0} {1}" />'
def col(locs, radius):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm), int((locs[2] - zero_x) * dpcm), int((locs[3] - zero_y) * dpcm), int(radius * dpcm))

curve_svg = [curve_pattern.format(*col(loc, 0.5)) for loc in cc05_n]
curve25_svg = [curve_pattern.format(*col(loc, 2.5)) for loc in cc25]
curve30_svg = [curve_pattern.format(*col(loc, 3.0)) for loc in cc30_n]

# <codecell>

circle03_pattern = '<circle cx="{0}" cy="{1}" r="%i" fill="gray"/>' % int(0.3 * dpcm)
circle10_pattern = '<circle cx="{0}" cy="{1}" r="%i"/>' % int(1.0 * dpcm)
def col(locs):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm))

circle03_svg = [circle03_pattern.format(*col(loc)) for loc in circles03]
circle10_svg = [circle10_pattern.format(*col(loc)) for loc in circles10]
circle00_svg = circle10_pattern.format(*col((0, 0)))
print circle00_svg

# <codecell>

grid_5 = [(0.5 * i, -1.2, 0.5 * i, 20.0) for i in range(-3, 55)] + [(-2.0, 0.5 * i, 27.0, 0.5* i) for i in range(-2, 42)]
grid_1 = [(0.1 * i, -1.2, 0.1 * i, 20.0) for i in range(-20, 270)] + [(-2.0, 0.1 * i, 27.0, 0.1* i) for i in range(-12, 210)]

grid_pattern = '<path d = "M%i %i L%i %i" />'
def col(locs):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm), int((locs[2] - zero_x) * dpcm), int((locs[3] - zero_y) * dpcm))
grid5_svg = [grid_pattern % col(loc) for loc in grid_5]
grid1_svg = [grid_pattern % col(loc) for loc in grid_1]
zero_point = col((0, 0, 0, 0))

# <codecell>

print zero_point

# <codecell>

docu = base.format("\n".join(grid1_svg),
                   "\n".join(grid5_svg),
                   "\n".join(cut_svg), 
                   "\n".join(curve_svg), 
                   "\n".join(curve25_svg), 
                   "\n".join(curve30_svg),  
                   "\n".join(circle03_svg), 
                   "\n".join(circle10_svg), 
                   "\n".join(m_svg), 
                   "\n".join(v_svg)
                   )
with open("micro12.html", 'w') as f:
    f.write(docu)

# <codecell>

20

# <codecell>

import math
locs = []
center = (21.7, 1.1)
radi = 0.4
for x, y in [(radi * math.sin(math.pi * d / 180) + center[0], radi * math.cos(math.pi * d/ 180) + center[1]) for d in range(0, 360, 30)]:
    locs.append((center[0], center[1], x, y))

print locs

# <codecell>

center = (11.3, 1.5)
left = center[0] - 0.4
right = center[0] + 0.4
upper = center[1] - 1.0
lower = center[1] + 0.4
loc = [(left, upper, right, upper),
       (left, upper, left, lower),
       (left, lower, right, lower),
       (right, upper, right, lower)]
print loc

# <codecell>


# <codecell>


# <codecell>


