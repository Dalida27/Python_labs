import os
import string

#exercise 1
os.chdir('/Users/dalidaassan/Desktop/kbtu/')
for dirpath, dirnames, filenames in os.walk('/Users/dalidaassan/Desktop/kbtu/'):
    print('Current Path:', dirpath)
    print('Directories', dirnames)
    print('Files:', filenames)
    print()




#exericise 2
print('Exist:', os.access('/Users/dalidaassan/Desktop/githowto/repositories/', os.F_OK))
print('Readable:', os.access('/Users/dalidaassan/Desktop/githowto/repositories/', os.R_OK))
print('Writable:', os.access('/Users/dalidaassan/Desktop/githowto/repositories/', os.W_OK))
print('Executable:', os.access('/Users/dalidaassan/Desktop/githowto/repositories/', os.X_OK))




#exercise 3
path_input = input("Enter a path: ")

def is_exist(some_path):
    if os.path.exists(some_path):
        for dirname, _, filenames in os.walk(some_path):
            print("Directory:", dirname)
            print("Filenames:")
            for i in filenames:
                print(os.path.join(dirname, i))
            print()
    else:
        print("Path does not exist")

is_exist(path_input)



#ecxercise 4
def count_l(f):
    with open(f, "r") as file:
        num=0
        for line in file:
            num+=1
    return num


filename="/Users/dalidaassan/Desktop/githowto/repositories/lab6/some.txt"
print("num of lines:", count_l(filename))




#exercise 5
def to_list(f):
    listtof=[1, 2, 3]

    with open(f, "a") as file:
        file.write(", ".join(str(i) for i in listtof))


def to_file(f):
    with open(f, "r") as file:
        print(file.read())


filename="/Users/dalidaassan/Desktop/githowto/repositories/lab6/some.txt"

to_list(filename)
to_file(filename)



#exercise 6
def to_generate():
    for l in string.ascii_uppercase:
        filename = f"{l}.txt" 
        with open(filename, 'w') as file:
            file.write("some words and string")

to_generate()



#exercise 7
def my_func(f):
    with open(f, "r") as file:
        bll=file.read()

    newf="newf.txt"

    with open(newf, "w") as file:
        file.write(bll)

my_func("/Users/dalidaassan/Desktop/githowto/repositories/lab6/some.txt")




#exercise 8
my_file="/Users/dalidaassan/Desktop/githowto/repositories/lab6/8ex.txt"

def deletor(f):
    if not os.path.exists(f):
        print("Doesn't exist")
    else:
        if not os.access(f, os.X_OK):
            print("Not access")
        else:
            os.remove(f)
            print("Deleted!")
deletor(my_file)