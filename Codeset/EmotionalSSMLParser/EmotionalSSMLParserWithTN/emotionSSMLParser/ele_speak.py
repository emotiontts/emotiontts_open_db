# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:49:50 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process speak element.
"""
from . import mainstructure, ele_s, attributes_processing, children_ele_processing, mainstructure_dump

activeSpeech = 0  # variable for mark element ( 0 : inactivate speech , 1 : activate speech)
result = ""
defaultLang = "ko"  # default language
gttsLang = "ko"  # language for gTTS


def getspeak(speakEle):
    """
    Process speak element's attributes and text value.

    Args:
        speakEle: Parse the speak element.

    """
    baseURI = ""
    onlangfailureAction = "processorchoice"  # action for speech synthesis when language failure occurs

    startmark = ""  # start of mark element
    endmark = ""  # end of mark element
    langAttr = ""

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(speakEle)

    if (checkAttr):
        children_ele_processing.evalChildren(speakEle)

    mainstructure_dump.sendQueue()
