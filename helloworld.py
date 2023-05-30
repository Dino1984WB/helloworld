#this is a basic program to be run in a docker container and demonstrate system logging


#prints helloworld once
def helloworld():
    print("hello, world!")

#repeatedly calls helloworld 10 times
def repeat():
    num = range(10)
    for x in num:
        helloworld()

#repeat function call
repeat()