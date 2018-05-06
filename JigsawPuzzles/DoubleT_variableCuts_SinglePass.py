# Johannes Fischer
# 09.11.2017

import math
import SVGtools
import numpy as np

def DrawDoubleT(a,x,y):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    global id
    xVals = [0, 0, 2, 2, 1, 1, 3, 3, 1, 1, 2, 2, 0, 0, 7, 7, 5, 5, 6, 6, 4, 4, 6, 6, 5, 5, 7, 7];
    yVals = [0, 3, 3, 2, 2, 1, 1, 7, 7, 6, 6, 5, 5, 8, 8, 5, 5, 6, 6, 7, 7, 1, 1, 2, 2, 3, 3, 0];
    f.write('<path id="path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return

def DrawTopLeft(a,x,y,c):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    # c: stroke-color
    global id
    xVals = [0, 0, 2, 2, 1, 1, 3, 3];
    yVals = [0, 3, 3, 2, 2, 1, 1, 4];
    f.write('<path id="TL_path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id,c));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    id = id+1;
    return

def DrawBottomLeft(a,x,y,c):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    # c: stroke-color
    global id
    xVals = [3, 3, 1, 1, 2, 2, 0, 0];
    yVals = [4, 7, 7, 6, 6, 5, 5, 8];
    f.write('<path id="BL_path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id,c));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    id = id+1;
    return

def DrawBottomRight(a,x,y,c):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    # c: stroke-color
    global id
    xVals = [7, 7, 5, 5, 6, 6, 4, 4];
    yVals = [8, 5, 5, 6, 6, 7, 7, 4];
    f.write('<path id="BR_path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id,c));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    id = id+1;
    return

def DrawTopRight(a,x,y,c):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    # c: stroke-color
    global id
    xVals = [4, 4, 6, 6, 5, 5, 7, 7];
    yVals = [4, 1, 1, 2, 2, 3, 3, 0];
    f.write('<path id="TR_path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id,c));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    id = id+1;
    return

def DrawTop(a,x,y,c):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    # c: stroke-color
    global id
    xVals = [0, 7];
    yVals = [0, 0];
    f.write('<path id="T_path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id,c));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return

def DrawBottom(a,x,y,c):
    # a: unit size
    # x: starting x-Pos
    # y: starting y-Pos
    # c: stroke-color
    global id
    xVals = [0, 7];
    yVals = [8, 8];
    f.write('<path id="B_path{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id,c));
    for ii in range (0, len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return


def DrawOutlineLeft(a,x,y):
    global id
    xVals = [0,0,2,2,1,1,3,3,1,1,2,2,0,0];
    yVals = [0,3,3,2,2,1,1,7,7,6,6,5,5,8];
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id));
    for ii in range (0,len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return;

def DrawOutlineRight(a,x,y):
    global id
    xVals = [7,7,5,5,6,6,4,4,6,6,5,5,7,7];
    yVals = [8,5,5,6,6,7,7,1,1,2,2,3,3,0];
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id));
    for ii in range (0,len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return;

def DrawOutlineBottom(a,x,y):
    global id
    xVals = [0,7,7,5,5,6,6,4,4,11,11,9,9,10,10,8,8];
    yVals = [8,8,5,5,6,6,7,7,4, 4, 7,7,6, 6, 5,5,8];
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id));
    for ii in range (0,len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return;

def DrawOutlineTop(a,x,y):
    global id
    xVals = [0,7,7,5,5,6,6,4,4,11,11,9,9,10,10,8,8];
    yVals = [0,0,3,3,2,2,1,1,4, 4, 1,1,2, 2, 3,3,0];
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M '.format(id));
    for ii in range (0,len(xVals)):
        f.write('{0:.2f},{1:.2f} '.format(x + a*xVals[ii],y + a*yVals[ii]));
    f.write('"/>\n');
    return;

def DrawLine(x1,y1,x2,y2):
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#0000ff;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M {1:.2f},{2:.2f} {3:.2f},{4:.2f}"/>\n'.format(id,x1,y1,x2,y2));
    return;

def RoundedRect(x0,y0,w,h,r,c):
    # w: width
    # h: height
    # r: radius in all 4 corners
    # c: color of rectangle
    # start with top left corner
    global id
    f.write('<path id="path_{0:d}" style="fill:none;fill-rule:evenodd;stroke:#{1:s};stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" \
    d="M {2:f},{3:f} H {4:f} A {5:f} {5:f} 0 0 1 {6:f} {7:f} V {8:f} A {5:f} {5:f} 0 0 1 {9:f} {10:f} H {11:f} A {5:f} {5:f} 0 0 1 {12:f} {13:f} V {14:f} A {5:f} {5:f} 0 0 1 {15:f} {16:f}"/>\n'\
    .format(id,c,x0+r,y0,x0+w-r,r,x0+w,y0+r,y0+h-r,x0+w-r,y0+h,x0+r,x0,y0+h-r,y0+r,x0+r,y0));
    return;

f = open('DoubleT_variableCuts_singlePass.svg','w');

# size of workbed
Y = 600;
X = 1210;

#write svg header
SVGtools.SVGheader(f,Y,X);

# smallest unit size
a = 3;#mm

# margin
mx = 15;#mm
my = 15;#mm

# number of elements along one side
N = 8;

cCut = '5555ff';
cMark = '888888';
cOuter = 'ff0000';

p = np.array([[ 2, 0, 2, 0, 4, 0, 4, 0, 4, 0, 5, 0, 5, 0, 5],
              [ 1, 2, 2, 2, 4, 4, 4, 4, 4, 5, 6, 5, 5, 5, 5],
              [ 1, 1, 1, 4, 4, 4, 4, 7, 7, 6, 6, 6, 6, 6, 6],
              [ 1, 1, 1, 7, 7, 4, 7, 7, 7, 7, 9, 6, 6, 6, 6],
              [ 1, 1, 1, 7, 3, 7, 7, 7, 7, 9,10, 9, 9, 6, 9],
              [ 1, 1, 1, 3, 3, 3, 3, 7,10,10,11, 9, 9, 9, 9],
              [ 1, 1, 3, 3, 3,10,10,10,10,10,11,11,11,11,11],
              [ 1, 1, 3,10,10,10,10,10,10,11,11,11,11,11,11]]);

id = 0;

for ii in range(0,N):
    for jj in range(0,N):
        if ii != 0 and ii != N-1 and jj != 0 and jj != N-1:
            if p[ii][2*jj] != p[ii][2*jj-1]:
                c = cCut;
            else:
                c = cMark;
            DrawTopLeft(a,mx+jj*8*a,my+ii*8*a,c);

            if p[ii][2*jj] != p[ii+1][2*jj-1]:
                c = cCut;
            else:
                c = cMark;
            DrawBottomLeft(a,mx+jj*8*a,my+ii*8*a,c);

            if p[ii][2*jj] != p[ii+1][2*jj+1]:
                c = cCut;
            else:
                c = cMark;
            DrawBottomRight(a,mx+jj*8*a,my+ii*8*a,c);

            if p[ii][2*jj] != p[ii][2*jj+1]:
                c = cCut;
            else:
                c = cMark;
            DrawTopRight(a,mx+jj*8*a,my+ii*8*a,c);

            if p[ii][2*jj] != p[ii-1][2*jj]:
                c = cCut;
            else:
                c = cMark;
            DrawTop(a,mx+jj*8*a,my+ii*8*a,c);

            if p[ii][2*jj-1] != p[ii-1][2*jj-1]:
                c = cCut;
            else:
                c = cMark;
            DrawTop(a,mx+4*a+(jj-1)*8*a,my+4*a+(ii-1)*8*a,c);

ii = 0;
for jj in range(0,N):
    c = cCut;
    DrawTopLeft(a,mx+jj*8*a,my+ii*8*a,c);
    DrawTopRight(a,mx+jj*8*a,my+ii*8*a,c);
    DrawTop(a,mx+jj*8*a,my+ii*8*a,c);
    #if jj != N-1:
        #DrawTop(a,mx+4*a+jj*8*a,my+4*a+ii*8*a,c);
    if (jj != N-1 and p[ii][2*jj] != p[ii+1][2*jj-1]) or jj == 0:
        c = cCut;
    else:
        c = cMark;
    DrawBottomLeft(a,mx+jj*8*a,my+ii*8*a,c);
    if (jj != N-1 and p[ii][2*jj] != p[ii+1][2*jj+1]) or jj == N-1:
        c = cCut;
    else:
        c = cMark;
    DrawBottomRight(a,mx+jj*8*a,my+ii*8*a,c);

ii = N-1;
for jj in range(0,N):
    c = cCut;
    DrawBottomRight(a,mx+jj*8*a,my+ii*8*a,c);
    DrawBottomLeft(a,mx+jj*8*a,my+ii*8*a,c);
    DrawBottom(a,mx+jj*8*a,my+ii*8*a,c);
    if jj != N-1:
        DrawBottom(a,mx+4*a+jj*8*a,my+4*a+(ii-1)*8*a,c);
    if p[ii][2*jj] != p[ii-1][2*jj]:
        c = cCut;
    else:
        c = cMark;
    DrawTop(a,mx+jj*8*a,my+ii*8*a,c);

    if jj != N-1:
        if p[ii][2*jj+1] != p[ii-1][2*jj+1]:
            c = cCut;
        else:
            c = cMark;
        DrawTop(a,mx+4*a+jj*8*a,my+4*a+(ii-1)*8*a,c);

    if (jj != N-1 and p[ii][2*jj] != p[ii][2*jj-1]) or jj == 0:
        c = cCut;
    else:
        c = cMark;
    DrawTopLeft(a,mx+jj*8*a,my+ii*8*a,c);
    if (jj != N-1 and p[ii][2*jj] != p[ii][2*jj+1]) or jj == N-1:
        c = cCut;
    else:
        c = cMark;
    DrawTopRight(a,mx+jj*8*a,my+ii*8*a,c);

jj = 0;
for ii in range(1,N-1):
    c = cCut;
    DrawTopLeft(a,mx+jj*8*a,my+ii*8*a,c);
    DrawBottomLeft(a,mx+jj*8*a,my+ii*8*a,c);
    if p[ii][2*jj] != p[ii+1][2*jj+1]:
        c = cCut;
    else:
        c = cMark;
    DrawBottomRight(a,mx+jj*8*a,my+ii*8*a,c);

    if p[ii][2*jj] != p[ii][2*jj+1]:
        c = cCut;
    else:
        c = cMark;
    DrawTopRight(a,mx+jj*8*a,my+ii*8*a,c);
    if p[ii][2*jj] != p[ii-1][2*jj]:
        c = cCut;
    else:
        c = cMark;
    DrawTop(a,mx+jj*8*a,my+ii*8*a,c);

jj = N-1;
for ii in range(1,N-1):
    c = cCut;
    DrawTopRight(a,mx+jj*8*a,my+ii*8*a,c);
    DrawBottomRight(a,mx+jj*8*a,my+ii*8*a,c);
    if p[ii][2*jj] != p[ii][2*jj-1]:
        c = cCut;
    else:
        c = cMark;
    DrawTopLeft(a,mx+jj*8*a,my+ii*8*a,c);

    if p[ii][2*jj] != p[ii+1][2*jj-1]:
        c = cCut;
    else:
        c = cMark;
    DrawBottomLeft(a,mx+jj*8*a,my+ii*8*a,c);

    if p[ii][2*jj] != p[ii-1][2*jj]:
        c = cCut;
    else:
        c = cMark;
    DrawTop(a,mx+jj*8*a,my+ii*8*a,c);

    if p[ii][2*jj-1] != p[ii-1][2*jj-1]:
        c = cCut;
    else:
        c = cMark;
    DrawTop(a,mx+4*a+(jj-1)*8*a,my+4*a+(ii-1)*8*a,c);

RoundedRect(0,a/2,2*mx+(N-1)*8*a+7*a,2*(my-a/2)+N*8*a,10,cOuter);

f.write('</svg>');