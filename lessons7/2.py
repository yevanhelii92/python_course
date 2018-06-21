def get_sum (**kwargs  ):
    return kwargs['x'] * kwargs['y']

kwargs1 = {"x": 2, "y": 5}
print(get_sum(**kwargs1))