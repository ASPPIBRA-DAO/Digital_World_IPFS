import qrcode

meu_qrcode = qrcode.make("https://**********")
meu_qrcode.save("qrcode_********.png")

links_produtos = {
    "Face": "https://*********",
    "Body": "https://",
    "Perfil": "https://",
    "Avatar": "https://",
    "Historico": "https://",
    "Genealogia": "https://",
}

for produto in links_produtos:
    link = links_produtos[produto]
    meu_qrcode = qrcode.make(links_produtos[produto])
    meu_qrcode.save(f"qrcode_{produto}.png")