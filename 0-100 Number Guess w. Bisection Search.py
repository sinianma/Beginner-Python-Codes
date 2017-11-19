low = 0
high = 100
guess = (low+high)/2
print ("Please think of a number betwen 0 and 100!")
print ("Is your secret number " + str(int(guess)) + "?")
response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while response == "h" or response == "l" or response == "c":
    while response == 'l':
        low = int(((high+low)/2))
        guess = int((low + high)/2)
        print ("Is your secret number " + str(guess) + "?")
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
            
    while response == 'h':
        high = int((high+low)/2)
        guess = int((low + high)/2)
        print ("Is your secret number " + str(guess) + "?")
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
           
    if response == 'c':
        print ("Game over. Your secret number was: " + str(guess))
        break

while response != "h" and response != "l" and response != "c":
    print ("Sorry, I did not understand your input.")
    print ("Is your secret number " + str(int(guess)) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while response == "h" or response == "l" or response == "c":
        while response == 'l':
            low = int((high+low)/2)
            guess = int((low + high)/2)
            print ("Is your secret number " + str(guess) + "?")
            response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
            
        while response == 'h':
            high = ((high+low)/2)
            guess = (low + high)/2
            print ("Is your secret number " + str(guess) + "?")
            response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
           
        if response == 'c':
            print ("Game over. Your secret number was: " + str(guess))
            break

        
