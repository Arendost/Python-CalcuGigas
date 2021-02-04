from tkinter import *
from tkinter import messagebox

root=Tk()

root.title("CalcuMegas")
root.geometry("500x175")
root.config(bg="White")

numeroPantalla=StringVar()
numeroPantalla2=StringVar()
numeroPantalla3=StringVar()
peracion=""
resultado=0


frame=Frame(root)
frame.pack()


def suma(num):
    global operacion
    global resultado
    resultado=int(num)
    numeroPantalla.set(resultado)


def el_resultado():
    global resultado
    numeroPantalla3.set((int(numeroPantalla.get())*int(numeroPantalla2.get()))/1024)
    print(numeroPantalla3)
    resultado=0


pantalla = Entry(frame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#03f943",justify="right")
l=Label(frame,text="Costo del Giga en Bolivares:",fg="white",font=("Comid Sans MS", 10),bg="#00AB9A" )
l.grid(row=1,column=0)


pantalla2 = Entry(frame,textvariable=numeroPantalla2)
pantalla2.grid(row=2,column=1,padx=10,pady=10,columnspan=4)
pantalla2.config(background="black",fg="#03f943",justify="right")
l1=Label(frame,text="Cantidad de Megas que vas a gastar:",fg="white",font=("Comid Sans MS", 10),bg="#00AB9A" )
l1.grid(row=2,column=0)


pantalla3 = Entry(frame,textvariable=numeroPantalla3)
pantalla3.grid(row=3,column=1,padx=10,pady=10,columnspan=4)
pantalla3.config(background="black",fg="#03f943",justify="right")
l1=Label(frame,text="Precio de los megas:",fg="white",font=("Comid Sans MS", 10),bg="#00AB9A" )
l1.grid(row=3,column=0)


Buttonsum=Button(frame,text="Calcular",width=4,command=lambda:el_resultado())
Buttonsum.grid(row=4,column=2)



root.mainloop()
