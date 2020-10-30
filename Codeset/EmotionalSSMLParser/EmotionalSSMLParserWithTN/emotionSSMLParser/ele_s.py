# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process s element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def gets(sEle):
    """
    Process s element's attributes and text value.

    Args:
      sEle: Parse the s element.

    """
    # Save the pre attribute's value
    oldIdAttr = mainstructure.file_data["s"]["id"]
    oldLangAttr = mainstructure.file_data["lang"]
    oldLangfailureAttr = mainstructure.file_data["onlangfailure"]

    oldEmoData = mainstructure.getEmoInfo()
    oldG2PData = mainstructure.getG2PInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(sEle)

    if checkAttr:
        children_ele_processing.evalChildren(sEle)

    initAttr = list()  # attribute list to initialize

    if oldIdAttr != "":
        mainstructure.file_data["s"]["id"] = oldIdAttr
    else:
        initAttr.append("id")

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

    if len(oldG2PData) > 0:
        mainstructure.saveG2PInfo(oldG2PData)
    else:
        mainstructure.deleteG2PInfo()

    # Init s element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(sEle, initAttr)
