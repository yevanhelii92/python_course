correct_login = "1234"
correct_pass = 1234
num = 1

while True :
    exit_cond = input ('For exit from system enter "end"')
    if exit_cond == 'end':
        print ("You are in system")
    login = int(input("Enter your login: "))
    password = int(input("Enter your password: "))
    if login == correct_pass and password == correct_pass:
        print ('Success')
        break
    elif login != correct_pass and password != correct_pass:
        print('Wrong pass and login')
    else :
        print('Wrong pass or login')