# Limbus Calculator for Uptying & Leveling
import math
from urllib.request import proxy_bypass
# For math.ceil so things round up since you can't use a decimal of a Ticket

tutorial_check = 0 # If this counter reaches 1, It will stop repeating the Tutorial. Works similarly to message_delivered, but this is for Functions
message_delivered = 'NO' # this is for stopping a message from looping inside the loop (so it doesn't repeat)


exp_ticket1 = 50 # EXP Luxcavation I ticket
exp_ticket2 = 200 # EXP Luxcavation II ticket
exp_ticket3 = 1000 # EXP Luxcavation III ticket
exp_ticket4 = 3000 # EXP Luxcavation IV ticket
exp_ticket1_amount = 0 # literally the same thing as before, these ones COUNT how many are needed tho
exp_ticket2_amount = 0
exp_ticket3_amount = 0
exp_ticket4_amount = 0
used_experience = 0 # I'm scared of removing this because I don't know why I put it here so it stays here
exp_needed = 0 
total_experience = 0 # putting a reminder of my past foolishness believing this would be simpler than it actually is
exp_ticket1_total = 0
exp_ticket2_total = 0
exp_ticket3_total = 0
exp_ticket4_total = 0
excess_exp = 0

thread = 0
shards = 0
total_thread = 0
total_shards = 0

ego_tier = '' # ZAYIN, TETH, HE, WAW, ALEPH
id_rarity = '' # 0, 00, 000
tier = '' # I, II, III, IV, V (i pray for Tier V.............maybe even VI...........................................probably Tier V...)
id_level = '' # Current max 55
wanted_id_level = '' # Current max 55

yes_no = ''
user_input = '' 
exp_mix_amount = 0

exp_ticket1_check = 0 # These 4 are for EXP Mixing. Allowing the program to see which EXP Tickets can and can't be mixed. This is moreso for the third & fourth exp mixing because like........................ its easier to code this way lmao :sob:
exp_ticket2_check = 0
exp_ticket3_check = 0
exp_ticket4_check = 0

exp_level_threshold = [0, 10, 12, 15, 20, 27, 40, 59, 88, 125, 168, 227, 298, 381, 482, 591, 728, 885, 1064, 1261, 1488, 1739, 2016, 2327, 2674, 3047, 3456, 3899, 4378, 4899, 3899, 4378, 4899, 5468, 6075, 4899, 5468, 6075, 6722, 7413, 6075, 6722, 7413, 8156, 8953, 7413, 7413, 7413, 7413, 7413, 8156, 8156, 8156, 8156, 8156] # Will be updated when new levels are added
total_exp = [0, 10, 22, 37, 57, 84, 124, 183, 271, 396, 564, 791, 1089, 1470, 1952, 2543, 3271, 4156, 5220, 6481, 7969, 9708, 11724, 14051, 16725, 19772, 23228, 27127, 31505, 36404, 40303, 44681, 49580, 55048, 61123, 66022, 71490, 77565, 84287, 91700, 97775, 1004497, 111910, 120066, 129019, 136432, 143845, 151258, 158671, 166084, 174240, 182396, 190552, 198708, 206864] # Will be updated when new levels are added
id_level_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]




# EGO UPTYING SORTING OUT
def ego_uptie_calculator():
	global total_shards # only reason I'm making this public is bc like I just wanna figure out how much resources it'll take for me to uptie 4 all my IDs + EGOs lel, and as of writing this, I'm very close to it!!!! (ID wise atleast, EGO wise is still............quite, yk..)
	global shards
	global total_thread
	global thread
	global ego_tier
	global tier


	if ego_tier == 'ZAYIN':
		if tier == 2:
			thread = 0
			thread += 20
			total_thread += 20
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 2.')
		elif tier == 3:
			thread = 0
			thread += 60
			total_thread += 60
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 3.')
		elif tier == 4:
			thread = 0
			thread += 110
			total_thread += 110
			shards = 0
			shards += 80
			total_shards += 80
			print(f'{thread} Thread & {shards} egoshards are required for a {ego_tier} EGO to get to Uptie 4.')
		elif tier > 4:
			print("Tier V EGOs haven't released yet!!!!!! Head! Execute this fool!")
		else:
			pass

	elif ego_tier == 'TETH':
		if tier == 2:
			thread = 0
			thread += 25
			total_thread += 25
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 2.')
		elif tier == 3:
			thread = 0
			thread += 70
			total_thread += 70
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 3.')
		elif tier == 4:
			thread = 0
			thread += 130
			total_thread += 130
			shards = 0
			shards += 90
			total_shards += 90
			print(f'{thread} Thread & {shards} egoshards are required for a {ego_tier} EGO to get to Uptie 4.')
		elif tier > 4:
			print("Tier V EGOs haven't released yet!!!!!! Head! Execute this fool!")
		else:
			pass


	elif ego_tier == 'HE':
		if tier == 2:
			thread = 0
			thread += 30
			total_thread += 30
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 2.')
		elif tier == 3:
			thread = 0
			thread += 80
			total_thread += 80
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 3.')
		elif tier == 4:
			thread = 0
			thread += 150
			total_thread += 150
			shards = 0
			shards += 100
			total_shards += 100
			print(f'{thread} Thread & {shards} egoshards are required for a {ego_tier} EGO to get to Uptie 4.')
		elif tier > 4:
			print("Tier V EGOs haven't released yet!!!!!! Head! Execute this fool!")
		else:
			pass


	elif ego_tier == 'WAW':
		if tier == 2:
			thread = 0
			thread += 35
			print(f'{thread} Thread is required for A {ego_tier} EGO to get to Uptie 2.')
		elif tier == 3:
			thread = 0
			thread += 90
			print(f'{thread} Thread is required for a {ego_tier} EGO to get to Uptie 3.')
		elif tier == 4:
			thread = 0
			thread += 170
			total_thread += 170
			shards = 0
			shards += 150
			total_shards += 150
			print(f'{thread} Thread & {shards} egoshards are required for a {ego_tier} EGO to get to Uptie 4.')
		elif tier > 4:
			print("Tier V EGOs haven't released yet!!!!!! Head! Execute this fool!")
		else:
			pass

	elif ego_tier == 'ALEPH':
		print("There's no ALEPH EGO yet :c")

	else:
		print('Invalid. Please Check that you typed it correctly.')
		pass

