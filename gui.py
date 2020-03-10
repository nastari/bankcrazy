import tkinter as tk
from PIL import Image, ImageTk


HEIGHT = 500
WIDTH = 600
INDEX_IMAGE = 'caixa.png'

root = tk.Tk()
root.title('Bank of Crazy')


#INDEX FRAME 
canvas = tk.Canvas(root,height= HEIGHT, width = WIDTH, bg='#BDB6F0')
canvas.pack()


#INDEX SUBFRAME

frameAcess = tk.Frame(root, bg='#5544C0')
frameAcess.place(relx = 0.03, rely= 0.03, relwidth = 0.94 ,relheight= 0.94)

# INDEX LABEL
labelAcess = tk.Label(frameAcess,text='Welcome to Bank of Crazy!', bg= '#9124C0', font=("Helvetica", 30))
labelAcess.pack(fill = 'both')



# FRAME OPTIONS INDEX PAGE 

centerOptionsFrame = tk.Frame(frameAcess, bg= '#5544C0')
centerOptionsFrame.place( rely = 0.4 , relwidth = 1,relheight= 0.20 )

button = tk.Button(centerOptionsFrame, text= "LOGIN", bg= '#DEDAE6',font=("Helvetica", 15))
button.pack( fill = 'x')

button = tk.Button(centerOptionsFrame, text= "Criar Conta", bg= '#DEDAE6',font=("Helvetica", 15))
button.pack( fill= 'x')



root.mainloop()