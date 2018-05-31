num = 1
pas = 9999


while num <= 5:
    user_pin_code = int (input('Enter pass :'))
    print ('You used {} attempt out of 5'.format(num))
    if user_pin_code == pas:
        print('Acces')
        num = 6
    else :
        num <= 1
        if num >= 5 :
            print ("Try again")