# ID UPTYING SORTING OUT
def id_uptie_calculator():
	global thread # I kinda hope someone reads this code tbh, likeee............. I dunno, I think it'd be nice. What Project Moon game is your favourite, viewer? (and why?)
	global total_thread
	global shards
	global total_shards 
	global id_level
	global id_rarity
	global tier

	if id_rarity == '0':
		if tier == 4:
			thread = 0
			thread += 50
			total_thread += 50
			shards = 0
			shards += 20
			total_shards += 20
			print(f'{thread} Thread & {shards} egoshards are required for an {id_level} Identity to get to Uptie 4.')
		elif tier < 4:
			print('Cmon.. Just play the game..They get to uptie 3 automatically...')
		elif tier > 4:
			print("So far, there's no Tier V for IDs confirmed, but I'm hopin!!! :'D one day . . .")
		else:
			pass

	elif id_rarity == '00':
			if tier == 2:
				thread = 0
				thread += 10
				total_thread += 10
				print(f'{thread} Thread is required for an {id_level} Identity to get to Uptie 2.')
			elif tier == 3:
				thread = 0
				thread += 40
				total_thread += 40
				print(f'{thread} Thread is required for an {id_level} Identity to get to Uptie 3.')
			elif tier == 4:
				thread = 0
				thread += 100
				total_thread += 100
				shards = 0
				shards += 30
				total_shards += 30
				print(f'{thread} Thread & {shards} egoshards are required for an {id_level} Identity to get to Uptie 4.')
			elif tier > 4:
				print("So far, there's no Tier V for IDs confirmed, but I'm hopin!!! :'D one day . . .")
			else:
				pass

	elif id_rarity == '000':
			if tier == 2:
				thread = 0
				thread += 20
				total_thread += 20
				print(f'{thread} Thread is required for an {id_level} Identity to get to Uptie 2.')
			elif tier == 3:
				thread = 0
				thread += 80
				total_thread += 80
				print(f'{thread} Thread is required for an {id_level} Identity to get to Uptie 3.')
			elif tier == 4:
				thread = 0
				thread += 150
				total_thread += 150
				shards = 0
				shards += 50
				total_shards += 50
				print(f'{thread} Thread & {shards} egoshards are required for an {id_level} Identity to get to Uptie 4.')		
			elif tier > 4:
				print("So far, there's no Tier V for IDs confirmed, but I'm hopin!!! :'D one day . . .")
			else:
				pass
	else:
		pass

