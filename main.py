def request():
    Reading1 = input('Enter Reading1:')
    Reading2 = input('Enter Reading2:')
    Reading3 = input('Enter Reading3:')
    Reading4 = input('Enter Reading4:')
    print('sum=', addition (Reading1,Reading2,Reading3,Reading4))
    print('Average temperature=', Average (Reading1,Reading2,Reading3,Reading4))

def addition(Reading1,Reading2,Reading3,Reading4):
    sum = int(Reading1) + int(Reading2) + int(Reading3) + int(Reading4)
    return sum

def Average (Reading1,Reading2,Reading3,Reading4):
    sum = int(Reading1) + int(Reading2) + int(Reading3) + int(Reading4)
    Average = sum / 4
    return Average

request()
