# Johannes Fischer
# 28.12.2017

import math
import SVGtools
import numpy as np



def DrawLine(x1,y1,x2,y2,c):
    global id
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{5:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M {1:.2f},{2:.2f} {3:.2f},{4:.2f}"/>\n'.format(id,x1,y1,x2,y2,c));
    id = id+1;
    return;

def RoundedRect(x0,y0,w,h,r,c):
    # w: width
    # h: height
    # r: radius in all 4 corners
    # c: color of rectangle
    # start with top left corner
    global id
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" \
    d="M {2:f},{3:f} H {4:f} A {5:f} {5:f} 0 0 1 {6:f} {7:f} V {8:f} A {5:f} {5:f} 0 0 1 {9:f} {10:f} H {11:f} A {5:f} {5:f} 0 0 1 {12:f} {13:f} V {14:f} A {5:f} {5:f} 0 0 1 {15:f} {16:f}"/>'\
    .format(id,c,x0+r,y0,x0+w-r,r,x0+w,y0+r,y0+h-r,x0+w-r,y0+h,x0+r,x0,y0+h-r,y0+r,x0+r,y0));
    return;

f = open('Lozenge_variableCuts_singlePass.svg','w');

# size of workbed
Y = 600;
X = 1210;

#write svg header
SVGtools.SVGheader(f,Y,X);

# cell length
a = 10;#mm

# margin
mx = 15;#mm
my = 15 + a*math.sqrt(2)/2;#mm

# number of elements along one side
N = 8;

p = np.array([[ 8, 6, 2, 2, 2, 2, 3, 3],
                [ 8, 6, 2, 2, 2, 2, 3, 0],
              [ 8, 6, 6, 2, 2, 2, 3, 3],
                [ 8, 8, 6, 9, 2, 2, 3, 0],
              [ 8, 1, 8, 6, 9, 2, 9, 3],
                [ 1, 1, 8, 6, 9, 9, 3, 0],
              [ 1,13, 1, 1, 6, 9, 9 ,9],
                [ 1,13, 1, 1, 6, 1, 9, 0],
              [ 1,13,13, 1, 6, 1, 9, 4],
                [ 1,13,13, 1, 1, 9, 4, 0],
              [ 7, 1,13,13, 1, 9, 4,10],
                [ 7, 1,13, 7, 1, 4,10, 0],
              [11, 7,13, 7, 4, 4, 4,10],
                [11, 7, 7, 4, 4, 4,10, 0],
              [11,11, 7, 4, 4, 4,10,10]]);

np.transpose(p);

id = 0;
# draw inner structure
for ii in range(1,N-1):
    for jj in range(1,N-1):
        # top left
        if p[2*ii][jj] != p[2*ii-1][jj-1]:
            c = '0000ff';
        else:
            c = '000000';
        DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);

        # top right
        if p[2*ii][jj] != p[2*ii-1][jj]:
            c = '0000ff';
        else:
            c = '000000';
        DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

        # bottom left
        if p[2*ii][jj] != p[2*ii+1][jj-1]:
            c = '0000ff';
        else:
            c = '000000';
        DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);

        # bottom right
        if p[2*ii][jj] != p[2*ii+1][jj]:
            c = '0000ff';
        else:
            c = '000000';
        DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

jj = 0;
for ii in range(0,N):
    c = '0000ff';
    # top left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);
    # bottom left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);
    # top right
    if p[2*ii][jj] != p[2*ii-1][jj]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);
    # bottom right
    if ii == N-1 or p[2*ii][jj] != p[2*ii+1][jj]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);



jj = N-1;
for ii in range(0,N):
    c = '0000ff';
    # top right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);
    # bottom right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+(ii)*a*math.sqrt(2),c);
    # top left
    if p[2*ii][jj] != p[2*ii-1][jj-1]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);

    # bottom left
    if ii == N-1 or p[2*ii][jj] != p[2*ii+1][jj-1]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);

ii = 0;
for jj in range(1,N-1):
    c = '0000ff';
    # top left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);
    # top right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);
    # bottom left
    if p[2*ii][jj] != p[2*ii+1][jj-1]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);
    # bottom right
    if p[2*ii][jj] != p[2*ii+1][jj]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

ii = N-1;
for jj in range(1,N-1):
    c = '0000ff';
    # bottom left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);
    # bottom right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+(ii)*a*math.sqrt(2),c);
    # top left
    if p[2*ii][jj] != p[2*ii-1][jj-1]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);
    # top right
    if p[2*ii][jj] != p[2*ii-1][jj]:
        c = '0000ff';
    else:
        c = '000000';
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);


RoundedRect(0,0,2*mx+N*a*math.sqrt(2), 2*my+(N-1)*a*math.sqrt(2),10,'ff0000');


