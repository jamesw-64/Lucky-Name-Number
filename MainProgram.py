##--------------------------------------
##             Import List
##--------------------------------------
import sys

##--------------------------------------
##            Variable List
##--------------------------------------

#The variables for finding if i has a score
_1point_  = "AJS"
_2points_ = "BKT"
_3points_ = "CLU"
_4points_ = "DMV"
_5points_ = "ENW"
_6points_ = "FOX"
_7points_ = "GPY"
_8points_ = "HQZ"
_9points_ = "IR"

#Trigger for debug mode
DEBUG = 0

#Iitalise user input variable
user_input = ""

#Initlase score variable
score = 0

#Iteration Variable
i = 0

#Final score, to store the score in a different variable so it is not lost
final_score = 0

#***NB: Some variables are optimised later in the program, which cannot be optimised here***

##--------------------------------------
##              Functions
##--------------------------------------

#ADDING IN VARIABLES FOR SCORES AND MEANINGS
def findscore(score):
        
        #create final score variable to assist with splitting and adding
        final_score = 0

        #interation check
        iteration = 0
        
        #begin loop
        for i in score:
                
                if(DEBUG == 1):
                        print("i == " + str(i))
                        print("final_score == " + str(final_score) + " + " + str(i))
                        print("iteration == " + str(iteration))
                        
                #adding i to final score
                final_score = final_score + int(i)

                #add to iteration
                iteration = iteration + 1
                
                if(DEBUG == 1):
                        print("final_score == " + str(final_score))

                #check for break condtion
                if(final_score <= 9 and iteration < 1):
                        if(DEBUG == 1):
                                print("Breaking loop")
                        break
        return(final_score)



##--------------------------------------
##             Main Program
##--------------------------------------

#Print one time greating
print("Welcome! With this program you will be able to find the meaning of your name.")

#Main loop
while True:
        #clean variables in case this is a second iteration

        #Initialize user input variable
        user_input = ""

        #Initialize score variable
        score = 0

        #Iteration Variable
        i = 0

        #Final score, to store the score in a different variable so it is not lost
        final_score = 0
        
        #menu loop
        while True:

                init_input = 4 #This cannot be 0, it will make the program exit

                #try, in case of valueerror
                try: #ensures program does not fall over in event that an incorrect charcter is entered at ibput here, for example a letter or symbol
                        init_input = int(input("""
MAIN MENU

-----------------------------------
1: Begin Program
2: Toggle debug mode
0: Quit
------------------------------------

What would you like to do: """))
                except ValueError:
                        print("That was not acceptable input.\n")

                
                #Break out of menu loop (INPUT 1)
                if(init_input == 1):
                        break

                #Ask for DEBUG (INPUT 2)
                elif(init_input == 2):
                        DEBUG = str(input("\nRun in debug mode? [Y/N] "))
                        DEBUG = DEBUG.upper()

                #If statemet for the debug mode
                        if (DEBUG == "Y"):
                                DEBUG = 1
                                print ("You have opted for DEBUG mode")
                        elif (DEBUG == "N"):
                                DEBUG = 0
                                print ("You have opted out of DEBUG mode.")
                        else:
                                DEBUG = 0
                                print ("Invalid input, progressing with DEBUG mode OFF.")

                #Exit (INPUT 0)
                if(init_input == 0):
                        sys.exit("goodbye")

        #Getting the input
        if(DEBUG == 1):
                print("Now asking user for input...")
                
        user_input = str(input("What is the name you want to use? Any character that is not a letter will be ignored: "))

        #Standardizing the input as it makes it easier to use
        if(DEBUG == 1):
                print("Variable 'user_input' is now " + user_input + ". Now making variable uppercase...")

        user_input = user_input.upper()
        
        if(DEBUG == 1):
                print("Variable 'user_input' is now " + user_input + ". Now creating 'score' variable and finding your score...")

        #Points loop
        for i in user_input:
                if(DEBUG == 1):
                        print("Checking if character " + str(i) + " is worth points")
                        
                #figure out if point is to be awarded
                find_1point = str(_1point_.find(i))
                find_2points = str(_2points_.find(i))
                find_3points = str(_3points_.find(i))
                find_4points = str(_4points_.find(i))
                find_5points = str(_5points_.find(i))
                find_6points = str(_6points_.find(i))  
                find_7points = str(_7points_.find(i))  
                find_8points = str(_8points_.find(i))
                find_9points = str(_9points_.find(i))
                
                #for one point
                if(find_1point != "-1"):
                        score = score + 1
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 1 point and your score is now " + str(score))
                                
                #for two points         
                if(find_2points != "-1"):
                        score = score + 2
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 2 points and your score is now " + str(score))
                                
                #for three points       
                if(find_3points != "-1"):
                        score = score + 3
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 3 points and your score is now " + str(score))
                                
                #for four points...
                if(find_4points != "-1"):
                        score = score + 4
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 4 points and your score is now " + str(score))

                #and so on
                if(find_5points != "-1"):
                        score = score + 5
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 5 points and your score is now " + str(score))

                if(find_6points != "-1"):
                        score = score + 6
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 6 points and your score is now " + str(score))
                                
                if(find_7points != "-1"):
                        score = score + 7
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 7 points and your score is now " + str(score))
                                
                if(find_8points != "-1"):
                        score = score + 8
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 8 points and your score is now " + str(score))
                                
                if(find_9points != "-1"):
                        score = score + 9
                        if(DEBUG == 1):
                                print(str(i)+ " is worth 9 points and your score is now " + str(score))


        #turn score into a string
        score = str(score)
        
        #call findscore function and store the returned int
        if(DEBUG == 1):
                print("Calling function for first time")
        final_score = findscore(score)

        while(final_score >= 10):
                if(DEBUG == 1):
                        print("Calling function again")
                final_score = findscore(str(final_score))

        #Print the result
        print("\nYour number is " + str(final_score) + "\n")
        if(final_score == 1):
                print("Your name means that you're SELFLESS AND GENEROUS")
        elif(final_score == 2):
                print("Your name means that you're a NATURAL PEACEMAKER")
        elif(final_score == 3):
                print("Your name means that you're CREATIVE AND OPTIMISTIC")
        elif(final_score == 4):
                print("Your name means that you're a HARD WORKER")
        elif(final_score == 5):
                print("Your name means that you VALUE FREEDOM")
        elif(final_score == 6):
                print("Your name means that you're a CARER AND PROVIDER")
        elif(final_score == 7):
                print("Your name means that you're a THINKER")
        elif(final_score == 8):
                print("Your name means that you have DIPLOMATIC SKILLS")
        elif(final_score == 9):
                print("Your name means that you're SELFLESS AND GENEROUS")
        else:
                print("Internal error. Calculations were incorrect. The program had a problem dealing with the input (" + user_input + ")")

        #Ask to try again
        retry = str(input("\nWant to go again? [Y/N] "))

        #standardize input for ease of use
        retry = retry.upper()
        
        if(retry == "N"):
                sys.exit("goodbye") #exit
        elif(retry == "Y"):
                print("Resetting") #repeat program
        else:
                print("Unknown input: Restarting...") #repeat program
