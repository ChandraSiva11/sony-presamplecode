import dict_swap_module as swp

dict_ = {1 : 'oNe', 2: 'two', 3: 'three', 4 : 'Four', 5 : 'fiVe', 6 : 'six', 7 : 'Seven', 8 : 'eight', 9 : 'nine'}

dictionary = swp.dict_swap(dict_)

dictionary[1] = 'one'
# dictionary[2] = 'Two'
# dictionary[3] = 'Three'
# dictionary[4] = 'FouR'
# dictionary[5] = 'fiVe'
# dictionary[6] = 'Six'
# dictionary[7] = 'Seve'
# dictionary[8] = 'Eight'
# dictionary[9] = 'nine'

print(dictionary)
# print(dictionary['three'])

