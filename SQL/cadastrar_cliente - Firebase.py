

def cadastrar_cliente():
    conexao = #####.connect('clientes.db')
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

