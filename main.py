from tkinter import Tk, Button, Entry
import tkinter as tk

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x300")

pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=160, padx=1, pady=0)


def mensaje(Evento):
    boton = Evento.widget
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, actual + boton['text']) 

def mensaje2(Evento):
    actual = pantalla.get()
    resultado = eval(actual)
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, resultado) 

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=0)
boton_1.bind("<Button-1>",mensaje)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.bind("<Button-1>",mensaje)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.bind("<Button-1>",mensaje)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.bind("<Button-1>",mensaje)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.bind("<Button-1>",mensaje)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.bind("<Button-1>",mensaje)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.bind("<Button-1>",mensaje)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.bind("<Button-1>",mensaje)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.bind("<Button-1>",mensaje)


boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_igual.bind("<Button-1>",mensaje2)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_punto.bind("<Button-1>",mensaje)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=2, column=3, padx=1, pady=1)
boton_mas.bind("<Button-1>",mensaje)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=1, column=3, padx=1, pady=1)
boton_menos.bind("<Button-1>",mensaje)

boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind("<Button-1>",mensaje)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.bind("<Button-1>",mensaje)



root.mainloop()