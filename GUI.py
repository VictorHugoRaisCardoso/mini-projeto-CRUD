from tkinter import *

class Gui(): #Esta classe é a base para a interface gráfica
    window = Tk()
    window.wm_title("Cadastro de Clientes")

    def run(self):
        Gui.window.mainloop()

    '''
    Nesta segunda parte estamos definindo algumas variaveis que receberão um método StringVar().
    Este método é quem vai armazenar as informações inseridas pelo usuário.
    Agora basta definir os nomes das variavei de maneira que seja fácil identificar para que ela serve.
    Fica aqui minha sugestão de nome, assim acho que fica bem claro o objetivo da variavel.
    '''
    texto_nome = StringVar()
    texto_sobrenome = StringVar()
    texto_email = StringVar()
    texto_CPF = StringVar()

    '''
    Agora vamos definir as varaveis que receber o método Labels que ficarão do lado direito das variaveis texto.
    As labels são caixas que exibem uma quantidade de texto no nosso app. Da mesma forma vamos definir as variaveis
    com nomes que deixem evidentes o objetivo da variavel.
    '''
    label_nome = Label(window,
                       text="Nome",
                       font="Arial 13",
                       )
    label_sobrenome = Label(window,
                            text="Sobrenome",
                            font="Arial 13",
                            )
    label_email = Label(window,
                        text="Email",
                        font="Arial 13",
                        )
    label_CPF = Label(window,
                      text="CPF",
                      font="Arial 13",
                      )

    '''
    Neste ponto cabe uma explicação melhor sobre os parametros que serão passados dentro do método Label.
    Label(window)
        O primeiro parametro é refente a nossa janela, que definimos o nome la em cima, neste caso vamos passar o nome window
    Label(window, textvariabel= )
        textvariabel é um parametro recebe uma variavel que lê os dados que usuário inseriu. Você se lembra onde fizemos isso?
        Se você se lembrou das variaveis que receberam a o método StringVar() você acertou em cheio.
        Então vamos passar para o parametro textvariabel a nossa variavel texto_(nome da variavel)
    '''
    entrada_nome = Entry(window, textvariable=texto_nome)
    entrada_sobrenome = Entry(window, textvariable=texto_sobrenome)
    entrada_email = Entry(window, textvariable=texto_email)
    entrada_CPF = Entry(window, textvariable=texto_CPF)

    '''
    Agora vamos criar uma variavel qur vai exibir a lista de clientes cadastrados na nossa janela
    Lembre - se sempre de nomear as variaveis com nomes simples e objetivos de entender, evite resumir os nomes
    Vou deixar a minha sugestão, caso encontre uma maneira de ser mais claro e objetivo que isso, por favor, Faça!
    Se puder também mande sua sugestão aqui para que eu possa atualizar o codigo fim de facilitar ainda mais o
    entendimento para todos.
    Bom, nesta variavel a coisa é bem simples, passamos como parametro dentro da ListBox o nome da nossa janela,
     neste caso, window, isso vai colocar dentro da nossa janela uma caixa que exibirá nossos clientes cadastrados.
    '''
    lista_de_clientes = Listbox(window)

    '''
    Pensando no futuro vamos criar uma barra de rolagem, isso vai nos permitir rolar a nossa lista de clientes para cima
    ou para baixo conforme a nessecidade caso a nossa lista fique muito grande. Da mesma forma que fizemos com a ListBox
    vamos fazer com a Scrollbar, passaremos como parametro dentro dela a nossa janela, no nosso caso, window.
    A barra_de_rolagem ainda não esta conectada a lista_de_clientes. Mais tarde faremos isso.
    '''
    barra_de_rolagem = Scrollbar(window)

    lista_de_clientes.configure(yscrollcommand=barra_de_rolagem.set)
    barra_de_rolagem.configure(command=lista_de_clientes.yview)

    '''
    Agora vamos criar os botões, sempre mantendo nomes objetivos, por mais que fiquem grandes, é melhor ser grande e facil
    de entender do que resumido e depois correr o risco de criar confusão na sua cabeça.
    Dentro de Button vamos passar o nome da nossa janela, no parametro text= vamos passar uma string que será exibida dentro
    do botão.
    '''
    botao_ver_todos = Button(window,
                            text='Ver Todos',
                            relief=GROOVE,
                            background="#8419dc"
                            )
    botao_buscar = Button(window,
                         text='Buscar',
                         background="#8419dc")
    botao_cadastrar = Button(window,
                            text='Cadastrar',
                            background="#8419dc")
    botao_atualizar = Button(window,
                            text='Atualizar Selecionados',
                            background="#8419dc")
    botao_deletar = Button(window,
                           text='Deletar Selecionados',
                           background="#8419dc")
    botao_fechar = Button(window,
                        text='Fechar',
                        background="#8419dc")

    '''
    Agora vamoas para a parte que provavelmente vai dar mais trabalho, que é a de associar tudo que criamos até agora ao 
    nosso layout, até agora nos só criamos as variaveis que armazenam os Textos, os Botões etc.
    Vamos esclarecer algumas coisas antes de continuar, nos vmaos usar algumas palavras que podem ser estranhas, são elas:
    row:
        quando usarmos a palavra row leia mentalmente "linha". quando usarmos este parametro quer dizer que estaremos colocando
        numa determinada linha um determinado objeto que criamos antes.
    column:
        Da mesma forma que fizemos com o row faremos com o column, ao ler column fale mentalmente "Coluna". Os conceitos são os
        mesmos.
    Por que "linha" e "coluna", aqui nos vamos usar o grid layout, ele funciona de maneira parecida com uma planilha.
    Sendo assim vamos colocar os objetos começando de cima para baixo e da esquerda para a direita a partir do row = 0
    e column = 0.
    ou seja nos vamos contruir nosso app a partir do topo e a partir do canto esquerdo.
    '''
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