#f.write('<path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 4,44 H 39 V 59 H 29 v -5 h 5 V 49 H 24 V 64 H 59 V 79 H 49 v -5 h 5 V 69 H 44 V 84 H 79 V 69 H 69 v 5 h 5 v 5 H 64 V 64 H 99 V 49 H 89 v 5 h 5 v 5 H 84 V 29 h 10 v 5 h -5 v 5 H 99 V 24" id="path1088"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 79,84 V 99 H 69 v -5 h 5 V 89 H 64 v 30 h 10 v -5 h -5 v -5 h 10 v 30 H 69 v -5 h 5 v -5 H 64 v 30 h 10 v -5 h -5 v -5 h 10 v 30 H 69 v -5 h 5 v -5 H 64 v 30 h 10 v -5 h -5 v -5 h 10 v 30 H 69 v -5 h 5 v -5 H 64 v 30 h 10 v -5 h -5 v -5 h 10 v 15 H 44 v 15 h 10 v -5 h -5 v -5 h 10 v 30 H 49 v -5 h 5 v -5 H 44 v 30 h 10 v -5 h -5 v -5 h 10 v 15" id="path1090"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m 64,304 v -15 h 10 v 5 h -5 v 5 H 79 V 269 H 69 v 5 h 5 v 5 H 64 v -15 h 35 v 15 H 89 v -5 h 5 v -5 H 84 v 15 h 35 v -15 h -10 v 5 h 5 v 5 h -10 v -30 h 10 v 5 h -5 v 5 h 10 v -30 h -10 v 5 h 5 v 5 h -10 v -15 h 35 v 15 h -10 v -5 h 5 v -5 h -10 v 15 h 35 v -15 h -10 v 5 h 5 v 5 h -10 v -30 h 10 v 5 h -5 v 5 h 10 v -15 h -35 v -15 h 10 v 5 h -5 v 5 h 10 v -15 h -35 v -15 h 10 v 5 h -5 v 5 h 10 V 164 H 84 v 15 h 10 v -5 h -5 v -5 h 10 v 15 H 64" id="path1092"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m 184,24 v 15 h 10 v -5 h -5 v -5 h 10 v 30 h -10 v -5 h 5 v -5 h -10 v 30 h 10 v -5 h -5 v -5 h 10 V 84 H 164 V 69 h 10 v 5 h -5 v 5 h 10 V 64 h -35 v 15 h 10 v -5 h -5 v -5 h 10 v 30 h -10 v -5 h 5 v -5 h -10 v 30 h 10 v -5 h -5 v -5 h 10 v 15 h -35 v 15 h 10 v -5 h -5 v -5 h 10 v 15 h -35 v -15 h 10 v 5 h -5 v 5 h 10 V 124 H 84 v -15 h 10 v 5 h -5 v 5 H 99 V 104 H 64" id="path1094"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m 144,224 h 35 v -15 h -10 v 5 h 5 v 5 h -10 v -15 h 35 v -15 h -10 v 5 h 5 v 5 h -10 v -30 h 10 v 5 h -5 v 5 h 10 v -30 h -10 v 5 h 5 v 5 h -10 v -15 h 35 v -15 h -10 v 5 h 5 v 5 h -10 v -30 h 10 v 5 h -5 v 5 h 10 V 104 H 184 V 89 h 10 v 5 h -5 v 5 h 10 V 84" id="path1096"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 319,84 H 284 V 69 h 10 v 5 h -5 v 5 h 10 V 64 h -35 v 15 h 10 v -5 h -5 v -5 h 10 V 84 H 244 V 69 h 10 v 5 h -5 v 5 h 10 V 64 H 224 V 49 h 10 v 5 h -5 v 5 h 10 V 44 h -35 v 15 h 10 v -5 h -5 v -5 h 10 v 15 h -35" id="path1098"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m 219,144 v 15 h -10 v -5 h 5 v -5 h -10 v 30 h 10 v -5 h -5 v -5 h 10 v 30 h -10 v -5 h 5 v -5 h -10 v 30 h 10 v -5 h -5 v -5 h 10 v 30 h -10 v -5 h 5 v -5 h -10 v 30 h 10 v -5 h -5 v -5 h 10 v 15 h -35 v 15 h 10 v -5 h -5 v -5 h 10 v 30 h -10 v -5 h 5 v -5 h -10 v 15" id="path1100"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m 319,164 h -35 v -15 h 10 v 5 h -5 v 5 h 10 v -15 h -35 v -15 h 10 v 5 h -5 v 5 h 10 v -15 h -35 v 15 h 10 v -5 h -5 v -5 h 10 v 15 h -35 v -15 h 10 v 5 h -5 v 5 h 10 v -15 h -35" id="path1102"/><path style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="m 204,204 h 35 v 15 h -10 v -5 h 5 v -5 h -10 v 15 h 35 v 15 h -10 v -5 h 5 v -5 h -10 v 15 h 35 v -15 h -10 v 5 h 5 v 5 h -10 v -15 h 35 v 15 h -10 v -5 h 5 v -5 h -10 v 15 h 35" id="path1104"/>');
f.write('</svg>');
f.close();
