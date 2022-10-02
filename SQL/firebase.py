import firebase_admin
from firebase_admin import credentials
import requests
import json
import pyrebase


firebaseConfig = {
  apiKey: "AIzaSyBXKIBhOKQuiX8g6fF8NBRA5jGVqzzz6ls",
  authDomain: "novo-mundo-46d03.firebaseapp.com",
  databaseURL: "https://novo-mundo-46d03-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "novo-mundo-46d03",
  storageBucket: "novo-mundo-46d03.appspot.com",
  messagingSenderId: "995186946108",
  appId: "1:995186946108:web:ab3a0485c4b929934e1339",
  measurementId: "G-3MG8J8Q5PW"
};

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin=pyrebase.initialize_app(cred)

link = "https://novo-mundo-46d03-default-rtdb.asia-southeast1.firebasedatabase.app/"



# Criar uma venda (POST)
dados = {'cliente': 'alon', 'preco': 150, 'produto': 'teclado'}
requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Criar um novo produto (POST)
dados = {'nome': 'teclado', 'preco': 150, 'quantidade': 80}
requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Editar a venda (PATCH)
dados = {'cliente': 'lira'}
requisicao = requests.patch(f'{link}/Vendas/-MyJSm_N0S8KhCc3nAku/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Pegar uma venda específico ou todas as vendas (GET)
requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
id_alon = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == "alon":
        print(id_venda)
        id_alon = id_venda

# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_alon}/.json')
print(requisicao)
print(requisicao.text)