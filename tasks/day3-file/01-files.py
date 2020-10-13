# open close read write seek
def simple_read_few_bytes(filename):
    fd = open(filename, "r")

    data = fd.read(10)

    print("data :%s" % data)

    fd.close()

def simple_read_twice(filename):
    fd = open(filename, "rt")

    data = fd.read(10)
    print("1: data :%s" % data)
    print("1: len  :%d" % len(data))

    data = fd.read(10)
    print("2: data :%s" % data)
    print("2: len  :%d" % len(data))

    fd.close()

def read_compleate_text_file(filename):
    fd = open(filename, "rt")
    i = 1
    while(True):
        data = fd.read(10)
        length = len(data)
        print("%d: len :%d, %s" % (i, length, data))

        i = i + 1
        if (length < 10):
            break

    fd.close()

def read_compleate_data(filename):
    fd = open(filename, "rt")
    data = fd.read()
    length = len(data)

    print("len :%d, %s" % (length, data))

    fd.close()

#read()
#read(1)
#readline
#readlines()

def read_line_text_file_1(filename):
    fd = open(filename, "rt")
    i = 1
    while(True):
        data = fd.readline()
        if (len(data) <= 0):
            break
        print("%d : len :%d, %s" % (i, len(data), data))

    fd.close()

#for d in "Hello world":
#for d in ["hai", "Hello", "Bye"]:
#for d in ("hai", "Hello", "Bye"):
#for d in fd:

def read_line_text_file_2(filename):
    fd = open(filename, "rt")
    i = 1

    for data in fd:
        print("%d : len :%d, %s" % (i, len(data), data))
        print(data)

        i  = i + 1
    fd.close()

def read_lines_text_file(filename):
    fd = open(filename, "rt")

    data = fd.readlines()

    fd.close()

    print("len :%d, %s" % (len(data), data))

    i = 1
    for line in data:
        print("%d. %s" % (i, line))
        i = i + 1
    return

#0 - Beginning
#1 - Current
#2 - End of file
def file_operations_seek(filename):
    fd = open(filename, "rb")

    print("file position :%d" % fd.tell())

    data = fd.read(10)
    print("file position :%d" % fd.tell())

    fd.seek(40)
    print("file position :%d" % fd.tell())

    data = fd.read(10)
    print(data)
    print("file position :%d" % fd.tell())

    fd.seek(100, 0)
    print("file position :%d" % fd.tell())

    fd.seek(10, 0)
    print("file position :%d" % fd.tell())

    fd.seek(20, 1)
    print("file position :%d" % fd.tell())

    fd.seek(-5, 1)
    print("file position :%d" % fd.tell())

    fd.seek(-10, 2)
    print("file position :%d" % fd.tell())
    
    fd.seek(0, 2)
    print("file position :%d" % fd.tell())
    
    fd.seek(30, 0)
    print("file position :%d" % fd.tell())
    
    fd.seek(-10, 1)
    print("file position :%d" % fd.tell())
    
    print("Name of the file  :%s" % fd.name)
    print("Closed or not     :%r" % fd.closed)
    print("Opening mode      :%s" % fd.mode)

    fd.close()
    return

def write_to_file(filename):
    fd = open(filename, "r+")
    print("file position :%d" % fd.tell())

    fd.write("Hello world")
    print("file position :%d" % fd.tell())

    fd.seek(30, 0)
    print("file position :%d" % fd.tell())

    fd.write("Hello world")
    print("file position :%d" % fd.tell())

    fd.close()
    return

def write_to_binary_file(filename):
    fd = open(filename,'wb')
    print("File pointer position : ",fd.tell())
    
    str1=bytes("Hellow World",'utf-8')
    fd.write(str1)
    print("File pointer position : ",fd.tell())

    fd.seek(30,0)
    fd.write(str1)
    print("File pointer position : ",fd.tell())
    
    fd.close()

def main():
    filename = "t.txt"
    #simple_read_few_bytes(filename)
    #simple_read_twice(filename)
    #read_compleate_text_file(filename)
    #read_line_text_file_1(filename)
    #read_line_text_file_2(filename)
    #read_compleate_data(filename)
    #read_lines_text_file(filename)
    #file_operations_seek(filename)
    #write_to_file(filename)
    write_to_binary_file("a.txt")
    return
    
if (__name__ == "__main__"):
    main()

