x=100
y=100
kx=150
ky=150
bx=0
by=0
def setup():
    global x,y,bx,by,kx,ky
    size(600,600)
def draw():
    global  x,y,bx,by,ky,kx
    fill(60,310,100)
    rect(0,0,600,600)
    fill(40,100,20)
    ellipse(x,y,15,15)
    fill(80,40,50)
    rect(kx,ky,50,50)
    x-=bx
    y-=by
    if keyPressed:    
        if key == "w":    
            bx=0
            by=1
        if key == "s":
            bx=0
            by=-1
        if key == "a":
            bx=1
            by=0                         
        if key == "d":
            bx=-1
            by=0
    if x<=5:
        bx=-bx
    if y>=5:
        by=-by
    if y<=595:
        by=-by
    if x>=595:
        bx=-bx
    if x>=kx and y>=ky and x<=kx and y<=ky:
      bx=-bx
      by=-by
