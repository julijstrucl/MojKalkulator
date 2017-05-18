import tkinter 

okno = tkinter.Tk()
okno.wm_title("MojKalkulator")

#-------------------------okvir0-----------------------------------
#ekran => okvir0

okvir0 = tkinter.Frame(okno)
okvir0.pack()
ekran = tkinter.Entry(okvir0)
ekran.pack()
ekran.insert(0,'')

#-------------------------okvir1-----------------------------------
#številčnica => okvir1
okvir1 = tkinter.Frame(okno)
okvir1.pack()

def ena():
    return ekran.insert('end', 1)
gumb1 = tkinter.Button(okvir1, text="1",command = ena,
                       height=2, width=3, bg='sky blue')
gumb1.grid(row=0,column=0)

def dva():
    return ekran.insert('end', 2)
gumb2 = tkinter.Button(okvir1, text="2",command = dva,
                       height=2, width=3, bg='sky blue')
gumb2.grid(row=0,column=1)

def tri():
    return ekran.insert('end', 3)
gumb3 = tkinter.Button(okvir1, text="3",command = tri,
                       height=2, width=3, bg='sky blue')
gumb3.grid(row=0,column=2)

def stiri():
    return ekran.insert('end', 4)
gumb4 = tkinter.Button(okvir1, text="4",command = stiri,
                       height=2, width=3, bg='sky blue')
gumb4.grid(row=1,column=0)

def pet():
    return ekran.insert('end', 5)
gumb5 = tkinter.Button(okvir1, text="5",command = pet,
                       height=2, width=3, bg='sky blue')
gumb5.grid(row=1,column=1)

def sest():
    return ekran.insert('end', 6)
gumb6 = tkinter.Button(okvir1, text="6",command = sest,
                       height=2, width=3, bg='sky blue')
gumb6.grid(row=1,column=2)

def sedem():
    return ekran.insert('end', 7)
gumb7 = tkinter.Button(okvir1, text="7",command = sedem,
                       height=2, width=3, bg='sky blue')
gumb7.grid(row=2,column=0)

def osem():
    return ekran.insert('end', 8)
gumb8 = tkinter.Button(okvir1, text="8",command = osem,
                       height=2, width=3, bg='sky blue')
gumb8.grid(row=2,column=1)

def devet():
    return ekran.insert('end', 9)
gumb9 = tkinter.Button(okvir1, text="9",command = devet,
                       height=2, width=3, bg='sky blue')
gumb9.grid(row=2,column=2)

def nic():
    return ekran.insert('end', 0)
gumb0 = tkinter.Button(okvir1, text="0",command = nic,
                       height=2, width=3, bg='sky blue')
gumb0.grid(row=3,column=1)

#naključno število
import random
def nakljucno():
    ekran.insert('end', random.randrange(1,1000))
gumb_nakljucno = tkinter.Button(okvir1, text="?",command = nakljucno,
                       height=2, width=3, bg='sky blue')
gumb_nakljucno.grid(row=3,column=2)

# decimalna vejica
def vejica():
    ekran.insert('end','.')
gumb_vejica = tkinter.Button(okvir1, text=",",command = vejica,
                       height=2, width=3, bg='sky blue')
gumb_vejica.grid(row=3,column=0)


# funkcije
def fakulteta():
    ekran.insert('end', 'math.factorial()')

gumb_fakulteta = tkinter.Button(okvir1, text="n!", command = fakulteta,
                               height=2, width=3, bg='chartreuse')
gumb_fakulteta.grid(row=0, column=3)


import math
def koren():
    ekran.insert('end', '**(0.5)')

gumb_koren = tkinter.Button(okvir1, text="√", command = koren,
                            height=2, width=3, bg='chartreuse')
gumb_koren.grid(row=1, column=3)

def kvadrat():
    ekran.insert('end', '**2')
    
gumb_kvadrat = tkinter.Button(okvir1, text="nn", command = kvadrat,
                              height=2, width=3, bg='chartreuse')
gumb_kvadrat.grid(row=2, column=3)

#splošne funkcije
def sestevanje():
    ekran.insert('end','+')
    sporocilo.set("A prvič uporabljaš kalkulator?")

gumb_sestevanje = tkinter.Button(okvir1, text="+", command = sestevanje,
                                height=2, width=3, bg='chartreuse')
gumb_sestevanje.grid(row=0, column=5)
            
def odstevanje():
    ekran.insert('end','-')
gumb_odstevanje = tkinter.Button(okvir1, text="-", command = odstevanje,
                                height=2, width=3, bg='chartreuse')
gumb_odstevanje.grid(row=1, column=5)

def mnozenje():
    ekran.insert('end','*')
gumb_mnozenje = tkinter.Button(okvir1, text="x", command = mnozenje,
                                height=2, width=3, bg='chartreuse')
gumb_mnozenje.grid(row=2, column=5)

def deljenje():
    ekran.insert('end','/')
    
gumb_deljenje = tkinter.Button(okvir1, text="/", command = deljenje,
                                height=2, width=3, bg='chartreuse')
gumb_deljenje.grid(row=3, column=5)


#pojavno okno z informacijami (okvir1)
from tkinter import messagebox
def info():
    messagebox.showinfo("Nekaj informacij", "'R' - resetira okno. Gumb '?' vam dodeli naključno število med 1 in 1000")
gumb_info = tkinter.Button(okvir1, text="i",command = info,
                           height=2, width=3, bg='gold')
gumb_info.grid(row=3,column=3)

#---------------------------------okvir2--------------------------------
#rezultat in reset => okvir2
okvir2 = tkinter.Frame(okno)
okvir2.pack()

def rezultat():
    try:
        t = eval(ekran.get())
        ekran.delete(0,'end')
        ekran.insert(0,t)
        sporocilo.set("Si našel kar si iskal?")
    except ZeroDivisionError:
        ekran.delete(0,'end')
        sporocilo.set("Deljenje z ničlo!")
    except SyntaxError:
        ekran.delete(0,'end')
        sporocilo.set("Pazi na pravilen zapis!")
    except NameError:
        ekran.delete(0,'end')
        sporocilo.set("To ne spada v kalkulator!")

gumb_rezultat = tkinter.Button(okvir2, text="=", command = rezultat,
                               height=2, width=10, cursor="heart", bg='khaki1')
gumb_rezultat.grid(row=0, column=1)

def reset():
    ekran.delete(0, 'end')
    sporocilo.set("Izračunaj še kaj")
gumb_reset = tkinter.Button(okvir2, text="R", command = reset,
                               height=2, width=9, bg='khaki1')
gumb_reset.grid(row=0, column=0)


#-------------------------okvir3-------------------------------
#lable => okvir3
okvir3 = tkinter.Frame(okno)
okvir3.pack()
sporocilo = tkinter.StringVar()
sporocilo.set("Preizkusi me!")
opomba = tkinter.Label(okvir3, textvariable=sporocilo)
opomba.pack()


okno.mainloop()








