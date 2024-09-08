import mercadopago
import mercadopago.sdk
from dotenv import load_dotenv
import os
load_dotenv()
public_key='APP_USR-2e356ce7-212f-441f-a772-93ded887ed2d'
token = 'APP_USR-4617851042682155-090114-d6030456905af64bfe0c1bf248822567-1970432507'
public_key = f'{public_key}'
token = f'{token}'
print(public_key)
print(token)
def criar_pagamento(itens_pedido,link):
    sdk = mercadopago.SDK(token)
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome = item.item_estoque.produto.nome
        preco = float(item.item_estoque.produto.preco)
        itens.append({'title':nome,'quantity':quantidade,'unit_price':preco})
    preference_data = {
        "items": itens,
        "auto_return":"all",
        "back_urls":{"success":link,"pending":link,"failure":link}
    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]['init_point']
    id = resposta['response']['id']
    return link_pagamento,id
