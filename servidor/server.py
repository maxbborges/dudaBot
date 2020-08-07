# Bibliotecas
from flask import Flask, render_template, Response, request
from time import time
import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client

from twilio.twiml.voice_response import Play, VoiceResponse

# Arquivos
from servidor.consulta import consulta,insert

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__, static_url_path='')

@app.route("/",methods=['GET','POST'])
def apresentacao():
    url = os.environ.get("URL_SERVER")
    id_aula = request.args.get('id')
    client = Client('ACdbd1d522bfef46b2bef87bda83e2ade5', '5fa809a444d03865426283073985addc')
    call = client.calls.create(
                        url=url+'aula?id='+id_aula,
                        to='+5561984185161',
                        from_='+18566663241'
                    )
    return ''

@app.route("/tratarAudio", methods=['POST'])
def main():
    # Recupera os dados enviados via POST
    dados = json.loads((request.data).decode('utf8').replace("'", '"'))
    # Define o nome do arquivo
    nome_audio = f'{dados["horario"]}-{dados["file_id"]}.{(dados["file_path"])[-3:]}'
    # Grava em um arquivo as aulas
    query = "INSERT INTO aulas (id,assunto,materia,url) values (%s,%s,%s,%s);"
    resultado = insert(query,[nome_audio[:-4],dados['assunto'],dados['materia'],dados['file_path']])
    client = Client('TWILIO_SID', 'TWILIO_TOKEN')

    RECIPENT_NUMBER = dados['numeros']
    TWILIO_NUMBER = '+18566663241'
    SMS_MESSAGE = 'Acesse: https://hackdudabot.herokuapp.com/audio?id='+str(dados["horario"])+'-'+dados["file_id"]+' ou ligue para +18566663241 para ouvir sua aula de '+dados["materia"]+'-'+dados["assunto"]+'!'

    message = client.messages.create(
        to=RECIPENT_NUMBER,
        from_=TWILIO_NUMBER,
        body=SMS_MESSAGE
        )
    return ''

@app.route("/aula", methods=['GET','POST'])
def audio():
    id_aula = request.args.get('id')
    query ="SELECT url,materia,assunto FROM aulas where id = '"+id_aula+"'"
    linhas = consulta(query)
    url = os.environ.get("URL_SERVER")
    if linhas!={}:
        response = VoiceResponse()
        response.say("A aula de {}-{} será reproduzida em instantes.".format(linhas[0]['materia'],linhas[0]['assunto']), language='pt-BR')
        response.play(url+'audio?id='+id_aula)
        response = response.to_xml()
        return response, 200, {'Content-Type': 'text/xml; charset=utf-8'}
    return 'error'

@app.route("/audio", methods=['GET','POST'])
def home():
    query ="SELECT url FROM aulas where id = '"+request.args.get('id')+"'"
    linhas = consulta(query)
    print (linhas)
    if linhas!={}:
        print (linhas[0]['url'])
        r = requests.get(linhas[0]['url'], stream=True)
        return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')
    return 'error'


# @app.route("/teste",methods=['GET','POST'])
# def teste():
#     response = VoiceResponse()
#     response.say("A aula de Portugues será reproduzida em instantes.", language='pt-BR')
#     response.play('https://api.twilio.com/cowbell.mp3')
#     response = response.to_xml()
#     return response, 200, {'Content-Type': 'text/xml; charset=utf-8'}

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=8000)
