dict_ = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}

sixth_value = dict_.setdefault('f')
print('Dictionary setdefault if key f is not in dict \t\t\t\t:', dict_)

dict_.setdefault('d', 7)
print('Dictionary setdefault not happen if key is already there \t:', dict_)

dict_.update({'e' : 8, 'a' : 11})
print('Dictionary update using update funcion in dict \t\t\t\t:', dict_)