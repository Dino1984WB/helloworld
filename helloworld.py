#this is a basic program to be run in a docker container and demonstrate system logging

def helloworld():
    print("hello, world!")

def repeat():
    num = range(10)
    for x in num:
        helloworld()

repeat()