from flask import Flask, render_template, Response, request
from time import time
from consulta import consulta,insert
import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

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
    print (resultado)

    # TWILIO_SID = os.environ.get('TWILIO_SID')
    # TWILIO_TOKEN  = os.environ.get('TWILIO_TOKEN')
    client = Client('ACdbd1d522bfef46b2bef87bda83e2ade5', '5fa809a444d03865426283073985addc')

    RECIPENT_NUMBER = dados['numeros']
    TWILIO_NUMBER = '+18566663241'
    SMS_MESSAGE = 'Acesse: https://hackdudabot.herokuapp.com/audio?id='+str(dados["horario"])+'-'+dados["file_id"]+' ou ligue para +18566663241 para ouvir sua aula de '+dados["materia"]+'-'+dados["assunto"]+'!'

    message = client.messages.create(
        to=RECIPENT_NUMBER,
        from_=TWILIO_NUMBER,
        body=SMS_MESSAGE
        )
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
    # app.run(debug=True,host='0.0.0.0',port=8000)
