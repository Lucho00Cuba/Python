
"""
from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.title("Hola Mundo")
#ventana.resizable(0, 0)

# Frames
frame_padre = Frame(ventana, width=250, height=250)
frame_padre.pack(side=BOTTOM, anchor=S ,fill=X, expand=YES)


frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="red",
    bd=5,
    relief=SOLID
)
frame.pack(side=LEFT, anchor=SW)

frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="green",
    bd=5,
    relief=SOLID
)
frame.pack(side=RIGHT, anchor=SE)

frame_padre = Frame(ventana, width=250, height=250)
frame_padre.pack(side=TOP, anchor=N , fill=X, expand=YES)

frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="blue",
    bd=5,
    relief=SOLID
)
frame.pack(side=LEFT)

frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
frame.pack(side=RIGHT)


ventana.mainloop()
"""
### 
"""
from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.title("Hola Mundo")
#ventana.resizable(0, 0)

# Frames
frame_padre = Frame(ventana, width=250, height=250)
frame_padre.pack(side=BOTTOM, anchor=S ,fill=X, expand=YES)


frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="red",
    bd=5,
    relief=SOLID
)
frame.pack(side=LEFT, anchor=SW)
frame.pack_propagate(False)

Label(frame, text="Primer Marco").pack(side=LEFT ,anchor=CENTER)

frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="green",
    bd=5,
    relief=SOLID
)
frame.pack(side=RIGHT, anchor=SE)

frame_padre = Frame(ventana, width=250, height=250)
frame_padre.pack(side=TOP, anchor=N , fill=X, expand=YES)

frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="blue",
    bd=5,
    relief=SOLID
)
frame.pack(side=LEFT)

frame = Frame(frame_padre, width=250, height=250)
frame.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
frame.pack(side=RIGHT)


ventana.mainloop()
"""