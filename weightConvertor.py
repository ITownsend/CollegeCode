weight = float(input('Enter your weight: '))
wtype = input('kilograms or pounds:')
if wtype == 'kilograms':
    (kilo) = weight / 0.45
    print("your weight in kilograms " + str(kilo))
elif wtype == 'pounds':
    pounds = weight * 2.2
    print("Your weight in pounds " + str(pounds))





