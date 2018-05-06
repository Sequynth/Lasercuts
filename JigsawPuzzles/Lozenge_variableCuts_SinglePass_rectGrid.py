# Johannes Fischer
# 28.12.2017

import math
import SVGtools
import numpy as np



def DrawLine(x1,y1,x2,y2,c):
    global id
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{5:s};stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M {1:.2f},{2:.2f} {3:.2f},{4:.2f}"/>\n'.format(id,x1,y1,x2,y2,c));
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

def DrawGrid(x0,y0,d,N,c):
    # x0: x-start
    # y0: y-start
    # d: distance of gridlines
    # N: Number of Lines in either direction
    # c: color of grid
    global id
    for ii in range(0,N):
        DrawLine(x0+ii*d,y0,x0+ii*d,y0+(N-1)*d,c);
    for jj in range(0,N):
        DrawLine(x0,y0+jj*d,x0+(N-1)*d,y0+jj*d,c);
    return;

f = open('Lozenge_variableCuts_singlePass_rectGrid.svg','w');

# size of workbed
Y = 600;
X = 1210;

#write svg header
SVGtools.SVGheader(f,Y,X);

# cell length
a = 10;#mm

# margin
mx = 10;#mm
my = 10 + a*math.sqrt(2)/2;#mm

# number of elements along one side
N = 8;

p = np.array([[ 8, 6, 2, 2, 2, 2, 3, 3],
                [ 8, 6, 2, 2, 2, 2, 3, 0],
              [ 8, 8, 6, 2, 2, 2, 3, 3],
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
c = '0000ff';
for ii in range(1,N-1):
    for jj in range(1,N-1):
        # top left
        if p[2*ii][jj] != p[2*ii-1][jj-1]:
            DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);

        # top right
        if p[2*ii][jj] != p[2*ii-1][jj]:
            DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

        # bottom left
        if p[2*ii][jj] != p[2*ii+1][jj-1]:
            DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);

        # bottom right
        if p[2*ii][jj] != p[2*ii+1][jj]:
            DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

jj = 0;
for ii in range(0,N):
    # top left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);
    # bottom left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);
    # top right
    if p[2*ii][jj] != p[2*ii-1][jj]:
        DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);
    # bottom right
    if ii == N-1 or p[2*ii][jj] != p[2*ii+1][jj]:
        DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);



jj = N-1;
for ii in range(0,N):
    # top right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);
    # bottom right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+(ii)*a*math.sqrt(2),c);
    # top left
    if p[2*ii][jj] != p[2*ii-1][jj-1]:
        DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);

    # bottom left
    if ii == N-1 or p[2*ii][jj] != p[2*ii+1][jj-1]:
        DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);

ii = 0;
for jj in range(1,N-1):
    # top left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);
    # top right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);
    # bottom left
    if p[2*ii][jj] != p[2*ii+1][jj-1]:
        DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);
    # bottom right
    if p[2*ii][jj] != p[2*ii+1][jj]:
        DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

ii = N-1;
for jj in range(1,N-1):
    # bottom left
    DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2),c);
    # bottom right
    DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii+0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+(ii)*a*math.sqrt(2),c);
    # top left
    if p[2*ii][jj] != p[2*ii-1][jj-1]:
        DrawLine(mx+jj*a*math.sqrt(2), my+ii*a*math.sqrt(2), mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2),c);
    # top right
    if p[2*ii][jj] != p[2*ii-1][jj]:
        DrawLine(mx+(jj+0.5)*a*math.sqrt(2), my+(ii-0.5)*a*math.sqrt(2), mx+(jj+1)*a*math.sqrt(2), my+ii*a*math.sqrt(2),c);

DrawGrid(mx+a*math.sqrt(2)/4,my-a*math.sqrt(2)/4,a*math.sqrt(2)/2,2*N,'000000');
#DrawGrid(mx+a*math.sqrt(2)/2,my,a*math.sqrt(2),2*N,'000000');

RoundedRect(0,0,2*mx+N*a*math.sqrt(2), 2*my+(N-1)*a*math.sqrt(2),10,'ff0000');

f.write('</svg>');
f.close();