# The Subtraction method for the Totals
def thread_shard_exp_total_subtract():
	global user_input
	global exp_ticket1_total
	global exp_ticket2_total
	global exp_ticket3_total
	global exp_ticket4_total
	global total_thread
	global total_shards
	global yes_no

	while True:
		yes_no = input('Would you like to remove some EXP Luxcavation I Tickets?\n>').upper() # EXP Luxcavation I
		if yes_no == 'YES':
			try:
				user_input = int(input('How many EXP Luxcavation I Tickets do you want to remove?\n>'))
			except ValueError:
				print('Please input an Integer.')
				pass
			if exp_ticket1_total - user_input > 0 or exp_ticket1_total - user_input == 0:
				exp_ticket1_total = exp_ticket1_total - user_input
				print(f'You now have {exp_ticket1_total} EXP Luxcavation I Tickets.')
				break
			elif exp_ticket1_total - user_input < 0:
				print('You cannot remove more EXP Tickets than you currently have in the Total, sorry; Try Again.')
				pass
			else:
				pass
		elif yes_no == 'NO':
			break
		else:
			print('Please input either Yes or No.')
			pass

	while True:
		yes_no = input('Would you like to remove some EXP Luxcavation II Tickets?\n>').upper() # EXP Luxcavation II
		if yes_no == 'YES':
			try:
				user_input = int(input('How many EXP Luxcavation II Tickets do you want to remove?\n>'))
			except ValueError:
				print('Please input an Integer.')
				pass
			if exp_ticket2_total - user_input > 0 or exp_ticket2_total - user_input == 0:
				exp_ticket2_total = exp_ticket2_total - user_input
				print(f'You now have {exp_ticket2_total} EXP Luxcavation II Tickets.')
				break
			elif exp_ticket2_total - user_input < 0:
				print('You cannot remove more EXP Tickets than you currently have in the Total, sorry; Try Again.')
				pass
			else:
				pass
		elif yes_no == 'NO':
			break
		else:
			print('Please input either Yes or No.')
			pass

	while True:
		yes_no = input('Would you like to remove some EXP Luxcavation III Tickets?\n>').upper() # EXP Luxcavation III
		if yes_no == 'YES':
			try:
				user_input = int(input('How many EXP Luxcavation III Tickets do you want to remove?\n>'))
			except ValueError:
				print('Please input an Integer.')
				pass
			if exp_ticket3_total - user_input > 0 or exp_ticket3_total - user_input == 0:
				exp_ticket3_total = exp_ticket3_total - user_input
				print(f'You now have {exp_ticket3_total} EXP Luxcavation III Tickets.')
				break
			elif exp_ticket3_total - user_input < 0:
				print('You cannot remove more EXP Tickets than you currently have in the Total, sorry; Try Again.')
				pass
			else:
				pass
		elif yes_no == 'NO':
			break
		else:
			print('Please input either Yes or No.')
			pass

	while True:
		yes_no = input('Would you like to remove some EXP Luxcavation IV Tickets?\n>').upper() # EXP Luxcavation IV
		if yes_no == 'YES':
			try:
				user_input = int(input('How many EXP Luxcavation IV Tickets do you want to remove?\n>'))
			except ValueError:
				print('Please input an Integer.')
				pass
			if exp_ticket4_total - user_input > 0 or exp_ticket4_total - user_input == 0:
				exp_ticket4_total = exp_ticket4_total - user_input
				print(f'You now have {exp_ticket4_total} EXP Luxcavation IV Tickets.')
				break
			elif exp_ticket4_total - user_input < 0:
				print('You cannot remove more EXP Tickets than you currently have in the Total, sorry; Try Again.')
				pass
			else:
				pass
		elif yes_no == 'NO':
			break
		else:
			print('Please input either Yes or No.')
			pass

	while True:
		yes_no = input('Would you like to remove some Thread?\n>').upper() # Thread
		if yes_no == 'YES':
			try:
				user_input = int(input('How many Thread do you want to remove?\n>'))
			except ValueError:
				print('Please input an Integer.')
				pass
			if total_thread - user_input > 0 or total_thread - user_input == 0:
				total_thread = total_thread - user_input
				print(f'You now have {total_thread} EXP Luxcavation II Tickets.')
				break
			elif total_thread - user_input < 0:
				print('You cannot remove more Thread than you currently have in the Total, sorry; Try Again.')
				pass
			else:
				pass
		elif yes_no == 'NO':
			break
		else:
			print('Please input either Yes or No.')
			pass

	while True:
		yes_no = input('Would you like to remove some Shards?\n>').upper() # Egoshards
		if yes_no == 'YES':
			try:
				user_input = int(input('How many Egoshards do you want to remove?\n>'))
			except ValueError:
				print('Please input an Integer.')
				pass
			if total_shards - user_input > 0 or total_shards - user_input == 0:
				total_shards = total_shards - user_input
				print(f'You now have {total_shards} EXP Luxcavation II Tickets.')
				break
			elif total_shards - user_input < 0:
				print('You cannot remove more Egoshards than you currently have in the Total, sorry; Try Again.')
				pass
			else:
				pass
		elif yes_no == 'NO':
			break
		else:
			print('Please input either Yes or No.')
			pass

