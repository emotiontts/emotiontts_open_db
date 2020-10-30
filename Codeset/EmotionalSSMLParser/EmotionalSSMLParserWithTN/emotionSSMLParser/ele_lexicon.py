# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:28:19 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process lexicon element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getlexicon(lexiconEle):
    """
    Process lexicon element's attributes and text value.

    Args:
        lexiconEle: Parse the lexicon element.

    """

    # Save the pre attribute's value
    oldUriAttr = mainstructure.file_data["lexicon"]["URI"]
    oldIdAttr = mainstructure.file_data["lexicon"]["id"]
    oldTypeAttr = mainstructure.file_data["lexicon"]["type"]
    oldFetchtimeAttr = mainstructure.file_data["lexicon"]["fetchtimeout"]
    oldMaxageAttr = mainstructure.file_data["lexicon"]["maxage"]
    oldMaxstaleAttr = mainstructure.file_data["lexicon"]["maxstale"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(lexiconEle)
    if (checkAttr):
        children_ele_processing.evalChildren(lexiconEle)

    initAttr = list()  # attribute list to initialize
    if oldUriAttr != "":
        mainstructure.file_data["lexicon"]["URI"] = oldUriAttr
    else:
        initAttr.append("URI")

    if oldIdAttr != "":
        mainstructure.file_data["lexicon"]["id"] = oldIdAttr
    else:
        initAttr.append("id")

    if oldTypeAttr != "":
        mainstructure.file_data["lexicon"]["type"] = oldTypeAttr
    else:
        initAttr.append("type")

    if oldFetchtimeAttr != "":
        mainstructure.file_data["lexicon"]["fetchtimeout"] = oldFetchtimeAttr
    else:
        initAttr.append("fetchtimeout")

    if oldMaxageAttr != "":
        mainstructure.file_data["lexicon"]["maxage"] = oldMaxageAttr
    else:
        initAttr.append("maxage")

    if oldMaxstaleAttr != "":
        mainstructure.file_data["lexicon"]["maxstale"] = oldMaxstaleAttr
    else:
        initAttr.append("maxstale")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init lexicon element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(lexiconEle, initAttr)
