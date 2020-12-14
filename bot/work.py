def can_float(num):
    try:
        float(num.replace(',', '.'))
        return True

    except:
        return False


def can_int(num):return num.isdigit()


def find_data(text):
    txt = ''

    num = 0

    for word in text.split(' '):
        if can_float(word.replace('+', '').replace('-', '')):
            num = float(word.replace(',', '.'))
            num = -num if not '+' in word else num

            if '-' in word:
                num = -num

        else:
            txt += word

    return [txt, num] if num and text != '' else None