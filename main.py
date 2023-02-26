# Сюда вписываем числа,которые хотим переводить

des_1 = [74201, 542003]
bin_1 = [10100011101, 11001100101]
hex_1 = ["60FA13", "F013D5"]
oct_1 = [135001, 74200]

str_bin = "01"


def des(i1):
    counter = 0
    if str(i1).isdigit() == True:  # проверяем на бин,восьмир
        for i in str(i1):
            if i in str_bin:
                counter += 1
        if len(str(i1)) == counter:  # нам дали двоичную
            chislo = 0
            str_i1 = [i for i in reversed(list(str(i1)))]
            for j in range(len(str_i1)):
                chislo += int(str_i1[j]) * 2 ** j
        else:
            chislo = 0
            str_i1 = [i for i in reversed(list(str(i1)))]
            for j in range(len(str_i1)):
                chislo += int(str_i1[j]) * 8 ** j
    else:  # работаем с 16ричной
        slovaric = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        spisok = i1.strip()
        chislo = 0
        l = len(spisok) - 1
        for digit in spisok:
            chislo += slovaric[digit] * 16 ** l
            l -= 1
    return (chislo)


print(f"{[des(i) for i in bin_1]}-перевод из бинарной системы в десятичную")
print(f"{[des(i) for i in hex_1]}-перевод из 16ричной системы в десятичную")
print(f"{[des(i) for i in oct_1]}-перевод 8ричной системы в десятичную\n")


def bin(i1):
    if i1 not in des_1:  # ибо эти числа могут попасть не только под 10тичную систему счисления
        chislo_1 = des(i1)
    else:
        chislo_1 = i1
    l = []
    ostatok = chislo_1 % 2
    l.append(ostatok)
    chel = chislo_1 // 2
    while chel > 1:
        ostatok = chel % 2
        l.append(ostatok)
        chel = chel // 2
    l.append(chel)
    l = list(reversed(l))
    t = []
    for i in l:
        t.append(str(i))
    c = "".join(t)
    return (c)


print(f"{[bin(i) for i in des_1]}-перевод из десятичной системы в бинарную")
print(f"{[bin(i) for i in hex_1]}-перевод из 16ричной системы в бинарную")
print(f"{[bin(i) for i in oct_1]}-перевод 8ричной системы в бинарную\n")


def oct(i1):
    if i1 not in des_1:
        chislo_1 = des(i1)
    else:
        chislo_1 = i1
    result = ''
    while chislo_1 > 0:
        result = str(chislo_1 % 8) + result
        chislo_1 //= 8
    return (result)


print(f"{[oct(i) for i in des_1]}-перевод из десятичной системы в 8ричную")
print(f"{[oct(i) for i in hex_1]}-перевод из 16ричной системы в 8ричную")
print(f"{[oct(i) for i in bin_1]}-перевод бинарной системы в 8ричную\n")


def hex(i1):
    if i1 not in des_1:
        chislo_1 = des(i1)
    else:
        chislo_1 = i1
    result = ""
    slovaric = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                13: 'D', 14: 'E', 15: 'F'}
    while (chislo_1 > 0):
        remainder = chislo_1 % 16
        result = slovaric[remainder] + result
        chislo_1 = chislo_1 // 16

    return result


print(f"{[hex(i) for i in des_1]}-перевод из десятичной системы в 16ричную")
print(f"{[hex(i) for i in oct_1]}-перевод из 8ричной системы в 16ричную")
print(f"{[hex(i) for i in bin_1]}-перевод бинарной системы в 16ричную\n")
