import ast
single_digit = {0: 'զրո', 1: 'մեկ', 2: 'երկու', 3: 'երեք', 4: 'չորս',
                5: 'հինգ', 6: 'վեց', 7: 'յոթ', 8: 'ութ',
                9: 'ինը'}

teen = {10: 'տաս', 11: 'տասնմեկ', 12: 'տասներկու', 13: 'տասներեք',
        14: 'տասնչորս', 15: 'տասնհինգ', 16: 'տասնվեց',
        17: 'տասնյոթ', 18: 'տասնութ', 19: 'տասնինը'}

tens = {20: 'քսան', 30: 'երեսուն', 40: 'քառասուն', 50: 'հիսուն', 60: 'վաթսուն',
        70: 'յոթանասուն', 80: 'ութսուն', 90: 'իննսուն'}

def spell_single_digit(digit):
    if 0 <= digit < 10:
        return single_digit[digit]

def spell_double_digit(number):
    if 10 <= number < 20:
        return teen[number]
    else:
        pass

    if 20 <= number < 100:
        div = (number // 10) * 10
        mod = number % 10
        if mod != 0:
            return tens[div] + spell_single_digit(mod)
        else:
            return tens[number]

def spell_three_digits(number):
    if 100 <= number < 1000:
        div = number // 100
        mod = number % 100
        if mod != 0:
            if mod < 10:
                if div == 1:
                    return "հարյուր " +  \
                       spell_single_digit(mod)
                else:
                    return spell_single_digit(div) + " հարյուր " +  \
                       spell_single_digit(mod)
            elif mod < 100:
                if div == 1:
                    return "հարյուր " + \
                       spell_double_digit(mod)
                else:
                    return spell_single_digit(div) + " հարյուր " + \
                       spell_double_digit(mod)
        else:
            if mod == 0:
                return "հարյուր"
            else:
                return spell_single_digit(div) + " հարյուր"

def spell(number):
    if 0 <= number < 1000000000000:
        if number == 0:
            print(spell_single_digit(number))
        result = ""
        loop = 0
        while number:
            mod = number % 1000
            if mod != 0:
                count = spell_three_digits(mod) or spell_double_digit(mod) \
                    or spell_single_digit(mod)
                if loop == 0:
                    result = count + " " + result
                elif loop == 1:
                    if mod == 1:
                        result = "հազար " + result
                    else:
                        result = count + " հազար " + result
                elif loop == 2:
                    result = count + " միլիոն " + result
                elif loop == 3:
                    result = count + " միլիարդ " + result
            number = number // 1000
            loop += 1
        print(result)
    elif number < 0:
        number = ast.literal_eval(input("Մուտքագրեք դրական թիվ: "))
        spell(number)
    else:
        number = ast.literal_eval(input("Մուտքագրեք տրիլիոնից փոքր թիվ: "))
        spell(number)

def main():
    number = ast.literal_eval(input("Մուտքագրեք դրական թիվ: "))
    spell(number)
main()

def sumTwoTerms(term1, term2):
   return term1 + term2

print("2 + 2 = {0}".format(sumTwoTerms(2, 2)))