# Bibliotecas
from flask import Flask, render_template, Response, request
from time import time
import requests
import json
from base64 import b64decode, b64encode
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse

# Arquivos
from servidor.consulta import consulta,insert
from servidor.config import configuracoes,credenciais

app = Flask(__name__, static_url_path='')

@app.route("/",methods=['GET'])
def main():
    return 'ok'

@app.route("/ligar",methods=['GET','POST'])
def apresentacao():
    url = configuracoes['URL_SERVER']
    id_aula = request.args.get('id')
    print ('Criando sessão.')
    client = Client(b64decode(credenciais['TWILIO_SID']).decode('utf-8'), b64decode(credenciais['TWILIO_TOKEN']).decode('utf-8'))

    # call = client.calls.create(
    #                     url=url+'aula?id='+id_aula,
    #                     to='+5561984185161',
    #                     from_=configuracoes['TWILIO_NUMBER']
    #                 )
    # print ('Realizando ligação.')
    # return ''

@app.route("/tratarAudio", methods=['POST'])
def tratarAudio():
    # Recupera os dados enviados via POST
    dados = json.loads((request.data).decode('utf8').replace("'", '"'))
    # Define o nome do arquivo
    nome_audio = f'{dados["horario"]}-{dados["file_id"]}.{(dados["file_path"])[-3:]}'
    # Grava em um arquivo as aulas
    query = "INSERT INTO aulas (id,assunto,materia,url) values (%s,%s,%s,%s);"
    resultado = insert(query,[nome_audio[:-4],dados['assunto'],dados['materia'],dados['file_path']])
    client = Client(credenciais['TWILIO_SID'], credenciais['TWILIO_TOKEN'])

    RECIPENT_NUMBER = dados['numeros']
    TWILIO_NUMBER = configuracoes['TWILIO_NUMBER']
    SMS_MESSAGE = 'Acesse: '+configuracoes['URL_SERVER']+'audio?id='+str(dados["horario"])+'-'+dados["file_id"]+' ou ligue '+TWILIO_NUMBER+' para ouvir sua aula de '+dados["materia"]+'-'+dados["assunto"]+'!'

    message = client.messages.create(
        to=RECIPENT_NUMBER,
        from_=TWILIO_NUMBER,
        body=SMS_MESSAGE
        )
    return ''

@app.route("/aula", methods=['GET','POST'])
def audio():
    id_aula = request.args.get('id')
    print ('Consultado aula com id ' +id_aula+ ', aguarde...')
    query ="SELECT url,materia,assunto FROM aulas where id = '"+id_aula+"'"
    linhas = consulta(query)
    if linhas!={}:
        print ('Foi encontrado aula com o id referenciado. Criando página...')
        response = VoiceResponse()
        response.say("A aula de {}-{} será reproduzida em instantes.".format(linhas[0]['materia'],linhas[0]['assunto']), language='pt-BR')
        response.play(configuracoes['URL_SERVER']+'audio?id='+id_aula)
        response = response.to_xml()
        return response, 200, {'Content-Type': 'text/xml; charset=utf-8'}
    return 'error'

@app.route("/audio", methods=['GET','POST'])
def home():
    id_aula = request.args.get('id')
    print ('Consultado audio com id ' +id_aula+ ', aguarde...')
    query ="SELECT url FROM aulas where id = '"+id_aula+"'"
    linhas = consulta(query)
    if linhas!={}:
        r = requests.get(linhas[0]['url'], stream=True)
        return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')
    return 'error'

if __name__ == "__main__":
    app.run(debug=True)
