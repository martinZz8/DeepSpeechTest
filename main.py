from os import listdir, remove
from os.path import dirname, isfile, join, basename
from datetime import datetime
from modelPaths import ModelPaths, AvailableLanguagesEnum
from helpers.getFileExtension import getFileExtension
from helpers.convertFileToWav import convertFileToWav
from helpers.transcriptFile import transcriptFile


def main():
    # -- Determine cwd --
    cwd = dirname(__file__)

    # -- Options --
    availableExtensions = [".wav", ".mp3", ".mp4"]
    folderNameToProcess = "data/audio/english"  # None or folder path relative to cwd (can be "data/audio/<language>" or "data/video/<language>")
    # Specify file names to transcript (relative path to cwd)
    # Note: if variable "folderNameToProcess" is specified, this variable is overridden
    filePathsToTranscript = [
        "data/audio/english/audio_2.wav",
        "data/audio/english/audio_5.mp3",
        "data/video/english/video_1.mp4"
    ]
    tempFolder = "data/_temp"
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

    # -- Create copy of "availableExtensions" for conversion of other types than ".wav"
    indexOfWavItem = availableExtensions.index(".wav")
    extensionsToBeConverted = availableExtensions[:indexOfWavItem] + availableExtensions[indexOfWavItem+1:]

    # -- Specify "filePathsToTranscript" (if "folderNameToProcess" is specified) --
    if folderNameToProcess is not None:
        absolutePathToAudioFolder = f"{cwd}/{folderNameToProcess}"
        filePathsToTranscript = [
            f"{folderNameToProcess}/{f}"
            for f in listdir(absolutePathToAudioFolder)
            if isfile(join(absolutePathToAudioFolder, f)) and (getFileExtension(f) in availableExtensions)
        ]

    # -- Transcript files --
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

        # Convert file into ".wav" 16kHz frequency (if it's already in other file type than ".wav")
        deleteTempFileAfterProcess = False
        fileExtension = getFileExtension(filePathToTranscript)

        if fileExtension in extensionsToBeConverted:
            filePathToTranscript = convertFileToWav(filePathToTranscript, tempFolder, cwd)
            deleteTempFileAfterProcess = True

        # Start process to transcript file
        print(f"-- Processing file: {filePathToTranscript} ({idx + 1} of {len(filePathsToTranscript)}; {currentLanguage.name.lower()} language) --")

        # Determine outputFilePath
        fileNameWithoutExtension = ".".join(basename(filePathToTranscript).split(".")[:-1])
        outputFilePath = f"{cwd}/{outputFolder}/{fileNameWithoutExtension}_{currentLanguage.name.lower()}_{outputFileSuffix}_{datetime.today().strftime('%Y-%m-%dT%H-%M-%S')}.txt"

        transcriptFile(filePathToTranscript, outputFilePath, currentModelPath, cwd)

        if deleteTempFileAfterProcess:
            remove(filePathToTranscript)


if __name__ == "__main__":
    main()
    print("-- END OF \"main.py\" SCRIPT --")
