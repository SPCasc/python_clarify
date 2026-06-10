from flask import Flask, request, jsonify
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Declara o objeto da aplicação - ao concluir a linha abaixo, é recomendável escrever a linha do if abaixo do outro rashtag informando o inicia o servidor flash
app = Flask(__name__)

@app.route("/consultar_ibge/<nome>", methods=["GET"])
def consultarIbge(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?nome={nome}"
    resposta = requests.get(url)
    dados = resposta.json()
    #vamos criar agora um data frame - uma estrutura de dados
    tabela = pd.DataFrame(dados[0]["res"])
    #vamos criar a imagem do excel - chamado de figura (fig). O 'ax' significa o axis da reta X 
    fig, ax = plt.subplots()
    ax.bar(tabela["nome"], tabela["frequencia"])
    ax.set_xlabel("nome")
    ax.set_ylabel("frequencia")
    plt.show()


# Inicia o servidor flask no endereço Localhost
if __name__ == "__main__":
    app.run(debug=True)

#acesso por http://127.0.0.1:5000/consultar_ibge/caio
