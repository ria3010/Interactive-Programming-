# template for "Stopwatch: The Game"
import simplegui
# define global variables
total_ticks = 0
var = False
x=0
y=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if(t == 0):
        return "0:00.0"
    elif(t <= 599):
        z = t/10
        if(z<10):
            return "0:0" +str(t/10)+"."+str(t%10)
        else:
            return "0:" +str(t/10)+"."+str(t%10)
    else:
        m = t%600
        n= m/10
        if(n<10):
            return str(t/600)+":"+'0'+str(m/10)+'.'+str(m%10)
        else:
            return str(t/600)+":" + str(m/10)+'.'+str(m%10)

def reflexes():
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global total_ticks,var
    var = False
    timer.start()

def stop_handler():
    global total_ticks,y,var,x
    if(var==False):
        var = True
        timer.stop()
        y += 1 
    #TODO
    #if(total_ticks is integer):
        #x += 1
    if total_ticks % 10 == 0 and total_ticks != 0 :
            x += 1
            y += 1    
       
    
def reset_handler():
    global total_ticks,var,y
    var = False
    y = 0
    total_ticks = 0
# define event handler for timer with 0.1 sec interval
def tick():
    global total_ticks
    total_ticks += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(total_ticks),[180,250],50,"Red")
    canvas.draw_text(str(x)+"/"+str(y),[300,200],50,"White")
    
# create frame
frame = simplegui.create_frame("Timer Frame",500,500)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)
frame.add_button("Start",start_handler,50)
frame.add_button("Stop",stop_handler,50)
frame.add_button("Reset",reset_handler,50)



# start frame
frame.start()
timer.start()

