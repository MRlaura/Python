decision='Y'
# to get inside the while loop the first time
while decision=='Y':
	try:
		decision= input ('Do you want to add a grade? Write Y or N\n').upper()
		if  decision=='Y':
			print ('You choose to add a grade')
			name = input ('Write the student\'s name\n').upper()
			grade= int (input ('Write the student\'s grade, between 1 and 20\n'))
		
			if grade>0 and grade<=20:
				if grade<=20 and grade>=19:
					print ('The student grade is A')
				elif grade<=18 and grade>=16:
					print ('The student grade is B')
			
				elif grade<=15 and grade>=13:
					print ('The student grade is C')
				
				elif grade<=12 and grade>=10:
					print ('The student grade is D')
				
				else: #grade<=9 and grade>=1
					print ('The student grade is E')
			else:
				print ('Invalid option. Write a grade between 1 and 20')
			
			
		else: # continuation of the if of line 5
			if decision!='N':
				print ('Invalid option. Please write Y or N')
				decision='Y' # allow the user to continue adding grades
			else:
				print ('You choose to exit. Thanks for using our services')
	except: # in case the user write a letter instead of numeric grade
		print ('Invalid option. Please write a number')