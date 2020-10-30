# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:52:35 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process emotion element.
"""
from . import emotionset, ele_emotion_category, ele_emotion_reference, ele_emotion_appraisal, \
    ele_emotion_action_tendency, ele_emotion_info, ele_emotion_dimension
from . import mainstructure
from .emotionVocabulary import getVocabulary

emotion_id_list = []


def checkEmotionId(id):
    """
    Process emotion id attribute

    Args:
        id : id attribute value
    Returns:
        boolean value : if emotion_id_list contains id, return false.
    """
    if id in emotion_id_list:
        print("error : id must be unique!!")
        return False
    else:
        emotion_id_list.append(id)
        return True


def getemotion(emotionEle):
    """
    Process emotion element's attributes

    Args:
        emotionEle: Parse the emotion element.
    Returns:
        result :  ??? 확인하기
    """
    vocaType = ""
    vocaTypeList = []
    nameList = []
    name = ''
    emotionChilds = emotionEle.getchildren()

    verAttr = mainstructure.file_data["emotionInfo"]["emotion"]["version"]
    idAttr = mainstructure.file_data["emotionInfo"]["emotion"]["id"]
    categorySetAttr = mainstructure.file_data["emotionInfo"]["emotion"]["category-set"]
    dimensionSetAttr = mainstructure.file_data["emotionInfo"]["emotion"]["dimension-set"]
    appraisalSetAttr = mainstructure.file_data["emotionInfo"]["emotion"]["appraisal-set"]
    actTendencySetAttr = mainstructure.file_data["emotionInfo"]["emotion"]["action-tendency-set"]

    startAttr = mainstructure.file_data["emotionInfo"]["emotion"]["start"]
    endAttr = mainstructure.file_data["emotionInfo"]["emotion"]["end"]
    durationAttr = mainstructure.file_data["emotionInfo"]["emotion"]["duration"]
    timeRefUriAttr = mainstructure.file_data["emotionInfo"]["emotion"]["time-ref-uri"]
    timeRefAnchorPointAttr = mainstructure.file_data["emotionInfo"]["emotion"]["time-ref-anchor-point"]
    offsetToStartAttr = mainstructure.file_data["emotionInfo"]["emotion"]["offset-to-start"]
    expressedThroughAttr = mainstructure.file_data["emotionInfo"]["emotion"]["expressed-through"]

    emotionAttrs = emotionEle.attrib

    for attr in emotionAttrs.keys():
        attrValue = emotionAttrs.get(attr)
        if attr in ["category-set", "dimension-set", "appraisal-set", "action-tendency-set"]:
            vocaType = attr[:-4]
            if vocaType not in vocaTypeList:
                vocaTypeList.append(vocaType)
            mainstructure.file_data["emotionInfo"]["emotion"][attr] = attrValue
            vocaItems = emotionset.emotionset(vocaType, attrValue)
        elif attr in ["start", "end", "duration", "time-ref-uri", "time-ref-anchor-point", "offset-to-start",
                      "expressed-through", "version"]:
            mainstructure.file_data["emotionInfo"]["emotion"][attr] = attrValue
        elif attr in ["id"]:
            check = checkEmotionId(attrValue)
            if check:
                mainstructure.file_data["emotionInfo"]["emotion"]["id"] = attrValue
        else:
            print("error : Wrong Attribute! ")

    if len(emotionChilds) == 0:
        print("error: element must contain at least one element.")

    for child in emotionChilds:
        if child.tag in ["category", "dimension", "appraisal", "action-tendency"] and child.tag == vocaType:
            if str(child.tag).find("-") != -1:
                name = eval("ele_emotion_" + str(child.tag).replace("-", "_") + ".get" + str(child.tag).replace("-",
                                                                                                                "_") + "(child,vocaItems)")
            else:
                name = eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child,vocaItems)")
        elif child.tag in ["category", "dimension", "appraisal", "action-tendency"] and child.tag not in vocaTypeList:
            print("error: ", child.tag, "is not in type list(attribute")
        elif child.tag in ["info", "reference"]:
            name = eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child)")
        else:
            print("Error : Wrong element")

        if name in nameList:
            print('error : same name exists. ', name)
        else:
            nameList.append(name)

        if verAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["version"] = verAttr
        if idAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["id"] = idAttr

        if categorySetAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["category-set"] = categorySetAttr
        if dimensionSetAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["dimension-set"] = dimensionSetAttr
        if appraisalSetAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["appraisal-set"] = appraisalSetAttr
        if actTendencySetAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["action-tendency-set"] = actTendencySetAttr

        if startAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["start"] = startAttr
        if endAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["end"] = endAttr
        if durationAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["duration"] = durationAttr
        if timeRefUriAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["time-ref-uri"] = timeRefUriAttr
        if timeRefAnchorPointAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["time-ref-anchor-point"] = timeRefAnchorPointAttr
        if offsetToStartAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["offset-to-start"] = offsetToStartAttr
        if expressedThroughAttr != "":
            mainstructure.file_data["emotionInfo"]["emotion"]["expressed-through"] = expressedThroughAttr
