def request():
    Reading1 = float(input('Enter Reading1:'))
    Reading2 = float(input('Enter Reading2:'))
    Reading3 = float(input('Enter Reading3:'))
    Reading4 = float(input('Enter Reading4:'))
    sum_result = addition(Reading1, Reading2, Reading3, Reading4)
    avg_result = Average(Reading1, Reading2, Reading3, Reading4)


    print('Sum =', sum_result)
    print('Average temperature in fahrenheit=', avg_result)
    print('Average temperature in Celsius =', celcius_result)




def addition(Reading1, Reading2, Reading3, Reading4):
    return Reading1 + Reading2 + Reading3 + Reading4


def Average(Reading1, Reading2, Reading3, Reading4):
    return (Reading1 + Reading2 + Reading3 + Reading4) / 4





request()
