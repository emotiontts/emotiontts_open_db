# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:09:09 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process lang element.
"""
from . import mainstructure, attributes_processing, children_ele_processing , mainstructure_dump
def getvoice(voiceEle):
    """
    Process lang element's attributes and text value.

    Args:
        langEle: Parse the voice element.

    """
    # Save the pre attribute's value
    oldGenderAttr=mainstructure.file_data["voice"]["gender"]
    oldAgeAttr = mainstructure.file_data["voice"]["age"]
    oldLangAttr=mainstructure.file_data["lang"]
    oldVariantAttr=mainstructure.file_data["voice"]["variant"]
    oldNameAttr=mainstructure.file_data["voice"]["name"]
    oldVoicefailAction=mainstructure.file_data["voice"]["onvoicefailure"]
    oldRequiredAttr=mainstructure.file_data["voice"]["required"]
    oldOrdering=mainstructure.file_data["voice"]["ordering"]
    oldEmoData = mainstructure.getEmoInfo()

    checkAttr = attributes_processing.setAttribute(voiceEle)
    if(checkAttr):
        children_ele_processing.evalChildren(voiceEle)
    
    initAttr = list()               # attribute list to initialize
    
    if oldGenderAttr != "":
        mainstructure.file_data["voice"]["gender"] = oldGenderAttr
    else:
        initAttr.append("gender")
        
    if oldAgeAttr !="":
        mainstructure.file_data["voice"]["age"] = oldAgeAttr
    else:
        initAttr.append("age")
        
    if oldLangAttr !="":
        mainstructure.file_data["lang"] = oldLangAttr
    else:
        initAttr.append("lang")
        
    if oldVariantAttr != "":
        mainstructure.file_data["voice"]["variant"] = oldVariantAttr
    else:
        initAttr.append("variant")
        
    if oldNameAttr != "":
        mainstructure.file_data["voice"]["name"] = oldNameAttr
    else:
        initAttr.append("name")
        
    if oldVoicefailAction != "":
        mainstructure.file_data["voice"]["onvoicefailure"] = oldVoicefailAction
    else:
        initAttr.append("onvoicefailure")
        
    if oldRequiredAttr  != "":
        mainstructure.file_data["voice"]["required"] = oldRequiredAttr
    else:
        initAttr.append("required")
        
    if oldOrdering  != "":
        mainstructure.file_data["voice"]["ordering"] = oldOrdering
    else:
        initAttr.append("ordering")
    
    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init voice element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(voiceEle, initAttr)