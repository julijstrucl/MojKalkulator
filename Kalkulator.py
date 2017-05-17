import tkinter 

okno = tkinter.Tk()
okno.wm_title("MojKalkulator")
#ekran => okvir0

okvir0 = tkinter.Frame(okno)
okvir0.pack()

ekran = tkinter.Entry(okvir0)
ekran.pack()
ekran.insert(0,'')


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

# funkcije
def fakulteta(n):
    if n%2==0 or n%2==1:
        if n==0:
            return 1
        m=1
        for i in range(n+1):
            m = m*i
        return m + stanje

gumb_fakulteta = tkinter.Button(okvir1, text="n!", command = fakulteta,
                               height=2, width=3, bg='chartreuse')
gumb_fakulteta.grid(row=0, column=4)


import math
def koren(n):
    if n>=0:
        return math.sqrt(n) + stanje 

gumb_koren = tkinter.Button(okvir1, text="√", command = koren,
                            height=2, width=3, bg='chartreuse')
gumb_koren.grid(row=1, column=4)

def kvadrat(n):
    return n**2 + stanje

gumb_kvadrat = tkinter.Button(okvir1, text="nn", command = kvadrat,
                              height=2, width=3, bg='chartreuse')
gumb_kvadrat.grid(row=2, column=4)

#splošne funkcije
def sestevanje():
    sporocilo.set("A prvič uporabljaš kalkulator?")
gumb_sestevanje = tkinter.Button(okvir1, text="+", command = sestevanje,
                                height=2, width=3, bg='chartreuse')
gumb_sestevanje.grid(row=0, column=5)
            
def odstevanje(n):
    return stanje - n
gumb_odstevanje = tkinter.Button(okvir1, text="-", command = odstevanje,
                                height=2, width=3, bg='chartreuse')
gumb_odstevanje.grid(row=1, column=5)

def mnozenje(n):
    return stanje * n
gumb_mnozenje = tkinter.Button(okvir1, text="x", command = mnozenje,
                                height=2, width=3, bg='chartreuse')
gumb_mnozenje.grid(row=2, column=5)

def deljenje(n):
    if n!=0:
        return stanje / n
gumb_deljenje = tkinter.Button(okvir1, text="/", command = deljenje,
                                height=2, width=3, bg='chartreuse')
gumb_deljenje.grid(row=3, column=5)

#rezultat in reset => okvir2
okvir2 = tkinter.Frame(okno)
okvir2.pack()
def rezultat():
    return stanje
gumb_rezultat = tkinter.Button(okvir2, text="=", command = rezultat,
                               height=2, width=10, cursor="heart", bg='khaki1')
gumb_rezultat.grid(row=0, column=1)

def reset():
    ekran.delete(0, 'end')
    sporocilo.set("Izračunaj še kaj")
gumb_reset = tkinter.Button(okvir2, text="R", command = reset,
                               height=2, width=9, bg='khaki1')
gumb_reset.grid(row=0, column=0)



#lable => okvir3
okvir3 = tkinter.Frame(okno)
okvir3.pack()
sporocilo = tkinter.StringVar()
sporocilo.set("Preizkusi me!")
opomba = tkinter.Label(okvir3, textvariable=sporocilo)
opomba.pack()






# ali za ekran uporabiti ENTRY ali Lable?? In kako uvesti računske funkcije
# v entry???
okno.mainloop()








