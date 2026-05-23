# tkinter
# pip instal tkinter eger calismazsa kullaniacaz
# Gradio,Tkinter (tk),CustomTkinter(ttk),kiwi

import tkinter as tk 
from tkinter import messagebox

# fonksiyonlar
def ad_yazdir():
    isim=kutu.get()  # Entry nin icine kullanicinin yazdigi  metni alir
    messagebox.showinfo("CIKTI",f"hosgeldin {isim}")

window=tk.Tk()
window.title("ilk pencere")
window.geometry("1280x720".format(1280,720))
window.configure(bg="#17AD6C")

etiket=tk.Label(window,text="lutfen adinizi giriiniz",font=None)
etiket.configure(bg="#CE2A48")
etiket.place(x=10,y=20)


kutu=tk.Entry(window,font=None)
kutu.place(x=500,y=400)
buton=tk.Button(window,text="HADI CALIS",font=None,command=ad_yazdir)
buton.place(x=400,y=300)

window.mainloop()
