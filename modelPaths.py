from enum import Enum


class AvailableLanguagesEnum(Enum):
    ENGLISH = 0
    POLISH = 1,
    OTHER = 2


class ModelPaths:
    def __init__(self, language: AvailableLanguagesEnum, modelPath: str, scorerPath: str):
        self.language = language
        self.modelPath = modelPath
        self.scorerPath = scorerPath

