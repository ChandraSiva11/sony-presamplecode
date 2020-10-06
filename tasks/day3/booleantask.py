tstr = "this is string example....wow!!!";
substr = "exam";

print("1. :%r" % bool(tstr.find(substr)))
print("2. :%r" % bool(tstr.find(substr, 10)))
print("3. :%r" % bool(tstr.find(substr, 20)))
print("4. :%r" % bool(tstr.find("Exams")))
print("5. :%r" % bool(tstr.index(substr)))
print("6. :%r" % bool(tstr.index(substr, 10)))

print()

print("1. :%r" % tstr.find(substr))
print("2. :%r" % tstr.find(substr, 10))
print("3. :%r" % tstr.find(substr, 20))
print("4. :%r" % tstr.find("Exams"))
print("5. :%r" % tstr.index(substr))
print("6. :%r" % tstr.index(substr, 10))
# print("7. :%d" % tstr.index(substr, 20))
