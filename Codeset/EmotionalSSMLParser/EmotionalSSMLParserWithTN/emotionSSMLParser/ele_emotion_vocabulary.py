# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:14:28 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process vocabulary element.
"""

from . import ele_emotion_item, ele_emotion_info, mainstructure
from .emotionVocabulary import *


def getvocabulary(voc):
    """
    Process vocabulary element's attributes and child elements.

    Args:
        voc : Parse the vocabulary element.
    """

    vocAttr = voc.attrib
    vocChilds = voc.getchildren()
    itemNameList = []
    info = True

    if vocAttr.get("type") is None or vocAttr.get("id") is None:
        print("error: Vocabulary needs both type and id attribute")

    if vocAttr.get("type") is not None and vocAttr.get("id") is not None:
        vocaType = vocAttr.get("type")
        vocaId = vocAttr.get("id")
        vocaUri = mainstructure.file_data["emotionInfo"]["emotion"][vocaType + "-set"].split('#')[0]

        if vocaType not in ["category", "dimension", "appraisal", "action-tendency"]:
            print("error :  vocAttr_type_value is wrong")

        if existVocabulary(vocaUri, vocaId) is True:
            print('error : same voca id exists.', vocaId, vocaUri)
            return
        else:
            for child in vocChilds:
                if child.tag == "item":
                    name = eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child)")
                    if name in itemNameList:
                        print('error : same item id exists.')
                    else:
                        itemNameList.append(name)
                elif child.tag == "info":
                    if info:
                        eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child)")
                        info = False
                    else:
                        print("error : already have <info>")
                else:
                    print("error : Wrong element")

        if len(itemNameList) == 0:
            print("error : must contain one or more <item>")

    voca = Vocabulary(vocaType, vocaUri, vocaId, itemNameList)
    saveVocabularyList(voca)
