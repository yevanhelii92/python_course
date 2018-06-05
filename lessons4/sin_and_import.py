import math
def get_sin(and_get):
    and_rad = math.radians(and_get)
    result = math.sin(and_rad)
    return round (result,3)

for ang in [ 30, 45, 90, 180 ]:
    print (get_sin(ang))