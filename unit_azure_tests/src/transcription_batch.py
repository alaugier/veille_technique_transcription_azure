
import azure.cognitiveservices.speech as speechsdk
import time

class BatchTranscriber:
    def __init__(self, speech_config, audio_filename):
        self.speech_config = speech_config
        self.audio_config = speechsdk.audio.AudioConfig(filename=audio_filename)
        self.speech_config.set_property(
            speechsdk.PropertyId.SpeechServiceConnection_EnableSpeakerDiarization, "true"
        )
        self.speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            audio_config=self.audio_config
        )
        self.transcriptions = []

    def recognized_cb(self, evt):
        speaker_id = evt.result.speaker_id
        text = evt.result.text
        self.transcriptions.append({
            'speaker': speaker_id,
            'text': text,
            'timestamp': evt.result.offset / 10000000
        })
        print(f"[Locuteur {speaker_id}] {text}")

    def transcribe(self, duration=60):
        self.speech_recognizer.recognized.connect(self.recognized_cb)
        print("Demarrage de la transcription...")
        self.speech_recognizer.start_continuous_recognition()
        time.sleep(duration)
        self.speech_recognizer.stop_continuous_recognition()
        print(f"Transcription terminee. {len(self.transcriptions)} segments detectes.")
        return self.transcriptions
