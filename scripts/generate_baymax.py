"""Generate native 1-bit Baymax sprites; no image libraries required."""
from pathlib import Path
import struct, zlib
ROOT = Path(__file__).resolve().parents[1]
W, H = 68, 140

def frame(blink=False, wave=False):
    # Intended physical appearance: white body on black. The encoded palette below
    # compensates for the inversion observed on the actual right display.
    pixels = [[0] * W for _ in range(H)]
    def ellipse(cx, cy, rx, ry, color):
        for y in range(H):
            for x in range(W):
                if ((x+.5-cx)/rx)**2 + ((y+.5-cy)/ry)**2 <= 1:
                    pixels[y][x] = color
    def polygon(points, color):
        for y in range(H):
            intersections=[]
            for a,b in zip(points, points[1:]+points[:1]):
                if min(a[1],b[1]) <= y+.5 < max(a[1],b[1]):
                    intersections.append(a[0]+(y+.5-a[1])*(b[0]-a[0])/(b[1]-a[1]))
            intersections.sort()
            for left,right in zip(intersections[::2],intersections[1::2]):
                for x in range(W):
                    if left <= x+.5 < right:pixels[y][x]=color
    def path(start, curves, color):
        points=[start];a=start
        for b,c,d in curves:
            for i in range(1,25):
                t=i/24;u=1-t
                points.append((u**3*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t**3*d[0],
                               u**3*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t**3*d[1]))
            a=d
        polygon(points,color)
    def line(points, color=0, width=1):
        for a,b in zip(points,points[1:]):
            dx,dy=b[0]-a[0],b[1]-a[1]; length=dx*dx+dy*dy
            for y in range(H):
                for x in range(W):
                    t=max(0,min(1,((x+.5-a[0])*dx+(y+.5-a[1])*dy)/length)) if length else 0
                    if (x+.5-a[0]-t*dx)**2+(y+.5-a[1]-t*dy)**2 <= (width/2+.15)**2:
                        pixels[y][x]=color
    # Trace the approved concept's contour coordinates, uniformly scaled.
    # Rest reference bounds: x=145..479, y=328..797 (334 x 469).
    # No separate neck: head overlaps the shoulders just as in the reference.
    scale = 62 / 334
    def point(p):return (34+(p[0]-312)*scale, 26+(p[1]-328)*scale)
    raster_path, raster_line, raster_ellipse = path, line, ellipse
    def path(start, curves, color):
        raster_path(point(start), [tuple(point(p) for p in curve) for curve in curves], color)
    def line(points, color=0, width=1):
        raster_line([point(p) for p in points], color, width)
    def ref_ellipse(cx,cy,rx,ry,color):
        x,y=point((cx,cy));raster_ellipse(x,y,rx*scale,ry*scale,color)
    # Feet retain the reference's short, wide shape.
    path((217,701), [((216,756),(221,791),(264,795)),
                        ((293,800),(307,787),(307,775)),((307,747),(308,727),(308,721))],1)
    path((316,721), [((316,747),(317,775),(323,788)),
                        ((336,802),(382,798),(396,770)),((406,748),(407,720),(407,701))],1)
    # Hanging arms and waving hand traced from the matching concept frames.
    path((247,448), [((211,458),(173,512),(156,567)),
                        ((145,594),(144,636),(146,661)),((147,675),(156,686),(169,684)),
                        ((183,684),(190,670),(193,651)),((199,589),(211,536),(225,507)),
                        ((232,480),(241,459),(247,448))],1)
    if wave:
        # Restore the earlier compact, rounded raised arm in native coordinates.
        raster_path((47,54), [((52,56),(52,67),(54,72)),((61,77),(66,65),(64,55)),
                              ((64,51),(65,47),(64,44)),((63,41),(62,41),(61,44)),
                              ((60,39),(58,39),(58,43)),((56,40),(54,40),(55,46)),
                              ((52,43),(51,45),(54,50)),((54,57),(50,60),(47,54))],1)
        raster_line([(55,51),(58,54),(61,51)],0,1)
    else:
        path((377,448), [((413,458),(451,512),(468,567)),
                            ((479,594),(480,636),(478,661)),((477,675),(468,686),(455,684)),
                            ((441,684),(434,670),(431,651)),((425,589),(413,536),(399,507)),
                            ((392,480),(383,459),(377,448))],1)
    # Broad belly: nearly vertical sides flare below the shoulders, then round inward.
    path((250,448), [((226,460),(214,482),(210,518)),
                        ((197,556),(184,610),(184,657)),((188,700),(244,734),(301,736)),
                        ((344,740),(408,705),(433,665)),((439,627),(423,560),(408,518)),
                        ((402,484),(390,462),(374,448)),((346,438),(279,438),(250,448))],1)
    line([(223,505),(220,542),(207,587),(196,626),(192,660)],0,1)
    line([(402,505),(405,542),(418,587),(429,626),(432,660)],0,1)
    line([(185,662),(207,690),(241,716),(276,733),(308,737),
          (344,733),(379,716),(411,690),(434,662)],0,1)
    # Head sits directly on the shoulders, with a broad flat top and oval cheeks.
    path((272,332), [((247,336),(220,361),(219,386)),
                        ((216,417),(230,444),(272,459)),((295,462),(328,462),(350,459)),
                        ((391,445),(407,420),(404,386)),((403,362),(377,337),(350,332)),
                        ((329,330),(293,330),(272,332))],1)
    line([(229,437),(248,452),(272,460),(350,460),(375,451),(394,436)],0,1)
    line([(263,400),(357,400)],0,1)
    if blink:
        line([(250,400),(277,400)],0,2);line([(344,400),(371,400)],0,2)
    else:
        ref_ellipse(263,397,13,13,0);ref_ellipse(357,397,13,13,0)
    ref_ellipse(363,510,19,19,0);ref_ellipse(363,510,13,13,1)
    line([(345,510),(381,510)],0,1)
    # Detail strokes can cut tiny detached slivers off the filled contour.
    # Remove only 1-3 pixel islands; preserve the head, feet and badge interiors.
    seen=set()
    for y in range(H):
        for x in range(W):
            if not pixels[y][x] or (x,y) in seen:continue
            pending=[(x,y)];seen.add((x,y));island=[]
            while pending:
                a,b=pending.pop();island.append((a,b))
                for c,d in ((a-1,b),(a+1,b),(a,b-1),(a,b+1)):
                    if 0<=c<W and 0<=d<H and pixels[d][c] and (c,d) not in seen:
                        seen.add((c,d));pending.append((c,d))
            if len(island)<=3:
                for a,b in island:pixels[b][a]=0
    return pixels

