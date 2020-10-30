# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:01:54 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong


Process lang element.
"""

from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump


def getlang(langEle):
    """
    Process lang element's attributes and text value.

    Args:
        langEle: Parse the lang element.

    """
    # Save the pre attribute's value
    oldLangAttr = mainstructure.file_data["lang"]
    oldLangfailureAttr = mainstructure.file_data["onlangfailure"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(langEle)
    if (checkAttr):
        children_ele_processing.evalChildren(langEle)

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

    # Init lang element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(langEle, initAttr)
