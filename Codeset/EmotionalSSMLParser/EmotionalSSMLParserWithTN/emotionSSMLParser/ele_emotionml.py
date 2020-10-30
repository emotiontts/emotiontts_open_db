# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process emotionml element.
"""
from . import ele_emotion_emotion, ele_emotion_vocabulary, ele_emotion_info, emotionset


def getemotionml(emotionmlEle):
    """
    Process emotionml element's attributes

    Args:
        emotionmlEle: Parse the emotionml element.

    """

    emotionmlChilds = emotionmlEle.getchildren()
    emotionmlAttrs = emotionmlEle.attrib

    # Process the attributes
    if emotionmlAttrs.get("version") is None:
        print("error : <emotionml> element must contain name attribute")

    for attr in emotionmlAttrs.keys():
        if attr in ["category-set", "dimension-set", "appraisal-set", "action-tendency-set"]:
            emotionset.emotionset(attr, emotionmlAttrs.get(attr))
        elif attr in ["version"]:
            emotionml_ver = emotionmlAttrs.get('version')
            if emotionml_ver != "1.0":  # emotionml version check( it must be version 1.0)
                print("error: emotionml version error.")
        else:
            print("error : Wrong Attribute! ")

    # Process the child elements
    for child in emotionmlChilds:
        if child.tag in ["emotion", "vocabulary", "info"]:
            eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child)")
        else:
            print("error : Wrong element")