frames=[frame(),frame(blink=True),frame(wave=True)]
# LVGL native panel is landscape; rotate artwork clockwise, like the status canvas.
lines=['/* Generated by scripts/generate_baymax.py. */', '#include <lvgl.h>']
for name, pixels in zip(('rest','blink','wave'), frames):
    data=[]
    for y in range(W):
        row=[pixels[H-1-x][y] for x in range(H)]
        for x in range(0,H,8):
            data.append(sum((row[x+i] if x+i < H else 0) << (7-i) for i in range(8)))
    lines += [f'static const uint8_t baymax_{name}_map[] = {{',
              '255,255,255,255, 0,0,0,255,']
    lines += [','.join(map(str,data[i:i+18]))+',' for i in range(0,len(data),18)]
    lines += ['};',f'const lv_img_dsc_t baymax_{name} = {{',
              '.header.cf=LV_IMG_CF_INDEXED_1BIT, .header.always_zero=0,',
              f'.header.w={H}, .header.h={W}, .data_size=sizeof(baymax_{name}_map),',
              f'.data=baymax_{name}_map', '};']
(ROOT/'boards/shields/nice_view_baymax/widgets/baymax.c').write_text('\n'.join(lines)+'\n')
# Enlarged exact-pixel geometry preview in intended physical display colours.
scale=4; width=W*3*scale; height=H*scale
raw=bytearray()
for y in range(height):
    raw.append(0)
    for pixels in frames:
        for value in pixels[y//scale]:raw.extend(bytes([255*value])*scale)
def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',width,height,8,0,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')
(ROOT/'docs/baymax-preview.png').write_bytes(png)
