'''
5. Escreva a função obter_colecao_mongodb(url_conexao, colecao) que irá se
conectar no MogodDB utilizando alguma biblioteca do Python. Ela possui os
seguintes parâmetros:
○ url_conexao: URI de conexão com banco de dados MongoDB, que também
informa a base de dados (database). Por exemplo: a URI
`mongodb://localhost/bancoexemplo', é a string de conexão para o banco
"bancoexemplo" da minha máquina local ("localhost").
○ colecao: É o nome da coleção (collection) do MongoDB que estaremos
acessando com esta função.
'''

from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    conn = MongoClient(url_conexao)
    col = conn[colecao]
    return col

if __name__ == '__main__':

    url_conexao = 'mongodb+srv://eronmorais:Bfohux0404*@magalu.ajidewl.mongodb.net/test'
    colecao = 'produto'

    conexao = obter_colecao_mongodb(url_conexao, colecao)
    print(conexao)