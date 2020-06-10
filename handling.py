#############################                KEYBOARD INTERRUPT                  ######################################

def main() :
    print("Not interrupted yet")

#############################                   NAME ERROR                       ######################################

def nameError(s) :
    try :
        while s :
            print("Read : ", s)
            s = raw_input("Enter : ")
    except NameError:
        print("Name error")

#############################                   ZERO ERROR                       ######################################

def zeroError(num1, num2) :
    try:
        res = num1 / num2
        print(res)
    except ZeroDivisionError:
        print("Don't give zero as divisor")
    finally:
        print("Zero division error handled successfully")

############################                INPUT OUTPUT ERROR                   #######################################

def openFile(name) :
    try:
        fh = open(name, "r")
        content = fh.read()
        print(content)
        fh.close()
    except IOError:
        print("Can't find or locate the file")

###########################                   VALUE ERROR                        #######################################

def functionName(level) :
    if level < 1 :
        raise ValueError("Invalid level!", level)

functionName(int(input()))

openFile(input())

num1, num2 = [int(x) for x in input().split()]

zeroError(num1, num2)

nameError(input())

if __name__ == '__main__' :
    try:
        while True :
            main()
    except KeyboardInterrupt:
        print("Interrupted")
        exit(0)

