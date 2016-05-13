# ping-pong-3000
пинг понг версия лямбда запускаеться через processing версии 2.2.1 и выше
вставить ниже описаный код в processing

x=100
bx=100
by=100
bxs=0
bys=0
ballxs=-2
ballys=2
def setup():
    global x,bx,by
    size(600,400)
    bx=width/2
    by=height/2
def draw():
    global x,bx,by,bxs,bys
    rect(0,0,600,400)
    rect(30,45,550,350)
    rect(0,230,600,0)
    ellipse(bx,by,10,10)
    rect(x,380,100,10)
    if keyPressed:
        if key == "a":
            x=x-1
        if key == "d":
            x=x+1
        if key == "p":
            bxs=2
            bys=2
    if by>=390:
        bxs=0
        bys=0
        bx=width/2
        by=height/2
    bx+=bxs              
    by+=bys
    if bx<=0:
        bxs=-bxs
    if by>=0:
        bys=-bys
    if by<=600:
        bys=-bys
    if bx>=575:
        bxs=-bxs
        что бы запустить игру нажмите p englisch
