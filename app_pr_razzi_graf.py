#app_pr_razzi_graf.py
#old grafic version

import tkinter as graf
def delete():
    for widget in root.winfo_children():
        widget.destroy()


#pagin1 = pagina principale
#(((P/1000)**(1/2))*100)
def pagina2_0():
    if __name__ == '__main__':
        print('dimensoni paracadute')
        pagina2 = graf.Tk()
        pagina2.geometry('770x450')
        pagina2.title('dimensioni paracadute')
        n1_p = graf.DoubleVar()
        n2_p = graf.DoubleVar()
        n1_box = graf.Entry(pagina2, textvariable = n1_p).pack()
        but1_p = graf.Button(root, text = 'esegui', command = par).pack()
        n2_label = graf.Label(pagina2, textvariable = n2_p).pack()
        pagina2.mainloop()


def par():
    n2_p.set(((n1_p.get()/1000)**(1/2))*100)


def pagina20():
    import paracaute_graf
    print('cioa')

rows = 0
while rows < 20:
    finestra.rowconfigure(rows, weight=1)
    finestra.columnconfigure(rows,weight=1)
    rows += 1

if __name__ == '__main__':

    root = graf.Tk()
    root.geometry('770x450')
    root.title('RocketApp')
    n1_p = graf.DoubleVar()
    n2_p = graf.DoubleVar()


    but1 = graf.Button(root, text = 'esegui', command = pagina2_0).grid(row = 3)

    root.mainloop()
