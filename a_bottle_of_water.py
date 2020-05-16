# This is a game
import random


def start():
    print("You wake up in a dark and cold room and don't know where you are.\n"
          "A strong pain at the back of your head makes you feel dizzy.\n"
          "You orient yourself and see a bottle of water on a table. \n"
          "There is also an open door.\n")
    print("What do you do?\n1. Take the bottle of water and walk through the door.\n"
          "2. Walk through the door without the bottle.")
    responds = input("> ")

    inventory = []

    if responds == '1':
        inventory.append('bottle')
        staircase(inventory)
    elif responds == '2':
        staircase(inventory)
    else:
        start()


def dead(string):
    print(string)
    print("\nTHE END.")
    exit(0)


def staircase(inventory):
    print("You enter a staircase. The stairs lead up and down.")
    print("What do you do?\n1. Take stairs down.\n"
          "2. Walk the stairs up.\n"
          "3. Go back.")
    responds = input("> ")

    if responds == '1':
        hall(inventory)
    elif responds == '2':
        tower(inventory)
    elif responds == '3':
        start()
    else:
        staircase(inventory)


def tower(inventory):
    print("You arrive on the top of a tower. A beautiful view of snowy mountains\n"
          "surprises you. On the wall you find a coin. There is only one way - down.")
    print("What do you do?\n1. Take the coin and go down.\n"
          "2. Do nothing.")
    responds = input("> ")

    if responds == '1':
        print("You throw the coin:")
        result = random.choice(['Heads!', 'Tails!'])

        if result == 'Heads!':
            print(result)
            dead("You jump from the tower and break your neck.")
        else:
            print(result)
            print("You take the coin and walk down the stairs.")
            inventory.append('coin')
            hall(inventory)
    elif responds == '2':
        dead("You freeze to death!")
    else:
        tower(inventory)


def hall(inventory):
    print("You are in a large empty hall. Each step you take is echoed. There is\n"
          "a large table with cutlery and dishes. On the wall there are pictures of ugly and \n"
          "scary looking people. At the end of the Hall are two doors. One to \n"
          "the left and one to the right.")
    print("What do you do?\n1. Take a fork.\n"
          "2. Take a plate.\n3. Take a knife.\n4. Take nothing.")
    responds1 = input("> ")

    if responds1 == '1':
        print("You add a fork to your inventory.")
        inventory.append('fork')
    elif responds1 == '2':
        print("You add a plate to your inventory.")
        inventory.append('plate')
    elif responds1 == '3':
        print("You add a knife to your inventory.")
        inventory.append('knife')
    elif responds1 == '4':
        print("You add nothing to your inventory.")
    else:
        print("You add nothing to your inventory.")

    print("What do you do next?\n1. Open the door on the right and walk through.\n"
          "2. Walk through the door on the left.")
    responds2 = input("> ")

    if responds2 == '1':
        print("The door is locked. You walk through the open door on the left.")
        trap(inventory)
    elif responds2 == '2':
        trap(inventory)
    else:
        hall(inventory)


def trap(inventory):
    print("You are trapped!! A tall and strong fellow, all dressed in black, stands\n"
          "in front of you. He draws a large sword. 'Go back into your chamber,' he shouts.\n"
          "Suddenly you see a key chain dangling from his coat.")

    if ('knife' in inventory or 'fork' in inventory) and len(inventory) > 1:
        print("You carry a weapon and other things. Your chances of winning a fight are 1:10.\n"
              "What do you do?\n1. Attack!\n2. Don't move.\n3. Walk back into your chamber.")

        responds1 = input("> ")

        if responds1 == '1':
            fight(inventory)
        elif responds1 == '2':
            dead("He repeats the command and after no response chops off your head!")
        elif responds1 == '3':
            dead("You starve to death.")
        else:
            dead("You mumble something. He chops off your head!")

    elif ('knife' in inventory or 'fork' in inventory) and len(inventory) == 1:
        print("You carry a weapon but no other things. Your chances of winning a fight are 1:100.\n"
              "What do you do?\n1. Attack!\n2. Don't move.\n3. Walk back into your chamber.")

        responds2 = input("> ")

        if responds2 == '1':
            fight(inventory)
        elif responds2 == '2':
            dead("He repeats the command and after no response chops off your head!")
        elif responds2 == '3':
            dead("You starve to death.")
        else:
            dead("You mumble something. He chops off your head!")

    elif not ('knife' in inventory or 'fork' in inventory) and len(inventory) > 1:
        print("You carry a few things but no weapon. Your chances of winning a fight are 1:1000.\n"
              "What do you do?\n1. Attack!\n2. Don't move.\n3. Walk back into your chamber.")

        responds3 = input("> ")

        if responds3 == '1':
            fight(inventory)
        elif responds3 == '2':
            dead("He repeats the command and after no response chops off your head!")
        elif responds3 == '3':
            dead("You starve to death.")
        else:
            dead("You mumble something. He chops off your head!")

    elif not ('knife' in inventory or 'fork' in inventory) and len(inventory) == 1:
        print("You carry a {0!s} but no weapon. Your chances of winning a fight are 1:10000.\n"
              "What do you do?\n1. Attack!\n2. Don't move.\n3. Walk back into your chamber.".format(inventory[0]))
        responds4 = input("> ")

        if responds4 == '1':
            fight(inventory)
        elif responds4 == '2':
            dead("He repeats the command and after no response chops off your head!")
        elif responds4 == '3':
            dead("You starve to death.")
        else:
            dead("You mumble something. He chops off your head!")

    elif len(inventory) == 0:
        print("You carry nothing. Your chances of winning a fight are 0.\n"
              "What do you do?\n1. Don't move.\n2. Walk back into your chamber.")

        responds5 = input("> ")

        if responds5 == '1':
            dead("He repeats the command and after no response chops off your head!")
        elif responds5 == '2':
            dead("You starve to death.")
        else:
            dead("You mumble something. He chops off your head!")

    else:
        print("You surrender and walk back into your chamber.")
        dead("You starve to death.")


def fight(inventory):

    item = 'knife' in inventory or 'fork' in inventory

    if item:
        print("You carry a weapon and {0} other item(s).".format(len(inventory) - 1))
        print("What do you do?\n1. Charge with the weapon.")

        if len(inventory) - 1 > 0:
            print("2. Throw one of the following items (enter item): {0}".format(', '.join(inventory)))
        else:
            pass

        responds1 = input("> ")

        if responds1 == '1':
            dead("You attack with your weapon. He chops off your head!")
        elif responds1 == 'coin':
            dead("He laughs and strikes you to the ground!")
        elif responds1 == 'bottle':
            print("The bottle strikes his head and he falls unconscious to the ground.\n"
                  "You grab the key and unlock the right door in the hall. You are free.")
            print("THE END")
            exit(0)
        elif responds1 == 'plate':
            dead("First he destroys the plate with his sword and then you.")
        elif responds1 == 'knife' or 'fork':
            dead("You miss. He destroys you.")
        else:
            dead("You mumble something. He chops off your head!")

    else:
        print("You carry one or more items.")
        print("What do you do?\n1. Throw one of the following item(s) (enter item): {0}".format(', '.join(inventory)))
        responds2 = input("> ")

        if responds2 == 'coin':
            dead("He laughs and strikes you to the ground!")
        elif responds2 == 'bottle':
            print("The bottle strikes his head and he falls unconscious to the ground.\n"
                  "You grab the key and unlock the right door in the hall. You are free.")
            print("THE END")
            exit(0)
        elif responds2 == 'plate':
            dead("First he destroys the plate with his sword and then you.")
        else:
            dead("You mumble something. He chops off your head!")


start()
