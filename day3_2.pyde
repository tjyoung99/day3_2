def setup():
    size(600,600)

def draw():
    background(255)
    fill(0,0,0)
    rect(200,0,200,600)
    fill(0,0,0)
    ellipse(300,100,200,200)
    ellipse(300,300,200,200)
    ellipse(300,500,200,200)
    if mouseY>100 and mouseY<300:
        fill(250,0,0)
    ellipse(300,100,200,200)
    if mouseY>300 and mouseY<500:
        fill (255,255,0)
    ellipse(300,300,200,200)
    if mouseY>500 and mouseY<600:
        fill (0,255,0)
    ellipse(300,500,200,200)
