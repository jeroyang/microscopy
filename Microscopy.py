# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

base = """
<!DOCTYPE html>
<html>
<body>

<svg height="794" width="1123">
<g fill="none" stroke="black" stroke-width="2">
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
  Sorry, your browser does not support inline SVG.
</svg>

</body>
</html>
"""

# <codecell>


# <codecell>


# <codecell>

cc30_n = [
    (9.0, 8.0, 12.0, 11.0),
    (13.0, 11.0, 16.0, 8.0)]

v_lines_n = [
    (15.6, 3.0, 15.6, 6.0),
    (4.3, -1.0, 4.3, 3.0),
    (9.9, -1.0, 9.9, 3.0),
    (17.5, -1.0, 17.5, 3.0),
    (23.1, -1.0, 23.1, 3.0),
    (23.1, 3.0, 21.9, 3.0)]

cc05_n = [
    (-0.5, 9.0, -1.0, 9.5),
    (-1.0, 15.5, -0.5, 16.0),
    (0.0, 17.5, 1.0, 17.5),
    (4.0, 17.5, 5.0, 17.5),
    (1.0, 18.5, 1.5, 19.0),
    (3.5, 19.0, 4.0, 18.5),
    (6.0, 17.5, 7.0, 17.5),
    (9.0, 12.0, 8.5, 11.5),
    (8.5, 13.5, 9.0, 13.0),
    (17.0, 8.5, 18.0, 8.5),
    (18.5, 6.5, 18.5, 7.5),
    (20.0, 8.5, 21.0, 8.5),
    (25.0, 8.5, 26.0, 8.5)]

cut_lines_n = [
    (0.0, 3.0, 0.0, 9.0),
    (-1.0, 9.5, -1.0, 15.5),
    (-0.5, 9.0, 0.0, 9.0),
    (-0.5, 16.0, 0.0, 16.0),
    (0.0, 11.5, 0.0, 13.5),
    (0.0, 16.0, 0.0, 17.5),
    (1.0, 17.0, 1.0, 18.5),
    (4.0, 17.0, 4.0, 18.5),
    (2.0, 18.0, 3.0, 18.0),
    (4.0, 3.0, 4.0, 8.0),
    (4.0, 8.0, 5.0, 8.0),
    (5.0, 3.0, 5.0, 8.0),
    (6.0, 16.0, 6.0, 17.5),
    (7.0, 16.0, 7.0, 17.5),
    (7.0, 11.5, 8.5, 11.5),
    (7.0, 13.5, 8.5, 13.5),
    (8.0, 9.0, 8.0, 11.5),
    (8.0, 13.5, 8.0, 16.0),
    (9.0, 3.0, 9.0, 8.0),
    (11.0, 8.0, 12.0, 8.0),
    (12.6, 6.0, 16.0, 6.0),
    (13.0, 6.5, 13.0, 7.5),
    (12.0, 8.0, 12.0, 11.0),
    (13.0, 8.0, 13.0, 11.0),
    (17.0, 8.0, 17.0, 17.0),
    (18.0, 8.0, 18.0, 8.5),
    (-1.3, 3.0, 12.7, 3.0),
    #(15.5, 3.0, 16.1, 3.0),
    
    (-1.3, -1.0, 15.5, -1.0),
    (15.5, -1.0, 25.9, -1.0),
    (15.5, -1.0, 15.5, 3.0),
    #(16.1, -1.0, 16.1, 3.0),
    (-1.3, -1.0, -1.3, 3.0),
    (25.9, -1.0, 25.9, 3.0),

    (15.5, 3.0, 23.1, 3.0),
    (18.5, 6.5, 20.0, 6.5),
    (18.5, 7.5, 20.0, 7.5),
    (16.0, 8.0, 17.0, 8.0),
    (17.0, 8.0, 17.0, 17.0),
    (5.0, 17.0, 6.0, 17.0),
    (7.0, 17.0, 17.0, 17.0),
    (26.0, 3.0, 26.0, 8.5),
    (25.0, 8.0, 25.0, 8.5),
    (18.0, 8.0, 20.0, 8.0),
    (21.0, 8.0, 25.0, 8.0),
    (26.0, 7.5, 26.0, 8.0),
    (1.5, 19.0, 3.5, 19.0),
    (5.0, 17.0, 5.0, 17.5),
    (9.0, 12.0, 9.0, 13.0),
    (20.0, 8.0, 20.0, 8.5),
    (21.0, 8.0, 21.0, 8.5),
    #(-0.5, -1.0, -0.5, 3.0),
    (14.0, 8.0, 15.0, 8.0)]

