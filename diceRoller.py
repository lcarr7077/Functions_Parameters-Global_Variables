import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

myroll = 0

def roll():
    print("rolling.....")
    time.sleep(2)
    global myroll
    myroll = random.randint(1,6)


def show_dice(roll):
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    else:
        print(s6)

while myroll != 6:
    roll()
    show_dice(myroll)