# Show how much Thread + Shards + EXP tickets are needed in Total
def thread_shard_exp_total():
	global total_thread
	global total_shards
	global exp_ticket1_total
	global exp_ticket2_total
	global exp_ticket3_total
	global exp_ticket4_total
	global user_input

	print('\nFor Thread & Egoshards you Require: ')
	print(f'{total_shards} Egoshards & {total_thread} Thread!')
	print('\nFor Experience Tickets, you Need: ')
	print(f'{exp_ticket1_total} EXP Luxcavation I Tickets!')
	print(f'{exp_ticket2_total} EXP Luxcavation II Tickets!!')
	print(f'{exp_ticket3_total} EXP Luxcavation III Tickets!!!')
	print(f'{exp_ticket4_total} EXP Luxcavation IV Tickets!!!!')

	while True:
		try:
			user_input = int(input('\nWould you like to \n1. Clear the Totals?\n2. Subtract part of the Totals?\n3. Display the Totals?\n4. Return to the Menu without any changes?\n>')) # only reason its not lower is bc i wanna make it match the ZAYIN-ALEPH stuff lel
		except ValueError:
			print('Please input an Integer.')
			pass

		if user_input == 4: # Ignore that this is counting backwards. I just didn't wanna change the code i did before bc this saves me like... atleast a minute of time lmao
			print('\nVery Well! Have a lovely day with this info, and may the Prescripts bless ya!')
			break

		elif user_input == 3:
			print('\nFor Thread & Egoshards you Require: ')
			print(f'{total_shards} Egoshards & {total_thread} Thread!')
			print('\nFor Experience Tickets, you Need: ')
			print(f'{exp_ticket1_total} EXP Luxcavation I Tickets!')
			print(f'{exp_ticket2_total} EXP Luxcavation II Tickets!!')
			print(f'{exp_ticket3_total} EXP Luxcavation III Tickets!!!')
			print(f'{exp_ticket4_total} EXP Luxcavation IV Tickets!!!!')

		elif user_input == 2:
			print('You have chosen to Subtract part of the Totals.')
			thread_shard_exp_total_subtract()

		elif user_input == 1:
			print('\nVery Well!..Good luck with whatever you use this for next!!!')
			total_shards = 0
			total_thread = 0
			exp_ticket1_total = 0
			exp_ticket2_total = 0
			exp_ticket3_total = 0
			exp_ticket4_total = 0
			break

		else:
			print('Invalid. Please Input an Integer.')
			pass

# EXP Required Calculator
def exp_required_calculator(): # I would like to say that I'm not in anyway a coding pro. please don't Judge TOO harshly :')
	global exp_needed # this isn't good practice but like.......................I'm not a pro so yk, it is what it is
	global total_exp
	global wanted_id_level
	global id_level
	global exp_ticket1
	global exp_ticket2
	global exp_ticket3
	global exp_ticket4
	global exp_ticket1_amount
	global exp_ticket2_amount
	global exp_ticket3_amount
	global exp_ticket4_amount
	global user_input
	global exp_ticket1_total
	global exp_ticket2_total
	global exp_ticket3_total
	global exp_ticket4_total

	if user_input == 1:
		exp_ticket1_amount = exp_needed / exp_ticket1
		exp_ticket1_total += math.ceil(exp_ticket1_amount)
		print(f'You need {math.ceil(exp_ticket1_amount)} Exp Luxcavation I Tickets!')

	elif user_input == 2:
		exp_ticket2_amount = exp_needed / exp_ticket2
		exp_ticket2_total += math.ceil(exp_ticket2_amount)
		print(f'You need {math.ceil(exp_ticket2_amount)} Exp Luxcavation II Tickets!')

	elif user_input == 3:
		exp_ticket3_amount = exp_needed / exp_ticket3
		exp_ticket3_total += math.ceil(exp_ticket3_amount)
		print(f'You need {math.ceil(exp_ticket3_amount)} Exp Luxcavation III Tickets!')

	elif user_input == 4:
		exp_ticket4_amount = exp_needed / exp_ticket4
		exp_ticket4_total += math.ceil(exp_ticket4_amount)
		print(f'You need {math.ceil(exp_ticket4_amount)} Exp Luxcavation IV Tickets!')

	else:
		pass

