while True :
    try:
        x = int(input('Enter number'))
    except (ValueError, NameError, TypeError) as err:
        print('input error {}'.format(err))
    else:
        print('nu i chto')
    finally:
        print('beda')
        break