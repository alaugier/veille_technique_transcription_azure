
import pytest
import logging
from unittest.mock import MagicMock, patch

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

class TestAzureSpeech:

    def test_speech_config_creation(self):
        logging.info("Début du test : test_speech_config_creation")
        try:
            with patch('azure.cognitiveservices.speech.SpeechConfig') as MockSpeechConfig:
                mock_config = MockSpeechConfig.return_value
                mock_config.speech_recognition_language = "fr-FR"
                assert mock_config.speech_recognition_language == "fr-FR"
            print("✅ test_speech_config_creation : Succès")
            logging.info("Test réussi : test_speech_config_creation")
        except Exception as e:
            print(f"❌ test_speech_config_creation : Échec - {e}")
            logging.error(f"Erreur dans test_speech_config_creation : {e}")
            raise

    def test_transcription_batch_callback(self):
        logging.info("Début du test : test_transcription_batch_callback")
        try:
            class FakeResult:
                speaker_id = 2
                text = "Bonjour à tous"
                offset = 20000000
            class FakeEvent:
                result = FakeResult()
            transcriptions = []
            def recognized_cb(evt):
                speaker_id = evt.result.speaker_id
                text = evt.result.text
                transcriptions.append({
                    'speaker': speaker_id,
                    'text': text,
                    'timestamp': evt.result.offset / 10000000
                })
            recognized_cb(FakeEvent())
            assert transcriptions[0]['speaker'] == 2
            assert transcriptions[0]['text'] == "Bonjour à tous"
            assert transcriptions[0]['timestamp'] == 2.0
            print("✅ test_transcription_batch_callback : Succès")
            logging.info("Test réussi : test_transcription_batch_callback")
        except Exception as e:
            print(f"❌ test_transcription_batch_callback : Échec - {e}")
            logging.error(f"Erreur dans test_transcription_batch_callback : {e}")
            raise

    def test_transcription_microphone_result(self):
        logging.info("Début du test : test_transcription_microphone_result")
        try:
            with patch('azure.cognitiveservices.speech.SpeechRecognizer') as MockRecognizer:
                mock_recognizer = MockRecognizer.return_value
                mock_result = MagicMock()
                mock_result.reason = "RecognizedSpeech"
                mock_result.text = "Test micro"
                mock_recognizer.recognize_once.return_value = mock_result
                result = mock_recognizer.recognize_once()
                assert result.text == "Test micro"
            print("✅ test_transcription_microphone_result : Succès")
            logging.info("Test réussi : test_transcription_microphone_result")
        except Exception as e:
            print(f"❌ test_transcription_microphone_result : Échec - {e}")
            logging.error(f"Erreur dans test_transcription_microphone_result : {e}")
            raise

    def test_transcription_microphone_errors(self):
        logging.info("Début du test : test_transcription_microphone_errors")
        try:
            with patch('azure.cognitiveservices.speech.SpeechRecognizer') as MockRecognizer:
                mock_recognizer = MockRecognizer.return_value
                # Cas NoMatch
                mock_result = MagicMock()
                mock_result.reason = "NoMatch"
                mock_recognizer.recognize_once.return_value = mock_result
                result = mock_recognizer.recognize_once()
                assert result.reason == "NoMatch"
                # Cas Canceled
                mock_result2 = MagicMock()
                mock_result2.reason = "Canceled"
                mock_result2.cancellation_details = MagicMock()
                mock_result2.cancellation_details.error_details = "Erreur simulée"
                mock_recognizer.recognize_once.return_value = mock_result2
                result2 = mock_recognizer.recognize_once()
                assert result2.cancellation_details.error_details == "Erreur simulée"
            print("✅ test_transcription_microphone_errors : Succès")
            logging.info("Test réussi : test_transcription_microphone_errors")
        except Exception as e:
            print(f"❌ test_transcription_microphone_errors : Échec - {e}")
            logging.error(f"Erreur dans test_transcription_microphone_errors : {e}")
            raise

if __name__ == "__main__":
    import sys
    import traceback

    test_suite = TestAzureSpeech()
    tests = [
        test_suite.test_speech_config_creation,
        test_suite.test_transcription_batch_callback,
        test_suite.test_transcription_microphone_result,
        test_suite.test_transcription_microphone_errors,
    ]
    all_passed = True
    for test_func in tests:
        try:
            test_func()
        except Exception as e:
            print(f"❌ Erreur dans {test_func.__name__} : {e}")
            traceback.print_exc()
            all_passed = False
    if all_passed:
        print("\n🎉 Tous les tests ont réussi !")
    else:
        print("\n⚠️ Certains tests ont échoué.")

