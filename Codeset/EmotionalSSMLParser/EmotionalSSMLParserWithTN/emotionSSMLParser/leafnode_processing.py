# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:45:32 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

"""

import json
from kolm.normalize import *

outputSent = ''
outputJson = {}
fileNum = 1


def queueProcessing(q):
    qList = list(q.queue)
    global outputSent
    global outputJson
    ele = ''
    code = ''
    index = 0
    isS = False

    while (index < len(qList)):
        loadData = json.loads(q.queue[index])
        loadDataSize = len(loadData)

        if loadDataSize == 2:
            if loadData['ele'] in ['speak', 's', 'p', 'lang', 'voice', 'prosody', 'emphasis', 'g2p']:
                ele = loadData['ele']
                code = loadData['code']
                if code == 1:
                    textProcessing(outputSent, outputJson, isS)
                    isS = False
                    code = 0
                    ele = ''
        else:

            if loadData['text'] == '':
                if len(outputSent) > 0:
                    textProcessing(outputSent, outputJson, isS)
                outputJson = loadData.copy()
                textProcessing('', outputJson, isS, True)

            if code == 0 and loadData['text'] != '':

                if ele == 's':
                    if len(outputSent) > 0 and isS == False:
                        textProcessing(outputSent, outputJson, isS)

                    isS = True

                outputSent += loadData['text']
                if len(outputJson) == 0:
                    outputJson = loadData

        index = index + 1


def textProcessing(text, jsonInfo, isS, isbreak=False):
    import re
    textList = []
    if isbreak:
        infoProcessing('', jsonInfo, isbreak)

    if len(text) > 0:
        if isS:
            infoProcessing(text.strip(), jsonInfo)
        else:
            textList = re.findall('[\s*\w+]+[.|!|?|~]*', text)
            for t in textList:
                infoProcessing(t.strip(), jsonInfo)

    initOutput()


def infoProcessing(text, jsonInfo, isbreak=False):
    outputInfo = {"text": "", "lang": "ko", "onlangfailure": "processorchoice",
                  "say-as": {"rawText": "", "interpret-as": "", "format": "", "detail": ""},
                  "voice": {"name": "", "gender": "", "age": "", "variant": "", "onvoicefailure": "priorityselect"},
                  "emotionInfo": {"name": "neutral", "value": ""},
                  "g2p": {"mode": "g2p", "source_lang": "ko_kr", "target_lang": "ko_kr"}
                  }

    breakInfo = {"break": {"time": ""}}

    if isbreak:
        if jsonInfo['break']['time'] != "":
            breakInfo['break']['time'] = jsonInfo['break']['time']
            outputInfo = breakInfo.copy()

    else:
        tmp = text.upper()
        tmp = readABC(tmp)
        tmp = readNumber(tmp)

        tmpStr = ''
        for t in tmp:
            tmpStr = tmpStr + t

        if tmpStr[-1] not in [".", "?", "!", "~"]:
            tmpStr = tmpStr + "."

        outputInfo["text"] = tmpStr

        if jsonInfo['lang'] != "":
            outputInfo['lang'] = jsonInfo['lang']

        if jsonInfo['onlangfailure'] != "":
            outputInfo['onlangfailure'] = jsonInfo['onlangfailure']

        for key in outputInfo['say-as'].keys():
            if jsonInfo['say-as'][key] != "":
                outputInfo['say-as'][key] = jsonInfo['say-as'][key]

        for key in outputInfo['voice'].keys():
            if jsonInfo['voice'][key] != "":
                outputInfo['voice'][key] = jsonInfo['voice'][key]

        for key in outputInfo['emotionInfo'].keys():
            if jsonInfo['emotionInfo']['category'][key] != "":
                outputInfo['emotionInfo'][key] = jsonInfo['emotionInfo']['category'][key]

        for key in outputInfo['g2p'].keys():
            if jsonInfo['g2p'][key] != "":
                outputInfo['g2p'][key] = jsonInfo['g2p'][key]
    saveInfo(outputInfo)


def saveInfo(outputInfo):
    import os
    try:
        if not os.path.isdir('./result'):
            os.mkdir('./result')
    except OSError as e:
        print(e)
        raise

    global fileNum
    with open('./result/info' + str(fileNum) + '.json', 'w', encoding='utf-8') as file:
        json.dump(outputInfo, file, ensure_ascii=False, indent="\t")
    print('info' + str(fileNum) + '.json : done.')
    fileNum = fileNum + 1


def initOutput():
    global outputSent
    global outputJson

    outputJson.clear()
    outputSent = ''
