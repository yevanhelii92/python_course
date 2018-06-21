while True :
    try:
        x = int(input('Enter number'))
        x = x / 0
        break
    except ValueError:
        print('input error')

# блок ексепт отлавливает ошибку перед выходом