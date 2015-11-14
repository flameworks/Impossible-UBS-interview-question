def interview(num):
	answers = []
	starting_num = 0
	while len(answers) < num:
	# while True:
		string = str(starting_num)
		string_length = len(string)
		if string_length%2 != 0:
			starting_num*= 10
		else:
			num1 = string[:string_length/2]
			num2 = string[string_length/2:]
			middle_sum = int(num1) + int(num2)
			if len(str(middle_sum))%2 == 0:
				middle_starting_pos = (string_length-len(str(middle_sum)))/2
				if middle_sum == int(string[middle_starting_pos:(string_length-middle_starting_pos)]):
					answers.append(string)
					print string
		starting_num += 1
	return answers