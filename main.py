from tkinter import ttk
from tkinter import messagebox
from Cadastro import *
from Abrir import *
import tkinter as tk
from tkinter import messagebox


def open_cadastrar():
    cadastrar = Cadastro()
    cadastrar.open_interface_cadastro()
    
def open_abrir():
    abrir = Abrir()
    abrir.open_interface_abrir()
    

class AuthenticationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Autenticação")
        self.root.geometry("300x100")
        self.icon=PhotoImage(file='icon.png')
        self.root.iconphoto(True,self.icon)
        
        
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Entrar", command=self.verify_password)
        self.submit_button.pack()
        
        # Bind the Return key to the password entry
        self.password_entry.bind("<Return>", lambda event: self.verify_password())      
        
    # Verificar se a senha está correta
    def verify_password(self):
        password = self.password_entry.get()
        self.root.destroy()  # Fechar a janela de autenticação
        if password == "pass":   
            open_interface()
        else:
            messagebox.showerror("Erro", "Senha incorreta.") 

def open_interface():
    root = tk.Tk()
    root.geometry("200x150")
    root.title("BD")
    icon=PhotoImage(file='icon.png')
    root.iconphoto(True,icon)
    
    frame = LabelFrame(
    root,
    text='Banco de Funcionários',
    bg='#f0f0f0',
    font=(20)
    )
    frame.pack(expand=True, fill=BOTH)
    
    label=Label(frame)
    label.pack(padx=(0,0), pady=(10, 0))

    cadastrar_button = tk.Button(frame, text="Cadastrar Funcionário",command=open_cadastrar,width=20)
    cadastrar_button.pack()
    
    procurar_button = tk.Button(frame, text="Procurar Funcionário",command=open_abrir,width=20)
    procurar_button.pack()
    
    root.mainloop()

def main():
    root = tk.Tk()
    auth_window = AuthenticationWindow(root)        
    root.mainloop()

if __name__ == '__main__':
    main()
