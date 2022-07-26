# Audio_Training_Microservice
Implement a service that stores information about audio files, provides access to this information and periodically updates this data with updates from an included deep learning model.

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

For personal use

python -m venv oxus_ai_env

mkdir local

.\oxus_ai_env\Scripts\Activate.ps1

pip install -r .\requirements.txt

Added one more package PySoundFile for windows and sox for linux to support touchaudio, so replace PySoundFile with sox in requirements.txt if its linux.