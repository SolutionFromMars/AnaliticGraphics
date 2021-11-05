from tkinter import *
from random import *
from math import *

wnd=Tk()
wnd.title('Рисование графиков')
H=800
W=1200
canvas=Canvas(wnd, width=W, height=H, bg='Black')
Thickness=1
ThickP=6
LineColor='White'
Number=20
Indent=25
X1=Y1=X2=Y2=0
Max=50
Data=[0]*Number
label=Label(wnd, fg='White', bg='Black')
Sum=0

def AdaptX(numeric=100): return abs((W-Indent*2)/Number*numeric+(W-Indent*2)/Number)
def AdaptY(numeric=100): return abs((H-Indent*2)/Number*numeric+(H-Indent*2)/Number)
def DrawPoint(X=100, Y=100): canvas.create_oval(Indent+X-(ThickP/2), H-Indent-Y+(ThickP/2), Indent+X+(ThickP/2), H-Indent-Y-(ThickP/2), outline="Red", fill="Red", width=Thickness)
def DrawLine(x1=0,y1=0,x2=100,y2=100): canvas.create_line(Indent+x1, H-Indent-y1, Indent+x2, H-Indent-y2, fill ='Green', width=Thickness)
def Change(count): return (H-Indent)/(Max+1)*count

canvas.create_line(Indent, H-Indent, Indent, Indent, width=Thickness, arrow=LAST, fill = LineColor)
canvas.create_line(Indent, H-Indent, W-Indent, H-Indent, width=Thickness, arrow=LAST, fill = LineColor) 
label.pack()
label.place(relx=.02, rely=.965)

for u in range(len(Data)):
    Data[u]=randint(0, Max)
    X1=AdaptX(u); Y1=Change(Data[u]); DrawLine(X1, Y1, X2, Y2); X2=X1; Y2=Y1
    label.config(text=Data[u])
  
for u in range(len(Data)): DrawPoint(AdaptX(u), Change(Data[u]))

for u in range(len(Data)): Sum += Data[u]

label.config(text=str(round((Sum/len(Data))/Max*100, 2))+'%')

canvas.pack(fill=BOTH, expand=True)
wnd.mainloop()