from tkinter import *
from cryptography.fernet import Fernet

# Função para descriptografar
def descriptografar():
    # Obtém o texto criptografado da Entrada1
    mensagem_criptografada = Entrada1.get()
    try:
        # Converte a representação em bytes
        mensagem_criptografada_bytes = mensagem_criptografada.encode()
        # Descriptografa os bytes e converte de volta para string
        mensagem_descriptografada = fernet.decrypt(mensagem_criptografada_bytes).decode()
        # Limpa o conteúdo atual da Entrada2
        Entrada2.delete(0, END)
        # Insere a mensagem descriptografada na Entrada2
        Entrada2.insert(0, mensagem_descriptografada)
    except Exception as e:
        print("Erro ao descriptografar:", str(e))

# Gere uma chave Fernet
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Mensagem que você deseja criptografar
mensagem = "ola"

# Criptografe a mensagem usando a chave Fernet
mensagem_criptografada = fernet.encrypt(mensagem.encode()).decode()

# Criação da janela tkinter
janela = Tk()
janela.geometry("500x500")
janela.title("Descriptografia")
janela.config(bg="lightblue")
janela.config(background="#dde")

# Rótulo para indicar que a entrada é o texto criptografado
Label(janela, text="TEXTO CRIPTOGRAFADO", background="#dde", foreground="#009", anchor=W).place(x=46, y=108, width=135, height=20)

# Entrada1 para inserir o texto criptografado
Entrada1 = Entry(janela)
Entrada1.place(relx=.1, rely=0.25, relheight=.040, relwidth=.8)
Entrada1.insert(0, mensagem_criptografada)  # Insere a mensagem criptografada na Entrada1

# Botão para descriptografar
botao = Button(janela, text="Descriptografar", foreground="white", bg="green", command=descriptografar)
botao.place(relx=0.1, rely=0.30)

# Entrada2 para exibir o texto descriptografado
Entrada2 = Entry(janela)
Entrada2.place(relx=.1, rely=0.40, relheight=.040, relwidth=.8)

# Inicialização da janela tkinter
janela.mainloop()
