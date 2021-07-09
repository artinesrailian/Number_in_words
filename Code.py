SingleDigit = {0: 'զրո', 1: 'մեկ', 2: 'երկու', 3: 'երեք', 4: 'չորս',
                5: 'հինգ', 6: 'վեց', 7: 'յոթ', 8: 'ութ',
                9: 'ինը'}

Teen = {10: 'տաս', 11: 'տասնմեկ', 12: 'տասներկու', 13: 'տասներեք',
        14: 'տասնչորս', 15: 'տասնհինգ', 16: 'տասնվեց',
        17: 'տասնյոթ', 18: 'տասնութ', 19: 'տասնինը'}

Tens = {20: 'քսան', 30: 'երեսուն', 40: 'քառասուն', 50: 'հիսուն', 60: 'վաթսուն',
        70: 'յոթանասուն', 80: 'ութսուն', 90: 'իննսուն'}

def SpellSingleDigit(Digit):
    if 0 <= Digit < 10:
        return SingleDigit[Digit]

def SpellTwoDigits(Number):
    if 10 <= Number < 20:
        return Teen[Number]

    if 20 <= Number < 100:
        Div = (Number // 10) * 10
        Mod = Number % 10
        if Mod != 0:
            return Tens[Div] + SpellSingleDigit(Mod)
        else:
            return Tens[Number]

def SpellThreeDigits(Number):
    if 100 <= Number < 1000:
        Div = Number // 100
        Mod = Number % 100
        if Mod != 0:
            if Mod < 10:
                if Div == 1:
                    return "հարյուր " +  \
                       SpellSingleDigit(Mod)
                else:
                    return SpellSingleDigit(Div) + " հարյուր " +  \
                       SpellSingleDigit(Mod)
            elif Mod < 100:
                if Div == 1:
                    return "հարյուր " + \
                       SpellTwoDigits(Mod)
                else:
                    return SpellSingleDigit(Div) + " հարյուր " + \
                       SpellTwoDigits(Mod)
        else:
            if Mod == 0:
                return "հարյուր"
            else:
                return SpellSingleDigit(Div) + " հարյուր"

def Spell(Number):
    if 0 <= Number < 1000000000000:
        if Number == 0:
            print (SpellSingleDigit(Number))
        a = ""
        Loop = 0
        while Number:
            Mod = Number % 1000
            if Mod != 0:
                c = SpellThreeDigits(Mod) or SpellTwoDigits(Mod) \
                    or SpellSingleDigit(Mod)
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