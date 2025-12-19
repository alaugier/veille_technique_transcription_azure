
import azure.cognitiveservices.speech as speechsdk

class MicrophoneTranscriber:
    def __init__(self, speech_config):
        self.audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=self.audio_config
        )

    def recognize(self):
        print("Parlez dans le microphone...")
        result = self.recognizer.recognize_once()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"Transcription : {result.text}")
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("Aucune parole detectee.")
            return None
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"Erreur : {cancellation.error_details}")
            return None
