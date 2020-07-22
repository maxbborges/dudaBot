'''
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticators = IAMAuthenticator("K2j5Kam_qa-DC42ViBkt0KKsIfvPIsQeMGSITBARGjDR")
speech_to_text = SpeechToTextV1(authenticator=authenticators)
speech_to_text.set_service_url("https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/895b7f88-720c-4d74-9838-ce7bbc917b76")
'''

import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('TOKEN_IBM')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('URL_IBM')

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

myRecognizeCallback = MyRecognizeCallback()

with open(join(dirname(__file__), './.', 'audio-file.mp3'),
              'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/mp3',
        recognize_callback=myRecognizeCallback,
        model='en-US_BroadbandModel',
        keywords=['colorado', 'tornado', 'tornadoes'],
        keywords_threshold=0.5,
        max_alternatives=3)