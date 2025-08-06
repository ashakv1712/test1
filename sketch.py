from p5 import *

def setup():
  global fish1, fish2, fish3
  createCanvas(windowWidth,windowHeight)
  drawTickAxes()
  fish1 = create_fish(300,20)
  fish2 = create_fish(200,17)
  fish3 = create_fish(100,15)

def draw():
  background(57,3,252)
  fill("yellow")
  rect(0,0,windowWidth,200)
  draw_fish(fish1)
  draw_fish(fish2)
  draw_fish(fish3)
  coral_moving()
  
def create_fish(y, size):
  
  fish = {
    "size" : size,
    "speed" : 1,
    "y" : y,
    "x" : random(300,500)
    }
  return fish 

def draw_fish(fish):

    textSize(fish["size"])
    text("🐠",fish["x"],fish["y"])

    fish["x"] -= fish["speed"]

#fish moves horzonatly acorss a screen

    if fish["x"] < 0:
      fish["x"] = random(300,500)

def coral_moving():
#use a dictionnary 
  Coral = {
    "color" : "pink",
    "length" : 300,
    "width" : 5,
     "x" : 10,  
     "y" : 100
  }

  noStroke()
  fill(Coral["color"])
  

  for i in range(10):
    rect(i * Coral["x"],Coral["y"],Coral["width"],Coral["length"])
   


def crab_moving(x):
#use for loop??
  
  x = 230 
  x = x+1
  text("🦀", x, 250)

  #for x in range:
    
