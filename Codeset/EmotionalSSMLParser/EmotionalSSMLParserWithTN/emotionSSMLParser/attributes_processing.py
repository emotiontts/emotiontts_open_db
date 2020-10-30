# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:38:47 2019
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong
"""
from . import ele_structure, mainstructure
import re

initLang = ""
initLangFailure = ""
idList = list()


def getAttribute(ele_name):
    return ele_structure.element[ele_name]['attr']


def checkRequiredAttribute(ele):
    eleAttr = ele.attrib
    ele_name = str(ele.tag)
    defRequired = ele_structure.element[ele_name]['requiredAttr']

    count = 0
    for attrKey in eleAttr.keys():
        if attrKey in defRequired:
            count += 1

    if count == len(defRequired):
        return True
    else:
        return False


def setEmotionMLAttribute(ele, vocaItems):
    eleStr = str(ele.tag)
    defAttr = getAttribute(eleStr)
    eleAttr = ele.attrib

    if checkRequiredAttribute(ele):
        for attrKey in eleAttr.keys():
            attrValue = eleAttr.get(attrKey)
            if attrKey not in defAttr:
                print('Error : Wrong attribute key')
                return False
            else:
                if not checkEmotionMLAttributeValue(attrKey, attrValue):
                    print('Error : Wrong attribute value')
                    return False
                if attrKey == 'name' and not checkEmotionMLNameAttribute(vocaItems, attrValue):
                    print('Error : Wrong attribute value(name)')
                    return False
                mainstructure.file_data['emotionInfo'][eleStr][attrKey] = attrValue
    else:
        print('Error : Check required Attribute')
        return False
    return True


def checkEmotionMLNameAttribute(vocaItems, attrValue):
    if attrValue in vocaItems:
        return True
    return False


def checkEmotionMLAttributeValue(attrKey, attrValue):
    if attrKey == 'value':
        if 0 <= float(attrValue) <= 1:
            return True
    elif attrKey == 'confidence':
        if 0 <= float(attrValue) <= 1:
            return True
    elif attrKey == 'name':
        return True
    return False


def setAttribute(ele):
    global initLang
    global initLangFailure

    eleStr = str(ele.tag)
    defAttr = getAttribute(eleStr)

    eleAttr = ele.attrib

    if checkRequiredAttribute(ele):
        for attrKey in eleAttr.keys():

            attrValue = eleAttr.get(attrKey)
            if attrKey not in defAttr:
                print('error: attribute 이상')
                return False
            else:

                if not checkAttributeValue(attrKey, attrValue):
                    print('error: ', attrKey, '의 ', attrValue, ' 값 이상')
                    return False
                if attrKey == 'lang':
                    mainstructure.file_data[attrKey] = attrValue
                elif attrKey == 'onlangfailure':
                    mainstructure.file_data[attrKey] = attrValue
                else:
                    mainstructure.file_data[eleStr][attrKey] = attrValue

        if 'id' in defAttr and 'id' not in eleAttr.keys():
            mainstructure.file_data[eleStr]['id'] = ""

    else:
        print('error : Required Attribute 확인')
        return False
    return True


# empty all attributes
def initAttribute(ele, initAttr=list()):
    global initLang
    global initLangFailure

    eleStr = str(ele.tag)
    defAttr = initAttr

    mainstructure.file_data["text"] = ""

    for attrKey in defAttr:
        if attrKey == 'lang':
            mainstructure.file_data[attrKey] = ""
        elif attrKey == 'onlangfailure':
            mainstructure.file_data[attrKey] = ""
        else:
            mainstructure.file_data[eleStr][attrKey] = ""


def checkAttributeValue(attrKey, attrValue):
    global idList
    if attrKey == 'version':
        if attrValue == '1.1':
            return True
    if attrKey == 'lang':
        if attrValue in ['ko', 'en-US']:
            return True
    elif attrKey == 'onlangfailure':
        if attrValue in ['changevoice', 'ignoretext', 'ignorelang', 'processorchoice']:
            return True
    elif attrKey == 'onvoicefailure':
        if attrValue in ['priorityselect', 'keepexisting', 'processorchoice']:
            return True
    elif attrKey == 'alias':
        return True
    elif attrKey == 'level':
        if attrValue in ["strong", "moderate", "none", "reduced"]:
            return True
    elif attrKey == 'strength':
        return True
    elif attrKey == 'time':
        return True
    elif attrKey == 'pitch':
        p = re.compile('[0-9]+(.[0-9]+)?Hz|(x-)?(low|high)|medium|default')
        if p.match(attrValue):
            return True
    elif attrKey == 'contour':
        c = re.compile('[0-9]+(.[0-9]+)?[%],[+|-]?[0-9]+(.[0-9])*(Hz|%|st)')
        pContours = attrValue.split(")")
        pContours.pop()  # 마지막 값 지우기 )를 기준으로 나눴기때문에 마지막에는 ''값이 들어감
        tmpContours = []
        for contourAttr in pContours:
            contourAttr = contourAttr.replace("(", " ")
            contourAttr = contourAttr.replace(" ", "")
            if c.match(contourAttr):
                tmpContours.append(contourAttr)
        if len(pContours) == len(tmpContours):
            return True
    elif attrKey == 'range':
        r = re.compile('[+|-]?[0-9]+(.[0-9]+)?Hz|(x-)?(low|high)|medium|default')
        if r.match(attrValue):
            return True
    elif attrKey == 'rate':
        ra = re.compile('[+]?[0-9]+(.[0-9]+)?[%]|(x-)?(slow|fast)|medium|default')
        if ra.match(attrValue):
            return True
    elif attrKey == 'duration':
        return True
    elif attrKey == 'volume':
        v = re.compile('[+|-]?[0-9]+(.[0-9]+)?dB|(x-)?(soft|loud)|medium|default|silent')
        if v.match(attrValue):
            return True

    elif attrKey == 'src':
        return True
    elif attrKey == 'fetchtimeout' or attrKey == 'clipBegin' or attrKey == 'clipEnd' or attrKey == 'repeatDur':
        t = re.compile('[+]?[0-9]+(.[0-9]+)?[s|ms]?')
        if t.match(attrValue):
            return True
    elif attrKey == 'fetchhint':
        if attrValue in ['prefetch', 'safe']:
            return True
    elif attrKey == 'maxage':
        ma = re.compile('[+]?[0-9]+(.[0-9]+)?')
        if ma.match(attrValue):
            return True
    elif attrKey == 'maxstale':
        ms = re.compile('[+]?[0-9]+(.[0-9]+)?')
        if ms.match(attrValue):
            return True
    elif attrKey == 'repeatCount':
        rc = re.compile('[+]?[0-9]+(.[0-9]+)?')
        if rc.match(attrValue):
            return True
    elif attrKey == 'soundLevel':
        sl = re.compile('[+|-]?[0-9]+(.[0-9]+)?dB')
        if sl.match(attrValue):
            return True
    elif attrKey == 'speed':
        s = re.compile('[+]?[0-9]+(.[0-9]+)?[%]')
        if s.match(attrValue):
            return True
    elif attrKey == 'name':
        return True

    elif attrKey == 'required':
        vRequiredFeatures = attrValue.split()
        if len(vRequiredFeatures) > 0:
            for vRequiredFeature in vRequiredFeatures:
                if vRequiredFeature in ['name', 'languages', 'gender', 'age', 'variant']:
                    return True
                else:
                    return False
        else:
            return False

    elif attrKey == 'ordering':
        vOrderings = attrValue.split()
        if len(vOrderings) > 0:
            for vOrdering in vOrderings:
                if vOrdering in ['name', 'languages', 'gender', 'age', 'variant']:
                    return True
                else:
                    return False
        else:
            return False

    elif attrKey == 'gender':
        if attrValue in ['male', 'female', 'neutral']:
            return True

    elif attrKey == 'age':
        if attrValue.isdigit():
            return True

    elif attrKey == 'variant':
        if attrValue.isdigit() and int(attrValue) > 0:
            return True

    elif attrKey == 'id':
        if attrValue not in idList:
            idList.append(attrValue)
            return True
    elif attrKey == 'role':
        return True

    elif attrKey == 'type':
        return True
    elif attrKey == 'URI':
        return True

    elif attrKey == 'ref':
        return True
    elif attrKey == 'content':
        return True
    elif attrKey == 'http-equiv':
        return True
    elif attrKey == 'ph':
        return True
    elif attrKey == 'alphabet':
        if attrValue == 'ipa':
            return True
        else:
            a = re.compile('[x-]')
            m = a.match(attrValue)
            if m.start() == 0:
                return True

    elif attrKey == 'interpret-as':
        if attrValue in ['date', 'time', 'telephone', 'characters', 'cardinal', 'ordinal']:
            return True
    elif attrKey == 'format':
        return True
    elif attrKey == 'detail':
        return True
    elif attrKey == 'mode':
        if attrValue in ['g2p', 'g2g']:
            return True
    elif attrKey == 'source_lang':
        if attrValue in ['ko_kr', 'ko_jr', 'ko_ks']:
            return True
    elif attrKey == 'target_lang':
        if attrValue in ['ko_kr', 'ko_jr', 'ko_ks']:
            return True
    elif attrKey == 'schemaLocation':
        return True
    return False
