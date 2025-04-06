import subprocess
#import sys
#from os.path import dirname
#sys.path.append(dirname(dirname(__file__)))
from modelPaths import ModelPaths


def transcriptFile(filePathToTranscript: str, outputFilePath: str, currentModelPath: ModelPaths, cwd: str):
    processName = "deepspeech"

    processArguments = [
        "--model",
        currentModelPath.modelPath,
        "--scorer",
        currentModelPath.scorerPath,
        "--audio",
        filePathToTranscript
    ]

    # Open the file "outputFilePath" and run the process
    with open(outputFilePath, "w", encoding="utf-8") as stdout:
        lsOutput = subprocess.Popen([processName] + processArguments, stdout=stdout, cwd=cwd)
        lsOutput.communicate()  # Will block for 30 seconds
