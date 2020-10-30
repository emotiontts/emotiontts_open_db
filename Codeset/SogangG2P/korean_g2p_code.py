'''

한글 자소 및 음소에 대한 정의 및 변환 함수

@author: Jeongpil Lee (koreanfeel@gmail.com)
@created at : 2018. 07. 30.

'''

g_cho_list = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ"]
g_cho_Roman = ["g", "n", "d", "l", "m", "b", "s", "y", "j", "q", "k", "t", "p", "h", "x", "w", "f", "c", "z"]

g_jung_list = ["ㅏ", "ㅓ", "ㅗ", "ㅜ", "ㅡ", "ㅣ", "ㅐ", "ㅔ", "ㅑ", "ㅕ", "ㅛ", "ㅠ", "ㅒ", "ㅖ", "ㅘ", "ㅝ", "ㅚ", "ㅟ", "ㅙ", "ㅞ", "ㅢ", ""]
g_jung_Roman = ["A", "o", "O", "U", "u", "E", "a", "e", "1", "2", "3", "4", "5", "6", "7", "8", "9", "[", "]", "<", ">", "/"]

g_jong_list = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㄲ", "ㅆ", "ㄳ", "ㄵ", "ㄶ", "ㄺ", "ㄻ", "ㄼ",
               "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅄ", ""]
g_jong_Roman = ["G", "N", "D", "L", "M", "B", "S", "0", "J", "Q", "K", "T", "P", "H", "X", "C", "~", "+", "@", "#", "$", "%",
                "^", "&", "*", "(", ")", "="]

p_cho_list = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ"]
p_cho_Roman = ["g", "n", "d", "l", "m", "b", "s", "-", "j", "q", "k", "t", "p", "h", "x", "w", "f", "c", "z"]

p_jung_list = ["ㅏ", "ㅓ", "ㅗ", "ㅜ", "ㅡ", "ㅣ", "ㅐ", "ㅔ", "ㅑ", "ㅕ", "ㅛ", "ㅠ", "ㅒ", "ㅖ", "ㅘ", "ㅝ", "ㅚ", "ㅟ", "ㅙ", "ㅞ", "ㅢ", ""]
p_jung_Roman = ["A", "o", "O", "U", "u", "E", "a", "e", "1", "2", "3", "4", "5", "6", "7", "8", "9", "[", "]", "<", ">", "/"]

p_jong_list = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅇ", ""]
p_jong_Roman = ["G", "N", "D", "L", "M", "B", "0", "="]

import hgtk

def conv_code_to_hangul(code, g_or_p='p', split_token='_'):
    words = code.split(split_token)

    word = ''

    if g_or_p == 'p':
        cho_Roman = p_cho_Roman
        jung_Roman = p_jung_Roman
        jong_Roman = p_jong_Roman
        cho_list = p_cho_list
        jung_list = p_jung_list
        jong_list = p_jong_list
    else:
        cho_Roman = g_cho_Roman
        jung_Roman = g_jung_Roman
        jong_Roman = g_jong_Roman
        cho_list = g_cho_list
        jung_list = g_jung_list
        jong_list = g_jong_list

    for k, p in enumerate(words):
        p = ''.join(p.split())

        if len(p) % 3 != 0:
            print('INVALID WORDS({}) :{}'.format(g_or_p, p))
            continue

        for i in range(0, len(p), 3):
            if p[i] not in cho_Roman:
                break

            if p[i+1] not in jung_Roman:
                break

            if p[i+2] not in jong_Roman:
                break

            chosung = cho_list[cho_Roman.index(p[i])]
            jungsung = jung_list[jung_Roman.index(p[i+1])]
            jongsung = jong_list[jong_Roman.index(p[i+2])]

            if jungsung == "" and jongsung == "":
                char = chosung
            else:
                try:
                    char = hgtk.letter.compose(chosung, jungsung, jongsung)
                except:
                    print('NotHangulException')
                    print(chosung, jungsung, jongsung)
            word += char

        if k < len(words) - 1:
            word += ' '

    return word

def conv_hangul_to_code(hangul, g_or_p='p', split_token='_'):
    split_token = split_token.strip()
    words = hangul.strip().split()
    out_seq = ''

    if g_or_p == 'p':
        cho_Roman = p_cho_Roman
        jung_Roman = p_jung_Roman
        jong_Roman = p_jong_Roman
        cho_list = p_cho_list
        jung_list = p_jung_list
        jong_list = p_jong_list
    else:
        cho_Roman = g_cho_Roman
        jung_Roman = g_jung_Roman
        jong_Roman = g_jong_Roman
        cho_list = g_cho_list
        jung_list = g_jung_list
        jong_list = g_jong_list

    for k, word in enumerate(words):
        for j, char in enumerate(word):
            try:
                char_tuple = hgtk.letter.decompose(char)
                chosung = cho_list.index(char_tuple[0])
                jungsung = jung_list.index(char_tuple[1])
                jongsung = jong_list.index(char_tuple[2])

                out_seq += cho_Roman[chosung] + " " + jung_Roman[jungsung] + " " + jong_Roman[jongsung]

            except hgtk.exception.NotHangulException:
                # 특수문자 등이 들어왔을 때에는 그대로 출력함
                out_seq += char

            if j < len(word) - 1:
                out_seq += ' '

        if k < len(words) - 1:
            out_seq = out_seq + ' ' + split_token + ' '

    return out_seq
