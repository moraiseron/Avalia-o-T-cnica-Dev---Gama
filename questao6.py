'''
6. O DBA da empresa criou um script para fazer uma atualização no banco de dados
MongoDB:
var sku = "" // a pessoa informa o sku aqui
var estoque = 0 // valor a ser informado do novo estoque
db.produto.update(
{
    sku: sku
},
{
    $inc: estoque
}
)
O problema que esse script está em JavaScript do MongoDB. Logo, escreva para
nós a função Python ajustar_estoque() com o seus devidos parâmetros para que
realize a atualização na coleção produto conforme o script que o DBA passou para
nós.
'''

from pymongo import MongoClient

url_conexao = 'mongodb+srv://eronmorais:Bfohux0404*@magalu.ajidewl.mongodb.net/test'
client = MongoClient(url_conexao)

collection = client.gama.produto


def ajustar_estoque(sku, estoque, collection):
    collection.update_one({"sku": sku}, {"$set": {"estoque": estoque}})


if __name__ == '__main__':
    sku = input('Digite o sku ')
    estoque = int(input('Qual o estoque '))

    ajustar_estoque(sku, estoque, collection)