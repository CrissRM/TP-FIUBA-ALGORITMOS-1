
def registrarse(lista):
    formulario_registro,root,cuadro_botones,textos = lista
    form_registro = formulario_registro(root,cuadro_botones,textos)
    form_registro.pack()
    cuadro_botones.pack_forget()
    
    
#llamando al método pack_forget() para hacerlos invisibles
#https://www.delftstack.com/es/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/
    