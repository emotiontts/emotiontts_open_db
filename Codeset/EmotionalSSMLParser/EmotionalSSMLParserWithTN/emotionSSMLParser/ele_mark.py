# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:15:30 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process mark element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump, ele_speak


def getmark(markEle):
    """
    Process mark element's attributes and text value.

    Args:
        markEle: Parse the mark element.

    """

    markAttrs = markEle.attrib

    if 'name' in markAttrs:
        name = markAttrs.get('name')
        if name == ele_speak.startmark:
            activeSpeech = 1
            print(activeSpeech)
        elif name == ele_speak.endmark:
            activeSpeech = 0
            print(activeSpeech)
    else:
        print("error: mark element needs name Attribute")

    markChilds = markEle.getchildren()

    if len(markChilds) != 0:
        print("error: mark element needs to be empty element")
