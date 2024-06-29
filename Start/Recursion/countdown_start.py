# Example file for Programming Foundations: Algorithms by Joe Marini
# use recursion to implement a countdown counter


def countdown(x):
    if x==0:
        return "Done!"
    else:
        print(x,"...")
        countdown(x-1)
        print(x,"hey")
    print("finished!")

countdown(5)
