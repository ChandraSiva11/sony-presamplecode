

dict_ = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}

dict_cpy = dict_
dict_bkp = dict_.copy()

print("Original dictionary\t", dict_, '\ncopied dictionary\t',dict_cpy,"\n")

dict_.pop("a")
print("One element removed from original dictionary\nOriginal dictionary\t", dict_, '\ncopied dictionary\t',dict_cpy,"\n")


print("Dictionary copied with copy option\nOriginal dictionary\t", dict_, '\ncopied dictionary\t',dict_bkp,)
