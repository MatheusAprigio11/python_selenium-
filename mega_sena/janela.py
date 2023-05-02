from tkinter import *
from tkinter import ttk
from read import listar_sorteio
from anos import todos_anos

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.comboBox()
        self.inputs()
        self.lista_frame2()
        janela.mainloop()
    

    def tela(self):
        self.janela.title('MEGASENA')
        self.janela.geometry('700x500')
        self.janela.configure(background='#C44536')
        self.janela.resizable(FALSE, FALSE)
        self.janela.maxsize(width=700, height=500)

    
    def frames(self):
        self.frame_0 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.janela, bg='black', highlightthickness=0.5, highlightbackground='white')
        self.frame_1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.35)

        self.frame_2 = Frame(self.janela, bg='#000', highlightthickness=0.03, highlightbackground='white')
        self.frame_2.place(relx=0.03, rely=0.60, relwidth=0.94, relheight=0.35)

    def botoes(self):
        # self.btBuscar = Button(self.frame_0, text='Buscar', bg='red', command=self.sel)
        # self.btBuscar.place(relx=0.15, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btLimpar = Button(self.frame_0, text='Limpar', bg='red', command=self.clear)
        self.btLimpar.place(relx=0.28, rely=0.25, relwidth=0.10, relheight=0.50)

        self.btRead = Button(self.frame_0, text='Read', bg='red', command=self.ler_sorteio)
        self.btRead.place(relx=0.55, rely=0.25, relwidth=0.10, relheight=0.50)

    
    def comboBox(self):
        self.lb_anos = Label(self.frame_0, text='Anos', background='red')
        self.lb_anos.pack()
        self.cb_anos=ttk.Combobox(self.frame_0,values=todos_anos)
        self.cb_anos.pack()
        self.cb_anos.place(relx=0.78, rely=0.30, relwidth=0.2, relheight=0.4)
        self.lb_anos.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.4)


    def inputs(self):
        self.inpNumb1 = Entry(self.frame_0)
        self.inpNumb1.place(relx=0.005, rely=0.25, relwidth=0.080, relheight=0.6)

        self.inpNumb2 = Entry(self.frame_0)
        self.inpNumb2.place(relx=0.12, rely=0.25, relwidth=0.080, relheight=0.6)

        self.inpNumb3 = Entry(self.frame_0)
        self.inpNumb3.place(relx=0.23, rely=0.25, relwidth=0.080, relheight=0.6)

        self.inpNumb4 = Entry(self.frame_0)
        self.inpNumb4.place(relx=0.34, rely=0.25, relwidth=0.080, relheight=0.6)

        self.inpNumb5 = Entry(self.frame_0)
        self.inpNumb5.place(relx=0.46, rely=0.25, relwidth=0.080, relheight=0.6)

        self.inpNumb6 = Entry(self.frame_0)
        self.inpNumb6.place(relx=0.58, rely=0.25, relwidth=0.080, relheight=0.6)


    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_1, height=3, columns=('col0',
                                                                      'col1',
                                                                      'col2',
                                                                      'col3',
                                                                      'col4',
                                                                      'col5',
                                                                      'col6'))
       

        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Sorteio')
        self.listaCli.heading('#2', text='N1')
        self.listaCli.heading('#3', text='N2')
        self.listaCli.heading('#4', text='N3')
        self.listaCli.heading('#5', text='N4')
        self.listaCli.heading('#6', text='N5')
        self.listaCli.heading('#7', text='N6')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=50)
        self.listaCli.column('#3', width=50)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)
        self.listaCli.column('#6', width=50)
        self.listaCli.column('#7', width=50)

        self.listaCli.place(relx=0.025, rely=0.080, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_1, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.98, rely=0.10, relwidth=0.02, relheight=0.85)


    def clear(self):
        self.listaCli.delete(*self.listaCli.get_children())

    def ler_sorteio(self):
        self.clear()
        sorteios = listar_sorteio()
        for sorteio in sorteios:
            self.listaCli.insert("", "end", values=sorteio)

    def get_ano(self):
        ano = self.lb_anos.get()
        return ano
    




janelaapp = Aplicacao()