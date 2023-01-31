from tkinter import *

with open("X:/IV. FG/Point Files/points0.txt",encoding = 'utf-8') as output_file:
    
    
    
    i = output_file.readlines()
    line = i[0]
    line = line.split(' ') 
    
    line2 = i[1]
    line2 = line2.split(' ') 
    
    line3 = i[2]
    line3 = line3.split(' ') 
    
    line4 = i[3]
    line4 = line4.split(' ') 
    

    
    
    x = int(line[0])
    x2 = int(line2[0])
    x3 = int(line3[0])
    x4 = int(line4[0])
    y = int(line[1])
    y2 = int(line2[1])
    y3 = int(line3[1])
    y4 = int(line4[1])
    
    window = Tk()
    canvas = Canvas(window,bg = 'white',width = 700,height = 400)
    canvas.pack()
    
    canvas.create_oval(x-2,y-2,x+2,y+2)
    canvas.create_line(x,y,x2,y2)
    
    canvas.create_oval(x2-2,y2-2,x2+2,y2+2)
    canvas.create_line(x2,y2,x3,y3)
    
    canvas.create_oval(x3-2,y3-2,x3+2,y3+2)
    canvas.create_line(x3,y3,x4,y4)
    canvas.create_oval(x4-2,y4-2,x4+2,y4+2)

    window.mainloop()