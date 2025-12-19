
import azure.cognitiveservices.speech as speechsdk
import os

class AzureSpeechConfig:
    def __init__(self, language="fr-FR", region="westeurope"):
        self.speech_key = os.environ.get('AZURE_SPEECH_KEY')
        self.region = region
        self.language = language
        self.speech_config = speechsdk.SpeechConfig(
            subscription=self.speech_key,
            region=self.region
        )
        self.speech_config.speech_recognition_language = self.language

    def get_config(self):
        return self.speech_config