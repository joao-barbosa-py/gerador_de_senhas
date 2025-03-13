import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        #Layout
        sg.theme("Dark2")
        layout = [
            [sg.Text("Site/Software", size=(10,1)),
             sg.Input(key="site", size=(20,1))],
            [sg.Text("E-mail/Usuário", size=(10,1)),
             sg.Input(key="usuario", size=(20,1))],
            [sg.Text("Quantidade de caracteres"),sg.Combo(values=list(range(30)), key="total_chars", default_value=1, size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button("Gerar Senha")]
        ]
        #Declarar Janela
        self.janela = sg.Window("Password Generator", layout)
    
    def start(self):
        while True:
            evento,valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Exit":
                break
            if evento == "Gerar Senha":
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.save_password(nova_senha, valores)
    
    def gerar_senha(self, valores):
        char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
        chars = random.choices(char_list,k=int(valores["total_chars"]))
        new_pass = "".join(chars)
        return new_pass
    
    def save_password(self, nova_senha, valores):
        with open("senhas.txt", "a", newline="") as arquivo:
            arquivo.write(f"Site: {valores['site']}, Usuario: {valores['usuario']}, Nova Senha: {nova_senha}\n")


        
        print("Arquivo Salvo")

gen = PassGen()
gen.start()