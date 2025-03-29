import os


def getFileExtension(fileName: str) -> str:
    filename, file_extension = os.path.splitext(fileName)
    return file_extension
