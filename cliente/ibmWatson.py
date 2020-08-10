#Bibliotecas
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from base64 import b64decode, b64encode

#Arquivos
from cliente.config import credenciais,configuracoes

#integração com ibm watson
ibm_token = b64decode(credenciais['API_KEY_IBM']).decode('utf-8')
api = IAMAuthenticator(ibm_token)
speech_to_text = SpeechToTextV1(authenticator=api)
url_service_ibm = configuracoes['URL_IBM']
speech_to_text.set_service_url(url_service_ibm)

def Audio_To_Text(fileName):
    with open(fileName, 'rb') as audio_file:
        result = speech_to_text.recognize(
            audio=audio_file, content_type="audio/mp3"
        ).get_result()
    print(result)
