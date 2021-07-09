single_digit = {0: 'զրո', 1: 'մեկ', 2: 'երկու', 3: 'երեք', 4: 'չորս',
                5: 'հինգ', 6: 'վեց', 7: 'յոթ', 8: 'ութ',
                9: 'ինը'}

Teen = {10: 'տաս', 11: 'տասնմեկ', 12: 'տասներկու', 13: 'տասներեք',
        14: 'տասնչորս', 15: 'տասնհինգ', 16: 'տասնվեց',
        17: 'տասնյոթ', 18: 'տասնութ', 19: 'տասնինը'}

Tens = {20: 'քսան', 30: 'երեսուն', 40: 'քառասուն', 50: 'հիսուն', 60: 'վաթսուն',
        70: 'յոթանասուն', 80: 'ութսուն', 90: 'իննսուն'}

def spell_single_digit(Digit):
    if 0 <= Digit < 10:
        return single_digit[Digit]

def spell_double_digit(number):
    if 10 <= number < 20:
        return Teen[number]

    if 20 <= number < 100:
        Div = (number // 10) * 10
        Mod = number % 10
        if Mod != 0:
            return Tens[Div] + spell_single_digit(Mod)
        else:
            return Tens[number]

def spell_three_digits(number):
    if 100 <= number < 1000:
        Div = number // 100
        Mod = number % 100
        if Mod != 0:
            if Mod < 10:
                if Div == 1:
                    return "հարյուր " +  \
                       spell_single_digit(Mod)
                else:
                    return spell_single_digit(Div) + " հարյուր " +  \
                       spell_single_digit(Mod)
            elif Mod < 100:
                if Div == 1:
                    return "հարյուր " + \
                       spell_double_digit(Mod)
                else:
                    return spell_single_digit(Div) + " հարյուր " + \
                       spell_double_digit(Mod)
        else:
            if Mod == 0:
                return "հարյուր"
            else:
                return spell_single_digit(Div) + " հարյուր"

def Spell(number):
    if 0 <= number < 1000000000000:
        if number == 0:
            print (spell_single_digit(number))
        a = ""
        Loop = 0
        while number:
            Mod = number % 1000
            if Mod != 0:
                c = spell_three_digits(Mod) or spell_double_digit(Mod) \
                    or spell_single_digit(Mod)
                if Loop == 0:
                    a = c + " " + a
                elif Loop == 1:
                    if Mod == 1:
                        a = "հազար " + a
                    else:
                        a = c + " հազար " + a
                elif Loop == 2:
                    a = c + " միլիոն " + a
                elif Loop == 3:
                    a = c + " միլիարդ " + a
            number = number // 1000
            Loop += 1
        print (a)
    elif number < 0:
        number = eval(input("Մուտքագրեք դրական թիվ: "))
        Spell(number)
    else:
        number = eval(input("Մուտքագրեք տրիլիոնից փոքր թիվ: "))
        Spell(number)

def main():
    number = eval(input("Մուտքագրեք դրական թիվ: "))
    Spell(number)
main()