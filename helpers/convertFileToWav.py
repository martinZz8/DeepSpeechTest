from os.path import basename
import subprocess


# Converts file inside filePath to ".wav" with FFMPEG tool (and using temp folder).
# Returns absolute location to newly created file (stored in temp folder)
def convertFileToWav(filePath: str, tempFolderPath: str, cwd: str) -> str:
    fileNameWithoutExtension = ".".join(basename(filePath).split(".")[:-1])
    outputFilePath = f"{tempFolderPath}/{fileNameWithoutExtension}.wav"
    processName = "ffmpeg"

    processArguments = [
        "-i",
        filePath,
        "-y",
        "-loglevel",
        "quiet",
        "-ar",
        "16000",
        outputFilePath
    ]

    lsOutput = subprocess.Popen([processName] + processArguments, cwd=cwd)
    lsOutput.communicate()  # Will block for 30 seconds

    return outputFilePath
