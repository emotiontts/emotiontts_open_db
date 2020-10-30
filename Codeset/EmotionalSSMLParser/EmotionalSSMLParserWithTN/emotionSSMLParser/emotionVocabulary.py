# -*- coding: utf-8 -*-
"""
Created on Wen May 27 11:29:37 2020
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""

vocabularyList = list()
vocaUriList = set()


# Vocabulary class
class Vocabulary:
    def __init__(self, vocaType, vocaUri, vocaId, items):
        self.vocaUri = vocaUri
        self.vocaType = vocaType
        self.vocaId = vocaId
        self.items = items

        vocaUriList.add(vocaUri)


def readVocabularyFile(vocaUri):
    if vocaUri in vocaUriList:
        return True
    else:
        return False


def existVocabulary(vocaUri, vocaId):
    for voca in vocabularyList:
        if voca.vocaId == vocaId and voca.vocaUri == vocaUri:
            return True
    return False


def saveVocabularyList(voca):
    vocabularyList.append(voca)


def getVocabulary(type, vocaUri, vocaId):
    for voca in vocabularyList:
        if voca.vocaType == type and voca.vocaId == vocaId and voca.vocaUri == vocaUri:
            return voca.items
    print('Error : No vocabulary with that ID.', vocaId)
    return list()
