from tkinter import*
import sqlite3
import tkinter as tk
from tkinter import ttk

class Cadastro:   
        def open_interface_cadastro(self):
            self.window = Toplevel() 
            self.window.geometry("1000x480")
            self.window.title("Cadastre o trabalhador")
            self.window.minsize(1100, 480)
            self.window.maxsize(1100, 480)
            self.icon=PhotoImage(file='icon.png')
            self.window.iconphoto(True,self.icon)
            
           
            i=0
            if i==0:
                        # Linha 0
                        Titulo = Label(self.window, text="Preencha as informações pessoais", font=("Arial", 15))
                        Titulo.grid(row=0, column=3+i, columnspan=3)
                        # Linha 8
                        TituloBancario = Label(self.window, text="Preencha os Dados Bancários", font=("Arial", 15))
                        TituloBancario.grid(row=8, column=3+i, columnspan=3)
                        # Linha 11
                        TituloDadosTrabalhistas = Label(self.window, text="Preencha os Documentos Pessoais Trabalhistas", font=("Arial", 15))
                        TituloDadosTrabalhistas.grid(row=11, column=3+i, columnspan=3)
                     
                    

            # Linha 1
            NomeCompletoLabel = Label(self.window, text="Nome Completo:")
            NomeCompletoLabel.grid(row=1, column=0+i)
            NomeCompletoEntrada = Entry(self.window, width=65)
            NomeCompletoEntrada.grid(row=1, column=1+i, columnspan=3)

            SexoLabel = Label(self.window, text="Sexo:")
            SexoLabel.grid(row=1, column=4+i)

            n = tk.StringVar()
            SexoEntrada = ttk.Combobox(self.window, width=17,textvariable=n)
            SexoEntrada['values'] = ('Masculino','Feminino')
            SexoEntrada.grid(row=1, column=5+i)


            # Linha 2
            DataNascimentoLabel = Label(self.window, text="Data de Nascimento:")
            DataNascimentoLabel.grid(row=2, column=0+i)
            DataNascimentoEntrada = Entry(self.window)
            DataNascimentoEntrada.grid(row=2, column=1+i)

            MunicipioNascimentoLabel = Label(self.window, text="Local de Nascimento/UF:")
            MunicipioNascimentoLabel.grid(row=2, column=2+i)
            MunicipioNascimentoEntrada = Entry(self.window)
            MunicipioNascimentoEntrada.grid(row=2, column=3+i)

            CordePeleLabel = Label(self.window, text="Cor de Pele:")
            CordePeleLabel.grid(row=2, column=4+i)
            CordePeleEntrada = Entry(self.window)
            CordePeleEntrada.grid(row=2, column=5+i)

            GrauDeInstrucaoLabel = Label(self.window, text="Grau de Instrução:")
            GrauDeInstrucaoLabel.grid(row=2, column=6+i)
            GrauDeInstrucaoEntrada = Entry(self.window)
            GrauDeInstrucaoEntrada.grid(row=2, column=7+i)

            # Linha 3
            EstadoCivilLabel = Label(self.window, text="Estado Civil:")
            EstadoCivilLabel.grid(row=3, column=0+i)
            EstadoCivilEntrada = Entry(self.window)
            EstadoCivilEntrada.grid(row=3, column=1+i)

            RegimeCasamentoLabel = Label(self.window, text="Regime de Casamento:")
            RegimeCasamentoLabel.grid(row=3, column=2+i)
            RegimeCasamentoEntrada = Entry(self.window)
            RegimeCasamentoEntrada.grid(row=3, column=3+i)

            NomeConjugeLabel = Label(self.window, text="Nome do Cônjuge:")
            NomeConjugeLabel.grid(row=3, column=4+i)
            NomeConjugeEntrada = Entry(self.window)
            NomeConjugeEntrada.grid(row=3, column=5+i)

            # Linha 4
            MaeLabel = Label(self.window, text="Mãe do trabalhador:")
            MaeLabel.grid(row=4, column=0+i)
            MaeEntrada = Entry(self.window)
            MaeEntrada.grid(row=4, column=1+i)

            PaiLabel = Label(self.window, text="Pai do trabalhador:")
            PaiLabel.grid(row=4, column=2+i)
            PaiEntrada = Entry(self.window)
            PaiEntrada.grid(row=4, column=3+i)

            # Linha 5
            RuaLabel = Label(self.window, text="Endereço Residencial:")
            RuaLabel.grid(row=5, column=0+i)
            RuaEntrada = Entry(self.window)
            RuaEntrada.grid(row=5, column=1+i)

            NumeroLabel = Label(self.window, text="Número:")
            NumeroLabel.grid(row=5, column=2+i)
            NumeroEntrada = Entry(self.window)
            NumeroEntrada.grid(row=5, column=3+i)

            BairroLabel = Label(self.window, text="Bairro:")
            BairroLabel.grid(row=5, column=4+i)
            BairroEntrada = Entry(self.window)
            BairroEntrada.grid(row=5, column=5+i)

            # Linha 6
            CidadeLabel = Label(self.window, text="Cidade:")
            CidadeLabel.grid(row=6, column=0+i)
            CidadeEntrada = Entry(self.window)
            CidadeEntrada.grid(row=6, column=1+i)

            EstadoLabel = Label(self.window, text="Estado:")
            EstadoLabel.grid(row=6, column=2+i)
            EstadoEntrada = Entry(self.window)
            EstadoEntrada.grid(row=6, column=3+i)

            CEPLabel = Label(self.window, text="CEP:")
            CEPLabel.grid(row=6, column=4+i)
            CEPEntrada = Entry(self.window)
            CEPEntrada.grid(row=6, column=5+i)

            # Linha 7
            TelefoneLabel = Label(self.window, text="Telefone Residencial:")
            TelefoneLabel.grid(row=7, column=0+i)
            TelefoneEntrada = Entry(self.window)
            TelefoneEntrada.grid(row=7, column=1+i)

            CelularLabel = Label(self.window, text="Telefone Celular:")
            CelularLabel.grid(row=7, column=2+i)
            CelularEntrada = Entry(self.window)
            CelularEntrada.grid(row=7, column=3+i)

            EmailLabel = Label(self.window, text="E-mail:")
            EmailLabel.grid(row=7, column=4+i)
            EmailEntrada = Entry(self.window)
            EmailEntrada.grid(row=7, column=5+i)

            # Linha 9
            BancoLabel = Label(self.window, text="Banco:")
            BancoLabel.grid(row=9, column=0+i)
            BancoEntrada = Entry(self.window)
            BancoEntrada.grid(row=9, column=1+i)

            AgenciaLabel = Label(self.window, text="Agência:")
            AgenciaLabel.grid(row=9, column=2+i)
            AgenciaEntrada = Entry(self.window)
            AgenciaEntrada.grid(row=9, column=3+i)

            ContaLabel = Label(self.window, text="nº da Conta:")
            ContaLabel.grid(row=9, column=4+i)
            ContaEntrada = Entry(self.window)
            ContaEntrada.grid(row=9, column=5+i)

            TipoContaLabel = Label(self.window, text="Tipo de Conta:")
            TipoContaLabel.grid(row=9, column=6+i)

            a = tk.StringVar()
            TipoContaEntrada = ttk.Combobox(self.window, width=17, textvariable=a)
            TipoContaEntrada['values'] = ('Conta Corrente','Conta Poupança')
            TipoContaEntrada.grid(row=9, column=7+i)

            # Linha 10
            PixLabel = Label(self.window, text="Pix:")
            PixLabel.grid(row=10, column=0+i)
            PixEntrada = Entry(self.window)
            PixEntrada.grid(row=10, column=1+i)

            TitularLabel = Label(self.window, text="Titular da Conta :")
            TitularLabel.grid(row=10, column=2+i)
            TitularEntrada = Entry(self.window)
            TitularEntrada.grid(row=10, column=3+i)
            
            TitularCPFLabel = Label(self.window, text="CPF do Titular:")
            TitularCPFLabel.grid(row=10, column=4+i)
            TitularCPFEntrada = Entry(self.window)
            TitularCPFEntrada.grid(row=10, column=5+i)
            
            TitularParentescoLabel = Label(self.window, text="Parentesco do Titular:")
            TitularParentescoLabel.grid(row=10, column=6+i)
            TitularParentescoEntrada = Entry(self.window)
            TitularParentescoEntrada.grid(row=10, column=7+i)
            
            
            # Linha 11
            CPFLabel = Label(self.window, text="CPF:")
            CPFLabel.grid(row=12, column=0+i)
            CPFEntrada = Entry(self.window)
            CPFEntrada.grid(row=12, column=1+i)

            PISLabel = Label(self.window, text="PIS:")
            PISLabel.grid(row=12, column=2+i)
            PISEntrada = Entry(self.window)
            PISEntrada.grid(row=12, column=3+i)

            CTPSLabel = Label(self.window, text="CTPS:")
            CTPSLabel.grid(row=12, column=4+i)
            CTPSEntrada = Entry(self.window)
            CTPSEntrada.grid(row=12, column=5+i)
            
            DataEspedicaoCPFLabel = Label(self.window, text="Data de expedição CPF:")
            DataEspedicaoCPFLabel.grid(row=12, column=6+i)
            DataEspedicaoCPFEntrada = Entry(self.window)
            DataEspedicaoCPFEntrada.grid(row=12, column=7+i)


            # Linha 13
            RGLabel = Label(self.window, text="RG:")
            RGLabel.grid(row=13, column=0+i)
            RGEntrada = Entry(self.window)
            RGEntrada.grid(row=13, column=1+i)

            ExpeditorRGLabel = Label(self.window, text="Orgão Espeditor:")
            ExpeditorRGLabel.grid(row=13, column=2+i)
            ExpeditorRGEntrada = Entry(self.window)
            ExpeditorRGEntrada.grid(row=13, column=3+i)       

            DataEspedicaoRGLabel = Label(self.window, text="Data de Expedição RG:")
            DataEspedicaoRGLabel.grid(row=13, column=4+i)
            DataEspedicaoRGEntrada = Entry(self.window)
            DataEspedicaoRGEntrada.grid(row=13, column=5+i)

            # Linha 14
            TitulodeEleitorLabel = Label(self.window, text="Titulo de Eleitor:")
            TitulodeEleitorLabel.grid(row=14, column=0+i)
            TitulodeEleitorEntrada = Entry(self.window)
            TitulodeEleitorEntrada.grid(row=14, column=1+i)

            ZonaLabel = Label(self.window, text="Zona:")
            ZonaLabel.grid(row=14, column=2+i)
            ZonaEntrada = Entry(self.window)
            ZonaEntrada.grid(row=14, column=3+i)
            
            SecaoLabel = Label(self.window, text="Seção:")
            SecaoLabel.grid(row=14, column=4+i)
            SecaoEntrada = Entry(self.window)
            SecaoEntrada.grid(row=14, column=5+i)
            
            #Linha 16
            LocaldeTrabalhoLabel = Label(self.window, text="Local de trabalho:")
            LocaldeTrabalhoLabel.grid(row=16, column=0+i)
            LocaldeTrabalhoEntrada = Entry(self.window)
            LocaldeTrabalhoEntrada.grid(row=16, column=1+i)
            
            
            def salvarDadosTrabalhador():
                # Establish a connection to the database
                conn = sqlite3.connect('trabalhador.db')
                cursor = conn.cursor()

                # Create a table if it doesn't exist
                cursor.execute('''CREATE TABLE IF NOT EXISTS trabalhador (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome_completo TEXT,
                                    sexo TEXT,
                                    data_nascimento TEXT,
                                    municipio_nascimento TEXT,
                                    cor_pele TEXT,
                                    grau_instrucao TEXT,
                                    estado_civil TEXT,
                                    regime_casamento TEXT,
                                    nome_conjuge TEXT,
                                    mae TEXT,
                                    pai TEXT,
                                    rua TEXT,
                                    numero TEXT,
                                    bairro TEXT,
                                    cidade TEXT,
                                    estado TEXT,
                                    cep TEXT,
                                    telefone_residencial TEXT,
                                    telefone_celular TEXT,
                                    email TEXT,
                                    banco TEXT,
                                    agencia TEXT,
                                    numero_conta TEXT,
                                    tipo_conta TEXT,
                                    pix TEXT,
                                    titular_conta TEXT,
                                    cpf_titular TEXT,
                                    parentesco TEXT,
                                    cpf_pessoal TEXT,
                                    pis TEXT,
                                    ctps TEXT,
                                    data_expedicao_cpf TEXT,
                                    rg TEXT,
                                    orgao_expeditor TEXT,
                                    data_expedicao_rg TEXT,
                                    titulo_eleitor TEXT,
                                    zona TEXT,
                                    secao TEXT,
                                    localdetrabalho TEXT
                                )''')

                # Get the input values from the entry fields
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
                cep = EstadoEntrada.get()
                telefone_residencial = TelefoneEntrada.get()
                telefone_celular = CelularEntrada.get()
                email = EmailEntrada.get()
                banco = BancoEntrada.get()
                agencia = AgenciaEntrada.get()
                numero_conta = ContaEntrada.get()
                tipo_conta = TipoContaEntrada.get()
                pix = PixEntrada.get()
                titular_conta = TitularEntrada.get()
                cpf = TitularCPFEntrada.get()
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

                # Insert worker data into the table
                cursor.execute('''INSERT INTO trabalhador (nome_completo, sexo, data_nascimento, municipio_nascimento, cor_pele,
                                grau_instrucao, estado_civil, regime_casamento, nome_conjuge, mae, pai, rua, numero, bairro, cidade,
                                estado, cep, telefone_residencial, telefone_celular, email, banco, agencia, numero_conta,
                                tipo_conta, pix, titular_conta, cpf_titular, parentesco, cpf_pessoal, pis, ctps, data_expedicao_cpf, rg,
                                orgao_expeditor, data_expedicao_rg, titulo_eleitor, zona, secao, localdetrabalho)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (nome_completo, sexo, data_nascimento, municipio_nascimento, cor_pele, grau_instrucao, estado_civil,
                                regime_casamento, nome_conjuge, mae, pai, rua, numero, bairro, cidade, estado, cep,
                                telefone_residencial, telefone_celular, email, banco, agencia, numero_conta, tipo_conta, pix,
                                titular_conta, cpf, parentesco, cpf_pessoal, pis, ctps, data_expedicao_cpf, rg, orgao_expeditor,
                                data_expedicao_rg, titulo_eleitor, zona, secao, localdetrabalho))

                # Commit the changes and close the connection
                conn.commit()
                conn.close()
            
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
            
            
            Barra_de_menu= tk.Menu(self.window)
            self.window.config(menu=Barra_de_menu)

            Arquivo_de_menu= Menu(Barra_de_menu,tearoff=0)
            
            Barra_de_menu.add_cascade(label="Arquivo",menu=Arquivo_de_menu)
            
            Arquivo_de_menu.add_command(label="Salvar",command=salvarDadosTrabalhador)
            Arquivo_de_menu.add_command(label="Limpar",command=limpar)
            Arquivo_de_menu.add_separator()
            Arquivo_de_menu.add_command(label="Sair",command=quit)
