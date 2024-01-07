from tkinter import *

class Gui(): #Esta classe é a base para a interface gráfica
    window = Tk()
    window.wm_title("Cadastro de Clientes")

    def run(self):
        Gui.window.mainloop()

    txtNome         = StringVar()
    txtSobrenome    = StringVar()
    txtEmail        = StringVar()
    txtCPF          = StringVar()

    lblnome        = Label(window, text="Nome", font="C059 13")
    lblsobrenome   = Label(window, text="Sobrenome", font="C059 13")
    lblemail       = Label(window, text="Email", font="C059 13")
    lblcpf         = Label(window, text="CPF", font="C059 13")

    entNome        = Entry(window, textvariable=txtNome)
    entSobrenome   = Entry(window, textvariable=txtSobrenome)
    entEmail       = Entry(window, textvariable=txtEmail)
    entCPF         = Entry(window, textvariable=txtCPF)

    listClientes   = Listbox(window)
    scrollClientes = Scrollbar(window)

    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    btnViewAll     = Button(window, text="Ver todos", background="#8419dc", foreground="white", relief=SOLID)
    btnBuscar      = Button(window, text="Buscar", background="#8419dc", foreground="white", relief=SOLID)
    btnInserir     = Button(window, text="Inserir", background="#8419dc", foreground="white", relief=SOLID)
    btnUpdate      = Button(window, text="Atualizar Selecionados", background="#8419dc", foreground="white", relief=SOLID)
    btnDel         = Button(window, text="Deletar Selecionados", background="#8419dc", foreground="white", relief=SOLID)
    btnClose       = Button(window, text="Fechar", background="#8419dc", foreground="white", relief=SOLID)

    lblnome.grid(row=0,column=0)
    lblsobrenome.grid(row=1,column=0)
    lblemail.grid(row=2,column=0)
    lblcpf.grid(row=3, column=0)

    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)

    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(sticky="NS", padx=0, pady=0)
        elif widget_class == "Scrollbar":
            child.grid_configure(sticky="NS", padx=0, pady=0)
        else:
            child.grid_configure(sticky="N", padx=x_pad, pady=y_pad)
