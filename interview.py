def interview(num):
	answers = []
	starting_num = 0
	while len(answers) < num:
	# while True:
		starting_num_str = str(starting_num)
		starting_num_length = len(starting_num_str)
		if starting_num_length%2 != 0:
			starting_num*= 10 #skips all numbers that have odd number of digits
		else:
			num1 = starting_num_str[:starting_num_length/2]
			num2 = starting_num_str[starting_num_length/2:]
			middle_sum = int(num1) + int(num2)
			middle_num_str = str(middle_sum)
			middle_num_length = len(middle_num_str)
			if middle_num_length%2 == 0: #only finding sums that have even number of digits
				middle_starting_pos = (starting_num_length - middle_num_length)/2
				if middle_sum == int(starting_num_str[middle_starting_pos:(starting_num_length-middle_starting_pos)]): #right in the middle
					answers.append(starting_num_str) #optional consolidation into array
					print starting_num_str
		starting_num += 1
	return answers