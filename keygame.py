inventory = []

def ask(question):
    return raw_input(question)

def say(what):
    print(what)

def verify_answer(answer, options):
    while answer not in options:
	answer = raw_input("Please choose from %s: " % " or ".join(options))
    return answer

def blue_room(describe=True):
    if describe:
        say("You are in a blue room. There is a red door to the east, a yellow door west and a box")
    answer = ask("Would you like to: go west, east or open the box? ")
    answer = verify_answer(answer, ["east", "west", "open box"])
    if answer == "east":
        if "red key" in inventory:
            red_room()
        else:
            say("you need a red key to open the red door")
            blue_room(False)
    elif answer == "west":
        if "yellow key" in inventory:
            yellow_room()
        else:
            say("you need a yellow key to open the yellow door")
            blue_room(False)
    else:
       if "yellow key" in inventory:
           say("the box is empty")
       else:
           say("you find a yellow key in the box")
           inventory.append("yellow key")
       blue_room(False)

def yellow_room(describe=True):
    if describe:
        say("You are in a yellow room. There is a blue door to the east and a box")
    answer = ask("Would you like to: go east or open the box? ")
    answer = verify_answer(answer, ["east", "open box"])
    if answer == "east":
        blue_room()
    else:
       if "red key" in inventory:
           say("the box is empty")
       else:
           say("you find a red key in the box")
           inventory.append("red key")
       yellow_room(False)

def red_room():
    say("You are in the red room!")

say("You left your favorite toys in the Red Room, but you forgot how to get there. Your goal in this game is to get back to the Red Room so you can play with your toy")
blue_room()
say("You have your toys and can play again! Congratulations!")
