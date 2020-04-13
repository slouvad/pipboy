from tkinter import *
root = Tk()
root.title("")
root.geometry("900x600+300+1000")
root.resizable(False,False)
#Настройка
canvas = Canvas(root,width=1020,height=620,bg="#002")
canvas.pack()
#Настройка цвета и поля. Вывод  
root.mainloop()

btn_2 = Batton(root,text="Ukroini")