# The Tutorial for EXP Mixing
def exp_mix_tutorial():
	global id_level
	global wanted_id_level
	global exp_ticket2_amount
	global exp_ticket2
	global exp_ticket4_amount
	global exp_ticket4
	global exp_needed
	global total_exp
	global excess_exp
	global tutorial_check

	print('Tutorial Time!!! (As the Prescripts Demand)')
	while True:
		try:
			id_level = int(input('First, Please set what your ID Level STARTS at.\n>'))
		except ValueError:
			print('Please input an Integer.')
		else:
			break
	while True:
		try:
			wanted_id_level = int(input('Now set what Level you WANT your ID to reach.\n>'))
		except ValueError:
			print('Please input an Integer')
		else:
			break
	exp_needed = total_exp[wanted_id_level-1] - total_exp[id_level-1]
	print('For the Tutorial you will be Mixing EXP Luxcavation Tickets II & IV.')

	while True:
		try:
			exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
		except ValueError:
			print('Please input an Integer')
			pass
		if exp_ticket2_amount == int:
			break
		else:
			pass

	while True:
		try: 
			exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
		except ValueError:
			print('Please input an Integer')
			pass
		if exp_ticket4_amount == int:
			break
		else:
			pass

	excess_exp = exp_needed - ((exp_ticket4_amount * exp_ticket4)+(exp_ticket2_amount * exp_ticket2)) # Calculates how much EXP is left-over after the calculation. # abs() prevents it from being a negative number.
	if excess_exp < 0: # If this value is Negative, it has gone overboard and there is an unnecessary amount of exp tickets use
		print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
	elif excess_exp > 0: # If this value is Positive, it has gone overboard and there isn't enough exp tickets used
		print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
		exp_ticket2_amount = excess_exp / exp_ticket2
		exp_ticket4_amount = excess_exp / exp_ticket4
		print(f"\nYou Could use either {exp_ticket2_amount} EXP Luxcavation II Tickets\nOR You could use {exp_ticket4_amount} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
	elif excess_exp == 0: # If this value is 0, the EXP Tickets used are the perfect amount
		print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
	else:
		pass
	tutorial_check += 1

# honestly this was the 2nd easiest of the choices to code
def mix_fourth_choice():
	global user_input
	global exp_ticket1
	global exp_ticket1_amount
	global exp_ticket2
	global exp_ticket2_amount
	global exp_ticket3
	global exp_ticket3_amount
	global exp_ticket4
	global exp_ticket4_amount
	global exp_mix_amount
	global excess_exp
	global exp_needed
	global exp_ticket1_check
	global exp_ticket2_check
	global exp_ticket3_check
	global exp_ticket4_check

	if exp_ticket1_check == 1 and exp_ticket2_check == 1 and exp_ticket3_check == 1:
		while True:
			try:
				exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 4 EXP Tickets
		if excess_exp < 0: 
			print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets, like damn!!!")
		elif excess_exp > 0:
			print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket4_amount = excess_exp / exp_ticket4
			print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\n\nOR ye could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!!!\nOR ya could use a mixture of all four!")
		elif excess_exp == 0:
			print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
		else:
			pass	
	
	elif exp_ticket1_check == 1 and exp_ticket3_check == 1 and exp_ticket4_check == 1:
		while True:
			try:
				exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 4 EXP Tickets
		if excess_exp < 0: 
			print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets, like damn!!!")
		elif excess_exp > 0:
			print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket4_amount = excess_exp / exp_ticket4
			print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\n\nOR ye could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!!!\nOR ya could use a mixture of all four!")
		elif excess_exp == 0:
			print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
		else:
			pass
	
	elif exp_ticket1_check == 1 and exp_ticket2_check == 1 and exp_ticket4_check == 1:
		while True:
			try:
				exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 4 EXP Tickets
		if excess_exp < 0: 
			print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets, like damn!!!")
		elif excess_exp > 0:
			print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket4_amount = excess_exp / exp_ticket4
			print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\n\nOR ye could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!!!\nOR ya could use a mixture of all four!")
		elif excess_exp == 0:
			print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
		else:
			pass

	elif exp_ticket2_check == 1 and exp_ticket3_check == 1 and exp_ticket4_check == 1:
		while True:
			try:
				exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 4 EXP Tickets
		if excess_exp < 0: 
			print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets, like damn!!!")
		elif excess_exp > 0:
			print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket4_amount = excess_exp / exp_ticket4
			print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\n\nOR ye could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!!!\nOR ya could use a mixture of all four!")
		elif excess_exp == 0:
			print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
		else:
			pass

	else:
		pass

# this one was very repetitive
def mix_third_choice():
	global user_input
	global exp_ticket1
	global exp_ticket1_amount
	global exp_ticket2
	global exp_ticket2_amount
	global exp_ticket3
	global exp_ticket3_amount
	global exp_ticket4
	global exp_ticket4_amount
	global exp_mix_amount
	global excess_exp
	global exp_needed
	global exp_ticket1_check
	global exp_ticket2_check
	global exp_ticket3_check
	global exp_ticket4_check


	if exp_ticket1_check == 1 and exp_ticket2_check == 1: # EXP Ticket 1 + 2..on second thought these titles are self-explanatory.
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Third Choice from:\n1. EXP Luxcavation Ticket III\n2. EXP Luxcavation Ticket IV\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1: # EXP3
			exp_ticket3_check = 1
			while True:
				try:
					exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # EXP4
			exp_ticket4_check = 1
			while True:
				try:
					exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass




	elif exp_ticket1_check == 1 and exp_ticket3_check == 1:
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Third Choice from:\n1. EXP Luxcavation Ticket II\n2. EXP Luxcavation Ticket IV\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1: # EXP2
			exp_ticket2_check = 1
			while True:
				try:
					exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # EXP4
			exp_ticket4_check = 1
			while True:
				try:
					exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


	elif exp_ticket1_check == 1 and exp_ticket4_check == 1:
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Third Choice from:\n1. EXP Luxcavation Ticket II\n2. EXP Luxcavation Ticket III\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1: # EXP2
			exp_ticket2_check = 1
			while True:
				try:
					exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # EXP3
			exp_ticket3_check = 1
			while True:
				try:
					exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass



	elif exp_ticket2_check == 1 and exp_ticket3_check == 1:
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Third Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket IV\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1: # EXP1
			exp_ticket1_check = 1
			while True:
				try:
					exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # EXP4
			exp_ticket4_check = 1
			while True:
				try:
					exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


	elif exp_ticket2_check == 1 and exp_ticket4_check == 1:
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Third Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket III\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1: # EXP1
			exp_ticket1_check = 1
			while True:
				try:
					exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # EXP3
			exp_ticket3_check = 1
			while True:
				try:
					exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


	elif exp_ticket3_check == 1 and exp_ticket4_check == 1:
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Third Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket III\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1: # EXP1
			exp_ticket1_check = 1
			while True:
				try:
					exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # EXP2
			exp_ticket2_check = 1
			while True:
				try:
					exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 3:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 3 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR you could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!\nOR ya could use a mixture of all three!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount == 4:
				mix_fourth_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


	else:
		pass
	
# this one was the hardest of the 4 choices to code
def mix_second_choice():
	global user_input
	global exp_ticket1
	global exp_ticket1_amount
	global exp_ticket2
	global exp_ticket2_amount
	global exp_ticket3
	global exp_ticket3_amount
	global exp_ticket4
	global exp_ticket4_amount
	global exp_mix_amount
	global excess_exp
	global exp_needed
	global exp_ticket1_check
	global exp_ticket2_check
	global exp_ticket3_check
	global exp_ticket4_check

	if user_input == 1: # First Choice EXP 1
		exp_ticket1_check = 1
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Second Choice from:\n1. EXP Luxcavation Ticket II\n2. EXP Luxcavation Ticket III\n3. EXP Luxcavation Ticket IV\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1:
			exp_ticket2_check = 1
			while True:
				try:
					exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket2_amount * exp_ticket2)) # Calculation for 2 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket2_amount = excess_exp / exp_ticket2
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


		elif user_input == 2: # For EXP Luxcavation Tickets III
			exp_ticket3_check = 1
			while True:
				try:
					exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket3_amount * exp_ticket3))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass




		elif user_input == 3: # For EXP Luxcavation Tickets IV
			exp_ticket4_check = 1
			while True:
				try:
					exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket4_amount * exp_ticket4))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


		else:
			pass



	elif user_input == 2: # First Choice EXP 2
		exp_ticket2_check = 1
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Second Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket III\n3. EXP Luxcavation Ticket IV\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1:
			exp_ticket1_check = 1
			while True:
				try:
					exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket1_amount * exp_ticket1)) 
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket1_amount = excess_exp / exp_ticket1
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


		elif user_input == 2: # For EXP Luxcavation Tickets III
			exp_ticket3_check = 1
			while True:
				try:
					exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket3_amount * exp_ticket3))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 3: # For EXP Luxcavation Tickets IV
			exp_ticket4_check = 1
			while True:
				try:
					exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket4_amount * exp_ticket4))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass


		else:
			pass

	elif user_input == 3: # First Choice EXP 3
		exp_ticket3_check = 1
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Second Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket II\n3. EXP Luxcavation Ticket IV\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1:
			exp_ticket1_check = 1
			while True:
				try:
					exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket3_amount * exp_ticket3)+(exp_ticket1_amount * exp_ticket1)) # Calculation for 2 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	
			elif exp_mix_amount >= 3:
				mix_third_choice()
			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # For EXP Luxcavation Tickets II
			exp_ticket2_check = 1
			while True:
				try:
					exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket3_amount * exp_ticket3)+(exp_ticket2_amount * exp_ticket2))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket3_amount = excess_exp / exp_ticket3
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	
			elif exp_mix_amount >= 3:
				mix_third_choice()
			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 3: # For EXP Luxcavation Tickets IV
			exp_ticket4_check = 1
			while True:
				try:
					exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR You could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass
		else:
			pass

	elif user_input == 4: # First Choice EXP 4
		exp_ticket4_check = 1
		while True:
			try:
				user_input = int(input("Please input which Ticket you'd like as your Second Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket II\n3. EXP Luxcavation Ticket III\n>"))
			except ValueError:
				print('Please input an Integer.')
			else:
				break

		if user_input == 1:
			exp_ticket1_check = 1
			while True:
				try:
					exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket1_amount * exp_ticket1)+(exp_ticket4_amount * exp_ticket4)) # Calculation for 2 EXP Tickets
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket1_amount = excess_exp / exp_ticket1
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets\nOR You could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 2: # For EXP Luxcavation Tickets II
			exp_ticket2_check = 1
			while True:
				try:
					exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket2_amount * exp_ticket2)+(exp_ticket4_amount * exp_ticket4))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket2_amount = excess_exp / exp_ticket2
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets\nOR You could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		elif user_input == 3: # For EXP Luxcavation Tickets III
			exp_ticket3_check = 1
			while True:
				try:
					exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
				except ValueError:
					print('Please input an Integer and Try again.')
				else:
					break
			if exp_mix_amount == 2:
				excess_exp = exp_needed - ((exp_ticket3_amount * exp_ticket3)+(exp_ticket4_amount * exp_ticket4))
				if excess_exp < 0: 
					print(f"You have an excess of {abs(excess_exp)} EXP!!!! That's WAYYYYYYYYYYYYYYY too much EXP! Ya don't need so much! Use less EXP tickets!!!")
				elif excess_exp > 0:
					print(f"You don't have enough EXP! Ya only have {excess_exp} left! To fix this you could...\n")
					exp_ticket3_amount = excess_exp / exp_ticket3
					exp_ticket4_amount = excess_exp / exp_ticket4
					print(f"\nYou Could use either {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets\nOR You could use {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets\nOR ya could use a mixture of both!")
				elif excess_exp == 0:
					print("Oh, well.. There's not much to say, that's exactly spot on. Good job. Neato. Cool, cool. HELL YEAH RAHHHHHHHHHHHHHHH")
				else:
					pass	

			elif exp_mix_amount >= 3:
				mix_third_choice()

			else: 
				print("I don't know how you got this Error.")
				pass

		else:
			pass

	else:
		pass