m_lines_n = [
    (1.0, 3.0, 1.0, 17.0),
    (0.0, 9.0, 0.0, 11.5),
    (0.0, 13.5, 0.0, 16.0),
    (0.0, 17.0, 5.0, 17.0),
    (1.0, 18.0, 4.0, 18.0),
    (4.0, 8.0, 4.0, 17.0),
    (5.0, 8.0, 5.0, 17.0),
    (6.0, 17.0, 7.0, 17.0),
    (8.0, 3.0, 8.0, 9.0),
    (8.0, 16.0, 8.0, 17.0),
    (9.0, 8.0, 9.0, 17.0),
    (12.0, 11.0, 12.0, 17.0),
    (13.0, 11.0, 13.0, 17.0),
    (16.0, 8.0, 16.0, 17.0),
    (19.0, 3.0, 19.0, 8.0),
    (22.0, 3.0, 22.0, 8.0),
    (23.0, 3.0, 23.0, 8.0),
    (6.0, 17.0, 7.0, 17.0),
    (12.0, 8.0, 13.0, 8.0),
    (12.6, 3.0, 12.6, 6.0),
    (12.0, 3.0, 12.0, 8.0),
    (13.0, 6.0, 13.0, 8.0),
    (16.0, 3.0, 16.0, 8.0),
    (8.0, 11.5, 8.0, 13.5),

    (20.3, -1.0, 20.3, 3.0),
    (23.1, 3.0, 25.9, 3.0), 
    (1.5, -1.0, 1.5, 3.0),
    (7.1, -1.0, 7.1, 3.0),
    (12.7, -1.0, 12.7, 3.0),
    (12.7, 3.0, 15.5, 3.0),
    (26.0, 6.5, 26.0, 7.5)]

circles03 = [
           (0.1, 1.5),
           (2.9, 1.5),
           (5.7, 1.5),
           (8.5, 1.5),
           (11.3, 1.5),
           (14.1, 1.5),
           (14.1, 4.5),
           (10.5, 4.5),
           (17.5, 4.5),
           (20.5, 4.5),
           (24.5, 4.5),
           
           (16.1, 1.5),
           (18.9, 1.5),
           (21.7, 1.5),
           (24.5, 1.5)
           ]

circles10 = []

# <codecell>

d = {'cut_lines': cut_lines_n, 'm_lines': m_lines_n, 'v_lines': v_lines_n}
for n, lines in d.items():
    print "%s = [" % n
    for line in lines:
        if line[0] <= 7 and line[1] >=3 and line[2] <= 7 and line[3] >= 3:
            print "    (%.1f, %.1f, %.1f, %.1f)," % (line[0] - 0.1, line[1], line[2] -0.1, line[3])
        else:
            print "    (%.1f, %.1f, %.1f, %.1f)," % line
    print "    ]"
    print

# <codecell>

cut_pattern = '<path d = "M%i %i L%i %i" />'
dpcm = 37.8
zero_x = -2.0
zero_y = -1.4
def cor(d):
    return int(float(d + 1.6) * dpcm)

def col(locs):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm), int((locs[2] - zero_x) * dpcm), int((locs[3] - zero_y) * dpcm))
cut_svg = [cut_pattern % col(loc) for loc in cut_lines_n]
m_svg = [cut_pattern %  col(loc) for loc in m_lines_n]
v_svg = [cut_pattern % col(loc) for loc in v_lines_n]

# <codecell>

curve_pattern = '<path d = "M{2} {3} A{4} {4} 0 0 1 {0} {1}" />'
def col(locs, radius):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm), int((locs[2] - zero_x) * dpcm), int((locs[3] - zero_y) * dpcm), int(radius * dpcm))

curve_svg = [curve_pattern.format(*col(loc, 0.5)) for loc in cc05_n]
curve30_svg = [curve_pattern.format(*col(loc, 3.0)) for loc in cc30_n]

# <codecell>

circle03_pattern = '<circle cx="{0}" cy="{1}" r="%i"/>' % int(0.3 * dpcm)
circle10_pattern = '<circle cx="{0}" cy="{1}" r="%i"/>' % int(1.0 * dpcm)
def col(locs):
    return (int((locs[0] - zero_x) * dpcm), int((locs[1] - zero_y) * dpcm))

circle03_svg = [circle03_pattern.format(*col(loc)) for loc in circles03]
circle10_svg = [circle10_pattern.format(*col(loc)) for loc in circles10]

# <codecell>

docu = base.format("\n".join(cut_svg), 
                   "\n".join(curve_svg), 
                   "\n".join(curve30_svg), 
                   "\n".join(circle03_svg), 
                   "\n".join(circle10_svg), 
                   "\n".join(m_svg), 
                   "\n".join(v_svg))
with open("micro1.html", 'w') as f:
    f.write(docu)

# <codecell>


# <codecell>

for i in range(1, 7):
    print 24.5 - 2.8 * i

# <codecell>


