import tkinter 

okno = tkinter.Tk()
okno.wm_title("MojKalkulator")

#številčnica
stanje = 0

def ena():
    return 1
gumb1 = tkinter.Button(okno, text="1",command = ena, height=2, width=3)
gumb1.grid(row=0,column=0)

def dva():
    return 2
gumb2 = tkinter.Button(okno, text="2",command = dva, height=2, width=3)
gumb2.grid(row=0,column=1)

def tri():
    return 3
gumb3 = tkinter.Button(okno, text="3",command = tri, height=2, width=3)
gumb3.grid(row=0,column=2)

def stiri():
    return 4
gumb4 = tkinter.Button(okno, text="4",command = stiri, height=2, width=3)
gumb4.grid(row=1,column=0)

def pet():
    return 5
gumb5 = tkinter.Button(okno, text="5",command = pet, height=2, width=3)
gumb5.grid(row=1,column=1)

def sest():
    return 6
gumb6 = tkinter.Button(okno, text="6",command = sest,height=2, width=3 )
gumb6.grid(row=1,column=2)

def sedem():
    return 7
gumb7 = tkinter.Button(okno, text="7",command = sedem, height=2, width=3)
gumb7.grid(row=2,column=0)

def osem():
    return 8
gumb8 = tkinter.Button(okno, text="8",command = osem, height=2, width=3)
gumb8.grid(row=2,column=1)

def devet():
    return 9
gumb9 = tkinter.Button(okno, text="9",command = devet,height=2, width=3 )
gumb9.grid(row=2,column=2)

def nic():
    return 0
gumb0 = tkinter.Button(okno, text="0",command = nic,height=2, width=3)
gumb0.grid(row=3,column=1)

# funkcije
def fakulteta(n):
    if n%2==0 or n%2==1:
        if n==0:
            return 1
        m=1
        for i in range(n+1):
            m = m*i
        return m

gumbfakulteta = tkinter.Button(okno, text="n!", command = fakulteta, height=2, width=3)
gumbfakulteta.grid(row=0, column=4)


import math
def koren(n):
    if n>=0:
        return math.sqrt(n)

gumbkoren = tkinter.Button(okno, text="√", command = koren, height=2, width=3)
gumbkoren.grid(row=1, column=4)

def sestevanje(n):
    return stanje + n
            
    

okno.mainloop()








