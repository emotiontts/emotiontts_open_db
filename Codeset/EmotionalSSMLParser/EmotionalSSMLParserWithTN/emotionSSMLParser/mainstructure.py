# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:44:37 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""
import json
from collections import OrderedDict
from . import mainstructure_dump


def getG2PInfo():
    g2p_data = {'mode': '', 'source_lang': '', 'target_lang': ''}
    dataIn = False

    for key in file_data['g2p'].keys():
        if file_data['g2p'][key] != "":
            g2p_data[key] = file_data['g2p'][key]
            dataIn = True

    if dataIn is True:
        return g2p_data
    else:
        return list()


def saveG2PInfo(g2p_data):
    for key in file_data['g2p'].keys():
        if file_data['g2p'][key] != "":
            file_data['g2p'][key] = g2p_data[key]


def deleteG2PInfo():
    for key in file_data['g2p'].keys():
        file_data['g2p'][key] = ""


def getEmoInfo():
    emo_data = {
        'emotion': {"version": "", "id": "", "category-set": "", "dimension-set": "", "appraisal-set": "",
                    "action-tendency-set": "", "start": "",
                    "end": "", "duration": "", "time-ref-uri": "", "time-ref-anchor-point": "", "offset-to-start": "",
                    "expressed-through": ""},
        'category': {"name": "", "value": "", "confidence": ""},
        'dimension': {"name": "", "value": "", "confidence": ""},
        'appraisal': {"name": "", "value": "", "confidence": ""},
        'action-tendency': {"name": "", "value": "", "confidence": ""},
        'trace': {"freq": "", "samples": ""},
        'info': {"id": ""},
        'reference': {"uri": "", "role": "", "media-type": ""}
    }
    dataIn = False
    for key, val in file_data['emotionInfo'].items():
        for k, v in val.items():
            if file_data['emotionInfo'][key][k] != "":
                emo_data[key][k] = file_data['emotionInfo'][key][k]
                dataIn = True

    if dataIn is True:
        return emo_data
    else:
        return list()


def saveEmoInfo(emo_data):
    for key, val in emo_data.items():
        for k, v in val.items():
            if emo_data[key][k] != "":
                file_data['emotionInfo'][key][k] = emo_data[key][k]


def deleteEmoInfo():
    for key, val in file_data['emotionInfo'].items():
        for k, v in val.items():
            file_data['emotionInfo'][key][k] = ""


def initMainStructure():
    # text
    file_data["text"] = ""
    file_data["g2p"] = {"mode": "", "source_lang": "", "target_lang": ""}
    # speak
    file_data["lang"] = ""
    file_data["onlangfailure"] = ""
    file_data["speak"] = {"base": "", "startmark": "", "endmark": ""}

    # lexicon
    file_data["lexicon"] = {"URI": "", "id": "", "type": "", "fetchtimeout": "", "maxage": "", "maxstale": ""}

    # lookup
    file_data["lookup"] = {"ref": ""}

    # say-as
    file_data["say-as"] = {"rawText": "", "interpret-as": "", "format": "", "detail": ""}

    # phoneme
    file_data["phoneme"] = {"ph": "", "alphabet": "", "type": ""}

    # sub
    file_data["sub"] = {"alias": ""}

    # voice
    file_data["voice"] = {"gender": "", "age": "", "variant": "", "name": "", "onvoicefailure": "", "required": "",
                          "ordering": ""}

    # emphasis
    file_data["emphasis"] = {"level": ""}

    # break
    file_data["break"] = {"time": "", "strength": ""}

    # meta
    file_data["meta"] = {"name": "", "content": "", "http-equiv": ""}

    # p,s
    file_data["p"] = {"id": ""}
    file_data["s"] = {"id": ""}

    # w,token
    file_data["w"] = {"role": "", "id": ""}
    file_data["token"] = {"role": "", "id": ""}

    # prosody
    file_data["prosody"] = {"pitch": "", "contour": "", "range": "",
                            "rate": "", "volume": "", "duration": ""}

    # audio
    file_data["audio"] = {"src": "", "fetchtimeout": "", "fetchhint": "", "maxage": "",
                          "maxstale": "", "clipBegin": "", "clipEnd": "", "repeatCount": "",
                          "repeatDur": "", "soundLevel": "", "speed": ""}

    # mark
    file_data["mark"] = {"name": ""}

    # emotion
    file_data["emotionInfo"] = {
        'emotion': {"version": "", "id": "", "category-set": "", "dimension-set": "",
                    "appraisal-set": "", "action-tendency-set": "", "start": "",
                    "end": "", "duration": "", "time-ref-uri": "", "time-ref-anchor-point": "",
                    "offset-to-start": "", "expressed-through": ""},
        'category': {"name": "", "value": "", "confidence": ""},
        'dimension': {"name": "", "value": "", "confidence": ""},
        'appraisal': {"name": "", "value": "", "confidence": ""},
        'action-tendency': {"name": "", "value": "", "confidence": ""},
        'trace': {"freq": "", "samples": ""},
        'info': {"id": ""},
        'reference': {"uri": "", "role": "", "media-type": ""}
    }


file_data = OrderedDict()
initMainStructure()
