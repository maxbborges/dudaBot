import os
from os.path import join, dirname
from dotenv import load_dotenv
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#leitura dos arquivos .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#integração com ibm watson
ibm_token = os.environ.get("API_KEY_IBM")
api = IAMAuthenticator(ibm_token)
speech_to_text = SpeechToTextV1(authenticator=api)
url_service_ibm = os.environ.get("URL_IBM")
speech_to_text.set_service_url(url_service_ibm)

def Audio_To_Text(fileName):
    with open(fileName, 'rb') as audio_file:
        result = speech_to_text.recognize(
            audio=audio_file, content_type="audio/mp3"
        ).get_result()
    print(result)