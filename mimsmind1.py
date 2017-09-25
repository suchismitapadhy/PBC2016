# Once again, the program generates a random number with number of digits equal to length. If the command line argument length is not provided,
# he default value is 3. This means that, by default, the random number is in the range of 000 and 999. 

# In this version, the program will establish a maximum number of rounds, maxrounds, equal to (2^length) + length.
#  For example, if length = 3, then maxrounds = 11.

# Then, the program prompts the user to type in a guess, informing the user of the number of digits expected. 
# The program will then read the user input, and provide 'bulls and cows' feedback to the user.
#  A matching digit in the correct position will result in a 'bull', while a matching digit in the wrong position will result 
#  in a 'cow'. For example, if the correct answer is '123', and the guess is '324', then the feedback will be one bull (for the digit '2') 
#  and one cow (for the digit '3'). More examples are provided below.

# At each round, if the user guess is incorrect and maxrounds is not yet reached, the program should increment the 
# counter for round and issue a new prompt for user input. Otherwise, the program should print a congratulatory or an apologetic 
# message with the number of guesses made, and terminate the game.

import random,sys

def bull(num1,num2):
	bull=0
	while num1>0 and num2>0:
		digit1=num1%10
		digit2=num2%10
		if digit1== digit2:
			bull+=1
		num1=num1//10
		num2=num2//10
	return bull

def cow(num1,num2):
	cow=0
	n1=list(str(num1))
	n2=list(str(num2))
	while len(n1)>0 and len(n2)>0:
		if n1[-1] in n2:
			cow+=1
			n2.remove(n1[-1])
			n1=n1[:-1]
		else:
			n1=n1[:-1]

	return cow-bull(num1,num2)

def mims_mind():
	try:
		if len(sys.argv)>1:
			num_of_digits=int(sys.argv[1])
		else:
			# print("No command line argument entered,setting it to default number of digits")
			num_of_digits=3
	except:
		print("Invalid command line argument entered,setting it to default number of digits")
		num_of_digits=3


	start_range=10**(num_of_digits-1)
	end_range=(10**num_of_digits)-1
	num=random.randint(start_range,end_range)
	guess_count=0
	maxrounds=(2**num_of_digits)+1
	print("Lets play the mims_mind game. you have {} guesses".format(maxrounds))
	print("Guess a {} digit number: ".format(num_of_digits), end=" ")
	while guess_count<=maxrounds:
		try:
			user_num=int(input())
			guess_count+=1
			b=bull(user_num,num)
			c=cow(user_num,num)
			if user_num!=num:
				print("{} bull(s),{} cow(s). Try Again: ".format(b,c), end=" ")
					
			else:
				print("Congratulations! You guessed the number in {} tries".format(guess_count))
				return
		except:
			print("Invalid Input. Try Again: ", end= " ")
			guess_count+=1
	print("sorry, you did not guess the number in {} tries. The correct number is {}".format(maxrounds,num))
		
def main():
	mims_mind()
	

if __name__=="__main__":
	main()
