from tkinter import *
import time

class Ball:
    def __init__(self , color , canvas , paddle):
        self.canvas = canvas 
        self.paddle = paddle
        self.boll = canvas.create_oval(15 , 15, 30 , 30, fill=color)
        self.canvas.move(self.boll , 250 , 120)
        self.x = 0
        self.y = -1
        
        


root = Tk()
root.title("Game_ball")
canvas = Canvas(root , width=600 , height=550 , bd = 0)
canvas.pack()
root.update()
paddle = Paddle(canvas , 'red')
ball = Ball('yellow' , canvas , paddle)



root.mainloop