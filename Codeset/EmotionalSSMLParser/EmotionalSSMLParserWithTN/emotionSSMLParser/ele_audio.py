# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:57:08 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process audio element.
"""

from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getaudio(audioEle):
    """
    Process audio element's attributes and text value.

    Args:
        audioEle: Parse the audio element.
    """
    # Save the pre attribute's value
    oldSrcAttr = mainstructure.file_data["audio"]["src"]
    oldFetchtimeoutAttr = mainstructure.file_data["audio"]["fetchtimeout"]
    oldFetchhintAttr = mainstructure.file_data["audio"]["fetchhint"]
    oldMaxageAttr = mainstructure.file_data["audio"]["maxage"]
    oldMaxstaleAttr = mainstructure.file_data["audio"]["maxstale"]
    oldClipBeginAttr = mainstructure.file_data["audio"]["clipBegin"]
    oldClipEndAttr = mainstructure.file_data["audio"]["clipEnd"]
    oldRepeatCountAttr = mainstructure.file_data["audio"]["repeatCount"]
    oldRepeatDurAttr = mainstructure.file_data["audio"]["repeatDur"]
    oldSoundLevelAttr = mainstructure.file_data["audio"]["soundLevel"]
    oldSpeedAttr = mainstructure.file_data["audio"]["speed"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(audioEle)
    if (checkAttr):
        children_ele_processing.evalChildren(audioEle)

    initAttr = list()  # attribute list to initialize
    if oldSrcAttr != "":
        mainstructure.file_data["audio"]["src"] = oldSrcAttr
    else:
        initAttr.append("src")

    if oldFetchtimeoutAttr != "":
        mainstructure.file_data["audio"]["fetchtimeout"] = oldFetchtimeoutAttr
    else:
        initAttr.append("fetchtimeout")

    if oldFetchhintAttr != "":
        mainstructure.file_data["audio"]["fetchhint"] = oldFetchhintAttr
    else:
        initAttr.append("fetchhint")

    if oldMaxageAttr != "":
        mainstructure.file_data["audio"]["maxage"] = oldMaxageAttr
    else:
        initAttr.append("maxage")

    if oldMaxstaleAttr != "":
        mainstructure.file_data["audio"]["maxstle"] = oldMaxstaleAttr
    else:
        initAttr.append("maxstle")

    if oldClipBeginAttr != "":
        mainstructure.file_data["audio"]["clipBegin"] = oldClipBeginAttr
    else:
        initAttr.append("clipBegin")

    if oldClipEndAttr != "":
        mainstructure.file_data["audio"]["clipEnd"] = oldClipEndAttr
    else:
        initAttr.append("clipEnd")

    if oldRepeatCountAttr != "":
        mainstructure.file_data["audio"]["repeatCount"] = oldRepeatCountAttr
    else:
        initAttr.append("repeatCount")

    if oldRepeatDurAttr != "":
        mainstructure.file_data["audio"]["repeatDur"] = oldRepeatDurAttr
    else:
        initAttr.append("repeatDur")

    if oldSoundLevelAttr != "":
        mainstructure.file_data["audio"]["soundLevel"] = oldSoundLevelAttr
    else:
        initAttr.append("soundLevel")

    if oldSpeedAttr != "":
        mainstructure.file_data["audio"]["speed"] = oldSpeedAttr
    else:
        initAttr.append("speed")
    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init audio element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(audioEle, initAttr)
