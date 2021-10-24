import time
import os

def deletefiles():
    os.remove(f"{username}_diet.txt")
    os.remove(f"{username}_workout.txt")

def timenow():
    return time.asctime(time.localtime())

def log_entry(category,entry):
    with open(f"{username}_{category}.txt","a") as f:
        f.write(f"{timenow()} -->  {entry}\n")

def read_entry(category):
    with open(f"{username}_{category}.txt") as f:
        content= f.read()
        print(content)

def creation():
    try:
        with open(f"{username}_diet.txt","x") as p:
            pass
        with open(f"{username}_workout.txt","x") as p:
            pass
    except FileExistsError:
        pass
print("welcome to health management system\n")
continue_ = 0
while continue_ != 2 :
    username = input("enter your name here :" )
    creation()

    print("what would u log to \n")

    category = int(input("1.diet of the day\n2.execise of the day\n3.delete files\n"))
    if category == 1:
        print("what would u like to proceede with\n"
              "1.enter data 2.read data")
        choosing = int(input("enter the number for what would u like to choose:"))

        if choosing == 1:
            entry= input("what did u ate?")
            log_entry("diet",entry)
        elif choosing == 2:
            read_entry("diet")
        else:
            print("you have selected  wrong category")

    elif category  == 2:
        print("what would u like to proceede with\n"
              "1.enter data 2.read data")
        choosing = int(input("enter the number for what would u like to choose:"))

        if choosing == 1:
            entry =input("what workout have u done ? :")
            log_entry("workout",entry)
        elif choosing == 2:
            read_entry("workout")
        else:
            print("you have selected  wrong category")
    elif category == 3:
        deletefiles()
        print("sucesfully deleted ")
    else:
            print("you have selected  wrong category")
    continue_= int(input("1. To continue\n"
                         "2.exit :"))
    os.system("cls")