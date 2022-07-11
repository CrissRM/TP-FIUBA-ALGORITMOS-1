from tkinter import Tk,Label,Button,Entry,Label,Frame,messagebox as mb
from configuraciones.estilos import estilos
"Autor Cristian Roldan"

def interfaz():
    root = Tk()
    root.title("FIUBLE - SERPIENTE")
    root.geometry("+300+200")
    root.minsize(width=700,height=400)
    root.configure(background=estilos["BACKGROUND_PRIMARY"])

    return root

def titulo_aplicacion(root):
    return Label(
        root,
        text="FIUBLE-SERPIENTE",
        padx=5,
        pady=5,
        font=("Raleway",25,"roman"),
        width=25,
        anchor="center",
        background=estilos["BACKGROUND_PRIMARY"],
        foreground=estilos["FOREGROUND_PRIMARY"],
        ).pack(side="top",padx=10,pady=10)

def boton_registar(root,funct,arg): 
    
    boton = Button(
        root,
        text=arg[3]["BOTON_REGISTRAR"],
        font=("Releway",10,"normal"),
        padx=5,
        pady=5,
        state="normal",
        background=estilos["BACKGROUND_BUTTON_REGISTRO"],
        foreground=estilos["FOREGROUND_BUTTON_REGISTRO"],
        activebackground=estilos["BACKGROUND_BUTTON_REGISTRO_ACTIVE"],
        command=lambda: funct(arg)
        )
    boton.pack(
            side="left",
            padx=10,
            pady=10
        )
    
    return boton

def boton_ingresar(root,funct,arg):
    
    boton = Button(
        root,
        text=arg[3]["BOTON_INGRESAR"],
        font=("Releway",10,"normal"),
        padx=5,
        pady=5,
        state="normal",
        background=estilos["BACKGROUND_BUTTON_INGRESO"],
        foreground=estilos["FOREGROUND_BUTTON_INGRESO"],
        activebackground=estilos["BACKGROUND_BUTTON_INGRESO_ACTIVE"],
        command=lambda: funct(arg)
        )
    boton.pack(
            side="left",
            padx=10,
            pady=10
        )
    return boton

def boton_volver(root,funct,arg):
    boton = Button(
        root,
        text=arg[2]["BOTON_VOLVER"],
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        foreground="#fff",
        background="red",
        command=lambda: funct(arg)
    )
    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_guardar_registro(root,funct,arg):
    boton = Button(
        root,
        text=arg[5]["BOTON_GUARDAR_REGISTRO"],
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="blue",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_acceder(root,funct,arg):
    boton = Button(
        root,
        text=arg[6]["BOTON_ACCEDER"],
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="blue",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_confirmar_defecto(root,funct,arg): 
    boton = Button(
        root,
        text=arg[4]["BOTON_CONFIRMAR"],
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="green",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_confirmar_personalizada(root,funct,arg): 
    boton = Button(
        root,
        text=arg[6]["BOTON_CONFIRMAR"],
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="green",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def entrada_texto(root):
    caja = Entry(
        root,
        font=("Releway",15,"normal"),
        width=15,
        background="#fff",
        foreground="#000",
        justify="left"
    )
    caja.pack(side="left",padx=10,pady=10)
    return caja

def entrada_clave(root):
    caja = Entry(
        root,
        font=("Releway",15,"normal"),
        width=15,
        background="#fff",
        foreground="#000",
        show="*",
        justify="left"
    )
    caja.pack(side="left",padx=10,pady=10)
    return caja

def etiqueta(root,texto):
    label = Label(
        root,
        text=texto,
        padx=5,
        pady=5,
        font=("Releway",12,"roman"),
        width=15,
        anchor="w",
        background=estilos["BACKGROUND_PRIMARY"],
        foreground=estilos["FOREGROUND_PRIMARY"]
    )
    label.pack(side="left",padx=10,pady=10)
    return label

def marco_visible(root):
    marco = Frame(
        root,
        padx=10,
        pady=10,
        background=estilos["BACKGROUND_PRIMARY"],
    )
    marco.pack()

    return marco

def marco_invisible(root):
    marco = Frame(
        root,
        padx=10,
        pady=10,
        background=estilos["BACKGROUND_PRIMARY"],
    )
    marco.pack_forget()

    return marco

def msg_warning(msg,textos):
  mb.showwarning(textos["WIDGET_WARNING_TITULO"],msg)

def msg_error(msg,textos):
  mb.showerror(textos["WIDGET_ERROR_TITULO"],msg)

def msg_info(msg,textos):
  mb.showinfo(textos["WIDGET_INFO_TITULO"],msg)

def msg_confirm(msg,textos):
  return mb.askyesno(textos["WIDGET_CONFIRM_TITULO"],msg)
