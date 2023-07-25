from logging import root
from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import re
from tkinter import messagebox
import pandas as pd
from datetime import datetime

class Abrir:
    

    def open_interface_abrir(self):

        self.windowabrir = Toplevel() 
        self.windowabrir.geometry("1280x480")
        self.windowabrir.title("Procurar trabalhador")
        self.windowabrir.minsize(1220, 480)
        self.windowabrir.maxsize(1220, 480)
        self.icon=PhotoImage(file='icon.png')
        self.windowabrir.iconphoto(True,self.icon)
        
        i=3
        
        NomeCompletoLabel = Label(self.windowabrir, text="Nome Completo:")
        NomeCompletoLabel.grid(row=1, column=0+i)
        NomeCompletoEntrada = Entry(self.windowabrir, width=65)
        NomeCompletoEntrada.grid(row=1, column=1+i, columnspan=3)
        
        SexoLabel = Label(self.windowabrir, text="Sexo:")
        SexoLabel.grid(row=1, column=4+i)
        SexoEntrada = Entry(self.windowabrir)
        SexoEntrada.grid(row=1, column=5+i)

        # Linha 2
        DataNascimentoLabel = Label(self.windowabrir, text="Data de Nascimento:")
        DataNascimentoLabel.grid(row=2, column=0+i)
        DataNascimentoEntrada = Entry(self.windowabrir)
        DataNascimentoEntrada.grid(row=2, column=1+i)

        MunicipioNascimentoLabel = Label(self.windowabrir, text="Local de Nascimento/UF:")
        MunicipioNascimentoLabel.grid(row=2, column=2+i)
        MunicipioNascimentoEntrada = Entry(self.windowabrir)
        MunicipioNascimentoEntrada.grid(row=2, column=3+i)

        CordePeleLabel = Label(self.windowabrir, text="Cor de Pele:")
        CordePeleLabel.grid(row=2, column=4+i)
        CordePeleEntrada = Entry(self.windowabrir)
        CordePeleEntrada.grid(row=2, column=5+i)

        GrauDeInstrucaoLabel = Label(self.windowabrir, text="Grau de Instrução:")
        GrauDeInstrucaoLabel.grid(row=2, column=6+i)
        GrauDeInstrucaoEntrada = Entry(self.windowabrir, width=16)
        GrauDeInstrucaoEntrada.grid(row=2, column=7+i)

        # Linha 3
        EstadoCivilLabel = Label(self.windowabrir, text="Estado Civil:")
        EstadoCivilLabel.grid(row=3, column=0+i)
        EstadoCivilEntrada = Entry(self.windowabrir)
        EstadoCivilEntrada.grid(row=3, column=1+i)

        RegimeCasamentoLabel = Label(self.windowabrir, text="Regime de Casamento:")
        RegimeCasamentoLabel.grid(row=3, column=2+i)
        RegimeCasamentoEntrada = Entry(self.windowabrir)
        RegimeCasamentoEntrada.grid(row=3, column=3+i)

        NomeConjugeLabel = Label(self.windowabrir, text="Nome do Cônjuge:")
        NomeConjugeLabel.grid(row=3, column=4+i)
        NomeConjugeEntrada = Entry(self.windowabrir)
        NomeConjugeEntrada.grid(row=3, column=5+i)

        # Linha 4
        MaeLabel = Label(self.windowabrir, text="Mãe do trabalhador:")
        MaeLabel.grid(row=4, column=0+i)
        MaeEntrada = Entry(self.windowabrir)
        MaeEntrada.grid(row=4, column=1+i)

        PaiLabel = Label(self.windowabrir, text="Pai do trabalhador:")
        PaiLabel.grid(row=4, column=2+i)
        PaiEntrada = Entry(self.windowabrir)
        PaiEntrada.grid(row=4, column=3+i)

        # Linha 5
        RuaLabel = Label(self.windowabrir, text="Endereço Residencial:")
        RuaLabel.grid(row=5, column=0+i)
        RuaEntrada = Entry(self.windowabrir)
        RuaEntrada.grid(row=5, column=1+i)

        NumeroLabel = Label(self.windowabrir, text="Número:")
        NumeroLabel.grid(row=5, column=2+i)
        NumeroEntrada = Entry(self.windowabrir)
        NumeroEntrada.grid(row=5, column=3+i)

        BairroLabel = Label(self.windowabrir, text="Bairro:")
        BairroLabel.grid(row=5, column=4+i)
        BairroEntrada = Entry(self.windowabrir)
        BairroEntrada.grid(row=5, column=5+i)

        # Linha 6
        CidadeLabel = Label(self.windowabrir, text="Cidade:")
        CidadeLabel.grid(row=6, column=0+i)
        CidadeEntrada = Entry(self.windowabrir)
        CidadeEntrada.grid(row=6, column=1+i)

        EstadoLabel = Label(self.windowabrir, text="Estado:")
        EstadoLabel.grid(row=6, column=2+i)
        EstadoEntrada = Entry(self.windowabrir)
        EstadoEntrada.grid(row=6, column=3+i)

        CEPLabel = Label(self.windowabrir, text="CEP:")
        CEPLabel.grid(row=6, column=4+i)
        CEPEntrada = Entry(self.windowabrir)
        CEPEntrada.grid(row=6, column=5+i)

        # Linha 7
        TelefoneLabel = Label(self.windowabrir, text="Telefone Residencial:")
        TelefoneLabel.grid(row=7, column=0+i)
        TelefoneEntrada = Entry(self.windowabrir)
        TelefoneEntrada.grid(row=7, column=1+i)

        CelularLabel = Label(self.windowabrir, text="Telefone Celular:")
        CelularLabel.grid(row=7, column=2+i)
        CelularEntrada = Entry(self.windowabrir)
        CelularEntrada.grid(row=7, column=3+i)

        EmailLabel = Label(self.windowabrir, text="E-mail:")
        EmailLabel.grid(row=7, column=4+i)
        EmailEntrada = Entry(self.windowabrir)
        EmailEntrada.grid(row=7, column=5+i)

        # Linha 9
        BancoLabel = Label(self.windowabrir, text="Banco:")
        BancoLabel.grid(row=9, column=0+i)
        BancoEntrada = Entry(self.windowabrir)
        BancoEntrada.grid(row=9, column=1+i)

        AgenciaLabel = Label(self.windowabrir, text="Agência:")
        AgenciaLabel.grid(row=9, column=2+i)
        AgenciaEntrada = Entry(self.windowabrir)
        AgenciaEntrada.grid(row=9, column=3+i)

        ContaLabel = Label(self.windowabrir, text="nº da Conta:")
        ContaLabel.grid(row=9, column=4+i)
        ContaEntrada = Entry(self.windowabrir)
        ContaEntrada.grid(row=9, column=5+i)

        TipoContaLabel = Label(self.windowabrir, text="Tipo de Conta:")
        TipoContaLabel.grid(row=9, column=6+i)
        TipoContaEntrada = Entry(self.windowabrir, width=16)
        TipoContaEntrada.grid(row=9, column=7+i)

        # Linha 10
        PixLabel = Label(self.windowabrir, text="Pix:")
        PixLabel.grid(row=10, column=0+i)
        PixEntrada = Entry(self.windowabrir)
        PixEntrada.grid(row=10, column=1+i)

        TitularLabel = Label(self.windowabrir, text="Titular da Conta :")
        TitularLabel.grid(row=10, column=2+i)
        TitularEntrada = Entry(self.windowabrir)
        TitularEntrada.grid(row=10, column=3+i)
        
        TitularCPFLabel = Label(self.windowabrir, text="CPF do Titular:")
        TitularCPFLabel.grid(row=10, column=4+i)
        TitularCPFEntrada = Entry(self.windowabrir)
        TitularCPFEntrada.grid(row=10, column=5+i)
        
        TitularParentescoLabel = Label(self.windowabrir, text="Parentesco do Titular:")
        TitularParentescoLabel.grid(row=10, column=6+i)
        TitularParentescoEntrada = Entry(self.windowabrir, width=16)
        TitularParentescoEntrada.grid(row=10, column=7+i)
        
        # Linha 11
        CPFLabel = Label(self.windowabrir, text="CPF:")
        CPFLabel.grid(row=12, column=0+i)
        CPFEntrada = Entry(self.windowabrir)
        CPFEntrada.grid(row=12, column=1+i)

        PISLabel = Label(self.windowabrir, text="PIS:")
        PISLabel.grid(row=12, column=2+i)
        PISEntrada = Entry(self.windowabrir)
        PISEntrada.grid(row=12, column=3+i)

        CTPSLabel = Label(self.windowabrir, text="CTPS:")
        CTPSLabel.grid(row=12, column=4+i)
        CTPSEntrada = Entry(self.windowabrir)
        CTPSEntrada.grid(row=12, column=5+i)
        
        DataEspedicaoCPFLabel = Label(self.windowabrir, text="Data de expedição CPF:")
        DataEspedicaoCPFLabel.grid(row=12, column=6+i)
        DataEspedicaoCPFEntrada = Entry(self.windowabrir, width=16)
        DataEspedicaoCPFEntrada.grid(row=12, column=7+i)


        # Linha 13
        RGLabel = Label(self.windowabrir, text="RG:")
        RGLabel.grid(row=13, column=0+i)
        RGEntrada = Entry(self.windowabrir)
        RGEntrada.grid(row=13, column=1+i)

        ExpeditorRGLabel = Label(self.windowabrir, text="Orgão Espeditor:")
        ExpeditorRGLabel.grid(row=13, column=2+i)
        ExpeditorRGEntrada = Entry(self.windowabrir)
        ExpeditorRGEntrada.grid(row=13, column=3+i)       

        DataEspedicaoRGLabel = Label(self.windowabrir, text="Data de Expedição RG:")
        DataEspedicaoRGLabel.grid(row=13, column=4+i)
        DataEspedicaoRGEntrada = Entry(self.windowabrir)
        DataEspedicaoRGEntrada.grid(row=13, column=5+i)

        # Linha 14
        TitulodeEleitorLabel = Label(self.windowabrir, text="Titulo de Eleitor:")
        TitulodeEleitorLabel.grid(row=14, column=0+i)
        TitulodeEleitorEntrada = Entry(self.windowabrir)
        TitulodeEleitorEntrada.grid(row=14, column=1+i)

        ZonaLabel = Label(self.windowabrir, text="Zona:")
        ZonaLabel.grid(row=14, column=2+i)
        ZonaEntrada = Entry(self.windowabrir)
        ZonaEntrada.grid(row=14, column=3+i)
        
        SecaoLabel = Label(self.windowabrir, text="Seção:")
        SecaoLabel.grid(row=14, column=4+i)
        SecaoEntrada = Entry(self.windowabrir)
        SecaoEntrada.grid(row=14, column=5+i)
        
        LocaldeTrabalhoLabel = Label(self.windowabrir, text="Local de trabalho:")
        LocaldeTrabalhoLabel.grid(row=16, column=0+i)
        LocaldeTrabalhoEntrada = Entry(self.windowabrir)
        LocaldeTrabalhoEntrada.grid(row=16, column=1+i)
        
        def rotatividade(pk):

            def Create_Rotativo():
                    conn = sqlite3.connect('trabalhador.db')
                    cursor = conn.cursor()

                    cursor.execute('''CREATE TABLE IF NOT EXISTS rotativo (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        pessoa INT,
                        classe TEXT,
                        data_inicio TEXT,
                        data_fim TEXT,
                        estado_contratual TEXT,
                        dias_sem_carteira TEXT,
                        data_inicio_YYYYMMDD TEXT,
                        FOREIGN KEY (pessoa) REFERENCES trabalhador(id)
                    )''')
                    conn.commit()
                    conn.close()
            Create_Rotativo()
            def Calculatar_dias():
                global TempoSemCarteiraEntrada
                global data_inicio_YYYYMMDD
                try:
                    from datetime import datetime
                    data_inicio_original = InicioContratoEntrada.get()
                    day, month, year = data_inicio_original.split('/')
                    data_inicio_YYYYMMDD = year + month + day


                    if FimContratoEntrada.get() == '':
                        begin_input = InicioContratoEntrada.get()
                        begin_date = datetime.strptime(begin_input, "%d/%m/%Y")

                        if ClasseEntrada.get() == 'CTPS':
                            TempoSemCarteiraEntrada = ''

                        if ClasseEntrada.get() == 'Diarista':
                            data_atual = datetime.now()
                            TempoSemCarteiraEntrada = (data_atual - begin_date).days
                    else:
                        begin_input = InicioContratoEntrada.get()
                        begin_date = datetime.strptime(begin_input, "%d/%m/%Y")

                        end_input = FimContratoEntrada.get()
                        end_date = datetime.strptime(end_input, "%d/%m/%Y")

                        if ClasseEntrada.get() == 'CTPS':
                            TempoSemCarteiraEntrada = ''

                        if ClasseEntrada.get() == 'Diarista':
                            TempoSemCarteiraEntrada = (end_date - begin_date).days
                except ValueError:
                    messagebox.showerror("Data Invalida", "Por favor, Entre com o formato de data correta: DD/MM/AAAA.")
                except Exception as e:
                    messagebox.showerror("Ocorreu um erro:", str(e))
                

                #result_label.config(text="The number of days between the two dates is: " + str(days_difference))
            def DefinirEstadoContratual():
                global EstadoContratual
                if FimContratoEntrada.get() == '':
                    EstadoContratual = 'ATIVO'
                else:
                    EstadoContratual = 'INATIVO'
            
            primarykey=pk
            conn = sqlite3.connect("trabalhador.db")
            cursor = conn.cursor()
            cursor.execute("SELECT nome_completo FROM trabalhador WHERE oid = :oid", {'oid': primarykey[0]})
            NomeTrabalhador = cursor.fetchone()[0]
            conn.commit()
            conn.close()
            
            wrotatividade = Toplevel(self.windowabrir)
            wrotatividade.geometry("750x320")
            wrotatividade.title("Rotatividade de " + NomeTrabalhador)
            wrotatividade.minsize(750, 320)
            wrotatividade.maxsize(750, 320)
            wrotatividade.iconphoto(True,self.icon)

            Frametitulo = Frame(wrotatividade, width=660, height=10,highlightbackground="black", highlightthickness=1)
            Frametitulo.grid(row=0, column=0, columnspan=16)

            TituloPreencherLabel = Label(Frametitulo, text="Ciclo Contratual de " + NomeTrabalhador, font=("Arial", 15))
            TituloPreencherLabel.grid(row=0, column=0, padx=182, pady=10)
            
            def MostrarEstadoAtualdoFuncionario():
                primarykey=pk
                conn = sqlite3.connect("trabalhador.db")
                cursor = conn.cursor()
                cursor.execute("SELECT estado_contratual FROM rotativo WHERE pessoa = :pessoa ORDER BY data_inicio DESC LIMIT 1", {'pessoa': primarykey[0]})
                records = cursor.fetchone()
                conn.commit()
                conn.close()
                
                if records is None:
                    # Handle the case when no records are found
                    estado = "SEM DADOS"
                    cor = "black"
                else:
                    estado = records[-1]
                    print(estado)
                    if estado == 'ATIVO':
                        cor = "green"
                    else:
                        cor = "red"
                MostrarEstadoLabel=Label(wrotatividade,text=estado,font=("Calibri",30),width=70,fg=cor)
                MostrarEstadoLabel.grid(row=7,column=0,columnspan=2)
                

            # Chame a função MostrarEstadoAtualdoFuncionario()
            MostrarEstadoAtualdoFuncionario()
            #classe
            ClasseLabel = Label(wrotatividade, text="Classe:")
            ClasseLabel.grid(row=1, column=0)
            
            n = tk.StringVar()
            ClasseEntrada = ttk.Combobox(wrotatividade, width=17, textvariable=n)
            ClasseEntrada['values'] = ('Diarista', 'CTPS')
            ClasseEntrada.grid(row=1, column=1, sticky="w")
            

            # Início do contrato
            InicioContratoLabel = Label(wrotatividade, text="Início do contrato")
            InicioContratoLabel.grid(row=2, column=0)

            InicioContratoEntrada = Entry(wrotatividade)
            InicioContratoEntrada.grid(row=2, column=1, sticky="w")

            # Fim do contrato
            FimContratoLabel = Label(wrotatividade, text="Fim do contrato")
            FimContratoLabel.grid(row=3, column=0)

            FimContratoEntrada = Entry(wrotatividade)
            FimContratoEntrada.grid(row=3, column=1, sticky="w")
            

            def reorganizar_ids():
                # Connect to the database
                conn = sqlite3.connect("trabalhador.db")
                cursor = conn.cursor()

                # Retrieve all records ordered by ID
                cursor.execute("SELECT id FROM rotativo ORDER BY id")
                records = cursor.fetchall()

                # Update the IDs
                for new_id, (old_id,) in enumerate(records, start=1):
                    cursor.execute("UPDATE rotativo SET id = ? WHERE id = ?", (new_id, old_id))

                # Commit the changes
                conn.commit()

                # Close the database connection
                conn.close()
                open_table()
            
            def cancelar():
                limpar()
                mostrar_salvar_Botao()
                CancelarBotao.grid_forget()

            def limpar():
                entries = [ClasseEntrada,InicioContratoEntrada,FimContratoEntrada]

                for entry in entries:
                    entry.delete(0, END)
            
            def Salvar_Rotativo():
                print("Classe:", ClasseEntrada.get())
                if ClasseEntrada.get()=='Diarista' or ClasseEntrada.get()=='CTPS':
                    try:    
                        Calculatar_dias()
                        DefinirEstadoContratual()
                        conn = sqlite3.connect('trabalhador.db')
                        cursor = conn.cursor()

                        # Get the input values from the entry fields
                        classe = ClasseEntrada.get()
                        data_inicio = InicioContratoEntrada.get()
                        data_fim = FimContratoEntrada.get()
                        estado_contratual = EstadoContratual
                        tempo_sem_carteira = TempoSemCarteiraEntrada

                        # Insert worker data into the table
                        cursor.execute('''INSERT INTO rotativo (pessoa, classe, data_inicio, data_fim, estado_contratual, dias_sem_carteira, data_inicio_YYYYMMDD)
                                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                    (primarykey[0],classe,data_inicio,data_fim,estado_contratual,tempo_sem_carteira, data_inicio_YYYYMMDD))

                        # Commit the changes and close the connection
                        conn.commit()
                        conn.close()
                        open_table()
                        reorganizar_ids()
                        MostrarEstadoAtualdoFuncionario()
                    except Exception as e:
                        messagebox.showerror("Ocorreu um erro", str(e))
                else:
                    messagebox.showerror("Classe Invalida", "Por favor, Insira uma das classes disponíveis: Diarista ou CTPS")

            def Atualizar_Rotativo(id):
                
                if ClasseEntrada.get()=='Diarista' or ClasseEntrada.get()=='CTPS':
                    try:
                        Calculatar_dias()
                        DefinirEstadoContratual()
                        confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja Atualizar o registro?")

                        if confirm:
                            pk1=id
                            pk2=id
                            
                            conn = sqlite3.connect('trabalhador.db')
                            cursor = conn.cursor()

                            pessoa = primarykey[0]
                            classe = ClasseEntrada.get()
                            data_inicio = InicioContratoEntrada.get()
                            data_fim = FimContratoEntrada.get()
                            estado_contratual = EstadoContratual
                            dias_sem_carteira = TempoSemCarteiraEntrada

                            cursor.execute("""UPDATE rotativo SET 
                                            pessoa = :pessoa,
                                            classe = :classe,
                                            data_inicio = :data_inicio,
                                            data_fim = :data_fim,
                                            estado_contratual = :estado_contratual,
                                            dias_sem_carteira = :dias_sem_carteira,
                                           data_inicio_YYYYMMDD = :data_inicio_YYYYMMDD
                                        WHERE oid = :oid""",
                                {
                                    'pessoa': pessoa,
                                    'classe': classe,
                                    'data_inicio': data_inicio,
                                    'data_fim': data_fim,
                                    'estado_contratual': estado_contratual,
                                    'dias_sem_carteira': dias_sem_carteira,
                                    'data_inicio_YYYYMMDD': data_inicio_YYYYMMDD,
                                    'oid': pk1
                                })


                            # Commit the changes and close the connection
                            conn.commit()
                            conn.close()
                            #on_button_click(pk2)
                            AtualizarBotao2.grid_forget()
                            CancelarBotao.grid_forget()
                            mostrar_salvar_Botao()
                            open_table()
                            reorganizar_ids()
                            MostrarEstadoAtualdoFuncionario()
                            print(pk1)
                        else:
                            messagebox.showinfo("Alerta", "A edição foi cancelada.")
                    except:
                        messagebox.showerror("Classe Invalida", "Por favor, Insira uma das classes disponíveis: Diarista ou CTPS")
                else:
                    messagebox.showerror("Classe Invalida", "Por favor, Insira uma das classes disponíveis: Diarista ou CTPS")
                
            def on_right_click(event):
                # Get the row index where the right-click event occurred
                row = table.identify_row(event.y)

                if row:
                    # Show a context menu with options
                    menu.post(event.x_root, event.y_root)
         
            def mostrar_editar():
                limpar()
                # Get the selected row
                selected_row = table.selection()[0]

                # Get the data from the selected row
                data = table.item(selected_row)['values']

                id = data[0]
                id=str(id)

                conn = sqlite3.connect("trabalhador.db")
                cursor = conn.cursor()

                # Query the database
                cursor.execute("SELECT * FROM rotativo where oid = " + id)
                records = cursor.fetchall()

                for record in records:
                    ClasseEntrada.insert(0, record[2])
                    InicioContratoEntrada.insert(0, record[3])
                    FimContratoEntrada.insert(0, record[4])
                    
                # Commit changes
                conn.commit()
                # Close connection
                conn.close()

                SalvarBotao.grid_forget()
                mostrar_atualizar_Botao(id)  

            def open_table():
                # Get the value for "pessoa" from the user input
                pessoa_value = primarykey[0]

                # Query the database to get the rows with the specific "pessoa" value
                query = f"SELECT id, classe, data_inicio, data_fim, estado_contratual, dias_sem_carteira FROM rotativo WHERE pessoa={pessoa_value} ORDER BY data_inicio_YYYYMMDD"
                cursor.execute(query)
                rows = cursor.fetchall()

                # Create a pandas DataFrame from the query result
                df = pd.DataFrame(rows, columns=["id","Classe", "Data Início", "Data Fim", "Estado Contratual", "Dias sem Carteira"])

                # Clear the existing table
                table.delete(*table.get_children())

                # Insert the data into the table
                for index, row in df.iterrows():
                    table.insert("", "end", values=row.tolist())
            
            def delete():
                # Get the selected row
                selected_row = table.selection()[0]

                # Get the data from the selected row
                data = table.item(selected_row)['values']

                id = data[0]
                id=str(id)
                # Confirmar antes de deletar
                confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar o registro?")

                if confirm:
                    # Conectar ao banco de dados
                    conn = sqlite3.connect("trabalhador.db")
                    cursor = conn.cursor()

                    # Excluir o registro
                    cursor.execute("DELETE FROM rotativo WHERE oid = ?", (id,))
                    conn.commit()

                    # Fechar conexão
                    conn.close()

                    messagebox.showinfo("Alerta", "Registro apagado com sucesso!")
                    
                    open_table()
                    reorganizar_ids()
                else:
                    messagebox.showinfo("Alerta", "A exclusão foi cancelada.")
                # Establish a connection to the database
            
            conn = sqlite3.connect('trabalhador.db')
            cursor = conn.cursor()
            
            # Create a frame for the table
            frame = tk.Frame(wrotatividade)
            frame.grid(row=1, column=4, rowspan=7, columnspan=4, padx=10, pady=10)

            # Create a scrollable table
            table = ttk.Treeview(frame, show="headings")
            table.grid(row=0, column=0, sticky="nsew")

            # Add scrollbar to the table
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")
            table.configure(yscrollcommand=scrollbar.set)

            # Add right-click event binding to the table
            table.bind("<Button-3>", on_right_click)

            # Hide the "pessoa" columns in the table
            table["columns"] = ("id","classe", "data_inicio", "data_fim", "estado_contratual", "dias_sem_carteira")
            table["columns"] = ("id","classe", "data_inicio", "data_fim", "estado_contratual", "dias_sem_carteira")

            # Define column headers
            table.heading("id", text="id")
            table.heading("classe", text="Classe")
            table.heading("data_inicio", text="Data Início")
            table.heading("data_fim", text="Data Fim")
            table.heading("estado_contratual", text="Estado Contratual")
            table.heading("dias_sem_carteira", text="Dias sem Carteira")

            # Set column widths
            table.column("id", width=1)
            table.column("classe", width=60)
            table.column("data_inicio", width=70)
            table.column("data_fim", width=70)
            table.column("estado_contratual", width=110)
            table.column("dias_sem_carteira", width=120)

            # Configure grid row and column weights
            wrotatividade.grid_rowconfigure(0, weight=1)
            wrotatividade.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            open_table()
            def mostrar_salvar_Botao():
                global SalvarBotao
                SalvarBotao = Button(wrotatividade,text="Inserir na linha do tempo",command=Salvar_Rotativo)
                SalvarBotao.grid(row=4,column=0)

            def mostrar_atualizar_Botao(id):
                pk=id
                global AtualizarBotao2
                AtualizarBotao2 = Button(wrotatividade,text="Editar linha do tempo",command=lambda: Atualizar_Rotativo(pk))
                AtualizarBotao2.grid(row=4,column=0)
                mostrar_cancelar_Botao()

            LimparBotao = Button(wrotatividade,text="Limpar",command=limpar)
            LimparBotao.grid(row=4,column=1,sticky="w")


            def mostrar_cancelar_Botao():
                global CancelarBotao
                CancelarBotao = Button(wrotatividade,text="Cancelar",command=cancelar)
                CancelarBotao.grid(row=4,column=1,sticky="e")



            mostrar_salvar_Botao()

            # Create context menu
            menu = tk.Menu(table, tearoff=False)
            menu.add_command(label="Editar", command=mostrar_editar)
            menu.add_command(label="Excluir",command=delete)
            #\\\---------------------------------------------------------------////

        def importar_para_csv():
           # Connect to the SQLite database
            conn = sqlite3.connect('trabalhador.db')

            # Retrieve data from the table
            data = pd.read_sql_query("SELECT * FROM trabalhador", conn)

            # Specify the file path for the CSV file
            csv_file_path = 'trabalhador.csv'

            # Save the data to the CSV file with comma delimiter
            data.to_csv(csv_file_path, index=False, sep=',')

            # Close the database connection
            conn.close()

            print("Data exported to CSV successfully.")
        
        def mostrar_botao_atualizar(pk):
            on_button_click(pk)
            primarykey = pk
            global AtualizarBotao
            AtualizarBotao = Button(self.windowabrir, text="Atualizar", command=lambda: atualizar(primarykey))
            AtualizarBotao.grid(row=17, column=6)
        
        def atualizar(primarykey):
             # Confirmar antes de deletar
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja Atualizar o registro?")

            if confirm:
                pk = str(primarykey)
                pk1 = re.findall(r'\d+', pk)[0]
                
                
                conn = sqlite3.connect('trabalhador.db')
                cursor = conn.cursor()

                nome_completo = NomeCompletoEntrada.get()
                sexo = SexoEntrada.get()
                data_nascimento = DataNascimentoEntrada.get()
                municipio_nascimento = MunicipioNascimentoEntrada.get()
                cor_pele = CordePeleEntrada.get()
                grau_instrucao = GrauDeInstrucaoEntrada.get()
                estado_civil = EstadoCivilEntrada.get()
                regime_casamento = RegimeCasamentoEntrada.get()
                nome_conjuge = NomeConjugeEntrada.get()
                mae = MaeEntrada.get()
                pai = PaiEntrada.get()
                rua = RuaEntrada.get()
                numero = NumeroEntrada.get()
                bairro = BairroEntrada.get()
                cidade = CidadeEntrada.get()
                estado = EstadoEntrada.get()
                cep = CEPEntrada.get()
                telefone_residencial = TelefoneEntrada.get()
                telefone_celular = CelularEntrada.get()
                email = EmailEntrada.get()
                banco = BancoEntrada.get()
                agencia = AgenciaEntrada.get()
                numero_conta = ContaEntrada.get()
                tipo_conta = ContaEntrada.get()
                pix = PixEntrada.get()
                titular_conta = TitularEntrada.get()
                cpf_titular = TitularCPFEntrada.get()
                parentesco = TitularParentescoEntrada.get()
                cpf_pessoal = CPFEntrada.get()
                pis = PISEntrada.get()
                ctps = CTPSEntrada.get()
                data_expedicao_cpf = DataEspedicaoCPFEntrada.get()
                rg = RGEntrada.get()
                orgao_expeditor = ExpeditorRGEntrada.get()
                data_expedicao_rg = DataEspedicaoRGEntrada.get()
                titulo_eleitor = TitulodeEleitorEntrada.get()
                zona = ZonaEntrada.get()
                secao = SecaoEntrada.get()
                localdetrabalho = LocaldeTrabalhoEntrada.get()

                cursor.execute("""UPDATE trabalhador SET 
                                nome_completo = :nome_completo,
                                sexo = :sexo,
                                data_nascimento = :data_nascimento,
                                municipio_nascimento = :municipio_nascimento,
                                cor_pele = :cor_pele,
                                grau_instrucao = :grau_instrucao,
                                estado_civil = :estado_civil,
                                regime_casamento = :regime_casamento,
                                nome_conjuge = :nome_conjuge,
                                mae = :mae,
                                pai = :pai,
                                rua = :rua,
                                numero = :numero,
                                bairro = :bairro,
                                cidade = :cidade,
                                estado = :estado,
                                cep = :cep,
                                telefone_residencial = :telefone_residencial,
                                telefone_celular = :telefone_celular,
                                email = :email,
                                banco = :banco,
                                agencia = :agencia,
                                numero_conta = :numero_conta,
                                tipo_conta = :tipo_conta,
                                pix = :pix,
                                titular_conta = :titular_conta,
                                cpf_titular = :cpf_titular,
                                parentesco = :parentesco,
                                cpf_pessoal = :cpf_pessoal,
                                pis = :pis,
                                ctps = :ctps,
                                data_expedicao_cpf = :data_expedicao_cpf,
                                rg = :rg,
                                orgao_expeditor = :orgao_expeditor,
                                data_expedicao_rg = :data_expedicao_rg,
                                titulo_eleitor = :titulo_eleitor,
                                zona = :zona,
                                secao = :secao,
                                localdetrabalho = :localdetrabalho
                                WHERE oid = :oid""",
                        {
                            'nome_completo': nome_completo,
                            'sexo': sexo,
                            'data_nascimento': data_nascimento,
                            'municipio_nascimento': municipio_nascimento,
                            'cor_pele': cor_pele,
                            'grau_instrucao': grau_instrucao,
                            'estado_civil': estado_civil,
                            'regime_casamento': regime_casamento,
                            'nome_conjuge': nome_conjuge,
                            'mae': mae,
                            'pai': pai,
                            'rua': rua,
                            'numero': numero,
                            'bairro': bairro,
                            'cidade': cidade,
                            'estado': estado,
                            'cep': cep,
                            'telefone_residencial': telefone_residencial,
                            'telefone_celular': telefone_celular,
                            'email': email,
                            'banco': banco,
                            'agencia': agencia,
                            'numero_conta': numero_conta,
                            'tipo_conta': tipo_conta,
                            'pix': pix,
                            'titular_conta': titular_conta,
                            'cpf_titular': cpf_titular,
                            'parentesco': parentesco,
                            'cpf_pessoal': cpf_pessoal,
                            'pis': pis,
                            'ctps': ctps,
                            'data_expedicao_cpf': data_expedicao_cpf,
                            'rg': rg,
                            'orgao_expeditor': orgao_expeditor,
                            'data_expedicao_rg': data_expedicao_rg,
                            'titulo_eleitor': titulo_eleitor,
                            'zona': zona,
                            'secao': secao,
                            'localdetrabalho': localdetrabalho,
                            'oid': pk1
                        })

                # Commit the changes and close the connection
                conn.commit()
                conn.close()
                on_button_click(pk)
                AtualizarBotao.grid_forget()
                print(pk1)
            else:
                messagebox.showinfo("Alerta", "A edição foi cancelada.")
        
        def reorganizar_ids():
            # Connect to the database
            conn = sqlite3.connect("trabalhador.db")
            cursor = conn.cursor()

            # Retrieve all records ordered by ID
            cursor.execute("SELECT id FROM trabalhador ORDER BY id")
            records = cursor.fetchall()

            # Update the IDs
            for new_id, (old_id,) in enumerate(records, start=1):
                cursor.execute("UPDATE trabalhador SET id = ? WHERE id = ?", (new_id, old_id))

            # Commit the changes
            conn.commit()

            # Close the database connection
            conn.close()
            mostrar_todos()
     
        def delete(pk):
            # Confirmar antes de deletar
            confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar o registro?")

            if confirm:
                # Conectar ao banco de dados
                conn = sqlite3.connect("trabalhador.db")
                cursor = conn.cursor()

                # Excluir o registro
                cursor.execute("DELETE FROM trabalhador WHERE oid = ?", (pk))
                conn.commit()

                # Fechar conexão
                conn.close()

                messagebox.showinfo("Alerta", "Registro apagado com sucesso!")
                
                reorganizar_ids()
                mostrar_todos()
                limpar()
            else:
                messagebox.showinfo("Alerta", "A exclusão foi cancelada.")
        
        def limpar():
                entries = [NomeCompletoEntrada, SexoEntrada, DataNascimentoEntrada, MunicipioNascimentoEntrada, CordePeleEntrada,
                        GrauDeInstrucaoEntrada, EstadoCivilEntrada, RegimeCasamentoEntrada, NomeConjugeEntrada, MaeEntrada,
                        PaiEntrada, RuaEntrada, NumeroEntrada, BairroEntrada, CidadeEntrada, EstadoEntrada, CEPEntrada,
                        TelefoneEntrada, CelularEntrada, EmailEntrada, BancoEntrada, AgenciaEntrada, ContaEntrada,
                        TipoContaEntrada, PixEntrada, TitularEntrada, TitularCPFEntrada, TitularParentescoEntrada, CPFEntrada,
                        PISEntrada, CTPSEntrada, DataEspedicaoCPFEntrada, RGEntrada, ExpeditorRGEntrada, DataEspedicaoRGEntrada,
                        TitulodeEleitorEntrada, ZonaEntrada, SecaoEntrada, LocaldeTrabalhoEntrada]

                for entry in entries:
                    entry.delete(0, END)
        
        def on_entry_focus_in(event):
            if ProcuraEntrada.get() == 'Pesquisar':
                ProcuraEntrada.delete(0, 'end')

        def on_entry_focus_out(event):
            if ProcuraEntrada.get() == '':
                ProcuraEntrada.insert(0, 'Pesquisar')
        
        def on_button_click(primary_key):
                limpar()
                print("Button clicked:", primary_key)
                primary_key_string=str(primary_key)
                primary_key_string=primary_key_string[1:-1]
                # connect to database
                conn = sqlite3.connect("trabalhador.db")
                cursor = conn.cursor()

                # Query the database
                cursor.execute("SELECT * FROM trabalhador where oid = " + primary_key_string)
                records = cursor.fetchall()

                for record in records:
                    NomeCompletoEntrada.insert(0, record[1])
                    SexoEntrada.insert(0, record[2])
                    DataNascimentoEntrada.insert(0, record[3])
                    MunicipioNascimentoEntrada.insert(0, record[4])
                    CordePeleEntrada.insert(0, record[5])
                    GrauDeInstrucaoEntrada.insert(0, record[6])
                    EstadoCivilEntrada.insert(0, record[7])
                    RegimeCasamentoEntrada.insert(0, record[8])
                    NomeConjugeEntrada.insert(0, record[9])
                    MaeEntrada.insert(0, record[10])
                    PaiEntrada.insert(0, record[11])
                    RuaEntrada.insert(0, record[12])
                    NumeroEntrada.insert(0, record[13])
                    BairroEntrada.insert(0, record[14])
                    CidadeEntrada.insert(0, record[15])
                    EstadoEntrada.insert(0, record[16])
                    CEPEntrada.insert(0, record[17])
                    TelefoneEntrada.insert(0, record[18])
                    CelularEntrada.insert(0, record[19])
                    EmailEntrada.insert(0, record[20])
                    BancoEntrada.insert(0, record[21])
                    AgenciaEntrada.insert(0, record[22])
                    ContaEntrada.insert(0, record[23])
                    TipoContaEntrada.insert(0, record[24])
                    PixEntrada.insert(0, record[25])
                    TitularEntrada.insert(0, record[26])
                    TitularCPFEntrada.insert(0, record[27])
                    TitularParentescoEntrada.insert(0, record[28])
                    CPFEntrada.insert(0, record[29])
                    PISEntrada.insert(0, record[30])
                    CTPSEntrada.insert(0, record[31])
                    DataEspedicaoCPFEntrada.insert(0, record[32])
                    RGEntrada.insert(0, record[33])
                    ExpeditorRGEntrada.insert(0, record[34])
                    DataEspedicaoRGEntrada.insert(0, record[35])
                    TitulodeEleitorEntrada.insert(0, record[36])
                    ZonaEntrada.insert(0, record[37])
                    SecaoEntrada.insert(0, record[38])
                    LocaldeTrabalhoEntrada.insert(0,record[39])
                # Commit changes
                conn.commit()
                # Close connection
                conn.close()
                        
        def ProcuraInteligente():
            textbox.delete(1.0, tk.END)
            # Get the search term
            term = ProcuraEntrada.get()

            # Connect to the database
            conn = sqlite3.connect("trabalhador.db")
            cursor = conn.cursor()

            # Query the database
            cursor.execute(
                "SELECT rowid, nome_completo FROM trabalhador WHERE nome_completo LIKE ? OR grau_instrucao LIKE ? OR cpf_pessoal LIKE ? OR rg LIKE ? ORDER BY nome_completo ",
                ('%' + term + '%', '%' + term + '%', '%' + term + '%', '%' + term + '%'))
            records = cursor.fetchall()

            p_records = ""
            if len(records) > 0:
                # Create a frame inside the textbox to hold the buttons
                button_frame = ttk.Frame(textbox)

                for record in enumerate(records):
                    string= (f"{record[1]}")
                    string1=re.sub(r'\d', '', string)
                    string1=string1[2:]
                    string0=re.findall(r'\d+', string)
                    button_text=(string1.replace("(", "").replace("'", "").replace(",", "-").replace("'","").replace(")",""))
                    button = ttk.Button(button_frame,width=30, text=button_text, command=lambda pk=string0: on_button_click(pk))
                    button.pack(fill=tk.X, pady=5)
                    context_menu = tk.Menu(button_frame, tearoff=False)
                    context_menu.add_command(label="Abrir", command=lambda pk=string0: on_button_click(pk))
                    context_menu.add_command(label="Editar", command=lambda pk=string0: mostrar_botao_atualizar(pk))
                    context_menu.add_separator()
                    context_menu.add_command(label="Rotatividade", command=lambda pk=string0: on_button_click(pk))
                    context_menu.add_separator()
                    context_menu.add_command(label="Apagar", command=lambda pk=string0: delete(pk))
                    button.context_menu = context_menu  # Attach the menu to the button

                    #right-click event to show the menu
                    button.bind("<Button-3>", lambda event, button=button: button.context_menu.post(event.x_root, event.y_root))

                button_frame.grid(row=1, column=0, columnspan=2, rowspan=15, sticky=tk.N + tk.S + tk.E + tk.W)

                # Insert the button frame into the textbox
                textbox.window_create(tk.END, window=button_frame)
            else:
                p_records = "Nenhum registro encontrado."
            textbox.insert(1.0, p_records)

            # Commit changes
            conn.commit()

            # Close connection
            conn.close()

        def mostrar_todos():
            # Create a scrollbar
            scrollbar = Scrollbar(self.windowabrir)
            scrollbar.grid(row=1, column=2,rowspan=15, sticky=tk.N + tk.S)

            # Create a textbox
            global textbox
            textbox = Text(self.windowabrir, yscrollcommand=scrollbar.set,width=24,height=23)
            textbox.grid(row=1, column=0,columnspan=2,rowspan=15, sticky=tk.N + tk.S + tk.E + tk.W)
            textbox.grid_propagate(False)  # Prevent the textbox from affecting its size based on content

            # Create a frame inside the textbox to hold the buttons
            button_frame = ttk.Frame(textbox)

            # Add buttons to the frame
            conn = sqlite3.connect("trabalhador.db")
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, nome_completo FROM trabalhador ORDER BY nome_completo ")
            records = cursor.fetchall()
            
            # Create the right-click menu
            
            
            
            for record in enumerate(records):
                string= (f"{record[1]}")
                string1=re.sub(r'\d', '', string)
                string1=string1[2:]
                string0=re.findall(r'\d+', string)
                button_text=(string1.replace("(", "").replace("'", "").replace(",", "-").replace("'","").replace(")",""))
                button = ttk.Button(button_frame,width=30, text=button_text, command=lambda pk=string0: on_button_click(pk))
                button.pack(fill=tk.X, pady=5)
                context_menu = tk.Menu(button_frame, tearoff=False)
                context_menu.add_command(label="Abrir", command=lambda pk=string0: on_button_click(pk))
                context_menu.add_command(label="Editar", command=lambda pk=string0: mostrar_botao_atualizar(pk))
                context_menu.add_separator()
                context_menu.add_command(label="Rotatividade", command=lambda pk=string0: rotatividade(pk))
                context_menu.add_separator()
                context_menu.add_command(label="Apagar", command=lambda pk=string0: delete(pk))
                button.context_menu = context_menu  # Attach the menu to the button

                    #right-click event to show the menu
                button.bind("<Button-3>", lambda event, button=button: button.context_menu.post(event.x_root, event.y_root))

            button_frame.grid(row=1, column=0, columnspan=2, rowspan=15, sticky=tk.N + tk.S + tk.E + tk.W)

            # Commit changes
            conn.commit()

            # Close connection
            conn.close()

            # Calculate the width of the largest button
            max_button_width = max(button.winfo_reqwidth() for button in button_frame.winfo_children())

            # Set the width of the frame based on the button width
            button_frame.config(width=max_button_width)

            # Insert the button frame into the textbox
            textbox.window_create(tk.END, window=button_frame)

            # Configure the scrollbar to work with the textbox
            scrollbar.config(command=textbox.yview)
        
        mostrar_todos()       

        ProcuraEntrada = Entry(self.windowabrir)
        ProcuraEntrada.insert(0, 'Pesquisar')
        ProcuraEntrada.bind('<FocusIn>', on_entry_focus_in)
        ProcuraEntrada.bind('<FocusOut>', on_entry_focus_out)
        ProcuraEntrada.grid(row=0, column=0)

        ProcuraEntrada.grid(row=0,column=0)
        ProcuraBotao = Button(self.windowabrir, text="Pesquisar",command=ProcuraInteligente)
        ProcuraBotao.grid(row=0,column=1)
        MostrarTodosBotao = Button(self.windowabrir, text="Mostrar todos",command= mostrar_todos)
        MostrarTodosBotao.grid(row=17,column=0)
