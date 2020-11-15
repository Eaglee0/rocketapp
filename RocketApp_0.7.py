#Rocket App 1.6 programma per calcolare dati per il razzo modellismo
import tkinter as graf
import time
from math import *

# def delete():
#     n =  0
#     for widget in pagina2.winfo_children():
#         widget.destroy()
#     n += 1
#
#     pagina2 = graf.Tk()
#     pagina2.geometry('770x450')
#     pagina2.title('dimensioni paracadute')
#     n1_p = graf.DoubleVar()
#     n2_p = graf.DoubleVar()
#     n1_box = graf.Entry(pagina2, textvariable = n1_p).pack()
#     but1_p = graf.Button(pagina2, text = 45'esegui', command = delete).pack()
#     n2_label = graf.Label(pagina2, textvariable = n2_p).pack()
#     pagina2.mainloop()

def par():
    pes = n1_p.get()
    di = (sqrt(pes/100))*100
    n2_p.set(di)#funzione per calcolare il diametro del paracadute
def alt():
    te = (n1_p.get()/2)
    altezza = ((9.81*(te**2))/2)
    n2_p.set(altezza)
    print(str(te))#funzione per calcolare l'altezza del volo
def altapo():
    te = n1_p.get()
    altezza = ((9.81*(te**2))/2)
    n2_p.set(altezza)
    print(str(te))#funzione per calcolare l'altezza del volo
def entry1():
    n2_box = graf.Entry(pagina, textvariable = n4_p).grid(row=7,column=2)
    but3_p = graf.Button(pagina, text = 'altezza con tempo di volo di salita', command = altapo).grid(row=8,column=2)#funzione per calcolare l'altezza "più precisa"







if __name__ == '__main__':

    print('dimensoni paracadute')
    pagina = graf.Tk()#si iniziallizza la pagina
    pagina.geometry('350x450')
    pagina.title('RocketApp')
    rows = 0
    while rows < 20:#si iniziallizzano le righe ella pagina
        pagina.rowconfigure(rows, weight=1)
        pagina.columnconfigure(rows,weight=1)
        rows += 1
    n1_p = graf.DoubleVar()#si creano le variabili
    n2_p = graf.DoubleVar()
    n4_p = graf.DoubleVar()
    but3_p = graf.Button(pagina, text = 'altezza con tempo di volo di salita', command = altapo).pack_forget()
    n2_box = graf.Entry(pagina, textvariable = n4_p).pack_forget()
    label_testo = graf.Label(pagina, font = ('Helvetica',9),text = '''inserisci il peso del razzo e clicca su calcola
    il dimaetro per calcolare il dimaetro del paracadute,
     oppure inserisci il tempo di volo e clicca su calcola
    l'altezza per calcolare l'altezza a cui è arrivato il tuo razzo''').grid(row=1,column=2)
    n1_box = graf.Entry(pagina, textvariable = n1_p).grid(row=2,column=2)#si crea il contenitore per l'unput
    but1_p = graf.Button(pagina, text = 'calcola il diametro del paracadute', command = par).grid(row=3,column=2)#si crea il bottone per il calcolo
    but2_p = graf.Button(pagina, text = 'altezza con tempo di volo intero', command = alt).grid(row=4,column=2)
    but3_p = graf.Button(pagina, text = 'altezza con tempo di volo di salita', command = altapo).grid(row=5,column=2)
    n2_label = graf.Label(pagina, textvariable = n2_p).grid(row=6,column=2)
    pagina.mainloop()
