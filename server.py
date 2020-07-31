from flask import Flask, render_template, Response, request
from funDownload import download
from time import time
import requests
import json

app = Flask(__name__, static_url_path='')

@app.route("/",methods=['GET'])
def apresentacao():
    return 'apresentacao'

@app.route("/tratarAudio", methods=['POST'])
def main():
    dados = json.loads((request.data).decode('utf8').replace("'", '"'))
    name_audio = f'{time()}-{dados["file_id"]}.{(dados["file_path"])[-3:]}'
    print (dados['file_path'])
    download(url=f'{dados["file_path"]}', fileName=name_audio)
    return ''

@app.route("/audio", methods=['GET', 'POST'])
def home():
    r = requests.get('https://api.telegram.org/file/bot975682863:AAF1Fu-98mW8tttIPjzjHWb8l8h5fqgLt30/voice/file_55.oga', stream=True)
    return Response(r.iter_content(chunk_size=1024), mimetype='audio/mpeg')

if __name__ == "__main__":
    app.run(debug=True)
