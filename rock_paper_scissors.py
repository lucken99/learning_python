
from random import choice

options = ["rock", "paper", "scissors", "lizard", "spock", "wolf", "sponge", "air",
			 "water", "dragon", "devil", "gun", "snake", "human", "tree"]


resolve = {"rock": {"lizard", "scissors"}, #"sponge", "wolf",
						 # "fire", "snake", "human", "tree"}, 
			"paper": {"spock", "rock"},# "air", "water", "dragon", "devil",
							# "lightning", "gun"},
			"scissors": {"lizard", "paper"}, #"snake", "human", "tree", "wolf", 
							# "sponge", "air"},
			# "gun": {"rock", "fire", "scissors", "snake",
			# 			"human", "tree", "wolf"},
			# "lightning": {"gun", "rock", "fire", "scissors",
			# 				"snake", "human", "tree"},
			# "devil": {"lightning", "gun", "rock", "fire",
			# 				"scissors", "snake", "human"},
			# "dragon": {"devil", "lightning", "gun", "rock",
			# 				"fire", "scissors", "snake"},
			# "water": {"dragon", "devil", "lightning", "gun",
			# 			"rock", "fire", "scissors"},
			# "air": {"water", "dragon", "devil", "lightning", "gun",
			# 			"rock", "fire"},
			# "sponge": {"paper", "air", "water", "dragon",
			# 			 "devil", "lightning", "gun",},
			# "wolf": {"sponge", "paper", "air", "water", "dragon",
			# 			 "devil", "lightning"},
			# "tree": {"wolf", "sponge", "paper", "air",
			#  			"water", "dragon", "devil"},
			# "human": {"tree", "wolf", "sponge", "paper", "air",
			#  			"water", "dragon", "devil"},
			# "snake": {"human", "tree", "wolf", "sponge", "paper", "air",
			#  			"water"},
			# "fire": {"scissors", "snake", "human", "tree",
			# 			"wolf", "sponge", "paper"},
			"lizard": {"paper", "spock"},

			"spock": {"scissors", "rock"},

			}


user_name = input("Enter your name: ")
print("Hello,", user_name)

d = dict()
file = open("rating.txt")
users = file.readlines()
for line in users:
	name, ini_score = line.strip('\n').split()
	d[name] = ini_score
file.close()
global score
score = 0
if user_name in d.keys():
	score = int(d[user_name])

user_options = input()
if user_options == "":
	options = options[:3]
else:
	options = user_options.split(',')


def result(user_input, computer_choice):
	global score 
	if user_input == computer_choice:
		
		score += 50
		print("There is a draw (",user_input,")",sep="")
	elif computer_choice not in resolve[user_input]:
		print("Sorry, but the computer chose", computer_choice)
	else:
		score += 100
		print("Well done. The computer chose", computer_choice,"and failed")

	# elif user_input == "rock" and computer_choice == "scissors":
	# 	score += 100
	# 	print("Well done. The computer chose", computer_choice,"and failed")
	# 	return score
	# elif user_input == "paper" and computer_choice == "rock":
	# 	score += 100
	# 	print("Well done. The computer chose", computer_choice,"and failed")
	# 	return score
	# elif user_input == "paper" and computer_choice == "scissors":
	# 	print("Sorry, but the computer chose", computer_choice)
	# 	return score
	# elif user_input == "scissors" and computer_choice == "rock":
	# 	print("Sorry, but the computer chose", computer_choice)
	# 	return score
	# elif user_input == "scissors" and computer_choice == "paper":
	# 	score += 100
	# 	print("Well done. The computer chose", computer_choice,"and failed")
	# 	return score








print("Okay, let's start")
while True:
	user_input = input()
	if user_input == "!exit":
		print("Bye!")
		break
	elif user_input == "!rating":
		print("Your rating:", score)
	elif user_input in options:
		computer_choice = choice(options)
		result(user_input, computer_choice)
	else:
		print("Invalid input")



