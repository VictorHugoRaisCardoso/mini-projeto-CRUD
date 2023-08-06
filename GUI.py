from tkinter import *

class Gui(): #Esta classe é a base para a interface gráfica
    window = Tk()
    window.wm_title("Cadastro de Clientes")

    def run(self):
        Gui.window.mainloop()


    texto_nome = StringVar()
    texto_sobrenome = StringVar()
    texto_email = StringVar()
    texto_CPF = StringVar()

    label_nome = Label(window,
                       text="Nome",
                       font="C059 13",
                       )
    label_sobrenome = Label(window,
                            text="Sobrenome",
                            font="C059 13",
                            )
    label_email = Label(window,
                        text="Email",
                        font="C059 13",
                        )
    label_CPF = Label(window,
                      text="CPF",
                      font="C059 13",
                      )

    entrada_nome = Entry(window, textvariable=texto_nome, foreground="blue", borderwidth=3)
    entrada_sobrenome = Entry(window, textvariable=texto_sobrenome, foreground="blue", borderwidth=3)
    entrada_email = Entry(window, textvariable=texto_email, foreground="blue", borderwidth=3)
    entrada_CPF = Entry(window, textvariable=texto_CPF, foreground="blue", borderwidth=3)

    lista_de_clientes = Listbox(window)

    barra_de_rolagem = Scrollbar(window)

    lista_de_clientes.configure(yscrollcommand=barra_de_rolagem.set)
    barra_de_rolagem.configure(command=lista_de_clientes.yview)

    botao_ver_todos = Button(window,
                            text="Ver Todos",
                            background="#8419dc",
                            foreground="white",
                            relief=SOLID,
                            )
    botao_buscar = Button(window,
                         text="Buscar",
                         background="#8419dc",
                         foreground="white",
                         relief=SOLID,
                         )
    botao_cadastrar = Button(window,
                            text="Cadastrar",
                            background="#8419dc",
                            foreground="white",
                            relief=SOLID,
                            )
    botao_atualizar = Button(window,
                            text="Atualizar Selecionados",
                            background="#8419dc",
                            foreground="white",
                            relief=SOLID,
                            )
    botao_deletar = Button(window,
                           text="Deletar Selecionados",
                           background="#8419dc",
                           foreground="white",
                           relief=SOLID,
                           )
    botao_fechar = Button(window,
                        text='Fechar',
                        background="#8419dc",
                        foreground="white",
                        relief=SOLID,
                        )

    label_nome.grid(row=0, column=0)
    label_sobrenome.grid(row=1, column=0)
    label_email.grid(row=2, column=0)
    label_CPF.grid(row=3, column=0)

    entrada_nome.grid(row=0, column=1)
    entrada_sobrenome.grid(row=1, column=1)
    entrada_email.grid(row=2, column=1)
    entrada_CPF.grid(row=3, column=1)

    lista_de_clientes.grid(row=0, column=2, rowspan=10)
    barra_de_rolagem.grid(row=0, column=6, rowspan=10)

    botao_ver_todos.grid(row=4, column=0, columnspan=2)
    botao_buscar.grid(row=5, column=0, columnspan=2)
    botao_cadastrar.grid(row=6, column=0, columnspan=2)
    botao_atualizar.grid(row=7, column=0, columnspan=2)
    botao_deletar.grid(row=8, column=0, columnspan=2)
    botao_fechar.grid(row=9, column=0, columnspan=2)

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
