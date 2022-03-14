print("Question1: A number multiplied by 3 and subtracted by 3 is the same as the number subtracted by 4 and then multiplied by 6. Find the answer!")
answer1 = 7
guessa1 = int(input("Answer: "))
guessed1 = False
guessed2 = False
score1=False
score2=False
complete_game=False
if guessa1 == 7:
    guessed1 = True
    score1=True
    print("The answer is correct")
else:    
  while guessed1 == False:
    guessa2 = int(input("Retry! Answer: "))
    if guessa2 == answer1:
        score1=False
        guessed1 = True
        print("The answer is correct")
        
inputValue = input("Do you want to continue?[Type 'Yes' or 'No']")

if inputValue == "No":
    print("Okay, hope you liked the game! Bye")
elif inputValue == "Yes"or"yes":
    print("Question2: A number multiplied by 2 and added by 6 is the same as the number subtracted by 3 and then multiplied by 8. Find the answer!")
    answer2 = 5
    guessb1 = int(input("Answer: "))
    
    if guessb1 == answer2:
     guessed2 = True
     score2=True
     complete_game=True
     print("The answer is correct")
    else:
        while guessed2 == False:
         guessb2 = int(input("Retry! Answer: "))
         if guessb2 == answer2:
            guessed2 = True
            score2=False
            complete_game=True
            print("The answer is correct")
            print("Thank you, hope you liked the game! Bye")
if complete_game==True:
 if score1==True and score2==True:
    print("Your score is 10/10(Perfect hits)! Congrats")
 elif score1==False and score2==True:
    print("Your score is 6/10(Perfect hits)! Great")
 elif score1==True and score2==False:
    print("Your score is 4/10(Perfect hits)! Good try")
 elif score1==False and score2==False:
    print("Your score is 0/10(Perfect hits)! Good luck next time")
 print("Thank you for playing, hope you liked the game! Bye")
