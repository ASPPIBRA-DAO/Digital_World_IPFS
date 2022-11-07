

def cadastrar_endereço():
    conexao = #########.connect('clientes.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO endereço VALUES (:continente,:pais,:estado,:municipio,:bairro)",
              {
                  'continente': entry_continente.get(),
                  'pais': entry_pais.get(),
                  'populaçao': entry_população.get(),
                  'extençao_territorial': entry_extençao_territorial.get(),
                  'bandeira': entry_bandeira.get(),
                  'idioma': entry_idioma.get(),
                  'moeda': entry_moeda.get(),
                  'estado': entry_estado.get(),
                  'uf': entry_uf.get(),
                  'municipio': entry_municipio.get(),
                  'bairro': entry_bairro.get(),
                  'rua': entry_rua.get(),
                  'quadra': entry_quadra.get(),
                  'lote': entry_lote.get(),
                  'geolocalizaçao': entry_geolocalizaçao.get(),
                  'cep': entry_cep.get()
              })





