# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 01:20:40 2021

@author: ruben
"""

import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

def saludo(nombre):
    print("Holi", nombre)

etiqueta = tk.Label(ventana, text = "Número más probable \nTablas - Calculo \nPara tubos de 10 mL, 1 mL y 0.1 mL (3 tubos cada uno)\n", bg = "#faf0e6")
etiqueta.pack(side = tk.TOP, fill=tk.X)

boton1 = tk.Button(ventana, text = "Presiona", padx = 10, pady = 5, command = lambda: saludo("Python"))
boton1.pack()

cajaTexto = tk.Entry(ventana, font="Times 20")
cajaTexto.pack()


def textoDeCaja():
    texto1 = cajaTexto.get()
    etiqueta2["text"] = texto1
    
botonC = tk.Button(ventana, text="click", command = textoDeCaja)
botonC.pack()


# Etqueta a mostrar
etiqueta2 = tk.Label(ventana)
etiqueta2.pack()


# Posición más específica

#boton2 = tk.Button(ventana, text = "B1")
#boton3 = tk.Button(ventana, text = "B2")
#boton4 = tk.Button(ventana, text = "B3")

#boton2.grid(row = 3, column = 2)

ventana.mainloop()