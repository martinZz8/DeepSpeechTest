Based on: https://deepspeech.readthedocs.io/en/v0.9.3/

** How to launch the deepspeech tool (from the cmd) **:
Note: Use Python 3.9, previous installation of this version needed (if there's need to create env, do it via "py -3 -m virtualenv --python=3.9 env")
1. Launch the virtualenv using: cmd -> powershell -> env\Scripts\activate
2. Install needed dependencies: python -m pip install -r requirements.txt
Note: To export dependencies we can use: python -m pip freeze > requirements.txt
3. Download needed models (and place them inside "data/models" folder of the project:
- model: https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
- scorer: https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
4. Run transcription of audio file:
deepspeech --model data/model/english/deepspeech-0.9.3-models.pbmm --scorer data/model/english/deepspeech-0.9.3-models.scorer --audio data/audio/english/audio_2.wav > data/output/output.txt

Note:
- We need to use .wav files only in sampling of 16000Hz (16MHz)
- If we have other audio types, just convert them to .wav before transcription

** How to launch the project (to process more files) **:
1. Launch and prepare virtualenv as in the case above (steps 1-3)
2. Specify options of the program inside "-- Options --" section of "main.py" script (to find your needs of which files to process)
3. In the terminal, type: python main.py

-- Used models --
1. English (from: https://deepspeech.readthedocs.io/en/v0.9.3/):
- model: https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
- scrorer: https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
2. Polish: (from: https://www.kaggle.com/code/jimregan/polish-deepspeech-models)

Note: To get data (models and audio), search them on my MediaFire account or outer disc drive

-- FFMPEG --
1. ffmpeg download: https://www.gyan.dev/ffmpeg/builds/
2. ffmpeg documentation: https://ffmpeg.org/ffmpeg.html
3. Note, that ffmpeg tool location should be added to Windows PATH env variable
4. Example of changing MP3 -> WAV (with 16kHz audio sampling frequency)
ffmpeg -i example_1.mp3 -y -loglevel quiet -ar 16000 example_1.wav