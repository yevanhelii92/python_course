h = int(input("hour =  "))
m = int(input("minute = "))
if 0 < h > 24 or 0 < m > 59:
        print("Wrong data")
else:
    if h > 12:
       h -= 12
    hAngle = 0.5 * (h * 60 + m)      # 0.5 это приводим с 24 до 12 часов
    mAngle = (360/60) * m            # узнаем сколько это градусов/минуту и умножаем на минуты
    angle = (hAngle - mAngle)
    print("Angle between {}".format(angle))
