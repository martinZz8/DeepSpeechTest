from os import listdir
from os.path import dirname, isfile, join, basename
import subprocess
from modelPaths import ModelPaths, AvailableLanguagesEnum
from helpers.getFileExtension import getFileExtension


def main():
    # -- Determine cwd --
    cwd = dirname(__file__)

    # -- Options --
    availableExtensions = [".wav"]
    folderNameToProcess = "data/audio/english"  # None or folder path relative to cwd
    # Specify file names to transcript (relative path to cwd)
    # Note: if variable "folderNameToProcess" is specified, this variable is overridden
    filePathsToTranscript = [
        "data/audio/english/audio_2.wav",
        "data/audio/polish/audio_1.wav"
    ]
    outputFolder = "data/output"  # Path relative to cwd
    outputFileSuffix = "output"
    modelPaths = {
        "english": ModelPaths(
            AvailableLanguagesEnum.ENGLISH,
            "data/model/english/deepspeech-0.9.3-models.pbmm",
            "data/model/english/deepspeech-0.9.3-models.scorer"
        ),
        "polish": ModelPaths(
            AvailableLanguagesEnum.POLISH,
            "data/model/polish/output_graph_pl.pbmm",
            "data/model/polish/kenlm_pl.scorer"
        )
    }

    # -- Specify "filePathsToTranscript" (if "folderNameToProcess" is specified) --
    if folderNameToProcess is not None:
        absolutePathToAudioFolder = join(cwd, folderNameToProcess)
        filePathsToTranscript = [
            f"{folderNameToProcess}/{f}"
            for f in listdir(absolutePathToAudioFolder)
            if isfile(join(absolutePathToAudioFolder, f)) and (getFileExtension(f) in availableExtensions)
        ]

    # -- Transcript files --
    # Determine process name
    processName = "deepspeech"

    for (idx, filePathToTranscript) in enumerate(filePathsToTranscript):
        # Determine the language the audio file is using
        currentLanguage: AvailableLanguagesEnum = AvailableLanguagesEnum.ENGLISH
        languageFolderName = filePathToTranscript.split("/")[2]

        if languageFolderName == AvailableLanguagesEnum.POLISH.name.lower():
            currentLanguage = AvailableLanguagesEnum.POLISH

        if languageFolderName == AvailableLanguagesEnum.OTHER.name.lower():
            currentLanguage = AvailableLanguagesEnum.OTHER

        # Specify the modelPaths to be used (for right language)
        currentModelPath = modelPaths.get("english")  # Note: We use language english for english and other

        if currentLanguage == AvailableLanguagesEnum.POLISH:
            currentModelPath = modelPaths.get("polish")

        # Determine arguments for the process
        fileNameWithoutExtension = ".".join(basename(filePathToTranscript).split(".")[:-1])

        processArguments = [
            "--model",
            currentModelPath.modelPath,
            "--scorer",
            currentModelPath.scorerPath,
            "--audio",
            filePathToTranscript
        ]

        # Determine outputFilePath
        outputFilePath = join(cwd, outputFolder, f"{fileNameWithoutExtension}_{currentLanguage.name.lower()}_{outputFileSuffix}.txt")

        # Open the file "outputFilePath" and run the process
        print(f"-- Processing file: {filePathToTranscript} ({idx + 1} of {len(filePathsToTranscript)}; {currentLanguage.name.lower()} language) --")

        with open(outputFilePath, "w", encoding="utf-8") as stdout:
            lsOutput = subprocess.Popen([processName] + processArguments, stdout=stdout, cwd=cwd)
            lsOutput.communicate()  # Will block for 30 seconds


if __name__ == "__main__":
    main()
    print("-- END OF \"main.py\" SCRIPT --")
