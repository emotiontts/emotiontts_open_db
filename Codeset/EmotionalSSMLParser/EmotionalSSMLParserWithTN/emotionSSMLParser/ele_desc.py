# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process desc element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getdesc(descEle):
    """
    Process desc element's attributes and text value.

    Args:
      descEle: Parse the desc element.
    """

    # Save the pre attribute's value
    oldLangAttr = mainstructure.file_data["lang"]
    oldLangfailureAttr = mainstructure.file_data["onlangfailure"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(descEle)
    if checkAttr:
        children_ele_processing.evalChildren(descEle)

    initAttr = list()  # attribute list to initialize
    if oldLangAttr != "":
        mainstructure.file_data["lang"] = oldLangAttr
    else:
        initAttr.append("lang")

    if oldLangfailureAttr != "":
        mainstructure.file_data["onlangfailure"] = oldLangfailureAttr
    else:
        initAttr.append("onlangfailure")

    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init desc element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(descEle, initAttr)
