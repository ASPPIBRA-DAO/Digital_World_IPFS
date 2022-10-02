import tkinter as tk
import sqlite3
import pandas as pd


#Criando Janela:

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela. geometry("330x350")


def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                'id_banco':entry_id_banco.get(),
                  'id_ipfs:':entry_id_ipfs.get(),
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'nome_social': entry_nome_social.get(),
                  'voz': entry_voz.get(),
                  'face': entry_face.get(),
                  'rg': entry_rg.get(),
                  'cpf': entry_cpf.get(),
                  'sexo': entry_sexo.get(),
                  'idade': entry_idade.get(),
                  'estatura': entry_estatura.get(),
                  'idioma': entry_idioma.get(),
                  'cor_pele': entry_cor_pele.get(),
                  'fator_rh': entry_fator_rh.get(),
                  'peso_kg': entry_peso_kg.get(),
                  'filhos': entry_filhos.get(),
                  'profissao': entry_profissao.get(),
                  'data_nascimento':entry_data_nascimento.get(),
                  'estado_civil':entry_estado_civil.get(),
                  'pais_origem': entry_pais_origem.get(),
                  'assinatura': entry_assinatura.get(),
                  'avatar': entry_avatar.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0,"end")
    entry_email.delete(0,"end")
    entry_telefone.delete(0,"end")

def exporta_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    # print(clientes_cadastrados)
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=[
      'id_banco',
        'id_ipfs:',
        'nome',
        'sobrenome',
        'nome_social',
        'voz',
        'face',
        'rg',
        'cpf',
        'sexo',
        'idade',
        'estatura',
        'idioma',
        'cor_pele',
        'fator_rh',
        'peso_kg',
        'filhos',
        'profissao',
        'data_nascimento',
        'estado_civil',
        'pais_origem',
        'assinatura',
        'avatar',
        'email',
        'telefone'
    ])
    clientes_cadastrados.to_excel('clientes.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


#Rótulos Entradas:

label_id_ipfs = tk.Label(janela, text='id_ipfs')
label_id_ipfs.grid(row=0,column=0, padx=10, pady=10)

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_nome_social = tk.Label(janela, text='nome_social')
label_nome_social.grid(row=0,column=0, padx=10, pady=10)

label_voz = tk.Label(janela, text='voz')
label_voz.grid(row=0,column=0, padx=10, pady=10)

label_face = tk.Label(janela, text='face')
label_face.grid(row=0,column=0, padx=10, pady=10)

label_rg = tk.Label(janela, text='rg')
label_rg.grid(row=0,column=0, padx=10, pady=10)

label_cpf = tk.Label(janela, text='cpf')
label_cpf.grid(row=0,column=0, padx=10, pady=10)

label_sexo = tk.Label(janela, text='sexo')
label_sexo.grid(row=0,column=0, padx=10, pady=10)

label_idade = tk.Label(janela, text='idade')
label_idade.grid(row=0,column=0, padx=10, pady=10)

label_estatura = tk.Label(janela, text='estatura')
label_estatura.grid(row=0,column=0, padx=10, pady=10)

label_idioma = tk.Label(janela, text='idioma')
label_idioma.grid(row=0,column=0, padx=10, pady=10)

label_cor_pele = tk.Label(janela, text='cor_pele')
label_cor_pele.grid(row=0,column=0, padx=10, pady=10)

label_fator_rh = tk.Label(janela, text='fator_rh')
label_fator_rh.grid(row=0,column=0, padx=10, pady=10)

label_peso_kg = tk.Label(janela, text='peso_kg')
label_peso_kg.grid(row=0,column=0, padx=10, pady=10)

label_filhos = tk.Label(janela, text='filhos')
label_filhos.grid(row=0,column=0, padx=10, pady=10)

label_profissao = tk.Label(janela, text='profissao')
label_profissao.grid(row=0,column=0, padx=10, pady=10)

label_data_nascimento = tk.Label(janela, text='data_nascimento')
label_data_nascimento.grid(row=0,column=0, padx=10, pady=10)

label_estado_civil = tk.Label(janela, text='estado_civil')
label_estado_civil.grid(row=0,column=0, padx=10, pady=10)

label_pais_origem = tk.Label(janela, text='pais_origem')
label_pais_origem.grid(row=0,column=0, padx=10, pady=10)

label_assinatura = tk.Label(janela, text='assinatura')
label_assinatura.grid(row=0,column=0, padx=10, pady=10)

label_avatar = tk.Label(janela, text='avatar')
label_avatar.grid(row=0,column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0 , padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#Caixas Entradas:

entry_id_ipfs = tk.Entry(janela , width =35)
entry_id_ipfs.grid(row=0,column=1, padx=10, pady=10)

entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width =35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_nome_social = tk.Entry(janela , width =35)
entry_nome_social.grid(row=0,column=1, padx=10, pady=10)

entry_voz = tk.Entry(janela , width =35)
entry_voz.grid(row=0,column=1, padx=10, pady=10)

entry_face = tk.Entry(janela , width =35)
entry_face.grid(row=0,column=1, padx=10, pady=10)

entry_rg = tk.Entry(janela , width =35)
entry_rg.grid(row=0,column=1, padx=10, pady=10)

entry_cpf = tk.Entry(janela , width =35)
entry_cpf.grid(row=0,column=1, padx=10, pady=10)

entry_sexo = tk.Entry(janela , width =35)
entry_sexo.grid(row=0,column=1, padx=10, pady=10)

entry_idade = tk.Entry(janela , width =35)
entry_idade.grid(row=0,column=1, padx=10, pady=10)

entry_estatura = tk.Entry(janela , width =35)
entry_estatura.grid(row=0,column=1, padx=10, pady=10)

entry_idioma = tk.Entry(janela , width =35)
entry_idioma.grid(row=0,column=1, padx=10, pady=10)

entry_cor_pele = tk.Entry(janela , width =35)
entry_cor_pele.grid(row=0,column=1, padx=10, pady=10)

entry_fator_rh = tk.Entry(janela , width =35)
entry_fator_rh.grid(row=0,column=1, padx=10, pady=10)

entry_peso_kg = tk.Entry(janela , width =35)
entry_peso_kg.grid(row=0,column=1, padx=10, pady=10)

entry_filhos = tk.Entry(janela , width =35)
entry_filhos.grid(row=0,column=1, padx=10, pady=10)

entry_profissao = tk.Entry(janela , width =35)
entry_profissao.grid(row=0,column=1, padx=10, pady=10)

entry_data_nascimento = tk.Entry(janela , width =35)
entry_data_nascimento.grid(row=0,column=1, padx=10, pady=10)

entry_estado_civil = tk.Entry(janela , width =35)
entry_estado_civil.grid(row=0,column=1, padx=10, pady=10)

entry_pais_origem = tk.Entry(janela , width =35)
entry_pais_origem.grid(row=0,column=1, padx=10, pady=10)

entry_assinatura = tk.Entry(janela , width =35)
entry_assinatura.grid(row=0,column=1, padx=10, pady=10)

entry_avatar = tk.Entry(janela , width =35)
entry_avatar.grid(row=0,column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width =35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width =35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=5, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)


janela.mainloop()