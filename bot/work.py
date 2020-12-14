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
        if '+' or '-' in word and can_float(word):
            num = float(word)

        else:
            txt += word

    print(text != '')

    return [txt, num] if num and text != '' else None