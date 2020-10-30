# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:37:33 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""

from . import removeNamespace, ele_emotionml
from .emotionVocabulary import *


def emotionset(vocaType, uri):
    splitedUrl = uri.split('#')
    if len(splitedUrl) > 1:
        uriPath = splitedUrl[0]
        emotionId = splitedUrl[1]
    else:
        print('Error : must refer to the ID')

    if readVocabularyFile(uriPath):
        print('already checked this uri', uriPath)
    else:
        doc = removeNamespace.removeNamespace("inputDoc/" + uriPath)
        ele_emotionml.getemotionml(doc.root)
    vocaItems = getVocabulary(vocaType, uriPath, emotionId)
    return vocaItems
