question 7
#http://www.codeskulptor.org/#user41_hABZTCVXOY_0.py
import simplegui
import random

point = [10,20]
change = [3,0.7]

def draw(canvas):
 #   canvas.draw_line([50,50],[180,50],5,"Red")
  #  canvas.draw_line([50,50],[50,140],5,"Red")
 #   canvas.draw_line([180,50],[180,140],5,"Red")
 #   canvas.draw_line([50,140],[180,140],5,"Red")
  canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], 1, 'Yellow', 'Orange')
    
    
def keydown(key):
    global point
    if key == simplegui.KEY_MAP['up']:
        point[0] += change[0]
        point[1] += change[1]
    collision()
  

def collision():
    global point
    if ((50 < point[0]<180) and 
       (50<point[1]<140)):
        print "collision"
 #   else:
 #       print "NO"
 #       print point
    
    
frame = simplegui.create_frame("testing",200,200)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

collision()
frame.start()



#queston 9
#http://www.codeskulptor.org/#user41_hABZTCVXOY_1.py
import simplegui

number = 5
width = 400
height = 400

def draw(canvas):
    global number
    canvas.draw_text(str(number),[width/2,height/2],20,"Red")
    
   
def keydown(key):
    global number
    if key == simplegui.KEY_MAP['up']:
        number = number*2
        
def keyup(key):
    global number 
    if key == simplegui.KEY_MAP['up']:
        number -= 3
        
frame = simplegui.create_frame("testing",width,height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
        
