# Johannes Fischer
# 03.10.2017

def SVGheader(f,h,w):
    # writes a valid header of a SVG file. Taken from an Inkscape file that was saved as "normal SVG"
    # Input arguments: 
    # f: pointer to file
    # h: document height
    # w: document width
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n');
    f.write('<svg\n   xmlns:dc="http://purl.org/dc/elements/1.1/"\n   xmlns:cc="http://creativecommons.org/ns#"\n   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n   xmlns:svg="http://www.w3.org/2000/svg"\n   xmlns="http://www.w3.org/2000/svg"\n   id="svg395"\n   height="{0:.5f}"\n   width="{1:.5f}"\n   version="1.1">\n'.format(h,w));