SingleDigit = {0: 'զրո', 1: 'մեկ', 2: 'երկու', 3: 'երեք', 4: 'չորս',
                5: 'հինգ', 6: 'վեց', 7: 'յոթ', 8: 'ութ',
                9: 'ինը'}

Teen = {10: 'տաս', 11: 'տասնմեկ', 12: 'տասներկու', 13: 'տասներեք',
        14: 'տասնչորս', 15: 'տասնհինգ', 16: 'տասնվեց',
        17: 'տասնյոթ', 18: 'տասնութ', 19: 'տասնինը'}

Tens = {20: 'քսան', 30: 'երեսուն', 40: 'քառասուն', 50: 'հիսուն', 60: 'վաթսուն',
        70: 'յոթանասուն', 80: 'ութսուն', 90: 'իննսուն'}

def spell_single_digit(Digit):
    if 0 <= Digit < 10:
        return SingleDigit[Digit]

def SpellTwoDigits(Number):
    if 10 <= Number < 20:
        return Teen[Number]

    if 20 <= Number < 100:
        Div = (Number // 10) * 10
        Mod = Number % 10
        if Mod != 0:
            return Tens[Div] + spell_single_digit(Mod)
        else:
            return Tens[Number]

def spell_three_digits(Number):
    if 100 <= Number < 1000:
        Div = Number // 100
        Mod = Number % 100
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
                       SpellTwoDigits(Mod)
                else:
                    return spell_single_digit(Div) + " հարյուր " + \
                       SpellTwoDigits(Mod)
        else:
            if Mod == 0:
                return "հարյուր"
            else:
                return spell_single_digit(Div) + " հարյուր"

def Spell(Number):
    if 0 <= Number < 1000000000000:
        if Number == 0:
            print (spell_single_digit(Number))
        a = ""
        Loop = 0
        while Number:
            Mod = Number % 1000
            if Mod != 0:
                c = spell_three_digits(Mod) or SpellTwoDigits(Mod) \
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
            Number = Number // 1000
            Loop += 1
        print (a)
    elif Number < 0:
        Number = eval(input("Մուտքագրեք դրական թիվ: "))
        Spell(Number)
    else:
        Number = eval(input("Մուտքագրեք տրիլիոնից փոքր թիվ: "))
        Spell(Number)

def main():
    Number = eval(input("Մուտքագրեք դրական թիվ: "))
    Spell(Number)
main()