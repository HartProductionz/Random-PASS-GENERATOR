		Prerequisite 
-Using Pycharm IDE
Lines # 1-6 deals with the summary of what the code will do

#Dont follow the (line on this, they are the line numbers on the .py file)


			Step 1 - Import (Lines 8-10)
		Import the required Modules 

Import Random
	- Allows us to generate random numbers
Import string
	- Gives us ASCII Letters, digits, and punctuation charcters 


			Step 2 - Define 
		Define the password Generator function 

def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

	
- This function takes the "length" (line #13) to specify length of the generated password

- The function first defines "characters" (line #14) variable which contains all the characters that we want to include 
	in the password : 		
	Uppercase & lowercase letters : (string.ascii_letters) 
	digits (string.digitis) 
	punctuation (string.puncuation) 

Then we use "random.choice" (line 15) to randomly select characters from the "characters" string to make the desired password

After that we will use the "join" method to link the recorded characters into one string

Lastly, our generated password is returned from the function (line 16)



		Step 3 : Test the generator 

if __name__ == "__main__":
    password_length = 12


generate_password = generate_strong_password(password_length)
    print("Generated Password:", generate_password)

	- If name = main refers to the script needing to be ran by the 	main .py file that the code was made on. 

	- we called the "generate_strong_password(line #24) with a specified 
	"password_length" 
	
	To get the results "generate_password" (line #25) while printing the statement "Generated Password:" (line25)
