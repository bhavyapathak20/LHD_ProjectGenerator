
# project generator

# importing random module
import random

# importing time module
import time


print("Random Project Generator")

# Making function


def project():
    project = ["Making Chess", "calculator", "hydrating reminder",
               "clock", "weather forcast", "study app"]

    print("Let me think of a project to assign you")

    time.sleep(4)

    print("The project for you is:", random.choice(project))

    time.sleep(2)
    
    again()


def again():
    
    another_project = input("Do you want another project? (Y/N): ").lower()

    if another_project == 'y':
        project()

    else:
        print("okay")

project()


    
