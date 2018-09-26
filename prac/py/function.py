def square(x):
    return x * x

def main():
    for i in range(8):      #if/for etc ends with: instead of {
        print("{} squared is {}".format(i, square(i)))  
                            #the braces are for the order of outputs following the . /similar to C

if __name__ == "__main__":
    main()
    # this line says, IF you are running this file (function.py)
    # run the function main()