# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:43:08 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong
"""

from . import ele_structure, mainstructure, ele_s, mainstructure_dump, \
    ele_sub, ele_lang, ele_emphasis, ele_break, ele_prosody, ele_audio, ele_mark, \
    ele_desc, ele_voice, ele_p, ele_token, ele_w, ele_say_as, ele_phoneme, ele_lexicon, ele_lookup, \
    ele_emotion_action_tendency, ele_emotion_appraisal, ele_emotion_category, ele_emotion_emotion, ele_emotion_info, \
    ele_emotion_item, ele_emotion_reference, \
    ele_emotion_trace, ele_emotion_vocabulary, ele_emotionml, emotionset, ele_g2p


def getChildren(ele_name):
    return ele_structure.element[ele_name]['child']


def evalChildren(ele, sayAsText=""):
    eleStr = str(ele.tag)
    defChildren = getChildren(eleStr)
    eleChildren = ele.getchildren()

    mainstructure_dump.putStatus(ele.tag, 0)
    if eleStr == 'break':
        if ele.text is not None:
            print("Error : Must be empty")
    elif eleStr == 'say-as':
        if ele.text is not None:
            mainstructure.file_data["text"] = sayAsText.strip()
            mainstructure_dump.mainstructurePrint()
    elif eleStr == 'audio' and ele.text is None:
        mainstructure_dump.mainstructurePrint()
    else:
        if ele.text is not None and len(ele.text.strip()) > 0:
            mainstructure.file_data["text"] = ele.text.strip()
            mainstructure_dump.mainstructurePrint()

    for child in eleChildren:
        if child.tag in defChildren:
            if str(child.tag).find("-") != -1:
                eval("ele_" + str(child.tag).replace("-", "_") + ".get" + str(child.tag).replace("-", "_") + "(child)")
            elif child.tag == "emotion":
                eval("ele_emotion_" + child.tag + ".get" + child.tag + "(child)")
            else:
                eval("ele_" + child.tag + ".get" + child.tag + "(child)")
        else:
            print("Error : Wrong element")

        if child.tail is not None and len(child.tail.strip()) > 0:
            mainstructure.file_data["text"] = child.tail.strip()
            mainstructure_dump.mainstructurePrint()

    mainstructure_dump.putStatus(ele.tag, 1)
