from graph import *
def draw_window(x,y,w,h):
    """
    x,y - centre of the window
    w,h - whidth and high of the window
    """
    l=w//10
    x1=x-w//2
    y1=y-h//2
    x2=x+w//2
    y2=y+h//2
    penColor(209,236,250)
    brushColor(209,236,250)
    rectangle (x1, y1, x2, y2)
    x1+=l; y1+=l; x2-=l; y2-=l
    penColor(149,209,242)
    brushColor(149,209,242)
    rectangle (x1, y1, x2, y2)
    penColor(209,236,250)
    brushColor(209,236,250)
    x1=x-l//2
    y1=y-h//2
    x2=x+l//2
    y2=y+h//2
    rectangle (x1, y1, x2, y2)
    x1=x-w//2
    y1=y-h//2+h//3-l//2
    x2=x+w//2
    y2=y-h//2+h//3+l//2
    rectangle (x1, y1, x2, y2)

def draw_clew(x,y,r):
    """
    x,y - center
    r - size
    """
    penColor(15,46,57)
    brushColor(192,192,192)
    penSize(1)
    circle(x, y, r//2)
    P=[(x, y+r//2),(x-r//2, y+r//2),(x-r//2-4, y+r),(x-r//2-8, y+r-4),(x-r//2-16, y+r-8),\
       (x-r//2-18, y+r-6),(x-r//2-25, y+r-16)]
    polyline(P)

def draw_ear(x, y, w, h):
    brushColor(255,128,64)
    P=[(x, y-5),((x+w*2//3), y-h), (x+w, y),(x, y-5)]
    polygon(P)
    brushColor(255,177,140)
    P=[(x+2, y-5),((x+w*2//3), y-h+2), (x+w-2, y),(x+2, y-5)]
    polygon(P)

def draw_lear(x, y, w, h):
    brushColor(255,128,64)
    P=[(x, y),((x+w//3), y-h), (x+w, y-5),(x, y)]
    polygon(P)
    brushColor(255,177,140)
    P=[(x+2, y),((x+w//3), y-h+2), (x+w-2, y-5),(x+2, y)]
    polygon(P)

def draw_noise(x, y, w, h):
    brushColor(255,177,140)
    P=[(x, y),(x+w//2, y+h), (x+w, y),(x, y)]
    polygon(P)
    line (x+w//2, y+h, x+w//2, y+h+4)
    P=[(x+w//2, y+h+4),(x+w//2+2, y+h+6), (x+w//2+4, y+h+8), (x+w//2+6, y+h+8), (x+w//2+8, y+h+6),(x+w//2+10, y+h+4)]
    polyline(P)
    P=[(x+w//2, y+h+4),(x+w//2-2, y+h+6), (x+w//2-4, y+h+8), (x+w//2-6, y+h+8), (x+w//2-8, y+h+6),(x+w//2-10, y+h+4)]
    polyline(P)
    

def draw_eye(x, y, r):
    brushColor(38,152,14)
    circle(x, y, r)
    brushColor(0, 0, 0)
    oval(x+1, y, r/10, r-1)
    brushColor(255,255,255)
    oval(x-r//10, y-r//10, r/10,r//3)
    
penColor(128,64,00)
penSize(1)
# wall
brushColor(74,74,00)
x1 = 70; y1 = 0
x2 = 430; y2 = 250
rectangle (x1, y1, x2, y2)
#window
x = 350; y = 110; w = 130; h=200
draw_window(x, y, w, h)
#floor
penColor(123,123,00)
brushColor(123,123,00)
x1 = 70; y1 = 250
x2 = 430; y2 = 600
rectangle (x1, y1, x2, y2)
#clew
draw_clew(200,460,30)
draw_clew(360,420,20)
#cat
#penColor(255,84,2)
brushColor(255,128,64)
oval(220, 380, 102,57)
oval(105, 397, 13,30)
#circle(120, 390, 42)
oval(395, 370, 80, 15)

oval(120, 380, 44, 42)
oval(145, 430, 30, 15)
circle(295, 412, 32)
oval(320, 455, 13,30)
#arc(350, 350, 70, 30, 270)

brushColor(38,152,14)
draw_lear(90,355,20,25)
draw_ear(130,355,20,25)
draw_eye(100, 375, 10)
draw_eye(138, 375, 10)
draw_noise(115,388,10,10)
run()
