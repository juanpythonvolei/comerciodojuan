import mercadopago
import mercadopago.sdk
from dotenv import load_dotenv
import os
load_dotenv()
public_key=f"{os.getenv('PUBLIC_KEY')"
token = f"{os.getenv('TOKEN')"
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
