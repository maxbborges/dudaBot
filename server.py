from flask import Flask, render_template, Response, request
from time import time
import requests
import json

app = Flask(__name__, static_url_path='')

@app.route("/",methods=['GET'])
def apresentacao():
    return 'apresentacao'

@app.route("/tratarAudio", methods=['POST'])
def main():
    # Recupera os dados enviados via POST
    dados = json.loads((request.data).decode('utf8').replace("'", '"'))
    # Define o nome do arquivo
    nome_audio = f'{time()}-{dados["file_id"]}.{(dados["file_path"])[-3:]}'
    # Grava em um arquivo as aulas
    with open('aulas.json', 'a+') as f:
        f.write('''{"id":"'''+nome_audio[:-4]+'''","assunto":"'''+dados['assunto']+'''","materia":"'''+dados['materia']+'''","url":"'''+dados['file_path']+'''"}''')
    return ''

@app.route("/audio", methods=['GET'])
def home():
    # abre o arquivo com as aulas
    linhas = open("aulas.json", "r")
    # Ler linha por linha, caso não encontre, retorna 0. *parametro: ?id=ID_AUDIO
    for linha in linhas:
        id = (json.loads(linha))['id']
        url = (json.loads(linha))['url']
        parametro = request.args.get('id')

        if(parametro==id):
            r = requests.get(url, stream=True)
            linhas.close()
            return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')

    linhas.close()
    return ''

if __name__ == "__main__":
    app.run(debug=True)
