# Limbus Calculator for Uptying & Leveling
import math
# For math.ceil so things round up since you can't use a decimal of a Ticket

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


file = open('LimbusCalculatorResults.txt', 'w')

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
		else:
			pass

	elif ego_tier == 'ALEPH':
		print("There's no ALEPH EGO yet :c")
	else:
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
			else:
				pass
	else:
		pass


# Show how much Thread + Shards + EXP tickets are needed in Total
def thread_shard_exp_total():
	global total_thread
	global total_shards
	global exp_ticket1_total
	global exp_ticket2_total
	global exp_ticket3_total
	global exp_ticket4_total

	print('\nFor Thread & Egoshards you Require: ')
	print(f'{total_shards} Egoshards & {total_thread} Thread!')
	print('\nFor Experience Tickets, you Need: ')
	print(f'{exp_ticket1_total} EXP Luxcavation I tickets!')
	print(f'{exp_ticket2_total} EXP Luxcavation II tickets!!')
	print(f'{exp_ticket3_total} EXP Luxcavation III tickets!!!')
	print(f'{exp_ticket4_total} EXP Luxcavation IV tickets!!!!')

	yes_no = input('\nWould you like to Clear the Totals? (Please type Yes or No for this)\n>').upper() # only reason its not lower is bc i wanna make it match the ZAYIN-ALEPH stuff lel
	if yes_no == 'NO':
		print('\nVery Well! Have a lovely day with this info, and may the Prescripts bless ya!')
	elif yes_no == 'YES':
		print('\nVery Well!..Good luck with whatever you use this for next!!!')
		total_shards = 0
		total_thread = 0
		exp_ticket1_total = 0
		exp_ticket2_total = 0
		exp_ticket3_total = 0
		exp_ticket4_total = 0
	else:
		pass

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
	global excess_exp
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

	elif user_input == 5:
		user_input = int(input("Please input which Tickets you'll use in a 1234 Format. P l e a s e .\nFor Example: 12, 23, 34, 234, 1234, like that.\n>"))
		if user_input == 12: # Trying to figure this out is rough
			exp_ticket2_amount = exp_needed / exp_ticket2 # Think this works
			exp_ticket2_total += math.ceil(exp_ticket2_amount)
			excess_exp = ((exp_needed // exp_ticket2) * exp_ticket2)/10 # Keeps it as a Decimal. Praying.
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket1_total += math.ceil(exp_ticket1_amount)
			print(f'You need {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets!')
			print(f'As well as {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets!')

		elif user_input == 123:
			exp_ticket3_amount = exp_needed / exp_ticket3
			exp_ticket3_total += math.ceil(exp_ticket3_amount)
			excess_exp = ((exp_needed // exp_ticket3) * exp_ticket3)/10
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket2_total += math.ceil(exp_ticket2_amount)
			excess_exp = ((excess_exp // exp_ticket2) * exp_ticket2)/10
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket1_total += math.ceil(exp_ticket1_amount)
			print(f'You need {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!')
			print(f'You need {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets!')
			print(f'You need {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets!')
		
		elif user_input == 1234:
			exp_ticket4_amount = exp_needed / exp_ticket4
			exp_ticket4_total += math.ceil(exp_ticket4_amount)
			excess_exp = ((exp_needed // exp_ticket4) * exp_ticket4)/10
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket3_total += math.ceil(exp_ticket3_amount)
			excess_exp = ((excess_exp // exp_ticket3) * exp_ticket3)/10
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket2_total += math.ceil(exp_ticket2_amount)
			excess_exp = ((excess_exp // exp_ticket2) * exp_ticket2)/10
			exp_ticket1_amount = excess_exp / exp_ticket1
			exp_ticket1_total += math.ceil(exp_ticket1_amount)
			print(f'You need {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!')
			print(f'You need {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!')
			print(f'You need {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets!')
			print(f'You need {math.ceil(exp_ticket1_amount)} EXP Luxcavation I Tickets!')
		
		elif user_input == 23:
			exp_ticket3_amount = exp_needed / exp_ticket3
			exp_ticket3_total += math.ceil(exp_ticket3_amount)
			excess_exp = ((exp_needed // exp_ticket3) * exp_ticket3)/10
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket2_total += math.ceil(exp_ticket2_amount)
			print(f'You need {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!')
			print(f'You need {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets!')
		
		elif user_input == 234:
			exp_ticket4_amount = excess_exp / exp_ticket4
			exp_ticket4_total += math.ceil(exp_ticket4_amount)
			excess_exp = ((exp_needed // exp_ticket4) * exp_ticket4)/10
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket3_total += math.ceil(exp_ticket3_amount)
			excess_exp = ((excess_exp // exp_ticket3) * exp_ticket3)/10
			exp_ticket2_amount = excess_exp / exp_ticket2
			exp_ticket2_total += math.ceil(exp_ticket2_amount)
			print(f'You need {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!')
			print(f'You need {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!')
			print(f'You need {math.ceil(exp_ticket2_amount)} EXP Luxcavation II Tickets!')

		elif user_input == 34:
			exp_ticket4_amount = exp_needed / exp_ticket4
			exp_ticket4_total += math.ceil(exp_ticket4_amount)
			excess_exp = ((exp_needed // exp_ticket4) * exp_ticket4)/10
			exp_ticket3_amount = excess_exp / exp_ticket3
			exp_ticket3_total += math.ceil(exp_ticket3_amount)
			print(f'You need {math.ceil(exp_ticket4_amount)} EXP Luxcavation IV Tickets!')
			print(f'You need {math.ceil(exp_ticket3_amount)} EXP Luxcavation III Tickets!')

		else:
			print("Ya either did it wrong or...IDK, just..somethin'.")
			pass
	else:
		pass

def menu_screen():
	global user_input # final global variable for now nvm i lied
	global ego_tier
	global tier
	global id_level
	global wanted_id_level
	global total_exp
	global exp_needed
	global id_rarity

	print('-+-+-+-+-+-+-\n1. Thread & Uptie for EGOs\n2. Thread & Uptie for IDs\n3. Levels for IDs\n4. Total Shard, Thread & Total EXP Ticket Amount!\n5. Exit the Calculator\n-+-+-+-+-+-+-')
	user_input = int(input('\n>'))
	if user_input == 1:
		ego_tier = input('Please choose what EGO Rank ya want from ZAYIN, TETH, HE, WAW or ALEPH!!!\n>').upper()
		tier = int(input('Please choose what EGO Tier ya desire to Reach from 2, 3 or 4!'))
		ego_uptie_calculator()
	elif user_input == 2:
		id_rarity = input(f"\nPlease choose your ID's Rarity from 0, 00 OR 000!!!\n>")
		tier = int(input(f"\nNow please choose your Desired Tier you wanna get from 2, 3 or 4!!!\n>"))
		id_uptie_calculator()
	elif user_input == 3:
		id_level = int(input("What's your ID's level currently?\n>"))
		wanted_id_level = int(input("What level do you want your ID to get to?\n>"))
		exp_needed = total_exp[wanted_id_level - 1] - total_exp[id_level] # EXP needed in Total to reach wanted_id_level 
		user_input = int(input('Which EXP Lux tickets would you like to use?\n1. EXP Luxcavation I\n2. EXP Luxcavation II\n3. EXP Luxcavation III\n4. EXP Luxcavation IV\n5. Multiple\n>'))
		exp_required_calculator()
	elif user_input == 4:
		thread_shard_exp_total()
	elif user_input == 5:
		print('Bai Bai! Love Ya! <3')
		exit()
	else:
		print('No additional choices yet!!!')
		pass
# 	exp_needed = total_exp[wanted_id_level - 1] - total_exp[id_level] # EXP needed in Total to reach wanted_id_level 
#	user_input = int(input('Which EXP Lux tickets would you like to use?\n1. EXP Luxcavation I\n2. EXP Luxcavation II\n3. EXP Luxcavation III\n4. EXP Luxcavation IV\n5. Multiple\n>'))

print('WELCOME TO THE LIMBUS CALCULATOR!!!\nPlease Choose a menu option from below!')
while True:
	menu_screen()
