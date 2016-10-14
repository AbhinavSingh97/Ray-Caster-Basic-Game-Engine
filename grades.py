def grade_calculator():
	check = True
	count = 0
	while check == True:
		print "Please enter correct integer values for grades \n"
		a = raw_input("How many A's have you received? ")
		b = raw_input("How many A-'s have you received? ")
		c = raw_input("How many B+'s have you received? ")
		d = raw_input("How many B's have you received? ")
		classes = raw_input("How many classes have you taken? ")
		try:
			A = int(a) * 4.0
			B = int(b) * 3.7
			C = int(c) * 3.3 
			D = int(d) * 3.0
			current_pts = A + B + C + D
			gpa = current_pts/int(classes)
			print "Your gpa is " + str(gpa) + "\n"
			check = False
		except:
			print "Seems like you didn't enter integers when asked, let's try it again"
			print "Failure to enter the correct response will terminate the program"
			print "You have" +str(3 - count) + " tries"
			count += 1
			if count == 3:
				return None
	
	answer = raw_input("Would you like to find out the grades you need to find a minimum gpa? (Y/N) ")
	if answer == "Y":
		min_gpa = raw_input("What is the minimum gpa you are trying to achieve? ")
		min_classes = raw_input("How many more classes will you be taking? ")
		total_classes = int(min_classes) + int(classes)
		points = float(min_gpa) * total_classes
		if (points - current_pts) > (4.0 * total_classes):
			print "Sorry you won't be able to achieve your desired GPA. "
		else: 
			print "The minimum number of points you need " + str(points - final)
	else:
		print "Understood, thank you for using the gpa calculator."
grade_calculator()

