# # In this version, the program generates a random number with number of digits equal to length. 
# # If the command line argument length is not provided, the default value is 1. Then, the program prompts the user to type in a guess, 
# informing the user of the number of digits expected. The program will then read the user input, and provide basic feedback to the user. 
# If the guess is correct, the program will print a congratulatory message with the number of guesses made and terminate the game. 
# Otherwise,
# # the program will print a message asking the user to guess a higher or lower number, and prompt the user to type in the next guess.

import random,sys

def mims_mind():
	try:
		if len(sys.argv)>1:
			num_of_digits=int(sys.argv[1])
		else:
			print("No command line argument entered,setting it to default number of digits")
			num_of_digits=1
	except:
		print("Invalid command line argument entered,setting it to default number of digits")
		num_of_digits=1

	start_range=10**(num_of_digits-1)
	end_range=(10**num_of_digits)-1
	num=random.randint(start_range,end_range)
	guess_count=0
	while True:
		user_num=int(input("Enter your guess"))
		guess_count+=1
		if user_num<num:
			print("Enter a higher number")
			print("The correct number is a {} digit number".format(num_of_digits))
		elif user_num>num:
			print("Enter a lower number")
			print("The correct number is a {} digit number".format(num_of_digits))
		else:
			print("Congratulations, your guess is right!")
			print("No. of guesses:"+str(guess_count))
			break
def main():
	mims_mind()


if __name__=="__main__":
	main()
	    	
	    	
	    	
	    
	    
	    	
	    	
	    	
    	
    	
    	