import wave
from helpers.getFileExtension import getFileExtension


# from: https://stackoverflow.com/questions/43490887/check-audios-sample-rate-using-python
def isWav16kHzAudioFile(filePath: str) -> bool:
    fileExtension = getFileExtension(filePath)

    if fileExtension != ".wav":
        return False

    with wave.open(filePath, "rb") as waveFile:
        frameRate = waveFile.getframerate()

    return frameRate == 16000