# This was the easiest part for these 4 choices :')
def mix_first_choice(): 
	global user_input
	global exp_ticket1_amount
	global exp_ticket2_amount
	global exp_ticket3_amount
	global exp_ticket4_amount
	global exp_mix_amount
	global exp_ticket1_check
	global exp_ticket2_check
	global exp_ticket3_check
	global exp_ticket4_check

	exp_ticket1_check = 0
	exp_ticket2_check = 0
	exp_ticket3_check = 0
	exp_ticket4_check = 0

	if user_input == 1: 
		print("You have chosen to use EXP Luxcavation Ticket I's as your first pick.")
		while True:
			try:
				exp_ticket1_amount = int(input('How many EXP Luxcavation I Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		if exp_mix_amount >= 2:
			mix_second_choice()
		else: 
			print("I don't know how you got this Error.")
			pass

	elif user_input == 2:
		print("You have chosen to use EXP Luxcavation Ticket II's as your first pick.")
		while True:
			try:
				exp_ticket2_amount = int(input('How many EXP Luxcavation II Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		if exp_mix_amount >= 2:
			mix_second_choice()
		else: 
			print("I don't know how you got this Error.")
			pass		

	elif user_input == 3:
		print("You have chosen to use EXP Luxcavation Ticket III's as your first pick.")
		while True:
			try:
				exp_ticket3_amount = int(input('How many EXP Luxcavation III Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		if exp_mix_amount >= 2:
			mix_second_choice()
		else: 
			print("I don't know how you got this Error.")
			pass

	elif user_input == 4:
		print("You have chosen to use EXP Luxcavation Ticket IV's as your first pick.")
		while True:
			try:
				exp_ticket4_amount = int(input('How many EXP Luxcavation IV Tickets would you like?\n>'))
			except ValueError:
				print('Please input an Integer and Try again.')
			else:
				break
		if exp_mix_amount >= 2:
			mix_second_choice()
		else: 
			print("I don't know how you got this Error.")
			pass

# EXP Mixing, though this one sucks B.T.W.
def mixing_exp_tickets():
	global user_input
	global id_level
	global wanted_id_level
	global total_exp
	global exp_needed
	global excess_exp
	global tutorial_check
	global exp_ticket1
	global exp_ticket2
	global exp_ticket3
	global exp_ticket4
	global exp_ticket1_amount
	global exp_ticket2_amount
	global exp_ticket3_amount
	global exp_ticket4_amount
	global user_input
	global exp_ticket1_total
	global exp_ticket2_total
	global exp_ticket3_total
	global exp_ticket4_total
	global yes_no
	global exp_mix_amount


	if tutorial_check > 0: # If the Value is above Zero, it always starts this ELIF statement, no matter what. I hope.
		while True:
			try:
				id_level = int(input('First, Please set what your ID Level STARTS at.\n>'))
			except ValueError:
				print('Please input an Integer.')
			else:
				break
		while True:
			try:
				wanted_id_level = int(input('Now set what Level you WANT your ID to reach.\n>'))
			except ValueError:
				print('Please input an Integer')
			else:
				break
		exp_needed = total_exp[wanted_id_level-1] - total_exp[id_level-1]
		while True:
			try:
				exp_mix_amount = int(input('Would you like to Mix 2, 3, or 4 EXP Tickets?'))
			except ValueError:
				print('Please input an Integer.')
			else:
				if exp_mix_amount > 4:
					print("You can only do 4, as there are only 4 EXP Ticket Types so far. Please try again.")
					pass
				elif 1 < exp_mix_amount <= 4:
					while True:
						try:
							user_input = int(input("Please input which Ticket you'd like as your First Choice from:\n1. EXP Luxcavation Ticket I\n2. EXP Luxcavation Ticket II\n3. EXP Luxcavation Ticket III\n4. EXP Luxcavation Ticket IV\n>"))
						except ValueError:
							print('Please input an Integer.')
						else:
							break
					mix_first_choice()
					break
				elif exp_mix_amount == 1:
					print("why did you choose this if you didn't wanna mix tickets???? Go back to the Menu and Type 3 for the Levels one.")
				else:
					pass

	elif tutorial_check == 0:
		while True:
			yes_no = input('Would you like to skip the Tutorial?').upper()
			if yes_no == 'YES':
				print('Very well, once you boot this Section up again, the Tutorial will not show.')
				tutorial_check =+ 1
				break
			elif yes_no == 'NO':
				exp_mix_tutorial()
			else:
				print('Input Yes or No.')
				pass

	else:
		pass

# Sharding an ID/EGO
def sharding():
	global user_input
	global total_shards
	
	try:
		user_input = int(input('\nYou have chosen to Shard. Would you like to Shard:\n1.A 00 ID?\n2.A 000 ID?\n3.An EGO?\n>'))
	except ValueError:
		print('Error. Please choose an Integer next time.')
	else:
		if user_input == 1:
			print('You have chosen to Shard a 00 ID, which adds 150 Egoshards to your Total Amount!')
			total_shards += 150

		elif user_input == 2:
			print('You have chosen to Shard a 000 ID, which adds 400 Egoshards to your Total Amount!')
			total_shards += 400

		elif user_input == 3:
			print('You have chosen to Shard an EGO, which adds 400 Egoshards to your Total Amount!')
			total_shards += 400

		else:
			pass

# MENU Screen
def menu_screen():
	global user_input # final global variable for now (nvm i lied)
	global ego_tier
	global tier
	global id_level
	global wanted_id_level
	global total_exp
	global exp_needed
	global id_rarity
	global message_delivered

	print('\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n1. Thread & Uptie for EGOs\n2. Thread & Uptie for IDs\n3. Levels for IDs\n4. Play around with Mixing Level Tickets!\n5. Sharding an ID/EGO\n6. Total Shard, Thread & Total EXP Ticket Amount!\n7. Exit the Calculator\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
	try:
		user_input = int(input('\n>'))
	except ValueError:
		print('Please input an Integer.')
		pass

	if user_input == 1:
		ego_tier = input('Please choose what EGO Rank ya want from ZAYIN, TETH, HE, WAW or ALEPH!!!\n>').upper()
		tier = int(input('Please choose what EGO Tier ya desire to Reach from 2, 3 or 4!'))
		ego_uptie_calculator()

	elif user_input == 2:
		id_rarity = input(f"\nPlease choose your ID's Rarity from 0, 00 OR 000!!!\n>")
		tier = int(input(f"\nNow please choose your Desired Tier you wanna get from 2, 3 or 4!!!\n>"))
		id_uptie_calculator()

	elif user_input == 3:
		while True:
			while True:
				try:
					id_level = int(input("What's your ID's level currently?\n>"))
				except ValueError:
					print('Please input an integer.')
					pass
				else:
					break
			while True:
				try:
					wanted_id_level = int(input("What level do you want your ID to get to?\n>"))
				except ValueError:
					print('Please input an integer.')
					pass
				else:
					break
			if 1 <= id_level <= 55:
				if 1 <= wanted_id_level <= 55:
					break
				elif wanted_id_level < 1:
					print('Please input an actual Number for your Wanted ID level from 1-55.')
				elif wanted_id_level > 55:
					print('Please input an actual Number for your Wanted ID level from 1-55.')
				else:
					pass
			elif id_level < 1:
				print('Please input an actual Number for your ID level from 1-55.')
			elif id_level > 55:
				print('Please input an actual Number for your ID level from 1-55.')
			else:
				pass
		exp_needed = total_exp[wanted_id_level-1] - total_exp[id_level] # EXP needed in Total to reach wanted_id_level 
		user_input = int(input('Which EXP Lux tickets would you like to use?\n1. EXP Luxcavation I\n2. EXP Luxcavation II\n3. EXP Luxcavation III\n4. EXP Luxcavation IV\n>'))
		exp_required_calculator()

	elif user_input == 4:
		exp_ticket1_amount = 0 # just to make sure.
		exp_ticket2_amount = 0
		exp_ticket3_amount = 0
		exp_ticket4_amount = 0
		mixing_exp_tickets()

	elif user_input == 5:
		sharding()

	elif user_input == 6:
		thread_shard_exp_total()

	elif user_input == 7:
		print('Seeya! Love to All!')
		exit()
	else:
		print('No additional choices yet!!!')
		pass
	# 	exp_needed = total_exp[wanted_id_level - 1] - total_exp[id_level] # EXP needed in Total to reach wanted_id_level 
	#	user_input = int(input('Which EXP Lux tickets would you like to use?\n1. EXP Luxcavation I\n2. EXP Luxcavation II\n3. EXP Luxcavation III\n4. EXP Luxcavation IV\n5. Multiple\n>'))

print('WELCOME TO THE LIMBUS CALCULATOR!!!\nPlease Choose a menu option from below!')
while True:
	menu_screen()

