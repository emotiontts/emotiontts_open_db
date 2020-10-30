# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:52:03 2018
@author: Ju-Hyun Lee, Hee Cho, Ki-Hyung Hong

Process say-as element.
"""
from . import mainstructure, attributes_processing, children_ele_processing, mainstructure_dump
import re
import queue


def getsay_as(sayEle):
    """
    Process say-as element's attributes and text value.

    Args:
      sayEle: Parse the say-as element.

    """
    sayAttribute = sayEle.attrib

    # Save the pre attribute's value
    oldInterpret_as = mainstructure.file_data["say-as"]["interpret-as"]
    oldFormatAttr = mainstructure.file_data["say-as"]["format"]
    oldDetailAttr = mainstructure.file_data["say-as"]["detail"]
    oldEmoData = mainstructure.getEmoInfo()

    # Process the attributes
    checkAttr = attributes_processing.setAttribute(sayEle)
    if checkAttr:
        interpret_as = mainstructure.file_data["say-as"]["interpret-as"]
        sayValue = ""

        if interpret_as == "date":
            sayValue = say_asDate(sayAttribute, sayEle.text)
        if interpret_as == "cardinal":
            sayValue = say_asCardinal(sayAttribute, sayEle)
        if interpret_as == "ordinal":
            sayValue = say_asOrdinal(sayEle)
        if interpret_as == "characters":
            sayValue = say_asChar(sayAttribute, sayEle)
        if interpret_as == "time":
            sayValue = say_asTime(sayAttribute, sayEle)
        if interpret_as == "telephone":
            sayValue = say_asTelephone(sayAttribute, sayEle.text)
        mainstructure.file_data["say-as"]["rawText"] = sayEle.text
        children_ele_processing.evalChildren(sayEle, sayValue)

    initAttr = list()  # attribute list to initialize

    if oldInterpret_as != "":
        mainstructure.file_data["s"]["interpret-as"] = oldInterpret_as
    else:
        initAttr.append("interpret-as")

    if oldFormatAttr != "":
        mainstructure.file_data["say-as"]["format"] = oldFormatAttr
    else:
        initAttr.append("format")

    if oldDetailAttr != "":
        oldDetailAttr = mainstructure.file_data["say-as"]["detail"] = oldDetailAttr
    else:
        initAttr.append("detail")
    if len(oldEmoData) > 0:
        mainstructure.saveEmoInfo(oldEmoData)
    else:
        mainstructure.deleteEmoInfo()

    # Init say-as element's attributes and text (mainstructure)
    if len(initAttr) > 0:
        attributes_processing.initAttribute(sayEle, initAttr)


def say_asDate(sayAttr, sayText):
    """
    Process say-as element's date attribute.

    Args:
        sayAttr: Parse say-as element attributes.
        sayText : Parse say-as element text values.

    Returns:
        date_print : Return the date value which are conforms to the output form
    """

    format_attr = sayAttr.get('format')  # format attributes : mdy, dmy, ymd,md, dm, ym, my, d, m , y
    delim = ['.', '-', '/']  # delimiter to sepearate text values
    dmy = [None, None, None]  # array of dmy(date, month, year) data
    month_dict = {'1': 'January', '2': 'Feburary', '3': 'March', '4': 'April', '5': 'May',
                  '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October',
                  '11': 'November', '12': 'December'}  # month dictionary

    # Process the say-as's text value into date format
    for d in delim:
        date_list = sayText.split(d)
        # if text value(date) is same with the format attr, process the date text value
        if len(date_list) == len(list(format_attr)):
            dateValue = queue.Queue()
            for i in date_list:
                dateValue.put(i)
            for j in list(format_attr):
                if j == 'd':  # Process day and check if day text value is correct
                    day_tmp = dateValue.get()
                    p = re.compile("0?[1-9]|[10-31]")
                    m = p.match(day_tmp)
                    if m and int(day_tmp) > 0 and int(day_tmp) < 32:
                        dmy[0] = day_tmp
                    else:
                        print("Error : day is not in the correct form.")

                elif j == 'm':  # Process month and check if month text value is correct
                    month_tmp = dateValue.get()
                    p = re.compile("0?[1-9]|[10-12]")
                    m = p.match(month_tmp)
                    if m.end() and int(month_tmp) > 0 and int(month_tmp) < 13:
                        dmy[1] = month_tmp
                    else:
                        print("Error : month is not in the correct form.")

                elif j == 'y':  # Process year and check if year text value is correct
                    year_tmp = dateValue.get()
                    p = re.compile("0?0?0?[0-9]|0?0?[10-99] |0?[100-999] |[1000-9999]")
                    m = p.match(year_tmp)
                    if m and int(year_tmp) > 0 and int(year_tmp) < 10000:
                        dmy[2] = year_tmp
                    else:
                        print("Error : years is not in the correct form.")
                else:
                    print("Error : format attribute has wrong value.")

            break
        else:  # if text value(date) is not same with the format attr, print error
            if delim.index(d) + 1 >= len(delim):
                print("Error : you used wrong delimiter (구분자가 잘못되었습니다)")
            else:
                print("Error : check the say-as text value.")

    # Depends on language, Write the date in the right form  (only support korean and english.)
    date_print = ""
    if mainstructure.file_data["lang"] == 'ko':
        if dmy[2] is not None:
            date_print += dmy[2] + "년 "
        if dmy[1] is not None:
            date_print += dmy[1] + "월 "
        if dmy[0] is not None:
            date_print += dmy[0] + "일 "

    elif mainstructure.file_data["lang"] == "en-US":
        date_print = ""
        if dmy[1] is not None:
            date_print += month_dict[str(int(dmy[1]))]
        if dmy[0] is not None:
            date_print += " " + dmy[0]
            tmp = int(dmy[0]) % 10
            if tmp == 1:
                date_print += "st "
            elif tmp == 2:
                date_print += "nd "
            elif tmp == 3:
                date_print += "rd "
            else:
                date_print += "th "

        if dmy[2] is not None:
            if dmy[0] is None and dmy[1] is None:
                date_print += dmy[2]
            else:
                date_print += ", " + dmy[2]

    return date_print


def say_asTelephone(sayAttr, sayText):
    """
    Process say-as element's telephone attribute.

    Args:
        sayAttr: Parse say-as element attributes.
        sayText : Parse say-as element text values.

    Returns:
        number : Return the number value which are conforms to the output form.
    """

    format_attr = sayAttr.get('format')  # format attributes (which means country code.)
    delim = ['.', '-', ' ', '/']  # delimiter to seperate text values
    country_code = ""  # telephones' country code
    say_val_list = list(sayText)

    number = ""
    if say_val_list[0] == '+':  # if text has '+' character, process the country code which is in the text values
        for i in range(1, len(say_val_list)):
            if say_val_list[i] in delim or say_val_list[i] == '(':
                sayText = sayText[i + 1:]
                break
            elif say_val_list[i].isdigit():
                country_code += say_val_list[i]
            else:
                print("Error your country code is not correct.")
                break
    else:  # if text does not have '+' character, format attribute is country code
        country_code = format_attr

    if country_code is None:  # If country code is None, print error.
        print("Warning : Your telephone number is not clear to which country it belongs.")
    else:  # If country code is not None, add country code to return variable(number.)
        number += country_code

    # Process the say-as's text value into telephone number.
    sayText = sayText.replace("(", "").replace(")", "")
    for d in delim:
        sayText = sayText.replace(d, "")
        if sayText.isdigit():
            number += sayText
            break
        else:
            print("Error : your phone number has wrong regulation.")
            break

    return number


def say_asTime(sayAttribute, say):
    """
    Process say-as element's time attribute.

    Args:
        sayAttribute: Parse say-as element attributes.
        say : Parse say-as element text values.

    Returns:
        result : Return the time value which are conforms to the output form.
    """
    # In case hms12
    qualifier = ['AM', 'A.M.', 'am', 'a.m.', 'A', 'a', 'PM', 'P.M.', 'pm', 'p.m.', 'P', 'p']  # am/pm Qualifier
    resultQualifier = ''  # used am/pm Qualifier
    resultField = ''  # used time field
    result = ''  # result time value(string)
    valueList = []  # result time value(list)
    timeField = [':', '.', '\040']
    formatValue = sayAttribute.get('format')

    # Check used time filed
    for s in timeField:
        if say.text.find(s) > 0:
            resultField = s
            break

    # if hms12, check qualifier
    for s in qualifier:
        if say.text.find(s) > 0:
            resultQualifier = s
            break

    # Remove am/pm qualifier
    if resultQualifier != '':
        timeValue = say.text.replace(resultQualifier, "").replace(" ", "")
    else:
        timeValue = say.text.replace(" ", "")

    # if field is empty
    if resultField == '\040' or resultField == '':
        say_asTimeNotSpace(timeValue, formatValue, valueList)
    # if field is not empty  (timeField 에 해당되는 것이 있을 때)
    else:
        valueList = valueList + timeValue.split(resultField)

    # To resolve index errors in valueList, set index 0 that is not used
    if len(valueList) != 3:
        num = 3 - len(valueList)
        for i in range(num):
            valueList.append(0)

    try:
        # Check the corresponding range of each hour, minute, and second
        if int(valueList[0]) != 0:
            if (formatValue == 'hms12' or formatValue == '') and int(valueList[0]) > 12 or int(valueList[0]) < 0:
                valueList.clear()
                li = say_asTimeNotSpace(timeValue, formatValue, valueList)
                if li == 0:
                    print('Error : Out of range')

            elif formatValue == 'hms24' and int(valueList[0]) > 23 or int(valueList[0]) < 0:
                valueList.clear()
                li = say_asTimeNotSpace(timeValue, formatValue, valueList)
                if li == 0:
                    print('Error :Out of range')
        else:
            valueList[0] = ""

        if int(valueList[1]) != 0:
            if int(valueList[1]) > 59 or int(valueList[1]) < 0:
                print('Error: Out of range-m')
        else:
            valueList[1] = ""

        if float(valueList[2]) != 0:
            if float(valueList[2]) > 60 or float(valueList[2]) < 0:
                print('Error: Out of range-s')
        else:
            valueList[2] = ""
    except ValueError as e:
        print("valueError: ", e)
        valueList.clear()

    # Special case : separated by '.' and seconds are expressed in '.'
    if len(valueList) == 4 and valueList[3] != '\040' and resultField == ".":
        valueList[2] = (valueList[2] + "." + valueList[3])
        del valueList[3]

    # Time Hour, minute, second/Morning and afternoon
    if valueList != []:
        result = say_asTimeScope(mainstructure.file_data["lang"], formatValue, resultQualifier, valueList)

    return result


def say_asTimeScope(lang, formatValue, resultQualifier, valueList):
    """
    Process say-as element's time attribute Scope.
    Time(Hour, minute, second/Morning and afternoon) value extraction

    Args:
        lang: target language
        formatValue : sayAttribute.get('format') value
        resultQualifier : list qualifier value
        valueList : result time value(list)

    Returns:
        result : Return the time value which are conforms to the output form.
    """
    amQualifier = ['AM', 'A.M.', 'am', 'a.m.', 'A', 'a']
    pmQualifier = ['PM', 'P.M.', 'pm', 'p.m.', 'P', 'p']
    timeUnitKo = ['시', '분', '초']
    timeUnitEng = ['hours', 'minutes', 'seconds']
    result = ''  # result value
    timeSlot = ' '  # Morning/afternoon value

    # use 0:0:0 with hms12 -> exception error
    if (formatValue == 'hms12' and valueList == ['', '', '']):
        result = ""
        print("오류 0:0:0 사용 할 수 없어요")

    # if hms24 , Convert to 12 hours and distinguish between morning and afternoon
    if formatValue == 'hms24' and valueList[0] != '' and int(valueList[0]) >= 12:
        if int(valueList[0]) == 12:
            resultQualifier = 'pm'
        else:
            valueList[0] = str(int(valueList[0]) - 12)
            resultQualifier = 'pm'
    elif formatValue == 'hms24' and valueList[0] != '':
        resultQualifier = 'am'

    # Korean
    if lang == 'ko':
        if (formatValue == 'hms24' and valueList == ['', '', '']) or (
                formatValue == 'hms12' and valueList == ['12', '', ''] and resultQualifier in amQualifier):
            result = '자정'
        elif (formatValue == 'hms24' and valueList == ['12', '', '']) or (
                formatValue == 'hms12' and valueList == ['12', '', ''] and resultQualifier in pmQualifier):
            result = '정오'
        else:
            if valueList[0] != '' and resultQualifier in pmQualifier:
                timeSlot = '오후'
            elif valueList[0] != '' and resultQualifier in amQualifier:
                timeSlot = '오전'

            for i in range(len(valueList)):
                if valueList[i] != '':
                    valueList[i] += timeUnitKo[i]

    # English
    else:
        if (formatValue == 'hms24' and valueList == ['', '', '']) or (
                formatValue == 'hms12' and valueList == ['12', '', ''] and resultQualifier in amQualifier):
            result = 'midnight'
        if (formatValue == 'hms24' and valueList == ['12', '', '']) or (
                formatValue == 'hms12' and valueList == ['12', '', ''] and resultQualifier in pmQualifier):
            result = 'noon'
        else:
            # English has different units.
            if valueList[0] != '' and ((int(valueList[0]) < 6 and resultQualifier in amQualifier) or (
                    int(valueList[0]) >= 9 and resultQualifier in pmQualifier)):
                timeSlot = 'in the night'
            if valueList[0] != '' and 6 <= int(valueList[0]) and int(
                    valueList[0]) < 12 and resultQualifier in amQualifier:
                timeSlot = 'in the morning'
            if valueList[0] != '' and (
                    int(valueList[0]) == 12 or int(valueList[0]) < 5) and resultQualifier in pmQualifier:
                timeSlot = 'in the afternoon'
            if valueList[0] != '' and 5 <= int(valueList[0]) < 9 and resultQualifier in pmQualifier:
                timeSlot = 'in the evening'

            for i in range(len(valueList)):
                if valueList[i] != '':
                    valueList[i] += timeUnitEng[i]

    # English : Convert 'hours' to 'o'clock'
    if valueList[1] == '':
        valueList[0] = valueList[0].replace("hours", " o'clock")

    if result == '':
        result += " ".join(valueList) + "   " + timeSlot

    return result


def say_asTimeNotSpace(timeValue, formatValue, valueList):
    """
    Process say-as element's time attribute.

    Args:
        timeValue: time element value
        formatValue : sayAttribute.get('format') value
        valueList : result time value(list)
    """
    timeValue = timeValue.replace(",", ".")
    timeCount = 0
    idx = 0
    while idx < len(timeValue) and timeCount <= 3:
        if timeCount == 0 and (formatValue == 'hms12' or formatValue == ''):
            checkNum = int(timeValue[idx:idx + 2])
            if checkNum >= 0 and checkNum <= 12:
                valueList.append(timeValue[idx:idx + 2])
                idx += 2
            else:
                valueList.append(timeValue[0])
                idx += 1

        if timeCount == 0 and formatValue == 'hms24':
            checkNum = int(timeValue[idx:idx + 2])
            if checkNum >= 0 and checkNum <= 23:
                valueList.append(timeValue[idx:idx + 2])
                idx += 2
            else:
                valueList.append(timeValue[0])
                idx += 1

        if timeCount == 1:
            checkNum = int(timeValue[idx:idx + 2])
            if checkNum >= 0 and checkNum <= 59:
                valueList.append(timeValue[idx:idx + 2])
                idx += 2
            else:
                valueList.append(timeValue[idx])
                idx += 1

        if timeCount == 2:
            checkNum = float(timeValue[idx:])
            if checkNum >= 0 and checkNum <= 59:
                valueList.append(timeValue[idx:])
                idx = len(timeValue)
            else:
                valueList.append(timeValue[idx])
                idx += 1

        if timeCount == 3:
            return 0

        timeCount = timeCount + 1


def say_asOrdinal(say):
    """
    Process say-as element's ordinal attribute.

    Args:
        say : Parse say-as element text values.

    Returns:
        result : Return the ordinal value which are conforms to the output form.
    """
    return say.text.strip()


def say_asCardinal(sayAttribute, say):
    """
    Process say-as element's cardinal attribute.

    Args:
        sayAttribute: Parse say-as element attributes.
        say : Parse say-as element text values.

    Returns:
        result : Return the cardinal value which are conforms to the output form.
    """
    result = ""
    saytext = say.text.strip()
    # Determining whether it is negative or positive (depending on language)
    if saytext[0] == '+':
        saytext = saytext.replace("+", "")

    elif saytext[0] == '-':
        saytext = saytext.replace("-", "")

    if sayAttribute.get('detail') is not None:
        size = int(len(saytext) / 3)
        count = 0

        if len(saytext) % 3 != 0:
            while count < size:
                result = sayAttribute.get('detail') + saytext[len(saytext) - 2 - count * 3:len(
                    saytext) - count * 3 + 1] + result
                count = count + 1
            result = saytext[0:len(saytext) % 3] + result
        else:
            while count < size:
                result = sayAttribute.get('detail') + saytext[
                                                      len(saytext) - 3 - count * 3:len(saytext) - count * 3] + result

                count = count + 1
            result = result[1:]

    if sayAttribute.get('format') is not None:
        size = int(len(saytext) / 3)
        count = 0
        while count < size:
            result = sayAttribute.get('format') + say.text[
                                                  len(saytext) - 2 - count * 3:len(saytext) - count * 3 + 1] + result
            count = count + 1

        if len(saytext) % 3 != 0:
            result = saytext[0:len(saytext) % 3] + result
        else:
            result = result[1:]

    # Determining whether it is negative or positive (depending on language)
    if say.text[0] == '+':
        if mainstructure.file_data['lang'] == "ko":
            result = "양수" + result
        else:
            result = "plus" + result
    elif say.text[0] == '-':
        if mainstructure.file_data['lang'] == "ko":
            result = "음수" + result
        else:
            result = "minus" + result

    return result


def say_asChar(sayAttribute, say):
    """
    Process say-as element's character attribute.

    Args:
        sayAttribute: Parse say-as element attributes.
        say : Parse say-as element text values.

    Returns:
        result : Return the character value which are conforms to the output form.
    """

    if sayAttribute.get('format') is not None:
        if sayAttribute.get('format') == "characters":
            print("characters' format value : " + sayAttribute.get('format'))
        elif sayAttribute.get('format') == "glyphs":
            print("characters'  format value : " + sayAttribute.get('format'))
        else:
            print("Error : characters' format  is wrong")

        result = say.text

        # Process the detail attribute which is the series of digits specifying how the characters are to be grouped.
        detailvalue = sayAttribute.get('detail')
        if detailvalue is not None:
            idx = 0
            detailvalueSplit = str(detailvalue.replace(" ", ""))
            size = len(detailvalueSplit)

            # Grouping the characters
            for i in range(int(size)):
                if i == int(size) - 1:
                    result = result + say.text[idx:]
                else:
                    result = result + say.text[idx:idx + int(detailvalueSplit[i])] + " "
                    idx = idx + int(detailvalueSplit[i])
        else:
            print("Warning : Detail attribute is not presented." + say.text)

    return result
