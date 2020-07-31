from flask import Flask, render_template, Response, request
from time import time
from consulta import consulta,insert
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
    nome_audio = f'{dados["horario"]}-{dados["file_id"]}.{(dados["file_path"])[-3:]}'
    # Grava em um arquivo as aulas
    query = "INSERT INTO aulas (id,assunto,materia,url) values (%s,%s,%s,%s);"
    resultado = insert(query,[nome_audio[:-4],dados['assunto'],dados['materia'],dados['file_path']])
    return ''

@app.route("/audio", methods=['GET'])
def home():
    query ="SELECT url FROM aulas where id = '"+request.args.get('id')+"'"
    linhas = consulta(query)
    if linhas!={}:
        r = requests.get(linhas[0]['url'], stream=True)
        return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')
    return 'error'

if __name__ == "__main__":
    app.run(debug=True)
