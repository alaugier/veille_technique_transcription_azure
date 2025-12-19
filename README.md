
# Veille Technique – Transcription Audio Azure Speech

## Présentation

Ce projet propose une solution de transcription audio (batch et temps réel) basée sur Azure Speech Services, intégrée dans un workflow Python modulaire et testé. Il s’inscrit dans le cadre d’une veille technique sur l’application des réseaux de neurones profonds à la prévision de séries temporelles et à la valorisation des données audio d’entreprise.

## Structure du projet


## Structure du projet

- `technical_monitoring/`
  - `main.tex`
  - `main.pdf`
  - `references.bib`
  - `README.md`
  - `unit_azure_tests/`
    - `requirements.txt`
    - `src/`
      - `config_azure_speech.py`
      - `transcription_batch.py`
      - `transcription_microphone.py`
    - `tests/`
      - `__init__.py`
      - `test_azure_speech.py`

## Installation

1. **Cloner le dépôt**  
   ```bash
   git clone https://github.com/alaugier/veille_technique_transcription_azure.git
   cd veille_technique_transcription_azure
   ```

2. Créer et activer un environnement virtuel

   ```bash
   python3 -m venv env_uaztests
   source env_uaztests/bin/activate
   ```

3. Installer les dépendances

   ```bash
   pip install -r unit_azure_tests/requirements.txt
   ```

## Utilisation

Transcription batch : voir unit_azure_tests/src/transcription_batch.py
Transcription temps réel (microphone) : voir unit_azure_tests/src/transcription_microphone.py
Configuration Azure : voir unit_azure_tests/src/config_azure_speech.py

## Lancer les tests unitaires

Vous pouvez exécuter les tests de deux façons :

- Avec pytest (recommandé) :
```bash
pytest unit_azure_tests/tests/test_azure_speech.py
```

- Ou directement :
```bash
python -m unit_azure_tests.tests.test_azure_speech
```

Les tests vérifient la configuration, la logique de transcription, la gestion des erreurs et utilisent des mocks pour simuler l’environnement Azure.

## Dépendances principales

- azure-cognitiveservices-speech
- pytest

Voir unit_azure_tests/requirements.txt pour la liste complète.

## Bonnes pratiques

- Les scripts sont organisés en classes pour faciliter la maintenance et les tests.
- Les tests unitaires sont automatisés et loggués pour garantir la robustesse du code.
- Un fichier requirements.txt permet de reproduire l’environnement facilement.

## Licence

## Liens utiles 

[Azure AI-Services speech service](http://learn.microsoft.com/fr-fr/azure/ai-services/speech-service/)

[Pytest documentation](http://docs.pytest.org/fr/latest/)
