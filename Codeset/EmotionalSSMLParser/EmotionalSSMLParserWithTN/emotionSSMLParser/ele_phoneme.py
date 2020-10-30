# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:28:41 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process phoneme element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getphoneme(phoEle):
    """
    Process phoneme element's attributes and text value.

    Args:
        phoEle: Parse the phoneme element.

    """
    # Save the pre attribute's value
    oldPhAttr = mainstructure.file_data["phoneme"]["ph"]
    oldAlpAttr = mainstructure.file_data["phoneme"]["alphabet"]
    oldTypeAttr = mainstructure.file_data["phoneme"]["type"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(phoEle)
    if (checkAttr):
        children_ele_processing.evalChildren(phoEle)

    initAttr = list()  # attribute list to initialize

    if oldPhAttr != "":
        mainstructure.file_data["phoneme"]["ph"] = oldPhAttr
    else:
        initAttr.append("ph")

    if oldAlpAttr != "":
        mainstructure.file_data["phoneme"]["alphabet"] = oldAlpAttr
    else:
        initAttr.append("alphabet")

    if oldTypeAttr != "":
        mainstructure.file_data["phoneme"]["type"] = oldTypeAttr
    else:
        initAttr.append("type")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init phoneme element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(phoEle, initAttr)
