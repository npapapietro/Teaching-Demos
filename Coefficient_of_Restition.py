from __future__ import division
from visual import*
from Tkinter import*

import tkMessageBox
def showsim():
    global e
    Cr =float( e.get() )
    ball1=sphere(pos=vector(10,0,0),radius=1,mass=1,color=color.green)
    ball2=sphere(pos=vector(-10,0,0),radius=1,mass=1,color=color.red)
    v1_i=-1
    v2_i=1
    ball1.velocity = vector(v1_i,0,0)
    ball2.velocity = vector(v2_i,0,0)
    t=0
    dt=0.1
    print(Cr*ball2.mass*(v2_i - v1_i)+ball1.mass*v1_i+ball2.mass*v2_i)/(ball1.mass+ball2.mass)
    while 1:
        rate(100)
        ball1.pos = ball1.pos + ball1.velocity*dt
        ball2.pos = ball2.pos + ball2.velocity*dt
        if t>9:
            ball1.velocity.x=(Cr*ball2.mass*(v2_i-v1_i)+ball1.mass*v1_i+ball2.mass*v2_i)/(ball1.mass+ball2.mass)
            ball2.velocity.x=(-Cr*ball1.mass*(v2_i-v1_i)+ball1.mass*v1_i+ball2.mass*v2_i)/(ball1.mass+ball2.mass)
           # print(ball1.velocity.x)
            t+=dt
        else:
            ball1.velocity = vector(v1_i,0,0)
            ball2.velocity = vector(v2_i,0,0)
            t+=dt
       
    
            
        


root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=showsim)
b.pack(side='bottom')
root.mainloop()

