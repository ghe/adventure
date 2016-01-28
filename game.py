def ask(question):
    return raw_input(question)

def say(what):
    print(what)

def verify_answer(answer, options):
    while answer not in options:
	answer = raw_input("Please choose from %s: " % " or ".join(options))
    return answer

say("You are in your bedroom. There is a door to your sister's room and a door to the hallway")
answer = ask("Would you like to go to the hallway or to your sister's room? ")
answer = verify_answer(answer, ["hallway", "sister's room"])
if answer == "hallway":
    say("You are in the hallway. You can change your sister's diaper here")
    say("you can also go to the bathroom")
    say("or you can do laundry")
    say("or you can go upstairs")
    answer = verify_answer(ask("what do you want to do? "), ["change diaper", "bathroom", "laundry", "upstairs"])
    say("great! you did %s" % answer)
else: #sister's room
    say("you get your sister to sleep")
