import tkinter 

okno = tkinter.Tk()
okno.wm_title("MojKalkulator")

#številčnica

def ena():
    return 1
gumb1 = tkinter.Button(okno, text="1",command = ena)
gumb1.pack()

def dva():
    return 2
gumb2 = tkinter.Button(okno, text="2",command = dva)
gumb2.pack()

def tri():
    return 3
gumb3 = tkinter.Button(okno, text="3",command = tri)
gumb3.pack()

def stiri():
    return 4
gumb4 = tkinter.Button(okno, text="4",command = stiri)
gumb4.pack()

def pet():
    return 5
gumb5 = tkinter.Button(okno, text="5",command = pet)
gumb5.pack()

def sest():
    return 6
gumb6 = tkinter.Button(okno, text="6",command = sest)
gumb6.pack()

def sedem():
    return 7
gumb7 = tkinter.Button(okno, text="7",command = sedem)
gumb7.pack()

def osem():
    return 8
gumb8 = tkinter.Button(okno, text="8",command = osem)
gumb8.pack()

def devet():
    return 9
gumb9 = tkinter.Button(okno, text="9",command = devet)
gumb9.pack()

def nic():
    return 0
gumb0 = tkinter.Button(okno, text="0",command = nic)
gumb0.pack()








